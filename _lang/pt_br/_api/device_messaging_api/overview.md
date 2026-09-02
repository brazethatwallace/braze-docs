---
nav_title: Visão geral
article_title: Visão geral da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos
page_order: 0
page_type: reference
description: "Saiba mais sobre a API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos da Braze e seus recursos em acesso antecipado."
hidden: true
---

# Visão geral da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos {#device-messaging-api-overview}

A API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos da Braze é um conjunto de endpoints REST or transferir estado representacional para integrar os recursos de envio de mensagens da Braze sem um SDK or kit de desenvolvimento de software da Braze. Você pode chamar esses endpoints a partir de aplicações cliente ou servidor.

{% alert important %}
Esta página está em beta. Os recursos e a documentação da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos estão sujeitos a alterações. Entre em contato com o gerente da sua conta Braze para solicitar acesso.
{% endalert %}

## Recursos suportados {#supported-capabilities}

Durante o acesso antecipado, você pode usar a API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos para:

- [Recuperar Banners elegíveis]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners) para um ID de usuário externo e um conjunto de posicionamentos
- [Relatar eventos de impressão e clique de Banner]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_track_banner_events)

A API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos retorna propriedades estruturadas de Banner para que você possa criar uma interface personalizada. Ela não retorna HTML renderizado.

## Requisitos de integração {#integration-requirements}

Para integrar a API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos, você precisa de:

- Um espaço de trabalho com a API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos ativada
- Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional do lado do cliente para esse espaço de trabalho
- O endpoint REST or transferir estado representacional para esse espaço de trabalho
- O ID de usuário externo do usuário
- O identificador de API or interface de programação do aplicativo (API) do app

Para saber mais sobre credenciais, consulte [Autenticação e segurança]({{site.baseurl}}/api/device_messaging_api/authentication).

## Orientações sobre a API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos e a REST or transferir estado representacional API or interface de programação do aplicativo (API) {#device-messaging-api-and-rest-api-guidance}

A API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos usa os mesmos endpoints REST or transferir estado representacional regionais que a REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze, mas possui um contrato separado de autenticação e resposta. As orientações gerais da REST or transferir estado representacional API or interface de programação do aplicativo (API) sobre chaves privadas do lado do servidor, corpos de resposta, erros e limites de frequência não se aplicam, a menos que um artigo da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos faça referência explícita a elas.

Use a documentação de endpoints da API or interface de programação do aplicativo (API) de envio de mensagens para dispositivos como fonte de verdade para campos de requisição, corpos de resposta, códigos de status e limites.