---
nav_title: Predictive Events
article_title: Predictive Events
description: "Este artigo aborda Predictive Events (anteriormente Predictive Purchases), uma ferramenta da Predictive Suite da Braze que oferece aos profissionais de marketing a capacidade de identificar e enviar mensagens aos usuários com base na probabilidade de realizarem um evento."
page_order: 9
alias: /predictive_purchases/
search_rank: 1
---

# Predictive Events {#predictive-events}

> Predictive Events é uma ferramenta poderosa da Predictive Suite da Braze para identificar e enviar mensagens aos usuários com base na probabilidade de realizarem um evento. Quando você cria uma previsão de evento, a Braze treina um modelo de machine learning usando [árvores de decisão com gradient boosting](https://en.wikipedia.org/wiki/Gradient_boosting) para aprender com a atividade anterior e prever a atividade futura.

## Sobre Predictive Events {#about-predictive-events}

Após a criação de uma previsão, os usuários recebem uma [pontuação de probabilidade]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#purchase_score) entre 0 e 100, indicando a probabilidade de realizarem o evento selecionado. Quanto maior a pontuação, maior a probabilidade de o usuário realizar esse evento. Os usuários também são classificados em categorias de probabilidade baixa, média e alta.

O verdadeiro valor de Predictive Events está no uso dos resultados da previsão para criar um Segment or segmento or segmento ou uma Campaign. Profissionais de marketing podem criar Campaigns direcionadas diretamente na página de **Previsão** para obter resultados imediatos de aumento de receita, ou salvar um Segment or segmento or segmento para uma futura Campaign ou Canvas. Não tem certeza de quem direcionar primeiro? Leia nossas [considerações estratégicas]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) para o envio de mensagens aos usuários com base na pontuação de probabilidade.

![Gráfico intitulado "Como Predictive Events funciona", exibindo dados de usuários sendo canalizados para o modelo de machine learning. O rótulo diz "Treine com dados históricos, compare o comportamento dos usuários que realizaram o evento em um determinado período com aqueles que não o fizeram." São mostrados também os resultados do machine learning, em que os usuários são classificados de menos propensos a mais propensos a realizar o evento. O rótulo diz "Preveja a probabilidade de eventos futuros, atribua uma pontuação de probabilidade aos usuários para um direcionamento preciso e conveniente."]({% image_buster /assets/img/how_predictive_events_works.png %})

## Acessando Predictive Events {#accessing-predictive-events}

{% multi_lang_include brazeai/predictions_page_access.md %}

Antes de comprar esse recurso, ele está disponível em modo de pré-visualização. Isso permite que você veja uma previsão de demonstração com dados sintéticos, bem como crie um modelo de previsão prévia por vez. Essa previsão será criada com base nos dados reais dos seus usuários, mas não permitirá o direcionamento de mensagens para os usuários de acordo com a pontuação de probabilidade. Ela também não será atualizada regularmente após a criação.

Com a pré-visualização, você também pode editar e reconstruir essa previsão ou arquivá-la e criar outras para testar a [qualidade da previsão]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#prediction_quality) esperada de [diferentes públicos]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) e se familiarizar com a análise de dados.