---
nav_title: Números de bucket aleatórios
article_title: Números de bucket aleatórios
page_order: 2
page_type: reference
description: "Este artigo aborda o conceito de números de bucket aleatórios e como você pode usá-los para criar variantes e grupos de controle."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# Números de bucket aleatórios {#random-bucket-numbers}

> Um número de bucket aleatório é um atributo de usuário que pode ser usado para criar segmentos uniformemente distribuídos de usuários aleatórios.

## Visão geral {#overview}

Quando um perfil de usuário é criado na Braze, esse usuário recebe automaticamente um número de bucket aleatório entre 0 e 9999 (inclusive). Você pode usar esses segmentos para testar a eficácia de várias Campaigns ou Canvas em grupos de usuários ao longo do tempo.

### Uso do grupo de controle global {#global-control-group-usage}

Os números de bucket aleatórios são usados no seu grupo de controle global&#8212;um grupo de usuários que não recebe nenhuma Campaign ou Canvas. A Braze seleciona aleatoriamente vários intervalos de números de bucket aleatórios e inclui os usuários desses buckets selecionados. Os números de bucket aleatórios são atribuídos sem ponderação ou consideração de números alocados recentemente.

{% alert note %}
Quando um usuário é excluído e recriado, ele recebe um número de bucket aleatório diferente, pois é considerado um novo usuário.
{% endalert %}

Se você tem um grupo de controle global configurado e deseja usar números de bucket aleatórios para outros casos de uso, confira [Pontos de atenção]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for).

### Quando usar números de bucket aleatórios {#when-to-use-random-bucket-numbers}

Se você deseja realizar testes de longo prazo sobre a eficácia de várias Campaigns ou Canvas ao longo do tempo, pode usar números de bucket aleatórios para segmentar seus usuários.

### Quando usar outra abordagem {#when-to-use-something-else}

Se você deseja segmentar usuários para testes dentro de uma única Campaign ou um único Canvas, use [testes A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) para Campaigns. Para Canvas, você pode criar diferentes [variantes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-21-add-a-variant) para testes no nível da jornada, ou usar [jornadas experimentais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para testes no nível da etapa.

## Criar segmentos usando números de bucket aleatórios {#create-segments-using-random-bucket-numbers}

Ao [criar um Segment or segmento or segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), adicione o filtro "Random Bucket #". Em seguida, especifique um número ou intervalo de números para incluir no seu Segment or segmento or segmento.

![Um filtro de Segment or segmento or segmento para números de bucket aleatórios não superiores a "3000".]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

Você pode usar esses tipos de segmentos se quiser executar um teste com três variantes diferentes e também incluir um grupo de controle. Considere o seguinte plano de exemplo para criar segmentos de tamanhos iguais para três variantes e um grupo de controle:

- Os números de bucket de 0 a 2499 correspondem ao Segment or segmento or segmento de controle
- Os números de bucket de 2500 a 4999 correspondem ao Segment or segmento or segmento que receberá a variante 1
- Os números de bucket de 5000 a 7499 correspondem ao Segment or segmento or segmento que receberá a variante 2
- Os números de bucket de 7500 a 9999 correspondem ao Segment or segmento or segmento que receberá a variante 3

Dependendo de quantos segmentos você deseja e da distribuição de usuários em cada Segment or segmento or segmento, seu plano pode ser diferente.

Para cada um dos seus segmentos de número de bucket aleatório, incluindo o grupo de controle, ative o [rastreamento de análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking). Ao avaliar o sucesso das variantes em relação ao grupo de controle, você pode acessar a página de [eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) e verificar com que frequência cada Segment or segmento or segmento concluiu determinados eventos personalizados.

{% alert tip %}
Ao usar segmentos de número de bucket aleatório em um Canvas, por exemplo como filtro em uma etapa de [divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split), certifique-se de que os [critérios de saída]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) do Canvas, os filtros de público e as etapas anteriores não direcionem segmentos que se sobreponham a um dos seus intervalos de bucket. Se isso acontecer, os usuários nesse intervalo podem ser removidos de forma desproporcional antes de chegar à divisão, causando uma distribuição desigual entre as jornadas.
{% endalert %}

### Reentrada aleatória de público usando números de bucket aleatórios {#random-audience-re-entry-using-random-bucket-numbers}

A reentrada aleatória de público pode ser útil para [testes A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/faq#what-is-the-difference-between-ab-testing-and-multivariate-testing) ou para direcionar grupos específicos de usuários nas suas Campaigns. Para realizar a reentrada aleatória de público com números de bucket aleatórios, faça o seguinte:

1. [Crie seu Segment or segmento or segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Defina os buckets aleatórios. Na sua Campaign ou Canvas, use o filtro de bucket aleatório para dividir seu público em diferentes grupos. Por exemplo, você pode especificar exatamente dois buckets aleatórios para dividir seu público (50% dos usuários por bucket).
3. Na seção **Target Audiences** da sua Campaign ou Canvas, especifique as configurações de bucket aleatório. Isso permite que a Braze atribua automaticamente os usuários aos buckets apropriados com base nas porcentagens definidas.
4. Configure uma lógica que permita que os usuários reentrem no Segment or segmento or segmento. Por exemplo, você pode permitir que os usuários reentrem no Segment or segmento or segmento se não interagiram com um app por 15 dias.
5. Lance sua Campaign e monitore o desempenho de cada bucket. Você pode analisar métricas como taxas de engajamento e taxas de conversão para determinar a eficácia da reentrada aleatória de público no seu caso de uso.