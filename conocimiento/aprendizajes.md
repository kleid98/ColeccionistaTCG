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

## 2026-11-10
- **Europa revaloriza menos el sellado de Riftbound que EE. UU.**: en Cardmarket (09-nov) Origins está +43 % sobre el PVP europeo (13 meses), Spiritforged +6 % (8 meses), Unleashed +2 % y Vendetta -12 %. Calibra a la baja el escenario "muy bueno". Fuente: guía de precios de Cardmarket.
- **Calendario Riot 2027**: Legacy 29-ene, Proving Grounds 2ª ed. 19-feb (40 $, solo cartas ya disponibles en sobres), The Reckoning 30-abr, sets 8 (T3) y 9 (T4). Un set cada ~3 meses presiona el sellado reciente. Fuente: playriftbound.com, "Products and Sets into 2027".
- **Pokémon Japón**: aviso oficial del 06-nov: sobres de 200 yen pasan a 230 yen desde mayo de 2027. Fuente: samuraiswordtokyo.com.
- **Cardmarket**: el `low` puede ser mucho menor que `trend` (Radiance 91 vs 105 €) y los trends de singles caras son ruidosos (Akali Overnumbered: trend 2.299, avg7 460). Para singles de más de 500 € no se fía del trend sin avg7 coherente.

## 2026-11-17
- **Riot reimprime a propósito sus sets tempranos**: seguirá imprimiendo Origins "hasta que el mercado tenga cantidades sanas", y esas reimpresiones "no serán las últimas". Aun así, Origins va +43 % sobre el PVP europeo. Para el sellado reciente, el escenario malo (reimpresión) sube del 30 % al 35 %. Fuente: playriftbound.com, "Flash Promos & Origins Reprint Updates", y el anuncio de enero de 2026 (cardsrealm).
- **Bans frecuentes y en bloque**: 3 cartas en septiembre, y 8 cartas más 2 campos de batalla el 23-nov (Riven, Broken Blade, con un 43 % del metajuego en el RC de Stuttgart), alguno preventivo (Baited Hook). Desde el 23-nov la banlist va por circuito. Las singles jugables necesitan un 30-40 % de escenario malo. Fuente: playriftbound.com, "Radiance Ban List Updates (Effective November 23, 2026)".
- **El sellado de Riftbound está ya más barato en EE. UU. que en Europa** (Radiance 97,51 $ y Vendetta 120 $ frente a 99 € y 124 € en Cardmarket), al revés que el 01-nov. Señal de que en Europa aún puede bajar más. Fuente: tcgindex.io (USA, fuente secundaria).

## 2026-11-18
- **Legacy cambia la estructura del sobre**: un hueco de común pasa a ser un hueco fijo de Leyenda o Campo de batalla (más o menos mitad y mitad), así que el sobre trae 6 comunes en vez de 7. Set de 239 cartas, 93 Showcase. Las Showcase de Leyendas y Campos siguen en el hueco Overnumbered. Las tasas de Origins no sirven tal cual para Legacy; habrá que esperar a aperturas tras el 29-ene. Fuente: nerdsnack.com (artículo del 09-nov-2026).
- **Las ETB y los Booster Bundle de los sets principales de Pokémon se revalorizan mucho en Europa en su primer año**: en Cardmarket (17-nov) la ETB de Mega Evolution (sep-2025) está a 94-101 € y la de Phantasmal Flames (nov-2025) a 92 €, frente a un PVP europeo de unos 55-60 € (PVP sin confirmar): +60-75 % en 12-14 meses. Los bundles, igual (Mega Evolution 56,72 €, Phantasmal Flames 56,57 €). En cambio, las displays recién salidas valen ya cerca de su precio a 1-2 años. Precedente útil para el escenario "normal" de Delta Reign. Fuente: guía de precios de Cardmarket.
- **La guía de Cardmarket no siempre se regenera cada noche**: el 18-nov a las 07:37 UTC seguía la del 17-nov (createdAt 02:51 CET). Hay que mirar `createdAt` antes de dar los cambios a 1 día por buenos.
