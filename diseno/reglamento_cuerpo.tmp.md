# Día 30 · Reglamento unificado v0.3

Borrador del 14 de octubre de 2026 · juego cooperativo de Santiago · para probar en Tabletop Simulator

Este documento junta en un solo sistema lo que estaba repartido en el kit de la prueba 1, su simulador, la hoja de base y losetas, el mazo de objetos y la mesa en línea. Todos los números siguen siendo **propuestas a probar**.

**Cómo leerlo**

- **Decisión:** cuando dos fuentes decían cosas distintas, se eligió una. La nota explica cuál y por qué. Todas están listadas en la sección 20.
- **[PROPUESTA]**: regla que no estaba definida en ninguna fuente y se inventó para cerrar el sistema. Son las primeras candidatas a cambiar después de jugar.
- Lo que no lleva marca viene de las fuentes tal cual.
- Fuente de referencia en caso de duda: el JavaScript de `prueba_1_simulador.html` para la expedición (ruido, zombies, combate, heridas) y `base_y_losetas.html` para la base, el mapa y el botín.

---

## Índice

1. El juego en una página
2. Componentes
3. Preparación
4. Objetivo, victoria y derrota
5. Los supervivientes
6. El día: las cuatro fases
7. La expedición: mapa, reloj y turno
8. Acciones
9. Ruido y horda
10. Zombies
11. Combate
12. Heridas, sangre y curación
13. Infección
14. Fatiga y acciones pesadas
15. Comida y agua
16. Mochila, objetos y botín
17. La base: entradas, construcción y noche
18. La señal de socorro
19. Resumen de turno (carta de referencia)
20. Lista de decisiones
21. Pendientes
- Anexo A. Tablas por edificio y errantes
- Anexo B. Escenario de entrenamiento (prueba 1)

---

## 1. El juego en una página

Día 30 es un juego cooperativo de supervivencia para 1 a 3 jugadores, de unas 2 horas. El grupo se refugia en una casa sobre la calle Las Heras. Un helicóptero pasará el **día 30**, pero solo los encontrará si la **señal de socorro** está armada y encendida.

Cada día tiene cuatro fases: en la **Base** construyen y curan; en la **Planificación** eligen quién sale y a dónde; en la **Expedición** recorren un barrio armado con losetas, hora por hora, buscando comida, agua, materiales y las piezas de la señal; en el **Regreso y noche** comen, beben y aguantan lo que venga a golpear las puertas.

La tensión central es el **ruido**: lo rápido y lo fuerte es ruidoso, y el ruido atrae zombies en el momento y, si se acumula, trae a la horda.

---

## 2. Componentes

Lista pensada para montar la mesa en Tabletop Simulator.

| Pieza | Cantidad | Uso |
|---|---|---|
| Hoja de la base (plano del refugio) | 1 | Entradas, barricadas, trampas, mejoras, depósito |
| Tablero de calendario | 1 | Días 1 a 30, tramos y marcador de día |
| Tablero de la señal | 1 | 5 etapas |
| Reloj de expedición | 1 | Horas de 07:00 a 21:00 |
| Hojas de superviviente | 1 por superviviente | Atributos, sangre (6), fatiga (3), heridas por zona, mochila (6) |
| Mazo de supervivientes | 7 (provisorio) | Ver sección 5 |
| Mazo de objetos | 74 cartas en 7 familias | Botín (sección 16) |
| Losetas de calle | Recta, Esquina, T, Cruce, Cortada | 3 × 3 zonas cada una |
| Losetas de edificio | 11 tipos | Casa, Almacén, Farmacia, Supermercado, Comisaría, Hospital, Ferretería, Taller, Estación de servicio, Escuela, Plaza |
| Fichas de edificio | 1 por edificio (valores 1 a 6) | Boca abajo hasta entrar |
| Plano de la ciudad | 1 | 5 barrios de destino |
| Figuras de zombie | ~40 | Caminante, Corredor, Bruto, Infectado ácido, Chillón |
| Marcador de estado del zombie | 1 por figura | Tranquilo / Alerta (en TTS: girar la figura o ficha de dos caras) |
| Fichas de daño | ~30 | Debajo de cada zombie |
| Fichas de ruido | 30 | En cada zona |
| Fichas de puerta / ventana / barricada | ~20 | Sobre el borde entre zonas |
| Fichas de construcción | 2 | Gasto diario en la base |
| Fichas de infección | 6 | Nivel de infección (sección 13) |
| Cartas de herida | 20 | Zona + tipo [PROPUESTA: carta física para lo que la hoja ya registra] |
| Dados | 2 d20, 3 d6, 1 d4, 1 d8, 1 d10, 1 d12 | |

---

## 3. Preparación

1. **Base.** Coloca la hoja de la base. Barricadas iniciales [PROPUESTA]: puerta principal nivel 1, puerta del patio nivel 1, ventana de la cocina 0, ventana del dormitorio 0, techo (claraboya) 1. Sin trampas ni mejoras.
2. **Recursos iniciales** [PROPUESTA], en el depósito de la base:

   | Comida | Agua | Medicina | Madera | Clavos | Cuerda | Munición | Combustible |
   |---|---|---|---|---|---|---|---|
   | 8 | 6 | 2 | 2 | 1 | 1 | 0 | 0 |

   Armas en el depósito [PROPUESTA]: 1 Cuchillo de cocina y 1 Bate con clavos. Retira esas cartas del mazo de objetos.
3. **Supervivientes.** Mezcla el mazo de supervivientes y roba **3, o 4 si juegan 3 personas**. Cada jugador elige uno y lo controla. Los que nadie elija se quedan en la base como **supervivientes del grupo**: los maneja la mesa en conjunto. Todos empiezan con sangre 6, fatiga 0 y sin heridas. El resto del mazo queda aparte para los rescates.
4. **Calendario** en el día 1. **Señal** con las 5 etapas sin marcar.
5. **Mazo de objetos.** Mezcla las 74 cartas boca abajo (es la reserva de la que sale el botín, sección 16).
6. **Zombies, fichas y dados** al alcance. Las fichas de edificio se mezclan boca abajo.
7. Empieza el día 1 por la **Fase 1: Base**.

**Jugar solo.** Con 1 jugador hay igual 3 supervivientes en el grupo: tú controlas al que sale, y decides por los que se quedan.

> **Decisión (tamaño del grupo):** la mesa en línea roba 3 supervivientes, la sala deja elegir libremente entre 7 y la hoja de base muestra 4 con 2 jugadores. Se roban 3 (como en la mesa), pero **4 con 3 jugadores**, para que siempre pueda quedar alguien de guardia en la base.

---

## 4. Objetivo, victoria y derrota

**Victoria.** Al empezar el **día 30** (Fase 1: Base) ganan si se cumplen las dos cosas:
- la **señal de socorro está activada** (las 5 etapas marcadas, sección 18), y
- queda **al menos 1 superviviente vivo en la base**.

El helicóptero llega y se los lleva. [PROPUESTA] Grado de victoria para comparar partidas: 1 punto por superviviente rescatado, −1 por cada uno con infección. "Victoria con mordedura" (del simulador) se anota aparte.

**Derrota.**
- Mueren todos los supervivientes del grupo.
- Llega el día 30 y la señal no está activada: el helicóptero pasa de largo.

**Muerte de tu superviviente.** Si muere el superviviente que controlas, tomas el control de uno del grupo que esté en la base. Si no queda ninguno libre, sigues opinando y decidiendo con la mesa hasta que haya un rescate.

---

## 5. Los supervivientes

### 5.1 Atributos

Cuatro atributos de 1 a 5: **Fuerza, Destreza, Constitución y Percepción**.

**Modificador = valor del atributo − 2.**

| Atributo | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Modificador | −1 | 0 | +1 | +2 | +3 |

| Atributo | Para qué sirve |
|---|---|
| Fuerza | Ataque y daño cuerpo a cuerpo |
| Destreza | Ataque con armas de fuego y arrojadizas; Defensa |
| Constitución | Pruebas de resistencia: noche afuera, caídas, infección [PROPUESTA] |
| Percepción | Guardia nocturna (suma su **valor**, no el modificador); Vigilar [PROPUESTA] |

**Prueba de atributo** [PROPUESTA, generaliza la fosa del taller]: d20 + modificador contra 10, salvo que la regla diga otra dificultad. Iguala o supera: éxito.

### 5.2 Valores derivados

| Valor | Cantidad |
|---|---|
| Puntos de acción (PA) | 3 por turno de expedición |
| Sangre | 6 como máximo (igual para todos) |
| Fatiga | 0 a 3 |
| Defensa | 10 + modificador de Destreza (+2 con chaleco antibalas) |
| Mochila | 6 espacios (8 con mochila grande o de montaña) |

