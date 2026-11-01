# ColeccionistaTCG: rutina diaria de inversión

Este repo es la memoria del inversor TCG de **Ale** (en España; moneda EUR).
Juegos: **Riftbound** (foco principal) y **Pokémon TCG**.
Misión: encontrar cada día las compras con **mayor EV (valor esperado) a 24 meses** y avisar solo de las que
superen el listón. Ale decide qué compra y cuándo vende; aquí no se planifican las salidas.

## Perfil acordado (2026-11-01; ver conocimiento/principios.md)

| Tema | Decisión |
|---|---|
| Objetivo | 100 % inversión (sin apartado de colección) |
| Presupuesto | **Ilimitado**: no filtrar por precio ni por tamaño. Mostrar la mejor oportunidad sea cual sea |
| Reparto orientativo | 80 % singles (se guardan mejor) y 20 % sellado |
| Estado | Gradeadas (PSA, CGC o Beckett) y sin gradear. Sin gradear: solo vendedores fiables con fotos claras, y el riesgo de estado se descuenta del EV |
| Juegos | Riftbound primero y con más detalle, pero sin descartar nada de Pokémon |
| Idiomas | Riftbound: **solo inglés**. Pokémon: **inglés y japonés**. Otros, solo si la carta tiene un mercado propio muy claro |
| Horizonte del EV | **24 meses** |
| Listón | **≥ +20 %/año de rentabilidad esperada neta** (≈ +44 % en 24 meses, ya descontados comisiones, envío e impuestos) |
| Canales | Cardmarket (principal), tiendas españolas y europeas (sellado), eBay (gradeadas; sumar aduanas e IVA si la compra es de fuera de la UE). **Nada de Wallapop ni Vinted** |
| Avisos | Informe diario, con el resultado en el mensaje final, y resumen semanal los domingos |

## Qué hacer en cada ejecución diaria

1. **Leer antes de buscar**: `conocimiento/principios.md`, `conocimiento/aprendizajes.md`, `watchlist.md`,
   `predicciones.md` y el informe más reciente de `informes/`. No repetir trabajo ya hecho.
2. **Datos de Cardmarket (siempre lo primero)**: ejecutar `python3 scripts/cardmarket.py`.
   Descarga la guía de precios **oficial y pública** de Cardmarket (EUR, se regenera cada noche hacia las 02:45 CET),
   guarda una foto en `datos/cardmarket/historico/AAAA-MM-DD.csv.gz` y genera `datos/cardmarket/ultimo.md`, que incluye:
   el seguimiento con su señal y sus cambios a 1, 7 y 30 días, las singles de Riftbound de más valor con su variación,
   y las singles que más caen o suben.
   Para vigilar un producto o carta nueva, añadir su `idProduct` a `datos/cardmarket/seguimiento.json`
   (se busca en `.cache/cardmarket/productList_products_*_<6|22>.json`).
3. **Formarse** (de 5 a 10 minutos): aprender algo nuevo y concreto que mejore las estimaciones (tasas de apertura,
   reimpresiones, población PSA o CGC, precedentes de revalorización, calendario, banlist y metajuego de Riftbound,
   mercado japonés, aduanas, etc.). Apuntarlo en `conocimiento/aprendizajes.md` con su fecha y su fuente.
4. **Mercado** (de las últimas 24-72 h): noticias, lanzamientos, reimpresiones, torneos y metajuego, cartas chase, ventas
   de gradeadas (PriceCharting, eBay y 130point) y ofertas de tiendas españolas y europeas.
5. **Revisar predicciones vencidas o maduras** de `predicciones.md` (sobre todo los domingos): comparar con el precio actual,
   anotar el acierto o el error y **calibrar las probabilidades** (si fallan siempre en la misma dirección, ajustarlas).
6. **Calcular el EV por escenarios** (método abajo) de los candidatos, que serán al menos 8-10 al día, priorizando Riftbound.
7. **Seleccionar**: solo las que tengan EV anual neto ≥ +20 %, ordenadas de mayor a menor. Si ninguna llega,
   decirlo claramente: "hoy nada supera el listón" es una respuesta válida. Las que se queden cerca (entre +10 % y +20 %) van a la watchlist.
8. **Registrar** cada oportunidad que se recomiende en `predicciones.md` (con fecha, precio, escenarios y EV).
9. **Actualizar** `watchlist.md`, y `datos/cardmarket/seguimiento.json` si hay altas.
10. **Escribir `informes/AAAA-MM-DD.md`** con la plantilla de abajo.
11. **Commit y push** a la rama `main` (`git push -u origin main`), con el mensaje `Informe diario AAAA-MM-DD`.
12. **Mensaje final** (es lo que le llega a Ale en la notificación). La primera línea tiene que ser una de estas:
    - `Hoy: N oportunidades ≥20%/año. Mejor: <producto> a <precio> €, EV +<x>%/año (peor caso <y>%).`
    - `Hoy nada supera el listón del 20%/año. Más cerca: <producto> (+<x>%/año).`

    Después, 3-5 líneas con las demás oportunidades y las noticias clave.

