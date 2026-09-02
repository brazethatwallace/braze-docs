---
nav_title: Mapeador visual
article_title: "Ingestão de dados na nuvem: Mapeador visual"
description: "Saiba como sincronizar uma tabela ou view do seu data warehouse com o mapeador visual da Ingestão de dados na nuvem, sem escrever SQL."
page_order: 12
page_type: reference
toc_headers: h2
---

# Ingestão de dados na nuvem: Mapeador visual {#cloud-data-ingestion-visual-mapper}

> Esta página explica como usar o mapeador visual para sincronizar uma tabela ou view do seu data warehouse com a Braze sem escrever SQL ou reestruturar seus dados.

{% alert important %}
O mapeador visual está atualmente em beta. Ele está disponível para sincronizações de atributos de usuário de todas as fontes de data warehouse da Ingestão de dados na nuvem, e tipos de sincronização adicionais serão disponibilizados ao longo do beta. Entre em contato com seu gerente de sucesso do cliente ou gerente de conta para obter acesso.
{% endalert %}

Com o mapeador visual, você pode sincronizar uma tabela ou view existente do seu data warehouse sem escrever SQL ou reestruturar seus dados. Em vez de criar uma tabela específica da Braze com as colunas `EXTERNAL_ID`, `UPDATED_AT` e `PAYLOAD`, você mapeia as colunas da sua tabela existente para campos da Braze diretamente no dashboard.

## Pré-requisitos {#prerequisites}

Antes de criar uma sincronização com o mapeador visual, você precisará de:

- Uma fonte de data warehouse ativa na Ingestão de dados na nuvem. Se você ainda não configurou uma, consulte [Integrações com data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).
- O nome da tabela ou view que você deseja sincronizar, conforme aparece no seu data warehouse.
- Uma coluna na sua tabela que contenha um identificador de usuário compatível e uma coluna com um timestamp que a Braze possa usar para sincronização incremental.

{% alert note %}
A Braze executa apenas consultas somente leitura nos seus dados e não modifica suas tabelas subjacentes. Objetos temporários podem ser criados durante a execução da consulta, mas não são persistidos.
{% endalert %}

## Criando uma sincronização com o mapeador visual {#creating-a-sync-with-the-visual-mapper}

### Etapa 1: Configurar a sincronização {#step-1-configure-the-sync}

1. Acesse **Data Settings** > **Cloud Data Ingestion** > **Syncs** e selecione **Create data sync**.
2. Escolha um nome para a sincronização e selecione uma fonte de dados ativa. Somente fontes ativas podem ser usadas.
3. Em **Data destination**, selecione **Braze Data Platform**.
4. Em **Data Type**, selecione **User Attributes**.
5. Selecione **Next: Data definition**.

### Etapa 2: Mapear o esquema de origem {#step-2-map-your-source-schema}

1. Na etapa **Data definition**, selecione **Visual mapper**.
2. No campo **Table**, insira o nome da tabela ou view conforme aparece no seu data warehouse.
3. Selecione **Map source schema**. A Braze lê o esquema da sua tabela ou view e lista todas as colunas com o tipo de dados detectado.

### Etapa 3: Revisar seus mapeamentos {#step-3-review-your-mappings}

A seção **Review mapping** rastreia dois mapeamentos obrigatórios. Sua sincronização não pode ser criada até que ambos estejam completos:

- Mapeie uma coluna para um identificador de usuário compatível: `external_id`, `braze_id`, `email`, `phone` ou um alias de usuário. As opções de identificador aparecem em **Identifiers** no menu suspenso do campo de destino.
- Mapeie uma coluna para `updated_at`. A Braze usa esse timestamp para sincronização incremental em sincronizações recorrentes, onde cada execução importa linhas em que `updated_at` é posterior ao último valor sincronizado.

Para cada coluna restante, você pode:

- **Manter o mapeamento padrão.** Cada coluna é mapeada para um campo da Braze com o mesmo nome. Se o campo ainda não existir no seu espaço de trabalho, ele será marcado como **New attribute** e criado durante a primeira execução da sincronização.
- **Mapear para um campo existente.** Pesquise no menu suspenso do campo de destino para mapear uma coluna para um atributo padrão ou personalizado existente no seu espaço de trabalho.
- **Mapear para um novo campo.** Digite diretamente no menu suspenso do campo de destino para mapear uma coluna para um novo atributo personalizado.
- **Excluir a coluna.** Desmarque a caixa de seleção **Import** para deixar uma coluna fora da sincronização.

