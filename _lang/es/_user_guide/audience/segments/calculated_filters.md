---
nav_title: Filtros calculados
article_title: Filtros calculados
page_order: 5.5
page_type: reference
description: "Este artículo de referencia explica cómo funcionan los filtros calculados, cómo se comparan con las extensiones de segmento SQL y cómo crear y administrar filtros calculados."
tool: Segments
---

# Filtros calculados {#calculated-filters}

> Los filtros calculados te permiten crear segmentos muy precisos a lo largo de un periodo extendido del historial de un usuario. Por ejemplo, usa filtros calculados para dirigirte a usuarios que han comprado un producto en particular en los últimos 16 meses o que han gastado una cantidad determinada de dinero en tu servicio. Refina esta audiencia utilizando propiedades del evento para hacer la segmentación aún más granular.

{% alert important %}
Los filtros calculados se encuentran actualmente en acceso anticipado. Si te interesa participar en el acceso anticipado, ponte en contacto con tu director de cuentas de Braze.
{% endalert %}

## Cómo funciona {#how-it-works}

Los Segments de Braze te ofrecen herramientas de segmentación potentes para crear grupos dinámicos de usuarios. Para la mayoría de los ejemplos, esto es suficiente para llegar a tu audiencia de forma eficaz. Los filtros calculados están diseñados para ejemplos avanzados en los que necesitas analizar comportamientos de hasta dos años atrás o aplicar lógica compleja, sin comprometer la retención de datos ni el rendimiento del sistema. Usa los **filtros de actividad de usuario** para criterios de compra y eventos de comercio electrónico, o los **filtros de objetos de datos** para la segmentación por cuentas y objetos personalizados.

Por ejemplo, la segmentación predeterminada de Braze encuentra usuarios que cumplen criterios específicos que tú defines, como identificar a un usuario que compró recientemente uno de tus productos. Los filtros calculados te permiten ir más allá, como identificar usuarios que compraron un color particular de un producto específico al menos dos veces entre 18 y 24 meses atrás. Los filtros calculados son una mejora, no un requisito. Si necesitas filtros más avanzados o una ventana histórica más amplia, son una gran herramienta para ayudarte mientras mantienes tu uso de datos optimizado.

## Filtros calculados y extensiones de segmento SQL {#calculated-filters-and-sql-segment-extensions}

Las [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) y los filtros calculados te ayudan a crear audiencias a partir del comportamiento de compra, pero utilizan herramientas y orígenes de datos diferentes. Las extensiones de segmento SQL utilizan SQL que escribes contra tus datos de Snowflake conectados.

| Comportamiento | Filtros calculados | Extensiones de segmento SQL |
|---|---|---|
| Cómo defines la audiencia | Elige compras o eventos recomendados de eCommerce, y conteos, ventanas de tiempo y filtros opcionales de propiedades | Escribe SQL contra tu conexión de Snowflake; usa plantillas, actualización incremental o actualización completa |
| Dónde se ejecuta la lógica | Los criterios y la actualización se gestionan en Braze como filtros calculados | La consulta se ejecuta en el contexto de tu almacén de datos según la configuración de tu extensión |
| Página de lista de filtros | Una lista compartida para filtros de actividad de usuario y de objetos de datos, la columna **Segments** muestra cuántos segmentos usan cada filtro, y los estados de procesamiento reflejan el estado de generación | Incluye una columna **Type** y filtros que varían según el tipo de extensión |
| Ejemplos típicos | Frecuencia de compra, gasto total y reglas basadas en propiedades durante la ventana seleccionada | Lógica respaldada por almacén de datos, uniones entre tablas y ventanas históricas o agregaciones más allá del formulario de filtros calculados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtros calculados y extensiones de segmento SQL" }

### Cuándo usar filtros calculados {#when-to-use-calculated-filters}

Usa filtros calculados cuando las reglas guiadas por el panel para actividad de usuario u objetos de datos son suficientes y no necesitas SQL arbitrario entre tablas del almacén de datos.

### Cuándo usar otros tipos de extensiones de segmento {#when-to-use-other-segment-extension-types}

