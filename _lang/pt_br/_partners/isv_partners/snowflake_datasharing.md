---
nav_title: Compartilhamento de dados do Snowflake
hidden: true
---

# Integração do compartilhamento de dados do Snowflake {#snowflake-data-sharing-integration}

> Quando o Snowflake Data Share é usado como método de integração, a Braze provisiona um compartilhamento para a sua instância do Snowflake em nome do cliente. Esse compartilhamento incluirá automaticamente todos os eventos de engajamento com mensagens e de comportamento do usuário.

Os compartilhamentos são provisionados por cliente após o cliente adquirir um direito de compartilhamento de dados do Snowflake. Quando um cliente solicita um compartilhamento de dados, a Braze adiciona um compartilhamento ao espaço de trabalho do cliente, e o cliente pode usar a interface de autoatendimento para adicionar os dados relevantes da conta Snowflake do parceiro.

![Provisionamento de compartilhamento de dados do Snowflake no dashboard da Braze]({% image_buster /assets/img/snowflake.png %})

Depois que o compartilhamento é provisionado, todos os dados ficam imediatamente acessíveis a partir da instância do Snowflake como um compartilhamento de dados de entrada.

![Compartilhamento de dados de entrada do Snowflake na instância do Snowflake do cliente]({% image_buster /assets/img/snowflake2.png %})

Na sua instância do Snowflake, você verá um compartilhamento por região. Cada tabela tem uma coluna, `app_group_id`, que funciona como uma chave de locatário para a Braze. À medida que novos clientes são adicionados a um compartilhamento dentro da mesma região, eles aparecerão como diferentes `app_group_ids` nas tabelas existentes.

{% alert important %}
Atualmente, a Braze hospeda todos os dados de nível de usuário nas regiões AWS US East-1 e EU-Central (Frankfurt) do Snowflake. Embora a Braze possa compartilhar entre regiões, é mais econômico para os clientes se o compartilhamento for feito com `US-EAST-1` e/ou `EU-CENTRAL-1`.
{% endalert %}

{% alert tip %}
Baixe os [esquemas de tabelas brutas](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) ou use este conjunto de [dados de eventos de amostra](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset) disponível no marketplace do Snowflake para se familiarizar com os eventos compartilhados.
{% endalert %}

## Tratamento de eventos duplicados {#handling-duplicate-events}

É esperado que haja duplicatas, mas todos os eventos possuem um identificador exclusivo, a coluna ID. As duplicatas podem ser removidas com `select distinct(id)`.

## Alterações interruptivas e não interruptivas {#breaking-versus-non-breaking-changes}

### Alterações não interruptivas {#non-breaking-changes}

Alterações não interruptivas podem ocorrer a qualquer momento e geralmente trazem funcionalidades adicionais. Exemplos de alterações não interruptivas:
- Adição de uma nova tabela ou visualização
- Adição de uma coluna a uma tabela ou visualização existente

{% alert important %}
Como novas colunas são consideradas não interruptivas, a Braze recomenda enfaticamente listar de modo explícito as colunas de interesse em cada consulta, em vez de usar consultas `SELECT *`. Como alternativa, você pode criar visualizações que nomeiem explicitamente as colunas e, em seguida, consultar essas visualizações em vez das tabelas diretamente.
{% endalert %}

### Alterações interruptivas {#breaking-changes}

Quando possível, as alterações interruptivas serão precedidas de um anúncio e de um período de migração. Exemplos de alterações interruptivas incluem:
- Remoção de uma tabela ou visualização
- Remoção de uma coluna de uma tabela ou visualização existente
- Alteração do tipo ou da nulabilidade de uma coluna existente

## Quando as tabelas SNAPSHOTS e CHANGELOGS são atualizadas {#when-snapshots-and-changelogs-tables-are-updated}

As tabelas SNAPSHOTS e CHANGELOGS rastreiam as alterações em Campaigns e Canvas. Entender quando essas tabelas são atualizadas é importante para consultar as variações de mensagens mais recentes e as configurações do Canvas.

### CHANGELOGS_CAMPAIGN_SHARED

Uma linha é adicionada a `CHANGELOGS_CAMPAIGN_SHARED` quando:
- A Campaign é lançada, OU
- Qualquer um dos seguintes campos registráveis é alterado:
  - Nome
  - Ações (incluindo alterações no conteúdo das mensagens)
  - Comportamentos de conversão

{% alert important %}
Salvar ou atualizar o rascunho pós-lançamento não dispara automaticamente uma atualização. A atualização é disparada somente quando você lança a Campaign ou aplica as alterações do rascunho pós-lançamento à Campaign ativa.
{% endalert %}

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED

`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` é derivada de `CHANGELOGS_CAMPAIGN_SHARED`. Essa tabela extrai e organiza a coluna de ações de `CHANGELOGS_CAMPAIGN_SHARED` em registros individuais de variação de mensagem. Ela é atualizada quando `CHANGELOGS_CAMPAIGN_SHARED` é atualizada.

### CHANGELOGS_CANVAS_SHARED

Uma linha é adicionada a `CHANGELOGS_CANVAS_SHARED` quando:
- O Canvas é lançado, OU
- Qualquer um dos seguintes campos registráveis é alterado:
  - Nome
  - Comportamentos de conversão
  - Variações (porcentagem, atribuições da primeira etapa, nomes das variações)

{% alert important %}
Salvar ou atualizar o rascunho pós-lançamento não dispara automaticamente uma atualização. A atualização é disparada somente quando você lança o Canvas ou aplica as alterações do rascunho pós-lançamento ao Canvas ativo.
{% endalert %}

### SNAPSHOTS_CANVAS_VARIATION_SHARED

`SNAPSHOTS_CANVAS_VARIATION_SHARED` é derivada de `CHANGELOGS_CANVAS_SHARED`. Essa tabela usa o mesmo padrão de extração que `SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` e é atualizada quando `CHANGELOGS_CANVAS_SHARED` é atualizada.

### SNAPSHOTS_CANVAS_STEP_SHARED

Uma linha é adicionada a `SNAPSHOTS_CANVAS_STEP_SHARED` quando:
- O Canvas é lançado, OU
- O Canvas ativo é atualizado (rascunho pós-lançamento aplicado), OU
- Qualquer um dos seguintes campos registráveis é alterado:
  - Nome
  - Ações (incluindo alterações no conteúdo da mensagem em variações de mensagens)

{% alert important %}
Salvar o rascunho pós-lançamento não dispara automaticamente uma atualização. A atualização é disparada somente quando você lança o Canvas ou aplica as alterações do rascunho pós-lançamento ao Canvas ativo.
{% endalert %}

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED

Uma linha é adicionada a `SNAPSHOTS_CANVAS_FLOW_STEP_SHARED` quando:
- O Canvas é lançado, OU
- O Canvas ativo é atualizado (rascunho pós-lançamento aplicado), OU
- Qualquer um dos seguintes campos registráveis é alterado:
  - Nome

{% alert important %}
Salvar o rascunho pós-lançamento não dispara automaticamente uma atualização. A atualização é disparada somente quando você lança o Canvas ou aplica as alterações do rascunho pós-lançamento ao Canvas ativo.
{% endalert %}

## Conformidade com o Regulamento Geral sobre a Proteção de Dados (GDPR) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}