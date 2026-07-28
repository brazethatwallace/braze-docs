---
nav_title: Uso compartido de datos de Snowflake
hidden: true
---

# Integración de uso compartido de datos de Snowflake {#snowflake-data-sharing-integration}

> Cuando se utiliza Snowflake Data Share como método de integración, Braze aprovisiona un recurso compartido en tu instancia de Snowflake en nombre del cliente. Este recurso compartido incluye automáticamente todos los eventos de participación con mensajes y de comportamiento de los usuarios.

Los recursos compartidos se aprovisionan por cliente después de que este haya adquirido un derecho de uso compartido de datos de Snowflake. Cuando un cliente solicita un uso compartido de datos, Braze añade un recurso compartido al espacio de trabajo del cliente, y este puede utilizar la interfaz de usuario de autoservicio para añadir los datos de la cuenta Snowflake del partner correspondiente.

![Aprovisionamiento de uso compartido de datos de Snowflake en el panel de Braze]({% image_buster /assets/img/snowflake.png %})

Una vez aprovisionado el recurso compartido, se puede acceder inmediatamente a todos los datos desde la instancia de Snowflake como un recurso compartido de datos entrantes.

![Recurso compartido de datos entrantes de Snowflake en la instancia de Snowflake del cliente]({% image_buster /assets/img/snowflake2.png %})

Dentro de tu instancia de Snowflake, verás un recurso compartido por región. Cada tabla tiene una columna, `app_group_id`, que es efectivamente una clave de inquilino para Braze. A medida que se añaden nuevos clientes a un recurso compartido dentro de la misma región, aparecen como diferentes `app_group_ids` dentro de las tablas existentes.

{% alert important %}
Braze aloja actualmente todos los datos a nivel de usuario en las regiones Snowflake AWS US East-1 y EU-Central (Frankfurt). Aunque Braze puede compartir entre regiones, es más rentable para los clientes si compartimos con `US-EAST-1` y/o `EU-CENTRAL-1`.
{% endalert %}

{% alert tip %}
Descarga los [esquemas de tablas sin procesar](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) o utiliza este conjunto de [datos de eventos de muestra](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset) disponible en el marketplace de Snowflake para familiarizarte con los eventos compartidos.
{% endalert %}

## Gestión de eventos duplicados {#handling-duplicate-events}

Se esperan duplicados, pero todos los eventos tienen un identificador único, la columna ID. Los duplicados pueden eliminarse haciendo `select distinct(id)`.

## Cambios de ruptura frente a cambios sin ruptura {#breaking-versus-non-breaking-changes}

### Cambios sin ruptura {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Dado que las columnas nuevas se consideran cambios sin ruptura, Braze recomienda encarecidamente enumerar explícitamente las columnas de interés en cada consulta en lugar de utilizar consultas `SELECT *`. Otra posibilidad es crear vistas que nombren explícitamente las columnas y, a continuación, consultar esas vistas en lugar de las tablas directamente.
{% endalert %}

### Cambios de ruptura {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

## Cuándo se actualizan las tablas SNAPSHOTS y CHANGELOGS {#when-snapshots-and-changelogs-tables-are-updated}

Las tablas SNAPSHOTS y CHANGELOGS realizan un seguimiento de los cambios en las campañas y los Canvas. Comprender cuándo se actualizan estas tablas es importante para consultar las variaciones de mensajes y las configuraciones de Canvas más recientes.

### CHANGELOGS_CAMPAIGN_SHARED

Se añade una fila a `CHANGELOGS_CAMPAIGN_SHARED` cuando:
- Se lanza la campaña, O
- Se modifica cualquiera de los siguientes campos con captura de instantánea:
  - Nombre
  - Acciones (incluidos los cambios en el contenido de los mensajes)
  - Comportamientos de conversión

{% alert important %}
Guardar o actualizar el borrador posterior al lanzamiento no desencadena automáticamente una actualización. La actualización se desencadena solo cuando lanzas la campaña o aplicas los cambios del borrador posterior al lanzamiento a la campaña activa.
{% endalert %}

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED

`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` se deriva de `CHANGELOGS_CAMPAIGN_SHARED`. Esta tabla extrae y aplana la columna de acciones de `CHANGELOGS_CAMPAIGN_SHARED` en registros individuales de variación de mensajes. Se actualiza en consecuencia cuando se actualiza `CHANGELOGS_CAMPAIGN_SHARED`.

### CHANGELOGS_CANVAS_SHARED

Se añade una fila a `CHANGELOGS_CANVAS_SHARED` cuando:
- Se lanza el Canvas, O
- Se modifica cualquiera de los siguientes campos con captura de instantánea:
  - Nombre
  - Comportamientos de conversión
  - Variaciones (porcentaje, asignaciones del primer paso, nombres de las variaciones)

{% alert important %}
Guardar o actualizar el borrador posterior al lanzamiento no desencadena automáticamente una actualización. La actualización se desencadena solo cuando lanzas el Canvas o aplicas los cambios del borrador posterior al lanzamiento al Canvas activo.
{% endalert %}

### SNAPSHOTS_CANVAS_VARIATION_SHARED

`SNAPSHOTS_CANVAS_VARIATION_SHARED` se deriva de `CHANGELOGS_CANVAS_SHARED`. Esta tabla utiliza el mismo patrón de extracción que `SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` y se actualiza en consecuencia cuando se actualiza `CHANGELOGS_CANVAS_SHARED`.

### SNAPSHOTS_CANVAS_STEP_SHARED

Se añade una fila a `SNAPSHOTS_CANVAS_STEP_SHARED` cuando:
- Se lanza el Canvas, O
- Se actualiza el Canvas activo (se aplica el borrador posterior al lanzamiento), O
- Se modifica cualquiera de los siguientes campos con captura de instantánea:
  - Nombre
  - Acciones (incluidos los cambios de contenido de los mensajes dentro de las variaciones de mensajes)

{% alert important %}
Guardar el borrador posterior al lanzamiento no desencadena automáticamente una actualización. La actualización se desencadena solo cuando lanzas el Canvas o aplicas los cambios del borrador posterior al lanzamiento al Canvas activo.
{% endalert %}

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED

Se añade una fila a `SNAPSHOTS_CANVAS_FLOW_STEP_SHARED` cuando:
- Se lanza el Canvas, O
- Se actualiza el Canvas activo (se aplica el borrador posterior al lanzamiento), O
- Se modifica cualquiera de los siguientes campos con captura de instantánea:
  - Nombre

{% alert important %}
Guardar el borrador posterior al lanzamiento no desencadena automáticamente una actualización. La actualización se desencadena solo cuando lanzas el Canvas o aplicas los cambios del borrador posterior al lanzamiento al Canvas activo.
{% endalert %}

## Cumplimiento del Reglamento General de Protección de Datos (RGPD) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}