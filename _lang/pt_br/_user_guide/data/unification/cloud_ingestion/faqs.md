---
nav_title: FAQ
article_title: Perguntas frequentes sobre ingestão de dados na nuvem
page_order: 10
page_type: FAQ
description: "Esta página responde às perguntas frequentes sobre a Ingestão de dados na nuvem."
toc_headers: h2
---

# Perguntas frequentes {#frequently-asked-questions}

> Esta página contém respostas para algumas perguntas frequentes sobre a Ingestão de dados na nuvem.

## Por que recebi o e-mail: "Error in CDI Sync"? {#why-was-i-emailed-error-in-cdi-sync}

Esse tipo de e-mail geralmente significa que há um problema com a configuração do seu CDI. Veja alguns problemas comuns e como resolvê-los:

### O CDI não consegue acessar o data warehouse ou a tabela usando suas credenciais {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

Isso pode significar que as credenciais no CDI estão incorretas ou configuradas de forma errada no data warehouse. Para saber mais, consulte [Integrações com data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

### A tabela não pode ser encontrada {#the-table-cannot-be-found}

Tente atualizar sua integração com a configuração correta do banco de dados ou crie os recursos correspondentes no data warehouse, como `database/table`.

### O catálogo não pode ser encontrado {#the-catalog-cannot-be-found}

O catálogo configurado na integração não existe no catálogo da Braze. Um catálogo pode ter sido removido após a configuração da integração. Para resolver o problema, atualize a integração para usar um catálogo diferente ou crie um novo catálogo que corresponda ao nome do catálogo na integração.

## Por que recebi o e-mail: "Row errors in your CDI sync"? {#why-was-i-emailed-row-errors-in-your-cdi-sync}

Esse tipo de e-mail significa que alguns dos seus dados não puderam ser processados durante a sincronização. Para descobrir o erro específico, você pode revisar os registros na Braze acessando **CDI** > **Sync Log**.

## Como corrigir o erro "Time must be string in ISO8601 Format" na configuração de CDI? {#how-do-i-fix-time-must-be-string-in-iso8601-format-in-cdi-setup}

Esse erro significa que o valor de `time` do evento na sua carga útil de CDI não está em um formato de data e hora compatível.

Para cargas úteis de eventos e compras, formate `time` como:

- Uma string ISO 8601, ou
- `yyyy-MM-dd'T'HH:mm:ss:SSSZ`

Se `time` for omitido, a Braze usa `UPDATED_AT` como o horário do evento.

Para conferir todos os requisitos de carga útil, consulte [Configuração de tabela para ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

## Como corrigir erros de Test Connection e e-mails de suporte? {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### Test Connection está lento {#test-connection-runs-slow}

O Test Connection é executado no seu data warehouse, então aumentar a capacidade do warehouse pode melhorar a velocidade. Usar uma instância SQL serverless minimiza o tempo de aquecimento e melhora a taxa de transferência de consultas, mas pode resultar em custos de integração ligeiramente mais altos.

### Erro ao conectar à instância do Snowflake: Incoming request with IP is not allowed to access Snowflake {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

Tente adicionar os IPs oficiais da Braze à sua lista de IPs permitidos. Para saber mais, consulte [Integrações com data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations), ou permita os IPs relevantes:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Erro ao executar SQL devido à configuração do cliente: 002003 (42S02): SQL compilation error: does not exist or not authorized {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

Se a tabela não existir, crie a tabela. Se a tabela existir, verifique se o usuário e a função têm permissões para ler a tabela.

### Could not use schema {#could-not-use-schema}

Se você receber esse erro, conceda acesso a esse schema para o usuário ou função especificado.

### Could not use role {#could-not-use-role}

Se você receber esse erro, permita que o usuário use a função especificada.

### User access disabled {#user-access-disabled}

Se você receber esse erro, permita que o usuário acesse sua conta do Snowflake.

### Erro ao conectar à instância do Snowflake com a chave atual e a antiga {#error-connecting-to-snowflake-instance-with-current-and-old-key}

Se você receber esse erro, verifique se o usuário está usando a chave pública atual conforme exibida no seu dashboard da Braze.
{% endtab %}

{% tab Redshift %}
### Test Connection está lento

O Test Connection é executado no seu data warehouse, então aumentar a capacidade do warehouse pode melhorar a velocidade. Usar uma instância SQL serverless minimiza o tempo de aquecimento e melhora a taxa de transferência de consultas, mas pode resultar em custos de integração ligeiramente mais altos.

### Permission denied for relation {table_name} {#permission-denied-for-relation-table_name}

Se você receber esse erro:

  - Conceda a permissão `usage` no schema para esse usuário.
  - Conceda a permissão `select` na tabela para esse usuário.

### Create Connection Error {#create-connection-error}

Se você receber esse erro, verifique se o endpoint e a porta do Redshift estão corretos.

### Create SSH Tunnel Error {#create-ssh-tunnel-error}

Se você receber esse erro:

  - Verifique se a chave pública no seu dashboard da Braze está no host ec2 usado para o túnel SSH.
  - Verifique se o nome de usuário está correto.
  - Verifique se o túnel SSH está correto.
{% endtab %}

{% tab BigQuery %}
### Test Connection está lento

O Test Connection é executado no seu data warehouse, então aumentar a capacidade do warehouse pode melhorar a velocidade. Usar uma instância SQL serverless minimiza o tempo de aquecimento e melhora a taxa de transferência de consultas, mas pode resultar em custos de integração ligeiramente mais altos.

### User does not have permission to query table {#user-does-not-have-permission-to-query-table}

Se você receber esse erro, adicione permissões de usuário para consultar a tabela.

### Your usage exceeded the custom quota {#your-usage-exceeded-the-custom-quota}

Se você receber esse erro, sua cota precisa ser atualizada para que você possa continuar sincronizando na taxa atual.

### Table was not found in location {region} Location {#table-was-not-found-in-location-region-location}

Se você receber esse erro, verifique se a tabela está no projeto e dataset corretos.

### Invalid JWT Signature {#invalid-jwt-signature}

Se você receber esse erro, verifique se o serviço de API do BigQuery está ativado para a sua conta.
{% endtab %}

{% tab Databricks %}
### Test Connection está lento

O Test Connection é executado no seu data warehouse, então aumentar a capacidade do warehouse pode melhorar a velocidade. Para o Databricks, pode haver de dois a cinco minutos de tempo de aquecimento quando a Braze se conecta a instâncias SQL Classic e Pro, o que causa atrasos durante a configuração e o teste da conexão, bem como no início das sincronizações agendadas. Usar uma instância SQL serverless minimiza o tempo de aquecimento e melhora a taxa de transferência de consultas, mas pode resultar em custos de integração ligeiramente mais altos.

### Command failed because warehouse was stopped {#command-failed-because-warehouse-was-stopped}

Se você receber esse erro, verifique se o warehouse do Databricks está em execução.

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden

Se você receber esse erro, consulte [Databricks: Forbidden error while accessing S3 data](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Como atualizo minhas preferências de alerta por e-mail para integrações de CDI? {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

Cada integração tem sua própria preferência de notificação. Acesse a página de CDI e selecione o nome da integração que deseja atualizar. Na seção **Notification preferences**, você pode atualizar como recebe alertas sobre a integração selecionada.

## O que acontece se um UPDATED_AT futuro for sincronizado com uma integração? {#what-happens-if-a-future-updated_at-gets-synced-with-an-integration}

A CDI usa `UPDATED_AT` para decidir quais dados são novos. Depois que um `UPDATED_AT` futuro é sincronizado, qualquer dado anterior a essa data e hora futura não será processado. Para corrigir isso:

1. Corrija o `UPDATED_AT`.
2. Remova quaisquer dados antigos que já foram sincronizados com a Braze.
3. Crie uma nova integração para processar essa tabela novamente.

## Por que "Rows Synced" não corresponde ao número no meu data warehouse? {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

O CDI usa `UPDATED_AT` para decidir quais registros devem ser coletados durante uma sincronização. Confira [esta ilustração]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion#how-it-works) para entender como funciona. No início de uma execução de sincronização, o CDI consulta seu data warehouse para obter todos os registros com `UPDATED_AT` posterior ao valor de `UPDATED_AT` processado anteriormente. Registros no exato timestamp de limite também podem ser ressincronizados se novas linhas compartilharem esse timestamp. Qualquer registro coletado no momento em que a consulta é executada é sincronizado na Braze. Veja os casos mais comuns em que um registro pode não ser sincronizado:

- Você está adicionando registros à tabela com um valor de `UPDATED_AT` que já foi processado.
- Você está atualizando valores de registros depois que eles foram processados por uma sincronização, mas mantendo `UPDATED_AT` inalterado.
- Você está adicionando ou atualizando registros enquanto uma sincronização está em andamento. Dependendo de quando a consulta do CDI é executada, podem ocorrer condições de corrida que fazem com que registros não sejam coletados.

{% alert tip %}
Para evitar esses comportamentos no futuro, recomendamos usar valores de `UPDATED_AT` monotonicamente crescentes e não atualizar a tabela durante a execução de sincronização agendada.
{% endalert %}

## Preciso de valores `UPDATED_AT` majoritariamente distintos para importações CDI de grande volume? {#do-i-need-mostly-distinct-updated_at-values-for-large-cdi-imports}

Sim. Para execuções de alto volume (por exemplo, mais de aproximadamente 10 milhões de linhas), certifique-se de que seus dados de origem tenham valores `UPDATED_AT` majoritariamente distintos. Se muitas linhas compartilharem o mesmo timestamp, a CDI tem mais chances de re-selecionar linhas em timestamps de fronteira em execuções posteriores. Isso pode aumentar sincronizações duplicadas e o consumo de pontos de dados.

Para saber mais sobre o comportamento de fronteira da CDI, consulte [Evitar ressincronização de linhas com timestamps duplicados]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps).

### Onde executo essas verificações SQL? {#where-do-i-run-these-sql-checks}

Execute as verificações diretamente no editor SQL do seu data warehouse, na mesma tabela ou view usada pela sua integração CDI:

- Snowflake: **Projects** > **Worksheets** (para saber mais, consulte [Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs))
- Redshift: Query Editor v2 (para saber mais, consulte [Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html))
- BigQuery: BigQuery Studio SQL workspace (para saber mais, consulte [BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction))
- Databricks: SQL editor (SQL warehouse) (para saber mais, consulte [Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/))
- Fabric: SQL query editor

Use este processo antes de ativar ou escalar uma sincronização de grande volume:

1. Identifique a tabela ou view de origem CDI exata e a janela de sincronização que você deseja validar.
2. Abra o editor SQL do seu data warehouse e selecione o mesmo banco de dados e schema usados pela CDI. Em seguida, use uma role com acesso de leitura à tabela ou view de origem.
3. Execute a consulta de contagem de timestamps distintos para medir quantos valores `UPDATED_AT` distintos existem nessa janela.
4. Execute a consulta que agrupa por `UPDATED_AT` e conta as linhas para encontrar timestamps com contagens de linhas excepcionalmente altas.
5. Se muitas linhas compartilharem timestamps idênticos, ajuste seu processo de ingestão para que lotes consecutivos usem valores `UPDATED_AT` progressivamente mais recentes, ou aumente a precisão dos timestamps para que as linhas fiquem mais distribuídas.
6. Execute ambas as consultas novamente até que a concentração seja reduzida. Depois, inicie ou escale sua sincronização.
7. Após o lançamento, monitore **CDI** > **Sync Log** para verificar se há volume inesperado de ressincronização em timestamps de fronteira.

Use verificações como estas no seu data warehouse:

```sql
SELECT
  COUNT(*) AS total_rows,
  COUNT(DISTINCT UPDATED_AT) AS distinct_timestamps,
  ROUND(COUNT(*) * 1.0 / NULLIF(COUNT(DISTINCT UPDATED_AT), 0), 2) AS avg_rows_per_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP);
```

```sql
SELECT
  UPDATED_AT,
  COUNT(*) AS rows_at_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP)
GROUP BY UPDATED_AT
ORDER BY rows_at_timestamp DESC
LIMIT 20;
```

Se o seu data warehouse não suportar `LIMIT` (por exemplo, Fabric), use uma sintaxe equivalente, como `TOP`.

## Por que uma sincronização CDI com poucas linhas ainda pode levar vários minutos? {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

Uma sincronização CDI inclui um período fixo de inicialização antes que o processamento das linhas comece. Como esse tempo de inicialização é semelhante independentemente do tamanho da sincronização, uma sincronização pequena ainda pode levar vários minutos e parecer mais lenta em linhas por minuto. O tempo total de sincronização ainda depende da complexidade da consulta de origem, do formato dos dados e da capacidade disponível no seu data warehouse. Para saber mais, consulte [Integrações com data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Durante uma sincronização, a ordem é preservada se vários registros compartilham o mesmo ID? {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

A ordem de processamento não é 100% previsível. Por exemplo, se houver várias linhas com o mesmo `EXTERNAL_ID` na tabela durante uma sincronização, não é possível garantir qual valor será mantido no perfil final. Se você estiver atualizando o mesmo `EXTERNAL_ID` com atributos diferentes na coluna de carga útil, todas as alterações serão refletidas quando a sincronização for concluída.

## Por que novos usuários não estão sendo criados a partir da minha sincronização CDI? {#why-are-new-users-not-being-created-from-my-cdi-sync}

Se a sua integração CDI tem a opção **Update existing users only** ativada, apenas os usuários que já existem na Braze são atualizados, e novos usuários não são criados. Isso significa que, se uma linha na sua tabela de sincronização faz referência a um `EXTERNAL_ID` que não corresponde a nenhum usuário existente na Braze, essa linha é ignorada.

Para criar novos usuários por meio da CDI, desative o botão **Update existing users only** nas configurações da sua integração. Acesse **Data Settings** > **Cloud Data Ingestion** e selecione uma integração.

## Quais são as medidas de segurança para CDI? {#what-are-the-security-measures-for-cdi}

### Nossas medidas {#our-measures}

A Braze tem as seguintes medidas em vigor para CDI:

- Todas as credenciais são criptografadas em nosso banco de dados, e apenas determinados colaboradores têm acesso autenticado a elas.
- Usamos conexões criptografadas para enviar dados aos data warehouses dos clientes.
- Fazemos solicitações aos endpoints da API da Braze usando as mesmas chaves de API e conexões TLS que recomendamos que nossos clientes usem.
- Atualizamos regularmente nossas bibliotecas e aplicamos todas as correções de segurança.

### Suas medidas {#your-measures}

Recomendamos que você e sua equipe configurem as seguintes medidas de segurança do seu lado:

- Restrinja o acesso às credenciais ao mínimo necessário para que o CDI funcione. Isso porque precisamos ser capazes de executar select (e count) nas tabelas e views específicas.
- Restrinja os IPs que podem acessar as tabelas aos [IPs da Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views) oficialmente publicados.