---
nav_title: "POST: Crear plantilla de correo electrónico"
article_title: "POST: Crear plantillas de correo electrónico"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint de Braze Crear plantillas de correo electrónico."
---
{% api %}
# Crear plantilla de correo electrónico {#create-email-template}
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> Utiliza este endpoint para crear plantillas de correo electrónico en el panel de Braze.

Estas plantillas estarán disponibles en la página **Plantillas y medios**. La respuesta de este endpoint incluye un campo para `email_template_id`, que puede utilizarse para actualizar la plantilla en posteriores llamadas a la API.

{% alert tip %}
También puedes llamar a este endpoint a través del [servidor MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) utilizando la función [`create_email_template`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#templates). Esto permite que herramientas de IA como Claude y Cursor creen plantillas de correo electrónico mediante indicaciones en lenguaje natural.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics) con el permiso `templates.email.create`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "template_name": (required, string) The name of your email template,
   "subject": (required, string) The email template subject line,
   "body": (required, string) The email template body that may include HTML,
   "plaintext_body": (optional, string) A plaintext version of the email template body,
   "preheader": (optional, string) The email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist,
   "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature is used on this template.
 }
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `template_name` | Obligatorio | Cadena | Nombre de tu plantilla de correo electrónico. |
| `subject` | Obligatorio | Cadena | Línea del asunto de la plantilla de correo electrónico. |
| `body` | Obligatorio | Cadena | Cuerpo de la plantilla de correo electrónico que puede incluir HTML. Hasta 400&nbsp;KB. |
| `plaintext_body` | Opcional | Cadena | Una versión en texto plano del cuerpo de la plantilla de correo electrónico. |
| `preheader` | Opcional | Cadena | Preencabezado de correo electrónico utilizado para generar vistas previas en algunos clientes. |
| `tags` | Opcional | Cadena | Las [etiquetas]({{site.baseurl}}/user_guide/messaging/governance/tags) ya deben existir. |
| `should_inline_css` | Opcional | Booleano | Habilita o deshabilita la característica `inline_css` por plantilla. Si no se proporciona, Braze utilizará la configuración predeterminada para el grupo de aplicaciones. Se espera uno de `true` o `false`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## Ejemplo de respuesta {#example-response}

```json
{
  "email_template_id": "232b6d29-7e41-4106-a0ab-1c4fe915d701",
  "message": "success"
}
```

## Solución de problemas {#troubleshooting}

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas, si procede.

| Error | Solución de problemas |
| --- | --- |
| El nombre de la plantilla es obligatorio. | Introduce un nombre para la plantilla. |
| Las etiquetas deben ser una matriz. | Las etiquetas deben formatearse como una matriz de cadenas, por ejemplo `["marketing", "promotional", "transactional"]`. |
| Todas las etiquetas deben ser cadenas. | Asegúrate de que tus etiquetas estén entre comillas (`""`). |
| No se han encontrado algunas etiquetas. | Para añadir una etiqueta al crear una plantilla de correo electrónico, la etiqueta debe existir ya en Braze. |
| El correo electrónico debe tener nombres de Content Blocks válidos. | El correo electrónico puede contener Content Blocks que no existen en este entorno. |
| Valor no válido para `should_inline_css`. Se esperaba uno de `true` o `false`. | Este parámetro solo acepta valores booleanos (true o false). Asegúrate de que el valor de `should_inline_css` no esté entre comillas (`""`), lo que hace que el valor se envíe como una cadena en lugar de un booleano. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

{% endapi %}