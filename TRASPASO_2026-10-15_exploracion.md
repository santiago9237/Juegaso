# Día 30 · Traspaso: exploración, losetas hexagonales y zombies en grupo

Sesión de ideas del 15 de octubre de 2026 (rama `ccr-4ec1d393-fed8iq`). En esta sesión no se tocó el reglamento: solo se trabajaron ideas para pasarlas a la sesión del proyecto entero.

**Para la otra sesión:** este archivo junta todo lo que se decidió hoy. El registro fila por fila está en `diseno/ideas_de_santiago.md` (ideas 15 a 23). Las reglas redactadas para leer están en `manual/reglas_exploracion_v0.1.pdf`, que cubre solo las ideas 15 a 21. Las ideas 22 y 23 están solo en este archivo y en el registro.

Cómo leer las marcas:
- **Decidido:** lo decidió Santiago.
- **[PROPUESTA]:** lo propuso Claude para cubrir un hueco; Santiago no lo descartó, pero hay que probarlo.
- **Pendiente:** todavía no se decidió.

---

## 1. Resumen en una línea por idea

| # | Idea | Estado |
|---|---|---|
| 15 | Losetas hexagonales de 7 espacios que se agregan durante la expedición | Decidido |
| 16 | Símbolos en la loseta: zombies que aparecen y botín | Decidido (qué significa cada símbolo: [PROPUESTA]) |
| 17 | Acción **Mirar a lo lejos** (2 PA) y **entrar a ciegas** | Decidido (zombies tranquilos o alertas: [PROPUESTA]) |
| 18 | Objetos de exploración: binoculares, mapa y linterna | Decidido |
| 19 | Habilidades: Explorador/a, Sigiloso/a, Vendedor/a ambulante | Decidido |
| 20 | Zombies en grupo, una figura por grupo; combate con d10; resistencia según el tamaño; empuje; ataque conjunto | Decidido (números: [PROPUESTA]) |
| 21 | Un superviviente por hexágono; se puede atravesar; combate adyacente | Decidido |
| 22 | De noche los zombies tienen una activación extra o se mueven más lejos | Idea (falta elegir y probar) |
| 23 | Turnos de más horas, más PA por turno y nuevos costos; los días hasta el helicóptero se deciden al final | Idea para la prueba |

## 2. Mapa y losetas (idea 15)

- **Decidido:** el mapa se arma con **losetas hexagonales de 7 espacios**: un hexágono central y 6 alrededor. Cada hexágono es un espacio para moverse o pelear.
- **Decidido:** el barrio **no se arma antes de jugar**. Se empieza con una sola loseta y se van agregando durante la expedición.
- **Decidido:** al poner una loseta, tiene que tener sentido con el dibujo. Por ejemplo, no se puede cortar una calle con una casa.
- **[PROPUESTA] Encaje:** el lado compartido entre dos losetas son 3 bordes de hexágono, y la calle cruza siempre por el borde del medio. La regla es **calle con calle, fondo con fondo**. Si una loseta no entra en ningún lado, se descarta y se saca otra.
- Se descartó el hexágono de 1 espacio por pieza: obligaba a poner demasiadas piezas por turno.
- **Consecuencia:** hay que rehacer el arte y los prompts (`arte/prompts/losetas.md` describe todavía losetas cuadradas de 3 × 3 con puntos rojos).
- **Pendiente:**
  - cuántas losetas tiene cada barrio (podría depender del peligro);
  - qué pasa cuando se termina el mazo;
  - en qué loseta aparece la pieza de la señal de socorro.

## 3. Símbolos de la loseta (idea 16)

- **Decidido:** cada loseta tiene símbolos chicos que indican **cuántos zombies aparecen** cuando se da vuelta y **cuánto botín tiene**.
- **[PROPUESTA] Mano:** cada mano es 1 carta del mazo de aparición. Así la loseta avisa qué tan peligrosa es la zona, pero no exactamente cuántos zombies hay, y no se memoriza.
- **[PROPUESTA] Caja:** cada caja es 1 registro de botín.
- **[PROPUESTA] Marca de aparición:** una marca en un hexágono indica dónde se pone el grupo de zombies.
- **[PROPUESTA] Edificios:** los zombies de adentro de un edificio siguen saliendo al abrir la puerta (idea 13: mazo de zombies). Los símbolos de la loseta son solo de la calle.

## 4. Mirar a lo lejos y entrar a ciegas (idea 17)

