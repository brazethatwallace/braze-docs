---
nav_title: Entendendo as instalações de usuários
article_title: Entendendo as instalações de usuários
page_order: 7
page_type: reference
description: "Este artigo de referência descreve as instalações de usuários (rastreamento de atribuição da instalação) e diferentes formas de aplicar essas informações nas suas campanhas."
tool:
  - Campaigns
  - Segments
---

# Entendendo as instalações de usuários {#understanding-user-installs}

> O rastreamento de atribuição da instalação é uma ótima maneira de melhorar o relacionamento inicial com seus usuários. Saber como, onde e, mais importante ainda, por que um usuário instala seu app permite que você entenda melhor quem é esse usuário e como apresentá-lo ao seu app.

Embora a Braze não ofereça rastreamento de atribuição da instalação, é possível fazer a integração com [serviços]({{site.baseurl}}/partners/message_orchestration) como Branch e AppsFlyer para fornecer dados de instalação de forma integrada.

## Segmente seus usuários {#segment-your-users}

Depois que o usuário instalar seu app, você pode começar a segmentá-lo com base nos seguintes [filtros de instalar atribuição]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#install-attribution). Por exemplo, um app de viagens poderia adicionar usuários que vieram de um anúncio relacionado a ofertas de férias na praia a um Segment "Beach Lovers". Da mesma forma, um app de música poderia segmentar usuários com base no gênero musical exibido no anúncio que levou à instalação.

## Práticas recomendadas {#best-practices}

### Integração personalizada {#personalized-onboarding}

Agora que você tem mais informações sobre o usuário, pode personalizar o processo de integração dele. Isso pode ser tão simples quanto alterar as imagens nas suas mensagens para se adequar às preferências dele, ou tão complexo quanto criar uma integração de usuário única para cada anúncio que possa levar a uma instalação. Para escalar uma sequência completa de mensagens que leve o comportamento do usuário em consideração, consulte nossa documentação sobre [Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

### Dados de referência do anúncio {#reference-data-from-the-ad}

Os usuários podem ser atraídos para o seu app por uma oferta promocional ou sorteio. Usar dados de atribuição de instalação permite que você envie Campaigns contendo códigos de desconto ou ofertas apenas para os usuários que instalaram o app por causa dessas promoções. De forma semelhante, se o seu anúncio contém informações sobre um produto específico (como um filme específico em um app de vídeo ou uma promoção em um app de eCommerce), você pode enviar Campaigns direcionando os usuários para a página correta do seu app.

## Avalie os esforços de publicidade {#evaluate-advertising-efforts}

Os dados de atribuição de instalação podem ser valiosos para avaliar a eficácia de diferentes campanhas de marketing. Analisar quais anúncios e campanhas estão gerando mais instalações e quais estão ficando para trás pode ajudar você a concentrar seus recursos nos anúncios mais eficientes.