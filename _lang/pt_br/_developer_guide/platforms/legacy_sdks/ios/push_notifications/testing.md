---
nav_title: Testes
article_title: Testes de notificação por push para iOS
platform: iOS
page_order: 29
description: "Este artigo de referência aborda o teste de push pela linha de comando para suas notificações por push no iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Testes {#push-testing}

Se você quiser testar notificações no app e notificações por push pela linha de comando, pode enviar uma única notificação pelo terminal via CURL e a [API or interface de programação do aplicativo (API) de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging). Você precisará substituir os seguintes campos pelos valores corretos para o seu caso de teste:

Campos obrigatórios:

- `YOUR-API-KEY-HERE` — disponível em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. Confira se a chave está autorizada a enviar mensagens pelo endpoint `/messages/send` da REST or transferir estado representacional API or interface de programação do aplicativo (API).
- `EXTERNAL_USER_ID` — disponível na página **Pesquisar usuários**.
- `REST_API_ENDPOINT_URL` — listado nas [Instâncias]({{site.baseurl}}/API or interface de programação do aplicativo (API)/basics#endpoints. Ensure using the endpoint corresponds to the Braze instance your workspace is on.

Optional fields:
- `YOUR_KEY1` (optional) da Braze. Certifique-se de que o endpoint corresponde à instância da Braze em que seu espaço de trabalho está.

Campos opcionais:
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send
```
