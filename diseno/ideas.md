# Día 30 – Ideas nuevas (agente de ideas)

2026-10-14 · v2 · propuestas para discutir, nada de esto es regla todavía

**Cambios de la v2 (decisiones del autor)**
- La partida dura **20 días** en 3 niveles de peligro: **1** (días 1–7), **2** (días 8–14) y **3** (días 15–20).
- **Comida y agua se unifican en Alimento.** Además de comerse, el Alimento (el agua) se gasta para **limpiar heridas**: cada herida sin limpiar pone 1 ficha de ruido por turno.
- **Un solo tipo de herida.** Toda herida queda **abierta** («olor a sangre») hasta que se limpia con agua (Alimento). **No hay mordedura ni infección.** Se sacaron la infección, el antibiótico como carta única, el zombie «conocido», el Triage de Marta y la carta Fiebre; los reemplazos están en cada sección.
- El **descanso rápido** es opcional.
- La aparición de zombies en la calle sale del mazo de aparición (`mazo_aparicion.md`), que reemplaza todas las tiradas de d6 de aparición y de errantes.
- Todo en voseo.

Todo lo que sigue parte del material de `fuentes/` y usa sus mismos términos: niveles de ruido (Silencio, Bajo, Medio, Alto, Máximo), fichas de ruido y horda, PA, sangre, fatiga (0 a 3), heridas por zona, Defensa de una entrada (nivel de barricada + trampa + Percepción del guardia), reloj de horas (salida 08:00, anochece 19:00), tablas d20 por edificio y las 5 etapas de la señal.

**Cómo leer las marcas**

| Marca | Significado |
|---|---|
| Impacto **A / M / B** | Cuánto mejora la experiencia o resuelve un hueco (alto, medio, bajo) |
| Coste **1 / 2 / 3** | Complejidad que agrega: 1 = una línea de regla o una carta; 2 = un subsistema chico o varias cartas; 3 = subsistema nuevo con componentes y pruebas propias |

---

## 0. Lo que falta o choca en el material actual

**Huecos**

| Hueco | Dónde aparece | Qué idea lo cubre |
|---|---|---|
| No hay mazo de eventos; la fase 4 se llama «Regreso y noche» pero no tiene reglas | `base_y_losetas.html` | §1 |
| No está definido cómo atacan los zombies a la base de noche | `base_y_losetas.html` («pendiente en las reglas») | §1.2 |
| ~~La mordedura «se prueba más adelante»~~ | El autor la sacó: no hay mordedura ni infección | §4.3 (olor a sangre) |
| Corredor, bruto, ácido y chillón sin vitalidad ni bono de ataque | `base_y_losetas.html` | §4.1 |
| «Zombies ocultos», «Vigilar» y «fichas de voz» se nombran pero no tienen regla | `mesa_online.html`, carta Movimiento y sigilo | §3, §4.2 |
| La etapa 3 (baliza) no tiene carta en la familia Señal; la etapa 5 no tiene procedimiento | `cartas_de_objetos.html`, `mesa_online.html` | §5.3, §2.4 |
| 20 días en ~2 h dan 6 minutos por día, y la meta de una expedición sola ya es de 6 minutos | README + kit | §2.1 |
| ~~Consumo de agua sin definir~~ | Lo resolvió el autor con el Alimento | §1.4 |

**Contradicciones detectadas (no son ideas, solo avisos)**

| Contradicción | Detalle |
|---|---|
| Señal 3/10 o 5 etapas | El plano de la base muestra «señal 3/10»; la mesa y las cartas usan 5 etapas. |
| Nombres de personajes | En la base: Julio Benítez, Sofía Paz y Nico Ferrer. En la mesa: Raúl Ibarra, Sofía Lenz y Nico Vidal. |
| Habilidad de Nico | «Correr le cuesta 1 PA en lugar de 2», pero el kit ya propone Correr a 1 PA. Si se adopta el kit, la habilidad no hace nada (ver §3). |
| Ruido del bate | En el kit es Medio; en la tabla de la casa y en la carta «Bate con clavos» es Bajo. |
| Recursos | La mesa tiene «Materiales» genérico; la base tiene 7 materiales separados. Con la v2, Comida y Agua pasan a ser una sola casilla de Alimento en la mesa y en las cartas. |
| Nombre del juego | «Día 30» con una partida de 20 días. ¿Queda como nombre, o pasa a «Día 20»? |
| Restos de infección en las fuentes | El kit tiene 4 tipos de herida (con mordedura). Las tablas de farmacia y hospital tienen «Antibióticos (frenan la infección)», «Kit de sutura: cierra una laceración» y la trampa del hospital («cualquier rasguño que recibas acá ya está infectado»). El bisturí «permite amputar». Hay que reescribirlos: ver §4.3. |

---

## 1. Mazo de eventos

### 1.1 Estructura propuesta

Tres mazos chicos, cada uno con su momento fijo en el día:

| Mazo | Cuándo se roba | Cartas |
|---|---|---|
| **Amanecer** | Fase 1 (Base), antes de planificar. 1 carta. | 9 |
| **Calle** | Al llegar al destino, 1 carta. Si la expedición sigue afuera a las 19:00, otra. | 9 |
| **Noche** | Fase 4, después de comer. 1 carta (2 desde el día 15). | 10 |

