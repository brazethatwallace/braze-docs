---
nav_title: Perfiles de usuario
article_title: Perfiles de usuario
page_order: 2
page_type: reference
tool:
  - Dashboard
description: "Este artículo de referencia describe cómo acceder al perfil de un usuario en el panel, los casos de uso de los perfiles y lo que contiene cada perfil."

---

# Perfiles de usuario {#user-profiles}

> Los perfiles de usuario son una excelente forma de encontrar información sobre usuarios específicos. Todos los datos persistentes asociados a un usuario se almacenan en su perfil de usuario.

## Acceder a los perfiles {#access-profiles}

Para acceder al perfil de un usuario, ve a la página **Buscar usuarios** y busca un usuario por cualquiera de los siguientes criterios:

- ID de usuario externo
- ID de Braze
- Correo electrónico
- Número de teléfono
- Token de notificaciones push
- Alias de usuario con el formato "[user_alias]:[alias_name]", como "amplitude_id:user_123"

Si se encuentra una coincidencia, puedes ver la información que has registrado para este usuario con el SDK de Braze. De lo contrario, si tu búsqueda devuelve varios perfiles de usuario, puedes fusionar cada perfil individualmente o realizar una fusión masiva de usuarios. Para un recorrido completo, consulta [Fusionar usuarios duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

{% alert note %}
**Buscar usuarios** no es lo mismo que **Búsqueda de usuarios** en el creador de Segments o Campaigns. **Búsqueda de usuarios** comprueba si un usuario específico coincide con tu audiencia y solo acepta `external_id` o `braze_id`. **Buscar usuarios** en esta página admite correo electrónico, teléfono, token de notificaciones push y alias de usuario. Para más información, consulta [Probar segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).
{% endalert %}

{% alert important %}
Cuando se utiliza un número de teléfono en la búsqueda, se convierte al formato [`E.164`](https://en.wikipedia.org/wiki/e.164). Los usuarios cuyos números de teléfono no se pueden convertir al formato `E.164` (por ejemplo, porque el número de teléfono tiene un código de país o código de área no válido) no se pueden buscar por número de teléfono.
{% endalert %}

![Resultados de búsqueda con un banner que dice "Varios usuarios coinciden con tus criterios de búsqueda" y dos botones etiquetados Anterior y Siguiente.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Casos de uso {#use-cases}

Los perfiles de usuario son un gran recurso para la solución de problemas y las pruebas, ya que puedes acceder fácilmente a información sobre el historial de participación de un usuario, su pertenencia a segmentos, su dispositivo y su sistema operativo.

Por ejemplo, si un usuario reporta un problema y no estás seguro de qué dispositivo y sistema operativo está utilizando, puedes usar la [pestaña Resumen](#overview-tab) para encontrar esta información (siempre que tengas su correo electrónico o ID de usuario). También puedes ver el idioma de un usuario, lo que podría ser útil si estás solucionando problemas con una [campaña multilingüe]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) que no se comportó como se esperaba.

Puedes usar la [pestaña Interacción](#engagement-tab) para verificar si un usuario determinado recibió una campaña. Además, si este usuario en particular recibió la campaña, puedes ver cuándo la recibió. También puedes verificar si un usuario está en un segmento determinado y si un usuario ha optado por recibir notificaciones push, correo electrónico o ambos. Esta información es útil para la solución de problemas. Por ejemplo, deberías verificar esta información si un usuario no recibe una campaña que esperabas que recibiera o recibe una campaña que no esperabas que recibiera.

## Elementos del perfil de usuario {#elements-of-user-profile}

Hay cinco secciones principales en el perfil de un usuario.

- **Resumen:** Información básica sobre el usuario, datos de sesión, atributos personalizados, eventos personalizados, compras y el dispositivo más reciente en el que el usuario inició sesión.
- **Interacción:** Información sobre la configuración de contacto del usuario, campañas recibidas, segmentos, estadísticas de comunicación, atribución de instalación y número de contenedor aleatorio.
- **Historial de eventos:** Eventos personalizados y compras de los últimos 30 días, con las propiedades completas del evento mostradas como JSON.
- **Historial de mensajes:** Eventos recientes relacionados con mensajería para este usuario de los últimos 30 días.
- **Elegibilidad de conmutadores de características:** Valida para qué conmutadores de características un usuario es actualmente elegible en despliegues, pasos en Canvas y experimentos.

{% tabs %}
{% tab Pestaña Resumen %}

### Pestaña Resumen {#overview-tab}

La pestaña **Resumen** contiene información básica sobre un usuario y sus interacciones con tu aplicación o sitio web.

| Categoría de resumen | Contiene |
| --- | --- |
| Perfil | Género, grupo de edad, ubicación, idioma, configuración regional, zona horaria y fecha de nacimiento. |
| Resumen de sesiones | Cuántas sesiones ha tenido, cuándo fueron su primera y última sesión, y en qué aplicaciones. |
| Atributos personalizados | Qué atributos personalizados están atribuidos a este usuario y su valor asociado, incluidos los atributos personalizados anidados. |
| Dispositivos recientes | En cuántos dispositivos ha iniciado sesión, detalles de cada dispositivo y sus ID de publicidad asociados (si los hay). |
| Eventos personalizados | Qué eventos personalizados ha realizado este usuario, cuántas veces y cuándo realizó cada evento por última vez. |
| Compras | Ingresos de por vida atribuidos a este usuario, su última compra, número total de compras y una lista de cada compra. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pestaña Resumen" }

Para más información sobre estos datos, consulta [Recopilación de datos del SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection).

{% endtab %}
<a id="engagement-tab"></a>
{% tab Pestaña Interacción %}

### Pestaña Interacción {#engagement-tab}

La pestaña **Interacción** contiene información sobre las interacciones de un usuario con los mensajes que le enviaste usando Braze.

| Categoría de interacción | Contiene |
| --- | --- |
| Configuración de contacto | Estado de suscripción para correo electrónico, SMS y push, y los grupos de suscripción con los que este usuario está asociado para estos tres canales. Esta sección también incluye información del registro de cambios para tokens de notificaciones push. Consulta [correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) y [push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) para obtener información sobre cómo se configuran las suscripciones y las adhesiones voluntarias. |
| Campaigns recibidas | **Campaigns recibidas** refleja los tiempos de envío y visualización específicos de cada canal. La mayoría de los canales registran un envío cuando Braze pasa el mensaje al proveedor de entrega, incluso cuando el mensaje no se entrega finalmente. Las **Content Cards** son diferentes: las campañas aparecen aquí solo después de que el usuario visualiza la tarjeta en la aplicación. Para un desglose por canal, consulta [Cuándo aparecen las campañas en Campaigns recibidas](#when-campaigns-appear-in-campaigns-received). <br><br>Cuando un mensaje se recibe, abre o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo identificador de canal que el perfil que registró la interacción (por ejemplo, la misma dirección de correo electrónico para correo electrónico, o el mismo número de teléfono para SMS o WhatsApp). Los usuarios que comparten un identificador con alguien que recibió, abrió o hizo clic en el mensaje pueden coincidir con este filtro incluso si no estaban originalmente en la campaña o no recibieron directamente el mensaje.<br><br>Estas listas utilizan [datos de interacción con mensajes]({{site.baseurl}}/api/data_retention/messaging_interaction_data) (incluidas las reglas de expiración) para determinar lo que aparece para la reorientación y el historial.<br><br> Selecciona una campaña de la lista para verla. |
| Segments | Segments en los que este usuario está incluido. Selecciona un segmento de la lista para verlo. |
| Estadísticas de comunicación | Cuándo este usuario recibió mensajes tuyos por última vez de cada canal. |
| Atribución de instalación | Información sobre cómo y cuándo un usuario instaló tu aplicación. Obtén más información sobre [comprender las instalaciones de usuarios]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/install_attribution). |
| Varios | El [número de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) del usuario. |
| Mensajes de Canvas recibidos | Mensajes de Canvas que este usuario ha recibido y cuándo. Los tiempos de envío siguen las mismas reglas de canal que **Campaigns recibidas**; consulta [Cuándo aparecen las campañas en Campaigns recibidas](#when-campaigns-appear-in-campaigns-received).<br><br> Cuando un mensaje se recibe, abre o se hace clic en él, Braze actualiza los datos de todos los perfiles que comparten el mismo identificador de canal que el perfil que registró la interacción (por ejemplo, la misma dirección de correo electrónico para correo electrónico, o el mismo número de teléfono para SMS o WhatsApp). Los usuarios que comparten un identificador con alguien que recibió, abrió o hizo clic en el mensaje pueden coincidir con este filtro incluso si no estaban originalmente en la campaña o no recibieron directamente el mensaje.<br><br> Selecciona un mensaje de la lista para verlo. |
| Predicciones | Puntuaciones de [predicción de cancelación]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) y [predicción de eventos]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events) para este usuario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pestaña Interacción" }

{% endtab %}
<a id="event-history-tab"></a>
{% tab Pestaña Historial de eventos %}

### Pestaña Historial de eventos {#event-history-tab}

{% alert note %}
Para ver la pestaña **Historial de eventos**, necesitas los [permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) **Buscar usuarios**, **Ver propiedades de eventos de usuario** y **Ver PII**, ya que las propiedades del evento pueden contener datos personales.
{% endalert %}

La pestaña **Historial de eventos** muestra los eventos personalizados y las compras que un usuario ha registrado. Úsala para verificar que los datos de eventos llegan correctamente y solucionar problemas a nivel de usuario directamente en el panel, sin necesidad de exportaciones de datos ni herramientas externas.

| Categoría del historial de eventos | Contiene |
| --- | --- |
| Lista de eventos | Eventos personalizados y compras de los últimos 30 días (hasta los 100 más recientes), ordenados del más nuevo al más antiguo. |
| Tipo de evento | Si la fila es un **Evento personalizado** o una **Compra**. |
| Marca de tiempo | Cuándo se registró el evento. |
| Nombre del evento | El nombre del evento personalizado o la compra. |
| Propiedades del evento | Las propiedades completas del evento, mostradas como JSON. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pestaña Historial de eventos" }

{% endtab %}
{% endtabs %}

### Cuándo aparecen las campañas en Campaigns recibidas {#when-campaigns-appear-in-campaigns-received}

En general, Braze muestra una campaña en **Campaigns recibidas** después de intentar enviar el mensaje. No se requiere una entrega al dispositivo o buzón de entrada del usuario para que se registre un envío. **Mensajes de Canvas recibidos** sigue las mismas reglas específicas de canal para cada tipo de mensaje de Canvas.

- **Correo electrónico:** Braze registra un envío cuando el mensaje se entrega a tu proveedor de servicios de correo electrónico (ESP). Después de esa entrega, el mensaje no se cancela por lógica de Liquid, limitación de velocidad o porque el usuario se marcó como inalcanzable. Los siguientes eventos suelen ser una entrega o un rebote.
- **Push:** Braze registra un envío cuando el mensaje se entrega al proveedor de push (por ejemplo, el servicio de notificaciones push de Apple (APN) o Firebase Cloud Messaging (FCM)). El proveedor generalmente intenta entregar de inmediato; si el dispositivo no está disponible (por ejemplo, sin conexión), el proveedor puede reintentar hasta que el mensaje expire.
- **Mensajes dentro de la aplicación:** Braze registra un envío cuando se lanza la campaña.
- **Content Cards:** Cuándo Braze registra un evento de _Enviado_ depende del tipo de entrega y tu configuración de **Creación de tarjeta**. Una campaña de Content Cards aparece en **Campaigns recibidas** en el perfil de usuario solo después de que el usuario visualiza la tarjeta en la aplicación. Para el desglose completo, consulta [Cuándo se registran los envíos]({{site.baseurl}}/user_guide/channels/content_cards/reporting#when-sends-are-logged) y [Campaigns recibidas y filtros de reorientación]({{site.baseurl}}/user_guide/channels/content_cards/reporting#campaigns-received-and-retargeting-filters) en el artículo de informes de Content Cards.
- **SMS, WhatsApp y webhooks:** Braze registra un envío cuando el mensaje entra en la ruta de entrega para ese canal (por ejemplo, el proveedor de SMS o WhatsApp, o tu endpoint de webhook).

{% alert note %}
Estas descripciones cubren cuándo se registra un envío para **Campaigns recibidas**. Son independientes de las [cancelaciones de mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) que pueden detener un mensaje antes de que llegue a un proveedor.
{% endalert %}

![La pestaña Interacción de un perfil de usuario mostrando su configuración de contacto y estadísticas de comunicación.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Pestaña Historial de mensajes {#messaging-history-tab}

La pestaña **Historial de mensajes** del perfil de usuario muestra eventos recientes relacionados con mensajería (aproximadamente 40) para un usuario individual de los últimos 30 días. Estos eventos incluyen los mensajes que se le enviaron al usuario, que recibió, con los que interactuó, y más.

Los datos de esta pestaña no se actualizan después de que se fusiona un usuario. Además, los eventos asociados con mensajes enviados a través de la API (por ejemplo, el [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#creating-new-users-with-api-sends)) no aparecen en esta pestaña si no se especifica un ID de campaña en esos envíos.

{% alert important %}
Los eventos de RCS actualmente no son compatibles en la pestaña **Historial de mensajes**.
{% endalert %}

![La pestaña Historial de mensajes mostrando qué Campaigns y Canvas ha recibido un usuario.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Ver y comprender los eventos {#viewing-and-understanding-events}

Para cada evento en la tabla **Historial de mensajes**, puedes ver el canal de mensajería, el tipo de evento, la marca de tiempo en que ocurrió el evento, la campaña o mensaje de Canvas asociado, y los datos del dispositivo del usuario. Para filtrar eventos específicos, haz clic en **Filtros** y selecciona eventos de la lista.

##### Eventos de interacción con mensajes {#message-engagement-events}

Los siguientes eventos de interacción con mensajes están disponibles para correo electrónico, SMS, push, mensajes dentro de la aplicación, Content Cards y webhooks. Para obtener más información sobre cómo se rastrean eventos específicos, consulta el [Glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

| Canal | Eventos de interacción disponibles |
| --- | --- |
| Correo electrónico | Rebote<br>Clic<br>Eventos de aplazamiento<br>Entrega<br>Marcar como correo no deseado<br>Apertura (ver [nota sobre el evento de apertura de correo electrónico](#note-on-email-open-event))<br>Envío<br>Rebote blando<br>Cancelar suscripción |
| SMS | Envío del operador<br>Entrega<br>Fallo de entrega<br>Recepción de entrada<br>Rechazo<br>Envío |
| Push | Rebote<br>Apertura influenciada<br>iOS en primer plano<br>Apertura<br>Envío |
| Mensaje dentro de la aplicación | Clic<br>Impresión |
| Content Cards | Clic<br>Descarte<br>Impresión<br>Envío |
| Webhooks | Envío |
| WhatsApp | Cancelación<br>Entrega<br>Fallo<br>Limitación de frecuencia<br>Recepción de entrada<br>Lectura<br>Envío |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos de interacción con mensajes" }

##### Eventos de cancelación de mensajes {#message-abort-events}

Los eventos de cancelación de mensajes ocurren cuando un mensaje enviado a un usuario fue cancelado debido a lógica condicional en [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) o [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content#aborting-messages), o por tiempos de espera en el renderizado de Liquid.

Los eventos de cancelación están disponibles para los siguientes canales:

- Correo electrónico
- SMS
- Push
- Webhooks

Los eventos de cancelación actualmente no están disponibles para mensajes dentro de la aplicación ni Content Cards.

##### Eventos de limitación de frecuencia {#frequency-cap-events}

Un evento de limitación de frecuencia ocurre cuando un usuario califica para recibir un mensaje, pero en realidad no lo recibe debido a la configuración de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#frequency-capping). Puedes personalizar la configuración de limitación de frecuencia desde **Configuración** > **Reglas de limitación de frecuencia**.

##### Destinos en blanco {#blank-destinations}

Algunos envíos de mensajes pueden aparecer en el historial de mensajes con destinos en blanco (indicados por "—"). Esto se debe a que algunos canales, como Content Cards y webhooks, no recopilan datos del dispositivo en el envío del mensaje.

Los envíos de Content Cards se registran cuando la tarjeta está disponible para ser vista. Dado que las Content Cards se pueden ver en múltiples dispositivos, los datos del dispositivo no se registran para un envío. En su lugar, esta información se registra en la impresión (cuando la tarjeta se ve realmente). Los webhooks se envían a un endpoint del sistema (no a un dispositivo), por lo que los datos del dispositivo no son aplicables.

#### Nota sobre el evento de apertura de correo electrónico {#note-on-email-open-event}

El seguimiento de aperturas de correo electrónico es propenso a errores en cualquier herramienta, incluido Braze. Con una variedad de funciones de protección de privacidad ofrecidas por diferentes clientes de correo electrónico que bloquean la carga automática de imágenes o las cargan proactivamente en el servidor, los eventos de apertura de correo electrónico son susceptibles tanto a falsos positivos como a falsos negativos.

Si bien las estadísticas de apertura de correo electrónico pueden ser útiles en conjunto, por ejemplo, para comparar la efectividad de diferentes líneas del asunto, no debes asumir que un evento de apertura individual para un usuario individual es significativo.

#### ¿Por qué ciertos campos están en blanco en la pestaña Historial de mensajes? {#why-are-certain-fields-blank-in-the-message-history-tab}

Algunos campos pueden estar ausentes en la pestaña **Historial de mensajes** de un usuario en los siguientes escenarios:

- Cuando a un evento le faltan datos para **Mensaje enviado**, esto indica que la campaña no tiene variaciones de mensaje.
- Cuando a un evento le faltan datos para **Campaign/Canvas** y **Mensaje enviado**, esto indica que este mensaje fue enviado desde una campaña de API (no campañas activadas por API) que no especificó el `campaign_id` y el `message_variation_id`. Estos campos son opcionales y pueden omitirse del cuerpo de la solicitud. Cuando se especifican estos campos, esa información se completa en los registros del historial de mensajes.
   - Si un mensaje en particular falta completamente del historial de mensajes pero aparece en el registro de **Campaigns recibidas**, es probable que el usuario haya recibido la campaña antes de ser identificado como el usuario actual. Si un perfil existente queda huérfano, el registro de **Campaigns recibidas** se transfiere, pero el historial de mensajes no.
- Cuando faltan datos para **Campaign/Canvas**, es posible que se haya enviado una prueba manual. Las pruebas manuales se registran en la pestaña **Historial de mensajes**, pero la campaña o Canvas que se envió no se registrará.
- Cuando un usuario está en un grupo semilla u otra audiencia de prueba interna, el **Historial de mensajes** puede mostrar metadatos limitados de la campaña o Canvas en comparación con los envíos de producción.

## Artículos relacionados {#related-articles}

- [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [POST: Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [POST: Eliminar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)