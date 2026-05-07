---
nav_title: Fontes conectadas
article_title: Fontes conectadas
description: "Esta página aborda como usar a Ingestão de Dados na Nuvem da Braze para sincronizar dados relevantes com sua integração Snowflake, Redshift, BigQuery e Databricks."
page_order: 2
page_type: reference

---

# Fontes conectadas {#connected-sources}

> As fontes conectadas são uma alternativa de cópia zero à sincronização direta de dados com o recurso de Ingestão de Dados na Nuvem (CDI) da Braze. Uma fonte conectada consulta diretamente seu data warehouse para criar novos **Segments** sem copiar nenhum dos dados subjacentes para a Braze.

Depois de adicionar uma fonte conectada ao seu espaço de trabalho da Braze, você pode criar um **Segment** CDI dentro das **Segment Extensions**. As CDI **Segment Extensions** permitem que você escreva SQL que consulta diretamente seu data warehouse (usando os dados disponibilizados por meio da sua Fonte Conectada CDI) e cria e mantém um grupo de usuários que podem ser direcionados dentro da Braze.

Para saber mais sobre como criar um **Segment** com essa fonte, consulte [CDI **Segment Extensions**]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/).

{% alert warning %}
Como as fontes conectadas são executadas diretamente no seu data warehouse, você incorrerá em todos os custos associados à execução dessas consultas no seu data warehouse. As fontes conectadas não registram pontos de dados, e as CDI **Segment Extensions** não consomem SQL **Segment** credits.
{% endalert %}

## Integração de fontes conectadas {#integrating-connected-sources}

### Etapa 1: Conecte seus recursos {#step-1-connect-your-resources}

As fontes conectadas de Ingestão de Dados na Nuvem exigem algumas configurações na Braze e na sua instância. Siga estas etapas para configurar a integração&#8722;algumas etapas serão realizadas no seu data warehouse e outras serão realizadas no dashboard da Braze.

{% tabs %}
{% tab Snowflake %}
**No seu data warehouse**
1. Crie uma função e conceda permissões para consultar e criar tabelas em um esquema.
2. Configure seu warehouse e conceda acesso a essa função.
3. Crie um usuário para essa função.
4. Dependendo da sua configuração, talvez seja necessário permitir IPs da Braze na sua política de rede do Snowflake.

**No dashboard da Braze**

{: start="5"}
5. Crie uma nova fonte conectada no dashboard da Braze.
6. Configure os detalhes de sincronização para a fonte conectada.
7. Recupere a chave pública fornecida no dashboard da Braze.

**No seu data warehouse**