**Mazo por capas (Impacto A · Coste 1).** Cada carta lleva un número romano igual al nivel de peligro: I, II o III. El día 1 se mezclan solo las I. El día 8 se suman las II y se remezcla el descarte; el día 15, las III. Así el mazo envejece con la partida al mismo ritmo que el mazo de aparición, sin reglas extra.

**Cartas de hito (Impacto A · Coste 1).** Fuera de los mazos, 6 cartas fijas que se leen en días concretos (ver §2.3).

### 1.2 Regla mínima de ataque nocturno (necesaria para el mazo Noche)

Las cartas de Noche dicen **qué** ataca y **por dónde**. Para resolverlo, una propuesta simple que usa lo que ya existe:

1. **Fuerza del ataque** = suma de los zombies: caminante 1, corredor 1, chillón 1, infectado ácido 2, bruto 3.
2. Se compara con la **Defensa de la entrada** (nivel de barricada + trampa + Percepción del guardia si vigila esa entrada).
3. **Si la Fuerza no supera la Defensa**, el ataque se rechaza. Las trampas de un uso se gastan igual.
4. **Si la supera**, la barricada baja 1 nivel por cada punto de diferencia. Si llega a 0 y todavía sobra diferencia, los zombies **entran**: el guardia (o, si no hay guardia, un superviviente al azar) recibe un ataque normal de cada uno. Quien está durmiendo y es sorprendido recibe los ataques con ventaja, salvo que haya Alarma de latas en esa entrada, que es lo que ya dice el texto de esa trampa.

Impacto **A** · Coste **2**. Es lo mínimo para que la base, las barricadas y las trampas importen.

### 1.3 Las cartas

**Mazo Amanecer (diario)**

| # | Carta | Nivel | Regla | Sabor |
|---|---|---|---|---|
| A1 | Llueve | I | Hoy el ruido Bajo no deja fichas. Con el Recolector de agua: +2 Alimento. | «Por fin. El techo gotea en tres lugares.» |
| A2 | Niebla | I | Durante la expedición los zombies solo te detectan en tu misma zona, como de noche. Atacar a distancia tiene desventaja. | «No se ve la esquina. Ellos tampoco.» |
| A3 | Día en calma | I | Nadie sale. Todos quitan 1 de fatiga y cada uno gana 1 ficha de construcción. El calendario avanza **2 días** (comen por los dos). | «Alguien encontró un mazo de cartas. Truco hasta la siesta.» |
| A4 | Ratas en la despensa | I | Pierden 1 Alimento, salvo que se quede en la base alguien con Percepción 4 o más. | «Las latas no, pero el arroz, todo.» |
| A5 | Ola de calor | II | Hoy, cada superviviente que sale gasta 1 Alimento al volver o gana 1 de fatiga. Las heridas sin limpiar ponen 2 fichas de ruido por turno en vez de 1 (el olor viaja). | «A las diez de la mañana ya no se puede respirar.» |
| A6 | Humo en el Centro | II | Elijan un barrio: hoy ese barrio tiene 1 caminante menos en cada edificio, pero 1 edificio al azar queda saqueado. | «Alguien prendió fuego a una manzana. Los muertos fueron a mirar.» |
| A7 | Discusión | II | Si alguien tiene 2 de fatiga o más, elijan: ese superviviente no sale hoy, o el grupo pierde la ficha de construcción del día. | «Nadie se acuerda de cómo empezó.» |
| A8 | El puente cede | II | Desde hoy, ir al Parque industrial cuesta 1 hora más (hay que cruzar el río Seco). Si gastan una Cuerda en la base, se arregla. | «Se oyó crujir toda la noche.» |
| A9 | Los muertos caminan de día | III | Hoy robás 2 cartas de aparición por ronda, como si fuera de noche. | «Ya no esperan a que oscurezca.» |

**Mazo Calle (expedición)**

| # | Carta | Nivel | Regla | Sabor |
|---|---|---|---|---|
| C1 | Cadáver con mochila | I | En la zona de entrada hay una mochila: 1 Registrar gratis con la tabla de la casa. Tirá d6: con 1–3, el cadáver es un caminante tranquilo en esa zona. | «Llevaba puesta una campera como la tuya.» |
| C2 | Perro suelto | I | Un perro sigue al grupo. Si le das 1 Alimento, se queda: esta noche suma +1 a la Defensa de la entrada del guardia. Si no, ladra: ruido Bajo en tu zona cada turno en que haya un zombie adyacente. | «Flaco, sin collar, y no muerde.» |
| C3 | Grafiti en la pared | I | En el próximo edificio que revelen, tiren 2 fichas de edificio y elijan cuál usar. | «"FARMACIA LLENA – NO ENTREN DE NOCHE". Firmado: Gabi.» |
| C4 | Alarma de auto | I | La primera vez que alguien Corra en una zona de calle, tirá d6: con 1–2, suena una alarma. Ruido Máximo en esa zona. | «Las baterías duran más que la gente.» |
| C5 | Sirena lejana | II | Todos los zombies del mapa se mueven 1 zona hacia el borde que elijan. En la próxima ronda no se roba carta de aparición. | «Una ambulancia, sola, dando vueltas. ¿Quién la maneja?» |
| C6 | Derrumbe | II | Una zona de calle, a elección del grupo pero no la de salida, queda bloqueada (como calle cortada) hasta el final de la expedición. | «La fachada entera, en un segundo.» |
| C7 | Saqueadores | II | Otro grupo se les cruza. Entreguen 2 recursos cualesquiera, o el edificio sin revelar más cercano queda saqueado antes de que lleguen. | «No apuntaron. Tampoco bajaron las armas.» |
| C8 | Radio policial | II | En la vereda hay un patrullero. Por 1 PA, tirá d20 + Percepción contra 14: si te sale, revelás 1 ficha de edificio de cualquier barrio. Con un 1 natural, se prende la sirena (ruido Máximo). | «Coordenadas a medias y un nombre: "San Roque".» |
| C9 | Ellos también buscan | III | El chillón más cercano del mapa (o 1 nuevo en el borde, si no hay) empieza **alerta**. | «Esa cosa olfatea el aire como un perro.» |