{% alert tip %}
Antes de criar um novo atributo, pesquise no menu suspenso de destino por um existente. Por exemplo, se sua tabela tem uma coluna `fav_color`, mas seu espaço de trabalho já rastreia `favorite_color`, considere mapear `fav_color` para `favorite_color` em vez de criar outro atributo.
{% endalert %}

{% alert note %}
Campos cujo tipo de dados não corresponde ao tipo detectado da sua coluna exibem um aviso de **Type mismatch**. Você ainda pode prosseguir, mas valores incompatíveis podem falhar na sincronização como erros de linha. Você pode visualizar erros de linha nos detalhes de execução de uma sincronização.
{% endalert %}

### Etapa 4: Pré-visualizar e validar {#step-4-preview-and-validate}

Selecione **prévia and validate** para executar uma verificação somente leitura na sua tabela ou view. A prévia mostra as primeiras 10 linhas usando os nomes dos campos mapeados e inclui apenas as colunas que você está importando.

### Etapa 5: Finalizar a criação da sincronização {#step-5-finish-creating-the-sync}

1. Na etapa **Notifications**, insira pelo menos um e-mail de contato para notificações de erros de sincronização. Opcionalmente, você pode ativar alertas de **Row Error** (enviados quando uma porcentagem de linhas falha na atualização) e notificações de **Sync success**.
2. Na etapa **agendar/cronograma**, ative **Recurring sync** para executar a sincronização em um cronograma, ou deixe desativado para uma sincronização única.
3. Revise a etapa **Summary**. Ela lista sua configuração, quais atributos são novos versus existentes e quaisquer colunas excluídas da importação devido a problemas de tipo de dados ou às suas seleções.
4. Selecione **Create sync**. Você também pode selecionar **Save as draft** em qualquer etapa para finalizar depois.

## Tratamento de alterações de esquema {#handling-schema-changes}

O mapeador visual verifica o esquema da sua tabela ou view em cada execução de sincronização e responde com base no tipo de alteração:

| Alteração na sua tabela de origem | Comportamento da sincronização |
|---|---|
| Uma nova coluna é adicionada | A sincronização continua, mas novas colunas não são sincronizadas automaticamente. Para incluir uma, edite a sincronização e mapeie-a. |
| Uma coluna mapeada é removida | A execução da sincronização falha e a sincronização é pausada. A alteração de esquema é exibida nos detalhes de execução da sincronização, e seus contatos de notificação recebem um alerta por e-mail. |
| Uma coluna mapeada é renomeada | Tratada como uma coluna removida mais uma nova coluna. |
| O tipo de dados de uma coluna muda | Não é detectada como uma alteração de esquema. Valores incompatíveis são reportados como erros de linha nos logs de sincronização. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tratamento de alterações de esquema" }

Para retomar uma sincronização pausada após a remoção de uma coluna, selecione **Edit sync** e revise seus mapeamentos. A coluna removida é sinalizada e não aparece mais no mapeador. Salvar seus mapeamentos confirma que a sincronização deve continuar sem essa coluna. Alternativamente, se os dados foram movidos para uma coluna diferente, mapeie a nova coluna antes de salvar.

## Perguntas frequentes {#frequently-asked-questions}

### Posso editar meus mapeamentos após a criação de uma sincronização? {#can-i-edit-my-mappings-after-a-sync-is-created}

Sim. Edite a sincronização e selecione **View and edit mapping**. O esquema atual da tabela de origem é carregado, com seus mapeamentos anteriores da criação da sincronização salvos. Você pode editar seus mapeamentos a partir daí.

### Posso transformar meus dados no mapeador visual? {#can-i-transform-my-data-in-the-visual-mapper}

Não. O mapeador visual sincroniza os valores das colunas exatamente como aparecem na sua fonte. Ele não oferece suporte a transformações, lógica condicional ou junções entre tabelas. Para esses casos de uso, use a opção SQL na etapa Data definition para modelar seus dados com uma consulta. Para saber mais, consulte [Ingestão de dados na nuvem: SQL Editor]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sql_editor).

### Minhas sincronizações CDI existentes mudam? {#do-my-existing-cdi-syncs-change}

Não. Sincronizações que usam o formato de tabela existente com as colunas `EXTERNAL_ID`, `UPDATED_AT` e `PAYLOAD` continuam funcionando, e você ainda pode criá-las selecionando **Table** na etapa **Data definition**. Nenhuma migração é necessária.

### Como meu uso da Braze é afetado? {#how-is-my-braze-usage-affected}

Cada coluna que você importa é gravada como uma atualização de atributo, e a cobrança de pontos de dados funciona da mesma forma que outras sincronizações de dados de usuários via CDI. Excluir colunas desnecessárias mantém suas sincronizações eficientes. Para saber mais, consulte [Melhores práticas de Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices).