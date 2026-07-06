---
nav_title: Filtros calculados
article_title: Filtros calculados
page_order: 5.5
page_type: reference
description: "Este artículo de referencia explica cómo funcionan los filtros calculados, cómo se comparan con las Extensiones de segmento SQL y cómo crear y administrar filtros calculados."
tool: Segments
---

# Filtros calculados {#calculated-filters}

> Los filtros calculados te permiten crear segmentos muy precisos a lo largo de un periodo extendido del historial de un usuario. Por ejemplo, usa filtros calculados para dirigirte a usuarios que han comprado un producto en particular en los últimos 16 meses o que han gastado una cantidad determinada de dinero en tu servicio. Refina esta audiencia utilizando propiedades del evento para hacer la segmentación aún más granular.

{% alert important %}
Los filtros calculados se encuentran actualmente en acceso anticipado. Si te interesa participar en el acceso anticipado, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Cómo funciona {#how-it-works}

Los segmentos de Braze te ofrecen herramientas de segmentación potentes para crear grupos dinámicos de usuarios. Para la mayoría de los casos de uso, esto es suficiente para llegar a tu audiencia de forma eficaz. Los filtros calculados están diseñados para casos de uso avanzados en los que necesitas analizar comportamientos de hasta dos años atrás o aplicar lógica compleja, sin comprometer la retención de datos ni el rendimiento del sistema. Puedes usar datos de tu propio [almacén de datos]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) para refinar aún más tu audiencia.

Por ejemplo, la segmentación predeterminada de Braze encuentra usuarios que cumplen criterios específicos que defines, como identificar a un usuario que compró recientemente uno de tus productos. Los filtros calculados te permiten profundizar más, como identificar usuarios que compraron un color en particular de un producto específico al menos dos veces entre 18 y 24 meses atrás. Los filtros calculados son una mejora, no un requisito. Si necesitas filtros más avanzados o una ventana histórica más amplia, son una gran herramienta que te ayuda a mantener optimizado el uso de tus datos.

## Filtros calculados y Extensiones de segmento SQL {#calculated-filters-and-sql-segment-extensions}

Las [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) y los filtros calculados te ayudan a crear audiencias a partir del comportamiento de compras y eventos personalizados, pero utilizan herramientas y orígenes de datos diferentes. Las Extensiones de segmento SQL usan SQL que escribes contra tus datos de Snowflake conectados.

| Comportamiento | Filtros calculados | Extensiones de segmento SQL |
|---|---|---|
| Cómo defines la audiencia | Elige compras, eventos recomendados de comercio electrónico, interacción con mensajes o eventos personalizados, y conteos, ventanas de tiempo y filtros de propiedades opcionales | Escribe SQL contra tu conexión de Snowflake; usa plantillas, actualización incremental o actualización completa |
| Dónde se ejecuta la lógica | Los criterios y la actualización se administran en Braze como filtros calculados | La consulta se ejecuta en el contexto de tu almacén de datos según la configuración de tu extensión |
| Página de lista de filtros | Un tipo de filtro calculado, la columna **Segments** muestra cuántos segmentos usan cada filtro, los estados **Procesando** y **Error de procesamiento** reflejan el estado de generación | Incluye una columna **Tipo** y filtros que varían según el tipo de extensión |
| Casos de uso típicos | Frecuencia de compra, gasto total, conteos de eventos personalizados y reglas basadas en propiedades durante la ventana seleccionada | Lógica respaldada por el almacén de datos, uniones entre tablas y ventanas históricas o agregaciones más allá del formulario de filtro calculado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtros calculados y Extensiones de segmento SQL" }

### Cuándo usar filtros calculados {#when-to-use-calculated-filters}

Usa filtros calculados cuando las reglas guiadas por el dashboard para compras, comercio electrónico, interacción con mensajes y eventos personalizados son suficientes y no necesitas SQL arbitrario entre tablas del almacén de datos.

### Cuándo usar otros tipos de extensiones de segmento {#when-to-use-other-segment-extension-types}

Usa [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) cuando necesites SQL completo, datos respaldados por Snowflake, plantillas o modos de actualización diseñados para consultas de almacén de datos grandes o complejas. Usa [Extensiones de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) cuando necesites SQL que consulte directamente tu almacén de datos utilizando datos de conexiones de [Ingesta de datos de Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

### Usa filtros calculados y extensiones de segmento juntos {#use-calculated-filters-and-segment-extensions-together}

Un segmento puede hacer referencia a un filtro calculado junto con una Extensión de segmento SQL o CDI; por ejemplo, una cohorte definida en el almacén de datos a partir de una extensión más reglas de compra o eventos personalizados que mantienes en el constructor de filtros calculados.

## Crear un filtro calculado {#create-a-calculated-filter}

Para crear un filtro calculado, define criterios basados en el comportamiento del usuario, luego guarda y activa el filtro antes de usarlo en un segmento.

### Paso 1: Configura los detalles {#step-1-set-up-details}

1. Ve a **Audiencia** > **Filtros calculados**.
2. Selecciona **Crear filtro calculado**.
3. Nombra tu filtro calculado describiendo a los usuarios a los que pretendes dirigirte. Un nombre descriptivo facilita encontrar el filtro cuando lo añadas a un segmento.
4. (Opcional) Añade [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) para organizar los filtros calculados en tu espacio de trabajo.

También puedes seleccionar **Habilitar actualización recurrente de audiencia** para actualizar el filtro de forma recurrente. Si no activas esta configuración, el filtro calculado no se actualizará a menos que modifiques el filtro o selecciones **Actualizar audiencia**.

### Paso 2: Elige tus criterios {#step-2-choose-your-criteria}

Elige un criterio de compra, comercio electrónico, evento personalizado o interacción con mensajes para la segmentación. Después de seleccionar un tipo de evento, elige el evento específico, cuántas veces el usuario debe haberlo completado (más de, menos de o igual a) y el periodo de tiempo.

Al elegir tu periodo de tiempo, puedes especificar un rango de fechas relativo (los últimos X días), una fecha de inicio, una fecha de fin o un rango de fechas exacto.

![Criterios de filtro calculado para usuarios que realizaron un evento personalizado más de cero veces en el rango de fechas del 21 de junio de 2026 al 27 de junio de 2026.]({% image_buster /assets/img/segment/calculated_filter_example.png %})

#### Segmentación por propiedades del evento {#event-property-segmentation}

Para aumentar la precisión de la segmentación, selecciona **Añadir filtros de propiedades**. Esto te permite filtrar por propiedades de tu compra, evento de comercio electrónico o evento personalizado. Braze admite la segmentación por propiedades del evento basada en objetos de cadena, numéricos, booleanos y de tiempo.

Para propiedades de cadena, introduce múltiples valores a la vez; por ejemplo, dirigirte a usuarios con un estado igual a oro, plata o bronce. Para eventos recomendados de comercio electrónico, el menú desplegable de propiedades se rellena con las propiedades disponibles para ese evento.

{% alert note %}
No necesitas filtros calculados para usar propiedades del evento en tu segmento. Los filtros calculados simplemente extienden la ventana histórica utilizada para crear un segmento predeterminado. Puedes crear un [segmento]({{site.baseurl}}/user_guide/audience/segments) predeterminado en tiempo real que use propiedades del evento de los últimos 30 días. De forma similar, puedes [planificar tu mensaje]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para que se desencadene en tiempo real basándose en una propiedad del evento, sin necesidad de un filtro calculado.
{% endalert %}

### Paso 3: Guarda y activa tu filtro {#step-3-save-and-activate-your-filter}

Selecciona **Guardar** para guardar tu filtro calculado. Puedes guardar un filtro sin activarlo, pero debes activar un filtro antes de que aparezca como opción cuando construyas un segmento.

Después de activar un filtro calculado, Braze lo evalúa en tiempo real cuando se evalúa un segmento, una campaña o un Canvas que lo referencia.

## Usar un filtro calculado en un segmento {#use-a-calculated-filter-in-a-segment}

Después de crear y activar un filtro calculado, añádelo al construir un segmento o definir una audiencia para una campaña o un Canvas.

1. En el constructor de segmentos, abre la lista de filtros.
2. En **Otros filtros**, selecciona **Filtro calculado existente**.
3. Selecciona el filtro calculado para incluirlo en la definición del segmento.

Después de añadir el filtro, selecciona el icono junto al menú desplegable del filtro para ver los detalles del filtro y confirmar los criterios aplicados a tu audiencia.

![Filtro calculado en un constructor de segmentos con un icono para ver más detalles.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

Para más información sobre la creación de segmentos, consulta [Crear un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Administrar filtros calculados {#manage-calculated-filters}

Ve a **Audiencia** > **Filtros calculados** para ver, editar y administrar filtros calculados en tu espacio de trabajo.

La página **Filtros calculados** lista todos los filtros calculados en tu espacio de trabajo. Puedes reducir la lista con los controles disponibles. Dado que solo hay un tipo de filtro calculado, no hay opción para filtrar por tipo y la tabla no incluye una columna **Tipo**. Usa la columna **Segments** para ver cuántos segmentos usan cada filtro calculado.

### Etiquetas de estado {#status-labels}

Cada filtro calculado muestra uno de los siguientes estados. **Procesando** y **Error de procesamiento** se muestran cuando la generación de membresía está en curso o no se completó correctamente.

| Estado | Descripción |
|---|---|
| Activo | El filtro está activado y disponible para usar en segmentos. |
| Borrador | El filtro está guardado pero no activado. |
| Archivado | El filtro está archivado. |
| Procesando | Braze está procesando una actualización del filtro. |
| Error de procesamiento | El intento de procesamiento más reciente no se completó correctamente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etiquetas de estado" }

### Editar y administrar filtros individuales {#edit-and-manage-individual-filters}

Abre el menú de fila de un filtro calculado para editar, archivar, actualizar la audiencia o ver cómo se está utilizando en la mensajería. No puedes editar un filtro calculado mientras se está procesando.

{% alert note %}
Tu espacio de trabajo puede tener hasta 500 filtros calculados activados a la vez. Ponte en contacto con tu director de cuentas de Braze si necesitas aumentar este límite.
{% endalert %}

#### Guardar versus activar {#save-versus-activate}

Puedes guardar un filtro calculado sin activarlo. Los filtros inactivos permanecen en tu espacio de trabajo pero no se pueden añadir a segmentos hasta que los actives. Selecciona **Activar filtro** para usar el filtro en la segmentación.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo crear un filtro calculado que use múltiples eventos personalizados? {#can-i-create-a-calculated-filter-that-uses-multiple-custom-events}

Al usar filtros calculados, puedes seleccionar un evento personalizado, un evento de compra, un evento de comercio electrónico o una interacción de canal. Sin embargo, puedes combinar múltiples filtros calculados con un AND u OR al crear el segmento.

Puedes añadir múltiples eventos o hacer referencia a múltiples tablas de Snowflake al usar [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

### ¿Puedo archivar filtros calculados si existen en una campaña activa? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

No. Antes de poder archivar un filtro calculado, necesitas eliminarlo de toda la mensajería activa.

### ¿Puedo usar arrays en filtros calculados? {#can-i-use-arrays-in-calculated-filters}

Sí. Para usar arrays, añade corchetes (`[]`) al nombre de tu propiedad. Si tu propiedad es `location_code`, deberías introducir `location_code[]`.

Braze usa `[]` para recorrer arrays y comprobar si algún elemento del array recorrido coincide con la propiedad del evento. Por ejemplo, podrías crear un filtro calculado de usuarios que coincidan con al menos un valor de una propiedad de array.

### ¿Cómo calcula Braze el periodo de tiempo para un periodo relativo de "últimos X días"? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

Cuando los filtros calculados calculan el periodo de tiempo relativo ("últimos X días"), la hora de inicio se establece a medianoche UTC. Por ejemplo, para un filtro calculado que se actualiza a las 2024-09-16 21:00 UTC y especifica 10 días, la hora de inicio se establece a 2024-09-06 00:00 UTC, no a 2024-09-06 21:00 UTC.

Sin embargo, puedes especificar las zonas horarias usando segmentos SQL para identificar usuarios que realizaron el evento personalizado hace 10 días basándose en la medianoche en la hora de la empresa, o usuarios que realizaron el evento hace 10 días basándose en la hora actual.