---
nav_title: Integrações de data warehouse
article_title: Integrações de data warehouse
alias: /partners/databricks/
description: "Esta página aborda como usar a Ingestão de Dados na Nuvem da Braze para sincronizar dados relevantes com sua integração do Snowflake, Redshift, BigQuery e Databricks."
page_order: 3
page_type: reference

---

# Integrações de armazenamento de data warehouse {#data-warehouse-storage-integrations}

> Esta página aborda como usar a Ingestão de Dados na Nuvem (CDI) da Braze para sincronizar dados relevantes com sua integração do Snowflake, Redshift, BigQuery e Databricks.

## Configuração de integrações de data warehouse {#setting-up-data-warehouse-integrations}

As integrações de Ingestão de Dados na Nuvem exigem algumas configurações no lado da Braze e na instância do seu data warehouse. Siga estas etapas para configurar a integração:

{% tabs %}
{% tab Snowflake %}
1. Na sua instância do Snowflake, configure as tabelas ou views que deseja sincronizar com a Braze.
2. Crie uma nova origem do Snowflake no dashboard da Braze.
3. Recupere a chave pública fornecida no dashboard da Braze e [anexe-a ao usuário do Snowflake para autenticação](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Crie uma sincronização no dashboard da Braze, teste a integração e inicie a sincronização.

{% alert tip %}
O [guia de início rápido do Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) fornece um código de exemplo e percorre as etapas necessárias para criar um pipeline automatizado usando o Snowflake Streams e o CDI para sincronizar dados com a Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Certifique-se de que o acesso da Braze seja permitido às tabelas do Redshift que você deseja sincronizar. A Braze se conecta ao Redshift pela internet.
2. Na sua instância do Redshift, configure as tabelas ou views que deseja sincronizar com a Braze.
3. Crie uma nova origem e sincronização no dashboard da Braze.
4. Teste a integração e inicie a sincronização.

{% alert note %}
As linhas processadas por sincronização dependem do desempenho do seu warehouse, da latência de rede e da quantidade de dados novos que correspondem à consulta de sincronização. Use o **Histórico de sincronização** da integração no dashboard para ver a duração e a contagem de linhas das execuções recentes.
{% endalert %}
{% endtab %}
{% tab BigQuery %}
1. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do BigQuery que contêm os dados que você deseja sincronizar.
2. Na sua conta do BigQuery, configure as tabelas ou views que deseja sincronizar com a Braze.
3. Crie uma nova origem e sincronização no dashboard da Braze.
4. Teste a integração e inicie a sincronização.
{% endtab %}
{% tab Databricks %}
1. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do Databricks que contêm os dados que você deseja sincronizar.
2. Na sua conta do Databricks, configure as tabelas ou views que deseja sincronizar com a Braze.
3. Crie uma nova origem e sincronização no dashboard da Braze.
4. Teste a integração e inicie a sincronização.

{% alert important %}
Pode haver de dois a cinco minutos de tempo de aquecimento quando a Braze se conecta às instâncias SQL Classic e Pro, o que pode causar atrasos durante a configuração e o teste da conexão, bem como no início das sincronizações agendadas. O uso de uma instância SQL serverless minimiza o tempo de aquecimento e melhora a taxa de transferência de consultas, mas pode resultar em custos de integração ligeiramente mais altos.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Crie uma entidade de serviço e conceda acesso às APIs do Fabric.
2. Configure um espaço de trabalho compartilhado e conceda à entidade de serviço acesso a ele.
3. No espaço de trabalho compartilhado do Fabric, configure as tabelas ou views que deseja sincronizar com a Braze.
4. Crie uma nova origem e sincronização no dashboard da Braze.
5. Teste a integração e inicie a sincronização.
{% endtab %}
{% endtabs %}

### Etapa 1: Configurar tabelas ou views {#step-1-set-up-tables-or-views}

Antes de começar, revise [Configuração de tabelas para Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup) para entender os requisitos da tabela de origem em comparação com os requisitos de formatação de `PAYLOAD`.

{% alert note %}
Sua tabela ou view de origem pode incluir colunas que não estão listadas para o seu warehouse nas guias da seção a seguir (por exemplo, auditoria ou hashing). A Braze lê apenas as colunas descritas nessas guias; outras colunas não são usadas durante as sincronizações de Ingestão de Dados na Nuvem.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

#### Etapa 1.1: Preparar a tabela {#step-11-set-up-the-table}

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

Você pode nomear o banco de dados, o esquema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no limite exato do timestamp podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.
- **Colunas de identificador de usuário** - Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado na Braze.
    - `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário da Braze. Ele é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da Ingestão de Dados na Nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se existirem vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade. Se você incluir tanto e-mail quanto telefone, o e-mail será usado como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se existirem vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade.
- `PAYLOAD` - Uma string JSON dos campos que você deseja sincronizar com o usuário na Braze.

#### Etapa 1.2: Configurar a função e as permissões do banco de dados {#step-12-set-up-the-role-and-database-permissions}

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Atualize os nomes conforme necessário, mas as permissões devem corresponder ao exemplo anterior.

#### Etapa 1.3: Configurar o warehouse e dar acesso à função da Braze {#step-13-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
O warehouse precisa ter o sinalizador de **retomada automática** ativado. Caso contrário, conceda à Braze privilégios adicionais de `OPERATE` no warehouse para que a Braze possa ativá-lo quando a consulta for executada.
{% endalert %}

#### Etapa 1.4: Configurar o usuário {#step-14-set-up-the-user}

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Após essa etapa, compartilhe as informações de conexão com a Braze para receber uma chave pública para anexar ao usuário.

{% alert note %}
Ao conectar diferentes espaços de trabalho à mesma conta do Snowflake, é necessário criar um usuário exclusivo para cada espaço de trabalho da Braze em que estiver criando uma integração. Dentro de um espaço de trabalho, é possível reutilizar o mesmo usuário em todas as integrações, mas a criação da integração falhará se um usuário na mesma conta do Snowflake for duplicado entre espaços de trabalho.
{% endalert %}

#### Etapa 1.5: Permitir IPs da Braze na política de rede do Snowflake (opcional) {#step-15-allow-braze-ips-in-snowflake-network-policy-optional}

Dependendo da configuração da sua conta do Snowflake, talvez seja necessário permitir os seguintes endereços IP na sua política de rede do Snowflake. Para saber mais sobre como ativar isso, consulte a documentação relevante do Snowflake sobre a [modificação de uma política de rede](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Etapa 1.1: Preparar a tabela

Opcionalmente, configure um novo banco de dados e esquema para manter sua tabela de origem
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

Você pode nomear o banco de dados, o esquema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no limite exato do timestamp podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.
- **Colunas de identificador de usuário** - Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado na Braze.
    - `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário da Braze. Ele é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da Ingestão de Dados na Nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se existirem vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade. Se você incluir tanto e-mail quanto telefone, o e-mail será usado como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se existirem vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade.
- `PAYLOAD` - Uma string JSON dos campos que você deseja sincronizar com o usuário na Braze.

#### Etapa 1.2: Criar usuário e conceder permissões {#step-12-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Essas são as permissões mínimas necessárias para esse usuário. Se estiver criando várias integrações CDI, talvez você queira conceder permissões a um esquema ou gerenciar as permissões usando um grupo.

#### Etapa 1.3: Permitir acesso aos IPs da Braze {#step-13-allow-access-to-braze-ips}

Se você tiver um firewall ou outras políticas de rede, deverá conceder à Braze acesso de rede à sua instância do Redshift. Um exemplo de endpoint de URL do Redshift é "example-cluster.ap-northeast-2.redshift.amazonaws.com".

Alguns aspectos importantes:
- Também pode ser necessário alterar seus grupos de segurança para permitir que a Braze acesse seus dados no Redshift.
- Certifique-se de permitir explicitamente o tráfego de entrada nos IPs da tabela e na porta usada para consultar seu cluster Redshift (o padrão é 5439). Você deve permitir explicitamente a conectividade TCP do Redshift nessa porta, mesmo que as regras de entrada estejam definidas como "permitir tudo".
- O endpoint do cluster Redshift deve ser acessível publicamente para que a Braze se conecte ao seu cluster.
     - Se não quiser que o cluster do Redshift seja acessível publicamente, você pode configurar uma instância VPC e EC2 para usar um túnel SSH para acessar os dados do Redshift. Para saber mais, confira esta [postagem do Centro de Conhecimento da AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).

Permita o acesso dos seguintes IPs correspondentes à região do seu dashboard da Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Etapa 1.1: Preparar a tabela

Opcionalmente, configure um novo projeto ou conjunto de dados para manter sua tabela de origem.

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
| `UPDATED_AT` | TIMESTAMP | OBRIGATÓRIO |
| `PAYLOAD` | JSON | OBRIGATÓRIO |
| `EXTERNAL_ID` | STRING | NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
| `BRAZE_ID` | STRING | NULLABLE |
| `EMAIL` | STRING | NULLABLE |
| `PHONE` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 1.1: Preparar a tabela" }

Você pode nomear o projeto, o conjunto de dados e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no limite exato do timestamp podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.
- **Colunas de identificador de usuário** - Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado na Braze.
    - `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário da Braze. Ele é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da Ingestão de Dados na Nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se existirem vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade. Se você incluir tanto e-mail quanto telefone, o e-mail será usado como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se existirem vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade.
- `PAYLOAD` - Uma string JSON dos campos que você deseja sincronizar com o usuário na Braze.

{% alert important %}
**Particionamento do BigQuery**

O CDI suporta partições para o BigQuery. Se você particionar por uma função de `UPDATED_AT` (por exemplo, na granularidade de um dia, semana ou hora, dependendo do tamanho do seu conjunto de dados), o BigQuery pode eliminar os dados que precisa escanear. Isso melhora o desempenho e a eficiência para tabelas muito grandes.

Não particione por nenhum outro campo. Teste diferentes configurações para encontrar a melhor opção para seus dados específicos.

Todas as consultas do CDI filtram por `UPDATED_AT`, mas esse comportamento pode mudar. Projete o esquema da sua tabela para _não_ exigir que as consultas incluam essa cláusula.

Para saber mais, consulte a [documentação de particionamento do BigQuery](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).
{% endalert %}

#### Etapa 1.2: Criar uma conta de serviço e conceder permissões {#step-12-create-a-service-account-and-grant-permissions}

Crie uma conta de serviço no GCP para a Braze usar para se conectar e ler dados da(s) sua(s) tabela(s). A conta de serviço deve ter as seguintes permissões:

- **BigQuery Connection User:** Permite que a Braze faça conexões
- **BigQuery User:** Fornece à Braze acesso para executar consultas, ler metadados de conjuntos de dados e listar tabelas.
- **BigQuery Data Viewer:** Fornece à Braze acesso para visualizar conjuntos de dados e seus conteúdos.
- **BigQuery Job User:** Fornece à Braze acesso para executar jobs

Depois de criar a conta de serviço e conceder permissões, gere uma chave JSON. Para saber mais, consulte [Criar e excluir chaves de conta de serviço](https://cloud.google.com/iam/docs/keys-create-delete). Você fará o upload dessa chave no dashboard da Braze em uma etapa posterior.

#### Etapa 1.3: Permitir acesso aos IPs da Braze

Se você tiver políticas de rede em vigor, deverá conceder à Braze acesso de rede à sua instância do BigQuery. Permita o acesso dos seguintes IPs correspondentes à região do seu dashboard da Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Etapa 1.1: Preparar a tabela

Opcionalmente, configure um novo catálogo ou esquema para manter sua tabela de origem.

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
| `UPDATED_AT` | TIMESTAMP | OBRIGATÓRIO |
| `PAYLOAD` | STRING, STRUCT ou MAP | OBRIGATÓRIO |
| `EXTERNAL_ID` | STRING | NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
| `BRAZE_ID` | STRING | NULLABLE |
| `EMAIL` | STRING | NULLABLE |
| `PHONE` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 1.1: Preparar a tabela" }

Você pode nomear o esquema e a tabela como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no limite exato do timestamp podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.
- **Colunas de identificador de usuário** - Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado na Braze.
    - `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário da Braze. Ele é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da Ingestão de Dados na Nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se existirem vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade. Se você incluir tanto e-mail quanto telefone, o e-mail será usado como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se existirem vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade.
- `PAYLOAD` - Uma string ou struct dos campos que você deseja sincronizar com o usuário na Braze.

#### Etapa 1.2: Criar um token de acesso {#step-12-create-an-access-token}

Para que a Braze acesse o Databricks, é necessário criar um token de acesso pessoal.

1. No seu espaço de trabalho do Databricks, selecione seu nome de usuário do Databricks na barra superior e, em seguida, selecione **User Settings** no menu suspenso.
2. Na guia Access tokens, selecione **Generate new token**.
3. Digite um comentário que ajude a identificar esse token, como "Braze CDI", e altere o tempo de vida do token para sem limite, deixando a caixa Lifetime (days) vazia (em branco).
4. Selecione **Generate**.
5. Copie o token exibido e selecione **Done**.

Mantenha o token em um local seguro até que seja necessário inseri-lo no dashboard da Braze durante a etapa de criação de credenciais.

#### Etapa 1.3: Permitir acesso aos IPs da Braze

Se você tiver políticas de rede em vigor, deverá conceder à Braze acesso de rede à sua instância do Databricks. Permita o acesso dos seguintes IPs correspondentes à região do seu dashboard da Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Etapa 1.1: Configurar a entidade de serviço e conceder acesso {#step-11-set-up-the-service-principal-and-grant-access}
A Braze se conecta ao seu warehouse do Fabric usando uma entidade de serviço com autenticação Entra ID. Crie uma nova entidade de serviço para a Braze usar e conceda acesso aos recursos do Fabric conforme necessário. A Braze precisa dos seguintes dados para se conectar:

* ID do locatário (também chamado de diretório) da sua conta do Azure
* ID da entidade principal (também chamada de ID do aplicativo) da entidade de serviço
* Segredo do cliente para autenticação da Braze

1. No portal do Azure, navegue até o centro de administração do Microsoft Entra e, em seguida, Registros de app
2. Selecione **+ New registration** em **Identity** > **Applications** > **App registrations**.
3. Digite um nome e selecione `Accounts in this organizational directory only` como o tipo de conta compatível. Em seguida, selecione **Register**.
4. Selecione o aplicativo (entidade de serviço) que você acabou de criar, depois navegue até **Certificates & secrets** > **+ New client secret**.
5. Digite uma descrição para o segredo e defina um período de vencimento. Em seguida, selecione **Add**.
6. Anote o segredo do cliente criado para usar na configuração da Braze.

{% alert note %}
O Azure não permite vencimento ilimitado dos segredos da entidade de serviço. Lembre-se de atualizar as credenciais antes que elas expirem para manter o fluxo de dados para a Braze.
{% endalert %}

#### Etapa 1.2: Conceder acesso aos recursos do Fabric {#step-12-grant-access-to-fabric-resources}
Forneça acesso para que a Braze se conecte à sua instância do Fabric. No portal de administração do Fabric, navegue até **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* Em **Developer settings**, ative a opção **Service principals can use Fabric APIs** para que a Braze possa se conectar usando o Microsoft Entra ID.
* Em **OneLake settings**, ative a opção **Users can access data stored in OneLake with apps external to Fabric** para que a entidade de serviço possa acessar os dados de um app externo.

#### Etapa 1.3: Configurar um espaço de trabalho compartilhado e conceder acesso {#step-13-set-up-a-shared-workspace-and-grant-access}

Todos os recursos do Fabric que você deseja conectar à Braze devem ser colocados em um espaço de trabalho compartilhado. Se você estiver usando apenas o **My Workspace** padrão, crie um novo espaço de trabalho compartilhado:

1. No menu de navegação, selecione **Workspaces** e, em seguida, selecione **+ New workspace**.
2. Insira um **Name** para o espaço de trabalho e selecione **Apply**.

Depois de ter um espaço de trabalho compartilhado, conceda à entidade de serviço o acesso:

1. Selecione o espaço de trabalho e, em seguida, selecione **Manage Access**.
2. Selecione **+ Add people or groups**.
3. Pesquise e selecione o nome da entidade de serviço que você criou na Etapa 1.1. Se ela não aparecer, confirme que você ativou a configuração **Service principals can use Fabric APIs** na Etapa 1.2.
4. No menu suspenso de função, selecione **Contributor**.

A entidade de serviço agora pode acessar os recursos do warehouse do Fabric neste espaço de trabalho por meio dos endpoints SQL, incluindo o warehouse a ser usado para a Braze.

#### Etapa 1.4: Preparar a tabela {#step-14-set-up-the-table}
A Braze oferece suporte a tabelas e views em Fabric Warehouses. Se precisar criar um novo warehouse, crie-o dentro do espaço de trabalho compartilhado da Etapa 1.3. Acesse **Create > Data Warehouse > Warehouse** no console do Fabric.

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

Você pode nomear o warehouse, o esquema e a tabela ou view como quiser, mas os nomes das colunas devem corresponder à definição anterior.

- `UPDATED_AT` - A hora em que essa linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no limite exato do timestamp podem ser ressincronizadas se novas linhas compartilharem o mesmo timestamp.
- **Colunas de identificador de usuário** - Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador (`external_id`, a combinação de `alias_name` e `alias_label`, `braze_id`, `email` ou `phone`). Uma tabela de origem pode ter colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado na Braze.
    - `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
    - `BRAZE_ID` - O identificador de usuário da Braze. Ele é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da Ingestão de Dados na Nuvem. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário.
    - `EMAIL` - O endereço de e-mail do usuário. Se existirem vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade. Se você incluir tanto e-mail quanto telefone, o e-mail será usado como identificador principal.
    - `PHONE` - O número de telefone do usuário. Se existirem vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade.
- `PAYLOAD` - Uma string JSON dos campos que você deseja sincronizar com o usuário na Braze.


#### Etapa 1.5: Obter a string de conexão do warehouse {#step-15-get-warehouse-connection-string}
Para recuperar o endpoint SQL do seu warehouse, acesse o **espaço de trabalho** no Fabric, passe o mouse sobre o nome do warehouse na lista de itens e selecione **Copy SQL connection string**.

![A página "Console do Fabric" no Microsoft Azure, onde os usuários devem recuperar a string de conexão SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Etapa 1.6: Permitir IPs da Braze no firewall (opcional) {#step-16-allow-braze-ips-in-firewall-optional}

Dependendo da configuração da sua conta Microsoft Fabric, talvez seja necessário permitir os seguintes endereços IP no seu firewall para permitir o tráfego da Braze. Para saber mais sobre como ativar esse recurso, consulte a documentação relevante sobre o [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Etapa 2: Criar uma nova origem no dashboard da Braze {#step-2-create-a-new-source-in-the-braze-dashboard}


{% tabs %}
{% tab Snowflake %}

No dashboard da Braze, acesse **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes**, selecione **Adicionar fonte de dados** e, em seguida, selecione **Snowflake**.

#### Etapa 2.1: Adicionar informações de conexão do Snowflake {#step-21-add-snowflake-connection-information}

Escolha um nome para sua origem e insira suas credenciais e configuração do Snowflake, depois prossiga para a próxima etapa.

Antes de continuar, confirme o valor inserido em **Snowflake Account Locator**.

Para o campo **Snowflake Account Locator**, insira seu [identificador de conta](https://docs.snowflake.com/en/user-guide/admin-account-identifier) do Snowflake. Insira apenas o valor do identificador de conta, como `myorganization-myaccount`. Não inclua `https://`, `.snowflakecomputing.com` ou qualquer caminho.

Para encontrar o identificador de conta do Snowflake:

1. No Snowsight, selecione o menu da sua conta.
2. Selecione **View account details**.
3. Copie o valor de **Account identifier**.
4. Se você copiar de uma URL do Snowflake, use apenas o valor antes de `.snowflakecomputing.com`.

#### Etapa 2.2: Adicionar uma chave pública ao usuário da Braze {#step-22-add-a-public-key-to-the-braze-user}

Após inserir suas credenciais e configuração, clique em **Save credentials** e gere uma chave RSA, depois volte ao Snowflake para concluir a configuração. Adicione a chave pública exibida no dashboard ao usuário que você criou para que a Braze se conecte ao Snowflake.

Para saber mais sobre como fazer isso, consulte a [documentação do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Se você quiser alternar as chaves a qualquer momento, a Braze pode gerar um novo par de chaves e fornecer a nova chave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

No dashboard da Braze, acesse **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes**, selecione **Adicionar fonte de dados** e, em seguida, selecione **Amazon Redshift**.

#### Etapa 2.1: Adicionar informações de conexão do Redshift e tabela de origem {#step-21-add-redshift-connection-information-and-source-table}

Escolha um nome para sua origem e insira suas credenciais e configuração do Redshift. Se estiver usando um túnel de rede privada, alterne o controle deslizante e insira as informações do túnel. Em seguida, prossiga para a próxima etapa.

{% alert note %}
No dashboard da Braze, o campo **Database name** aceita apenas letras (A–Z, a–z), números (0–9) e sublinhados (_), embora o Amazon Redshift suporte caracteres adicionais em identificadores de banco de dados.
{% endalert %}

#### Etapa 2.2: Testar conexão e conectar à origem {#step-22-test-connection-and-connect-to-source}

Em seguida, selecione **Test connection**. Se for bem-sucedido, finalize as configurações restantes e clique em **Connect to Source**. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

#### Solução de problemas: identificador de snapshot inválido {#troubleshooting-invalid-snapshot-identifier}

Se a Braze retornar um erro `Invalid snapshot identifier` durante o **Test connection** ou a configuração da sincronização, o Redshift não consegue resolver a referência de snapshot usada quando o objeto de origem é consultado.

No Redshift, um snapshot é um backup pontual de um cluster. Cada snapshot tem um identificador exclusivo usado pelo Redshift para referenciar esse estado de backup. Para saber mais, consulte [Snapshots e backups do Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html).

Esse erro pode ocorrer quando os metadados mudam enquanto a Braze valida o objeto de origem, como durante operações de cópia, restauração ou replicação de snapshots. Para saber mais, consulte [copiar snapshots para outra região da AWS](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html) e [restaurar um cluster a partir de um snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-cluster-from-snapshot.html).

Para solucionar o problema:

1. Verifique as configurações de origem na Braze, incluindo endpoint do cluster, banco de dados, esquema e nome do objeto.
2. Execute a mesma consulta diretamente no Redshift para confirmar que a tabela ou view é legível e estável.
3. Tente novamente após a conclusão de atividades de snapshot, restauração, redimensionamento ou replicação.
4. Se o problema persistir, consulte uma view materializada em vez de uma tabela base que muda frequentemente.

Uma view materializada armazena resultados de consulta pré-computados que você pode atualizar em um cronograma, o que pode tornar as leituras mais estáveis para sincronizações CDI. Para saber mais, consulte [views materializadas no Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html).

Exemplo:

```sql
CREATE MATERIALIZED VIEW ingestion.users_attributes_mv AS
SELECT updated_at, external_id, alias_label, alias_name, braze_id, email, phone, payload
FROM ingestion.users_attributes_sync;

REFRESH MATERIALIZED VIEW ingestion.users_attributes_mv;
```

Depois de criar a view materializada, use o nome da view materializada como o objeto de origem na sua sincronização CDI da Braze em vez da tabela base.
{% endtab %}
{% tab BigQuery %}

No dashboard da Braze, acesse **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes**, selecione **Adicionar fonte de dados** e, em seguida, selecione **Google BigQuery**.

#### Etapa 2.1: Adicionar informações de conexão do BigQuery e tabela de origem {#step-21-add-bigquery-connection-information-and-source-table}

Escolha um nome para sua origem. Em seguida, faça upload da chave JSON e forneça um nome para a conta de serviço. Depois, insira os campos de configuração restantes.

#### Etapa 2.2: Testar conexão e conectar à origem

Em seguida, selecione **Test connection**. Se for bem-sucedido, finalize as configurações restantes e clique em **Connect to Source**. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{% endtab %}
{% tab Databricks %}

No dashboard da Braze, acesse **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes**, selecione **Adicionar fonte de dados** e, em seguida, selecione **Databricks**.

#### Etapa 2.1: Adicionar informações de conexão do Databricks e tabela de origem {#step-21-add-databricks-connection-information-and-source-table}

Escolha um nome para sua origem e insira suas credenciais e configuração do Databricks. Em seguida, prossiga para a próxima etapa.

#### Etapa 2.2: Testar conexão e conectar à origem

Em seguida, selecione **Test connection**. Se for bem-sucedido, finalize as configurações restantes e clique em **Connect to Source**. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{% alert note %}
Você deve testar com êxito uma origem antes que ela possa ser criada. Se você fechar a página de criação, sua origem não será salva.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

No dashboard da Braze, acesse **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes**, selecione **Adicionar fonte de dados** e, em seguida, selecione **Microsoft Fabric**.

#### Etapa 2.1: Configurar uma sincronização de Ingestão de Dados na Nuvem {#step-21-set-up-a-cloud-data-ingestion-sync}

Escolha um nome para sua origem e insira suas credenciais e configuração do Microsoft Fabric.
- **Credentials Name** é um rótulo para essas credenciais na Braze; você pode definir um valor útil aqui
- Consulte as etapas na seção 1 para obter detalhes sobre como recuperar o Tenant ID, o Principal ID, o Client Secret e a Connection String

#### Etapa 2.2: Testar conexão e conectar à origem

Em seguida, selecione **Test connection**. Se for bem-sucedido, finalize as configurações restantes e clique em **Connect to Source**. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{% alert note %}
Você deve testar com êxito uma origem antes que ela possa ser criada. Se você fechar a página de criação, sua origem não será salva.
{% endalert %}

{% endtab %}

{% endtabs %}

### Etapa 3: Criar uma nova sincronização no dashboard da Braze {#step-3-create-a-new-sync-in-the-braze-dashboard}
Acesse **Configurações de dados** > **Ingestão de dados na nuvem** > **Sincronizações** e selecione **Criar sincronização de dados**.

{% tabs %}
{% tab Snowflake %}

#### Etapa 3.1: Configurar detalhes da sincronização e testar conexão {#step-31-configure-sync-details-and-test-connection}
Escolha um nome para sua sincronização. Em seguida, selecione qualquer origem ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e clique em **Test Connection**.

Se for bem-sucedido, uma prévia dos dados será exibida. Selecione **Next: Notifications** para continuar. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{% alert note %}
Você deve testar com êxito uma sincronização antes de prosseguir para as próximas etapas. Se precisar sair da página de criação da sincronização, clique em **Salvar como rascunho** para manter seu trabalho em andamento.
{% endalert %}

#### Etapa 3.2: Adicionar preferências de notificação {#step-32-add-notification-preferences}
Insira e-mail(s) de contato para notificações de erros de sincronização. A Braze usa essas informações de contato para enviar notificações sobre erros de integração, como perda inesperada de acesso à tabela.

Os e-mails de contato recebem apenas notificações de erros globais ou no nível da sincronização, como tabelas ausentes, permissões e outros. Eles não recebem notificações sobre problemas no nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações.

Esses problemas podem incluir:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões
- (Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

#### Etapa 3.3: Agendamento {#step-33-scheduling}
Por fim, configure sua sincronização como não recorrente ou recorrente.

Sincronizações não recorrentes podem ser disparadas manualmente ou via API.

Sincronizações recorrentes podem ter uma frequência de cada 15 minutos a uma vez por mês. A Braze agenda a sincronização recorrente no fuso horário UTC.

{% endtab %}

{% tab Redshift %}

#### Etapa 3.1: Configurar detalhes da sincronização e testar conexão
Escolha um nome para sua sincronização. Em seguida, selecione qualquer origem ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e clique em **Test Connection**.

Se for bem-sucedido, uma prévia dos dados será exibida. Selecione **Next: Notifications** para continuar. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{% alert note %}
Você deve testar com êxito uma sincronização antes de prosseguir para as próximas etapas. Se precisar sair da página de criação da sincronização, clique em **Salvar como rascunho** para manter seu trabalho em andamento.
{% endalert %}

#### Etapa 3.2: Adicionar preferências de notificação
Insira e-mail(s) de contato para notificações de erros de sincronização. A Braze usa essas informações de contato para enviar notificações sobre erros de integração, como perda inesperada de acesso à tabela.

Os e-mails de contato recebem apenas notificações de erros globais ou no nível da sincronização, como tabelas ausentes, permissões e outros. Eles não recebem notificações sobre problemas no nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações.

Esses problemas podem incluir:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões

(Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

#### Etapa 3.3: Agendamento
Por fim, configure sua sincronização como não recorrente ou recorrente.

Sincronizações não recorrentes podem ser disparadas manualmente ou via API.

Sincronizações recorrentes podem ter uma frequência de cada 15 minutos a uma vez por mês. A Braze agenda a sincronização recorrente no fuso horário UTC.

{% endtab %}

{% tab BigQuery %}

#### Etapa 3.1: Configurar detalhes da sincronização e testar conexão
Escolha um nome para sua sincronização. Em seguida, selecione qualquer origem ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e clique em **Test Connection**.

Se for bem-sucedido, uma prévia dos dados será exibida. Selecione **Next: Notifications** para continuar. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{% alert note %}
Você deve testar com êxito uma sincronização antes de prosseguir para as próximas etapas. Se precisar sair da página de criação da sincronização, clique em **Salvar como rascunho** para manter seu trabalho em andamento.
{% endalert %}

#### Etapa 3.2: Adicionar preferências de notificação
Insira e-mail(s) de contato para notificações de erros de sincronização. A Braze usa essas informações de contato para enviar notificações sobre erros de integração, como perda inesperada de acesso à tabela.

Os e-mails de contato recebem apenas notificações de erros globais ou no nível da sincronização, como tabelas ausentes, permissões e outros. Eles não recebem notificações sobre problemas no nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações. Esses problemas podem incluir:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões

(Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

#### Etapa 3.3: Agendamento
Por fim, configure sua sincronização como não recorrente ou recorrente.

Sincronizações não recorrentes podem ser disparadas manualmente ou via API.

Sincronizações recorrentes podem ter uma frequência de cada 15 minutos a uma vez por mês. A Braze agenda a sincronização recorrente no fuso horário UTC.

{% endtab %}

{% tab Databricks %}

#### Etapa 3.1: Configurar detalhes da sincronização e testar conexão
Escolha um nome para sua sincronização. Em seguida, selecione qualquer origem ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e clique em **Test Connection**.

Se for bem-sucedido, uma prévia dos dados será exibida. Selecione **Next: Notifications** para continuar. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{% alert note %}
Você deve testar com êxito uma sincronização antes de prosseguir para as próximas etapas. Se precisar sair da página de criação da sincronização, clique em **Salvar como rascunho** para manter seu trabalho em andamento.
{% endalert %}

#### Etapa 3.2: Adicionar preferências de notificação
Insira e-mail(s) de contato para notificações de erros de sincronização. A Braze usa essas informações de contato para enviar notificações sobre erros de integração, como perda inesperada de acesso à tabela.

Os e-mails de contato recebem apenas notificações de erros globais ou no nível da sincronização, como tabelas ausentes, permissões e outros. Eles não recebem notificações sobre problemas no nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações.

Esses problemas podem incluir:
- Problemas de conectividade
- Falta de recursos
- Problemas de permissões

(Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

#### Etapa 3.3: Agendamento
Por fim, configure sua sincronização como não recorrente ou recorrente.

Sincronizações não recorrentes podem ser disparadas manualmente ou via API.

Sincronizações recorrentes podem ter uma frequência de cada 15 minutos a uma vez por mês. A Braze agenda a sincronização recorrente no fuso horário UTC.

{% endtab %}
{% tab Microsoft Fabric %}

#### Etapa 3.1: Configurar detalhes da sincronização e testar conexão

Escolha um nome para sua sincronização. Em seguida, selecione qualquer origem ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e clique em **Test Connection**.

Se for bem-sucedido, uma prévia dos dados será exibida. Selecione **Next: Notifications** para continuar. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{% alert note %}
Você deve testar com êxito uma sincronização antes de prosseguir para as próximas etapas. Se precisar sair da página de criação da sincronização, clique em **Salvar como rascunho** para manter seu trabalho em andamento.
{% endalert %}

#### Etapa 3.2: Adicionar preferências de notificação
Insira e-mail(s) de contato para notificações de erros de sincronização. A Braze usa essas informações de contato para enviar notificações sobre erros de integração, como perda inesperada de acesso à tabela.

Os e-mails de contato recebem apenas notificações de erros globais ou no nível da sincronização, como tabelas ausentes, permissões e outros. Eles não recebem notificações sobre problemas no nível de linha. Os erros globais indicam problemas críticos com a conexão que impedem a execução das sincronizações.

Esses problemas podem incluir:

- Problemas de conectividade
- Falta de recursos
- Problemas de permissões

(Somente para sincronizações de catálogos) A camada do catálogo está sem espaço

#### Etapa 3.3: Agendamento
Por fim, configure sua sincronização como não recorrente ou recorrente.

Sincronizações não recorrentes podem ser disparadas manualmente ou via API.

Sincronizações recorrentes podem ter uma frequência de cada 15 minutos a uma vez por mês. A Braze agenda a sincronização recorrente no fuso horário UTC.

{% endtab %}
{% endtabs %}

{% alert note %}
Você deve testar com êxito uma integração antes que ela possa passar do estado Rascunho para o estado Ativo. Se você fechar a página de criação, sua integração será salva e você poderá acessar novamente a página de detalhes para fazer alterações e testes.
{% endalert %}

## Configurar integrações ou usuários adicionais (opcional) {#set-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Snowflake.

Se você reutilizar o mesmo usuário e função em todas as integrações, não precisará adicionar a chave pública novamente.
{% endtab %}
{% tab Redshift %}
Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Snowflake ou do Redshift.

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard da Braze até que ele seja removido de todas as sincronizações ativas.
{% endtab %}
{% tab BigQuery %}

Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do BigQuery.

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard da Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% tab Databricks %}

Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Databricks.

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard da Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% tab Microsoft Fabric %}

Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para sincronizar uma tabela diferente. Ao criar sincronizações adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Fabric.

Se você reutilizar o mesmo usuário em várias integrações, não será possível excluir o usuário no dashboard da Braze até que ele seja removido de todas as sincronizações ativas.

{% endtab %}
{% endtabs %}

## Executar a sincronização {#running-the-sync}

{% tabs %}
{% tab Snowflake %}
Quando ativada, sua sincronização será executada de acordo com o cronograma configurado durante a instalação. Se você quiser executar a sincronização fora do cronograma normal de testes ou buscar os dados mais recentes, selecione **Sync Now**. Essa execução não afetará as sincronizações futuras programadas regularmente.

{% endtab %}
{% tab Redshift %}
Quando ativada, sua sincronização será executada de acordo com o cronograma configurado durante a instalação. Se você quiser executar a sincronização fora do cronograma normal de testes ou buscar os dados mais recentes, selecione **Sync Now**. Essa execução não afetará as sincronizações futuras programadas regularmente.

{% endtab %}
{% tab BigQuery %}

Quando ativada, sua sincronização será executada de acordo com o cronograma configurado durante a instalação. Se você quiser executar a sincronização fora do cronograma normal de testes ou buscar os dados mais recentes, selecione **Sync Now**. Essa execução não afetará as sincronizações futuras programadas regularmente.

{% endtab %}
{% tab Databricks %}

Quando ativada, sua sincronização será executada de acordo com o cronograma configurado durante a instalação. Se você quiser executar a sincronização fora do cronograma normal de testes ou buscar os dados mais recentes, selecione **Sync Now**. Essa execução não afetará as sincronizações futuras programadas regularmente.

{% endtab %}
{% tab Microsoft Fabric %}

Quando ativada, sua sincronização será executada de acordo com o cronograma configurado durante a instalação. Se você quiser executar a sincronização fora do cronograma normal de testes ou buscar os dados mais recentes, selecione **Sync Now**. Essa execução não afetará as sincronizações futuras programadas regularmente.

{% endtab %}

{% endtabs %}