---
nav_title: LiveRamp
article_title: LiveRamp
description: "Saiba como conectar a LiveRamp e a Braze por meio do Snowflake Data Sharing ou do Braze Currents para criar campanhas de marketing altamente personalizadas e relevantes."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# LiveRamp

> Saiba como conectar a LiveRamp e a Braze por meio do Snowflake Data Sharing ou do Braze Currents para criar campanhas de marketing altamente personalizadas e relevantes, reduzindo o tempo até os insights, quebrando silos de dados e otimizando o engajamento dos clientes. Essa integração aprimora o marketing baseado em dados, fornecendo insights acionáveis baseados em pessoas e consolidando pontos de contato com o consumidor para uma melhor segmentação do público e campanhas oportunas.

## Opções de integração {#integration-options}

Você pode integrar a LiveRamp com a Braze usando um dos dois métodos:

- **Snowflake Data Sharing:** compartilhe dados da Braze diretamente por meio dos Secure Data Shares do Snowflake sem mover dados. Esse método aproveita benchmarks fornecidos pelo Snowflake para ajudar a refinar suas estratégias de marketing em relação aos padrões do setor.
- **Braze Currents:** envie dados de engajamento em tempo real e em nível de evento da Braze para um destino de armazenamento em nuvem (Amazon S3, Google Cloud Storage ou Microsoft Azure Blob Storage), depois carregue esses dados no seu data warehouse e use os recursos de resolução de identidade da LiveRamp no seu ambiente de nuvem.

