---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Este artigo descreve a parceria entre a Braze e o Snowflake, abrangendo tanto o Compartilhamento de Dados (da Braze para o Snowflake) quanto a Ingestão de Dados na Nuvem."
page_type: partner
search_tag: Partner
---

# Snowflake

> O [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) é um data warehouse de nuvem SQL criado para fins específicos e disponibilizado como software como serviço (SaaS). O Snowflake fornece um data warehouse mais rápido, mais fácil de usar e muito mais flexível do que as ofertas tradicionais. Com a arquitetura exclusiva e patenteada do Snowflake, é fácil reunir todos os seus dados, executar análises rápidas e obter insights orientados por dados para todos os seus usuários.

A Braze oferece duas integrações com o Snowflake. Juntas, elas fornecem um pipeline de dados bidirecional completo entre seus ambientes da Braze e do Snowflake.

## Escolhendo uma integração {#choosing-an-integration}

### Compartilhamento de dados (Braze para Snowflake) {#data-sharing-braze-to-snowflake}

O [Compartilhamento Seguro de Dados]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing) do Snowflake oferece acesso seguro e em tempo real aos dados de engajamento e de Campaigns da Braze diretamente na sua instância do Snowflake. Nenhum dado é copiado ou transferido entre contas — todo o compartilhamento é realizado por meio da camada de serviços e do armazenamento de metadados exclusivos do Snowflake.

**Use o Compartilhamento de Dados quando quiser:**
- Consultar dados de eventos e de Campaigns da Braze usando SQL no Snowflake
- Criar relatórios complexos e realizar modelagem de atribuição
- Unir dados da Braze a outros dados no seu data warehouse Snowflake
- Fazer benchmarks dos seus dados de engajamento entre canais, setores e plataformas de dispositivos

Para instruções de configuração, consulte [Compartilhamento de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing).

### Ingestão de dados na nuvem (Snowflake para Braze) {#cloud-data-ingestion-snowflake-to-braze}

