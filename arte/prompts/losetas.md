# Prompts: losetas del mapa (v2)

Decisión de Santiago: todas las losetas tienen **la misma calle**, siempre en el mismo lugar, y **siempre los 9 puntos rojos** de la grilla de 3 × 3 (la grilla no se dibuja). Las losetas de casas tienen un espacio de calle y otro para las casas.

## Sistema

- Loseta cuadrada, grilla invisible de 3 × 3 zonas. Exportación para TTS: 1500 × 1500 px.
- **Calle (igual en todas):** columna del medio, vertical, de borde superior a borde inferior. Asfalto con línea amarilla y vereda a cada lado, dentro de esa columna. Toca los bordes de arriba y de abajo en el tercio del medio. Así cualquier loseta se conecta con cualquier otra (girándolas 90° se arman calles horizontales).
- **Columnas laterales:** izquierda y derecha. Ahí va lo que cambia: baldíos, casas o edificios especiales. No tocan la calle de otras losetas: se tocan entre sí (un fondo con otro fondo).
- **9 puntos rojos:** centro de cada zona, a 1/6, 1/2 y 5/6 del ancho y del alto. Calle: 3 puntos. Cada columna lateral: 3 puntos, uno por habitación o espacio.
- **Casas y edificios:** ocupan una columna lateral entera (3 habitaciones, una por zona, cada una con su punto) y tienen la puerta hacia la vereda.
- Si ChatGPT pone mal los puntos: pedir la loseta sin puntos y ponerlos con `herramientas/puntos_loseta.py ... --todos`.

## Mensaje 1 (reglas + primera loseta)

Ver el texto en la respuesta del chat; es el mismo que figura abajo.

```
I'm making a set of square map tiles for a post-apocalyptic zombie board game for Tabletop Simulator. I'll ask for many tiles, one by one, in this chat. ALL of them must follow these fixed rules exactly, so every tile connects with every other one. Use the attached image only as a style reference.

FIXED RULES FOR EVERY TILE:
1. FORMAT: perfectly square 1:1, pure top-down 90° view, no perspective, no isometric angle, light from the top-left. Buildings are shown with the roof removed so the rooms are visible.
2. STYLE: hand-drawn ink linework with cross-hatching, muted desaturated colors, illustrated tabletop battle map. Cracked grey asphalt with a faded yellow dashed center line, beige stone sidewalks with square slabs, overgrown dark-green grass and weeds, rusted cars, rubble, broken fences. Thin worn parchment border (#D8C8A6). Gloomy and abandoned but clean and readable.
3. INVISIBLE 3x3 GRID: the tile is divided into 3 equal columns and 3 equal rows (9 square zones). Do NOT draw the grid lines.
4. THE STREET (identical on every tile): the MIDDLE COLUMN is always the same vertical street: a straight asphalt road with a sidewalk on each side, running from the top edge to the bottom edge. It touches the top and bottom edges exactly in the middle third. Same width, same position, same look on every tile. No other road anywhere.
5. LEFT and RIGHT COLUMNS: this is what changes from tile to tile (lots, houses or buildings). Buildings fill their column and their front doors open onto the sidewalk of the street. The outer left and right edges end in yard, fence or wall, never in road.
6. RED DOTS (always exactly 9): one solid dark-red circle with a soft glow in the CENTER of each of the 9 zones: at 1/6, 1/2 and 5/6 of the width, combined with 1/6, 1/2 and 5/6 of the height. Three dots on the street, three in the left column, three in the right column. All the same size (about 1/12 of the tile width). No other dots or markers.
7. NEVER draw: grid lines, numbers, letters, text, signs with words, people, zombies, characters, blood pools, logos, watermarks, 3D render, photorealism.

Confirm you understood, then make the first tile:

THIS TILE: LEFT COLUMN: an empty lot with tall weeds and a burned-out car. RIGHT COLUMN: a small parking lot with two abandoned cars and a dumpster. A faded crosswalk across the street in the middle row.
```

## Mensajes siguientes (uno por loseta)

Todos empiezan con `Next tile, same fixed rules.`

