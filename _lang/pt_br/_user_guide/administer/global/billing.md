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

Aqui, você encontra gráficos de uso que se aplicam aos seus espaços de trabalho. Seu dashboard pode exibir métricas de uso diferentes com base nos produtos que você adquiriu.

![Gráfico de uso mostrando visitantes únicos mensais]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Esses gráficos podem mostrar usuários ativos mensais, visitantes únicos mensais e envios de e-mail. Gráficos de uso como esses são particularmente úteis ao planejar o orçamento de uso e obter uma compreensão mais profunda de quais espaços de trabalho contribuem para o uso geral.

### Detalhes do contrato {#contract-details}

Os detalhes do contrato listam a data de início e término do seu contrato atual com a Braze.

#### Considerações {#considerations}

Se o seu contrato usa visitantes únicos mensais (MUV) e você muda para um contrato que usa apenas usuários ativos mensais (MAU), seus dados históricos ainda aparecem no gráfico de MUV e seus novos dados aparecem apenas no gráfico de MAU. Por exemplo, se o seu contrato termina em outubro, o gráfico de MUV mostra dados até o final de setembro.

## Eventos e atributos mais usados por app {#most-used-events-and-attributes-by-app}

Em **Eventos e atributos mais usados por app**, você pode verificar os fatores que impulsionam o uso de pontos de dados de atributos e eventos personalizados.

![Eventos e atributos mais usados por app]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Para cada app, você pode selecionar **Ver detalhamento** para visualizar uma contagem estimada de cada atributo personalizado, atributo de perfil e evento personalizado específico para o período selecionado, bem como a porcentagem das atualizações de atributos e eventos desse app que foram geradas por esse atributo ou evento.

![Guia de detalhamento de eventos e atributos mais usados por app]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Detalhamentos de dados como esses podem ajudar você a entender quais pontos de dados específicos estão consumindo grandes porcentagens da sua cota. Recomendamos que você monitore essas informações periodicamente para garantir que não está gastando pontos de dados de forma acidental e desnecessária. Seu CSM pode orientar você a aproveitar ao máximo o seu plano atual ou oferecer opções com maior flexibilidade.

## Dashboard de total de pontos de dados {#total-data-points-dashboard}

A guia **Total de uso de pontos de dados** oferece uma visão detalhada do uso de pontos de dados. Você pode visualizar todos os dados nesta seção agregados por semanas ou meses.

{% alert note %}
As informações de pontos de dados são armazenadas em cache a cada 24 horas.
{% endalert %}

Se você é administrador e não consegue visualizar a guia **Total de uso de pontos de dados**, verifique se o seu navegador permite cookies de terceiros para o domínio do seu dashboard da Braze e se não está no modo de navegação anônima.

![Filtrando o uso de pontos de dados por semanas]({% image_buster /assets/img/subscription_and_billing2.png %})

### Detalhes do contrato

Aqui, você encontra informações sobre quando o seu contrato atual com a Braze começa e termina, bem como os pontos de dados alocados e a soma de todos os pontos de dados que foram usados até o momento no seu contrato atual.

Os campos nesta seção são definidos da seguinte forma:

- **Tipo de contrato:** Estrutura do período de faturamento, anual ou plurianual.
- **Data de início e término do contrato:** Data de início e término de todo o contrato.
- **Pontos de dados alocados:** A quantidade de pontos de dados alocados no contrato por período de faturamento.
- **Uso de pontos de dados do contrato:** Um total acumulado de todos os pontos de dados registrados ao longo da vigência do contrato, que não é redefinido no próximo período de faturamento.

### Dados de faturamento da empresa {#company-billing-data}

#### Uso total de pontos de dados por app {#app-level-total-data-point-usage}

Este gráfico mostra o uso de pontos de dados em todos os apps.

![Uso total de pontos de dados por app mostrando os pontos de dados usados para cada app.]({% image_buster /assets/img/app_level_total.png %})

Selecione um dos totais para visualizar a tabela **Uso de pontos de dados ao longo do tempo**, que mostra os totais semanais de pontos de dados para cada espaço de trabalho. Linhas com a coluna **Nome do app** em branco representam pontos de dados que não estão associados a nenhum app (como pontos de dados usados em solicitações que não especificam um `app_id`).

![Uso de pontos de dados ao longo do tempo mostrando o total semanal de pontos de dados para dois espaços de trabalho.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Uso de pontos de dados por espaço de trabalho {#workspace-data-point-usage}

Este gráfico permite avaliar o uso total de pontos de dados de uma empresa por espaço de trabalho. Com ele, você consegue entender como cada espaço de trabalho está contribuindo para o uso de pontos de dados da empresa.

![Gráfico de uso de pontos de dados por espaço de trabalho para dois espaços de trabalho]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Uso de pontos de dados do ciclo de faturamento por fonte de evento {#billing-cycle-data-point-usage-by-event-source}

Este gráfico permite visualizar como o uso de pontos de dados está distribuído entre diferentes fontes de eventos, como diferentes atributos de API, eventos personalizados e sessões.

![Uso de pontos de dados do ciclo de faturamento por fonte de evento exibindo a alocação de pontos de dados entre diferentes fontes de eventos.]({% image_buster /assets/img/event_source_stats.png %})

#### Uso de pontos de dados ao longo do tempo {#data-point-usage-over-time}

Este gráfico permite visualizar rapidamente o uso total de pontos de dados em comparação com a quantidade alocada de pontos de dados.

![Uso de pontos de dados ao longo do tempo comparando os pontos de dados alocados no ciclo de faturamento atual com o total acumulado]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

## Próximas etapas {#next-steps}

- [Preferências de notificação]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) para configurar alertas para eventos relacionados ao faturamento e limites de uso.
- [Dashboard de uso de créditos]({{site.baseurl}}/credits_usage_dashboard) para monitorar o consumo de créditos de mensagens.