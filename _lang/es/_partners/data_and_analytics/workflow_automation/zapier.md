---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "Este artículo de referencia describe la asociación entre Braze y Zapier, una herramienta web de automatización que permite compartir datos entre aplicaciones web y utilizar esa información para automatizar acciones."
page_type: partner
search_tag: Partner

---
# Integración con Zapier {#zapier-integration}

> [Zapier](https://zapier.com/) es una herramienta web de automatización que permite compartir datos entre aplicaciones web y luego utilizar esa información para automatizar acciones.

La asociación entre Braze y Zapier aprovecha la API de Braze y los [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook) de Braze para conectarse con aplicaciones de terceros, como Google Workplace, Slack, Salesforce, WordPress, etc., y automatizar diversas acciones.

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
|---|---|
| Cuenta Zapier | Se requiere una cuenta Zapier para aprovechar esta asociación. |
| Punto de conexión REST de Braze | La URL de tu punto de conexión REST. Tu punto de conexión dependerá de la [URL de Braze para tu instancia]({{site.baseurl}}/api/basics/#api-definitions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

En el siguiente ejemplo de Zapier, enviaremos información de WordPress a Braze mediante un webhook POST. Esta información puede utilizarse para crear un Canvas de Braze.

### Paso 1: Crear un desencadenante en Zapier {#step-1-create-a-zapier-trigger}

Utilizando la terminología de Zapier, un "zap" es un flujo de trabajo automatizado que conecta tus aplicaciones y servicios. La primera parte de cualquier zap es designar un desencadenante. Una vez habilitado tu zap, Zapier realizará automáticamente las acciones respectivas siempre que se detecte tu desencadenante.

Usando nuestro ejemplo de WordPress, en la plataforma Zapier, configuraremos nuestro zap para que se active cuando se añada una nueva publicación de WordPress y seleccionaremos **Published** y **Posts** como **Post Status** y **Post Type**.

![En la plataforma Zapier, dentro de un zap, selecciona que el desencadenante sea "nuevo comentario", "cualquier webhook" o "nueva publicación". Para este ejemplo, se selecciona "nueva publicación".][5]

![En la plataforma Zapier, dentro de un zap, configura el desencadenante seleccionando el estado y el tipo de publicación deseados. Para este ejemplo, se selecciona "Published" y "Posts".][6]

### Paso 2: Añadir un webhook de acción {#step-2-add-an-action-webhook}

A continuación, define la acción del zap. Cuando tu zap está habilitado y se detecta tu desencadenante, la acción se producirá automáticamente.

Siguiendo con nuestro ejemplo, queremos enviar una solicitud POST como JSON a un punto de conexión de Braze. Para ello, selecciona la opción **Webhooks** en **Apps**.

![]({% image_buster /assets/img_archive/zapier3.png %})

### Paso 3: Configurar el POST de Braze {#step-3-set-up-braze-post}

Cuando configures tu webhook, utiliza la siguiente configuración y proporciona tu punto de conexión REST de Braze en la URL del webhook. Cuando hayas terminado, selecciona **Publish**.

- **Method**: POST
- **Webhook URL**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Data Pass-Through**: False
- **Unflatten**: No
- **Request Header**:
  - **Content-Type**: application/json
  - **Authorization**: Bearer YOUR-API-KEY
- **Data**:

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "context":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### Paso 4: Crear una Campaign en Braze {#step-4-create-a-braze-campaign}

Una vez que hayas configurado correctamente tu zap, puedes personalizar tus Campaigns o Canvas de Braze con datos de WordPress utilizando el formato Liquid para mostrar la información en tus mensajes.

## Uso de Zapier con el punto de conexión `/users/track` {#using-zapier-with-the-userstrack-endpoint}

Para enviar datos al punto de conexión [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze (por ejemplo, al usar un desencadenante como **New or Updated Spreadsheet Row** en Google Sheets), utiliza **Webhooks by Zapier** con una **Custom Request**; no uses la acción estándar **POST**. La acción POST estándar formatea la solicitud de una manera que no es compatible con el punto de conexión `/users/track`.

1. En Zapier, elige tu desencadenante (por ejemplo, **New or Updated Spreadsheet Row** en Google Sheets).
2. Para la acción, selecciona **Webhooks by Zapier** y elige **Custom Request** (no POST).
3. Establece **Method** en POST, introduce la URL de tu punto de conexión REST de Braze (por ejemplo, `https://rest.iad-01.braze.com/users/track`) y formatea el cuerpo de la solicitud con comillas dobles alrededor de cada elemento, como lo harías en Postman o en una llamada a la API. Mapea los campos de tu desencadenante (por ejemplo, columnas de la hoja de cálculo) en el cuerpo JSON donde corresponda.
4. Añade los encabezados obligatorios:
   - **Content-Type**: `application/json`
   - **Authorization**: `Bearer YOUR-REST-API-KEY` (usa tu clave de API REST de Braze sin corchetes ni comillas)
5. Prueba el paso y activa tu zap.

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}