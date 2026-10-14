# Modelos 3D para Tabletop Simulator

Generados con `python3 herramientas/modelos_3d.py`. Vista previa: `vista_previa.png`.

| Carpeta | Qué es |
|---|---|
| `caminante`, `corredor`, `bruto`, `infectado_acido`, `chillon` | Zombies: figura de cartón con la ilustración del juego al frente, dorso en tinta y base con el nombre |
| `marta_rios`, `raul_ibarra`, `sofia_lenz`, `tomas_ferro`, `nico_vidal`, `aurelio_pando`, `elena_quiroga` | Supervivientes iniciales: miniatura low-poly con su color y un accesorio del oficio |
| `elias_ortega`, `carla_sosa`, `lu` | Supervivientes de rescate |

Cada carpeta tiene `<id>.obj` (malla), `<id>.png` (textura), `<id>_collider.obj` (collider simple) y `<id>.mtl` (solo para visores 3D; TTS no lo usa).

## Cargar en Tabletop Simulator

1. Objects → Components → Custom → **Model**.
2. **Model/Mesh:** el `.obj`. **Diffuse/Image:** el `.png`. **Collider:** el `_collider.obj`.
3. Type: **Figurine**. Material: **Cardboard** (zombies) o **Plastic** (supervivientes).
4. Cuando TTS pregunte, subí los archivos a la **Steam Cloud** para que los demás jugadores los vean.
5. Escala: 1 unidad del modelo = 1 unidad de mesa. La base mide 1,2 de diámetro y entra en una zona de loseta (2 × 2). Si queda grande o chica, ajustala con la herramienta Scale y guardala en una bolsa infinita por tipo de zombie.
