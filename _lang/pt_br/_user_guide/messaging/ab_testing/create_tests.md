---
nav_title: Criar testes
article_title: Criar testes
page_order: 1
page_type: reference
description: "Este artigo explica como criar testes multivariantes e Testes A/B com a Braze."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/messaging/ab_testing/optimizations'
---

# Criar testes multivariantes e Testes A/B {#creating-tests}

> Você pode criar um teste multivariante ou Teste A/B para qualquer campanha que tenha como alvo um único canal e um único dispositivo. Por exemplo, se quiser usar testes multivariantes ou Testes A/B para uma campanha de push, você pode segmentar apenas dispositivos iOS ou apenas dispositivos Android — não ambos os tipos de dispositivo na mesma campanha.

![O menu suspenso ao selecionar o botão "Criar campanha" para escolher entre multicanal ou canal único.]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## Etapa 1: Crie sua campanha

1. Acesse **Envio de mensagens** > **Campanhas**.
2. Selecione **Criar campanha** e um canal para a campanha na seção que permite testes multivariantes e Testes A/B. Para documentação detalhada sobre cada canal de envio de mensagens, consulte [Criar uma campanha]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/).

## Etapa 2: Componha suas variantes

Você pode criar até oito variantes da sua mensagem, diferenciando títulos, conteúdo, imagens e muito mais. O número de diferenças entre as mensagens determina se o teste é multivariante ou A/B. Um Teste A/B examina o efeito de alterar uma variável, enquanto um teste multivariante examina duas ou mais.

Para algumas ideias de como começar a diferenciar suas variantes, consulte [Dicas para diferentes canais](#tips-different-channels).

![Selecionando "Adicionar variante" para uma campanha.]({% image_buster /assets/img/ab_create_2.png %})

## Etapa 3: Programe sua campanha

Programar sua campanha multivariante funciona da mesma forma que programar qualquer outra campanha da Braze. Todos os [tipos de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/) padrão estão disponíveis.

Depois que um teste multivariante começa, você não pode fazer alterações na campanha. Se você alterar os parâmetros, como a linha de assunto ou o corpo HTML, a Braze considera o experimento comprometido e o desativa imediatamente.

{% alert important %}
Para usar uma [otimização]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/) (disponível para canais selecionados), programe sua campanha para envio único. Otimizações não estão disponíveis para campanhas recorrentes ou com reelegibilidade ativada.
{% endalert %}

## Etapa 4: Escolha um segmento e distribua seus usuários entre as variantes

Selecione os segmentos desejados e distribua os membros entre as variantes selecionadas e o [grupo de controle](#including-a-control-group) opcional. Para práticas recomendadas sobre como escolher um segmento para testar, consulte [Escolhendo um segmento](#choosing-a-segment).

Para campanhas de push, e-mail e webhook programadas para envio único, você também pode usar uma [otimização]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/). Uma otimização reserva uma parte do seu público-alvo do Teste A/B e a mantém para um segundo envio otimizado com base nos resultados do primeiro teste.

### Grupo de controle {#including-a-control-group}

Você pode reservar uma porcentagem do seu público-alvo para um grupo de controle aleatório. Os usuários no grupo de controle não recebem o teste, mas a Braze monitora a taxa de conversão deles durante toda a campanha.

Ao visualizar seus resultados, você pode comparar as taxas de conversão das suas variantes com uma taxa de conversão de referência fornecida pelo seu grupo de controle. Isso permite comparar tanto os efeitos das suas variantes quanto os efeitos das suas variantes em relação à taxa de conversão que resultaria se você não enviasse nenhuma mensagem.

![Painel de Testes A/B que mostra a distribuição percentual do Grupo de Controle, Variante 1, Variante 2 e Variante 3 com 25% para cada grupo.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
Não é recomendado usar um grupo de controle ao determinar um vencedor por *Aberturas* ou *Cliques*. Como o grupo de controle não recebe a mensagem, esses usuários não podem realizar nenhuma abertura ou clique. Portanto, a taxa de conversão desse grupo é 0% por definição e não constitui uma comparação significativa com as variantes.
{% endalert %}

#### Grupos de controle com Testes A/B

Ao usar limite de taxa com um Teste A/B, o limite de taxa não é aplicado ao grupo de controle da mesma forma que ao grupo de teste, o que é uma fonte potencial de viés temporal. Use janelas de conversão apropriadas para evitar esse viés.

#### Grupos de controle com Seleção inteligente

O tamanho do grupo de controle para uma campanha com [Seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/) é baseado no número de variantes. Se cada variante é enviada para mais de 20% dos usuários, o grupo de controle é de 20%, e as variantes são distribuídas igualmente nos 80% restantes. No entanto, se você tiver variantes suficientes para que cada uma seja enviada para menos de 20% dos usuários, o grupo de controle precisa ser menor. Quando a Seleção inteligente começa a analisar a performance do seu teste, o grupo de controle cresce ou diminui com base nos resultados.

## Etapa 5: Defina um evento de conversão (opcional)

Definir um evento de conversão para uma campanha permite que você veja quantos destinatários dessa campanha realizaram uma ação específica após recebê-la.

Isso só afeta o teste se você escolheu **Taxa de conversão primária** nas etapas anteriores. Para saber mais, consulte [Eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/).

## Etapa 6: Revise e lance

Na página de confirmação, revise os detalhes da sua campanha multivariante e lance o teste! Em seguida, saiba como [entender os resultados do seu teste]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).

## Informações importantes

Se o seu experimento já começou a enviar e você editar a mensagem, o experimento se torna inválido e todos os resultados do experimento são removidos.

- Para evitar qualquer interferência no comportamento esperado do experimento, recomendamos não editar mensagens dentro de uma hora do lançamento da campanha do experimento.
- Se o seu experimento foi concluído e você editar a mensagem após o envio, os resultados do experimento permanecem disponíveis na análise de dados do dashboard. No entanto, se você relançar a campanha, os resultados do experimento são removidos.

### Dicas para diferentes canais {#tips-different-channels}

Dependendo do canal selecionado, você pode testar diferentes componentes da sua mensagem. Por exemplo, tente compor variantes com uma ideia do que você quer testar e o que espera provar. Quais alavancas você pode usar e quais são os efeitos desejados? Embora existam milhões de possibilidades que você pode investigar usando testes multivariantes e Testes A/B, aqui estão algumas sugestões para começar:

