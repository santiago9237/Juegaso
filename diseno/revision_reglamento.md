# Revisión del reglamento unificado v0.3

Revisión completa de `diseno/reglamento.md` (1180 líneas, secciones 1 a 22 y anexos A y B), contrastada con `diseno/revision.md` y con las fuentes. Mismo formato que la revisión anterior: gravedad, dónde, qué está mal y propuesta.

**Fuera de alcance:** por aviso del coordinador, la v0.4 va a reescribir varios temas. Esta revisión no reporta hallazgos sobre ellos:
- el idioma (voseo);
- el agua, que pasa a ser "Alimento";
- la cantidad de días;
- los tramos, que pasan a niveles de peligro;
- los d6 de aparición y errantes, que pasan a un mazo de aparición.

**Lo que se comprobó y está bien:**
- **Anexo A:** comparado por script contra los datos de `base_y_losetas.html`. Rangos d20, textos, espacios, zombies por tramo, registros, ventaja o desventaja y notas son idénticos. Solo se añadió la marca **[Señal]**.
- **Referencias de la sección 18 a filas de las tablas:** son correctas. Comisaría 18 y 19, ferretería 17 y 18, hospital 18, taller 18 y 19, estación 17 y 19, escuela 18 y 19.
- **Referencias internas:** existen y apuntan a lo que dicen (16.4, 17.5, 17.6, 21.2, 21.3, 21.9, D22, Anexo A, Anexo B).
- **Probabilidades del combate (sección 11):** correctas. Cuchillo 25 %, bate 50 %, pistola 42 % por disparo y 55 % con ventaja.
- **Cartas de herida:** 20 = 5 zonas × 4 tipos.
- **Sección 22:** recoge los 24 hallazgos alta y media de `revision.md` (A1–A7, M1a–n, M2–M17). Lo que de verdad resuelve está en la sección final de este documento.

**Gravedad:**
- **Alta:** la regla no se puede aplicar o rompe la partida.
- **Media:** se contradice, deja una duda en la mesa o cambia el resultado según quién la lea.
- **Baja:** redacción, coherencia menor o detalle.

---

## Gravedad alta

### R1. El mazo no alcanza para 30 días, y no hay regla para devolver las cartas consumidas
- **Dónde:**
  - 16.2: "Comida 15", "Medicina 10".
  - 16.4: "Busca en el mazo una carta de la familia … y tómala" y "Si la carta pedida ya no está en el mazo (salió antes), no encuentras eso [PROPUESTA]".
  - 15: comer cada noche.
  - 3.2: recursos iniciales en el depósito.
  - 3.5: "Mezcla las 74 cartas".
- **Qué está mal:**
  - Comer, curar, disparar, construir o usar Distraer gasta cartas, pero el reglamento no dice adónde van: ¿descarte, de vuelta al mazo, fuera del juego?
  - Tampoco dice si el depósito de la base guarda **cartas** o **contadores**. La mesa en línea usa contadores; 3.2 da números ("Comida 8…").
  - Si las cartas gastadas salen del juego, el mazo se agota enseguida:
    - Con 3 supervivientes se comen al menos 3 Comidas por noche. Eso es cerca de 60 en 20 noches, y el mazo tiene 15 cartas de Comida.
    - Con la regla "si ya no está, no encuentras eso", la partida es imposible de ganar a mitad de camino.
  - Los recursos iniciales tampoco dicen si salen del mazo. 3.2 solo retira las 2 armas, y 3.5 manda mezclar las 74 igual.
- **Propuesta:** escribir el ciclo de las cartas. Por ejemplo:
  - "Al descargar en la base, las cartas de Comida (Alimento), Medicina, Munición y materiales se pasan a contadores del depósito y las cartas vuelven a un descarte."
  - "Cuando el mazo se acaba, se mezcla el descarte."
  - Así la regla de 16.4 ("si ya no está…") solo afecta a cartas únicas (armas, señal, equipo).
  - Los recursos iniciales son contadores y no tocan el mazo.
  - Corregir 3.5: "mezcla las 72 cartas restantes".

---

## Gravedad media

