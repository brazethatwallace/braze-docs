---
nav_title: "POST: Criar modelo de e-mail"
article_title: "POST: Criar modelos de e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Criar modelos de e-mail\"."
---
{% api %}
# Criar modelo de e-mail {#create-email-template}
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> Use esse endpoint para criar modelos de e-mail no dashboard da Braze.

Esses modelos estarão disponíveis na página **Modelos e mídias**. A resposta desse endpoint inclui um campo para `email_template_id`, que pode ser usado para atualizar o modelo em chamadas subsequentes à API.

{% alert tip %}
Você também pode chamar esse endpoint por meio do [servidor MCP da Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) usando a função [`create_email_template`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#templates). Isso permite que ferramentas de IA como Claude e Cursor criem modelos de e-mail por meio de prompts em linguagem natural.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## Pré-requisitos {#prerequisites}
Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics) com a permissão `templates.email.create`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}

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

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `template_name` | Obrigatória | String | Nome do seu modelo de e-mail. |
| `subject` | Obrigatória | String | Linha de assunto do modelo de e-mail. |
| `body` | Obrigatória | String | Corpo do modelo de e-mail que pode incluir HTML. Até 400&nbsp;KB. |
| `plaintext_body` | Opcional | String | Uma versão em texto simples do corpo do modelo de e-mail. |
| `preheader` | Opcional | String | Pré-cabeçalho de e-mail usado para gerar prévias em alguns clientes. |
| `tags` | Opcional | String | As [tags]({{site.baseurl}}/user_guide/messaging/governance/tags) já devem existir. |
| `should_inline_css` | Opcional | Booleano | Ativa ou desativa o recurso `inline_css` por modelo. Se não for fornecido, a Braze usará a configuração padrão para o grupo de apps. Espera-se `true` ou `false`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
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

## Exemplo de resposta {#example-response}

```json
{
  "email_template_id": "232b6d29-7e41-4106-a0ab-1c4fe915d701",
  "message": "success"
}
```

## Solução de problemas {#troubleshooting}

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas, se aplicável.

| Erro | Solução de problemas |
| --- | --- |
| É necessário informar o nome do modelo. | Digite um nome de modelo. |
| As tags devem ser uma matriz. | As tags devem ser formatadas como uma matriz de strings, por exemplo, `["marketing", "promotional", "transactional"]`. |
| Todas as tags devem ser strings. | Confira se as tags estão entre aspas (`""`). |
| Algumas tags não puderam ser encontradas. | Para adicionar uma tag ao criar um modelo de e-mail, a tag já deve existir na Braze. |
| O e-mail deve ter nomes de Content Blocks válidos. | O e-mail pode conter Content Blocks que não existem nesse ambiente. |
| Valor inválido para `should_inline_css`. Esperava-se `true` ou `false`. | Esse parâmetro aceita apenas valores booleanos (true ou false). Certifique-se de que o valor de `should_inline_css` não esteja entre aspas (`""`), o que faz com que o valor seja enviado como uma string. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }

{% endapi %}