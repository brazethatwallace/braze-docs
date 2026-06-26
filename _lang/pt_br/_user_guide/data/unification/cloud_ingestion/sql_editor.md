---
nav_title: Editor SQL
article_title: "Ingestão de dados na nuvem: Editor SQL"
description: "Saiba como criar e validar sincronizações de Ingestão de dados na nuvem com consultas de SQL."
page_order: 11
page_type: reference
toc_headers: h2
---

# Ingestão de dados na nuvem: Editor SQL {#cloud-data-ingestion-sql-editor}

> Esta página explica como usar o Editor SQL da Ingestão de dados na nuvem (CDI) da Braze para criar e validar sincronizações com consultas de SQL.

O Editor SQL da Ingestão de dados na nuvem permite criar sincronizações escrevendo consultas de SQL diretamente no seu data warehouse. Isso elimina a necessidade de criar ou manter uma tabela CDI dedicada, que antes era obrigatória na [Etapa 1.1 das Integrações de Data Warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

Use o Editor SQL quando quiser:

- Sincronizar dados sem modificar tabelas upstream
- Trabalhar com dados brutos no seu warehouse
- Evitar a construção de uma coluna `PAYLOAD`
- Lidar com casos de uso de dados mais complexos com SQL

{% alert important %}
O Editor SQL da Ingestão de dados na nuvem está em beta. Fale com o seu gerente de sucesso do cliente ou gerente de conta para obter acesso.
{% endalert %}

## Pré-requisitos e limitações {#prerequisites-and-limitations}

O Editor SQL tem as seguintes limitações:

- Disponível apenas para fontes de data warehouse: Snowflake, Redshift, BigQuery, Databricks e Fabric.
- Apenas consultas de leitura com uma única instrução são suportadas.

{% alert note %}
A Braze executa apenas consultas de leitura nos seus dados e não modifica suas tabelas subjacentes. Objetos temporários podem ser criados durante a execução da consulta, mas não são persistidos.
{% endalert %}

## Criar uma nova sincronização com o Editor SQL {#create-a-new-sql-editor-sync}

Siga estas etapas para criar primeiro uma fonte e depois uma sincronização com o Editor SQL. Se você já configurou uma fonte para CDI, pule para a Etapa 3.

{% alert note %}
Essas etapas usam uma fonte Snowflake como exemplo. O processo de configuração para outras fontes de data warehouse é semelhante e pode ser encontrado na [Etapa 2: Criar uma nova fonte no dashboard da Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#step-2-create-a-new-source-in-the-braze-dashboard) da documentação [Configurando integrações de data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#setting-up-data-warehouse-integrations).
{% endalert %}

### Etapa 1: Configurar sua role, permissões, warehouse e usuário no Snowflake {#step-1-set-up-your-snowflake-role-permissions-warehouse-and-user}

Antes de criar sua fonte Snowflake no CDI, verifique se o usuário Snowflake que a Braze utiliza tem acesso aos dados que você deseja consultar e um warehouse para executar consultas.

#### Etapa 1.1: (Opcional) Criar um banco de dados e schema {#step-11-optional-create-a-database-and-schema}

Se necessário, crie um banco de dados e schema dedicados para seus dados CDI:

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```

#### Etapa 1.2: Configurar role e permissões de banco de dados {#step-12-set-up-role-and-database-permissions}

Conceda acesso às tabelas que você deseja sincronizar:

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.MY_USER_TABLE TO ROLE BRAZE_INGESTION_ROLE;
```

Você também pode conceder acesso a múltiplas tabelas ou tabelas futuras, dependendo do seu caso de uso. Por exemplo, para conceder acesso a todas as tabelas futuras em um schema:

```sql
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
```

#### Etapa 1.3: Configurar o warehouse e conceder acesso à role da Braze {#step-13-set-up-the-warehouse-and-grant-access-to-the-braze-role}

Crie um warehouse para a Braze executar consultas:

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
O warehouse deve ter a retomada automática ativada. Se não tiver, conceda à Braze privilégios adicionais de `OPERATE` no warehouse para que a Braze possa ativá-lo quando a consulta for executada.
{% endalert %}

#### Etapa 1.4: Criar um usuário Snowflake {#step-14-create-a-snowflake-user}

Crie um usuário para a Braze e atribua a role:

```sql
CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Você usará esse usuário ao configurar sua fonte Snowflake na Braze.

### Etapa 2: Criar uma nova fonte no dashboard da Braze {#step-2-create-a-new-source-in-the-braze-dashboard}

Nesta etapa, crie sua fonte Snowflake na Braze e valide a conexão.

#### Etapa 2.1: Adicionar uma fonte Snowflake {#step-21-add-a-snowflake-source}

1. No dashboard da Braze, acesse **Configurações de dados** > **Ingestão de dados na nuvem** > **Fontes**.
2. Selecione **Add data source**.
3. Selecione **Snowflake**.

#### Etapa 2.2: Inserir detalhes da conexão {#step-22-enter-connection-details}

Escolha um nome para sua fonte e insira suas credenciais e configuração do Snowflake.

{% alert note %}
Para o campo **Snowflake Account Locator**, insira o [identificador de conta](https://docs.snowflake.com/en/user-guide/admin-account-identifier) do Snowflake, que normalmente segue um formato como `xy12345.us-east-1.aws`. Isso não é o mesmo que um nome de banco de dados ou nome de warehouse.
{% endalert %}

#### Etapa 2.3: Concluir a configuração da chave RSA {#step-23-complete-rsa-key-setup}

Após inserir suas credenciais e configuração, selecione **Save credentials** e gere uma chave RSA. Em seguida, volte ao Snowflake para concluir a configuração. Adicione a chave pública exibida no dashboard ao usuário que você criou para a Braze se conectar ao Snowflake.

Para mais informações, consulte [Autenticação por par de chaves do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth). Se quiser rotacionar as chaves em algum momento, a Braze pode gerar um novo par de chaves e fornecer a nova chave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```

De volta à Braze, selecione **Test connection** para verificar o acesso à fonte e, em seguida, crie a fonte.

### Etapa 3: Criar uma nova sincronização e escrever sua consulta SQL {#step-3-create-a-new-sync-and-write-your-sql-query}

1. Acesse **Configurações de dados** > **Ingestão de dados na nuvem** > **Syncs**.
2. Selecione **Create data sync**.
3. Escolha qualquer sincronização em **Data Type**.
4. Referencie a fonte da Etapa 2.
5. Selecione **SQL** e escreva uma consulta SQL que retorne dados de usuários do seu warehouse. Sua consulta SQL define os dados que serão sincronizados com a Braze. O resultado da consulta se torna o schema da sua sincronização.

Você pode usar o Source Explorer para navegar pelas tabelas e views disponíveis para sincronização, ou o gerador de SQL com IA para obter a ajuda do Braze Operator na sua consulta SQL.

{% alert note %}
Apenas consultas de leitura são suportadas, incluindo cláusulas `JOIN`. Para mais detalhes, consulte [Restrições de SQL](#sql-constraints).
{% endalert %}

### Etapa 4: Pré-visualizar e validar sua consulta {#step-4-preview-and-validate-your-query}

Selecione **Preview and validate** para executar sua consulta.

A pré-visualização:

- Exibe os resultados em formato de tabela
- Mostra até 100 linhas
- Mostra até 250 colunas

Para validar com sucesso, sua consulta SQL deve retornar várias colunas obrigatórias:

| Tipo de dados da sincronização | Colunas obrigatórias |
|---|---|
| Atributos | - Um identificador de usuário, sendo um dos seguintes: `external_id`, `braze_id`, `alias_name` e `alias_label`, e-mail ou número de telefone.<br>- `UPDATED_AT`.<br>- Pelo menos uma coluna adicional (atributo) para sincronizar. |
| Excluir usuários | - Um identificador de usuário, sendo um dos seguintes: `external_id`, `braze_id`, `alias_name` e `alias_label`, e-mail ou número de telefone.<br>- `UPDATED_AT`. |
| Canvas Triggers | - Um identificador de usuário, sendo um dos seguintes: `external_id`, `braze_id`, `alias_name` e `alias_label`, e-mail ou número de telefone.<br>- `UPDATED_AT`. |
| Eventos personalizados | - Um identificador de usuário, sendo um dos seguintes: `external_id`, `braze_id`, `alias_name` e `alias_label`, e-mail ou número de telefone.<br>- `UPDATED_AT`.<br>- `NAME` para representar o nome do evento.<br>- `TIME` para representar o horário do evento. Se indisponível, o CDI usa `UPDATED_AT` como substituto. |
| Eventos de compra | - Um identificador de usuário, sendo um dos seguintes: `external_id`, `braze_id`, `alias_name` e `alias_label`, e-mail ou número de telefone.<br>- `UPDATED_AT`.<br>- `PRODUCT_ID`.<br>- `CURRENCY`.<br>- `PRICE`.<br>- `TIME` para representar o horário do evento de compra. Se indisponível, o CDI usa `UPDATED_AT` como substituto. |
| Catálogo | - `ID` para representar o identificador do item do catálogo.<br>- `UPDATED_AT`.<br>- Pelo menos uma coluna adicional (campo do catálogo) para sincronizar. |
| Contas | - `ID` para representar o identificador da conta.<br>- `NAME` para representar o nome da conta.<br>- `UPDATED_AT`.<br>- Pelo menos uma coluna adicional (campo da conta) para sincronizar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 4: Pré-visualizar e validar sua consulta" }

Colunas adicionais além das obrigatórias são sincronizadas como atributos, propriedades de contexto do Canvas, propriedades de eventos, campos de catálogo e campos de conta, respectivamente. Consulte [Comportamento de validação](#validation-behavior) e [Solução de problemas](#troubleshooting) para dicas úteis sobre erros de pré-visualização e validação e como corrigi-los.

### Etapa 5: Revisar o mapeamento de atributos e criar a sincronização {#step-5-review-attribute-mapping-and-create-sync}

Quando a validação for bem-sucedida, continue para **Next: Notifications** e crie sua sincronização.

{% alert important %}
Uma configuração SQL incorreta pode levar a resultados indesejados, incluindo o consumo excessivo de data points e riscos operacionais mais amplos. Você é responsável por garantir que a lógica da sua consulta esteja correta e deve pré-visualizar cuidadosamente todos os resultados antes de ativar uma sincronização.
{% endalert %}

## Restrições de SQL {#sql-constraints}

### Usar apenas consultas `SELECT` {#use-select-queries-only}

Apenas consultas de leitura são suportadas.

Você pode usar:

- `SELECT`
- `WITH` (CTEs)
- `JOIN`

Você não pode usar:

- `INSERT`, `UPDATE` ou `DELETE`
- `CREATE` ou `DROP`
- Múltiplas instruções separadas por `;`

### Usar uma única instrução {#use-a-single-statement}

Sua consulta deve ser uma única instrução executável.

## Comportamento de validação {#validation-behavior}

O Editor SQL valida sua consulta antes de permitir que você prossiga.

### Erros de SQL {#sql-errors}

Se sua consulta contiver erros de sintaxe:

- A validação falha
- Nenhuma pré-visualização é exibida
- Seu warehouse retorna uma mensagem de erro

### Erros de compilação {#compilation-errors}

Se sua consulta referenciar tabelas, colunas ou objetos inválidos ou não autorizados:

- A validação falha
- Nenhuma pré-visualização é exibida
- Seu warehouse retorna uma mensagem de erro

### Erros de conexão {#connection-errors}

Se a Braze não conseguir se conectar ao seu warehouse:

- A validação falha
- Nenhuma pré-visualização é exibida
- Uma mensagem de erro de conexão é exibida

### Tempo limite da consulta {#query-timeout}

Se sua consulta demorar muito para executar:

- A Braze encerra a consulta
- A validação falha
- Um erro de tempo limite é exibido

### Erros de schema da tabela {#table-schema-errors}

Se sua consulta compilar, a validação ainda pode falhar se:

- Nenhuma coluna de identificador for encontrada
- `UPDATED_AT` estiver ausente
- Outras colunas obrigatórias estiverem ausentes

Nesse caso, a pré-visualização ainda é exibida para ajudar você a chegar a uma validação bem-sucedida. Consulte a [Etapa 4 na seção anterior](#step-4-preview-and-validate-your-query) para detalhes sobre as colunas obrigatórias para cada tipo de dados de sincronização.

### Resultados com zero linhas {#zero-row-results}

Se sua consulta retornar zero linhas:

- A validação **é aprovada**
- Você ainda pode criar a sincronização
- Nenhum usuário é atualizado até que linhas sejam retornadas

## Suporte a `PAYLOAD` (legado) {#payload-support-legacy}

O Editor SQL suporta [tabelas CDI legadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-1-set-up-tables-or-views) onde uma coluna `PAYLOAD` está presente.

Se sua consulta incluir:

- Um identificador válido
- `UPDATED_AT`
- Uma coluna `PAYLOAD`
- Colunas adicionais

Então:

- A Braze sincroniza apenas a coluna `PAYLOAD`
- A Braze ignora as colunas adicionais

## Editar uma sincronização SQL {#edit-a-sql-sync}

Ao editar uma sincronização existente:

- Qualquer alteração no SQL requer revalidação
- Você não pode salvar alterações inválidas
- Alterações válidas entram em vigor após salvar

Se uma execução de sincronização já estiver em andamento, suas alterações entrarão em vigor na próxima execução.

## Solução de problemas {#troubleshooting}

Esta seção inclui erros comuns e orientações sobre como solucioná-los.

### Sem pré-visualização disponível {#no-preview-available}

Quando você vê "No preview available", um dos seguintes tipos de erro pode estar causando isso.

| Tipo de erro | Etapas para resolver |
|---|---|
| "No preview available" | Leia o banner de erro para obter dicas. |
| "Unable to connect to the source" | Verifique o nome de usuário configurado, o localizador de conta e a configuração de autenticação por par de chaves RSA.<br>Verifique se o warehouse está em execução.<br>Confirme o acesso à rede. |
| "SQL syntax error" | Verifique a sintaxe do seu SQL. |
| "Object does not exist or not authorized" | Verifique se a role tem acesso `SELECT` à tabela.<br>Confirme as permissões de banco de dados e schema.<br>Verifique erros de digitação no nome da tabela. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sem pré-visualização disponível" }

### Coluna de identidade obrigatória {#identity-column-required}

Verifique se sua consulta inclui um identificador válido, como `external_id`.

### Coluna `UPDATED_AT` ausente {#updated_at-column-is-missing}

Adicione uma coluna de timestamp para sincronização incremental.

### Adicione mais colunas... Não há atributos/campos de catálogo/campos de conta para sincronizar {#add-more-columns-there-are-no-attributescatalog-fieldsaccount-fields-to-sync}

Adicione pelo menos uma coluna adicional além do identificador e `UPDATED_AT`.

### Tempo limite de execução da consulta excedido {#query-execution-timed-out}

Otimize sua consulta ou use um warehouse maior.