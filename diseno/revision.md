# Día 30: revisión de errores, contradicciones y huecos

Revisión de todo el material de `fuentes/` (14 oct 2026): README, kit de prueba 1, simulador (con su JS), base y losetas (con su JS y tablas), cartas de objetos, mesa online, sala de juego y dirección de arte.

**Qué se comprobó con cálculo:**
- Las 10 tablas de botín d20 cubren del 1 al 20 sin huecos ni solapes.
- Todas las tablas de ficha tienen 6 filas.
- La tabla de errantes cubre del 1 al 6.
- El mazo suma exactamente 74 cartas: medicina 10, comida 15, agua 8, armas 7, recursos 20, señal 4 y equipo 10. Los materiales son 13 en 6 tipos, como dice la nota.
- Los 7 supervivientes suman 12 puntos de atributo cada uno, igual que el personaje neutro del kit (3/3/3/3).
- La probabilidad de que un caminante te acierte (d20+2 contra 11) es 60 %, como dice el kit.

**Leyenda de gravedad:**
- **Alta:** rompe una partida o deja dos versiones incompatibles de una regla central.
- **Media:** genera dudas en la mesa o un resultado distinto según quién lea.
- **Baja:** texto, coherencia menor o detalle de implementación.

---

## Resumen rápido de las contradicciones principales

| Tema | Kit prueba 1 | Simulador | Cartas / tablas | Mesa / sala / arte |
|---|---|---|---|---|
| Sigilo | 2 PA, 1 zona | 2 PA | — | Carta: 1 PA |
| Correr | 1 PA, 2 zonas, 1 vez por turno | 1 PA, 1 o 2 zonas | — | Carta: 2 PA "hasta 2 zonas". Estudiante: "1 PA en lugar de 2" |
| Caminar | 1 PA, ruido bajo | Igual | — | No existe en la carta |
| Vendar / curar | 2 PA, solo laceración | 2 PA | Medicina: 1 PA (vendar, entablillar, rasguño) | Enfermera: "1 PA en lugar de 2" |
| Bate | d6+Fuerza, ruido medio, 2 espacios | d6+1, medio, 2 | Carta: d6, ruido bajo, 2 espacios. Tablas: d6, ruido bajo, **1 espacio** | — |
| Cuchillo | d4 **+ Fuerza** de daño | d4+1 | d4 (la Fuerza solo suma al impacto) | — |
| Sangre por herida | 1 por herida; torso +1; cabeza aturde | Igual | Medicina habla de "carta de herida" | Mesa: cabeza **−3**, torso **−2**, resto **0** |
| Muerte por cabeza | 2.ª herida en la cabeza | Igual (incluye rasguños) | — | La mesa no permite 2 heridas en una zona |
| Señal | — | — | Etapas 1, 2, 3 (bengalas), 4 | Mesa: 5 etapas. Base: "señal 3/**10**" |
| Recursos de la base | — | — | Base: comida, agua, medicinas y 7 materiales. Cartas: munición y combustible aparte | Mesa: comida, agua, materiales, medicinas, munición y combustible |

---

## Gravedad alta

### A1. Los costes de movimiento no coinciden entre el kit, la carta y una habilidad
- **Dónde:**
  - `kit_prueba_1.md` → "Sigilo \| 2 \| Silencio", "Correr \| 1 \| Medio \| Te mueves 2 zonas. Una vez por turno".
  - `direccion_de_arte.html` → carta "Movimiento y sigilo": "Sigilo 1 PA", "Correr 2 PA · Te mueves hasta 2 zonas". La muestra de tipografía también dice "Correr · 2 PA · Ruido medio".
  - `mesa_online.html` → Estudiante: "Correr le cuesta 1 PA en lugar de 2".
- **Qué está mal:**
  - El kit ya avisa que cambia la carta, pero la carta, la muestra tipográfica y la habilidad del Estudiante siguen con los valores viejos.
  - Con las reglas del kit, Correr ya cuesta 1 PA, así que la habilidad del Estudiante no hace nada.
  - La carta tampoco tiene Caminar, y trae Huir y Vigilar, que el kit no tiene.
