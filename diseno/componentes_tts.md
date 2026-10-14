# Día 30 · Componentes para Tabletop Simulator

Plan de diseño de todos los componentes físicos para montar Día 30 en Tabletop Simulator (TTS).
Agente de diseño · 14 oct 2026 · borrador v0.2 (con las decisiones del autor en `diseno/ideas_de_santiago.md`: voseo, Alimento, 20 días con 3 niveles de peligro y mazo de aparición)

Fuentes: `fuentes/kit_prueba_1.md`, `fuentes/direccion_de_arte.html`, `fuentes/cartas_de_objetos.html`, `fuentes/base_y_losetas.html` y `fuentes/mesa_online.html`. Todo lo que no está en las fuentes aparece como **propuesta**. Las contradicciones entre documentos están en la sección 7.

**Resumen**
- El montaje se arma en dos cajas virtuales: el **Kit prueba 1** (expedición mínima, lo primero que hay que probar) y el **Juego completo** (base, ciudad, losetas, 20 días con 3 niveles de peligro).
- Las cartas se diseñan a 750 × 1050 px (como las de acción y objetos actuales) y se exportan a TTS en hojas de 4096 px de lado como máximo.
- Las fichas usan colores fuertes y no llevan texto. Las cartas, losetas y tableros siguen la dirección C, "papel en la oscuridad": la mesa de TTS es noche y todo lo que es del juego es papel.
- Para el mazo de botín, la hoja lleva solo las **33 caras únicas** y las 74 cartas se arman en TTS duplicando. Así las cartas se ven más nítidas.
- Todo texto impreso en componentes va en **voseo rioplatense** (ver 3.0).
- La aparición de zombies sale de un **mazo de aparición** propio (3.10). Ya no hay d6 de aparición ni de errantes.

---

## 1. Inventario de componentes

### 1.1 Tipos de objeto de TTS que se usan

| Tipo TTS | Para qué | Notas técnicas |
|---|---|---|
| **Custom Deck** | Todos los mazos | Hoja en cuadrícula de 10 × 7 como máximo. La última casilla es la carta oculta. Las cartas son rectángulos: TTS no recorta por transparencia |
| **Custom Tile** | Losetas, hojas de jugador, fichas de dos caras (zombies, puertas, fichas de edificio), tablas de referencia | Formas: caja, hexágono, círculo o caja redondeada. Imagen arriba y, si hace falta, otra abajo. Se da vuelta con F |
| **Custom Token** | Fichas de una cara con silueta (ruido, daño, heridas, balas) | Recorta la forma por el canal alfa del PNG: permite bordes de papel irregulares. Se apila |
| **Custom Board** | Tablero de base, mapa de la ciudad, tablero de tiempo | Una imagen grande, plana, que se deja bloqueada |
| **Custom Figurine** | Supervivientes (y, si se quiere, los zombies especiales) | Figura de cartón de pie, PNG con alfa |
| **Custom Dice** | Dado de zona de herida (opcional) | Usar la plantilla oficial de TTS para el d6 personalizado |
| **Nativos** | d4, d6, d8, d10, d12, d20, bolsas, bolsas infinitas, contadores, PDF, Notebook | Los dados nativos alcanzan. Las bolsas infinitas son ideales para las fichas genéricas |

### 1.2 Kit prueba 1 · expedición mínima

Corresponde a `kit_prueba_1.md`: 1 personaje, 12 turnos y un mapa de 6 × 3 zonas.

| Componente | Cant. | Tipo TTS | Tirada que usa | Comentario |
|---|---|---|---|---|
| Loseta P1-A (columnas A–C) | 1 | Custom Tile, caja | — | Calle, patio, casa (B2–C2), BASE en A3. Puerta B2/B3 |
| Loseta P1-B (columnas D–F) | 1 | Custom Tile, caja | — | Farmacia: salón E2 y depósito F2. Vidriera E1/E2, puerta D2/E2, puerta trasera con llave F2/F3. Estacionamiento F3 |
| Hoja del superviviente de prueba | 1 | Custom Tile, caja | — | Atributos 3/3/3/3 (+1), 3 PA, sangre 6, Defensa 11, mochila de 6 |
| Superviviente | 1 | Custom Figurine | — | Figura neutra ("Superviviente de prueba") |
| Cartas del kit | 7 | Custom Deck | Ver columna de daño | Cuchillo (d4 + F), Bate (d6 + F), Pistola (d10, 6 balas), Venda, Analgésico, Kit médico, Alimento. Comparten dorso con el botín |
| Caminantes | 10 | Custom Tile, círculo de 2 caras | d20 + 2 al atacar | Cara "tranquilo" y cara "alerta" (reemplaza la moneda cara/ceca) |
| Fichas de ruido | 20 (bolsa infinita) | Custom Token | — | Horda con 5 en una zona o edificio |
| Fichas de daño de zombie | Bolsa infinita | Custom Token | Daño del arma | Se ponen debajo del zombie. Cae con 5 |
| Puertas y ventanas | 4 (+2 de repuesto) | Custom Tile, caja de 2 caras | d6 (cae con un 6) | Puerta cerrada/abierta ×2, puerta con llave/forzada ×1, vidriera intacta/rota ×1 |
| Ficha de farmacia | 1 | Custom Tile, círculo de 2 caras | d6 al abrir | Al frente, la tabla de zombies y botín (d6). Al dorso, la casa (d6: con 1–2 hay un caminante) |
| Reloj de turnos 1–12 | 1 tira + 1 marcador | Custom Tile + Custom Token | — | Del turno 9 al 12, franja de noche. La aparición sale del mazo de aparición (nivel de peligro 1), no del d6 del kit |
| Fichas de herida ("olor a sangre") | Bolsa infinita | Custom Tile, círculo de 2 caras (abierta / limpia) | d6 de zona (o el dado de zona) | Hay un solo tipo de herida. Cada herida es una gota roja sobre su zona del cuerpo y queda abierta hasta limpiarla con agua |
| Ficha "escondido" | 1 | Custom Token | — | Se quita al empezar el turno siguiente |
| Ficha de pistola encasquillada | 1 | Custom Token | 1 natural | — |
| Ficha de kit médico | 1 | (es la carta) | — | — |
| Hoja de registro de partidas | 1 | Notebook de TTS o PDF | — | La tabla del final del kit |
| Reglas del kit | 1 | Custom PDF | — | `kit_prueba_1.md` exportado a PDF |
| Mazo de aparición | ~30–40 | Custom Deck | — | El mismo del juego completo (3.10). Se juega con nivel 1 |
| Dados | 2 d20, 2 d6, 1 d4, 1 d10 | Nativos | — | Los 2 d20 son para ventaja y desventaja. Los d6 son para la zona de la herida y para las puertas. Se quitan el d6 de aparición, el de borde y el de tipo de herida |

### 1.3 Juego completo · cartas

