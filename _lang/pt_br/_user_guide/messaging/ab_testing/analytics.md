---
nav_title: Análise de dados
article_title: Análise de dados de testes A/B
page_order: 10
page_type: reference
description: "Este artigo explica como visualizar e interpretar os resultados de uma campanha multivariante ou de testes A/B."
---

# Análise de dados de testes multivariantes e A/B {#multivariate-and-ab-test-analytics}

> Este artigo explica como visualizar os resultados de um teste multivariante ou A/B. Se você ainda não configurou seu teste, consulte [Criar testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) para ver o passo a passo.

Após o lançamento da sua campanha, você pode verificar o desempenho de cada variante selecionando sua campanha na seção **Campaigns** do dashboard.

## Análise por opção de otimização {#analytics-by-optimization-option}

Sua visualização de análise varia dependendo de se você selecionou uma [otimização]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) durante sua configuração inicial.

### Distribuição manual de variantes {#manual-variant-distribution}

Se **Otimizar com BrazeAI<sup>TM</sup>** estiver desativado, a página de **Análise de dados de Campanha** mostra o desempenho das suas variantes em comparação com o grupo de controle, caso você tenha incluído um.

![Seção de desempenho da Análise de dados de Campanha para uma campanha de e-mail com múltiplas variantes. A tabela lista várias métricas de desempenho para cada variante, como destinatários, bounces, cliques e conversões.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Para saber mais, consulte o artigo [Análise de dados de Campanha]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) para seu canal de envio de mensagens.

### Otimizar com BrazeAI<sup>TM</sup> {#optimize-with-brazeai}

Se você usar **Otimizar com BrazeAI<sup>TM</sup>**, a visão geral da campanha mostra qualquer aumento após a janela do experimento para uma campanha de envio único ou após o primeiro período de otimização para uma campanha de envio múltiplo. Campanhas de envio único também mostram detalhes sobre o teste inicial e a variante com melhor desempenho.

Para saber mais, consulte [Otimizando testes A/B com BrazeAI]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

![Análise de dados de Campanha mostrando o aumento com Otimizar com BrazeAI<sup>TM</sup>, incluindo métricas de comparação após a janela do experimento.]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %})

### Otimização de envio único {#single-send-optimization}

Para uma campanha de envio único usando **Otimizar com BrazeAI<sup>TM</sup>**, a guia **Resultado do teste A/B** mostra os resultados do teste inicial e do envio otimizado.

O **Resultado do teste A/B** é dividido em duas guias: **Teste inicial** e **Variante vencedora**.

{% tabs local %}
{% tab Teste inicial %}

A guia **Teste inicial** mostra as métricas de cada variante do teste A/B inicial enviado a uma parte do seu Segment-alvo. Você pode ver um resumo de como todas as variantes se saíram e se houve ou não uma vencedora durante o teste.

Se uma variante superou todas as outras com mais de 95% de [confiança]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#understanding-confidence), a Braze marca essa variante com o rótulo "Vencedora".

Se nenhuma variante superar todas as outras com 95% de confiança e você optar por enviar a variante com melhor desempenho mesmo assim, a variante com melhor desempenho ainda será enviada e indicada com o rótulo "Vencedora".