- **Propuesta:**
  - Cerrar la decisión cuando haya datos de la prueba 1.
  - Si se adopta el kit, actualizar la carta (Sigilo 2 / Caminar 1 / Correr 1) y la muestra tipográfica.
  - Rehacer la habilidad del Estudiante, por ejemplo "Correr 3 zonas" o "puede Correr dos veces por turno".

### A2. Las heridas y la sangre funcionan distinto en el kit y en la mesa
- **Dónde:**
  - `mesa_online.html` → `SANGRE_POR_ZONA = { cabeza: 3, torso: 2 }` y `g.heridas[zona] = ahora` (una sola herida por zona).
  - `kit_prueba_1.md` → "Toda herida resta 1 de sangre", "Torso: pierdes 1 sangre extra", "Mueres si … recibes una segunda herida en la cabeza".
- **Qué está mal:**
  - En la mesa, una herida en la cabeza quita 3 de sangre y una en el brazo o las piernas no quita nada.
  - En el kit, cualquier herida quita 1, el torso quita 2 y la cabeza 1 más aturdimiento.
  - La mesa no puede anotar dos heridas en la misma zona. Así no se puede aplicar la muerte por segunda herida en la cabeza, y una nueva herida reemplaza a la anterior.
  - La mesa tampoco aplica sangrado por laceración.
  - La carta Medicina habla de "carta de herida", que no existe en ningún otro documento.
- **Propuesta:**
  - Elegir un solo modelo; el del kit es el que se está probando.
  - En la mesa, guardar una lista de heridas por zona y aplicar −1 general, −1 extra en torso y muerte en la segunda herida de cabeza.
  - Decidir si las heridas son cartas o anotaciones en la hoja, y corregir el texto de Medicina en consecuencia.

### A3. Hay dos sistemas de botín incompatibles: tablas d20 por edificio y mazo de 74 cartas
- **Dónde:**
  - `base_y_losetas.html`: "Cada Registrar … tira d20 en su tabla de botín", con 10 tablas.
  - `cartas_de_objetos.html`: "Lo que sale al usar Registrar en un mueble", con 74 cartas.
- **Qué está mal:**
  - No se dice cómo conviven los dos sistemas.
  - Muchos resultados de las tablas no tienen carta: Tonfa, Martillo, Llave inglesa, Bisturí, Motosierra, Botella incendiaria, Bate de sóftbol, Linterna, Chaleco antibalas, Palanca, Soplete, Camilla plegable, Fósforos y velas, Megáfono, Mapa de rutas, Mapa escolar, Libreta de fiado, Kit de sutura, Batería de auto, Antena y cable coaxial, Desinfectante, Antibióticos, Analgésicos y Férula.
  - Las cantidades no encajan con "1 carta = 1 unidad = sus espacios":
    - "Vendas ×2" ocupa [1] espacio.
    - "Agua ×3" y "agua ×4" ocupan [2].
    - "Combustible ×2" ocupa [2], pero la carta de combustible ocupa 2 por unidad.
    - "Chapa ×2" ocupa [2], pero la carta ocupa 2 por unidad.
    - "Clavos ×2" y "alambre ×2" ocupan [1].
    - "Munición ×2" ocupa [1].
    - "Antibióticos ×3" ocupa [1].
  - El mazo tiene 1 escopeta y 1 pistola, pero las tablas pueden dar varias de cada una.
- **Propuesta:** elegir una de dos opciones.
  - (a) La tirada d20 dice qué familia y cuántas cartas se roban del mazo.
  - (b) Las tablas son la fuente de verdad y el mazo se rehace a partir de ellas.
  - En los dos casos, cada objeto de las tablas tiene que tener carta (o anotación) y los espacios se cuentan por unidad.