**Mazo Noche**

| # | Carta | Nivel | Regla | Sabor |
|---|---|---|---|---|
| N1 | Rasguños en la puerta | I | 2 caminantes atacan la entrada con menos Defensa. | «Toc. Toc. Toc. Nunca se cansan.» |
| N2 | Noche en calma | I | No hay ataque. El guardia también descansa (quita 1 de fatiga). | «Se oyen grillos. Parece otro mundo.» |
| N3 | Golpes que piden ayuda | I | Alguien golpea y pide entrar. Si abren, tirá d6: 1–3, un superviviente (robá del mazo); 4–5, un superviviente con 2 heridas abiertas y sin nada en la mochila; 6, un caminante en la sala común. Si no abren, no pasa nada. | «Dijo un nombre. Ninguno lo conocía.» |
| N4 | Pesadillas | I | El superviviente con más fatiga no la recupera esta noche. | «Gritó dormido. Afuera algo respondió.» |
| N5 | Pasos en el techo | II | 1 corredor ataca el Techo (claraboya). Si entra, cae en la sala común. | «Algo corre por la chapa.» |
| N6 | El generador se oye | II | Si la etapa 2 está hecha, elijan: lo apagan (mañana la radio no funciona) o 1 caminante más ataca cada entrada. | «Ese zumbido es la esperanza. Y es un faro.» |
| N7 | Chillón en la vereda | II | El guardia tira d20 + Percepción contra 14. Si no le sale, el chillón chilla: +2 caminantes en cada ataque de esta noche. | «Primero el silencio. Después, eso.» |
| N8 | La horda pasa | III | 6 caminantes cruzan la calle Las Heras. Si alguna entrada tiene una trampa de un uso o una Alarma de latas, salta y la horda ataca esa entrada. Si no, pasa de largo. | «Nadie respiró en cuarenta minutos.» |
| N9 | Olor a sangre | III | Cada herida abierta que haya en la base suma 1 caminante al ataque de esta noche, contra la entrada con menos Defensa. | «Vienen olfateando, con la cabeza baja, directo a la puerta.» |
| N10 | Asedio | III | 1 bruto y 2 caminantes atacan la puerta principal; 1 corredor, la ventana con menos Defensa. | «Esta vez vinieron a quedarse.» |

Impacto **A** · Coste **2** (28 cartas, todas con reglas que ya existen).

### 1.4 Alimento y heridas sin limpiar: ideas que lo aprovechan

La regla del autor (el agua limpia heridas; una herida sin limpiar pone 1 ficha de ruido por turno) convierte cada herida en un **rastro**. Algunas ideas que la usan sin agregar componentes:

| Idea | Regla | Impacto · Coste |
|---|---|---|
| **Limpiar en la calle** | Limpiar una herida: 1 PA, Silencio, gastás 1 Alimento de la mochila. Las fichas que ya se pusieron se quedan. | A · 1 |
| **Ola de calor** (A5) | Duplica el rastro de las heridas sin limpiar ese día. | M · 1 (ya incluida) |
| **El rastro llega a casa** | Si alguien vuelve a la base con una herida sin limpiar, esa noche la carta de Noche suma 1 caminante al ataque. En el nivel 3 se vuelve una carta propia (N9 «Olor a sangre»). | M · 1 |
| **Decidir quién se limpia** | Con 1 solo Alimento en la mochila, hay que elegir: comer esa noche o limpiar la herida de un compañero. Esa es la tensión que buscamos, así que no hace falta otra regla. | — |

---

## 2. Arco de los 20 días

### 2.1 Descanso rápido opcional y ritmo (Impacto A · Coste 2)

20 días en unas 2 h dan 6 minutos por día, y una expedición sola ya apunta a 6 minutos. El descanso rápido es **opcional**: el grupo lo usa cuando no le conviene salir.

| Palanca | Regla | Efecto |
|---|---|---|
| **Descanso rápido** (opcional) | En la fase 1, el grupo puede declarar descanso por 1 o 2 días: nadie sale, se come Alimento por cada día, se roba 1 sola carta de Noche en total y cada uno quita 1 de fatiga y gana 1 ficha de construcción por día. | Los días sin expedición se resuelven en 1 minuto. |
| **Viajes largos** | Los barrios de 3 horas (Hospital San Roque) se pueden hacer como expedición de 2 días: duermen afuera y resuelven 1 carta de Noche en el edificio más seguro del mapa. | Da sentido a los destinos lejanos y ahorra un ciclo de base. |
| **Carta A3 «Día en calma»** | Ya está en el mazo Amanecer. | Salto de calendario al azar y amable en el nivel 1. |

