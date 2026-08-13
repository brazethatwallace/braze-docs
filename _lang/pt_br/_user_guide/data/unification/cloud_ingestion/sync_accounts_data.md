---
nav_title: Sincronize e exclua os dados da conta
article_title: Sincronize os dados da conta usando CDI
page_order: 5
page_type: reference
description: "Aprenda como sincronizar os dados da sua conta da Braze usando CDI."

---

# Sincronize os dados da conta usando CDI {#sync-account-data-using-cdi}

> Aprenda como sincronizar os dados da sua conta da Braze usando CDI.

## Pré-requisitos {#prerequisites}

{% alert note %}
Faça atualizações no esquema da sua conta apenas quando a sincronização estiver pausada ou não estiver agendada, para evitar conflitos entre os dados do seu data warehouse e o esquema na Braze.
{% endalert %}

## Como a sincronização funciona {#how-syncing-works}

- Cada sincronização importa linhas em que `UPDATED_AT` é posterior ao último timestamp sincronizado. Linhas no timestamp exato do limite podem ser ressincronizadas se novas linhas compartilharem esse mesmo timestamp. Para saber mais, consulte [Evitar ressincronização de linhas com timestamps duplicados]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps).
- Os dados da integração criam ou atualizam contas com base no `id` fornecido.
- Se `DELETED` for `true`, a conta é excluída.
- A sincronização não registra pontos de dados, mas todos os dados sincronizados contam para o uso total de contas, medido pelo total de dados armazenados — não é necessário limitar apenas aos dados alterados.
- Campos que não estão no esquema de contas são descartados; atualize o esquema antes de sincronizar novos campos.
- Você pode atualizar, retomar ou pausar uma sincronização passando o cursor sobre o nome da sincronização e selecionando a ação correspondente.

## Sincronize os dados da sua conta {#sync-your-account-data}

Você pode sincronizar os dados da sua conta usando CDI por meio de um data warehouse ou de um armazenamento de arquivos.

{% tabs local %}
{% tab Data Warehouse %}
Para integrar sua fonte de dados com seu data warehouse:

{% subtabs %}
{% subtab Snowflake %}

1. Crie uma tabela de origem no Snowflake. Use os nomes do exemplo ou escolha seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma view ou view materializada em vez de uma tabela.
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the account to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Name of the account to be created or updated
         NAME VARCHAR(16777216) NOT NULL,
         --Account fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The account associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. Crie uma role, um warehouse e um usuário, e conceda permissões. Se você já tiver credenciais de outra sincronização, pode reutilizá-las — certifique-se de que elas tenham acesso à tabela de contas.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Se você usa políticas de rede, adicione os IPs da Braze à lista de permissões para que o serviço de CDI possa se conectar. Para a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).
4. No dashboard da Braze, acesse **Data Settings** > **Cloud Data Ingestion** e crie uma nova sincronização.
5. Insira os detalhes de conexão (ou reutilize os existentes) e adicione a tabela de origem.
6. Selecione o tipo de sincronização **Accounts** e insira o nome da integração e o cronograma.
7. Escolha a frequência de sincronização.
8. Adicione a chave pública do dashboard ao usuário que você criou. Isso requer um usuário com acesso `SECURITYADMIN` ou superior no Snowflake.
9. Selecione **Test Connection** para confirmar a configuração.
10. Quando terminar, salve a sincronização.

{% endsubtab %}
{% subtab Redshift %}

