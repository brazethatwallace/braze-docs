---
nav_title: Predictive Churn
article_title: Predictive Churn
description: "Esta landing page aborda o Predictive Churn, uma ferramenta da Predictive Suite da Braze que permite definir o que significa churn para o seu negócio, bem como os usuários que você gostaria de evitar que abandonassem sua marca."
page_order: 8
alias: /predictive_churn/
search_rank: 2
---

# Predictive Churn {#predictive-churn}

> Com o Predictive Churn, uma ferramenta da Predictive Suite da Braze, você pode definir o que significa churn para o seu negócio e identificar os usuários que deseja reter. Quando você cria uma previsão, a Braze treina um modelo de machine learning usando [árvores de decisão com reforço de gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para reconhecer usuários em risco, analisando padrões de comportamento passado — tanto de usuários que abandonaram quanto daqueles que permaneceram.

{% alert tip %}
Para saber mais, consulte [Definição de churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) e [População de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## Sobre o Predictive Churn {#about-predictive-churn}

Após a construção do modelo de previsão, os usuários da população de previsão receberão uma [pontuação de risco de churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/#churn_score) entre 0 e 100, indicando a probabilidade de churn de acordo com a sua definição. Quanto maior a pontuação, maior a probabilidade de o usuário abandonar.

A atualização das pontuações de risco da população de previsão pode ser feita com a [frequência que você escolher]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-prediction). Dessa forma, você pode entrar em contato com usuários que correm risco de churn antes que isso realmente aconteça e evitar que ocorra. Usando até três previsões ativas, é possível aproveitar o Predictive Churn para adaptar modelos individuais que ajudem a evitar o churn em segmentos específicos de usuários que você considera mais valiosos.

![Uma visão geral do churn, que inclui uma população de previsão passada com treinamento usando dados históricos. Isso contribui para prever o risco de churn futuro, medindo a população prevista de hoje com uma pontuação de risco de churn.]({% image_buster /assets/img/churn/churn_overview.png %})

## Acessando o Predictive Churn {#accessing-predictive-churn}

{% multi_lang_include brazeai/predictions_page_access.md %}

Antes de comprar esse recurso, ele está disponível em modo de pré-visualização. Isso permitirá ver uma previsão de churn de demonstração com dados sintéticos e criar um modelo de previsão de churn com base nos seus dados de usuários por vez. Essa pré-visualização não permitirá o direcionamento de usuários para envio de mensagens de acordo com o risco de churn e não será atualizada regularmente após a criação.

Com a pré-visualização, você também pode editar e reconstruir sua previsão ou arquivá-la e criar outras para testar a [qualidade de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/) esperada de diferentes [definições]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).