- **Decidido:** **Mirar a lo lejos · 2 PA · silencio.** Ponés una loseta nueva **adyacente a la loseta donde estás**, girada como quieras, siempre que tenga sentido con el dibujo. Ves los zombies y los edificios y después decidís si vas.
- Se empezó con 1 PA y Santiago lo subió a **2 PA**: así ocupa casi todo el turno y entrar a ciegas se vuelve una opción real cuando hay apuro.
- **[PROPUESTA] Al mirar,** los zombies se ponen **tranquilos**.
- **[PROPUESTA] Entrar a ciegas:** moverte a un espacio sin loseta pone la loseta igual, pero los zombies aparecen **alertas**, y los que quedan adyacentes a vos te atacan antes de que sigas. Es la idea de Santiago de "cruzarse de frente con un zombie".
- **Relación con Vigilar:** es parecida (mira un edificio antes de entrar). Hay que ver si conviven o se unen.

## 5. Objetos de exploración (idea 18)

- **Binoculares (decidido):** Mirar a lo lejos revela **2 losetas** en vez de 1.
  - Pendiente: dónde va la segunda. [PROPUESTA] puede ir adyacente a la primera.
- **Mapa (decidido):** al encontrarlo revelás **3 losetas**.
  - [PROPUESTA] van conectadas a las que ya están, con sus zombies tranquilos.
- **Linterna (decidido):** de noche **no se puede mirar a lo lejos sin luz**. Con linterna sí se puede, pero los zombies de esa loseta aparecen alertas.
- **Descartados por Santiago:** radio de la policía, dron, perro, walkie-talkies.
- **Descartados también los "lugares del mapa"** (azotea, pintadas de supervivientes, carteles): suman complejidad.

## 6. Habilidades de exploración (idea 19, decidido)

- **Explorador/a:** Mirar a lo lejos le cuesta 1 PA.
- **Sigiloso/a:** cuando entra a ciegas, los zombies aparecen tranquilos.
- **Vendedor/a ambulante:** una vez por expedición, elige la loseta que se revela entre las 2 de arriba del mazo.
  - Reemplaza a "nacido/a en el barrio": como conoce todos los barrios, la habilidad sirve en cualquier mapa.

## 7. Zombies en grupo y combate (idea 20)

- **Decidido:** los zombies que aparecen juntos van en **una sola figura o ficha de grupo**, con su número (por ejemplo, un grupo de 3), y **se mueven juntos**. Así no se llenan los hexágonos de figuras.
- **Decidido:** los zombies **atacan como en Zombicide**, y un grupo grande hace mucho más daño.
  - [PROPUESTA] 1 herida por cada zombie del grupo.
- **Decidido:** **combate con d10** (en vez de d6). La tirada decide si acertás. Después, el **daño del arma** tiene que alcanzar la **resistencia** del zombie o del grupo. Un arma de daño 1, por ejemplo, no mata a un zombie blindado.
- **Decidido:** los grupos tienen **resistencia según su tamaño**. Si acertás y el daño alcanza la resistencia, **muere el grupo entero**. Si no alcanza, no le pasa nada.
  - Con una figura de grupo no se puede sacar un zombie ni dejar marcadores de daño, por eso no se acumula daño entre ataques.
- **Decidido · Empuje:** si acertás pero tu daño no alcanza, el grupo **retrocede 1 hexágono**.
- **Decidido · Ataque conjunto:** si dos jugadores están adyacentes al mismo grupo, pueden atacar juntos y **sumar el daño** de sus aciertos en esa misma tirada. Así se pueden matar grupos grandes.
- **Decidido:** más adelante se pueden agregar **armas especiales de daño 3**.
- **Decidido:** **la horda hace mucho daño** (cuánto, a determinar).
- **[PROPUESTA] Resistencia por tamaño:**

  | Tamaño | Resistencia |
  |---|---|
  | 1–2 | 1 |
  | 3–4 | 2 |
  | 5 (la horda) | 3 |

  Hoy ninguna arma tiene daño 3, así que la horda solo se mata con ataque conjunto (por ejemplo hacha 2 + cuchillo 1).
- **[PROPUESTA] Tipos de grupo:**
  - un grupo es de un solo tipo (el corredor se mueve 2 y el caminante 1);
  - bruto, chillón y blindado van solos y tienen su propia resistencia;
  - dos grupos del mismo tipo que caen en el mismo hexágono se juntan;
  - un grupo de 5 es una horda;
  - un grupo nunca se separa;
  - el estado (tranquilo o alerta) es del grupo entero.
- **[PROPUESTA] En TTS:** una ficha con estados del 1 al 5.
- **A actualizar:** `diseno/armas.md` está escrito con d6 y combate "en tu zona". Hay que pasarlo a d10 y a hexágonos adyacentes.

## 8. Ocupación de hexágonos y movimiento (idea 21, decidido)

