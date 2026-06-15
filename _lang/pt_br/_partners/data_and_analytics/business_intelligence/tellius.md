---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "Este artigo de referência descreve a parceria entre a Braze e a Tellius, uma plataforma de inteligência de decisão e análise aumentada, permitindo que você aproveite os dados, sem depender de engenheiros de BI, para criar dashboards e gerar insights para tomar melhores decisões de marketing."
page_type: partner
search_tag: Partner

---

# Tellius

> [A Tellius](https://www.tellius.com/), uma plataforma de inteligência de decisão e análise aumentada, permite que você responda a perguntas sobre seus dados usando pesquisa em linguagem natural e se aprofunde para entender o "porquê" com insights orientados por IA.

A integração da Braze com a Tellius permite que os usuários aproveitem os dados, sem depender de engenheiros de BI, para criar dashboards e gerar insights para tomar melhores decisões de marketing. Essa integração exige que os dados da Braze sejam armazenados no Snowflake, onde a Tellius pode se conectar diretamente e executar consultas com integração em modo ao vivo.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Tellius | É necessário ter uma conta da Tellius para usar essa parceria. Você pode começar sua jornada com a Tellius usando uma [avaliação gratuita](https://www.tellius.com/free-trial/)|
| Programa de Compartilhamento de Dados do Snowflake | Para os clientes atuais do Snowflake, entre em contato com seu representante da Braze sobre o programa de Compartilhamento de Dados do Snowflake para canalizar seus dados da Braze para sua instância do Snowflake.|
| Conta de leitor do Snowflake | Para clientes que não são do Snowflake, entre em contato com seu representante da Braze para se informar sobre a possibilidade de obter uma conta de leitor do Snowflake para acessar seus dados da Braze.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Obter acesso à Braze por meio do Snowflake {#step-1-obtain-access-to-braze-through-snowflake}

A Braze armazena dados granulares de clientes no Snowflake. Você pode aproveitar seus dados da Braze para gerar insights por meio do programa de Compartilhamento de Dados do Snowflake da Braze ou obtendo uma conta de leitor do Snowflake.

Siga a [integração do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) para fazer a configuração.

### Etapa 2: Conectar a Tellius aos dados da Braze no Snowflake {#step-2-connect-tellius-to-braze-data-in-snowflake}

Conecte a Tellius aos dados da Braze no Snowflake por meio de um dos seguintes métodos:

- Acesso direto: Para carregar dados na Tellius, siga as etapas de como [carregar conjuntos de dados](https://help.tellius.com/article/jn6o59d5gk-load-datasets).
- Acesso OAuth: Para obter acesso OAuth ao Snowflake, siga as etapas da [autenticação por OAuth](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake).

### Etapa 3: Criar Business View na Tellius a partir dos dados carregados {#step-3-create-business-view-in-tellius-from-loaded-data}

Para começar a usar a pesquisa em linguagem natural e os insights automatizados, crie um [Business View](https://help.tellius.com/article/hy9yvh5tom-create-business-view) e selecione conjuntos de dados da sua conexão com o Snowflake.

### Etapa 4: Obter o máximo de valor dos seus dados usando a Tellius {#step-4-get-the-most-value-out-of-your-data-using-tellius}

Na Tellius, há uma interface guiada que apresenta os recursos da plataforma. Para perguntas adicionais e orientações, consulte a [base de conhecimento](https://help.tellius.com/) completa.