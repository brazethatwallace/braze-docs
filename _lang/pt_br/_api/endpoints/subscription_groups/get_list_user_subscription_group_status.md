---
nav_title: "GET: Listar o status do grupo de inscrições dos usuários"
article_title: "GET: Listar status do grupo de inscrições do usuário"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para listar o status do grupo de inscrições do usuário."

---
{% api %}
# Listar status do grupo de inscrições do usuário {#list-users-subscription-group-status}
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> Use este endpoint para obter o estado de inscrição de um usuário em um grupo de inscrições.

Esses grupos estarão disponíveis na página do **Grupo de inscrições**. A resposta deste endpoint incluirá o ID externo e o status subscribed, unsubscribed ou unknown para o grupo de inscrições específico solicitado na chamada de API. Isso pode ser usado para atualizar o estado do grupo de inscrições em chamadas subsequentes de API ou para ser exibido em uma página da web hospedada.

Se você quiser ver exemplos ou testar este endpoint para **grupos de inscrições para e-mail**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

Se você quiser ver exemplos ou testar este endpoint para **grupos de inscrições de SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

Se você quiser ver exemplos ou testar este endpoint para **grupos do WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `subscription.status.get`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types?tab=subscription%20group%20ids) | Obrigatório | String | O `id` do seu grupo de inscrições. |
| `external_id` | Obrigatório* | String | O `external_id` do usuário (deve incluir pelo menos um e no máximo 50 `external_ids`). <br><br>Quando um `external_id` e `email`/`phone` são enviados juntos, apenas os `external_id`(s) fornecidos serão aplicados à consulta de resultado. |
| `email` | Obrigatório* | String | O endereço de e-mail do usuário. Pode ser passado como um array de strings com no máximo 50.<br><br> Enviar tanto um endereço de e-mail quanto um número de telefone (sem `external_id`) resultará em um erro. |
| `phone` | Obrigatório* | String no formato [E.164](https://en.wikipedia.org/wiki/E.164) | O número de telefone do usuário. Se o e-mail não estiver incluído, você deve incluir pelo menos um número de telefone (com no máximo 50).<br><br> Enviar tanto um endereço de e-mail quanto um número de telefone (sem `external_id`) resultará em um erro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação" }

*Um entre `external_id`, `email` ou `phone` é obrigatório para cada usuário.

- Para grupos de inscrições de SMS e WhatsApp, é necessário `external_id` ou `phone`. Quando ambos são enviados, apenas o `external_id` é usado para a consulta e o número de telefone é aplicado a esse usuário.
- Para grupos de inscrições para e-mail, é necessário `external_id` ou `email`. Quando ambos são enviados, apenas o `external_id` é usado para a consulta e o endereço de e-mail é aplicado a esse usuário.

## Exemplo de solicitação {#example-request}

{% tabs %}
{% tab Múltiplos usuários %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS e WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab E-mail %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@example.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Resposta {#response}

Todas as respostas bem-sucedidas retornarão `Subscribed`, `Unsubscribed` ou `Unknown` dependendo do status e do histórico do usuário com o grupo de inscrições.

```json
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% alert important %}
Este endpoint retorna o status do grupo de inscrições de forma independente do estado global de inscrição do usuário. Se um usuário tiver cancelado a inscrição globalmente, o dashboard da Braze o mostrará como cancelado em cada grupo de inscrições. No entanto, este endpoint ainda retorna o último status salvo do grupo de inscrições (por exemplo, `Subscribed`) porque o estado global de inscrição se sobrepõe aos grupos de inscrições individuais sem sobrescrevê-los.<br><br>A Braze preserva os estados individuais dos grupos de inscrições para que, se o usuário se reinscrever globalmente, cada grupo de inscrições retorne ao seu status salvo anteriormente. Para determinar o estado efetivo de inscrição de um usuário, verifique tanto o status de inscrição global quanto o status do grupo de inscrições retornado por este endpoint.
{% endalert %}

{% endapi %}