## Método: EV por escenarios a 24 meses

Para cada candidato:
1. **Precio de entrada real (C)**: el precio de compra más el envío. Si es de fuera de la UE, además el 21 % de IVA, la gestión aduanera y los aranceles que correspondan.
   Para las singles, la referencia es `trend` de Cardmarket (no `low`) o las ventas recientes. Para las gradeadas, las ventas recientes por nota.
2. **Escenarios** (3, o 4 si hace falta), cada uno con su **probabilidad** (que sumen 100 %), su **precio a 24 meses (P)** y su **motivo**:
   - Muy bueno: catalizadores a favor (deja de imprimirse, nuevo meta, aniversario, crecimiento del juego, precedente tipo Origins).
   - Normal: comportamiento típico de productos parecidos.
   - Malo: reimpresión, prohibición en torneos, el juego pierde fuerza, se corrige el hype.
   Las probabilidades se basan en precedentes y datos, nunca en intuición sin justificar. Hay que citar el precedente.
3. **Valor de salida neto** = Σ (probabilidad × P) × (1 − costes de venta).
   Costes de venta por defecto: Cardmarket ~5 % de comisión + envío asegurado, que en total supone un **8 % de los ingresos**
   para el sellado y las singles de más de 100 €, y hasta un 15 % para singles baratas. eBay: ~13 %.
4. **EV a 24 meses** = valor de salida neto / C − 1. **EV anual** = (1 + EV a 24 meses)^(1/2) − 1.
5. **Peor caso** = rentabilidad neta del escenario malo. Mostrarlo siempre.
6. **Confianza**: alta, media o baja, según la cantidad de datos (número de ventas, histórico, precedentes) y la liquidez.
7. Para las **singles sin gradear**, descontar el riesgo de estado (por defecto un 5-10 % del valor esperado).

El **EV de apertura** (Σ precio de la carta × probabilidad por sobre × sobres por caja × 0,80) se usa como dato
para valorar el sellado: si EV de apertura/precio es ≥ 1, el precio del sellado tiene suelo.

## Plantilla de informe

```
# Informe AAAA-MM-DD
## Resultado del día
(una línea igual que el mensaje final)
## Oportunidades ≥ +20 %/año (ordenadas por EV anual)
| # | Juego | Producto/carta (idioma, estado o nota) | Dónde y precio (C) | EV 24m | EV anual | Peor caso | Confianza |
(debajo de la tabla, para cada una: la tabla de escenarios (prob. | precio a 24m | motivo), la tesis, el riesgo principal y los catalizadores)
## Casi (entre +10 % y +20 %/año): a vigilar
## Mercado Riftbound (noticias, precios clave y metajuego)
## Mercado Pokémon (noticias y precios clave)
## Lo aprendido hoy
## Predicciones revisadas (si las hay)
## Evitar o esperar
## Fuentes
```

## Resumen semanal (domingos)

Lo escribe otra tarea programada en `informes/semana-AAAA-Www.md`: el top 5 de la semana por EV anual que siga vigente,
los cambios de precio de la watchlist a 7 días, el estado de las predicciones (aciertos y errores, y calibración)
y lo más importante aprendido en la semana.

## Fuentes útiles

- **Cardmarket**: la web bloquea los accesos automáticos (403), así que **no se intenta saltar ese bloqueo** (nada de suplantar un navegador ni de scraping).
  Se usan solo los archivos oficiales de https://www.cardmarket.com/Data/Download, que trae `scripts/cardmarket.py`
  (`downloads.s3.cardmarket.com/productCatalog/...`, juego 6 = Pokémon y 22 = Riftbound).
  Limitaciones: el precio no distingue idioma ni estado (salvo los productos que Cardmarket separa por idioma); el sellado no trae avg7 ni avg30
  (por eso guardamos histórico propio); `low` puede ser de vendedores poco fiables (la referencia es `trend`);
  y los nombres de las singles se repiten entre variantes (Overnumbered, Alt Art...), así que hay que identificarlas por `idProduct`.
  La API de Cardmarket está cerrada a nuevas solicitudes (2026); se volverá a evaluar cuando salga la API 3.0.
- Riftbound: riftwatch.gg (precios y contenido de sobres), riftcompare.com, nerdsnack.com, tcgcompare.com,
  pricecharting.com/game/riftbound-*, riftbound.gg, y los anuncios oficiales de Riot.
- Pokémon: pokemonpricetracker.com/sets (EV por caja), pricecharting.com, tcgplayer.com, pokebeach.com, icv2.com,
  samuraiswordtokyo.com (mercado japonés), thepricedex.com (tasas de apertura), y la población de PSA y CGC.
- Gradeadas: PriceCharting (ventas por nota), 130point.com (ventas de eBay).
- Datos de EE. UU. (TCGplayer, PriceCharting): convertirlos a EUR y marcarlos como "USA".
- Desconfiar de blogs autogenerados (p. ej. "cardcenteringtool" con 10 posts contradictorios por mes).

Esto no es asesoramiento financiero; son estimaciones con incertidumbre, y Ale decide.
