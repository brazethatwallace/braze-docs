---
nav_title: optilyz
article_title: optilyz
description: "Este artículo de referencia describe la asociación entre Braze y optilyz, que te permite ejecutar campañas de correo directo más centradas en el cliente, sostenibles y rentables."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyz](https://optilyz.com) es una plataforma de automatización de correo directo que te permite ejecutar campañas de correo directo más centradas en el cliente, sostenibles y rentables.

_Esta integración está mantenida por optilyz._

## Sobre la integración {#about-the-integration}

Usa la integración de webhook de optilyz y Braze para enviar a tus clientes correo directo, como cartas, postales y autoenvíos.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de optilyz | Se necesita una cuenta de optilyz para aprovechar esta asociación. |
| Clave de API de optilyz<br><br>`<OPTILYZ_API_KEY>` | Tu administrador del éxito del cliente de optilyz te proporcionará tu clave de API de optilyz.<br><br>Esta clave de API te permitirá conectar tus cuentas de Braze y optilyz. |
| ID de automatización de optilyz<br><br>`<OPTILYZ_AUTOMATION_ID>` | El ID de automatización se encuentra en un recuadro en el encabezado de la página.<br><br>Cuando hayas iniciado sesión en optilyz, puedes navegar hasta la automatización a la que deseas enviar los datos.<br>Primero hay que activar la automatización. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Casos de uso {#use-cases}

Gestionar el correo directo como un canal digital significa alejarse de los envíos masivos y aprovechar el canal como parte de los recorridos (digitales) de tus clientes. Los beneficios de un enfoque moderno del correo directo son:
- Aumento de las tasas de conversión mediante una mayor relevancia, casos de uso adicionales, pruebas A/B más sencillas y efectos de canales cruzados
- Reducción del esfuerzo mediante la automatización y una solución de extremo a extremo
- Reducción de costes mediante contratos marco y transparencia de costes

## Integración {#integration}

Para integrarte con optilyz, usa la [API de optilyz](https://www.optilyz.com/doc/api/) para enviar los datos del destinatario al webhook de Braze.

### Paso 1: Crea tu plantilla de webhook de Braze {#step-1-create-your-braze-webhook-template}

Para crear una plantilla de webhook de optilyz que puedas usar en futuras Campaigns o Canvas, ve a **Contenido** > **Webhook** en la plataforma Braze. Luego, selecciona **Crear plantilla de webhook**.

Si deseas crear una campaña de webhook de optilyz única o usar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva campaña.

En tu nueva plantilla de webhook, completa los siguientes campos:
- **Webhook URL**: La URL del webhook es única para cada cliente y tu administrador del éxito del cliente de optilyz te la proporcionará.
- **Request Body**: Texto sin procesar

#### Encabezados de solicitud y método {#request-headers-and-method}

optilyz también requiere un encabezado HTTP para la autorización y un método HTTP. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Settings**, debes reemplazar `<OPTILYZ_API_KEY>` con tu clave de API de optilyz. Esta clave debe incluir un ":" justo después de la clave y estar codificada en base 64.

- **HTTP Method**: POST
- **Request Headers**:
  - **Authorization**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Los encabezados de solicitud y el método HTTP mostrados en el constructor de webhooks de Braze.]({% image_buster /assets/img/optilyz/optilyz_settings.png %}){: style="max-width:50%"}

#### Cuerpo de la solicitud {#request-body}

En el siguiente cuerpo de solicitud, puedes usar cualquier etiqueta de personalización de Liquid y crear una plantilla de solicitud personalizada de acuerdo con la [documentación de la API](https://www.optilyz.com/doc/api/) de optilyz.

El campo `variation` es opcional y puede definir qué diseño dentro de la automatización debe utilizarse. Si se omite una variación, optilyz asignará aleatoriamente una de las variaciones definidas.

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![Una imagen del código del cuerpo de la solicitud y la URL del webhook mostrados en la pestaña de redacción del constructor de webhooks de Braze.]({% image_buster /assets/img/optilyz/optilyz_compose.png %})

### Paso 2: Previsualiza tu solicitud {#step-2-preview-your-request}

A continuación, previsualiza tu solicitud en el panel **vista previa** o navega a la pestaña **Test**, donde puedes seleccionar un usuario al azar, un usuario existente o personalizar el tuyo propio para probar tu webhook. Recuerda guardar tu plantilla antes de salir de la página.

![Diferentes campos de prueba disponibles en la pestaña de prueba del constructor de webhooks de Braze.]({% image_buster /assets/img/optilyz/optilyz_testing.png %})

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas de webhook actualizadas se pueden encontrar en la lista **Plantillas de Webhook guardadas** al crear una nueva [campaña de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}