Meta de diseño a medir: unas 10–12 expediciones por partida.

### 2.2 Qué cambia en cada nivel de peligro

| | **Nivel 1 · Aprendizaje (1–7)** | **Nivel 2 · Presión (8–14)** | **Nivel 3 · Cuenta regresiva (15–20)** |
|---|---|---|---|
| Zombies en edificios | Primera columna de las tablas | Segunda columna | Tercera columna, +1 corredor de noche |
| Mazo de aparición | ~0,4 zombies por carta, casi solo caminantes | ~1 por carta, aparecen los especiales | ~1,5 por carta, casi ninguna viene vacía |
| Mazo de eventos | Solo cartas I | Se suman las II | Se suman las III; 2 cartas de Noche por noche |
| Ritmo | Explorar y aprender el barrio | Elegir qué barrio abandonar | Ir a buscar lo que falta de la señal, cueste lo que cueste |
| Alimento | Abunda cerca de la base (Las Acacias) | Las Acacias saqueadas; hay que cruzar | Cada barrio cercano saqueado da desventaja al registrar |
| Novedad | — | Aparecen los rastreros (§4.2) | Destinos de nivel 3 (§5.1) |

### 2.3 Giros narrativos: cartas de hito

Se leen al empezar el día indicado, antes de la carta de Amanecer.

| Día | Hito | Regla | Impacto · Coste |
|---|---|---|---|
| 1 | **El helicóptero pasa** | Se oye un rotor sobre el río. Se recibe la ficha de calendario del día 20. No tiene regla: es la promesa. | M · 1 |
| 5 | **Primera transmisión** | Si tienen la etapa 1, la radio da una pista: revelen 1 ficha de edificio con objeto de señal. Si no, no pasa nada (pero ya saben que existe). | M · 1 |
| 8 | **Se corta la luz del todo** (empieza el nivel 2) | Desde hoy, en todos los edificios las zonas interiores sin ventana se juegan a oscuras (desventaja al atacar), salvo con linterna. | A · 1 |
| 10 | **Los otros** | Un grupo vive en la escuela del Barrio Norte. Elijan: alianza (cada 3 días pueden cambiar 2 recursos por 2 de otro tipo) o ignorarlos. Si los ignoran, desde el día 15 la carta Saqueadores (C7) se aplica sola en cada expedición. | A · 2 |
| 14 | **La migración** | Saquen del mazo de aparición 2 copias de Calle vacía y metan 2 de Caminante. La horda se acerca a la ciudad. | A · 1 |
| 17 | **Confirmación** | Si tienen las etapas 1 y 4, la radio confirma el punto de aterrizaje: elijan **la base** o **un punto alto** (§5.1). Sin esas etapas, es la base. | A · 1 |

### 2.4 El clímax del día 20: «La última noche»

**Impacto A · Coste 3.** Es la escena por la que se va a recordar el juego.

1. **Activación (etapa 5).** A las 17:00 del día 20 se prende todo. Es ruido Máximo: atrae una horda, como ya dice la etapa.
2. **Mapa táctico de la base.** Se juega sobre el plano de la casa de calle Las Heras como mapa de zonas: dormitorio, cocina, sala común, patio y techo (el plano ya tiene «AL TECHO»). Las 5 entradas tienen su Defensa actual.
3. **Oleadas.** Cada turno se roba una carta de oleada (6 cartas: 3C, 2C 1R, 1B 1C, 1A 2C, 1H 2C, 2R) y ataca la entrada que indique, con la regla del §1.2. Los que entran se juegan con el kit normal: turnos, PA y combate. El mazo de aparición no se usa en el clímax.
4. **Mantener la baliza.** Cada turno, alguien en el techo gasta 1 PA en la baliza (etapa 3). Si en un turno nadie lo hace, el helicóptero llega 1 turno más tarde.
5. **Llegada.** El helicóptero aterriza al final del turno 6 y espera 2 turnos. Quien esté en el techo se salva. «Un helicóptero que no espera»: al final del turno 8, despega.
6. **Señal incompleta.** Con 4 etapas (sin Mensaje), llega en el turno 9 y espera 1 solo turno. Con 3 o menos, pasa de largo, salvo que alguien dispare 2 bengalas en el mismo turno.

**Final por grados:** se salvan todos / se salva al menos uno / no se salva nadie. Un epílogo de una línea por superviviente en el diario (§7) convierte el resultado en historia.

**Variante del punto alto (si la eligieron el día 17):** el clímax se juega en la loseta de la Antena del cerro o en el campanario (§5.2). No hay barricadas, pero el helicóptero llega en el turno 4. La decisión del día 17 importa de verdad: defensas conocidas o menos tiempo expuestos.

---

## 3. Supervivientes

Se conservan los nombres (los de la mesa), la profesión y los atributos. Cada uno recibe una **habilidad** revisada, un **momento** (1 vez por partida, se marca al usarlo) y un **defecto**. El defecto es lo que hace que elegir a quién sacar sea una decisión y no una cuenta.

**Impacto A · Coste 2** para el conjunto.

