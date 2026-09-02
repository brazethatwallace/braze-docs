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

Nos testes A/B, o profissional de marketing experimenta uma única variável dentro da Campaign (como linhas de assunto de e-mail ou horário de envio da mensagem). Isso envolve dividir aleatoriamente um subconjunto do público em dois ou mais grupos, apresentar a cada grupo uma variante diferente e observar qual variante apresenta a maior taxa de conversão. Normalmente, a variante com melhor desempenho é enviada em seguida para o restante do público.

#### Testes multivariantes {#multivariate-testing}

Os testes multivariantes são uma extensão dos testes A/B que permitem ao profissional de marketing testar múltiplas variáveis ao mesmo tempo para determinar a combinação mais eficaz. Por exemplo, você pode testar a linha de assunto do seu e-mail, a imagem que acompanha o texto e a cor do botão de CTA. Esse tipo de teste permite explorar mais variáveis e combinações de variantes em um único experimento, obtendo insights de forma mais rápida e abrangente do que os testes A/B. No entanto, testar mais variáveis e combinações em um único experimento exige um público maior para alcançar significância estatística.

### Como os resultados dos testes A/B são calculados? {#how-are-ab-test-results-calculated}

A Braze testa todas as variantes umas contra as outras usando testes qui-quadrado de Pearson, que medem se uma variante supera estatisticamente todas as outras em um nível de significância de p < 0,05, ou o que chamamos de 95% de significância. Entre todas as variantes que excedem esse limite de significância, a variante com melhor desempenho é determinada como a "vencedora".

Esse é um teste separado da pontuação de confiança, que descreve apenas o desempenho de uma variante em comparação com o grupo de controle, com um valor numérico entre 0 e 100%. Especificamente, ela representa nossa confiança de que a diferença padronizada na taxa de conversão entre a variante e o grupo de controle é significativamente maior do que o acaso.

### Por que a distribuição de variantes não é uniforme? {#why-isnt-the-variant-distribution-even}

A atribuição de variantes é aleatorizada a cada envio, então a divisão real pode não corresponder exatamente às porcentagens configuradas — especialmente com amostras menores. Para saber mais, consulte [Distribuição de variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/variant_distribution).

## Executando e concluindo testes {#running-and-concluding-tests}

### Quando o teste inicial termina? {#when-is-the-initial-test-over}

Para uma Campaign de envio único usando **Otimizar com BrazeAI<sup>TM</sup>**, o teste inicial termina após a duração configurada do experimento. O BrazeAI<sup>TM</sup> então envia a variante com melhor desempenho para o público restante.

Para Campaigns recorrentes, baseadas em ação e disparadas por API que enviam várias vezes, **Otimizar com BrazeAI<sup>TM</sup>** acompanha continuamente o desempenho das variantes e direciona o tráfego da Campaign para as variantes com melhor desempenho.

### Como a Braze lida com usuários que receberam uma variante de mensagem em uma Campaign recorrente ou etapa de entrada do Canvas? {#how-does-braze-handle-users-who-received-a-message-variant-in-a-recurring-campaign-or-canvas-entry-step}

Os usuários são atribuídos aleatoriamente a uma variante específica antes de receberem a Campaign pela primeira vez. Cada vez subsequente que a Campaign é recebida (ou o usuário reentra em uma variante do Canvas), eles recebem a mesma variante, a menos que os percentuais das variantes sejam modificados. Se os percentuais das variantes mudarem, os usuários podem ser redistribuídos para outras variantes. Os usuários permanecem nessas variantes até que os percentuais sejam modificados novamente. Os usuários são redistribuídos apenas para as variantes que foram editadas.

Por exemplo, digamos que temos uma Campaign ou Canvas com três variantes. Se apenas a Variante A e a Variante B forem alteradas ou atualizadas, os usuários na Variante C não serão redistribuídos porque o percentual da Variante C não foi alterado. Os grupos de controle permanecem consistentes se o percentual da variante não for alterado. Usuários que receberam mensagens anteriormente não podem entrar no grupo de controle em um envio posterior, e nenhum usuário no grupo de controle pode receber uma mensagem.

{% alert note %}
Um usuário pode ser marcado como tendo "recebido" uma mensagem se compartilhar um identificador de canal (como um e-mail ou número de telefone) com alguém que recebeu, abriu ou clicou na mensagem.
{% endalert %}

#### E as jornadas experimentais? {#what-about-experiment-paths}

O mesmo se aplica porque as jornadas do Canvas que seguem um experimento também são variantes.

#### Posso tomar ações para redistribuir usuários em Campaigns e Canvas? {#can-i-take-actions-to-redistribute-users-in-campaigns-and-canvases}

A única maneira de redistribuir usuários em Canvas é usar [jornadas aleatórias em jornadas experimentais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#step-1-choose-the-number-of-paths-and-audience-distribution), que sempre randomizam as atribuições de jornada quando os usuários reentram no Canvas. No entanto, isso não é um experimento padrão e pode invalidar qualquer resultado de experimento porque o grupo de controle pode ser contaminado com usuários do tratamento.

## Confiança e viés {#confidence-and-bias}

### A confiança aumenta com o tempo? {#does-confidence-increase-over-time}

A confiança aumenta com o tempo se todas as outras condições se mantiverem constantes. Manter constante significa que não há outros fatores de marketing que possam influenciar as variantes, como a Variante A mencionando uma promoção de 25% de desconto que termina no meio do teste.

A confiança é uma medida de quão segura a Braze está de que a variante é diferente do grupo de controle. À medida que mais mensagens são enviadas, o poder estatístico do teste aumenta, o que elevaria a confiança de que as diferenças medidas no desempenho não se devem ao acaso. De modo geral, uma amostra maior aumenta nossa confiança em identificar diferenças menores de desempenho entre as variantes e o grupo de controle.

No entanto, se as taxas de conversão entre as variantes e o grupo de controle convergirem (se aproximarem) à medida que mais mensagens são enviadas, a confiança pode diminuir, pois a diferença medida que você busca está encolhendo, o que pode superar o benefício de uma amostra maior.

### A atribuição de grupos de controle e teste pode introduzir viés nos testes? {#can-control-and-test-group-assignments-introduce-bias-to-testing}

Não há maneira prática pela qual os atributos ou comportamentos de um usuário antes da criação de uma Campaign ou Canvas específico possam variar sistematicamente entre as variantes e o grupo de controle.

Para atribuir usuários a variantes de mensagem, variantes de Canvas ou seus respectivos grupos de controle, começamos vinculando o ID de usuário gerado aleatoriamente ao ID de Campaign ou Canvas gerado aleatoriamente. Em seguida, aplicamos um algoritmo de hash sha256 e dividimos o resultado por 100, mantendo o resto (também conhecido como módulo de 100). Por fim, ordenamos os usuários em fatias que correspondem às porcentagens de atribuição para as variantes (e o grupo de controle opcional) escolhidas no dashboard.

### Por que não é possível usar limite de frequência com um grupo de controle? {#why-cant-i-use-rate-limiting-with-a-control-group}

Atualmente, a Braze não oferece suporte a limite de frequência com testes A/B que possuem grupo de controle. O limite de frequência não se aplica ao grupo de controle da mesma forma que às variantes, o que introduz viés. Em vez disso, considere usar [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection), que ajusta automaticamente a porcentagem de usuários que recebem cada variante com base no desempenho da Campaign.