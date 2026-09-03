---
nav_title: Sincronizar registros e observabilidade
article_title: Sincronizar registros e observabilidade
page_order: 8
page_type: reference
description: "Esta página fornece uma visão geral dos recursos de observabilidade disponíveis no CDI."
---

# Sincronizar registros e observabilidade {#sync-logs-and-observability}

> O dashboard de **Sync Log** da ingestão de dados na nuvem (CDI) permite monitorar todos os dados processados pelo CDI, verificar se os dados foram sincronizados com sucesso e diagnosticar quaisquer problemas com dados "incorretos" ou ausentes.

Para acessar os registros de sincronização, acesse **Configurações de dados** > **Cloud Data Ingestion** e selecione a guia **Sync Log**.

<!-- support-analyzer-phase2:cdi_updated_at_row_sync -->
{% alert note %}
Se as contagens de linhas do data warehouse não corresponderem a **Rows Synced** ou se você vir execuções com **Partial Success**, abra o **Run ID** no Sync Log e revise os valores de **Error reason** no nível da linha. O CDI seleciona linhas usando `UPDATED_AT` — linhas com timestamps já processados, `UPDATED_AT` inalterado após edições ou gravações durante uma sincronização ativa podem ser ignoradas. Para casos comuns, consulte [Por que "Rows Synced" não corresponde ao número no meu data warehouse?]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/faqs#why-doesnt-rows-synced-match-the-number-in-my-warehouse) e [Perguntas frequentes sobre ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/faqs).
{% endalert %}

## Entendendo o dashboard de Registro de Sincronização {#understanding-the-sync-log-dashboard}

A página principal de **Registro de Sincronização** fornece uma visão geral de alto nível de todas as suas execuções de sincronização, incluindo uma visão geral das sincronizações recentes por seu status atual ou final.

* **Running:** Trabalhos de sincronização que estão em andamento.
* **Success:** Trabalhos de sincronização que foram concluídos e todas as linhas foram processadas com sucesso.
* **Partial Success:** Trabalhos de sincronização que foram concluídos, mas uma ou mais linhas encontraram um erro.
* **Error:** Trabalhos de sincronização que não foram concluídos.
* **Limit Exceeded:** Trabalhos de sincronização que pararam de processar porque um limite de dados foi excedido.

![Um exemplo de registros de sincronização com 6.576 sucessos totais.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Os registros de sincronização também fornecem os seguintes detalhes para cada sincronização:

* **Sync name:** O nome da configuração de sincronização.
* **Run ID:** Um identificador único para uma execução específica da sincronização. Selecione esse ID para ver mais detalhes ou para referenciar uma execução de sincronização com o suporte da Braze.
* **Status:** O status da execução (success, partial success, error, running).
* **New rows read from source:** O número de novas linhas extraídas do seu data warehouse para esta execução.
* **Results:** Um detalhamento de quantas linhas tiveram sucesso ou falharam dentro da execução.
* **Last "UPDATED_AT":** O timestamp do registro mais recente processado nesta execução de sincronização.
* **Run start time:** Quando o trabalho de sincronização começou.
* **Run duration:** O tempo total que o trabalho de sincronização levou para ser concluído.

### Retenção de dados {#data-retention}

Os dados do registro de sincronização, incluindo todas as cargas úteis em nível de linha e detalhes de erros, são retidos por até **30 dias**. Registros com mais de 30 dias são automaticamente removidos.

Metadados de execução de sincronização, como o número de linhas processadas, são retidos por pelo menos 12 meses.

### Filtrando registros de sincronização {#filtering-sync-logs}

Você pode filtrar a tabela de registros de sincronização para encontrar execuções específicas. Os filtros disponíveis incluem:

* **Job start date:** Selecione um intervalo predefinido (como "Last 30 days") ou um intervalo de datas personalizado.
* **Status:** Filtre por um ou mais status de sincronização (como exibir apenas os status **Error** e **Partial success**).
* **Sync name:** Pesquise por uma sincronização específica pelo nome.

Para investigar uma sincronização específica, selecione o **Run ID** relevante na tabela de registros de sincronização. Na página **Run details**, você encontrará um registro granular, linha por linha, da sincronização.

### Visão geral da execução {#run-overview}

Esta seção resume a execução selecionada, incluindo horário de início, horário de término, duração e o número total de linhas lidas da fonte. Ela também fornece uma contagem de quantas linhas tiveram sucesso e quantas resultaram em erro.

### Linhas processadas nesta execução {#rows-processed-in-this-run}

Esta tabela fornece visibilidade em nível de linha dos dados processados durante a sincronização, permitindo que você valide registros individuais.

* **Search:** Você pode pesquisar por um usuário específico nos resultados da execução usando a barra **Search by user ID**.
* **Detalhes disponíveis:**
  * **UPDATED_AT:** O timestamp da coluna `UPDATED_AT` para aquela linha específica.
  * **ID:** Os identificadores do usuário (como `external_id`, `email` ou `alias_name`) usados para associar o registro a um perfil de usuário da Braze.
  * **Status:** O status de processamento individual para aquela linha (**Success** ou **Error**).
  * **Source payload:** Um link para visualizar a carga útil dos dados.
  * **Error reason:** Se o status for **Error**, esta coluna fornece uma mensagem explicando por que a linha falhou ao sincronizar.

#### Visualizando cargas úteis {#viewing-payloads}

Para ver os dados exatos enviados para a Braze para uma linha específica, selecione **View payload** na coluna **Source** payload. Isso exibe a carga útil JSON bruta que foi processada para aquele usuário.

#### Exportando registros de sincronização {#exporting-sync-logs}

Selecione **Export rows** para exportar os registros em nível de linha de uma execução de sincronização. Em seguida, escolha exportar por:

* **Rows with errors:** Baixa um arquivo contendo apenas as linhas que tiveram status **Error**.
* **All rows:** Baixa um arquivo contendo todas as linhas processadas na execução.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Exporting sync logs for all rows' %}

Os registros não podem ser exportados diretamente do dashboard. Após a exportação ser gerada, você receberá um e-mail com um link para baixar o arquivo de exportação do registro.

## Notificações {#notifications}

Você pode configurar notificações por e-mail para se manter informado sobre o status das suas sincronizações de CDI. Essas configurações são definidas quando você cria uma sincronização e podem ser atualizadas a qualquer momento.

### Notificações de erro {#error-notifications}

É necessário informar pelo menos um endereço de e-mail de contato para receber notificações de erros no nível da sincronização. Esses alertas são enviados quando um trabalho de sincronização inteiro falha ao ser executado ou concluído, ou se a sincronização encontra um erro que exige intervenção do usuário para correção, como credenciais expiradas ou uma tabela de origem ausente.

As notificações adicionais incluem:

- **Erro de linha:** Receba alertas quando uma determinada porcentagem de linhas falhar ao ser atualizada em uma sincronização.
- **Limite de falha (%):** Especifique a porcentagem de falhas de linha que deve disparar um alerta. Por exemplo, definir esse valor como **1** enviaria uma notificação se 1% ou mais das linhas em uma execução de sincronização resultarem em erro.
- **Sincronização bem-sucedida:** Receba uma notificação após a conclusão bem-sucedida de uma sincronização.
- **Alertar mesmo se nenhuma linha for alterada:** Receba uma notificação mesmo quando uma execução de sincronização bem-sucedida processar zero linhas novas ou atualizadas.