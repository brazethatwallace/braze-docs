---
nav_title: Buenas prácticas
hidden: true
---

# Buenas prácticas sobre el ciclo de vida de los usuarios e identificadores {#user-lifecycle-and-identifiers-best-practices}

## Recopilación de datos {#data-collection}

Más información sobre cómo Braze recopila datos:
- [Recopilación de datos del SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)
- [Buenas prácticas de recopilación de datos]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)
- [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

## Identificadores de Braze {#braze-identifiers}

- `braze_id`: un identificador asignado por Braze que es inalterable y está asociado a un usuario concreto cuando se crea en nuestra base de datos.
- `external_id`: un identificador asignado por el cliente, normalmente un UUID. Recomendamos a los clientes que asignen el `external_id` cuando el usuario pueda ser identificado de forma inequívoca. Una vez identificado un usuario, no puede volver a ser anónimo.
- `user_alias`: un identificador alternativo único que el cliente puede asignar como medio de referenciar al usuario por un ID antes de que se le asigne un `external_id`. Los alias de usuario pueden fusionarse posteriormente con otros alias o con un `external_id` cuando haya uno disponible a través del endpoint [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) de Braze.
    - Dentro del endpoint [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), el campo `merge_behavior` puede utilizarse para especificar qué datos del perfil de alias de usuario deben persistir en el perfil de usuario conocido.
    - Ten en cuenta que para que el alias de usuario sea un perfil al que se pueda enviar mensajes, debes incluir el correo electrónico y/o el teléfono como atributo estándar en el perfil.
- `device_id`: un identificador específico del dispositivo generado automáticamente. Un perfil de usuario puede tener asociados varios `device_ids`. Por ejemplo, un usuario que haya iniciado sesión en su cuenta en la computadora del trabajo, la computadora de casa, la tableta y la aplicación iOS tendría 4 `device_ids` asociados a su perfil.
- Dirección de correo electrónico y número de teléfono:
    - Se admiten como identificador en el endpoint de seguimiento de usuarios de Braze.
    - Cuando se utiliza la dirección de correo electrónico o los números de teléfono como identificador dentro de una solicitud, hay tres resultados posibles:
        1. Si no existe un usuario con este correo electrónico/teléfono en Braze, se creará un perfil de usuario de solo correo electrónico/solo teléfono, y los datos de la solicitud se añadirán al perfil.
        2. Si ya existe un perfil con este correo electrónico/teléfono en Braze, se actualizará para incluir los datos enviados en la solicitud.
        3. En un caso de uso con más de un perfil con este correo electrónico/teléfono, se dará prioridad al perfil actualizado más recientemente.
    - Ten en cuenta que si existe un perfil de usuario de solo correo electrónico/solo teléfono y luego se crea un perfil identificado con el mismo correo electrónico/teléfono (como otro perfil con la misma dirección de correo electrónico Y un ID externo), Braze creará un segundo perfil. Las actualizaciones posteriores irán al perfil con el ID externo.
        - Los dos perfiles pueden fusionarse utilizando el endpoint [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) de Braze

## Gestión de usuarios anónimos {#handling-anonymous-users}

Para un caso de uso en el que necesites crear o actualizar un perfil de usuario en Braze sin tener acceso a un `external_id`, se puede pasar otro identificador, como una dirección de correo electrónico o un número de teléfono, al endpoint [Exportar usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) de Braze para determinar si existe un perfil para el usuario en Braze.

```json
{
 "email_address": "test@example.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Si existe un usuario en Braze con ese correo electrónico o teléfono, se devolverá su perfil. En caso contrario, se devolverá un array "users" vacío. La ventaja de utilizar el endpoint de exportación para determinar si ya existe un usuario con esa dirección de correo electrónico es que te permitirá saber si hay algún perfil de usuario anónimo asociado al usuario. Por ejemplo, un perfil anónimo creado a través del SDK (que tendrá `braze_id`) o un perfil de alias de usuario creado previamente.

Si la solicitud no devuelve un perfil de usuario, puedes elegir entre crear un alias de usuario o crear un usuario de solo correo electrónico:

### Alias de usuario {#user-alias}

Utiliza el endpoint de seguimiento de usuarios para crear un alias de usuario, usando el identificador elegido como nombre del alias. Al incluir `_update_existing_only` como `false` dentro del objeto de atributo, evento o compra donde se define el nuevo alias de usuario, puedes crear el perfil de alias y añadir atributos, eventos y compras a ese perfil simultáneamente.

Para que el alias de usuario sea un perfil al que se pueda enviar mensajes, debes incluir la dirección de correo electrónico en el campo `email`, como se muestra en el siguiente ejemplo.

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

Más adelante podrás identificar y fusionar este alias de usuario con un `external_id` cuando haya uno disponible a través de nuestro endpoint [Identificar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

### Creación de un usuario de solo correo electrónico {#creating-an-email-only-user}

Utiliza la dirección de correo electrónico como identificador en el endpoint de seguimiento de usuarios.

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
Esta funcionalidad está en acceso anticipado.
{% endalert %}

## Sincronización de datos con perfiles de usuario {#syncing-data-to-user-profiles}

[Seguimiento del usuario]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- Se trata de un endpoint de acceso público que puede crear y actualizar usuarios en Braze, como registrar atributos en el perfil de usuario. Este endpoint tiene un límite de velocidad de 50 000 solicitudes por minuto aplicado a nivel de espacio de trabajo.
- Cuando utilices este endpoint, incluye la clave `partner` como se muestra en nuestra documentación para partners.

[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview#what-is-cloud-data-ingestion)
- De forma similar al endpoint de seguimiento del usuario, los datos pueden sincronizarse con los perfiles de usuario a través de Cloud Data Ingestion. Al utilizar esta herramienta, los atributos, eventos y compras se registran en los perfiles configurando y conectando la tabla o vista del almacén de datos que deseas sincronizar con el espacio de trabajo de Braze deseado.

[Puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points)
- Braze tiene un modelo de puntos de datos en el que los puntos de datos se registran por cada "escritura" en el perfil de usuario, independientemente de si el valor ha cambiado. Por este motivo, recomendamos que solo se envíen a Braze los atributos que hayan cambiado.

## Envío de audiencias de usuarios a Braze {#sending-audiences-of-users-to-braze}

[Documentación del partner de sincronización de importación de cohortes]({{site.baseurl}}/partners/isv_partners/cohort_import)<br>
- Las audiencias de usuarios pueden sincronizarse con Braze como una cohorte utilizando los endpoints de la API de importación de cohortes de Braze. En lugar de que estas audiencias se almacenen en el perfil del usuario como atributos de usuario, los clientes pueden crear y dirigirse a esta cohorte a través de un filtro de marca del partner dentro de nuestra herramienta de segmentación. Esto te permite encontrar y dirigirte de forma más eficiente a un segmento concreto de usuarios.
- Los endpoints de importación de cohortes no son públicos y son específicos de cada partner. Por este motivo, las sincronizaciones con los endpoints de cohorte no contarán para los límites de velocidad del espacio de trabajo de un cliente.

[Seguimiento del usuario]({{site.baseurl}}/api/endpoints/user_data/post_user_track)<br>
- Se trata de un endpoint de acceso público que se puede utilizar inmediatamente para crear usuarios en Braze denotando a un usuario en una audiencia concreta a través de un atributo de usuario. La principal diferencia entre este endpoint y el endpoint de importación de cohortes es que las audiencias enviadas mediante este endpoint se almacenarían en el perfil del usuario, mientras que el endpoint de importación de cohortes se mostraría como un filtro en nuestra herramienta de segmentación. Este endpoint tiene un límite de velocidad de 50 000 solicitudes por minuto aplicado a nivel de espacio de trabajo.
- Cuando utilices este endpoint, asegúrate de incluir la clave `partner` como se indica en nuestra [documentación para partners]({{site.baseurl}}/partners/isv_partners/api_partner).

[Puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points)<br>
- Braze tiene un modelo de puntos de datos en el que los puntos de datos se registran por cada "escritura" en el perfil de usuario, independientemente de si el valor ha cambiado.
- Los puntos de datos se generan tanto por la importación de cohortes como por los endpoints de seguimiento del usuario.

## Transmisión de análisis de interacción al partner {#engagement-analytics-streaming-to-partner}

### Currents

Currents es una herramienta de transmisión de análisis de interacción de mensajes casi en tiempo real en Braze. Transmitirá datos a nivel de usuario sobre todos los envíos, entregas, aperturas, clics, etc., de Campaigns y Canvas enviados desde el espacio de trabajo del cliente. Un par de cosas a tener en cuenta: Currents tiene un precio por conector para el cliente, por lo que todos los nuevos partners de Currents deben pasar por un proceso de acceso anticipado. Pedimos a nuestros partners que cuenten con cinco clientes como parte del acceso anticipado antes de crear la interfaz de usuario personalizada y poner el conector a disposición del público.
- [Documentación para partners]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)
- [Eventos de interacción de mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events): todos los clientes que adquieran un conector de Currents tendrán acceso a estos eventos.
- [Eventos de comportamiento del usuario]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events): no todos los clientes que adquieren un conector de Currents adquieren un conector de "todos los eventos" que incluya estos eventos.

### Snowflake Data Share

Los clientes que adquieran un conector de Snowflake Data Share tendrán acceso automático tanto a los eventos de interacción de mensajes como a los de comportamiento del usuario. Cuando se utiliza Snowflake Data Share como integración del partner, Braze proporcionará un recurso compartido a la instancia de Snowflake del partner en nombre del cliente. Como nota, el intercambio de datos entre regiones supone un precio más elevado para nuestros clientes, por lo que pedimos a los partners que deseen integrarse con Snowflake que tengan en cuenta que necesitan una cuenta en `US-EAST-1` y/o `EU-CENTRAL-1`.
- [Documentación para partners]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)

## Creación y activación de Campaigns y Canvas {#building-and-triggering-campaigns-and-canvases}

### Creación de activos en Braze {#creating-assets-in-braze}
Braze ofrece una serie de endpoints que permiten a los clientes y partners crear/actualizar plantillas de correo electrónico y Content Blocks dentro del espacio de trabajo del cliente. Estas plantillas y Content Blocks pueden, a su vez, utilizarse en las Campaigns y Canvas del cliente en Braze.
- Plantillas de correo electrónico
    - [Endpoint para crear plantilla]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
    - [Endpoint para actualizar plantilla]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks)
    - [Endpoint para crear Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
    - [Endpoint para actualizar Content Block]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)

### Campaigns y Canvas activados por API {#api-triggered-campaigns-and-canvases}

Los clientes pueden configurar Campaigns y Canvas para que se activen mediante la API. Las solicitudes de API para activar estas campañas pueden utilizarse para personalizar y segmentar aún más la campaña introduciendo propiedades de activación de API y parámetros de audiencia o destinatario.
- [Activación de campañas a través de la API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body)
    - Las campañas son mensajes singulares, como correos electrónicos individuales.
- [Activación de Canvas mediante API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#request-body)
    - Canvas es una interfaz unificada en la que los especialistas en marketing pueden crear campañas con múltiples mensajes y pasos para formar un recorrido cohesivo. Al activar un Canvas, estás introduciendo a un usuario en el flujo del Canvas, donde seguirá recibiendo mensajes hasta que deje de cumplir los criterios del Canvas.
- [Propiedades de activación de API/propiedades de entrada en Canvas]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    - Datos que pueden introducirse dinámicamente en el mensaje en el momento del envío.

### Campaigns de API {#api-campaigns}
Al crear Campaigns de API (diferentes de las Campaigns activadas por API mencionadas en esta sección), el panel de Braze solo se utiliza para generar un `campaign_id`, que permite al cliente realizar un seguimiento de los análisis para la elaboración de informes de la campaña. El propio mensaje de la campaña se define dentro de la solicitud de la API.
- [Enviar Campaign de API inmediatamente]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [Programar una Campaign de API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)

### ID de envío {#send-ids}
Utiliza el endpoint de Braze para generar un ID de envío que pueda utilizarse para desglosar los análisis de la campaña por envío. Por ejemplo, si se crea un `campaign_id` (Campaign de API) por ubicación, se podría generar un ID de envío por cada envío para realizar un seguimiento del rendimiento de los diferentes mensajes para una ubicación concreta.
- [ID de envío]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)

## Contenido conectado {#connected-content}

El contenido conectado se puede utilizar en cualquier tipo de canal para realizar una solicitud de API al endpoint especificado en el momento del envío y rellenar el mensaje con lo que se devuelva en la respuesta.

La versatilidad del contenido conectado hace que sea una característica utilizada por muchos de nuestros clientes para insertar contenido que no vive o no puede vivir en Braze. Algunos de los casos de uso más comunes que vemos son:
- Plantillas de contenido de blogs o artículos en mensajes
- Recomendaciones de contenido
- Metadatos del producto
- Localización y traducción

Cosas a tener en cuenta:
- Braze no cobra por las llamadas a la API y no contarán para tu uso de puntos de datos.
- Hay un límite de 1 MB para las respuestas de contenido conectado.
- Las llamadas de contenido conectado se realizarán cuando se envíe el mensaje, excepto en el caso de los mensajes dentro de la aplicación, que realizarán esta llamada cuando se visualice el mensaje.
- Las llamadas de contenido conectado no siguen redirecciones. Braze requiere que el tiempo de respuesta del servidor sea inferior a 2 segundos por razones de rendimiento; si el servidor tarda más de 2 segundos en responder, el contenido no se insertará.
- Los sistemas de Braze pueden realizar la misma llamada a la API de contenido conectado más de una vez por destinatario. Esto se debe a que Braze puede necesitar realizar una llamada a la API de contenido conectado para representar la carga útil de un mensaje, y las cargas útiles de los mensajes pueden representarse varias veces por destinatario para validación, lógica de reintento u otros fines internos.

Consulta estos artículos para obtener más información sobre el contenido conectado:
- [Realizar una llamada de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Anular contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)
- [Reintentos de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)