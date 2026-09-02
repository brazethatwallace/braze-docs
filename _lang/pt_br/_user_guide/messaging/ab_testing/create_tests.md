---
nav_title: Criar testes
article_title: Criar testes
page_order: 1
page_type: reference
description: "Este artigo explica como criar testes multivariantes e testes A/B com a Braze."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/messaging/ab_testing/optimizations'
---

# Criar testes multivariantes e testes A/B {#creating-tests}

> Você pode criar um teste multivariante ou teste A/B para qualquer Campaign que tenha como alvo um único canal. Por exemplo, se quiser usar testes multivariantes ou testes A/B para uma Campaign de push, você pode segmentar dispositivos iOS e Android na mesma Campaign.

![O menu suspenso ao selecionar o botão "Criar campanha" para escolher entre multicanal ou canal único.]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## Etapa 1: Crie sua campaign {#step-1-create-your-campaign}

1. Acesse **Messaging** > **Campaigns**.
2. Selecione **Create campaign** e um canal para a campaign na seção que permite testes multivariantes e testes A/B. Para documentação detalhada sobre cada canal de envio de mensagens, consulte [Criar uma campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign).

## Etapa 2: Componha suas variantes {#step-2-compose-your-variants}

Você pode criar até oito variantes da sua mensagem, diferenciando títulos, conteúdo, imagens e muito mais. O número de diferenças entre as mensagens determina se o teste é multivariante ou A/B. Um teste A/B examina o efeito de alterar uma variável, enquanto um teste multivariante examina duas ou mais.

Para algumas ideias sobre como começar a diferenciar suas variantes, consulte [Dicas para diferentes canais](#tips-different-channels).

![Selecionando "Adicionar variante" em uma Campaign.]({% image_buster /assets/img/ab_create_2.png %})

## Etapa 3: Agendar sua campaign {#step-3-schedule-your-campaign}

O agendamento da sua Campaign multivariante funciona da mesma forma que o agendamento de qualquer outra Campaign da Braze. Todos os [tipos de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) padrão estão disponíveis.

Depois que um teste multivariante começa, você não pode fazer alterações na Campaign. Se você alterar os parâmetros, como a linha de assunto ou o corpo HTML, a Braze considera o experimento comprometido e desativa o experimento imediatamente.

Para otimizar automaticamente suas variantes, consulte [Otimizando testes A/B com BrazeAI]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection). Campaigns de envio único e de envio múltiplo usam métodos e requisitos de otimização diferentes.

## Etapa 4: Escolha um Segment or segmento e distribua seus usuários entre as variantes {#step-4-choose-a-segment-and-distribute-your-users-across-variants}