| Mazo | Diseños | Cartas | Tipo TTS | Tirada que usa | Origen |
|---|---|---|---|---|---|
| **Botín (objetos)** | 33 | 74 | Custom Deck | Daño del arma (d4/d6/d8/d10/d12). Registrar: ver sección 7 | `cartas_de_objetos.html` |
| · Medicina | 5 | 10 (2 de cada) | | — | Pastillas, vendas, botiquín, alcohol, jeringa |
| · Alimento (antes Comida) | 5 | 15 (3 de cada) | | — | Lata, galletas, mermelada, arroz, cereal. Cuenta como 1 Alimento |
| · Alimento (antes Agua) | 2 | 8 (4 de cada) | | — | Botella y cantimplora. Mismo sello que el resto del Alimento, más un uso extra impreso: "o gastala para limpiar una herida" |
| · Armas | 5 | 7 | | d20 + F (cuerpo a cuerpo) o d20 + D; daño d4/d6/d8/d10/d12 | Cuchillo ×2, Bate ×2, Hacha ×1, Pistola ×1, Escopeta ×1 |
| · Recursos | 8 | 20 | | — | Munición ×4, Madera ×3 (vale 2), Clavos ×3, Chapa ×2, Alambre ×2, Cuerda ×2, Semillas ×1, Combustible ×3 |
| · Señal | 4 | 4 | | — | Radio, Generador, Manual, GPS |
| · Equipo | 4 | 10 | | — | Walkie ×2, Baterías ×4, Bengala ×3, Mochila de montaña ×1 |
| **Supervivientes** | 7 | 7 | Custom Deck | — | `mesa_online.html`: Marta, Raúl, Sofía, Tomás, Nico, Aurelio y Elena. Se roban 3 al empezar y 1 en cada "Rescate" |
| **Acciones** | 4 propuestas | 4 por jugador (12) | Custom Deck | — | Solo existe "Movimiento y sigilo". Propuesta: Combate, Entrar y forzar, Buscar y curar. Va con fichas numeradas del 1 al 5. Pendiente de reglas (prueba 2) |
| **Zombies (perfiles)** | 5 | 5 | Custom Deck | Ataque d20 + 2 | Caminante, corredor, bruto, ácido y chillón, con ilustración y datos. Es de consulta |
| **Aparición de zombies** | Unos 30–40 | Unas 30–40 | Custom Deck | — (no se tiran dados) | Contenido en `diseno/mazo_aparicion.md`, que arma otro agente. Se roba después del turno de los jugadores. Cada carta trae un tipo de zombie y 3 cantidades, una por nivel de peligro. Plantilla en 3.10 |
| **Referencia** | 6 | 6 por jugador (18) | Custom Deck | — | Turno, acciones y ruido, combate, heridas (y cómo limpiarlas), horda, fases del día |
| **Kit prueba 1** | 7 | 7 | Custom Deck | — | Ver 1.2 |
| *Reservado: eventos nocturnos* | — | — | Custom Deck | — | La dirección de arte los nombra, pero no están definidos |

### 1.4 Juego completo · losetas, tableros y hojas

| Componente | Cant. | Tipo TTS | Tirada que usa | Comentario |
|---|---|---|---|---|
| Loseta de calle: recta | 6 | Custom Tile, caja | — | Entradas por el centro de cada borde (máscara N/E/S/O) |
| Loseta de calle: esquina | 4 | Custom Tile | — | — |
| Loseta de calle: en T | 4 | Custom Tile | — | — |
| Loseta de calle: cruce | 2 | Custom Tile | — | — |
| Loseta de calle: cortada | 2 | Custom Tile | — | Barricada de autos |
| Losetas de edificio | 18 | Custom Tile, caja | — | Casa ×4, Almacén ×2, Farmacia ×2, Supermercado, Comisaría, Hospital, Ferretería y Escuela ×1, Taller ×2, Estación de servicio ×1, Plaza ×2. Alcanza para la plantilla más grande (T3: 5 × 3, 8 edificios) |
| Fichas de edificio 1–6 | 12 (2 juegos) | Custom Tile, círculo de 2 caras | El número reemplaza al d6 | Dorso con la casita sobre tinta. Van en una bolsa y se sacan boca abajo |
| Tablas de edificio | 10 | Custom Tile, caja de 2 caras | d20 de botín (con ventaja o desventaja: 2d20) | Al frente, zombies por ficha (1–6) × nivel de peligro (1: días 1–7 · 2: días 8–14 · 3: días 15–20), con registros y notas. Al dorso, botín d20. La plaza no lleva |
| Tablero de base | 1 | Custom Board | Defensa por entrada (sin dados) | Casa con patio sobre calle Las Heras: 5 entradas, camas, depósito, mejoras y señal |
| Mapa de la ciudad | 1 | Custom Board | — | 5 barrios con horas de ida, peligro (☠ 1–3), plantilla y edificios posibles |
| Plantillas de mapa | 4 | Custom Tile pequeña o Notebook | — | P3, T1, T2 y T3: dónde va calle (R) y dónde edificio (B) |
| Tablero de tiempo | 1 | Custom Board | — | Días 1–20 en 3 franjas de nivel de peligro (1–7, 8–14, 15–20), casilla de nivel de peligro, 4 fases del día y reloj de horas 07–21 (anochece a las 19) |
| Hoja de jugador | 3 | Custom Tile, caja | — | Genérica, con hueco para la carta de superviviente (ver 3.5) |
| Supervivientes | 7 | Custom Figurine | — | Uno por carta. El rescatado sale a la mesa cuando entra al grupo |

### 1.5 Juego completo · fichas y marcadores

Todas las fichas genéricas van en **bolsas infinitas**, para no contar existencias. Las cantidades indican cuántas habría en una caja física.

| Ficha | Cant. física | Tipo TTS | Cara(s) | Tirada |
|---|---|---|---|---|
| Caminante | 24 | Custom Tile, círculo de 2 caras | Tranquilo / alerta | Ataca con d20 + 2 |
| Corredor | 8 | Custom Tile, círculo de 2 caras | Tranquilo / alerta | — |
| Bruto | 4 | Custom Tile, círculo de 2 caras, ×1,25 | Tranquilo / alerta | — |
| Infectado ácido | 4 | Custom Tile, círculo de 2 caras | Tranquilo / alerta | — |
| Chillón | 4 | Custom Tile, círculo de 2 caras | Tranquilo / alerta | — |
| Ruido | 40 (bolsa infinita) | Custom Token | 1 | — |
| Daño de zombie | Bolsa infinita | Custom Token | 1 (y de 3) | — |
| Herida ("olor a sangre") | 10 (bolsa infinita) | Custom Tile, círculo de 2 caras | 1. Va en la casilla de zona de la hoja. Abierta (gota roja): pone 1 ficha de ruido por turno en la zona del superviviente. Al limpiarla con 1 carta de Alimento (agua) se da vuelta a la cara "limpia" (gota tachada) y queda como herida hasta curarla en la base | d6 de zona |
| Fatiga | Bolsa infinita | Custom Token | 1 | — |
| Bala (disparos de munición) | Bolsa infinita | Custom Token | 1 | — |
| Voz | Bolsa infinita | Custom Token | 1 | — |
| Números 1–5 para la acción elegida | 5 por jugador (15) | Custom Tile, círculo de 2 caras | Número / dorso del color del jugador | — |
| Construcción ("obra") | 3 | Custom Token | 1 | — |
| Tablón de barricada | 15 (3 por entrada) | Custom Token apilable | 1 | Nivel = cantidad de tablones apilados |
| Blindaje de chapa (nivel 3) | 5 | Custom Token | 1 | — |
| Trampas | Alarma ×2, Estacas ×2, Púas ×2, Fosa ×1, Incendiaria ×2 | Custom Tile, círculo | Letra A/E/P/F/I sobre icono | Estacas: d6 de daño |
| Puerta / ventana | 8 / 6 | Custom Tile, caja de 2 caras | Cerrada/abierta · intacta/rota | d6 (con un 6 cae) |
| "Saqueado" | 8 | Custom Token (sello) | 1 | — |
| Registro restante | Bolsa infinita | Custom Token | 1 | Al revelar se ponen N fichas (1–3) y se quita una por cada Registrar |
| Escondido | 3 | Custom Token | 1 | — |
| Marcador de día | 1 | Custom Token | 1 | — |
| Marcador de nivel de peligro | 1 | Custom Tile, caja de 2 caras | Nivel 1 / 2 en una cara y 3 en la otra; mejor 3 estados de TTS (1, 2, 3) | — |
| Marcador de hora | 1 | Custom Token | 1 | — |
| Marcador de fase del día | 1 | Custom Token | 1 | — |
| Marcador de señal (etapas) | 5 | Custom Tile, círculo de 2 caras | Pendiente / completa | — |
| Marcadores de sangre y fatiga | 1 + 1 por jugador | Custom Token del color del jugador | 1 | — |
| Recursos del depósito | Contadores nativos ×5 | Nativo (Counter) | — | Alimento, medicinas, materiales, munición y combustible (comida y agua de `mesa_online` se unen) |