### 5.3 Mazo provisorio de supervivientes

| Superviviente | F / D / C / P | Habilidad |
|---|---|---|
| Marta Ríos, enfermera | 2 / 3 / 3 / 4 | **Manos firmes.** Primeros auxilios le cuesta 1 PA en lugar de 2 |
| Raúl Ibarra, ex policía | 4 / 3 / 3 / 2 | **Entrenamiento.** Ventaja en el primer ataque con arma de fuego de cada expedición |
| Sofía Lenz, mecánica | 3 / 4 / 3 / 2 | **Manos de taller.** Forzar o Barricar le cuesta 1 PA y hace un nivel menos de ruido |
| Tomás Ferro, cocinero | 4 / 2 / 4 / 2 | **Raciones.** Una vez por día, 1 Comida alimenta a 2 personajes |
| Nico Vidal, estudiante | 1 / 5 / 2 / 4 | **Ágil.** Sigilo le cuesta 1 PA en lugar de 2 [PROPUESTA: adaptado] |
| Aurelio Pando, cazador | 3 / 3 / 2 / 4 | **Rastreador.** Su Vigilar llega a 2 zonas y no gasta PA una vez por turno [PROPUESTA: adaptado] |
| Elena Quiroga, maestra | 2 / 2 / 3 / 5 | **Calma.** Pendiente: depende de las fichas de voz de la prueba 2. Mientras tanto [PROPUESTA]: una vez por día, un superviviente del grupo quita 1 de fatiga extra al descansar |

> **Decisión (habilidades de Nico y Aurelio):** la habilidad original de Nico ("Correr le cuesta 1 PA en lugar de 2") quedó sin sentido porque Correr ahora cuesta 1 PA (ver sección 8). Se pasa al Sigilo, que es lo caro. La de Aurelio hablaba de "zombies ocultos", que no existen en estas reglas; se adapta a la nueva acción Vigilar.

En la mesa en línea los personajes tienen otros apellidos que en la hoja de base (Julio Benítez, Sofía Paz, Nico Ferrer). **Decisión:** valen los nombres y atributos de `mesa_online.html`, que es la única fuente con atributos.

---

## 6. El día: las cuatro fases

Cada día se juega en este orden. El calendario se divide en tres tramos que cambian las tablas:

| Tramo | Días | Nombre | Valor de tramo |
|---|---|---|---|
| 1 | 1–10 | Aprendizaje | 1 |
| 2 | 11–20 | Presión | 2 |
| 3 | 21–30 | Cuenta regresiva | 3 |

### Fase 1 · Base (amanecer, 07:00)

En este orden:

1. **¿Día 30?** Si es el día 30, comprueben la victoria (sección 4) y termina la partida.
2. **Clima** [PROPUESTA]: tira 1d6. Con 1 o 2 llueve: si tienen Recolector de agua, suman 2 Agua.
3. **Huerta** [PROPUESTA]: si está construida, en los días pares suma 1 Comida.
4. **Infección:** avanza la infección de cada superviviente infectado, salvo que gasten 1 Medicina (sección 13).
5. **Curación:** pueden gastar Medicina para curar heridas (sección 12). También se puede amputar (sección 13).
6. **Construcción:** reciben las fichas de construcción del día (1, o 2 con Taller) y las gastan en barricadas, trampas o mejoras (sección 17). Las fichas no gastadas se pierden.
7. **Señal:** pueden marcar etapas de la señal con los objetos que haya en la base (sección 18).

### Fase 2 · Planificación (07:00)

1. **Quién sale.** Sale **un superviviente por jugador**, y cada jugador lleva al suyo. Un jugador puede dejar a su superviviente en la base y salir con otro del grupo (cambian de control por ese día) [PROPUESTA].
2. **Quién se queda.** Los que se quedan **descansan** (quitan 1 de fatiga esa noche). Uno de ellos puede hacer **guardia**: no descansa, pero suma su Percepción a la defensa de todas las entradas esa noche. Si no queda nadie en la base, no hay guardia ni descanso [PROPUESTA: era pendiente].
3. **Destino.** Eligen un barrio en el plano de la ciudad. Todos los que salen van al mismo barrio [PROPUESTA].

   | Barrio | Tipo | Viaje (horas por tramo) | Peligro | Plantilla | Edificios posibles | Saqueados al empezar |
   |---|---|---|---|---|---|---|
   | Las Acacias | Residencial | 1 | 1 | P3 (3 × 3 losetas) | Casa ×4, Almacén | 2 |
   | Barrio Norte | Escuela y casas | 1 | 1 | T2 (4 × 3) | Escuela, Casa ×2, Farmacia, Almacén | 0 |
   | Centro | Comercios y servicios | 2 | 2 | T1 (4 × 3) | Farmacia, Supermercado, Comisaría, Casa, Almacén, Ferretería | 0 |
   | Parque industrial | Galpones y talleres | 2 | 2 | T3 (5 × 3) | Taller ×2, Estación de servicio, Ferretería, Supermercado, Almacén, Casa | 0 |
   | Hospital San Roque | Zona sanitaria | 3 | 3 | T2 (4 × 3) | Hospital, Farmacia, Plaza, Casa, Almacén | 0 |

   Los edificios que se saquean quedan saqueados para siempre [PROPUESTA: la hoja de base ya lleva la cuenta por barrio].
4. **Equipo.** Cada uno carga su mochila con lo que haya en el depósito (sección 16). La comida y el agua que se llevan se pueden usar afuera, pero lo que no vuelve se pierde.
5. **Salida a las 08:00.**

### Fase 3 · Expedición (08:00 a 21:00)

Se arma el barrio, se juega hora por hora y se vuelve. Ver secciones 7 a 11.

### Fase 4 · Regreso y noche (después de la expedición)

En este orden:

1. **Descargar.** Todo lo que traen en la mochila pasa al depósito. Los rasguños se borran (sección 12).
2. **Comer y beber** (sección 15): Comida y Agua de cada superviviente. Si falta, se aplican las penas.
3. **Sangre y fatiga:** recuperación de sangre (sección 12); los que descansaron quitan 1 de fatiga; se borran las marcas de esfuerzo (sección 14).
4. **Amenaza nocturna:** tirada de ataque a la base y su resolución (sección 17.6).
5. **Diario:** anoten una línea del día. Avanza el calendario un día.

---

## 7. La expedición: mapa, reloj y turno

### 7.1 El mapa

- El barrio se arma con **losetas de 3 × 3 zonas** (cada zona son unos 10 m) siguiendo la plantilla del barrio: R = loseta de calle, B = loseta de edificio. La hoja de base la arma sola; en TTS se puede armar a mano con la misma plantilla.
- **Calles.** Entran y salen siempre por el centro de cada borde, así cualquier loseta encaja con cualquier otra. Las calles que mueren en el borde del mapa siguen hacia afuera.
- **Edificios.** Se colocan al azar en los huecos B, con la puerta hacia una calle vecina. Cada uno recibe una ficha de edificio boca abajo, salvo la Plaza. Los saqueados del barrio se marcan con el sello "Saqueado".
- **Entrada.** El equipo entra por la flecha, en la zona de borde de la primera loseta de calle de la columna izquierda.
- **Movimiento** solo en horizontal y vertical, nunca en diagonal.
- **Bordes entre zonas.** Libre (calle, vereda, patio, paso interno), pared, puerta (abierta o cerrada; con llave o sin llave), ventana (intacta o rota) o barricada.

| Borde | Pasan supervivientes | Pasan zombies | Baja el ruido | Bloquea la vista |
|---|---|---|---|---|
| Libre, puerta abierta, ventana rota | Sí | Sí | No | No |
| Puerta cerrada | Abriéndola | Solo si la derriban | Sí, 1 nivel | Sí |
| Ventana intacta | Rompiéndola | Solo si la derriban | Sí, 1 nivel | **No** (se ve a través) |
| Pared | No | No | Sí, 1 nivel | Sí |
| Barricada [PROPUESTA] | No | Solo si la derriban | Sí, 1 nivel | Sí |

**Zombies al llegar** [PROPUESTA]: antes del primer turno tira en la tabla de errantes (Anexo A) tantas veces como el **peligro** del barrio. Cada resultado se coloca en la zona central de una loseta de calle al azar, sin contar la de entrada. Empiezan tranquilos.

### 7.2 El reloj de la expedición

