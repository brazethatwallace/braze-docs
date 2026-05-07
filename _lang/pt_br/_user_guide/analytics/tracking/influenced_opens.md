---
nav_title: Aberturas por influência
article_title: Aberturas por influência
page_order: 2
page_type: reference
description: "Este artigo de referência explica as aberturas por influência e como você pode rastreá-las para fornecer um nível mais rico de detalhes em suas campanhas push."
channel: push

---

# Aberturas por influência {#influenced-opens}

> Quando um usuário seleciona uma notificação por push e é direcionado para o seu app, a Braze registra isso como uma abertura direta. Quando os usuários não selecionam a notificação, mas ainda podem ser influenciados pela notificação por push, a Braze registra como uma abertura por influência. Isso fornece um nível mais rico de detalhes sobre o efeito das suas campanhas push.

## Como funciona {#how-it-works}

Em sua base, as aberturas por influência medem o número de usuários que abrem o app depois de receber uma notificação sem selecioná-la. Como não há nenhuma ação direta que vincule a notificação à abertura do app, uma abertura por influência é registrada se o usuário abrir o app menos de trinta minutos após receber a notificação por push ou menos da metade do tempo médio desde a última sessão do usuário.

Por exemplo, digamos que você envie uma notificação por push para os usuários do seu app. Se um usuário que normalmente abre o app 30 vezes por dia abrir seu app seis horas depois de receber o push, o push recebe pouco ou nenhum crédito por influenciar a abertura. No entanto, se um usuário que normalmente usa o app uma vez por mês abrir o app seis horas depois de receber o push, a abertura terá uma chance muito maior de ser contada como uma abertura por influência.

Isso difere da definição de aberturas de app como um evento de conversão para uma Campaign push. Para conversões, todas as aberturas dentro da janela de conversão serão atribuídas à Campaign. As aberturas por influência definem uma janela de tempo e crédito de atribuição com base no comportamento de um usuário individual.

## Visualização das aberturas por influência de uma Campaign {#viewing-a-campaigns-influenced-opens}

As aberturas por influência são adicionadas às aberturas diretas de uma Campaign para obter um número total de aberturas. Isso é exibido na página **Campaign Analytics** de uma Campaign push. O total de aberturas e as aberturas diretas são mostrados nas seções de desempenho da mensagem e **Desempenho histórico**. As aberturas por influência são a diferença entre as duas medidas.

![Estatísticas de aberturas por influência na página de detalhes da Campaign]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

Para saber mais sobre o rastreamento de aberturas, confira a seção de rastreamento de conversões de nossas [práticas recomendadas para push]({{site.baseurl}}/user_guide/channels/push/best_practices/).