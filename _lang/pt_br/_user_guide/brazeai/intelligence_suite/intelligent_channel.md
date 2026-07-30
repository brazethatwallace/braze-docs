---
nav_title: Filtro de canal
article_title: Filtro Canal Inteligente
page_order: 1.5
description: "Este artigo aborda o filtro Canal Inteligente, que seleciona a parte do seu público para a qual o canal de envio de mensagens selecionado é o melhor canal. Neste caso, \"melhor\" significa \"tem a maior probabilidade de engajamento, dado o histórico do usuário\"."
search_rank: 11
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Filtro Canal Inteligente {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommost-engaged-channel-stylefloatrightwidth120pxborder0-classnoimgborderintelligent-channel-filter}

> O filtro `Intelligent Channel` (anteriormente `Most Engaged`) seleciona a parte do seu público para quem o canal de envio de mensagens selecionado é o "melhor" canal.

## Sobre o filtro {#about-the-filter}

![O filtro Intelligent Channel com um menu suspenso para os diferentes canais que podem ser selecionados.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

Neste caso, "melhor" significa que o canal tem a maior probabilidade de engajamento, dado o histórico do usuário. Você pode selecionar e-mail, SMS, WhatsApp, web push ou mobile push (incluindo qualquer sistema operacional ou dispositivo móvel disponível) como canal.

O Canal Inteligente calcula uma taxa de engajamento para cada usuário em cada canal compatível, classifica esses canais e trata o canal com a classificação mais alta como o melhor canal daquele usuário.

Para ativar o filtro Canal Inteligente, selecione o filtro **Intelligent Channel** na página **Público-alvo** ao criar uma Campaign ou Canvas.

## Como o engajamento é calculado por canal {#how-engagement-is-calculated-by-channel}

O Canal Inteligente compara canais usando uma taxa de engajamento: o número de interações com mensagens dividido pelo número de mensagens recebidas. A Braze avalia até as últimas 100 mensagens recebidas por canal nos últimos seis meses.

Toda vez que uma mensagem é enviada a um usuário ou que um usuário interage com uma mensagem, a taxa de engajamento é recalculada em segundos. Um usuário só pode ser contado como tendo interagido com uma mensagem uma vez (por exemplo, uma abertura e um clique no mesmo e-mail fazem com que essa mensagem seja marcada como tendo sido engajada apenas uma vez, não duas).

### Dados de interação por canal {#interaction-data-by-channel}

A Braze rastreia os seguintes eventos ao calcular as taxas de engajamento:

- **E-mail:** Aberturas ([aberturas por máquina]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) excluídas). Cliques em e-mail não são incluídos.
- **Mobile push:** Aberturas Diretas. Cada plataforma móvel (como iOS, Android e Kindle) é pontuada separadamente. Aberturas por Influência de push não são incluídas.
- **Web push:** Aberturas
- **SMS:** Cliques em links encurtados
- **WhatsApp:** Leituras de mensagens ou cliques em links rastreados