### R2. La ruta de los zombies se contradice en el mismo párrafo
- **Dónde:** 10.4: "cada puerta cerrada … cuenta como 4 zonas. En la práctica: rodean por una abertura pasable si el rodeo es de hasta 4 zonas más".
- **Qué está mal:**
  - Si cruzar la puerta cuesta 4 en lugar de 1, el camino por la puerta vale D+3, donde D es el largo del camino directo.
  - Un rodeo de L zonas solo se prefiere si L < D+3. O sea, rodean si el rodeo es de **hasta 2 zonas más**; con 3 hay empate, y con 4 golpean la puerta.
  - La frase "en la práctica" contradice la regla que resume. El simulador se comporta como la primera frase.
- **Propuesta:** "Rodean si el rodeo es de hasta 2 zonas más; con 3, empate (eligen los jugadores); con más, golpean". La otra opción es cambiar el peso a 5 y dejar "hasta 4".

### R3. El Chillón se repite sin límite y no está claro si ataca o chilla
- **Dónde:** 10.1: "Si en la fase de zombies te detecta, chilla en lugar de moverse: ruido máximo en su zona y aparece 1 caminante".
- **Qué está mal:**
  - La regla 1 de 10.4 ("si hay un superviviente en su zona, ataca") va antes. Con alguien en su zona, no se sabe si ataca o chilla.
  - Chilla en **cada** fase en que te detecte. Cada turno pone 3 fichas de ruido y 1 caminante. En dos turnos llega la horda (5 fichas), y genera caminantes sin fin mientras lo veas.
- **Propuesta:**
  - "El Chillón chilla una sola vez (la primera vez que te detecta); después actúa como un caminante."
  - Aclarar que en tu zona ataca.

### R4. Infección: el nivel 4 se alcanza a la mañana pero la muerte llega "esa noche"
- **Dónde:**
  - 13: "En cada Fase de Base, la infección sube 1 nivel".
  - Nivel 4: "Muere y se levanta esa noche dentro de la base".
  - 6, Fase 1, paso 4.
- **Qué está mal:**
  - Entre la mañana y la noche el superviviente está en nivel 4. No hay efecto definido para ese día: ¿puede salir de expedición?
  - Si está afuera esa noche (o pasa la noche afuera), "se levanta dentro de la base" no aplica.
- **Propuesta:** "Al llegar a nivel 4 en la Fase de Base, muere en ese momento y se levanta en la base: resolver la irrupción antes de la Planificación." La otra opción es "no puede salir y muere en la Fase 4".

### R5. Un rasguño infectado no se puede curar después de volver
- **Dónde:**
  - 12.1: rasguño "Se borra al volver a la base".
  - 6, Fase 4, paso 1: "Los rasguños se borran".
  - 8.4: Primeros auxilios "limpia un rasguño infectado (hospital, ficha 6) y quita esa infección".
  - 13: amputar "solo si la mordedura está en un brazo o en las piernas".
- **Qué está mal:**
  - Al volver, el rasguño desaparece, pero la infección queda.
  - Limpiar solo se puede en expedición (Primeros auxilios), y amputar exige mordedura.
  - Un rasguño infectado que no se limpió en el momento queda sin cura posible, aunque la sección 22 (D13) dice que se cura "limpiando un rasguño infectado".
- **Propuesta:** el rasguño infectado no se borra al volver, o en la base se limpia con 1 Medicina (Fase 1, paso 5).

### R6. La trampa incendiaria suma +3 dos veces
- **Dónde:**
  - 17.1: "Defensa = barricada + trampa + Percepción".
  - 17.4: incendiaria, Defensa "+3".
  - 17.6: "Si se activa una trampa incendiaria, se suma su +3 a la defensa en ese momento".
- **Qué está mal:** según cómo se lea, la incendiaria da +3 siempre (como trampa) y otros +3 al activarse, o solo +3 la primera noche. Tampoco dice si "después se borra" quita también la defensa permanente.
- **Propuesta:** "La incendiaria no suma defensa hasta que se activa: la primera noche que atacan esa entrada suma +3 y después se descarta." En la tabla de 17.4, poner "+3 (un uso)".

### R7. La detección de noche y escondido se puede leer al revés
- **Dónde:** 10.3: "De noche y si estás escondido, solo te detecta en tu misma zona."
- **Qué está mal:** leído literalmente, la restricción exige las dos condiciones a la vez. El simulador y el kit la aplican con cualquiera de las dos.
- **Propuesta:** "De noche, o si estás escondido, solo te detecta…".