1. Crie uma tabela de origem no Redshift. Use os nomes do exemplo ou escolha seus próprios nomes de banco de dados, esquema e tabela. Você também pode usar uma view ou view materializada em vez de uma tabela.
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the account to be created or updated
       id varchar not null,
       --Name of the account to be created or updated
       name varchar not null,
       --Account fields and values that should be added or updated
       payload varchar(max),
       --The account associated with this ID should be deleted
       deleted boolean
    )
    ```
2. Crie um usuário e conceda permissões. Se você já tiver credenciais de outra sincronização, pode reutilizá-las — certifique-se de que elas tenham acesso à tabela de contas.
    {% raw %}
    ```sql
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE ACCOUNTS_SYNC TO braze_user;
    ```
    {% endraw %}
3. Se você tem um firewall ou políticas de rede, permita que a Braze acesse sua instância do Redshift. Para a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab BigQuery %}

1. (Opcional) Crie um novo projeto ou dataset para sua tabela de origem.
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. Crie a tabela de origem para sua integração CDI:
    ```sql
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp,
      id STRING,
      name STRING,
      payload JSON,
      deleted BOOLEAN
    );
    ```

    Consulte a tabela a seguir ao criar sua tabela de origem:

    | Nome do campo | Tipo | Obrigatório? |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | Sim |
    | `PAYLOAD` | JSON | Sim |
    | `ID` | String | Sim |
    | `NAME` | String | Sim |
    | `DELETED` | Boolean | Opcional |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sincronize os dados da sua conta" }

{:start="3"}
3. Crie um usuário e conceda permissões. Se você já tiver credenciais de outra sincronização, pode reutilizá-las desde que tenham acesso à tabela de contas.

    | Permissão | Finalidade |
    |------------|---------|
    | BigQuery Connection User | Permite que a Braze se conecte. |
    | BigQuery User | Permite que a Braze execute consultas, leia metadados e liste tabelas. |
    | BigQuery Data Viewer | Permite que a Braze visualize datasets e conteúdos. |
    | BigQuery Job User | Permite que a Braze execute jobs. |
    {: .reset-td-br-1 .reset-td-br-2 aria-label="Sincronize os dados da sua conta" }

    Após conceder as permissões, gere uma chave JSON. Consulte [Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) para instruções. Você fará o upload dela no dashboard da Braze posteriormente.

{:start="4"}
4. Se você usa políticas de rede, permita que os IPs da Braze acessem sua instância do BigQuery. Para a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Databricks %}

1. Crie um catálogo ou esquema para sua tabela de origem.
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. Crie a tabela de origem para sua integração CDI:
    ```sql
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp(),
      id STRING,
      name STRING,
      payload STRING, STRUCT, or MAP,
      deleted BOOLEAN
    );
    ```

    Consulte a tabela a seguir ao criar sua tabela de origem:

    | Nome do campo | Tipo | Obrigatório? |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | Sim |
    | `PAYLOAD` | String, Struct ou Map | Sim |
    | `ID` | String | Sim |
    | `NAME` | String | Sim |
    | `DELETED` | Boolean | Opcional |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sincronize os dados da sua conta" }

{:start="3"}
3. Crie um token de acesso pessoal no Databricks:
    1. Selecione seu nome de usuário e depois selecione **User Settings**.
    2. Na guia **Access tokens**, selecione **Generate new token**.
    3. Adicione um comentário para identificar o token, como "Braze CDI".
    4. Deixe **Lifetime (days)** em branco para não ter expiração e selecione **Generate**.
    5. Copie e salve o token em local seguro para uso no dashboard da Braze.

{:start="4"}
4. Se você usa políticas de rede, permita que os IPs da Braze acessem sua instância do Databricks. Para a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Microsoft Fabric %}

1. Crie uma ou mais tabelas para sua integração CDI com estes campos:
    ```sql
    CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
    (
      UPDATED_AT DATETIME2(6) NOT NULL,
      PAYLOAD VARCHAR NOT NULL,
      ID VARCHAR NOT NULL,
      NAME VARCHAR NOT NULL,
      DELETED BIT
    )
    GO
    ```

{:start="2"}
2. Crie um service principal e conceda permissões. Se você já tiver credenciais de outra sincronização, pode reutilizá-las — certifique-se de que elas tenham acesso à tabela de contas.

{:start="3"}
3. Se você usa políticas de rede, permita que os IPs da Braze acessem sua instância do Microsoft Fabric. Para a lista de IPs, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab File Storage %}
Para sincronizar dados de contas a partir de armazenamento de arquivos, crie um arquivo de origem com os campos a seguir.

| Campo | Obrigatório? | Descrição |
| --- | --- | --- |
| `ID` | Sim | ID da conta a ser atualizada ou criada |
| `NAME` | Sim | Nome da conta |
| `PAYLOAD` | Sim | String JSON dos campos a serem sincronizados com a conta na Braze |
| `DELETED` | Opcional | Booleano indicando se a conta deve ser excluída da Braze |
| `UPDATED_AT` | _*Não suportado_ | O armazenamento de arquivos não suporta colunas `UPDATED_AT` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sincronize os dados da sua conta" }

{% alert note %}
Os nomes de arquivo devem seguir as regras da AWS e ser únicos. Adicione timestamps para ajudar a garantir a unicidade. Para saber mais sobre sincronização com Amazon S3, consulte [Integrações de armazenamento de arquivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).
{% endalert %}

Os exemplos a seguir mostram formatos JSON e CSV válidos para sincronizar dados de contas a partir de armazenamento de arquivos.

{% subtabs %}
{% subtab JSON Accounts %}
```jsonl
{"id":"s3-qa-0","name":"account0","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"id":"s3-qa-1","name":"account1","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":true}
{"id":"s3-qa-2","name":"account2","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":false}
{"id":"s3-qa-3","name":"account3","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
```

{% alert important %}
Cada linha do seu arquivo de origem deve conter JSON válido, caso contrário o arquivo será ignorado.
{% endalert %}
{% endsubtab %}
{% subtab CSV Accounts with Delete %}
```plaintext
ID,NAME,PAYLOAD,DELETED
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}",TRUE
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}",FALSE
```
{% endsubtab %}
{% subtab CSV Accounts without Delete %}
```plaintext
ID,NAME,PAYLOAD
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}"
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}"
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Criar uma view de sincronização {#create-a-sync-view}

Criar uma view de sincronização no seu data warehouse permite que a fonte seja atualizada automaticamente sem a necessidade de reescrever consultas adicionais.

Por exemplo, se você tem uma tabela de dados de conta chamada `account_details_1` com `account_id`, `account_name` e três atributos adicionais, você poderia criar uma view de sincronização como a seguinte:

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    account_id as id,
    account_name as name,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "account_details_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    account_id as id,
    account_name as name,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "account_details_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    account_id as ID,
    account_name as NAME,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.account_details_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    account_id as ID,
    account_name as NAME,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.account_details_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [BRAZE_CLOUD_PRODUCTION].[INGESTION].[ACCOUNTS_SYNC]
AS SELECT
    account_id as ID,
    account_name as NAME,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[account_details_1] ;
```
{% endtab %}
{% endtabs %}