Aberturas por Influência de push, cliques em e-mail e atividade de sessão não são usados pelo Canal Inteligente. A atividade de sessão é usada pelo [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#about-intelligent-timing).

O Canal Inteligente não oferece suporte a webhooks, LINE, Kakao Talk, In-App Messages ou Content Cards.

{% alert important %}
Para calcular a taxa de engajamento do canal de SMS, ative o [encurtamento de links de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) com rastreamento avançado e rastreamento de cliques. Sem esse rastreamento, o SMS pode ser selecionado como o Canal Inteligente com uma taxa de engajamento de 0% devido ao nosso [comportamento de desempate]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#tie-breaking).
{% endalert %}

## Dados insuficientes {#not-enough-data}

Para que a Braze determine qual canal é o "melhor", é necessário que haja dados suficientes. Isso significa que um usuário deve ter recebido pelo menos três ou mais mensagens em um canal antes que esse canal possa ser classificado, e deve ter dados suficientes em pelo menos dois canais compatíveis.

Se os usuários não tiverem recebido mensagens suficientes nos canais, eles serão enquadrados na opção "Dados insuficientes" desse filtro. Isso permite que você use qualquer canal de envio de mensagens compatível para direcionar esses usuários.

Por exemplo, suponha que você queira que os usuários que preferem push recebam um push e que os usuários que não têm dados suficientes recebam a mesma mensagem push. Nesse caso, você poderia definir o filtro do Canal Inteligente como **Mobile push** e usar **OR** para adicionar um segundo filtro de Canal Inteligente definido como **Not Enough Data**. Uma Campaign separada com o filtro de Canal Inteligente definido como e-mail poderia abordar os usuários que preferem e-mail.

![Filtros de Canal Inteligente para mobile push ou dados insuficientes.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Campaigns e etapas do Canvas que ignoram o [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules) não são contabilizadas pelo Canal Inteligente e não podem contribuir para os requisitos de dados.
{% endalert %}

## Mobile push {#mobile-push}

O mobile push incorpora Android, iOS, Kindle e outros canais de dispositivos móveis disponíveis na Braze. A Braze pontua cada plataforma móvel separadamente ao calcular as taxas de engajamento.

Quando você usa o filtro Canal Inteligente definido como **Mobile push**, um usuário corresponde se iOS push ou Android push for o canal com a classificação mais alta. Isso não força o usuário a receber notificações por push em um dispositivo específico. A classificação é usada apenas para determinar se o mobile push é o melhor canal daquele usuário em comparação com e-mail, web push, SMS e WhatsApp.

## Filtro de probabilidade de abertura de mensagem para canais individuais {#individual-channels}

Em vez de deixar a Braze escolher o único melhor canal para um usuário, você pode usar o [filtro de segmentação "Probabilidade de abertura de mensagem"]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) para filtrar usuários com base na probabilidade de abrirem uma mensagem em um canal específico que você escolher. Esse filtro é calculado pela porcentagem de interações dividida pelo total de mensagens recebidas nas últimas 100 mensagens enviadas por canal.

A Probabilidade de abertura de mensagem usa os mesmos dados de engajamento subjacentes do Canal Inteligente, mas permite que você defina um limite para um único canal em vez de selecionar o melhor canal do usuário. Está disponível para e-mail, mobile push, SMS e web push.

Observe que um usuário deve ter recebido pelo menos três mensagens em um canal específico antes de poder ter uma pontuação de probabilidade para esse canal. Usuários sem dados suficientes para medir a probabilidade de um canal podem ser selecionados usando "está em branco."

## Práticas recomendadas e estratégia de uso eficaz {#best-practices-and-effective-use-strategy}

### Desempate {#tie-breaking}

Como alguns usuários recebem um número baixo de mensagens, não é incomum haver empates nas taxas de engajamento entre os canais disponíveis para um determinado usuário (por exemplo, um único usuário pode ter uma taxa de engajamento de 20% tanto para e-mail quanto para mobile push). Nesses casos, os empates são desfeitos priorizando (dando uma classificação mais alta) o canal com os eventos de interação mais recentes.

Se os canais empatados tiverem uma taxa de engajamento de 0%, a Braze desfaz o empate usando o canal com a mensagem recebida mais recente.

### Canais inacessíveis {#unreachable-channels}

Um usuário pode ter dados suficientes para que a Braze determine uma classificação de canais, mas depois se tornar inacessível em seu canal de maior classificação. Por exemplo, um usuário cujo melhor canal histórico é e-mail pode ter cancelado recentemente a inscrição de e-mail. Se você enviar uma mensagem nesse canal, ela não será entregue a esse usuário. Usuários que não podem ser alcançados em canais específicos devem ser direcionados ou encaminhados separadamente.

### Dimensionamento do público {#audience-sizing}

O Canal Inteligente permite o direcionamento antecipado e seletivo da fração de usuários que têm uma probabilidade muito maior de engajamento com uma mensagem do que o restante do seu público. Não é provável que isso represente a maioria dos usuários de um público típico. Em vez disso, espere que esse filtro encontre os 5 a 20% do seu público habitual que têm um histórico estabelecido de engajamento em um determinado canal.