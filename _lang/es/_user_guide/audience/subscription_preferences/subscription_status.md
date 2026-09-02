---
nav_title: Estado de suscripción
article_title: Estado de suscripción
page_order: 0
page_type: reference
description: "Descubre cómo Braze rastrea el estado de suscripción en correo electrónico, LINE, servicio de mensajes cortos, RCS y WhatsApp, y cómo el estado controla la entrega de mensajes."

---

# Estado de suscripción {#subscription-status}

> Descubre cómo Braze rastrea el estado de suscripción en los canales de mensajería, cómo interactúan el estado global y el estado del grupo de suscripción, y dónde se aplican las reglas específicas de cada canal.

El estado de suscripción indica a Braze si un usuario es elegible para recibir mensajes en un canal. El estado puede controlar la segmentación de Campaigns y Canvas, los filtros de Segments y si Braze intenta la entrega.

## Cómo funciona el estado de suscripción en Braze {#how-subscription-status-works-in-braze}

Braze rastrea el estado de suscripción en dos niveles:

| Nivel | Qué controla | Canales |
| ----- | ------------ | ------- |
| Estado de suscripción global | Si un usuario puede recibir mensajes en ese canal en general | Correo electrónico, push |
| Estado del grupo de suscripción | Si un usuario ha optado por un grupo específico dentro de un canal | Correo electrónico, servicio de mensajes cortos, MMS, RCS, WhatsApp, LINE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cómo funciona el estado de suscripción en Braze" }

El estado global y el estado del grupo de suscripción funcionan juntos. Para el correo electrónico, un usuario que se ha dado de baja globalmente no recibirá correos electrónicos aunque esté suscrito a un grupo de suscripción. Para servicio de mensajes cortos, RCS, WhatsApp y LINE, los usuarios deben estar suscritos al grupo de suscripción correspondiente para recibir mensajes de ese grupo.

Puedes ver y actualizar el estado de suscripción en el perfil de un usuario en **Engagement** > **Contact settings**, a través de la REST or transferencia de estado representacional API, el SDK or kit de desarrollo de software, la importación de CSV, los centros de preferencias y los flujos de adhesión voluntaria específicos de cada canal. Braze no cuenta los cambios de estado de suscripción como puntos de datos.

{% alert note %}
Los grupos de suscripción añaden una adhesión voluntaria granular dentro de un canal (por ejemplo, servicio de mensajes cortos promocional frente a transaccional). El estado global de correo electrónico y la pertenencia al grupo de suscripción funcionan juntos a la hora de decidir a quién se puede contactar.
{% endalert %}

## Correo electrónico {#email}

Braze tiene tres estados de suscripción global para el correo electrónico. Estos estados controlan si los usuarios reciben mensajes dirigidos a audiencias suscritas o con adhesión voluntaria. Por ejemplo, los usuarios en el estado `unsubscribed` no reciben mensajes dirigidos a usuarios `subscribed` u `opted-in`.

| Estado | Definición |
| ------ | ---------- |
| Con adhesión voluntaria (opted-in) | Un usuario ha confirmado explícitamente que desea recibir correos electrónicos. Braze recomienda un proceso de adhesión voluntaria explícito para obtener el consentimiento de los usuarios para enviar correos electrónicos. |
| Suscrito (subscribed) | Un usuario no se ha dado de baja ni ha optado explícitamente por recibir correos electrónicos. Este es el estado de suscripción predeterminado cuando se crea un perfil de usuario. |
| Dado de baja (unsubscribed) | Un usuario se ha dado de baja explícitamente de tus correos electrónicos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de suscripción de correo electrónico" }

### Comportamiento específico del correo electrónico {#email-specific-behavior}