Baldíos y calle:
- B1 · `THIS TILE: LEFT COLUMN: a collapsed bus stop with a toppled bench and broken glass. RIGHT COLUMN: a fenced yard overgrown with bushes and a fallen tree. A pothole full of rainwater on the street.`
- B2 · `THIS TILE: LEFT COLUMN: a burned kiosk and a pile of sandbags. RIGHT COLUMN: an overturned delivery van with scattered boxes on a grassy lot.`

Casas (una casa por columna; 3 habitaciones, una por zona, puerta a la vereda):
- H1 · `THIS TILE: LEFT COLUMN: an empty weedy lot with a rusted car. RIGHT COLUMN: a one-story house with three rooms stacked from top to bottom, one per zone: bedroom, living room, kitchen. Front door from the living room onto the sidewalk; doorways between rooms.`
- H2 · `THIS TILE: LEFT COLUMN: a house with three rooms from top to bottom: garage with a car and tools, living room, bathroom. Front door from the living room onto the sidewalk. RIGHT COLUMN: a house with three rooms: kitchen, dining room, bedroom. Front door from the dining room onto the sidewalk.`
- H3 · `THIS TILE: LEFT COLUMN: a ransacked house with three rooms from top to bottom: bedroom with a mattress against the door, living room with overturned furniture, pantry. Barricaded windows. Front door from the living room onto the sidewalk. RIGHT COLUMN: a backyard with a dog house, a clothesline and a broken fence.`
- H4 · `THIS TILE: LEFT COLUMN: a small grocery corner store with three rooms from top to bottom: store room, shop with empty shelves and a counter, back office. Shop door onto the sidewalk. RIGHT COLUMN: a house with three rooms: kids' bedroom, living room, kitchen; front door from the living room.`

Especiales (el edificio ocupa una columna entera y la otra columna es su anexo, así es más grande que una casa):
- E1 Farmacia · `THIS TILE: RIGHT COLUMN: a pharmacy with three rooms from top to bottom: storage room with boxes, sales floor with knocked-over medicine shelves and a glass shop window, pharmacist counter with a locked cabinet. Entrance from the sales floor onto the sidewalk, green cross on the entrance mat (no letters). LEFT COLUMN: the pharmacy's parking lot with an abandoned ambulance and a delivery van.`
- E2 Comisaría · `THIS TILE: RIGHT COLUMN: a police station with three rooms from top to bottom: holding cells with bars, office with desks and an armory with an empty gun rack and a steel door, entrance hall with a reception behind bulletproof glass and sandbags. Entrance onto the sidewalk. LEFT COLUMN: the station's fenced yard with two crashed police cars and a barricade of concrete blocks.`
- E3 Supermercado · `THIS TILE: BOTH SIDE COLUMNS are one big supermarket split by the street: RIGHT COLUMN: the sales floor with long shelf aisles, checkouts and shopping carts, sliding entrance onto the sidewalk. LEFT COLUMN: the supermarket's warehouse with pallets, a cold room and a loading dock facing the sidewalk.`
- E4 Hospital · `THIS TILE: RIGHT COLUMN: a hospital wing with three rooms from top to bottom: patient ward with beds, operating room, emergency reception with double doors onto the sidewalk. LEFT COLUMN: the ambulance bay with two ambulances, triage tents and stretchers, and a generator.`

Cruces opcionales (misma calle, mismo ancho, para unir calles paralelas):
- X1 · `THIS TILE: exception to rule 4: the street ALSO runs horizontally through the middle row with the exact same width and look, making a four-way crossroads in the center zone, touching all four edges in their middle third. The four corner zones are sidewalk corners: a crashed car against a traffic light, a burned kiosk, sandbags, an overgrown planter. Keep the 9 red dots.`
- X2 · `THIS TILE: exception to rule 4: T-junction. The vertical street as always, plus a branch with the exact same width going from the center zone to the RIGHT edge (middle third). LEFT COLUMN: an empty lot with rubble. Top-right and bottom-right zones: sidewalk corners with a broken streetlight. Keep the 9 red dots.`

## Correcciones
- Calle corrida: `Same tile, but the street must be exactly the middle third of the tile, straight from top edge to bottom edge, same as the first tile.`
- Puntos mal: `Same tile, but exactly 9 red dots, one in the center of each zone of the invisible 3x3 grid.`
- Estilo distinto: `Keep exactly the same style as the first tile of this chat.`