### 1.6 Dados

| Dado | Cant. | Tipo | Para qué |
|---|---|---|---|
| d20 | 2 por jugador (color del jugador) + 2 grises para zombies | Nativo | Ataque (d20 + mod contra Defensa); ventaja y desventaja con 2d20; ataque de zombie (d20 + 2); botín de edificio (d20) |
| d4, d6, d8, d10, d12 | 1 de cada por jugador | Nativo | Daño de cuchillo, bate, hacha, pistola y escopeta |
| d6 | 2 grises comunes | Nativo | Puerta que cae (6), estacas y, en la prueba 1, farmacia, casa y registrar. **Ya no hay d6 de aparición ni de errantes**: los reemplaza el mazo de aparición |
| d6 "zona de herida" | 1 | Custom Dice | Cabeza / Torso / Torso / Brazo izq. / Brazo der. / Piernas |

El dado de zona de herida es opcional: con un d6 nativo y la tabla impresa en la hoja también funciona. Ya no hay tipos de herida (ni rasguño, laceración, fractura o mordedura), ni infección, ni antibióticos.

---

## 2. Especificación de archivos

### 2.1 Criterios generales

- **Originales y exportación por separado.** Los originales (`arte/`) se hacen a la medida de diseño: cartas a 750 × 1050 px y losetas a 1500 × 1500. Lo que se sube a TTS (`tts/`) se genera desde esos originales. Nunca se edita una hoja exportada a mano.
- **Lado máximo de 4096 px por imagen.** TTS acepta imágenes más grandes, pero 4096 es el límite práctico para que carguen bien en cualquier placa de video y no tarden en descargarse.
- **JPG con calidad 90** para todo lo rectangular y sin transparencia: hojas de cartas, losetas y tableros. **PNG con alfa** solo para Custom Token y Custom Figurine, porque la transparencia define la forma. Las caras de los Custom Tile circulares pueden ser JPG cuadrados, porque TTS recorta el círculo.
- **Color sRGB** y sin perfiles raros. Al exportar desde un navegador o Figma, verificar que el papel #d8c8a6 no se desplace.
- **Versión en el nombre.** TTS guarda las imágenes en caché según la URL. Si se reemplaza un archivo y se lo vuelve a subir con el mismo nombre, algunos jugadores van a seguir viendo la versión vieja. Cada cambio de arte lleva un nuevo sufijo `_v02`, `_v03`, etc.
- **Nombres:** minúsculas, `snake_case`, sin tildes ni ñ (`senal`, no `señal`). Llevan el prefijo del mazo y un número de hoja con 2 dígitos.

### 2.2 Hojas de cartas (Custom Deck)

Reglas de TTS: la cuadrícula tiene como máximo 10 columnas × 7 filas, y la **casilla de abajo a la derecha es la carta oculta**. Por eso entran 69 cartas por hoja como máximo. Todas las casillas miden lo mismo. Las casillas sobrantes van en papel liso. En el diálogo de importación se completan Width, Height y Number, y se marca *Back is hidden*. Aunque esté marcado, la última casilla se deja igual con la imagen oculta, por compatibilidad.

Formato de carta: 750 × 1050 px, proporción 5:7 (como una carta de póker), que es la proporción de la carta por defecto de TTS.

| Mazo | Caras en la hoja | Cuadrícula | Carta exportada | Hoja | Hojas | Dorso |
|---|---|---|---|---|---|---|
| Botín | 33 únicas + oculta | 7 × 5 | 585 × 819 | 4095 × 4095 | 1 | `botin_dorso` (mochila a tinta sobre noche) |
| Botín, variante con copias en la hoja | 74 | 8 × 5 | 512 × 716 | 4096 × 3580 | 2 (37 + 37) | ídem |
| Supervivientes | 7 + oculta | 4 × 2 | 750 × 1050 | 3000 × 2100 | 1 | `supervivientes_dorso` (silueta) |
| Acciones (4 por jugador) | 4 + oculta → 3 × 2 | 3 × 2 | 750 × 1050 | 2250 × 2100 | 1 por color de jugador (3) | `dorso_carta.png` (el 30 rojo) |
| Zombies (perfiles) | 5 + oculta | 3 × 2 | 750 × 1050 | 2250 × 2100 | 1 | `zombies_dorso` |
| Aparición de zombies | Unos 12–15 diseños + oculta (copias en TTS) | 4 × 4 | 750 × 1050 | 2924 × 4096 (cartas de 731 × 1024) | 1 | `aparicion_dorso` (mano del suelo) |
| Referencia | 6 + oculta → 4 × 2 | 4 × 2 | 750 × 1050 | 3000 × 2100 | 1 | `referencia_dorso` |
| Kit prueba 1 | 7 + oculta | 4 × 2 | 750 × 1050 | 3000 × 2100 | 1 | `botin_dorso` |

- **Botín: se recomienda la hoja de caras únicas.** Se importa con Number = 33. Después se duplica en TTS cada carta según la columna "copias" del JSON que genera el script, se junta todo en un mazo y se guarda. Un mazo guardado repite el mismo número de carta sin costo. Las cartas quedan a 819 px de alto en vez de 716.
- **Acciones con dorso por jugador.** Las acciones van en el color del jugador (marco u óxido/verde/azul en el sello), así no se mezclan los mazos. Si al final las cartas son idénticas para todos, alcanza con una sola hoja.
- **Dorsos:** una imagen suelta por mazo, de 750 × 1050 JPG. Cada mazo tiene un dorso distinto, para que nunca se mezclen.
- **Sin bordes recortados.** El borde irregular de la maqueta (`clip-path`) no sirve en TTS, porque la carta es un rectángulo con esquinas apenas redondeadas. Se resuelve con papel a sangre hasta el borde y un "borde quemado" pintado (viñeta sepia de unos 24 px) que imita el rasgado.

### 2.3 Losetas, tableros y hojas

| Archivo | Medida (px) | Formato | Tipo TTS | Medida en mesa (propuesta, para calibrar) |
|---|---|---|---|---|
| Loseta de calle o edificio | 1500 × 1500 (500 px por zona) | JPG | Custom Tile, caja, grosor 0,2 | 6 × 6 unidades (zona de 2 × 2) |
| Losetas P1-A y P1-B | 1500 × 1500 | JPG | Custom Tile | 6 × 6 |
| Tablero de base | 3600 × 2240 (proporción 900:560 de la maqueta) | JPG | Custom Board | Unas 18 × 11,2 |
| Mapa de la ciudad | 3200 × 2100 (640:420) | JPG | Custom Board | Unas 14 × 9,2 |
| Tablero de tiempo | 3600 × 1200 | JPG | Custom Board | Unas 18 × 6 |
| Hoja de jugador | 2400 × 1600 | JPG | Custom Tile, caja, grosor 0,1 | Unas 12 × 8 |
| Hoja del superviviente de prueba | 2400 × 1600 | JPG | Custom Tile | Unas 12 × 8 |
| Tabla de edificio (2 caras) | 1500 × 1050 por cara | JPG | Custom Tile, caja | Unas 7 × 4,9 |
| Ficha de farmacia | 1050 × 1050 | JPG | Custom Tile | — |
| Reloj de turnos P1 | 2400 × 300 | JPG | Custom Tile | Unas 12 × 1,5 |