### R8. No está claro si el Corredor ataca en la misma activación en que llega
- **Dónde:** 10.1: "Se mueve 2 zonas por activación (paso a paso, puede cambiar de objetivo entre pasos)".
- **Qué está mal:** si en el primer paso entra a tu zona, no se dice si sigue de largo, se detiene o ataca. Con la regla 10.4 ("hace lo primero que se cumpla"), el ataque solo debería ocurrir en la fase siguiente.
- **Propuesta:** "Si en el primer paso entra a una zona con supervivientes, se detiene; ataca en la próxima fase de zombies."

### R9. Las explosiones dañan a supervivientes con "d10", pero ellos no tienen puntos de vida
- **Dónde:**
  - Anexo A, estación de servicio, ficha 4: "explota (d10 a cada uno en la zona)".
  - 11.1: botella incendiaria, "d10 a cada zombie de una zona".
- **Qué está mal:**
  - Los supervivientes no tienen vitalidad: reciben heridas (12.1). "d10 a cada uno" no se puede aplicar a ellos.
  - La botella no dice si también afecta a los supervivientes que estén en la zona.
- **Propuesta:** "Cada superviviente en la zona recibe 1 herida (2 si sale 8+ en el d10)". Y aclarar que la botella también hiere a los supervivientes de esa zona.

### R10. Recursos: no queda claro si el combustible es un material más
- **Dónde:**
  - Sección 22, M2: "Comida, Agua, Medicina, Munición, Combustible y 6 materiales".
  - D20: "7 materiales separados".
  - 16.4: "los materiales … (madera, clavos, chapa, alambre, cuerda, combustible, semillas)".
- **Qué está mal:** el mismo reglamento dice 6 y 7 materiales. La duda de la revisión anterior (B5) sigue abierta.
- **Propuesta:** fijar "Combustible es un recurso aparte, no material" (como el mazo), y corregir D20 y 16.4.

### R11. Barricar en expedición: no se puede quitar y no dice dónde se pone
- **Dónde:**
  - 8.2: "Barricar ▲ … una abertura adyacente pasa a barricada".
  - 7.1: barricada, "Pasan supervivientes: No".
- **Qué está mal:**
  - No hay acción para quitar la barricada, así que te puedes encerrar a ti mismo.
  - No se dice si vale en un borde libre (calle) o solo en puertas y ventanas.
  - No se dice qué pasa con la Madera si la barricada cae.
- **Propuesta:**
  - "Solo en puertas y ventanas."
  - "Quitar barricada: 1 PA, ruido bajo."
  - "Si un zombie la derriba, queda rota."

### R12. Las cuentas de turnos por barrio no son coherentes entre sí
- **Dónde:** 7.2: "Con un barrio a 1 hora hay 10 turnos de día (09:00 a 18:00)… A 3 horas, solo 5 turnos para volver con luz."
- **Qué está mal:**
  - A 1 hora cuenta incluido el turno de las 18:00, que es la "última hora para salir". Con ese mismo criterio, a 3 horas (de 11:00 a 16:00) son 6 turnos, no 5.
  - Al revés: si a 3 horas son 5, a 1 hora son 9.
  - Tampoco queda claro si quien sale en el turno de las 18:00 llega "después de las 19:00" (+1 fatiga, +1 amenaza).
- **Propuesta:** "El turno de las 19 − viaje es el último en que se puede usar Salir del barrio para llegar a las 19:00 justas, sin penalización." Con eso son 10 turnos a 1 hora y 6 a 3 horas.

### R13. La mordedura cuenta de dos maneras en la victoria
- **Dónde:**
  - Sección 4: "−1 por cada uno con infección. 'Victoria con mordedura' (del simulador) se anota aparte."
  - Anexo B: "Una mordedura se anota como 'victoria con mordedura'".
- **Qué está mal:** en el juego completo la mordedura ya es infección y tiene su propio −1. "Victoria con mordedura" sobra en la sección 4 y confunde.
- **Propuesta:** dejar "victoria con mordedura" solo en el Anexo B.

### R14. Baterías y walkie-talkies: 6 cartas sin uso
- **Dónde:**
  - 16.4: "Batería de auto y Baterías: hacen funcionar walkie-talkies. Walkie-talkie: sin efecto hasta las acciones ocultas".
  - D22: las baterías no hacen falta para la radio.
  - Anexo A, taller 13: "da energía a la radio por 3 días".
- **Qué está mal:**
  - Las 4 Baterías y los 2 Walkie-talkies del mazo (8 % del mazo) no hacen nada en v0.3.
  - El texto del anexo contradice D22.
- **Propuesta:**
  - Sacarlos del mazo hasta la prueba 2, o dar a las baterías un uso (por ejemplo, la linterna gasta 1 Batería por expedición).
  - Marcar en el anexo que "por 3 días" no aplica (D22).

### R15. Nico con Sigilo a 1 PA vuelve a traer el problema que se quiso arreglar
- **Dónde:**
  - 5.3: "Ágil. Sigilo le cuesta 1 PA en lugar de 2".
  - D1: se descartó Sigilo a 1 PA porque dejaba sin sentido las otras opciones.
- **Qué está mal:** para Nico, Sigilo (1 PA, silencio) es siempre mejor que Caminar (1 PA, ruido bajo). Un superviviente entero queda fuera de la decisión rápido o silencioso que la prueba 1 quiere medir.
- **Propuesta:** otras opciones:
  - "Una vez por turno, Sigilo a 1 PA".
  - "Correr no es pesada para él".
  - "Correr hasta 3 zonas".

### R16. Sec. 4 y sec. 7.2: "en la base" al llegar al amanecer del último día
- **Dónde:**
  - Sección 4: hace falta "al menos 1 superviviente vivo en la base".
  - 7.2, "Noche afuera": "llegas al amanecer siguiente".
- **Qué está mal:** no se dice si quien pasó afuera la última noche cuenta como "en la base" en la Fase 1 del último día.
- **Propuesta:** "Llegas antes de la Fase 1: cuentas para la victoria."

---

## Revisión de la regla nueva: acciones pesadas ▲ y fatiga (sección 14)

En general, la regla está bien construida:
- Las marcas aparecen en todos los lugares donde corresponde: 8.1, 8.2, 8.3, 14.1 y 19.
- El umbral de 4 y el reinicio diario son simples.
- No hay contador en la base ni en el combate nocturno, y eso es coherente.
- Correr pesado más "no correr con fatiga 2" se frena solo.
- El bate (▲, ruido bajo, más daño) contra el cuchillo (sin ▲, silencio) queda como una decisión real.

Hallazgos:

### F1 (media). "Cargar a un herido" no tiene regla de base
- **Dónde:**
  - 14.1: "Cargar a un herido o a un rescatado que no puede moverse solo, por cada zona (no con camilla)".
  - Anexo A, hospital 17: Camilla.
- **Qué está mal:**
  - Ninguna regla deja a un superviviente sin poder moverse: las piernas solo impiden Correr y el agotado tiene 2 PA.
  - El rescatado "sigue al que lo encontró" (16.4).
  - No existe la acción Cargar: ni su coste en PA ni si el cargador se mueve igual.
  - La fila de la tabla y la Camilla no tienen a qué aplicarse.
- **Propuesta:**
  - Definir un estado "no puede moverse" (por ejemplo: fractura en piernas más sangre 2 o menos, o rescatado herido).
  - Definir "Cargar: mueves 1 zona con él por 2 PA ▲".
  - Si no, quitar la fila hasta que exista.

### F2 (baja). "Salir del barrio con la mochila llena" se evita gratis
- **Dónde:** 8.1 y 14.1: la marca solo cuenta con "todos los espacios ocupados". Soltar cuesta 0 PA (8.4).
- **Qué está mal:** soltando cualquier objeto antes de salir, la marca se evita sin coste. La regla no cambia ninguna decisión.
- **Propuesta:** contar por peso ("con 5 o más espacios ocupados") o quitar la fila.

### F3 (media). La fatiga sube y casi nunca baja para quien sale todos los días
- **Dónde:**
  - 14.4: con fatiga 1 ya "come 2 Comidas".
  - 14.3: solo descansa quien se queda en la base.
  - 14.2: además suma +1 por llegar tarde, +1 por pasar hambre y +1 por fiebre.
- **Qué está mal:**
  - Quien sale a diario no descansa nunca. Una sola marca de fatiga le hace comer doble cada noche hasta que se tome un día libre.
  - Pasar hambre da +1 de fatiga, y la fatiga hace comer doble: es un espiral (hambre → fatiga → más hambre). Revisarlo cuando exista el Alimento de la v0.4.
  - El texto de D26 ("jugar con cuidado no cansa") es cierto dentro de la expedición, pero no para la economía de alimento de toda la partida.
  - Ya está en 21.1, pero conviene probarlo en concreto.