### A4. La señal de socorro y la condición de victoria están indefinidas o se contradicen
- **Dónde:**
  - `mesa_online.html` → `ETAPAS` (5 etapas): "Baliza o fuego de señal" y "Activación · Ruido máximo".
  - `base_y_losetas.html` → `señal ${S.senal}/10` y "Señal 3/10".
  - Tablas → "Bengalas ×2: etapa 3 de la señal" (comisaría) y "bengala ×1: etapa 3" (estación de servicio).
  - `cartas_de_objetos.html` → la Bengala es Equipo y solo dice "Úsala con la acción Distraer".
  - "Generador", esp 2 (carta), frente a "Generador portátil/de emergencia", [4] (tablas).
  - Mesa, sala y arte: "El helicóptero llega el día 30".
- **Qué está mal:**
  - La base cuenta la señal sobre 10 y el resto sobre 5 etapas.
  - La carta Bengala no menciona la etapa 3.
  - El generador ocupa 2 espacios en la carta y 4 en las tablas.
  - La etapa 5 no tiene ni objeto ni regla.
  - No se dice qué pasa si el día 30 la señal está incompleta, si completarla antes adelanta el rescate, ni cuál es la condición de derrota del juego completo (¿muerte de todos?, ¿de uno?).
  - La radio "necesita Baterías para usarse" y la batería dura "1 día", pero no se dice si la radio tiene que estar encendida todos los días hasta el 30.
  - Lo mismo con el generador: "Mantiene el generador encendido 1 día".
- **Propuesta:**
  - Fijar 5 etapas y corregir la base a "x/5".
  - Añadir "Etapa 3" a la carta Bengala o retirarlo de las tablas.
  - Unificar los espacios del generador.
  - Escribir la regla de victoria y derrota, y el mantenimiento (o no) de la radio y el generador.

### A5. Daño y ruido de las armas distintos en cada documento
- **Dónde:**
  - Kit: "Bate \| 2 \| d6 + Fuerza \| Medio" y "Cuchillo \| 1 \| d4 + Fuerza".
  - Carta "Bate con clavos": ruido 1 (Bajo), esp 2.
  - Tablas: "Bate · d6 · ruido bajo" [1] y "Cuchillo de cocina · d4".
  - Carta Cuchillo: "Ataca con d20 + Fuerza", con daño solo d4.
- **Qué está mal:**
  - El bate es medio o bajo según el documento, y ocupa 1 o 2 espacios.
  - En el kit la Fuerza suma al impacto **y** al daño; en las cartas solo al impacto.
  - "d4 + Fuerza" no aclara si es el valor (3) o el modificador (+1). El simulador usa +1.
  - La regla de pifia (+1 ficha de ruido) solo aparece en la carta del bate, como si fuera exclusiva de esa arma.
- **Propuesta:**
  - Un solo valor por arma en todos los documentos.
  - Escribir "d4 + modificador de Fuerza" si se mantiene el daño con Fuerza.
  - Mover la pifia a la regla general de combate.

### A6. Falta la equivalencia entre turnos de 3 PA y el reloj de horas del juego completo
- **Dónde:**
  - Kit: turnos de 3 PA, noche desde el turno 9.
  - `base_y_losetas.html`: reloj de horas (08:00, anochece a las 19:00), "Cada vez que el reloj avanza una hora, se tira 1 d6" de errantes.
  - Registrar sigue costando "2 PA".
- **Qué está mal:**
  - No se dice cuántos turnos o PA son una hora, cuántas horas consume registrar o moverse por una loseta, ni cómo se pasa del reloj de 12 turnos al de horas.
  - Las losetas no tienen regla de horda: no hay umbral de fichas ni lugar de llegada. Los errantes la reemplazan solo en parte.
- **Propuesta:** definir "1 hora = N turnos de 3 PA" (o una ronda de todos los jugadores), y llevar al juego completo la horda del kit o descartarla explícitamente.

### A7. El simulador no revela la farmacia ni la casa si un zombie rompe la abertura
- **Dónde:** `prueba_1_simulador.html`.
  - `revealFarm` solo se llama dentro de `doAct` (acciones del jugador).
  - `revealCasa` solo con `a.k==='abrir'` sobre `'7-13'`.
  - En la fase de zombies: `S.edges[k]='broken'`.
