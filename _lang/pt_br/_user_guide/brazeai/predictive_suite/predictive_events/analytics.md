---
nav_title: Análise de eventos
article_title: Análise preditiva de eventos
description: "Este artigo de referência cobre os diferentes componentes incluídos na página de análise de Predictive Events e como eles podem ser usados para tomar decisões informadas."
page_order: 1.3

---

# Análise preditiva de eventos {#predictive-event-analytics}

> Depois que sua previsão for construída e treinada, você terá acesso à página de **análises de previsão**. Esta página ajuda você a decidir quais usuários você deve segmentar com base em sua pontuação de probabilidade ou categoria.

## Sobre a análise preditiva de eventos {#about-predictive-event-analytics}

Assim que a previsão terminar de treinar e esta página estiver populada, você pode começar a usar [filtros]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) em segmentos ou Campaigns para começar a usar os resultados do modelo. Se você deseja ajuda para decidir quem direcionar e por quê, esta página pode ajudar com base na precisão histórica do modelo e nos seus próprios objetivos de negócios.

Estes são os componentes que compõem a análise preditiva de eventos:

- [Pontuação de probabilidade](#purchase_score)
- [Qualidade da previsão](#prediction_quality)
- [Precisão estimada](#estimated_results)
- [Tabela de correlação de eventos](#correlation_table)

A distribuição das pontuações de probabilidade para todo o público de previsão é exibida no topo da página em um gráfico. Usuários em buckets mais à direita têm pontuações mais altas e são mais propensos a realizar o evento. Usuários em buckets mais à esquerda são menos propensos a realizar o evento. O controle deslizante abaixo do gráfico permitirá que você selecione uma seção de usuários e estime quais seriam os resultados de direcionar esses usuários.

À medida que você move os controles deslizantes para diferentes posições, a barra na metade esquerda do painel informará quantos usuários do público total de previsão seriam direcionados usando a parte da população que você selecionou.

![]({% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}){: style="max-width:90%"}

## Pontuação de probabilidade {#purchase_score}

Usuários na população de previsão receberão uma pontuação de probabilidade entre 0 e 100. Quanto maior a pontuação, maior a probabilidade de realizar o evento.

A seguir está como um usuário é categorizado dependendo de sua pontuação de probabilidade:

- **Baixo:** entre 0 e 50
- **Médio:** entre 50 e 75
- **Alto:** entre 75 e 100

As pontuações e as categorias correspondentes serão atualizadas de acordo com o cronograma que você escolheu na página de **Criação de Previsão**. O número de usuários com pontuações de probabilidade em cada um dos 20 intervalos de tamanho igual ou em cada uma das categorias de probabilidade é exibido no gráfico no topo da página.

### Acessando pontuações de probabilidade no nível do usuário {#accessing-user-level-likelihood-scores}

Para visualizar a pontuação de probabilidade de um único usuário, procure esse usuário no dashboard e acesse **Engajamento** > **Previsões** para ver sua pontuação. Para acessar pontuações e categorias para vários usuários de uma só vez, crie um [segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) usando os filtros [Pontuação de probabilidade de evento]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#event-likelihood-score) ou [Categoria de probabilidade de evento]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#event-likelihood-category) e, em seguida, exporte os usuários desse segmento. Ao exportar, você pode incluir as pontuações de probabilidade nos dados exportados.

{% alert note %}
Embora tanto Predictive Events quanto [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/) atribuam pontuações aos usuários, existem diferenças importantes:<br><br>

- **Predictive Events** (previsões de compra): Consideram todos os usuários na população de previsão, independentemente de já terem realizado o evento-alvo anteriormente. Por exemplo, uma previsão de compra pode identificar usuários propensos a fazer sua primeira compra.
- **Predictive Churn**: Considera apenas usuários que já realizaram o evento personalizado. As previsões de churn identificam usuários que já realizaram alguma ação anteriormente e que provavelmente deixarão de fazê-la. Um usuário que nunca fez login não pode ser considerado em "churn" se não fizer login.

Ao exportar pontuações de risco de churn de um segmento, essas pontuações refletem o modelo de previsão de churn, que difere dos modelos de previsão de compras ou outros eventos.
{% endalert %}

## Precisão estimada {#estimated_results}

Na metade direita do painel abaixo do gráfico, mostramos estimativas da precisão esperada do direcionamento da parte do público de previsão que você selecionou de duas maneiras: quantos usuários selecionados devem realizar o evento e quantos não devem.

![O público selecionado e a precisão estimada exibidos no dashboard da Braze.]({% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %})

### Espera-se que realizem o evento {#expected-to-perform}

Você pode usar a precisão estimada para verificar quantos usuários selecionados devem realizar o evento.

A previsão não é perfeitamente precisa, e nenhuma previsão jamais é, o que significa que a Braze não será capaz de identificar todos os futuros usuários que realizarão o evento. As pontuações de probabilidade são como um conjunto de previsões informadas e confiáveis. A barra de progresso indica quantos dos "verdadeiros positivos" esperados na população de previsão serão direcionados com o público selecionado. Observe que esperamos que esse número de usuários realize o evento mesmo que você não envie uma mensagem para eles.

### Não se espera que realizem o evento {#not-expected-to-perform}

Você pode usar a precisão estimada para verificar quantos usuários selecionados provavelmente não realizarão o evento.

Todos os modelos de machine learning cometem erros. Pode haver usuários em sua seleção que tenham uma pontuação de alta probabilidade, mas que não acabem realmente realizando o evento. Eles não realizariam o evento se você não tomasse nenhuma ação. Eles serão direcionados de qualquer maneira, então isso é um erro ou "falso positivo". A largura total desta segunda barra de progresso representa o número esperado de usuários que não realizarão o evento, e a parte preenchida são aqueles que serão incorretamente direcionados usando a posição atual do controle deslizante.

Usando essas informações, incentivamos você a decidir quantos dos verdadeiros positivos você deseja capturar, quantos falsos positivos você pode aceitar serem direcionados e qual é o custo dos erros para o seu negócio. Se você está enviando uma promoção valiosa, pode querer direcionar apenas para não compradores (falsos positivos) favorecendo o lado esquerdo do gráfico. Ou, você pode querer incentivar os compradores que frequentemente compram (verdadeiros positivos) a fazê-lo novamente, selecionando uma seção de usuários que favorece o lado direito do gráfico.

## Qualidade da previsão {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Tabela de correlação de eventos {#correlation_table}

Esta análise exibe atributos ou comportamentos de usuários que estão correlacionados com eventos na população de previsão. Os atributos avaliados são idade, país, gênero e idioma. Comportamentos analisados incluem sessões, compras, total de dólares gastos, eventos personalizados e Campaigns e etapas do Canvas recebidos nos últimos 30 dias.

As tabelas são divididas em esquerda e direita para mais e menos propensos a realizar o evento, respectivamente. Para cada linha, a razão pela qual os usuários com o comportamento ou atributo na coluna da esquerda são mais ou menos propensos a realizar o evento é exibida na coluna da direita. Esse número é a razão entre as pontuações de probabilidade de usuários com esse comportamento ou atributo dividida pela probabilidade de realizar o evento de toda a população de previsão.

Esta tabela é atualizada apenas quando a previsão é re-treinada e não quando as pontuações de probabilidade do usuário são atualizadas.

{% alert note %}
Os dados de correlação para pré-visualização das previsões serão parcialmente ocultos. Uma compra é necessária para revelar esta informação. Entre em contato com o seu gerente de conta para saber mais.
{% endalert %}

## Solução de problemas {#troubleshooting}

### Não é possível criar uma previsão {#unable-to-create-a-prediction}

Se você não conseguir criar uma previsão para um evento personalizado, isso pode ser devido ao tamanho insuficiente da amostra. A Braze estima o número de usuários que realizaram o evento e, se um número suficiente de usuários não tiver realizado o evento, a amostra pode não fornecer dados suficientes para treinar o modelo. Nesse caso, o sistema pode extrapolar para nenhum usuário, impedindo a criação da previsão.

Para criar uma previsão bem-sucedida, certifique-se de que um número suficiente de usuários na sua população de previsão tenha realizado o evento personalizado de destino. O limite exato varia, mas eventos com uso muito baixo na sua base de usuários podem não fornecer dados suficientes para um treinamento confiável do modelo.