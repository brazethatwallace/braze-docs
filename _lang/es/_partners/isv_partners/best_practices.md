---
nav_title: Buenas prácticas
hidden: true
---

# Buenas prácticas sobre el ciclo de vida de los usuarios e identificadores {#user-lifecycle-and-identifiers-best-practices}

## Recopilación de datos {#data-collection}

Obtén más información sobre cómo Braze recopila datos:
- [Recopilación de datos del SDK or kit de desarrollo de software]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)
- [Buenas prácticas de recopilación de datos]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)
- [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

## Identificadores de Braze {#braze-identifiers}

- `braze_id`: Un identificador asignado por Braze que es inalterable y está asociado con un usuario en particular cuando se crea en nuestra base de datos.
- `external_id`: Un identificador asignado por el cliente, generalmente un UUID. Recomendamos que los clientes asignen el `external_id` cuando el usuario pueda ser identificado de forma única. Después de que un usuario es identificado, no se puede revertir a anónimo.
- `user_alias`: Un identificador alternativo único que el cliente puede asignar como medio para hacer referencia al usuario mediante un ID antes de que se asigne un `external_id`. Los alias de usuario se pueden fusionar posteriormente con otros alias o con un `external_id` cuando uno esté disponible a través del endpoint [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) de Braze.
    - Dentro del endpoint [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), el campo `merge_behavior` se puede utilizar para especificar qué datos del perfil del alias de usuario deben conservarse en el perfil del usuario conocido.
    - Ten en cuenta que para que el alias de usuario sea un perfil al que se puedan enviar mensajes, debes incluir el correo electrónico o el teléfono como atributo estándar en el perfil.
- `device_id`: Un identificador generado automáticamente y específico del dispositivo. Un perfil de usuario puede tener varios `device_ids` asociados. Por ejemplo, un usuario que haya iniciado sesión en su cuenta desde su computadora del trabajo, su computadora personal, su tableta y su aplicación para iOS tendrá 4 `device_ids` asociados con su perfil.
- Dirección de correo electrónico y número de teléfono:
    - Compatibles como identificador en el endpoint de seguimiento de usuarios de Braze.
    - Cuando se utiliza la dirección de correo electrónico o el número de teléfono como identificador en una solicitud, hay tres resultados posibles:
        1. Si un usuario con este correo electrónico/teléfono no existe en Braze, se creará un perfil de usuario solo con correo electrónico/teléfono, y cualquier dato en la solicitud se añadirá al perfil.
        2. Si ya existe un perfil con este correo electrónico/teléfono en Braze, se actualizará para incluir cualquier dato enviado en la solicitud.
        3. En un caso de uso con más de un perfil con este correo electrónico/teléfono, se priorizará el perfil actualizado más recientemente.
    - Ten en cuenta que si existe un perfil de usuario solo con correo electrónico/teléfono y luego se crea un perfil identificado con el mismo correo electrónico/teléfono (como otro perfil con la misma dirección de correo electrónico Y un ID externo), Braze creará un segundo perfil. Las actualizaciones posteriores se dirigirán al perfil con el ID externo.
        - Los dos perfiles se pueden fusionar utilizando el endpoint [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) de Braze

## Manejo de usuarios anónimos {#handling-anonymous-users}

Para un caso de uso en el que necesites crear o actualizar un perfil de usuario en Braze sin tener acceso a un `external_id`, se puede pasar otro identificador, como una dirección de correo electrónico o un número de teléfono, al endpoint de Braze [Exportar usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para determinar si existe un perfil del usuario dentro de Braze.

```json
{
 "email_address": "test@example.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Si un usuario existe en Braze con ese correo electrónico o teléfono, se devolverá su perfil. De lo contrario, se devolverá un array de "users" vacío. La ventaja de usar el endpoint de exportación para determinar si ya existe un usuario con esa dirección de correo electrónico es que te permite identificar si hay perfiles de usuarios anónimos asociados con ese usuario. Por ejemplo, un perfil anónimo creado a través del SDK or kit de desarrollo de software (que tendrá un `braze_id`) o un perfil de alias de usuario creado previamente.

Si la solicitud no devuelve un perfil de usuario, puedes optar por crear un alias de usuario o crear un usuario solo con correo electrónico:

### Alias de usuario {#user-alias}

Usa el endpoint de seguimiento de usuarios para crear un alias de usuario, utilizando el identificador que elijas como nombre del alias. Al incluir `_update_existing_only` como `false` dentro del objeto de atributo, evento o compra donde se define el nuevo alias de usuario, puedes crear el perfil de alias y añadir atributos, eventos y compras a ese perfil de forma simultánea.

Para que el alias de usuario sea un perfil al que se puedan enviar mensajes, debes incluir la dirección de correo electrónico en el campo `email`, como se muestra en el siguiente ejemplo.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@example.com",
       "alias_label" : "email"
     },
     "email": "test@example.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

Posteriormente, puedes identificar y fusionar este alias de usuario con un `external_id` cuando esté disponible a través de nuestro endpoint [Identificar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

### Crear un usuario solo con correo electrónico {#creating-an-email-only-user}

Usa la dirección de correo electrónico como identificador en el endpoint de seguimiento de usuarios.

```json
{
    "attributes": [
        {
            "email": "test@example.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
Esta funcionalidad se encuentra en acceso anticipado.
{% endalert %}

## Sincronización de datos con perfiles de usuario {#syncing-data-to-user-profiles}

[User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- Este es un endpoint de acceso público que puede crear y actualizar usuarios en Braze, como registrar atributos en el perfil de usuario. Este endpoint tiene un límite de velocidad de 50.000 solicitudes por minuto aplicado a nivel del espacio de trabajo.
- Cuando uses este endpoint, incluye la clave `partner` como se muestra en nuestra documentación de partners.

[Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview#what-is-cloud-data-ingestion)
- De forma similar al endpoint de user track, los datos pueden sincronizarse con los perfiles de usuario a través de la ingesta de datos en la nube. Cuando uses esta herramienta, los atributos, eventos y compras se registran en los perfiles configurando y conectando la tabla o vista del almacén de datos que deseas sincronizar con el espacio de trabajo de Braze deseado.

[Puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points)
- Braze tiene un modelo de puntos de datos en el que los puntos de datos se registran por cada "escritura" en el perfil de usuario, independientemente de si el valor ha cambiado. Por esta razón, recomendamos que solo se envíen a Braze los atributos que hayan cambiado.

## Envío de audiencias de usuarios a Braze {#sending-audiences-of-users-to-braze}

[Documentación de sincronización del partner de importación de cohortes]({{site.baseurl}}/partners/isv_partners/cohort_import)<br>
- Las audiencias de usuarios se pueden sincronizar con Braze como una cohorte utilizando los endpoints de la API de importación de cohortes de Braze. En lugar de almacenar estas audiencias en el perfil de usuario como atributos de usuario, los clientes pueden crear y segmentar esta cohorte a través de un filtro con la marca del partner dentro de nuestra herramienta de segmentación. Esto te permite encontrar y segmentar de manera más eficiente un grupo particular de usuarios.
- Los endpoints de importación de cohortes no son públicos y son específicos de cada partner. Por esta razón, las sincronizaciones con los endpoints de cohortes no contarán para los límites de velocidad del espacio de trabajo de un cliente.

[Seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track)<br>
- Este es un endpoint de acceso público que se puede utilizar de inmediato para crear usuarios en Braze indicando que un usuario pertenece a una audiencia particular a través de un atributo de usuario. La diferencia principal entre este endpoint y el endpoint de importación de cohortes es que las audiencias enviadas con este endpoint se almacenan en el perfil de usuario, mientras que el endpoint de importación de cohortes se muestra como un filtro en nuestra herramienta de segmentación. Este endpoint tiene un límite de velocidad de 50 000 solicitudes por minuto aplicado a nivel de espacio de trabajo.
- Al utilizar este endpoint, asegúrate de incluir la clave `partner` como se muestra en nuestra [documentación del partner]({{site.baseurl}}/partners/isv_partners/api_partner).

[Puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points)<br>
- Braze tiene un modelo de puntos de datos en el que se registra un punto de datos por cada "escritura" en el perfil de usuario, independientemente de si el valor ha cambiado.
- Los puntos de datos se generan tanto con la importación de cohortes como con los endpoints de seguimiento de usuarios.

## Análisis de participación con transmisión al partner {#engagement-analytics-streaming-to-partner}

### Currents

Currents es una herramienta de transmisión de análisis de participación de mensajes en tiempo casi real en Braze. Transmite datos a nivel de usuario sobre todos los envíos, entregas, aperturas, clics, etc., de Campaigns y Canvas enviados desde el espacio de trabajo del cliente. Un par de cosas a tener en cuenta: Currents se cobra por conector para el cliente, por lo que todos los nuevos partners de Currents deben pasar por un proceso de acceso anticipado (EA). Pedimos que nuestros partners tengan cinco clientes como parte del EA antes de que construyamos la interfaz personalizada con marca y hagamos el conector disponible públicamente.
- [Documentación del partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)
- [Eventos de participación de mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) - todos los clientes que adquieren un conector de Currents tendrán acceso a estos eventos.
- [Eventos de comportamiento del usuario]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) - no todos los clientes que adquieren un conector de Currents comprarán un conector de "todos los eventos" que incluya estos eventos.

### Snowflake Data Share

Los clientes que adquieren un conector de Snowflake Data Share tendrán acceso automáticamente tanto a los eventos de participación de mensajes como a los eventos de comportamiento del usuario. Cuando se utiliza Snowflake Data Share como integración del partner, Braze proporcionará un recurso compartido a la instancia de Snowflake del partner en nombre del cliente. Como nota, el uso compartido de datos entre regiones tiene un precio más alto para nuestros clientes, por lo que pedimos a los partners que deseen integrarse con Snowflake que tengan en cuenta que necesitan una cuenta en `US-EAST-1` y/o `EU-CENTRAL-1`.
- [Documentación del partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)

## Creación y desencadenamiento de campañas y Canvas {#building-and-triggering-campaigns-and-canvases}

### Creación de activos en Braze {#creating-assets-in-braze}
Braze ofrece una serie de endpoints que permiten a los clientes y partners crear o actualizar plantillas de correo electrónico y Content Blocks dentro del espacio de trabajo de un cliente. Estas plantillas y Content Blocks pueden, a su vez, utilizarse en las Campaigns y Canvas del cliente en Braze.
- Plantillas de correo electrónico
    - [Endpoint de creación de plantilla]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
    - [Endpoint de actualización de plantilla]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
    - [Endpoint de creación de Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
    - [Endpoint de actualización de Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)

### Campaigns y Canvas desencadenados por API {#api-triggered-campaigns-and-canvases}

Los clientes pueden configurar Campaigns y Canvas para que se desencadenen por API. Las solicitudes de API para desencadenar estas campañas pueden utilizarse para personalizar y segmentar aún más la campaña, pasando propiedades de desencadenamiento de API y parámetros de audiencia o destinatario.
- [Desencadenar Campaigns a través de API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body)
    - Las Campaigns son mensajes individuales, como correos electrónicos específicos.
- [Desencadenar Canvas a través de API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#request-body)
    - Canvas es una interfaz unificada donde los especialistas en marketing pueden crear campañas con múltiples mensajes y pasos para formar un recorrido cohesivo. Al desencadenar un Canvas, estás ingresando a un usuario en el flujo de Canvas, donde continuará recibiendo mensajes hasta que ya no cumpla con los criterios del Canvas.
- [Propiedades de desencadenamiento de API/propiedades de entrada de Canvas]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    - Datos que pueden completarse dinámicamente en el mensaje en el momento del envío.

### Campaigns de API {#api-campaigns}
Al crear Campaigns de API (diferentes de las Campaigns desencadenadas por API mencionadas en esta sección), el panel de Braze solo se utiliza para generar un `campaign_id`, que permite al cliente realizar un seguimiento de los análisis para los informes de la campaña. El mensaje de la campaña en sí se define dentro de la solicitud de API.
- [Enviar Campaign de API inmediatamente]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [Programar una Campaign de API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)

### ID de envío {#send-ids}
Utiliza el endpoint de Braze para generar un ID de envío que se pueda usar para desglosar los análisis de la campaña por envío. Por ejemplo, si se crea un `campaign_id` (Campaign de API) por ubicación, se podría generar un ID de envío por cada envío para realizar un seguimiento del rendimiento de los diferentes mensajes en una ubicación particular.
- [ID de envío]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)

## Contenido conectado {#connected-content}

El contenido conectado se puede utilizar en cualquier tipo de canal para realizar una solicitud de API al endpoint especificado en el momento del envío y completar lo que se devuelve en la respuesta dentro del mensaje.

La versatilidad del contenido conectado hace de esta una característica utilizada por muchos de nuestros clientes para insertar contenido que no está o no puede estar en Braze. Algunos de los ejemplos más comunes que vemos son:
- Insertar contenido de blogs o artículos en los mensajes
- Recomendaciones de contenido
- Metadatos de productos
- Localización y traducción

Aspectos a tener en cuenta:
- Braze no cobra por las llamadas a la API y no se contabilizarán en tu uso de punto de datos.
- Existe un límite de 1 MB para las respuestas de contenido conectado.
- Las llamadas de contenido conectado se realizarán cuando se envíe el mensaje, excepto en el caso de los mensajes dentro de la aplicación, que realizarán esta llamada cuando se visualice el mensaje.
- Las llamadas de contenido conectado no siguen redirecciones. Braze requiere que el tiempo de respuesta del servidor sea inferior a 2 segundos por motivos de rendimiento; si el servidor tarda más de 2 segundos en responder, el contenido no se insertará.
- Los sistemas de Braze pueden realizar la misma llamada a la API de contenido conectado más de una vez por destinatario. Esto se debe a que Braze puede necesitar realizar una llamada a la API de contenido conectado para representar la carga útil de un mensaje, y las cargas útiles de los mensajes pueden representarse varias veces por destinatario para validación, lógica de reintentos u otros fines internos.

Consulta estos artículos para obtener más información sobre el contenido conectado:
- [Realizar una llamada de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Cancelar contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)
- [Reintentos de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)