| Canal | Aspectos da mensagem que você pode alterar | Resultados a observar |
| ---------------------| --------------- | ------------- |
| Push | Texto <br> Uso de imagens e emojis <br> Deep links  <br> Apresentação de números (por exemplo, "triplicar" versus "aumentar em 200%")  <br> Apresentação de tempo (por exemplo, "termina à meia-noite" versus "termina em 6 horas") | Aberturas  <br> Taxa de conversão |
| E-mail | Assunto <br> Nome de exibição <br> Saudação <br> Corpo do texto <br> Uso de imagens e emojis <br> Apresentação de números (por exemplo, "triplicar" versus "aumentar em 200%") <br> Apresentação de tempo (por exemplo, "termina à meia-noite" versus "termina em 6 horas") | Aberturas  <br> Taxa de conversão |
| Mensagem no app | Aspectos listados para "push" <br> [Especificações de imagem para mensagens no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#in-app-messages) | Clique <br> Taxa de conversão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Ao executar Testes A/B, não se esqueça de gerar [relatórios de funil]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/) que permitem entender como cada variante impactou seu funil de conversão, especialmente se "conversão" para o seu negócio envolve múltiplas etapas ou ações.
{% endalert %}

Além disso, a duração ideal do seu teste também pode variar dependendo do canal. Leve em consideração o tempo médio que a maioria dos usuários pode precisar para interagir com cada canal.

Por exemplo, se você está testando um push, pode obter resultados significativos mais rapidamente do que ao testar e-mail, já que os usuários veem pushes imediatamente, mas podem levar dias para ver ou abrir um e-mail. Se você está testando mensagens no app, lembre-se de que os usuários precisam abrir o app para ver a campanha. Portanto, você deve esperar mais tempo para coletar resultados tanto dos seus usuários mais ativos quanto dos mais típicos.

Se você não tem certeza de quanto tempo seu teste deve durar, o recurso [Seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/) pode ser útil para encontrar uma variante vencedora de forma eficiente.

### Escolhendo um segmento {#choosing-a-segment}

Como diferentes segmentos dos seus usuários podem responder de forma diferente às mensagens, o sucesso de uma mensagem específica diz algo tanto sobre a mensagem em si quanto sobre o segmento-alvo. Portanto, tente projetar um teste com o segmento-alvo em mente.

Por exemplo, enquanto usuários ativos podem ter taxas de resposta iguais para "Esta oferta expira amanhã!" e "Esta oferta expira em 24 horas!", usuários que não abriram o app há uma semana podem ser mais responsivos à segunda formulação, pois ela cria um maior senso de urgência.

Além disso, ao escolher em qual segmento executar seu teste, certifique-se de que o tamanho desse segmento seja grande o suficiente para o seu teste. Em geral, testes multivariantes e Testes A/B com mais variantes exigem um grupo de teste maior para alcançar resultados estatisticamente significativos. Isso ocorre porque mais variantes resultam em menos usuários vendo cada variante individual.

{% alert tip %}
Como referência, você provavelmente precisa de cerca de 15.000 usuários por variante (incluindo o controle) para alcançar 95% de intervalo de confiança nos resultados do seu teste. No entanto, o número exato de usuários necessários pode ser maior ou menor, dependendo do seu caso específico. Para orientações mais precisas sobre tamanhos de amostra de variantes, considere consultar uma [calculadora de tamanho de amostra](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Viés e aleatorização

Uma pergunta comum sobre as atribuições de grupos de controle e teste é se elas podem introduzir viés nos seus testes. Outros às vezes se perguntam como sabemos se essas atribuições são realmente aleatórias.

Os usuários são atribuídos a variantes de mensagem, variantes de Canvas ou seus respectivos grupos de controle concatenando seu ID de usuário (gerado aleatoriamente) com o ID da campanha ou Canvas (gerado aleatoriamente), calculando o módulo desse valor por 100 e, em seguida, ordenando os usuários em faixas que correspondem às porcentagens de atribuição para variantes e controle opcional escolhidas no dashboard. Portanto, não há uma forma prática de que os comportamentos dos usuários antes da criação de uma campanha ou Canvas específico variem sistematicamente entre variantes e controle. Também não é prático ser mais aleatório (ou mais precisamente, pseudoaleatório) do que esta implementação.

#### Erros a evitar

Existem alguns erros comuns a evitar que criam a aparência de diferenças com base no canal de envio de mensagens se os públicos não forem filtrados corretamente.

Por exemplo, se você enviar uma mensagem push para um público amplo com um controle, o grupo de teste envia mensagens apenas para usuários com um token por push. No entanto, o grupo de controle inclui tanto usuários que têm um token por push quanto usuários que não têm. Nesse caso, seu público inicial para a campanha ou Canvas deve filtrar por ter um token por push (`Foreground Push Enabled` é `true`). O mesmo deve ser feito para elegibilidade de receber mensagens em outros canais: optou por receber, tem um token por push ou está inscrito.

Observe que se uma variante de controle não contiver nenhuma etapa do Canvas, os eventos de critérios de saída não são registrados para os usuários na variante de controle.

{% alert note %}
Se você usar manualmente números de bucket aleatórios para grupos de controle, confira os [pontos de atenção]({{site.baseurl}}/user_guide/audience/global_control_group/#things-to-watch-for) nos seus grupos de controle.
{% endalert %}