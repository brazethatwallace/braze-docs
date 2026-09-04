---
nav_title: "GET: Ver información sobre la plantilla de correo electrónico"
article_title: "GET: Ver información sobre la plantilla de correo electrónico"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint de Braze Ver plantilla de correo electrónico."
---
{% api %}
# Ver información sobre la plantilla de correo electrónico {#see-email-template-information}
{% apimethod get %}
/templates/email/info
{% endapimethod %}

> Usa este endpoint para obtener información sobre tus plantillas de correo electrónico.

{% alert important %}
No se aceptan plantillas creadas con el editor de arrastrar y soltar para correo electrónico.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

## Requisitos previos {#prerequisites}
Para usar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics) con el permiso `templates.email.info`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `email_template_id` | Obligatorio | Cadena | Consulta [el identificador de API de la plantilla de correo electrónico]({{site.baseurl}}/api/identifier_types). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```
{% endraw %}

## Respuesta {#response}

```json
{
  "email_template_id": (string) Your email template's API Identifier,
  "template_name": (string) The name of your email template,
  "description": (string) The email template description,
  "subject": (string) The email template subject line,
  "preheader": (optional, string) The email preheader used to generate previews in some clients),
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "should_inline_css": (optional, boolean) Whether there is inline CSS in the body of the template - defaults to the css inlining value for the workspace,
  "tags": (string) Tag names,
  "created_at": (string) The time the email was created at in ISO 8601,
  "updated_at": (string) The time the email was updated in ISO 8601
}
```

Las imágenes de esta respuesta se mostrarán en la variable `body` como HTML.

{% endapi %}