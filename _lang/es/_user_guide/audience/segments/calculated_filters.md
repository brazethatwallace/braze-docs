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

Los Segments de Braze te ofrecen herramientas de segmentación potentes para crear grupos dinámicos de usuarios. Para la mayoría de los casos, esto es suficiente para llegar a tu audiencia de forma eficaz. Los filtros calculados están diseñados para casos avanzados en los que necesitas analizar comportamientos de hasta dos años atrás o aplicar lógica compleja, sin comprometer la retención de datos ni el rendimiento del sistema. Puedes usar datos de tu propio [almacén de datos]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) para refinar aún más tu audiencia.

Por ejemplo, la segmentación predeterminada de Braze encuentra usuarios que cumplen criterios específicos que tú defines, como identificar a un usuario que compró recientemente uno de tus productos. Los filtros calculados te permiten ir más allá, como identificar usuarios que compraron un color específico de un producto determinado al menos dos veces entre 18 y 24 meses atrás. Los filtros calculados son una mejora, no un requisito. Si necesitas filtros más avanzados o un periodo histórico más amplio, son una gran herramienta que te ayuda a mantener tu uso de datos optimizado.

## Filtros calculados y extensiones de segmento SQL {#calculated-filters-and-sql-segment-extensions}

Las [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) y los filtros calculados ayudan a crear audiencias a partir de comportamientos de compra y eventos personalizados, pero utilizan herramientas y orígenes de datos diferentes. Las extensiones de segmento SQL utilizan SQL que tú escribes contra tus datos conectados de Snowflake.

| Comportamiento | Filtros calculados | Extensiones de segmento SQL |
|---|---|---|
| Cómo defines la audiencia | Elige compras, eventos recomendados de eCommerce, interacción con mensajes o eventos personalizados, y conteos, ventanas de tiempo y filtros opcionales de propiedades | Escribe SQL contra tu conexión de Snowflake; usa plantillas, actualización incremental o actualización completa |
| Dónde se ejecuta la lógica | Los criterios y la actualización se gestionan en Braze como filtros calculados | La consulta se ejecuta en el contexto de tu almacén de datos según la configuración de tu extensión |
| Página de lista de filtros | Una lista compartida de filtros de actividad de usuario y de objetos de datos; la columna **Segments** muestra cuántos segmentos usan cada filtro, y los estados de procesamiento reflejan el estado de generación | Incluye una columna **Type** y filtros que varían según el tipo de extensión |
| Ejemplos típicos | Frecuencia de compra, gasto total, conteos de eventos personalizados y reglas basadas en propiedades durante la ventana seleccionada | Lógica respaldada por el almacén de datos, uniones entre tablas y ventanas históricas o agregaciones que van más allá del formulario de filtros calculados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtros calculados y extensiones de segmento SQL" }

### Cuándo usar filtros calculados {#when-to-use-calculated-filters}

Usa filtros calculados cuando las reglas guiadas por el panel de actividad de usuario u objetos de datos sean suficientes y no necesites SQL arbitrario en las tablas del almacén de datos.

### Cuándo usar otros tipos de extensiones de segmento {#when-to-use-other-segment-extension-types}

