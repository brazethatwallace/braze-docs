---
nav_title: "POST: Atualizar modelo de e-mail"
article_title: "POST: Atualizar modelos de e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Atualizar modelo de e-mail\"."

---
{% API or interface de programação do aplicativo (API) %}
# Atualizar modelos de e-mail existentes {#update-existing-email-templates}
{% apimethod post %}
/templates/email/update
{% endapimethod %}

> Use esse endpoint para atualizar modelos de e-mail no dashboard da Braze.

É possível acessar o `email_template_id` de um modelo de e-mail navegando até ele na página **Modelos e mídias**. O [endpoint Criar modelo de e-mail]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) também retornará uma referência `email_template_id`.

Todos os campos, exceto o `email_template_id`, são opcionais, mas você precisa especificar pelo menos um campo para atualizar.

{% alert tip %}
Você também pode chamar esse endpoint por meio do [servidor MCP da Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) usando a função [`update_email_template`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#templates). Isso permite que ferramentas de IA como Claude e Cursor atualizem modelos de e-mail por meio de prompts em linguagem natural.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## Pré-requisitos {#prerequisites}
Para usar esse endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics) com a permissão `templates.email.update`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "email_template_id": (required, string) Your email template's API Identifier,
  "template_name": (optional, string) The name of your email template,
  "subject": (optional, string) The email template subject line,
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "preheader": (optional, string) The email preheader used to generate previews in some clients,
  "tags": (optional, array of Strings) Tags must already exist,
  "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature will be applied to the template.
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `email_template_id` | Obrigatório | String | O [identificador de API or interface de programação do aplicativo (API) do seu modelo de e-mail]({{site.baseurl}}/api/identifier_types). |
| `template_name` | Opcional | String | Nome do seu modelo de e-mail. |
| `subject` | Opcional | String | Linha de assunto do modelo de e-mail. |
| `body` | Opcional | String | Corpo do modelo de e-mail que pode incluir HTML. |
| `plaintext_body` | Opcional | String | Uma versão em texto simples do corpo do modelo de e-mail. |
| `preheader` | Opcional | String | Pré-cabeçalho de e-mail usado para gerar prévias em alguns clientes. |
| `tags` | Opcional | String | As [tags]({{site.baseurl}}/user_guide/messaging/governance/tags) já devem existir. |
| `should_inline_css` | Opcional | Boolean | Ativa ou desativa o recurso `inline_css` por modelo. Se não for fornecido, a Braze usará a configuração padrão para o grupo de apps. Espera-se `true` ou `false`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## Solução de problemas {#troubleshooting}

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas, se aplicável.

| Erro | Solução de problemas |
| --- | --- |
| É necessário informar o nome do modelo. | Insira um nome de modelo. |
| As tags devem ser uma matriz. | As tags devem ser formatadas como uma matriz de strings, por exemplo, `["marketing", "promotional", "transactional"]`. |
| Todas as tags devem ser strings. | Confira se as tags estão entre aspas (`""`). |
| Algumas tags não puderam ser encontradas. | Para adicionar uma tag ao criar um modelo de e-mail, a tag já deve existir na Braze. |
| Valor inválido para `should_inline_css`. Esperava-se `true` ou `false`. | Esse parâmetro aceita apenas valores booleanos (true ou false). Certifique-se de que o valor de `should_inline_css` não esteja entre aspas (`""`), o que faz com que o valor seja enviado como uma string. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }

{% endapi %}