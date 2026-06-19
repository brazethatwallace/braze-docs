---
nav_title: Análise de dados
article_title: Análise de dados de testes A/B
page_order: 10
page_type: reference
description: "Este artigo explica como visualizar e interpretar os resultados de uma campanha multivariante ou de testes A/B."
---

# Análise de dados de testes multivariantes e A/B {#multivariate-and-ab-test-analytics}

> Este artigo explica como visualizar os resultados de um teste multivariante ou A/B. Se você ainda não configurou seu teste, consulte [Criar testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) para ver o passo a passo.

Após o lançamento da sua campanha, você pode verificar o desempenho de cada variante selecionando sua campanha na seção **Campaigns** do dashboard.

## Análise de dados por opção de otimização {#analytics-by-optimization-option}

A visualização da análise de dados varia dependendo da [otimização]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/) selecionada durante a configuração inicial.

### Sem otimização {#no-optimization}

Se você selecionou **No optimization** ao configurar sua campanha, a visualização da análise de dados permanecerá a mesma. A página **Campaign Analytics** da sua campanha mostrará o desempenho das suas variantes em comparação com o grupo de controle, caso você tenha incluído um.

![Seção de desempenho da página Campaign Analytics para uma campanha de e-mail com múltiplas variantes. A tabela lista diversas métricas de desempenho para cada variante, como destinatários, bounces, cliques e conversões.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Para mais detalhes, consulte o artigo [Análise de dados de Campanha]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics/) do seu canal de envio de mensagens.

### BrazeAI<sup>TM</sup> Variant Selection (somente push) {#brazeai-variant-selection-push-only}

Se você estiver usando BrazeAI<sup>TM</sup> Variant Selection, dependendo de ser um envio único ou uma campanha recorrente, após o término da janela do experimento (ou do primeiro período para campanhas recorrentes), você verá o aumento, se houver, na página inicial da campanha. Você também verá mais detalhes semelhantes à variante vencedora abaixo, caso execute uma campanha de envio único.

Para mais detalhes sobre como reportamos o aumento no BrazeAI<sup>TM</sup> Variant Selection, consulte [Seleção de variante]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection/).

![Resultados de aumento do BrazeAI Variant Selection]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %})

### Variante vencedora {#winning-variant}

Se você selecionou **Winning Variant** como otimização ao configurar sua campanha, você terá acesso a uma guia adicional na análise de dados da campanha chamada **A/B Test Result**. Após a variante vencedora ser enviada aos usuários restantes do seu teste, essa guia mostra os resultados desse envio.

O **A/B Test Result** é dividido em duas guias: **Initial Test** e **Winning Variant**.

{% tabs local %}
{% tab Initial Test %}

A guia **Initial Test** mostra as métricas de cada variante do teste A/B inicial enviado a uma parte do seu segmento-alvo. Você pode ver um resumo do desempenho de todas as variantes e se houve ou não uma vencedora durante o teste.

Se uma variante superou todas as outras com mais de 95% de [intervalo de confiança]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/#understanding-confidence), a Braze marca essa variante com o rótulo "Winner".

Se nenhuma variante superou todas as outras com 95% de intervalo de confiança e você optou por enviar a variante com melhor desempenho mesmo assim, a variante com melhor desempenho ainda será enviada e indicada com o rótulo "Winner".

