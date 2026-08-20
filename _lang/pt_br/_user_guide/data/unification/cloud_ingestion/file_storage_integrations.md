---
nav_title: Integrações de armazenamento de arquivos
article_title: Integrações de armazenamento de arquivos
description: "Esta página aborda a Ingestão de Dados na Nuvem da Braze e como sincronizar dados relevantes do S3 para a Braze."
page_order: 4
page_type: reference

---

# Integrações de armazenamento de arquivos {#file-storage-integrations}

> Esta página aborda como configurar o suporte à Ingestão de Dados na Nuvem e sincronizar dados relevantes do S3 para a Braze.

## Como funciona {#how-it-works}

Você pode usar a Ingestão de Dados na Nuvem (CDI) para S3 para integrar diretamente um ou mais buckets S3 da sua conta AWS com a Braze. Quando novos arquivos são publicados no S3, uma mensagem é postada no SQS, e a Ingestão de Dados na Nuvem da Braze processa esses novos arquivos.

A Ingestão de Dados na Nuvem é compatível com o seguinte:

- Arquivos JSON
- Arquivos CSV
- Arquivos Parquet
- Dados de atributos, eventos personalizados, eventos de compra, exclusão de usuários e catálogos

## Pré-requisitos {#prerequisites}

A integração requer os seguintes recursos:

 - Bucket S3 para armazenamento de dados
 - Fila SQS para notificações de novos arquivos
 - Função IAM para acesso da Braze

### Definições da AWS {#aws-definitions}

Primeiro, defina os termos usados durante esta tarefa.

| Termo | Definição |
| --- | --- |
| Amazon Resource Name (ARN) | O ARN é um identificador exclusivo para recursos da AWS. |
| Identity and Access Management (IAM) | O IAM é um serviço web que permite controlar com segurança o acesso aos recursos da AWS. Neste tutorial, crie uma política do IAM e atribua-a a uma função do IAM para integrar seu bucket S3 com a ingestão de dados na nuvem da Braze. |
| Amazon Simple Queue Service (SQS) | O SQS é uma fila hospedada que permite integrar sistemas e componentes de software distribuídos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definições da AWS" }

## Configurando a Ingestão de Dados na Nuvem na AWS {#setting-up-cloud-data-ingestion-in-aws}

### Etapa 1: Criar um bucket de origem {#step-1-create-a-source-bucket}

Crie um bucket S3 de uso geral com as configurações padrão na sua conta AWS. Os buckets S3 podem ser reutilizados em diferentes sincronizações, desde que a pasta seja única.

As configurações padrão são:

- ACLs desativadas
- Bloquear todo o acesso público
- Desativar o versionamento do bucket
- Criptografia SSE-S3
  - SSE-S3 é o único tipo de criptografia do lado do servidor compatível. A criptografia Amazon KMS não é compatível.

Anote a região onde você criou o bucket — você criará uma fila SQS na mesma região na próxima etapa.

### Etapa 2: Criar a fila SQS {#step-2-create-sqs-queue}

Crie uma fila SQS para rastrear quando objetos são adicionados ao bucket que você criou. Use as configurações padrão por enquanto.

Uma fila SQS deve ser globalmente única (por exemplo, apenas uma pode ser usada para uma sincronização CDI e não pode ser reutilizada em outro espaço de trabalho).

{% alert important %}
Certifique-se de criar essa fila SQS na mesma região em que você criou o bucket.
{% endalert %}

Anote o ARN e a URL da fila SQS — você precisará deles com frequência durante essa configuração.

