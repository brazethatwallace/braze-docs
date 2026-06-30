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

## Por que recebi o e-mail: "Erro na sincronização do CDI"? {#why-was-i-emailed-error-in-cdi-sync}

Esse tipo de e-mail geralmente significa que há um problema com a configuração do seu CDI. Aqui estão alguns problemas comuns e como corrigi-los:

### O CDI não consegue acessar o data warehouse ou a tabela usando suas credenciais {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

Isso pode significar que as credenciais no CDI estão incorretas ou mal configuradas no data warehouse. Para saber mais, consulte [Integrações de data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

### A tabela não pode ser encontrada {#the-table-cannot-be-found}

Tente atualizar sua integração com a configuração correta do banco de dados ou criar recursos correspondentes no data warehouse, como `database/table`.

### O catálogo não pode ser encontrado {#the-catalog-cannot-be-found}

O catálogo configurado na integração não existe no catálogo da Braze. Um catálogo pode ser removido depois que a integração foi configurada. Para resolver o problema, atualize a integração para usar um catálogo diferente ou crie um novo catálogo que corresponda ao nome do catálogo na integração.

## Por que recebi o e-mail: "Erros de linha na sua sincronização de CDI"? {#why-was-i-emailed-row-errors-in-your-cdi-sync}

Esse tipo de e-mail significa que alguns dos seus dados não puderam ser processados durante a sincronização. Para descobrir o erro específico, você pode revisar os registros na Braze acessando **CDI** > **Sync Log**.

## Como faço para corrigir erros na conexão de teste e nos e-mails de suporte? {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### A conexão de teste é lenta {#test-connection-runs-slow}

A conexão de teste está sendo executada no seu data warehouse, portanto, aumentar a capacidade do data warehouse pode melhorar sua velocidade. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará a taxa de transferência da consulta, mas poderá resultar em custos de integração ligeiramente mais altos.

### Erro ao conectar-se à instância do Snowflake: a solicitação de entrada com IP não tem permissão para acessar o Snowflake {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

Tente adicionar os IPs oficiais da Braze à sua lista de permissões de IP. Para saber mais, consulte [Integrações de data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations), ou permita os IPs relevantes:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Erro ao executar o SQL devido à configuração do cliente: 002003 (42S02): erro de compilação SQL: não existe ou não está autorizado {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

Se a tabela não existir, crie a tabela. Se a tabela existir, verifique se o usuário e a função têm permissão para ler a tabela.

### Não foi possível usar o esquema {#could-not-use-schema}

Se receber esse erro, conceda acesso a esse esquema para o usuário ou função especificada.

### Não foi possível usar a função {#could-not-use-role}

Se você receber esse erro, permita que esse usuário use a função especificada.

### Acesso do usuário desativado {#user-access-disabled}

Se receber esse erro, permita que esse usuário tenha acesso à sua conta do Snowflake.

### Erro ao se conectar à instância do Snowflake com a chave atual e a antiga {#error-connecting-to-snowflake-instance-with-current-and-old-key}

Se receber esse erro, verifique se o usuário está usando a chave pública atual, conforme exibido no dashboard da Braze.
{% endtab %}

{% tab Redshift %}
### A conexão de teste é lenta

A conexão de teste está sendo executada no seu data warehouse, portanto, aumentar a capacidade do data warehouse pode melhorar sua velocidade. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará a taxa de transferência da consulta, mas poderá resultar em custos de integração ligeiramente mais altos.

### Permissão negada para a relação {table_name} {#permission-denied-for-relation-table_name}

Se você receber esse erro:

  - Conceda a permissão `usage` no esquema para esse usuário.
  - Conceda a permissão `select` na tabela para esse usuário.

### Erro ao criar conexão {#create-connection-error}

Se você receber esse erro, verifique se o endpoint e a porta do Redshift estão corretos.

### Erro ao criar túnel SSH {#create-ssh-tunnel-error}

Se você receber esse erro:

  - Verifique se a chave pública no seu dashboard da Braze está no host ec2 usado para o tunelamento SSH.
  - Verifique se o seu nome de usuário está correto.
  - Verifique se o túnel SSH está correto.
{% endtab %}

{% tab BigQuery %}
### A conexão de teste é lenta

A conexão de teste está sendo executada no seu data warehouse, portanto, aumentar a capacidade do data warehouse pode melhorar sua velocidade. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará a taxa de transferência da consulta, mas poderá resultar em custos de integração ligeiramente mais altos.

### O usuário não tem permissão para consultar a tabela {#user-does-not-have-permission-to-query-table}

Se receber esse erro, adicione permissões de usuário para consultar a tabela.

### Seu uso excedeu a cota personalizada {#your-usage-exceeded-the-custom-quota}

Se receber esse erro, sua cota precisará ser atualizada para que você possa continuar sincronizando na taxa atual.

### A tabela não foi encontrada no local {region} {#table-was-not-found-in-location-region-location}

Se você receber esse erro, verifique se a tabela está no projeto e no conjunto de dados corretos.

### Assinatura JWT inválida {#invalid-jwt-signature}

Se você receber esse erro, verifique se o serviço da API do BigQuery está ativado na sua conta.
{% endtab %}

{% tab Databricks %}
### A conexão de teste é lenta

A conexão de teste está sendo executada no seu data warehouse, portanto, aumentar a capacidade do data warehouse pode melhorar sua velocidade. Para o Databricks, pode haver de dois a cinco minutos de tempo de aquecimento quando a Braze se conecta às instâncias do SQL Classic e Pro, o que causará atrasos durante a configuração e o teste da conexão, bem como no início das sincronizações programadas. O uso de uma instância de SQL sem servidor minimizará o tempo de aquecimento e melhorará a taxa de transferência da consulta, mas poderá resultar em custos de integração ligeiramente mais altos.

### O comando falhou porque o warehouse foi interrompido {#command-failed-because-warehouse-was-stopped}

Se você receber esse erro, verifique se o Databricks warehouse está em execução.

### Serviço: Amazon S3; Código de status: 403; Código de erro: 403 Forbidden {#service-amazon-s3-status-code-403-error-code-403-forbidden}

Se você receber esse erro, consulte [Databricks: Erro forbidden ao acessar dados do S3](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Como faço para atualizar minhas preferências de alerta por e-mail para integrações CDI? {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

Cada integração tem sua própria preferência de notificação. Acesse a página do CDI e selecione o nome da integração que deseja atualizar. Na seção **Preferências de notificação**, é possível atualizar a forma como você recebe alertas referentes à integração selecionada.

## O que acontece se um `UPDATED_AT` futuro for sincronizado com uma integração? {#what-happens-if-a-future-updated_at-gets-synced-with-an-integration}

O CDI usa `UPDATED_AT` para decidir quais dados são novos. Depois que um `UPDATED_AT` futuro for sincronizado, todos os dados anteriores a essa data e hora futuras não serão processados. Para corrigir isso:

1. Corrija `UPDATED_AT`.
2. Remova quaisquer dados antigos que já estejam sincronizados com a Braze.
3. Crie uma nova integração para processar essa tabela novamente.

## Por que "Rows Synced" não corresponde ao número no meu data warehouse? {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

O CDI usa `UPDATED_AT` para decidir quais registros devem ser coletados durante uma sincronização. Dê uma olhada [nesta ilustração]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion#what-gets-synced) para ver como funciona. No início de uma execução de sincronização, o CDI consulta seu data warehouse para obter todos os registros com `UPDATED_AT` posterior ao valor `UPDATED_AT` processado anteriormente. Registros no timestamp exato do limite também podem ser ressincronizados se novas linhas compartilharem esse timestamp. Qualquer registro coletado no momento em que a consulta for executada será sincronizado com a Braze. Aqui estão os casos comuns em que um registro pode não ser sincronizado:

- Você está adicionando registros à tabela com um valor `UPDATED_AT` que já foi processado.
- Você está atualizando os valores de registro depois que eles foram processados por uma sincronização, mas deixando `UPDATED_AT` inalterado.
- Você está adicionando ou atualizando registros enquanto uma sincronização está em andamento. Dependendo de quando a consulta do CDI é executada, pode haver condições de corrida que fazem com que os registros não sejam coletados.

{% alert tip %}
Para evitar esses comportamentos no futuro, recomendamos usar valores `UPDATED_AT` que aumentem monotonicamente e não atualizar a tabela durante a execução da sincronização agendada.
{% endalert %}

## Preciso de valores `UPDATED_AT` majoritariamente distintos para importações grandes do CDI? {#do-i-need-mostly-distinct-updated_at-values-for-large-cdi-imports}

Sim. Para execuções de alto volume (por exemplo, mais de aproximadamente 10 milhões de linhas), certifique-se de que seus dados de origem tenham valores `UPDATED_AT` majoritariamente distintos. Se muitas linhas compartilharem o mesmo timestamp, o CDI terá mais chances de resselecionar linhas nos timestamps de limite em execuções posteriores. Isso pode aumentar sincronizações duplicadas e o consumo de pontos de dados.

Para saber mais sobre o comportamento de limite do CDI, consulte [Evitar ressincronização de linhas com timestamps duplicados]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps).

### Onde devo executar essas verificações SQL? {#where-do-i-run-these-sql-checks}

Execute as verificações diretamente no editor SQL do seu data warehouse, na mesma tabela ou visualização usada pela sua integração CDI:

- Snowflake: **Projects** > **Worksheets** (para saber mais, consulte [Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs))
- Redshift: Query Editor v2 (para saber mais, consulte [Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html))
- BigQuery: BigQuery Studio SQL workspace (para saber mais, consulte [BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction))
- Databricks: SQL editor (SQL warehouse) (para saber mais, consulte [Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/))
- Fabric: SQL query editor

Use este processo antes de ativar ou escalar uma sincronização grande:

1. Identifique a tabela ou visualização de origem do CDI e a janela de sincronização que deseja validar.
2. Abra o editor SQL do seu data warehouse e selecione o mesmo banco de dados e esquema usados pelo CDI. Em seguida, use uma função com acesso de leitura à tabela ou visualização de origem.
3. Execute a consulta de contagem de timestamps distintos para medir quantos valores `UPDATED_AT` distintos existem nessa janela.
4. Execute a consulta que agrupa por `UPDATED_AT` e conta as linhas para encontrar timestamps com contagens de linhas incomumente altas.
5. Se muitas linhas compartilharem timestamps idênticos, ajuste seu processo de ingestão para que lotes consecutivos usem valores `UPDATED_AT` progressivamente mais recentes, ou aumente a precisão do timestamp para que as linhas fiquem mais distribuídas.
6. Execute ambas as consultas novamente até que a concentração seja reduzida e, em seguida, lance ou escale sua sincronização.
7. Após o lançamento, monitore **CDI** > **Sync Log** para verificar se há volume inesperado de ressincronização nos timestamps de limite.

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

Se o seu data warehouse não suportar `LIMIT` (por exemplo, Fabric), use uma sintaxe equivalente como `TOP`.

## Por que uma sincronização do CDI com poucas linhas ainda pode levar vários minutos? {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

Uma sincronização do CDI inclui um período fixo de inicialização antes que o processamento das linhas comece. Como esse tempo de inicialização é semelhante independentemente do tamanho da sincronização, uma sincronização pequena ainda pode levar vários minutos e parecer mais lenta em linhas por minuto. O tempo total de sincronização ainda depende da complexidade da consulta de origem, do formato dos dados e da capacidade disponível no seu data warehouse. Para saber mais, consulte [Integrações de data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Durante uma sincronização, a ordem é preservada se vários registros tiverem o mesmo ID? {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

A ordem de processamento não é 100% previsível. Por exemplo, se houver várias linhas com o mesmo `EXTERNAL_ID` na tabela durante uma sincronização, não é possível garantir qual valor será incluído no perfil final. Se você estiver atualizando o mesmo `EXTERNAL_ID` com atributos diferentes na coluna de carga útil, todas as alterações serão refletidas quando a sincronização for concluída.

## Por que novos usuários não estão sendo criados a partir da minha sincronização do CDI? {#why-are-new-users-not-being-created-from-my-cdi-sync}

Se sua integração do CDI tiver a opção **Atualizar apenas usuários existentes** ativada, apenas os usuários que já existem na Braze são atualizados, e novos usuários não são criados. Isso significa que, se uma linha na sua tabela de sincronização referenciar um `EXTERNAL_ID` que não corresponda a nenhum usuário existente na Braze, essa linha será ignorada.

Para criar novos usuários através do CDI, desative o toggle **Atualizar apenas usuários existentes** nas configurações da sua integração. Acesse **Configurações de dados** > **Ingestão de dados na nuvem** e selecione uma integração.

## Quais são as medidas de segurança do CDI? {#what-are-the-security-measures-for-cdi}

### Nossas medidas {#our-measures}

A Braze tem as seguintes medidas em vigor para o CDI:

- Todas as credenciais são criptografadas em nosso banco de dados, e somente determinados colaboradores têm acesso autenticado a elas.
- Usamos conexões criptografadas para transferir dados aos data warehouses dos clientes.
- Fazemos solicitações aos endpoints da API da Braze usando as mesmas chaves de API e conexões TLS que recomendamos que nossos clientes usem.
- Atualizamos regularmente nossas bibliotecas e aplicamos todos os patches de segurança.

### Suas medidas {#your-measures}

Recomendamos que você e sua equipe configurem as seguintes medidas de segurança do seu lado:

- Restrinja o acesso às credenciais ao mínimo necessário para o funcionamento do CDI. Isso porque precisamos ser capazes de executar select (e count) nas tabelas e visualizações específicas.
- Restrinja os IPs que podem acessar as tabelas aos [IPs da Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views) publicados oficialmente.