Usa las [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) cuando necesites SQL completo, datos respaldados por Snowflake, plantillas o modos de actualización diseñados para consultas de almacén de datos grandes o complejas. Usa las [extensiones de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) cuando necesites SQL que consulte directamente tu almacén de datos utilizando datos de conexiones de [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

### Usa filtros calculados y extensiones de segmento juntos {#use-calculated-filters-and-segment-extensions-together}

Un segmento puede hacer referencia a un filtro calculado junto con una extensión de segmento SQL o CDI; por ejemplo, una cohorte definida en el almacén de datos a partir de una extensión más reglas de compra que mantienes en el generador de filtros calculados.

## Crear un filtro calculado {#create-a-calculated-filter}

Para crear un filtro calculado, elige un tipo de filtro si se te solicita, define tus criterios, luego guarda y activa el filtro antes de usarlo en un Segment.

### Paso 1: Configura los detalles {#step-1-set-up-details}

1. Ve a **Audiencia** > **Filtros calculados**.
2. Selecciona **Crear filtro**.
3. Si tu espacio de trabajo tiene [Cuentas]({{site.baseurl}}/user_guide/data/activation/accounts) habilitadas, selecciona un tipo de filtro:
   - **Filtros de actividad de usuario:** Acciones y comportamientos de los usuarios.
   - **Filtros de objetos de datos:** Atributos y relaciones de los objetos de datos.
4. Ingresa un nombre que describa la audiencia a la que pretendes dirigirte. Un nombre descriptivo facilita encontrar el filtro cuando lo añadas a un Segment.
5. (Opcional) Añade [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) para organizar los filtros calculados en tu espacio de trabajo.

Para los **filtros de actividad de usuario**, selecciona **Habilitar actualización recurrente de audiencia** para actualizar el filtro de forma periódica. Si no activas esta configuración, el filtro no se actualiza a menos que lo modifiques o selecciones **Actualizar audiencia**. Los **filtros de objetos de datos** se actualizan cada hora.

### Paso 2: Elige tus criterios {#step-2-choose-your-criteria}

{% tabs %}
{% tab Filtros de objetos de datos %}

Si seleccionaste **Filtros de objetos de datos**, elige un objeto de datos, luego añade condiciones de atributo, relación o grupo de filtros. Para la segmentación basada en cuentas, consulta [Objetos de cuenta]({{site.baseurl}}/user_guide/data/activation/accounts).

{% endtab %}
{% tab Filtros de actividad de usuario %}

Si **Crear filtro** abre directamente el constructor de actividad de usuario, o si seleccionas **Filtros de actividad de usuario**, elige una de las siguientes opciones de **Criterio** para la segmentación:

- **Realizó una compra**
- **Realizó un evento de eCommerce**

Después de seleccionar un tipo de evento, elige el evento específico, cuántas veces el usuario debe haberlo completado (más de, menos de o igual a) y el período de tiempo.

{% alert note %}
Los filtros de **más de** y **menos de** son exclusivos, es decir, no incluyen el número que especifiques. Por ejemplo, un filtro de **más de 4 veces y menos de 16 veces** incluye usuarios que han tenido 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 o 15 veces.
{% endalert %}

Al elegir tu período de tiempo, puedes especificar un rango de fechas relativo (los últimos X días), una fecha de inicio, una fecha de fin o un rango de fechas exacto. Para rangos relativos, ingresa de **1** a **730** días (dos años). Para rangos de fechas absolutos, la fecha de inicio debe estar dentro de los últimos dos años y la fecha de fin debe estar dentro de los próximos dos años.

#### Segmentación por propiedades del evento {#event-property-segmentation}

Para aumentar la precisión de la segmentación, selecciona **Añadir filtros de propiedades del evento**. Esto te permite filtrar según las propiedades de tu compra o evento de eCommerce. Braze admite la segmentación por propiedades del evento basada en objetos de cadena, numéricos, booleanos y de tiempo.

Para propiedades de cadena, ingresa varios valores a la vez; por ejemplo, segmentar usuarios con un estado igual a oro, plata o bronce. Para los eventos recomendados de eCommerce, el menú desplegable de propiedades se rellena con las propiedades disponibles para ese evento.

{% alert note %}
No necesitas filtros calculados para usar propiedades del evento en tu Segment. Los filtros calculados simplemente amplían la ventana histórica utilizada para crear un Segment predeterminado. Puedes crear un [Segment]({{site.baseurl}}/user_guide/audience/segments) predeterminado en tiempo real que utilice propiedades del evento de los últimos 30 días. De manera similar, puedes [programar tu mensaje]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para que se desencadene en tiempo real según una propiedad del evento, sin necesidad de un filtro calculado.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 3: Guarda y activa tu filtro {#step-3-save-and-activate-your-filter}

Selecciona **Guardar como borrador** para guardar un nuevo filtro calculado sin activarlo. Para un filtro activado, selecciona **Guardar cambios** para guardar tus actualizaciones. Debes seleccionar **Activar filtro** antes de que el filtro esté disponible en el constructor de Segments.

Después de activar un filtro calculado, Braze comienza a calcular su audiencia. Cuando el procesamiento se complete, podrás seleccionar el filtro al crear una audiencia.

## Usar un filtro calculado en un segmento {#use-a-calculated-filter-in-a-segment}

Después de crear y activar un filtro calculado, agrégalo al crear un segmento o definir una audiencia para una Campaign o Canvas.

1. En el constructor de segmentos, abre la lista de filtros.
2. En **Otros filtros**, selecciona **Filtro calculado existente**.
3. Selecciona el filtro calculado para incluirlo en la definición del segmento.

Después de agregar el filtro, selecciona el icono junto al menú desplegable del filtro para ver los detalles del filtro y confirmar los criterios aplicados a tu audiencia.

![Filtro calculado en un constructor de segmentos con un icono para ver más detalles.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

Para más información sobre la creación de segmentos, consulta [Crear un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Gestionar filtros calculados {#manage-calculated-filters}

Ve a **Audiencia** > **Filtros calculados** para ver, editar y gestionar los filtros calculados en tu espacio de trabajo.

La página **Filtros calculados** muestra juntos los filtros de actividad de usuarios y de objetos de datos. Puedes acotar la lista con los controles disponibles, pero la página no incluye un control de filtrar por tipo ni una columna **Tipo**. Usa la columna **Segments** para ver cuántos Segments utilizan cada filtro calculado.

### Etiquetas de estado {#status-labels}

Cada filtro calculado muestra uno de los siguientes estados. **Procesando** y **Procesamiento fallido** se muestran cuando la generación de membresía está en curso o no se completó correctamente.

| Estado | Descripción |
|---|---|
| Activo | El filtro está activado y disponible para usar en Segments. |
| Borrador | El filtro está guardado pero no activado. |
| Archivado | El filtro está archivado. |
| Actualización deshabilitada | Las actualizaciones recurrentes de audiencia están deshabilitadas. Braze puede establecer este estado automáticamente cuando un filtro con actualización programada no se utiliza. |
| Procesando | Braze está procesando una actualización del filtro. |
| Procesamiento fallido | El intento de procesamiento más reciente no se completó correctamente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etiquetas de estado" }

### Editar y gestionar filtros individuales {#edit-and-manage-individual-filters}

Abre el menú de fila de un filtro calculado para realizar una acción. Las acciones que ves dependen del estado del filtro.

Para filtros que no están archivados, el menú de fila incluye **Editar**, **Uso en mensajería**, **Archivar** y **Actualizar audiencia**. **Actualizar audiencia** está disponible para filtros activos que no están procesándose. Puedes editar un filtro calculado mientras se está procesando, pero no puedes guardar los cambios hasta que el procesamiento se complete.

{% alert note %}
Tu espacio de trabajo puede tener hasta 100 filtros calculados activos a la vez. Contacta a tu director de cuentas de Braze si necesitas aumentar este límite.
{% endalert %}

#### Desarchivar {#unarchive}

Puedes desarchivar un filtro de cualquiera de las siguientes maneras:

- Selecciona **Desarchivar** en el menú de fila del filtro.
- Selecciona uno o más filtros archivados y luego selecciona **Desarchivar**.
- Abre un filtro calculado archivado y selecciona **Desarchivar** en su página.

Cuando desarchivas un filtro, su estado vuelve al que tenía antes de archivarlo:

- Un borrador vuelve a **Borrador**.
- Un filtro activado vuelve a **Activo**, cuenta para el límite de filtros activos y Braze inicia una actualización de audiencia.

Espera a que el procesamiento termine antes de desarchivar un filtro que muestra **Procesando**. Si has alcanzado el límite de filtros activos, archiva un filtro activo antes de desarchivar otro filtro activo.

#### Guardar versus activar {#save-versus-activate}

Puedes guardar un filtro calculado sin activarlo. Los filtros inactivos permanecen en tu espacio de trabajo pero no se pueden agregar a Segments hasta que los actives. Selecciona **Activar filtro** para usar el filtro en la segmentación.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo archivar un filtro calculado si está en uso? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

No. Antes de archivar un filtro calculado, debes eliminarlo de todos los Campaigns, Canvas y Segments que lo utilicen. Tampoco puedes archivar un filtro mientras su estado sea **Procesando**; espera a que el procesamiento finalice.

### ¿Puedo usar matrices en filtros calculados? {#can-i-use-arrays-in-calculated-filters}

Sí. Para usar matrices, agrega corchetes (`[]`) al nombre de tu propiedad. Si tu propiedad es `location_code`, deberías introducir `location_code[]`.

Braze utiliza `[]` para recorrer matrices y comprobar si algún elemento de la matriz recorrida coincide con la propiedad del evento. Por ejemplo, podrías crear un filtro calculado de usuarios que coincidan con al menos un valor de una propiedad de tipo matriz.

### ¿Cómo calcula Braze el período de tiempo para un período relativo de "últimos X días"? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

Cuando los filtros calculados calculan el período de tiempo relativo ("últimos X días"), la hora de inicio se establece a medianoche UTC. Por ejemplo, para un filtro calculado que se actualiza a las 2024-09-16 21:00 UTC y especifica 10 días, la hora de inicio se establece en 2024-09-06 00:00 UTC, no en 2024-09-06 21:00 UTC. Los filtros calculados siempre utilizan UTC para las ventanas de tiempo; la zona horaria de tu espacio de trabajo no aplica.

Sin embargo, puedes especificar zonas horarias utilizando [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) para identificar usuarios que realizaron un evento hace 10 días basándose en la medianoche en la hora de la empresa, o usuarios que realizaron el evento hace 10 días basándose en la hora actual.