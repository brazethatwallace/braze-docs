---
nav_title: Rokt Calendar
article_title: Rokt Calendar
description: "Este artículo de referencia describe la asociación entre Braze y Rokt Calendar, una tecnología de marketing de calendario dinámico que permite a las marcas impulsar eventos 1:1 y comunicaciones promocionales, en forma de eventos de calendario y notificaciones."
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Rokt Calendar

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/) es una tecnología de marketing de calendario dinámico que permite a las marcas impulsar eventos 1:1 y comunicaciones promocionales en forma de eventos de calendario y notificaciones.

_Esta integración la mantiene Rokt Calendar._

## Sobre la integración {#about-the-integration}

La integración de Braze y Rokt Calendar permite que tus suscriptores de Rokt Calendar y sus datos se envíen a Braze a través de un webhook de Braze. Después puedes usar estos datos en Canvas de Braze para la segmentación de recorridos y la segmentación de audiencia utilizando cualquiera de los siguientes [atributos de Rokt Calendar](#audience-segmentation) personalizados.

## Requisitos previos {#prerequisites}

| Requisito  | Descripción |
| ------------ | ----------- |
| Cuenta de Rokt Calendar | Se necesita una cuenta de Rokt Calendar específica para cada cliente para aprovechar esta asociación. Ponte en contacto con [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) para hablar con un director de cuentas  |
| Configuración de Rokt Calendar | Tu director de cuentas de Rokt Calendar trabajará contigo para configurar el calendario de la forma que mejor se adapte a tus necesidades, incluyendo ajustes como:<br>- Indicador de fusión<br>- Indicador de respaldo de SubscriberID<br>- Captura de correo electrónico, si es necesario |
| Credenciales OAuth de Rokt Calendar | Esta clave proporcionada por tu director de cuentas de Rokt Calendar te permitirá conectar tus cuentas de Braze y Rokt Calendar.<br><br>Se puede crear en el dashboard de Braze en **Settings** > **Connected Content**. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. Deberás proporcionar esta clave a tu director de cuentas de Rokt Calendar.<br><br> Se puede crear en el dashboard de Braze desde **Settings** > **API Keys**. |
| [Punto de conexión REST de Braze]({{site.baseurl}}/api/basics/#endpoints) | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la URL de Braze para tu instancia. |
| ID de suscriptor externo | Es el identificador utilizado por el proceso de suscripción de Rokt Calendar para emparejar al suscriptor del calendario con el usuario de Braze. Esto es algo que tú pasas a Rokt Calendar.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Segmentación de la audiencia {#audience-segmentation}

Cuando Rokt Calendar crea un nuevo usuario o hace coincidir un suscriptor existente con un usuario de Braze, Rokt Calendar enviará los siguientes atributos de suscripción personalizados que puedes filtrar dentro de Braze:

| Atributo personalizado  | Definición       | Ejemplo          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Código de la cuenta de Rokt Calendar | `brazetest/f5733866ade2` y `brazetest/ff10919f1078` |
| `rokt:account_id` | ID de la cuenta de Rokt Calendar | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Nombre de la cuenta de Rokt Calendar | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Código del calendario de Rokt Calendar | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | ID del calendario de Rokt Calendar | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Título del calendario de Rokt Calendar | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | Código de país relacionado con la suscripción creada | `AU/f5733866ade2` |
| `rokt:device_name` | Tipo de dispositivo relacionado con la suscripción creada | `Desktop/f5733866ade2` |
| `rokt:geo_country` | País de origen relacionado con la suscripción creada | `Australia/f5733866ade2` |
| `rokt:optIn1` | Si el usuario ha optado por la primera de las 2 adhesiones voluntarias relacionadas con la suscripción creada | `True/f5733866ade2` |
| `rokt:optIn2` | Si el usuario ha optado por la segunda de las 2 adhesiones voluntarias relacionadas con la suscripción creada | `True/f5733866ade2` |
| `rokt:source` | La fuente de la suscripción creada | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | La dirección de correo electrónico introducida por el usuario durante el proceso de suscripción | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | El ID de suscripción, que sirve como identificador único, relacionado con la suscripción creada | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | Método de suscripción (webcal/Google) relacionado con la suscripción creada. | `WebCal/f5733866ade2` |
| `rokt:tags` | Etiquetas de calendario utilizadas relacionadas con la suscripción creada. | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Audience segmentation #audience-segmentation" }

Rokt Calendar también activará un evento personalizado `subscribe` tan pronto como el usuario se haya suscrito a tu calendario de Rokt, que se puede utilizar en la segmentación de Braze o como desencadenante de una campaña o un componente de Canvas.

## Integración {#integration}

### Paso 1: Crear una audiencia de suscriptores del calendario {#step-1-building-an-audience-of-calendar-subscribers}

Para enviar eventos de calendario desde Canvas, primero debes tener configurado un calendario de Rokt con usuarios ya suscritos. Para ello, deberás informar a tus usuarios de dónde y cómo suscribirse al calendario. Rokt Calendar te recomienda que:

#### Proporcionar puntos de integración de suscripciones {#provide-subscription-integration-points}
Para crear una audiencia de suscriptores del calendario, tendrás que ofrecer un destino al que el usuario pueda navegar y suscribirse. Algunos ejemplos de puntos de integración de suscripciones incluyen:
  - Añadir un botón de calendario a tu sitio web
  - Añadir un enlace de calendario en un correo electrónico o SMS
  - Añadir un botón de calendario a tu aplicación
  - Añadir un enlace al calendario en las redes sociales

#### Promocionar el calendario {#promote-the-calendar}
Para crear una audiencia de suscriptores, tendrás que promocionar el calendario entre tu audiencia para que sepan cómo suscribirse. Algunos ejemplos de promoción del calendario incluyen:
  - Publicaciones en redes sociales
  - Boletines y actualizaciones por correo electrónico
  - Entradas de blog
  - Notificaciones dentro de la aplicación

### Paso 2: Crear un webhook de Rokt Calendar en Braze {#step-2-create-a-rokt-calendar-webhook-in-braze}

En Braze, puedes configurar una campaña de webhook o un webhook dentro de un Canvas para:

- Enviar un nuevo evento personalizado: permite añadir nuevos eventos a los calendarios de un segmento de suscriptores.
- Actualizar un evento personalizado: permite actualizar un evento existente en los calendarios de los suscriptores.

Para crear una plantilla de webhook de Rokt Calendar para usar en futuras campañas o Canvas, navega a **Templates** > **Webhook Templates** en la plataforma Braze.

Si deseas crear una campaña de webhook de Rokt Calendar única o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva campaña.

{% tabs %}
{% tab Send a new event %}
Una vez que hayas seleccionado la plantilla de webhook de Rokt Calendar, deberías ver lo siguiente:
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Request Body**: Raw Text
{% endtab %}
{% tab Update an existing event %}
Una vez que hayas seleccionado la plantilla de webhook de Rokt Calendar, deberías ver lo siguiente:
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Request Body**: Raw Text
{% endtab %}
{% endtabs %}

#### Encabezados de solicitud y método {#request-headers-and-method}

Rokt Calendar requiere un `HTTP Header` para la autorización que incluya el nombre de tu credencial de contenido conectado de Rokt Calendar. Lo siguiente ya estará incluido dentro de la plantilla como pares clave-valor, pero en la pestaña **Settings**, debes sustituir `<Rokt-Calendar-API>` por el nombre de la credencial que se encuentra en `Manage Settings > Connected Content > Credential`.

{% raw %}
- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Bearer `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud {#request-body}

{% tabs local %}
{% tab Send a new event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab Update an existing event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab Event details %}
Los siguientes campos incluyen información que puede personalizarse a nivel de evento.

| Campo             | Definición       | Ejemplo          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>***Obligatorio** | Un identificador único para el evento que se va a añadir o actualizar | `Event_00001`
| `eventTitle` <br>***Obligatorio** | El título del evento tal y como aparecería en el calendario | Rebajas de verano 2019
| `eventDescr` | La descripción del evento tal y como aparecería en el calendario | La venta dura tres días; haz clic en este enlace `www.mybusiness.com/sale` para ver las ofertas. |
| `eventLocation` | La ubicación del evento tal y como aparecería en el calendario; ten en cuenta que esto se utiliza a menudo como una segunda llamada a la acción, complementaria al eventTitle. | Abre el evento para obtener un 50 % de descuento |
| `eventStart` <br>***Obligatorio**  | La fecha y hora de inicio del evento tal y como aparecerían en el calendario | `2019-02-21T15:00:00` |
| `eventEnd` <br>***Obligatorio**  | La fecha y hora de finalización del evento tal y como aparecerían en el calendario | `2019-02-21T16:00:00` |
| `eventTz` <br>***Obligatorio**  | La zona horaria del evento tal y como aparecería en el calendario; ten en cuenta que la lista de zonas horarias aplicables se puede encontrar [aquí](https://roktcalendar-api.readme.io/docs/timezones). | `Eastern Standard Time` |
| `notifyBefore` <br>***Obligatorio**  | El tiempo de recordatorio del evento tal y como aparecería en el calendario; ten en cuenta que se expresa en minutos | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Request body" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Para obtener una lista de zonas horarias válidas, consulta [https://roktcalendar-api.readme.io/reference/timezones](https://roktcalendar-api.readme.io/reference/timezones).
{% endalert %}

### Paso 3: Previsualizar tu solicitud {#step-3-preview-your-request}

Previsualiza tu solicitud en el panel de **vista previa** o navega a la pestaña **Test**, donde puedes seleccionar un usuario al azar, un usuario existente o personalizar el tuyo propio para probar tu webhook.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas de webhook actualizadas se pueden encontrar en la lista **Saved Webhook Templates** al crear una nueva [campaña de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}