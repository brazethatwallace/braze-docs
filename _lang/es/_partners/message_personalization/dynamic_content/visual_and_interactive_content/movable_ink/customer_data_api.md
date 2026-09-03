---
nav_title: Conexión a la API de datos de clientes
article_title: Conéctate a la API de datos de clientes de Movable Ink
description: "Este artículo de referencia describe cómo conectarse para activar los datos de eventos de clientes almacenados en Braze para generar contenido personalizado en Movable Ink mediante la API de datos de clientes."
page_type: partner
search_tag: Partner
---

# Conéctate a la API de datos de clientes de Movable Ink {#connect-to-the-movable-ink-customer-data-api}

> La integración de la API de datos de clientes de Braze y Movable Ink permite a los especialistas en marketing activar los datos de eventos de clientes almacenados en Braze para generar contenido personalizado dentro de Movable Ink.

Movable Ink es capaz de ingerir eventos de comportamiento de Braze a través de su API de datos de clientes. Los eventos se almacenarán en los perfiles de usuario en función del identificador único de usuario (UUID) que se pase a Movable Ink.

Para obtener más información sobre Stories, la API de datos de clientes de Movable Ink y cómo Movable Ink aprovecha los datos de comportamiento, visita los siguientes artículos del centro de soporte:

- [Potenciar los contenidos con datos de comportamiento](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Introducción y guía de la API de datos de clientes](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [Preguntas frecuentes: API de datos de clientes](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Movable Ink | Se necesita una cuenta de Movable Ink para beneficiarse de esta asociación. |
| Credenciales de la API de Movable Ink | El equipo de soluciones de Movable Ink generará las credenciales de la API por ti. Las credenciales de la API consisten en:{::nomarkdown}<ul><li>Una URL de endpoint (a la que se enviarán los datos)</li><li>Nombre de usuario y contraseña (utilizados para autenticar la API)</li></ul>{:/} Si lo deseas, Movable Ink puede proporcionar el nombre de usuario y la contraseña como un valor codificado en base64 para ser utilizado como un valor de encabezado de autorización básica. |
| Cargas útiles de eventos de comportamiento | Deberás compartir las cargas útiles de tus eventos con tu equipo de Movable Ink Client Experience. Consulta [Compartir cargas útiles de eventos](#event-payloads) con Movable Ink para obtener más detalles. |
| Activos creativos y lógica empresarial | Deberás compartir activos creativos con Movable Ink, incluidos archivos de Adobe Photoshop (PSD) que indiquen a Movable Ink cómo construir el bloque y una imagen alternativa. También deberás proporcionar la lógica de negocio para saber cómo y cuándo mostrar el bloque de contenido activado por el partner. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crea una campaña webhook en Braze {#step-1-create-a-webhook-campaign-in-braze}

#### Paso 1a: Crea una nueva campaña {#step-1a-create-a-new-campaign}

1. En Braze, [crea una campaña webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).
2. Dale a tu campaña un nombre y una descripción opcional.
3. Selecciona **Blank Template** como plantilla.

#### Paso 1b: Añade tus credenciales de la API de datos de clientes {#step-1b-add-your-customer-data-api-credentials}

1. En el campo **Webhook URL**, introduce la URL del endpoint de Movable Ink.

![Pestaña Redactar del creador de webhooks en Braze con la URL del endpoint de Movable Ink y el cuerpo de la solicitud configurados como pares clave/valor JSON.]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2. Selecciona la pestaña **Settings**.
3. Añade los siguientes encabezados de solicitud como pares clave-valor:

| Clave | Valor |
| --- | --- |
| Content-Type | application/json |
| Authorization | Introduce la autenticación básica que recibiste de Movable Ink. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 1b: Añade tus credenciales de la API de datos de clientes" }

![Pestaña de configuración del creador de webhooks en Braze con pares clave-valor para Content-Type y Authorization.]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### Paso 1c: Configura tu carga útil {#step-1c-configure-your-payload}

1. Vuelve a la pestaña **Compose**.
2. Para tu **Request Body**, crea tu propio cuerpo de solicitud con pares clave-valor JSON o introduce la carga útil de tu evento como texto sin formato. Consulta las [cargas útiles de ejemplo](#sample-payloads) para ver ejemplos de eventos estándar de comercio electrónico.

![Pestaña Redactar del creador de webhooks en Braze con pares clave-valor JSON para ID, marca de tiempo, ID de usuario y tipo de evento.]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### Paso 1d: Prueba tu webhook {#step-1d}

Deberás compartir una carga útil de ejemplo con tu equipo de Movable Ink Client Experience. Puedes generar esta carga útil en la pestaña **Test** basándote en la carga útil que has construido.

{% alert important %}
Movable Ink recomienda esperar para probar tu webhook en Braze hasta que tu equipo de Movable Ink Client Experience haya confirmado que ha completado el mapeado y está listo para recibir una prueba. Si este mapeado no está completo, es probable que recibas un error al realizar la prueba.
{% endalert %}

Para probar tu webhook, haz lo siguiente:

1. Selecciona la pestaña **Test**.
2. Previsualiza el mensaje como un usuario para ver una carga útil de evento de ejemplo para ese usuario. Puedes elegir entre previsualizar como usuario aleatorio, usuario específico o usuario personalizado.
3. Si todo parece correcto, haz clic en **Send test** para enviar una solicitud de prueba.

![Mensaje de respuesta de webhook en Braze que muestra una respuesta 200 OK.]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### Paso 2: Finaliza la configuración de tu campaña {#step-2-finalize-your-campaign-setup}

#### Paso 2a: Programa tu campaña {#step-2a-schedule-your-campaign}

Cuando hayas terminado de redactar y probar el webhook, [programa tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Braze admite entregas programadas, basadas en acciones y activadas por API. La [entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) suele ser la más adecuada para la mayoría de los casos de uso de eventos de comportamiento. Si tienes preguntas sobre lo que tiene sentido para tu caso de uso, ponte en contacto con tus administradores de éxito de cliente de Braze y Movable Ink.

Para la entrega basada en acciones:

1. Especifica la acción desencadenante. Este es el evento que activará el webhook a Movable Ink.
2. Asegúrate de que **Schedule Delay** esté configurado en **Immediately**. Los datos de los eventos deben enviarse a Movable Ink inmediatamente después de que se produzca el evento, sin demora.
3. Establece la duración de la campaña especificando una hora de inicio. Es probable que no se aplique una hora de finalización, aunque puede establecerse si es necesario para el caso de uso.

{% alert note %}
Para asegurarte de que los datos se transmiten a Movable Ink en tiempo real, no selecciones **Send campaign to users in their local time zone**.
{% endalert %}

#### Paso 2b: Especifica tu audiencia {#step-2b-specify-your-audience}

A continuación, determina a qué usuarios quieres dirigir esta campaña. Para más detalles, consulta [Dirigirse a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users).

Asegúrate de no utilizar pruebas A/B en tu campaña desmarcando la casilla **Control Group**. Si se incluye un grupo de control, a un porcentaje de usuarios no se les enviarán datos a Movable Ink. Toda tu audiencia debe dirigirse a la variante y no al grupo de control.

![Panel de pruebas A/B en una campaña de Braze con una distribución de variantes del 100 % asignada a la variante 1, y sin grupo de control.]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### Paso 2c: Elige eventos de conversión (opcional) {#step-2c-choose-conversion-events-optional}

Si lo deseas, puedes asignar eventos de conversión a esta campaña dentro de Braze.

Sin embargo, dado que el webhook solo pretende transmitir datos, es probable que la atribución a este nivel sea menos útil que la atribución a nivel de campaña después de que los datos de comportamiento de Braze se utilicen para personalizar el contenido.

### Paso 3: Lanza la campaña {#step-3-launch-the-campaign}

Revisa la configuración de tu webhook y lanza tu campaña.

## Consideraciones {#considerations}

### Alineación con un identificador único de usuario {#aligning-on-a-unique-user-identifier}

Asegúrate de que el valor del identificador único de usuario (UUID) que estás utilizando como tu `mi_u` esté disponible dentro de Braze y se pueda incluir en las cargas útiles de eventos enviados a Movable Ink.

Esto garantiza que los eventos de comportamiento a los que Movable Ink hace referencia al generar una imagen estén asociados al mismo cliente para el que recibieron los eventos de comportamiento. Si el valor UUID no es el mismo que el `external_id` de Braze, el UUID debe capturarse y pasarse a Braze como atributo o en las propiedades del evento de un evento de Braze para aprovechar este identificador.

Braze rastrea el comportamiento de los usuarios en múltiples plataformas (como la web y la aplicación móvil), por lo que un mismo usuario puede tener varios identificadores anónimos distintos. Estos identificadores pueden fusionarse en el perfil de usuario único conocido de Stories cuando se envía un evento `identify` a Movable Ink, siempre y cuando el evento `identify` incluya tanto un identificador anónimo como el identificador único conocido.

Una vez que Movable Ink recibe un `user_id` para un único usuario, todos los eventos futuros para ese usuario deben incluir ese mismo `user_id`.

### Compartir cargas útiles de eventos con Movable Ink {#event-payloads}

Antes de configurar el conector a la API de datos de clientes de Movable Ink, asegúrate de compartir tus cargas útiles de eventos con tu equipo de Movable Ink Client Experience. Esto permite a Movable Ink mapear tus eventos a su esquema de eventos y evitará cualquier llamada a la API rechazada o fallida.

Puedes generar una carga útil de evento dentro de Braze utilizando cualquier propiedad del evento. Genera una carga útil de ejemplo para un usuario aleatorio o buscando un ID de usuario específico. Consulta el [paso 1d](#step-1d) para obtener más detalles.

Comparte esta carga útil de ejemplo con tu equipo de Movable Ink Client Experience. Asegúrate de que no haya información sensible de identificación personal en la carga útil de ejemplo (como dirección de correo electrónico, número de teléfono o fechas de nacimiento completas).

Para obtener más información sobre las propiedades de eventos personalizados y el formato esperado de los datos contenidos en las propiedades, consulta [Propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

### Usuarios conocidos frente a anónimos {#known-versus-anonymous-users}

En Braze, los eventos pueden registrarse bajo un perfil de usuario anónimo. Los identificadores que se vinculan al perfil de usuario durante el registro de eventos dependen de cómo se creó el usuario (a través del SDK de Braze o API) y de su etapa actual en el ciclo de vida del usuario.

#### Solo reenvío de eventos de Braze para usuarios conocidos {#only-forwarding-braze-events-for-known-users}

En tu campaña webhook, utiliza el filtro `External User ID` para dirigirte únicamente a los usuarios que tengan un `external_id` con el filtro `External User ID` `is not blank`.

#### Reenvío de eventos de Braze para usuarios anónimos y conocidos {#forwarding-braze-events-for-anonymous-and-known-users}

Si quieres reenviar eventos de Braze de usuarios anónimos (usuarios antes de que se asigne un `external_id` a su perfil), deberás decidir qué identificador utilizar como `anonymous_id` para Movable Ink hasta que esté disponible un `external_id`. Elige un `anonymous_id` que permanezca constante en tu perfil de usuario de Braze. Puedes utilizar la lógica Liquid en el cuerpo del webhook para decidir si pasar un `anonymous_id` o un `user_id`.

Para más información, consulta los webhooks de ejemplo en [cargas útiles de ejemplo](#sample-payloads).

## Cargas útiles de ejemplo {#example-payloads}

### Evento de vista del producto {#product-view-event}

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@example.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

En este ejemplo, se utiliza una dirección de correo electrónico con hash como `anonymous_id` para los usuarios que no disponen de `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### Evento de vista de categoría {#category-view-event}

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Example webhook %}

Este ejemplo muestra un webhook que rastrea eventos solo para usuarios conocidos (usuarios con un `external_id`).

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### Evento de identificación {#identify-event}

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

En este ejemplo, se utiliza una dirección de correo electrónico con hash como `anonymous_id` para los usuarios que no disponen de `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}