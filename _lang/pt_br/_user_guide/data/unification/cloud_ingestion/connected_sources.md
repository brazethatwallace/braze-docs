---
nav_title: Fontes conectadas
article_title: Fontes conectadas
description: "Esta página aborda como usar a Ingestão de Dados na Nuvem da Braze para sincronizar dados relevantes com sua integração Snowflake, Redshift, BigQuery e Databricks."
page_order: 2
page_type: reference

---

# Fontes conectadas {#connected-sources}

> As fontes conectadas são uma alternativa de cópia zero à sincronização direta de dados com o recurso de Ingestão de Dados na Nuvem (CDI) da Braze. Uma fonte conectada consulta diretamente seu data warehouse para criar novos segmentos sem copiar nenhum dos dados subjacentes para a Braze.

Depois de adicionar uma fonte conectada ao seu espaço de trabalho da Braze, você pode criar um Segment or segmento or segmento CDI dentro das extensões de Segment or segmento or segmento. As extensões de Segment or segmento or segmento CDI permitem que você escreva SQL que consulta diretamente seu data warehouse (usando os dados disponibilizados por meio da sua fonte conectada CDI) e cria e mantém um grupo de usuários que podem ser direcionados dentro da Braze.

Para saber mais sobre como criar um Segment or segmento or segmento com essa fonte, consulte [Extensões de Segment or segmento or segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).

{% alert warning %}
Como as fontes conectadas são executadas diretamente no seu data warehouse, você incorrerá em todos os custos associados à execução dessas consultas no seu data warehouse. As fontes conectadas não registram pontos de dados, e as extensões de Segment or segmento or segmento CDI não consomem créditos de Segment or segmento or segmento SQL.
{% endalert %}

## Integrando fontes conectadas {#integrating-connected-sources}

### Etapa 1: Conecte seus recursos {#step-1-connect-your-resources}

As fontes conectadas da Ingestão de Dados na Nuvem exigem algumas configurações na Braze e na sua instância. Siga estas etapas para configurar a integração&#8722;algumas etapas serão feitas no seu data warehouse e outras no dashboard da Braze.

{% tabs %}
{% tab Snowflake %}
**No seu data warehouse**
1. Crie uma função (role) e conceda permissões para consultar e criar tabelas em um esquema.
2. Configure seu warehouse e conceda acesso a essa função.
3. Crie um usuário para essa função.
4. Dependendo da sua configuração, pode ser necessário permitir os IPs da Braze na política de rede do Snowflake.

**No dashboard da Braze**

{: start="5"}
5. Crie uma nova fonte conectada no dashboard da Braze.
6. Configure os detalhes de sincronização da fonte conectada.
7. Obtenha a chave pública fornecida no dashboard da Braze.

**No seu data warehouse**