![Resultados de um teste inicial enviado para determinar a variante vencedora, em que nenhuma variante teve desempenho superior às outras com confiança suficiente para atingir o limite de 95% de confiança para significância estatística.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Como a variante vencedora é selecionada {#how-the-winning-variant-is-selected}

A Braze testa todas as variantes umas contra as outras com [testes qui-quadrado de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Isso mede se uma variante supera estatisticamente todas as outras em um nível de significância de p < 0,05, ou o que chamamos de 95% de significância. Se sim, a variante vencedora é indicada com o rótulo "Vencedora".

Esse é um teste separado da pontuação de confiança, que descreve apenas o desempenho de uma variante em comparação com o grupo de controle com um valor numérico entre 0 e 100%.

Uma variante pode ter desempenho melhor que o grupo de controle, mas o teste qui-quadrado verifica se uma variante é melhor que todas as demais. [Testes de acompanhamento](#recommended-follow-ups) podem fornecer mais detalhes.

{% endtab %}
{% tab Variante vencedora %}

A guia **Variante vencedora** mostra os resultados do segundo envio, em que cada usuário restante recebeu a variante com melhor desempenho do teste inicial. Seu **% do público** somará a porcentagem do Segment-alvo que você reservou para o grupo da variante vencedora.

![Resultados da variante vencedora enviada ao grupo da variante vencedora.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Se você quiser ver o desempenho da variante vencedora ao longo de toda a campanha, incluindo os envios do teste A/B, consulte a página de **Análise de dados de Campanha**.

### Campanhas existentes com variante personalizada {#personalized-variant}

A variante personalizada não está disponível para novas campanhas. Para uma campanha existente que usa essa otimização, o **Resultado do teste A/B** é dividido em duas guias: **Teste inicial** e **Variante personalizada**.

{% tabs local %}
{% tab Teste inicial %}

A guia **Teste inicial** mostra as métricas de cada variante do teste A/B inicial enviado a uma parte do seu Segment-alvo.

![Resultados de um teste inicial enviado para determinar a variante com melhor desempenho para cada usuário. Uma tabela mostra o desempenho de cada variante com base em várias métricas para o canal-alvo.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Por padrão, o teste procura associações entre os eventos personalizados de cada usuário e suas preferências de variante de mensagem. Essa análise detecta se eventos personalizados aumentam ou diminuem a probabilidade de responder a uma variante de mensagem específica. Essas relações são então usadas para determinar quais usuários recebem qual variante de mensagem no envio final.

As relações entre eventos personalizados e preferências de mensagem são exibidas na tabela na guia **Envio inicial**.

![Tabelas de dados de eventos personalizados para a Variante 1 e Variante 2 mostrando pontuações de impacto de eventos personalizados que indicam como cada evento influencia a preferência de variante.]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Se o teste não encontrar uma relação significativa entre eventos personalizados e preferências de jornada, o teste recorre a um método de análise baseado em sessões, e nenhuma tabela de dados de eventos personalizados é exibida.

{% details Método de análise de fallback %}

**Método de análise baseado em sessões**<br>
Se o método de fallback for usado para determinar as variantes personalizadas, a guia **Teste inicial** mostra uma divisão das variantes preferidas dos usuários com base em uma combinação de certas características.

Essas características são:

- **Recência:** Quando tiveram a última sessão
- **Frequência:** Com que frequência têm sessões
- **Tempo de uso:** Há quanto tempo são usuários

Por exemplo, o teste pode descobrir que a maioria dos usuários prefere a Variante A, mas usuários que tiveram uma sessão entre 3 e 12 dias atrás, que têm entre 1 e 12 dias entre sessões e que foram criados nos últimos 67 a 577 dias tendem a preferir a Variante B. Portanto, usuários nessa subpopulação receberam a Variante B no segundo envio, enquanto os demais receberam a Variante A.

![A tabela de Características do Usuário, que mostra quais usuários têm previsão de preferir a Variante A e a Variante B com base nos três buckets em que se enquadram para recência, frequência e tempo de uso.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Como as variantes personalizadas são selecionadas**<br>
Com esse método, a mensagem recomendada para um usuário individual é a soma dos efeitos de sua recência, frequência e tempo de uso específicos. Recência, frequência e tempo de uso são divididos em buckets, conforme ilustrado na tabela de **Características do Usuário**. O intervalo de tempo de cada bucket é determinado pelos dados dos usuários em cada campanha individual e varia de campanha para campanha.

Cada bucket pode ter uma contribuição ou "impulso" diferente em direção a cada variante de mensagem. A intensidade do impulso para cada bucket é determinada pelas respostas dos usuários no envio inicial usando [regressão logística](https://en.wikipedia.org/wiki/Logistic_regression). Esta tabela apenas resume os resultados exibindo com qual variante os usuários em cada bucket tenderam a interagir. A variante personalizada real de qualquer usuário individual depende da soma dos efeitos dos três buckets em que ele se encontra — um para cada característica.

{% enddetails %}

{% endtab %}
{% tab Variante personalizada %}

A guia **Variante personalizada** mostra os resultados do segundo envio, em que cada usuário restante recebeu a variante com a qual tinha mais probabilidade de interagir.

Os três cartões nesta página mostram o aumento projetado, os resultados gerais e os resultados projetados caso você tivesse enviado apenas a variante vencedora. Mesmo que não haja aumento, o que pode acontecer ocasionalmente, o resultado é o mesmo que enviar apenas a variante vencedora (um teste A/B tradicional).

- **Aumento projetado:** A melhoria na sua métrica de otimização selecionada para este envio devido ao uso de variantes personalizadas em vez de um teste A/B padrão (se os usuários restantes tivessem recebido apenas a variante vencedora).
- **Resultados gerais:** Os resultados do segundo envio com base na sua métrica de otimização escolhida (*Aberturas únicas*, *Cliques únicos* ou *Evento de conversão primária*).
- **Resultados projetados:** Os resultados projetados do segundo envio com base na sua métrica de otimização escolhida caso você tivesse enviado apenas a variante vencedora.

![Guia Variante personalizada para uma campanha otimizada para aberturas únicas. Os cartões mostram o aumento projetado, as aberturas únicas gerais (com variante personalizada) e as aberturas únicas projetadas (com variante vencedora).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

A tabela nesta página mostra as métricas de cada variante do envio da variante personalizada. Seu **% do público** soma a porcentagem do Segment-alvo que você reservou para o grupo de variante personalizada.

![Tabela de resultados do envio da variante personalizada mostrando métricas de desempenho para Variante A, Variante B e Todas as variações, incluindo porcentagem do público, envios, entregas, aberturas, cliques e conversões.]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Entendendo a confiança {#understanding-confidence}

A confiança é a medida estatística de quão certos estamos de que uma diferença nos dados, como taxas de conversão, é real e não apenas resultado do acaso.

{% alert note %}
Não está vendo a confiança nos seus resultados? A confiança só aparece se você tiver um grupo de controle.
{% endalert %}

Uma parte importante dos seus resultados é a confiança. Por exemplo, e se o grupo de controle tivesse uma taxa de conversão de 20% e a Variante A tivesse uma taxa de conversão de 25%? Isso parece indicar que enviar a Variante A é mais eficaz do que não enviar nenhuma mensagem. Ter uma confiança de 95% significa que a diferença entre as duas taxas de conversão provavelmente se deve a uma diferença real nas respostas dos usuários e que há apenas 5% de probabilidade de que a diferença tenha ocorrido por acaso.

A Braze compara a taxa de conversão de cada variante com a taxa de conversão do controle usando um procedimento estatístico chamado [Teste&nbsp;Z](https://en.wikipedia.org/wiki/Z-test). Um resultado de 95% ou mais de confiança, como no exemplo anterior, indica que a diferença é estatisticamente significativa. Isso vale para qualquer lugar no dashboard da Braze onde você veja uma métrica de confiança que descreva a diferença entre duas mensagens ou populações de usuários.

Em geral, uma confiança de pelo menos 95% é necessária para demonstrar que seus resultados refletem as preferências reais dos usuários e não são resultado do acaso. Em testes científicos rigorosos, 95% de confiança (ou, como é comumente referido, o valor "p" sendo menor que 0,05) é o padrão usado para determinar significância estatística. Se você não conseguir atingir 95% de confiança repetidamente, tente aumentar o tamanho da amostra ou diminuir o número de variantes.

A confiança reflete a probabilidade de que uma diferença observada entre as taxas de conversão da variante e do controle seja real, e não resultado do acaso. Ela depende do tamanho da amostra e da magnitude da diferença entre as taxas de conversão. Se as taxas gerais de conversão são altas ou baixas normalmente é menos importante do que a diferença observada e o tamanho da amostra para determinar a força da medida de confiança. É possível que uma variante tenha uma taxa de conversão muito diferente de outra e ainda assim não tenha uma confiança de 95% ou mais. Também é possível que dois conjuntos de variantes tenham taxas de conversão ou aumento semelhantes, mas confiança diferente.

À medida que mais dados chegam, a confiança pode diminuir se as taxas de conversão da variante e do controle se aproximarem — a diferença que você está medindo está ficando menor, o que pode superar o efeito de uma amostra maior.

### Resultados estatisticamente insignificantes {#statistically-insignificant-results}

Um teste que não atinge 95% de confiança ainda pode conter insights importantes. Veja algumas coisas que você pode aprender com um teste com resultados estatisticamente insignificantes:

- É possível que todas as suas variantes tenham tido aproximadamente o mesmo efeito. Saber disso economiza o tempo que você teria gasto fazendo essas alterações. Às vezes, você pode descobrir que táticas de marketing convencionais, como repetir sua chamada para ação, não necessariamente funcionam para o seu público.
- Embora seus resultados possam ter sido resultado do acaso, eles podem orientar a hipótese do seu próximo teste. Se múltiplas variantes parecem ter resultados aproximadamente iguais, execute algumas delas novamente junto com novas variantes para ver se você consegue encontrar uma alternativa mais eficaz. Se uma variante tiver desempenho melhor, mas não de forma significativa, você pode realizar outro teste em que a diferença dessa variante seja mais acentuada.
- Continue testando! Um teste com resultados insignificantes deve levar a certas perguntas. Realmente não houve diferença entre suas variantes? Você deveria ter estruturado seu teste de forma diferente? Você pode responder a essas perguntas executando testes de acompanhamento.
- Embora os testes sejam úteis para descobrir qual tipo de mensagem gera mais resposta do seu público, também é importante entender quais alterações nas mensagens têm apenas um efeito insignificante. Isso permite que você continue testando em busca de uma alternativa mais eficaz ou economize o tempo que seria gasto decidindo entre duas mensagens alternativas.

Independentemente de o seu teste ter uma vencedora clara, pode ser útil executar um [teste de acompanhamento](#recommended-follow-ups) para confirmar seus resultados ou aplicar suas descobertas a um cenário ligeiramente diferente.

## Discrepâncias entre o grupo de controle e a variante {#discrepancies-between-the-control-group-and-variant}

Em campanhas de mensagens no app com divisões A/B ou multivariantes, as porcentagens que você configura são metas de atribuição. As impressões reportadas raramente correspondem exatamente a essas porcentagens, porque apenas os usuários que realizam a ação-gatilho registram impressões, e os usuários do grupo de controle que disparam o gatilho registram uma impressão mesmo sem ver a mensagem.

Por exemplo, digamos que uma campanha tenha um público-alvo de 200 usuários no lançamento, com 100 usuários no grupo de controle e 100 usuários na variante.

Os 100 usuários na variante recebem a carga útil da mensagem no app, e 50 deles realizam a ação-gatilho e veem a mensagem no app. Os 100 usuários no grupo de controle só são rastreados se realizarem a ação-gatilho da campanha, e 75 deles realizam a ação-gatilho e registram uma impressão, mas não veem a mensagem no app.

Apesar da divisão inicial de 50/50, as impressões únicas registradas não são equilibradas. O grupo da variante tem 50 impressões, enquanto o grupo de controle tem 75 impressões.

Além disso, mensagens de variante que exigem mais tempo de renderização, como aquelas com imagens grandes ou Connected Content com templates, podem registrar menos impressões do que o grupo de controle quando os usuários disparam a mensagem, mas saem antes que a renderização seja concluída.

### Postergações de mensagens no app {#in-app-message-delays}

Para campanhas de mensagens no app disparadas que incluem exibições com postergação, as impressões do grupo de controle serão registradas quando o usuário final teria originalmente recebido a mensagem no app. Por exemplo, se uma campanha estiver configurada para postergar a exibição em uma hora, as impressões do grupo de controle não serão registradas até que a postergação de uma hora tenha passado. Isso ajuda no rastreamento preciso de impressões relacionadas ao momento pretendido da entrega da mensagem.

## Removendo variantes de mensagem após o lançamento {#removing-message-variants-after-launch}

Se você remover uma variante de mensagem de uma campanha ou Canvas clicando no **X** no criador (por exemplo, ao substituir uma mensagem de um modelo), a variante será marcada como excluída. A análise de dados está vinculada ao ID exclusivo de cada variante, então a remoção de uma variante afeta os relatórios:

- A análise de dados pré-existente da variante excluída (como aberturas, cliques e conversões) não aparece mais na análise de dados da campanha atual ou da etapa do Canvas.
- Os detalhamentos por variante excluem variantes excluídas. Se você adicionar uma variante substituta, ela receberá um novo ID de variante e começará sem dados históricos, então as métricas podem aparecer como 0.

Isso se aplica apenas quando você exclui e adiciona variantes novamente. Editar o conteúdo de uma variante existente no lugar não afeta a análise de dados histórica.

Para saber mais sobre variantes excluídas em relatórios, consulte [Variantes de mensagem excluídas]({{site.baseurl}}/user_guide/analytics/reports/report_builder#deleted-message-variants).

## Acompanhamentos recomendados {#recommended-follow-ups}

Um teste multivariante e A/B pode (e deve!) inspirar ideias para testes futuros, além de orientar mudanças na sua estratégia de envio de mensagens. Possíveis ações de acompanhamento incluem:

### Mudar sua estratégia de envio de mensagens com base nos resultados do teste {#change-your-messaging-strategy-based-on-test-results}

Os resultados do seu teste multivariante podem levar você a mudar a forma como redige ou formata suas mensagens.

### Mudar a forma como você entende seus usuários {#change-the-way-you-understand-your-users}

Cada teste esclarece os comportamentos dos seus usuários, como eles respondem a diferentes canais de envio de mensagens e as diferenças (e semelhanças) entre seus segmentos.

### Melhorar a forma como você estrutura testes futuros {#improve-the-way-you-structure-future-tests}

O tamanho da sua amostra era muito pequeno? As diferenças entre suas variantes eram muito sutis? Cada teste oferece uma oportunidade de aprender como melhorar testes futuros. Se sua confiança é baixa, o tamanho da amostra é muito pequeno e deve ser aumentado para testes futuros. Se você não encontrar uma diferença clara entre o desempenho das suas variantes, é possível que as diferenças fossem muito sutis para ter um efeito perceptível nas respostas dos usuários.

### Executar um teste de acompanhamento com um tamanho de amostra maior {#run-a-follow-up-test-with-a-larger-sample-size}

Amostras maiores aumentam as chances de detectar pequenas diferenças entre variantes.

### Executar um teste de acompanhamento usando um canal de envio de mensagens diferente {#run-a-follow-up-test-using-a-different-messaging-channel}

Se você descobrir que uma estratégia específica é muito eficaz em um canal, pode querer testar essa estratégia em outros canais. Se um tipo de mensagem é eficaz em um canal, mas não em outro, você pode concluir que certos canais são mais propícios a certos tipos de mensagens. Ou talvez haja uma diferença entre usuários que são mais propensos a ativar notificações por push e aqueles que são mais propensos a prestar atenção em mensagens no app. Em última análise, executar esse tipo de teste ajudará você a aprender como seu público interage com seus diferentes canais de comunicação.

### Executar um teste de acompanhamento em um Segment diferente de usuários {#run-a-follow-up-test-on-a-different-segment-of-users}

Para fazer isso, crie outro teste com o mesmo canal de envio de mensagens e variantes, mas escolha um Segment diferente de usuários. Por exemplo, se um tipo de mensagem foi extremamente eficaz para usuários engajados, pode ser útil investigar seu efeito em usuários inativos. É possível que os usuários inativos respondam de forma semelhante, ou podem preferir outra variante. Esse teste ajudará você a aprender mais sobre seus diferentes segmentos e como eles respondem a diferentes tipos de mensagens. Por que fazer suposições sobre seus segmentos quando você pode basear sua estratégia em dados?

### Executar um teste de acompanhamento baseado em insights de um teste anterior {#run-a-follow-up-test-based-on-insights-from-a-previous-test}

Use os insights que você obteve de testes anteriores para orientar os futuros. Um teste anterior sugere que uma técnica de envio de mensagens é mais eficaz? Você não tem certeza sobre qual aspecto específico de uma variante a tornou melhor? Executar testes de acompanhamento baseados nessas perguntas ajudará você a gerar descobertas valiosas sobre seus usuários.

### Comparar o impacto de longo prazo de diferentes variantes {#compare-the-long-term-impact-of-different-variants}

Se você está fazendo testes A/B em mensagens de reengajamento, não se esqueça de comparar o impacto de longo prazo de diferentes variantes usando [Relatórios de retenção]({{site.baseurl}}/user_guide/analytics/reports/retention_reports). Você pode usar os relatórios de retenção para analisar como cada variante impactou qualquer comportamento de usuário de sua escolha dias, semanas ou um mês após o recebimento da mensagem, e verificar se houve aumento.