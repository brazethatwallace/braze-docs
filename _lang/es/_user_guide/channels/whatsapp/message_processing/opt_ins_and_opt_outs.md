---
nav_title: "Adhesiones y cancelaciones"
article_title: "Adhesiones y cancelaciones"
description: "Este artículo de referencia cubre los diferentes métodos de adhesión voluntaria y cancelación de suscripción en WhatsApp."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
---

# Adhesión voluntaria y cancelación de suscripción {#opt-in-and-opt-out}

> Gestionar las adhesiones y cancelaciones de WhatsApp es crucial, ya que WhatsApp monitorea tu [calificación de calidad del número de teléfono](https://www.facebook.com/business/help/896873687365001), y una calificación baja puede resultar en la reducción de tus límites de mensajes. <br><br>Una forma de mantener una calificación de alta calidad es evitar que los usuarios bloqueen o reporten tu empresa. Esto se puede lograr proporcionando [mensajes de alta calidad](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (como valor para tus usuarios), controlando la frecuencia de los mensajes y permitiendo que los clientes cancelen la recepción de futuras comunicaciones. <br><br>Esta página cubre cómo configurar adhesiones y cancelaciones, y las diferencias entre los modificadores "regex" e "is".

Las adhesiones pueden provenir de fuentes externas o de métodos de Braze, como SMS o mensajes dentro de la aplicación y en el explorador. Las cancelaciones se pueden gestionar usando palabras clave configuradas en Braze y botones de marketing de WhatsApp. Consulta los siguientes métodos como guía para configurar adhesiones y cancelaciones.

#### Métodos de adhesión voluntaria {#opt-in-methods}
- [Métodos de adhesión externos a Braze](#external-to-braze-opt-in-methods)
  - [Lista de adhesión creada externamente](#externally-built-opt-in-list)
  - [Mensaje saliente en el canal de soporte al cliente de WhatsApp](#outbound-message-in-customer-support-whatsapp-channel)
  - [Mensaje entrante de WhatsApp](#inbound-whatsapp-message)
- [Métodos de adhesión con Braze](#braze-powered-opt-in-methods)

#### Métodos de cancelación {#opt-out-methods}
- [Palabras clave generales de cancelación](#general-opt-out-keywords)
- [Selección de cancelación de marketing](#marketing-opt-out-selection)

## Configurar adhesiones para tu canal de WhatsApp en Braze {#set-up-opt-ins-for-your-braze-whatsapp-channel}

Para las adhesiones de WhatsApp, debes cumplir con los [requisitos de WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). También necesitarás proporcionar a Braze la siguiente información:
- Un `external_id`, un [número de teléfono]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers/) y un estado de suscripción actualizado para cada usuario. Esto se puede hacer usando el [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) o a través del [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar el número de teléfono y el estado de suscripción.

{% alert note %}
Braze lanzó una mejora en el punto de conexión `/users/track` que permite actualizaciones del estado de suscripción. Puedes obtener más información en [Grupos de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/#update-subscription-status). Sin embargo, si ya has creado protocolos de adhesión usando el [punto de conexión `/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/), puedes continuar haciéndolo allí.
{% endalert %}

### Métodos de adhesión externos a Braze {#external-to-braze-opt-in-methods}

Tu aplicación o sitio web (registro de cuenta, página de pago, configuración de cuenta, terminal de tarjeta de crédito) hacia Braze.

Donde ya tengas consentimiento de marketing para correo electrónico o mensajes de texto, incluye una sección adicional para WhatsApp. Después de que un usuario se adhiera, necesita un `external_id`, un [número de teléfono]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers/) y un estado de suscripción actualizado. Para hacer esto, dependiendo de cómo esté configurada tu instalación de Braze, aprovecha el [punto de conexión `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) o usa el [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Lista de adhesión creada externamente {#externally-built-opt-in-list}

Si has usado WhatsApp anteriormente, es posible que ya hayas creado una lista de usuarios con adhesiones según los requisitos de WhatsApp. En este caso, carga un CSV o usa la API con la [siguiente información]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#csv) en Braze.

#### Mensaje saliente en el canal de soporte al cliente de WhatsApp {#outbound-message-in-customer-support-whatsapp-channel}

En tu canal de soporte al cliente, haz un seguimiento de los problemas resueltos con un mensaje automático preguntando si desean adherirse a los mensajes de marketing. La funcionalidad aquí depende de la disponibilidad de características en tu herramienta de soporte al cliente elegida y de dónde almacenas la información del usuario.

1. Proporciona un [enlace de mensaje](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) desde tu número de teléfono de WhatsApp Business.
2. Proporciona [acciones de respuesta rápida]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users/#quick-replies) donde el cliente responda "Sí" para indicar la adhesión.
3. Configura un desencadenador de palabra clave personalizada.
4. Para cualquiera de esas ideas, probablemente necesitarás completar el flujo con lo siguiente:
	- Llamar al [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar o crear un usuario.
	- Aprovechar el [punto de conexión `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) o usar el [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Mensaje entrante de WhatsApp {#inbound-whatsapp-message}

Haz que los clientes envíen un mensaje entrante al número de WhatsApp.

Esto se puede configurar como un Canvas o una campaña, dependiendo de si deseas que el usuario reciba un mensaje de confirmación en el nuevo canal.

1. Crea una campaña con el desencadenador de entrega basada en acciones de un mensaje entrante.
2. Crea una campaña de webhook. Para ver un ejemplo de webhook, consulta [Grupos de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs/#update-subscription-status).

{% alert tip %}
Ten en cuenta que puedes crear una URL o un código QR para unirse a un canal de WhatsApp desde el [administrador de WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/) en **Phone Number** > **Message Links**.<br>![Compositor de código QR de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Métodos de adhesión con Braze {#braze-powered-opt-in-methods}

#### Mensaje SMS {#sms-message}

En Canvas, configura una campaña que pregunte a los clientes si desean adherirse a recibir mensajes de WhatsApp usando uno de los siguientes métodos:
- Segmento de clientes: grupo de marketing suscrito fuera de EE. UU.
- Configuración de desencadenador de palabra clave personalizada

Obtén más información sobre cómo actualizar el estado de suscripción de los perfiles de usuario en [Grupos de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/#update-subscription-status).

#### Mensaje dentro de la aplicación o en el explorador {#in-app-or-in-browser-message}

Crea un mensaje dentro de la aplicación o una ventana emergente en el explorador que invite a los clientes a adherirse al uso de WhatsApp.

Usa un [mensaje HTML dentro de la aplicación](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) con el ["puente" de JavaScript]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/#javascript-bridge) para interactuar con el SDK de Braze. Asegúrate de usar el ID del grupo de suscripción de WhatsApp.

#### Formulario de captura de número de teléfono {#phone-number-capture-form}

Usa la plantilla de [formulario de captura de número de teléfono]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture/) en el editor de arrastrar y soltar para mensajes dentro de la aplicación para recopilar números de teléfono de los usuarios y hacer crecer tus grupos de suscripción de WhatsApp.

## Configurar cancelaciones para tu canal de WhatsApp en Braze {#set-up-opt-outs-for-your-braze-whatsapp-channel}

### Interruptor de "Ofertas y anuncios" de WhatsApp {#whatsapp-offers-and-announcements-toggle}

WhatsApp proporciona un interruptor de "Ofertas y anuncios" en la configuración de la aplicación que permite a los usuarios cancelar la recepción de mensajes de marketing. Este interruptor funciona de forma independiente de los grupos de suscripción de Braze:

- **Los grupos de suscripción de Braze** se gestionan a través de tu integración con Braze (API, centro de preferencias o SDK) y controlan a qué usuarios diriges tus mensajes.
- **El interruptor nativo de WhatsApp** es controlado por Meta y se aplica a nivel de plataforma, fuera de Braze.

Estas dos capas no se sincronizan automáticamente por diseño. Cuando un usuario desactiva el interruptor de "Ofertas y anuncios" en WhatsApp, Meta bloquea la entrega de mensajes de marketing a nivel de plataforma, incluso si el estado de suscripción del usuario en Braze aparece como "Suscrito". La preferencia del usuario se respeta en el momento de la entrega.

{% alert note %}
Dado que Braze no recibe una señal de cancelación hasta que se intenta un envío y Meta devuelve un error, los recuentos de suscripción en Braze pueden no reflejar a los usuarios que han cancelado a través del interruptor de WhatsApp hasta que se intente enviar un mensaje. Esto significa que las estimaciones de alcance pueden estar ligeramente sobreestimadas hasta que se produzca ese ciclo de retroalimentación.
{% endalert %}

### Palabras clave generales de cancelación {#general-opt-out-keywords}

Puedes configurar una campaña o un Canvas que permita a los usuarios que envíen ciertas palabras cancelar la recepción de futuros mensajes. Los Canvas pueden ser especialmente beneficiosos, ya que te permiten incluir un mensaje de seguimiento que confirme la cancelación exitosa.

#### Paso 1: Crea un Canvas con un desencadenador de "Mensaje entrante de WhatsApp" {#step-1-create-a-canvas-with-a-trigger-of-inbound-whatsapp-message}

![Paso de entrada de Canvas basado en acciones que ingresa a los usuarios que envían un mensaje entrante de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Al seleccionar desencadenadores de palabras clave, incluye palabras como "Stop" o "No Message". Si eliges este método, asegúrate de que tus clientes conozcan tus palabras de cancelación. Por ejemplo, después de recibir la adhesión inicial, incluye una respuesta de seguimiento como "Para cancelar estos mensajes, envía "Stop" en cualquier momento."

![Paso de mensaje para enviar un mensaje entrante de WhatsApp donde el cuerpo del mensaje es "STOP" o "NO MESSAGE".]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Paso 2: Actualiza el perfil del usuario {#step-2-update-the-users-profile}

Actualiza el perfil del usuario usando uno de los métodos descritos en [Grupos de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/#update-subscription-status).

### Selección de cancelación de marketing {#marketing-opt-out-selection}

Dentro del creador de plantillas de mensajes de WhatsApp, puedes incluir la opción de "cancelación de marketing". Cada vez que incluyas esto, asegúrate de que la plantilla se use en un Canvas con un paso posterior para un cambio de grupo de suscripción.

1. Crea una plantilla de mensaje con la respuesta rápida de "cancelación de marketing".<br>![Plantilla de mensaje con una opción de pie de página de "Cancelación de marketing".]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Sección para configurar un botón de cancelación de marketing.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Crea un Canvas que use esta plantilla de mensaje.<br><br>
3. Sigue los pasos del ejemplo anterior pero con el texto desencadenador "STOP PROMOTIONS".<br><br>
4. Actualiza el estado de suscripción del usuario usando uno de los métodos descritos en [Grupos de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/#update-subscription-status).

## Configurar flujos de trabajo de adhesión y cancelación {#set-up-opt-in-and-opt-out-workflows}

Puedes configurar flujos de trabajo de respuesta a las palabras clave "START" y "STOP" para WhatsApp con estos dos métodos:

- [Paso de Actualización de usuario](#user-update-step)
- [Campaña de webhook para desencadenar una segunda campaña de WhatsApp](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Paso de Actualización de usuario {#user-update-step}

El [paso de Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) puede agregar el número de teléfono del usuario al grupo de suscripción de WhatsApp cuando el usuario envía una palabra clave al número de teléfono del grupo de suscripción.

El paso de Actualización de usuario evita condiciones de carrera porque el usuario no avanzará al siguiente paso en el Canvas antes de que su número de teléfono se agregue al grupo de suscripción. También tiene menos pasos de configuración que los otros métodos, por lo que Braze generalmente recomienda este método.

1. Crea un Canvas con el paso basado en acciones **Send a WhatsApp Inbound Message**. Selecciona **Where the message body** e ingresa "START" para **Is**.

{% alert important %}
Para los mensajes "STOP", invierte el paso del mensaje que confirma la cancelación y el paso de Actualización de usuario. Si no lo haces, el usuario será eliminado del grupo de suscripción primero y luego no será elegible para recibir el mensaje de confirmación.
{% endalert %}

![Un paso de mensaje de WhatsApp donde el cuerpo del mensaje es "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. En el Canvas, crea un paso de **Set Up User Update** y para **Action** selecciona **Advanced JSON Editor**. <br><br>![Paso de Actualización de usuario con una acción de "Advanced JSON Editor".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3. Completa el **User Update object** con la siguiente carga útil JSON, reemplazando `XXXXXXXXXXX` con tu ID de grupo de suscripción:

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4. Agrega un paso posterior de mensaje de WhatsApp. <br><br>![Paso de Actualización de usuario en un Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Consideraciones {#considerations}

La actualización puede completarse a velocidades variables porque Braze agrupa las solicitudes del [paso de Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) en lotes.

### Campaña de webhook para desencadenar una segunda campaña de WhatsApp {#webhook-campaign-to-trigger-a-second-whatsapp-campaign}

Una campaña de webhook puede desencadenar la entrada a una segunda campaña después de agregar el número de teléfono del usuario al grupo de suscripción de WhatsApp cuando el usuario envía una palabra clave al número de teléfono del grupo de suscripción.

{% alert important %}
No necesitas usar este método para los mensajes STOP. El mensaje de confirmación se enviará antes de que el usuario sea eliminado del grupo de suscripción, por lo que puedes usar uno de los otros dos pasos.
{% endalert %}

1. Crea una campaña o un Canvas con un paso basado en acciones **Send a WhatsApp Inbound Message**. Selecciona **Where the message body** e ingresa "START" para **Is**.

![Paso de mensaje de WhatsApp donde el cuerpo del mensaje es "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2. En la campaña o el Canvas, crea un paso de mensaje de webhook y cambia el **Request Body** a **Raw Text**.

![Paso de mensaje para un webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3. Ingresa la [URL del punto de conexión]({{site.baseurl}}/api/basics/) del cliente en la **Webhook URL**, seguida del enlace del punto de conexión `campaigns/trigger/send`. Por ejemplo, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Campo de URL del webhook en la sección "Compose Webhook".]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4. En el texto sin formato, ingresa la siguiente carga útil JSON y reemplaza `XXXXXXXXXXX` con tu ID de grupo de suscripción. Necesitarás reemplazar el `campaign_id` después de crear tu segunda campaña.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5. Crea una campaña de WhatsApp (tu segunda campaña) y configura el desencadenador como API. Asegúrate de copiar este `campaign_id` en la carga útil JSON de tu primera campaña.

#### Consideraciones

- Las actualizaciones de atributos desde la carga útil JSON del desencadenador de API del Canvas aún no son compatibles, por lo que solo puedes desencadenar una campaña de WhatsApp para el mensaje de respuesta de WhatsApp (como en el paso 2).
- Una plantilla de WhatsApp debe estar aprobada para enviarla como mensaje de respuesta. Esto se debe a que una respuesta rápida requiere que el desencadenador del mensaje entrante esté dentro de la misma campaña o Canvas. Si usas un [paso de Actualización de usuario](#user-update-step), puedes enviar un mensaje de respuesta rápida sin la aprobación de Meta.

## Comprender la diferencia entre los modificadores "regex" e "is" {#understanding-the-difference-between-regex-and-is-modifiers}

En esta tabla, se usa `STOP` como ejemplo de palabra desencadenadora para demostrar cómo funcionan los modificadores.

| Modificador | Palabra desencadenadora | Acción |
| --- | --- | --- |
| `Is` | `STOP` | Captura cualquier uso de la palabra completa "stop" sin importar las mayúsculas o minúsculas. Por ejemplo, captura "stop" pero no "please stop". |
| `Matches regex` | `STOP` | Captura cualquier uso de "STOP" en esa combinación exacta de mayúsculas y minúsculas. Por ejemplo, captura "STOP" y "PLEASE STOP" pero no "stop". |
| `Matches regex` | `(?i)STOP(?-i)` | Captura cualquier uso de "STOP" en cualquier combinación de mayúsculas y minúsculas. Por ejemplo, captura "stop", "please stop" y "never stop sending me messages". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comprender la diferencia entre los modificadores regex e is" }