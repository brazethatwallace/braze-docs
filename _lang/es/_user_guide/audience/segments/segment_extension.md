---
nav_title: Extensiones de segmento
article_title: Extensiones de segmento
page_order: 5
page_type: reference
description: "Este artículo práctico te guiará sobre cómo configurar y usar una extensión de segmento para mejorar tus capacidades de segmentación."
tool: Segments
---

# Extensiones de segmento {#segment-extensions}

> Las extensiones de segmento te permiten crear segmentos muy precisos a lo largo de un período extendido del historial de un usuario. Por ejemplo, usando extensiones de segmento puedes dirigirte a usuarios que han comprado un producto en particular en los últimos dieciséis meses o que han gastado una cantidad determinada de dinero con tu servicio. Refina esta audiencia usando propiedades del evento para hacer la segmentación aún más granular.

La segmentación de Braze te permite dirigirte a usuarios basándote en eventos personalizados o comportamiento de compra. Las extensiones de segmento mejoran esta capacidad, permitiéndote aprovechar datos históricos guardados en el perfil de usuario. Usando extensiones de segmento, puedes identificar y alcanzar a usuarios que han completado cualquier evento personalizado o evento de compra cualquier número de veces en los últimos dos años (730 días).

## ¿Por qué usar extensiones de segmento? {#why-use-segment-extensions}

Los Segments de Braze te ofrecen herramientas de segmentación potentes para crear grupos dinámicos de usuarios. Para la mayoría de los casos de uso, esto es suficiente para alcanzar a tu audiencia de manera efectiva. Las extensiones de segmento están diseñadas para casos de uso avanzados donde necesitas analizar comportamientos de hasta dos años atrás o aplicar lógica compleja, sin comprometer la retención de datos ni el rendimiento del sistema. Puedes usar consultas [SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) (extensiones de segmento SQL) o datos de tu propio [almacén de datos]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) para refinar aún más tu audiencia.

Por ejemplo, la segmentación predeterminada de Braze encontrará usuarios que cumplan criterios específicos que definas, como identificar a un usuario que recientemente compró uno de tus productos. Las extensiones de segmento te permiten ir más allá, como identificar usuarios que compraron un color particular de un producto específico al menos dos veces entre 18 y 24 meses atrás. Las extensiones de segmento son una mejora, no un requisito. Si necesitas filtros más avanzados o una ventana de retrospectiva más larga, son una gran herramienta para ayudarte mientras mantienes tu uso de datos optimizado.

{% alert note %}
Hay una asignación predeterminada de 25 extensiones de segmento activas por espacio de trabajo en un momento determinado. Si necesitas aumentar este límite, ponte en contacto con tu administrador de éxito de cliente de Braze para discutir tu caso de uso.
{% endalert %}

## Crear una extensión de segmento {#creating-a-segment-extension}

Para crear una extensión de segmento, crearás un filtro para refinar un segmento de tus usuarios basándote en propiedades de eventos personalizados. Al crear una extensión de segmento, elegirás si el segmento será estático o se actualizará dinámicamente en un intervalo establecido.

### Paso 1: Navega a extensiones de segmento {#step-1-navigate-to-segment-extensions}

Ve a **Audience** > **Segment Extensions**.

Desde la tabla de extensiones de segmento, selecciona **Create New Extension** y luego selecciona tu experiencia de creación de extensión de segmento:

- **Simple extension:** Crea una extensión de segmento enfocada en un solo evento usando un formulario guiado.
Ideal para cuando no quieres usar SQL.
- **Start with a template:** Crea un segmento SQL con una plantilla personalizable usando datos de Snowflake.
- **Incremental refresh:** Escribe un segmento SQL de Snowflake que actualice automáticamente los últimos 2 días de datos o actualiza manualmente según sea necesario. Ideal para equilibrar precisión y eficiencia de costos.
- **Full refresh:** Escribe un segmento SQL con datos de Snowflake o cualquier [fuente conectada de CDI]({{site.baseurl}}/cdi_segment_extensions) que recalcule toda la audiencia tras una actualización manual. Ideal para cuando necesitas una vista completa y actualizada de tu audiencia.

