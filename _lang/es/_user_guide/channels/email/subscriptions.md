---
nav_title: "Suscripciones"
article_title: "Suscripciones de correo electrónico"
page_order: 5
description: "Este artículo de referencia cubre los diferentes estados de suscripción de los usuarios, cómo gestionar las suscripciones de correo electrónico y cómo segmentar usuarios en función de las mismas."
channel:
  - email
---

# Suscripciones de correo electrónico {#email-subscriptions}

> Aprende sobre los estados globales de suscripción de correo electrónico, los pies de página y las páginas de cancelación de suscripción, los centros de preferencias y la segmentación de Campaigns. Para los grupos de suscripción en todos los canales, consulta [Grupos de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

Este documento es solo para fines informativos. No pretende proporcionar, ni se puede confiar en él como fuente de asesoramiento legal en ningún sentido. El envío de correos electrónicos de marketing y transaccionales puede estar sujeto a requisitos legales específicos. Para asegurarte de que lo haces en cumplimiento con todas las leyes, normas y regulaciones aplicables específicas de tu empresa, debes buscar el asesoramiento de tu equipo legal y/o de cumplimiento normativo.

## Estados de suscripción {#subscription-states}

Braze utiliza estados de suscripción globales para controlar qué usuarios reciben correo electrónico. Para ver las definiciones de `opted-in`, `subscribed` y `unsubscribed`, cómo el estado global difiere de los grupos de suscripción y cómo funciona el estado de suscripción en otros canales, consulta [Estado de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#email).

### Direcciones de correo electrónico con suscripción cancelada {#unsubscribed-email-addresses}

Braze cancela automáticamente la suscripción de cualquier usuario que la cancele manualmente a través de un [pie de página personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer). Si el usuario actualiza su dirección de correo electrónico y **Volver a suscribir a los usuarios cuando actualicen su correo electrónico** está habilitado en **Configuración de envío**, se reanuda el envío normal.

Si un usuario marca uno o más de tus correos electrónicos como correo no deseado, Braze solo envía correos transaccionales a ese usuario. Los correos transaccionales se refieren a la opción **Enviar a todos los usuarios, incluidos los que cancelaron su suscripción** en **Público objetivo**.

{% alert tip %}
Consulta nuestras mejores prácticas de [calentamiento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) para obtener orientación sobre cómo volver a interactuar con tus usuarios de manera efectiva.
{% endalert %}

### Rebotes y correos electrónicos no válidos {#bounces-and-invalid-emails}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}

Cuando una dirección de correo electrónico tiene un rebote duro, Braze no cambia automáticamente el estado de suscripción del usuario a "canceló suscripción". Si una dirección tiene un rebote duro (no es válida o no existe), Braze la marca como no válida y no intenta más envíos. Si el usuario cambia su dirección de correo electrónico, Braze reanuda el envío. Braze reintenta los rebotes blandos durante 72 horas.

### Actualización de los estados de suscripción de correo electrónico {#updating-email-subscription-states}

Hay cuatro formas de actualizar el estado de suscripción de correo electrónico de un usuario:

#### Integración de SDK {#sdk-integration}

Usa el SDK de Braze para actualizar el estado de suscripción de un usuario.

#### REST API

Usa el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para actualizar el [atributo `email_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) de un usuario. Por ejemplo, para establecer el estado de suscripción de correo electrónico de un usuario como cancelado cuando utiliza un enlace de cancelación de suscripción personalizado, incluye `email_subscribe: "unsubscribed"` en los atributos de usuario de tu solicitud.

#### Perfil de usuario {#user-profile}

1. Busca al usuario a través de **Buscar usuarios**.
2. En **Interacción**, selecciona **Canceló suscripción**, **Suscrito** o **Adhesión voluntaria** para cambiar el estado de suscripción del usuario.

El perfil de usuario también muestra una marca de tiempo de cuándo se cambió por última vez la suscripción del usuario. Se registra una marca de tiempo cuando el estado es **Adhesión voluntaria** o **Canceló suscripción**, pero no cuando el estado es **Suscrito**; por ejemplo, un perfil recién creado que nunca ha optado explícitamente por recibir o dejar de recibir no tiene marca de tiempo de suscripción.

#### Centro de preferencias {#preference-center}

Incluye Liquid del [centro de preferencias](#email-preference-center) en la parte inferior de tus correos electrónicos para permitir que los usuarios opten por recibir o dejar de recibir mensajes. Braze administra las actualizaciones del estado de suscripción desde el centro de preferencias.

### Verificación del estado de suscripción de correo electrónico {#checking-email-subscription-state}

![Perfil de usuario de John Doe con su estado de suscripción de correo electrónico establecido en Suscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Usa cualquiera de los siguientes métodos para verificar el estado de suscripción de correo electrónico de un usuario:

1. **Exportación de REST API:** Usa los endpoints [Exportar usuarios por Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) o [Exportar usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para exportar perfiles de usuario individuales en formato JSON.
2. **Perfil de usuario:** Busca el perfil del usuario en la página [Buscar usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles), luego selecciona la pestaña **Interacción** para ver y actualizar manualmente el estado de suscripción de un usuario.

Cuando un usuario actualiza su dirección de correo electrónico, su estado de suscripción se establece como suscrito. Si la dirección de correo electrónico actualizada ya existe en otro lugar dentro de un espacio de trabajo de Braze, el usuario hereda el estado de suscripción de ese usuario existente, a menos que **Volver a suscribir a los usuarios cuando actualicen su configuración de correo electrónico** esté activado en **Configuración de envío**.

Para solucionar problemas con los cambios de estado de suscripción, revisa el evento de Currents [Cambio de estado de suscripción global]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events) (`users.behaviors.subscription.GlobalStateChange`), que incluye el historial y la fuente de los cambios de estado de suscripción.

Las siguientes fuentes pueden desencadenar un cambio en el estado de suscripción de correo electrónico:

| Fuente | Descripción |
| ------ | ----------- |
| SDK | Actualización de atributo de usuario enviada a través de un SDK de Braze |
| REST API | Actualización de atributo de usuario enviada a través del endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) |
| Panel | Estado de suscripción cambiado manualmente en la página del perfil de usuario |
| Importación CSV | Estado de suscripción establecido durante una importación CSV de usuarios |
| Centro de preferencias | El usuario actualizó su preferencia desde un centro de preferencias alojado en Braze |
| Página de suscripción | El usuario seleccionó un enlace de cancelación de suscripción en un correo electrónico y llegó a la página de suscripción de Braze |
| List-Unsubscribe | El usuario canceló la suscripción a través del encabezado nativo list-unsubscribe del cliente de correo electrónico |
| Paso de actualización de usuario en Canvas | Estado de suscripción actualizado por un [paso de actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) en un Canvas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fuentes de actualización del estado de suscripción de correo electrónico" }

Cuando el estado de suscripción global de correo electrónico de un usuario cambia, Braze propaga ese estado a otros perfiles que comparten la misma dirección de correo electrónico, hasta 100 perfiles por cambio. Braze no garantiza la propagación cuando más de 100 perfiles comparten la misma dirección de correo electrónico. Si los usuarios que comparten un correo electrónico muestran diferentes estados de suscripción, ponte en contacto con soporte de Braze.

## Grupos de suscripción {#subscription-groups}

Los grupos de suscripción de correo electrónico permiten a los usuarios adherirse o cancelar su suscripción a categorías específicas de correo electrónico (como boletines informativos o promociones) sin cambiar su estado de suscripción global de correo electrónico. Los grupos que crees están disponibles para añadirlos a tu [centro de preferencias]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

Para obtener más información sobre la creación de grupos, la segmentación, el archivado y el comportamiento específico de cada canal, consulta [Grupos de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups).

## Centro de preferencias de correo electrónico {#email-preference-center}

El centro de preferencias de correo electrónico te permite gestionar qué usuarios reciben boletines de grupos de suscripción. Encuéntralo en el panel en **Grupos de suscripción**. Cada grupo de suscripción que crees se añade a la lista del centro de preferencias.

Para obtener más información sobre cómo añadir o personalizar un centro de preferencias, consulta [Centro de preferencias]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

## Cambio de suscripciones de correo electrónico {#changing-email-subscriptions}

En la mayoría de los casos, los usuarios administran su suscripción de correo electrónico a través de enlaces incluidos en los correos electrónicos que reciben. Inserta un pie de página legalmente conforme con un enlace de cancelación de suscripción en la parte inferior de cada correo electrónico. Cuando los usuarios seleccionan la URL de cancelación de suscripción, Braze cancela su suscripción y muestra una página de confirmación del cambio. Incluye esta etiqueta de Liquid: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

{% alert note %}
Solo puedes usar la etiqueta de Liquid {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%} en Campaigns de correo electrónico y Canvas. No puedes usar esta etiqueta en otros canales de mensajería.
{% endalert %}

Cuando un usuario selecciona "Cancelar suscripción de todos los tipos de correos electrónicos listados" en el centro de preferencias, Braze establece su estado de suscripción global de correo electrónico como `unsubscribed` y cancela su suscripción de todos los grupos.

Las cancelaciones de suscripción del lado del destinatario —enlaces de cancelación de suscripción, list-unsubscribe, envíos del centro de preferencias y cancelaciones de suscripción reportadas por el ESP— aparecen en la tabla `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` de Snowflake. Las cancelaciones de suscripción realizadas a través de la REST API no se incluyen en esa tabla; en su lugar, emiten eventos [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) o [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events). Para el esquema de la tabla, consulta [USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED).

### Creación de pies de página personalizados {#custom-footer}

Si no deseas usar el pie de página predeterminado, crea un pie de página de correo electrónico personalizado a nivel de espacio de trabajo y úsalo como plantilla en cada correo electrónico usando {% raw %}`{{${email_footer}}}`{% endraw %}.

Esto te evita crear un nuevo pie de página para cada plantilla de correo electrónico o Campaign de correo electrónico. Para ver los pasos, consulta [Pie de página de correo electrónico personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer).

#### Administración de estados de suscripción para direcciones IP chinas {#managing-subscription-states-for-chinese-ip-addresses}

Si anticipas direcciones IP chinas, no dependas únicamente de un enlace de cancelación de suscripción para mantener las listas de `unsubscribed`. Proporciona rutas alternativas de cancelación de suscripción, como un ticket de soporte o un correo electrónico de un representante de atención al cliente.

### Creación de una página personalizada para cancelar la suscripción {#creating-a-custom-unsubscribe-page}

Cuando los usuarios seleccionan una URL de cancelación de suscripción en un correo electrónico, abren una página de destino predeterminada que confirma el cambio de suscripción.

Para usar una página de destino personalizada en su lugar:

1. Ve a **Preferencias de correo electrónico** > **Páginas de suscripción y pies de página**.
2. Añade el HTML de tu página personalizada.

Incluye un enlace de resuscripción (por ejemplo {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) para que los usuarios puedan deshacer una cancelación de suscripción accidental. Al igual que {% raw %}`${set_user_to_unsubscribed_url}`{% endraw %}, solo puedes usar esta etiqueta en Campaigns de correo electrónico y Canvas.

También puedes enviar a los usuarios a tu sitio y actualizar el estado con la REST API de Braze (por ejemplo, un enlace con {% raw %}`?user_id={{${user_id}}}`{% endraw %} y luego llamar a [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)).

{% alert note %}
Si usas el pie de página del panel en lugar de solo un bloque de contenido HTML, la plantilla aún debe contener {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} para guardarse. Para usar una URL de cancelación de suscripción diferente temporalmente, puedes comentar la etiqueta predeterminada. Un ejemplo es: {% raw %}`<!-- {{${set_user_to_unsubscribed_url}}} -->`{% endraw %}.
{% endalert %}

![Página personalizada para cancelar la suscripción con una vista previa que dice "¡Lamentamos verte partir!".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Creación de una página personalizada de adhesión voluntaria {#creating-a-custom-opt-in-page}

Usa una página personalizada de adhesión voluntaria para permitir que los usuarios reconozcan y controlen las preferencias de notificación antes de suscribirse. Esta comunicación adicional puede ayudar a que las Campaigns de correo electrónico no terminen en las carpetas de correo no deseado.

1. Ve a **Configuración** > **Preferencias de correo electrónico**.
2. Selecciona **Páginas de suscripción y pies de página**.
3. Personaliza el estilo en la sección **Página personalizada de adhesión voluntaria** para ver cómo indica a tus usuarios que se han suscrito.

Los usuarios llegan a esta página a través de la etiqueta {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}. Al igual que otras etiquetas de Liquid de suscripción de correo electrónico, solo puedes usar esta etiqueta en Campaigns de correo electrónico y Canvas.

{% alert tip %}
Usa un proceso de doble adhesión voluntaria para mejorar el alcance. Braze envía un correo electrónico de confirmación adicional donde el usuario confirma las preferencias de notificación a través de un enlace. Después de la confirmación, el usuario queda con adhesión voluntaria.
{% endalert %}

![Correo electrónico personalizado de adhesión voluntaria con un mensaje "Nos alegra que sigas queriendo saber de nosotros".]({% image_buster /assets/img/custom_optin.png %})

## Suscripciones y segmentación de Campaigns {#subscriptions-and-campaign-targeting}

De forma predeterminada, Braze dirige las Campaigns con mensajes push o de correo electrónico a los usuarios que están suscritos o con adhesión voluntaria. Cambia esto en **Público objetivo** seleccionando el menú desplegable junto a **Enviar a estos usuarios:**.

Braze admite tres estados de segmentación:

- Usuarios que están suscritos o con adhesión voluntaria (predeterminado).
- Solo usuarios con adhesión voluntaria.
- Todos los usuarios, incluidos los que cancelaron su suscripción.

{% alert important %}
Es tu responsabilidad cumplir con todas las [leyes de correo no deseado]({{site.baseurl}}/user_guide/administer/global/privacy/spam_regulations) aplicables al usar esta configuración de segmentación.
{% endalert %}

## Segmentación por suscripciones de usuario {#segmenting-by-user-subscriptions}

Usa los filtros "Estado de suscripción de correo electrónico" y "Estado de suscripción push" para segmentar usuarios por estado de suscripción.

Usa esto para dirigirte a usuarios que no han optado ni por recibir ni por dejar de recibir mensajes, y fomenta una adhesión voluntaria explícita. Crea un segmento con el filtro "El estado de suscripción de correo electrónico/push es Suscrito" y envía Campaigns a usuarios que están suscritos pero no con adhesión voluntaria.

![Estado de suscripción de correo electrónico utilizado como filtro de segmento.]({% image_buster /assets/img_archive/not_optin.png %})