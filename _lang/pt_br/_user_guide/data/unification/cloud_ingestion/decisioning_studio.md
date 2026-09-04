---
nav_title: Sincronizar dados do Decisioning Studio
article_title: "Sincronizar dados do BrazeAI Decisioning Studio"
description: "Saiba como sincronizar tabelas do data warehouse com o BrazeAI Decisioning Studio usando a ingestão de dados na nuvem."
page_order: 6.5
page_type: reference
toc_headers: h2
---

# Sincronizar dados do BrazeAI Decisioning Studio {#sync-brazeai-decisioning-studio-data}

> Esta página explica como sincronizar dados do seu data warehouse diretamente com o BrazeAI Decisioning Studio™ usando a ingestão de dados na nuvem (CDI).

Com o destino Decisioning Studio da CDI, é possível sincronizar dados do warehouse diretamente com o BrazeAI Decisioning Studio. Os dados dessas sincronizações ficam disponíveis para o Decisioning Studio para ativação, mas seus perfis de usuário e espaços de trabalho da Braze permanecem inalterados.

{% alert important %}
Esse recurso está em acesso antecipado. Entre em contato com seu CSM ou gerente de conta para obter acesso.
{% endalert %}

## Como funciona {#how-it-works}

Ao criar uma sincronização, escolha o Decisioning Studio como destino e escreva uma consulta SQL que retorne os dados que você deseja sincronizar. A CDI executa essa consulta no cronograma que você definir e entrega os resultados como um ativo do Decisioning Studio. Cada sincronização é mapeada para um único ativo, então não é possível apontar mais de uma sincronização para o mesmo ativo.

Diferentemente das sincronizações com a Braze Data Platform, as sincronizações do Decisioning Studio não mapeiam seus dados para perfis de usuário, eventos ou catálogos.

Para outras formas de disponibilizar dados para o Decisioning Studio, consulte [Conectar suas fontes de dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources).

## Pré-requisitos {#prerequisites}

- Acesso à Braze e ao BrazeAI Decisioning Studio.
- Uma fonte de data warehouse ativa na ingestão de dados na nuvem. Se você ainda não configurou uma, consulte [Integrações de data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).
- A tabela ou view que você deseja sincronizar.
- Uma coluna (ou colunas) nessa tabela para usar como chave primária e uma coluna de timestamp que a CDI possa usar para sincronização incremental.

## Criar uma sincronização do Decisioning Studio {#create-a-decisioning-studio-sync}

### Etapa 1: Criar a sincronização e selecionar o destino {#step-1-create-the-sync-and-select-the-destination}

1. Acesse **Data Settings** > **Cloud Data Ingestion** > **Syncs**.
2. Selecione **Create data sync**.
3. Insira um **Integration Name** e selecione sua fonte em **Data sources**.
4. Em **Destination**, defina **Data destination** como **BrazeAI Decisioning Studio™**.
5. Em **Data category**, selecione o tipo de **Decisioning Studio data** que melhor corresponde à sua tabela. Escolha entre **Customer profile**, **Message engagement events**, **Conversion events** ou **Other**. Isso rotula os dados para o Decisioning Studio e não altera a forma como a CDI processa suas linhas.

### Etapa 2: Escrever sua consulta SQL {#step-2-write-your-sql-query}

Na etapa **Data definition**, escreva uma consulta SQL que retorne os dados da tabela ou view que você deseja sincronizar. O resultado da consulta se torna o esquema da sua sincronização.

Você pode usar o Source Explorer para navegar pelas tabelas e views disponíveis, ou o gerador de SQL com IA para obter ajuda na escrita da sua consulta.

Sua consulta deve retornar uma coluna `UPDATED_AT`, pois a CDI usa `UPDATED_AT` para sincronização incremental e rastreamento de alterações. Em cada execução de sincronização, a CDI sincroniza apenas as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Se a coluna de timestamp que você identificou ainda não se chama `UPDATED_AT`, você pode criar um alias na sua consulta:

```sql
SELECT *, LAST_MODIFIED AS UPDATED_AT FROM my_table
```

