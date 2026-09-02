---
nav_title: Integrações de data warehouse
article_title: "Integrações de armazenamento de data warehouse"
alias: /partners/databricks/
description: "Esta página aborda como usar a Ingestão de Dados na Nuvem da Braze para sincronizar dados relevantes com sua integração do Snowflake, Redshift, BigQuery e Databricks."
page_order: 3
page_type: reference
---

# Integrações de armazenamento de data warehouse {#data-warehouse-storage-integrations}

> Esta página aborda como usar a Ingestão de Dados na Nuvem (CDI) da Braze para sincronizar dados relevantes com sua integração do Snowflake, Redshift, BigQuery e Databricks.

## Configurando integrações com data warehouse {#setting-up-data-warehouse-integrations}

As integrações de ingestão de dados na nuvem exigem alguma configuração do lado da Braze e na instância do seu data warehouse. Siga estas etapas para configurar a integração:

{% tabs %}
{% tab Snowflake %}
1. Na sua instância do Snowflake, configure as tabelas ou views que deseja sincronizar com a Braze.
2. Crie uma nova fonte Snowflake no dashboard da Braze.
3. Obtenha a chave pública fornecida no dashboard da Braze e [adicione-a ao usuário do Snowflake para autenticação](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Crie uma sincronização no dashboard da Braze, teste a integração e inicie a sincronização.

{% alert tip %}
O [guia de início rápido do Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) fornece código de exemplo e orienta as etapas necessárias para criar um pipeline automatizado usando Snowflake Streams e CDI para sincronizar dados com a Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Certifique-se de que o acesso da Braze é permitido nas tabelas do Redshift que deseja sincronizar. A Braze se conecta ao Redshift pela internet.
2. Na sua instância do Redshift, configure as tabelas ou views que deseja sincronizar com a Braze.
3. Crie uma nova fonte e sincronização no dashboard da Braze.
4. Teste a integração e inicie a sincronização.

{% alert note %}
As linhas processadas por sincronização dependem do desempenho do seu data warehouse, latência de rede e quantidade de dados novos que correspondem à consulta de sincronização. Use o **Histórico de sincronização** da integração no dashboard para ver a duração e a contagem de linhas das execuções recentes.
{% endalert %}
{% endtab %}
{% tab BigQuery %}
1. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e dataset(s) do BigQuery que contêm os dados que deseja sincronizar.
2. Na sua conta do BigQuery, configure as tabelas ou views que deseja sincronizar com a Braze.
3. Crie uma nova fonte e sincronização no dashboard da Braze.
4. Teste a integração e inicie a sincronização.
{% endtab %}
{% tab Databricks %}
1. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e dataset(s) do Databricks que contêm os dados que deseja sincronizar.
2. Na sua conta do Databricks, configure as tabelas ou views que deseja sincronizar com a Braze.
3. Crie uma nova fonte e sincronização no dashboard da Braze.
4. Teste a integração e inicie a sincronização.

{% alert important %}
Pode haver de dois a cinco minutos de tempo de aquecimento quando a Braze se conecta a instâncias SQL Classic e Pro, o que pode causar atrasos durante a configuração e teste da conexão, bem como no início de sincronizações agendadas. Usar uma instância SQL serverless minimiza o tempo de aquecimento e melhora a taxa de consultas, mas pode resultar em custos de integração ligeiramente mais altos.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Crie um service principal e conceda acesso às APIs do Fabric.
2. Configure um espaço de trabalho compartilhado e conceda ao service principal acesso a ele.
3. No espaço de trabalho compartilhado do Fabric, configure as tabelas ou views que deseja sincronizar com a Braze.
4. Crie uma nova fonte e sincronização no dashboard da Braze.
5. Teste a integração e inicie a sincronização.
{% endtab %}
{% endtabs %}

### Etapa 1: Configurar tabelas ou views {#step-1-set-up-tables-or-views}

Antes de começar, revise [Configuração de tabelas para ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup) para entender os requisitos da tabela de origem em comparação com os requisitos de formatação do `PAYLOAD`.

{% alert note %}
Sua tabela ou view de origem pode incluir colunas que não estão listadas para o seu data warehouse nas guias da seção a seguir (por exemplo, auditoria ou hashing). A Braze lê apenas as colunas descritas nessas guias; outras colunas não são usadas durante as sincronizações de ingestão de dados na nuvem.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

#### Etapa 1.1: Configurar a tabela {#step-11-set-up-the-table}

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Você pode nomear o banco de dados, schema e tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - O momento em que esta linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no exato timestamp de limite podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.
- **Colunas de identificação do usuário** - Sua tabela pode conter uma ou mais colunas de identificação do usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica o usuário que deseja atualizar. Deve corresponder ao valor `external_id` usado na Braze.
    - `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter múltiplos aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário da Braze. É gerado pelo SDK or kit de desenvolvimento de software da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID externo de usuário ou alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se existirem múltiplos perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente é priorizado para atualizações. Se você incluir tanto e-mail quanto telefone, o e-mail é usado como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se existirem múltiplos perfis com o mesmo número de telefone, o perfil atualizado mais recentemente é priorizado para atualizações.
- `PAYLOAD` - Esta é uma string JSON dos campos que deseja sincronizar com o usuário na Braze.

#### Etapa 1.2: Configurar o role e as permissões do banco de dados {#step-12-set-up-the-role-and-database-permissions}

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Atualize os nomes conforme necessário, mas as permissões devem corresponder ao exemplo anterior.

#### Etapa 1.3: Configurar o warehouse e conceder acesso ao role da Braze {#step-13-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
O warehouse precisa ter o flag **auto-resume** ativado. Caso contrário, conceda à Braze privilégios adicionais de `OPERATE` no warehouse para que a Braze possa ativá-lo quando a consulta for executada.
{% endalert %}

#### Etapa 1.4: Configurar o usuário {#step-14-set-up-the-user}

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Após esta etapa, compartilhe as informações de conexão com a Braze para receber uma chave pública para adicionar ao usuário.

{% alert note %}
Ao conectar diferentes espaços de trabalho à mesma conta do Snowflake, você deve criar um usuário único para cada espaço de trabalho da Braze em que está criando uma integração. Dentro de um espaço de trabalho, você pode reutilizar o mesmo usuário entre integrações, mas a criação da integração falhará se um usuário na mesma conta do Snowflake estiver duplicado em espaços de trabalho diferentes.
{% endalert %}

#### Etapa 1.5: Permitir IPs da Braze na política de rede do Snowflake (opcional) {#step-15-allow-braze-ips-in-snowflake-network-policy-optional}

Dependendo da configuração da sua conta do Snowflake, pode ser necessário permitir os seguintes endereços IP na sua política de rede do Snowflake. Para saber mais sobre como ativar isso, consulte a documentação relevante do Snowflake sobre [modificar uma política de rede](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Etapa 1.1: Configurar a tabela

Opcionalmente, configure um novo banco de dados e schema para conter sua tabela de origem
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Crie uma tabela (ou view) para usar na sua integração CDI
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Você pode nomear o banco de dados, schema e tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - O momento em que esta linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no exato timestamp de limite podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.
- **Colunas de identificação do usuário** - Sua tabela pode conter uma ou mais colunas de identificação do usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica o usuário que deseja atualizar. Deve corresponder ao valor `external_id` usado na Braze.
    - `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter múltiplos aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário da Braze. É gerado pelo SDK or kit de desenvolvimento de software da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID externo de usuário ou alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se existirem múltiplos perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente é priorizado para atualizações. Se você incluir tanto e-mail quanto telefone, o e-mail é usado como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se existirem múltiplos perfis com o mesmo número de telefone, o perfil atualizado mais recentemente é priorizado para atualizações.
- `PAYLOAD` - Esta é uma string JSON dos campos que deseja sincronizar com o usuário na Braze.

#### Etapa 1.2: Criar o usuário e conceder permissões {#step-12-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Essas são as permissões mínimas exigidas para esse usuário. Se estiver criando múltiplas integrações CDI, pode ser útil conceder permissões a um schema ou gerenciar permissões usando um grupo.

#### Etapa 1.3: Permitir acesso aos IPs da Braze {#step-13-allow-access-to-braze-ips}

Se você tiver um firewall ou outras políticas de rede, é necessário conceder à Braze acesso de rede à sua instância do Redshift. Um exemplo de endpoint de URL do Redshift é "example-cluster.ap-northeast-2.redshift.amazonaws.com".

Algumas coisas importantes:
- Pode ser necessário alterar seus grupos de segurança para permitir que a Braze acesse seus dados no Redshift.
- Certifique-se de permitir explicitamente o tráfego de entrada nos IPs da tabela e na porta usada para consultar seu cluster do Redshift (o padrão é 5439). Você deve permitir explicitamente a conectividade TCP do Redshift nesta porta, mesmo que as regras de entrada estejam definidas como "permitir tudo".
- O endpoint do cluster do Redshift deve ser acessível publicamente para que a Braze se conecte ao seu cluster.
     - Se não quiser que seu cluster do Redshift seja acessível publicamente, você pode configurar uma VPC e uma instância EC2 para usar um túnel SSH para acessar os dados do Redshift. Para saber mais, consulte a [publicação do AWS Knowledge Center](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).

Permita o acesso dos seguintes IPs correspondentes à região do seu dashboard da Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Etapa 1.1: Configurar a tabela

Opcionalmente, configure um novo projeto ou dataset para conter sua tabela de origem.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crie uma ou mais tabelas para usar na sua integração CDI com os seguintes campos:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Nome do campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 1.1: Configurar a tabela" }

Você pode nomear o projeto, dataset e tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - O momento em que esta linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no exato timestamp de limite podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.
- **Colunas de identificação do usuário** - Sua tabela pode conter uma ou mais colunas de identificação do usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica o usuário que deseja atualizar. Deve corresponder ao valor `external_id` usado na Braze.
    - `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter múltiplos aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário da Braze. É gerado pelo SDK or kit de desenvolvimento de software da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID externo de usuário ou alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se existirem múltiplos perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente é priorizado para atualizações. Se você incluir tanto e-mail quanto telefone, o e-mail é usado como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se existirem múltiplos perfis com o mesmo número de telefone, o perfil atualizado mais recentemente é priorizado para atualizações.
- `PAYLOAD` - Esta é uma string JSON dos campos que deseja sincronizar com o usuário na Braze.

{% alert important %}
**Particionamento do BigQuery**

O CDI suporta partições para o BigQuery. Se você particionar por uma função de `UPDATED_AT` (por exemplo, na granularidade de um dia, semana ou hora, dependendo do tamanho do seu dataset), o BigQuery pode reduzir os dados que precisa varrer. Isso melhora o desempenho e a eficiência para tabelas muito grandes.

Não particione por outros campos. Teste diferentes configurações para encontrar a melhor opção para seus dados específicos.

Todas as consultas CDI filtram por `UPDATED_AT`, mas esse comportamento pode mudar. Projete o schema da sua tabela para _não_ exigir que as consultas incluam essa cláusula.

Para saber mais, consulte a [documentação de particionamento do BigQuery](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).
{% endalert %}

#### Etapa 1.2: Criar uma conta de serviço e conceder permissões {#step-12-create-a-service-account-and-grant-permissions}

Crie uma conta de serviço no GCP para que a Braze use para conectar e ler dados da(s) sua(s) tabela(s). A conta de serviço deve ter as seguintes permissões:

- **BigQuery Connection User:** Permite que a Braze faça conexões
- **BigQuery User:** Fornece à Braze acesso para executar consultas, ler metadados de datasets e listar tabelas.
- **BigQuery Data Viewer:** Fornece à Braze acesso para visualizar datasets e seu conteúdo.
- **BigQuery Job User:** Fornece à Braze acesso para executar jobs

Após criar a conta de serviço e conceder permissões, gere uma chave JSON. Para saber mais, consulte [Criar e excluir chaves de conta de serviço](https://cloud.google.com/iam/docs/keys-create-delete). Faça o upload dessa chave no dashboard da Braze em uma etapa posterior.

#### Etapa 1.3: Permitir acesso aos IPs da Braze

Se você tiver políticas de rede ativas, é necessário conceder à Braze acesso de rede à sua instância do BigQuery. Permita o acesso dos seguintes IPs correspondentes à região do seu dashboard da Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Etapa 1.1: Configurar a tabela

Opcionalmente, configure um novo catálogo ou schema para conter sua tabela de origem.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crie uma ou mais tabelas para usar na sua integração CDI com os seguintes campos:


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Nome do campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| STRING, STRUCT, or MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 1.1: Configurar a tabela" }

Você pode nomear o schema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - O momento em que esta linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no exato timestamp de limite podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.
- **Colunas de identificação do usuário** - Sua tabela pode conter uma ou mais colunas de identificação do usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica o usuário que deseja atualizar. Deve corresponder ao valor `external_id` usado na Braze.
    - `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter múltiplos aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário da Braze. É gerado pelo SDK or kit de desenvolvimento de software da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID externo de usuário ou alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se existirem múltiplos perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente é priorizado para atualizações. Se você incluir tanto e-mail quanto telefone, o e-mail é usado como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se existirem múltiplos perfis com o mesmo número de telefone, o perfil atualizado mais recentemente é priorizado para atualizações.
- `PAYLOAD` - Esta é uma string ou struct dos campos que deseja sincronizar com o usuário na Braze.

#### Etapa 1.2: Criar um token de acesso {#step-12-create-an-access-token}

Para que a Braze acesse o Databricks, é necessário criar um token de acesso pessoal.

1. No seu espaço de trabalho do Databricks, selecione seu nome de usuário do Databricks na barra superior e, em seguida, selecione **User Settings** no menu suspenso.
2. Na guia Access tokens, selecione **Generate new token**.
3. Insira um comentário que ajude a identificar este token, como "Braze CDI", e altere o tempo de vida do token para sem prazo de validade, deixando o campo Lifetime (days) vazio (em branco).
4. Selecione **Generate**.
5. Copie o token exibido e, em seguida, selecione **Done**.

Mantenha o token em um local seguro até que precise inseri-lo no dashboard da Braze durante a etapa de criação de credenciais.

#### Etapa 1.3: Permitir acesso aos IPs da Braze

Se você tiver políticas de rede ativas, é necessário conceder à Braze acesso de rede à sua instância do Databricks. Permita o acesso dos seguintes IPs correspondentes à região do seu dashboard da Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Etapa 1.1: Configurar o service principal e conceder acesso {#step-11-set-up-the-service-principal-and-grant-access}
A Braze se conecta ao seu Fabric warehouse usando um service principal com autenticação Entra ID. Crie um novo service principal para a Braze usar e conceda acesso aos recursos do Fabric conforme necessário. A Braze precisa dos seguintes detalhes para se conectar:

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
O Azure não permite expiração ilimitada em secrets de service principal. Lembre-se de atualizar as credenciais antes que expirem para manter o fluxo de dados para a Braze.
{% endalert %}

#### Etapa 1.2: Conceder acesso aos recursos do Fabric {#step-12-grant-access-to-fabric-resources}
Forneça acesso para a Braze se conectar à sua instância do Fabric. No portal de administração do Fabric, navegue até **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* Em **Developer settings**, ative **Service principals can use Fabric APIs** para que a Braze possa se conectar usando o Microsoft Entra ID.
* Em **OneLake settings**, ative **Users can access data stored in OneLake with apps external to Fabric** para que o service principal possa acessar dados de um app externo.

#### Etapa 1.3: Configurar um espaço de trabalho compartilhado e conceder acesso {#step-13-set-up-a-shared-workspace-and-grant-access}

Quaisquer recursos do Fabric que deseje conectar à Braze devem ser colocados em um espaço de trabalho compartilhado. Se você só usou o **My Workspace** padrão, crie um novo espaço de trabalho compartilhado:

1. No menu de navegação, selecione **Workspaces** e, em seguida, selecione **+ New workspace**.
2. Insira um **Name** para o espaço de trabalho e selecione **Apply**.

Após ter um espaço de trabalho compartilhado, conceda ao service principal acesso:

1. Selecione o espaço de trabalho e, em seguida, selecione **Manage Access**.
2. Selecione **+ Add people or groups**.
3. Pesquise e selecione o nome do service principal que você criou na etapa 1.1. Se ele não aparecer, confirme que você ativou a configuração **Service principals can use Fabric APIs** na etapa 1.2.
4. No menu suspenso de role, selecione **Contributor**.

O service principal agora pode acessar os recursos do Fabric warehouse neste espaço de trabalho por meio de seus endpoints SQL, incluindo o warehouse a ser usado para a Braze.

#### Etapa 1.4: Configurar a tabela {#step-14-set-up-the-table}
A Braze suporta tanto tabelas quanto views em Fabric Warehouses. Se precisar criar um novo warehouse, crie-o no espaço de trabalho compartilhado da etapa 1.3. Acesse **Create > Data Warehouse > Warehouse** no console do Fabric.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Você pode nomear o warehouse, schema e tabela ou view como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - O momento em que esta linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no exato timestamp de limite podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.
- **Colunas de identificação do usuário** - Sua tabela pode conter uma ou mais colunas de identificação do usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica o usuário que deseja atualizar. Deve corresponder ao valor `external_id` usado na Braze.
    - `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter múltiplos aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário da Braze. É gerado pelo SDK or kit de desenvolvimento de software da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da ingestão de dados na nuvem. Para criar novos usuários, especifique um ID externo de usuário ou alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se existirem múltiplos perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente é priorizado para atualizações. Se você incluir tanto e-mail quanto telefone, o e-mail é usado como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se existirem múltiplos perfis com o mesmo número de telefone, o perfil atualizado mais recentemente é priorizado para atualizações.
- `PAYLOAD` - Esta é uma string JSON dos campos que deseja sincronizar com o usuário na Braze.


#### Etapa 1.5: Obter a string de conexão do warehouse {#step-15-get-warehouse-connection-string}
Para obter o endpoint SQL do seu warehouse, acesse o **workspace** no Fabric, passe o mouse sobre o nome do warehouse na lista de itens e selecione **Copy SQL connection string**.

![A página do console do Fabric no Microsoft Azure, onde os usuários devem obter a string de conexão SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Etapa 1.6: Permitir IPs da Braze no firewall (opcional) {#step-16-allow-braze-ips-in-firewall-optional}

Dependendo da configuração da sua conta do Microsoft Fabric, pode ser necessário permitir os seguintes endereços IP no seu firewall para liberar o tráfego da Braze. Para saber mais sobre como ativar isso, consulte a documentação relevante sobre [Acesso Condicional do Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Etapa 2: Criar uma nova fonte no dashboard da Braze {#step-2-create-a-new-source-in-the-braze-dashboard}


{% tabs %}
{% tab Snowflake %}

No dashboard da Braze, acesse **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecione **Add data source** e, em seguida, selecione **Snowflake**.

#### Etapa 2.1: Adicionar informações de conexão do Snowflake {#step-21-add-snowflake-connection-information}

Escolha um nome para sua fonte e insira suas credenciais e configuração do Snowflake, depois prossiga para a próxima etapa.

Antes de continuar, confirme o valor que você inseriu em **Snowflake Account Locator**.

Para o campo **Snowflake Account Locator**, insira o [identificador da sua conta](https://docs.snowflake.com/en/user-guide/admin-account-identifier) do Snowflake. Insira apenas o valor do identificador da conta, como `myorganization-myaccount`. Não inclua `https://`, `.snowflakecomputing.com`, nem nenhum caminho.

Para encontrar o identificador da sua conta do Snowflake:

1. No Snowsight, selecione o menu da sua conta.
2. Selecione **View account details**.
3. Copie o valor do **Account identifier**.
4. Se copiar de uma URL do Snowflake, use apenas o valor antes de `.snowflakecomputing.com`.

#### Etapa 2.2: Adicionar uma chave pública ao usuário da Braze {#step-22-add-a-public-key-to-the-braze-user}

Após inserir suas credenciais e configuração, clique em **Save credentials** e gere uma chave RSA e volte ao Snowflake para concluir a configuração. Adicione a chave pública exibida no dashboard ao usuário que você criou para a Braze se conectar ao Snowflake.

Para saber mais sobre como fazer isso, consulte a [documentação do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Se quiser fazer a rotação das chaves em qualquer momento, a Braze pode gerar um novo par de chaves e fornecer a nova chave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

No dashboard da Braze, acesse **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecione **Add data source** e, em seguida, selecione **Amazon Redshift**.

#### Etapa 2.1: Adicionar informações de conexão do Redshift e tabela de origem {#step-21-add-redshift-connection-information-and-source-table}

Escolha um nome para sua fonte e insira suas credenciais e configuração do Redshift. Se estiver usando um túnel de rede privada, ative o botão e insira as informações do túnel. Em seguida, prossiga para a próxima etapa.

{% alert note %}
No dashboard da Braze, o campo **Database name** aceita apenas letras (A–Z, a–z), números (0–9) e sublinhados (_), mesmo que o Amazon Redshift suporte caracteres adicionais em identificadores de banco de dados.
{% endalert %}

#### Etapa 2.2: Testar a conexão e conectar à fonte {#step-22-test-connection-and-connect-to-source}

Em seguida, selecione **Test connection**. Quando for bem-sucedido, finalize as configurações restantes e clique em **Connect to Source**. Se a conexão falhar, uma mensagem de erro aparecerá para ajudar na solução do problema.

#### Solução de problemas: identificador de snapshot inválido {#troubleshooting-invalid-snapshot-identifier}

Se a Braze retornar um erro `Invalid snapshot identifier` durante **Test connection** ou a configuração de sincronização, o Redshift não consegue resolver a referência de snapshot usada quando o objeto de origem é consultado.

No Redshift, um snapshot é um backup point-in-time de um cluster. Cada snapshot tem um identificador único usado pelo Redshift para referenciar aquele estado de backup. Para saber mais, consulte [Snapshots e backups do Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html).

Esse erro pode ocorrer quando metadados mudam enquanto a Braze valida o objeto de origem, como durante operações de cópia, restauração ou replicação de snapshots. Para saber mais, consulte [copiar snapshots para outra região AWS](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html) e [restaurar um cluster a partir de um snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-cluster-from-snapshot.html).

Para solucionar:

1. Verifique as configurações da fonte na Braze, incluindo endpoint do cluster, banco de dados, schema e nome do objeto.
2. Execute a mesma consulta diretamente no Redshift para confirmar que a tabela ou view é legível e estável.
3. Tente novamente após a conclusão de atividades de snapshot, restauração, redimensionamento ou replicação.
4. Se o problema persistir, consulte uma materialized view em vez de uma tabela base que muda frequentemente.

Uma materialized view armazena resultados de consultas pré-computados que podem ser atualizados em um cronograma, o que pode tornar as leituras mais estáveis para sincronizações CDI. Para saber mais, consulte [materialized views no Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html).

Exemplo:

```sql
CREATE MATERIALIZED VIEW ingestion.users_attributes_mv AS
SELECT updated_at, external_id, alias_label, alias_name, braze_id, email, phone, payload
FROM ingestion.users_attributes_sync;

REFRESH MATERIALIZED VIEW ingestion.users_attributes_mv;
```

Após criar a materialized view, use o nome da materialized view como o objeto de origem na sua sincronização CDI da Braze em vez da tabela base.
{% endtab %}
{% tab BigQuery %}

No dashboard da Braze, acesse **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecione **Add data source** e, em seguida, selecione **Google BigQuery**.

#### Etapa 2.1: Adicionar informações de conexão do BigQuery e tabela de origem {#step-21-add-bigquery-connection-information-and-source-table}

Escolha um nome para sua fonte. Em seguida, faça o upload da chave JSON e forneça um nome para a conta de serviço. Depois, insira os campos de configuração restantes.

#### Etapa 2.2: Testar a conexão e conectar à fonte

Em seguida, selecione **Test connection**. Quando for bem-sucedido, finalize as configurações restantes e clique em **Connect to Source**. Se a conexão falhar, uma mensagem de erro aparecerá para ajudar na solução do problema.

{% endtab %}
{% tab Databricks %}

No dashboard da Braze, acesse **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecione **Add data source** e, em seguida, selecione **Databricks**.

#### Etapa 2.1: Adicionar informações de conexão do Databricks e tabela de origem {#step-21-add-databricks-connection-information-and-source-table}

Escolha um nome para sua fonte e insira suas credenciais e configuração do Databricks. Em seguida, prossiga para a próxima etapa.

#### Etapa 2.2: Testar a conexão e conectar à fonte

Em seguida, selecione **Test connection**. Quando for bem-sucedido, finalize as configurações restantes e clique em **Connect to Source**. Se a conexão falhar, uma mensagem de erro aparecerá para ajudar na solução do problema.

{% alert note %}
Você deve testar a fonte com sucesso antes que ela possa ser criada. Se fechar a página de criação, sua fonte não será salva.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

No dashboard da Braze, acesse Data Settings > Cloud Data Ingestion > Sources, selecione **Add data source** e, em seguida, selecione **Microsoft Fabric**.

#### Etapa 2.1: Configurar uma sincronização de ingestão de dados na nuvem {#step-21-set-up-a-cloud-data-ingestion-sync}

Escolha um nome para sua fonte e insira suas credenciais e configuração do Microsoft Fabric.
- **Credentials Name** é um rótulo para essas credenciais na Braze; você pode definir um valor útil aqui
- Consulte as etapas na seção 1 para saber como obter o Tenant ID, Principal ID, Client Secret e Connection String

#### Etapa 2.2: Testar a conexão e conectar à fonte

Em seguida, selecione **Test connection**. Quando for bem-sucedido, finalize as configurações restantes e clique em **Connect to Source**. Se a conexão falhar, uma mensagem de erro aparecerá para ajudar na solução do problema.

{% alert note %}
Você deve testar a fonte com sucesso antes que ela possa ser criada. Se fechar a página de criação, sua fonte não será salva.
{% endalert %}

{% endtab %}

{% endtabs %}

### Etapa 3: Criar uma nova sincronização no dashboard da Braze {#step-3-create-a-new-sync-in-the-braze-dashboard}
Acesse **Data Settings** > **Cloud Data Ingestion** > **Syncs** e selecione **Create data sync**.

{% tabs %}
{% tab Snowflake %}

#### Etapa 3.1: Configurar os detalhes da sincronização e testar a conexão {#step-31-configure-sync-details-and-test-connection}
Escolha um nome para sua sincronização. Em seguida, selecione qualquer fonte ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e clique em **Test Connection**.

Quando for bem-sucedido, uma prévia dos dados aparecerá. Selecione **Next: Notifications** para continuar. Se a conexão falhar, uma mensagem de erro aparecerá para ajudar na solução do problema.

{% alert note %}
Você deve testar a sincronização com sucesso antes de prosseguir para as próximas etapas. Se precisar fechar a página de criação da sincronização, clique em **Save as draft** para salvar seu progresso.
{% endalert %}

#### Etapa 3.2: Adicionar preferências de notificação {#step-32-add-notification-preferences}
Insira o(s) e-mail(s) de contato para notificações de erros de sincronização. A Braze usa essas informações de contato para enviar notificações sobre erros de integração, como perda inesperada de acesso à tabela.

Os e-mails de contato recebem notificações apenas de erros globais ou no nível da sincronização, como tabelas ausentes, permissões e outros. Eles não recebem problemas no nível de linha. Erros globais indicam problemas críticos na conexão que impedem a execução das sincronizações.

Esses problemas podem incluir:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Apenas para sincronizações de catálogos) O nível do catálogo está sem espaço

#### Etapa 3.3: Agendamento {#step-33-scheduling}
Por último, configure sua sincronização como não recorrente ou recorrente.

Sincronizações não recorrentes podem ser acionadas manualmente ou via API or interface de programação do aplicativo (API).

Sincronizações recorrentes podem ter uma frequência de 15 em 15 minutos até uma vez por mês. A Braze agenda a sincronização recorrente no fuso horário UTC.

{% endtab %}

{% tab Redshift %}

#### Etapa 3.1: Configurar os detalhes da sincronização e testar a conexão
Escolha um nome para sua sincronização. Em seguida, selecione qualquer fonte ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e clique em **Test Connection**.

Quando for bem-sucedido, uma prévia dos dados aparecerá. Selecione **Next: Notifications** para continuar. Se a conexão falhar, uma mensagem de erro aparecerá para ajudar na solução do problema.

{% alert note %}
Você deve testar a sincronização com sucesso antes de prosseguir para as próximas etapas. Se precisar fechar a página de criação da sincronização, clique em **Save as draft** para salvar seu progresso.
{% endalert %}

#### Etapa 3.2: Adicionar preferências de notificação
Insira o(s) e-mail(s) de contato para notificações de erros de sincronização. A Braze usa essas informações de contato para enviar notificações sobre erros de integração, como perda inesperada de acesso à tabela.

Os e-mails de contato recebem notificações apenas de erros globais ou no nível da sincronização, como tabelas ausentes, permissões e outros. Eles não recebem problemas no nível de linha. Erros globais indicam problemas críticos na conexão que impedem a execução das sincronizações.

Esses problemas podem incluir:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões

(Apenas para sincronizações de catálogos) O nível do catálogo está sem espaço

#### Etapa 3.3: Agendamento
Por último, configure sua sincronização como não recorrente ou recorrente.

Sincronizações não recorrentes podem ser acionadas manualmente ou via API or interface de programação do aplicativo (API).

Sincronizações recorrentes podem ter uma frequência de 15 em 15 minutos até uma vez por mês. A Braze agenda a sincronização recorrente no fuso horário UTC.

{% endtab %}

{% tab BigQuery %}

#### Etapa 3.1: Configurar os detalhes da sincronização e testar a conexão
Escolha um nome para sua sincronização. Em seguida, selecione qualquer fonte ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e clique em **Test Connection**.

Quando for bem-sucedido, uma prévia dos dados aparecerá. Selecione **Next: Notifications** para continuar. Se a conexão falhar, uma mensagem de erro aparecerá para ajudar na solução do problema.

{% alert note %}
Você deve testar a sincronização com sucesso antes de prosseguir para as próximas etapas. Se precisar fechar a página de criação da sincronização, clique em **Save as draft** para salvar seu progresso.
{% endalert %}

#### Etapa 3.2: Adicionar preferências de notificação
Insira o(s) e-mail(s) de contato para notificações de erros de sincronização. A Braze usa essas informações de contato para enviar notificações sobre erros de integração, como perda inesperada de acesso à tabela.

Os e-mails de contato recebem notificações apenas de erros globais ou no nível da sincronização, como tabelas ausentes, permissões e outros. Eles não recebem problemas no nível de linha. Erros globais indicam problemas críticos na conexão que impedem a execução das sincronizações. Esses problemas podem incluir:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões

(Apenas para sincronizações de catálogos) O nível do catálogo está sem espaço

#### Etapa 3.3: Agendamento
Por último, configure sua sincronização como não recorrente ou recorrente.

Sincronizações não recorrentes podem ser acionadas manualmente ou via API or interface de programação do aplicativo (API).

Sincronizações recorrentes podem ter uma frequência de 15 em 15 minutos até uma vez por mês. A Braze agenda a sincronização recorrente no fuso horário UTC.

{% endtab %}

{% tab Databricks %}

#### Etapa 3.1: Configurar os detalhes da sincronização e testar a conexão
Escolha um nome para sua sincronização. Em seguida, selecione qualquer fonte ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e clique em **Test Connection**.

Quando for bem-sucedido, uma prévia dos dados aparecerá. Selecione **Next: Notifications** para continuar. Se a conexão falhar, uma mensagem de erro aparecerá para ajudar na solução do problema.

{% alert note %}
Você deve testar a sincronização com sucesso antes de prosseguir para as próximas etapas. Se precisar fechar a página de criação da sincronização, clique em **Save as draft** para salvar seu progresso.
{% endalert %}

#### Etapa 3.2: Adicionar preferências de notificação
Insira o(s) e-mail(s) de contato para notificações de erros de sincronização. A Braze usa essas informações de contato para enviar notificações sobre erros de integração, como perda inesperada de acesso à tabela.

Os e-mails de contato recebem notificações apenas de erros globais ou no nível da sincronização, como tabelas ausentes, permissões e outros. Eles não recebem problemas no nível de linha. Erros globais indicam problemas críticos na conexão que impedem a execução das sincronizações.

Esses problemas podem incluir:
- Problemas de conectividade
- Falta de recursos
- Problemas de permissões

(Apenas para sincronizações de catálogos) O nível do catálogo está sem espaço

#### Etapa 3.3: Agendamento
Por último, configure sua sincronização como não recorrente ou recorrente.

Sincronizações não recorrentes podem ser acionadas manualmente ou via API or interface de programação do aplicativo (API).

Sincronizações recorrentes podem ter uma frequência de 15 em 15 minutos até uma vez por mês. A Braze agenda a sincronização recorrente no fuso horário UTC.

{% endtab %}
{% tab Microsoft Fabric %}

#### Etapa 3.1: Configurar os detalhes da sincronização e testar a conexão

Escolha um nome para sua sincronização. Em seguida, selecione qualquer fonte ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e clique em **Test Connection**.

Quando for bem-sucedido, uma prévia dos dados aparecerá. Selecione **Next: Notifications** para continuar. Se a conexão falhar, uma mensagem de erro aparecerá para ajudar na solução do problema.

{% alert note %}
Você deve testar a sincronização com sucesso antes de prosseguir para as próximas etapas. Se precisar fechar a página de criação da sincronização, clique em **Save as draft** para salvar seu progresso.
{% endalert %}

#### Etapa 3.2: Adicionar preferências de notificação
Insira o(s) e-mail(s) de contato para notificações de erros de sincronização. A Braze usa essas informações de contato para enviar notificações sobre erros de integração, como perda inesperada de acesso à tabela.

Os e-mails de contato recebem notificações apenas de erros globais ou no nível da sincronização, como tabelas ausentes, permissões e outros. Eles não recebem problemas no nível de linha. Erros globais indicam problemas críticos na conexão que impedem a execução das sincronizações.

Esses problemas podem incluir:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões

(Apenas para sincronizações de catálogos) O nível do catálogo está sem espaço

#### Etapa 3.3: Agendamento
Por último, configure sua sincronização como não recorrente ou recorrente.

Sincronizações não recorrentes podem ser acionadas manualmente ou via API or interface de programação do aplicativo (API).

Sincronizações recorrentes podem ter uma frequência de 15 em 15 minutos até uma vez por mês. A Braze agenda a sincronização recorrente no fuso horário UTC.

{% endtab %}
{% endtabs %}

{% alert note %}
Você deve testar uma integração com sucesso antes que ela possa passar do estado Rascunho para Ativo. Se fechar a página de criação, sua integração será salva, e você poderá revisitar a página de detalhes para fazer alterações e testar.
{% endalert %}

## Configurar integrações ou usuários adicionais (opcional) {#set-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar credenciais existentes se estiver conectando à mesma conta do Snowflake.

Se você reutilizar o mesmo usuário e a mesma função entre integrações, não será necessário adicionar a chave pública novamente.
{% endtab %}
{% tab Redshift %}
Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar credenciais existentes se estiver conectando à mesma conta do Snowflake ou do Redshift.

Se você reutilizar o mesmo usuário entre integrações, não será possível excluir o usuário no dashboard da Braze até que ele seja removido de todas as sincronizações ativas.
{% endtab %}
{% tab BigQuery %}

Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar credenciais existentes se estiver conectando à mesma conta do BigQuery.

Se você reutilizar o mesmo usuário entre integrações, não será possível excluir o usuário no dashboard da Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% tab Databricks %}

Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar credenciais existentes se estiver conectando à mesma conta do Databricks.

Se você reutilizar o mesmo usuário entre integrações, não será possível excluir o usuário no dashboard da Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% tab Microsoft Fabric %}

Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar credenciais existentes se estiver conectando à mesma conta do Fabric.