- **Propuesta:** probar dos variantes:
  - (a) Comer doble solo con fatiga 2 o más.
  - (b) Quien vuelve antes de las 19:00 y no hizo ninguna acción pesada después de las 15:00 también quita 1 de fatiga.

### F4 (baja). No se dice si se acumulan las fuentes de 2 PA
- **Dónde:** 7.3, paso 5: "2 si estás aturdido, agotado o con infección en nivel 3".
- **Qué está mal:** no aclara qué pasa con aturdido y agotado a la vez.
- **Propuesta:** "No se acumulan: nunca menos de 2 PA." La otra opción es "−1 PA por cada una, mínimo 1".

### F5 (baja). La exención de Sofía no aparece en su carta
- **Dónde:**
  - 5.3: Manos de taller, sin mención al ▲.
  - 14.4: "para ella no son pesadas".
- **Qué está mal:** quien lea solo la carta del superviviente no se entera de que Forzar y Barricar no la cansan.
- **Propuesta:** copiar la frase en 5.3 y en la carta.

### F6 (baja). El contador "de 0 a 4" nunca muestra 4
- **Dónde:** 14.1: "un contador de 0 a 4". Al llegar a 4 se convierte en fatiga y se borra.
- **Propuesta:** "contador de 0 a 3".

### F7 (baja). Constitución tiene usos que el reglamento no aplica
- **Dónde:**
  - 5.1: Constitución sirve para "noche afuera, caídas, infección".
  - Anexo A, taller ficha 4: la caída en la fosa se tira con **Destreza**.
  - Sección 13: la infección no usa ninguna prueba.
- **Propuesta:** dejar solo "noche afuera y amputación", o añadir una prueba de Constitución contra la fiebre (nivel 2).

---

## Gravedad baja

1. **Recursos iniciales sin chapa, alambre ni semillas.** 3.2 no los lista; se entiende que empiezan en 0. Escribirlo.
2. **Dados.** La sección 2 trae "1 d8", pero la motosierra usa 2d8. Pasar a 2 d8.
3. **Índice.** Dice "17. La base: entradas, construcción y noche"; el título de la sección es solo "La base".
4. **Resumen de la sección 19.**
   - La línea de ruido no menciona la barricada (9 y 7.1 sí).
   - La de victoria dice "hay alguien vivo" sin "en la base".
5. **"Distraer sin carta"** en el Anexo A (bengalas) se contradice con 8.3 ("gasta una carta").
6. **"Que veas" en Distraer.** No está definido para 2 zonas de distancia (10.3 solo define la vista de los zombies). Usar "por aberturas pasables", como el alcance de las armas de fuego.
7. **Registrar en la vereda.** Comisaría ficha 4: "1 registro en la vereda" contradice 16.3 ("Se registra en cualquier habitación del edificio"). Aceptarlo como excepción explícita.
8. **Percepción y Vigilar.** 5.1 dice que Percepción sirve para "Vigilar [PROPUESTA]", pero la acción Vigilar (8.4) no usa Percepción.
9. **Cartas de herida.** Hay una carta por cada combinación. Si dos supervivientes (o el mismo dos veces) reciben la misma herida, falta la carta. Basta con decir "anótala en la hoja si la carta no está".
10. **Fosa tapada.** Se construye en la Fase 1, antes de decidir quién sale. "Alguien de la base" puede salir ese mismo día con la fatiga de cavar. Aclarar si el que cava puede salir.
11. **El guardia puede hacer inexpugnable una entrada.**
    - En el peligro más bajo, la fuerza del ataque va de 3 a 8.
    - Con Elena de guardia (Percepción 5) y una barricada de nivel 3, la entrada tiene defensa 8 o más: en ese nivel no cae nunca, y en el más alto casi nunca.
    - Es una propuesta: anotarlo para la prueba de 21.6.
12. **Desventaja con el brazo herido.** 11 dice "una herida en el brazo derecho" sin "(salvo rasguño)", que sí está en 12.1.
13. **Bate en el entrenamiento.** El Anexo B no lista el ruido del bate como excepción. En el entrenamiento rige ruido **bajo** (reglamento), pero el simulador usa **medio**. Añadirlo a la lista de "anotar con qué regla se jugó".
14. **"Fuerza" sin aclarar.** "Sin arma: d20 + Fuerza, daño 1" (8.3) no dice "modificador", el mismo problema que se arregló en A5.

