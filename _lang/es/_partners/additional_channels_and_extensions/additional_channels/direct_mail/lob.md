---
nav_title: Lob
article_title: Lob
alias: /partners/lob/
description: "Este artículo de referencia describe la asociación entre Braze y Lob.com, que te permite enviar cartas, postales y cheques por correo directo."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com](https://lob.com) es un servicio en línea que te permite enviar correo directo a tus usuarios.

_Esta integración está mantenida por Lob._

## Sobre la integración {#about-the-integration}

Con esta integración, puedes:

- Enviar cartas, postales y cheques por correo utilizando webhooks de Braze y la API de Lob.
- Compartir eventos de Lob con Braze como atributos y eventos personalizados utilizando la Transformación de datos de Braze y los webhooks de Lob.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de Lob | Se necesita una cuenta de Lob para beneficiarse de esta asociación. |
| Clave de API de Lob | Tu clave de API de Lob se encuentra en la sección de configuración, debajo de tu nombre, en el dashboard de Lob. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Enviar correo utilizando webhooks de Braze {#sending-mail-using-braze-webhooks}

### Paso 1: Elige un punto de conexión de Lob {#step-1-choose-a-lob-endpoint}

Dependiendo de lo que quieras hacer en Lob, tendrás que utilizar el punto de conexión correspondiente en la solicitud HTTP de tu webhook. Para obtener información detallada sobre cada punto de conexión, consulta [la documentación de referencia de la API de Lob](https://lob.com/docs#intro).

| URL base | Puntos finales disponibles |
| ------------ | ------------------- |
| `https://api.lob.com/` | `/v1/addresses<br>/v1/addresses/{id}`<br>`/v1/verify`<br>`/v1/postcards`<br>`/v1/postcards/{id}`<br>`/v1/letter`<br>`/v1/letter/{id}`<br>`/v1/checks<br>/v1/checks/{id}`<br>`/v1/bank_accounts`<br>`/v1/bank_accounts/{id}`<br>`/v1/bank_accounts/{id}/verify`<br>`/v1/areas<br>/v1/areas/{id}`<br>`/v1/routes/{zip_code}`<br>`/v1/routes`<br>`/v1/countries<br>/v1/states`|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1: Elige un punto de conexión de Lob" }

### Paso 2: Crea tu plantilla de webhook de Braze {#step-2-create-your-braze-webhook-template}

Para crear una plantilla de webhook de Lob para utilizarla en futuras Campaigns o Canvas, ve a **Contenido** > **Webhook** en el panel de Braze. A continuación, selecciona **Crear plantilla de webhook**.

Si quieres hacer una Campaign de webhook de Lob única o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva Campaign.

En tu nueva plantilla de webhook, rellena los siguientes campos:

- **Webhook URL**: `<LOB_API_ENDPOINT>`
- **Request Body**: Raw Text

#### Encabezados de solicitud y método {#request-headers-and-method}

Lob requiere un encabezado HTTP para la autorización y un método HTTP. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Settings**, debes sustituir `<LOB_API_KEY>` por tu clave de API de Lob. Esta clave debe incluir un ":" justo después de la clave y estar codificada en base 64.

- **HTTP Method**: POST
- **Request Headers**:
  - **Authorization**: Basic `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Código del cuerpo de la solicitud y URL del webhook mostrados en la pestaña de redacción del creador de webhooks de Braze.]({% image_buster /assets/img_archive/lob_full_request.png %})

#### Cuerpo de la solicitud {#request-body}

A continuación se muestra un ejemplo de cuerpo de solicitud para el punto de conexión de postales de Lob. Aunque este cuerpo de solicitud se proporciona en la plantilla base de Lob en Braze, si deseas utilizar otros puntos de conexión, deberás ajustar tus campos Liquid en consecuencia.

{% raw %}
```json
{
  "description": "Demo Postcard",
  "to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
  },
  "front": "https://lob.com/postcardfront.pdf",
  "back": "https://lob.com/postcardback.pdf",
  "use_type": "marketing",
  "size": "6x11"
}
```
{% endraw %}

### Paso 3: Previsualiza tu solicitud {#step-3-preview-your-request}

En este punto, tu Campaign debería estar lista para probarla y enviarla. Comprueba el dashboard de Lob y los registros de mensajes de error de la consola para desarrolladores de Braze si te encuentras con errores. Por ejemplo, el siguiente error fue causado por un encabezado de autenticación formateado incorrectamente.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas de webhook actualizadas pueden encontrarse en la lista **Plantillas de Webhook guardadas** al crear una nueva [Campaign de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}

![Un registro de mensajes de error que muestra la hora, el nombre de la aplicación, el canal y el mensaje de error. El mensaje de error incluye la alerta del mensaje y el código de estado.]({% image_buster /assets/img_archive/error_log.png %})

## Compartir eventos mediante webhooks de Lob {#sharing-events-using-lob-webhooks}

[La Transformación de datos de Braze]({{site.baseurl}}/user_guide/data/unification/data_transformation/) te permite crear y administrar webhooks para automatizar el flujo de datos desde plataformas externas a Braze. A cada transformación se le asigna un punto de conexión único, que otras plataformas pueden utilizar como destino de su webhook.

{% alert important %}
La plantilla de Transformación de datos de Lob envía eventos utilizando tu [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), que registra puntos de datos. Te recomendamos que establezcas un límite de velocidad en la configuración de tu webhook de Lob para evitar el registro excesivo de datos.
{% endalert %}

### Paso 1: Crea una transformación en Braze {#step-1-create-a-transformation-in-braze}

1. En el panel de Braze, ve a **Configuración de datos** > **Transformaciones de datos** y, a continuación, selecciona **Crear transformación**.
2. Introduce un nombre corto y descriptivo para tu transformación.
3. En **Experiencia de edición**, selecciona **Utilizar una plantilla**, busca Lob y marca la casilla.
4. Cuando hayas terminado, selecciona **Crear transformación**. Se te redirigirá al editor de transformaciones, que utilizarás en el siguiente paso.

### Paso 2: Rellena la plantilla de Lob {#step-2-fill-out-the-lob-template}

Con esta plantilla, puedes transformar uno de tus eventos de Lob en un evento personalizado o atributo que pueda utilizarse en Braze. Sigue los comentarios en línea para terminar de construir la plantilla.

{% alert tip %}
Para obtener información detallada sobre la estructura de la carga útil de los webhooks de Lob, consulta [Lob: Uso de webhooks](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks).
{% endalert %}

```json
// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JavaScript dot notation, such as payload.x.y.z

// In this example, this function removes the periods and underscores of the event_type.id sent in the Lob payload so that an event id that is formatted like: `letter.processed_for_delivery` will log an event to Braze with the name `letter processed for delivery`.

function formatString(input) {
    return input.replace(/[._]/g, ' ');
}

let braze_event = formatString(payload.event_type.id);

// In this example, a metadata value passed in the Lob Webhook called 'external_ID' is being used to match the Event to the corresponding Braze user.

let brazecall = {
  "attributes": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "Most Recent Mailer": payload.body.description
    }
  ],
  "events": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "name": braze_event,
      "time": new Date().toISOString(),
// Customize the properties to the Lob event you are syncing. Our example below pulls in the Tracking Events array of objects associated with certain Lob events.
      "properties": {
        "tracking_events": payload.body.tracking_events
      }
    }
  ]
};
// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

### Paso 3: Crea un webhook en Lob {#step-3-create-a-webhook-in-lob}

1. Cuando hayas terminado de crear tu plantilla, selecciona **Activar** y, a continuación, copia la **URL del webhook** en el portapapeles.
2. En Lob, [crea un nuevo webhook](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks#receiving-a-webhook-1) y, a continuación, utiliza la URL de tu webhook de Braze para recibir el webhook.