{: start="8"}
8. Anexe a chave pública do dashboard da Braze ao [usuário do Snowflake para autenticação](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Quando terminar, você pode usar a fonte conectada para criar uma ou mais Extensões de segmento CDI.
{% endtab %}

{% tab Redshift %}
1. Configure os dados de origem e os recursos necessários no seu ambiente Redshift.
2. Crie uma nova fonte conectada no dashboard da Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais Extensões de segmento CDI.
{% endtab %}

{% tab BigQuery %}
1. Configure os dados de origem e os recursos necessários no seu ambiente BigQuery.
2. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do BigQuery que contêm os dados que você deseja sincronizar.
3. Crie uma nova fonte conectada no dashboard da Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais Extensões de segmento CDI.
{% endtab %}

{% tab Databricks %}
1. Configure os dados de origem e os recursos necessários no seu ambiente Databricks.
2. Crie uma conta de serviço e permita o acesso ao(s) projeto(s) e conjunto(s) de dados do Databricks que contêm os dados que você deseja sincronizar.
3. Crie uma nova fonte conectada no dashboard da Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais Extensões de segmento CDI.

{% alert important %}
Pode haver de dois a cinco minutos de tempo de aquecimento quando a Braze se conecta a instâncias SQL Classic e Pro, o que levará a atrasos durante a configuração e teste da conexão, bem como durante a criação e atualização da Extensão de segmento CDI. O uso de uma instância SQL serverless minimizará o tempo de aquecimento e melhorará a taxa de transferência das consultas, mas poderá resultar em custos de integração ligeiramente mais altos.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Crie uma entidade de serviço e permita o acesso ao espaço de trabalho do Fabric que será usado para sua integração.
2. No seu espaço de trabalho do Fabric, configure os dados de origem e conceda permissões à sua entidade de serviço.
3. Crie uma nova fonte conectada no dashboard da Braze.
4. Teste a integração.
5. Use a fonte conectada para criar uma ou mais Extensões de segmento CDI.
{% endtab %}

{% endtabs %}

### Etapa 2: Configure seu data warehouse {#step-2-set-up-your-data-warehouse}

Configure os dados de origem e os recursos necessários no seu ambiente de data warehouse. A fonte conectada pode fazer referência a uma ou mais tabelas, portanto, certifique-se de que o usuário da Braze tenha permissão para acessar todas as tabelas desejadas na fonte conectada.

{% tabs %}
{% tab Snowflake %}
#### Etapa 2.1: Criar uma função e conceder permissões {#step-21-create-a-role-and-grant-permissions}

Crie uma função para sua fonte conectada usar. Essa função será usada para gerar a lista de tabelas disponíveis nas suas Extensões de segmento CDI e para consultar tabelas de origem para criar novos **Segments**. Depois que a fonte conectada for criada, a Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema de origem.

Você pode optar por conceder acesso a todas as tabelas em um esquema ou conceder privilégios somente a tabelas específicas. Quaisquer tabelas às quais a função da Braze tenha acesso estarão disponíveis para consulta na Extensão de segmento CDI.

A permissão `create table` é necessária para que a Braze possa criar uma tabela com os resultados da consulta da sua Extensão de segmento CDI antes de atualizar o segmento na Braze. A Braze criará uma tabela temporária por segmento, e a tabela só persistirá enquanto a Braze estiver atualizando o segmento.

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

#### Etapa 2.2: Configurar o warehouse e conceder acesso à função da Braze {#step-22-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
O warehouse precisa ter o sinalizador de **retomada automática** ativado. Se não estiver, você precisará conceder à Braze privilégios adicionais de `OPERATE` no warehouse para que a Braze o ative quando for o momento de executar a consulta.
{% endalert %}

#### Etapa 2.3: Configurar o usuário {#step-23-set-up-the-user}
```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Você compartilhará informações de conexão com a Braze e receberá uma chave pública para anexar ao usuário em uma etapa posterior.

{% alert note %}
Ao conectar diferentes espaços de trabalho à mesma conta do Snowflake, é necessário criar um usuário exclusivo para cada espaço de trabalho da Braze em que estiver criando uma integração. Em um espaço de trabalho, é possível reutilizar o mesmo usuário em todas as integrações, mas a criação da integração falhará se um usuário na mesma conta do Snowflake for duplicado em espaços de trabalho diferentes.
{% endalert %}

#### Etapa 2.4: Permitir IPs da Braze na sua política de rede do Snowflake (opcional) {#step-24-allow-braze-ips-in-your-snowflake-network-policy-optional}

Dependendo da configuração da sua conta do Snowflake, talvez seja necessário permitir os seguintes endereços IP na sua política de rede do Snowflake. Para saber mais sobre como fazer isso, consulte a documentação relevante do Snowflake sobre [modificação de uma política de rede](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Etapa 2.1: Criar usuário e conceder permissões {#step-21-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Crie um usuário para sua fonte conectada usar. Esse usuário será usado para gerar a lista de tabelas disponíveis nas suas Extensões de segmento CDI e para consultar tabelas de origem para criar novos **Segments**. Depois que a fonte conectada for criada, a Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema de origem. Se estiver criando várias integrações CDI, talvez você queira conceder permissões a um esquema ou gerenciar as permissões usando um grupo.

Você pode optar por conceder acesso a todas as tabelas em um esquema ou conceder privilégios somente a tabelas específicas. Quaisquer tabelas às quais a função da Braze tenha acesso estarão disponíveis para consulta na Extensão de segmento CDI. Certifique-se de conceder acesso a todas as novas tabelas ao usuário quando elas forem criadas, ou defina permissões padrão para o usuário.

A permissão `create table` é necessária para que a Braze possa criar uma tabela com os resultados da consulta da sua Extensão de segmento CDI antes de atualizar o segmento na Braze. A Braze criará uma tabela temporária por segmento, que só persistirá enquanto a Braze estiver atualizando o segmento.


#### Etapa 2.2: Permitir acesso aos IPs da Braze {#step-22-allow-access-to-braze-ips}

Se você tiver um firewall ou outras políticas de rede, deverá conceder à Braze acesso de rede à sua instância do Redshift. Permita o acesso dos IPs abaixo correspondentes à região do seu dashboard da Braze.

Também pode ser necessário alterar seus grupos de segurança para permitir que a Braze acesse seus dados no Redshift. Certifique-se de permitir explicitamente o tráfego de entrada nos IPs abaixo e na porta usada para consultar seu cluster Redshift (o padrão é 5439). Você deve permitir explicitamente a conectividade TCP do Redshift nessa porta, mesmo que as regras de entrada estejam definidas como "permitir tudo". Além disso, é importante que o endpoint do cluster Redshift seja acessível publicamente para que a Braze se conecte ao seu cluster.

Se não quiser que o cluster do Redshift seja acessível publicamente, você pode configurar uma instância VPC e EC2 para usar um túnel SSH para acessar os dados do Redshift. Para saber mais, consulte [AWS: Como posso acessar um cluster privado do Amazon Redshift a partir da minha máquina local?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Etapa 2.1: Criar uma conta de serviço e conceder permissões {#step-21-create-a-service-account-and-grant-permissions}

Crie uma conta de serviço no GCP para a Braze usar para se conectar e ler dados da(s) sua(s) tabela(s). A conta de serviço deve ter as permissões abaixo:

- **BigQuery Connection User:** Permite que a Braze faça conexões.
- **BigQuery User:** Fornece à Braze acesso para executar consultas, ler metadados de conjuntos de dados e listar tabelas.
- **BigQuery Data Viewer:** Fornece à Braze acesso para visualizar conjuntos de dados e seus conteúdos.
- **BigQuery Job User:** Fornece à Braze acesso para executar jobs.
- **bigquery.tables.create** Fornece à Braze acesso para criar tabelas temporárias durante a atualização do segmento.

Crie uma conta de serviço para ser usada pela sua fonte conectada. Esse usuário será usado para gerar a lista de tabelas disponíveis nas suas Extensões de segmento CDI e para consultar tabelas de origem para criar novos **Segments**. Depois que a fonte conectada for criada, a Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema de origem.

Você pode optar por conceder acesso a todas as tabelas em um conjunto de dados ou conceder privilégios somente a tabelas específicas. Quaisquer tabelas às quais a função da Braze tenha acesso estarão disponíveis para consulta na Extensão de segmento CDI.

A permissão `create table` é necessária para que a Braze possa criar uma tabela com os resultados da consulta da sua Extensão de segmento CDI antes de atualizar o segmento na Braze. A Braze criará uma tabela temporária por segmento, e a tabela só persistirá enquanto a Braze estiver atualizando o segmento.

Depois de criar a conta de serviço e conceder permissões, gere uma chave JSON. Para saber mais, consulte [Google Cloud: Criar e excluir chaves de conta de serviço](https://cloud.google.com/iam/docs/keys-create-delete). Você fará upload dela no dashboard da Braze mais tarde.

#### Etapa 2.2: Permitir acesso aos IPs da Braze

Se você tiver políticas de rede em vigor, deverá conceder à Braze acesso de rede à sua instância do BigQuery. Permita o acesso dos IPs abaixo correspondentes à região do seu dashboard da Braze.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Etapa 2.1: Criar um token de acesso {#step-21-create-an-access-token}

Para que a Braze acesse o Databricks, é necessário criar um token de acesso pessoal.

1. No seu espaço de trabalho do Databricks, selecione seu nome de usuário do Databricks na barra superior e, em seguida, selecione **User Settings** no menu suspenso.
2. Certifique-se de que a conta de serviço tenha privilégios `CREATE TABLE` no esquema usado para a fonte conectada.
3. Na guia **Access tokens**, selecione **Generate new token**.
4. Digite um comentário que ajude a identificar esse token, como "Braze CDI", e altere o tempo de vida do token para sem tempo de vida, deixando a caixa Lifetime (days) vazia (em branco).
5. Selecione **Generate**.
6. Copie o token exibido e, em seguida, selecione **Done**.

Esse token será usado para gerar a lista de tabelas disponíveis nas suas Extensões de segmento CDI e para consultar tabelas de origem para criar novos **Segments**. Depois que a fonte conectada for criada, a Braze descobrirá os nomes e a descrição de todas as tabelas disponíveis para o usuário no esquema de origem.

Você pode optar por conceder acesso a todas as tabelas em um esquema ou conceder privilégios somente a tabelas específicas. Quaisquer tabelas às quais a função da Braze tenha acesso estarão disponíveis para consulta na Extensão de segmento CDI.

A permissão `create table` é necessária para que a Braze possa criar uma tabela com os resultados da consulta da sua Extensão de segmento CDI antes de atualizar o segmento na Braze. A Braze criará uma tabela temporária por segmento, que só persistirá enquanto a Braze estiver atualizando o segmento.

Mantenha o token em um local seguro até que seja necessário inseri-lo no dashboard da Braze durante a etapa de criação de credenciais.

#### Etapa 2.2: Permitir acesso aos IPs da Braze

Se você tiver políticas de rede em vigor, deverá conceder à Braze acesso de rede à sua instância do Databricks. Permita o acesso dos IPs abaixo correspondentes à região do seu dashboard da Braze.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Etapa 2.1: Conceder acesso aos recursos do Fabric {#step-21-grant-access-to-fabric-resources}
A Braze se conectará ao seu warehouse do Fabric usando uma entidade de serviço com autenticação Entra ID. Você criará uma nova entidade de serviço para a Braze usar e concederá acesso aos recursos do Fabric conforme necessário. A Braze precisará dos seguintes detalhes para se conectar:

* ID do locatário (também chamado de diretório) da sua conta do Azure
* ID da entidade principal (também chamada de ID do aplicativo) para a entidade de serviço
* Segredo do cliente para autenticação da Braze

1. No portal Azure, navegue até o centro de administração Microsoft Entra e, em seguida, **App Registrations**.
2. Selecione **+ New registration** em **Identity > Applications > App registrations**
3. Digite um nome e selecione `Accounts in this organizational directory only` como o tipo de conta compatível. Em seguida, selecione **Register**.
4. Selecione o aplicativo (entidade de serviço) que você acabou de criar e navegue até **Certificates & secrets > + New client secret**.
5. Digite uma descrição para o segredo e defina um período de vencimento para o segredo. Em seguida, selecione **Add**.
6. Anote o segredo do cliente criado para ser usado na configuração da Braze.

{% alert note %}
O Azure não permite vencimento ilimitado em segredos de entidade de serviço. Lembre-se de atualizar as credenciais antes que elas expirem para manter o fluxo de dados para a Braze.
{% endalert %}

#### Etapa 2.2: Conceder acesso aos recursos do Fabric {#step-22-grant-access-to-fabric-resources}
Você fornecerá acesso para que a Braze se conecte à sua instância do Fabric. No seu portal de administração do Fabric, navegue até **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* Em **Developer settings**, ative "Service principals can use Fabric APIs" para que a Braze possa se conectar usando o Microsoft Entra ID.
* Em **OneLake settings**, ative "Users can access data stored in OneLake with apps external to Fabric" para que a entidade de serviço possa acessar os dados de um aplicativo externo.

#### Etapa 2.3: Obter a string de conexão do warehouse {#step-23-get-warehouse-connection-string}

Você precisará do endpoint SQL do seu warehouse para que a Braze possa se conectar. Para recuperar o endpoint SQL, acesse o **espaço de trabalho** no Fabric e, na lista de itens, passe o mouse sobre o nome do warehouse e selecione **Copy SQL connection string**.

![A página "Fabric Console" no Microsoft Azure, onde os usuários devem recuperar a string de conexão SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})

#### Etapa 2.4: Permitir IPs da Braze no firewall (opcional) {#step-24-allow-braze-ips-in-firewall-optional}

Dependendo da configuração da sua conta Microsoft Fabric, talvez seja necessário permitir os seguintes endereços IP no seu firewall para permitir o tráfego da Braze. Para saber mais sobre como ativar esse recurso, consulte a documentação relevante sobre [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Etapa 3: Criar uma fonte conectada no dashboard da Braze {#step-3-create-a-connected-source-in-the-braze-dashboard}

{% tabs %}
{% tab Snowflake %}
#### Etapa 3.1: Adicionar informações de conexão do Snowflake e tabela de origem {#step-31-add-snowflake-connection-information-and-source-table}

Crie uma fonte conectada no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Connected Sources** e selecione **Create new data sync** > **Snowflake Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Insira as informações do seu data warehouse do Snowflake e do esquema de origem e prossiga para a próxima etapa.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### Etapa 3.2: Configurar detalhes de sincronização {#step-32-configure-sync-details}

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova Extensão de segmento CDI.

Configure um tempo máximo de execução para essa fonte. A Braze abortará automaticamente as consultas que excederem o tempo máximo de execução quando estiver criando ou atualizando um segmento. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos na sua conta do Snowflake.

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário da Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### Etapa 3.3: Anote a chave pública {#step-33-note-the-public-key}

Na etapa **Test connection**, anote a chave pública RSA. Você precisará dela para concluir a integração no Snowflake.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### Etapa 3.1: Adicionar informações de conexão do Redshift e tabela de origem {#step-31-add-redshift-connection-information-and-source-table}

Crie uma fonte conectada no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Connected Sources** e selecione **Create data connection** > **Amazon Redshift Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Insira as informações do seu data warehouse Redshift e esquema de origem e prossiga para a próxima etapa.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### Etapa 3.2: Configurar detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova Extensão de segmento CDI.

Configure um tempo máximo de execução para essa fonte. A Braze abortará automaticamente as consultas que excederem o tempo máximo de execução quando estiver criando ou atualizando um segmento. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos na sua conta do Redshift.

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário da Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### Etapa 3.3: Anote a chave pública (opcional) {#step-33-note-the-public-key-optional}

Se suas credenciais tiverem a opção **Connect with SSH Tunnel** selecionada, anote a chave pública RSA na etapa **Test connection**. Você precisará dela para concluir a integração no Redshift.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### Etapa 3.1: Adicionar informações de conexão do BigQuery e tabela de origem {#step-31-add-bigquery-connection-information-and-source-table}

Crie uma fonte conectada no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Connected Sources** e selecione **Create new data sync** > **Google BigQuery Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Insira as informações do seu projeto e conjunto de dados do BigQuery e prossiga para a próxima etapa.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### Etapa 3.2: Configurar detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova Extensão de segmento CDI.

Configure um tempo máximo de execução para essa fonte. A Braze abortará automaticamente as consultas que excederem o tempo máximo de execução quando estiver criando ou atualizando um segmento. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos na sua conta do BigQuery.

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário da Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### Etapa 3.3: Teste a conexão {#step-33-test-the-connection}

Selecione **Test Connection** para verificar se a lista de tabelas visíveis para o usuário é a esperada e, em seguida, selecione **Done**. Sua fonte conectada agora está criada e pronta para uso nas Extensões de segmento CDI.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### Etapa 3.1: Adicionar informações de conexão do Databricks e tabela de origem {#step-31-add-databricks-connection-information-and-source-table}

Crie uma fonte conectada no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Connected Sources** e selecione **Create new data sync** > **Databricks Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Insira as informações das suas credenciais do Databricks e, opcionalmente, o catálogo e o esquema de origem, e prossiga para a próxima etapa.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### Etapa 3.2: Configurar detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova Extensão de segmento CDI.

Configure um tempo máximo de execução para essa fonte. A Braze abortará automaticamente as consultas que excederem o tempo máximo de execução quando estiver criando ou atualizando um segmento. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos na sua conta do Databricks.

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dedicar um warehouse maior ao usuário da Braze.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### Etapa 3.3: Teste a conexão

Selecione **Test Connection** para verificar se a lista de tabelas visíveis para o usuário é a esperada e, em seguida, selecione **Done**. Sua fonte conectada agora está criada e pronta para uso nas Extensões de segmento CDI.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Microsoft Fabric %}
#### Etapa 3.1: Adicionar informações de conexão do Microsoft Fabric e tabela de origem {#step-31-add-microsoft-fabric-connection-information-and-source-table}

Crie uma fonte conectada no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Connected Sources** e selecione **Create new data sync** > **Microsoft Fabric Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Insira as informações das suas credenciais do Microsoft Fabric, bem como o warehouse e o esquema de origem, e prossiga para a próxima etapa.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_1.png %})

#### Etapa 3.2: Configurar detalhes de sincronização

Escolha um nome para a fonte conectada. Esse nome será usado na lista de fontes disponíveis quando você criar uma nova Extensão de segmento CDI.

Configure um tempo máximo de execução para essa fonte. A Braze abortará automaticamente as consultas que excederem o tempo máximo de execução quando estiver criando ou atualizando um segmento. O tempo máximo de execução permitido é de 60 minutos; um tempo de execução menor reduzirá os custos incorridos na sua conta do Microsoft Fabric.

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou aumentar a capacidade do Fabric.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_2.png %})

#### Etapa 3.3: Teste a conexão

Selecione **Test Connection** para verificar se a lista de tabelas visíveis para o usuário é a esperada e, em seguida, selecione **Done**. Sua fonte conectada agora está criada e pronta para uso nas Extensões de segmento CDI.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Finalizar a configuração do data warehouse {#step-4-finalize-the-data-warehouse-configuration}

{% tabs %}
{% tab Snowflake %}
Adicione a chave pública que você anotou na última etapa ao seu usuário no Snowflake. Isso permitirá que a Braze se conecte ao Snowflake. Para detalhes sobre como fazer isso, consulte a [documentação do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).

Se quiser fazer a rotação das chaves a qualquer momento, você pode criar uma nova chave pública acessando **Data Access Management** em **Cloud Data Ingestion** e selecionando **Generate New Key** para a respectiva conta.

![Gerenciamento de acesso a dados para credenciais de acesso a dados do Snowflake, com um botão para gerar nova chave.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Depois de adicionar a chave ao usuário no Snowflake, selecione **Test Connection** na Braze e, em seguida, selecione **Done**. Sua fonte conectada agora está criada e pronta para uso nas Extensões de segmento CDI.
{% endtab %}

{% tab Redshift %}
Se estiver se conectando com um túnel SSH, adicione a chave pública que você anotou na última etapa ao usuário do túnel SSH.

Depois de adicionar a chave ao usuário, selecione **Test Connection** na Braze e, em seguida, selecione **Done**. Sua fonte conectada agora está criada e pronta para uso nas Extensões de segmento CDI.

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
Você deve testar com êxito uma fonte antes que ela possa passar do estado "rascunho" para o estado "ativo". Se precisar sair da página de criação, sua integração será salva e você poderá acessar novamente a página de detalhes para fazer alterações e testes.
{% endalert %}

## Configuração de integrações ou usuários adicionais (opcional) {#setting-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Você pode configurar várias integrações com a Braze, mas cada integração deve ser configurada para conectar um esquema diferente. Ao criar conexões adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Snowflake.

Se você reutilizar o mesmo usuário e função em todas as integrações, não precisará adicionar a chave pública novamente.
{% endtab %}

{% tab Redshift %}
Você pode configurar várias fontes com a Braze, mas cada fonte deve ser configurada para conectar um esquema diferente. Ao criar fontes adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Redshift.
{% endtab %}

{% tab BigQuery %}
Você pode configurar várias fontes com a Braze, mas cada fonte deve ser configurada para conectar um conjunto de dados diferente. Ao criar fontes adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do BigQuery.
{% endtab %}

{% tab Databricks %}
Você pode configurar várias fontes com a Braze, mas cada fonte deve ser configurada para conectar um esquema diferente. Ao criar fontes adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Databricks.
{% endtab %}

{% tab Microsoft Fabric %}
Você pode configurar várias fontes com a Braze, mas cada fonte deve ser configurada para conectar um esquema diferente. Ao criar fontes adicionais, você pode reutilizar as credenciais existentes se estiver se conectando à mesma conta do Azure.
{% endtab %}
{% endtabs %}

## Usando a fonte conectada {#using-the-connected-source}

Após a fonte ser criada, você pode usá-la para criar uma ou mais Extensões de segmento CDI. Para saber mais sobre como criar um segmento com essa fonte, consulte a [documentação das Extensões de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/).

{% alert note %}
Se as consultas estiverem constantemente atingindo o tempo limite e você tiver definido um tempo de execução máximo de 60 minutos, considere tentar otimizar o tempo de execução da consulta ou dedicar mais recursos de computação (como um warehouse maior) ao usuário da Braze.
{% endalert %}