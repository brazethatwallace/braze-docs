---
nav_title: Eppo
article_title: Eppo
description: "Aprenda como integrar o Eppo com a Braze."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) é uma plataforma de experimentação de próxima geração que permite que as equipes realizem testes A/B, gerenciem recursos em grande escala e aproveitem insights impulsionados por IA para a tomada de decisões baseada em dados.

*Esta integração é mantida pela Eppo.*

A integração entre a Braze e o Eppo permite que você configure testes A/B na Braze e analise os resultados no Eppo para descobrir insights e vincular o desempenho das mensagens a métricas de negócios de longo prazo, como receita ou retenção.

## Pré-requisitos {#prerequisites}

| Requisito                          | Descrição                                                                           |
|------------------------------------|-------------------------------------------------------------------------------------|
| Conta Eppo                         | Uma conta Eppo é necessária para aproveitar esta parceria.                           |
| Currents ou Snowflake Data Sharing | Currents ou Snowflake Data Sharing é necessário para que a Eppo analise os dados de experimentos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Configure Currents ou Snowflake Data Sharing na Braze {#step-1-configure-currents-or-snowflake-data-sharing-in-braze}

A Eppo analisa experimentos diretamente no seu data warehouse. Para ativar a integração, os dados de engajamento com mensagem da Braze precisam estar disponíveis no warehouse conectado à Eppo. Você pode exportar dados de Campaign da Braze usando Currents ou acessar os dados da Braze na sua instância do Snowflake usando o [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake).

### Etapa 2: Configure seu experimento em uma Campaign ou Canvas da Braze {#step-2-set-up-your-experiment-in-a-braze-campaign-or-canvas}

Você pode usar os recursos nativos de testes A/B nas suas Campaigns e Canvas. Para saber mais, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

### Etapa 3: Configure a Eppo para medir experimentos da Braze {#step-3-set-up-eppo-to-measure-braze-experiments}

Para executar experimentos usando dados da Braze na Eppo, crie [tabelas de atribuição](https://docs.geteppo.com/data-management/definitions/assignment-sql/) no seu warehouse com base nos dados de eventos de mensagem no nível do usuário exportados da Braze. Tabelas separadas são recomendadas para experimentos de Canvas e Campaign porque dependem de metadados diferentes.

{% tabs local %}
{% tab experimentos do canva %}
Para experimentos do Canvas, as atribuições podem ser criadas:

- No nível de entrada do Canvas (`users.canvas.Entry`)
- Ou em uma etapa de experimento do Canvas (`users.canvas.experimentstep.SplitEntry`)

Nesses casos, campos como `canvas_name`, `experiment_step_id`, `canvas_variation_name` e `experiment_split_id` são usados para definir o nome do experimento e a variação.

{% endtab %}

{% tab experimentos de campaign %}
Para experimentos de Campaign, use eventos de envio (como push, e-mail, SMS) para determinar quando um usuário entrou no experimento. `campaign_name`, `message_variation_name` e `time` são usados para preencher a tabela de atribuição.

{% endtab %}
{% endtabs %}

Para rastrear métricas específicas de mensagem (como cliques ou aberturas), inclua uma **Entidade Secundária** criando um `combined_id` que une o ID do usuário com o nome da Campaign ou do Canvas. Esse `combined_id` também é usado nas suas tabelas de fatos para alinhar as métricas com o experimento e a variação corretos.

A Eppo usa essas tabelas de atribuição e de fatos para analisar os resultados, e é recomendável configurar um **Protocolo** na Eppo para padronizar a configuração de experimentos futuros. Para saber mais, consulte a [documentação da Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Suporte {#support}

Para perguntas sobre como configurar o Braze Currents, o compartilhamento de dados do Snowflake ou campanhas multivariantes, entre em contato com seu gerente de sucesso do cliente da Braze.

Para obter assistência na configuração da Eppo para medir experimentos da Braze, entre em contato com a equipe de suporte da Eppo.