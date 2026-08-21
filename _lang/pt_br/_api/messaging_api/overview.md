---
nav_title: Visão geral
article_title: Visão geral da API de envio de mensagens
page_order: 0
page_type: reference
description: "Saiba mais sobre a API de envio de mensagens da Braze e seus recursos em acesso antecipado."
hidden: true
---

# Visão geral da API de envio de mensagens {#messaging-api-overview}

A API de envio de mensagens da Braze é um conjunto de endpoints REST para integrar os recursos de envio de mensagens da Braze sem um SDK da Braze. Você pode chamar esses endpoints a partir de aplicações cliente ou servidor.

{% alert important %}
Esta página está em beta. Os recursos e a documentação da API de envio de mensagens estão sujeitos a alterações. Entre em contato com o gerente da sua conta Braze para solicitar acesso.
{% endalert %}

## Recursos compatíveis {#supported-capabilities}

Durante o acesso antecipado, você pode usar a API de envio de mensagens para:

- [Recuperar Banners elegíveis]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_sync_banners) para um ID de usuário externo e um conjunto de posicionamentos
- [Reportar eventos de impressão e clique de Banner]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_track_banner_events)

A API de envio de mensagens retorna propriedades estruturadas de Banner para que você possa construir uma interface personalizada. Ela não retorna HTML renderizado.

## Requisitos de integração {#integration-requirements}

Para integrar a API de envio de mensagens, você precisa de:

- Um espaço de trabalho com a API de envio de mensagens ativada
- Uma chave da API REST do lado do cliente para esse espaço de trabalho
- O endpoint REST para esse espaço de trabalho
- O ID de usuário externo do usuário
- O identificador de API do app

Para saber mais sobre credenciais, consulte [Autenticação e segurança]({{site.baseurl}}/api/messaging_api/authentication).

## Orientações sobre a API de envio de mensagens e a REST API {#messaging-api-and-rest-api-guidance}

A API de envio de mensagens usa os mesmos endpoints REST regionais que a REST API da Braze, mas possui um contrato de autenticação e resposta separado. As orientações gerais da REST API sobre chaves privadas do lado do servidor, corpos de resposta, erros e limites de frequência não se aplicam, a menos que um artigo da API de envio de mensagens faça referência explícita a elas.

Use a documentação de endpoints da API de envio de mensagens como fonte de verdade para campos de requisição, corpos de resposta, códigos de status e limites.