![Tabla con diferentes experiencias de creación de extensiones de segmento para seleccionar.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Si seleccionas una experiencia que usa SQL, consulta [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) para más información. Si seleccionas **Simple extension**, continúa al paso 2.

#### Uso de créditos SQL {#sql-credit-usage}

Los siguientes tipos de extensiones de segmento consumen créditos SQL:

- Extensiones de segmento SQL (tanto actualización incremental como completa)
- Segmentos de catálogo
- Segmentos de CDI
    - Los créditos se consumen dentro de tu propio almacén de datos

### Paso 2: Nombra tu extensión de segmento {#step-2-name-your-segment-extension}

Nombra tu extensión de segmento describiendo el tipo de usuarios que pretendes filtrar. Esto asegurará que esta extensión pueda ser encontrada fácil y correctamente al aplicarla como filtro en tu segmento.

![Extensión de segmento llamada "Online Shoppers Extension - 90 Days".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Paso 3: Elige tus criterios {#step-3-choose-your-criteria}

Selecciona entre criterios de compra, interacción con mensajes, evento recomendado de comercio electrónico o evento personalizado para la segmentación. Después de seleccionar los criterios del tipo de evento deseado, elige qué artículo comprado, interacción con mensaje, evento recomendado de comercio electrónico o evento personalizado deseas segmentar para tu lista de usuarios. Luego elige cuántas veces (más de, menos de o igual a) el usuario necesitaría haber completado el evento, y el período de tiempo; para las extensiones de segmento específicamente, puedes retroceder hasta los últimos 730 días (2 años).

La segmentación basada en datos de eventos de más de 730 días se puede realizar usando otros filtros ubicados en **Segments**. Al elegir tu período de tiempo, puedes especificar un rango de fechas relativo para seleccionar los últimos X días, una fecha de inicio, una fecha de fin o un rango de fechas exacto (fecha A a fecha B).

![Criterios de segmentación para usuarios que realizaron un evento personalizado más de 2 veces en el rango de fechas del 1 de marzo de 2025 al 31 de marzo de 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

Si estás creando una extensión de segmento usando un evento recomendado de comercio electrónico, primero selecciona **eCommerce Recommended Event** como tu criterio, luego selecciona un evento del menú desplegable.

![Un criterio de evento recomendado de comercio electrónico con un menú desplegable de eventos recomendados disponibles.]({% image_buster /assets/img/segment/ecommerce_recommended_event_criterion.png %})

#### Segmentación por propiedades del evento {#event-property-segmentation}

Para aumentar la precisión de la segmentación, selecciona la casilla **Add Property Filters**. Esto te permitirá profundizar basándote en las propiedades específicas de tu compra o evento personalizado. Admitimos la segmentación por propiedades del evento basada en objetos de cadena, numéricos, booleanos y de tiempo.

Para propiedades de cadena, puedes ingresar múltiples valores a la vez. En el ejemplo a continuación, este filtro busca usuarios con un estado igual a cualquiera de los siguientes: oro, plata o bronce.

![Segmentación basada en propiedades de cadena.]({% image_buster /assets/img/segment/property5.png %})

![Segmentación basada en propiedades numéricas.]({% image_buster /assets/img/segment/property2.png %})

![Segmentación basada en propiedades booleanas.]({% image_buster /assets/img/segment/property3.png %})

![Segmentación basada en objetos de fecha y hora.]({% image_buster /assets/img/segment/property4.png %})

Si estás usando eventos recomendados de comercio electrónico y agregas una propiedad del evento, el menú desplegable de propiedades se completará automáticamente con las propiedades disponibles para ese evento recomendado de comercio electrónico específico.

![Detalles de la extensión de segmento con un menú desplegable de propiedades disponibles.]({% image_buster /assets/img/segment/ecommerce_recommended_event_properties.png %})

También admitimos la segmentación basada en [propiedades de eventos anidados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects). En el menú desplegable de comparación, selecciona la comparación que coincida con el tipo de datos de tu propiedad anidada. Puedes usar la misma sintaxis de propiedades de eventos anidados para agregar propiedades anidadas para cualquier evento recomendado de comercio electrónico que contenga propiedades anidadas. Para información sobre las diferentes propiedades anidadas disponibles, consulta [Tipos de eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events). Para generar el esquema necesario para el nombre de propiedad de tu extensión de segmento, sigue los pasos en [Objetos anidados en eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

![Segmentación basada en propiedades de eventos anidados.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

Las extensiones de segmento dependen del almacenamiento a largo plazo de propiedades del evento y no tienen un límite de almacenamiento de propiedades con marca de tiempo. Puedes consultar propiedades del evento rastreadas en los últimos dos años. Usar propiedades del evento dentro de extensiones de segmento no afecta el uso de puntos de datos.

{% alert note %}
No necesitas extensiones de segmento para usar propiedades del evento o atributos personalizados anidados en tu segmento. Las extensiones de segmento simplemente extienden la ventana histórica utilizada para crear un segmento predeterminado. Puedes crear un [segmento]({{site.baseurl}}/user_guide/audience/segments) predeterminado en tiempo real que use propiedades del evento de los últimos 30 días o que use atributos personalizados anidados. De manera similar, puedes [planificar tu mensaje]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para que se desencadene en tiempo real basándote en una propiedad del evento, sin necesidad de una extensión de segmento.
{% endalert %}

### Paso 4: Configura los ajustes de actualización (opcional) {#step-4-designate-refresh-settings-optional}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

### Paso 5: Guarda tu extensión de segmento {#step-5-save-your-segment-extension}

Después de seleccionar **Save**, tu extensión de segmento comenzará a procesarse. El tiempo que tarda en generarse tu extensión de segmento depende de cuántos usuarios tengas, cuántos eventos personalizados o eventos de compra estés capturando, y cuántos días estés consultando en el historial.

Mientras tu extensión de segmento se está procesando, verás una pequeña animación junto al nombre de la extensión de segmento, y la palabra "Processing" en la columna **Last Processed** en la lista de extensiones de segmento. Ten en cuenta que no podrás editar una extensión de segmento mientras se está procesando.

![Página "Segment Extensions" con dos extensiones activas.]({% image_buster /assets/img/segment/segment_extension5.png %})

Cuando una extensión de segmento se está procesando, Braze continuará usando la versión histórica del segmento predeterminado anterior al inicio del procesamiento para fines de segmentación de audiencia. El procesamiento ocurre cada vez que se guarda o actualiza, e implica consultar y actualizar perfiles de usuario; en otras palabras, la membresía de tu segmento predeterminado no se actualiza instantáneamente. Esto significa que, a menos que la acción de un usuario se realice antes de que comience el procesamiento de la actualización, no podemos garantizar que el usuario será incluido en la extensión de segmento una vez que esa actualización en particular se complete. Por el contrario, los usuarios que estaban en la extensión de segmento antes de la actualización y que ya no cumplen los criterios continuarán coincidiendo con tu segmento predeterminado hasta que el proceso de actualización se complete y se apliquen las actualizaciones.

### Paso 6: Usa tu extensión en un segmento {#step-6-use-your-extension-in-a-segment}

Después de crear una extensión de segmento, puedes usarla como filtro al crear un segmento o definir una audiencia para una campaña o Canvas. Comienza eligiendo **Braze Segment Extension** de la lista de filtros en la sección **User Attributes**.

![Sección "Filters" con un menú desplegable de filtros que muestra "Braze Segment Extensions".]({% image_buster /assets/img/segment/segment_extension7.png %})

Desde la lista de filtros de Braze Segment Extension, elige la extensión de segmento que deseas incluir o excluir en este segmento.

![Un filtro "Braze Segment Extensions" que incluye un segmento "1 email click in the last 56 days".]({% image_buster /assets/img/segment/segment_extension6.png %})

Para ver los criterios de la extensión de segmento, selecciona **View Extension Details** para mostrar los detalles en una nueva ventana.

![Extensión para "1 email click in the last 56 days".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Ahora puedes proceder como de costumbre con la [creación de tu segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Puedo crear una extensión de segmento que use múltiples eventos personalizados? {#can-i-create-a-segment-extension-that-uses-multiple-custom-events}

Sí. Puedes agregar múltiples eventos o hacer referencia a múltiples tablas de Snowflake al usar [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

Al usar extensiones de segmento de **extensión simple**, puedes seleccionar un evento personalizado, un evento de compra o una interacción de canal. Sin embargo, puedes combinar múltiples extensiones de segmento con un AND u OR al crear el segmento predeterminado.

### ¿Puedo archivar extensiones de segmento si existen en una campaña activa? {#can-i-archive-segment-extensions-if-they-exist-in-an-active-campaign}

No. Antes de poder archivar una extensión de segmento, necesitas eliminarla de toda la mensajería activa.

### ¿Puedo usar arrays en extensiones de segmento? {#can-i-use-arrays-in-segment-extensions}

Sí. Para usar arrays, agrega corchetes (`[]`) al nombre de tu propiedad. Si tu propiedad es `location_code`, ingresarías `location_code[]`.

Braze usa `[]` para recorrer arrays y verificar si algún elemento en el array recorrido coincide con la propiedad del evento. Por ejemplo, podrías crear una extensión de segmento de usuarios que coincidan con al menos un valor de una propiedad de array.

### ¿Cómo calcula Braze el período de tiempo para un período relativo de "últimos __ días"? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-__-days}

Cuando las extensiones de segmento calculan el período de tiempo relativo ("últimos X días"), la hora de inicio se establece a medianoche UTC. Por ejemplo, para una extensión de segmento que se actualiza a las 2024-09-16 21:00 UTC y especifica 10 días, la hora de inicio se establece a 2024-09-06 00:00 UTC, no a 2024-09-06 21:00 UTC.

Sin embargo, puedes especificar las zonas horarias usando segmentos SQL para identificar usuarios que realizaron el evento personalizado hace 10 días basándote en la medianoche en la hora de la empresa, o usuarios que realizaron el evento hace 10 días basándote en la hora actual.