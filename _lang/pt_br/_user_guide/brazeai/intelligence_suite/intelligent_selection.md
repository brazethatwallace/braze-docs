---
nav_title: Seleção inteligente
article_title: Seleção inteligente
page_order: 1.0
description: "Este artigo aborda a Seleção inteligente, um recurso que analisa o desempenho de uma campanha recorrente ou do Canvas duas vezes por dia e ajusta automaticamente a porcentagem de usuários que recebem cada variante de mensagem."
search_rank: 10
toc_headers: h2
---

# Seleção inteligente {#intelligent-selection}

> A Seleção inteligente é um recurso que analisa o desempenho de uma Campaign recorrente ou do Canvas duas vezes por dia e ajusta automaticamente a porcentagem de usuários que recebem cada variante de mensagem.

## Pré-requisitos {#prerequisites}

{% tabs %}
{% tab Campaign %}
Antes de adicionar a Seleção inteligente à sua Campaign, certifique-se de que tudo está configurado corretamente:

- Sua Campaign é enviada em um cronograma recorrente. Campaigns de envio único não são compatíveis.
- Você adicionou pelo menos duas variantes de mensagem.
- Você definiu um evento de conversão para medir o desempenho entre as variantes.
- A janela de reelegibilidade está definida para 24 horas ou mais. Janelas mais curtas não são compatíveis, pois afetariam a integridade da variante de controle. Para saber mais, consulte [esta FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endtab %}

{% tab Canvas %}
Para usar a Seleção inteligente em um Canvas, confirme o seguinte:
- Seu Canvas inclui pelo menos duas variantes de mensagem em uma etapa de Mensagem.
- Você adicionou pelo menos um evento de conversão.
{% endtab %}
{% endtabs %}

## Sobre a Seleção inteligente {#about-intelligent-selection}

Uma variante que pareça ter um desempenho melhor do que outras será enviada a mais usuários, enquanto as variantes com desempenho inferior serão direcionadas a menos usuários. Cada ajuste é feito usando um [algoritmo estatístico](https://en.wikipedia.org/wiki/Multi-armed_bandit) que garante que a Braze está ajustando para diferenças reais de desempenho e não apenas por acaso.

![Seção de testes A/B de uma Campaign com a Seleção inteligente ativada.]({% image_buster /assets/img/intelligent_selection1.png %})

A Seleção inteligente irá:
- Examinar repetidamente os dados de desempenho e mudar gradualmente o tráfego da Campaign para as variantes vencedoras.
- Verificar se mais usuários recebem sua variante de melhor desempenho sem sacrificar a confiança estatística.
- Excluir as variantes de baixo desempenho e identificar as variantes de alto desempenho mais rapidamente do que em um [teste A/B tradicional]({{site.baseurl}}/user_guide/messaging/ab_testing).
- Testar com mais frequência e com mais confiança de que seus usuários verão sua melhor mensagem.

A Seleção inteligente funciona melhor para Campaigns que enviam mais de uma vez. Ela precisa de dados de desempenho iniciais para começar a otimizar, então Campaigns de envio único não se beneficiarão. Para essas Campaigns, recomendamos usar um [teste A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) tradicional.


Você pode adicionar a Seleção inteligente às suas Campaigns e Canvas.

{% tabs %}
{% tab Campaign %}
A Seleção inteligente pode ser adicionada a qualquer Campaign de múltiplos envios na etapa **Público-alvo** do criador de Campaigns da Braze. Campaigns que enviam apenas uma vez não podem aproveitar esse recurso.

{% alert note %}
A Seleção inteligente não pode ser usada em Campaigns com um período de reelegibilidade de menos de 24 horas, pois isso afetaria a integridade da variante de controle. Para saber mais, consulte [FAQ de Inteligência]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}

{% tab Canvas %}
Adicione pelo menos um evento de conversão e duas variantes ao seu Canvas. Em seguida, selecione uma das porcentagens de variante na etapa de Construção.

![Um Canvas com duas variantes, cada uma definida com 50% de distribuição de variantes, permitindo que a Seleção inteligente seja ativada.]({% image_buster /assets/img/intelligent_selection.png %})

Isso permite que você edite a distribuição de variantes e ative a Seleção inteligente.

![Opção de Seleção inteligente ativada para um Canvas]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

A Seleção inteligente não estará disponível se você ainda não tiver adicionado eventos de conversão ao seu Canvas ou se seu Canvas for composto de uma única variante.