La medida en mesa se ajusta con la escala del objeto. El criterio es que **una zona de loseta (2 × 2 unidades) aloje 4 fichas de zombie de 0,9 unidades** sin que se superpongan, más la figura de un superviviente. Hay que medirlo con la herramienta de regla de TTS en la primera sesión de montaje.

### 2.4 Fichas, figuras y dados

| Archivo | Medida (px) | Formato | Tipo TTS |
|---|---|---|---|
| Ficha de zombie: tranquilo y alerta | 512 × 512 por cara | JPG (TTS recorta el círculo) | Custom Tile, círculo |
| Ficha de edificio: frente 1–6 y dorso | 512 × 512 | JPG | Custom Tile, círculo |
| Fichas genéricas (ruido, daño, heridas, etc.) | 256 × 256 | PNG con alfa | Custom Token |
| Tablón, chapa y sello "Saqueado" | 512 × 256 | PNG con alfa | Custom Token |
| Puerta y ventana (2 caras) | 512 × 256 | JPG | Custom Tile, caja |
| Superviviente de pie | 600 × 900 | PNG con alfa | Custom Figurine |
| Dado de zona de herida | Plantilla d6 de TTS, unos 256 px por cara | PNG | Custom Dice |

### 2.5 Estructura de carpetas

```
Juegaso/
├── fuentes/                     # (no se toca)
├── diseno/
│   └── componentes_tts.md       # este documento
├── herramientas/
│   └── hoja_de_cartas.py        # une cartas sueltas en hojas para TTS
├── arte/                        # originales a medida de diseño (750×1050, 1500×1500…)
│   ├── cartas/{botin,supervivientes,acciones,zombies,aparicion,referencia,kit_p1}/
│   │   └── botin_medicina_frasco_pastillas.png …
│   ├── losetas/  tableros/  fichas/  figuras/
│   └── manifiestos/botin.csv    # archivo,copias (fija orden y copias)
└── tts/                         # solo lo que se sube a TTS (generado)
    ├── cartas/
    │   ├── botin/  botin_v01_hoja_01.jpg  botin_v01.json  botin_dorso_v01.jpg
    │   ├── supervivientes/  acciones/  zombies/  aparicion/  referencia/  kit_p1/
    ├── losetas/
    │   ├── calles/     calle_recta_v01.jpg  calle_esquina_v01.jpg …
    │   ├── edificios/  edif_casa_v01.jpg  edif_farmacia_v01.jpg …
    │   └── prueba1/    p1_loseta_a_v01.jpg  p1_loseta_b_v01.jpg
    ├── tableros/  base_v01.jpg  ciudad_v01.jpg  tiempo_v01.jpg  hoja_jugador_v01.jpg
    ├── tablas/    tabla_casa_frente_v01.jpg  tabla_casa_dorso_v01.jpg …
    ├── fichas/    zombie_caminante_tranquilo_v01.jpg  …_alerta_v01.jpg  ruido_v01.png …
    ├── figuras/   sup_marta_rios_v01.png …
    ├── dados/     dado_zona_herida_v01.png
    └── pdf/       kit_prueba_1_v01.pdf
```

Nombres de las cartas sueltas: `<mazo>_<familia>_<nombre>.png`, por ejemplo `botin_armas_bate_con_clavos.png` o `botin_recursos_madera_tablones.png`. El orden alfabético agrupa por familia. Si se necesita otro orden, lo fija el manifiesto.

---

## 3. Plantillas de maquetación

Medidas en px sobre el original. Fuentes: **Big Shoulders Stencil Display** (títulos), **Barlow Condensed** (interfaz, números y sellos), **Barlow** (texto de regla) y **Special Elite** (sabor, pie y notas). Las cuatro son Google Fonts con licencia OFL, así que se pueden incrustar en el arte sin problema. Colores de carta: papel #dccba8, tinta #24201a y sepia #6b5a43.

### 3.0 Voseo en todo el texto impreso

Decisión del autor: todo el material va en voseo rioplatense. Imperativos y presentes de segunda persona: *elegí, marcá, tirá, robá, gastá, usá, descartá, llevá, podés, tenés, te movés, sos*. Pronombres: *vos, te, tu*. Con enclíticos, sin tilde: *descartala, usala, llevala, gastala*.

| Antes (tuteo) | Ahora (voseo) |
|---|---|
| Elige 1 y marca con ficha numerada | Elegí 1 y marcá con ficha numerada |
| Cómo te mueves y cuánto te oyen | Cómo te movés y cuánto te oyen |
| Te mueves 1 zona | Te movés 1 zona |
| No puedes moverte | No podés moverte |
| Descártala · Úsala · Llévala | Descartala · Usala · Llevala |
| Tira d20 + Fuerza | Tirá d20 + Fuerza |
| Roba un superviviente | Robá un superviviente |

El sabor ya estaba en voseo ("Corta si la agarrás mal", "incluso en vos"). Antes de exportar cada hoja hay que buscar en el texto *-as/-es* de segunda persona (puedes, tienes, mueves) y tildes de imperativo (elige, tira, marca, úsala).

### 3.1 Reglas de legibilidad en TTS

- **A distancia de mesa** (cámara normal), una carta se ve de unos 60–100 px de alto y una ficha de 20–30 px. A esa distancia solo se leen **color, forma y un número grande**. Por eso las fichas no llevan texto, y en las cartas el sello de familia y los espacios tienen que reconocerse por color y forma.
- **Con zoom** (Alt sobre la carta), la carta llena unos 700–900 px de alto en una pantalla de 1080p. Lo justo para leer texto de unos 18 px exportados.
- **Tamaños mínimos sobre el original de 750 px**, pensados para que, reducidos al 78 % en la hoja del botín, sigan legibles: regla de 28 px (se exporta a ~22), sabor de 24 px (~19) y pie de 20 px (~16; es lo único que puede quedar chico, porque no es necesario para jugar). Título de 60–66 px.
- **Margen seguro de 48 px** en todo el borde. TTS redondea las esquinas y el borde quemado se come unos 24 px.
- **Esquina superior izquierda:** cuando la mano se llena, TTS superpone las cartas. La identidad de la carta (sello y espacios de mochila) tiene que leerse en la franja izquierda superior, de 0 a 300 px de ancho.
- **Contraste:** tinta sobre papel da más de 10:1. El texto sobre noche usa hueso #ece5d6, nunca gris para texto de regla.
- **Daltonismo:** los sellos de familia se diferencian por color **y** por la palabra o el icono. Las fichas, por color **y** silueta.

### 3.2 Carta de objeto (botín) · 750 × 1050

Basada en `cartas_de_objetos.html` (`.carta`, 1 cqi = 7,5 px).

