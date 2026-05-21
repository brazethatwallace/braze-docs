---
nav_title: "POST: Envie e-mails de transação usando a entrega disparada por API"
article_title: "POST: Envie e-mails de transação usando a entrega disparada por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para envio de e-mails de transação usando a entrega disparada por API."

---

{% api %}
# Envie e-mails de transação usando a entrega disparada por API {#send-transactional-emails-using-api-triggered-delivery}
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Use esse endpoint para enviar mensagens transacionais únicas e imediatas a um usuário designado.

Esse endpoint é usado juntamente com a criação de uma [Campaign de e-mail de transação]({{site.baseurl}}/api/api_campaigns/transactional_campaigns/) da Braze e o ID de Campaign correspondente.

{% alert important %}
O e-mail de transação está atualmente disponível como parte de alguns pacotes da Braze. Entre em contato com seu gerente de sucesso do cliente da Braze para mais detalhes.
{% endalert %}

Semelhante ao [endpoint de envio de Campaign disparada]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), esse tipo de Campaign permite que você armazene o conteúdo da mensagem dentro do dashboard da Braze e, ao mesmo tempo, determine quando e para quem a mensagem será enviada por meio da sua API. Ao contrário do endpoint de envio de Campaign disparada, que aceita um público ou Segment para o qual enviar mensagens, uma solicitação a esse endpoint deve especificar um único usuário por meio de `external_user_id` ou `user_alias`, pois esse tipo de Campaign foi criado para o envio de mensagens 1:1 de alertas, como confirmações de pedidos ou redefinições de senha.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `transactional.send`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## Parâmetros de jornada {#path-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `campaign_id` | Obrigatória | String | ID da Campaign |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `external_send_id` | Opcional | String | Uma string compatível com Base64. Validada com o seguinte regex:<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>Esse campo opcional permite que você passe um identificador interno para esse envio específico, que é incluído em eventos enviados do postback de evento HTTP transacional. Quando passado, esse identificador também é usado como chave de deduplicação, que a Braze armazena por 24 horas. <br><br>Passar o mesmo identificador em outra solicitação não resulta em uma nova instância de envio pela Braze por 24 horas. |
| `trigger_properties` | Opcional | Objeto | Consulte [propriedades do gatilho]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Pares de chave-valor de personalização que se aplicam ao usuário nesta solicitação. |
| `recipient` | Obrigatória | Objeto | O usuário para o qual você está direcionando esta mensagem. Pode conter `attributes` e um único `external_user_id` ou `user_alias`.<br><br>Observe que, se você fornecer um ID de usuário externo que não existe na Braze, passar quaisquer campos para o objeto `attributes` cria esse perfil de usuário na Braze e envia a mensagem para o usuário recém-criado. <br><br>Se você enviar várias solicitações para o mesmo usuário com dados diferentes no objeto `attributes`, os atributos `first_name`, `last_name` e `email` são atualizados de forma síncrona e aplicados como template na sua mensagem. Os atributos personalizados não têm essa mesma proteção, portanto, tenha cuidado ao atualizar um usuário por meio dessa API e ao passar diferentes valores de atributos personalizados em rápida sucessão. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## Exemplo de solicitação {#example-request}

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## Resposta {#response}

O endpoint de envio de e-mail de transação responde com o `dispatch_id` da mensagem, que representa a instância desse envio de mensagem. Esse identificador pode ser usado junto com eventos do postback de evento HTTP transacional para rastrear o status de um e-mail individual enviado a um único usuário.

### Exemplos de respostas {#example-responses}

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## Solução de problemas {#troubleshooting}

O endpoint também pode retornar um código de erro e uma mensagem legível em alguns casos, a maioria dos quais são erros de validação. Aqui estão alguns erros comuns que você pode receber ao fazer solicitações inválidas.

| Erro | Solução de problemas |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | O ID de Campaign fornecido não é de uma Campaign transacional. |
| `The external reference has been queued.  Please retry to obtain send_id.` | O external_send_id foi criado recentemente. Tente um novo external_send_id se você pretende enviar uma nova mensagem. |
| `Campaign does not exist` | O ID de Campaign fornecido não corresponde a uma Campaign existente. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | O ID de Campaign fornecido corresponde a uma Campaign arquivada. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | O ID de Campaign fornecido corresponde a uma Campaign pausada. |
| `campaign_id must be a string of the campaign api identifier` | O ID de Campaign fornecido não é um formato válido. |
| `Error authenticating credentials` | A chave de API fornecida é inválida. |
| `Invalid whitelisted IPs ` | O endereço IP que está enviando a solicitação não está na lista de permissões de IP (se estiver sendo usada). |
| `You do not have permission to access this resource` | A chave de API usada não tem permissão para realizar essa ação. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

A maioria dos endpoints na Braze tem uma implementação de limite de taxa que retorna um código de resposta 429 se você fizer muitas solicitações. O endpoint de envio transacional tem uma alocação horária paga medida em unidades (por exemplo, 50.000 unidades por hora, dependendo do seu pacote). Não há um limite de taxa separado por endpoint para esse endpoint: você pode enviar além do seu volume alocado, mas apenas o volume alocado é coberto pelo SLA; solicitações acima dessa alocação ainda são enviadas, mas não são cobertas pelo SLA. As solicitações para esse endpoint contam para o seu [limite geral de taxa de API externa]({{site.baseurl}}/api/api_limits/). Se você exceder esse limite (por exemplo, 250.000 solicitações por hora em todos os endpoints), a Braze retorna 429 e limita as solicitações até que o limite seja redefinido. A contagem de volume transacional é redefinida a cada hora. Entre em contato com o suporte da Braze se precisar de mais informações sobre essa funcionalidade.

## Postback de evento HTTP transacional {#transactional-http-event-postback}

{% multi_lang_include http_event_postback.md %}

{% endapi %}