- **Cancelaciones de suscripción e informes de correos no deseados:** Braze da de baja automáticamente a los usuarios que cancelan su suscripción a través de un [pie de página personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer). Si un usuario marca un correo electrónico como correo no deseado, Braze solo envía correos transaccionales (mensajes enviados con **Enviar a todos los usuarios, incluidos los dados de baja**).
- **Rebotes duros:** Cuando una dirección de correo electrónico tiene un rebote duro, Braze no establece automáticamente el estado de suscripción del usuario como `unsubscribed`. Braze marca la dirección como no válida y deja de enviar hasta que el usuario actualice su dirección de correo electrónico.
- **Direcciones de correo electrónico compartidas:** Cuando el estado de suscripción global de correo electrónico de un usuario cambia, Braze propaga ese estado a otros perfiles que comparten la misma dirección de correo electrónico, hasta 100 perfiles por cambio.
- **Actualizaciones de dirección de correo electrónico:** Cuando un usuario actualiza su dirección de correo electrónico, su estado de suscripción se establece como `subscribed`, a menos que la dirección actualizada ya exista en otro perfil, en cuyo caso el usuario hereda el estado de ese perfil.

Para actualizar el estado de suscripción, verificar el estado, centros de preferencias y segmentación de campañas, consulta [Suscripciones de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions).

## LINE {#line}

LINE es la fuente de verdad para el estado de suscripción de LINE. Aunque un perfil de usuario tenga un `native_line_id`, Braze no entregará mensajes de LINE a menos que ese usuario siga tu canal de LINE.

El estado de suscripción de LINE se rastrea por `native_line_id`, no por `external_id`. Si varios perfiles comparten el mismo `native_line_id`, heredan el mismo estado de suscripción de LINE.

| Estado | Definición |
| ------ | ---------- |
| Suscrito | El usuario siguió tu canal de LINE desde su aplicación de LINE. |
| Dado de baja | El usuario no ha seguido tu canal de LINE o dejó de seguirlo explícitamente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de suscripción de LINE" }

### Herramienta de sincronización de suscripciones {#subscription-sync-tool}

Después de una integración exitosa del canal de LINE, Braze despliega una herramienta de sincronización de suscripciones para alinear los perfiles existentes de Braze con los datos de seguidores de LINE:

- Los perfiles con un `native_line_id` que siguen tu canal se actualizan a `subscribed`.
- Los seguidores sin un perfil de Braze correspondiente obtienen un perfil anónimo con `native_line_id`, un alias de usuario `line_id` y el estado `subscribed`.

No puedes establecer el estado del grupo de suscripción de LINE manualmente durante la integración: LINE controla el estado y Braze lo sincroniza.

### Actualizaciones de eventos de seguimiento y dejar de seguir {#follow-and-unfollow-event-updates}

Cuando Braze recibe eventos de webhook de LINE para tu canal integrado:

- **Seguir:** Todos los perfiles con un `native_line_id` coincidente se establecen como `subscribed`. Si no existe ningún perfil, Braze [crea un usuario anónimo]({{site.baseurl}}/user_guide/channels/line/message_users/user_management).
- **Dejar de seguir:** Todos los perfiles con un `native_line_id` coincidente se establecen como `unsubscribed`.

Para los pasos de configuración, la reconciliación de usuarios y los ejemplos, consulta [Configuración de LINE]({{site.baseurl}}/user_guide/channels/line/line_setup#user-setup) y [Grupos de suscripción de LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

## servicio de mensajes cortos y RCS {#sms-and-rcs}

servicio de mensajes cortos y RCS utilizan el estado del grupo de suscripción, no un estado global de canal separado. Un usuario puede estar `subscribed` a un grupo transaccional y `unsubscribed` de un grupo promocional al mismo tiempo.

| Estado | Definición |
| ------ | ---------- |
| Suscrito | El usuario está suscrito para recibir servicio de mensajes cortos y RCS de un grupo de suscripción específico, ya sea a través de la API de suscripción de Braze, una palabra clave de adhesión voluntaria u otro método compatible. Cuando la [doble adhesión voluntaria]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) está habilitada, los usuarios deben confirmar la adhesión voluntaria antes de que el estado se actualice a `Subscribed`. |
| Dado de baja | El usuario optó por salir de ese grupo de suscripción enviando una palabra clave de exclusión o a través de la [API de suscripción de Braze]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de suscripción de servicio de mensajes cortos y RCS" }