Se você reutilizar o mesmo usuário entre integrações, não será possível excluir o usuário no dashboard da Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% endtabs %}

## Executando a sincronização {#running-the-sync}

{% tabs %}
{% tab Snowflake %}
Quando ativada, sua sincronização é executada no cronograma configurado durante a configuração. Se você quiser executar a sincronização fora do cronograma normal de testes ou buscar os dados mais recentes, selecione **Sync Now**. Essa execução não afeta as sincronizações futuras programadas regularmente.

{% endtab %}
{% tab Redshift %}
Quando ativada, sua sincronização é executada no cronograma configurado durante a configuração. Se você quiser executar a sincronização fora do cronograma normal de testes ou buscar os dados mais recentes, selecione **Sync Now**. Essa execução não afeta as sincronizações futuras programadas regularmente.

{% endtab %}
{% tab BigQuery %}

Quando ativada, sua sincronização é executada no cronograma configurado durante a configuração. Se você quiser executar a sincronização fora do cronograma normal de testes ou buscar os dados mais recentes, selecione **Sync Now**. Essa execução não afeta as sincronizações futuras programadas regularmente.

{% endtab %}
{% tab Databricks %}

Quando ativada, sua sincronização é executada no cronograma configurado durante a configuração. Se você quiser executar a sincronização fora do cronograma normal de testes ou buscar os dados mais recentes, selecione **Sync Now**. Essa execução não afeta as sincronizações futuras programadas regularmente.

{% endtab %}
{% tab Microsoft Fabric %}

Quando ativada, sua sincronização é executada no cronograma configurado durante a configuração. Se você quiser executar a sincronização fora do cronograma normal de testes ou buscar os dados mais recentes, selecione **Sync Now**. Essa execução não afeta as sincronizações futuras programadas regularmente.

{% endtab %}

{% endtabs %}