| Superviviente | F/D/C/P | Habilidad (revisada) | Momento (1 vez por partida) | Defecto |
|---|---|---|---|---|
| **Marta Ríos**, enfermera | 2/3/3/4 | *Manos firmes.* Vendar, limpiar una herida o usar Medicina le cuesta 1 PA. Puede limpiar 2 heridas con 1 solo Alimento. En la base, 1 vez por día, quita 1 herida con 1 Medicina en vez de 2. | *Sutura de campaña.* Limpia todas las heridas abiertas de los supervivientes de su zona sin gastar Alimento. | *Turno doble.* Cada vez que cura en la base, gana 1 de fatiga. |
| **Raúl Ibarra**, ex policía | 4/3/3/2 | *Entrenamiento.* Ventaja en su primer ataque con arma de fuego de cada expedición. En la comisaría abre la puerta blindada sin palanca (sabe dónde está la llave). | *Cubrir.* Este turno, un compañero de su zona o de una adyacente no recibe ataques. | *Gatillo fácil.* Si un zombie entra en su zona y él tiene un arma de fuego cargada, tirá d6: con 1, dispara sin querer (gasta 1 disparo y hace ruido Máximo). |
| **Sofía Lenz**, mecánica | 3/4/3/2 | *Manos de taller.* Forzar o barricar le cuesta 1 PA y hace 1 nivel menos de ruido. | *Puente.* En el taller o la estación de servicio, convierte un 18 o 19 de botín en un 20 («Un auto arranca»). | *No se va sin terminar.* Si se queda en la base y hay materiales para una barricada o una mejora, tiene que gastar su ficha en eso o gana 1 de fatiga. |
| **Tomás Ferro**, cocinero | 4/2/4/2 | *Raciones.* 1 vez por día, 1 Alimento alimenta a 2. Ventaja al registrar en almacén y supermercado. | *Guiso.* Una noche, nadie come doble por fatiga y todos quitan 1 de fatiga. | *Pesado.* No puede Correr dos turnos seguidos. |
| **Nico Vidal**, estudiante | 1/5/2/4 | *Ágil* (corregida). Puede Correr dos veces por turno, y la segunda vez el ruido es Bajo. | *Por la ventana.* Pasa por una ventana intacta sin romperla (en Silencio). | *Inexperto.* Un 1 o un 2 natural al atacar es pifia. |
| **Aurelio Pando**, cazador | 3/3/2/4 | *Rastreador.* Vigilar revela todos los zombies ocultos de una zona adyacente (ver rastreros, §4.2). Ve 1 zona más que el resto. | *Tiro limpio.* Un ataque suyo contra un zombie tranquilo es crítico automático. | *Viejo.* Si la expedición vuelve después de las 19:00, gana 1 de fatiga extra. |
| **Elena Quiroga**, maestra | 2/2/3/5 | *Calma.* Cada uno del grupo recibe +1 ficha de voz por expedición. Con ella en la base, la carta «Discusión» (A7) no tiene efecto. | *Voz de mando.* Este turno, todos los del grupo tienen +1 PA. | *Sus alumnos.* Si en el destino hay una escuela, tiene que entrar y registrarla al menos 1 vez antes de volver. |

**Sobre Nico.** Su habilidad actual («Correr cuesta 1 PA en lugar de 2») queda vacía si se adopta el Correr a 1 PA del kit. La versión propuesta mantiene la idea de «rápido» con la regla nueva.

### 3.1 Supervivientes de rescate (nuevos)

Son para los resultados «Rescate: robá un superviviente». Son menos completos que los iniciales, porque llegan tarde.

| Superviviente | F/D/C/P | Habilidad | Defecto | Impacto · Coste |
|---|---|---|---|---|
| **Don Elías Ortega**, radioaficionado jubilado | 1/2/2/4 | Con él en la base, la etapa 4 (Mensaje) no necesita manual ni GPS: la arma él en 2 días de descanso rápido. | No sale de expedición. Consume 1 Alimento extra por día (toma remedios con mucha agua). | A · 1 |
| **Carla Sosa**, bombera | 4/3/4/2 | Empieza con el Hacha de bombero. Fuerza sin tirada (lo que dice la carta) y no recibe rasguños del infectado ácido. | *Corre hacia el fuego.* Si hay ruido Máximo en el mapa, su primer movimiento del turno es hacia ahí. | M · 1 |
| **Lu**, 12 años, la sobrina de alguien | 1/4/2/4 | Cabe por la claraboya y por ventanas chicas: entra a zonas cerradas sin abrir ni romper nada. | Mochila de 4 espacios. Si muere, todos ganan 2 de fatiga. | M · 1 |

### 3.2 Cartas de trauma (Impacto M · Coste 2)

Un mazo de 8 cartas. Un superviviente roba una cuando llega a 3 de fatiga o cuando ve morir a un compañero en su zona. Ejemplos: *Insomnio* (no recupera fatiga con el descanso rápido), *Temblor* (desventaja en el primer ataque de cada expedición), *Mudo* (no usa fichas de voz), *Acumulador* (no puede soltar objetos fuera de la base), *Fobia a los encierros* (no registra en zonas sin ventana). Se sacan con un Día en calma o con 2 Medicinas. Le dan un arco a cada personaje sin escribirle una historia previa.

---

## 4. Zombies

