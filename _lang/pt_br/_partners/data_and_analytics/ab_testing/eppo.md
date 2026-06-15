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

| Requisito | Descrição |
|---|---|
| Conta Eppo | Uma conta Eppo é necessária para aproveitar esta parceria. |
| Currents ou Compartilhamento de Dados Snowflake | Currents ou Compartilhamento de Dados Snowflake é necessário para que o Eppo analise os dados do experimento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Configure Currents ou Compartilhamento de Dados Snowflake na Braze {#step-1-configure-currents-or-snowflake-data-sharing-in-braze}

O Eppo analisa experimentos diretamente no seu data warehouse. Para ativar a integração, os dados de engajamento com mensagem da Braze devem estar disponíveis no warehouse conectado ao Eppo. Você pode exportar dados de Campaign da Braze usando Currents ou acessar dados da Braze na sua instância Snowflake usando [Compartilhamento de Dados Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### Etapa 2: Configure seu experimento em uma Campaign ou Canvas da Braze {#step-2-set-up-your-experiment-in-a-braze-campaign-or-canvas}

Você pode usar recursos nativos de testes A/B em suas Campaigns e Canvas. Para saber mais, veja [Testes multivariantes e A/B](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing#what-are-multivariate-and-ab-testing).

### Etapa 3: Configure o Eppo para medir experimentos da Braze {#step-3-set-up-eppo-to-measure-braze-experiments}

Para realizar experimentos usando dados da Braze no Eppo, crie [tabelas de atribuições](https://docs.geteppo.com/data-management/definitions/assignment-sql/) no seu warehouse com base em dados de eventos de mensagens em nível de usuário exportados da Braze. Tabelas separadas são recomendadas para experimentos de Canvas e Campaign porque dependem de metadados diferentes.

{% tabs local %}
{% tab experimentos do Canvas %}
Para experimentos do Canvas, as atribuições podem ser criadas de duas maneiras:

- No nível de entrada do Canvas (`users.canvas.Entry`)
- Ou em uma etapa de experimento do Canvas (`users.canvas.experimentstep.SplitEntry`)

Nesses casos, campos como `canvas_name`, `experiment_step_id`, `canvas_variation_name` e `experiment_split_id` são usados para definir o nome e a variação do experimento.

{% endtab %}

{% tab experimentos de Campaign %}
Para experimentos de Campaign, use eventos de envio (como push, e-mail, SMS) para determinar quando um usuário entrou no experimento. `campaign_name`, `message_variation_name` e `time` são usados para preencher a tabela de atribuição.

{% endtab %}
{% endtabs %}

Para rastrear métricas específicas de mensagens (como cliques ou aberturas), inclua uma **Entidade Secundária** criando um `combined_id` que junta o ID do usuário com o nome da Campaign ou do Canvas. Esse `combined_id` também é usado em suas tabelas de fatos para alinhar métricas com o experimento e a variação corretos.

O Eppo usa essas atribuições e tabelas de fatos para analisar resultados, e é recomendável configurar um **Protocolo** no Eppo para padronizar a configuração de experimentos futuros. Para saber mais, consulte a [documentação do Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Suporte {#support}

Para perguntas sobre como configurar Braze Currents, Compartilhamento de Dados Snowflake ou configurar Campaigns multivariantes, entre em contato com seu gerente de sucesso do cliente da Braze.

Para assistência na configuração do Eppo para medir experimentos da Braze, entre em contato com a equipe de suporte do Eppo.