- **Qué está mal:**
  - Si un caminante derriba la puerta principal, la vidriera o la puerta de la casa, el jugador entra sin que se tire la ficha. La farmacia queda sin zombies, con botín normal y con la entrada "No entró" en el registro.
  - Esto cambia los resultados de la prueba.
  - El kit tampoco lo resuelve: solo dice "La primera vez que abres una abertura".
- **Propuesta:**
  - Regla: "La ficha se tira la primera vez que una abertura del edificio queda abierta, la abras tú o un zombie, o cuando entras por primera vez".
  - En el código, llamar a `revealFarm`/`revealCasa` cuando un zombie rompe la abertura, o al entrar en una celda del edificio.

---

## Gravedad media

### M1. Diferencias entre el kit y lo que hace el simulador
Todas en `prueba_1_simulador.html`. Si el simulador es "la implementación exacta" (README), el kit debería recoger estas reglas, o el código adaptarse al kit.

| # | El kit dice | El simulador hace | Propuesta |
|---|---|---|---|
| a | Los efectos de zona de una laceración, mordedura, etc. no tienen duración; "Fractura: dura hasta el final" sugiere que los demás son temporales | `effect()` cuenta toda herida que no sea rasguño, también laceraciones vendadas: **todo efecto de zona es permanente** | Decidir: el efecto termina al vendar (laceración) o al final de la expedición (fractura), o todos permanentes. Ver M7 |
| b | Mordedura "cuenta como derrota diferida" | Resultado "Victoria con mordedura" | Anotarla como derrota en el registro, o cambiar el kit |
| c | Los zombies "no abren puertas…; frente a una puerta cerrada tiran d6" | También derriban la **vidriera intacta** y la **puerta con llave** (las trata igual, con peso 4 en el camino) | Decir en el kit si la vidriera y la puerta trasera pueden caer con un 6 |
| d | "Rodean por la abertura más cercana" | `stepToward` prefiere golpear una puerta si rodear cuesta más de 4 pasos | Fijar la regla: siempre rodean si hay camino, o golpean si el desvío es mayor que X |
| e | No hay acción Cerrar puerta | "Cerrar puerta · 1 PA · ruido bajo" | Añadirla al kit (es clave para el refugio de la casa) o quitarla |
| f | Un zombie pasa a alerta "cuando te detecta o se mueve hacia tu ruido" | También pasa a alerta cuando lo atacas, aciertes o falles, y pierde la ventaja | Añadirlo al kit: "Un zombie atacado queda alerta" |
| g | No dice qué pasa con ventaja y desventaja a la vez | Se anulan | Añadirlo al kit |
| h | "Segunda herida en la cabeza" (y "rasguño: sin efecto de zona") | Cuenta los rasguños en la cabeza para la muerte | Decidir si un rasguño en la cabeza cuenta |
| i | Ruido: baja 1 nivel al atravesar "una pared o una puerta cerrada" | También baja en la **vidriera intacta**, y el alcance se recalcula con el nivel ya reducido (por ejemplo, Medio tras una pared llega a 1 zona total, no a 2) | Escribirlo así en el kit o cambiar el código |
| j | Aparición: "1-2 fila 1, 3-4 columna F, 5-6 fila 3" | Columna F = solo F1/F3 (excluye F2, que es el depósito); fila 3 excluye A3 (la base); la zona exacta dentro de la fila se elige al azar | Ver M10 |
| k | Noche "desde el turno 9: la aparición ocurre con 1 o 2" | La tirada del final del turno 8 ya usa la probabilidad nocturna | Aclarar en qué reloj se aplica |
| l | Correr: "Te mueves 2 zonas" | Permite 1 o 2 zonas | Aclarar "hasta 2" |
| m | Material: 10 zombies | Zombies sin límite | Ver M11 |
| n | El jugador elige a qué zombie ataca | Siempre ataca al más dañado de la zona | Baja; dejar elegir |

### M2. Nombres y cantidades de recursos distintos en cada documento
- **Dónde:**
  - Mesa: `RECURSOS` = comida, agua, **materiales** (genérico), medicinas, **munición**, combustible.
  - Base: comida, agua, medicinas + madera, clavos, chapa, alambre, cuerda, **combustible**, semillas (combustible cuenta como material; no hay munición).
  - Cartas: "Recursos" = munición + combustible + 6 materiales ("13 repartidas en seis tipos", sin combustible).
- **Qué está mal:**
  - Ningún resultado de las tablas da "medicinas": dan vendas, desinfectante, analgésicos, antibióticos y botiquines.
  - La mesa no puede llevar materiales por tipo, que la base necesita para construir.
- **Propuesta:** lista única de recursos de la base (por ejemplo: comida, agua, medicina, munición, combustible, madera, clavos, chapa, alambre, cuerda, semillas), usada igual en mesa, base y cartas.

### M3. Recursos y estados sin consumo o sin consecuencia
- **Agua:**
  - "Consumo diario por definir (sección 12)" (cartas) y "El agua sigue sin consumo definido".
  - La base calcula el consumo solo de comida.
  - La sección 12 del reglamento no está en las fuentes.
- **Comida:** no se dice qué pasa si falta.
- **Fatiga:**
  - Va de 0 a 3, pero solo se gana cavando la fosa y se quita descansando.
  - No se dice qué la produce en expedición ni qué pasa al llegar a 3. `cavador()` evita llegar a 3 sin que haya una regla que lo explique.
- **Constitución:** atributo sin ningún uso en ningún documento. La sangre es fija en 6.
- **Propuesta:**
  - Definir el consumo de agua (por ejemplo, 1 por superviviente y día).
  - Escribir los efectos de pasar hambre o sed y de llegar a fatiga 3.
  - Dar uso a Constitución (sangre máxima = 3 + Con, o tiradas de infección).

### M4. Supervivientes: nombres, atributos, cómo se eligen y cuántos hay en el grupo
- **Dónde:**
  - Base: "Julio Benítez · Ex policía", "Sofía Paz · Mecánica", "Nico Ferrer · Estudiante".
  - Mesa: "Raúl Ibarra", "Sofía Lenz", "Nico Vidal".
  - Sala: "Todavía no tienen atributos ni habilidad", aunque la mesa ya los tiene.
- **Qué está mal:**
  - Cada documento elige de forma distinta:
    - Sala: cada jugador elige libremente entre los 7.
    - Mesa: se roban 3 y "los que nadie elija se quedan en la base".
    - Base: 4 supervivientes con 2 jugadores.
  - Con 3 jugadores en la mesa no queda nadie en la base. La base reconoce: "la guardia de esta noche no está resuelta (pendiente en las reglas)".
- **Propuesta:**
  - Fijar los nombres.
  - Fijar el tamaño del grupo inicial: por ejemplo, jugadores + 1, o siempre 3.
  - Regla para una base vacía: sin guardia, defensa sin Percepción.

### M5. Habilidades y cartas que usan acciones o fichas que no existen
- "Primeros auxilios" (Enfermera) no está definido: el kit tiene Vendar a 2 PA y Medicina dice 1 PA.
- "Vigilar" y "zombies ocultos" (Cazador, carta de acción): en las losetas los zombies se colocan a la vista al revelar.
- "Ficha de voz" (Maestra, Vigilar): no tiene regla. Es de las acciones ocultas que vienen después.
- "Barricar" en expedición (Mecánica, carta Tablones) y "Distraer" (Bengala, Megáfono): no se definen.
- "Huir": solo aparece en la carta.
- La Mecánica (Forzar 1 PA) y la Palanca ("forzar cuesta 1 PA en vez de 2") no dicen si se acumulan. El Hacha "sirve para Forzar sin tirada", pero Forzar no lleva tirada en el kit.
- **Propuesta:** un glosario de acciones con coste y ruido. Marcar como "pendiente de prueba 2" lo que dependa de acciones ocultas.

### M6. El Kit médico y las curaciones: nombres y costes que no coinciden
- **Dónde:**
  - Kit: objetivo "Kit médico"; Vendar 2 PA, solo frena laceraciones.
  - Mazo y tablas: no hay "Kit médico"; existen "Botiquín completo", "Kit de sutura: cierra una laceración" y "Vendas".
  - Carta Medicina: "vendar, entablillar o limpiar un rasguño" a 1 PA.
- **Qué está mal:**
  - El objeto objetivo de la prueba 1 no existe en el juego completo.
  - En el kit, limpiar un rasguño no sirve para nada (el rasguño no tiene efecto). Solo tendría sentido si causa infección.
  - "Entablillar" una fractura no tiene efecto definido.
- **Propuesta:** decidir si "Kit médico" = "Botiquín completo", y escribir qué cura cada cosa en la expedición y en la base.

### M7. Huecos de las heridas en el kit
- La cabecera de la tabla dice "Efecto mientras tengas ahí una herida", pero cabeza ("tu próximo turno") y torso ("al recibirla") son efectos de un solo uso.
- No se dice cuándo termina el efecto de una laceración o de una mordedura.
- No se dice qué pasa con el brazo izquierdo si la mochila ya está llena. El simulador obliga a soltar algo; el kit no lo dice.
- **Propuesta:** reescribir la tabla en dos columnas, "Al recibirla" y "Mientras dure", y añadir "Si la mochila excede su capacidad, sueltas objetos en la zona".

### M8. Infección y mordedura sin reglas
- Las referencias están repartidas:
  - "Antibióticos (frenan la infección)" en las tablas.
  - "1 Medicina frena la infección 1 día" en la carta.
  - "Cualquier rasguño que recibas acá ya está infectado" en el hospital.
  - "Ácido: solo infección" en la paleta.
- No hay regla de cuándo una herida se infecta, qué hace la infección ni cuándo mata.
- La carta Bisturí "permite amputar en la base", sin regla.
- **Propuesta:** escribir la regla de infección antes de la prueba que use el hospital.

### M9. Zombies distintos del caminante sin estadísticas completas
- `ZOMBIES` en la base solo da Defensa y movimiento. Faltan la vitalidad, el ataque y el daño de Corredor, Bruto, Infectado ácido y Chillón ("Mucha vitalidad", "Poca vitalidad").
- El Chillón hace aparecer "1 caminante en la puerta": no se dice cuál, si la del edificio o la más cercana.
- Brutos "con chaleco (+2 a su defensa)": su defensa base no tiene vitalidad asociada.
- **Propuesta:** una ficha numérica por tipo, como la del caminante del kit (Defensa 8 · vitalidad 5 · d20+2 · 1 zona).

### M10. Aparición y horda del kit: zonas ambiguas
- "Columna F" incluye F2 (depósito de la farmacia, interior) y "fila 3" incluye A3 (la base).
- No se dice cómo se elige la zona dentro de la fila.
- Horda: "zona de borde del mapa más cercana", sin desempate. Desde la casa (B2), B1, A2 y B3 están a la misma distancia.
- **Propuesta:**
  - "Fila 1: tira d6 para la columna."
  - "Columna F: F1 o F3."
  - "Fila 3: B3 a F3."
  - Desempate: la zona de borde más lejana al superviviente, o elegida al azar.

### M11. Material del kit que puede no alcanzar
- Hay 10 zombies (monedas), pero se pueden juntar 3 iniciales + 3 de la farmacia + 1 de la casa + 3 por cada horda + apariciones: fácilmente más de 10.
- **Propuesta:** subir a 15 fichas o añadir la regla "si no quedan zombies, no aparece ninguno / el más lejano se mueve".

### M12. Defensa nocturna de la base sin mecánica
- La base calcula "Defensa de una entrada = nivel de barricada + trampa (+ Percepción del guardia)".
- No existe el ataque nocturno contra el que se compara esa defensa.
- Las trampas hablan de "el evento", "esa noche", "segundo movimiento de los corredores".
- "Percepción del guardia": no se dice si suma a todas las entradas o a una.
- **Propuesta:** escribir la fase "Regreso y noche": cuántos zombies atacan, contra qué entrada, qué tirada se hace y qué pasa si superan la defensa.

