---
nav_title: SessionM
article_title: SessionM
description: "Este artículo de referencia describe la asociación entre Braze y SessionM, una plataforma de interacción con los clientes y fidelización."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
---

# Plataforma de fidelización SessionM {#sessionm-loyalty-platform}

> [SessionM](https://sessionm.com/) es una plataforma de interacción con los clientes y fidelización, parte de Capillary Technologies, que proporciona características de gestión de campañas y soluciones de gestión de la fidelización para ayudar a los especialistas en marketing a impulsar el alcance específico y aumentar la interacción y la ganancia.

## Requisitos previos {#prerequisites}

| Fuente | Requisito | Descripción |
| --- | --- | --- |
| Braze | Una clave de API REST de Braze | Una clave de API REST de Braze con permisos `trigger_send`. Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Braze | Un punto de conexión REST de Braze | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la URL de Braze para [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
| Braze y SessionM | Identificador coincidente | Para utilizar la integración, asegúrate de que tanto SessionM como Braze tienen un registro de los identificadores utilizados por cada plataforma. Las referencias a `user_id` corresponden al identificador de usuario de SessionM generado en el momento de la creación del perfil en SessionM. |
| SessionM | Una cuenta de SessionM | Se necesita una cuenta de SessionM para beneficiarse de esta asociación. |
| SessionM | Un punto de conexión REST de SessionM Core | Tu punto de conexión dependerá de la URL de SessionM de tu instancia. Se puede crear en el panel de SessionM desde **Digital Properties**. |
| SessionM | Una clave de API REST de SessionM Core | La clave de API de SessionM asociada a tu instancia y a la integración con Braze. Esta clave puede utilizarse para todas las llamadas basadas en el núcleo, incluidas las etiquetas. Se puede crear en el panel de SessionM desde **Digital Properties**. |
| SessionM | Un secreto de API REST de SessionM Core | El secreto de API de SessionM asociado a tu instancia y a la integración con Braze. Esta clave puede utilizarse para todas las llamadas basadas en el núcleo, incluidas las etiquetas. Se puede crear en el panel de SessionM desde **Digital Properties**. |
| SessionM | Un punto de conexión REST de SessionM Connect | Tu punto de conexión dependerá de la URL de SessionM de tu instancia. Ponte en contacto con tu director de cuentas técnicas de SessionM o con el equipo de entrega para que te lo proporcionen. |
| SessionM | Una cadena de autorización REST de SessionM Connect | La cadena de autorización básica de SessionM Connect asociada a tu instancia. Esta cadena de autenticación se puede utilizar para todas las llamadas basadas en conexión, incluido get_user_offers. Ponte en contacto con tu director de cuentas técnicas de SessionM o con el equipo de entrega para que te la proporcionen. |
| SessionM | Un ID de minorista REST de SessionM Connect | Un GUID de identificación único para el cliente específico asociado a tu instancia. Ponte en contacto con tu director de cuentas técnicas de SessionM o con el equipo de entrega para que te lo proporcionen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prerequisites" }

## Casos de uso {#use-cases}

Los siguientes casos de uso muestran algunas formas de aprovechar la integración de SessionM y Braze.

- Crea una segmentación que incorpore datos de todas las plataformas de fidelización, gestión de clientes y mensajería.
- Utiliza una segmentación sólida para dirigirte a grupos específicos de usuarios con ofertas y promociones.
- Aprovecha la información más actualizada sobre usuarios, ofertas y fidelización al enviar mensajes.
- Proporciona notificaciones detalladas a los clientes sobre el progreso y la finalización de las actividades promocionales y de fidelización.
- Notifica a los clientes cuando se conceda una nueva oferta y proporciona los detalles de la misma.

## Integración de SessionM con Braze {#integrating-sessionm-with-braze}

### Paso 1: Crear un segmento en Braze {#step-1-create-a-segment-in-braze}

En Braze, crea un segmento de usuarios al que dirigirte con promociones y ofertas de SessionM.

![Creador de segmentos con el filtro "Atributos personalizados" seleccionado.]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### Paso 2: Importar segmentos de Braze a SessionM {#step-2-import-braze-segments-into-sessionm}

#### Opción 1: Exportar al punto de conexión de etiquetas de SessionM (recomendado) {#option-1-export-to-the-sessionm-tag-endpoint-recommended}

Primero, crea una campaña webhook en Braze y configura la URL del webhook como {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}. Utiliza Liquid para definir el `user_id` dentro de la URL.

Utilizando un **cuerpo de solicitud** de texto sin formato, compón el cuerpo del webhook para incluir las etiquetas deseadas que se añadirán al perfil de usuario en SessionM y el tiempo de vida deseado. Un ejemplo:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

En la pestaña **Configuración**, añade los pares clave-valor para cada campo del encabezado de solicitud:
    - Crea una clave `Content-Type` con su valor correspondiente `application/json`
    - Crea una clave `Authorization` con un valor correspondiente `Basic YOUR-ENCODED-STRING-KEY`. Ponte en contacto con tu equipo de SessionM para obtener la clave de cadena codificada para tu punto de conexión.

![Configuración del webhook.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

Programa tu entrega, configura tu **Target Audiences** para que se dirija al segmento [que creaste anteriormente](#step-1-create-a-segment-in-braze) y, a continuación, lanza tu campaña.

{% alert important %}
Este proceso también puede realizarse a través de un cliente API, como Postman, haciendo una solicitud directamente al [punto de conexión de etiquetas de SessionM](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag) especificando el cliente, el nombre de la etiqueta y un tiempo de vida para cada usuario en la llamada (un único usuario por llamada).
<br><br>
El siguiente ejemplo de solicitud utiliza cURL.

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### Opción 2: Importación CSV {#option-2-csv-import}

Exporta tu segmento de Braze utilizando el segmentador de Braze y proporciona un archivo CSV a SessionM que contenga los clientes a etiquetar, el nombre de la etiqueta y un tiempo de vida para cada usuario del archivo.

## Recuperar la cartera de ofertas en tiempo real con Braze {#retrieving-real-time-offer-wallet-with-braze}

La integración de SessionM con Braze permite extraer en tiempo real los datos de usuario de SessionM en el momento del envío del mensaje, mediante contenido conectado, para eliminar el riesgo de comunicar a los clientes ofertas de fidelización caducadas, vencidas o ya canjeadas.

El siguiente ejemplo muestra cómo se utiliza el contenido conectado para crear una plantilla de datos de cartera de ofertas en un mensaje. Sin embargo, el contenido conectado puede utilizarse con cualquiera de los puntos de conexión de SessionM Connect.

### Paso 1: Emitir oferta en SessionM {#step-1-issue-offer-in-sessionm}

SessionM emite ofertas a los clientes a partir de varias palancas internas diferentes que pueden configurarse. Una vez emitidas, las ofertas pasan a un estado que SessionM denomina "cartera de ofertas".

Un cliente debe completar la acción requerida o cumplir el objetivo y se le emite la oferta dentro de SessionM.

A continuación, SessionM añade la oferta a la cartera del cliente en el estado emitido.

### Paso 2: Llamar a la API de cartera de ofertas de SessionM {#step-2-call-sessionm-offer-wallet-api}

En el paso en Canvas o Campaign con las ofertas de SessionM, utiliza [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/) para hacer una llamada a la API al [punto de conexión de SessionM `get_user_offers`](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/).

En la solicitud de contenido conectado, especifica el `user_id` de SessionM del usuario y tu `retailer_id` para recuperar la lista completa de ofertas activas que el cliente tiene en su cartera. Cada solicitud a este punto de conexión puede incluir un único usuario. Ponte en contacto con el equipo de SessionM para obtener la clave de cadena codificada para el encabezado de autorización básica en tu llamada de contenido conectado.

En el cuerpo de la solicitud, `culture` está predeterminado a `en-US`, pero puedes utilizar Liquid para crear una plantilla con el idioma del usuario para las ofertas multilingües de SessionM (por ejemplo, utilizando {% raw %}`"culture":"{{${language}}}"`{% endraw %}).

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### Paso 3: Rellenar la cartera de ofertas en la mensajería de Braze {#step-3-populate-offer-wallet-to-braze-messaging}

Tras realizar una solicitud al punto de conexión, SessionM devuelve la lista completa de ofertas en el estado emitido, junto con los detalles completos de cada oferta. Este es un ejemplo de respuesta devuelta:

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

Utilizando la notación de puntos de Liquid, esto se puede introducir en el mensaje. Por ejemplo, para personalizar el mensaje con el resultado `offer_id`, podrías aprovechar la carga útil de retorno utilizando {% raw %}`{{wallet.payload.available_points}}`{% endraw %}, que devuelve `100`.

{% alert note %}
Se trata de una API individual. Si tienes intención de enviar un lote de más de 500 usuarios, ponte en contacto con tu equipo de cuenta de SessionM para informarte sobre cómo incorporar datos masivos en la integración.
{% endalert %}

## Configuración de la mensajería desencadenada {#setting-up-triggered-messaging}

La integración entre SessionM y Braze permite que los datos de perfil de usuario, los detalles de la oferta y los saldos de puntos se rellenen dinámicamente en los mensajes y se envíen en tiempo real al cliente en el punto de acción.

### Paso 1: El equipo de entrega de SessionM configura las plantillas {#step-1-sessionm-delivery-team-configures-templates}

Colabora con tu equipo de entrega de SessionM para desarrollar plantillas que puedas utilizar en tu mensajería desencadenada. SessionM insertará datos de perfil de usuario, detalles de la oferta y saldos de puntos en la mensajería y los desencadenará en Braze para la mensajería de clientes en tiempo real.

Los campos estándar presentes en todas las plantillas de SessionM incluyen:
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
Al configurar `broadcast flag` en `true`, el mensaje se enviará a todo el segmento al que se dirija la Campaign o Canvas en Braze.
{% endalert %}

Se pueden configurar campos adicionales en función de necesidades específicas:

- **Datos de oferta:** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **Datos de concesión de puntos:** `point award amount`, `point account name`
- **Datos del evento desencadenante:** Cualquier dato del evento desencadenante que utilice el resultado del webhook de desencadenar/enviar
- **Datos específicos de la campaña:** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

Los campos adicionales se envían a Braze como `trigger_properties` para personalizar el mensaje.

### Paso 2: Crea una Campaign o Canvas en Braze {#step-2-create-a-braze-campaign-or-canvas}

Crea una Campaign activada por API o un Canvas en Braze para que lo desencadene SessionM. Si se han configurado campos adicionales, como `offer_id` u `offer title`, utiliza Liquid (como {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}) para añadir los campos personalizados a tu mensajería.

![Propiedades de desencadenamiento de API.]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

En la pestaña **Schedule Delivery**, anota el ID de la Campaign o del Canvas, ya que se añadirá a la **Configuración avanzada** de la campaña de SessionM.

![Campaign desencadenada por API.]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

Finaliza los detalles de tu Campaign o Canvas y selecciona **Launch**.

### Paso 3: Crea una campaña promocional o de mensajería de SessionM {#step-3-create-a-sessionm-promotional-or-messaging-campaign}

A continuación, crea tu campaña en SessionM.

![Creación de campaña en SessionM.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

Actualiza la configuración avanzada de la campaña de SessionM para incluir la siguiente carga útil JSON que contiene el `braze_campaign_id` o `braze_canvas_id`.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![Configuración avanzada de SessionM.]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

Crea un desencadenador de mensajes en el horario o comportamiento deseado. A continuación, selecciona **Braze Messaging Variant** como **Messaging Variant** en el menú **External Message** para utilizar la plantilla.

![Mensaje externo de SessionM.]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

Esta plantilla extrae los atributos estáticos y dinámicos relevantes y llama al punto de conexión de Braze.

![Plantilla de Braze en SessionM.]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}