Selecione os Segments para segmentar e distribua os membros entre as variantes selecionadas e o [grupo de controle](#including-a-control-group) opcional. Para conferir as práticas recomendadas sobre como escolher um Segment or segmento para testar, consulte [Escolher um Segment or segmento](#choosing-a-segment).

Para Campaigns compatíveis, ative **Otimizar com BrazeAI<sup>TM</sup>** para otimizar automaticamente a distribuição das variantes. Para uma Campaign de envio único, a Braze reserva parte do público para um segundo envio otimizado. Para uma Campaign de múltiplos envios, o BrazeAI<sup>TM</sup> ajusta a distribuição ao longo do tempo.

### Grupo de controle {#including-a-control-group}

Você pode reservar uma porcentagem do seu público-alvo para um grupo de controle aleatório. Os usuários no grupo de controle não recebem o teste, mas a Braze monitora a taxa de conversão deles durante toda a Campaign.

Ao visualizar seus resultados, você pode comparar as taxas de conversão das suas variantes com uma taxa de conversão de referência fornecida pelo seu grupo de controle. Isso permite comparar tanto os efeitos das suas variantes quanto os efeitos das suas variantes em relação à taxa de conversão que resultaria se você não enviasse nenhuma mensagem.

![Painel de testes A/B que mostra a divisão percentual do grupo de controle, variante 1, variante 2 e variante 3 com 25% para cada grupo.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
Não é recomendado usar um grupo de controle ao determinar um vencedor por _Aberturas_ ou _Cliques_. Como o grupo de controle não recebe a mensagem, esses usuários não podem realizar nenhuma abertura ou clique. Portanto, a taxa de conversão desse grupo é 0% por definição e não constitui uma comparação significativa com as variantes.
{% endalert %}

#### Grupos de controle e testes A/B {#control-groups-and-ab-testing}

Ao usar limite de frequência com um teste A/B, o limite de frequência não é aplicado ao grupo de controle da mesma forma que ao grupo de teste, o que é uma fonte potencial de viés temporal. Use janelas de conversão apropriadas para evitar esse viés.

#### Grupos de controle com Otimizar com BrazeAI<sup>TM</sup> {#control-groups-with-optimize-with-brazeai}

Para uma Campaign de múltiplos envios com [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), o tamanho inicial do grupo de controle depende do número de variantes. Se cada variante recebe mais de 20% dos usuários, o grupo de controle começa em 20%, e as variantes dividem os 80% restantes igualmente. Com mais variantes, o grupo de controle começa menor. À medida que o BrazeAI<sup>TM</sup> analisa o desempenho, o grupo de controle pode crescer ou diminuir.

## Etapa 5: Designe um evento de conversão (opcional) {#step-5-designate-a-conversion-event-optional}

Definir um evento de conversão para uma Campaign permite que você veja quantos destinatários dessa Campaign realizaram uma ação específica após recebê-la.

Isso afeta o teste apenas se você escolheu **Taxa de conversão primária** nas etapas anteriores. Para saber mais, consulte [Eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).

## Etapa 6: Revisar e lançar {#step-6-review-and-launch}

Na página de confirmação, revise os detalhes da sua Campaign multivariante e lance o teste! Em seguida, aprenda como [entender os resultados do seu teste]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).

## O que saber {#things-to-know}

Se o seu experimento já começou a enviar e você editar a mensagem, o experimento será invalidado e todos os resultados do experimento serão removidos.

- Para evitar qualquer interferência no comportamento esperado do experimento, recomendamos evitar edições na mensagem dentro de uma hora antes do lançamento da Campaign do experimento.
- Se o experimento estiver concluído e você editar a mensagem após o envio, os resultados do experimento continuarão disponíveis na análise de dados do seu dashboard. No entanto, se você relançar a Campaign, os resultados do experimento serão removidos.

### Dicas para diferentes canais {#tips-different-channels}

Dependendo do canal que você selecionar, é possível testar diferentes componentes da sua mensagem. Por exemplo, tente compor variantes com uma ideia do que você quer testar e o que espera provar. Quais alavancas você pode utilizar e quais são os efeitos desejados? Embora existam milhões de possibilidades que você pode investigar usando testes multivariantes e A/B, aqui estão algumas sugestões para começar:

| Canal | Aspectos da mensagem que você pode alterar | Resultados esperados |
| ---------------------| --------------- | ------------- |
| Push | Texto <br> Uso de imagens e emojis <br> Deep links  <br> Apresentação de números (por exemplo, "triplicar" versus "aumentar em 200%")  <br> Apresentação de tempo (por exemplo, "termina à meia-noite" versus "termina em 6 horas") | Aberturas  <br> Taxa de conversão |
| E-mail | Linha de assunto <br> Nome de exibição <br> Saudação <br> Corpo do texto <br> Uso de imagens e emojis <br> Apresentação de números (por exemplo, "triplicar" versus "aumentar em 200%") <br> Apresentação de tempo (por exemplo, "termina à meia-noite" versus "termina em 6 horas") | Aberturas  <br> Taxa de conversão |
| Mensagem no app | Aspectos listados para "push" <br> [Especificações de imagem para mensagens no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#image-specifications) | Clique <br> Taxa de conversão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dicas para diferentes canais" }

{% alert tip %}
Ao executar testes A/B, não se esqueça de gerar [relatórios de funil]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) que permitem entender como cada variante impactou seu funil de conversão, especialmente se a "conversão" para o seu negócio envolve múltiplas etapas ou ações.
{% endalert %}

Além disso, a duração ideal do seu teste também pode variar dependendo do canal. Tenha em mente a quantidade média de tempo que a maioria dos usuários pode precisar para interagir com cada canal.

Por exemplo, se você está testando um push, pode obter resultados significativos mais rápido do que ao testar e-mails, já que os usuários veem os pushes imediatamente, mas pode levar dias até que vejam ou abram um e-mail. Se está testando mensagens no app, lembre-se de que os usuários precisam abrir o app para ver a Campaign, então você deve esperar mais tempo para coletar resultados tanto dos usuários que abrem o app com mais frequência quanto dos usuários mais típicos.

Se você não tem certeza de quanto tempo seu teste deve durar, [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) pode configurar e executar a otimização automaticamente.

### Escolhendo um Segment or segmento {#choosing-a-segment}

Como diferentes Segments dos seus usuários podem responder de formas diferentes ao envio de mensagens, o sucesso de uma mensagem específica diz algo tanto sobre a mensagem em si quanto sobre o Segment or segmento de destino. Portanto, tente planejar um teste com seu público-alvo em mente.

Por exemplo, enquanto usuários ativos podem ter taxas de resposta iguais para "Esta oferta expira amanhã!" e "Esta oferta expira em 24 horas!", usuários que não abriram o app por uma semana podem responder melhor à segunda opção, pois ela cria uma sensação maior de urgência.

Além disso, ao escolher em qual Segment or segmento executar o teste, certifique-se de que o tamanho desse Segment or segmento seja grande o suficiente para o seu teste. Em geral, testes multivariantes e A/B com mais variantes exigem um grupo de teste maior para alcançar resultados estatisticamente significativos. Isso porque mais variantes resultam em menos usuários vendo cada variante individual.

{% alert tip %}
Como referência, você provavelmente precisa de cerca de 15.000 usuários por variante (incluindo o grupo de controle) para alcançar 95% de confiança nos resultados do teste. No entanto, o número exato de usuários necessários pode ser maior ou menor, dependendo do seu caso específico. Para orientações mais precisas sobre tamanhos de amostra por variante, considere consultar uma [calculadora de tamanho de amostra](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Viés e randomização {#bias-and-randomization}

Uma pergunta comum sobre atribuições de grupos de controle e teste é se elas podem introduzir viés no teste. Outros às vezes se perguntam como sabemos se essas atribuições são realmente aleatórias.

Os usuários são atribuídos a variantes de mensagem, variantes do Canvas ou seus respectivos grupos de controle concatenando seu ID de usuário (gerado aleatoriamente) com o ID da Campaign ou do Canvas (gerado aleatoriamente), calculando o módulo desse valor por 100 e então ordenando os usuários em faixas que correspondem às porcentagens de atribuição para variantes e grupo de controle opcional escolhidos no dashboard. Portanto, não há forma prática de que o comportamento dos usuários antes da criação de uma Campaign ou Canvas específico varie sistematicamente entre variantes e controle. Também não é prático ser mais aleatório (ou, mais precisamente, pseudo-aleatório) do que esta implementação.

#### Erros a evitar {#mistakes-to-avoid}

Existem alguns erros comuns a serem evitados para não criar a aparência de diferenças com base no canal de envio de mensagens caso os públicos não sejam filtrados corretamente.

Por exemplo, se você enviar uma mensagem push para um público amplo com um grupo de controle, o grupo de teste envia mensagens apenas para usuários com um token por push. No entanto, o grupo de controle inclui tanto usuários que possuem um token por push quanto usuários que não possuem. Nesse caso, o público inicial da sua Campaign ou Canvas deve filtrar por ter um token por push (`Foreground Push Enabled` é `true`). O mesmo deve ser feito para a elegibilidade de receber mensagens em outros canais: aceitar receber, ter um token por push ou estar inscrito.

Observe que, se uma variante de controle não consistir em nenhuma etapa do Canvas, os eventos de critérios de saída não são registrados para os usuários na variante de controle.

{% alert note %}
Se você usa manualmente números de bucket aleatórios para grupos de controle, confira os [pontos de atenção]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for) nos seus grupos de controle.
{% endalert %}