### M13. Mejoras y objetos con efecto vago o sin regla de apoyo
- **Huerta:** "Comida extra cada pocos días". No dice cuánta ni cada cuántos días.
- **Recolector:** "Agua extra cuando llueve", pero no hay clima.
- **Cama extra:** "Lugar para un rescatado más", sin límite de camas definido (el plano dibuja 4).
- **Batería de auto:** "da energía a la radio por 3 días", sin regla de energía de la radio.
- **Clavos:** "En la base repara un objeto dañado", pero solo el Infectado ácido daña objetos, y los "rompe".
- **Linterna, Fósforos y velas, Walkie-talkie** (en cooperativo con conversación libre), **Libreta de fiado** y **Mapa de rutas** (las horas de viaje no se descuentan en ninguna regla): sin uso mecánico.
- **Propuesta:** dar un número o una regla a cada uno, o sacarlo del botín hasta que tenga uso.

### M14. Registrar con zombies en la zona
- `base_y_losetas.html`: "No se puede registrar con zombies en tu zona".
- El kit y el simulador lo permiten. Por ejemplo, se puede registrar el salón con un caminante dentro.
- **Propuesta:** decidirlo y ponerlo en el kit (es una decisión de tensión importante para la prueba del ruido).

### M15. Duración de la partida inconsistente con la meta del kit
- Arte: "Cooperativo · ~2 h".
- Kit: "La meta es que una expedición completa entre en unos 6 minutos".
- 30 días × 6 min son 3 h solo de expediciones, sin base, planificación ni noche.
- **Propuesta:** revisar la meta: menos días con expedición, expediciones de 3 a 4 min, o una duración de 3 a 4 h.

### M16. Faltan archivos que el material referencia
- `figuras3d.js`: los botones "Activar zombies" y "Errantes · d6" de la base dependen de él y no funcionan sin él.
- La carpeta `img/` con todas las ilustraciones.
- `pendientes.md` (mesa).
- La "sección 12" del reglamento (cartas).
- `arte/prompts_ilustraciones.md` (cartas).
- **Propuesta:** incorporarlos al repo o quitar las referencias.

### M17. La probabilidad de la pistola que da el kit es condicional
- Kit: "la pistola suele matar de un tiro (60 % de las veces)".
- El 60 % solo cuenta el daño (d10 ≥ 5). Para acertar hace falta 7+ en el d20 (70 %).
- Por disparo, la probabilidad real de matar es del 42 %, o del 55 % con ventaja.
- Para comparar: el cuchillo mata de un golpe el 25 % de las veces que acierta, y el bate el 50 %.
- **Propuesta:** corregir el texto para que la observación de la prueba no parta de un número equivocado.

---

## Gravedad baja

1. **Esconderse.**
   - Kit: "Termina tu turno".
   - Carta: "No puedes moverte" y "si no hay zombies en tu zona".
   - Unificar.
2. **Puntaje en el simulador.** Se calcula también en las derrotas, y no cuenta las vendas iniciales. El kit dice "al volver suma". Poner el puntaje a 0 si no se vuelve.
3. **Preguntas del simulador.** Le faltan dos preguntas de la hoja del kit: "¿Qué regla tuviste que buscar más veces?" y "¿Cuántos minutos duró un turno?".
4. **Ventaja por la espalda.** Solo la carta del Cuchillo dice "Atacar por la espalda da ventaja"; es regla general. Igual con la pifia de ruido (ver A5).
5. **Combustible.** Es "material" en la base (`MATS`) y "recurso" aparte en las cartas.
6. **Mochila.** "Mochila grande: +2 espacios" (tablas) y "Mochila de montaña: 6 a 8" (carta) son el mismo objeto con dos nombres.
7. **Equipo de un solo uso.** La intro de Equipo dice "se usan y se conservan, salvo la bengala", pero las Baterías también se gastan.
8. **Walkie-talkies.** "Par de walkie-talkies" (comisaría) es 1 resultado; en el mazo son 2 cartas sueltas. ¿Un hallazgo da las 2?
9. **Munición.**
   - Kit: pistola con 6 balas.
   - Cartas: 1 Munición = 3 disparos.
   - Tablas: "Pistola … con munición ×1".
   - Válido como evolución, pero conviene anotar que el kit es una excepción.
