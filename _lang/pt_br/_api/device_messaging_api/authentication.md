---
nav_title: Autenticação e segurança
article_title: Autenticação e segurança da API de envio de mensagens do dispositivo
page_order: 1
page_type: reference
description: "Saiba como autenticar solicitações da API de envio de mensagens do dispositivo com segurança."
hidden: true
---

# Autenticação e segurança da API de envio de mensagens do dispositivo {#device-messaging-api-authentication-and-security}

A API de envio de mensagens do dispositivo usa chaves da REST API do lado do cliente. Essas chaves são diferentes das chaves privadas da REST API usadas para solicitações da REST API da Braze no lado do servidor.

{% alert important %}
Esta página está em beta. Os recursos e a documentação da API de envio de mensagens do dispositivo estão sujeitos a alterações. Entre em contato com o gerente da sua conta Braze para solicitar acesso.
{% endalert %}

## Chaves da API REST do lado do cliente {#client-side-rest-api-keys}

As chaves da API REST do lado do cliente são limitadas a um espaço de trabalho e restritas a permissões da API de envio de mensagens do dispositivo. Você pode incorporar essas chaves em aplicações do lado do cliente.

{% alert important %}
Use apenas uma chave da API REST do lado do cliente em uma aplicação do lado do cliente. Nunca exponha uma chave da API REST privada do lado do servidor em código do lado do cliente.
{% endalert %}

Para criar uma chave da API REST do lado do cliente:

1. Acesse **Configurações** > **APIs e identificadores** > **Chaves de API** no dashboard da Braze.
2. Selecione **Criar chave de API**.
3. Em **Tipo de chave**, selecione **Cliente**.
4. Atribua a permissão `banners.sync` para recuperar Banners, a permissão `banners.track` para reportar eventos de Banner, ou ambas.

## Autenticação de solicitações {#authenticating-requests}

Envie a chave da API REST do lado do cliente como um token bearer no cabeçalho `Authorization`:

```bash
Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}
```

Use HTTPS e o [endpoint REST]({{site.baseurl}}/api/basics#endpoints) da sua instância da Braze.

## Identidade do usuário {#user-identity}

Uma chave da API REST do lado do cliente autentica o aplicativo e o espaço de trabalho que estão fazendo a chamada, não o usuário. O `external_user_id` em uma solicitação identifica o usuário associado ao conteúdo e aos eventos do Banner.

Aplique os controles de autorização do seu aplicativo antes de fazer solicitações à API de envio de mensagens do dispositivo.

## Erros de autenticação {#authentication-errors}

Falhas de autenticação e permissão podem variar de acordo com o endpoint. Consulte a tabela de códigos de status de cada endpoint e o [tratamento de erros da API de envio de mensagens do dispositivo]({{site.baseurl}}/api/device_messaging_api/error_handling).