---
nav_title: FAQ
article_title: FAQ sobre testes multivariantes e testes A/B
page_order: 21
page_type: reference
toc_headers: h2
description: "Este artigo aborda perguntas frequentes sobre testes multivariantes e testes A/B com a Braze."
---

# FAQ sobre testes multivariantes e testes A/B {#multivariate-and-ab-test-faq}

> Este artigo aborda perguntas frequentes sobre testes multivariantes e testes A/B com a Braze.

## Conceitos básicos de testes {#testing-basics}

### Qual é a diferença entre testes A/B e testes multivariantes? {#what-is-the-difference-between-ab-testing-and-multivariate-testing}

#### Testes A/B {#ab-testing}

Nos testes A/B, o profissional de marketing experimenta uma única variável dentro da Campaign (como o assunto do e-mail ou o horário de envio da mensagem). Isso envolve dividir aleatoriamente um subconjunto do público em dois ou mais grupos, apresentar a cada grupo uma variação diferente e observar qual variação apresenta a maior taxa de conversão. Normalmente, a variação com melhor desempenho é enviada em seguida para o restante do público.

#### Testes multivariantes {#multivariate-testing}

Os testes multivariantes são uma extensão dos testes A/B, que permitem ao profissional de marketing testar múltiplas variáveis ao mesmo tempo para determinar a combinação mais eficaz. Por exemplo, você pode testar o assunto do seu e-mail, a imagem que acompanha o texto e a cor do botão de CTA. Esse tipo de teste permite explorar mais variáveis e combinações de variações em um único experimento, obtendo insights de forma mais rápida e abrangente do que os testes A/B. No entanto, testar mais variáveis e combinações em um único experimento exige um público maior para alcançar significância estatística.

### Como os resultados dos testes A/B são calculados? {#how-are-ab-test-results-calculated}

A Braze testa todas as variantes entre si usando testes qui-quadrado de Pearson, que medem se uma variante supera estatisticamente todas as outras em um nível de significância de p < 0,05, ou o que chamamos de significância de 95%. Entre todas as variantes que excedem esse limite de significância, a variante com melhor desempenho é determinada como a "vencedora".

Esse é um teste separado do intervalo de confiança, que descreve apenas o desempenho de uma variante em comparação com o controle, com um valor numérico entre 0 e 100%. Especificamente, ele representa nossa confiança de que a diferença padronizada na taxa de conversão entre a variante e o controle é significativamente maior do que o acaso.

### Por que a distribuição de variantes não é uniforme? {#why-isnt-the-variant-distribution-even}

A atribuição de variantes é aleatória em cada envio, então a divisão real pode não corresponder exatamente às porcentagens configuradas — especialmente com amostras menores. Para saber mais, consulte [Distribuição de variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/variant_distribution).

## Execução e conclusão de testes {#running-and-concluding-tests}

### Quando o teste inicial termina? {#when-is-the-initial-test-over}

Ao usar a Variante Vencedora para Campaigns de envio único, o teste termina quando o Horário de Envio da Variante Vencedora chega. A Braze considerará uma variante como vencedora se ela apresentar a maior taxa de conversão com uma margem estatisticamente significativa.

Para Campaigns recorrentes, baseadas em ação e disparadas por API, você pode usar a Seleção inteligente para acompanhar continuamente os dados de desempenho de cada variante e otimizar continuamente o tráfego da Campaign para as variantes com melhor desempenho. Com a Seleção inteligente, em vez de definir explicitamente um grupo experimental onde os usuários recebem variantes aleatórias, o algoritmo da Braze refinará continuamente sua estimativa da variante com melhor desempenho, permitindo potencialmente uma seleção mais rápida da melhor opção.

### Como a Braze lida com usuários que receberam uma variante de mensagem em uma Campaign recorrente ou etapa de entrada do Canvas? {#how-does-braze-handle-users-who-received-a-message-variant-in-a-recurring-campaign-or-canvas-entry-step}

Os usuários são atribuídos aleatoriamente a uma variante específica antes de receber a Campaign pela primeira vez. Cada vez que a Campaign é recebida novamente (ou o usuário reentra em uma variante do Canvas), eles recebem a mesma variante, a menos que as porcentagens das variantes sejam modificadas. Se as porcentagens das variantes mudarem, os usuários podem ser redistribuídos para outras variantes. Os usuários permanecem nessas variantes até que as porcentagens sejam modificadas novamente. Os usuários são redistribuídos apenas para as variantes que foram editadas.

