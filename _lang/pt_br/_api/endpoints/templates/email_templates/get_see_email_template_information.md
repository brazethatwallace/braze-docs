---
nav_title: "GET: Ver informações do modelo de e-mail"
article_title: "GET: Ver informações do modelo de e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Ver informações do modelo de e-mail\"."

---
{% api %}
# Ver informações do modelo de e-mail {#see-email-template-information}
{% apimethod get %}
/templates/email/info
{% endapimethod %}

> Use este endpoint para obter informações sobre seus modelos de e-mail.

{% alert important %}
Modelos criados usando o editor de arrastar e soltar para e-mail não são aceitos.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

## Pré-requisitos {#prerequisites}
Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `templates.email.info`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `email_template_id` | Obrigatória | String | Veja [identificador de API de modelo de e-mail]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```
{% endraw %}

## Resposta {#response}

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

As imagens nesta resposta aparecerão na variável `body` como HTML.

{% endapi %}