```
 0 ┌──────────────────────────────────────────┐
48 │ [SELLO FAMILIA]  ■■ espacios            │  48–100  sello (Barlow Cond 27 px, color de familia,
   │                                          │          rotado −3°) + cuadros de mochila (33 px, rayados)
112│ TÍTULO DE LA CARTA                        │ 112–236  Big Shoulders 64 px, hasta 2 líneas
   │                                          │
248│ ┌──────────────────────────────────────┐ │ 248–706  ilustración 654 × 458 (200:140), marco de tinta
   │ │        ilustración a tinta           │ │          irregular, viñeta clara al centro
   │ └──────────────────────────────────────┘ │
718│ DAÑO d6 │ RUIDO ▮▮▯▯ Bajo │ ESPACIOS 2   │ 718–800  solo armas: 3 columnas, número 48 px
   │                                          │
   │ CUENTA COMO 1 MEDICINA.                  │ 718/812–900  regla (Barlow 28 px; títulos en Cond 30 px)
   │ Expedición · 1 PA: …                     │          idéntica en toda la familia
908│ Etiqueta medio borrada. Vencía en 2019.  │ 908–962  sabor (Special Elite 24 px, sepia)
972│ Medicina · 1/5 ·········· ×2 en el mazo  │ 972–1002 pie (Special Elite 20 px, línea punteada arriba)
   └──────────────────────────────────────────┘ margen 48
```

- **Sello de familia** con los colores ya definidos: Medicina #2c6656, **Alimento #9a4a2e** (el sello de Comida; el azul #3b5870 de Agua se deja de usar), Arma #7e2626, Recurso #5a4a35 (el sello dice el recurso: Munición, Madera…), Señal #8f6a16 y Equipo #2f4f5e.
- **Cambio propuesto para TTS:** sumar una **franja de color de familia de 12 px en el borde izquierdo**, a sangre y por debajo del borde quemado. En la mano de TTS y en una pila mezclada, la familia se reconoce sin hacer zoom.
- **Alimento con agua (botella y cantimplora):** mismo sello, misma regla base ("Cuenta como 1 Alimento.") y una **segunda línea de regla** separada por una línea punteada: *"o gastala para limpiar una herida"*. Va con un icono de gota que también se repite en la ficha de herida abierta. Así se lee como un uso extra y no como otra familia. El texto de la regla ocupa 2 líneas más; se compensa bajando la ilustración a 430 px de alto en esas 2 cartas.
- **Regla de Medicina, a corregir:** el texto de la fuente ("limpiar un rasguño", "1 Medicina frena la infección 1 día") ya no vale, porque no hay tipos de herida ni infección. Queda: "Cuenta como 1 Medicina. Base: 2 Medicinas curan 1 herida." El uso en expedición lo define el reglamento.
- **Familia Alimento:** 7 diseños y 23 cartas. Regla común: "Cuenta como 1 Alimento. Cada superviviente come 1 por día, o 2 si termina el día con fatiga. Guardalo en la base al volver de la expedición."
- **Espacios:** 1 o 2 cuadros rayados, o la palabra "puesta" para la mochila de montaña. La propuesta es acercarlos al sello (arriba a la izquierda), por la regla de la mano superpuesta.
- **Ilustración:** las maquetas SVG actuales sirven para la primera versión en TTS. El arte final se hace con los prompts de tinta de `arte/prompts_ilustraciones.md` (sección Objetos).
- **Dorso del botín:** noche #16191d, mochila o caja abierta a tinta en papel, y la palabra "BOTÍN" en Big Shoulders. El dorso de las acciones ya es el 30 rojo, y hay que distinguirlos.

### 3.3 Carta de acción · 750 × 1050

Basada en la maqueta "Después · tinta sobre papel" de `direccion_de_arte.html`.

```
 48–200  Cabecera centrada: título Big Shoulders 67 px ("MOVIMIENTO Y SIGILO")
         + subtítulo Special Elite 25 px ("Cómo te movés y cuánto te oyen"); doble filete de tinta
 220–960 5 filas iguales (~148 px cada una), separadas por línea punteada:
         [nº en círculo irregular 75 px] NOMBRE (Cond 45 px)            [1 PA] (chip Special Elite 28 px)
                                         descripción (Barlow 26 px)
                                         ▮▮▯▯ Medio · 2 zonas (Special Elite 25 px; Medio/Alto en óxido #8e3f22)
 972–1002 pie: "Día 30 · carta de acción · elegí 1 y marcá con ficha numerada" (20 px)
```

- El número de la fila (1–5) coincide con la ficha numerada del jugador, que se pone boca abajo sobre la carta.
- Hay que actualizar el texto a los costes del kit si la prueba 1 los valida: Sigilo 2 PA / 1 zona y Correr 1 PA / 2 zonas.
- Marca del jugador: un punto o marco del color del asiento en la esquina superior izquierda.

### 3.4 Carta de superviviente · 750 × 1050

```
 48–110  NOMBRE (Big Shoulders 58 px) · profesión (Special Elite 26 px)
 120–620 retrato a tinta 654 × 500 (encuadre 2:3 recortado al pecho), mismo estilo que los zombies
 632–760 atributos en 4 casillas: F D C P · valor (Big Shoulders 56 px) + modificador (Cond 28 px, "+1")
 772–940 habilidad: nombre en Cond 32 px mayúsculas + texto Barlow 28 px
 952–1002 pie: "Superviviente · provisorio" y el número de la carta (1/7)
```

Dorso: silueta de grupo a contraluz, sin texto, en noche y papel.

### 3.5 Hoja de jugador (genérica) · 2400 × 1600

Papel sobre noche, como el resto. Sirve para cualquier superviviente: la carta se apoya en el hueco.

