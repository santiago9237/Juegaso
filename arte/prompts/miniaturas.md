# Miniaturas estilo Zombicide · imagen con ChatGPT → 3D con IA → Tabletop Simulator

## Paso 1 · Imagen de cada personaje (ChatGPT)

Pegá primero este bloque fijo y después el personaje. Una imagen por mensaje.

```
Create a product photo of a single 28mm tabletop board game miniature, in the style of the Zombicide miniatures: a hand-painted plastic figure with realistic proportions, slightly exaggerated hands, head and weapon so they read well at small scale, clean painted details, subtle edge highlights and shading.

The figure stands on a round black plastic base (25 mm), in a dynamic but compact pose: both feet on the base, arms and weapon close to the body (nothing thin sticking far out).

Full body visible, centered, front three-quarter view, camera at the height of the figure's chest. Plain light grey seamless background, soft even studio light, no shadows on the background, no other objects, no text, no logo.

Setting: a post-apocalyptic city in South America, 2026. Clothes are worn, dirty and patched.
```

Después, una de estas líneas (`THIS MINIATURE: …`):

| Personaje | Prompt |
|---|---|
| Marta Ríos, enfermera | `THIS MINIATURE: Marta, a tired 40-year-old nurse with dark hair in a ponytail, light-blue hospital scrubs with a cardigan, a white medical bag with a red cross on her shoulder, holding a kitchen knife in one hand and a roll of bandage in the other.` |
| Raúl Ibarra, ex policía | `THIS MINIATURE: Raúl, a broad 45-year-old ex police officer with short black hair and dark skin, navy uniform shirt with a torn black tactical vest, police cap, aiming a pistol with both hands.` |
| Sofía Lenz, mecánica | `THIS MINIATURE: Sofía, a 30-year-old mechanic with short brown hair and a bandana, orange work overalls stained with grease, rolled sleeves, a big wrench in one hand and a toolbelt.` |
| Tomás Ferro, cocinero | `THIS MINIATURE: Tomás, a heavy-set 50-year-old cook with a mustache, white chef jacket and a bloodstained apron over a worn jacket, holding a meat cleaver raised.` |
| Nico Vidal, estudiante | `THIS MINIATURE: Nico, a skinny 19-year-old student with messy dark hair, red hoodie, jeans and sneakers, a school backpack, gripping a baseball bat with nails, nervous but ready.` |
| Aurelio Pando, cazador | `THIS MINIATURE: Aurelio, a 60-year-old hunter with a grey beard and an orange wool beanie, green hunting jacket, brown trousers, holding a scoped hunting rifle across his body.` |
| Elena Quiroga, maestra | `THIS MINIATURE: Elena, a 58-year-old school teacher with grey hair in a bun, burgundy cardigan, long skirt over boots, holding a pump shotgun, calm and stern.` |
| Elías Ortega, radioaficionado | `THIS MINIATURE: Elías, a thin 70-year-old radio amateur with glasses and white hair, beige vest full of pockets, a portable radio with an antenna in one hand and an old revolver in the other.` |
| Carla Sosa, bombera | `THIS MINIATURE: Carla, a strong 35-year-old firefighter, mustard-yellow firefighter coat and trousers with reflective stripes, red helmet, holding a red fire axe with both hands.` |
| Lu, 12 años | `THIS MINIATURE: Lu, a small 12-year-old girl with a dark bob haircut, green hoodie too big for her, jeans, sneakers and a little orange backpack, holding a flashlight. She is clearly shorter than an adult miniature.` |
| Caminante | `THIS MINIATURE: a walker zombie: a dead office worker in a torn suit and loose tie, grey rotting skin, slow shambling pose with arms reaching forward.` |
| Corredor | `THIS MINIATURE: a runner zombie: a dead jogger in torn sportswear, lean and fast, caught mid-sprint leaning forward, mouth open.` |
| Bruto | `THIS MINIATURE: a brute zombie: a huge muscular dead construction worker in a torn orange safety vest, bloated arms, hunched, twice as wide as a normal zombie, on a 32 mm base.` |
| Infectado ácido | `THIS MINIATURE: an acid zombie: a dead man with bubbling, dripping green ooze from his mouth and wounds, green acid puddle on the base.` |
| Chillón | `THIS MINIATURE: a screamer zombie: a gaunt dead woman with long ragged hair, head thrown back and mouth wide open in a scream, thin arms spread.` |

## Paso 2 · Pasar la imagen a 3D (IA de imagen a 3D)

Subí cada imagen a un generador de imagen → 3D (por ejemplo Tripo3D, Meshy o Rodin). Opciones:
- Modelo **con textura** (PBR o solo color).
- Exportar en **OBJ** (con su PNG de textura) o GLB.
- Polígonos: entre 10 000 y 30 000 (TTS acepta hasta unos 65 000 vértices; menos es más fluido con muchos zombies).

## Paso 3 · Tabletop Simulator

Objects → Components → Custom → Model: el OBJ como Mesh, el PNG como Diffuse, Type Figurine, Material Plastic. Si el generador da GLB o el modelo queda muy pesado, se convierte y reduce en Blender (Decimate) o con un script.
