Si ves dos entradas de datos personalizados con el mismo nombre visible, es posible que una de ellas incluya un espacio invisible al inicio o al final.

Para solucionar y corregir esto:

1. Ve a **Configuración de datos** > **Atributos personalizados** o **Eventos personalizados**, y localiza las dos entradas que parecen tener el mismo nombre.
2. Confirma si uno de los nombres contiene espacios en blanco ocultos:
    1. Haz clic derecho en cada nombre y selecciona **Inspeccionar**.
    2. Revisa el valor del texto HTML en las herramientas de desarrollador de tu navegador.
    3. Compara los valores (por ejemplo, `email` frente a ` email`).
    4. Si es necesario, consulta [Inspeccionar y editar páginas y estilos con Chrome DevTools](https://developer.chrome.com/docs/devtools/inspect-mode).
3. Decide qué nombre debe permanecer como tu clave canónica y estandariza esa ortografía y uso de mayúsculas exactos.
4. Si una entrada incluye espacios al inicio o al final y fue creada directamente en el panel, deja de usar esa entrada y cambia a la clave canónica:
    - Actualiza cualquier flujo de trabajo del panel, importaciones CSV y runbooks internos para usar la clave canónica.
    - [Bloquea datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) de la entrada incorrecta cuando estés listo para retirarla.
5. Verifica tus rutas de ingesta:
    - Las cargas útiles de API y SDK eliminan automáticamente los espacios al inicio y al final.
    - Los nombres creados en el panel no se recortan automáticamente, por lo que se requieren entrada manual y gobernanza.