Para mais informações sobre como `UPDATED_AT` controla a sincronização incremental, incluindo o que acontece quando você move o valor para trás, consulte [Entendendo a coluna UPDATED_AT]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#understanding-the-updated_at-column).

{% alert note %}
Apenas consultas de leitura com uma única instrução são suportadas, incluindo cláusulas `JOIN`. A CDI executa consultas somente leitura e não modifica suas tabelas subjacentes.
{% endalert %}

### Etapa 3: Pré-visualizar e validar sua consulta {#step-3-preview-and-validate-your-query}

Selecione **prévia and validate** para executar sua consulta. A seção **Query prévia (first 10 rows)** mostra as primeiras 10 linhas retornadas da sua fonte, junto com o tipo de dado detectado de cada coluna, para que você possa confirmar que os dados estão corretos antes de continuar.

### Etapa 4: Selecionar uma chave primária {#step-4-select-a-primary-key}

Toda sincronização do Decisioning Studio precisa de uma chave primária ou composta — uma ou mais colunas que identificam cada linha de forma exclusiva. Após a validação ser concluída, abra o menu suspenso **Primary key** e selecione uma coluna para servir como chave primária. Selecionar múltiplas colunas forma uma chave composta.

{% alert tip %}
Uma boa chave primária é única para cada linha, nunca está vazia e é estável entre as execuções de sincronização. Evite valores gerados no momento da consulta, como `UUID()` ou `CURRENT_TIMESTAMP`, pois eles podem causar linhas duplicadas ou descartadas.
{% endalert %}

### Etapa 5: Configurar notificações, cronograma e criar a sincronização {#step-5-set-notifications-schedule-and-create-the-sync}

1. Na etapa **Notifications**, insira um ou mais **Contact Email(s)** para receber notificações de erros de sincronização. Você também pode ativar as notificações de **Row Error** e **Sync success**.
2. Na etapa **agendar/cronograma**, ative **Recurring sync** para executar a sincronização automaticamente em um cronograma. Com **Recurring sync** desativado, a sincronização é executada apenas quando você a dispara, seja manualmente pelo dashboard ou pelo endpoint [Disparar uma sincronização]({{site.baseurl}}/api/endpoints/cdi/post_job_sync).
3. Revise o **Summary** e crie a sincronização.

## Editar uma sincronização {#editing-a-sync}

Ao editar uma sincronização existente, qualquer alteração na sua consulta SQL requer revalidação antes de salvar. Chaves primárias e compostas não podem ser alteradas e devem continuar sendo retornadas.

Alterações válidas entram em vigor na próxima execução de sincronização.

## Lidar com alterações de esquema {#handling-schema-changes}

A CDI lida com alterações de esquema da fonte de forma aditiva. Em cada execução de sincronização, a CDI compara o esquema da sua fonte com o ativo existente do Decisioning Studio e adiciona quaisquer novas colunas, preservando as que já existem.

| Alteração na sua tabela de origem | Comportamento da sincronização |
|---|---|
| Uma nova coluna é adicionada | A CDI adiciona a coluna ao ativo do Decisioning Studio. Linhas entregues antes da existência da coluna mostram `null` para ela. |
| Uma coluna é removida | A CDI para de atualizar essa coluna, mas a coluna e seus dados existentes permanecem no ativo. As outras colunas continuam sendo sincronizadas. |
| Uma coluna é renomeada | Tratada como uma coluna removida mais uma nova coluna. A coluna original permanece no ativo e a nova coluna é adicionada. |
| O tipo de dado de uma coluna muda | A CDI converte os valores quando possível. Linhas que não podem ser convertidas são reportadas como erros de linha nos detalhes de execução da sincronização. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lidar com alterações de esquema" }

Quando a CDI detecta uma alteração de esquema, ela é exibida nos detalhes de execução da sincronização e na página de edição da sincronização, e seus contatos de notificação recebem um alerta por e-mail. Para alterar quais colunas são entregues, atualize sua consulta SQL e revalide.