**Cada turno de expedición es 1 hora** [PROPUESTA: las fuentes no decían cuántos turnos hay por hora].

| Hora | Qué pasa |
|---|---|
| 07:00 | Alba: fases de Base y Planificación |
| 08:00 | Salen de la base |
| 08:00 + viaje | Llegan al barrio: empieza el primer turno |
| 19:00 − viaje | Última hora para salir del barrio y llegar con luz |
| 19:00 | **Anochece** (reglas de noche, abajo) |
| 21:00 | Fin de la expedición: quien no esté en la base pasa la noche afuera |

Con un barrio a 1 hora hay 10 turnos de día (09:00 a 18:00) y 2 de noche. A 3 horas, solo 5 turnos para volver con luz.

**De noche (desde las 19:00):**
- Los zombies solo te detectan en tu misma zona.
- Disparar tiene desventaja.
- Se tira **dos veces** en la tabla de errantes cada hora.
- Al entrar a un edificio se lee la columna del **tramo siguiente** (en el tramo 3 se suma 1 corredor).

**Volver.** Un superviviente en la zona de entrada usa **Salir del barrio** (1 PA, silencio): sale del mapa y llega a la base cuando pasan las horas de viaje. Cada uno puede volver por separado.
- **Viaje de noche** [PROPUESTA]: por cada hora de viaje después de las 19:00, tira 1d6: con 1 o 2, un caminante te alcanza y te ataca una vez (d20 + 2 contra tu Defensa).
- **Noche afuera** [PROPUESTA]: si a las 21:00 sigues en el barrio o viajando, haz una prueba de Constitución contra 12. Si fallas, mueres (desapareces en la noche). Si la pasas, llegas al amanecer siguiente con +2 de fatiga, sin comer ni beber esa noche, y no puedes salir ese día.

### 7.3 El turno

Cada turno (1 hora) tiene 5 pasos, siempre en este orden:

1. **Supervivientes.** Cada superviviente gasta hasta 3 PA. Los jugadores deciden el orden y pueden alternar acción por acción [PROPUESTA]. Cada acción con ruido pone sus fichas en la zona donde termina, al momento.
2. **Zombies.** Cada zombie actúa una vez (sección 10).
3. **Horda.** Si una zona de calle, o un edificio sumando todas sus zonas, tiene 5 o más fichas de ruido, llega la horda (sección 9).
4. **Disipación.** Quita 1 ficha de ruido de cada zona que tenga fichas.
5. **Reloj.** Cada laceración sin vendar quita 1 de sangre. Avanza el reloj 1 hora y tira en la tabla de errantes (sección 10.5). Se renuevan los PA (2 si estás aturdido), se termina "escondido" y se puede volver a Correr.

> **Decisión (aparición de zombies):** el kit de la prueba 1 hace aparecer un caminante con un 1 en d6 (1 o 2 de noche). La hoja de base usa la tabla de errantes por hora en la loseta más ruidosa. Se adopta **la tabla de errantes**, porque escala con el tramo y con el ruido. La regla del d6 queda solo para el escenario de entrenamiento (Anexo B).

---

## 8. Acciones

Con 3 PA por turno puedes repetir acciones. El ruido se aplica en la zona donde termina la acción.

### 8.1 Movimiento

| Acción | PA | Ruido | Efecto |
|---|---|---|---|
| Sigilo | 2 | Silencio | Te mueves 1 zona. No se puede si hay un zombie en tu zona |
| Caminar | 1 | Bajo | Te mueves 1 zona |
| Correr ▲ | 1 | Medio | Te mueves 1 o 2 zonas. Una vez por turno. No con herida en las piernas ni con fatiga 2 o más |
| Esconderse | 1 | Silencio | Hasta tu próximo turno solo te detectan zombies de tu zona. Termina tu turno. Se puede usar con zombies en tu zona, pero esos te siguen viendo |
| Salir del barrio | 1 | Silencio | Solo en la zona de entrada. Empiezas el viaje de vuelta. Con la mochila llena deja 1 marca de esfuerzo ▲ |

▲ = acción pesada: deja 1 marca de esfuerzo (sección 14).

> **Decisión (coste de Sigilo y Correr):** la carta de acción "Movimiento y sigilo" pone Sigilo a 1 PA por 1 zona y Correr a 2 PA por 2 zonas; así Correr nunca conviene (mismo coste por zona y además hace ruido). Se adopta el esquema del kit de prueba 1 y su simulador: **Sigilo 2 PA silencioso, Caminar 1 PA bajo, Correr 1 PA por 2 zonas con ruido medio**. Hay que actualizar la carta.
>
> **Decisión (Huir):** la carta tenía "Huir · 1 PA · ruido medio: sales por la salida más cercana". Se elimina: Correr ya cubre ese uso y no hay restricción para salir de una zona con zombies.

### 8.2 Puertas y obstáculos

| Acción | PA | Ruido | Efecto |
|---|---|---|---|
| Abrir puerta | 1 | Bajo | Abre una puerta sin llave adyacente |
| Cerrar puerta | 1 | Bajo | Cierra una puerta abierta adyacente (no una derribada) |
| Forzar ▲ | 2 | Medio | Abre una puerta con llave, trabada o una reja. Sin tirada. Con palanca o hacha: 1 PA |
| Romper ventana ▲ | 1 | Alto | La ventana queda abierta para siempre |
| Barricar ▲ [PROPUESTA] | 2 | Medio | Gasta 1 Madera: una abertura adyacente pasa a barricada |

El ruido de las acciones sobre aberturas se hace en la zona donde estás.

### 8.3 Combate

| Acción | PA | Ruido | Efecto |
|---|---|---|---|
| Atacar | 1 | El del arma | Sección 11. Sin arma: d20 + Fuerza, daño 1 [PROPUESTA]. Con un arma cuerpo a cuerpo de 2 espacios es pesada ▲ |
| Destrabar | 1 | Silencio | Arregla un arma de fuego encasquillada |
| Distraer [PROPUESTA] | 1 | Ver efecto | Lanzas algo a una zona a 2 o menos que veas: ruido **medio** en esa zona, no en la tuya. Gasta una carta cualquiera de la mochila. Con Bengala: ruido **alto** y alcance 3. Con megáfono: ruido medio, alcance 4, no se gasta |

### 8.4 Objetos y cuidado

| Acción | PA | Ruido | Efecto |
|---|---|---|---|
| Registrar | 2 | Bajo | Gasta 1 registro del edificio y tira d20 en su tabla (sección 16). No con zombies en tu zona |
| Primeros auxilios | 2 | Bajo | Gasta 1 Medicina, a ti o a alguien de tu zona: detiene una laceración, **o** recupera 1 de sangre, **o** limpia un rasguño infectado (hospital, ficha 6) y quita esa infección |
| Comer o beber [PROPUESTA] | 1 | Silencio | Gasta 1 Comida o 1 Agua: borras tus marcas de esfuerzo. Una vez por expedición |
| Intercambiar [PROPUESTA] | 1 | Silencio | Pasas o recibes objetos con alguien de tu zona |
| Vigilar [PROPUESTA] | 1 | Silencio | Miras en secreto la ficha de un edificio cuya puerta está en una zona adyacente. No se colocan sus zombies hasta que alguien entre |
| Soltar | 0 | Silencio | Dejas un objeto en tu zona. Se puede recoger después (1 PA) |

> **Decisión (Primeros auxilios):** la carta de Medicina dice 1 PA y el kit de prueba dice Vendar 2 PA. Se queda **2 PA**: con 1 PA la habilidad de Marta no tendría efecto.
>
> **Decisión (analgésicos):** en el kit, el analgésico era una acción aparte (1 PA, +1 sangre). En el mazo, vendas, analgésicos, desinfectante y antibióticos son todos **Medicina**. Se une todo en Primeros auxilios, que deja elegir entre parar la laceración o recuperar sangre.

---

## 9. Ruido y horda

El ruido hace dos cosas: **en el momento** atrae a los zombies que lo oyen, y **acumulado** en fichas puede traer a la horda.

| Nivel | Alcance | Fichas que deja |
|---|---|---|
| Silencio | 0 zonas | 0 |
| Bajo | 1 zona | 1 |
| Medio | 2 zonas | 1 |
| Alto | 3 zonas | 2 |
| Máximo | Todo el mapa | 3 |

**Cómo se propaga** (igual que el simulador): desde la zona de origen, el ruido avanza zona por zona. Cada vez que cruza una pared, una puerta cerrada, una ventana intacta o una barricada, baja 1 nivel para lo que está del otro lado. Llega a un zombie si la distancia recorrida no supera el alcance del nivel que le queda. Una puerta abierta o una ventana rota no lo bajan. Por eso el ruido bajo dentro de un edificio cerrado no sale.