![Selecionando "Advanced" com um exemplo de objeto JSON para definir quem pode acessar uma fila.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Etapa 3: Configurar a política de acesso {#step-3-set-up-access-policy}

Para configurar a política de acesso, escolha **Advanced options**.

Adicione a seguinte declaração à política de acesso da fila, substituindo `YOUR-BUCKET-NAME-HERE` pelo nome do seu bucket, `YOUR-SQS-ARN` pelo ARN da sua fila SQS e `YOUR-AWS-ACCOUNT-ID` pelo ID da sua conta AWS:

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
2. Dê um nome à configuração. Opcionalmente, especifique um prefixo ou sufixo para direcionar se você deseja que apenas um subconjunto de arquivos seja ingerido pela Braze.
3. Em **Destination**, selecione **SQS queue** e forneça o ARN da fila SQS que você criou na etapa 2.

{% alert note %}
Se você fizer upload dos seus arquivos para a pasta raiz de um bucket S3 e depois mover alguns dos arquivos para uma pasta específica dentro do bucket, poderá encontrar um erro inesperado. Em vez disso, você pode alterar as notificações de evento para enviar apenas para os arquivos no prefixo, evitar colocar arquivos no bucket S3 fora desse prefixo ou atualizar a integração sem prefixo, o que então ingere todos os arquivos.
{% endalert %}

### Etapa 5: Criar uma política IAM {#step-5-create-an-iam-policy}

Crie uma política IAM para permitir que a Braze interaja com o seu bucket de origem. Para começar, faça login no console de gerenciamento da AWS como administrador da conta.

1. Acesse a seção IAM do console da AWS, selecione **Policies** na barra de navegação e depois selecione **Create Policy**.<br><br>![O botão "Create policy" no console da AWS.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Abra a guia **JSON** e insira o seguinte trecho de código na seção **Policy Document**, substituindo `YOUR-BUCKET-NAME-HERE` pelo nome do seu bucket e `YOUR-SQS-ARN-HERE` pelo nome da sua fila SQS:

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

![Um exemplo de política chamada "new-policy-name."]({% image_buster /assets/img/create_policy_3_name.png %})

![O campo de descrição da política.]({% image_buster /assets/img/create_policy_4_created.png %})

### Etapa 6: Criar uma função IAM {#step-6-create-an-iam-role}

Para concluir a configuração na AWS, crie uma função IAM e anexe a política IAM da etapa 5 a ela.

1. Na mesma seção IAM do console onde você criou a política IAM, acesse **Roles** > **Create Role**.

![O botão "Create role".]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. Na AWS, selecione **Another AWS Account** como o tipo de seletor de entidade confiável. Forneça o ID da sua conta Braze. Marque a caixa de seleção **Require external ID**.
3. Na Braze, acesse **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecione **Add data source** e selecione **Amazon S3** na seção de fontes de arquivo.
4. Copie o **Braze Account ID** gerado automaticamente.

![A página "Add New Source" mostrando as seções Source Name e S3 Connection Details.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. Na AWS, cole o ID da conta e selecione **Next**.

![A página "Create Role" do S3. Esta página possui campos para nome da função, descrição da função, entidades confiáveis, políticas e limite de permissões.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Anexe a política criada na etapa 4 à função. Pesquise a política na barra de busca e marque a caixa de seleção ao lado da política para anexá-la. Selecione **Next** quando concluir.

![ARN da função com a new-policy-name selecionada.]({% image_buster /assets/img/create_role_3_attach.png %})

Dê um nome e uma descrição à função e selecione **Create Role**.

![Um exemplo de função chamada "new-role-name".]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Anote o ARN da função que você criou e o ID externo que você gerou, pois você precisará deles para criar a integração de Ingestão de Dados na Nuvem.

## Configurando a ingestão de dados na nuvem na Braze {#setting-up-cloud-data-ingestion-in-braze}

1. Primeiro, crie uma nova fonte no dashboard da Braze. Acesse **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecione **Add data source** e, em seguida, selecione **Amazon S3**.
2. Escolha um nome para sua fonte e insira as informações do processo de configuração da AWS para criar uma nova fonte. Especifique o seguinte:

  - Role ARN
  - ID externo
  - Nome do bucket
  - Região

![A seção de detalhes de conexão do S3 mostrando credenciais (configuração da AWS e configuração da Braze) e campos de configuração.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Selecione **Test connection** para confirmar que a Braze pode acessar seu bucket. Após um teste bem-sucedido, selecione **Connect to Source**. Se a conexão falhar, uma mensagem de erro será exibida para ajudar a solucionar o problema.

{: start="4"}
4. Em seguida, crie uma nova sincronização. Acesse **Data Settings** > **Cloud Data Ingestion** > **Syncs** e selecione **Create data sync**.

{: start="5"}
5. Escolha um nome para sua sincronização. Em seguida, selecione qualquer fonte S3 ativa e insira sua tabela de origem para a sincronização. Selecione um tipo de dados e selecione **Test Connection**.

![Uma opção para testar a conexão com uma prévia dos dados.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Insira as informações restantes do processo de configuração da AWS. Especifique o seguinte:
- URL do SQS (deve ser exclusiva para cada nova integração)
- Caminho da pasta (opcional, deve ser exclusivo entre as sincronizações em um espaço de trabalho)

7. Selecione um tipo de dados e selecione **Test Connection** para confirmar que a Braze pode listar os arquivos disponíveis para ingestão (não os dados dentro desses arquivos). Após o sucesso, selecione **Next: Notifications**.
8. Adicione e-mail(s) de contato para notificações caso a sincronização seja interrompida por problemas de acesso ou permissões. Opcionalmente, ative notificações para erros no nível do usuário e sincronizações bem-sucedidas.
9. Crie a sincronização.

## Formatos de arquivo obrigatórios {#required-file-formats}

A Ingestão de Dados na Nuvem aceita arquivos JSON, CSV e Parquet. As colunas obrigatórias dependem do tipo de dados:

- Dados de usuários (atributos, eventos personalizados, eventos de compra) usam identificadores de usuário e uma carga útil
- Dados de catálogo usam identificadores de catálogo

Se você estiver usando o S3 para dados de catálogo, use esta página junto com [Sincronizar e excluir dados de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) para requisitos e comportamentos específicos de catálogo.

A Braze não impõe requisitos adicionais de nome de arquivo além do que é exigido pela AWS. Os nomes de arquivo devem ser únicos. Adicionar um timestamp ajuda a garantir a unicidade.

Para exemplos de todos os tipos de arquivo aceitos (atributos, eventos personalizados, compras, catálogos e exclusões de usuários), consulte os arquivos de exemplo em [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Identificadores de usuário {#user-identifiers}

Para sincronizações de dados de usuários (atributos, eventos personalizados, eventos de compra), cada linha no arquivo de origem requer exatamente um identificador de usuário e uma coluna `PAYLOAD`. Um arquivo de origem pode conter linhas com diferentes tipos de identificadores, mas cada linha individual deve usar apenas um.

| Identificador | Descrição |
| --- | --- |
| `EXTERNAL_ID` | Identifica o usuário que você deseja atualizar. Deve corresponder ao valor `external_id` usado na Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador único, e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
| `BRAZE_ID` | O identificador de usuário da Braze. Ele é gerado pelo SDK da Braze, e novos usuários não podem ser criados usando um Braze ID por meio da Ingestão de Dados na Nuvem. Para criar novos usuários, especifique um ID externo ou alias de usuário. |
| `EMAIL` | O endereço de e-mail do usuário. Se existirem vários perfis com o mesmo endereço de e-mail, o perfil atualizado mais recentemente terá prioridade nas atualizações. Se você incluir e-mail e telefone, a Braze usará o e-mail como identificador principal. |
| `PHONE` | O número de telefone do usuário. Se existirem vários perfis com o mesmo número de telefone, o perfil atualizado mais recentemente terá prioridade nas atualizações. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identificadores de usuário" }

Além de um identificador, cada linha deve incluir uma coluna `PAYLOAD` contendo uma string JSON dos campos que você deseja sincronizar com o usuário na Braze.

{% alert note %}
Diferentemente das fontes de data warehouse, a coluna `UPDATED_AT` não é obrigatória nem aceita para sincronizações de armazenamento de arquivos.
{% endalert %}

### Identificadores de catálogo {#catalog-identifiers}

Para sincronizações de catálogo, o arquivo de origem deve conter as seguintes colunas. Arquivos de catálogo usam identificadores diferentes dos arquivos de dados de usuários.

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
Cada linha do arquivo de origem deve conter JSON válido, caso contrário o arquivo será ignorado.
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
Cada linha do arquivo de origem deve conter JSON válido, caso contrário o arquivo será ignorado.
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
Cada linha do arquivo de origem deve conter JSON válido, caso contrário o arquivo será ignorado.
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
Inclua uma coluna `DELETED` opcional. Quando `DELETED` é `true`, o item do catálogo correspondente é removido do catálogo na Braze. Para a lista completa de colunas obrigatórias, consulte [Identificadores de catálogo](#catalog-identifiers). Para o comportamento de exclusão, consulte [Excluindo itens do catálogo](#deleting-catalog-items). Para um fluxo de ponta a ponta de configuração de catálogo (incluindo a criação do catálogo de destino e o comportamento de sincronização), consulte [Sincronizar e excluir dados de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).
{% endtab %}

{% endtabs %}

## Excluindo dados {#deleting-data}

A ingestão de dados na nuvem para S3 permite excluir usuários e itens de catálogo por meio de uploads de arquivos. Use sincronizações e formatos de arquivo separados para cada caso.

- **[Excluindo usuários](#deleting-users)** – Crie uma sincronização com o tipo de dados **Delete Users** e faça upload de arquivos que contenham apenas identificadores de usuários (sem carga útil).
- **[Excluindo itens de catálogo](#deleting-catalog-items)** – Use sua sincronização de catálogo existente e adicione uma coluna `deleted` (ou `DELETED`) para marcar itens para remoção.

### Excluindo usuários {#deleting-users}

Para excluir perfis de usuário na Braze usando arquivos no S3:

1. Crie uma nova sincronização de ingestão de dados na nuvem (a mesma [configuração da AWS e da Braze](#setting-up-cloud-data-ingestion-in-aws) usada para outras sincronizações).
2. Ao configurar a sincronização na Braze, defina **Data Type** como **Delete Users**.
3. Faça upload de arquivos para o seu bucket S3 que contenham apenas colunas de identificadores de usuários. Não inclua uma coluna `PAYLOAD` — a sincronização falhará se a carga útil estiver presente, para evitar exclusões acidentais.

Cada linha no arquivo deve identificar exatamente um usuário usando uma das seguintes opções:

| Identificador | Descrição |
| --- | --- |
| `EXTERNAL_ID` | Corresponde ao `external_id` usado na Braze. |
| `ALIAS_NAME` e `ALIAS_LABEL` | Ambas as colunas juntas identificam o usuário por alias. |
| `BRAZE_ID` | ID de usuário gerado pela Braze (somente usuários existentes). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Excluindo usuários" }

{% alert important %}
A exclusão de usuários é permanente e não pode ser desfeita. Inclua apenas os usuários que você pretende remover. Para mais detalhes, consulte [Excluir usuários com ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users).
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

Quando a sincronização é executada, a Braze processa os novos arquivos no bucket e exclui os perfis de usuário correspondentes.

### Excluindo itens de catálogo {#deleting-catalog-items}

Para remover itens de um catálogo usando armazenamento de arquivos:

1. Use a mesma sincronização S3 que você usa para [sincronizar dados de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) (tipo de dados **Catalogs**).
2. Nos seus arquivos CSV ou JSON, adicione uma coluna opcional **`deleted`** (ou **`DELETED`**).
3. Defina `deleted` como `true` para qualquer item de catálogo que você deseja remover do catálogo na Braze.

Cada linha ainda precisa de `ID` e `PAYLOAD`. Para linhas marcadas para exclusão, a carga útil pode ser mínima; a Braze remove o item pelo `ID`.

**Exemplo – JSON (exclusão de item de catálogo):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Exemplo – CSV (exclusão de item de catálogo):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Quando a sincronização é executada, as linhas com `deleted: true` fazem com que o item de catálogo correspondente seja excluído na Braze. Para ver o comportamento completo de sincronização e exclusão de catálogos, consulte [Sincronizar e excluir dados de catálogo]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).

## Informações importantes {#things-to-know}

- Os arquivos adicionados ao bucket S3 de origem não devem exceder 512&nbsp;MB. Arquivos maiores que 512&nbsp;MB resultam em erro e não são sincronizados com a Braze.
- Embora não haja limite adicional para o número de linhas por arquivo, recomendamos usar arquivos menores para melhorar a velocidade das suas sincronizações. Por exemplo, um arquivo de 500&nbsp;MB levaria consideravelmente mais tempo para ser ingerido do que cinco arquivos separados de 100&nbsp;MB.
- Não há limite adicional para o número de arquivos enviados em um determinado período.
- A ordenação não é suportada dentro dos arquivos nem entre eles. Recomendamos agrupar as atualizações periodicamente se você estiver monitorando possíveis condições de corrida.

## Solução de problemas {#troubleshooting}

### Upload de arquivos e processamento {#uploading-files-and-processing}

A CDI só processa arquivos adicionados após a criação da sincronização. Nesse processo, a Braze verifica se novos arquivos foram adicionados, o que dispara uma nova mensagem para o SQS. Isso inicia uma nova sincronização para processar o novo arquivo.

Você pode usar arquivos existentes para validar se a Braze consegue acessar seu bucket e detectar arquivos para ingestão, mas eles não são sincronizados com a Braze. Para que a CDI os processe, você precisa fazer o re-upload para o S3 de qualquer arquivo existente que deseja sincronizar.

### Lidando com erros inesperados de arquivo {#handling-unexpected-file-errors}

Se você está observando um número alto de erros ou arquivos com falha, pode ser que outro processo esteja adicionando arquivos ao bucket S3 em uma pasta diferente da pasta de destino da CDI.

Quando arquivos são enviados para o bucket de origem, mas não na pasta de origem, a CDI processa a notificação do SQS, porém não executa nenhuma ação no arquivo. Isso pode aparecer como um erro.

Se o seu problema está relacionado a notificações do S3 ou permissões de destino do SQS (por exemplo, erros de validação de destino), consulte a documentação da AWS:

- [Ativando e configurando notificações de eventos usando o console do Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Concedendo permissões para publicar mensagens de notificação de eventos em um destino](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Solução de problemas no Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)