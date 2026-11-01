# Aprendizajes diarios

## 2026-11-01
- **Estructura de los sobres de Riftbound**: 14 cartas, 24 sobres por display y PVP de 119,99 $ / 127,99 €. En Origins: épicas en 1 de cada 4 sobres, unas 2 Alt Art por display, 1 Overnumbered cada 3 displays y, de cada 10 Overnumbered, 1 es Signature. La Ultimate de Radiance sale en un 0,025 % de los sobres (1 de cada 4.000). Fuente: riftwatch.gg.
- **El EV de las cajas modernas de Pokémon queda muy por debajo de su precio** (ratio de 0,53-0,59): el precio del sellado lo sostiene la demanda de coleccionistas y especuladores, no lo que trae dentro. Fuente: pokemonpricetracker.com, 31-oct-2026.
- **En Riftbound, el valor de un set suele concentrarse en las Overnumbered y Signature**: las Signature van de 2.000 a 6.500 $, pero con muy pocas ventas, así que hay que tomarlas como rango. Fuente: nerdsnack.com, 25-oct-2026.
- **Cardmarket bloquea las descargas automáticas (403).** Hay que conseguir sus precios por vías indirectas.

## 2026-11-01 (b): acceso a Cardmarket
- Cardmarket publica cada día, de forma **oficial y pública**, su guía de precios y su catálogo (https://www.cardmarket.com/Data/Download): un JSON por juego, con Pokémon como juego 6 y Riftbound como juego 22. Cada producto trae avg, low, trend, avg1, avg7 y avg30 en EUR, y ya incluye el sellado (displays, ETB y cajas). Ahora lo automatiza `scripts/cardmarket.py`.
- La API de Cardmarket no acepta solicitudes nuevas (help.cardmarket.com). La web devuelve 403 a los bots, y no se debe intentar saltar ese bloqueo.
- **Primeros datos en EUR (31-oct)**: la display de Riftbound Radiance tiene un trend de 114,73 €, **por debajo del PVP europeo de 127,99 €**, y la caja de 6 displays sale a unos 123 € por display. Vendetta: 127,25 €. Origins: 176,89 €, frente a unos 226 $ en EE. UU. En general, **Cardmarket está un 10-25 % por debajo de TCGplayer** en Riftbound.
- En Pokémon, las ETB de Chaos Rising (61,81 €), Perfect Order (60,66 €) y Pitch Black (68,33 €) están cerca del PVP europeo. Las displays de Perfect Order y Chaos Rising siguen por encima (175-185 €).