**Pifia.** Un 1 natural al atacar deja 1 ficha de ruido extra en tu zona.

**Horda (umbral: 5 fichas).** En el paso de Horda, se cuentan las fichas de cada zona de calle por separado y, en cada edificio, la suma de todas sus zonas. Si algún total llega a 5:
1. Aparecen 3 caminantes en la zona de borde del mapa más cercana a ese lugar (si hay empate, al azar). [PROPUESTA] En el tramo 2 se suma 1 corredor; en el tramo 3, 1 corredor y 1 caminante más.
2. Se quitan todas las fichas de ese lugar.

**Disipación.** Al final de cada turno se quita 1 ficha de cada zona. El ruido aislado se olvida; el ruido seguido se acumula.

---

## 10. Zombies

### 10.1 Tipos

| Tipo | Defensa | Vitalidad | Ataque | Movimiento | Especial |
|---|---|---|---|---|---|
| Caminante | 8 | 5 | d20 + 2 | 1 zona | Llega en grupo |
| Corredor | 12 | 4 [PROPUESTA] | d20 + 2 [PROPUESTA] | 2 zonas | Se mueve 2 zonas por activación (paso a paso, puede cambiar de objetivo entre pasos) |
| Bruto | 10 | 10 [PROPUESTA] | d20 + 3 [PROPUESTA] | 1 zona | Siempre empieza en la habitación más lejana. Con chaleco (comisaría 6): +2 Defensa |
| Infectado ácido | 9 | 5 [PROPUESTA] | d20 + 2 [PROPUESTA] | 1 zona | Si te hiere, además se rompe un objeto de tu mochila (lo eliges tú) |
| Chillón | 8 | 3 [PROPUESTA] | d20 + 1 [PROPUESTA] | 1 zona | Si en la fase de zombies te detecta, chilla en lugar de moverse: ruido máximo en su zona y aparece 1 caminante en la puerta del edificio (o en el borde de su loseta si está en la calle) |

"Vitalidad" es el daño que aguanta: cuando el daño acumulado llega a ese número, cae. El daño se marca con fichas debajo de la figura.

### 10.2 Tranquilo o alerta

Cada zombie está **tranquilo** o **alerta**. Pasa a alerta cuando te detecta, se mueve hacia un ruido, ataca o recibe un ataque. Vuelve a tranquilo en cualquier fase de zombies en que no detecte a nadie ni oiga nada. Los zombies que se colocan al revelar un edificio, al llegar al barrio o como errantes empiezan **tranquilos**. Los que llegan con la horda o con "¡Aaah!" empiezan **alerta** [PROPUESTA].

### 10.3 Detección

Un zombie te detecta si:
- está en tu zona, o
- está en una zona adyacente sin pared ni puerta cerrada de por medio (una ventana intacta **no** tapa la vista).

De noche y si estás escondido, solo te detecta en tu misma zona.

### 10.4 Qué hace cada zombie

En la fase de zombies, cada zombie hace **lo primero que se cumpla**:

1. **Si hay un superviviente en su zona, ataca.** Si hay varios, ataca al que hizo más ruido este turno en esa zona; si empatan, eligen los jugadores [PROPUESTA].
2. **Si oyó ruido este turno, se mueve 1 zona hacia el ruido** de nivel más alto que le llegó. Si hay empate, hacia el más cercano.
3. **Si detecta a un superviviente, se mueve 1 zona hacia él** (el más cercano).
4. Si no, se queda quieto.

El ruido "de este turno" es el de todas las acciones de todos los supervivientes en el paso 1 del turno.

**Rutas y puertas.** Los zombies no abren puertas ni pasan por paredes. Van por la ruta más corta, donde cada puerta cerrada (con llave o sin llave), barricada o ventana intacta cuenta como 4 zonas. En la práctica: rodean por una abertura pasable si el rodeo es de hasta 4 zonas más; si es más largo, van a golpear la abertura cerrada. Un zombie que quiere cruzar una abertura cerrada tira 1d6: con 6 la derriba y queda abierta (rota) para siempre; si no, se queda donde está.

> **Decisión (qué derriban los zombies):** el kit solo habla de puertas cerradas y de "rodear por la abertura más cercana"; el simulador deja que derriben también la vidriera y la puerta con llave, y prefiere golpear si rodear cuesta más de 4 pasos. Se adopta **el simulador**, escrito como regla.

**Figuras.** Si se acaban las figuras de un tipo, no aparecen más de ese tipo [PROPUESTA].

**Ataque del zombie.** Tira su ataque contra tu Defensa. Si iguala o supera, recibes una herida (sección 12). Cada zombie de tu zona ataca una vez.

### 10.5 Errantes

En el paso de Reloj de cada turno, tira 1d6 en la **tabla de errantes** (Anexo A), columna del tramo, en la **loseta de calle con más fichas de ruido** (si hay empate, la más cercana al equipo). Los errantes aparecen en el borde de esa loseta: en una salida de calle al azar [PROPUESTA]. De noche se tira dos veces.

---

## 11. Combate

**Atacar** cuesta 1 PA. Tira d20 + modificador contra la Defensa del zombie. Si iguala o supera, aciertas y tiras el daño del arma. Cuando el daño acumulado llega a la vitalidad, el zombie cae.

- **Modificador de ataque:** Fuerza con armas cuerpo a cuerpo; Destreza con armas de fuego y arrojadizas.
- **Daño:** cuerpo a cuerpo, dado del arma + modificador de Fuerza (mínimo 1). Armas de fuego y arrojadizas, solo el dado.
- **Alcance:** cuerpo a cuerpo, solo zombies de tu zona. Armas de fuego, tu zona o hasta 2 zonas por aberturas pasables. Eliges a qué zombie atacas.
- **Ventaja:** atacas a un zombie tranquilo (por la espalda). Tiras 2d20 y usas el mejor.
- **Desventaja:** tienes una herida en el brazo derecho, disparas de noche o atacas en una zona a oscuras. Tiras 2d20 y usas el peor.
- Ventaja y desventaja juntas se anulan: tiras 1d20.
- **Crítico (20 natural):** aciertas siempre y haces el daño máximo del arma (dado máximo + Fuerza en cuerpo a cuerpo), sin tirar.
- **Pifia (1 natural):** fallas siempre y dejas 1 ficha de ruido extra. Un arma de fuego, además, se encasquilla: cuesta 1 PA destrabarla.
- **Ruido:** el ataque hace el ruido de su arma, aciertes o no.
- **Munición:** cada disparo gasta 1 disparo. Una carta de Munición son 3 disparos (márcalos con fichas sobre la carta).

### 11.1 Armas

| Arma | Esp. | Daño | Ruido | Notas |
|---|---|---|---|---|
| Cuchillo de cocina | 1 | d4 + F | Silencio | |
| Bisturí | 1 | d4 + F | Silencio | Permite amputar en la base |
| Bate con clavos / bate de sóftbol | 2 | d6 + F | Bajo | |
| Martillo, Tonfa, Llave inglesa | 1 | d6 + F | Bajo | |
| Hacha de bombero | 2 | d8 + F | Medio | Forzar cuesta 1 PA |
| Pistola | 1 | d10 | Máximo | Fuego. Alcance 2 |
| Escopeta | 2 | d12 | Máximo | Fuego. Alcance 2 |
| Motosierra | 2 | 2d8 + F | Máximo | Gasta 1 Combustible por expedición |
| Botella incendiaria | 1 | d10 a cada zombie de una zona | Alto | Arrojadiza, alcance 2, un uso |

> **Decisión (daño y ruido de las armas):** el kit usa bate d6 con ruido **medio** y pistola con 6 balas; las cartas y las tablas de botín ponen el bate en ruido **bajo**, y agregan hacha d8 y escopeta d12. Se adopta la versión de las cartas y tablas, que además deja una escalera limpia: **silencio d4, bajo d6, medio d8, máximo d10–d12**. El modificador de Fuerza suma al daño cuerpo a cuerpo (como en el kit y el simulador); las armas de fuego no suman nada.
>
> **Decisión (espacios):** la tabla de la casa dice que el bate ocupa 1 espacio; la carta y el kit dicen 2. Vale **la carta**.
>
> **Decisión (munición):** el kit da 6 balas a la pistola; el mazo dice 1 Munición = 3 disparos. Vale **el mazo**. Una pistola encontrada "con munición ×1" trae 1 carta de Munición.

