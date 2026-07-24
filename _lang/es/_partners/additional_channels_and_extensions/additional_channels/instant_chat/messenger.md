---
nav_title: Messenger
article_title: Facebook Messenger
alias: /partners/messenger/
description: "Este artículo de referencia describe la asociación entre Braze y Facebook Messenger, una de las plataformas de mensajería instantánea más populares del mundo."
page_type: partner
search_tag: Partner

---

# Facebook Messenger

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) es una de las plataformas de mensajería instantánea más populares del mundo, utilizada por casi mil millones de usuarios activos al mes. A través de esta plataforma, las marcas pueden crear chatbots atractivos para interactuar de forma inteligente y automática con sus clientes.

La integración de Braze y Facebook aprovecha las funciones de webhooks, segmentación, personalización y activación de Braze para enviar mensajes a tus usuarios en Facebook Messenger a través de la API de la plataforma Messenger. Nuestra plataforma incluye una plantilla de webhook personalizada para Facebook Messenger en **Contenido** > **Webhook**.

La plataforma Facebook Messenger está pensada para "mensajes no promocionales que faciliten una transacción preexistente, proporcionen otras acciones de atención al cliente o entreguen contenidos solicitados por una persona". Para obtener más información, consulta [las directrices de la plataforma de Facebook](https://developers.facebook.com/docs/messenger-platform) y [ejemplos de casos de uso aceptables](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable).

## Requisitos previos {#prerequisites}

Ten en cuenta lo siguiente antes de proceder con la integración:

- Facebook no permite el uso de la plataforma Messenger para enviar mensajes de marketing.
- Necesitarás el permiso explícito del usuario para enviar mensajes desde tu página.
- Para enviar mensajes a usuarios que no son usuarios de prueba de tu aplicación de Facebook, tu aplicación tendrá que pasar la [revisión de aplicaciones](https://developers.facebook.com/docs/messenger-platform/app-review) de Facebook.<br><br>

| Requisito | Origin | Acceso | Descripción |
| --- | --- | --- | --- |
| Página de Facebook Messenger | Facebook | [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Se utilizará una página de Facebook como identidad de tu bot. Cuando la gente chatee con tu aplicación, verá el nombre de la página y la foto del perfil. |
| Aplicación Facebook Messenger | Facebook | [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | La aplicación de Facebook contiene la configuración de tu bot de Messenger, incluidos los tokens de acceso. |
| Revisión y aprobación del bot de la aplicación | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | Cuando estés listo para lanzar tu bot al público, debes enviarlo a Facebook para su revisión y aprobación. Este proceso de revisión permite asegurarse de que tu bot de Messenger cumple las políticas y funciona como se espera antes de ponerlo a disposición de todo el mundo en Messenger. |
| ID de ámbito de página (PSID) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Necesitas tener los PSID de los usuarios para enviar mensajes en Facebook Messenger. Cuando un usuario interactúa con tu aplicación a través de Messenger, Facebook creará un PSID. Este PSID se puede enviar a Braze como un atributo personalizado de cadena. |
| Token de acceso a la página | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | Estos tokens de acceso son similares a los tokens de acceso de usuario, salvo que proporcionan permiso a las API que leen, escriben o modifican los datos pertenecientes a una página de Facebook. Para obtener un token de acceso a una página, necesitas obtener un token de acceso de usuario y solicitar el permiso `manage_pagespermission`. Una vez que tengas el token de acceso de usuario, obtendrás el token de acceso a la página a través de la API Graph. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Requisitos previos" }

## Integración {#integration}

A continuación se muestra cómo configurar un webhook de Braze para Facebook Messenger.
Si necesitas más ayuda para configurar tu bot, en el [repositorio GitHub de Braze](https://github.com/Appboy/appboy-fb-messenger-bot) encontrarás un tutorial completo sobre el bot de Messenger y un código de ejemplo.

### Paso 1: Recopila tus PSID {#step-1-collect-your-psids}

Para enviar mensajes en Facebook Messenger, necesitas recopilar los identificadores específicos de página (PSID) de tus usuarios para identificarlos e interactuar con ellos de forma coherente. Los PSID no coinciden con el ID de Facebook del usuario. Facebook crea este identificador cada vez que envías un mensaje a un cliente o cuando un cliente te envía un mensaje a ti.

Los PSID se pueden encontrar utilizando uno de los diversos [puntos de entrada](https://developers.facebook.com/docs/messenger-platform/discovery) que ofrece Facebook. Después de que el usuario envíe un mensaje a tu aplicación o realice una acción en una conversación, como pulsar un botón o enviar un mensaje, su PSID se incluirá en la propiedad `sender.id` del evento webhook, para que tu bot pueda identificar quién realizó la acción.

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

Cada vez que envíes un mensaje, su PSID se incluirá en la propiedad `recipient.id` de la solicitud para identificar quién debe recibir el mensaje.

### Paso 2: Enviar a Braze como atributo personalizado {#step-2-send-to-braze-as-a-custom-attribute}

Cuando estés seguro de que recibes los PSID, coordínalo y compártelo con tus desarrolladores para enviar los PSID a Braze como [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#custom-attributes). Los PSID son cadenas a las que se puede acceder mediante una [llamada a la API](https://developers.facebook.com/documentation/business-messaging/messenger-platform/send-messages).

### Paso 3: Configura tu plantilla de webhook {#step-3-set-up-your-webhook-template}

Para crear una plantilla de webhook de Facebook Messenger:

1. Ve a **Contenido** > **Webhook** y selecciona **Crear plantilla de webhook**.
2. Selecciona **Plantillas** > **Plantillas de Braze**.
3. Busca y selecciona la plantilla "Facebook Messenger".
4. Selecciona **Seleccionar plantilla**.

1. Proporciona un nombre de plantilla y añade equipos y etiquetas, según sea necesario.
2. Escribe tu mensaje o elige una plantilla de mensaje de [las que Facebook pone a tu disposición](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages). También puedes elegir el [tipo](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) de mensaje o la [etiqueta](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags).
3. Incluye el PSID como atributo personalizado. Para ello, utiliza el botón **+** azul y blanco situado en la esquina del cuadro **Request Body**.
3. Añade tu token de acceso a la página en la URL del webhook sustituyendo `FACEBOOK_PAGE_ACCESS_TOKEN` por tu token.

#### Previsualizar y probar tu webhook {#previewing-and-testing-your-webhook}

Antes de enviar tu mensaje, prueba tu webhook. Asegúrate de que tu ID de Messenger está guardado en Braze (o búscalo y prueba como usuario personalizado), y utiliza la vista previa para enviar el mensaje de prueba:

![Pestaña de prueba en la plantilla del webhook de Facebook Messenger que muestra que puedes previsualizar el mensaje enviándolo a un usuario existente.]({% image_buster /assets/img_archive/fbm-test.png %})

Si recibes el mensaje correctamente, puedes configurar sus opciones de entrega.

## Uso de esta integración {#using-this-integration}

Una vez configurada, utiliza esta integración para dirigirte a los usuarios de Facebook Messenger. Si no envías mensajes utilizando los números de teléfono de los usuarios y planeas enviar mensajes de Messenger repetidamente, debes [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment) para todos los usuarios para los que exista el ID de Messenger como atributo personalizado y activar el [seguimiento de análisis]({{site.baseurl}}/user_guide/audience/segments/segment_data) para realizar un seguimiento de tus tasas de suscripción a Messenger a lo largo del tiempo.

![Filtro de segmento "messenger_id" configurado como "no está en blanco".]({% image_buster /assets/img_archive/fbm-segmentation.png %})

Si decides no crear un segmento específico para los suscriptores de Messenger, asegúrate de incluir un filtro para el ID de Messenger existente para evitar errores.

También puedes utilizar otra segmentación para orientar tus campañas de Messenger, y el resto del proceso de creación de la campaña funciona como con cualquier otra campaña.