---
nav_title: Seleção de Variante
article_title: Seleção de Variante
page_order: 1.6
description: "Este artigo aborda a Seleção de Variante BrazeAI<sup>TM</sup>, um recurso que permite que suas campanhas A/B otimizem automaticamente para o melhor engajamento."
search_rank: 10
toc_headers: h2
---

# Seleção de Variante BrazeAI<sup>TM</sup> {#variant-selection}

> A Seleção de Variante BrazeAI<sup>TM</sup> é um recurso que permite que seus testes A/B de envio único ou recorrentes executem automaticamente um experimento e otimizem para os melhores resultados de engajamento.

{% alert note %}
A Seleção de Variante BrazeAI<sup>TM</sup> está disponível atualmente apenas para push.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar a Seleção de Variante BrazeAI<sup>TM</sup>, você precisa do seguinte na sua Campaign ou Canvas:

{% tabs %}
{% tab Campaign %}
- Adicione pelo menos duas variantes de mensagem.
- Se você não estiver usando envio único, defina pelo menos um evento de conversão e configure seu período de reelegibilidade para 24 horas ou mais. Períodos mais curtos não são compatíveis, pois afetariam a integridade da variante de controle.
{% endtab %}

{% tab Canvas %}
- Inclua pelo menos duas variantes de mensagem em uma etapa de Mensagem.
- Se você não estiver usando envio único, tenha pelo menos um evento de conversão.
{% endtab %}
{% endtabs %}

## Envio único {#single-send}

Depois que você adicionar sua segunda variante, a Seleção de Variante BrazeAI<sup>TM</sup> é ativada automaticamente, definindo parâmetros ideais para o experimento (observamos uma melhoria de ~25% ao seguir os parâmetros ideais), executa seu experimento e então envia a variante vencedora. Você não precisa fazer mais nada.

Para personalizar seu experimento, oferecemos as seguintes opções de personalização:

### Meta de otimização {#optimization-goal}

Recomendamos usar aberturas, a menos que você tenha uma configuração sólida de evento de conversão com uma quantidade significativa de conversões, para que o algoritmo tenha os dados necessários para fornecer os melhores resultados.
- Aberturas
- Eventos de conversão

### Duração do experimento {#experiment-duration}

Recomendamos usar o padrão; no entanto, oferecemos duas outras opções, incluindo a possibilidade de usar sua própria duração personalizada:
- 4 horas
- 24 horas
- 72 horas
- Personalizado

### Grupo de controle e distribuições de variantes {#control-group-and-variant-distributions}

Você pode remover um grupo de controle ou editar as distribuições de variantes, mas recomendamos usar os parâmetros ideais que definimos.

![Opções de otimização de variante para envio único]({% image_buster /assets/img_archive/braze_ai_variant_selection_single_send_options.png %})

## Recorrente {#recurring}

Depois que você adicionar sua segunda variante, a Seleção de Variante BrazeAI<sup>TM</sup> é ativada automaticamente e otimiza continuamente usando um teste estatístico multi-armed bandit. Ela envia mais mensagens para as variantes com melhor desempenho e menos para aquelas com pior desempenho.

Começa com uma distribuição uniforme para treinar e otimizar, e então duas vezes por dia ajusta a distribuição em favor das variantes de alto desempenho e contra as de baixo desempenho, até reunir evidências suficientes para ter confiança (95%+) de que escolheu a distribuição ideal.

## Relatórios {#reporting}

![Relatório de melhoria]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Após a conclusão do teste para envio único, e após um breve intervalo para envio recorrente, temos dados confiáveis para reportar. Reportamos qualquer melhoria que a Seleção de Variante BrazeAI<sup>TM</sup> conseguiu alcançar no dashboard.

{% tabs %}
{% tab Envio único %}
Após o envio da coorte de treinamento, a Braze aguarda o período definido na configuração de duração e analisa os dados. Com base na distribuição das variantes concorrentes, calculamos uma média de como seria o desempenho se nenhuma otimização fosse feita, e então calculamos a melhoria com base na variante vencedora.

Por exemplo (assumindo uma distribuição uniforme):
- Variante 1: 3,5%
- Variante 2: 3%
- Variante 3: 2,5%
- Variante 4: 2%

A taxa de abertura sem otimização é 2,75% (0,035*0,25 + 0,03*0,25 + 0,025*0,25 + 0,02*0,25). A Seleção de Variante escolhe a Variante 1, 3,5%, então a melhoria é de 27,3%.
{% endtab %}

{% tab Recorrente %}
A Braze analisa rotineiramente os resultados quando fazemos ajustes e mostra a melhoria com base na média da melhoria de cada período.

Calculamos a melhoria do período com base em quanto ajustamos, de forma semelhante ao envio único.

Por exemplo:
- Variante 1: 3,5%, 25% da coorte
- Variante 2: 3%, 25% da coorte
- Variante 3: 2,5%, 25% da coorte
- Variante 4: 2%, 25% da coorte

A taxa de abertura sem otimização é 2,75% (0,035*0,25 + 0,03*0,25 + 0,025*0,25 + 0,02*0,25). A Seleção de Variante dá mais peso às variantes de melhor desempenho.

Digamos que ela faça o seguinte:
- Variante 1: 65%
- Variante 2: 15%
- Variante 3: 10%
- Variante 4: 5%

Isso equivale a uma taxa de abertura escolhida de 3,075% (0,035*0,65 + 0,03*0,15 + 0,025*0,1 + 0,02*0,05), o que representa uma melhoria de 11,8%. Calculamos isso a cada período e então fazemos a média ao longo de todo o período de otimização.
{% endtab %}
{% endtabs %}

## Perguntas frequentes {#faq}

### Por que a reelegibilidade em menos de 24 horas não está disponível quando combinada com a Seleção de Variante para Campaigns ou Canvas recorrentes? {#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-variant-selection-for-recurring-campaigns-or-canvases}

Não permitimos que Campaigns com Seleção de Variante tenham reelegibilidade em um período muito curto porque nossos testes mostram que isso afeta a integridade da variante de controle e pode levar a distribuições indesejáveis.

### Por que minhas variantes estão mostrando envios iguais durante os estágios iniciais da minha Campaign recorrente? {#why-are-my-variants-showing-equal-sends-during-the-early-stages-of-my-recurring-campaign}

A Seleção de Variante só determina as alocações finais de variantes após um período de treinamento, durante o qual os envios são distribuídos uniformemente entre as variantes. Ela se ajusta ao longo do tempo conforme percebe tendências de desempenho. Se você não quiser enviar uniformemente durante os estágios iniciais da sua Campaign, use variantes fixas para um teste A/B tradicional.

### A Seleção de Variante recorrente para de otimizar sem escolher uma vencedora clara? {#does-recurring-variant-selection-stop-optimizing-without-picking-a-clear-winner}

Sim, ela para de otimizar quando tem 95% de confiança de que continuar o experimento não melhorará a taxa de conversão em mais de 1% da taxa atual.

### Por que não consigo ativar a Seleção de Variante no meu Canvas ou Campaign? {#why-cant-i-enable-variant-selection-in-my-canvas-or-campaign}

Para envio único, você não pode ativar a Seleção de Variante se seu Canvas ou Campaign for composto por uma única variante.

Para recorrente, você não pode ativar a Seleção de Variante se:
- Você não adicionou eventos de conversão à sua Campaign ou ao seu Canvas.
- Você ativou a reelegibilidade com um período inferior a 24 horas.
- Seu Canvas ou Campaign for composto por uma única variante.