{% alert note %}
Canvas pode usar a Seleção inteligente com reelegibilidade ativada, mas a Braze não pode garantir que um usuário receba a mesma variante ao reentrar, pois a alocação ideal muda ao longo do tempo. Campaigns exigem uma janela de reelegibilidade de 24 horas ou mais quando a Seleção inteligente está ativada. Para saber mais, consulte [Por que a reelegibilidade em menos de 24 horas não está disponível quando combinada com a Seleção inteligente?](#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}
{% endtabs %}

## Tempo de execução {#run-time}

Para Campaigns e Canvas, a Seleção inteligente será executada até reunir evidências suficientes sobre as taxas de conversão "verdadeiras" das variantes. O "suficiente" é determinado por uma métrica especial chamada "arrependimento". Você pode pensar nisso como algo semelhante ao intervalo de confiança, pois a Seleção inteligente será desativada quando houver dados suficientes para saber qual é a melhor variante.

Na maioria dos casos, a Seleção inteligente escolherá uma das variantes como a variante vencedora. Essa variante receberá 100% do público para envios futuros.

{% alert note %}
É possível que a Seleção inteligente pare de otimizar sem escolher um único vencedor claro. A Seleção inteligente interrompe a otimização quando tem 95% de confiança de que a continuação do experimento não melhorará a taxa de conversão em mais de 1% da taxa atual.
{% endalert %}

## Distribuição de variantes da Seleção inteligente {#intelligent-selection-variant-distribution}

A Seleção inteligente baseia sua distribuição de variantes no status atual das conversões da Campaign. Ela só determina as distribuições finais após o período de treinamento.

Isso significa que, durante as fases iniciais da Campaign, tanto as seleções inteligentes de 99% quanto de 1% podem receber envios aproximadamente iguais, mas as porcentagens finais para alocação de variantes podem ser definidas em 99%—1%.

Se você não quiser que a Seleção inteligente envie 50/50 durante as fases iniciais da Campaign, recomendamos usar um teste A/B tradicional com variantes fixas.

## Perguntas frequentes {#faq}

### Por que a reelegibilidade em menos de 24 horas não está disponível quando combinada com a Seleção inteligente? {#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection}

Não permitimos que Campaigns com Seleção inteligente tenham reelegibilidade em um período muito curto, pois isso afetaria a integridade da variante de controle. Ao criar um intervalo de 24 horas, ajudamos a garantir que o algoritmo tenha um conjunto de dados estatisticamente válido para trabalhar.

Normalmente, Campaigns com reelegibilidade farão com que os usuários entrem novamente na mesma variante que receberam antes. Com a Seleção inteligente, a Braze não pode garantir que um usuário receberá a mesma variante de Campaign, porque a distribuição de variantes teria mudado devido ao aspecto de alocação ideal desse recurso. Se o usuário pudesse entrar novamente antes de a Seleção inteligente reexaminar o desempenho da variante, os dados poderiam ser distorcidos por causa dos usuários que reentraram.

Por exemplo, se uma Campaign estiver usando estas variantes:

- Variante A: 20%
- Variante B: 20%
- Controle: 60%

Então, a distribuição de variantes poderia ser a seguinte para a segunda rodada:

- Variante A: 15%
- Variante B: 25%
- Controle: 60%

### Por que minhas variantes da Seleção inteligente estão mostrando envios iguais durante os estágios iniciais da minha Campaign? {#why-are-my-intelligent-selection-variants-showing-equal-sends-during-the-early-stages-of-my-campaign}

A Seleção inteligente aloca variantes para envio com base no status atual da conversão da Campaign. Ela só determina as alocações finais de variantes após um período de treinamento, em que os envios são feitos de forma homogênea entre as variantes. Se não quiser que a Seleção inteligente envie uniformemente durante os estágios iniciais da sua Campaign, use variantes fixas para um teste A/B tradicional.

### A Seleção inteligente deixará de otimizar sem escolher um vencedor claro? {#will-intelligent-selection-stop-optimizing-without-picking-a-clear-winner}

A Seleção inteligente interromperá a otimização quando tiver 95% de confiança de que a continuação do experimento não melhorará a taxa de conversão em mais de 1% da taxa atual.

### Por que não consigo ativar a Seleção inteligente no meu Canvas ou na minha Campaign (opção acinzentada)? {#why-cant-i-enable-intelligent-selection-in-my-canvas-or-campaign-grayed-out}

A Seleção inteligente não estará disponível se:

- Você não adicionou eventos de conversão à sua Campaign ou ao Canvas
- Você está criando uma Campaign de envio único
- Sua Campaign tem reelegibilidade ativada com uma janela de menos de 24 horas
- Seu Canvas é composto por uma única variante, sem variantes adicionais ou grupos de controle adicionados
- Seu Canvas é composto por um único grupo de controle, sem variantes adicionadas