![Resultados de um teste inicial enviado para determinar a variante vencedora, onde nenhuma variante teve desempenho melhor que as outras com intervalo de confiança suficiente para atingir o limite de 95% de significância estatística.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Como a variante vencedora é selecionada {#how-the-winning-variant-is-selected}

A Braze testa todas as variantes entre si usando [testes qui-quadrado de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Isso mede se uma variante supera estatisticamente todas as outras em um nível de significância de p < 0,05, ou o que chamamos de 95% de significância. Se sim, a variante vencedora é indicada com o rótulo "Winner".

Esse é um teste separado do intervalo de confiança, que descreve apenas o desempenho de uma variante em comparação com o controle com um valor numérico entre 0 e 100%.

Uma variante pode ter desempenho melhor que o grupo de controle, mas o teste qui-quadrado verifica se uma variante é melhor que todas as demais. [Testes de acompanhamento](#recommended-follow-ups) podem fornecer mais detalhes.

{% endtab %}
{% tab Winning Variant %}

A guia **Winning Variant** mostra os resultados do segundo envio, em que cada usuário restante recebeu a variante com melhor desempenho do teste inicial. Seu **Audience %** somará a porcentagem do segmento-alvo que você reservou para o grupo da variante vencedora.

![Resultados da variante vencedora enviada ao grupo da variante vencedora.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Se você quiser ver o desempenho da variante vencedora ao longo de toda a campanha, incluindo os envios do teste A/B, consulte a página **Campaign Analytics**.

### Variante personalizada {#personalized-variant}

Se você selecionou **Personalized Variant** como otimização ao configurar sua campanha, o **A/B Test Result** é dividido em duas guias: **Initial Test** e **Personalized Variant**.

{% tabs local %}
{% tab Initial Test %}

A guia **Initial Test** mostra as métricas de cada variante do teste A/B inicial enviado a uma parte do seu segmento-alvo.

![Resultados de um teste inicial enviado para determinar a variante com melhor desempenho para cada usuário. Uma tabela mostra o desempenho de cada variante com base em diversas métricas para o canal-alvo.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Por padrão, o teste busca associações entre os eventos personalizados dos usuários e suas preferências de variante de mensagem. Essa análise detecta se eventos personalizados aumentam ou diminuem a probabilidade de resposta a uma variante de mensagem específica. Essas relações são então usadas para determinar qual usuário recebe qual variante de mensagem no envio final.

As relações entre eventos personalizados e preferências de mensagem são exibidas na tabela da guia **Initial Send**.

![Tabela mostrando as relações entre eventos personalizados e preferências de variante de mensagem]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Se o teste não encontrar uma relação significativa entre eventos personalizados e preferências de jornada, ele recorre a um método de análise baseado em sessões, e nenhuma tabela de dados de eventos personalizados é exibida.

{% details Método de análise alternativo %}

**Método de análise baseado em sessões**<br>
Se o método alternativo for usado para determinar as variantes personalizadas, a guia **Initial Test** mostra uma divisão das variantes preferidas dos usuários com base em uma combinação de certas características.

Essas características são:

- **Recência:** Quando foi a última sessão do usuário
- **Frequência:** Com que frequência o usuário tem sessões
- **Tempo de uso:** Há quanto tempo o usuário está cadastrado

Por exemplo, o teste pode descobrir que a maioria dos usuários prefere a Variante A, mas usuários que tiveram uma sessão entre 3 e 12 dias atrás, têm entre 1 e 12 dias entre sessões e foram criados nos últimos 67 a 577 dias tendem a preferir a Variante B. Portanto, os usuários dessa subpopulação receberam a Variante B no segundo envio, enquanto os demais receberam a Variante A.

![A tabela de características do usuário, que mostra quais usuários têm previsão de preferir a Variante A e a Variante B com base nos três buckets em que se enquadram para recência, frequência e tempo de uso.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Como as variantes personalizadas são selecionadas**<br>
Com esse método, a mensagem recomendada para um usuário individual é a soma dos efeitos de sua recência, frequência e tempo de uso específicos. Recência, frequência e tempo de uso são divididos em buckets, conforme ilustrado na tabela **User Characteristics**. O intervalo de tempo de cada bucket é determinado pelos dados dos usuários em cada campanha individual e varia de campanha para campanha.

Cada bucket pode ter uma contribuição ou "impulso" diferente em direção a cada variante de mensagem. A intensidade do impulso para cada bucket é determinada pelas respostas dos usuários no envio inicial usando [regressão logística](https://en.wikipedia.org/wiki/Logistic_regression). Esta tabela apenas resume os resultados mostrando com qual variante os usuários de cada bucket tenderam a interagir. A variante personalizada real de qualquer usuário individual depende da soma dos efeitos dos três buckets em que ele se encontra — um para cada característica.

{% enddetails %}

{% endtab %}
{% tab Personalized Variant %}

A guia **Personalized Variant** mostra os resultados do segundo envio, em que cada usuário restante recebeu a variante com a qual tinha maior probabilidade de interagir.

Os três cartões nesta página mostram o aumento projetado, os resultados gerais e os resultados projetados caso você tivesse enviado apenas a variante vencedora. Mesmo que não haja aumento, o que pode acontecer às vezes, o resultado é o mesmo que enviar apenas a variante vencedora (um teste A/B tradicional).

- **Aumento projetado:** A melhoria na métrica de otimização selecionada para este envio devido ao uso de variantes personalizadas em vez de um teste A/B padrão (se os usuários restantes tivessem recebido apenas a variante vencedora).
- **Resultados gerais:** Os resultados do segundo envio com base na métrica de otimização escolhida (*Unique Opens*, *Unique Clicks* ou *Primary Conversion Event*).
- **Resultados projetados:** Os resultados projetados do segundo envio com base na métrica de otimização escolhida caso você tivesse enviado apenas a variante vencedora.

![Guia Personalized Variant para uma campanha otimizada para aberturas únicas. Os cartões mostram o aumento projetado, as aberturas únicas gerais (com variante personalizada) e as aberturas únicas projetadas (com variante vencedora).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

A tabela nesta página mostra as métricas de cada variante do envio da variante personalizada. Seu **Audience %** soma a porcentagem do segmento-alvo que você reservou para o grupo da variante personalizada.

![Tabela de métricas para cada variante do envio da variante personalizada]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Entendendo o intervalo de confiança {#understanding-confidence}

O intervalo de confiança é a medida estatística de quão certos estamos de que uma diferença nos dados, como taxas de conversão, é real e não apenas resultado do acaso.

{% alert note %}
Não está vendo o intervalo de confiança nos seus resultados? O intervalo de confiança só aparece se você tiver um grupo de controle.
{% endalert %}

Uma parte importante dos seus resultados é o intervalo de confiança. Por exemplo, e se o grupo de controle tivesse uma taxa de conversão de 20% e a Variante A tivesse uma taxa de conversão de 25%? Isso parece indicar que enviar a Variante A é mais eficaz do que não enviar nenhuma mensagem. Ter um intervalo de confiança de 95% significa que a diferença entre as duas taxas de conversão provavelmente se deve a uma diferença real nas respostas dos usuários e que há apenas 5% de probabilidade de que a diferença tenha ocorrido por acaso.

A Braze compara a taxa de conversão de cada variante com a taxa de conversão do controle usando um procedimento estatístico chamado [Teste&nbsp;Z](https://en.wikipedia.org/wiki/Z-test). Um resultado de 95% ou mais de intervalo de confiança, como no exemplo anterior, indica que a diferença é estatisticamente significativa. Isso vale para qualquer lugar no dashboard da Braze onde você veja uma métrica de intervalo de confiança que descreva a diferença entre duas mensagens ou populações de usuários.

Em geral, um intervalo de confiança de pelo menos 95% é necessário para demonstrar que seus resultados refletem as preferências reais dos usuários e não são resultado do acaso. Em testes científicos rigorosos, 95% de intervalo de confiança (ou, como é comumente referido, o valor "p" sendo menor que 0,05) é o padrão usado para determinar significância estatística. Se você não conseguir atingir 95% de intervalo de confiança repetidamente, tente aumentar o tamanho da amostra ou diminuir o número de variantes.

O intervalo de confiança não indica se uma variante é melhor que as outras. É puramente uma medida de quão certos estamos de que as duas (ou mais) taxas de conversão são realmente diferentes entre si. Isso depende apenas do tamanho da amostra e das diferenças entre as taxas de conversão aparentes. Se as taxas gerais são altas ou baixas não afeta a força da medida de intervalo de confiança. É possível que uma variante tenha uma taxa de conversão muito diferente de outra e ainda assim não tenha um intervalo de confiança de 95% ou mais. Também é possível que dois conjuntos de variantes tenham taxas de conversão/aumento semelhantes, mas intervalos de confiança diferentes.

### Resultados estatisticamente insignificantes {#statistically-insignificant-results}

Um teste que não atinge 95% de intervalo de confiança ainda pode conter insights importantes. Veja algumas coisas que você pode aprender com um teste com resultados estatisticamente insignificantes:

- É possível que todas as suas variantes tenham tido aproximadamente o mesmo efeito. Saber disso economiza o tempo que você teria gasto fazendo essas alterações. Às vezes, você pode descobrir que táticas de marketing convencionais, como repetir sua chamada para ação, não necessariamente funcionam para o seu público.
- Embora seus resultados possam ter sido resultado do acaso, eles podem orientar a hipótese do seu próximo teste. Se múltiplas variantes parecem ter resultados aproximadamente iguais, execute algumas delas novamente junto com novas variantes para ver se você consegue encontrar uma alternativa mais eficaz. Se uma variante tiver desempenho melhor, mas não de forma significativa, você pode realizar outro teste em que a diferença dessa variante seja mais acentuada.
- Continue testando! Um teste com resultados insignificantes deve levar a certas perguntas. Realmente não houve diferença entre suas variantes? Você deveria ter estruturado seu teste de forma diferente? Você pode responder a essas perguntas executando testes de acompanhamento.
- Embora os testes sejam úteis para descobrir qual tipo de mensagem gera mais resposta do seu público, também é importante entender quais alterações nas mensagens têm apenas um efeito insignificante. Isso permite que você continue testando em busca de uma alternativa mais eficaz ou economize o tempo que seria gasto decidindo entre duas mensagens alternativas.

Independentemente de o seu teste ter uma vencedora clara, pode ser útil executar um [teste de acompanhamento](#recommended-follow-ups) para confirmar seus resultados ou aplicar suas descobertas a um cenário ligeiramente diferente.

## Discrepâncias entre o grupo de controle e a variante {#discrepancies-between-the-control-group-and-variant}

Em campanhas de mensagens no app, a forma como os usuários são rastreados e como as impressões são registradas pode causar discrepâncias na divisão esperada entre o grupo de controle e a variante. Isso acontece porque as impressões reais registradas podem não refletir essa divisão, e a Braze não tem controle sobre o comportamento individual do usuário em relação a quem realizará o gatilho.

Por exemplo, digamos que uma campanha tenha um público-alvo de 200 usuários no lançamento, com 100 usuários no grupo de controle e 100 usuários na variante.

Os 100 usuários na variante recebem a carga útil da mensagem no app, e 50 deles realizam a ação-gatilho e veem a mensagem no app. Os 100 usuários no grupo de controle só são rastreados se realizarem a ação-gatilho da campanha, e 75 deles realizam a ação-gatilho e registram uma impressão, mas não veem a mensagem no app.

Apesar da divisão inicial de 50/50, as impressões únicas registradas não são equilibradas. O grupo da variante tem 50 impressões, enquanto o grupo de controle tem 75 impressões.

### Postergações de mensagens no app {#in-app-message-delays}

Para campanhas de mensagens no app disparadas que incluem exibições com postergação, as impressões do grupo de controle serão registradas quando o usuário final teria originalmente recebido a mensagem no app. Por exemplo, se uma campanha estiver configurada para postergar a exibição em uma hora, as impressões do grupo de controle não serão registradas até que a postergação de uma hora tenha passado. Isso ajuda no rastreamento preciso de impressões relacionadas ao momento pretendido da entrega da mensagem.

## Acompanhamentos recomendados {#recommended-follow-ups}

Um teste multivariante e A/B pode (e deve!) inspirar ideias para testes futuros, além de orientar mudanças na sua estratégia de envio de mensagens. Possíveis ações de acompanhamento incluem:

#### Mudar sua estratégia de envio de mensagens com base nos resultados do teste {#change-your-messaging-strategy-based-on-test-results}

Os resultados do seu teste multivariante podem levar você a mudar a forma como redige ou formata suas mensagens.

#### Mudar a forma como você entende seus usuários {#change-the-way-you-understand-your-users}

Cada teste esclarece os comportamentos dos seus usuários, como eles respondem a diferentes canais de envio de mensagens e as diferenças (e semelhanças) entre seus segmentos.

#### Melhorar a forma como você estrutura testes futuros {#improve-the-way-you-structure-future-tests}

O tamanho da sua amostra era muito pequeno? As diferenças entre suas variantes eram muito sutis? Cada teste oferece uma oportunidade de aprender como melhorar testes futuros. Se seu intervalo de confiança é baixo, o tamanho da amostra é muito pequeno e deve ser aumentado para testes futuros. Se você não encontrar uma diferença clara entre o desempenho das suas variantes, é possível que as diferenças fossem muito sutis para ter um efeito perceptível nas respostas dos usuários.

#### Executar um teste de acompanhamento com um tamanho de amostra maior {#run-a-follow-up-test-with-a-larger-sample-size}

Amostras maiores aumentam as chances de detectar pequenas diferenças entre variantes.

#### Executar um teste de acompanhamento usando um canal de envio de mensagens diferente {#run-a-follow-up-test-using-a-different-messaging-channel}

Se você descobrir que uma estratégia específica é muito eficaz em um canal, pode querer testar essa estratégia em outros canais. Se um tipo de mensagem é eficaz em um canal, mas não em outro, você pode concluir que certos canais são mais propícios a certos tipos de mensagens. Ou talvez haja uma diferença entre usuários que são mais propensos a ativar notificações por push e aqueles que são mais propensos a prestar atenção em mensagens no app. Em última análise, executar esse tipo de teste ajudará você a aprender como seu público interage com seus diferentes canais de comunicação.

#### Executar um teste de acompanhamento em um segmento diferente de usuários {#run-a-follow-up-test-on-a-different-segment-of-users}

Para fazer isso, crie outro teste com o mesmo canal de envio de mensagens e variantes, mas escolha um segmento diferente de usuários. Por exemplo, se um tipo de mensagem foi extremamente eficaz para usuários engajados, pode ser útil investigar seu efeito em usuários inativos. É possível que os usuários inativos respondam de forma semelhante, ou podem preferir outra variante. Esse teste ajudará você a aprender mais sobre seus diferentes segmentos e como eles respondem a diferentes tipos de mensagens. Por que fazer suposições sobre seus segmentos quando você pode basear sua estratégia em dados?

#### Executar um teste de acompanhamento baseado em insights de um teste anterior {#run-a-follow-up-test-based-on-insights-from-a-previous-test}

Use os insights que você obteve de testes anteriores para orientar os futuros. Um teste anterior sugere que uma técnica de envio de mensagens é mais eficaz? Você não tem certeza sobre qual aspecto específico de uma variante a tornou melhor? Executar testes de acompanhamento baseados nessas perguntas ajudará você a gerar descobertas valiosas sobre seus usuários.

#### Comparar o impacto de longo prazo de diferentes variantes {#compare-the-long-term-impact-of-different-variants}

Se você está fazendo testes A/B em mensagens de reengajamento, não se esqueça de comparar o impacto de longo prazo de diferentes variantes usando [Relatórios de retenção]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/). Você pode usar os relatórios de retenção para analisar como cada variante impactou qualquer comportamento de usuário de sua escolha dias, semanas ou um mês após o recebimento da mensagem, e verificar se houve aumento.