{: start="8"}
8. Adicione a chave pública do dashboard da Braze ao [usuário do Snowflake para autenticação](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Quando terminar, você poderá usar a fonte conectada para criar uma ou mais extensões de Segment or segmento or segmento CDI.
{% endtab %}

{% tab Redshift %}
1. Configure os dados de origem e os recursos necessários no seu ambiente Redshift.
2. Crie uma nova fonte conectada no dashboard da Braze.
3. Teste a integração.
4. Use a fonte conectada para criar uma ou mais extensões de Segment or segmento or segmento CDI.
{% endtab %}

{% tab BigQuery %}
1. Configure os dados de origem e os recursos necessários no seu ambiente BigQuery.
2. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do BigQuery que contêm os dados que você deseja sincronizar.
3. Crie uma nova fonte conectada no dashboard da Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais extensões de Segment or segmento or segmento CDI.
{% endtab %}

{% tab Databricks %}
1. Configure os dados de origem e os recursos necessários no seu ambiente Databricks.
2. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do Databricks que contêm os dados que você deseja sincronizar.
3. Crie uma nova fonte conectada no dashboard da Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais extensões de Segment or segmento or segmento CDI.

{% alert important %}
Pode haver de dois a cinco minutos de tempo de aquecimento quando a Braze se conecta a instâncias SQL Classic e Pro, o que causará atrasos durante a configuração e teste da conexão, bem como durante a criação e atualização de extensões de Segment or segmento or segmento CDI. Usar uma instância SQL serverless minimizará o tempo de aquecimento e melhorará a taxa de transferência de consultas, mas pode resultar em custos de integração ligeiramente mais altos.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Crie uma entidade de serviço (service principal) e permita o acesso ao espaço de trabalho do Fabric que será usado para sua integração.
2. No seu espaço de trabalho do Fabric, configure os dados de origem e conceda permissões à sua entidade de serviço.
3. Crie uma nova fonte conectada no dashboard da Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais extensões de Segment or segmento or segmento CDI.
{% endtab %}

{% endtabs %}

### Etapa 2: Configure seu data warehouse {#step-2-set-up-your-data-warehouse}

Configure os dados de origem e os recursos necessários no ambiente do seu data warehouse. A fonte conectada pode referenciar uma ou mais tabelas, então certifique-se de que o usuário da Braze tenha permissão para acessar todas as tabelas desejadas na fonte conectada.

{% tabs %}
{% tab Snowflake %}
#### Etapa 2.1: Crie uma função e conceda permissões {#step-21-create-a-role-and-grant-permissions}

Crie uma função para a sua fonte conectada usar. Essa função será usada para gerar a lista de tabelas disponíveis nas suas extensões de Segment or segmento or segmento CDI e para consultar tabelas de origem para criar novos segmentos. Após a criação da fonte conectada, a Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema de origem.

Você pode optar por conceder acesso a todas as tabelas em um esquema ou conceder privilégios apenas a tabelas específicas. As tabelas às quais a função da Braze tiver acesso estarão disponíveis para consulta na extensão de Segment or segmento or segmento CDI.

A permissão `create table` é necessária para que a Braze possa criar uma tabela com os resultados da consulta da extensão de Segment or segmento or segmento CDI antes de atualizar o Segment or segmento or segmento na Braze. A Braze criará uma tabela temporária por Segment or segmento or segmento, e a tabela persistirá apenas enquanto a Braze estiver atualizando o Segment or segmento or segmento.

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### Etapa 2.2: Configure o warehouse e conceda acesso à função da Braze {#step-22-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
O warehouse precisa ter a flag **auto-resume** ativada. Caso contrário, você precisará conceder à Braze privilégios adicionais de `OPERATE` no warehouse para que a Braze possa ativá-lo quando for hora de executar a consulta.
{% endalert %}

#### Etapa 2.3: Configure o usuário {#step-23-set-up-the-user}
```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Você compartilhará as informações de conexão com a Braze e receberá uma chave pública para adicionar ao usuário em uma etapa posterior.

{% alert note %}
Ao conectar diferentes espaços de trabalho à mesma conta do Snowflake, você deve criar um usuário exclusivo para cada espaço de trabalho da Braze onde estiver criando uma integração. Dentro de um espaço de trabalho, você pode reutilizar o mesmo usuário em diferentes integrações, mas a criação da integração falhará se um usuário na mesma conta do Snowflake for duplicado entre espaços de trabalho.
{% endalert %}

#### Etapa 2.4: Permita os IPs da Braze na política de rede do Snowflake (opcional) {#step-24-allow-braze-ips-in-your-snowflake-network-policy-optional}

Dependendo da configuração da sua conta do Snowflake, pode ser necessário permitir os seguintes endereços IP na política de rede do Snowflake. Para saber mais sobre como fazer isso, consulte a documentação relevante do Snowflake sobre [modificação de uma política de rede](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Etapa 2.1: Crie um usuário e conceda permissões {#step-21-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Crie um usuário para a sua fonte conectada usar. Esse usuário será usado para gerar a lista de tabelas disponíveis nas suas extensões de Segment or segmento or segmento CDI e para consultar tabelas de origem para criar novos segmentos. Após a criação da fonte conectada, a Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema de origem. Se estiver criando múltiplas integrações CDI, você pode conceder permissões a um esquema ou gerenciar permissões usando um grupo.

Você pode optar por conceder acesso a todas as tabelas em um esquema ou conceder privilégios apenas a tabelas específicas. As tabelas às quais a função da Braze tiver acesso estarão disponíveis para consulta na extensão de Segment or segmento or segmento CDI. Certifique-se de conceder acesso a quaisquer novas tabelas ao usuário quando elas forem criadas, ou defina permissões padrão para o usuário.

A permissão `create table` é necessária para que a Braze possa criar uma tabela com os resultados da consulta da extensão de Segment or segmento or segmento CDI antes de atualizar o Segment or segmento or segmento na Braze. A Braze criará uma tabela temporária por Segment or segmento or segmento, que persistirá apenas enquanto a Braze atualizar o Segment or segmento or segmento.


#### Etapa 2.2: Permita o acesso aos IPs da Braze {#step-22-allow-access-to-braze-ips}

Se você tiver um firewall ou outras políticas de rede, deve conceder à Braze acesso de rede à sua instância do Redshift. Permita o acesso dos seguintes IPs correspondentes à região do seu dashboard da Braze.

Também pode ser necessário alterar seus grupos de segurança para permitir o acesso da Braze aos seus dados no Redshift. Certifique-se de permitir explicitamente o tráfego de entrada nos IPs da seção a seguir e na porta usada para consultar seu cluster Redshift (o padrão é 5439). Você deve permitir explicitamente a conectividade TCP do Redshift nessa porta, mesmo que as regras de entrada estejam configuradas como "permitir tudo". Além disso, é importante que o endpoint do cluster Redshift seja acessível publicamente para que a Braze possa se conectar ao seu cluster.

Se você não quiser que seu cluster Redshift seja acessível publicamente, pode configurar uma VPC e uma instância EC2 para usar um túnel SSH para acessar os dados do Redshift. Para saber mais, consulte [AWS: Como acessar um cluster privado do Amazon Redshift a partir da minha máquina local?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Etapa 2.1: Crie uma conta de serviço e conceda permissões {#step-21-create-a-service-account-and-grant-permissions}

Crie uma conta de serviço no GCP para a Braze usar para se conectar e ler dados da(s) sua(s) tabela(s). A conta de serviço deve ter as seguintes permissões:

- **BigQuery Connection User:** Permite que a Braze faça conexões.
- **BigQuery User:** Fornece à Braze acesso para executar consultas, ler metadados de conjuntos de dados e listar tabelas.
- **BigQuery Data Viewer:** Fornece à Braze acesso para visualizar conjuntos de dados e seus conteúdos.
- **BigQuery Job User:** Fornece à Braze acesso para executar jobs.
- **bigquery.tables.create** Fornece à Braze acesso para criar tabelas temporárias durante a atualização de segmentos.

Crie uma conta de serviço para a sua fonte conectada usar. Esse usuário será usado para gerar a lista de tabelas disponíveis nas suas extensões de Segment or segmento or segmento CDI e para consultar tabelas de origem para criar novos segmentos. Após a criação da fonte conectada, a Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema de origem.

Você pode optar por conceder acesso a todas as tabelas em um conjunto de dados ou conceder privilégios apenas a tabelas específicas. As tabelas às quais a função da Braze tiver acesso estarão disponíveis para consulta na extensão de Segment or segmento or segmento CDI.

A permissão `create table` é necessária para que a Braze possa criar uma tabela com os resultados da consulta da extensão de Segment or segmento or segmento CDI antes de atualizar o Segment or segmento or segmento na Braze. A Braze criará uma tabela temporária por Segment or segmento or segmento, e a tabela persistirá apenas enquanto a Braze estiver atualizando o Segment or segmento or segmento.

Após criar a conta de serviço e conceder as permissões, gere uma chave JSON. Para saber mais, consulte [Google Cloud: Criar e excluir chaves de conta de serviço](https://cloud.google.com/iam/docs/keys-create-delete). Você fará o upload dessa chave no dashboard da Braze posteriormente.

#### Etapa 2.2: Permita o acesso aos IPs da Braze

Se você tiver políticas de rede em vigor, deve conceder à Braze acesso de rede à sua instância do BigQuery. Permita o acesso dos seguintes IPs correspondentes à região do seu dashboard da Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Etapa 2.1: Crie um token de acesso {#step-21-create-an-access-token}

Para que a Braze acesse o Databricks, é necessário criar um token de acesso pessoal.

1. No seu espaço de trabalho do Databricks, selecione seu nome de usuário do Databricks na barra superior e, em seguida, selecione **User Settings** no menu suspenso.
2. Certifique-se de que a conta de serviço tenha privilégios de `CREATE TABLE` no esquema usado para a fonte conectada.
3. Na guia **Access tokens**, selecione **Generate new token**.
4. Insira um comentário que ajude a identificar esse token, como "Braze CDI", e altere o tempo de vida do token para sem limite, deixando o campo Lifetime (days) vazio (em branco).
5. Selecione **Generate**.
6. Copie o token exibido e selecione **Done**.

Esse token será usado para gerar a lista de tabelas disponíveis nas suas extensões de Segment or segmento or segmento CDI e para consultar tabelas de origem para criar novos segmentos. Após a criação da fonte conectada, a Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema de origem.

Você pode optar por conceder acesso a todas as tabelas em um esquema ou conceder privilégios apenas a tabelas específicas. As tabelas às quais a função da Braze tiver acesso estarão disponíveis para consulta na extensão de Segment or segmento or segmento CDI.

A permissão `create table` é necessária para que a Braze possa criar uma tabela com os resultados da consulta da extensão de Segment or segmento or segmento CDI antes de atualizar o Segment or segmento or segmento na Braze. A Braze criará uma tabela temporária por Segment or segmento or segmento, que persistirá apenas enquanto a Braze atualizar o Segment or segmento or segmento.

Guarde o token em um local seguro até que precise inseri-lo no dashboard da Braze durante a etapa de criação de credenciais.

#### Etapa 2.2: Permita o acesso aos IPs da Braze

Se você tiver políticas de rede em vigor, deve conceder à Braze acesso de rede à sua instância do Databricks. Permita o acesso dos seguintes IPs correspondentes à região do seu dashboard da Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Etapa 2.1: Conceda acesso aos recursos do Fabric {#step-21-grant-access-to-fabric-resources}
A Braze se conectará ao seu warehouse do Fabric usando uma entidade de serviço com autenticação Entra ID. Você criará uma nova entidade de serviço para a Braze usar e concederá acesso aos recursos do Fabric conforme necessário. A Braze precisará dos seguintes detalhes para se conectar:

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
O Azure não permite vencimento ilimitado em segredos de entidade de serviço. Lembre-se de atualizar as credenciais antes que elas expirem para manter o fluxo de dados para a Braze.
{% endalert %}

#### Etapa 2.2: Conceda acesso aos recursos do Fabric {#step-22-grant-access-to-fabric-resources}
Você fornecerá acesso para a Braze se conectar à sua instância do Fabric. No portal de administração do Fabric, navegue até **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* Em **Developer settings**, ative "Service principals can use Fabric APIs" para que a Braze possa se conectar usando o Microsoft Entra ID.
* Em **OneLake settings**, ative "Users can access data stored in OneLake with apps external to Fabric" para que a entidade de serviço possa acessar dados de um app externo.

#### Etapa 2.3: Obtenha a string de conexão do warehouse {#step-23-get-warehouse-connection-string}

Você precisará do endpoint SQL do seu warehouse para que a Braze possa se conectar. Para obter o endpoint SQL, acesse o **workspace** no Fabric e, na lista de itens, passe o mouse sobre o nome do warehouse e selecione **Copy SQL connection string**.
Mantenha esse valor disponível para a configuração de credenciais na Etapa 3.

#### Etapa 2.4: Permita os IPs da Braze no firewall (opcional) {#step-24-allow-braze-ips-in-firewall-optional}

Dependendo da configuração da sua conta do Microsoft Fabric, pode ser necessário permitir os seguintes endereços IP no seu firewall para permitir o tráfego da Braze. Para saber mais sobre como ativar isso, consulte a documentação relevante sobre [Acesso Condicional do Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Etapa 3: Crie uma fonte conectada no dashboard da Braze {#step-3-create-a-connected-source-in-the-braze-dashboard}

{% tabs %}
{% tab Snowflake %}
#### Etapa 3.1: Adicione as informações de conexão do Snowflake e a tabela de origem {#step-31-add-snowflake-connection-information-and-source-table}

Crie uma fonte conectada no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, selecione **Add data source** e, em seguida, selecione **Snowflake**.

Em **Setup source**, insira o seguinte:
- **Credentials:** **Account Locator**, **Username** e **Role**
- **Configuration:** **Warehouse**, **Database** e **Schema**

Se estiver criando novas credenciais do Snowflake, selecione **Save credentials and generate RSA key** antes de testar a conexão.

#### Etapa 3.2: Configure os detalhes de sincronização {#step-32-configure-sync-details}

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova extensão de Segment or segmento or segmento CDI.

Configure um tempo máximo de execução para essa fonte. A Braze interromperá automaticamente quaisquer consultas que excedam o tempo máximo de execução. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos na sua conta do Snowflake. Essa configuração se aplica a consultas executadas por meio dessa fonte, incluindo sincronizações e extensões de Segment or segmento or segmento CDI que a utilizam.

{% alert note %}
Se as consultas estiverem atingindo o tempo limite consistentemente e você tiver definido um tempo máximo de execução de 60 minutos, considere otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário da Braze.
{% endalert %}

#### Etapa 3.3: Anote a chave pública {#step-33-note-the-public-key}

Na etapa **Test connection**, anote a chave pública RSA. Você precisará dela para concluir a integração no Snowflake.

{% endtab %}
{% tab Redshift %}
#### Etapa 3.1: Adicione as informações de conexão do Redshift e a tabela de origem {#step-31-add-redshift-connection-information-and-source-table}

Crie uma fonte conectada no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, selecione **Add data source** e, em seguida, selecione **Amazon Redshift**.

Em **Setup source**, insira o seguinte:
- **Credentials:** **Redshift Host URL**, **Username**, **Password** e **Port**
- **Configuration:** **Database** e **Schema**

Se necessário, ative **Connect with SSH Tunnel** e insira **Tunnel Host**, **Tunnel Port** e **Tunnel Username**.

#### Etapa 3.2: Configure os detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova extensão de Segment or segmento or segmento CDI.

Configure um tempo máximo de execução para essa fonte. A Braze interromperá automaticamente quaisquer consultas que excedam o tempo máximo de execução. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos na sua conta do Redshift.
Essa configuração se aplica a consultas executadas por meio dessa fonte, incluindo sincronizações e extensões de Segment or segmento or segmento CDI que a utilizam.

{% alert note %}
Se as consultas estiverem atingindo o tempo limite consistentemente e você tiver definido um tempo máximo de execução de 60 minutos, considere otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário da Braze.
{% endalert %}

#### Etapa 3.3: Anote a chave pública (opcional) {#step-33-note-the-public-key-optional}

Se suas credenciais tiverem **Connect with SSH Tunnel** selecionado, anote a chave pública RSA na etapa **Test connection**. Você precisará dela para concluir a integração no Redshift.

{% endtab %}
{% tab BigQuery %}
#### Etapa 3.1: Adicione as informações de conexão do BigQuery e a tabela de origem {#step-31-add-bigquery-connection-information-and-source-table}

Crie uma fonte conectada no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, selecione **Add data source** e, em seguida, selecione **Google BigQuery**.

Em **Setup source**, insira o seguinte:
- **Credentials:** **Credential name** e faça o upload da sua **JSON key**
- **Configuration:** **Project** e **Dataset**

#### Etapa 3.2: Configure os detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova extensão de Segment or segmento or segmento CDI.

Configure um tempo máximo de execução para essa fonte. A Braze interromperá automaticamente quaisquer consultas que excedam o tempo máximo de execução. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos na sua conta do BigQuery. Essa configuração se aplica a consultas executadas por meio dessa fonte, incluindo sincronizações e extensões de Segment or segmento or segmento CDI que a utilizam.

{% alert note %}
Se as consultas estiverem atingindo o tempo limite consistentemente e você tiver definido um tempo máximo de execução de 60 minutos, considere otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário da Braze.
{% endalert %}

#### Etapa 3.3: Teste a conexão {#step-33-test-the-connection}

Selecione **Test Connection** para verificar se a lista de tabelas visíveis para o usuário é a esperada e, em seguida, selecione **Done**. Sua fonte conectada foi criada e está pronta para uso em extensões de Segment or segmento or segmento CDI.

{% endtab %}
{% tab Databricks %}
#### Etapa 3.1: Adicione as informações de conexão do Databricks e a tabela de origem {#step-31-add-databricks-connection-information-and-source-table}

Crie uma fonte conectada no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, selecione **Add data source** e, em seguida, selecione **Databricks**.

Em **Setup source**, insira o seguinte:
- **Credentials:** **Credential Name**, **Hostname**, **HTTP jornada** e **Access Token**
- **Configuration:** **Catalog** e **Schema**

#### Etapa 3.2: Configure os detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova extensão de Segment or segmento or segmento CDI.

Configure um tempo máximo de execução para essa fonte. A Braze interromperá automaticamente quaisquer consultas que excedam o tempo máximo de execução. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos na sua conta do Databricks. Essa configuração se aplica a consultas executadas por meio dessa fonte, incluindo sincronizações e extensões de Segment or segmento or segmento CDI que a utilizam.

{% alert note %}
Se as consultas estiverem atingindo o tempo limite consistentemente e você tiver definido um tempo máximo de execução de 60 minutos, considere otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário da Braze.
{% endalert %}

#### Etapa 3.3: Teste a conexão

Selecione **Test Connection** para verificar se a lista de tabelas visíveis para o usuário é a esperada e, em seguida, selecione **Done**. Sua fonte conectada foi criada e está pronta para uso em extensões de Segment or segmento or segmento CDI.

{% endtab %}
{% tab Microsoft Fabric %}
#### Etapa 3.1: Adicione as informações de conexão do Microsoft Fabric e a tabela de origem {#step-31-add-microsoft-fabric-connection-information-and-source-table}

Crie uma fonte conectada no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, selecione **Add data source** e, em seguida, selecione **Microsoft Fabric**.

Em **Setup source**, insira o seguinte:
- **Credentials:** **Credentials Name**, **Tenant ID**, **Principal ID**, **Client Secret** e **Connection String**
- **Configuration:** **Database** e **Schema**

Se **Connect with SSH Tunnel** estiver disponível no seu espaço de trabalho e for necessário para sua configuração, insira também **Tunnel Host**, **Tunnel Port** e **Tunnel Username**.

#### Etapa 3.2: Configure os detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova extensão de Segment or segmento or segmento CDI.

Configure um tempo máximo de execução para essa fonte. A Braze interromperá automaticamente quaisquer consultas que excedam o tempo máximo de execução. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos na sua conta do Microsoft Fabric. Essa configuração se aplica a consultas executadas por meio dessa fonte, incluindo sincronizações e extensões de Segment or segmento or segmento CDI que a utilizam.

{% alert note %}
Se as consultas estiverem atingindo o tempo limite consistentemente e você tiver definido um tempo máximo de execução de 60 minutos, considere otimizar o tempo de execução da consulta ou escalar a capacidade do Fabric.
{% endalert %}

#### Etapa 3.3: Teste a conexão

Selecione **Test Connection** para verificar se a lista de tabelas visíveis para o usuário é a esperada e, em seguida, selecione **Done**. Sua fonte conectada foi criada e está pronta para uso em extensões de Segment or segmento or segmento CDI.

{% endtab %}
{% endtabs %}

### Etapa 4: Finalize a configuração do data warehouse {#step-4-finalize-the-data-warehouse-configuration}

{% tabs %}
{% tab Snowflake %}
Adicione a chave pública que você anotou na última etapa ao seu usuário no Snowflake. Isso permitirá que a Braze se conecte ao Snowflake. Para detalhes sobre como fazer isso, consulte a [documentação do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).

Se você quiser fazer a rotação das chaves em algum momento, pode criar uma nova chave pública acessando **Data Access Management** em **Cloud Data Ingestion** e selecionando **Generate New Key** para a respectiva conta.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Após adicionar a chave ao usuário no Snowflake, selecione **Test Connection** na Braze e, em seguida, selecione **Done**. Sua fonte conectada foi criada e está pronta para uso em extensões de Segment or segmento or segmento CDI.
{% endtab %}

{% tab Redshift %}
Se estiver conectando com um túnel SSH, adicione a chave pública que você anotou na última etapa ao usuário do túnel SSH.

Após adicionar a chave ao usuário, selecione **Test Connection** na Braze e, em seguida, selecione **Done**. Sua fonte conectada foi criada e está pronta para uso em extensões de Segment or segmento or segmento CDI.

{% endtab %}
{% tab BigQuery %}
Isso não se aplica ao BigQuery.

{% endtab %}
{% tab Databricks %}
Isso não se aplica ao Databricks.

{% endtab %}
{% tab Microsoft Fabric %}
Isso não se aplica ao Microsoft Fabric.

{% endtab %}
{% endtabs %}

{% alert note %}
Você deve testar uma fonte com sucesso antes que ela possa passar do estado "rascunho" para o estado "ativo". Se precisar sair da página de criação, sua integração será salva e você poderá revisitar a página de detalhes para fazer alterações e testar.
{% endalert %}

## Configurando integrações ou usuários adicionais (opcional) {#setting-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para se conectar a um schema diferente. Ao construir relacionamentos or criar conexões adicionais, você pode reutilizar credenciais existentes se estiver se conectando à mesma conta do Snowflake.

Se você reutilizar o mesmo usuário e a mesma função entre integrações, não será necessário adicionar a chave pública novamente.
{% endtab %}

{% tab Redshift %}
Você pode configurar várias fontes de dados com a Braze, mas cada fonte deve ser configurada para se conectar a um schema diferente. Ao criar fontes adicionais, você pode reutilizar credenciais existentes se estiver se conectando à mesma conta do Redshift.
{% endtab %}

{% tab BigQuery %}
Você pode configurar várias fontes de dados com a Braze, mas cada fonte deve ser configurada para se conectar a um dataset diferente. Ao criar fontes adicionais, você pode reutilizar credenciais existentes se estiver se conectando à mesma conta do BigQuery.
{% endtab %}

{% tab Databricks %}
Você pode configurar várias fontes de dados com a Braze, mas cada fonte deve ser configurada para se conectar a um schema diferente. Ao criar fontes adicionais, você pode reutilizar credenciais existentes se estiver se conectando à mesma conta do Databricks.
{% endtab %}

{% tab Microsoft Fabric %}
Você pode configurar várias fontes de dados com a Braze, mas cada fonte deve ser configurada para se conectar a um schema diferente. Ao criar fontes adicionais, você pode reutilizar credenciais existentes se estiver se conectando à mesma conta do Azure.
{% endtab %}
{% endtabs %}

## Usando a fonte conectada {#using-the-connected-source}

Após a criação da fonte, você pode usá-la para criar uma ou mais extensões de Segment or segmento or segmento CDI. Para saber mais sobre como criar um Segment or segmento or segmento com essa fonte, consulte a [documentação de extensões de Segment or segmento or segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).

{% alert note %}
Se as consultas estiverem atingindo o tempo limite de forma consistente e você tiver definido um tempo máximo de execução de 60 minutos, considere otimizar o tempo de execução da consulta ou dedicar mais recursos computacionais (como um data warehouse maior) ao usuário da Braze.
{% endalert %}