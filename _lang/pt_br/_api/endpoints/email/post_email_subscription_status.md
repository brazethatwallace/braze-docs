---
nav_title: "POST: Alterar o status da inscrição de e-mail"
article_title: "POST: Alterar o status da inscrição de e-mail"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Alterar o status da inscrição de e-mail do usuário\"."

---
{% api %}
# Alterar o status da inscrição de e-mail {#change-email-subscription-status}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/status
{% endapimethod %}

> Use esse endpoint para definir o estado global da inscrição de e-mail para seus usuários.

Os usuários podem ser `opted_in`, `unsubscribed` ou `subscribed` (sem aceitação ou exclusão específica).

{% alert note %}
Esse endpoint atualiza o estado global da inscrição de e-mail do usuário, que é diferente do status do grupo de inscrições. O estado global da inscrição se aplica a todos os e-mails, enquanto os [grupos de inscrições]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) permitem um controle mais granular sobre tipos específicos de e-mails. Quando um usuário tem a inscrição cancelada globalmente, ele não receberá e-mails independentemente do status do grupo de inscrições. Para consultar o status do grupo de inscrições, use o [endpoint Listar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status).
{% endalert %}

É possível definir o estado da inscrição de e-mail para um endereço de e-mail que ainda não esteja associado a nenhum de seus usuários na Braze. Quando esse endereço de e-mail for posteriormente associado a um usuário, o estado de inscrição de e-mail que você enviou será automaticamente definido.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `email.status`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@example.com",
  "subscription_state": "subscribed"
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `email` | Obrigatório | String ou matriz | Endereço de e-mail em string para modificar ou uma matriz de até 50 endereços de e-mail para modificar. |
| `subscription_state` | Obrigatório | String | "subscribed", "unsubscribed" ou "opted_in". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Solução de problemas com bloqueios de e-mail do SendGrid {#troubleshooting-sendgrid-email-blocks}

Quando o SendGrid bloqueia um destinatário, atualize o status da inscrição com esse endpoint e revise o engajamento usando filtros de segmento. Use os eventos de soft bounce do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para monitoramento de entregabilidade e confirme o estado da inscrição antes de tentar reenviar.

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@example.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}