- **No puede haber dos supervivientes en el mismo hexágono.**
- Se puede caminar **atravesando** a otro jugador o a un zombie.
- **Los combates son entre hexágonos adyacentes.**
- **Pendiente:**
  - alcance de pistola, escopeta y rifle en hexágonos;
  - si en un hexágono puede haber más de un grupo de zombies;
  - qué pasa con el empuje si el hexágono de atrás está ocupado o no tiene loseta.

## 9. La noche (idea 22)

- **Idea de Santiago:** cuando se hace de noche, los zombies tienen **una activación extra** o **se mueven más lejos**. Todavía no eligió.
- **Lo que ya dice el reglamento:**
  - anochece a las 19:00;
  - de noche se roban 2 cartas de aparición;
  - el corredor nunca está tranquilo;
  - disparar es con desventaja.
- **[PROPUESTA] +1 de movimiento de noche:** el caminante se mueve 2 y el corredor 3.
  - Es más simple y no alarga la partida.
  - Con la activación extra, cada grupo ataca dos veces (un grupo de 3 pegaría 6 heridas) y la fase de zombies dura el doble.
  - Si en la prueba la noche no asusta lo suficiente, se puede probar la activación extra solo para los grupos alertas.
- **Pendiente: medirlo en la prueba.** Cuántas horas dentro del juego dura una expedición y cuántos minutos reales. Hoy 1 turno es 1 hora, y la expedición va de 07:00 a 21:00, con unos 10 turnos de día y 2 de noche. Para medirlo sirve anotar en cada expedición:

  | Expedición | Turnos de día | Turnos de noche | Losetas reveladas | Minutos reales | ¿Llegó la noche? ¿Qué pasó? |
  |---|---|---|---|---|---|
  | 1 | | | | | |
  | 2 | | | | | |
  | 3 | | | | | |

  Como la partida apunta a unas 2 horas y dura 20 días, sirve dividir: si cada expedición tarda más de unos 5 minutos reales, hay que acortar los días o hacer que no todos los días haya expedición.

## 9 bis. Tiempo y puntos de acción (idea 23)

- **Idea de Santiago:**
  - probar **turnos de más horas** del juego;
  - **más PA por turno**;
  - ajustar cuántos PA consume cada actividad.
- **Para qué:** con más PA se puede balancear mejor cuántos PA quita la **fatiga** y las ventajas y desventajas por **horario, clima, heridas**, etc.
- **Decidido:** **los días hasta el helicóptero se deciden al final**, cuando todas las mecánicas estén pulidas. Los 20 días de la idea 6 quedan provisorios.
- **Contexto:** un turno de Zombicide tarda unos 5–10 minutos reales con 4–6 supervivientes. Con 3 acciones por superviviente, un turno de Día 30 andaría en 3–5 minutos reales. Una expedición de 12 turnos serían entonces 40–60 minutos, así que hay que medirlo en la prueba.
- **[PROPUESTA]:**
  - 6 PA por turno de 2 horas;
  - los costos actuales ×2 (caminar 2, mirar a lo lejos 4);
  - modificadores de ±1 PA por fatiga, noche, lluvia o heridas.

  Con números más grandes, una sola desventaja no te deja sin turno.

## 10. Lo que estas ideas cambian en el proyecto

Secciones del reglamento y archivos que van a necesitar cambios cuando se pasen las ideas:

- **Mapa y barrio:** plantilla del barrio, entrada por la flecha, la hoja de base que arma el mapa sola. Pasa a exploración loseta por loseta.
- **Movimiento:** "solo horizontal y vertical, nunca en diagonal" deja de hacer falta con hexágonos. Zonas pasa a hexágonos.
- **Ruido:** la propagación zona por zona pasa a hexágono por hexágono. Además hay que ver qué es "la loseta más ruidosa", porque ahora las losetas son de 7 espacios.
- **Aparición:** el mazo de aparición se usa también al revelar losetas (manos). Los errantes siguen como estén.
- **Combate y armas:** d10, resistencia, grupos, empuje, ataque conjunto, adyacencia.
- **Acciones:** sumar Mirar a lo lejos y revisar Vigilar.
- **Arte:** `arte/prompts/losetas.md` y `herramientas/puntos_loseta.py` son del sistema cuadrado.

## 11. Imágenes de referencia (en `arte/img/`)

| Archivo | Qué muestra |
|---|---|
| `idea_loseta_cuadrada_vs_hexagonos.png` | Primera comparación: loseta cuadrada con grilla sutil contra un hexágono por espacio |
| `idea_exploracion_por_turnos.png` | Exploración en 3 turnos: hexágonos de 7 contra cuadradas de 3 × 3 |
| `idea_mirar_a_lo_lejos.png` | Mirar a lo lejos (2 PA) contra entrar a ciegas, con los símbolos de la loseta y el ataque desde un hexágono adyacente. Muestra zombies sueltos, no fichas de grupo |