### 4.1 Valores para los que no los tienen (Impacto A · Coste 1)

El caminante ya está probado en el kit. El resto se propone con la misma escala. Son los valores que usa `mazo_aparicion.md`.

| Zombie | Defensa | Vitalidad | Ataque | Movimiento | Regla especial |
|---|---|---|---|---|---|
| Caminante | 8 | 5 | d20 + 2 | 1 | Sin cambios. Llega en grupo. |
| Corredor | 12 | 4 | d20 + 3 | 2 | De noche nunca está tranquilo: no se lo puede atacar con ventaja después de las 19:00. El Alambre de púas le saca el segundo movimiento (ya existe). |
| Bruto | 10 | 12 | d20 + 4 | 1 | Su golpe suma +1 a la tirada de tipo de herida (más fracturas). Rompe una puerta cerrada con 4–6 en lugar de 6. Las armas de d4 solo le hacen daño con crítico. |
| Infectado ácido | 9 | 6 | d20 + 2 | 1 | Si te golpea, se te rompe un objeto de la mochila (ya existe). Si lo matás con cuchillo, bisturí o las manos, recibís un rasguño (salpica). Las armas largas (bate, hacha, tonfa) no salpican. |
| Chillón | 8 | 4 | d20 + 1 | 1 | Chilla al detectarte (ya existe) o al recibir daño sin morir. Si lo matás mientras está tranquilo, no llega a chillar. Chilla una sola vez por expedición. |

### 4.2 Variantes nuevas

| Variante | Regla | Dónde aparece | Impacto · Coste |
|---|---|---|---|
| **Rastrero** (sin piernas) | Se pone **boca abajo**, como zombie oculto. No se mueve. Ataca con ventaja al primero que registre o termine el turno en su zona. Se revela con Vigilar (y Aurelio los revela todos en una zona adyacente). Defensa 7, vitalidad 3. | 1 por edificio en las filas «Trampa» desde el nivel 2, o en lugar del resultado «¡Aaah!» | A · 1. Le da sentido a Vigilar y a la habilidad del cazador, que hoy no tienen a quién revelar. |
| **Hinchado** | Defensa 8, vitalidad 3. Si muere en una zona con supervivientes, revienta: cada uno tira d6 y con 1–3 recibe un rasguño ácido (se le rompe un objeto). Matarlo a distancia evita el problema. | Hospital y estación de servicio, nivel 3 | M · 1 |
| **Conocido** | Cuando un superviviente muere afuera, su figura se queda en ese barrio como zombie, con las estadísticas del caminante y **su mochila**. Matarlo recupera todo lo que llevaba. | Cualquier barrio | A · 1. No necesita componentes nuevos: usa la ficha del muerto. Es el giro emocional más barato del juego. |

### 4.3 Infección (Impacto A · Coste 1)

La mordedura ya existe; falta qué hace.

1. Se pone un contador de infección en 0 sobre la carta del mordido. Cada noche sube 1.
2. **1 Medicina frena 1 día** (ya está en las cartas): ese día el contador no sube.
3. Con 2: fiebre. Desventaja en todo y no recupera fatiga.
4. Con 3: muere al amanecer y se levanta. Si estaba en la base, aparece como caminante en la sala común.
5. **Curas.** Los antibióticos curan si se usan antes de que el contador llegue a 2. Por eso se propone que **los antibióticos sean carta única** (responde la pregunta abierta de `cartas_de_objetos.html`). La amputación con bisturí (ya existe en el hospital) cura si la mordedura es en un brazo o en las piernas: la herida pasa a ser una fractura permanente en esa zona y se pierden 2 de sangre.
6. Una mordedura también es una herida: si no se limpia con Alimento, pone su ficha de ruido por turno como cualquier otra.

---

## 5. Destinos, edificios y objetos de señal

### 5.1 Barrios nuevos

| Barrio | Horas · peligro | Edificios | Por qué existe | Impacto · Coste |
|---|---|---|---|---|
| **Cerro de la Antena** | 3 h · 2 | casa, estación de servicio, plaza + loseta especial **Antena** | Punto alto: la etapa 3 (baliza) se puede hacer acá con ventaja, y es el lugar alternativo de aterrizaje del día 20. | A · 2 |
| **Costanera del río Seco** | 2 h · 2 | casa, almacén, club náutico (casa con muelle), plaza | Alimento: registrar en el muelle con una Cuerda da Alimento ×2 (agua del río, hervida). Con bote (resultado 20) la vuelta cuesta 1 hora menos. | M · 2 |
| **Aeroclub** (solo desde el día 15) | 3 h · 3 | taller ×2, gasolinera, oficina (casa) | Etapa 4 asegurada: en la oficina, del 15 al 20 sale manual o GPS. A cambio, tercera columna de zombies con 1 bruto extra. | M · 2 |

### 5.2 Edificios nuevos

