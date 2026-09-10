---
nav_title: Faturamento
article_title: Faturamento
alias: /subscription_and_usage/
page_order: 5
page_type: reference
description: "Este artigo de referência aborda a página de Faturamento, onde você pode monitorar e verificar o consumo de dados."
tool: Dashboard
search_rank: 5
---

# Faturamento {#billing}

> Saiba como usar a página **Faturamento** para monitorar e verificar o consumo de dados em espaços de trabalho, apps e fontes de eventos. Este artigo aborda as diferentes seções da página e as informações que elas podem fornecer.

Para acessar a página **Faturamento**, acesse **Configurações** > **Faturamento**.

A página **Faturamento** inclui as seguintes guias:

- [Inscrições e uso](#subscriptions-and-usage)
- [Eventos e atributos mais usados por app](#most-used-events-and-attributes-by-app)
- [Total de uso de pontos de dados](#total-data-points-dashboard)

## Inscrições e uso {#subscriptions-and-usage}

A guia **Inscrições e uso** inclui gráficos de uso e os detalhes do seu contrato. Os dados nesta página são atualizados diariamente às 22h, horário do leste dos EUA (ET). Eles não refletem a atividade em tempo real.

### Gráficos de uso {#usage-graphs}

Aqui, você encontra gráficos de uso que se aplicam aos seus espaços de trabalho. Seu próprio dashboard pode mostrar métricas de uso diferentes com base nos produtos que você adquiriu.

![Gráfico de uso mostrando visitantes únicos mensais]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Esses gráficos podem mostrar usuários ativos mensais, visitantes únicos mensais e envios de e-mail. Gráficos de uso como esses são particularmente úteis ao tentar planejar o uso e obter uma compreensão mais profunda de quais espaços de trabalho contribuem para o uso geral.

### Detalhes do contrato {#contract-details}

Os detalhes do contrato listam as datas de início e término do seu contrato atual com a Braze.

#### Considerações {#considerations}

Se o seu contrato utiliza visitantes únicos mensais (MUV) e você muda para um contrato que utiliza apenas usuários ativos mensais (MAU), seus dados históricos ainda aparecem no gráfico de MUV e seus novos dados aparecem apenas no gráfico de MAU. Por exemplo, se o seu contrato termina em outubro, o gráfico de MUV mostra dados até o final de setembro.

## Eventos e atributos mais usados por app {#most-used-events-and-attributes-by-app}

Em **Eventos e Atributos Mais Usados por App**, você pode verificar os principais fatores de uso de pontos de dados de atributos e eventos personalizados.

![Eventos e atributos mais usados por app]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Para cada app, você pode selecionar **See breakdown** para visualizar uma contagem estimada de cada atributo personalizado, atributo de perfil e evento personalizado específico no período selecionado, bem como a porcentagem das atualizações de atributos e eventos daquele app que foram impulsionadas por esse atributo ou evento.

![Guia de detalhamento de eventos e atributos mais usados por app]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Detalhamentos de dados como esses podem ajudar você a entender quais pontos de dados específicos estão consumindo grandes porcentagens da sua cota. Recomendamos que você monitore essas informações periodicamente para garantir que não está gastando pontos de dados de forma acidental e desnecessária. Seu gerente de sucesso do cliente pode fornecer orientações para aproveitar ao máximo seu plano atual ou oferecer opções com maior flexibilidade.

## Dashboard de total de pontos de dados {#total-data-points-dashboard}

A guia **Total Data Points Usage** oferece uma visão detalhada do uso dos seus pontos de dados. Você pode visualizar todos os dados nesta seção agregados por semanas ou meses.

{% alert note %}
As informações de pontos de dados são armazenadas em cache a cada 24 horas.
{% endalert %}

Se você é administrador e não consegue visualizar a guia **Total Data Points Usage**, verifique se o seu navegador permite cookies de terceiros para o domínio do dashboard da Braze e se não está no modo de navegação anônima.

![Filtrando o uso de pontos de dados por semanas]({% image_buster /assets/img/subscription_and_billing2.png %})

### Detalhes do contrato

Aqui, você encontra informações sobre quando seu contrato atual com a Braze começa e termina, além dos pontos de dados alocados e um total de todos os pontos de dados usados até o momento no seu contrato atual.

Os campos nesta seção são definidos da seguinte forma:

- **Contract Type:** Estrutura do período de faturamento, podendo ser Anual ou Plurianual.
- **Contract Start and End Date:** Data de início e término do contrato completo.
- **Allotted Data Points:** A quantidade de pontos de dados alocados no contrato por período de faturamento.
- **Contract Data Point Usage:** Um total acumulado de todos os pontos de dados registrados ao longo da vigência do contrato, que não é redefinido no próximo período de faturamento.

### Dados de faturamento da empresa {#company-billing-data}

#### Uso total de pontos de dados por app {#app-level-total-data-point-usage}

Este gráfico mostra o uso de pontos de dados em todos os apps.

![Uso total de pontos de dados por app mostra os pontos de dados usados em cada app.]({% image_buster /assets/img/app_level_total.png %})

Selecione um dos totais para visualizar a tabela **Data Point Usage Over Time**, que mostra os totais semanais de pontos de dados para cada espaço de trabalho. Linhas com a coluna **App Name** em branco representam pontos de dados que não estão associados a nenhum app (como pontos de dados usados em solicitações que não especificam um `app_id`).

![Uso de pontos de dados ao longo do tempo mostrando os totais semanais de pontos de dados para dois espaços de trabalho.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Uso de pontos de dados por espaço de trabalho {#workspace-data-point-usage}

Este gráfico permite avaliar o uso total de pontos de dados de uma empresa por espaço de trabalho. Ele oferece a capacidade de analisar como cada espaço de trabalho contribui para o uso de pontos de dados da empresa.

![Gráfico de uso de pontos de dados por espaço de trabalho para dois espaços de trabalho]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Uso de pontos de dados por fonte de evento no ciclo de faturamento {#billing-cycle-data-point-usage-by-event-source}

Este gráfico permite visualizar como o uso de pontos de dados é distribuído entre diferentes fontes de evento, como diferentes atributos de API, eventos personalizados e sessões.

![Uso de pontos de dados por fonte de evento no ciclo de faturamento exibindo a alocação de pontos de dados entre diferentes fontes de evento.]({% image_buster /assets/img/event_source_stats.png %})

#### Uso de pontos de dados ao longo do tempo {#data-point-usage-over-time}

Este gráfico permite visualizar rapidamente o uso total de pontos de dados em comparação com a quantidade alocada de pontos de dados.

![Uso de pontos de dados ao longo do tempo comparando os pontos de dados alocados no ciclo de faturamento atual com o total acumulado]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

## Próximas etapas {#next-steps}

{% article_tiles %}
- name: Preferências de notificação
  link: /docs/user_guide/administer/global/admin_settings/notification_preferences
- name: Dashboard de uso de créditos
  link: /docs/credits_usage_dashboard
{% endarticle_tiles %}