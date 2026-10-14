# Día 30 · Traspaso de la sesión en la nube

Resumen de todo lo trabajado en la sesión de Claude Code en la nube del 14 de octubre de 2026, para continuar en la sesión local. Todo lo que figura acá está en este repositorio (`santiago9237/Juegaso`, rama `claude/tabletop-simulator-board-game-wx5e3u`).

**Para la sesión local:** leé este archivo primero. Después, según la tarea: `diseno/ideas_de_santiago.md` (decisiones del autor), `manual/manual.html` (reglas al día), `arte/prompts/` (prompts de imágenes) y `herramientas/` (scripts).

---

## 1. El juego

- **Día 30** (nombre provisorio; se decide al final). Cooperativo de supervivencia zombie, 1 a 3 jugadores, unas 2 horas, para probar en Tabletop Simulator (TTS).
- El grupo vive en una casa en la calle Las Heras y tiene que armar una **señal de socorro de 5 etapas** antes de que pase el helicóptero.
- Cada día: **Base → Planificación → Expedición → Regreso y noche**.
- Eje central: el **ruido**. Rápido y fuerte hace ruido; el ruido atrae zombies y, acumulado (5 fichas), trae la horda.
- Estilo de arte: **tinta sobre papel envejecido**, dirección C "papel en la oscuridad". Paleta: noche #16191D, papel #D8C8A6, tinta #1B1A17, óxido #B4583A, rojo 30 #922B2B, luna #D9B45A, verde radio #2E7D6B, ácido #9BD14B. Fuentes: Big Shoulders Stencil Display (títulos), Barlow Condensed (interfaz), Special Elite (notas). Las fuentes están en `arte/fuentes/`.

## 2. Decisiones de Santiago (firmes)

Registro completo en `diseno/ideas_de_santiago.md`.

| # | Decisión |
|---|---|
| 1 | **Acciones pesadas → fatiga.** Forzar puerta y otras acciones pesadas (▲) dejan marcas de esfuerzo; se acumulan y dan fatiga. |
| 2 | **Alimento único.** Comida y agua cuentan igual para las **raciones**; cada carta tiene su nombre y da 1 o más raciones. |
| 3 | **El agua limpia heridas.** Una herida sin limpiar atrae zombies (1 ficha de ruido por turno). |
| 4 | **Voseo** rioplatense en todo el material. |
| 5 | **Duración ~2 horas.** |
| 6 | **20 días** (antes 30), con **descanso rápido** opcional: pasa el día pero sube la dificultad. |
| 7 | **Nivel de peligro** en 3 tramos: días 1–7, 8–14, 15–20. |
| 8 | **Mazo de zombies (aparición)** después del turno de los jugadores; cada carta tiene tipo y 3 cantidades según el nivel de peligro. Reemplaza los d6. También se usa al entrar a un edificio. |
| 9 | **Un solo tipo de herida** (sin rasguño, laceración, fractura). |
| 10 | **Sin mordida ni infección** (nada estilo Project Zomboid). |
| 11 | **Mazos separados:** alimentos, eventos, materiales, armas y munición, zombies, supervivientes (+ medicina, objetos de señal y equipo propuestos). Cada "robá una carta" dice de qué mazo. |
| 12 | **Raciones:** se descartan al consumir y el descarte se vuelve a mezclar. |
| 13 | Zombies al entrar a un edificio: se roban del mazo de zombies. |
| 14 | **Rebuscar:** una tirada de dado decide de qué mazo se roba. |
| 15 | El nombre del juego se decide al final. |

### Decisiones de esta sesión, todavía SIN confirmar por Santiago

- **Combate estilo Zombicide** (propuesto, Santiago lo usó como base al definir armas): d6 por ataque, cada acierto mata a un zombie si el daño alcanza su dureza (caminante, corredor, chillón, ácido 1; bruto 2). Los zombies pegan automático: 1 herida por zombie en tu zona (bruto 2). Detalle en `diseno/armas.md`.
- **Armas** (Santiago definió la lista y los alcances; los números son propuesta): ver tabla en `diseno/armas.md`.

  | Arma | Dados | Acierta | Daño | Alcance | Ruido | Espacios |
  |---|---|---|---|---|---|---|
  | Cuchillo | 1 | 4+ | 1 | Tu zona | Silencio | 1 |
  | Bate | 2 | 4+ | 1 | Tu zona | Bajo | 2 ▲ |
  | Hacha | 1 | 3+ | 2 | Tu zona | Medio | 2 ▲ |
  | Escopeta | 3 | 4+ | 1 (2 en tu zona), hasta 3 zombies | 0–1 | Máximo | 2 |
  | Pistola | 1 | 3+ | 1 | 0–2 | Máximo | 1 |
  | Rifle | 1 | 3+ | 2 | 1–3 (5+ en tu zona) | Máximo | 2 |

- **Hoja de personaje** pedida por Santiago: horizontal, mochila al medio con espacio para cartas, **sangre 15** (gota), **hambre 5** (comida), **fatiga 3** (esfuerzo), lista de acciones abajo. Prompt en `arte/prompts/hoja_de_personaje.md`.
  - **Preguntas abiertas:** las reglas usan 6 de sangre; con zombies que pegan automático, 15 encaja, pero falta confirmarlo. El **medidor de hambre (0–5)** no existe en las reglas: hay que definir cómo sube (¿+1 por noche sin raciones?) y qué efecto tiene cada nivel.

## 3. Archivos del repositorio

| Ruta | Qué es |
|---|---|
| `fuentes/` | Copias de los 7 artefactos de claude.ai de donde salió el diseño (kit de la prueba 1, simulador, base y losetas, cartas de objetos, mesa en línea, sala de juego, dirección de arte). `README.md` los explica. |
| `diseno/ideas_de_santiago.md` | Registro de las decisiones del autor. |
| `diseno/reglamento.md` | Reglamento unificado **v0.3** (del agente de Mecánicas). **Desactualizado:** 30 días, 4 tipos de herida e infección. La v0.4 quedó a medio hacer. |
| `diseno/ideas.md` | Ideas v2: mazo de eventos (28 cartas Amanecer/Calle/Noche), arco de 20 días, hitos, clímax "La última noche", supervivientes con habilidad y defecto, rescatados, zombies, barrios, ganchos de TTS, top 10. Ya en 20 días, voseo y sin infección. |
| `diseno/mazo_aparicion.md` | Mazo de zombies: 37 cartas con cantidades por nivel y promedios. |
| `diseno/componentes_tts.md` | Plan de componentes para TTS v0.2: inventario, medidas, plantillas y disposición de la mesa. |
| `diseno/revision.md`, `diseno/revision_reglamento.md` | Revisiones de errores y contradicciones (de las fuentes y del reglamento v0.3). |
| `diseno/armas.md` | Armas con combate d6 (propuesta). |
| `manual/Dia30_manual_v0.4.pdf` y `manual/manual.html` | **Manual v0.4**: 21 páginas con arte, aplica todas las decisiones hasta los mazos separados. Es la versión más al día de las reglas, salvo el combate d6, las armas nuevas, la sangre 15 y el hambre. |
| `arte/img/` | Ilustraciones: 5 zombies, portada (mano del suelo), carta de acción, dorso, fichas. |
| `arte/prompts/hoja_de_personaje.md` | Prompt para ChatGPT de la hoja de personaje. |
| `arte/prompts/losetas.md` | **Sistema de losetas v2** y prompts (ver sección 4). |
| `arte/prompts/miniaturas.md` | Prompts de miniaturas estilo Zombicide (10 supervivientes + 5 zombies) para pasar después a 3D con Tripo3D o Meshy. |
| `herramientas/hoja_de_cartas.py` | Arma hojas de cartas para TTS desde imágenes sueltas (cuadrícula de hasta 10×7, carta oculta, JSON para importar). |
| `herramientas/puntos_loseta.py` | Pone los 9 puntos rojos exactos en una loseta (`--todos`, `--zonas A1,B2`, `--losetas 2x2`). |
| `herramientas/modelos_3d.py` | Genera los modelos 3D provisorios. |
| `herramientas/simular_prueba1.py`, `combate.py`, `economia.py`, `noche.py` | Scripts del agente de Balance (sin terminar; usan las reglas viejas). |
| `modelos/` | 15 modelos 3D para TTS (OBJ + PNG + collider): 5 zombies como figuras de cartón con su ilustración, 10 supervivientes low-poly provisorios. `LEEME.md` explica cómo cargarlos. Vista previa: `modelos/vista_previa.png`. |

## 4. Sistema de losetas (v2, decidido por Santiago)

- Loseta cuadrada, grilla invisible de 3×3 zonas, 1500×1500 px para TTS.
- **La misma calle en todas:** columna del medio, vertical, de borde a borde, tocando arriba y abajo en el tercio del medio. Girando 90° se arman calles horizontales. Se pueden sumar losetas de cruce y de T con la misma calle.
- **Siempre 9 puntos rojos**, uno en el centro de cada zona, sin dibujar la grilla.
- **Columnas laterales:** baldíos, casas (3 habitaciones apiladas, una por zona, con la puerta a la vereda) o edificios especiales (farmacia, comisaría, supermercado, hospital: el edificio ocupa una columna y la otra es su anexo).
- Prompts listos en `arte/prompts/losetas.md`. Se pega primero el mensaje de reglas fijas, con la loseta de referencia adjunta, y después un mensaje por loseta.
- Si ChatGPT corre los puntos, se pide la loseta sin puntos y se corre `herramientas/puntos_loseta.py ... --todos`.