Usa las [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) cuando necesites SQL completo, datos respaldados por Snowflake, plantillas o modos de actualización diseñados para consultas de almacén de datos grandes o complejas. Usa las [extensiones de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) cuando necesites SQL que consulte directamente tu almacén de datos utilizando datos de las conexiones de [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

### Usa filtros calculados y extensiones de segmento juntos {#use-calculated-filters-and-segment-extensions-together}

Un segmento puede hacer referencia a un filtro calculado junto con una extensión de segmento SQL o CDI; por ejemplo, una cohorte definida en el almacén de datos a partir de una extensión, más reglas de compra o eventos personalizados que mantienes en el constructor de filtros calculados.

## Crea un filtro calculado {#create-a-calculated-filter}

Para crear un filtro calculado, elige un tipo de filtro si se te solicita, define tus criterios, luego guarda y activa el filtro antes de usarlo en un segmento.

### Paso 1: Configura los detalles {#step-1-set-up-details}

1. Ve a **Audience** > **Calculated Filters**.
2. Selecciona **Create filter**.
3. Si tu espacio de trabajo tiene [Accounts]({{site.baseurl}}/user_guide/data/activation/accounts) habilitado, selecciona un tipo de filtro:
   - **User activity filters:** Acciones y comportamientos de los usuarios.
   - **Data Object filters:** Atributos y relaciones para objetos de datos.
4. Introduce un nombre que describa la audiencia a la que deseas dirigirte. Un nombre descriptivo facilita encontrar el filtro cuando lo agregues a un segmento.
5. (Opcional) Agrega [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) para organizar los filtros calculados en tu espacio de trabajo.

Para **User activity filters**, selecciona **Enable recurring audience update** para actualizar el filtro de forma recurrente. Si no activas esta configuración, el filtro no se actualiza a menos que lo modifiques o selecciones **Update audience**. Los **Data Object filters** se actualizan cada hora.

### Paso 2: Elige tus criterios {#step-2-choose-your-criteria}

{% tabs %}
{% tab Filtros de objetos de datos %}

Si seleccionaste **Data Object filters**, elige un objeto de datos y luego agrega condiciones de atributo, relación o grupo de filtros. Para la segmentación basada en cuentas, consulta [Objetos de cuenta]({{site.baseurl}}/user_guide/data/activation/accounts).

{% endtab %}
{% tab Filtros de actividad de usuario %}

Si **Create filter** abre directamente el constructor de actividad de usuario, o si seleccionas **User activity filters**, elige una de las siguientes opciones de **Criterion** para la segmentación:

- **Made a Purchase**
- **Performed an eCommerce event**
- **Performed a Custom Event**
- **Interacted with Message Channel**

Las opciones de **Criterion** disponibles varían según las características habilitadas en tu espacio de trabajo. **Performed an eCommerce event** siempre está disponible. Si no ves otra opción que necesitas, comunícate con tu director de cuentas de Braze.

Después de seleccionar un tipo de evento, elige el evento específico, cuántas veces el usuario debe haberlo completado (más de, menos de o igual a) y el período de tiempo.

{% alert note %}
Los filtros de **más de** y **menos de** son exclusivos: no incluyen el número que especificas. Por ejemplo, un filtro de **más de 4 veces y menos de 16 veces** incluye a los usuarios que lo han realizado 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 o 15 veces.
{% endalert %}

Al elegir tu período de tiempo, puedes especificar un rango de fechas relativo (los últimos X días), una fecha de inicio, una fecha de fin o un rango de fechas exacto.

![Criterios de filtro calculado para usuarios que realizaron un evento personalizado más de cero veces en el rango de fechas del 21 de junio de 2026 al 27 de junio de 2026.]({% image_buster /assets/img/segment/calculated_filter_example.png %})

#### Segmentación por propiedades del evento {#event-property-segmentation}

Para aumentar la precisión de la segmentación, selecciona **Add Property Filters**. Esto te permite filtrar por propiedades de tu compra, evento de eCommerce o evento personalizado. Braze admite la segmentación por propiedades del evento basada en objetos de cadena, numéricos, booleanos y de tiempo.

Para propiedades de cadena, introduce varios valores a la vez; por ejemplo, dirigirte a usuarios con un estado igual a gold, silver o bronze. Para los eventos recomendados de eCommerce, el menú desplegable de propiedades se rellena con las propiedades disponibles para ese evento.

{% alert note %}
No necesitas filtros calculados para usar propiedades del evento en tu segmento. Los filtros calculados simplemente amplían la ventana histórica utilizada para crear un segmento predeterminado. Puedes crear un [segmento]({{site.baseurl}}/user_guide/audience/segments) predeterminado en tiempo real que use propiedades del evento de los últimos 30 días. De manera similar, puedes [programar tu mensaje]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para que se desencadene en tiempo real según una propiedad del evento, sin necesidad de un filtro calculado.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 3: Guarda y activa tu filtro {#step-3-save-and-activate-your-filter}

Selecciona **Save as draft** para guardar un nuevo filtro calculado sin activarlo. Para un filtro activado, selecciona **Save changes** para guardar tus actualizaciones. Debes seleccionar **Activate filter** antes de que un borrador aparezca como opción al construir un segmento.

Después de activar un filtro calculado, Braze comienza a calcular su audiencia. Cuando el procesamiento se completa, puedes seleccionar el filtro al construir una audiencia.

## Usar un filtro calculado en un segmento {#use-a-calculated-filter-in-a-segment}

Después de crear y activar un filtro calculado, agrégalo al construir un segmento o definir una audiencia para una Campaign o Canvas.

1. En el constructor de segmentos, abre la lista de filtros.
2. En **Otros filtros**, selecciona **Filtro calculado existente**.
3. Selecciona el filtro calculado que deseas incluir en la definición del segmento.

Después de agregar el filtro, selecciona el icono junto al menú desplegable del filtro para ver los detalles del filtro y confirmar los criterios aplicados a tu audiencia.

![Filtro calculado en un constructor de segmentos con un icono para ver más detalles.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

Para más información sobre cómo construir segmentos, consulta [Crear un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Gestionar filtros calculados {#manage-calculated-filters}

Ve a **Audiencia** > **Filtros calculados** para ver, editar y gestionar los filtros calculados en tu espacio de trabajo.

La página **Filtros calculados** muestra juntos los filtros de actividad de usuarios y objetos de datos. Puedes refinar la lista con los controles disponibles, pero la página no incluye un control para filtrar por tipo ni una columna **Tipo**. Usa la columna **Segments** para ver cuántos Segments utilizan cada filtro calculado.

### Etiquetas de estado {#status-labels}

Cada filtro calculado muestra uno de los siguientes estados. **Procesando** y **Error de procesamiento** aparecen cuando la generación de pertenencia está en curso o no se completó correctamente.

| Estado | Descripción |
|---|---|
| Activo | El filtro está activado y disponible para usarse en Segments. |
| Borrador | El filtro está guardado pero no activado. |
| Archivado | El filtro está archivado. |
| Actualización deshabilitada | Las actualizaciones recurrentes de audiencia están deshabilitadas. |
| Procesando | Braze está procesando una actualización del filtro. |
| Error de procesamiento | El intento de procesamiento más reciente no se completó correctamente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etiquetas de estado" }

### Editar y gestionar filtros individuales {#edit-and-manage-individual-filters}

Abre el menú de fila de un filtro calculado para realizar una acción. Las acciones que ves dependen del estado del filtro.

Para los filtros que no están archivados, el menú de fila incluye **Editar**, **Uso en mensajería**, **Archivar** y **Actualizar audiencia**. **Actualizar audiencia** está disponible para filtros activos que no están en procesamiento. Puedes editar un filtro calculado mientras se está procesando, pero no puedes guardar los cambios hasta que el procesamiento se complete.

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
- Un filtro activado vuelve a **Activo**, cuenta para el límite de filtros activos, y Braze inicia una actualización de audiencia.

Espera hasta que el procesamiento termine antes de desarchivar un filtro que muestra **Procesando**. Si has alcanzado el límite de filtros activos, archiva un filtro activo antes de desarchivar otro filtro activo.

#### Guardar versus activar {#save-versus-activate}

Puedes guardar un filtro calculado sin activarlo. Los filtros inactivos permanecen en tu espacio de trabajo, pero no se pueden agregar a Segments hasta que los actives. Selecciona **Activar filtro** para usar el filtro en la segmentación.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo crear un filtro calculado que use múltiples eventos personalizados? {#can-i-create-a-calculated-filter-that-uses-multiple-custom-events}

Al usar filtros calculados, puedes seleccionar un evento personalizado, un evento de compra, un evento de eCommerce o una interacción de canal. Sin embargo, puedes combinar múltiples filtros calculados con un AND o un OR al crear el Segment.

Puedes añadir múltiples eventos o hacer referencia a múltiples tablas de Snowflake al usar [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

### ¿Puedo archivar un filtro calculado si está en uso? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

No. Antes de poder archivar un filtro calculado, elimínalo de todas las Campaigns, Canvas y Segments que lo utilicen.

### ¿Puedo usar arrays en los filtros calculados? {#can-i-use-arrays-in-calculated-filters}

Sí. Para usar arrays, añade corchetes (`[]`) al nombre de tu propiedad. Si tu propiedad es `location_code`, introducirías `location_code[]`.

Braze usa `[]` para recorrer arrays y comprobar si algún elemento en el array recorrido coincide con la propiedad del evento. Por ejemplo, podrías crear un filtro calculado de usuarios que coincidan con al menos un valor de una propiedad de array.

### ¿Cómo calcula Braze el periodo de tiempo para un periodo de tiempo relativo de "últimos X días"? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

Cuando los filtros calculados calculan el periodo de tiempo relativo ("últimos X días"), la hora de inicio se establece a medianoche UTC. Por ejemplo, para un filtro calculado que se actualiza a las 2024-09-16 21:00 UTC y especifica 10 días, la hora de inicio se establece en 2024-09-06 00:00 UTC, no en 2024-09-06 21:00 UTC.

Sin embargo, puedes especificar las zonas horarias usando segmentos SQL para identificar a los usuarios que realizaron el evento personalizado hace 10 días basándose en la medianoche en la hora de la empresa, o a los usuarios que realizaron el evento hace 10 días basándose en la hora actual.