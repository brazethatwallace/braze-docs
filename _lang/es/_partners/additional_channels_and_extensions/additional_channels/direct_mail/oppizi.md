---
nav_title: Oppizi
article_title: Oppizi
alias: /partners/oppizi/
description: "Este artículo de referencia describe la asociación entre Braze y Oppizi."
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/) es el líder mundial en marketing offline, que ofrece una solución integral para que las empresas realicen campañas de correo directo y folletos mensurables y específicas.

_Esta integración está mantenida por Oppizi._

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Cuenta Oppizi | Para utilizar esta integración se necesita una cuenta activa de Oppizi. |
| Clave de API de Oppizi | Se encuentra en tu cuenta de Oppizi en **Integrations** > **Braze**. |
| ID de flujo de trabajo de correo directo de Oppizi | Crea un flujo de trabajo en Oppizi en la página **Direct Mail Workflow** para obtener un ID. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Con la integración de Oppizi, puedes:

* **Enviar postales automatizadas de correo directo** utilizando desencadenadores de Braze conectados a los flujos de trabajo de webhook y correo directo de Oppizi.
* **Configurar umbrales, oleadas y límites** en los flujos de trabajo de correo directo de Oppizi para controlar el envío de tus campañas.
* **Diseñar postales profesionales** con la herramienta de diseño integrada de Oppizi, sin necesidad de tener experiencia en diseño.
* **Seguir el rendimiento de la campaña** en tiempo real con el dashboard de Oppizi.

## Integración {#integration}

### Paso 1: Genera tu clave de API de Oppizi {#step-1-generate-your-oppizi-api-key}

Para utilizar tu plantilla de webhook en Braze, primero tendrás que generar tu clave de API de Oppizi.

1. Inicia sesión en Oppizi.
2. Ve a **Integrations** > **Braze**.
3. Genera tu clave de API.

Desde esta página puedes gestionar, revocar y crear tus claves cuando lo necesites.

### Paso 2: Crea una plantilla de webhook en Braze {#step-2-create-a-braze-webhook-template}

A continuación, crea una plantilla de webhook para Oppizi en Braze para utilizarla en futuras Campaigns o Canvas:

1. En Braze, ve a **Content** > **Webhook**.
2. Selecciona **Create webhook template**.
3. Proporciona un nombre para la plantilla.
4. En tu plantilla de webhook, rellena los siguientes campos:

- **Webhook URL:** `https://webhooks.oppizi.com/events`
- **Request body:** **Raw Text**

Para el método de solicitud y los encabezados, Oppizi requiere que se incluya en la plantilla un método HTTP junto con los siguientes encabezados HTTP. Rellena los siguientes campos:

- **HTTP method:** POST
- **Request headers:**
  - **Authorization:** `Bearer <oppiziAPIKey>`
  - **Content-Type:** `application/json`

![Un ejemplo del encabezado del webhook de Oppizi en Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

Para el **Request Body**, debes incluir el campo **oppiziWorkflowID**. Este ID se genera cuando se crea un flujo de trabajo en Oppizi y es necesario para especificar a qué flujo de trabajo de correo directo deben añadirse tus destinatarios. Cada flujo de trabajo de correo directo en Oppizi tiene un ID único, así que si creas una plantilla de webhook de Oppizi en Braze, asegúrate de actualizar siempre el ID del flujo de trabajo al correcto.

{% alert note %}
Comprueba que los atributos personalizados requeridos están configurados en tu cuenta de Braze para las direcciones postales de tus destinatarios, ya que son necesarios para enviar correo directo.
{% endalert %}

![Un ejemplo de plantilla de webhook de Oppizi en Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

A continuación se muestra un ejemplo de cuerpo de solicitud:

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### Paso 3: Crea un flujo de trabajo de correo directo en Oppizi {#step-3-create-a-direct-mail-workflow-in-oppizi}

1. En Oppizi, ve a **Direct Mail Workflow** > **Create workflow**.
2. Configura los detalles del flujo de trabajo, incluyendo umbrales, oleadas, formato de postal e ilustraciones.
3. En la sección de detalles del webhook, encontrarás un cuerpo de solicitud listo para usar, incluido el ID de tu flujo de trabajo, que puedes pegar directamente en Braze.

### Paso 4: Vista previa y prueba de tu solicitud en Braze {#step-4-preview-and-test-your-request-in-braze}

Después de añadir el cuerpo de tu solicitud con el ID de flujo de trabajo de Oppizi, realiza una prueba para confirmar que tu configuración funciona como esperabas.

Para ejecutar la prueba, actualiza `requestType` de `live` a `test` en el cuerpo de la solicitud. Ten en cuenta que este paso es crucial para evitar añadir destinatarios de prueba a tu audiencia de correo directo.

Cuando termines las pruebas, actualiza `requestType` de nuevo a `live` y guarda tu Canvas. Ahora ya estás listo para lanzar tus campañas automatizadas de correo directo.