10. **Plantilla T3 (Parque industrial).** Tiene 8 huecos de edificio y el pool tiene 7. El código rellena con una plaza sin avisar.
11. **Español rioplatense y neutro mezclados.** La mesa usa voseo ("Sentate", "Elegí", "No tenés"); la sala y el kit, tuteo ("Elige", "Inicia sesión"); las cartas mezclan ("si la agarrás mal", "incluso en vos" junto a "Úsala", "Descártala"). Elegir un registro para el material impreso.
12. **Texto de la sala.** `pintarEstado` muestra "Queda 2 lugar libre". Pluralizar.
13. **Sala pensada para dos.** La sala habla de "tu amigo" (singular) aunque admite 3 jugadores.
14. **Extensión de la portada.** El pie de foto en arte dice "mano_del_suelo.png" y el archivo es `.jpg`.
15. **Nombre del zombie ácido.** "Ácido" (arte) frente a "Infectado ácido" (resto).
16. **Kit, mapa.** El kit dice "18 zonas de unos 10 m" y "cuadros de 5 cm". Correcto, pero no dice si la BASE (A3) tiene paredes ni si los zombies pueden entrar. En el simulador es una zona abierta más.
17. **Kit, duración.** "20 a 30 minutos" por partida de prueba contra la meta de 6 minutos por expedición. No es una contradicción si se aclara que la primera es con aprendizaje.
18. **Botín de la farmacia en el kit.** "Comida" en el depósito no tiene uso en la prueba, solo puntaje. Está bien si es intencional (medir la codicia); conviene decirlo.

---

## Preguntas que solo Santiago puede decidir

1. **Movimiento:** ¿te quedas con los costes del kit (Sigilo 2 / Caminar 1 / Correr 1 por 2 zonas) o con los de la carta (Sigilo 1 / Correr 2)? ¿Qué pasa con la habilidad del Estudiante?
2. **Heridas:**
   - ¿Modelo del kit (−1 por herida, torso −1 extra) o de la mesa (cabeza −3, torso −2, resto 0)?
   - ¿Cuánto duran los efectos de zona de una laceración o una mordedura?
   - ¿Un rasguño en la cabeza cuenta para la muerte por segunda herida?
3. **Botín:** ¿las tablas d20 por edificio o el mazo de cartas? Si conviven, ¿cuál decide qué objeto sale?
4. **Señal:**
   - ¿5 etapas o 10 puntos?
   - ¿Qué pasa el día 30 si la señal no está completa? ¿Y si se completa antes?
   - ¿La radio y el generador gastan batería y combustible cada día?
5. **Victoria y derrota del juego completo:** ¿pierden todos si muere uno, si mueren todos, o solo si no llega el helicóptero?
6. **Agua:** ¿cuánto se consume por día y qué pasa con la sed y el hambre?
7. **Armas:**
   - ¿El bate es de ruido bajo o medio? ¿Ocupa 1 o 2 espacios?
   - ¿La Fuerza suma al daño cuerpo a cuerpo o solo al impacto?
8. **Medicinas:** ¿todo es "1 Medicina" o los antibióticos son carta única? ¿El "Kit médico" del kit es el "Botiquín completo"?
9. **Grupo:**
   - ¿Cuántos supervivientes empiezan según el número de jugadores?
   - ¿Se eligen libremente o se roban 3?
   - ¿Qué nombres quedan?
10. **Reloj:** ¿cuántos turnos de 3 PA equivalen a una hora de expedición?
11. **Zombies y aberturas:**
    - ¿Pueden derribar la vidriera y la puerta con llave?
    - ¿Se puede registrar con zombies en la zona?
12. **Mordedura e infección:** ¿qué hacen y cómo se curan? En la prueba 1, ¿la mordedura es derrota o victoria con nota?
13. **Fatiga y Constitución:** ¿qué produce fatiga en expedición, qué pasa al llegar a 3 y para qué sirve Constitución?
14. **Duración objetivo:** ¿la partida de 30 días tiene que durar unas 2 h? Si es así, ¿cuánto puede durar una expedición?
15. **Tono del texto:** ¿voseo rioplatense o español neutro para las cartas y el reglamento?