```
┌──────────────┬───────────────────────────────┬──────────────────────┐
│ HUECO CARTA  │ SANGRE  ○○○○○○  (0–6, gotas)   │ CUERPO (silueta)     │
│ superviviente│ FATIGA  ○○○     (0–3)          │ 5 casillas de herida │
│ (snap point, │ PA      ○○○     (3 por turno)  │ cabeza · torso       │
│  medida de   │ DEFENSA [10 + mod D] grande   │ brazo izq · brazo der│
│  carta)      │ ESCONDIDO [casilla]            │ piernas              │
├──────────────┴───────────────────────────────┴──────────────────────┤
│ MOCHILA: 6 ■ ■ ■ ■ ■ ■ (+2 punteados para la mochila de montaña) → franja para apoyar cartas │
│ Recordatorio: modificador = atributo − 2 · Muere con sangre 0 o 2.ª herida en la cabeza       │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

- La franja de la mochila es una zona para dejar las cartas de objeto superpuestas. La capacidad se cuenta con los cuadros de cada carta, no con casillas fijas.
- Las 5 casillas de herida (cabeza, torso, brazo izq., brazo der., piernas) **no tienen tipos**: cada una es un hueco del tamaño de la ficha de gota (256 px), con el efecto de esa zona en letra chica. Ejemplo: "Brazo izq.: mochila −1". Con lugar para 2 gotas por casilla, por la regla de la segunda herida en la cabeza.
- Los marcadores de sangre y fatiga son fichas del color del jugador con snap points en cada casilla.
- **Hoja del superviviente de prueba (P1):** la misma maqueta con la carta impresa (3/3/3/3, Defensa 11) y la tabla de armas iniciales en la franja inferior.

### 3.6 Loseta · 1500 × 1500

Basada en `tesela()` de `base_y_losetas.html` (viewBox 300 → ×5).

- Fondo de papel #dccba6 con grano y viñeta. Marco de tinta de 15 px.
- **Rejilla de zonas:** líneas punteadas cada 500 px, tinta al 35 %. Tiene que verse con zoom de mesa, así que va a 5 px de grosor (no 1).
- **Calles:** asfalto #bba983 y veredas #d3c19a. Entran por el centro de cada borde (500–1000 px), para que cualquier loseta encaje con cualquier otra. Llevan cordón, grietas y autos de ambientación.
- **Edificios:** muros de 35 px de tinta, ventanas dobles y puerta abierta hacia la vereda (abajo, sin rotar). La loseta se gira en TTS para que mire a la calle. En el centro va la placa con el nombre (Big Shoulders 90 px, sobre papel con borde).
- **Puertas entre zonas** marcadas con un hueco en el muro: el lugar exacto donde va la ficha de puerta.
- **Zona de la ficha de edificio:** un círculo punteado de 260 px en la zona central, donde se apoya la ficha boca abajo.
- **Prueba 1:** coordenadas A–F y 1–3 en los bordes exteriores (Cond 60 px). En A3, "BASE" estampado en rojo #922b2b. En la loseta, el (Z) de los zombies iniciales marcado con una cruz sepia.

### 3.7 Tablero de base · 3600 × 2240

Basado en `dibujarBase()`: un plano a tinta de la casa con patio.

- 5 entradas con un recuadro de defensa (puerta principal, puerta del patio, ventana de la cocina, ventana del dormitorio y techo). Cada una tiene una casilla para apilar tablones (nivel 0–3) y otra para la ficha de trampa.
- Camas (4 + cama extra): un hueco de carta para cada superviviente que se queda en la base. Más un puesto de **guardia**.
- **Depósito:** 5 casillas de recurso (Alimento, Medicinas, Materiales, Munición, Combustible) con un contador nativo encima, y una zona para dejar las cartas de material y alimento que vuelven de la expedición.
- **Mejoras** (taller, huerta, recolector, cama extra): casillas con el coste impreso y la ficha de "hecho".
- **Señal de socorro:** una tira de 5 etapas con nombre y requisito (Radio o antena · Energía · Baliza · Mensaje · Activación), con la etapa 5 en rojo y el aviso "ruido máximo: atrae una horda".

### 3.8 Tablero de tiempo · 3600 × 1200

- **Fila 1, días 1–20:** 20 casillas grandes (unos 160 px) divididas en **3 franjas de nivel de peligro**, marcadas arriba con un rótulo y un número grande en un círculo irregular: **1** (días 1–7, papel claro), **2** (días 8–14, papel oscuro con borde óxido) y **3** (días 15–20, papel quemado con borde rojo #922b2b). Entre franja y franja, un filete grueso de tinta. Las casillas 8 y 15 llevan una flecha "sube el peligro". El día 20 lleva el helicóptero. El nombre "Día 30" está pendiente.
- **Casilla de nivel de peligro** (a la izquierda de la fila 1): un hueco para el marcador de nivel (1/2/3), que se mueve al pasar a los días 8 y 15. Es el número que se lee en las cartas de aparición y en las tablas de edificio.
- **Descanso rápido:** casilla "pasa el día" junto al calendario, como recordatorio de la regla.
- **Fila 2, fases del día:** Base · Planificación · Expedición · Regreso y noche.
- **Fila 3, reloj de horas 07–21:** franjas de alba, viaje, saqueo y noche. Desde las 19 la franja es de noche (azul noche), con el recordatorio "de noche, robá 1 carta de aparición más" (a confirmar con `mazo_aparicion.md`).

### 3.9 Fichas

Recomendación sobre la pregunta abierta de la dirección de arte: **las fichas conservan colores fuertes** para leerse en la mesa, pero con trazo de tinta y textura de papel en el borde, para que no parezcan de otro juego.

| Ficha | Forma | Color e icono |
|---|---|---|
| Ruido | Círculo de 0,8 u | Óxido #b4583a, ondas concéntricas en hueso |
| Daño | Gota irregular de 0,6 u | Rojo 30 #922b2b, número 1 en hueso (la de 3 es más grande) |
| Fatiga | Hexágono | Gris #9a9f9f, "zzz" a tinta |
| Voz | Globo | Verde radio #2e7d6b |
| Bala | Cápsula | Latón (luna #d9b45a) |
| Construcción | Cuadrado | Papel oscuro #b9a682, martillo |
| Escondido | Círculo | Noche con un ojo tachado en hueso |
| Herida / olor a sangre | Círculo de 0,6 u con una gota, Custom Tile de 2 caras | **Abierta:** rojo 30 #922b2b, gota en hueso con 2 ondas de ruido a los costados. **Limpia:** papel con la gota a tinta, tachada. Es la única ficha de herida |
| Nivel de peligro | Cuadrado de 1 u, 3 estados | Número Big Shoulders 1/2/3 sobre papel claro, oscuro o quemado (los mismos tonos que las franjas del calendario) |
| Números 1–5 | Círculo de 0,9 u | Frente en papel con número Big Shoulders al 60 %; dorso en el color del jugador |
| Zombie | Círculo de 0,9 u (bruto 1,1 u) | Frente "tranquilo": ilustración recortada en un círculo de papel con un aro de tinta fino. Dorso "alerta": la misma ilustración con un aro rojo grueso (40 px) y un "!" arriba |
| Ficha de edificio | Círculo de 0,9 u | Dorso: casita en papel sobre tinta (como `fichaDorso`). Frente: número 1–6 sobre papel |

Las fichas de zombie no llevan texto. El tipo se reconoce por la ilustración y por una **marca de borde**: caminante sin marca, corredor con 2 rayas, bruto con aro doble, ácido con un punto verde y chillón con ondas.

**Herida = gota roja.** Hay un solo tipo de herida y toda herida queda abierta hasta limpiarla con agua. En el paso de reloj se mira la hoja: cada gota roja deja 1 ficha de ruido en tu zona. Al limpiarla, la ficha se da vuelta a "limpia" y sigue contando como herida hasta curarla en la base.

### 3.10 Carta de aparición de zombies · 750 × 1050

El contenido (tipos, cantidades, textos especiales y cuántas copias) lo define `diseno/mazo_aparicion.md`. Esta es la plantilla. La carta se lee **de un vistazo desde la mesa**, porque se roba en cada turno: lo que importa es el tipo de zombie y el número del nivel actual.

```
 0 ┌──────────────────────────────────────────┐
48 │ TIPO DE ZOMBIE            [● marca]      │  48–130  nombre del tipo en Big Shoulders 72 px
   │                                          │          + marca de borde del tipo (la misma de la ficha)
140│ ┌──────────────────────────────────────┐ │ 140–600  ilustración a página casi completa (654 × 460),
   │ │  ilustración del zombie (tinta)      │ │          recorte de las ilustraciones 2:3 existentes
   │ └──────────────────────────────────────┘ │
612│ ┌──────────┬──────────┬──────────┐       │ 612–860  TABLA DE CANTIDADES: 3 columnas iguales (218 px)
   │ │ NIVEL 1  │ NIVEL 2  │ NIVEL 3  │       │          rótulo "NIVEL n" en Cond 30 px sobre una franja
   │ │   ①      │   ②      │   ③      │       │          con el tono del calendario (claro, oscuro, quemado)
   │ │    1     │    2     │    3     │       │          número en Big Shoulders 150 px; "—" si es 0
   │ └──────────┴──────────┴──────────┘       │
872│ Texto especial opcional (Barlow 28 px)   │ 872–960  hasta 3 líneas; si no hay, queda una frase de sabor
   │ «Sabor a máquina» (Special Elite 24 px)  │          en Special Elite
972│ Aparición · 7/36                         │ 972–1002 pie: número de carta
   └──────────────────────────────────────────┘