| Edificio | Zonas | Rasgo (como las notas de las fichas) | Botín destacado | Impacto · Coste |
|---|---|---|---|---|
| **Iglesia** | Nave, sacristía, campanario | El campanario es punto alto. Tocar la campana: 1 PA, Distraer con ruido Máximo **en la zona que elijas a hasta 4 zonas** (el sonido viene de arriba). | Velas y fósforos, bidones de agua del bautisterio (Alimento ×2), soga de la campana (Cuerda ×2), Rescate. | A · 2 |
| **Cuartel de bomberos** | Garaje, dormitorios, torre de mangueras | La autobomba no arranca, pero su escalera es un punto alto móvil para el día 20. | Hacha de bombero, trajes ignífugos (+2 Defensa contra el infectado ácido), Combustible, bengalas. | M · 2 |
| **Radio FM** | Estudio, sala de equipos, terraza con antena | Prender cualquier equipo es ruido Alto. | Etapa 1 (antena) y etapa 4 (manual del transmisor) en la misma tabla, con 19 y 20. Muy buscado, muy peligroso. | A · 2 |
| **Torre de agua** | Base, escalera, tanque | Una sola entrada; subir cuesta 2 PA por zona. Arriba nadie te detecta desde la calle. | Alimento ×4 (el tanque), Chapa, Alambre. Punto alto. | B · 1 |

Ejemplo de fila de zombies para la **Radio FM**, con el formato existente y las columnas por nivel de peligro:

| Ficha | Nivel 1 | Nivel 2 | Nivel 3 | Registros | Mod. | Nota |
|---|---|---|---|---|---|---|
| 1 | — | 1C | 1C 1R | 1 | d | «Ya desarmaron el transmisor.» |
| 2 | 1C | 2C | 2C 1R | 1 | | |
| 3 | 1C 1R | 2C 1R | 3C 1R 1H | 2 | | |
| 4 | 2C | 2C 1R | 2C 1R 1H | 2 | | «Sala insonorizada: el ruido Medio o menor no sale del estudio.» |
| 5 | 1C | 2C 1R | 2C 2R | 3 | v | «Los equipos siguen en sus racks.» |
| 6 | 3C 1R | 3C 2R 1H | 4C 2R 1H 1A | 3 | v | «Trampa: el último locutor siguió transmitiendo hasta el final.» |

### 5.3 Objetos de señal: completar las etapas (Impacto A · Coste 1)

| Etapa | Hoy | Propuesta |
|---|---|---|
| 1 · Radio o antena | Radio portátil, antena, radios de la comisaría y la escuela | Sin cambios. |
| 2 · Energía | Generadores + Combustible | Sin cambios. |
| 3 · Baliza o fuego | Solo bengalas (en Equipo) y la nota «en la base o en un punto alto» | Tres caminos: **Pira** (se construye en la base: 2 Madera + 2 Combustible), **Espejo de señales** (carta de Señal nueva, sale con 20 en casa y escuela) y **Reflector de estadio** (carta nueva, en escuela o club; necesita la etapa 2). |
| 4 · Mensaje | Manual técnico o GPS | + Don Elías (§3.1). |
| 5 · Activación | Sin procedimiento | Es el clímax (§2.4); no necesita objeto. |

**Cada etapa cambia algo del juego (Impacto A · Coste 1).** Así la señal deja de ser una lista para tachar:

| Etapa hecha | Efecto inmediato |
|---|---|
| 1 | Se activan los hitos de radio (días 5 y 17) y la carta C8 tiene ventaja. |
| 2 | La base tiene luz: el guardia suma +1 a la Defensa, pero entra en juego la carta N6. |
| 3 | En el nivel 3, cada noche tirá d6: con 6 pasa un helicóptero de reconocimiento y deja 1 recurso a elección en el patio. |
| 4 | Pueden elegir el punto de aterrizaje el día 17. |

---

## 6. Escenarios y variantes

| Variante | Regla | Impacto · Coste |
|---|---|---|
| **Solitario** | Manejás 2 supervivientes que salen juntos, con 2 PA cada uno en vez de 3. No se usan fichas de voz. Empezás con 1 superviviente extra en la base. | A · 1 |
| **Los últimos días** (escenario corto, ~40 min) | Empieza el día 15 (nivel 3) con las etapas 1 y 2 hechas, 2 barricadas en nivel 2 y el mazo de eventos con las capas I, II y III. Ideal para probar el clímax sin jugar la partida entera. | A · 1 |
| **La primera semana** (tutorial) | Días 1–7 (nivel 1), con un objetivo corto: construir el taller y conseguir la etapa 1. Enseña base, expedición y noche. | M · 1 |
| **Dificultad** | Ver la tabla de abajo. | M · 1 |
| **Campaña: la ciudad recuerda** | 3 partidas seguidas en la misma ciudad. Los barrios saqueados siguen saqueados, los conocidos (§4.2) se quedan en su barrio y los supervivientes rescatados conservan sus traumas. Cada partida suma un barrio nuevo (§5.1). | M · 3 |
| **Modo diario** | Al final de cada día, un jugador escribe una línea en el diario. Al terminar, se lee completo. No tiene regla de juego, pero es la mitad de la experiencia en una partida de 2 h. | M · 1 |

**Dificultad**

| Nivel | Alimento inicial | Umbral de horda | Mazo de eventos | Mazo de aparición | Helicóptero espera |
|---|---|---|---|---|---|
| Superviviente | 12 | 6 fichas | Sin cartas III | +2 Calle vacía | 3 turnos |
| Normal | 10 | 5 fichas | Normal | Normal | 2 turnos |
| Pesadilla | 7 | 4 fichas | Las II desde el día 5 | −2 Calle vacía, +2 Rezagado | 1 turno |