## 5. Mazo de cartas que armó Santiago (`mazo1.tsdb`)

Archivo de su programa de mazos, con imágenes en `C:\Users\santiago\Desktop\JUEGASO\imagenes nuevas\`. Hoja de 10×7, cartas de 1060×1484 px, 69 cartas:

| Tipo | Cartas | Tipo | Cartas |
|---|---|---|---|
| Agua | 8 | Vendas | 6 |
| Cantimplora | 5 | Analgésico | 4 |
| Barra proteica | 7 | Botiquín | 3 |
| Vegetales | 6 | Combustible | 5 |
| Carne | 5 | Mochila | 2 |
| Energizante | 4 | Generador | 1 |
| Lata vacía | 6 | GPS | 1 |
| Botella vacía | 6 | | |

**Problemas detectados:** mezcla varios mazos en uno (contradice los mazos separados); 12 cartas vacías sin regla; faltan la radio (etapa 1, sin ella no se gana), la bengala y el manual; no hay armas ni materiales de construcción.

**Propuesta sin confirmar:**
- **Alimentos (36):** agua 7 (1 ración, limpia herida), cantimplora 4 (2, limpia herida), barra 7 (1), vegetales 6 (1), carne 4 (2), energizante 4 (1, borra esfuerzo), lata vacía 2 (basura), botella vacía 2 (se rellena en la base y pasa a ser agua).
- **Medicina (12):** vendas 6, analgésico 4, botiquín 2.
- Combustible → Materiales (5). Mochila → Equipo (2).
- **Señal (6):** generador 1, GPS 1, más radio 1, manual 1 y bengala 2, que faltan.

## 6. Tabletop Simulator: notas prácticas

- **Custom Tile** con imágenes distintas no se apila. Para mezclar losetas: meterlas en una **Bag** (clic derecho → Shuffle) o hacerlas como **Custom Deck** de cartas cuadradas y escalarlas.
- Para armar el mapa: **Grid** con el tamaño de la loseta + Snapping; bloquear con L.
- Imágenes: cartas de 750×1050 o la medida propia, hojas de hasta 10×7 y 4096 px de lado, JPG. Versión en el nombre del archivo (TTS guarda en caché). Subir a la Steam Cloud para jugar online.
- Se puede generar un archivo de partida guardada (`.json` en `Documentos/My Games/Tabletop Simulator/Saves`) con todo armado, si se conocen las URLs o rutas de las imágenes.

## 7. Herramientas externas

- **ChatGPT** para imágenes. Desde la sesión local se puede usar con Claude in Chrome. Otra opción: la API de OpenAI con `OPENAI_API_KEY` como secreto del entorno y `api.openai.com` permitido en la red.
- **Tripo3D, Meshy o Rodin** para pasar imágenes de miniaturas a 3D (exportar OBJ con textura, 10 000–30 000 polígonos).
- Artefactos de claude.ai con el material original: Kit de prueba 1, Prueba 1, Dirección de arte, Sala de juego, Mesa, Base y losetas, Cartas de objetos (copias en `fuentes/`).

## 8. Pendientes, en orden sugerido

1. Confirmar con Santiago: **combate d6 y armas**, **sangre 15** y **medidor de hambre** (definir reglas).
2. Reescribir el **reglamento v0.4** con todas las decisiones (base: el manual v0.4 + combate d6 + armas + hoja de personaje). Actualizar el manual.
3. Revisar con números la **tabla de Rebuscar** y los **valores de raciones** (propuestos por la coordinación, sin revisión de Balance).
4. Separar `mazo1` en mazos y crear las cartas que faltan (radio, bengala, manual, armas, materiales).
5. Generar las losetas con los prompts v2 y ponerles los puntos.
6. Generar la hoja de personaje.
7. Miniaturas 3D con IA (prompts listos) para reemplazar los modelos provisorios.
8. Armar un archivo de partida de TTS con todo.
9. Pendientes de diseño: duración real (10–12 turnos por expedición: ¿entra en 2 h?), zonas del cuerpo con la herida única, ataque nocturno, espiral de fatiga y hambre, cartas de evento finales, arte de las cartas en tinta y papel, nombre del juego.
