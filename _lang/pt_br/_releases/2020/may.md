---
nav_title: Maio
page_order: 8
noindex: true
page_type: update
description: "Este artigo contém notas de versão de maio de 2020."
---
# Maio de 2020 {#may-2020}

## Google Tag Manager

Foram adicionados documentação e exemplos de como implantar e gerenciar o SDK or kit de desenvolvimento de software da Braze para Android usando o [Google Tag Manager]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

## Novo endpoint de API or interface de programação do aplicativo (API) para lista de proibições de e-mail {#new-blacklist-email-api-endpoint}

Agora você pode colocar endereços de e-mail [em uma lista de proibições]({{site.baseurl}}/api/endpoints/email/post_blacklist) por meio da API or interface de programação do aplicativo (API) da Braze. A inclusão de um endereço de e-mail na lista de proibições cancelará a inscrição do usuário no e-mail e o marcará como hard bounce.

## Alteração da chave de API or interface de programação do aplicativo (API) para endpoints da API or interface de programação do aplicativo (API) da Braze {#api-key-change-for-braze-api-endpoints}

A partir de maio de 2020, a Braze mudou a forma como lemos as chaves de API or interface de programação do aplicativo (API) para torná-las mais seguras. Agora, as chaves de API or interface de programação do aplicativo (API) devem ser passadas como um cabeçalho da solicitação. Os exemplos podem ser encontrados nas páginas de endpoints individuais em **Example Request**, bem como em **API or interface de programação do aplicativo (API) Key Explanation**.

A Braze continuará a oferecer suporte ao `api_key` sendo transmitido por meio do corpo da solicitação e dos parâmetros de URL, mas acabará sendo descontinuado (a definir). **Atualize suas chamadas de API or interface de programação do aplicativo (API) adequadamente.** Essas alterações foram atualizadas no [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro).
{% details API or interface de programação do aplicativo (API) Key Explanation %}
{% tabs %}
{% tab GET Request %}
Este exemplo usa o endpoint `/email/hard_bounces`.

**Antes: chave de API or interface de programação do aplicativo (API) no corpo da solicitação**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key={YOUR_REST_API_KEY}&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@example.com' \
```
**Agora: chave de API or interface de programação do aplicativo (API) no cabeçalho**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@example.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST Request %}
Este exemplo usa o endpoint `/user/track`.

**Antes: chave de API or interface de programação do aplicativo (API) no corpo da solicitação**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key": YOUR-API-KEY-HERE ,
	"attributes": [
 	{
 	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
**Agora: chave de API or interface de programação do aplicativo (API) no cabeçalho**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
	"attributes": [
 	{
	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}