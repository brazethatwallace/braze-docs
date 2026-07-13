---
nav_title: Relatórios de retenção
article_title: Relatórios de retenção para Campaigns e Canvas
page_order: 9
tool: Reports
page_type: reference
description: "Esta página explica como medir a retenção de usuários que realizaram um evento de retenção selecionado em uma Campaign ou Canvas específico."
---

# Relatórios de retenção {#retention-reports}

> A retenção de usuários é uma das métricas mais importantes para qualquer profissional de marketing. Manter os usuários engajados voltando para mais indica que o negócio está saudável. A Braze permite que você meça a retenção de usuários diretamente na página **Analytics** da sua Campaign ou Canvas.

{% alert important %}
Os relatórios de retenção não estão disponíveis para Campaigns disparadas por API.
{% endalert %}

## Executando um relatório de retenção {#running-a-retention-report}

### Etapa 1: Selecione um intervalo de datas {#step-1-select-a-date-range}

![Data do relatório]({% image_buster /assets/img/date_select_retention.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Comece acessando qualquer Campaign ou Canvas no seu dashboard da Braze e selecione um intervalo de datas para o seu relatório. Selecionar um intervalo de datas adequado é crucial por causa da forma como ele afeta os relatórios de retenção.

Este relatório incluirá todos os usuários que entraram inicialmente na Campaign ou Canvas durante esse período e, desses usuários, os dados daqueles que realizaram o evento de retenção durante o intervalo de datas aparecerão no relatório.

Para selecionar um intervalo de datas, navegue até a página **Analytics** da Campaign ou Canvas e selecione vários intervalos ou defina um intervalo personalizado para o seu relatório.

### Etapa 2: Selecione um evento de retenção {#step-2-select-a-retention-event}

{% tabs %}
{% tab Campaign %}

Em seguida, vá até a seção **Campaign Retention**. A retenção da Campaign mostra a taxa na qual qualquer usuário que recebeu essa Campaign específica realizou um evento de retenção (especificado por você no relatório de retenção) ao longo dos 30 dias a partir do momento em que recebeu a Campaign.

{% endtab %}
{% tab Canvas %}

Em seguida, selecione **Analyze Variants**. A partir daqui, você pode analisar suas variantes, conferir seu relatório de funil e visualizar seu relatório de retenção. A retenção do Canvas mostra a taxa na qual qualquer usuário que recebeu esse Canvas específico realizou um evento de retenção (especificado por você no relatório de retenção) ao longo dos 30 dias a partir do momento em que recebeu o Canvas.

{% endtab %}
{% endtabs %}

![Selecione um evento de retenção]({% image_buster /assets/img/retention_1.png %}){: style="max-width:80%"}

### Etapa 3: Gere o relatório {#step-3-generate-the-report}

Depois de selecionar um evento de retenção, selecione **Run Report** para iniciar a consulta.

![Executar relatório]({% image_buster /assets/img/retention_2.png %}){: style="max-width:80%"}

Essa consulta pode levar alguns minutos para ser executada, dependendo da quantidade de dados que precisam ser recuperados para gerar os resultados. Se demorar muito, você verá uma notificação pedindo para tentar carregar o relatório novamente. Pode ser necessário aguardar até cinco minutos antes que o relatório seja carregado.

Depois que o relatório for gerado, ele não poderá ser executado novamente com o mesmo evento de retenção por 24 horas. Você sempre verá um registro de data e hora de quando o relatório foi gerado pela última vez e uma opção para regenerá-lo, caso tenha se passado mais de um dia. No entanto, você pode alterar o evento de retenção e executar o relatório novamente para analisar o impacto da Campaign em diferentes KPIs.

O relatório listará apenas os dias em que a Campaign ou Canvas estava enviando mensagens. Para algumas Campaigns e Canvas, isso pode significar que o relatório mostra apenas um dia, caso tenha sido enviado apenas uma vez. Se for recorrente ou disparado, você poderá ver vários dias na tabela.

{% tabs %}
{% tab Campaign %}

![Relatório completo]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Relatório completo]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Explicação do relatório {#report-explanation}

O relatório de retenção oferece tanto uma fórmula de retenção contínua quanto uma de retenção por intervalo. Para visualizar o relatório da sua Campaign ou Canvas com um desses tipos de retenção, selecione **Rolling Retention** ou **Range Retention** em **Type of Retention**.

### Retenção contínua {#rolling-retention}

A retenção contínua mede quantos usuários retornam e realizam o evento de retenção em ou após qualquer um dos dias listados no topo do relatório. Portanto, se um usuário iniciou uma sessão entre os dias três e sete, ele será contado como retido nas colunas "3 dias", "1 dia" e "0 dias". Qualquer usuário contado como retido após a marca de 30 dias a partir do envio da Campaign ou Canvas será contado na coluna "30 dias" naquela linha.

Um usuário que completa o evento várias vezes durante um período de 30 dias ou mais será contado como parte de múltiplos intervalos de tempo. Por exemplo, um usuário que completa uma sessão após um dia será incrementado nas colunas para >0 e >1. Se ele completar o evento novamente após três dias, será novamente incrementado nas colunas anteriores (>0 e >1), o que pode resultar em uma taxa de retenção superior a 100%.

#### Como ler relatórios de retenção contínua {#how-to-read-rolling-retention-reports}

A forma de ler o gráfico do relatório de retenção para uma coluna de dia três seria: Y% ou Y número de usuários (com base nas unidades escolhidas) realizaram o evento três ou mais dias após receber a Campaign no dia Z.

![Relatório contínuo]({% image_buster /assets/img/campaign_retention3.png %})

Como outro exemplo, referindo-se à tabela na imagem anterior, em 25 de março, um total de 38 usuários realizaram o evento de retenção. A retenção do dia zero foi de 68,42%, o que significa que 68,42% dos usuários realizaram o evento de retenção zero ou mais dias (no dia zero ou depois) após receber a Campaign. A retenção do dia sete foi de 57,89%, o que significa que 57,89% dos usuários realizaram o evento sete ou mais dias (no dia sete ou depois) após receber a Campaign.

Essa informação pode ser útil se você quiser saber a porcentagem de usuários que usaram e que não usaram seu produto 30 dias ou mais após o primeiro uso. Um valor de porcentagem ou número na coluna do dia 30 indica a porcentagem de usuários que retornaram no dia 30 ou depois.

### Retenção por intervalo {#range-retention}

A retenção por intervalo mede quantos usuários retornam no intervalo de dias listado no topo do relatório. Portanto, se um usuário iniciou uma sessão entre os dias três e sete e novamente no dia 13, ele seria contado como retido nos intervalos "Dia 3-7" e "Dia 7-14".

#### Como ler relatórios de retenção por intervalo {#how-to-read-range-retention-reports}

Os relatórios por intervalo são alguns dos relatórios mais intuitivos de ler. Eles indicam claramente, de todos os usuários em uma coorte, qual porcentagem desses usuários realizou o evento de retenção dentro de um determinado intervalo de datas. Por exemplo, na imagem a seguir, referenciando a coorte Todos os usuários, no intervalo de datas "Dia 0 (0-24h)", 35,71% da coorte realizou o evento de retenção. Se um usuário realiza múltiplos eventos de retenção dentro de múltiplos intervalos de datas, ele será contado como retido para cada intervalo.

![Relatório de retenção]({% image_buster /assets/img/range_retention.png %})

### Componentes do relatório de retenção {#retention-report-components}

- **Coluna de usuários**: O valor exibido é o número de usuários únicos que realizaram a ação inicial dentro do período selecionado; a contagem de usuários para o dia atual será excluída, pois está sendo calculada.
- **Linhas da coorte Z**: Mostra os dias em que a Campaign ou Canvas estava enviando mensagens.
- **Colunas do dia X**: Dias variando entre 0 e 30 dias em diversos incrementos.
- **Linha Todos os usuários**: Também conhecida como linha de resumo do relatório, resume os dados de retenção para todo o período. Observe que, se um usuário recebeu a Campaign ou Canvas em múltiplas coortes, seus resultados serão contados duas vezes aqui.
- **Porcentagens/Números**: Mostra a porcentagem ou o número de usuários que realizaram o evento X ou mais dias após receber a Campaign ou Canvas no dia Z. Essas porcentagens são as médias ponderadas. Valores incompletos serão indicados por um asterisco.
- **Intervalo de datas**: Definido na página **Details** da Campaign ou Canvas, o intervalo de datas inclui todos os usuários que receberam a Campaign ou Canvas durante esse período e, desses usuários, os dados daqueles que realizaram o evento de retenção durante o intervalo de datas aparecerão no relatório.
- **Unidades**: Você pode ajustar as unidades entre a porcentagem de usuários e o número de usuários nos controles do gráfico. Unidades específicas podem ser mais significativas ao avaliar o impacto de uma Campaign ou Canvas.
- **Mapeamento de cores**: No seu relatório de retenção, porcentagens ou números de usuários mais altos recebem tons mais escuros de azul. Porcentagens ou números de usuários mais baixos recebem tons mais claros de azul. Isso é feito para ajudar os usuários a visualizar esses dados.
- **Gráfico do relatório de retenção**: Este gráfico resume os resultados de todas as coortes para o intervalo de datas selecionado.

### Desempenho por variante {#performance-by-variant}

Visualizar seu relatório de retenção por variante permite comparar a retenção contínua para cada variante ou variação de mensagem no período selecionado, bem como o grupo de controle. Este relatório pode ser visualizado alternando **Show Performance For** para **By Variant**.

Alguns casos de uso para mostrar o desempenho por variante:

- Algumas variantes ou experimentos parecem ter resultados sem impacto ou sem significância estatística? Dê outra olhada e veja se uma ou outra teve um impacto de longo prazo.
- Veja como é a retenção quando você não envia uma mensagem, analisando os dados de retenção do grupo de controle.

{% tabs %}
{% tab Campaign %}

![Visualizar por variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

![Visualizar por variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Componentes do relatório de retenção por variante {#retention-report-by-variant-components}

- **Intervalo de datas**: Definido na página **Details** da Campaign ou Canvas, o intervalo de datas inclui todos os usuários que receberam a Campaign ou Canvas durante esse período e, desses usuários, os dados daqueles que realizaram o evento de retenção durante o intervalo de datas aparecerão no relatório. A cada dia, a taxa de retenção, a variação percentual em relação ao grupo de controle e a confiança são medidas.
- **Taxa de retenção**: Mostra a taxa de retenção por variante. A taxa de retenção é equivalente ao número de usuários que realizaram o evento de retenção dividido pelo total de usuários que receberam a Campaign ou Canvas.
- **Variação percentual em relação ao controle**: Quantifica a variação percentual por variante em relação ao grupo de controle.
- **Confiança**: {% multi_lang_include analytics/metrics.md metric='Confidence' %} A Braze compara a taxa de conversão de cada variante com a taxa de conversão do controle usando um procedimento estatístico chamado Teste Z para calcular uma porcentagem de [confiança]({{site.baseurl}}/user_guide/messaging/ab_testing#understanding-confidence).
- **Unidades**: Você pode ajustar as unidades entre a porcentagem de usuários e o número de usuários nos controles do gráfico. Unidades específicas podem ser mais significativas ao avaliar o impacto de uma Campaign ou Canvas.
- **Gráfico de variantes**: Este gráfico resume os resultados por variante para o intervalo de datas selecionado.

## O que observar nos seus relatórios de retenção {#things-to-look-for-in-your-retention-reports}

Os relatórios de retenção são simples de gerar, mas desafiadores de interpretar e agir com base neles. Os tópicos e perguntas a seguir podem ajudar você a aproveitar melhor seus relatórios de retenção.

- Considere tendências por dia da semana para Campaigns recorrentes (por exemplo, as coortes de segunda-feira têm melhor desempenho do que as de sábado?).
- Onde o impacto começa a diminuir? Isso pode ser um sinal de que uma nova Campaign ou Canvas direcionado aos usuários naquele momento é necessário como um impulso adicional para a retenção.
- Você está percebendo fadiga de mensagens?
- Uma otimização específica que você fez em uma Campaign ou Canvas há X dias teve um impacto positivo?