(El Alimento inicial de Normal sale de sumar la comida y el agua de la partida de ejemplo del día 6: 6 + 4.)

---

## 7. Ganchos para Tabletop Simulator

| Gancho | Qué hace | Por qué en TTS | Impacto · Coste |
|---|---|---|---|
| **Botón de botín por edificio** | Cada ficha de edificio tiene un botón (Lua) que tira d20, aplica ventaja o desventaja según la ficha, lee la tabla y deja la carta de objeto sobre la mesa. | Las 11 tablas d20 son lo más lento de jugar en físico. | A · 2 |
| **Mazo de aparición con botón** | Al terminar el turno de los jugadores, un botón roba 1 carta (2 de noche), lee la cantidad del nivel actual y saca los zombies de la bolsa al borde de la loseta con más ruido. | Saca de encima la parte más mecánica de cada ronda. | A · 2 |
| **Contador de ruido con horda automática** | Las fichas de ruido son contadores por zona; al llegar a 5, el script avisa y saca 3 caminantes al borde más cercano. La disipación es un botón. Las heridas sin limpiar suman su ficha solas en cada turno. | Quita la contabilidad que más se olvida. | A · 2 |
| **Zombies con dos estados** | Cada figura tiene estado tranquilo y alerta (tecla de estados). El rastrero entra boca abajo bajo una niebla de guerra (Fog of War) de su zona, que se levanta cuando alguien Vigila. | Mantiene oculto lo oculto sin que nadie tenga que no mirar. | A · 1 |
| **Calendario con niveles** | Un botón «Pasar de día» mueve el calendario, suma las cartas II el día 8 y las III el día 15 (eventos y aparición) y saca las cartas de hito en su día. | Imposible olvidarse de un hito. | A · 2 |
| **Mapa por semilla** | Las losetas se arman con la misma lógica de `base_y_losetas.html` (plantillas P3, T1, T2, T3) a partir de una semilla; la misma semilla repite el mapa. | Permite comparar partidas de prueba en igualdad de condiciones. | M · 3 |
| **Guardado por día** | Al empezar cada día se guarda el estado, y se puede volver para probar otra decisión. | En la etapa de pruebas vale oro: una partida, varias ramas. | A · 1 |
| **Acciones ocultas en la mano** | Las cartas de acción numeradas se eligen en la zona de mano de cada jugador y se revelan juntas con un botón. | La prueba 2 (acciones ocultas) funciona sin pantallas de cartón. | M · 1 |
| **Diario automático** | Un Notebook de TTS recibe una línea por cada evento («Día 12. Queda 1 de Alimento.»), con la tipografía de máquina de escribir de la dirección de arte. | Cierra la partida con su historia escrita. | M · 1 |
| **Barricadas con estados** | Cada entrada de la base es un objeto con estados 0–3 y un hueco para la trampa; la Defensa se calcula sola. | La regla nocturna del §1.2 sin cuentas. | M · 2 |
| **Audio en el día 20** | El reproductor de música de TTS pone un rotor de helicóptero que se acerca turno a turno en el clímax. | Barato y muy dramático. | B · 1 |
| **Hoja de registro** | Al terminar, un botón copia al Notebook el día alcanzado, las etapas, los muertos, las hordas y las cartas de aparición de cada nivel (como la hoja de registro del kit). | Los datos de varias partidas valen más que la impresión de una. | M · 1 |

---

## 8. Top 10 recomendado

Ordenado por la relación entre impacto y coste, y por cuánto destraba otras piezas.

| # | Idea | Sección | Impacto · Coste | Por qué primero |
|---|---|---|---|---|
| 1 | Regla mínima de ataque nocturno | §1.2 | A · 2 | Sin ella, barricadas, trampas, guardia y el mazo Noche no funcionan. |
| 2 | Descanso rápido opcional + medir el ritmo | §2.1 | A · 2 | Hay que confirmar que 20 días entran en 2 h; eso cambia todo lo demás. |
| 3 | Mazo de eventos por capas I/II/III (28 cartas) | §1.1, §1.3 | A · 2 | Acompaña los 3 niveles de peligro con una sola regla y llena la fase 4. |
| 4 | Clímax «La última noche» | §2.4 | A · 3 | Es el final del juego; hoy la etapa 5 no tiene procedimiento. |
| 5 | Valores de corredor, bruto, ácido y chillón | §4.1 | A · 1 | Sin números no se pueden jugar ni las tablas de edificio ni el mazo de aparición. |
| 6 | Infección en 3 noches + antibiótico como carta única | §4.3 | A · 1 | Cierra la mordedura y responde una pregunta abierta. |
| 7 | Defecto y momento para los 7 supervivientes (y arreglar a Nico) | §3 | A · 2 | Hace que elegir a quién sacar sea interesante. |
| 8 | Cada etapa de la señal cambia algo + caminos para la etapa 3 | §5.3 | A · 1 | La señal pasa de lista a motor de la partida. |
| 9 | Rastrero y conocido | §4.2 | A · 1 | Le dan sentido a Vigilar y al cazador; el conocido es el giro emocional más barato. |
| 10 | Escenario «Los últimos días» + guardado por día en TTS | §6, §7 | A · 1 | La forma más rápida de probar el final y las reglas nuevas en Tabletop Simulator. |