**Lo que hay que observar.** Contra un caminante (Fuerza 3), el cuchillo mata de un golpe el 25 % de las veces que acierta y es silencioso; el bate, el 50 %; la pistola, el 60 % de las veces que acierta, pero acierta el 70 %: **mata de un disparo el 42 %** de las veces (55 % con ventaja) y se oye en todo el mapa. (El kit decía "60 %": ese número es solo el daño, sin contar el acierto.) Si una opción gana siempre, hay que tocar los números.

---

## 12. Heridas, sangre y curación

### 12.1 Recibir una herida

Cada golpe recibido son dos tiradas de d6: una para la **zona** y otra para el **tipo**. Toda herida resta **1 de sangre** al recibirla. Toma una carta de herida o anótala en la hoja.

| d6 | Zona | Al recibirla (si no es rasguño) | Mientras dure la herida (si no es rasguño) |
|---|---|---|---|
| 1 | Cabeza | **Aturdido:** tu próximo turno tienes 2 PA | — (cuenta para la muerte por segunda herida en la cabeza) |
| 2–3 | Torso | Pierdes 1 sangre extra | — |
| 4 | Brazo izquierdo | Si la mochila queda excedida, sueltas objetos al momento | La mochila tiene 1 espacio menos |
| 5 | Brazo derecho | — | Desventaja al atacar |
| 6 | Piernas | — | No puedes Correr |

| d6 | Tipo | Efecto |
|---|---|---|
| 1–2 | Rasguño | Solo la sangre. Sin efecto de zona. Se borra al volver a la base |
| 3–4 | Laceración | Pierdes 1 sangre en cada paso de Reloj hasta detenerla con Primeros auxilios. Tiene efecto de zona |
| 5 | Fractura | Efecto de zona |
| 6 | Mordedura | Efecto de zona y **infección** (sección 13) |

Los efectos de zona de laceraciones, fracturas y mordeduras duran **hasta que la herida se cura en la base**, aunque la laceración esté vendada (así lo hace el simulador).

**Muerte.** Mueres si tu sangre llega a 0, o si recibes una herida en la cabeza mientras ya tienes otra herida en la cabeza sin curar (sea del tipo que sea, rasguño incluido).

> **Decisión (sangre por heridas de cabeza y torso):** la mesa en línea resta 3 de sangre por cualquier herida en la cabeza y 2 por el torso. El kit y el simulador restan 1 por herida, 1 extra en el torso (salvo rasguño), aturden con la cabeza y matan con la segunda herida en la cabeza. Se adopta **el kit y el simulador**, que son las reglas probadas; con 6 de sangre, −3 por un golpe en la cabeza es demasiado azar. En los dos casos el torso termina costando 2: la mesa en línea debe pasar a "−1 por herida, +1 en torso salvo rasguño".

### 12.2 Recuperar sangre y curar

- **En expedición:** Primeros auxilios (sección 8.4).
- **Por la noche** [PROPUESTA]: cada superviviente que comió y bebió y no tiene laceraciones sin vendar recupera 1 de sangre. Si además descansó en la base ese día, recupera 1 más. Una laceración sin vendar al llegar a la base se puede vendar gratis con 1 Medicina; si no, quita 1 de sangre esa noche.
- **Curar una herida (Fase de Base):** 2 Medicinas quitan 1 carta de herida (laceración, fractura o mordedura; la mordedura curada **no** quita la infección).
- **Fractura** [PROPUESTA]: además de las 2 Medicinas, el superviviente no puede salir de expedición ese día.

---

## 13. Infección

Una mordedura infecta. Pon una ficha de infección en el **nivel 1** del superviviente. (En el Hospital, ficha 6, cualquier rasguño también infecta.)

En cada Fase de Base, la infección sube 1 nivel salvo que el grupo gaste **1 Medicina** por ese superviviente (frena la infección 1 día).

| Nivel | Efecto [PROPUESTA] |
|---|---|
| 1 | Sin efecto visible |
| 2 | Fiebre: +1 de fatiga cada día |
| 3 | Delirio: 2 PA por turno de expedición y no puede hacer guardia |
| 4 | Muere y se levanta **esa noche dentro de la base**: un caminante (en el tramo 3, un infectado ácido) aparece en la base y se resuelve como una irrupción sin entrada (sección 17.6) |

**Amputar** [PROPUESTA] (Fase de Base, solo si la mordedura está en un brazo o en las piernas): gasta 1 Medicina y usa un bisturí. Quita la infección y la carta de mordedura, cuesta 2 de sangre y el efecto de esa zona queda **para siempre**. Con hacha o cuchillo en lugar de bisturí: además, prueba de Constitución contra 12 o recibes una laceración en la misma zona. Una mordedura en la cabeza o el torso no se puede amputar.

> **Decisión (antibióticos):** las tablas nombran antibióticos que "frenan la infección" y la hoja de cartas pregunta si deben ser una carta única. Por ahora **todo es Medicina** (1 Medicina frena la infección 1 día, como dice la carta). Si las partidas muestran que la infección es una condena demasiado barata o demasiado cara, los antibióticos pasan a carta única que la cura.

---

## 14. Fatiga y acciones pesadas

La fatiga va de 0 a 3 y se anota en la hoja. En la expedición no se gana por salir, sino por **esfuerzo**: algunas acciones son **pesadas** (símbolo **▲** en las tablas y en la carta de referencia).

### 14.1 Acciones pesadas y contador de esfuerzo

Cada vez que haces una acción pesada, pones **1 marca de esfuerzo** en tu hoja (en TTS, un contador de 0 a 4 junto a la fatiga).

| Acción pesada ▲ | Marcas | Origen |
|---|---|---|
| Forzar | 1 | Idea del autor |
| Romper ventana | 1 | [PROPUESTA] |
| Barricar | 1 | [PROPUESTA] |
| Correr | 1 | [PROPUESTA] |
| Atacar con un arma cuerpo a cuerpo de 2 espacios (bate, hacha, motosierra) | 1 | [PROPUESTA] |
| Cargar a un herido o a un rescatado que no puede moverse solo, por cada zona (no con camilla) | 1 | [PROPUESTA] |
| Salir del barrio con la mochila llena (todos los espacios ocupados) | 1 | [PROPUESTA] |

**Umbral: 4 marcas = +1 de fatiga.** Al llegar a 4, sumas 1 de fatiga al momento y borras las 4 marcas; si sobran, siguen contando.

**Reinicio:** las marcas que queden por debajo de 4 se borran en la Fase 4 de cada día. No pasan al día siguiente.

**Respiro** [PROPUESTA]: la acción Comer o beber (1 PA, silencio, una vez por expedición) borra todas tus marcas de esfuerzo.

En la base no hay contador: cavar la fosa tapada da +1 de fatiga directo (de la hoja de base).

### 14.2 Otras formas de ganar fatiga

- +1 si llegas a la base después de las 19:00. [PROPUESTA]
- +2 por pasar la noche afuera. [PROPUESTA]
- +1 por noche sin comer. [PROPUESTA]
- +1 por día con infección en nivel 2. [PROPUESTA]
- +1 por cavar la fosa tapada (de la hoja de base).

### 14.3 Quitar fatiga

- **Descansar:** quien se queda en la base sin hacer guardia quita 1 de fatiga en la Fase 4 (de la hoja de base). El guardia no descansa.
- Quien duerme sin cama no descansa (sección 17.5).

### 14.4 Efectos por nivel

| Fatiga | Efecto |
|---|---|
| 0 | Ninguno |
| 1 | Esa noche come 2 Comidas en lugar de 1 (de la hoja de base y la carta de Comida) |
| 2 | Come 2 y **no puede Correr** [PROPUESTA] |
| 3 | **Agotado:** come 2, no puede Correr, tiene **2 PA** por turno de expedición, no puede hacer guardia ni cavar [PROPUESTA] |
| Más de 3 | No se anota: cada punto que no se puede sumar cuesta **1 de sangre** [PROPUESTA] |

La comida doble se calcula con la fatiga que tienes **antes** de descansar esa noche.

**Habilidad de Sofía Lenz (Manos de taller).** Forzar y Barricar le cuestan 1 PA, hacen un nivel menos de ruido y **para ella no son pesadas** [PROPUESTA]. La palanca y el hacha también bajan Forzar a 1 PA, pero no le quitan el ▲. Para Sofía no se suman: Forzar no baja de 1 PA.