{% alert important %}
Os [Secure Data Shares](https://docs.snowflake.com/en/user-guide/data-sharing-intro) do Snowflake não transferem dados entre a LiveRamp, o Snowflake e a Braze. Os dados são compartilhados apenas por meio dos serviços e do armazenamento de metadados do Snowflake, o que significa que nenhum dado é copiado e não há cobranças adicionais de armazenamento. O acesso aos dados compartilhados é controlado e governado usando os controles de acesso da sua conta Snowflake.
{% endalert %}

## Casos de uso {#use-cases}

Essa integração suporta os seguintes casos de uso em todos os ambientes de data warehouse:

- **Minimização de dados:** as soluções da LiveRamp usam recursos de compartilhamento seguro de dados ou resolução de identidade nativa na nuvem para ler tabelas diretamente do seu data warehouse. Nenhum dado é movido até o ponto de entrega ao parceiro downstream.
- **Ativação segura de dados primários:** ao usar a resolução de identidade da LiveRamp, o aplicativo de ativação da LiveRamp utiliza apenas as tabelas baseadas em RampID no seu data warehouse, de modo que as IPI nunca precisam sair do seu ambiente.
- **Acelerar o TTL:** ao resolver os dados para o RampID diretamente no seu ambiente, a entrega a um destino final pode ocorrer em questão de horas, em comparação com vários dias quando se usa a abordagem mais tradicional baseada em arquivos da LiveRamp. Isso aumenta muito a capacidade de otimizar o desempenho da campanha em tempo hábil.
- **Economia operacional:** por meio do compartilhamento seguro de dados ou da resolução de identidade nativa na nuvem, você economiza tempo e dinheiro quando comparado à coordenação da saída de arquivos para a LiveRamp ou diretamente para qualquer destino final.

## Integração com Snowflake Data Sharing {#integration-with-snowflake-data-sharing}

As etapas a seguir descrevem como integrar a LiveRamp com a Braze por meio do Snowflake Data Sharing.

### Pré-requisitos {#prerequisites}

| Pré-requisito       | Descrição                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Conta Snowflake | Você precisa de uma conta do Snowflake com permissões de nível de administrador.                                                                                                                                      |
| Conta LiveRamp  | Entre em contato com sua equipe de contas LiveRamp ou [snowflake@liveramp.com](mailto:snowflake@liveramp.com) para discutir os aplicativos LiveRamp necessários dentro do Snowflake.                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

### Etapa 1: Solicite um compartilhamento de dados da Braze {#step-1-request-a-data-share-from-braze}

Primeiro, entre em contato com seu gerente de conta da Braze ou gerente de sucesso do cliente para comprar um Conector de Compartilhamento de Dados Snowflake para sua conta Braze. Quando você solicitar um compartilhamento de dados, a Braze provisionará o compartilhamento a partir do(s) espaço(s) de trabalho em que o compartilhamento foi adquirido. Depois que o compartilhamento é provisionado, todos os dados ficam imediatamente acessíveis a partir da sua instância do Snowflake na forma de um compartilhamento de dados de entrada. Quando o compartilhamento estiver visível em sua instância, crie um banco de dados a partir do compartilhamento para poder ver e consultar as tabelas.

Para obter um passo a passo completo, consulte o [guia de integração do Snowflake com a Braze]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### Etapa 2: Configure o app LiveRamp no Snowflake {#step-2-set-up-the-liveramp-app-in-snowflake}

Os recursos de tradução e resolução de identidade estão disponíveis no Snowflake por meio do app nativo de Resolução e Tradução de Identidade da LiveRamp, que cria um compartilhamento para a sua conta, abrindo uma visualização para consultar o conjunto de dados de referência a partir do seu próprio ambiente do Snowflake.

Para configurar o app nativo, siga estas etapas na documentação da LiveRamp: [Configure o app nativo da LiveRamp no Snowflake](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). Quando terminar, passe para a próxima etapa.

### Etapa 3: Crie uma tabela de dados {#step-3-create-a-data-table}

{% alert warning %}
Antes de preparar qualquer tabela baseada em IPI, certifique-se de entender o [filtro de privacidade da LiveRamp](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html), que é executado durante os trabalhos para garantir que as colunas de atributos (não identificadores) em suas tabelas de entrada não contenham valores muito exclusivos. Isso é fundamental para manter a privacidade do consumidor e evitar a reidentificação.
{% endalert %}

Em seguida, crie uma tabela de dados com o [formato necessário](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) que será chamada no app nativo da LiveRamp. Consulte as categorias a seguir para determinar quais de seus identificadores são elegíveis para resolução:

| Tipo de identificador | Descrição  |
|-----------------|--------------|
| IPI completa        | As informações de identificação pessoal (IPI) incluem o nome, o endereço postal, o e-mail e o número de telefone do usuário. **Nota:** nem todos os identificadores são necessários para cada registro. |
| Apenas e-mail      | Os endereços de e-mail do usuário, como `alex-lee@email.com`. |
| Dispositivo          | Inclui cookies de terceiros, IDs de publicidade móvel (MAIDs), IDs de TV conectada (CTV IDs) e RampIDs (resolvidos para um RampID de residência). |
| CIDs            | Esses são identificadores de um parceiro de plataforma ou de uma sincronização de identidade com a LiveRamp, como seu ID de cliente interno. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Crie uma tabela de dados" }

#### Identificadores da Braze {#braze-identifiers}

Os registros de eventos da Braze contêm identificadores que podem ser usados no app nativo da LiveRamp. Para obter uma lista completa dos identificadores disponíveis para cada tipo de evento, baixe o [Braze Event Schemas and Identifiers](/docs/assets/download_file/data-sharing-raw-table-schemas.txt).

| Tipo de identificador | Descrição  |
|-----------------|--------------|
| `AD_ID` | IDs de publicidade, como `ios_idfa`, `google_ad_id`, `roku_ad_id`, capturados em tipos de eventos específicos, que podem ser usados em conjunto com os serviços de resolução de dispositivos da LiveRamp. Por padrão, os IDs de publicidade não são coletados&#8212;no entanto, você pode ativar o rastreamento seguindo a [documentação da Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default). |
| `EMAIL_ADDRESS`   | Endereço de e-mail que pode ser usado em conjunto com os serviços de resolução somente por e-mail da LiveRamp |
| `TO_PHONE_NUMBER` | Número de telefone, que pode ser usado em conjunto com os serviços de resolução de IPI da LiveRamp. |
| `EXTERNAL_USER_ID` | O ID externo associado a um usuário, que pode ser usado em conjunto com os serviços de resolução de dispositivos (CID) da LiveRamp. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identificadores da Braze" }

{% alert important %}
O uso de qualquer identificador personalizado específico do cliente ou da marca no aplicativo da LiveRamp requer uma [sincronização de identidade com a LiveRamp](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html).
{% endalert %}

### Etapa 4: Defina suas variáveis {#step-4-set-your-variables}

Em seguida, defina suas variáveis para o trabalho na planilha de etapas de execução fornecida no app. Isso inclui detalhes como o banco de dados de destino, as tabelas associadas (dados de entrada, métricas, registro) e a definição do nome da tabela de saída. Para obter um passo a passo completo, consulte [LiveRamp: Especifique as variáveis](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727).

### Etapa 5: Crie a tabela de metadados para resolução de IPI {#step-5-create-the-metadata-table-for-pii-resolution}

Agora que suas variáveis estão definidas, crie a tabela de metadados para a resolução de IPI. Isso fornecerá detalhes sobre o tipo de trabalho específico a ser executado com base na categoria de identificadores envolvidos. Para obter um passo a passo completo, consulte [LiveRamp: Crie a tabela de metadados](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### Etapa 6: Execute a operação de resolução de identidade {#step-6-perform-the-identity-resolution-operation}

Por fim, execute a operação de resolução de identidade. Para obter um passo a passo completo, consulte [LiveRamp: Execute a operação de resolução de identidade](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

{% tabs local %}
{% tab example input %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab example output %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Próximas etapas {#next-steps}

Com seus dados agora pseudonimizados para sua codificação dedicada de RampID, você pode compartilhar as tabelas baseadas em RampID com o aplicativo Managed Activation da LiveRamp para simplificar o atendimento aos seus principais parceiros de plataforma de publicidade. O aplicativo Activation inclui uma interface amigável para o usuário comercial, com recursos de segmentação adicional e seleção/configuração de parceiros de destinos downstream. Para mais detalhes sobre o aplicativo, entre em contato com sua equipe de contas LiveRamp ou [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Integração com Braze Currents {#integration-with-braze-currents}

O Braze Currents fornece um fluxo em tempo real de eventos de engajamento que podem ser exportados para destinos de armazenamento em nuvem. Você pode usar o Currents com a LiveRamp para enviar dados de eventos da Braze para o armazenamento em nuvem, carregá-los no seu data warehouse e, em seguida, aplicar os recursos de resolução de identidade da LiveRamp no seu ambiente de nuvem.

### Como funciona {#how-it-works}

1. **A Braze fornece dados em tempo real em nível de evento:** a Braze envia dados brutos de engajamento para o seu data warehouse ou destino de armazenamento por meio do Currents.
2. **A LiveRamp conecta os dados ao RampID:** a LiveRamp remove as IPI e conecta seus dados ao identificador universal da sua marca, o RampID.
3. **Ative e meça:** dados primários da Braze podem ser combinados com outros dados de terceiros para criar segmentos de clientes mais precisos para publicidade. Públicos pseudonimizados são enviados para a LiveRamp para ativação downstream em parceiros de plataforma, e a LiveRamp recebe dados de exposição de anúncios dos parceiros para mensuração em nível de pessoa.

### Plataformas de nuvem suportadas {#supported-cloud-platforms}

Os recursos de resolução de identidade da LiveRamp estão disponíveis nos seguintes ambientes de nuvem:

| Plataforma | Solução LiveRamp | Descrição |
|----------|------------------|-------------|
| Google BigQuery | [LiveRamp Embedded Identity in BigQuery](https://docs.liveramp.com/identity/en/liveramp-embedded-identity-in-bigquery.html#liveramp-embedded-identity-in-bigquery) | Realize a resolução de identidade e a tradução de RampID nativamente no BigQuery usando o BigQuery Entity Resolution Framework. Carregue os dados do Currents do Google Cloud Storage no BigQuery antes de executar a resolução de identidade. |
| AWS | [LiveRamp Identity in AWS](https://docs.liveramp.com/identity/en/liveramp-identity-in-aws.html#liveramp-identity-in-aws) | Resolva identificadores para RampIDs e realize a tradução de identidade usando o AWS Entity Resolution ou por meio do Amazon Data Exchange (ADX) standalone. Carregue os dados do Currents do Amazon S3 antes de executar a resolução de identidade. |
| Microsoft Azure | Entre em contato com a LiveRamp | O Azure Blob Storage é suportado como destino do Currents. Entre em contato com seu representante LiveRamp para soluções de resolução de identidade específicas para o Azure. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Plataformas de nuvem suportadas" }

{% alert note %}
O LiveRamp Embedded Identity in BigQuery está atualmente em beta. Entre em contato com [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com) para discutir a participação no programa.
{% endalert %}

### Pré-requisitos

| Pré-requisito | Descrição |
|-------------|-------------|
| Braze Currents | Para enviar dados de eventos para o armazenamento em nuvem, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) configurado para sua conta. |
| Conta de armazenamento em nuvem | Você precisa de uma conta de armazenamento em nuvem (Amazon S3, Google Cloud Storage ou Microsoft Azure Blob Storage) para onde o Currents envia seus dados. |
| Conta LiveRamp | Entre em contato com sua equipe de contas LiveRamp ou [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com) para configurar a resolução de identidade da LiveRamp no seu ambiente de nuvem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

### Etapa 1: Configure o Braze Currents {#step-1-set-up-braze-currents}

Primeiro, configure o Braze Currents para enviar seus dados de engajamento para o destino de armazenamento em nuvem. Consulte os guias a seguir com base na plataforma escolhida:

- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)

Configure o Currents para exportar os eventos que contêm os identificadores necessários para a resolução de identidade da LiveRamp. Para obter uma lista completa dos identificadores disponíveis para cada tipo de evento, consulte os glossários de [eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) e [eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

### Etapa 2: Configure a resolução de identidade da LiveRamp {#step-2-set-up-liveramp-identity-resolution}

Depois que o Currents estiver enviando dados para o armazenamento em nuvem, trabalhe com seu representante LiveRamp para configurar a resolução de identidade no seu ambiente de nuvem:

- **Para BigQuery:** siga o guia de configuração do [LiveRamp Embedded Identity in BigQuery](https://docs.liveramp.com/identity/en/liveramp-embedded-identity-in-bigquery.html#liveramp-embedded-identity-in-bigquery) para ativar a resolução de identidade e a tradução de RampID. Coordene com seu representante LiveRamp para concluir as etapas de acordo e provisionamento necessárias para o programa beta.
- **Para AWS:** siga o guia de configuração do [LiveRamp Identity in AWS](https://docs.liveramp.com/identity/en/liveramp-identity-in-aws.html#liveramp-identity-in-aws) para configurar a resolução de identidade de RampID usando o AWS Entity Resolution ou o ADX standalone.

### Etapa 3: Carregue e transforme seus dados {#step-3-load-and-transform-your-data}

Crie um processo de ETL (Extract, Transform, Load) para:

1. Carregar os dados do Currents do armazenamento em nuvem nas tabelas do seu data warehouse.
2. Transformar os dados no formato exigido pelo serviço de resolução de identidade da LiveRamp.
3. Preparar tabelas de entrada com os identificadores necessários para a resolução da LiveRamp (como endereços de e-mail, IDs de dispositivo ou IDs externos de usuário).

### Etapa 4: Execute a resolução de identidade {#step-4-perform-identity-resolution}

Use a resolução de identidade nativa na nuvem da LiveRamp para resolver seus identificadores da Braze em RampIDs. O processo:

1. Resolve os identificadores fornecidos (IPI ou dispositivo) para o identificador pseudônimo baseado em pessoa da LiveRamp, o RampID.
2. Grava as tabelas de saída com RampIDs de volta no seu data warehouse, com os dados de IPI removidos.

### Etapa 5: Ative seus públicos {#step-5-activate-your-audiences}

Com seus dados agora pseudonimizados para RampID, você pode:

- Combinar dados primários da Braze com outras fontes de dados para criar segmentos de clientes mais precisos.
- Ativar públicos pseudonimizados por meio da plataforma de ativação da LiveRamp para campanhas publicitárias.
- Receber dados de exposição de anúncios dos parceiros para mensuração em nível de pessoa.

Para mais detalhes sobre ativação, entre em contato com sua equipe de contas LiveRamp ou [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com).

## Solução de problemas {#troubleshooting}

{% alert note %}
Se você tiver questões ou problemas mais específicos, entre em contato com [martech@liveramp.com](mailto:martech@liveramp.com) ou [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com).
{% endalert %}

### Regiões do Snowflake {#snowflake-regions}

O app nativo do Snowflake está atualmente disponível apenas para as seguintes regiões baseadas nos EUA:

  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### Privacidade e valores de coluna {#privacy-column-values}

O processo de resolução de identidade da LiveRamp avalia a combinação de todos os valores de coluna por linha em busca de valores exclusivos. Se uma determinada combinação de valores de coluna ocorrer 3 ou menos vezes, as linhas que contêm esses valores não poderão ser correspondidas e não serão retornadas na tabela de saída. Da mesma forma, para garantir a privacidade, o serviço da LiveRamp avalia a exclusividade das combinações de valores de coluna, garantindo que, se mais de 5% das linhas do arquivo se tornarem não correspondíveis devido a combinações raras, o trabalho falhará.

### Dados históricos {#historical-data}

Os dados históricos no Snowflake remontam a abril de 2019, mas pode haver pequenas diferenças nos dados anteriores a agosto de 2019 devido a alterações no produto.

### Velocidade, desempenho e custo {#speed-performance-cost}

A velocidade e o custo das consultas dependem do tamanho do warehouse usado. Considere suas necessidades de acesso aos dados ao selecionar o tamanho do warehouse.

### Benchmarks da Braze {#braze-benchmarks}

Os benchmarks permitem que você compare suas métricas com os padrões do setor, disponíveis diretamente no Snowflake Data Exchange.

### Alterações interruptivas e não interruptivas {#breaking-vs-non-breaking-changes}

Esteja ciente das mudanças que podem afetar sua integração. As mudanças interruptivas serão precedidas de um anúncio e de um período de migração.