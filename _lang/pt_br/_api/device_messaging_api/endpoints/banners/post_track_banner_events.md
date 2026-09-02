---
nav_title: "POST: Rastrear eventos de análise de dados de Banners"
article_title: "POST: Rastrear eventos de análise de dados de Banners"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Use este endpoint para rastrear eventos de impressão, clique e dispensa para Banners."
hidden: true
---

{% api %}
# Rastrear eventos de análise de dados de Banners {#track-banner-analytics-events}
{% apimethod post %}
/v1/device-messaging/banners/track
{% endapimethod %}

> Use este endpoint para registrar eventos de impressão, clique e dispensa para Banners.

A Braze valida cada evento separadamente. Quando uma solicitação contém eventos válidos e inválidos, a Braze processa os eventos válidos e retorna detalhes sobre os eventos ignorados no array `errors`. Se nenhum evento for válido, a Braze retorna um código de status `400`.

{% alert important %}
Esta página está em beta. Os recursos e a documentação da API de envio de mensagens para dispositivos estão sujeitos a alterações. Entre em contato com o gerente da sua conta Braze para solicitar acesso.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa do seguinte:

- Um espaço de trabalho com Banners ativados
- Uma [chave da API REST do lado do cliente]({{site.baseurl}}/api/device_messaging_api/authentication) com a permissão `banners.track`
- O [endpoint REST]({{site.baseurl}}/api/basics#endpoints) da sua instância da Braze
- Um `id` de Banner retornado pelo [endpoint Recuperar Banners para um usuário]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)

Inclua a chave da API REST do lado do cliente no cabeçalho `Authorization` como um token bearer.

## Limite de frequência {#rate-limit}

Os limites de frequência se aplicam por espaço de trabalho. Se você exceder o limite de frequência, a Braze retornará um código de status `429`. Quando disponíveis, use os cabeçalhos de resposta `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` e `X-RateLimit-Retry-After` para monitorar seu uso e determinar quando tentar novamente.

Para saber mais, consulte [Limites de frequência da API de envio de mensagens do dispositivo]({{site.baseurl}}/api/device_messaging_api/rate_limits).

## Dispensar Banners {#dismissing-banners}

Rastrear um evento `dismiss` dispensa o Banner para o usuário especificado. Sincronizações de Banner subsequentes para esse usuário não incluirão Banners dispensados anteriormente, a menos que a reelegibilidade esteja configurada na Campaign.

{% alert note %}
Eventos de dispensa são processados de forma assíncrona e não são refletidos imediatamente. Em casos raros, o processamento pode levar alguns minutos. Evite chamar o [endpoint Recuperar Banners para um usuário]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners) imediatamente após uma dispensa, pois o Banner ainda pode ser retornado durante esse intervalo.
{% endalert %}

A Braze não reconcilia o estado do Banner na sua interface. Ocultar o Banner após uma dispensa e mantê-lo oculto até que a Braze processe o evento é responsabilidade do seu app.

## Corpo da solicitação {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "{BANNER_ID}",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    }
  ]
}
```

## Parâmetros da solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição | Exemplo |
|---|---|---|---|---|
| `external_user_id` | Obrigatório | String | O ID externo do usuário associado a todos os eventos na solicitação. O valor codificado em UTF-8 deve ter menos de 987 bytes. | `user_abc123` |
| `app_id` | Obrigatório | String | O [identificador de API do app]({{site.baseurl}}/api/identifier_types#app-identifier). Deve identificar um app no espaço de trabalho autenticado. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | Obrigatório | String | A versão do app host. Não deve exceder 255 caracteres. | `1.0.0` |
| `events` | Obrigatório | Array de objetos | Um ou mais eventos de análise de dados de Banner para registrar. | `[{"id":"bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E","event_type":"impression","timestamp":"2026-04-09T12:00:00Z"}]` |
| `events[].id` | Obrigatório | String | O `id` do Banner retornado pelo endpoint Recuperar Banners para um usuário. Use o ID do Banner, não o `placement_id`, para que a Braze atribua o evento à Campaign e à variante corretas. | `bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E` |
| `events[].event_type` | Obrigatório | String | O tipo de evento. Os valores possíveis são `impression`, `click` e `dismiss`. | `impression` |
| `events[].timestamp` | Obrigatório | String | A data e hora em que o evento ocorreu, formatada como uma string [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | `2026-04-09T12:00:00Z` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Parâmetros da solicitação" }

## Exemplo de solicitação {#example-request}

Substitua *`YOUR_REST_API_URL`* pelo [endpoint REST]({{site.baseurl}}/api/basics#endpoints) da sua instância da Braze.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/track' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    },
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "click",
      "timestamp": "2026-04-09T12:00:05Z"
    }
  ]
}'
```

## Parâmetros da resposta {#response-parameters}

| Parâmetro | Tipo de dados | Descrição |
|---|---|---|
| `events_processed` | Inteiro | O número de eventos que a Braze validou e enfileirou. |
| `message` | String | O status do lote de eventos aceito. |
| `errors` | Array de objetos | Detalhes sobre os eventos que a Braze ignorou. Este array está ausente quando a Braze processa todos os eventos. |
| `errors[].type` | String | O erro de validação do evento ignorado. |
| `errors[].index` | Inteiro | O índice baseado em zero do evento ignorado no array `events` da solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parâmetros da resposta" }

## Exemplos de resposta {#example-responses}

### Todos os eventos processados {#all-events-processed}

Quando a Braze aceita todos os eventos, ela retorna um código de status `202`.

```json
{
  "events_processed": 2,
  "message": "success"
}
```

### Alguns eventos ignorados {#some-events-skipped}

A Braze também retorna um código de status `202` quando aceita pelo menos um evento válido. A resposta identifica os eventos ignorados.

```json
{
  "events_processed": 2,
  "message": "success",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click, dismiss.",
      "index": 2
    }
  ]
}
```

### Nenhum evento válido {#no-valid-events}

Se a Braze não conseguir processar nenhum evento, ela retornará um código de status `400`.

```json
{
  "message": "No valid events provided.",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click, dismiss.",
      "index": 0
    },
    {
      "type": "'timestamp' is required",
      "index": 1
    }
  ]
}
```

## Códigos de status {#status-codes}

| Código de status | Descrição |
|---|---|
| `202` | A Braze aceitou pelo menos um evento. A resposta lista os eventos ignorados. |
| `400` | A solicitação está malformada, os campos obrigatórios são inválidos ou nenhum evento é válido. |
| `401` | A chave da API REST do lado do cliente está ausente ou é inválida. |
| `403` | A chave da API REST do lado do cliente não tem a permissão `banners.track`. |
| `404` | O recurso de Banners não está ativado para o espaço de trabalho. |
| `429` | O espaço de trabalho excedeu seu limite de frequência. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Códigos de status" }

Para saber mais, consulte [Tratamento de erros e novas tentativas da API de envio de mensagens do dispositivo]({{site.baseurl}}/api/device_messaging_api/error_handling).

{% endapi %}