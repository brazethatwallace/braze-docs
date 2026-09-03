---
article_title: Preguntas frecuentes
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Esta página contiene una recopilación de las preguntas más frecuentes, clasificadas por categorías."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### ¿Cómo gestiono los datos de usuarios anónimos? {#how-do-i-handle-anonymous-user-data}

{% apitags %}
Users
{% endapitags %}

Inicialmente, cuando se reconoce un perfil de usuario a través del SDK, Braze crea un perfil de usuario anónimo con un `braze_id` asociado: un identificador de usuario único establecido por Braze.

Para realizar un seguimiento más exhaustivo de los usuarios anónimos, puedes implementar [alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases) que te permitan etiquetar a los usuarios anónimos con un identificador. Estos usuarios pueden exportarse utilizando sus alias o referenciarse mediante la API.

Si un perfil de usuario anónimo con un alias es reconocido posteriormente con un `external_id`, será tratado como un perfil de usuario identificado normal, pero conservará su alias existente y podrá seguir siendo referenciado por ese alias.

Para los usuarios con alias que quieras fusionar con usuarios identificados, puedes fusionar cualquier campo pertinente del perfil real que desees conservar. Tendrías que exportar esos datos antes de eliminarlos del perfil de alias utilizando nuestro [endpoint Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier). Luego puedes usar nuestro [endpoint Seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para publicar estos eventos en el perfil que conservaste. Esto preservará cualquier dato que desees conservar, como atributos que se registraron previamente en un perfil pero no en el otro.

Para obtener un desglose completo de los diferentes métodos de recopilación de datos de usuarios nuevos y existentes en Braze, consulta las [mejores prácticas de recopilación de datos]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices).

{% endapi %}
{% api %}

### ¿Cómo puedo importar usuarios que ya he recopilado e identificado fuera de Braze? {#how-can-i-import-users-i-have-already-collected-and-identified-outside-of-braze}

{% apitags %}
Users
{% endapitags %}

Para importar usuarios previamente identificados, puedes cargar un CSV en Braze o enviar datos a través de la API.

#### CSV

Puedes cargar y actualizar perfiles de usuario mediante archivos CSV desde **Audience** > **Import Users**. Al importar los datos de tus clientes, deberás especificar el identificador único de cada cliente, también conocido como `external_id`.

Antes de iniciar la importación de CSV, es importante que tu equipo de ingeniería entienda cómo se identificarán los usuarios en Braze. Normalmente se trata de un ID de base de datos utilizado internamente. Esto debería alinearse con la forma en que los usuarios serán identificados por el SDK de Braze en móviles y web, de modo que cada cliente tendrá un único perfil de usuario dentro de Braze en todos sus dispositivos. Obtén más información sobre el [ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) de Braze.

Cuando proporcionas un `external_id` en tu importación, Braze actualizará cualquier usuario existente con el mismo `external_id` o creará un nuevo usuario identificado con ese `external_id` establecido si no se encuentra ninguno.

Para más información y para descargar plantillas de importación CSV, consulta [importación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv).

#### API