```

- **Legibilidad de las cantidades:** son lo más importante de la carta. El número va a 150 px (unos 110 px en la hoja exportada). Hasta con la carta chica sobre el descarte, sin zoom, se distingue 1, 2 o 3. Cada columna repite su nivel de dos formas, con el rótulo "NIVEL 2" y con el número en círculo. Además va en el tono de papel de su franja del calendario, así se busca la columna por color.
- **Dónde aparecen:** si la carta dice el lugar (borde de la loseta más ruidosa, zona de la puerta, etc.), se imprime como un icono chico sobre la tabla. El texto va en el bloque especial.
- **Cartas especiales** (horda, nada, "el chillón llama", etc.) usan la misma estructura. Si no aparece ningún zombie, la tabla muestra "—" en las 3 columnas y el texto especial crece.
- **Varios tipos en una carta:** la ilustración se divide en 2 y la tabla tiene 2 filas (una por tipo), con números de 100 px.
- **Dorso:** `aparicion_dorso`. La mano que sale del suelo (`mano_del_suelo.jpg`) recortada en un círculo, sobre noche, con la palabra "APARICIÓN" en óxido. Tiene que ser distinto del dorso del botín (mochila) y del de las acciones (el 30 rojo).
- **Tipo TTS:** Custom Deck. En la hoja van solo los diseños únicos y las copias se hacen en TTS, igual que en el botín.
- **Texto en voseo:** por ejemplo, "Si hay un superviviente escondido en esa loseta, robá otra carta".

---

## 4. Disposición de la mesa en TTS

### 4.1 Mesa y colores de jugador

- Mesa rectangular grande, con superficie oscura. La dirección C va sobre noche: se usa una mesa de imagen propia (*Custom table*) con la textura noche #16191d, o una mesa de madera oscura con iluminación baja.
- **Asientos:** Jugador 1 = **Orange** (óxido #8e3f22), Jugador 2 = **Green** (#3d5f4a), Jugador 3 = **Blue** (#33495f). Son los mismos colores que `COLOR_JUG` del prototipo. Los otros 7 colores de TTS quedan sin zona de mano.
- Con 1 jugador se usan las zonas de Orange. Las de Green y Blue quedan vacías, sin ningún cambio.

### 4.2 Plano (vista desde arriba; los jugadores se sientan abajo)

```
                         ┌─────────── LADO DE ARRIBA (sin jugadores) ──────────┐
                         │ [Mapa de la ciudad]      [Tablero de tiempo]        │
                         │  14×9                     18×6 · día/fase/hora       │
                         │                                                      │
  ┌ RESERVA (izquierda) ┐ │      ┌──────── ZONA DE EXPEDICIÓN ────────┐  ┌ BASE ┐ │
  │ Bolsas infinitas:   │ │      │ hasta 5×3 losetas de 6×6 = 30×18 u │  │ tablero│ │
  │ ruido, daño,        │ │      │ (vacía al empezar el día)           │  │ 18×11 │ │
  │ heridas, fatiga,    │ │      │                                     │  │ señal,│ │
  │ voz, bala, registro │ │      │                                     │  │ depósito│
  │ Zombies por tipo    │ │      └─────────────────────────────────────┘  └──────┘ │
  │ Bolsa fichas edif.  │ │  [Mazo aparición][Descarte aparición] junto al mapa   │
  │                     │ │  Pilas de losetas: calles por tipo · edificios         │
  │ Tablas de edificio  │ │  Mazo de botín · descarte · supervivientes             │
  └─────────────────────┘ │  Dados comunes (gris) · dado de zona de herida          │
                         │                                                      │
                         │ [Hoja J1 Orange]   [Hoja J2 Green]   [Hoja J3 Blue]  │
                         │  + 2d20, d4–d12     + ídem             + ídem          │
                         │  + referencia       + referencia       + referencia    │
                         └──── zonas de mano Orange · Green · Blue (abajo) ─────┘
```

- **Zona de expedición, al centro:** el área más grande. Va vacía y desbloqueada. Las losetas se ponen según la plantilla del barrio. Conviene activar en TTS una cuadrícula de 2 unidades (*Grid*) con *snap* activo, para que las losetas encajen solas.
- **Base, a la derecha:** se juega al principio y al final del día. Es un Custom Board **bloqueado**, con *snap points* en las entradas, camas y depósito.
- **Ciudad y tiempo, arriba:** bloqueados, porque se leen en cada fase. Los marcadores de día, nivel de peligro, fase y hora quedan sueltos.
- **Mazo de aparición, junto a la zona de expedición** (arriba a la izquierda del mapa, en el borde más cercano a la reserva de zombies): el mazo boca abajo y, al lado, el descarte boca arriba. Cada uno tiene un *snap point* y un rótulo en la mesa. Al robar, la carta se da vuelta sobre el descarte, a la vista de todos, y la cantidad se lee con el marcador de nivel de peligro, que queda arriba en el tablero de tiempo. Cuando se acaba, se mezcla el descarte.
- **Reserva, a la izquierda:** bolsas infinitas con un nombre claro ("Ruido", "Daño"…), una pila de zombies por tipo y la bolsa de fichas de edificio.
- **Jugadores, abajo:** la hoja de cada jugador está bloqueada, con sus dados (coloreados con el tinte del asiento) y sus cartas de referencia al lado. Las cartas de acción van en la mano, en la zona de mano de TTS.
- Con 1 jugador, la hoja de Orange va al centro de la fila de abajo. Con 2, Orange y Green. Con 3, las tres.

### 4.3 Montaje del Kit prueba 1

Una **bolsa guardada** ("Kit prueba 1") que se saca sobre la mesa vacía. Contiene:
- Las losetas P1-A y P1-B, una al lado de la otra, al centro.
- La hoja del superviviente de prueba abajo, con las 7 cartas del kit al lado (las 3 armas, a elegir 2) y la figura en A3.
- Los 10 caminantes, en 3 (en C1, F1 y D3, cara tranquilo) y 7 en reserva.
- La bolsa de ruido, las 4 puertas sobre sus bordes, la ficha de farmacia y el reloj 1–12 arriba.
- El mazo de aparición y su descarte, al lado de la loseta P1-B (borde F).
- Los dados y el PDF del kit.

Así la prueba 1 se monta en un minuto, sin el resto del juego en la mesa.

### 4.4 Ajustes útiles de TTS

- **Bloquear** (L) todo lo que es tablero o hoja, y **ponerle nombre** a cada objeto (clic derecho, Name). El nombre aparece al pasar el mouse.
- Ponerle a cada zombie su **descripción**: Defensa, movimiento y efecto.
- *Snap points* en las casillas de la base, de las hojas y del tablero de tiempo.
- Opcional, para ambientar: bajar la iluminación de la mesa (*Lighting*) cuando anochece.
- Sin scripts Lua en la v0.1: todo se hace a mano, igual que en la mesa física. Más adelante se podría automatizar el robo del mazo de aparición, con un botón que lea el nivel de peligro.

---

## 5. Guardado y subida: Steam Cloud y Workshop

### 5.1 Importar con Steam Cloud

1. Generar los archivos de `tts/` con nombres versionados (`_v01`).
2. En TTS: **Objects → Components → Custom →** Deck / Tile / Token / Board / Figurine / Dice. Hacer clic en el objeto sobre la mesa para abrir el diálogo de importación.
3. En cada campo de imagen, tocar el icono de carpeta y elegir el archivo local. TTS pregunta **"Local o Cloud"**: hay que elegir siempre **Cloud**. El archivo se sube a la Steam Cloud y el campo pasa a una URL `steamusercontent`. Con "Local", los demás jugadores no ven nada.
4. Para un Custom Deck, completar Width, Height y Number con los valores del JSON del script, y marcar *Back is hidden*.
5. **Modding → Cloud Manager:** crear la carpeta `Dia30`, ordenar los archivos y borrar versiones viejas. La Steam Cloud tiene una cuota limitada, que se ve en el Cloud Manager.
6. Si se cambia un arte: subir el archivo nuevo con otro sufijo de versión y, en el objeto, usar *Custom → reemplazar URL*. Si alguien sigue viendo la imagen vieja: **Modding → Cache → borrar caché**.

### 5.2 Guardar

- **Objetos guardados** (*Saved Objects*): guardar por separado la bolsa del "Kit prueba 1", la "Caja de fichas" y cada mazo terminado. Se reutilizan entre partidas.
- **Partida:** *Games → Save & Load → Save* con un nombre como "Día 30 · v0.1 · mesa montada". Conviene guardar una mesa armada para la prueba 1 y otra para el juego completo.

### 5.3 Workshop (para jugar con amigos)

1. Antes de subir, revisar que **ninguna URL sea local** (`file:///`). Cargar la partida, abrir un par de objetos y mirar sus campos.
2. **Modding → Workshop Upload:** título "Día 30 (prueba)", una descripción breve con el número de versión, una imagen de portada (`mano_del_suelo.jpg` o una captura de la mesa) y elegir la partida guardada.
3. En la página del Workshop en Steam, poner la visibilidad en **Solo amigos** u **Oculto**: es material de prueba, no se publica.
4. Para actualizar: *Workshop Upload →* elegir el ítem existente y **Update**. Los amigos suscriptos reciben la versión nueva. Anotar los cambios en la descripción.
5. **Para jugar:** el anfitrión crea un servidor (*Create → Multiplayer*, con contraseña o solo amigos) y carga el ítem del Workshop. Cada jugador se sienta en Orange, Green o Blue.

