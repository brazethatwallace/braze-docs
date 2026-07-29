---
nav_title: Integrações de armazenamento de arquivos
article_title: Integrações de armazenamento de arquivos
description: "Esta página aborda a Ingestão de Dados na Nuvem da Braze e como sincronizar dados relevantes do Amazon S3 ou Google Cloud Storage para a Braze."
page_order: 4
page_type: reference

---

# Integrações de armazenamento de arquivos {#file-storage-integrations}

> Esta página aborda como configurar a Ingestão de Dados na Nuvem para sincronizar dados do Amazon S3 ou Google Cloud Storage para a Braze.

## Como funciona {#how-it-works}

Você pode usar a Ingestão de Dados na Nuvem (CDI) para integrar diretamente um ou mais buckets de armazenamento na sua conta de nuvem com a Braze. Quando você adiciona um novo arquivo a um bucket, seu provedor de nuvem publica uma notificação, e a Ingestão de Dados na Nuvem da Braze sincroniza os dados.

O mecanismo de notificação depende do seu provedor:

- **Amazon S3:** quando novos arquivos são publicados no S3, uma mensagem é postada em uma fila do Amazon Simple Queue Service (SQS), e a Braze consome essa mensagem para ingerir o novo arquivo.
- **Google Cloud Storage (GCS):** quando novos arquivos são finalizados no bucket, o GCS publica uma notificação `OBJECT_FINALIZE` em um tópico Pub/Sub. A Braze consome essas notificações de uma assinatura Pub/Sub para ingerir o novo arquivo.

A Ingestão de Dados na Nuvem suporta o seguinte:

- Arquivos JSON
- Arquivos CSV
- Arquivos Parquet
- Dados de atributos, eventos personalizados, eventos de compra, exclusão de usuários e catálogos

## Configuração da Ingestão de Dados na Nuvem {#setting-up-cloud-data-ingestion}

As etapas de configuração dependem do seu provedor de armazenamento de arquivos. Selecione a guia do seu provedor e, em seguida, conclua a configuração compartilhada nas seções a seguir.

{% tabs %}
{% tab Amazon S3 %}

A integração requer os seguintes recursos:

- Bucket S3 para armazenamento de dados
- Fila SQS para notificações de novos arquivos
- Função IAM para acesso da Braze

### Definições da AWS {#aws-definitions}

| Termo | Definição |
| --- | --- |
| Nome do Recurso da Amazon (ARN) | O ARN é um identificador exclusivo dos recursos da AWS. |
| Gerenciamento de Identidade e Acesso (IAM) | IAM é um serviço da web que permite controlar com segurança o acesso aos recursos da AWS. Neste tutorial, crie uma política de IAM e atribua-a a uma função de IAM para integrar seu bucket S3 à Ingestão de Dados na Nuvem da Braze. |
| Serviço de Fila Simples da Amazon (SQS) | O SQS é uma fila hospedada que permite integrar sistemas e componentes de software distribuídos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definições da AWS" }

## Configuração da Ingestão de Dados na Nuvem na AWS {#setting-up-cloud-data-ingestion-in-aws}

### Etapa 1: Criar um bucket de origem {#step-1-create-a-source-bucket}

Crie um bucket S3 de uso geral com configurações padrão na sua conta AWS. Buckets S3 podem ser reutilizados em sincronizações desde que a pasta seja única.

As configurações padrão são:

- ACLs desativadas
- Bloquear todo o acesso público
- Desativar o controle de versão do bucket
- Criptografia SSE-S3
  - SSE-S3 é o único tipo de criptografia do lado do servidor suportado. A criptografia do Amazon KMS não é suportada.

Anote a região em que você criou o bucket — você criará uma fila SQS na mesma região na próxima etapa.

### Etapa 2: Criar fila SQS {#step-2-create-sqs-queue}

Crie uma fila SQS para rastrear quando os objetos são adicionados ao bucket que você criou. Use as definições de configuração padrão por enquanto.

Uma fila SQS deve ser única globalmente (por exemplo, apenas uma pode ser usada para uma sincronização CDI e não pode ser reutilizada em outro espaço de trabalho).

