#!/usr/bin/env python3
"""Descarga la guía de precios oficial y pública de Cardmarket (Pokémon y Riftbound),
guarda una foto diaria en datos/cardmarket/historico/ y genera datos/cardmarket/ultimo.md.

Fuente: https://www.cardmarket.com/Data/Download (archivos públicos que se regeneran cada noche, ~02:45 CET).
Uso: python3 scripts/cardmarket.py
"""
import csv, datetime as dt, gzip, json, os, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache", "cardmarket")
HIST = os.path.join(ROOT, "datos", "cardmarket", "historico")
OUT_MD = os.path.join(ROOT, "datos", "cardmarket", "ultimo.md")
SEG = os.path.join(ROOT, "datos", "cardmarket", "seguimiento.json")
BASE = "https://downloads.s3.cardmarket.com/productCatalog"
JUEGOS = {"pokemon": 6, "riftbound": 22}
CATS_SELLADO_POKEMON = {"Pokémon Display", "Pokémon Elite Trainer Boxes", "Pokémon Box Set"}


def bajar(ruta):
    os.makedirs(CACHE, exist_ok=True)
    destino = os.path.join(CACHE, ruta.replace("/", "_"))
    with urllib.request.urlopen(f"{BASE}/{ruta}", timeout=120) as r, open(destino, "wb") as f:
        f.write(r.read())
    with open(destino, encoding="utf-8") as f:
        return json.load(f)


def cargar(juego, gid):
    pg = bajar(f"priceGuide/price_guide_{gid}.json")
    precios = {p["idProduct"]: p for p in pg["priceGuides"]}
    prods = {}
    for tipo in ("singles", "nonsingles"):
        for p in bajar(f"productList/products_{tipo}_{gid}.json")["products"]:
            p["tipo"] = tipo
            prods[p["idProduct"]] = p
    return pg["createdAt"], precios, prods


def nombres_expansion(prods):
    """Deduce el nombre del set a partir del sellado ("Radiance Booster Box" -> idExpansion de Radiance)."""
    m = {}
    for p in sorted(prods.values(), key=lambda x: len(x["name"])):
        if p["tipo"] != "nonsingles":
            continue
        for suf in (" Booster Box", " Booster Display", " Elite Trainer Box", " Booster Bundle", " Booster"):
            if p["name"].endswith(suf) and "(" not in p["name"]:
                m.setdefault(p["idExpansion"], p["name"][: -len(suf)])
                break
    return m


def foto_previa(fecha, dias):
    """Devuelve {(juego,id): trend} del histórico más cercano a `dias` antes de `fecha` (±3 días)."""
    objetivo = fecha - dt.timedelta(days=dias)
    for delta in (0, -1, 1, -2, 2, -3, 3):
        f = os.path.join(HIST, f"{objetivo + dt.timedelta(days=delta)}.csv.gz")
        if os.path.exists(f) and objetivo + dt.timedelta(days=delta) < fecha:
            with gzip.open(f, "rt", encoding="utf-8") as fh:
                return {(r["juego"], int(r["idProduct"])): float(r["trend"]) for r in csv.DictReader(fh) if r["trend"]}
    return {}


def pct(nuevo, viejo):
    if not nuevo or not viejo:
        return ""
    return f"{(nuevo / viejo - 1) * 100:+.0f}%"


