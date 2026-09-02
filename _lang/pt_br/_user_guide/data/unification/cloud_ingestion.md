---
nav_title: Ingestão de dados na nuvem
article_title: Ingestão de Dados na Nuvem da Braze
alias: /cloud_ingestion/
description: "Este artigo de referência cobre as fontes de Ingestão de Dados na Nuvem da Braze e recomendações de configuração de dados."
page_order: 1
toc_headers: h2
---

# Ingestão de Dados na Nuvem da Braze {#braze-cloud-data-ingestion}

> A Ingestão de Dados na Nuvem (CDI) da Braze permite que você configure uma conexão direta da sua solução de armazenamento de dados para sincronizar dados relevantes de usuários e outros dados não relacionados a usuários com a Braze. Esses dados podem ser usados para personalização ou segmentação para potencializar seus casos de uso de marketing. A integração flexível da Ingestão de Dados na Nuvem suporta estruturas de dados complexas, incluindo JSON aninhado e arrays de objetos.

## Como funciona {#how-it-works}

Com a Ingestão de Dados na Nuvem (CDI) da Braze, você configura uma integração entre sua instância de data warehouse e o espaço de trabalho da Braze para sincronizar dados de forma recorrente. Essa sincronização é executada conforme um cronograma que você define, e cada integração pode ter um cronograma diferente. As sincronizações podem ocorrer com frequência de até 15 minutos ou com pouca frequência, como uma vez por mês. Se você precisar que as sincronizações ocorram com mais frequência do que a cada 15 minutos, entre em contato com seu CSM ou considere usar chamadas da REST API para ingestão de dados em tempo real.

As integrações de armazenamento de arquivos do Amazon S3 são orientadas a eventos. A Braze ingere novos arquivos quando as notificações do S3/SQS chegam. Para detalhes de configuração, consulte [Integrações de armazenamento de arquivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).

{% alert note %}
A frequência de sincronização no dashboard controla com que frequência a Braze executa uma sincronização (por exemplo, opções como execuções de hora em hora ou mais frequentes dentro de uma hora). Ela não define um intervalo personalizado maior que uma hora entre as execuções. Para executar uma sincronização fora da cadência programada — como sob demanda após a conclusão do carregamento do seu warehouse — use o endpoint [Disparar uma sincronização]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) com o ID da sua integração.
{% endalert %}

Quando uma sincronização é executada, a Braze se conecta diretamente à sua instância de data warehouse, recupera todos os novos dados da tabela especificada e atualiza os dados correspondentes no seu dashboard da Braze. Cada vez que a sincronização é executada, quaisquer dados atualizados são refletidos na Braze.

### Encontrando o ID da sua integração {#finding-your-integration-id}

