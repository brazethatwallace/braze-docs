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
O Databricks Delta Sharing com a Braze está em **beta fechado**. A disponibilidade, as regiões suportadas e o comportamento do produto podem mudar. Entre em contato com o seu gerente de sucesso do cliente da Braze para participar ou confirmar se esse recurso está ativado para o seu espaço de trabalho.
{% endalert %}

O Databricks Delta Sharing faz parte da Distribuição de Dados da Braze. Para uma visão geral completa das opções de Distribuição de Dados, consulte [Distribuição de dados]({{site.baseurl}}/user_guide/data/distribution/).

## Configurar o Delta Sharing {#set-up-delta-sharing}

No Databricks, o compartilhamento de dados acontece entre um provedor de dados e um destinatário de dados. A sua conta da Braze é a **provedora de dados** porque cria e envia o compartilhamento, e a sua conta do Databricks é o **destinatário de dados** porque consome o compartilhamento para criar um catálogo que você pode consultar. Para saber mais, consulte a documentação do Databricks sobre [leitura de dados compartilhados usando Databricks-to-Databricks Delta Sharing (para destinatários)](https://docs.databricks.com/en/delta-sharing/read-data-databricks.html).

### Etapa 1: Configurar o compartilhamento na Braze {#step-1-configure-sharing-from-braze}

1. Na Braze, acesse **Integrações de parceiros** > **Compartilhamento de dados** > **Databricks Delta Sharing**.
2. Insira o seu identificador de compartilhamento do Databricks.
3. Quando terminar, selecione **Create Datashare**. A Braze envia o compartilhamento para a sua conta do Databricks.

### Etapa 2: Criar um catálogo no Databricks {#step-2-create-a-catalog-in-databricks}

1. Após alguns minutos, você deverá receber o compartilhamento de entrada na sua conta do Databricks.
2. Usando o compartilhamento de entrada, crie um catálogo para visualizar e consultar as tabelas. Por exemplo:
    {% raw %}
    ```sql
    CREATE CATALOG [IF NOT EXISTS] <catalog-name> USING SHARE braze.<share-name>;
    ```
    {% endraw %}
3. Conceda privilégios para que os usuários e grupos corretos possam consultar o novo catálogo.

{% alert warning %}
Os dados compartilhados são somente leitura no seu espaço de trabalho do Databricks. Você pode consultá-los como qualquer outro dado, mas não pode modificar ou excluir linhas nas tabelas compartilhadas por meio do compartilhamento.
{% endalert %}

## Uso e visualização {#usage-and-visualization}

Depois que o compartilhamento de dados for provisionado, crie um catálogo a partir do compartilhamento recebido para que as tabelas compartilhadas apareçam no seu espaço de trabalho do Databricks e possam ser consultadas como qualquer outro dado armazenado lá. Os dados compartilhados permanecem somente leitura.

Assim como o Currents, você pode usar o Databricks Delta Sharing para:

- Criar relatórios complexos
- Realizar modelagem de atribuição
- Compartilhar dados com segurança dentro da sua própria empresa
- Mapear dados brutos de eventos ou de usuários para um CRM (como o Salesforce)
- E muito mais

Para uma lista completa de tabelas e colunas disponíveis no Databricks, [baixe os esquemas de tabelas brutas do Databricks](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt) como arquivo de texto. Esse arquivo reflete o esquema do Databricks Delta Sharing (por exemplo, `DB_CREATED_AT` para o horário de ingestão). Ele não é intercambiável com os [esquemas de tabelas brutas do Snowflake](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) ou a [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/), que descrevem a nomenclatura e os campos do Snowflake.

{% alert note %}
Durante o beta fechado, nem todas as tabelas listadas no arquivo de esquema do Databricks podem estar disponíveis no seu compartilhamento. Os nomes e tipos de colunas também podem diferir do Snowflake Data Sharing (por exemplo, `DB_CREATED_AT` em vez de `SF_CREATED_AT`). Entre em contato com o seu gerente de sucesso do cliente da Braze se precisar da lista de tabelas atual para o seu espaço de trabalho.
{% endalert %}

### Esquema de ID do usuário {#user-id-schema}

Observe as seguintes diferenças entre as convenções de nomenclatura da Braze e do Databricks para IDs de usuário.

| Esquema da Braze | Esquema do Databricks | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `USER_ID` | O identificador único que a Braze atribui automaticamente. |
| `external_id` | `EXTERNAL_USER_ID` | O identificador único do perfil de um usuário que você define na Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de ID do usuário" }

## Informações importantes e limitações {#important-information-and-limitations}

### Disponibilidade do beta fechado {#closed-beta-availability}

Durante o beta fechado, o seu compartilhamento pode não incluir todas as tabelas no arquivo de [esquemas de tabelas brutas do Databricks](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt). Os dados compartilhados também podem diferir do Snowflake Data Sharing em nomes e tipos de colunas. Por exemplo, os compartilhamentos do Databricks usam `DB_CREATED_AT` para o horário de ingestão, enquanto os compartilhamentos do Snowflake usam `SF_CREATED_AT`.

### Alterações com e sem quebra de compatibilidade {#breaking-versus-non-breaking-changes}

#### Alterações sem quebra de compatibilidade {#non-breaking-changes}

Alterações sem quebra de compatibilidade podem acontecer a qualquer momento e geralmente fornecem funcionalidades adicionais. Exemplos de alterações sem quebra de compatibilidade:

- Adicionar uma nova tabela ou view
- Adicionar uma coluna a uma tabela ou view existente

{% alert important %}
Como novas colunas são consideradas alterações sem quebra de compatibilidade, a Braze recomenda fortemente listar explicitamente as colunas de interesse em cada consulta em vez de usar consultas `SELECT *`. Como alternativa, crie views que nomeiem explicitamente as colunas e consulte essas views em vez de consultar as tabelas compartilhadas diretamente.
{% endalert %}

#### Alterações com quebra de compatibilidade {#breaking-changes}

Quando possível, alterações com quebra de compatibilidade são precedidas por um anúncio e um período de migração. Exemplos de alterações com quebra de compatibilidade incluem:

- Remover uma tabela ou view
- Remover uma coluna de uma tabela ou view existente
- Alterar o tipo ou a nulabilidade de uma coluna existente

### Regiões do Databricks {#databricks-regions}

Durante o beta fechado, os provedores de nuvem e as regiões suportadas podem variar por espaço de trabalho e fase de lançamento. Entre em contato com o seu gerente de sucesso do cliente da Braze para conhecer as opções disponíveis para a sua conta.

### Política de retenção {#retention-policy}

Durante o beta fechado, o preenchimento histórico além do período de retenção padrão pode ser limitado.

Você pode consultar os dois anos mais recentes de dados para cada evento na view `USERS_*_SHARED` correspondente.

### Conformidade com o Regulamento Geral de Proteção de Dados (GDPR) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Consulta de dados compartilhados: `TIME` e desempenho de consultas {#querying-shared-data-time-and-query-performance}

Os dados de eventos nas views de compartilhamento de dados (por exemplo, `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) são clusterizados no campo `TIME`. Ao filtrar por quando o evento ocorreu, use `TIME` como filtro preferencial. Consultas que restringem linhas usando `TIME` geralmente têm melhor desempenho do que consultas que filtram por `DB_CREATED_AT`, porque a clusterização está alinhada com o horário do evento.

| Campo | Significado |
| ----- | ------- |
| `TIME` | Timestamp Unix do momento em que o evento ocorreu. Prefira este campo ao filtrar por horário de ocorrência. |
| `DB_CREATED_AT` | Timestamp de quando a linha foi carregada no Databricks (horário de ingestão). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consulta de dados compartilhados: TIME e desempenho de consultas" }

### Velocidade, desempenho e custo das consultas {#speed-performance-and-cost-of-queries}

A velocidade, o desempenho e o custo de qualquer consulta que você executar sobre os dados dependem do tamanho do SQL warehouse utilizado. Dependendo do volume de dados acessados, pode ser necessário um warehouse maior para que a consulta seja concluída com sucesso. Para saber mais, consulte a documentação do Databricks sobre [criação e configuração de um SQL warehouse](https://docs.databricks.com/en/compute/sql-warehouse/create.html) (incluindo tamanho do cluster e escalabilidade).