### Comportamiento específico de servicio de mensajes cortos y RCS {#sms-and-rcs-specific-behavior}

- **Herencia de número de teléfono:** Cuando se añade o actualiza un número de teléfono en un perfil, el número hereda el estado del grupo de suscripción del perfil o de cualquier perfil existente que ya utilice ese número.
- **Gestión de palabras clave:** Los usuarios pueden optar por suscribirse o darse de baja enviando [palabras clave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) predeterminadas o personalizadas. Braze actualiza el estado de suscripción automáticamente.
- **Cumplimiento:** Braze nunca envía servicio de mensajes cortos o RCS a usuarios que no estén suscritos al grupo de suscripción seleccionado.

Para la configuración, el envío y la gestión de grupos de suscripción, consulta [Grupos de suscripción de servicio de mensajes cortos, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).

## WhatsApp {#whatsapp}

WhatsApp también utiliza el estado del grupo de suscripción. Meta requiere un [consentimiento de adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) explícito antes de enviar mensajes de marketing.

| Estado | Definición |
| ------ | ---------- |
| Suscrito | El usuario confirmó explícitamente que desea recibir mensajes de WhatsApp de tu empresa, a través de un flujo de adhesión voluntaria o la API de suscripción de Braze. |
| Dado de baja | El usuario no ha optado por la adhesión voluntaria o su adhesión fue eliminada. Los usuarios dados de baja no reciben mensajes de los números de teléfono de ese grupo de suscripción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de suscripción de WhatsApp" }

### Requisitos de adhesión voluntaria {#opt-in-requirements}

Para enviar mensajes a los usuarios en WhatsApp, proporciona a Braze un `external_id`, un [número de teléfono]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) y un estado de suscripción actualizado para cada usuario. Recopila las adhesiones voluntarias en tu sitio web, aplicación, servicio de mensajes cortos, In-App Messages, hilos de WhatsApp entrantes o mediante una importación de CSV de usuarios que ya optaron por la adhesión en otro lugar.

### Métodos de exclusión {#opt-out-methods}

Los usuarios pueden darse de baja a través de:

- **Flujos de trabajo de palabras clave entrantes:** Canvas o Campaigns activados por palabras clave de exclusión (por ejemplo, "STOP"), con un paso de seguimiento que actualiza el estado de suscripción.
- **Respuestas rápidas de exclusión de marketing:** Plantillas de mensajes con el botón de exclusión de marketing de Meta, combinadas con un paso de actualización del grupo de suscripción en tu Canvas.
- **Bloqueos e informes:** Si un usuario bloquea tu empresa, los mensajes posteriores no se entregan ni se facturan, pero el estado de suscripción de Braze no se actualiza. Los informes de los usuarios tampoco cambian el estado de suscripción.

### Interruptor "Ofertas y anuncios" de WhatsApp {#whatsapp-offers-and-announcements-toggle}

El interruptor nativo de **Ofertas y anuncios** de WhatsApp es independiente de los grupos de suscripción de Braze. Cuando un usuario lo desactiva en WhatsApp, Meta bloquea la entrega de marketing aunque Braze muestre `subscribed`. Las dos capas no se sincronizan automáticamente.

Para flujos de trabajo paso a paso de adhesión voluntaria y exclusión, consulta [Adhesiones voluntarias y exclusiones de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) y [Grupos de suscripción de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

## Segmentar y dirigir por estado de suscripción {#segment-and-target-by-subscription-status}

Usa los filtros de estado de suscripción en el constructor de segmentos para dirigir o suprimir audiencias por canal, por ejemplo, los filtros **Email Subscription Status**, **Push Subscription Status** y **Subscription Group**.

Al crear Campaigns y Canvas, las opciones de **Send Settings** y **Target Audience** te permiten enviar solo a usuarios con un estado de suscripción específico (como suscrito y con adhesión voluntaria). Para las definiciones de filtros de correo electrónico y push, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).