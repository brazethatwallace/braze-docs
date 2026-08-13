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

## Entendendo o dashboard de Sync Log {#understanding-the-sync-log-dashboard}

A página principal de **Sync Log** fornece uma visão geral de alto nível de todas as suas execuções de sincronização, incluindo uma visão geral das sincronizações recentes pelo seu status atual ou final.

* **Running:** Trabalhos de sincronização que estão atualmente em andamento.
* **Success:** Trabalhos de sincronização que foram concluídos e todas as linhas foram processadas com sucesso.
* **Partial Success:** Trabalhos de sincronização que foram concluídos, mas uma ou mais linhas encontraram um erro.
* **Error:** Trabalhos de sincronização que falharam ao concluir.
* **Limit Exceeded:** Trabalhos de sincronização que pararam de processar porque um limite de dados foi excedido.

![Um exemplo de registros de sincronização com 6.576 sucessos totais.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Os registros de sincronização também fornecem os seguintes detalhes para cada sincronização:

* **Nome da sincronização:** O nome da configuração de sincronização.
* **ID da execução:** Um identificador único para uma execução específica da sincronização. Selecione este ID para ver mais detalhes ou para referenciar uma execução de sincronização com o suporte da Braze.
* **Status:** O status da execução (success, partial success, error, running).
* **Novas linhas lidas da origem:** O número de novas linhas extraídas do seu data warehouse para esta execução.
* **Resultados:** Uma análise de quantas linhas foram bem-sucedidas ou falharam durante a execução.
* **Último `UPDATED_AT`:** O timestamp do registro mais recente processado nesta execução de sincronização.
* **Hora de início da execução:** Quando o trabalho de sincronização começou.
* **Duração da execução:** O tempo total que o trabalho de sincronização levou para ser concluído.

### Retenção de dados {#data-retention}

Os dados do registro de sincronização, incluindo todas as cargas úteis em nível de linha e detalhes de erro, são retidos por até **30 dias**. Registros com mais de 30 dias são automaticamente excluídos.

Metadados da execução de sincronização, como o número de linhas processadas, são retidos por pelo menos 12 meses.

### Filtrando registros de sincronização {#filtering-sync-logs}

Você pode filtrar a tabela de registros de sincronização para encontrar execuções específicas. Os filtros disponíveis incluem:

* **Data de início do trabalho:** Selecione um intervalo predefinido (como "Últimos 30 dias") ou um intervalo de datas personalizado.
* **Status:** Filtre por um ou mais status de sincronização (como mostrar apenas os status **Error** e **Partial Success**).
* **Nome da sincronização:** Pesquise por uma sincronização específica pelo seu nome.

Para investigar uma sincronização específica, selecione o **Run ID** relevante na tabela de registros de sincronização. Na página **Run details**, você encontrará um registro granular, linha por linha, da sincronização.

### Visão geral da execução {#run-overview}

Esta seção resume a execução selecionada, incluindo seu horário de início, horário de término, duração e o número total de linhas lidas da origem. Ela também fornece uma contagem de quantas linhas foram bem-sucedidas e quantas resultaram em erro.

### Linhas processadas nessa execução {#rows-processed-in-this-run}

Esta tabela fornece visibilidade em nível de linha sobre os dados processados durante a sincronização, permitindo que você valide registros individuais.

* **Pesquisar:** Você pode pesquisar por um usuário específico nos resultados da execução usando a barra **Search by user ID**.
* **Detalhes disponíveis:**
  * **`UPDATED_AT`:** O timestamp da coluna `UPDATED_AT` para essa linha específica.
  * **ID:** Os identificadores de usuário (como `external_id`, `email` ou `alias_name`) usados para corresponder o registro a um perfil de usuário da Braze.
  * **Status:** O status de processamento individual para essa linha (**Success** ou **Error**).
  * **Carga útil da origem:** Um link para visualizar a carga útil de dados.
  * **Razão do erro:** Se o status for **Error**, esta coluna fornece uma mensagem explicando por que a linha falhou na sincronização.

#### Visualizando cargas úteis {#viewing-payloads}

Para ver os dados exatos enviados à Braze para uma linha específica, selecione **View payload** na coluna de carga útil **Source**. Isso exibe a carga útil JSON bruta que foi processada para esse usuário.

#### Exportando registros de sincronização {#exporting-sync-logs}

Selecione **Export rows** para exportar os registros em nível de linha para uma execução de sincronização. Em seguida, escolha exportar por:

* **Linhas com erros:** Baixa um arquivo contendo apenas as linhas que tiveram um status de **Error**.
* **Todas as linhas:** Baixa um arquivo contendo todas as linhas processadas na execução.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Exporting sync logs for all rows' %}

Os registros não podem ser exportados diretamente do dashboard. Após a exportação ser gerada, você receberá um e-mail com um link para baixar o arquivo de exportação do registro.

## Notificações {#notifications}

Você pode configurar notificações por e-mail para se manter informado sobre o status das suas sincronizações CDI. Essas configurações são definidas quando você cria uma sincronização e podem ser atualizadas a qualquer momento.

### Notificações de erro {#error-notifications}

É necessário pelo menos um endereço de e-mail de contato para receber notificações sobre erros em nível de sincronização. Esses alertas são enviados quando um trabalho de sincronização inteiro falha ao ser executado ou concluído, ou se a sincronização encontra um erro que requer intervenção do usuário para ser corrigido, como credenciais expiradas ou uma tabela de origem ausente.

Notificações adicionais incluem:

- **Erro na linha:** Receba alertas quando uma certa porcentagem de linhas falhar ao atualizar dentro de uma sincronização.
- **Limite de falhas (%):** Especifique a porcentagem de falhas de linha que deve disparar um alerta. Por exemplo, definir isso para **1** enviaria uma notificação se 1% ou mais das linhas em uma execução de sincronização resultarem em erro.
- **Sucesso da sincronização:** Receba uma notificação após a conclusão bem-sucedida de uma sincronização.
- **Alerta mesmo se nenhuma linha mudar:** Receba uma notificação mesmo quando uma execução de sincronização bem-sucedida processar zero linhas novas ou atualizadas.