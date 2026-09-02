---
nav_title: Tratamento de erros e novas tentativas
article_title: Tratamento de erros e novas tentativas da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos
page_order: 2
page_type: reference
description: "Saiba como lidar com respostas, erros e novas tentativas da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos."
hidden: true
---

# Tratamento de erros e novas tentativas da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos {#device-messaging-api-error-handling-and-retries}

Os corpos de resposta e a semântica de sucesso da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos variam conforme o endpoint. Use o esquema de resposta e a tabela de códigos de status de cada endpoint como o contrato oficial.

{% alert important %}
Esta página está em beta. Os recursos e a documentação da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos estão sujeitos a alterações. Entre em contato com o gerente da sua conta Braze para solicitar acesso.
{% endalert %}

## Respostas de sucesso {#success-responses}

Os endpoints de Banner usam respostas de sucesso diferentes:

- `POST /v1/device-messaging/banners/sync` retorna um código de status `200` com um objeto `banners`.
- `POST /v1/device-messaging/banners/track` retorna um código de status `202` com `events_processed` e `message`. Se a Braze ignorar eventos individuais, a resposta também inclui um array `errors`.

Uma resposta `202` do endpoint de rastreamento significa que a Braze aceitou pelo menos um evento válido. Revise o array `errors` para identificar eventos ignorados.

## Respostas de erro {#error-responses}

Os campos de resposta de erro também variam:

- Erros de recuperação de banner usam um campo `error`.
- Erros de rastreamento de banner usam um campo `message` e podem incluir um array `errors` indexado.

Não analise o texto da mensagem de erro para determinar o comportamento do aplicativo. Use o código de status HTTP e os campos específicos do endpoint.

## Orientações para novas tentativas {#retry-guidance}

Use as orientações a seguir para decidir se deve tentar novamente:

| Código de status | Orientações para nova tentativa |
|---|---|
| `400` | Corrija a solicitação antes de tentar novamente. Para rastreamento de Banner, corrija os eventos ignorados antes de reenviá-los. |
| `401` ou `403` | Verifique a chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional no lado do cliente e suas permissões antes de tentar novamente. |
| `404` | Confirme se a API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos está ativada para o espaço de trabalho e se a URL do endpoint está correta. |
| `429` | Reduza a taxa de solicitações e tente novamente com recuo exponencial. Use os cabeçalhos de resposta de limite de taxa quando disponíveis. |
| `5XX` | Tente novamente com recuo exponencial e um número máximo de tentativas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Orientações para novas tentativas da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos" }

Para o corpo exato da resposta e os códigos de status compatíveis, consulte o endpoint relevante:

- [Recuperar Banners para um usuário]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)
- [Rastrear eventos de análise de dados de Banner]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_track_banner_events)