# Prompts: losetas del mapa

Para generar con ChatGPT (imagen). Todas las losetas comparten los mismos parámetros, así encajan entre sí como en Carcassonne o Zombicide.

## Sistema

- **Loseta simple:** cuadrada, 3 × 3 zonas. Se exporta a 1500 × 1500 px (500 px por zona).
- **Loseta grande (hospital, supermercado):** 2 × 2 losetas = 6 × 6 zonas, cuadrada, 3000 × 3000 px.
- **Bordes.** Cada borde de loseta es de uno de dos tipos:
  - **C (calle):** la calzada llega al borde **en el tercio del medio**, con una vereda a cada lado. Calzada = el tercio central; las veredas ocupan el borde interno de los tercios laterales.
  - **V (vereda / terreno):** no llega calle. Termina en vereda, pasto, cerca o fondo de terreno.
  - Una loseta solo se pone al lado de otra si los bordes que se tocan son iguales (C con C, V con V).
- **Familias:**
  - **Calles:** la calzada ocupa el tercio central. Los tercios laterales son terrenos (baldíos, autos, escombros). No hay edificios a los que se entre.
  - **Manzanas:** sin calle. Un edificio (casa, farmacia, comisaría) con su patio. Todos sus bordes son V. La puerta mira hacia un borde, que se pone junto a una loseta de calle.
  - **Grandes:** hospital y supermercado, 2 × 2 losetas, todos los bordes V.
- **Puntos rojos:** NO se piden a ChatGPT. Se ponen después con `herramientas/puntos_loseta.py`, siempre en el centro de las zonas, así quedan iguales en todas.
  - Calle: los 9 centros (3 en la calzada, 6 en los terrenos).
  - Casa: 1 por habitación y 1 por patio. Las paredes de las habitaciones siguen las líneas de la cuadrícula, para que cada habitación tenga una zona con su punto en el centro.

## Bloque fijo (pegarlo en TODOS los prompts, sin cambiarlo)

```
Top-down orthographic map tile for a post-apocalyptic zombie survival board game, to be used in Tabletop Simulator. Perfectly square image, 1:1. Pure 90° overhead view, no perspective, no isometric angle, no shadows that change direction between tiles: light comes from the top-left.

STYLE (identical on every tile of the set): hand-drawn ink linework with cross-hatching, painted in muted, desaturated colors, like an illustrated tabletop battle map; aged parchment frame color #D8C8A6 only in a thin worn border; cracked grey asphalt with faded yellow center lines; beige stone sidewalks with square slabs; overgrown dark-green grass and weeds; rusted cars, rubble, broken fences, trash. Gloomy, abandoned, after the apocalypse, but clean and readable: the floor of every area must stay visible for placing miniatures.

GRID (critical): the tile is divided into an invisible 3 × 3 grid of equal square zones. Walls of buildings and the edges of the road must follow these grid lines exactly. Do NOT draw the grid lines, do NOT draw any dots, circles, markers, numbers, letters, text, labels, compass, logo or watermark.

EDGES (critical, so tiles connect like Carcassonne): where a road reaches a tile edge, the asphalt occupies exactly the middle third of that edge, with a sidewalk on each side, and it runs straight and perpendicular into the edge. Edges without road end in sidewalk, grass, fence or yard, never in asphalt. Nothing important touches the outer border.

AVOID: people, zombies, characters, blood pools, text, signs with letters, dots, grid lines, frames thicker than a few pixels, 3D render, photorealism, tilted camera.
```

## Bloque variable (uno por loseta, va debajo del bloque fijo)

### Calles (todas con terrenos en los tercios laterales)

**C1 · Recta** (bordes: arriba C, abajo C, izquierda V, derecha V)
```
THIS TILE: a straight road running from the top edge to the bottom edge through the middle column of the grid. Left column: an empty lot with tall weeds and a burned-out car. Right column: a small parking lot with two abandoned cars and a dumpster. A faded crosswalk across the road in the middle row.
```

