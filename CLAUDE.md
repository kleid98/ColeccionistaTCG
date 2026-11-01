# ColeccionistaTCG: rutina diaria

Este repo es la memoria del coleccionista de **Pokémon TCG** y **Riftbound** (League of Legends TCG).
Objetivo: coleccionar y mantener a **medio y largo plazo** (de 1 a 5 años o más), comprar solo cuando el precio sea bueno
y priorizar productos y cartas con **EV (valor esperado) alto** en relación con su precio.

Usuario: Ale, en España. Moneda de referencia: **EUR**. Mercado de referencia: **Cardmarket**.
Para datos de EE. UU. se usan TCGplayer y PriceCharting, siempre convertidos y marcados como "USA".

## Qué hacer en cada ejecución diaria

1. **Leer antes de buscar**: `conocimiento/principios.md`, `conocimiento/aprendizajes.md`, `watchlist.md`
   y el informe más reciente de `informes/`. No repetir trabajo ya hecho.
2. **Formarse** (5-10 min): aprender una cosa nueva y concreta sobre coleccionismo o inversión TCG
   (tasas de apertura, reimpresiones, gradeo PSA/CGC, ciclos de precio, calendario, rotación,
   mercado japonés, tiendas en España, etc.). Apuntarla en `conocimiento/aprendizajes.md`
   con fecha y fuente. Si cambia una regla, actualizar `principios.md`.
3. **Datos de Cardmarket (siempre lo primero)**: ejecutar `python3 scripts/cardmarket.py`.
   Descarga la guía de precios **oficial y pública** de Cardmarket (EUR, se regenera cada noche hacia las 02:45 CET),
   guarda una foto en `datos/cardmarket/historico/AAAA-MM-DD.csv.gz` y genera `datos/cardmarket/ultimo.md`,
   que incluye la tabla de seguimiento con su señal (🟢 en objetivo), los cambios a 1, 7 y 30 días y las singles que más caen o suben.
   Es la **fuente principal de precios en EUR**. Para vigilar un producto nuevo, añadir su `idProduct`
   (está en `.cache/cardmarket/productList_products_nonsingles_<6|22>.json`) a `datos/cardmarket/seguimiento.json`.
   Si el informe pide un objetivo de precio distinto, actualizar también `objetivo_eur`.
4. **Mercado**: buscar noticias y precios de las últimas 24-72 h:
   - Pokémon: displays/ETB/bundles en circulación y fuera de impresión, lanzamientos (inglés y japonés),
     anuncios de reimpresiones, cartas chase y su tendencia.
   - Riftbound: precios de displays por set, singles (Overnumbered, Signature, Ultimate, Alt Art),
     calendario (próximo: Legacy, 29-ene-2027), formatos y banlist, que mueven la demanda de singles.
5. **Calcular o estimar el EV** de los productos candidatos (ver la fórmula abajo). Indicar siempre
   si el EV es publicado (y por quién) o una estimación propia.
6. **Elegir oportunidades**: de 3 a 6 como máximo, cada una con precio actual, precio objetivo de compra,
   EV/precio, tesis, riesgo y horizonte. Si hoy no hay nada bueno, decirlo: "hoy no comprar" es una respuesta válida.
7. **Actualizar `watchlist.md`**: precios actuales, alertas que han saltado (precio ≤ objetivo), altas y bajas.
8. **Escribir `informes/AAAA-MM-DD.md`** con la plantilla de abajo.
9. **Commit y push** a la rama `main` (`git push -u origin main`), con el mensaje `Informe diario AAAA-MM-DD`.

## EV: cómo se calcula aquí

- **EV de apertura** = Σ (precio de mercado de la carta × probabilidad por sobre) × sobres por caja.
  - EV neto ≈ EV bruto × 0,80 (comisiones de Cardmarket, envíos y venta a precio inferior al de mercado).
  - Ratio **EV/precio**: ≥ 1,0 → abrir puede compensar; entre 0,6 y 1,0 → mejor mantener cerrado; < 0,6 → precio sostenido por especulación del sellado.
- **EV de mantener (sellado)**: probabilidad de revalorización a 2-3 años según precedentes del set y del juego,
  la distancia al PVP, el riesgo de reimpresión y lo que se espera que siga imprimiéndose.
- Para las singles: precio actual frente a su mínimo de 30/90 días, demanda competitiva o coleccionista y población gradeada.

## Reglas de compra (resumen; el detalle está en principios.md)

- Sellado moderno: comprarlo cerca del PVP o por debajo, nunca persiguiendo el hype de la semana del lanzamiento.
- Los productos que siguen en impresión bajan tras el lanzamiento: esperar entre 4 y 10 semanas.
- Pokémon moderno: casi nunca compensa abrir cajas para ganar dinero (EV/precio < 1). Para la carta que se quiere, comprar la single.
- Alertar siempre de los riesgos de reimpresión y de las fuentes poco fiables.

## Plantilla de informe

```
# Informe AAAA-MM-DD
## Resumen en 3 líneas
## Lo aprendido hoy
## Mercado Pokémon (noticias + precios clave)
## Mercado Riftbound (noticias + precios clave)
## Oportunidades de compra (tabla: producto | precio | objetivo | EV/precio | tesis | riesgo | horizonte)
## Evitar / esperar
## Cambios en la watchlist
## Fuentes
```

## Fuentes útiles

- Pokémon: pokemonpricetracker.com/sets (EV por caja), pricecharting.com, tcgplayer.com, pokebeach.com,
  icv2.com, samuraiswordtokyo.com (mercado japonés), cardtrack.com, thepricedex.com (tasas de apertura).
- Riftbound: riftwatch.gg (precios y contenido de sobres), riftcompare.com, nerdsnack.com, tcgcompare.com,
  pricecharting.com/game/riftbound-*, riftbound.gg.
- **Cardmarket**: la web bloquea los accesos automáticos (403), así que **no se intenta saltar ese bloqueo** (nada de suplantar un navegador ni de scraping).
  Se usan solo los archivos oficiales de https://www.cardmarket.com/Data/Download, que trae `scripts/cardmarket.py`
  (`downloads.s3.cardmarket.com/productCatalog/...`, juego 6 = Pokémon y 22 = Riftbound).
  Limitaciones: el precio no distingue idioma ni estado; el sellado de Pokémon no trae avg7 ni avg30 (por eso guardamos histórico propio);
  y `low` puede ser de vendedores poco fiables, así que la referencia es `trend`.
  La API de Cardmarket está cerrada a nuevas solicitudes (2026); se volverá a evaluar cuando salga la API 3.0.
- Desconfiar de blogs autogenerados (p. ej. "cardcenteringtool" con 10 posts contradictorios por mes).

Esto no es asesoramiento financiero; es el diario de un coleccionista.