> **Decisión (fatiga en expedición, idea de Santiago):** las fuentes dicen que la fatiga va de 0 a 3, que descansar quita 1, que cavar la fosa da 1 y que con fatiga se come doble, pero no cómo se gana afuera ni qué hace cada nivel. Se adopta la idea del autor de **acciones pesadas**: cada una deja 1 marca y **4 marcas dan +1 de fatiga**. Se eligió 4 porque una expedición típica (10 a 12 turnos) tiene entre 3 y 6 acciones pesadas: jugar con cuidado no cansa; abusar de Correr y Forzar da 1 o 2 de fatiga. El contador se borra cada día para no llevar cuentas largas; la fatiga en sí queda. Esto reemplaza el "+1 fijo por expedición" del primer borrador, que hacía que quien sale comiera doble siempre. Correr es pesada porque es la acción que más se repite: así la velocidad tiene un segundo coste además del ruido. Sofía, la especialista en forzar y barricar, no acumula esfuerzo con esas dos acciones, para que su habilidad siga valiendo aunque el grupo tenga palanca u hacha.

---

## 15. Comida y agua

En la Fase 4, después de descargar:

- **Comida:** cada superviviente come 1 Comida, o 2 si tiene fatiga (antes de quitar la fatiga del descanso). La habilidad de Tomás permite que, una vez por día, 1 Comida alimente a 2.
- **Agua** [PROPUESTA]: el grupo bebe **1 Agua por cada 2 supervivientes** vivos, redondeando hacia arriba (3 supervivientes: 2 Agua). La fatiga no cambia el agua.

**Si falta** [PROPUESTA]:
- Cada superviviente que no come gana 1 de fatiga y no recupera sangre esa noche.
- Si falta agua, **todos** los supervivientes pierden 1 de sangre y no recuperan sangre esa noche. Dos noches seguidas sin agua: además, +1 de fatiga cada uno.

> **Decisión (consumo de agua):** las fuentes dejan el agua "sin consumo definido (sección 12)". Se propone medio Agua por persona y día porque en las tablas de botín el agua sale bastante menos que la comida (en la casa, 2 resultados de 20 contra 3; en el almacén, 3 contra 7). Su falta castiga más que la de comida (sangre en lugar de fatiga) para que siga siendo un recurso que importa. Con lluvia y recolector se recupera agua sin salir.

---

## 16. Mochila, objetos y botín

### 16.1 Mochila

- 6 espacios (8 con mochila grande o mochila de montaña, que no ocupan espacio). Una herida en el brazo izquierdo quita 1 espacio.
- Cada carta ocupa los espacios que marcan sus cuadros. Si un efecto te deja con más peso del que puedes llevar, sueltas cosas al momento hasta entrar.
- Al encontrar algo que no entra, sueltas otra cosa o lo dejas en la zona.

### 16.2 El mazo de objetos

74 cartas en 7 familias. En las familias de recursos, las variantes cambian de dibujo y de nombre pero **cuentan igual**: todo lo que lleva el sello Medicina es 1 Medicina.

| Familia | Cartas | Esp. | Regla |
|---|---|---|---|
| Medicina | 10 | 1 | 1 Medicina. En expedición: Primeros auxilios. En la base: 2 curan una herida, 1 frena la infección 1 día |
| Comida | 15 | 1 | 1 Comida |
| Agua | 8 | 1 | 1 Agua |
| Armas | 7 | según arma | Cada una con su daño y ruido (sección 11.1) |
| Recursos | 20 | 1–2 | Munición (3 disparos), Madera (Tablones = 2 Madera, 2 esp.), Clavos, Chapa (2 esp.), Alambre, Cuerda, Semillas, Combustible (2 esp.) |
| Señal | 4 | 1–2 | Radio portátil (etapa 1), Generador (etapa 2), Manual técnico y GPS de mano (etapa 4) |
| Equipo | 10 | 0–1 | Walkie-talkie, Baterías, Bengala, Mochila de montaña |

### 16.3 Entrar a un edificio

1. **Revelar.** Se da vuelta la ficha del edificio (1 a 6) la primera vez que **una abertura del edificio queda abierta, la abra un superviviente o la derribe un zombie**, o cuando alguien entra por primera vez. Se busca la fila en la tabla de ese tipo (Anexo A).

   > **Decisión (revelar):** el kit dice "la primera vez que abres una abertura" y el simulador solo revela con acciones del jugador; si un zombie derribaba la puerta, se entraba sin tirar la ficha. Se revela también en ese caso.
2. **Colocar zombies.** Se usa la columna del tramo (de noche, la del tramo siguiente; en el tramo 3 de noche, +1 corredor). Se reparten de a uno por las habitaciones, de la más lejana a la puerta hacia la más cercana. Bruto y chillón van a la más lejana. Empiezan tranquilos. Aplica la nota de la fila (puerta trabada, oscuridad, trampa…).
3. **Registrar.** Cada Registrar (2 PA, ruido bajo) gasta 1 de los registros del edificio y tira d20 en su tabla de botín (con ventaja o desventaja si la fila lo dice). No se puede registrar con zombies en tu zona. Se registra en cualquier habitación del edificio.
4. **Saqueado.** Cuando se gastan todos los registros, el edificio queda saqueado. Lo que no entra en la mochila se queda ahí.

### 16.4 Del resultado a la carta

> **Decisión (botín):** el kit de prueba usa tablas de d6 por zona y la hoja de base usa una tabla de d20 por tipo de edificio, mientras que el mazo de objetos es "lo que sale al usar Registrar". Se unen así: **la tabla de d20 dice qué encuentras y el mazo da la carta física**. Las tablas de d6 del kit quedan solo para el escenario de entrenamiento.

- Busca en el mazo una carta de la familia que corresponda y tómala. **Los espacios se cuentan siempre por carta**, con el valor de la carta; la columna de espacios de las tablas es orientativa (por ejemplo, el Generador ocupa 2, como su carta, no 4). Un resultado "×2" son 2 cartas (cada una ocupa lo suyo). "Botiquín completo" son 2 Medicinas.
- Vendas, analgésicos, desinfectante, antibióticos y kit de sutura son **Medicina**. Latas y snacks son **Comida**.
- Si la carta pedida ya no está en el mazo (salió antes), no encuentras eso [PROPUESTA].
- **Objetos sin carta todavía** (linterna, palanca, soplete, chaleco, tonfa, martillo, megáfono, mapa de rutas, camilla, batería de auto, motosierra, botella incendiaria…): se anotan en una carta en blanco con el texto de la tabla [PROPUESTA]. La linterna anula la desventaja por oscuridad [PROPUESTA].
- **¡Aaah!** El zombie aparece en tu zona, alerta. No ataca hasta la fase de zombies.
- **Rescate:** roba un superviviente del mazo. Se suma al grupo y viaja con ustedes (no lo controla nadie hasta llegar; [PROPUESTA] cuenta como superviviente sin acciones que sigue al que lo encontró, y los zombies también pueden atacarlo).
- **Objetos de uso suelto** [PROPUESTA]: Libreta de fiado, Mensaje en el pizarrón y Mapa escolar revelan fichas de edificio (miras la ficha sin colocar zombies, como Vigilar). Mapa de rutas: el próximo viaje cuesta 1 hora menos por tramo. Fósforos y velas: la base cuenta como si tuviera guardia con Percepción 1 una noche, y se descartan. Batería de auto y Baterías: hacen funcionar walkie-talkies. Walkie-talkie: sin efecto hasta las acciones ocultas (prueba 2).
- **Infectado ácido y Clavos:** el objeto que "rompe" el ácido queda **dañado** (gira la carta): no se puede usar ni cuenta como recurso. En la base, 1 Clavos lo repara [PROPUESTA; así la carta de Clavos tiene uso].
- Los materiales que la tabla da para la base (madera, clavos, chapa, alambre, cuerda, combustible, semillas) se guardan en el depósito al volver.

> **Decisión (recursos de la base):** la mesa en línea agrupa todo como "Materiales"; la hoja de base y el mazo los separan en 7 tipos. Se separan, porque cada barricada, trampa y mejora pide materiales concretos. La mesa en línea debe actualizar su contador.

---

## 17. La base

El refugio es una casa con patio sobre la calle Las Heras: dormitorio, cocina, sala común (con la mesa de planificación y la radio), patio y acceso al techo.

### 17.1 Entradas y defensa

Cinco entradas: **puerta principal, puerta del patio, ventana de la cocina, ventana del dormitorio y techo (claraboya)**.

**Defensa de una entrada = nivel de barricada (0 a 3) + trampa + Percepción del guardia.**

### 17.2 Fichas de construcción

Cada día reciben **1 ficha de construcción** (2 con Taller). Cada barricada, trampa o mejora gasta 1 ficha más sus materiales. Las fichas no se guardan de un día al otro.