**C2 · Recta, variante** (arriba C, abajo C)
```
THIS TILE: a straight road from the top edge to the bottom edge through the middle column. Left column: a collapsed bus stop with a toppled bench and broken glass. Right column: a fenced yard overgrown with bushes and a fallen tree branch across the sidewalk. A pothole full of rainwater in the top row.
```

**C3 · Esquina** (abajo C, derecha C; arriba V, izquierda V)
```
THIS TILE: an L-shaped road: it enters from the bottom edge (middle third) and turns 90° to exit through the right edge (middle third). The turn is in the center zone. Top-left area: a vacant lot with rubble and a rusted car. Top-right and bottom-left corners: sidewalk corners with a broken streetlight and overgrown planters.
```

**C4 · T** (izquierda C, derecha C, abajo C; arriba V)
```
THIS TILE: a T-junction: a road crosses the tile horizontally from the left edge to the right edge through the middle row, and a third branch leaves from the center down to the bottom edge. Top row: a long sidewalk with an overturned delivery van and scattered boxes. Bottom-left and bottom-right corners: small grassy lots with a broken fence.
```

**C5 · Cruce** (los cuatro bordes C)
```
THIS TILE: a four-way crossroads: roads reach all four edges through their middle third and meet in the center zone, with faded crosswalks on each side of the intersection. The four corners are sidewalk corners: a crashed car against a traffic light, a burned kiosk, a pile of sandbags, an overgrown planter.
```

**C6 · Calle cortada** (abajo C; resto V)
```
THIS TILE: a dead-end road that enters from the bottom edge (middle third) and ends in the center zone against a barricade of concrete blocks, sandbags and a crashed police car. Top row: an empty lot with weeds behind the barricade. Left and right columns: sidewalks and small yards.
```

### Manzanas (casa: 2 × 3 zonas de casa + 1 columna de patio; puerta al borde que diga)

**M1 · Casa con living y cocina** (puerta hacia abajo)
```
THIS TILE: a city block with no road. A one-story house fills the left two columns of the grid (6 zones), seen from above with the roof removed. Its rooms follow the grid: a living room (top two zones of the house), a kitchen (middle-left zone), a bathroom (middle-right zone), a bedroom (bottom two zones). Interior walls along the grid lines, with doorways between rooms. The front door is in the middle of the bottom wall, opening to a short path that reaches the bottom edge. The right column is a back yard with grass, a clothesline and a shed. Furniture is drawn but leaves floor space in the center of every room.
```

**M2 · Casa en L** (puerta hacia la izquierda)
```
THIS TILE: a city block with no road. An L-shaped one-story house, roof removed: it fills the whole top row and the whole left column (5 zones). Rooms follow the grid: top-left zone is the entrance hall, the rest of the top row is a living room and a dining room, the left column below holds a kitchen and a bedroom. The front door opens to the left edge from the entrance hall. The other 4 zones are a walled courtyard with a dry fountain, weeds and garden chairs. Interior walls on grid lines with doorways.
```

**M3 · Casa de dos ambientes con garaje** (puerta hacia la derecha)
```
THIS TILE: a city block with no road. A house, roof removed, in the right two columns (6 zones): top row a garage with a car and tools, middle row a living room, bottom row two bedrooms (one per zone). The front door opens to the right edge from the living room; the garage door also opens to the right. The left column is a side yard with a dog house, a vegetable patch gone wild and a broken fence. Walls on grid lines, doorways between rooms.
```

**M4 · Casa saqueada** (puerta hacia arriba)
```
THIS TILE: a city block with no road. A ransacked house, roof removed, filling the bottom two rows (6 zones): living room, kitchen and pantry in the middle row; two bedrooms and a bathroom in the bottom row, each in its own zone. Barricaded windows, overturned furniture, a mattress against a door. The front door opens upward to the top row, which is a front garden with a gate in the middle of the top edge.
```