---

## ¿La sección 22 resuelve de verdad cada hallazgo?

| Hallazgo | Veredicto | Comentario |
|---|---|---|
| A1 Costes de movimiento | **Resuelto** | La carta y la muestra tipográfica quedan pendientes en 21.9. Ver R15 (Nico) |
| A2 Heridas y sangre | **Resuelto** | Modelo único en 12.1. La mesa en línea queda pendiente en 21.9 |
| A3 Dos sistemas de botín | **Parcial** | La unión d20 + carta está bien, pero falta el ciclo de las cartas consumidas (R1) |
| A4 Señal y victoria | **Resuelto** | 5 etapas, victoria y derrota escritas. Detalle en R16 |
| A5 Armas | **Resuelto** | Queda la ambigüedad de "Fuerza" en el ataque sin arma (baja 18) |
| A6 Turnos y horas; horda | **Resuelto** | Hay un error de cuenta en los turnos de cada barrio (R12). La aparición se reescribe en la v0.4 |
| A7 Revelar edificios | **Resuelto** | En las reglas (16.3). El simulador sigue pendiente en 21.9 |
| M1a Duración de los efectos de zona | **Resuelto** | |
| M1b Mordedura | **Parcial** | Queda el resto "victoria con mordedura" en la sección 4 (R13) |
| M1c–d Derribar y rodear | **Parcial** | Escrito como regla, pero la frase "hasta 4 zonas más" contradice el peso de 4 (R2) |
| M1e–h, M1l, M1n | **Resueltos** | |
| M1i Ruido a través de ventana | **Resuelto** | |
| M1j–k, M10 Aparición y desempate | **Resuelto en v0.3** | Se reescribe con el mazo de aparición de la v0.4: no se revisó |
| M1m, M11 Figuras | **Parcial** | "~40" sin desglose por tipo. La regla "si se acaban las de un tipo" necesita saber cuántas hay de cada tipo |
| M2 Recursos | **Parcial** | Contradicción interna sobre si el combustible es material (R10) |
| M3 Agua, hambre, fatiga, Constitución | **Resuelto** | El agua no se revisó (pasa a Alimento en la v0.4). Constitución con usos que no se aplican (F7). Espiral de hambre y fatiga (F3) |
| M4 Grupo y base vacía | **Resuelto** | |
| M5 Acciones inexistentes | **Resuelto** | Barricar quedó incompleta (R11) |
| M6 Kit médico y curaciones | **Resuelto** | |
| M7 Tabla de heridas y mochila excedida | **Resuelto** | |
| M8 Infección y amputación | **Parcial** | Tiempo del nivel 4 (R4) y rasguño infectado sin cura (R5) |
| M9 Estadísticas de los zombies | **Parcial** | Valores puestos, pero el Chillón queda sin límite (R3) y el Corredor ambiguo (R8) |
| M12 Defensa nocturna | **Parcial** | Sistema completo, con la doble suma de la incendiaria (R6) |
| M13 Objetos vagos | **Parcial** | Las Baterías y los Walkie-talkies siguen sin uso (R14) |
| M14 Registrar con zombies | **Resuelto** | Prohibido (D15). El Anexo B lo advierte |
| M15 Duración | **Pendiente** | En 21.2. Depende de la nueva cantidad de días de la v0.4: no se revisó |
| M16 Archivos faltantes | **Fuera de alcance** | Correcto que no lo resuelva el reglamento |
| M17 Probabilidad de la pistola | **Resuelto** | Las cifras se verificaron |

---

## Preguntas para Santiago

1. **Cartas consumidas:** ¿vuelven al mazo (o a un descarte que se remezcla) o salen del juego? ¿El depósito guarda cartas o contadores? (R1)
2. **Chillón:** ¿chilla una sola vez o en cada turno? (R3)
3. **Combustible:** ¿es un material o un recurso aparte? (R10)
4. **Fatiga y alimento:** ¿se come doble desde fatiga 1 o desde fatiga 2? ¿Hay alguna forma de quitar fatiga sin quedarse en la base? (F3)
5. **Nico:** ¿Sigilo siempre a 1 PA o una versión limitada? (R15)
6. **Cargar heridos:** ¿hace falta en v0.3 o se saca la fila de acciones pesadas? (F1)
7. **Baterías y walkie-talkies:** ¿se sacan del mazo hasta la prueba 2? (R14)
