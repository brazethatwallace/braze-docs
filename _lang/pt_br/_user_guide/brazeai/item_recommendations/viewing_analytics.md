---
nav_title: Analytics
article_title: "Análise de dados de recomendação de itens"
description: "Saiba mais sobre a análise de dados de recomendação de itens e como visualizá-las na Braze."
page_order: 1.3
---

# Análise de dados de recomendação de itens {#item-recommendation-analytics}

> Saiba mais sobre a análise de dados de recomendação de itens e como visualizá-las na Braze.

## Ver análise de dados {#view-analytics}

Você pode ver a análise de dados da sua recomendação para verificar quais itens foram recomendados aos usuários e qual foi a precisão do modelo de recomendação.

1. Acesse **Analytics** > **Item Recommendation**.
2. Selecione sua recomendação na lista.

## Métricas disponíveis {#available-metrics}

### Público {#audience}

Essas métricas descrevem o público da sua recomendação. Dependendo do tipo de recomendação e dos dados de análise disponíveis, a seção **Público** pode incluir **Precisão** e **Cobertura**.

Para recomendações **AI Personalized**, o cartão **Tipo de recomendação** mostra a taxa estimada de personalização, os usuários com o evento configurado e a população total. Para recomendações **Most Recent**, ele mostra a proporção de usuários que recebem recomendações **Most Recent** em comparação com o fallback **Most Popular**. As recomendações **Most Popular** e **Trending** não exibem um detalhamento do tipo de recomendação por usuário.

![Métricas de público de recomendação mostrando precisão, cobertura e tipos de recomendação divididos entre itens personalizados e mais populares.]({% image_buster /assets/img/item_recs_analytics_1.png %}){: style="max-width:80%;"}

Consulte a tabela a seguir para saber mais:

| Métrica              | Descrição |
| ------------------- | ---------- |
| **Precisão**           | A porcentagem de vezes em que o modelo adivinhou corretamente o próximo item que um usuário compraria. A precisão depende muito do tamanho e da composição específicos do seu catálogo, e deve ser usada como um guia para entender com que frequência o modelo está correto.<br><br>Em testes anteriores, os modelos tiveram bom desempenho com números de precisão variando de 6 a 20%. Essa métrica é atualizada quando o modelo é retreinado.  |
| **Cobertura**            | Qual porcentagem dos itens disponíveis no catálogo é recomendada para pelo menos um usuário. Você pode esperar uma cobertura de itens maior com recomendações de itens personalizadas em comparação com as mais populares. |
| **Taxa de personalização** | Para recomendações **AI Personalized**, a porcentagem estimada de usuários com recomendações personalizadas armazenadas em seus perfis, calculada em relação ao número total de usuários que realizaram o evento configurado nos últimos 24 meses. Usuários que realizaram o evento, mas não têm dados suficientes para gerar uma recomendação personalizada, recebem os itens mais populares como fallback ao receberem mensagens. |
| **Tipo de recomendação** | Para recomendações **Most Recent**, a porcentagem de usuários que recebem recomendações **Most Recent** em comparação com o fallback **Most Popular**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Público" }

### Itens {#items}

Esta tabela inclui métricas sobre seus itens personalizados, mais recentes e mais populares do seu catálogo.

![Tabelas lado a lado listando itens atribuídos a usuários, separados por recomendações personalizadas e recomendações mais populares.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Consulte a tabela a seguir para saber mais:

| Métrica              | Descrição |
| ------------------- | ---------- |
| **Itens personalizados**<br><br>**Itens mais recentes** | Esta coluna lista cada item do catálogo em ordem decrescente de frequência de recomendação para os usuários. Ela também mostra quantos usuários foram atribuídos a cada item pelo modelo.<br><br>Os itens **Personalizados** ou **Mais recentes** serão listados dependendo do [tipo de recomendação]({{site.baseurl}}/user_guide/brazeai/item_recommendations). |
| **Itens mais populares** | Esta coluna lista cada item do catálogo em ordem decrescente de popularidade. Popularidade aqui se refere aos itens do catálogo com os quais os usuários interagem com mais frequência em todo o espaço de trabalho. Os mais populares são usados como fallback quando a recomendação personalizada ou mais recente não pode ser calculada para um usuário individual. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Itens" }

### Visão geral {#overview}

Esta é uma visão geral da configuração de recomendação escolhida, incluindo quando a recomendação foi atualizada pela última vez.

![Tabela de visão geral da recomendação exibindo tipo, catálogo, tipo de evento, nome do evento personalizado, nome da propriedade e data da última atualização.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }