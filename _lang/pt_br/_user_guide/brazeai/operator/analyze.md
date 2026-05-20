---
nav_title: Analisar
article_title: Operator Analyze
page_order: 100
description: "Faça perguntas em linguagem natural sobre o engajamento dos seus canais, receita atribuída e como você se compara aos benchmarks do setor. Você recebe gráficos, comparações e insights práticos em segundos."
page_type: reference
hidden: true
---

# Operator Analyze {#operator-analyze}

> O Operator Analyze responde a perguntas de desempenho em linguagem natural no BrazeAI Operator<sup>TM</sup>. As respostas incluem gráficos, comparações e insights curtos. Você não precisa criar um dashboard nem gerar um relatório completo antes.

{% alert important %}
O Operator Analyze está atualmente em beta. Os recursos e as análises compatíveis estão em evolução. Para solicitar acesso para a sua conta, entre em contato com o seu gerente de sucesso do cliente.
{% endalert %}

## Por que usar o Operator Analyze? {#why-use-operator-analyze}

A maioria das perguntas sobre desempenho ainda exige trocar de ferramenta, criar visualizações ou esperar por outra pessoa. Exemplos incluem "Como foi a semana passada?", "Estamos dentro do benchmark?" e "Qual Campaign está gerando os melhores resultados?"

O Operator Analyze cobre métricas de engajamento, *Receita Atribuída* e benchmarks do setor. São os mesmos dados que você normalmente extrairia para um relatório ou dashboard. Pergunte com suas próprias palavras no painel do Operator. Você recebe um gráfico, uma comparação ranqueada ou uma tabela, além de um a cinco insights práticos.

## Acessar o Operator Analyze {#access-operator-analyze}

O Operator Analyze funciona no painel de conversa do Operator.

