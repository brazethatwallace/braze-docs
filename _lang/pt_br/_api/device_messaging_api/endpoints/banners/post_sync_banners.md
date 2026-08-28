---
nav_title: "POST: Recuperar Banners para um usuário"
article_title: "POST: Recuperar Banners para um usuário"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Use este endpoint para recuperar Banners elegíveis para um usuário."
hidden: true
---

{% api %}
# Recuperar Banners para um usuário {#retrieve-banners-for-a-user}
{% apimethod post %}
/v1/device-messaging/banners/sync
{% endapimethod %}

> Use este endpoint para recuperar o Banner elegível para cada posicionamento solicitado para um usuário.

A resposta contém propriedades estruturadas do Banner que você pode usar para criar uma interface personalizada. Ela não contém HTML renderizado.

{% alert important %}
Esta página está em beta. Os recursos e a documentação da API de envio de mensagens para dispositivos estão sujeitos a alterações. Entre em contato com o gerente da sua conta Braze para solicitar acesso.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa do seguinte:

- Um espaço de trabalho com Banners ativados
- Uma [chave da API REST do lado do cliente]({{site.baseurl}}/api/device_messaging_api/authentication) com a permissão `banners.sync`
- O [endpoint REST]({{site.baseurl}}/api/basics#endpoints) da sua instância da Braze

Inclua a chave da API REST do lado do cliente no cabeçalho `Authorization` como um token bearer.

## Limite de frequência {#rate-limit}

Os limites de frequência se aplicam por espaço de trabalho. Se você exceder o limite de frequência, a Braze retornará um código de status `429`. Quando disponíveis, use os cabeçalhos de resposta `X-RateLimit-Limit`, `X-RateLimit-Remaining` e `X-RateLimit-Reset` para monitorar seu uso.

Para saber mais, consulte [Limites de frequência da API de envio de mensagens para dispositivos]({{site.baseurl}}/api/device_messaging_api/rate_limits).

## Corpo da requisição {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}
```

## Parâmetros da requisição {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição | Exemplo |
|---|---|---|---|---|
| `external_user_id` | Obrigatório | String | O ID externo do usuário. | `user_abc123` |
| `app_id` | Obrigatório | String | O [identificador de API do app]({{site.baseurl}}/api/identifier_types#app-identifier). Deve identificar um app no espaço de trabalho autenticado. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | Obrigatório | String | A versão do app host. Não deve exceder 255 caracteres. | `1.0.0` |
| `placements` | Obrigatório | Array de strings | Um ou mais IDs de posicionamento para recuperar Banners. Inclua pelo menos um ID de posicionamento. | `["home_hero", "sidebar_promo"]` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Parâmetros da requisição" }

## Exemplo de requisição {#example-request}

Substitua *`YOUR_REST_API_URL`* pelo [endpoint REST]({{site.baseurl}}/api/basics#endpoints) da sua instância da Braze.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/sync' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}'
```

## Parâmetros da resposta {#response-parameters}

| Parâmetro | Tipo de dados | Descrição |
|---|---|---|
| `banners` | Objeto | Um mapa de cada ID de posicionamento solicitado para o Banner resolvido. O valor é `null` quando nenhum Banner é elegível para um posicionamento. |
| `banners.{placement_id}.id` | String | O identificador único do Banner. Use este valor para reportar eventos de impressão e clique. |
| `banners.{placement_id}.placement_id` | String | O ID de posicionamento associado ao Banner. |
| `banners.{placement_id}.is_control` | Booleano | Se o Banner é uma variante do grupo de controle. |
| `banners.{placement_id}.is_test_send` | Booleano | Se o Banner é de um envio de teste. O padrão é `false`. |
| `banners.{placement_id}.expires_at` | Inteiro | O timestamp Unix, em segundos, após o qual o Banner não deve ser exibido. Um valor de `-1` significa que o Banner não expira. |
| `banners.{placement_id}.properties` | Objeto ou null | Propriedades definidas pelo profissional de marketing para o Banner. Cada propriedade contém um `type` e um `value`. |
| `banners.{placement_id}.properties.{property}.type` | String | O tipo da propriedade. Os valores possíveis são `number`, `string`, `boolean`, `image`, `jsonobject` e `datetime`. |
| `banners.{placement_id}.properties.{property}.value` | Número, string, booleano ou objeto | O valor da propriedade. O tipo JSON corresponde ao `type`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parâmetros da resposta" }

## Exemplo de resposta {#example-response}

Uma requisição bem-sucedida retorna um código de status `200` e o Banner resolvido para cada posicionamento solicitado.

```json
{
  "banners": {
    "home_hero": {
      "id": "this_banner_is_a_stub_01",
      "placement_id": "home_hero",
      "is_control": false,
      "is_test_send": false,
      "expires_at": 1735689600,
      "properties": {
        "headline": {
          "type": "string",
          "value": "Level Up Your Game"
        },
        "cta_label": {
          "type": "string",
          "value": "Shop Now"
        }
      }
    },
    "sidebar_promo": null
  }
}
```

## Códigos de status {#status-codes}

| Código de status | Descrição |
|---|---|
| `200` | A Braze resolveu os dados do Banner para cada posicionamento solicitado. |
| `400` | A requisição contém parâmetros ausentes ou inválidos. |
| `401` | A chave da API REST do lado do cliente está ausente, é inválida ou não possui a permissão `banners.sync`. |
| `404` | O endpoint não está disponível. Esta resposta não diferencia uma chave de API ausente ou inválida de um recurso de Banners desativado. |
| `429` | O espaço de trabalho excedeu seu limite de frequência. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Códigos de status" }

Para saber mais, consulte [Tratamento de erros e novas tentativas da API de envio de mensagens para dispositivos]({{site.baseurl}}/api/device_messaging_api/error_handling).

{% endapi %}