{% alert important %}
Certifique-se de criar esta SQS na mesma região em que você criou o bucket.
{% endalert %}

Anote o ARN e o URL da fila SQS — você precisará deles com frequência durante esta configuração.

![Selecionando "Avançado" com um objeto JSON de exemplo para definir quem pode acessar uma fila.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Etapa 3: Configurar a política de acesso {#step-3-set-up-access-policy}

Para configurar a política de acesso, selecione **Advanced options**.

Anexe a seguinte declaração à política de acesso da fila, tomando cuidado para substituir `YOUR-BUCKET-NAME-HERE` pelo nome do bucket, `YOUR-SQS-ARN` pelo ARN da fila SQS e `YOUR-AWS-ACCOUNT-ID` pelo ID da conta da AWS:

``` json
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
}
```

### Etapa 4: Adicionar uma notificação de evento ao bucket S3 {#step-4-add-an-event-notification-to-the-s3-bucket}

1. No bucket criado na etapa 1, acesse **Properties** > **Event notifications**.
2. Dê um nome à configuração. Opcionalmente, especifique um prefixo ou sufixo para direcionamento se quiser que apenas um subconjunto de arquivos seja ingerido pela Braze.
3. Em **Destination**, selecione **SQS queue** e forneça o ARN da SQS que você criou na etapa 2.

{% alert note %}
Se você fizer upload dos seus arquivos para a pasta raiz de um bucket S3 e depois mover alguns dos arquivos para uma pasta específica no bucket, pode encontrar um erro inesperado. Em vez disso, você pode alterar as notificações de evento para enviar apenas para os arquivos no prefixo, evitar colocar arquivos no bucket S3 fora desse prefixo ou atualizar a integração sem prefixo, o que fará com que todos os arquivos sejam ingeridos.
{% endalert %}

### Etapa 5: Criar uma política de IAM {#step-5-create-an-iam-policy}

Crie uma política de IAM para permitir que a Braze interaja com seu bucket de origem. Para começar, faça login no console de gerenciamento da AWS como administrador da conta.

1. Acesse a seção IAM do console da AWS, selecione **Policies** na barra de navegação e, em seguida, selecione **Create Policy**.<br><br>![O botão "Create policy" no console da AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Abra a guia **JSON** e insira o seguinte trecho de código na seção **Policy Document**, tomando o cuidado de substituir `YOUR-BUCKET-NAME-HERE` pelo nome do bucket e `YOUR-SQS-ARN-HERE` pelo nome da fila do SQS:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```

{: start="3"}
3. Selecione **Review Policy** quando terminar.

4. Dê um nome e uma descrição à política e selecione **Create Policy**.

![Uma política de exemplo chamada "new-policy-name".]({% image_buster /assets/img/create_policy_3_name.png %})

![O campo de descrição para a política.]({% image_buster /assets/img/create_policy_4_created.png %})

### Etapa 6: Criar uma função de IAM {#step-6-create-an-iam-role}

Para concluir a configuração na AWS, crie uma função de IAM e anexe a ela a política de IAM da etapa 5.

1. Na mesma seção de IAM do console em que criou a política de IAM, acesse **Roles** > **Create Role**.

![O botão "Create Role".]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. Na AWS, selecione **Another AWS Account** como o tipo de seletor de entidade confiável. Forneça seu ID de conta da Braze. Marque a caixa de seleção **Require external ID**.
3. Na Braze, acesse **Configurações de dados** > **Ingestão de Dados na Nuvem** > **Sources**, selecione **Add data source** e selecione **Amazon S3** na seção de fontes de arquivo.
4. Copie o **Braze Account ID** gerado automaticamente.

![A página "Add New Source" mostrando as seções Source Name e S3 Connection Details.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. Na AWS, cole o ID da conta e selecione **Next**.

![A página "Create Role" do S3. Essa página tem campos para nome da função, descrição da função, entidades confiáveis, políticas e limite de permissões.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Anexe a política criada na etapa 4 à função. Procure a política na barra de pesquisa e marque a caixa de seleção ao lado da política para anexá-la. Selecione **Next** quando terminar.

![ARN da função com a nova política selecionada.]({% image_buster /assets/img/create_role_3_attach.png %})

Dê um nome e uma descrição à função e selecione **Create Role**.

![Uma função de exemplo chamada "new-role-name".]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Anote o ARN da função que você criou e o ID externo que você gerou, pois você precisará deles para criar a integração de Ingestão de Dados na Nuvem.

## Configuração da Ingestão de Dados na Nuvem na Braze {#setting-up-cloud-data-ingestion-in-braze}

1. Primeiro, crie uma nova origem no dashboard da Braze. Acesse **Configurações de dados** > **Ingestão de Dados na Nuvem** > **Sources**, selecione **Add data source** e, em seguida, selecione **Amazon S3**.
2. Escolha um nome para sua origem e insira as informações do processo de configuração da AWS para criar uma nova origem. Especifique o seguinte:

  - ARN da função
  - ID externo
  - Nome do bucket
  - Região

![A seção S3 Connection Details mostrando Credentials (configuração da AWS e da Braze) e campos de Configuration.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Selecione **Test connection** para confirmar que a Braze pode acessar seu bucket. Após um teste bem-sucedido, selecione **Connect to Source**. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{: start="4"}
4. Em seguida, crie uma nova sincronização. Acesse **Configurações de dados** > **Ingestão de Dados na Nuvem** > **Syncs** e selecione **Create data sync**.

{: start="5"}
5. Escolha um nome para sua sincronização. Em seguida, selecione qualquer origem S3 ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dado e selecione **Test Connection**.

![Uma opção para testar a conexão com uma prévia de dados.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Insira as informações restantes do processo de configuração da AWS. Especifique o seguinte:
- URL do SQS (deve ser exclusivo para cada nova integração)
- Caminho da pasta (opcional, deve ser único entre as sincronizações em um espaço de trabalho)

7. Selecione um tipo de dado e selecione **Test Connection** para confirmar que a Braze pode listar os arquivos disponíveis para ingestão (não os dados dentro desses arquivos). Após o sucesso, selecione **Next: Notifications**.
8. Adicione e-mail(s) de contato para notificações se a sincronização for interrompida devido a problemas de acesso ou permissões. Opcionalmente, ative as notificações para erros no nível do usuário e sucessos de sincronização.
9. Crie a sincronização.

{% endtab %}
{% tab Google Cloud Storage %}

A integração requer os seguintes recursos:

- Um bucket Cloud Storage para armazenamento de dados
- Um tópico e uma assinatura Pub/Sub para notificações de novos arquivos
- Uma conta de serviço cuja chave JSON você faz upload para a Braze

### Definições do GCP {#gcp-definitions}

| Termo | Definição |
| --- | --- |
| Projeto do Google Cloud | Um projeto organiza todos os seus recursos do Google Cloud e é identificado por um ID de projeto e um número de projeto exclusivos. |
| Bucket Cloud Storage | Um bucket é o contêiner que armazena os arquivos de dados que você deseja que a Braze ingira. |
| Tópico Pub/Sub | Um tópico é o recurso nomeado que recebe notificações de novos arquivos do seu bucket Cloud Storage. |
| Assinatura Pub/Sub | Uma assinatura se conecta a um tópico e entrega suas mensagens. A Braze consome notificações de novos arquivos de uma assinatura pull. |
| Conta de serviço | Uma conta de serviço é uma identidade não humana que a Braze usa para acessar seu bucket e sua assinatura. Você faz upload da chave JSON dela para a Braze. |
| Função IAM | Uma função de Gerenciamento de Identidade e Acesso (IAM) é uma coleção de permissões que você concede à conta de serviço no seu bucket e na sua assinatura. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definições do GCP" }

## Configuração da Ingestão de Dados na Nuvem no Google Cloud {#setting-up-cloud-data-ingestion-in-google-cloud}

### Etapa 1: Criar um bucket Cloud Storage {#step-1-create-a-cloud-storage-bucket}

No console do Google Cloud, acesse **Cloud Storage** > **Buckets** > **Create**. Anote o ID do projeto e o nome do bucket — você precisará deles ao configurar a origem na Braze. Recomendamos ativar o acesso uniforme no nível do bucket para que as permissões sejam gerenciadas com IAM.

Alternativamente, crie o bucket com gcloud:

```shell
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=YOUR-REGION \
  --uniform-bucket-level-access
```

### Etapa 2: Criar um tópico e uma assinatura Pub/Sub {#step-2-create-a-pubsub-topic-and-subscription}

No console do Google Cloud, acesse **Pub/Sub** > **Topics** > **Create topic**. Você pode deixar o Google criar uma assinatura padrão ou criar uma separadamente. Em seguida, crie uma assinatura **pull** nesse tópico.

Alternativamente, use gcloud:

```shell
gcloud pubsub topics create YOUR-TOPIC --project=YOUR-PROJECT-ID
gcloud pubsub subscriptions create YOUR-SUBSCRIPTION \
  --topic=YOUR-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
```

Anote o **ID da assinatura** — a Braze precisa da assinatura (não do tópico) quando você cria a sincronização. A assinatura deve ser do tipo pull.

### Etapa 3: Enviar notificações do bucket para o tópico {#step-3-send-bucket-notifications-to-the-topic}

{% alert important %}
A criação de uma notificação do Cloud Storage para o Pub/Sub não está disponível no console do Google Cloud. Você deve usar gcloud (mostrado aqui), Terraform ou a API JSON. Para saber mais, consulte [Configurar notificações Pub/Sub para Cloud Storage](https://cloud.google.com/storage/docs/reporting-changes#enabling) na documentação do Google Cloud.
{% endalert %}

Primeiro, conceda ao agente de serviço do Cloud Storage permissão para publicar no tópico e, em seguida, crie a notificação para `OBJECT_FINALIZE`. O evento `OBJECT_FINALIZE` é disparado sempre que um novo objeto é criado ou finalizado no bucket.

```shell
# Get the Cloud Storage service agent for your project
gcloud storage service-agent --project=YOUR-PROJECT-ID

# Grant it Pub/Sub Publisher on the topic
gcloud pubsub topics add-iam-policy-binding YOUR-TOPIC \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"

# Create the OBJECT_FINALIZE notification (optionally scope to a folder with --object-prefix)
gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
  --topic=YOUR-TOPIC \
  --event-types=OBJECT_FINALIZE \
  --payload-format=json
```

Substitua os seguintes espaços reservados nesses comandos:

- `YOUR-PROJECT-ID`: o ID do seu projeto do Google Cloud, o identificador legível (por exemplo, `my-gcp-project`).
- `YOUR-TOPIC`: o tópico Pub/Sub que você criou na [Etapa 2](#step-2-create-a-pubsub-topic-and-subscription).
- `YOUR-BUCKET-NAME`: o nome do seu bucket Cloud Storage.
- `YOUR-PROJECT-NUMBER`: o número do seu projeto, o identificador numérico usado no endereço de e-mail do agente de serviço do Cloud Storage. Isso é diferente do ID do projeto. Encontre-o no **Dashboard** do console do Google Cloud ou execute o seguinte comando:

```shell
gcloud projects describe YOUR-PROJECT-ID --format="value(projectNumber)"
```

### Etapa 4: Criar uma conta de serviço {#step-4-create-a-service-account}

No console do Google Cloud, acesse **IAM & Admin** > **Service Accounts** > **Create service account**.

Alternativamente, use gcloud:

```shell
gcloud iam service-accounts create braze-cdi-gcs \
  --project=YOUR-PROJECT-ID \
  --display-name="Braze CDI GCS"
```

### Etapa 5: Conceder permissões {#step-5-grant-permissions}

O conector precisa exatamente destas permissões: `storage.buckets.get`, `storage.objects.get` e `storage.objects.list` no bucket, e `pubsub.subscriptions.consume` na assinatura. Você pode concedê-las com uma função personalizada ou funções predefinidas.

**Função personalizada:** crie uma função personalizada com exatamente essas permissões e vincule-a ao bucket e à assinatura:

```shell
gcloud iam roles create brazeCdiGcs --project=YOUR-PROJECT-ID \
  --title="Braze CDI GCS" \
  --permissions=storage.buckets.get,storage.objects.get,storage.objects.list,pubsub.subscriptions.consume \
  --stage=GA

gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"

gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"
```

**Funções predefinidas:** conceda `roles/storage.objectViewer` e `roles/storage.legacyBucketReader` no bucket, e `roles/pubsub.subscriber` na assinatura. A função `objectViewer` fornece `storage.objects.get` e `storage.objects.list`, e `legacyBucketReader` fornece `storage.buckets.get`:

```shell
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.legacyBucketReader"
gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber"
```

### Etapa 6: Criar uma chave JSON {#step-6-create-a-json-key}

No console do Google Cloud, abra a conta de serviço, acesse **Keys** > **Add key** > **Create new key** e selecione **JSON**.

Alternativamente, use gcloud:

```shell
gcloud iam service-accounts keys create braze-cdi-gcs-key.json \
  --iam-account=braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com
```

## Configuração da Ingestão de Dados na Nuvem na Braze

1. Na Braze, acesse **Configurações de dados** > **Ingestão de Dados na Nuvem** > **Sources**, selecione **Add data source** e, em seguida, selecione **Google Cloud Storage**.

![A tela "Add New Source" com Google Cloud Storage selecionado na lista de fontes de dados.]({% image_buster /assets/img/cloud_ingestion/gcs_source_picker.png %})

{: start="2"}
2. Preencha os campos da origem:
    - **Bucket** — o nome do seu bucket
    - **Project ID** — o ID do seu projeto GCP
    - **Service account JSON key** — faça upload do arquivo de chave da etapa 6 e dê um nome à credencial

![O formulário de origem do Google Cloud Storage mostrando os campos Bucket, Project ID e upload de credencial.]({% image_buster /assets/img/cloud_ingestion/gcs_source_form.png %})

{: start="3"}
3. Selecione **Test connection** e, em seguida, selecione **Connect to Source**.
4. Crie uma sincronização. Acesse **Configurações de dados** > **Ingestão de Dados na Nuvem** > **Syncs** e selecione **Create data sync**. Escolha um nome para a sincronização e um **Data Type** (como **User Attributes**, **Custom Events**, **Purchase Events**, **Catalog** ou **Delete Users**) e, em seguida, selecione **Next**.
5. Na etapa **Data definition**, selecione sua origem GCS e especifique o seguinte:
    - **Pub/Sub subscription ID** — o ID da assinatura da etapa 2 (não o tópico)
    - **Folder path** (opcional) — um prefixo de caminho dentro do bucket (consulte [Sincronizando uma pasta em um bucket compartilhado](#syncing-a-folder-in-a-shared-bucket))

![O formulário de sincronização do Google Cloud Storage mostrando os campos Pub/Sub subscription ID e folder path.]({% image_buster /assets/img/cloud_ingestion/gcs_sync_form.png %})

{: start="6"}
6. Selecione **Preview and validate** para confirmar que a Braze pode acessar a assinatura e listar os arquivos disponíveis para ingestão. Um teste bem-sucedido listará os arquivos existentes no bucket, mas esses arquivos não serão sincronizados automaticamente.
7. Adicione e-mail(s) de contato para notificações de erros. As sincronizações do Google Cloud Storage são orientadas por eventos, então não é necessário agendar — a Braze ingere novos arquivos à medida que são enviados. Revise o resumo e selecione **Create sync**.

### Sincronizando uma pasta em um bucket compartilhado {#syncing-a-folder-in-a-shared-bucket}

Você pode reutilizar um bucket em várias sincronizações, mas cada sincronização deve apontar para uma pasta distinta **e** ter sua própria assinatura Pub/Sub dedicada.


{% alert important %}
O caminho da pasta e a assinatura devem ser únicos entre as sincronizações em um espaço de trabalho para múltiplas sincronizações compartilhando o mesmo bucket de origem.
{% endalert %}

Para cada pasta que você deseja sincronizar em um bucket compartilhado:

1. Defina o campo **Folder** da sincronização com o prefixo do caminho (por exemplo, `attributes/`). A Braze só lista e ingere objetos cujo caminho começa com esse prefixo.
2. Crie um tópico dedicado e uma notificação com escopo de prefixo para essa pasta, e depois crie uma assinatura nesse tópico:

    ```shell
    # One topic per folder
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Grant the Cloud Storage service agent publisher on the topic
    gcloud pubsub topics add-iam-policy-binding YOUR-ATTRIBUTES-TOPIC \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
      --role="roles/pubsub.publisher"

    # Notification scoped to the folder with --object-prefix
    gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
      --topic=YOUR-ATTRIBUTES-TOPIC --event-types=OBJECT_FINALIZE \
      --payload-format=json --object-prefix=attributes/

    # One subscription per sync
    gcloud pubsub subscriptions create YOUR-ATTRIBUTES-SUBSCRIPTION \
      --topic=YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
    ```

3. Conceda à conta de serviço da Braze permissão de consumo nessa assinatura, como na [Etapa 5](#step-5-grant-permissions):

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    Se você criou a função personalizada na [Etapa 5](#step-5-grant-permissions), use `--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"` em vez disso.
4. Ao criar a sincronização na Braze, insira o novo **Pub/Sub subscription ID** e o **Folder path** dessa pasta para que a sincronização ingira apenas os arquivos dessa pasta.


{% endtab %}
{% endtabs %}

## Formatos de arquivo necessários {#required-file-formats}

Os formatos de arquivo necessários são os mesmos para Amazon S3 e Google Cloud Storage. A Ingestão de Dados na Nuvem aceita arquivos JSON, CSV e Parquet. As colunas obrigatórias dependem do tipo de dado:

- Dados de usuários (atributos, eventos personalizados, eventos de compra) usam identificadores de usuário e uma carga útil
- Dados de catálogo usam identificadores de catálogo

Se você estiver usando armazenamento de arquivos para dados de catálogo, use esta página junto com [Sincronizar e excluir dados do catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) para requisitos e comportamentos específicos de catálogo.

A Braze não impõe requisitos adicionais de nome de arquivo além do que é imposto pelo seu provedor de armazenamento de arquivos. Os nomes dos arquivos devem ser únicos. Adicionar um timestamp ajuda a garantir a exclusividade.

Para exemplos de todos os tipos de arquivo suportados (atributos, eventos personalizados, compras, catálogos e exclusões de usuários), consulte os arquivos de amostra em [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Identificadores de usuário {#user-identifiers}

Para sincronizações de dados de usuários (atributos, eventos personalizados, eventos de compra), cada linha no seu arquivo de origem requer exatamente um identificador de usuário e uma coluna `PAYLOAD`. Um arquivo de origem pode conter linhas com diferentes tipos de identificadores, mas cada linha individual deve usar apenas um.

| Identificador | Descrição |
| --- | --- |
| `EXTERNAL_ID` | Identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado na Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter múltiplos aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
| `BRAZE_ID` | O identificador de usuário da Braze. Isso é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da Ingestão de Dados na Nuvem. Para criar novos usuários, especifique um ID externo ou um alias de usuário. |
| `EMAIL` | O endereço de e-mail do usuário. Se houver vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade nas atualizações. Se você incluir e-mail e telefone, a Braze usará o e-mail como identificador principal. |
| `PHONE` | O número de telefone do usuário. Se houver vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identificadores de usuário" }

Além de um identificador, cada linha deve incluir uma coluna `PAYLOAD` contendo uma string JSON dos campos que você deseja sincronizar com o usuário na Braze.

{% alert note %}
Diferente das fontes de data warehouse, a coluna `UPDATED_AT` não é obrigatória nem suportada para sincronizações de armazenamento de arquivos.
{% endalert %}

### Identificadores de catálogo {#catalog-identifiers}

Para sincronizações de catálogo, seu arquivo de origem deve conter as seguintes colunas. Arquivos de catálogo usam identificadores diferentes dos arquivos de dados de usuários.

| Coluna | Obrigatória | Descrição |
| --- | --- | --- |
| `ID` | Sim | O identificador único do item do catálogo. Usado para criar, atualizar ou excluir o item na Braze. |
| `PAYLOAD` | Sim | Uma string JSON dos campos e valores do catálogo a serem sincronizados. Deve corresponder ao esquema do seu catálogo na Braze. |
| `DELETED` | Não | Quando `true`, o item do catálogo com o `ID` correspondente é removido do catálogo na Braze. Omita esta coluna ou defina como `false` para operações de criação ou atualização. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Identificadores de catálogo" }

### Exemplos {#examples}

{% tabs %}
{% tab JSON Attributes %}
``` json
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```
{% alert important %}
Todas as linhas do seu arquivo de origem devem conter JSON válido, ou o arquivo será ignorado.
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
Todas as linhas do seu arquivo de origem devem conter JSON válido, ou o arquivo será ignorado.
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
Todas as linhas do seu arquivo de origem devem conter JSON válido, ou o arquivo será ignorado.
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
Inclua uma coluna opcional `DELETED`. Quando `DELETED` é `true`, esse item de catálogo é removido do catálogo na Braze. Para a lista completa de colunas obrigatórias, consulte [Identificadores de catálogo](#catalog-identifiers). Para o comportamento de exclusão, consulte [Excluindo itens do catálogo](#deleting-catalog-items). Para um fluxo de configuração de catálogo de ponta a ponta (incluindo a criação do catálogo de destino e o comportamento de sincronização), consulte [Sincronizar e excluir dados do catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).
{% endtab %}

{% endtabs %}

## Excluindo dados {#deleting-data}

A Ingestão de Dados na Nuvem para armazenamento de arquivos suporta a exclusão de usuários e itens do catálogo por meio de uploads de arquivos. Use sincronizações e formatos de arquivo separados para cada um.

- **[Excluindo usuários](#deleting-users)** – Crie uma sincronização com o tipo de dado **Delete Users** e faça upload de arquivos que contenham apenas identificadores de usuários (sem carga útil).
- **[Excluindo itens do catálogo](#deleting-catalog-items)** – Use sua sincronização de catálogo existente e adicione uma coluna `deleted` (ou `DELETED`) para marcar itens para remoção.

### Excluindo usuários {#deleting-users}

Para excluir perfis de usuários na Braze usando arquivos no seu bucket de origem:

1. Crie uma nova sincronização de Ingestão de Dados na Nuvem (mesma configuração que para outras sincronizações).
2. Ao configurar a sincronização na Braze, defina **Data Type** como **Delete Users**.
3. Faça upload de arquivos para seu bucket de origem que contenham apenas colunas de identificador de usuário. Não inclua uma coluna `PAYLOAD` — a sincronização falha se a carga útil estiver presente, para evitar exclusões acidentais.

Cada linha no arquivo deve identificar exatamente um usuário usando um dos seguintes:

| Identificador | Descrição |
| --- | --- |
| `EXTERNAL_ID` | Corresponde ao `external_id` usado na Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Ambas as colunas juntas identificam o usuário por alias. |
| `BRAZE_ID` | ID de usuário gerado pela Braze (apenas usuários existentes). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Excluindo usuários" }

{% alert important %}
A exclusão de usuários é permanente e não pode ser desfeita. Inclua apenas usuários que você realmente pretende remover. Para mais detalhes, consulte [Excluir usuários com Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users).
{% endalert %}

**Exemplo – JSON (exclusão de usuários):**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**Exemplo – CSV (exclusão de usuários):**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

Quando a sincronização é executada, a Braze processa novos arquivos no bucket e exclui os perfis de usuário correspondentes.

### Excluindo itens do catálogo {#deleting-catalog-items}

Para remover itens de um catálogo usando armazenamento de arquivos:

1. Use a mesma sincronização que você usa para [sincronizar dados do catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) (tipo de dado **Catalogs**).
2. Nos seus arquivos CSV ou JSON, adicione uma coluna opcional **`deleted`** (ou **`DELETED`**).
3. Defina `deleted` como `true` para qualquer item do catálogo que você deseja remover do catálogo na Braze.

Cada linha ainda precisa de `ID` e `PAYLOAD`. Para linhas marcadas para exclusão, a carga útil pode ser mínima; a Braze remove o item pelo `ID`.

**Exemplo – JSON (exclusão de item do catálogo):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Exemplo – CSV (exclusão de item do catálogo):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Quando a sincronização é executada, linhas com `deleted: true` fazem com que o item do catálogo correspondente seja excluído na Braze. Para o comportamento completo de sincronização e exclusão do catálogo, consulte [Sincronizar e excluir dados do catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).

## Informações importantes {#things-to-know}

- Os arquivos adicionados ao bucket de origem não devem exceder 512&nbsp;MB. Esse limite se aplica tanto ao Amazon S3 quanto ao Google Cloud Storage. Arquivos maiores que 512&nbsp;MB resultarão em um erro e não serão sincronizados com a Braze.
- Embora não haja limite adicional no número de linhas por arquivo, recomendamos usar arquivos menores para melhorar a velocidade das suas sincronizações. Por exemplo, um arquivo de 500&nbsp;MB levaria consideravelmente mais tempo para ser ingerido do que cinco arquivos separados de 100&nbsp;MB.
- Não há limite adicional no número de arquivos enviados em um determinado período.
- A ordenação não é suportada dentro ou entre arquivos. Recomendamos agrupar atualizações periodicamente se você estiver monitorando possíveis condições de corrida.

## Solução de problemas {#troubleshooting}

### Upload e processamento de arquivos {#uploading-files-and-processing}

O CDI só processará arquivos que forem adicionados após a criação da sincronização. Nesse processo, a Braze procura novos arquivos sendo adicionados, o que dispara uma nova notificação. Isso inicia uma nova sincronização para processar o novo arquivo. Para o Amazon S3, a notificação é uma mensagem para o SQS. Para o Google Cloud Storage, é uma mensagem `OBJECT_FINALIZE` para o Pub/Sub.

Você pode usar arquivos existentes para validar se a Braze consegue acessar seu bucket e detectar arquivos para ingestão, mas eles não são sincronizados com a Braze. Para que o CDI os processe, você deve fazer upload novamente para o bucket de origem de quaisquer arquivos existentes que deseja sincronizar.

### Tratando erros inesperados de arquivos (Amazon S3) {#handling-unexpected-file-errors-amazon-s3}

Se você estiver observando um alto número de erros ou arquivos com falha, pode haver outro processo adicionando arquivos ao bucket S3 em uma pasta diferente da pasta de destino do CDI.

Quando arquivos são enviados para o bucket de origem, mas não na pasta de origem, o CDI processará a notificação do SQS, mas não tomará nenhuma ação sobre o arquivo, então isso pode aparecer como um erro.

Se o seu problema estiver relacionado a notificações do S3 ou permissões de destino do SQS (por exemplo, erros de validação de destino), consulte a documentação da AWS:

- [Habilitando e configurando notificações de eventos usando o console do Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Concedendo permissões para publicar mensagens de notificação de eventos em um destino](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Solução de problemas no Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### Tratando erros inesperados de arquivos (Google Cloud Storage) {#handling-unexpected-file-errors-google-cloud-storage}

Assim como no Amazon S3, o CDI só processa arquivos enviados após a criação da sincronização. Cada novo objeto dispara uma mensagem `OBJECT_FINALIZE` para o seu tópico Pub/Sub. Para ingerir arquivos que já existem no bucket, faça upload deles novamente.

Se os arquivos não estiverem sendo ingeridos, verifique o seguinte:

- A notificação do bucket existe. Liste as notificações no bucket com `gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME`.
- O agente de serviço do Cloud Storage tem `roles/pubsub.publisher` no tópico.
- A conta de serviço da Braze tem permissão de consumo na assinatura (`pubsub.subscriptions.consume`, concedida por meio da função personalizada ou `roles/pubsub.subscriber`).

Para saber mais, consulte [Notificações Pub/Sub para Cloud Storage](https://cloud.google.com/storage/docs/pubsub-notifications) na documentação do Google Cloud.