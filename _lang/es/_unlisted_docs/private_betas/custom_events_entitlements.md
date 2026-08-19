---
article_title: Eventos personalizados
permalink: "/custom_events_entitlements/"
hidden: true
---

# [![Curso de Braze Learning]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Eventos personalizados {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Este artículo describe los eventos personalizados y sus propiedades, los filtros de segmentación relacionados, las propiedades de entrada de Canvas, los análisis relevantes y más. Para obtener información sobre los eventos de Braze en general, consulta [Eventos]({{site.baseurl}}/user_guide/data/custom_data/events).

Los eventos personalizados son acciones realizadas por tus usuarios o actualizaciones sobre ellos. Cuando se registran eventos personalizados, pueden desencadenar cualquier número y tipo de campañas de seguimiento. Luego puedes usar [filtros de segmentación](#segmentation-filters) para segmentar usuarios en función de la frecuencia y la última vez que ocurrieron esos eventos personalizados. Esto hace que los eventos personalizados sean ideales para rastrear interacciones de alto valor de los usuarios dentro de tu aplicación.

## Ejemplos {#use-cases}

Algunos ejemplos comunes de eventos personalizados incluyen:

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Derechos {#entitlements}

Los derechos determinan la capacidad de eventos personalizados, que hace un seguimiento del número de nombres de eventos diferentes que defines. Puedes tener hasta 2000 eventos personalizados por espacio de trabajo. Si necesitas aumentar tu capacidad, ponte en contacto con tu director de cuentas de Braze para obtener más información.

A medida que tu espacio de trabajo se acerque al número máximo de eventos personalizados, recibirás notificaciones en el panel y por correo electrónico para ayudarte a mantenerte al día.

Incluso después de alcanzar la capacidad, los eventos personalizados existentes se pueden seguir recibiendo. Sin embargo, no podrás crear nuevos eventos personalizados. Los datos recibidos para eventos personalizados que aún no existan no se procesarán.

## Gestión de eventos personalizados {#managing-custom-events}

Puedes gestionar, crear o bloquear eventos personalizados en el panel yendo a **Configuración de datos** > **Eventos personalizados**.

Selecciona el menú junto a un evento personalizado para las siguientes acciones:

### Bloqueo {#blocklisting}

Puedes bloquear eventos personalizados individuales a través del menú de acciones, o seleccionar y bloquear hasta 100 eventos de forma masiva.

Cuando bloqueas un evento personalizado:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

Además, si un evento personalizado bloqueado está actualmente referenciado por filtros o desencadenadores en otras áreas de Braze, aparecerá un modal de advertencia explicando que todas las instancias de los filtros o desencadenadores que lo referencian serán eliminadas y archivadas.

### Añadir descripciones {#adding-descriptions}

Puedes añadir una descripción a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) `Manage Events, Attributes, Purchases`. Selecciona **Editar descripción** para el evento personalizado e introduce lo que desees, como una nota para tu equipo.

## Añadir etiquetas {#adding-tags}

Puedes añadir etiquetas a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) "Manage Events, Attributes, Purchases". Las etiquetas se pueden usar para filtrar la lista de eventos.

### Ver informes de uso {#viewing-usage-reports}

El informe de uso enumera todos los Canvas, Campaigns y Segments que utilizan un evento personalizado específico. La lista no incluye usos de Liquid.

Puedes ver hasta 100 informes de uso a la vez seleccionando las casillas de verificación de varios eventos personalizados y luego seleccionando **Ver informe de uso**.

## Exportar datos {#exporting-data}

Para exportar la lista de eventos personalizados como un archivo CSV, selecciona el botón **Exportar todo** en la parte superior de la página. Se generará el archivo CSV y se te enviará un enlace de descarga por correo electrónico.

## Registro de eventos personalizados {#logging-custom-events}

Los eventos personalizados requieren una configuración adicional. Consulta los enlaces de documentación de la plataforma para encontrar los métodos utilizados para registrar eventos personalizados y añadir propiedades y cantidades.