Você pode encontrar o ID da sua integração na URL ao visualizar uma integração no dashboard da Braze. Navegue até **Data Settings** > **Cloud Data Ingestion** e selecione uma integração. O ID da integração aparece na URL no formato `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Por exemplo, se a sua URL for `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`, o ID da sua integração é `abc123xyz`. Você pode usar esse ID ao fazer chamadas de API para disparar sincronizações ou verificar o status da sincronização.

## Casos de uso {#use-cases}

Com os recursos de Ingestão de Dados na Nuvem da Braze, você pode:

- Criar uma integração simples diretamente do seu data warehouse ou solução de armazenamento de arquivos para a Braze em apenas alguns minutos.
- Sincronizar dados de usuários com segurança, incluindo atributos, eventos e compras do seu data warehouse para a Braze.
- Fechar o ciclo de dados com a Braze combinando a Ingestão de Dados na Nuvem com Currents ou Snowflake Data Sharing.

Além disso, as [Fontes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) são uma alternativa de cópia zero. Você pode fazer com que a Braze consulte diretamente seu data warehouse ou solução de armazenamento de arquivos para construir segmentos CDI &#8212;tudo sem copiar os dados subjacentes para a Braze.

## Fontes de dados compatíveis {#supported-data-sources}

A Ingestão de Dados na Nuvem pode sincronizar dados de:

   - Amazon Redshift
   - Databricks
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Tipos de dados compatíveis {#supported-data-types}

A Ingestão de Dados na Nuvem é compatível com os seguintes tipos de dados:

### Dados de usuários {#user-data}
- Atributos de usuário, incluindo:
   - Atributos personalizados aninhados
   - Arrays de objetos
   - Status de inscrição
- Eventos personalizados
- Eventos de compra
- Solicitações de exclusão de usuários

### Objetos que não são de usuários {#non-user-objects}
- Itens de catálogo

### Envio de mensagens com cópia zero {#zero-copy-messaging}
- Fontes conectadas

## Identificadores de usuário para ingestão de dados {#user-identifiers-for-data-ingestion}

Ao sincronizar dados de usuários por meio da Ingestão de Dados na Nuvem, você pode identificar usuários usando um ou mais dos seguintes tipos de identificadores. Cada linha na sua tabela de origem deve conter um valor para apenas um tipo de identificador por vez, mas sua tabela pode incluir colunas para um, dois, três, quatro ou todos os cinco tipos de identificadores.

| Identificador | Descrição |
|------------|-------------|
| `EXTERNAL_ID` | O ID externo que identifica o perfil de usuário a ser criado ou atualizado. Deve corresponder ao valor `external_id` usado na Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo, e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
| `BRAZE_ID` | O identificador de usuário da Braze gerado pelo SDK da Braze. Não é possível criar novos usuários usando um Braze ID por meio da Ingestão de Dados na Nuvem. Para criar novos usuários, especifique um ID externo de usuário ou um alias de usuário. |
| `EMAIL` | O endereço de e-mail do usuário. Se existirem vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade nas atualizações. Se você incluir e-mail e telefone, o e-mail será usado como identificador principal. |
| `PHONE` | O número de telefone do usuário. Se existirem vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identificadores de usuário para ingestão de dados" }

Para informações detalhadas sobre a configuração de colunas da tabela e os requisitos de formatação da carga útil, consulte [Configuração de tabelas para Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

Para instruções de configuração específicas por fonte e exemplos de SQL, consulte [Integrações com data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Uso de pontos de dados {#data-point-usage}

Para clientes com cobrança baseada em pontos de dados, a cobrança de pontos de dados da Ingestão de Dados na Nuvem é equivalente à cobrança por atualizações feitas pelo [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Consulte [Pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points) para saber mais.

{% alert important %}
A Ingestão de Dados na Nuvem da Braze conta para o limite de frequência disponível. Portanto, se você estiver enviando dados por outro método, o limite de frequência será combinado entre a API da Braze e a Ingestão de Dados na Nuvem.
{% endalert %}

## Limitações do produto {#product-limitations}

| Limitação | Descrição |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integrações | Não há limite para a quantidade de integrações que você pode configurar. No entanto, você pode configurar apenas uma integração por tabela ou visualização. |
| Número de linhas | Por padrão, cada execução pode sincronizar até 500 milhões de linhas. Sincronizações com mais de 500 milhões de novas linhas são interrompidas. Se você precisar de um limite maior, entre em contato com seu CSM ou com o suporte da Braze. |
| Atributos por linha | Cada linha deve conter um único ID de usuário e um objeto JSON com até 250 atributos. Cada chave no objeto JSON conta como um atributo (ou seja, um array conta como um atributo). |
| Tamanho da carga útil | Cada linha pode conter uma carga útil de até 1 MB. Cargas úteis maiores que 1 MB são rejeitadas, e o erro "Payload was greater than 1MB" é registrado no log de sincronização junto com o ID externo associado e a carga útil truncada. |
| Tipo de dados | Você pode sincronizar atributos de usuário, eventos e compras por meio da Ingestão de Dados na Nuvem. |
| Região da Braze | Este produto está disponível em todas as regiões da Braze. Qualquer região da Braze pode se conectar a qualquer região de fonte de dados. |
| Região de origem | A Braze se conecta ao seu data warehouse ou ambiente na nuvem em qualquer região ou provedor de nuvem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitações do produto" }