### 17.3 Barricadas

Para subir 1 nivel una entrada (máximo 3):

| Del nivel | Al nivel | Cuesta | Qué es |
|---|---|---|---|
| 0 | 1 | 1 Madera, 1 Clavos | Tablones clavados |
| 1 | 2 | 2 Madera, 1 Clavos | Doble tablón |
| 2 | 3 | 1 Chapa, 1 Clavos | Blindaje de chapa |

### 17.4 Trampas

Una trampa por entrada. Suma a la defensa de esa entrada.

| Trampa | Cuesta | Defensa | Dónde | Efecto |
|---|---|---|---|---|
| Alarma de latas | 1 Cuerda, 1 Alambre | +1 | Puertas, ventanas, techo | Si algo entra por acá, nadie queda sorprendido durmiendo |
| Estacas | 2 Madera, 1 Clavos | +1 | Puertas, ventanas | El primer zombie que entra recibe d6 de daño |
| Alambre de púas | 2 Alambre | +2 | Ventanas, techo | Los corredores que entran por acá pierden su ataque en la primera ronda [adaptado: en la base no hay zonas] |
| Fosa tapada | 1 Madera, 1 Cuerda, +1 fatiga a alguien de la base con fatiga menor que 2 | +2 | Puertas | El primer zombie cae y queda fuera del evento |
| Trampa incendiaria | 1 Combustible, 1 Cuerda | +3 | Puertas | La primera noche que algo ataca esta entrada se enciende: +3 a la defensa. Después se borra |

### 17.5 Mejoras permanentes

| Mejora | Cuesta | Efecto |
|---|---|---|
| Taller | 2 Madera, 2 Clavos, 1 Chapa | 2 fichas de construcción por día |
| Huerta | 2 Madera, 1 Semillas, 2 Agua | Comida extra cada pocos días: +1 Comida en los días pares [PROPUESTA] |
| Recolector de agua | 2 Chapa, 1 Alambre | Agua extra cuando llueve: +2 Agua con 1–2 en el d6 de clima [PROPUESTA] |
| Cama extra | 2 Madera, 1 Clavos, 1 Cuerda | Lugar para un rescatado más |

**Camas** [PROPUESTA]: la base tiene 4 camas. Cada Cama extra suma 1. Quien duerme sin cama no descansa (no quita fatiga).

### 17.6 La noche: amenaza y ataque a la base [PROPUESTA]

Las fuentes definen la defensa de cada entrada pero no cómo se ataca. Esta es la propuesta completa.

**1. Tirada de amenaza.** 1d6 + valor de tramo (1, 2 o 3), más:
- +1 si alguien llegó a la base después de las 19:00;
- +2 si hoy se encendió el generador en la base;
- +3 si la señal está activada (etapa 5).

| Total | Esa noche |
|---|---|
| 4 o menos | Noche tranquila |
| 5–6 | 1 ataque |
| 7–8 | 2 ataques |
| 9 o más | 3 ataques (horda: suma 1 corredor al primero) |

**2. Cada ataque.** Elige la entrada con 1d6: 1 puerta principal, 2 puerta del patio, 3 ventana de la cocina, 4 ventana del dormitorio, 5 techo, 6 la de menor defensa. Dos ataques pueden caer en la misma entrada.

**Fuerza del ataque = 1d6 + valor de tramo + 1.** Si se activa una trampa incendiaria, se suma su +3 a la defensa en ese momento.

- **Fuerza menor o igual que la defensa:** los rechazan. Nada más.
- **Fuerza mayor que la defensa: irrupción.** La barricada de esa entrada baja 1 nivel (si tenía). Entra 1 caminante, más 1 por cada 2 puntos de diferencia. En el tramo 3, uno de ellos es corredor.

**3. Combate en la base.** Se resuelve por rondas, sin PA ni ruido:
1. Aplica las trampas de esa entrada (estacas, fosa, púas).
2. **Sorpresa:** si no hay guardia ni alarma de latas en esa entrada, cada zombie hace un ataque gratis con ventaja contra un superviviente al azar.
3. **Ronda:** cada superviviente de la base ataca una vez con el arma que tenga (las del depósito se reparten antes de la noche); luego cada zombie que siga en pie ataca una vez a un superviviente (el guardia primero, después al azar). Se repite hasta que no queden zombies.
4. Las heridas se tiran como en la expedición.

---

## 18. La señal de socorro

Cinco etapas, en orden. Cada etapa se marca en la Fase de Base, con los objetos ya en la base.

| Etapa | Qué es | Cómo se cumple | Dónde se encuentra |
|---|---|---|---|
| 1 | Radio o antena | Llevar a la base una radio o antena | Radio portátil (mazo); radio de la guardia (comisaría 18); antena y cable coaxial (ferretería 17); radio del laboratorio (escuela 19) |
| 2 | Energía | Un generador y 1 Combustible | Generador (mazo; ferretería 18, hospital 18, taller 18). Encenderlo en la base es ruido máximo: +2 a la amenaza de esa noche |
| 3 | Baliza o fuego de señal | Entregar 1 Bengala, **o** armar un fuego de señal en el techo: 2 Madera + 1 Combustible + 1 ficha de construcción [PROPUESTA] | Bengalas (comisaría 19, estación de servicio 17, mazo) |
| 4 | Mensaje | Un Manual técnico **o** un GPS: con uno alcanza | Manual (mazo; escuela 18); GPS (mazo; taller 19, estación de servicio 19) |
| 5 | Activación | Con las etapas 1 a 4 marcadas, desde el **día 26**, gastan 1 Combustible [PROPUESTA] | — |

**Activación.** Es ruido máximo: desde esa noche y hasta el día 30, la amenaza suma +3 cada noche (sección 17.6). Por eso conviene activarla tarde, pero no tan tarde que falte combustible o alguien vivo para hacerlo.

> **Decisión (cantidad de etapas):** la hoja de base muestra la señal como "3/10"; la mesa en línea y el mazo de objetos usan 5 etapas. Valen **las 5 etapas**.
>
> **Decisión (baterías y radio):** la carta de la radio dice "necesita Baterías para usarse" y la batería de auto "da energía a la radio por 3 días". Para no llevar cuenta diaria, las baterías no son necesarias para marcar la etapa 1: la energía es la etapa 2. Las baterías quedan para los walkie-talkies.

---

## 19. Resumen de turno (carta de referencia)

> Pensado para imprimir o poner como carta grande en TTS. Cabe en una página.

**EL DÍA**
1. **BASE (07:00)** · ¿Día 30? → victoria si la señal está activada y hay alguien vivo · clima (d6: 1–2 llueve) · huerta (días pares +1 Comida) · infección: +1 nivel o 1 Medicina · curar: 2 Medicinas = 1 herida · construir: 1 ficha (2 con Taller) + materiales · marcar señal.
2. **PLANIFICACIÓN** · sale 1 por jugador · los demás descansan (−1 fatiga) · 1 guardia (+Percepción a todas las entradas, no descansa) · destino · mochila (6).
3. **EXPEDICIÓN (08:00)** · viaje 1–3 h · 1 turno = 1 hora · anochece 19:00 · fin 21:00.
4. **REGRESO Y NOCHE** · descargar, rasguños fuera · comer (1, o 2 con fatiga) · beber (1 Agua por cada 2) · sangre +1 si comió y bebió (+1 si descansó) · fatiga (+1 por salir, +1 si volvió después de 19:00) · amenaza: d6 + tramo → ataques · día +1.

**EL TURNO (1 HORA)**
1. **Supervivientes:** 3 PA cada uno (2 si aturdido o agotado). El ruido va al momento.
2. **Zombies:** en tu zona → atacan · oyó ruido → 1 zona hacia el más fuerte · te ve → 1 zona hacia ti · si no, quieto. (Corredor: 2 zonas.)
3. **Horda:** 5+ fichas en una zona de calle o en un edificio → 3 caminantes por el borde más cercano, se quitan las fichas.
4. **Disipación:** −1 ficha en cada zona.
5. **Reloj:** laceraciones −1 sangre · +1 hora · errantes d6 en la loseta más ruidosa (de noche, 2 veces).

**ACCIONES**

