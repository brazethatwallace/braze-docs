---
nav_title: Melhorar a baixa latência
article_title: Melhorar a baixa latência para Content Cards como banners
page_order: 10
description: "Este artigo aborda estratégias para garantir que os requisitos de baixa latência sejam atendidos com Content Cards."
channel:
  - content cards
---

# Melhorar a latência para Content Cards como banners {#improve-latency-for-content-cards-as-banners}

> Se você está enfrentando latência na sua implementação de Content Cards para casos de uso críticos, como banners na página inicial, confira esta página para conhecer estratégias e dicas que ajudam a resolver e acelerar a renderização.

{% alert tip %}
Você quer exibir banners personalizados e em destaque no seu app ou site? Experimente os [Banners]({{site.baseurl}}/user_guide/channels/banners), que foram criados para dar suporte a casos de uso de banners com baixa latência.
{% endalert %}

## Use entrada agendada em vez de entrada baseada em ação {#use-scheduled-entry-instead-of-action-based-entry}

Cartões baseados em ação, tanto em Campaigns quanto em Canvas, exigem processamento em segundo plano. A Braze precisa primeiro receber a notificação da ação de disparo (como uma compra realizada ou uma sessão iniciada) antes de criar um cartão para o usuário. Por isso, haverá um atraso até que esses cartões fiquem disponíveis.

Cartões baseados em ação adicionam complexidade ao seu aplicativo, pois você pode acabar precisando fazer polling e atualização contínuos enquanto espera o cartão ficar disponível. Em vez disso, configure seu cartão como `Scheduled Entry`, que funcionará como uma janela de disponibilidade para que o cartão esteja sempre disponível para o público-alvo.

Se você agendar seus cartões com antecedência, eles estarão prontos, esperando o usuário abrir o app e solicitar os cartões.

## Use a lógica de envio "At First Impression" {#use-at-first-impression-send-logic}

Junto com envios agendados, a opção `At First Impression` evita latência por conta da velocidade com que um cartão é criado e armazenado na Braze. A opção `At Campaign Launch` cria todos os cartões para todos os usuários segmentados antecipadamente, o que pode levar tempo para ser concluído. A opção `At First Impression` gera um cartão para o usuário na primeira vez em que ele é solicitado, como quando o usuário abre o app pela primeira vez.

Isso significa que, junto com a entrada agendada, os cartões ficam disponíveis imediatamente, assim que você precisar deles, seja no início da sessão ou em uma janela de elegibilidade baseada em tempo.

## Lembre-se de que a entrada no Canvas é um pré-requisito para receber cartões {#remember-that-canvas-entry-is-a-prerequisite-for-receiving-cards}

Ao usar o Canvas, lembre-se de que o usuário precisa primeiro entrar no Canvas com base nos critérios de entrada configurados e, *em seguida*, deve passar pela etapa de mensagem de Content Cards. Só então o cartão estará disponível para o seu app ou website. Lembre-se de que há uma latência integrada para o cartão ser criado depois que o usuário passa pela etapa, o que pode atrasar a disponibilidade do cartão.

## Não atualize os cartões excessivamente {#dont-refresh-cards-excessively}

Os Content Cards são atualizados automaticamente pelo SDK a cada início de nova sessão. Você também pode solicitar manualmente uma atualização dos Content Cards a qualquer momento durante uma sessão ativa. Em versões compatíveis do SDK, a Braze envia atualizações e remoções para o dispositivo durante a sessão por meio da [entrega em tempo real]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#real-time-delivery), o que reduz a necessidade de atualizar manualmente.

Chamar o método `requestContentCardsRefresh` e atualizar com muita frequência pode levar a um limite de frequência. Se o seu app for temporariamente limitado, talvez você não consiga atualizar os cartões quando precisar ou em um momento crítico do engajamento do usuário com o seu app.

Para evitar que isso aconteça, chame esse método de atualização apenas em momentos importantes do ciclo de vida do usuário, como depois que um usuário faz uma compra ou após fazer upgrade do nível de inscrição.

## Evite incluir Connected Content {#avoid-including-connected-content}

O Connected Content enriquece os Content Cards com dados de APIs próprias ou de terceiros. No entanto, quando incluído em uma mensagem de cartão de conteúdo, ele bloqueia a disponibilidade do cartão até que a solicitação de rede do Connected Content seja concluída. Em alguns casos, isso faz com que os SDKs tentem novamente alguns segundos depois, em um esforço para não atrasar a lógica de renderização do seu app, que pode aguardar o SDK concluir sua tarefa de atualização.

Se você precisar usar Connected Content, agende esses cartões com antecedência e use a opção `At Campaign Launch` para que os cartões sejam pré-criados antes da próxima sessão do usuário. Observe que esses cartões não estarão disponíveis imediatamente, pois a Braze grava todos os cartões para todos os usuários elegíveis.