---

## 6. Herramienta: `herramientas/hoja_de_cartas.py`

Une imágenes sueltas en hojas válidas para un Custom Deck de TTS. Requiere Python 3.9 o superior y Pillow.

```bash
# Botín: solo caras únicas, en el orden y con las copias del manifiesto
python3 herramientas/hoja_de_cartas.py --manifiesto arte/manifiestos/botin.csv \
    --salida tts/cartas/botin/botin_v01 --oculta arte/cartas/botin/botin_dorso.png

# Variante con las 74 copias físicas en las hojas
python3 herramientas/hoja_de_cartas.py --manifiesto arte/manifiestos/botin.csv --expandir-copias \
    --salida tts/cartas/botin/botin_copias_v01 --oculta arte/cartas/botin/botin_dorso.png

# Una carpeta cualquiera, en orden alfabético, con la cuadrícula fijada a mano
python3 herramientas/hoja_de_cartas.py arte/cartas/supervivientes/ --cols 4 --filas 2 \
    --salida tts/cartas/supervivientes/supervivientes_v01
```

- **Qué hace:** elige la cuadrícula más compacta (como máximo 10 × 7) y reserva la última casilla para la carta oculta (el dorso, o un "?" genérico si no se le pasa ninguno). Si hacen falta varias hojas, reparte las cartas en partes iguales. Reduce las cartas si la hoja pasaría de `--max-lado` (4096 por defecto). Aplana la transparencia sobre papel y ajusta las imágenes que tengan otra proporción (`--ajuste cubrir|contener|estirar`).
- **Qué genera:** `<salida>_hoja_NN.jpg` (o `.png`) y `<salida>.json`. El JSON trae la cuadrícula, Width, Height y Number para el diálogo de TTS, y el orden de las cartas con su `card_id` (hoja × 100 + casilla) y sus copias.
- **Probado** con 33 imágenes de relleno y un manifiesto de 74 copias. Resultados:
  - Caras únicas: una hoja de 7 × 5, de 4095 × 4095 px, con cartas de 585 × 819.
  - Con copias: 2 hojas de 8 × 5 (37 + 37 cartas), de 4096 × 3580 px.
  - Con 2 cartas: una hoja de 2 × 2.
  - Cuadrícula fija de 4 × 3 en PNG: 3 hojas de 11 cartas.

  La carta oculta queda siempre en la última casilla.

---

## 7. Contradicciones y decisiones pendientes que afectan a los componentes

| Tema | Lo que dicen las fuentes | Efecto en TTS / propuesta |
|---|---|---|
| Botín: mazo o tabla | `cartas_de_objetos`: Registrar da una carta del mazo. `base_y_losetas`: Registrar tira d20 en la tabla del edificio | Hay que decidir uno. Si queda la tabla, el resultado dice qué carta buscar en el mazo (en TTS se busca con clic derecho, Search). Si queda el mazo, las tablas de edificio se reducen a los zombies |
| Señal | 5 etapas (`mesa_online` y cartas de señal) contra un contador "Señal 3/10" (`base_y_losetas`) | Se diseña la tira de 5 etapas. Hay que confirmar si existe el contador de 10 |
| Heridas | Kit: toda herida −1 de sangre, torso −1 extra. `mesa_online`: cabeza −3, torso −2. Cartas de objeto: "2 Medicinas quitan 1 **carta** de herida" | Decisión del autor: un solo tipo de herida, sin mordedura ni infección. Se usan las gotas sobre la silueta y no hay mazo de heridas. Falta unificar la pérdida de sangre por zona |
| Correr | Kit: 1 PA, 2 zonas. Carta de acción: 2 PA. Habilidad de Nico: "Correr le cuesta 1 PA en lugar de 2" | La carta de acción y la carta de Nico se rehacen después de la prueba 1 |
| Ruido del bate | Kit: Medio. Carta: barra 1 = Bajo. Tabla de la casa: "ruido bajo" | Hay que unificarlo antes de imprimir la carta |
| Munición | Kit: pistola con 6 balas. Cartas: 1 Munición = 3 disparos | En el kit, la pistola trae 6 fichas de bala |
| Mochila grande | Carta "Mochila de montaña": de 6 a 8. Tabla de la casa: "+2 espacios" | Coinciden. La hoja ya tiene 2 cuadros punteados |
| Nombres de personajes | `mesa_online`: Raúl Ibarra, Sofía Lenz, Nico Vidal. `base_y_losetas`: Julio Benítez, Sofía Paz, Nico Ferrer | Para las cartas se usa `mesa_online`, que tiene atributos |
| Cartas de acción | Solo está diseñada "Movimiento y sigilo" | Se reserva una hoja de 3 × 2 por jugador |
| Fichas: tinta o color | Pregunta abierta en la dirección de arte | Recomendación: color fuerte con borde de tinta (sección 3.9) |
| Infectado ácido y chillón | Marcados como "propuesta" | Se incluyen 4 fichas de cada uno. Son baratos de quitar |
| Nombre "Día 30" | La partida pasa a 20 días | El logo y los dorsos con el 30 rojo quedan pendientes. Antes de imprimir dorsos definitivos hay que confirmar el nombre |
| Mazo de aparición y prueba 1 | El kit usaba d6 de aparición. La decisión 8 lo reemplaza por el mazo | En el kit de TTS se usa el mazo a nivel 1. Si se quiere repetir la prueba 1 tal cual, alcanza con un d6 nativo suelto |
| Agua: limpiar heridas | Toda herida queda abierta (1 ruido por turno) hasta limpiarla con agua | **Cerrado:** la gota va en todas las heridas |

**Orden de trabajo sugerido:**
1. Kit prueba 1: 2 losetas, hoja, 7 cartas, caminantes y fichas básicas.
2. Mazo de botín, con las maquetas SVG actuales exportadas a PNG.
3. Mazo de aparición, cuando esté `mazo_aparicion.md`, y ficha de herida (gota).
4. Base, tiempo (20 días) y ciudad.
5. Losetas del juego completo y tablas de edificio.
6. Supervivientes y acciones, después de la prueba 2.