| Acción | PA | Ruido |
|---|---|---|
| Sigilo 1 zona (no con zombie en tu zona) | 2 | — |
| Caminar 1 zona | 1 | Bajo |
| Correr 2 zonas (1 vez/turno) | 1 | Medio |
| Esconderse (termina turno) | 1 | — |
| Abrir / cerrar puerta | 1 | Bajo |
| Forzar (palanca/hacha: 1 PA) | 2 | Medio |
| Romper ventana | 1 | Alto |
| Barricar (1 Madera) | 2 | Medio |
| Atacar | 1 | Del arma |
| Destrabar | 1 | — |
| Distraer (gasta 1 carta) | 1 | Medio allá |
| Registrar (sin zombies) | 2 | Bajo |
| Primeros auxilios (1 Medicina) | 2 | Bajo |
| Comer o beber (1/expedición) | 1 | — |
| Intercambiar / Vigilar | 1 | — |
| Salir del barrio | 1 | — |

**RUIDO** · Silencio 0 zonas/0 fichas · Bajo 1/1 · Medio 2/1 · Alto 3/2 · Máximo todo/3 · −1 nivel por pared, puerta cerrada o ventana intacta · pifia +1 ficha.

**COMBATE** · d20 + Fuerza (cuerpo a cuerpo) o Destreza (fuego) ≥ Defensa del zombie · daño: dado + Fuerza (cuerpo a cuerpo) o dado (fuego) · ventaja contra tranquilo · desventaja con brazo derecho herido, disparando de noche o a oscuras · 20: daño máximo · 1: falla, +1 ficha, el arma de fuego se encasquilla.

**ZOMBIES** · Caminante D8 V5 · Corredor D12 V4, 2 zonas · Bruto D10 V10 · Ácido D9 V5, rompe un objeto · Chillón D8 V3, chilla (ruido máximo + 1 caminante) · ataque d20+2 contra tu Defensa (10 + Destreza).

**HERIDAS** · d6 zona: 1 cabeza (aturdido) · 2–3 torso (−1 extra) · 4 brazo izq. (−1 espacio) · 5 brazo der. (desventaja) · 6 piernas (no correr) · d6 tipo: 1–2 rasguño · 3–4 laceración (−1/hora) · 5 fractura · 6 mordedura (infección) · toda herida −1 sangre · mueres con sangre 0 o con 2 heridas en la cabeza.

**NOCHE** · menos de 5: tranquila · 5–6: 1 ataque · 7–8: 2 · 9+: 3 · Fuerza 1d6 + tramo + 1 contra defensa (barricada + trampa + Percepción del guardia) · si la supera, entran zombies.

---

## 20. Lista de decisiones

Contradicciones entre fuentes y la versión elegida.

| # | Tema | Fuentes en conflicto | Se eligió |
|---|---|---|---|
| D1 | Coste de Sigilo y Correr | Carta de acción (Sigilo 1 PA, Correr 2 PA) contra kit y simulador | Kit: Sigilo 2 PA silencio, Caminar 1 PA bajo, Correr 1 PA 2 zonas medio, 1 vez por turno |
| D2 | Acción Huir | Carta de acción | Eliminada; la cubre Correr |
| D3 | Habilidad de Nico | Mesa en línea ("Correr le cuesta 1 PA en lugar de 2") | Pasa a Sigilo a 1 PA |
| D4 | Habilidad de Aurelio y acción Vigilar | Carta y mesa hablan de zombies ocultos, que no existen | Vigilar mira la ficha de un edificio adyacente; Aurelio a 2 zonas |
| D5 | Daño y ruido de armas | Kit (bate medio, sin hacha ni escopeta) contra cartas y tablas (bate bajo, hacha d8, escopeta d12) | Cartas y tablas: escalera silencio d4, bajo d6, medio d8, máximo d10–d12; Fuerza suma en cuerpo a cuerpo |
| D6 | Espacios del bate | Tabla de la casa (1) contra carta y kit (2) | Carta: 2. En general manda el valor de la carta |
| D7 | Munición | Kit (pistola con 6 balas) contra mazo (1 Munición = 3 disparos) | Mazo |
| D8 | Sangre por heridas de cabeza y torso | Mesa en línea (cabeza −3, torso −2) contra kit y simulador (−1, torso −1 extra, cabeza aturde, 2.ª herida en la cabeza mata) | Kit y simulador |
| D9 | Segunda herida en la cabeza | El texto del kit no aclara si el rasguño cuenta; el simulador sí lo cuenta | Cuenta cualquier herida en la cabeza sin curar; los rasguños se borran al volver |
| D10 | Duración del efecto de zona | El kit da a entender que la fractura dura más; el simulador aplica igual cualquier herida que no sea rasguño, vendada o no | Simulador: dura hasta curarla en la base |
| D11 | Coste de Primeros auxilios | Carta de Medicina (1 PA) contra kit (Vendar 2 PA) y habilidad de Marta | 2 PA; Marta 1 PA |
| D12 | Analgésicos, vendas, antibióticos | Kit y tablas los separan; el mazo los une en Medicina | Medicina; Primeros auxilios elige entre parar la laceración o +1 sangre |
| D13 | Antibióticos e infección | Tablas ("frenan la infección") contra pregunta abierta del mazo | Medicina frena 1 día; curar solo amputando (por ahora) |
| D14 | Sistema de botín | Tablas d6 del kit, tablas d20 de la base, mazo de objetos | d20 por edificio decide; el mazo da la carta; el d6 queda para el entrenamiento |
| D15 | Registrar con zombies en la zona | Simulador lo permite; hoja de base lo prohíbe | Prohibido |
| D16 | Aparición de zombies por turno | Kit (d6 = 1, de noche 1–2, en un borde) contra hoja de base (tabla de errantes por hora en la loseta más ruidosa) | Tabla de errantes |
| D17 | Noche | Kit (desde el turno 9) contra reloj de la base (19:00) | 19:00, con un turno por hora |
| D18 | Forzar con tirada | La carta del hacha dice "sin tirada", lo que sugiere que normalmente hay tirada; el kit no tiene tirada | Sin tirada; hacha y palanca bajan el coste a 1 PA |
| D19 | Ventaja y desventaja a la vez | Solo el simulador lo resuelve | Se anulan |
| D20 | Recursos de construcción | Mesa en línea ("Materiales" único) contra base y mazo (7 materiales) | 7 materiales separados |
| D21 | Escala de la señal | Hoja de base ("señal 3/10") contra mesa y mazo (5 etapas) | 5 etapas |
| D22 | Baterías para la radio | Carta de radio y batería de auto | No hacen falta para la etapa 1 |
| D23 | Etapa 3 con bengala | Tablas ("Bengalas ×2" y "bengala ×1" cumplen la etapa 3) contra carta de Bengala (solo Distraer) | 1 Bengala basta; la carta debe sumar esa línea |
| D24 | Nombres de supervivientes | Hoja de base (Julio Benítez, Sofía Paz, Nico Ferrer) contra mesa en línea | Mesa en línea (tiene atributos) |
| D25 | Alambre de púas en la base | "Pierden su segundo movimiento" supone zonas que la base no tiene | Pierden su ataque en la primera ronda |

---

## 21. Pendientes

Preguntas que este reglamento no cierra y conviene mirar en las próximas pruebas.

1. **Balance de comida.** Con +1 de fatiga por expedición, quien sale come 2 casi siempre. Con 3 supervivientes y 1 jugador, el grupo come unas 4 Comidas por día. Hay que contar cuánta comida trae una expedición típica y ajustar (por ejemplo, fatiga solo si se vuelve después de las 17:00).
2. **Duración.** Meta del kit: una expedición en unos 6 minutos. Con 10 a 12 turnos por expedición y 30 días, la partida se pasa mucho de 2 horas. Opciones: menos días jugables (eventos en los días tranquilos), menos turnos por expedición (1 turno = 2 horas) o días "de base" que no salen.
3. **Acciones ocultas y fichas de voz** (prueba 2): la carta de acción dice "elige 1 y marca con ficha numerada" y Elena reparte fichas de voz. No están en este reglamento.
4. **Mazo de supervivientes definitivo** y rescatados (cuántas cartas, cuántas camas).
5. **Valores de los zombies nuevos** (vitalidad y ataque de corredor, bruto, ácido y chillón).
6. **Ataque a la base:** la propuesta de la sección 17.6 no está probada. Mirar cuántas noches con irrupción hay por tramo.
7. **Cartas sin dibujo** de los objetos de las tablas que no están en el mazo (linterna, palanca, chaleco, etc.).
8. **Reparar objetos dañados** con Clavos (lo dice la carta de Clavos, pero ninguna regla daña objetos salvo el infectado ácido, que los rompe).
9. **Actualizar fuentes** si se aceptan estas decisiones: carta "Movimiento y sigilo", habilidades de Nico y Aurelio, carta de Medicina (2 PA), carta de Bengala (etapa 3), contadores de la mesa en línea (sangre por zona, materiales).
