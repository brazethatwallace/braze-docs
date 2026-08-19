---
nav_title: Autenticação e segurança
article_title: Autenticação e segurança da API de envio de mensagens
page_order: 1
page_type: reference
description: "Saiba como autenticar solicitações da API de envio de mensagens com segurança."
hidden: true
---

# Autenticação e segurança da API de envio de mensagens {#messaging-api-authentication-and-security}

{% alert important %}
Esta página está em beta. Os recursos e a documentação da API de envio de mensagens estão sujeitos a alterações.
{% endalert %}

A API de envio de mensagens usa chaves da REST API do lado do cliente. Essas chaves são diferentes das chaves privadas da REST API usadas para solicitações da REST API da Braze no lado do servidor.

## Chaves da REST API do lado do cliente {#client-side-rest-api-keys}

As chaves da REST API do lado do cliente são limitadas a um espaço de trabalho e restritas às permissões da API de envio de mensagens. Você pode incorporar essas chaves em aplicativos do lado do cliente.

{% alert important %}
Use apenas uma chave da REST API do lado do cliente em um aplicativo do lado do cliente. Nunca exponha uma chave privada da REST API do lado do servidor em código do lado do cliente.
{% endalert %}

Para criar uma chave da REST API do lado do cliente:

1. Acesse **Configurações** > **APIs e identificadores** > **Chaves de API** no dashboard da Braze.
2. Selecione **Criar chave de API**.
3. Em **Tipo de chave**, selecione **Cliente**.
4. Atribua a permissão `banners.sync` para recuperar Banners, a permissão `banners.track` para reportar eventos de Banner, ou ambas.

## Autenticação de solicitações {#authenticating-requests}

Envie a chave da REST API do lado do cliente como um token bearer no cabeçalho `Authorization`:

```bash
Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}
```

Use HTTPS e o [endpoint REST]({{site.baseurl}}/api/basics#endpoints) da sua instância da Braze.

## Identidade do usuário {#user-identity}

Uma chave da REST API do lado do cliente autentica o aplicativo chamador e o espaço de trabalho, não o usuário. O `external_user_id` em uma solicitação identifica o usuário associado ao conteúdo e aos eventos de Banner.

Aplique os controles de autorização do seu aplicativo antes de fazer solicitações à API de envio de mensagens.

## Erros de autenticação {#authentication-errors}

Falhas de autenticação e permissão podem variar conforme o endpoint. Consulte a tabela de códigos de status de cada endpoint e o [tratamento de erros da API de envio de mensagens]({{site.baseurl}}/api/messaging_api/error_handling).