**M5 · Dúplex** (puerta hacia abajo)
```
THIS TILE: a city block with no road. Two small attached houses, roof removed, sharing a middle wall: each house takes one column of the grid, the left and middle columns, with three rooms each (one per zone: living, kitchen, bedroom). Each house has its own front door at the bottom edge. The right column is a shared parking strip with a rusty pickup truck.
```

### Edificios especiales de una loseta (ocupan las 9 zonas: más grandes que una casa)

**E1 · Farmacia** (puerta hacia abajo)
```
THIS TILE: a city block with no road, completely filled by a pharmacy, roof removed, 9 zones. Bottom row: the store front with a glass shop window along the bottom edge and the entrance door in the middle, shelves of medicine boxes knocked over, a counter. Middle row: the back of the shop with the pharmacist's counter and a locked medicine cabinet. Top row: a storage room with boxes and a back door that opens to the top edge, plus a small office and a toilet, each in its own zone. Green cross painted on the floor mat at the entrance (no letters).
```

**E2 · Comisaría** (puerta hacia abajo)
```
THIS TILE: a city block with no road, completely filled by a small police station, roof removed, 9 zones. Bottom row: entrance hall with a reception desk behind bullet-proof glass, front door in the middle of the bottom edge, sandbags. Middle row: an office with desks and filing cabinets, a locker room, an armory with an empty gun rack and a heavy steel door. Top row: two holding cells with bars and an interview room. Overturned chairs, scattered papers, spent shell casings. No letters on signs.
```

### Edificios grandes (2 × 2 losetas: cuadrada, 6 × 6 zonas)

Cambiar en el bloque fijo "3 × 3 grid" por "6 × 6 grid" y "middle third" por "never: this tile has no road".

**G1 · Supermercado** (puerta hacia abajo)
```
THIS TILE: a large square map tile representing a whole supermarket, roof removed, on an invisible 6 × 6 grid. Bottom two rows: the sales floor entrance with checkout counters, abandoned shopping carts and an automatic sliding door in the middle of the bottom edge; outside it a thin strip of parking with two cars. Middle rows: long aisles of shelves running vertically, many knocked over, with clear walking space between them. Top two rows: the stock room with pallets and boxes, a cold room, a manager's office and a loading dock with a roll-up door on the top edge. Walls follow the grid lines.
```

**G2 · Hospital** (puerta hacia abajo)
```
THIS TILE: a large square map tile representing a small hospital, roof removed, on an invisible 6 × 6 grid. Bottom two rows: the emergency entrance with an ambulance bay outside, double doors in the middle of the bottom edge, a waiting room with rows of chairs and a reception desk. Middle rows: a long corridor running left to right with rooms on both sides: patient rooms with beds, an operating room, an X-ray room. Top two rows: a pharmacy store room, a staff room, a morgue with steel drawers and a generator room with a back door on the top edge. Gurneys and wheelchairs in the corridor, curtains, scattered medical supplies. Walls follow the grid lines.
```

## Después de generar cada loseta

1. Revisá los bordes: la calzada tiene que tocar el borde en el tercio del medio, recta.
2. Agregá los puntos:
   ```
   python3 herramientas/puntos_loseta.py c1.png tts/losetas/calle_recta_v01.jpg --todos
   python3 herramientas/puntos_loseta.py m1.png tts/losetas/casa_m1_v01.jpg --zonas A1,A2,B2,A3,C1,C2,C3
   python3 herramientas/puntos_loseta.py hospital.png tts/losetas/hospital_v01.jpg --losetas 2x2 --zonas C6,B5,E5,A3,C3,E3,B1,D1,F1
   ```
3. En Tabletop Simulator: Custom Tile, cuadrado. Loseta simple 6 × 6 unidades de mesa (zona de 2 × 2); grande 12 × 12.