Para cargar usuarios a través de la API, puedes utilizar nuestro [endpoint Seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para importarlos a Braze.

Si no estás seguro de si el usuario ya existe en Braze, puedes implementar nuestro [endpoint Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para verificarlo. Si identificas que el usuario ya existe en Braze, puedes usar nuestro endpoint `/users/track` para publicar los nuevos datos que deseas añadir al perfil de usuario que ya existe en Braze.

{% alert note %}
Ten en cuenta los siguientes matices cuando utilices el endpoint `/users/track`:

- Al crear usuarios de solo alias a través de este endpoint, debes establecer explícitamente el indicador `_update_existing_only` en false.
- La actualización del estado de suscripción con este endpoint actualizará tanto el usuario especificado por su ID externo (como Usuario1) como el estado de suscripción de cualquier usuario con el mismo correo electrónico que ese usuario (Usuario1).
{% endalert %}

{% endapi %}
{% api %}

### ¿Cuál es la diferencia entre los estados de suscripción push? {#whats-the-difference-between-the-push-subscription-statuses}

{% apitags %}
Users
{% endapitags %}

Hay tres opciones de estado de suscripción push: suscrito, adhesión voluntaria y cancelación de suscripción.

Por defecto, para que tu usuario reciba tus mensajes a través de push, su estado de suscripción push debe ser suscrito o adhesión voluntaria, y debe estar habilitado para push. Puedes anular esta configuración si es necesario al redactar un mensaje.

| Estado de adhesión voluntaria | Descripción |
|---|---|
| Suscrito | Estado predeterminado de la suscripción push cuando se crea un perfil de usuario en Braze. |
| Adhesión voluntaria | Un usuario ha expresado explícitamente su preferencia por recibir notificaciones push. Braze cambiará automáticamente el estado de adhesión voluntaria de un usuario a `Opted-In` si acepta un aviso push a nivel del sistema operativo.<br><br>Esto no se aplica a usuarios con Android 12 o inferior. |
| No suscrito | Un usuario se da de baja explícitamente de push a través de tu aplicación o de otros métodos que tu marca proporciona. Por defecto, las Campaigns push de Braze solo se dirigen a los usuarios que están en `Subscribed` o `Opted-in` para push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="¿Cuál es la diferencia entre los estados de suscripción push?" }

{% endapi %}
{% api %}

### ¿Qué pasa si he identificado usuarios duplicados? {#what-if-ive-identified-duplicated-users}

{% apitags %}
Users
{% endapitags %}

Si has identificado usuarios duplicados, tendrás que limpiar esos perfiles de usuario. Puedes hacerlo mediante los siguientes pasos:

1. Exporta los perfiles de usuario utilizando nuestro endpoint `/users/export/ids`.
2. Identifica el perfil de usuario correcto (en última instancia, tu equipo tendrá que decidir sobre la información correcta) y, o bien:
    - Fusiona los campos pertinentes del perfil real que quieras conservar utilizando el endpoint `/user/track`.
    - Elimina el perfil duplicado y no útil sin fusionar ningún dato utilizando el endpoint users/delete. Después de eliminar un perfil de usuario, **no hay forma de recuperar la información**.

{% alert important %}
Te recomendamos que primero importes los nuevos perfiles de usuario con el `external_id` correcto y los atributos y eventos personalizados correspondientes. Una vez eliminados los perfiles de usuario, no se pueden recuperar, por lo que la eliminación debe ser el último paso.
{% endalert %}

Algunas cosas adicionales a tener en cuenta:

- Cualquier dato de participación (como Campaigns o Canvas recibidos) en perfiles de usuario duplicados se perderá. La única forma de conservar el contexto histórico de participación es añadirlo como atributo personalizado (como un atributo personalizado de matriz de todas las Campaigns o Canvas recibidos).
- Al migrar perfiles de usuario, también depende de tu equipo decidir qué perfil de usuario de los duplicados se conservará. Braze no puede decidir ni proporcionarte una lista de perfiles que eliminar.
- En última instancia, será importante que tu equipo evalúe el proceso de registro desde la experiencia de los usuarios y se asegure de que solo se llama al método `changeUser()` cuando un usuario se identifica.

{% endapi %}
{% api %}

<!-- Segments -->

### ¿Cómo puedo crear un segmento cuando importo un grupo de usuarios a través de CSV? {#how-do-i-create-a-segment-when-i-import-a-group-of-users-through-csv}

{% apitags %}
Segments
{% endapitags %}

Para importar tu archivo CSV, ve a la página **User Import** en la sección Users. La tabla de **Recent Imports** muestra hasta veinte de las importaciones más recientes, sus nombres de archivo, el número de líneas del archivo, el número de líneas importadas correctamente, el total de líneas de cada archivo y el estado de cada importación.

El panel **Import CSV** contiene instrucciones de importación y un botón para iniciar la importación. Haz clic en **Select CSV File** y selecciona el archivo que te interese. A continuación, antes de hacer clic en **Start Import**, tienes la opción de indicar a Braze qué hacer con esta lista en «What do you want us to do with the users in this CSV».

Selecciona **Import Users in this CSV and also make it possible to retarget this specific batch of users as a group**, y luego selecciona **Automatically generate a segment from the users who are imported from this CSV**. Tras hacer clic en **Start Import**, Braze cargará el archivo, comprobará los encabezados de columna y los tipos de datos de cada columna, y creará un segmento.

Para descargar una plantilla CSV, consulta [importación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv).

{% endapi %}
{% api %}

### ¿Qué tipos de filtros puedo utilizar al crear un segmento? {#what-types-of-filters-can-i-use-when-creating-a-segment}

{% apitags %}
Segments
{% endapitags %}

El SDK de Braze te proporciona un potente arsenal de filtros para segmentar y dirigirte a tus usuarios en función de características y atributos específicos. Puedes utilizar el glosario de [filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) para buscar o acotar estos filtros por categoría de filtro (datos personalizados, actividad de usuario, retargeting, actividad de marketing, atributos de usuario, atribución de instalación, actividad social, pruebas, otros).

{% endapi %}
{% api %}

### ¿Cómo configuro la segmentación por ubicación para poder segmentar a los usuarios según su ubicación más reciente y utilizarla en mis campañas y estrategias basadas en la ubicación? {#how-do-i-set-up-location-targeting-so-that-i-can-segment-users-by-their-most-recent-location-and-use-it-in-my-location-based-campaigns-and-strategies}

{% apitags %}
Segments
{% endapitags %}

Ve a la página **Segments**, en Engagement, para ver todos tus segmentos de usuarios actuales. En esta página puedes crear y nombrar nuevos segmentos. Para empezar, haz clic en **Create Segment** y asigna un nombre a tu segmento.

Una vez que hayas creado tu segmento, añade un filtro `Most Recent Location` para dirigirte a los usuarios por el último lugar en el que utilizaron tu aplicación. Puedes resaltar a los usuarios en una región circular estándar o crear una región poligonal personalizada.

- Para las regiones circulares, puedes mover el origen y ajustar el radio de ubicación para tu segmentación.
- Para las regiones poligonales, puedes designar más específicamente qué áreas deseas incluir en tu segmento.

{% alert tip %}
¿Te interesa aprovechar la segmentación por ubicación con la ayuda de un partner de Braze? Consulta nuestros [partners de ubicación contextual]({{site.baseurl}}/partners/message_personalization) disponibles de Braze.
{% endalert %}

{% endapi %}
{% api %}

### ¿Cómo puedo dirigirme a listas precisas de usuarios en función de su evento personalizado y su comportamiento de compra en los últimos 365 días? {#how-can-i-target-precise-lists-of-users-based-on-their-custom-event-and-purchase-behavior-in-the-past-365-days}

{% apitags %}
Segments
{% endapitags %}

¡Puedes usar [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension)! Las extensiones de segmento te permiten dirigirte a una lista de usuarios más precisa de lo que podrías con un segmento normal.

Puedes crear hasta 10 extensiones de segmento por espacio de trabajo. Una vez generadas estas listas de extensiones, pueden incluirse o excluirse como filtro en tus segmentos. Al crear una extensión de segmento, también puedes especificar que la lista se regenere una vez cada 24 horas.

1. En Engagements, expande **Segments** y haz clic en **Segment Extension**.
2. En la tabla de extensiones de segmento, haz clic en **+ Create New Extension**.
3. Nombra tu extensión de segmento describiendo el tipo de usuarios que pretendes filtrar. Esto garantizará que esta extensión pueda descubrirse fácilmente y con precisión al aplicarla como filtro en tu segmento.
4. Selecciona entre un criterio de compra o de evento personalizado para la segmentación.
5. Elige qué artículo comprado o evento personalizado específico deseas segmentar para tu lista de usuarios.
6. Elige cuántas veces (más, menos o igual) el usuario tendría que haber completado el evento, y cuántos días mirar hacia atrás, hasta 365 días.

Para aumentar la precisión de la segmentación, puedes seleccionar **Add Property Filters** y segmentar en función de las propiedades específicas de tu compra o evento personalizado. Braze admite la segmentación de propiedades de eventos basada en objetos de cadena, numéricos, booleanos y temporales.

También admitimos la segmentación basada en [propiedades de eventos anidados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

Las extensiones de segmento se basan en el almacenamiento a largo plazo de propiedades de eventos y no tienen el límite de almacenamiento de propiedades de eventos personalizados de 30 días. Esto significa que puedes consultar las propiedades de eventos rastreadas en el último año, y el seguimiento no espera hasta que se haya configurado primero la extensión.

{% alert note %}
El uso de propiedades de eventos dentro de las extensiones de segmento no afecta al uso de puntos de datos.
{% endalert %}

{% endapi %}
{% api %}

#### Mantener actualizadas las extensiones de segmento {#keeping-segment-extensions-up-to-date}

{% apitags %}
Segments
{% endapitags %}

Puedes especificar si quieres que esta extensión represente una instantánea en el tiempo, o si quieres que la extensión se regenere a diario. Tu extensión siempre comenzará a procesarse después del guardado inicial. Si deseas que la extensión se regenere diariamente, selecciona **Regenerate Extension Daily** y la regeneración comenzará a procesarse alrededor de la medianoche de cada día en la zona horaria de tu empresa.

Cuando hayas terminado, haz clic en **Save**. Tu extensión comenzará a procesarse. El tiempo que se tarda en generar la extensión depende del número de usuarios que tengas, de cuántos eventos personalizados o de compra estés capturando y de cuántos días estés mirando hacia atrás en el historial.

Por último, una vez creada una extensión, puedes utilizarla como filtro al crear un segmento o definir una audiencia para una Campaign o Canvas. Para empezar, selecciona `Braze Segment Extension` en la lista de filtros de la sección **User Attributes**. En la lista de filtros de Braze Segment Extension, elige la extensión que deseas incluir o excluir en este segmento. Para ver los criterios de extensión, haz clic en **View Extension Details**. Ahora puedes proceder como de costumbre con la creación de tu segmento.

{% endapi %}
{% api %}

<!-- Campaigns -->

### ¿Cómo se crea una Campaign multicanal? {#how-do-you-create-a-multichannel-campaign}

{% apitags %}
Campaigns
{% endapitags %}

Consulta [Campaigns multicanal]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#create-a-multichannel-campaign) en **Crear una Campaign** para conocer los pasos de configuración, los canales compatibles y cómo cambiar de creador.

{% endapi %}
{% api %}

### ¿Cómo puedo empezar a probar y optimizar las Campaigns? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

{% apitags %}
Campaigns
{% endapitags %}

Crear Campaigns multivariantes y ejecutar Canvas con múltiples variantes es una excelente forma de empezar. Por ejemplo, puedes ejecutar una [Campaign multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing) para probar un mensaje con diferentes textos o líneas del asunto. Los Canvas con múltiples variantes son útiles para probar flujos de trabajo completos.

{% endapi %}
{% api %}

### ¿Por qué existe una diferencia entre el número de destinatarios únicos y el número de envíos para una Campaign o Canvas determinados? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

{% apitags %}
Campaigns
{% endapitags %}

Una posible explicación de esta diferencia podría deberse a que la Campaign o Canvas tiene activada la reelegibilidad. Al tenerla activada, los usuarios que cumplan los requisitos del segmento y de la configuración de entrega podrán recibir el mensaje más de una vez. Si la reelegibilidad no está activada, entonces la explicación probable de la diferencia entre envíos y destinatarios únicos puede deberse a que los usuarios tienen múltiples dispositivos en distintas plataformas asociados a sus perfiles.

Por ejemplo, si tienes un Canvas con notificaciones push tanto para iOS como para web, un usuario determinado con dispositivos móviles y de escritorio podría recibir más de un mensaje.

{% endapi %}
{% api %}

### ¿Qué ofrece la entrega en zona horaria local? {#what-does-local-time-zone-delivery-offer}

{% apitags %}
Campaigns
{% endapitags %}

La entrega en zona horaria local te permite entregar Campaigns de mensajería a un segmento en función de la zona horaria individual de cada usuario. Sin entrega en zona horaria local, las Campaigns se programarán en función de la configuración de zona horaria de tu empresa en Braze.

Por ejemplo, una empresa con sede en Londres que envíe una Campaign a las 12 del mediodía llegará a los usuarios de la costa oeste de Estados Unidos a las 4 de la madrugada. Si tu aplicación solo está disponible en determinados países, puede que esto no suponga un riesgo para ti; de lo contrario, te recomendamos encarecidamente que evites enviar notificaciones push de madrugada a tu base de usuarios.

{% endapi %}
{% api %}

### ¿Cómo reconoce Braze la zona horaria de un usuario? {#how-does-braze-recognize-a-users-time-zone}

{% apitags %}
Campaigns
{% endapitags %}

Braze determinará automáticamente la zona horaria del usuario a partir de su dispositivo. Esto está diseñado para garantizar la precisión de la zona horaria y la cobertura total de tus usuarios. Los usuarios creados a través de la API de usuario o de otro modo sin zona horaria tendrán la zona horaria de tu empresa como zona horaria predeterminada hasta que sean reconocidos en tu aplicación por el SDK.

Puedes comprobar la zona horaria de tu empresa en la [configuración de empresa]({{site.baseurl}}/user_guide/administer/global/admin_settings).

{% endapi %}
{% api %}

### ¿Cómo programo una Campaign en zona horaria local? {#how-do-i-schedule-a-local-time-zone-campaign}

{% apitags %}
Campaigns
{% endapitags %}

Al programar una Campaign, debes elegir enviarla a una hora determinada y luego seleccionar **Send campaign to users in their local time zone**.

Braze recomienda encarecidamente que todas las Campaigns en zona horaria local se programen con 24 horas de antelación. Dado que una Campaign de este tipo debe enviarse a lo largo de todo un día, programarlas con 24 horas de antelación permite que tu mensaje llegue a todo tu segmento. Sin embargo, puedes programar estas Campaigns con menos de 24 horas de antelación si es necesario. Ten en cuenta que Braze no enviará mensajes a los usuarios que hayan superado la hora de envío en más de 1 hora.

Por ejemplo, si son las 13:00 y programas una Campaign en zona horaria local para las 15:00, la Campaign se enviará inmediatamente a todos los usuarios cuya hora local sea entre las 15:00 y las 16:00, pero no a los usuarios cuya hora local sea las 17:00. Además, la hora de envío que elijas para tu Campaign no debe haber ocurrido todavía en la zona horaria de tu empresa.

La edición de una Campaign de zona horaria local programada con menos de 24 horas de antelación no alterará la programación del mensaje. Si decides editar una Campaign de zona horaria local para enviarla a una hora posterior (por ejemplo, a las 19:00 en lugar de a las 18:00), los usuarios que se encontraban en el segmento objetivo cuando se eligió la hora de envío original seguirán recibiendo el mensaje a la hora original (18:00). Si editas una zona horaria local para que se envíe a una hora más temprana (por ejemplo, a las 16:00 en lugar de a las 17:00), la Campaign se seguirá enviando a todos los miembros del segmento a la hora original (17:00).

{% alert note %}
Para los pasos de Canvas, los usuarios no necesitan estar en el paso durante 24 horas para recibir el siguiente paso en la entrega de zona horaria local.
{% endalert %}

Si has permitido que los usuarios vuelvan a ser elegibles para la Campaign, volverán a recibirla a la hora original (17:00). Sin embargo, para todas las apariciones posteriores de tu Campaign, tus mensajes solo se enviarán a la hora actualizada.

{% endapi %}
{% api %}

### ¿Cuándo entran en vigor los cambios en las Campaigns de zona horaria local? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

{% apitags %}
Campaigns
{% endapitags %}

Los segmentos objetivo para Campaigns en zona horaria local deben incluir al menos una ventana de 48 horas para cualquier filtro basado en el tiempo para garantizar la entrega a todo el segmento. Por ejemplo, considera un segmento dirigido a usuarios en su segundo día con los siguientes filtros:

- Aplicación utilizada por primera vez hace más de 1 día
- Aplicación utilizada por primera vez hace menos de 2 días

La entrega en zona horaria local puede pasar por alto a los usuarios de este segmento en función de la hora de entrega y de la zona horaria local de los usuarios. Esto se debe a que un usuario puede abandonar el segmento en el momento en que su zona horaria activa la entrega.

{% endapi %}
{% api %}

### ¿Qué cambios puedo hacer en las Campaigns programadas antes de su lanzamiento? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

{% apitags %}
Campaigns
{% endapitags %}

Cuando la Campaign está programada, es necesario realizar las ediciones de todo lo que no sea la composición del mensaje antes de poner los mensajes en cola para su envío. Como en todas las Campaigns, no puedes editar los eventos de conversión una vez lanzada la Campaign.

{% endapi %}
{% api %}

### ¿Cuál es la «zona segura» antes de que se pongan en cola los mensajes de una Campaign programada? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-queued}

{% apitags %}
Campaigns
{% endapitags %}

- Las Campaigns programadas una sola vez pueden editarse hasta la hora de envío programada.
- Las Campaigns programadas recurrentes pueden editarse hasta la hora de envío programada.
- Las Campaigns con hora de envío local pueden editarse hasta 24 horas antes de la hora de envío programada.
- Las Campaigns con hora de envío óptima pueden editarse hasta 24 horas antes del día previsto para el envío de la Campaign.

{% endapi %}
{% api %}

### ¿Qué ocurre si realizo una edición dentro de la «zona segura»? {#what-if-i-make-an-edit-within-the-safe-zone}

{% apitags %}
Campaigns
{% endapitags %}

Cambiar la hora de envío en las Campaigns dentro de este plazo puede provocar comportamientos no deseados, por ejemplo:

- Braze no enviará mensajes a los usuarios que hayan superado la hora de envío en más de una hora.
- Los mensajes que ya estaban en cola pueden seguir enviándose a la hora originalmente programada, en lugar de a la hora ajustada.

{% endapi %}
{% api %}

### ¿Qué debo hacer si la «zona segura» ya ha pasado? {#what-should-i-do-if-the-safe-zone-has-already-passed}

{% apitags %}
Campaigns
{% endapitags %}

Para asegurarte de que las Campaigns funcionan como se desea, recomendamos detener la Campaign actual (esto detendrá cualquier mensaje en cola). A continuación, puedes duplicar la Campaign, realizar los cambios necesarios y lanzar la nueva Campaign. Es posible que tengas que excluir de esta Campaign a los usuarios que ya hayan recibido la primera Campaign.

Asegúrate de reajustar las horas de programación de la Campaign para tener en cuenta el envío según la zona horaria.

{% endapi %}
{% api %}

### ¿Cuándo evalúa Braze a los usuarios para la entrega en zona horaria local? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

{% apitags %}
Campaigns
{% endapitags %}

Braze evalúa la elegibilidad de los usuarios para la entrada en:

- La hora de Samoa (UTC+13) del día programado
- La hora local del usuario en el día programado

Para que un usuario sea elegible para la entrada, debe ser elegible en ambas comprobaciones. Por ejemplo, si el lanzamiento de un Canvas está programado para el 7 de agosto de 2021 a las 14:00 hora local, la segmentación de un usuario ubicado en Nueva York requeriría las siguientes comprobaciones de elegibilidad:

- Nueva York el 6 de agosto de 2021 a las 21:00
- Nueva York el 7 de agosto de 2021 a las 14:00

Para entrar, un usuario debe coincidir con tu audiencia y filtros en ambos momentos de evaluación. Si el usuario no cumple los requisitos en la primera comprobación, Braze no ejecuta la segunda comprobación. No hay una duración mínima que un usuario deba haber estado en el segmento antes del lanzamiento; solo importa la elegibilidad en cada comprobación.

Este comportamiento de evaluación es independiente de [con cuánta antelación programas la Campaign en el panel]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign). Para la explicación completa, ejemplos y orientación sobre programación, consulta [¿Cuándo evalúa Braze a los usuarios para la entrega en zona horaria local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery) y [¿Cómo programo una Campaign en zona horaria local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign) en las preguntas frecuentes de Campaigns.

{% endapi %}
{% api %}

### ¿Por qué el número de usuarios que entran en una Campaign no coincide con el esperado? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

{% apitags %}
Campaigns
{% endapitags %}

El número de usuarios que entran en una Campaign puede diferir del número esperado debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, la audiencia se evalúa antes del desencadenante (a menos que se utilice un [desencadenante por cambio de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Esto hará que los usuarios abandonen la Campaign si inicialmente no forman parte de la audiencia seleccionada antes de que se evalúen las acciones desencadenantes.

{% endapi %}
{% api %}

<!-- Canvases -->

### ¿Qué ocurre si la audiencia y la hora de envío son idénticas para un Canvas que tiene una variante, pero múltiples ramas? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

{% apitags %}
Canvases
{% endapitags %}

Ponemos en cola un trabajo para cada paso: se ejecutan más o menos al mismo tiempo y uno de ellos «gana». En la práctica, la distribución puede ser algo uniforme, pero es probable que tenga al menos un ligero sesgo hacia el paso que se creó primero.

Además, no podemos garantizar cómo será exactamente esa distribución. Si deseas garantizar una división uniforme, añade un filtro de [número de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers).

{% endapi %}
{% api %}

### ¿Qué ocurre cuando detienes un Canvas? {#what-happens-when-you-stop-a-canvas}

{% apitags %}
Canvases
{% endapitags %}

Cuando detienes un Canvas, se aplica lo siguiente:

- Se impedirá a los usuarios entrar en el Canvas.
- No se enviarán más mensajes, sin importar dónde se encuentre el usuario en el flujo.
    - **Excepción:** los Canvas de correo electrónico no se detendrán inmediatamente. Después de que las solicitudes de envío vayan a SendGrid, no hay nada que podamos hacer para evitar que se entreguen al usuario.

{% alert note %}
Detener un Canvas no hará salir a los usuarios que estén esperando en un paso. Si vuelves a habilitar el Canvas y los usuarios siguen esperando, completarán el paso y pasarán al siguiente componente. Sin embargo, si ha transcurrido el tiempo en el que el usuario debería haber pasado al siguiente componente, saldrá del Canvas.
{% endalert %}

{% endapi %}
{% api %}

### ¿Cuándo se desencadena un evento de excepción? {#when-does-an-exception-event-trigger}

{% apitags %}
Canvases
{% endapitags %}

Los eventos de excepción solo se desencadenan mientras el usuario está esperando recibir el componente de Canvas asociado. Si un usuario realiza una acción por adelantado, el evento de excepción no se desencadenará.

Si deseas exceptuar a los usuarios que han realizado un determinado evento con antelación, utiliza [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) en su lugar.

{% endapi %}
{% api %}

### ¿Cómo afecta la edición de un Canvas a los usuarios que ya están en él? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

{% apitags %}
Canvases
{% endapitags %}

Si editas algunos de los pasos de un Canvas de varios pasos, los usuarios que ya estaban en la audiencia pero no han recibido los pasos recibirán la versión actualizada del mensaje. Ten en cuenta que esto solo ocurrirá si aún no han sido evaluados para el paso.

Para obtener más información sobre lo que puedes o no puedes editar después del lanzamiento, consulta [Cambiar tu Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits).

{% endapi %}
{% api %}

### ¿Cómo se realiza el seguimiento de las conversiones de los usuarios en un Canvas? {#how-are-user-conversions-tracked-in-a-canvas}

{% apitags %}
Canvases
{% endapitags %}

Un usuario solo puede convertir una vez por entrada de Canvas.

Las conversiones se asignan al mensaje más reciente recibido por el usuario para esa entrada. El bloque de resumen al principio de un Canvas refleja todas las conversiones realizadas por los usuarios dentro de esa ruta, hayan recibido o no un mensaje. Cada paso posterior solo mostrará las conversiones que se produjeron mientras ese era el paso más reciente recibido por el usuario.

{% details Ejemplos %}

#### Ejemplo 1 {#use-case-1}

Hay una ruta de Canvas con 10 notificaciones push y el evento de conversión es «session start» («Abre la aplicación»):

- El usuario A abre la aplicación después de entrar pero antes de recibir el primer mensaje.
- El usuario B abre la aplicación después de cada notificación push.

**Resultado:**
El resumen mostrará dos conversiones, mientras que los pasos individuales mostrarán una conversión de uno en el primer paso y cero en todos los pasos posteriores.

{% alert note %}
Si las horas tranquilas están activas cuando se produce el evento de conversión, se aplican las mismas reglas.
{% endalert %}

#### Ejemplo 2 {#use-case-2}

Hay un Canvas de un solo paso con horas tranquilas:

1. El usuario entra en el Canvas.
2. El primer paso no tiene retraso, pero está dentro de las horas tranquilas, por lo que el mensaje se suprime.
3. El usuario realiza el evento de conversión.

**Resultado:**
El usuario contará como convertido en la variante general del Canvas, pero no en el paso, ya que no recibió el paso.

{% enddetails %}

{% endapi %}
{% api %}

### Al observar el número de usuarios únicos, ¿es más preciso el análisis de Canvas o el segmentador? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

{% apitags %}
Canvases
{% endapitags %}

El segmentador es una estadística más precisa para los datos de usuarios únicos en comparación con las estadísticas de Canvas o de Campaigns. Esto se debe a que las estadísticas de Canvas y de Campaigns son números que Braze incrementa cuando ocurre algo, lo que significa que hay variables que podrían hacer que este número fuera diferente al del segmentador. Por ejemplo, los usuarios pueden convertir más de una vez en un Canvas o una Campaign.

{% endapi %}
{% api %}

### ¿Por qué el número de usuarios que entran en un Canvas no coincide con el número esperado? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

{% apitags %}
Canvases
{% endapitags %}

El número de usuarios que entran en un Canvas puede diferir del número esperado debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, la audiencia se evalúa antes del desencadenante (a menos que se utilice un desencadenante de [cambio de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Esto hará que los usuarios abandonen el Canvas si no forman parte de la audiencia seleccionada antes de que se evalúe cualquier acción desencadenante.

{% endapi %}
{% api %}

<!-- Analytics -->

### ¿Qué métricas mide Braze? {#what-metrics-does-braze-measure}

{% apitags %}
Analytics
{% endapitags %}

Dependiendo del canal, Braze mide una variedad de métricas que te permiten determinar el éxito de una Campaign e informar las futuras. Encontrarás una lista completa en nuestro [glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% endapi %}
{% api %}

### ¿Cómo se calculan los ingresos en Braze? {#how-is-revenue-calculated-in-braze}

{% apitags %}
Analytics
{% endapitags %}

En la página **Revenue**, puedes ver datos sobre ingresos o compras durante periodos de tiempo específicos, para un producto concreto, o los ingresos o compras totales de tu aplicación. Estas cifras de ingresos se generan a partir de las compras realizadas por los destinatarios de la Campaign dentro de un determinado periodo de conversión.

Dicho esto, es importante tener en cuenta que Braze es una herramienta de marketing y no de gestión de ingresos. Nuestro [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object) no admite reembolsos ni cancelaciones, por lo que es posible que aparezcan discrepancias al comparar los datos con otras herramientas.

{% endapi %}
{% api %}

### ¿Qué funciones de elaboración de informes permite Currents? {#what-reporting-capabilities-does-currents-enable}

{% apitags %}
Analytics
{% endapitags %}

Nuestra herramienta Currents transmite continuamente datos sobre la participación con la mensajería y el comportamiento de los clientes a uno de nuestros muchos partners de datos, lo que te permite utilizar los datos únicos y valiosos que crea Braze para potenciar tus esfuerzos de inteligencia empresarial y análisis en otros partners de primera clase.

Estos datos van más allá de las métricas de participación con la mensajería, y también pueden incluir cifras más complejas, como el rendimiento de atributos y eventos personalizados. Para más detalles, consulta nuestro [glosario de eventos de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

{% endapi %}
{% api %}

### ¿Cómo puedo programar un informe de participación recurrente? {#how-can-i-schedule-a-recurring-engagement-report}

{% apitags %}
Analytics
{% endapitags %}

Para programar un informe de participación recurrente, haz lo siguiente:

1. En tu cuenta del panel, ve a **Engagement Reports**, en **Data**.
2. Haz clic en **+ Create New Report**.
3. Añade las [Campaigns y los mensajes de Canvas]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#manually-select-campaigns-or-canvases) (individualmente o [por etiqueta]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#automatically-select-campaigns-or-canvases)) que desees compilar en tu informe.
4. [Añade estadísticas]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#add-statistics-to-your-reports) a tu informe.
5. Selecciona la compresión y el delimitador para tu informe.
6. Introduce las direcciones de correo electrónico de los usuarios de la empresa que deben recibir este informe.
7. Selecciona el [periodo de tiempo]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#select-time-frame) a partir del cual deseas que tu informe ejecute los datos.
8. Selecciona los [intervalos (diario, semanal, etc.)]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#select-data-display) en los que deseas ver el desglose de tus datos.
9. Programa tu informe para que [se envíe inmediatamente]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#schedule-your-report) o en un [momento futuro especificado]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#schedule-your-report).
10. Ejecuta el informe y ábrelo en tu correo electrónico cuando llegue.

{% endapi %}
{% api %}

### ¿Cuál es la diferencia entre los informes de participación y el generador de informes? {#whats-the-difference-between-engagement-reports-and-the-report-builder}

{% apitags %}
Analytics
{% endapitags %}

Los informes de participación te proporcionan CSV de estadísticas de participación para mensajes específicos de Campaigns y Canvas a través de un correo electrónico activado. Determinados datos se agregan a nivel de Campaign o Canvas en lugar de a nivel de variante o paso individual. Los informes no se guardan en el panel, y volver a ejecutar el informe puede dar lugar a estadísticas actualizadas.

El generador de informes te permite comparar los resultados de varias Campaigns o Canvas en una sola vista para que puedas determinar fácilmente qué estrategias de participación han tenido un mayor impacto en tus métricas clave. Tanto para las Campaigns como para los Canvas, puedes exportar los datos y guardar el informe para consultarlo en el futuro.

Para obtener más información sobre los usos de los informes y análisis en Braze, consulta el [resumen de informes]({{site.baseurl}}/user_guide/analytics/reports).

{% endapi %}