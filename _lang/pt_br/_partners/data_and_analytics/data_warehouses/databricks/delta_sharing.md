---
nav_title: "Delta Sharing"
article_title: Databricks Delta Sharing
page_order: 0
description: "Este artigo de referência aborda o Databricks Delta Sharing com a Braze (beta fechado), que permite acessar dados de engajamento e de Campaign da Braze na sua conta do Databricks."
page_type: partner
search_tag: Partner
permalink: /delta_sharing/
hidden: true
---

# Databricks Delta Sharing

> O Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html) permite compartilhar com segurança dados de engajamento e de Campaign da Braze em tempo real no seu ambiente Databricks. Este artigo descreve como o compartilhamento funciona a partir da Braze como provedora de dados para a sua conta do Databricks como destinatária, e como consultar tabelas compartilhadas.

{% alert important %}
O Databricks Delta Sharing com a Braze está em **beta fechado**. A disponibilidade, as regiões suportadas e o comportamento do produto podem mudar. Entre em contato com o seu CSM da Braze para participar ou confirmar se esse recurso está ativado para o seu espaço de trabalho.
{% endalert %}

O Databricks Delta Sharing faz parte da Distribuição de Dados da Braze. Para uma visão geral completa das opções de Distribuição de Dados, consulte [Distribuição de dados]({{site.baseurl}}/user_guide/data/distribution).

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Acesso ao beta fechado | Entre em contato com seu gerente de sucesso do cliente da Braze para participar ou confirmar se esse recurso está ativado para o seu espaço de trabalho. |
| Permissões do espaço de trabalho da Braze | [Visualizar integrações do Currents]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para visualizar o Compartilhamento de Dados. [Editar integrações do Currents]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para criar, atualizar ou excluir um compartilhamento Delta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Configurar o Delta Sharing {#set-up-delta-sharing}

Para o Databricks, o compartilhamento de dados acontece entre um provedor de dados e um destinatário de dados. Sua conta da Braze é o **provedor de dados** porque cria e envia o compartilhamento, e sua conta do Databricks é o **destinatário de dados** porque consome o compartilhamento para criar um catálogo que você pode consultar. Para saber mais, consulte a documentação do Databricks sobre [leitura de dados compartilhados usando o Databricks-to-Databricks Delta Sharing (para destinatários)](https://docs.databricks.com/en/delta-sharing/read-data-databricks.html).

### Etapa 1: Configurar o compartilhamento a partir da Braze {#step-1-configure-sharing-from-braze}

1. Na Braze, acesse **Partner Integrations** > **Data Sharing** > **Databricks Delta Sharing**.
2. Insira seu identificador de compartilhamento do Databricks.
3. Quando terminar, selecione **Create Datashare**. A Braze envia o compartilhamento para sua conta do Databricks.

### Etapa 2: Criar um catálogo no Databricks {#step-2-create-a-catalog-in-databricks}

1. Após alguns minutos, você deverá receber o compartilhamento de entrada na sua conta do Databricks.
2. Usando o compartilhamento de entrada, crie um catálogo para visualizar e consultar as tabelas. Por exemplo:
    {% raw %}
    ```sql
    CREATE CATALOG [IF NOT EXISTS] <catalog-name> USING SHARE braze.<share-name>;
    ```
    {% endraw %}
3. Conceda privilégios para que os usuários e grupos certos possam consultar o novo catálogo.

{% alert warning %}
Os dados compartilhados são somente leitura no seu espaço de trabalho do Databricks. Você pode consultá-los como outros dados, mas não pode modificar ou excluir linhas nas tabelas compartilhadas por meio do compartilhamento.
{% endalert %}

## Uso e visualização {#usage-and-visualization}

Após o compartilhamento de dados ser provisionado, crie um catálogo a partir do compartilhamento recebido para que as tabelas compartilhadas apareçam no seu espaço de trabalho do Databricks e possam ser consultadas como qualquer outro dado armazenado lá. Os dados compartilhados permanecem somente leitura.

De forma semelhante ao Currents, você pode usar o Databricks Delta Sharing para:

{% multi_lang_include partners/data_sharing_use_cases.md %}

Para uma lista completa de tabelas e colunas disponíveis no Databricks, [baixe os esquemas de tabelas brutas do Databricks](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt) como um arquivo de texto. Esse arquivo reflete o esquema do Databricks Delta Sharing (por exemplo, `DB_CREATED_AT` para tempo de ingestão). Ele não é intercambiável com os [esquemas de tabelas brutas do Snowflake](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) ou com a [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables), que descrevem a nomenclatura e os campos do Snowflake.

{% alert note %}
Durante o beta fechado, nem todas as tabelas listadas no arquivo de esquema do Databricks podem estar disponíveis no seu compartilhamento. Os nomes e tipos de colunas também podem diferir do Snowflake Data Sharing (por exemplo, `DB_CREATED_AT` em vez de `SF_CREATED_AT`). Entre em contato com seu gerente de sucesso do cliente da Braze se você precisar da lista de tabelas atual para o seu espaço de trabalho.
{% endalert %}

### Esquema de ID do usuário {#user-id-schema}

Observe as seguintes diferenças entre as convenções de nomenclatura da Braze e do Databricks para IDs de usuário.

| Esquema Braze | Esquema Databricks | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `USER_ID` | O identificador exclusivo que a Braze atribui automaticamente. |
| `external_id` | `EXTERNAL_USER_ID` | O identificador exclusivo do perfil de um usuário que você define na Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de ID do usuário" }

## Informações importantes e limitações {#important-information-and-limitations}

### Disponibilidade do beta fechado {#closed-beta-availability}

Durante o beta fechado, seu compartilhamento pode não incluir todas as tabelas no arquivo de [esquemas de tabelas brutas do Databricks](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt). Os dados compartilhados também podem diferir do Snowflake Data Sharing em nomes e tipos de colunas. Por exemplo, os compartilhamentos do Databricks usam `DB_CREATED_AT` para o horário de ingestão, enquanto os compartilhamentos do Snowflake usam `SF_CREATED_AT`.

### Alterações com e sem quebra de compatibilidade {#breaking-versus-non-breaking-changes}

#### Alterações sem quebra de compatibilidade {#non-breaking-changes}

Alterações sem quebra de compatibilidade podem acontecer a qualquer momento e geralmente fornecem funcionalidades adicionais. Exemplos de alterações sem quebra de compatibilidade:

- Adicionar uma nova tabela ou view
- Adicionar uma coluna a uma tabela ou view existente

{% alert important %}
Como novas colunas são consideradas alterações sem quebra de compatibilidade, a Braze recomenda fortemente listar explicitamente as colunas de interesse em cada consulta em vez de usar consultas `SELECT *`. Como alternativa, crie views que nomeiem explicitamente as colunas e consulte essas views em vez de consultar as tabelas compartilhadas diretamente.
{% endalert %}

#### Alterações com quebra de compatibilidade {#breaking-changes}

Quando possível, alterações com quebra de compatibilidade são precedidas por um comunicado e um período de migração. Exemplos de alterações com quebra de compatibilidade incluem:

- Remover uma tabela ou view
- Remover uma coluna de uma tabela ou view existente
- Alterar o tipo ou a nulabilidade de uma coluna existente

### Regiões do Databricks {#databricks-regions}

Durante o beta fechado, os provedores de nuvem e regiões compatíveis podem variar por espaço de trabalho e implantação. Entre em contato com seu gerente de sucesso do cliente da Braze para conhecer as opções disponíveis para sua conta.

### Política de retenção {#retention-policy}

Durante o beta fechado, o preenchimento histórico além da janela de retenção padrão pode ser limitado.

Você pode consultar os dados mais recentes de dois anos para cada evento na view `USERS_*_SHARED` correspondente.

### Conformidade com o Regulamento Geral sobre a Proteção de Dados (GDPR) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Consulta de dados compartilhados: `TIME` e desempenho de consultas {#querying-shared-data-time-and-query-performance}

Os dados de eventos nas views de compartilhamento de dados (por exemplo, `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) são clusterizados no campo `TIME`. Ao filtrar por quando o evento ocorreu, use `TIME` como filtro preferencial. Consultas que restringem linhas usando `TIME` geralmente têm melhor desempenho do que consultas que filtram por `DB_CREATED_AT`, porque a clusterização está alinhada com o horário do evento.

| Campo | Significado |
| ----- | ------- |
| `TIME` | Timestamp Unix de quando o evento aconteceu. Prefira este campo ao filtrar por horário de ocorrência. |
| `DB_CREATED_AT` | Timestamp de quando a linha foi carregada no Databricks (horário de ingestão). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consulta de dados compartilhados: TIME e desempenho de consultas" }

### Velocidade, desempenho e custo das consultas {#speed-performance-and-cost-of-queries}

A velocidade, o desempenho e o custo de qualquer consulta que você execute sobre os dados dependem do tamanho do SQL warehouse utilizado. Dependendo da quantidade de dados acessados, pode ser necessário um warehouse maior para que a consulta seja concluída com sucesso. Para saber mais, consulte a documentação do Databricks sobre [criar e configurar um SQL warehouse](https://docs.databricks.com/en/compute/sql-warehouse/create.html) (incluindo tamanho do cluster e escalonamento).