- **Grabación de pantalla:** Una grabación de los pasos que seguiste antes de ver el error, incluyendo cualquier transición de página.
- **Marca de tiempo y zona horaria:** La hora exacta en que ocurrió el error y tu zona horaria.
- **Navegador y versión:** El navegador que estás usando (por ejemplo, Chrome 120, Safari 17) y si has intentado reproducir el error en un navegador diferente.
{% if include.context == 'Canvas' -%}
- **Pasos para reproducir:** Una descripción clara de las acciones que desencadenan el error, incluyendo cualquier paso en Canvas o configuración específica involucrada.
{% elsif include.context == 'campaign' -%}
- **Pasos para reproducir:** Una descripción clara de las acciones que desencadenan el error, incluyendo cualquier configuración específica de Campaign o Canvas involucrada.
{% endif -%}
- **Registros de red (opcional):** Abre las herramientas de desarrollador de tu navegador (pestaña **Network**), reproduce el error y exporta el registro de red como un archivo de registro HTTP Archive (HAR). Esto ayuda al equipo de soporte a identificar qué llamada a la API está agotando el tiempo de espera.