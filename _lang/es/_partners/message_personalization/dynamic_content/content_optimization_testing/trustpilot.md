---
nav_title: Trustpilot
article_title: Trustpilot
description: "Esta página explica cómo integrar Trustpilot con Braze, enviar invitaciones de reseña y personalizar mensajes con información sobre las reseñas de productos."
alias: /partners/trustpilot/
page_type: partner
search_tag: Partner
---

# Trustpilot

> [Trustpilot](https://www.trustpilot.com/) es una plataforma de reseñas en línea que permite a los clientes compartir opiniones y te permite administrar y responder a las reseñas.

Esta página proporciona una guía paso a paso para:

* Crear invitaciones de reseña utilizando la API de creación de invitaciones de Trustpilot
* Personalizar mensajes con reseñas de productos a través de la API de reseñas de productos de Trustpilot

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

| Requisitos | Descripción |
| --- | --- |
| Una cuenta de Trustpilot | Necesitas una cuenta de Trustpilot con acceso a la API de Trustpilot. |
| Una clave de autenticación de Trustpilot | Tendrás que configurar una clave de API y solicitar un token de acceso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Obtén tus credenciales de API de Trustpilot {#step-1-get-your-trustpilot-api-credentials}

1. [Inicia sesión en Trustpilot](https://app.contentful.com/login) con tus credenciales.
2. Crea o recupera la clave de API y el secreto en el dashboard de Trustpilot yendo a **Integrations** > **Developers** > **APIs**. Si aún no tienes una clave de API, crea una nueva:
   1. Ve a **Application Name** > **Create Application**
   2. Copia tu clave de API y tu secreto, que se utilizarán para autenticar tus solicitudes de contenido conectado.

## Enviar invitaciones de reseña de Trustpilot {#sending-trustpilot-review-invitations}

### Paso 1: Configura una campaña de webhook en Braze {#step-1-set-up-a-braze-webhook-campaign}

Configura una Campaign de webhook en Braze basada en acciones para desencadenar las API de Trustpilot y enviar invitaciones de reseña por correo electrónico a los usuarios. Por ejemplo, podrías enviar una invitación de reseña después de que un usuario realice un pedido con los siguientes detalles del webhook:
   * [URL del webhook](https://developers.trustpilot.com/invitation-api?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..#create-invitation(s)): `https://invitations-api.trustpilot.com/v1/private/business-units/{businessUnitId}/email-invitations`
   * Método: POST
   * Añade la información relevante del cliente como pares clave-valor

### Paso 2: Recupera el token de acceso {#step-2-retrieve-the-access-token}

1. Utiliza [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) para realizar una solicitud al [punto de conexión de autenticación de Trustpilot](https://documentation-apidocumentation.trustpilot.com/authentication?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..) para recuperar el token de acceso.
2. Utiliza el tipo de concesión **client_credentials** e introduce tu clave de API y tu secreto en una etiqueta de contenido conectado para recuperar un token. La solicitud de contenido conectado puede introducirse en el encabezado de solicitud. El contenido conectado puede tener este aspecto:

{% raw %}

```liquid
{% connected_content
https://api.trustpilot.com/v1/oauth/oauth-business-users-for-applications/accesstoken
:method post
:headers {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic {{'API_KEY:API_SECRET' | base64_encode}}" }
:body grant_type=client_credentials
:save token
:retry
:cache_max_age 3600 %}

{{token.access_token}}

```

{% endraw %}

{: start="3"}
3. Añade el token de acceso al encabezado de solicitud de tu Campaign de webhook.

{% alert tip %}
Consulta [la documentación de Trustpilot](https://support.trustpilot.com/hc/en-us/community/posts/11947443933074-Braze-Trustpilot-Setup-Instructions-for-triggering-API-invites) para obtener instrucciones más detalladas.
{% endalert %}

## Personalizar mensajes con información sobre reseñas de productos {#personalizing-messages-with-product-review-insights}

En tu Campaign de Braze, haz una llamada de contenido conectado para solicitar datos al [punto de conexión de resumen de reseñas de productos](https://developers.trustpilot.com/product-reviews-api#get-product-reviews-summary) de Trustpilot ({% raw %}`https://api.trustpilot.com/v1/product-reviews/business-units/{businessUnitId}`{% endraw %}). Este método recupera reseñas de productos para SKU específicos de la unidad de negocio. El siguiente ejemplo especifica el SKU concreto del producto y filtra las reseñas de cinco estrellas.

{% raw %}
```liquid
{% connected_content https://api.trustpilot.com/v1/product-reviews/business-units/66ea0530xxxxxx/reviews?sku={{event_properties.${item_sku}}}&stars=5
   :method get
   :headers {"apikey": "xxxxx"}
   :content_type application/json :save result %}
```
{% endraw %}

![Contenido conectado en un correo electrónico utilizando Liquid para extraer información.]({% image_buster /assets/img/trustpilot_connected_content_example.png %}){:style="max-width:38%;"}

La solicitud de contenido conectado devolverá las reseñas de los productos.

{% raw %}
```liquid
  {
   "productReviews": [
       {
           "id": "670d5810ba62e6b31de97de9",
           "createdAt": "2024-10-14T17:42:40.286Z",
           "stars": 5,
           "content": "Such a great toy truck, my kids really enjoy it! ",
           "consumer": {
               "id": "6176xxxx",
               "displayName": "Kevin Bob"
           },
           "language": "en",
           "attributeRatings": [],
           "attachments": [],
           "firstCompanyComment": null
       }
   ],
   "links": []
 ```
{% endraw %}

{: start="2"}
2. Utiliza la sintaxis Liquid para introducir el contenido relevante en tu mensaje. Por ejemplo, para extraer el contenido de la reseña del producto, utiliza la etiqueta de Liquid {% raw %}`{{result.productReviews[0].content}}`{% endraw %}.

![Correo electrónico personalizado con una reseña de un camión de juguete que el usuario dejó en su carrito.]({% image_buster /assets/img/trustpilot_personalized_email.png %}){:style="max-width:38%;"}