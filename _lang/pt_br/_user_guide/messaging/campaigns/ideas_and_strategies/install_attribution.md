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

# Entendendo as instalações de usuários

> O rastreamento de atribuição da instalação é uma ótima maneira de melhorar o relacionamento inicial com seus usuários. Saber como, onde e, mais importante ainda, por que um usuário instala seu app permite que você entenda melhor quem é esse usuário e como apresentá-lo ao seu app.

Embora a Braze não ofereça rastreamento de atribuição da instalação, é possível fazer a integração com [serviços]({{site.baseurl}}/partners/message_orchestration/) como Branch e AppsFlyer para fornecer dados de instalação de forma integrada.

## Segmente seus usuários

Assim que o usuário instalar seu app, você pode começar a segmentá-lo com base nos seguintes [filtros de atribuição da instalação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#install-attribution). Por exemplo, um app de viagens poderia adicionar usuários que vieram de um anúncio sobre ofertas de férias na praia a um segmento "Amantes de Praia". Da mesma forma, um app de música poderia segmentar usuários com base no gênero musical exibido no anúncio que levou à instalação.

## Práticas recomendadas

### Integração personalizada

Agora que você tem mais informações sobre o usuário, é possível personalizar o processo de integração dele. Isso pode ser tão simples quanto alterar as imagens nas suas mensagens para se adequar às preferências do usuário, ou tão complexo quanto criar uma integração única para cada anúncio que possa levar a uma instalação. Para escalar uma sequência completa de mensagens que leve em consideração o comportamento do usuário, consulte nossa documentação sobre [Canvas]({{site.baseurl}}/developer_guide/rest_api/messaging/#canvas).

### Dados de referência do anúncio

Os usuários podem ser atraídos para o seu app por uma oferta promocional ou brinde. Usar dados de atribuição da instalação permite que você envie campanhas com códigos de desconto ou ofertas apenas para os usuários que instalaram o app por causa dessas promoções. De forma semelhante, se o seu anúncio contém informações sobre um produto específico (como um filme específico em um app de vídeo ou uma promoção em um app de eCommerce), você pode enviar campanhas direcionando os usuários para a página correta do seu app.

## Avalie os esforços de publicidade

Os dados de atribuição da instalação podem ser valiosos para avaliar a eficácia de diferentes campanhas de marketing. Analise quais anúncios e campanhas estão gerando mais instalações e quais estão ficando para trás. Assim, você pode concentrar seus recursos nos anúncios mais eficazes.