---
nav_title: Setembro
page_order: 4
noindex: true
page_type: update
description: "Este artigo contém notas de versão de setembro de 2019."
---

# Setembro de 2019 {#september-2019}

## App da Braze no OneLogin {#braze-app-within-onelogin}

Os clientes poderão simplesmente pesquisar e selecionar a Braze no [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin/) para login iniciado por SP ou IdP. Isso significa que os clientes não precisarão adicionar um aplicativo personalizado no OneLogin. Como resultado, isso deve preencher previamente determinadas configurações, como atributos que vimos surgir desde o lançamento do SAML SSO.

## Parceria com a Rokt Calendar {#rokt-calendar-partnership}

A [Rokt Calendar]({{site.baseurl}}/partners/home/) oferece aos clientes da Braze a capacidade de alinhar suas iniciativas de marketing personalizado e estender o conteúdo personalizado ao calendário do usuário final. Dessa forma, a experiência do usuário final é mais fluida e desenvolve ainda mais a fidelidade aos serviços de nossos clientes. Os clientes poderão...

- Enviar um convite de calendário por meio da plataforma Braze para "salvar a data" e ampliar nossa comunicação
- Atualizar um convite existente se o conteúdo do evento tiver sido alterado.

## Parceria com a Passkit {#passkit-partnership}

Com a [Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit/), os clientes da Braze poderão expandir seu engajamento com o cliente para a carteira móvel. Eles poderão personalizar campanhas de carteira usando a poderosa segmentação da Braze e orquestrar junto com canais como push, mensagens no app e muito mais.

## Retorno do valor do dispatch ID por meio de endpoints de envio de mensagens {#dispatch-id-value-return-via-messaging-endpoints}

O `dispatch_id` de uma mensagem será incluído nas seguintes respostas dos endpoints de envio de mensagens:
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-API-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

Dessa forma, os clientes que usam envio de mensagens transacionais podem rastrear a chamada de volta por meio do Currents.

## Changelogs de Canvas {#canvas-changelogs}

Você já se perguntou sobre os detalhes de quem está trabalhando em um Canvas na sua conta? Não se pergunte mais! Agora você pode acessar os changelogs de Canvas.

![Changelogs de Canvas]({% image_buster /assets/img/canvas-changelog1.png %})
![Changelogs de Canvas]({% image_buster /assets/img/canvas-changelog2.png %})