1. Selecione **BrazeAI Operator<sup>TM</sup>** ao lado do seu perfil de usuário em qualquer página do dashboard da Braze.
2. Pergunte sobre engajamento de canal ou comparações com benchmarks (veja [Exemplos de perguntas](#example-questions)).
3. O Operator retorna a resposta e, quando útil, um gráfico ou tabela e uma lista curta de insights.

Para saber mais sobre o painel de chat do Operator, consulte [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/).

## Exemplos de perguntas {#example-questions}

Descreva o que você quer saber. Não é necessário usar uma formulação fixa. Selecione uma guia para ver exemplos de prompts.

{% tabs %}
{% tab Comparações com benchmarks %}

* "Como a nossa *taxa de abertura* de e-mail se compara aos benchmarks do setor nos últimos 30 dias?"
* "Estamos acima ou abaixo do benchmark para *taxa de cliques* de SMS neste trimestre?"
* "Onde estamos abaixo do desempenho do setor no nosso mix de canais?"

{% endtab %}
{% tab Visões gerais de canal %}

* "Quais canais estão com melhor desempenho para nós no FY26 até agora?"
* "Detalhe o engajamento por canal nos últimos 90 dias."
* "Quanta *Receita Atribuída* cada canal de marketing gerou no último trimestre?"

{% endtab %}
{% tab Detalhamento de Campaigns e Canvas %}

* "Quais são as nossas 10 melhores Campaigns de e-mail por *taxa de cliques* neste trimestre fiscal?"
* "Quais Canvas geraram mais *Cliques* no mês passado?"
* "Quais Campaigns geraram mais *Receita Atribuída* no Q1 do FY26?"
* "Mostre as nossas Campaigns de push com pior desempenho nos últimos 30 dias."

{% endtab %}
{% tab Análise de tendências %}

* "Qual é a tendência mês a mês do engajamento de push no FY26?"
* "Como a *taxa de cliques* de e-mail mudou trimestre a trimestre no último ano?"
* "Como a nossa *Receita Atribuída* evoluiu nos últimos 12 meses?"
* "Mostre a tendência semanal de engajamento para mensagens no app nos últimos 90 dias."

{% endtab %}
{% tab Receita e conversões %}

Pergunte sobre *Receita Atribuída* e *Conversões* agregadas no nível de Campaign, Canvas, canal ou programa.

* "Compare *Receita Atribuída* e *Conversões* do trimestre mais recente com o trimestre anterior."
* "Quais Campaigns geraram mais *Receita Atribuída* nos últimos 90 dias?"
* "Detalhe a *Receita Atribuída* por canal no FY26 até agora."

{% endtab %}
{% tab Revisões abrangentes %}

* "Faça uma revisão completa do nosso programa de engajamento com recomendações."
* "Onde estão as nossas maiores oportunidades e riscos entre os canais agora?"

{% endtab %}
{% endtabs %}

## Visualizações {#visualizations}

O Operator adiciona um gráfico quando os dados permitem. **Gráficos de linha** são ideais para séries temporais, **gráficos de barra** para comparações entre categorias e **tabelas** para os demais casos. As tabelas mostram porcentagens com duas casas decimais e usam vírgulas para números grandes.

Quando uma resposta inclui múltiplas métricas, o Operator prioriza taxas de engajamento (*taxa de abertura*, *taxa de cliques*, *taxa de abertura de push*) em vez de contagens brutas.

## Canais e métricas compatíveis {#supported-channels-and-metrics}

*Receita Atribuída* e *Conversões* usam a mesma agregação por Campaign, Canvas, canal e programa mostrada em [Exemplos de perguntas](#example-questions) na guia **Receita e conversões**.

| Canal | Métricas | Benchmarks do setor |
| --- | --- | --- |
| E-mail | *Envios*, *Entregas*, *Aberturas Únicas*, *Cliques Únicos*, *Cancelamentos de inscrição* | Sim |
| Push (iOS, Android, Web) | *Envios*, *Entregas*, *Aberturas* | Sim |
| SMS | *Envios*, *Entregas*, *Cliques em links* | Sim |
| In-App Messages | *Impressões*, *Cliques* | Sim |
| Content Cards | *Envios*, *Impressões*, *Cliques* | Sim |
| WhatsApp | *Envios*, *Entregas*, *Leituras*, *Cliques* | Ainda não |
| RCS | *Envios*, *Entregas*, *Leituras*, *Cliques* (incluindo subtipos de URL de texto, botão, ação, ação de resposta e botão de resposta) | Ainda não |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Supported channels, metrics, and benchmark availability" }

{% alert tip %}
O Operator usa contagens únicas para taxas (por exemplo, *Aberturas Únicas* divididas por *Entregas* para *taxa de abertura de e-mail*). Se um valor diferir de um dashboard, compare a janela de atribuição, o período e a definição. O Operator lista os três em cada resposta.
{% endalert %}

## Períodos e janelas de atribuição {#time-periods-and-attribution-windows}

### Ano fiscal vs. ano calendário {#fiscal-year-vs-calendar-year}

O Operator Analyze usa por padrão o **ano fiscal da Braze**, que vai de 1º de fevereiro a 31 de janeiro.

| Trimestre fiscal | Meses |
| --- | --- |
| FQ1 | Fev – Abr |
| FQ2 | Mai – Jul |
| FQ3 | Ago – Out |
| FQ4 | Nov – Jan |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze fiscal quarters and calendar months" }

Para perguntas sobre o ano calendário, inclua "CY", "calendar year" ou "standard year". Prompts ambíguos como "last year" fazem o Operator confirmar qual calendário você quer dizer.

Você também pode usar intervalos no formato ISO, como `Q4 2025` ou `2025-03-01 to 2025-05-31`.

### Janelas de atribuição {#attribution-windows}

O Operator Analyze usa por padrão **7 dias**. Especifique uma janela na sua pergunta para alterar:

* **1 dia** para verificações rápidas de engajamento
* **3 dias** para Campaigns de ciclo curto
* **7 dias** para visões gerais e leituras de Campaigns (padrão)
* **30 dias** para visões estratégicas ou de longo prazo
* **Todas as janelas** para uma comparação lado a lado de 1D / 3D / 7D / 30D

Se os resultados diferirem em mais de 50% entre as janelas, o Operator mostra as quatro lado a lado.

## Atualização dos dados {#data-freshness}

Os dados são atualizados diariamente. A atividade do mesmo dia aparece após a próxima atualização. Cada resposta informa a data mais recente no conjunto de dados. Se essa data parecer desatualizada, entre em contato com o seu gerente de sucesso do cliente.

## O que está fora do escopo {#whats-out-of-scope}

* **Detalhamento de desempenho por produto.** *Receita Atribuída* e engajamento são agregados no nível de Campaign, Canvas, canal ou programa. Eles não são detalhados por produtos ou SKUs. Perguntas no nível de produto ou SKU não são compatíveis. Entre em contato com o seu gerente de sucesso do cliente para essas análises.
* **Benchmarks do setor para WhatsApp e RCS.** As métricas de engajamento para ambos os canais são compatíveis. Os benchmarks ainda não estão disponíveis.

Perguntas fora do escopo recebem uma resposta direta, uma alternativa sugerida quando possível ou um direcionamento para o seu gerente de sucesso do cliente.

## Dicas para melhores resultados {#tips-for-better-results}

* **Período:** Prefira intervalos explícitos ("FY26 Q2", "os últimos 90 dias") em vez de frases vagas como "último trimestre" quando precisar de precisão.
* **Métricas:** Nomeie a taxa que você quer (*taxa de abertura*, *taxa de cliques*, *taxa de clique por abertura*). O Operator informa a fórmula utilizada.
* **Perguntas de acompanhamento:** Aprofunde-se em um resultado, mude a janela ou troque de canal. O Operator mantém o contexto ao longo da conversa.
* **Nomenclatura de canal:** WhatsApp e RCS usam *taxa de leitura* (não *taxa de abertura*). SMS usa *taxa de cliques em links*.
* **Perguntas combinadas:** Benchmark mais tendência em um único prompt é compatível.

## Privacidade e segurança dos dados {#data-privacy-and-security}

O Operator Analyze segue o mesmo modelo de privacidade e segurança do BrazeAI Operator<sup>TM</sup>. Para saber mais, consulte [Privacidade e segurança dos dados]({{site.baseurl}}/user_guide/brazeai/operator/#data-privacy-and-security).

## Próximas etapas {#next-steps}

* [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/)
* [Revisar ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/)