A [Ingestão de dados na nuvem (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) permite sincronizar dados da sua instância Snowflake diretamente na Braze. Isso permite manter atributos de usuário, eventos e compras na Braze atualizados com o seu data warehouse de referência.

**Use a Ingestão de dados na nuvem quando quiser:**
- Sincronizar atributos de usuário do Snowflake para perfis de usuário na Braze
- Enviar dados de eventos ou de compras do Snowflake para a Braze
- Manter a Braze sincronizada com as transformações de dados que acontecem no seu data warehouse
- Evitar a criação e manutenção de pipelines ETL personalizados do Snowflake para a Braze

Para saber mais sobre o compartilhamento de dados do Snowflake, consulte [Introdução ao Compartilhamento Seguro de Dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Pré-requisitos {#prerequisites}

Antes de usar esse recurso, você precisará completar o seguinte:

| Requisito | Descrição |
| ----------- | ----------- |
| Acesso à Braze | Para acessar esse recurso na Braze, você precisará entrar em contato com seu gerente de conta ou gerente de sucesso do cliente da Braze. |
| Permissões do espaço de trabalho da Braze | [Ver integrações do Currents]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para visualizar o Compartilhamento de Dados. [Editar integrações do Currents]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para criar, atualizar ou excluir um compartilhamento de dados. |
| Conta Snowflake | Uma conta Snowflake com permissões de `admin`. Para clientes não HIPAA, o Snowflake Standard ou Enterprise Edition é suportado. Para compartilhamento de dados em conformidade com HIPAA, o Business Critical Edition é necessário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Configurando o compartilhamento seguro de dados {#setting-up-secure-data-sharing}

Para o Snowflake, o compartilhamento de dados ocorre entre um [provedor de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) e um [consumidor de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Nesse contexto, sua conta da Braze é o provedor de dados, pois ela cria e envia o compartilhamento de dados — enquanto sua conta do Snowflake é o consumidor de dados, pois usa o compartilhamento para criar um banco de dados. Para mais detalhes, consulte [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Etapa 1: Envie o compartilhamento de dados a partir da Braze {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Etapa 2: Crie o banco de dados no Snowflake {#step-2-create-the-database-in-snowflake}

1. Após alguns minutos, você deve receber o compartilhamento de dados de entrada na sua conta do Snowflake.
2. Usando o compartilhamento de dados de entrada, crie um banco de dados para visualizar e consultar as tabelas. Por exemplo:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Conceda privilégios para consultar o novo banco de dados.

{% alert warning %}
Se você excluir e recriar um compartilhamento no dashboard da Braze, será necessário descartar o banco de dados criado anteriormente e recriá-lo usando `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` para consultar o compartilhamento de entrada.
Se você tiver vários espaços de trabalho compartilhando dados para a mesma conta do Snowflake, consulte as [Perguntas frequentes sobre o compartilhamento de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) para orientações sobre como gerenciar configurações com vários espaços de trabalho.
{% endalert %}

## Uso e visualização {#usage-and-visualization}

Depois que o compartilhamento de dados for provisionado, será necessário criar um banco de dados a partir do compartilhamento de dados recebido, fazendo com que todas as tabelas compartilhadas apareçam na sua instância do Snowflake e possam ser consultadas como qualquer outro dado armazenado na sua instância. No entanto, lembre-se de que os dados compartilhados são somente leitura e podem apenas ser consultados, sem possibilidade de modificação ou exclusão.

Assim como o Currents, você pode usar o Compartilhamento Seguro de Dados do Snowflake para:

{% multi_lang_include partners/data_sharing_use_cases.md %}

Para uma lista completa das tabelas e colunas disponíveis, consulte a [Referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). O Compartilhamento de Dados do Snowflake inclui todas as tabelas dessa referência, além de tabelas exclusivas do Snowflake para snapshots, changelogs de Campaigns e Canvas, eventos do console de agentes e eventos de repetição de mensagens.

Você também pode [baixar os esquemas brutos de tabelas](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) como um arquivo de texto.

### Esquema de ID do usuário {#user-id-schema}

Observe as seguintes diferenças entre as convenções de nomenclatura da Braze e do Snowflake para IDs de usuário.

| Esquema da Braze | Esquema do Snowflake | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | O identificador exclusivo atribuído automaticamente pela Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | O identificador exclusivo do perfil de um usuário definido pelo cliente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de ID do usuário" }

## Informações importantes e limitações {#important-information-and-limitations}

### Alterações com quebra versus sem quebra {#breaking-versus-non-breaking-changes}

#### Alterações sem quebra {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Como novas colunas são consideradas alterações sem quebra, a Braze recomenda fortemente listar explicitamente as colunas de interesse em cada consulta em vez de usar consultas `SELECT *`. Alternativamente, você pode criar views que nomeiem explicitamente as colunas e, em seguida, consultar essas views em vez das tabelas diretamente.
{% endalert %}

#### Alterações com quebra {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Regiões do Snowflake {#snowflake-regions}

Atualmente, a Braze hospeda todos os dados em nível de usuário nas regiões do Snowflake AWS US East-1, EU-Central (Frankfurt), AP-Northeast-1 (Tóquio), AP-Southeast-2 (Sydney) e AP-Southeast-3 (Jacarta). Para usuários fora dessas regiões, a Braze pode fornecer compartilhamento de dados para clientes em comum que hospedam sua infraestrutura Snowflake em qualquer região AWS, Azure ou GCP.

### Retenção de dados {#data-retention}

#### Política de retenção {#retention-policy}

Quaisquer dados com mais de dois anos serão arquivados e movidos para armazenamento de longo prazo. Como parte do processo de arquivamento, todos os eventos são anonimizados e quaisquer campos sensíveis de informações de identificação pessoal (IPI) são removidos (isso inclui campos opcionalmente IPI como `properties`). Os dados arquivados ainda contêm o campo `user_id`, o que permite análises por usuário em todos os dados de eventos.

Você poderá consultar os dois anos mais recentes de dados para cada evento na view `USERS_*_SHARED` correspondente. Além disso, cada evento terá uma view `USERS_*_SHARED_ALL` que pode ser consultada para retornar tanto dados anonimizados quanto não anonimizados.

#### Dados históricos {#historical-data}

O arquivo de dados históricos de eventos no Snowflake remonta a abril de 2019. Nos primeiros meses em que a Braze armazenou dados no Snowflake, foram feitas alterações no produto que podem ter resultado em alguns desses dados parecendo ligeiramente diferentes ou tendo alguns valores nulos (já que não estávamos passando dados para todos os campos disponíveis naquele momento). O ideal é considerar que quaisquer resultados que incluam dados anteriores a agosto de 2019 podem parecer ligeiramente diferentes do esperado.

### Conformidade com o Regulamento Geral de Proteção de Dados (GDPR) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Consultando dados compartilhados: `TIME` e performance de consulta {#querying-shared-data-time-and-query-performance}

Os dados de eventos nas views de compartilhamento de dados (por exemplo, `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) são **clusterizados no campo `TIME`**. Ao filtrar por **quando o evento ocorreu**, use **`TIME`** como o filtro preferido. Consultas que restringem linhas usando **`TIME`** são geralmente **mais performáticas** do que consultas que filtram por **`SF_CREATED_AT`**, porque a clusterização se alinha com o horário do evento.

| Campo | Significado |
| ----- | ----------- |
| `TIME` | Timestamp Unix do momento em que o evento ocorreu. Prefira este ao filtrar por horário de ocorrência. |
| `SF_CREATED_AT` | Timestamp de quando a linha foi carregada no Snowflake (horário de ingestão). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consultando dados compartilhados: TIME e performance de consulta" }

### Velocidade, performance e custo de consultas {#speed-performance-cost-of-queries}

A velocidade, a performance e o custo de qualquer consulta executada sobre os dados são determinados pelo tamanho do warehouse que você usa para consultar os dados. Em alguns casos, dependendo do volume de dados que você está acessando para análise, pode ser necessário usar um warehouse de tamanho maior para que a consulta seja bem-sucedida. O Snowflake oferece excelentes recursos sobre como determinar o melhor tamanho a ser usado, incluindo [Visão geral dos warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) e [Considerações sobre warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Para um conjunto de consultas de exemplo como referência ao configurar o Snowflake, confira nossos exemplos de [consultas de exemplo]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) e [configuração do pipeline de eventos ETL]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup).

Para instruções de configuração, consulte [Ingestão de dados na nuvem: integrações com data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).