Por exemplo, digamos que temos uma Campaign ou Canvas com três variantes. Se apenas a Variante A e a Variante B forem alteradas ou atualizadas, os usuários da Variante C não serão redistribuídos porque a porcentagem da Variante C não foi alterada. Os grupos de controle permanecem consistentes se a porcentagem da variante não for alterada. Usuários que receberam mensagens anteriormente não podem entrar no grupo de controle em um envio posterior, e nenhum usuário no grupo de controle pode receber uma mensagem.

{% alert note %}
Um usuário pode ser marcado como tendo "recebido" uma mensagem se compartilhar um identificador de canal (como um e-mail ou número de telefone) com alguém que recebeu, abriu ou clicou na mensagem.
{% endalert %}

#### E quanto às Jornadas do experimento? {#what-about-experiment-paths}

O mesmo se aplica, pois as jornadas do Canvas que seguem um experimento também são variantes.

#### Posso tomar ações para redistribuir usuários em Campaigns e Canvas? {#can-i-take-actions-to-redistribute-users-in-campaigns-and-canvases}

A única maneira de redistribuir usuários em Canvas é usar [Jornadas Aleatórias nas Jornadas do Experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#step-1-choose-the-number-of-paths-and-audience-distribution), que sempre randomizará as atribuições de jornada quando os usuários reentrarem no Canvas. No entanto, isso não é um experimento padrão e pode invalidar quaisquer resultados do experimento, pois o grupo de controle pode ser contaminado com usuários do grupo de tratamento.

## Intervalo de confiança e viés {#confidence-and-bias}

### O intervalo de confiança aumenta com o tempo? {#does-confidence-increase-over-time}

O intervalo de confiança aumenta com o tempo se todas as outras condições permanecerem constantes. Manter constante significa que não há outros fatores de marketing que possam influenciar as variantes, como a Variante A mencionando uma promoção de 25% de desconto que termina no meio do teste.

O intervalo de confiança é uma medida de quão confiante a Braze está de que a variante é diferente do controle. À medida que mais mensagens são enviadas, o poder estatístico do teste aumenta, o que eleva o intervalo de confiança de que as diferenças medidas no desempenho não se devem ao acaso. Geralmente, uma amostra maior aumenta nossa confiança em identificar diferenças menores no desempenho entre variantes e controle.

No entanto, se as taxas de conversão entre as variantes e o controle convergirem (ficarem mais próximas) à medida que mais mensagens são enviadas, o intervalo de confiança pode diminuir, pois a diferença medida que importa está encolhendo, o que pode superar o benefício de uma amostra maior.

### A atribuição de grupos de controle e teste pode introduzir viés nos testes? {#can-control-and-test-group-assignments-introduce-bias-to-testing}

Não há uma maneira prática pela qual os atributos ou comportamentos de um usuário antes da criação de uma Campaign ou Canvas específico possam variar sistematicamente entre variantes e controle.

Para atribuir usuários a variantes de mensagem, variantes do Canvas ou seus respectivos grupos de controle, começamos vinculando o ID de usuário gerado aleatoriamente ao ID da Campaign ou Canvas gerado aleatoriamente. Em seguida, aplicamos um algoritmo de hash sha256 e dividimos o resultado por 100, mantendo o resto (também conhecido como módulo de 100). Por fim, ordenamos os usuários em fatias que correspondem às porcentagens de atribuição para variantes (e controle opcional) escolhidas no dashboard.

### Por que não posso usar limite de taxa com um grupo de controle? {#why-cant-i-use-rate-limiting-with-a-control-group}

Atualmente, a Braze não oferece suporte a limite de taxa com testes A/B que possuem um grupo de controle. Isso ocorre porque o limite de taxa não se aplica ao grupo de controle da mesma forma que às variantes, introduzindo viés. Em vez disso, considere usar a [Seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection), que ajusta automaticamente a porcentagem de usuários que receberão cada variante com base na análise de dados e no desempenho da Campaign.