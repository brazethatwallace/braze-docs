---
nav_title: Kubit
article_title: Kubit
description: "Este artigo de referência descreve a parceria entre a Braze e o Kubit, uma plataforma de análise de dados sem código e de autoatendimento que oferece insights instantâneos sobre o produto, permitindo a importação de coortes de usuários do Kubit e seu direcionamento no envio de mensagens da Braze."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> O [Kubit](https://kubit.ai/) é uma plataforma de análise de dados sem código e de autoatendimento que oferece insights instantâneos sobre o produto.

A integração da Braze com o Kubit permite a [importação de coortes de usuários do Kubit]({{site.baseurl}}/partners/data_and_analytics/cohort_import/kubit/) e seu direcionamento no envio de mensagens da Braze. Além disso, com o uso do [compartilhamento seguro de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), é possível integrar os dados brutos de campanhas e impressões da Braze com a análise de dados do produto Kubit para medir o impacto dessas campanhas em tempo real. Essa abordagem fornece insights sobre o ciclo de vida completo dos seus usuários sem exigir nenhum esforço de engenharia.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta corporativa do Kubit | É necessário ter uma conta corporativa do Kubit para usar essa parceria. |
| Correspondência de IDs de usuário | Os dados de seus clientes no Kubit e na Braze devem ter IDs de usuário correspondentes nas duas plataformas. Isso também inclui UUIDs anônimos. Visite nossa [documentação]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android) para ler sobre como a Braze define IDs de usuário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Analisando dados da Braze no Kubit {#analyzing-braze-data-in-kubit}

Aproveite o [compartilhamento seguro de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) para compartilhar seus dados brutos de campanhas e impressões da Braze com o Kubit e incorporá-los à análise de dados de autoatendimento do Kubit, proporcionando uma visão completa do ciclo de vida dos usuários.

Para referência, aqui estão todos os [campos da Braze](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) disponíveis para serem incorporados à análise de dados do Kubit. Os detalhes dessa etapa são muito específicos para cada cliente e exigem configurações especiais. Fale com seu gerente de conta do Kubit ou com [support@kubit.ai](support@kubit.ai) para saber mais.