{% details Ampliar para ver la documentación por plataforma %}

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Almacenamiento de eventos personalizados {#custom-event-storage}

Todos los datos almacenados en el **perfil de usuario**, incluidos los metadatos de eventos personalizados (primera o última ocurrencia, recuento total y X en Y durante 30 días), se conservan indefinidamente mientras cada perfil esté [activo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users).

## Filtros de segmentación {#segmentation-filters}

La siguiente tabla muestra los filtros disponibles para segmentar usuarios por eventos personalizados.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el evento personalizado ha ocurrido **más de X veces** | **MÁS DE** | **NÚMERO** |
| Comprobar si el evento personalizado ha ocurrido **menos de X veces** | **MENOS DE** | **NÚMERO** |
| Comprobar si el evento personalizado ha ocurrido **exactamente X veces** | **EXACTAMENTE** | **NÚMERO** |
| Comprobar si el evento personalizado ocurrió por última vez **después de la fecha X** | **DESPUÉS DE** | **HORA** |
| Comprobar si el evento personalizado ocurrió por última vez **antes de la fecha X** | **ANTES DE** | **HORA** |
| Comprobar si el evento personalizado ocurrió por última vez **hace más de X días** | **MÁS DE** | **NÚMERO DE DÍAS ATRÁS** (número positivo) |
| Comprobar si el evento personalizado ocurrió por última vez **hace menos de X días** | **MENOS DE** | **NÚMERO DE DÍAS ATRÁS** (número positivo) |
| Comprobar si el evento personalizado ocurrió **más de X (máx. = 50) veces** | **MÁS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado ocurrió **menos de X (máx. = 50) veces** | **MENOS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado ocurrió **exactamente X (máx. = 50) veces** | **EXACTAMENTE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Análisis {#analytics}

Braze registra el número de veces que han ocurrido los eventos personalizados y la última vez que cada usuario los realizó para la segmentación. Para la configuración de informes, filtros y opciones de exportación, consulta [Informe de eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report).

En la página **Custom Events Report**, puedes ver de forma agregada con qué frecuencia ocurre cada evento personalizado. Las líneas grises superpuestas en la serie temporal indican la última vez que se envió una Campaign, lo cual es útil para ver cómo tus Campaigns afectaron la actividad de eventos personalizados.

![Gráfico de recuento de eventos personalizados en la página Custom Events del panel que muestra tendencias para un evento personalizado][8]

También puedes usar **Filters** para desglosar tus eventos personalizados por hora, usuarios activos mensuales (MAU), Segments o fórmulas de KPI.

{% alert tip %}
[Incrementa atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#integers) para mantener un contador de una acción de usuario similar a un evento personalizado. Sin embargo, no puedes ver datos de atributos personalizados en una serie temporal. Las acciones de usuario que no necesitan ser analizadas en una serie temporal deben registrarse usando este método.
{% endalert %}

### Por qué no se muestran los análisis de eventos personalizados {#why-custom-events-analytics-arent-showing}

Los Segments creados con datos de eventos personalizados no pueden mostrar datos históricos anteriores a su creación.

## Propiedades de eventos personalizados {#custom-event-properties}

Las propiedades de eventos personalizados son metadatos o atributos de eventos personalizados que describen una ocurrencia específica de un evento. Estas propiedades pueden utilizarse para calificar aún más las condiciones de activación, aumentar la personalización en la mensajería, realizar seguimiento de conversiones y generar análisis más sofisticados a través de la exportación de datos sin procesar.

Las propiedades de eventos personalizados no se almacenan en el perfil de Braze y, por lo tanto, no consumen puntos de datos (consulta [Puntos de datos](#data-points) para conocer las excepciones).

{% alert important %}
Cada evento personalizado o compra puede tener hasta 256 propiedades de eventos personalizados distintas. Si un evento personalizado o una compra se registra con más de 256 propiedades, solo se capturarán y estarán disponibles para su uso las primeras 256.
{% endalert %}

### Formato esperado {#expected-format}

Los valores de las propiedades deben ser un objeto donde las claves son los nombres de las propiedades y los valores son los valores de las propiedades. Los nombres de las propiedades deben ser cadenas no vacías de 255 caracteres o menos, sin signos de dólar iniciales (`$`).

Los valores de las propiedades pueden ser cualquiera de los siguientes tipos de datos:

| Tipo de datos | Descripción |
| --- | --- |
| Números | Como [enteros](https://en.wikipedia.org/wiki/Integer) o [flotantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleanos | Valor de `true` o `false`. |
| Fechas y horas | Formateados como cadenas en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) o `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. No se admiten dentro de arrays. |
| Cadenas | 255 caracteres o menos. |
| Arrays | Los arrays no pueden incluir fechas y horas. |
| Objetos | Los objetos se ingieren como cadenas. |
| Objetos anidados | Objetos que están dentro de otros objetos. Para más información, consulta la sección de este artículo sobre [Objetos anidados](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Los objetos de propiedades de eventos que contienen valores de arrays u objetos pueden tener una carga útil de propiedades de eventos de hasta 100&nbsp;KB.

Puedes cambiar el tipo de datos de tu propiedad de evento personalizado, pero ten en cuenta los impactos de [cambiar los tipos de datos]({{site.baseurl}}/help/help_articles/data/change_custom_data_type) después de que se hayan recopilado los datos.

### Uso de propiedades de eventos personalizados {#using-custom-event-properties}

Las propiedades de eventos personalizados pueden utilizarse para calificar activadores de Campaign, realizar seguimiento de conversiones y personalizar la mensajería.

#### Activar mensajes {#trigger-messages}

Utiliza las propiedades de eventos personalizados para delimitar aún más tu audiencia para una Campaign o Canvas en particular. Por ejemplo, si tienes una aplicación de comercio electrónico y quieres enviar un mensaje a un usuario cuando abandona su carrito, puedes añadir una propiedad de evento personalizado de `cart value` para mejorar tu público objetivo y permitir una mayor personalización de la Campaign.

![Filtros de propiedades de eventos personalizados para un carrito abandonado. Dos filtros se combinan con un operador AND para enviar esta Campaign a usuarios que abandonaron su carrito con un valor de carrito entre 100 y 200 dólares][16]

Las propiedades de eventos personalizados anidadas también son compatibles con la [entrega basada en acciones][19].

![Filtros de propiedades de eventos personalizados para un carrito abandonado. Se selecciona un filtro si algún artículo del carrito tiene un precio superior a 100 dólares.][20]

#### Personalizar mensajes {#personalize-messages}

También puedes utilizar las propiedades de eventos personalizados para la personalización dentro de la plantilla de mensajería. Cualquier Campaign que utilice [entrega basada en acciones][19] con un evento desencadenante puede usar las propiedades de eventos personalizados de ese evento para la personalización de la mensajería.

Por ejemplo, si tienes una aplicación de juegos y quieres enviar un mensaje a los usuarios que completaron un nivel, podrías personalizar aún más tu mensaje con una propiedad para el tiempo que les tomó a los usuarios completar ese nivel. En este ejemplo, el mensaje se personaliza para tres Segments diferentes utilizando [lógica condicional][18]. La propiedad de evento personalizado llamada `time_spent` puede incluirse en el mensaje llamando a ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Si el usuario no tiene conexión a internet, los mensajes dentro de la aplicación activados con propiedades de eventos personalizados con plantilla (por ejemplo, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) fallarán y no se mostrarán.
{% endalert %}

Para obtener una lista completa de las etiquetas de Liquid que harán que los mensajes dentro de la aplicación se entreguen como mensajes dentro de la aplicación con plantilla, consulta [Preguntas frecuentes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/).

##### Consideraciones con los filtros {#considerations-with-filters}

- **Llamadas a la API:** Al realizar llamadas a la API y usar el filtro "está en blanco", una propiedad de evento personalizado se considera "en blanco" si se excluye de la llamada. Por ejemplo, si incluyeras `"event_property": ""`, entonces tus usuarios se considerarían "no en blanco".
- **Enteros:** Al filtrar por una propiedad de evento personalizado numérica y el número es muy grande, no uses el filtro "exactamente". Si un número es demasiado grande, puede redondearse a cierta longitud, por lo que tu filtro no funcionará como se espera.

#### Segmentación {#segmentation}

Utiliza la segmentación por propiedades de eventos para segmentar a los usuarios en función de los eventos personalizados realizados y las propiedades asociadas a esos eventos. Esto aumenta tus opciones de filtrado al segmentar por compras y eventos personalizados.

Las propiedades de eventos para eventos personalizados se actualizan en tiempo real para cualquier Segment que las utilice. Puedes gestionar las propiedades yendo a **Configuración de datos** > **Eventos personalizados** y seleccionando **Gestionar propiedades** para el evento personalizado asociado. Las propiedades de eventos personalizados utilizadas en ciertos filtros de Segment tienen un historial retrospectivo máximo de 30 días.

##### Añadir propiedades de eventos para la segmentación {#adding-event-properties-for-segmentation}

Necesitarás el [permiso de usuario]({{site.baseurl}}/user_guide/data/data_points#viewing-data-point-usage) "Manage Custom Event Property Segmentation" para crear Segments basados en la frecuencia y la antigüedad de las propiedades de eventos.

De forma predeterminada, puedes tener 20 propiedades de eventos segmentables por espacio de trabajo. Contacta a tu director de cuentas de Braze para aumentar este límite.

Para añadir propiedades de eventos para la segmentación, haz lo siguiente:

1. Ve a tu evento personalizado y selecciona **Gestionar propiedades**.
2. Selecciona el conmutador **Habilitar segmentación** para añadir la propiedad de evento para la segmentación. Puedes acceder a opciones de filtrado adicionales al segmentar.

Los filtros de segmentación por propiedades de eventos incluyen:

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![Un grupo de filtros que "tiene 'Carrito abandonado' con propiedad 'número de artículos' y valor '2' 'más de' '1' vez en los últimos '30' días del calendario.][3]

Los datos solo se registran para una propiedad de evento determinada después de que haya sido habilitada por tu administrador de éxito de cliente, y las propiedades de eventos solo están disponibles a partir de esa fecha en adelante.

##### Puntos de datos {#data-points}

En lo que respecta al uso de la suscripción, las propiedades de eventos personalizados habilitadas para la segmentación con los siguientes filtros se cuentan como puntos de datos separados, además del punto de datos contado por el propio evento personalizado:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propiedades de entrada de Canvas y propiedades de eventos {#canvas-entry-properties-and-event-properties}

Puedes utilizar `canvas_entry_properties` y `event_properties` en tus recorridos de usuario de Canvas. Consulta [Propiedades de entrada de Canvas y propiedades de eventos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) para obtener más información y ejemplos.

{% tabs local %}
{% tab Propiedades de entrada de Canvas %}

Las [propiedades de entrada de Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object) son las propiedades que mapeas para Canvas que son basados en acciones o activados por API. Ten en cuenta que el objeto `canvas_entry_properties` tiene un límite de tamaño máximo de 50 KB.

{% alert note %}
Específicamente para los canales de mensajes dentro de la aplicación, `canvas_entry_properties` solo puede referenciarse en Canvas Flow y en el editor de Canvas original si tienes habilitadas las propiedades de entrada persistentes en el editor original como parte del acceso anticipado anterior.
{% endalert %}

Para la mensajería de Canvas Flow, `canvas_entry_properties` puede utilizarse en cualquier paso de mensaje con este formato de Liquid: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Ten en cuenta que los eventos deben ser eventos personalizados o eventos de compra para poder utilizarse de esta manera.

#### Ejemplo {#use-case}

{% raw %}
Supongamos que una tienda minorista, RetailApp, tiene la siguiente solicitud: `"canvas_entry_properties" : {"product_name" : "shoes", "product_price" : 79.99}`. RetailApp puede incluir el nombre del producto (shoes) en un mensaje con el Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

RetailApp también puede activar mensajes específicos para enviar según diferentes propiedades de `product_name` en un Canvas que se dirige a usuarios después de que hayan activado un evento de compra. Por ejemplo, pueden enviar mensajes diferentes a los usuarios que compraron zapatos y a los usuarios que compraron otra cosa añadiendo el siguiente Liquid en un paso de mensaje.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expandir para el editor de Canvas original %}

A partir del 28 de febrero de 2023, ya no puedes crear ni duplicar Canvas utilizando el editor original. Esta sección está disponible solo como referencia.

Para los Canvas creados con el editor original, `canvas_entry_properties` solo puede referenciarse en el primer paso completo de un Canvas.

{% enddetails %}
{% endtab %}

{% tab Propiedades de eventos %}

{% alert important %}
No puedes usar `event_properties` en el paso de mensaje principal. En su lugar, debes usar `canvas_entry_properties` o añadir un paso de Rutas de Acción con el evento correspondiente **antes** del paso de mensaje que incluye `event_properties`.
{% endalert %}

Las propiedades de eventos se refieren a las propiedades que estableces para eventos personalizados y compras. Estas `event_properties` pueden utilizarse en Campaigns con entrega basada en acciones y en Canvas.

En Canvas Flow, las propiedades de eventos personalizados y de compra pueden utilizarse en Liquid en cualquier paso de mensaje que siga a un paso de Rutas de Acción. Asegúrate de usar {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} si haces referencia a estas `event_properties`. Estos eventos deben ser eventos personalizados o eventos de compra para poder utilizarse de esta manera en el componente de mensaje.

En el primer paso de mensaje que sigue a una Ruta de Acción, puedes usar `event_properties` relacionadas con el evento referenciado en esa Ruta de Acción. Estas `event_properties` solo pueden utilizarse si el usuario realmente realizó la acción (y no fue al grupo de Todos los demás). Puedes tener otros pasos (que no sean otro paso de Rutas de Acción o de mensaje) entre esta Ruta de Acción y el paso de mensaje.

{% details Expandir para el editor de Canvas original %}

A partir del 28 de febrero de 2023, ya no puedes crear ni duplicar Canvas utilizando el editor original. Esta sección está disponible solo como referencia.

Para el editor de Canvas original, `event_properties` no puede utilizarse en pasos completos programados. Sin embargo, puedes usar `event_properties` en el primer paso completo de un Canvas basado en acciones, incluso si el paso completo está programado.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Objetos anidados {#nested-objects}

Puedes utilizar objetos anidados (objetos dentro de otro objeto) para enviar datos JSON anidados como propiedades de eventos personalizados y compras. Estos datos anidados pueden utilizarse para crear plantillas de información personalizada en mensajes, activar envíos de mensajes y segmentar usuarios.

Para obtener más información, consulta nuestra página dedicada sobre [Objetos anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects).

## Almacenamiento de propiedades de eventos personalizados {#custom-event-property-storage}

Las propiedades de eventos personalizados están diseñadas para ayudarte a aumentar la precisión de la segmentación y hacer que los mensajes se sientan aún más personalizados. Las propiedades de eventos personalizados se pueden almacenar en Braze tanto a corto como a largo plazo.

Puedes segmentar en función de los valores de las propiedades del evento de dos maneras:

1. **En los últimos 30 días:** El personal de soporte de Braze puede habilitar la segmentación por propiedades del evento basándose en la frecuencia y la antigüedad de valores específicos de propiedades del evento dentro de Braze Segments. Si deseas aprovechar las propiedades del evento dentro de los segmentos, ponte en contacto con tu director de cuentas de Braze o tu administrador de éxito de cliente. Esta opción afectará al uso de datos.<br><br>
2. **Dentro y más allá de 30 días:** Para cubrir tanto la segmentación de propiedades del evento a corto como a largo plazo, puedes usar las [extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension). Esta característica segmenta a los usuarios en función de eventos personalizados y propiedades del evento registrados en los últimos dos años. Esta opción no afectará al uso de datos.

Ponte en contacto con tu administrador de éxito de cliente de Braze para obtener recomendaciones sobre el mejor enfoque en función de tus necesidades específicas.

[1]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/schema_generation_example.png %}
[8]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventPropertiesNested.png %} "customEventPropertiesNested.png"