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

Cartões baseados em ação, tanto em Campaigns quanto em Canvas, exigem processamento em segundo plano. A Braze precisa primeiro receber a notificação da ação de gatilho (como uma compra realizada ou o início de uma sessão) antes de criar um cartão para o usuário. Por isso, haverá um atraso antes que esses cartões fiquem disponíveis.

Cartões baseados em ação adicionam complexidade ao seu aplicativo, pois você pode acabar fazendo consultas e atualizações contínuas enquanto espera o cartão ficar disponível. Em vez disso, configure seu cartão como `Scheduled Entry`, que funcionará como uma janela de disponibilidade para que o cartão esteja sempre disponível para o público-alvo.

Se você agendar seus cartões com antecedência, eles estarão prontos, esperando o usuário abrir o app e solicitar os cartões.

## Use a lógica de envio "At First Impression" {#use-at-first-impression-send-logic}

Junto com envios agendados, a opção `At First Impression` evita latência por conta da velocidade com que um cartão é criado e armazenado na Braze. A opção `At Campaign Launch` cria todos os cartões para todos os usuários segmentados com antecedência, o que pode levar tempo para ser concluído. Já a opção `At First Impression` gera um cartão para o usuário na primeira vez que ele é solicitado, como quando o usuário abre o app pela primeira vez.

Isso significa que, junto com a entrada agendada, os cartões estarão disponíveis imediatamente, assim que você precisar deles, seja no início da sessão ou em uma janela de elegibilidade baseada em tempo.

## Lembre-se de que a entrada no Canvas é um pré-requisito para receber cartões {#remember-that-canvas-entry-is-a-prerequisite-for-receiving-cards}

Ao usar Canvas, lembre-se de que o usuário precisa primeiro entrar no Canvas com base nos critérios de entrada configurados e, *depois*, precisa passar pela etapa de mensagem de cartão de conteúdo. Somente então o cartão ficará disponível para o seu app ou site. Tenha em mente que existe uma latência embutida para a criação do cartão depois que o usuário passa pela etapa, o que pode atrasar a disponibilidade do cartão.

## Não atualize os cartões excessivamente {#dont-refresh-cards-excessively}

Os Content Cards são atualizados automaticamente pelo SDK or kit de desenvolvimento de software a cada início de nova sessão. Você também pode solicitar manualmente uma atualização dos Content Cards a qualquer momento durante uma sessão ativa.

Chamar o método `requestContentCardsRefresh` e atualizar com muita frequência pode levar a um limite de taxa. Se o seu app for temporariamente limitado, talvez você não consiga atualizar os cartões quando precisar ou em um momento crítico do engajamento do usuário com o app.

Para evitar que isso aconteça, chame esse método de atualização apenas em momentos importantes do ciclo de vida do usuário, como após uma compra ou após o usuário fazer upgrade do nível de inscrição.

## Evite incluir Conteúdo conectado {#avoid-including-connected-content}

O Conteúdo conectado enriquece os Content Cards com dados de APIs próprias ou de terceiros. No entanto, quando incluído em uma mensagem de cartão de conteúdo, ele bloqueia a disponibilidade do cartão até que a requisição de rede do Conteúdo conectado seja concluída. Em alguns casos, isso faz com que os SDKs tentem novamente alguns segundos depois, para não atrasar a lógica de renderização do app, que pode estar aguardando o SDK or kit de desenvolvimento de software concluir a tarefa de atualização.

Se você precisar usar Conteúdo conectado, agende esses cartões com antecedência e use a opção `At Campaign Launch` para que os cartões sejam pré-criados antes da próxima sessão do usuário. Observe que esses cartões não ficarão disponíveis imediatamente, pois a Braze precisa gravar todos os cartões para todos os usuários elegíveis.