def main():
    datos, expansiones, fecha = {}, {}, None
    for juego, gid in JUEGOS.items():
        creado, precios, prods = cargar(juego, gid)
        datos[juego] = (precios, prods)
        expansiones[juego] = nombres_expansion(prods)
        fecha = dt.date.fromisoformat(creado[:10])

    # 1) Foto diaria (csv.gz): sellado relevante y singles con trend >= 5 € (Riftbound) o >= 50 € (Pokémon)
    os.makedirs(HIST, exist_ok=True)
    filas = []
    for juego, (precios, prods) in datos.items():
        for pid, p in prods.items():
            q = precios.get(pid)
            if not q or not q.get("trend"):
                continue
            if p["tipo"] == "nonsingles":
                if juego == "pokemon" and (p["categoryName"] not in CATS_SELLADO_POKEMON or q["trend"] < 15):
                    continue
            elif q["trend"] < (5 if juego == "riftbound" else 50):
                continue
            filas.append({"juego": juego, "idProduct": pid, "nombre": p["name"], "categoria": p["categoryName"],
                          "idExpansion": p["idExpansion"], "low": q.get("low") or "", "trend": q["trend"],
                          "avg7": q.get("avg7") or "", "avg30": q.get("avg30") or ""})
    with gzip.open(os.path.join(HIST, f"{fecha}.csv.gz"), "wt", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(sorted(filas, key=lambda r: (r["juego"], r["idProduct"])))

    hace = {d: foto_previa(fecha, d) for d in (1, 7, 30)}
    L = [f"# Cardmarket: guía de precios del {fecha}", "",
         "Fuente: guía de precios pública y oficial de Cardmarket (EUR). `trend` es el precio de referencia; "
         "`low` puede ser engañoso (otros idiomas, mal estado o vendedores con poca reputación).", "",
         "## Seguimiento", "",
         "| Producto | Low | Trend | Objetivo | Δ1d | Δ7d | Δ30d | Señal |", "|---|---|---|---|---|---|---|---|"]
    seg = json.load(open(SEG, encoding="utf-8"))["productos"]
    for s in seg:
        precios, _ = datos[s["juego"]]
        q = precios.get(s["idProduct"], {})
        t, lo, obj = q.get("trend"), q.get("low"), s["objetivo_eur"]
        k = (s["juego"], s["idProduct"])
        senal = "🟢 en objetivo" if t and t <= obj else ("🟡 a ≤10%" if t and t <= obj * 1.10 else "🔴")
        L.append(f"| {s['nombre']} ({s['juego']}) | {lo or '-'} | {t or '-'} | {obj} | "
                 f"{pct(t, hace[1].get(k))} | {pct(t, hace[7].get(k))} | {pct(t, hace[30].get(k))} | {senal} |")

    # 2a) Riftbound: las 40 singles de más valor, con su variación (sirven para buscar candidatos con EV)
    precios, prods = datos["riftbound"]
    top = sorted(((q["trend"], pid) for pid, q in precios.items()
                  if prods.get(pid, {}).get("tipo") == "singles" and q.get("trend")), reverse=True)[:40]
    L += ["", "## Riftbound: las 40 singles de más valor", "",
          "| Carta | Set | idProduct | Low | Trend | Avg7 | Avg30 | Δ7d | Δ30d |", "|---|---|---|---|---|---|---|---|---|"]
    for t, pid in top:
        q, p, k = precios[pid], prods[pid], ("riftbound", pid)
        L.append(f"| {p['name']} | {expansiones['riftbound'].get(p['idExpansion'], p['idExpansion'])} | {pid} | "
                 f"{q.get('low') or '-'} | {t} | {q.get('avg7') or '-'} | {q.get('avg30') or '-'} | "
                 f"{pct(t, hace[7].get(k))} | {pct(t, hace[30].get(k))} |")

    # 2) Singles: caídas y subidas sostenidas. Para filtrar cartas con pocas ventas y ventas atípicas se exige:
    #    trend, avg7, avg30 y low presentes y de 20 € o más, con trend y avg7 apuntando en la misma dirección.
    for juego, (precios, prods) in datos.items():
        cand = []
        for pid, q in precios.items():
            p = prods.get(pid)
            t, a7, a30, lo = q.get("trend"), q.get("avg7"), q.get("avg30"), q.get("low")
            if not p or p["tipo"] != "singles" or not all((t, a7, a30, lo)) or min(t, a30) < 20:
                continue
            r, r7 = t / a30, a7 / a30
            if not (0.4 <= r <= 2.5) or not (0.5 <= r7 <= 2.0) or lo < 0.3 * t:
                continue
            if (r < 0.85 and r7 < 0.95) or (r > 1.2 and r7 > 1.05):
                cand.append((r, p["name"].replace("|", "/"), expansiones[juego].get(p["idExpansion"], p["idExpansion"]), t, a30, lo))
        for titulo, lista in (("Caídas (posible oportunidad)", sorted(cand)[:12]),
                              ("Subidas (hype: no perseguir)", sorted(cand, reverse=True)[:12])):
            L += ["", f"## {juego.capitalize()}: singles. {titulo}", "",
                  "| Carta | Set | Trend | Avg30 | Trend/Avg30 | Low |", "|---|---|---|---|---|---|"]
            lista = [x for x in lista if (x[0] < 1) == titulo.startswith("Caídas")]
            L += [f"| {n} | {e} | {t} | {a} | {r:.2f} | {lo} |" for r, n, e, t, a, lo in lista] or ["| (sin señales hoy) | | | | | |"]

    # 3) Sellado: mayores cambios a 7 días (cuando haya histórico)
    if hace[7]:
        mov = []
        for r in filas:
            if r["categoria"].endswith("Single"):
                continue
            v = hace[7].get((r["juego"], r["idProduct"]))
            if v and r["trend"] >= 30:
                mov.append((r["trend"] / v - 1, r["juego"], r["nombre"], v, r["trend"]))
        mov.sort()
        L += ["", "## Sellado: mayores cambios a 7 días", "", "| Producto | Hace 7 días | Hoy | Δ |", "|---|---|---|---|"]
        L += [f"| {n} ({j}) | {v} | {t} | {c*100:+.0f}% |" for c, j, n, v, t in (mov[:8] + mov[-8:])]
    else:
        L += ["", "_Todavía no hay una semana de histórico: los cambios a 7 y 30 días aparecerán según se acumulen fotos diarias._"]

    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    sys.exit(main())
