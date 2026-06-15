---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Este artigo de referência descreve a parceria entre a Braze e a Fivetran, uma ferramenta de automação de fluxo de trabalho que pode ajudá-lo na tomada de decisões com base em dados, fornecendo dados prontos para consulta em seu data warehouse na nuvem."
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [A Fivetran](https://fivetran.com/) é uma marca reconhecida mundialmente, cujos produtos voltados para analistas e pipelines totalmente gerenciados viabilizam decisões baseadas em dados, fornecendo dados prontos para consulta em seu data warehouse na nuvem.

A integração da Braze com a Fivetran permite que os usuários criem um pipeline sem manutenção que possibilita coletar e analisar dados da Braze conectando todos os seus aplicativos e bancos de dados a um data warehouse central. Depois que os dados são coletados no data warehouse central, as equipes de dados podem explorar os dados da Braze de forma eficaz usando suas ferramentas de business intelligence preferidas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Fivetran | É necessário ter uma conta [Fivetran](https://fivetran.com/login?next=%2Fdashboard) para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as seguintes permissões:<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze  | Sua URL de endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/api/basics/#api-definitions). |
| Braze Currents | O [Braze Currents](https://www.braze.com/product/data-agility-management/currents/) deve estar conectado ao Amazon S3 ou ao Google Cloud Storage. |
| Amazon S3 ou Google Cloud Storage | Essa integração exige que você tenha acesso a um Amazon S3 ou Google Cloud Storage. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integração {#integration}

A seguinte integração do Currents é compatível com o [Amazon S3](#setting-up-braze-currents-for-s3) e o [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage).

### Configuração do Braze Currents para S3 {#setting-up-braze-currents-for-s3}

#### Etapa 1: localize seu ID externo {#step-one}

No [dashboard da Fivetran](https://fivetran.com/dashboard), selecione **+ Connector** e, em seguida, selecione o conector **Braze** para iniciar o formulário de configuração. Em seguida, selecione **Amazon S3**. Anote o ID externo fornecido aqui; você precisará dele para permitir que a Fivetran acesse seu bucket S3.

![O formulário do conector Fivetran para a Braze. O campo de ID externo necessário para esta etapa está localizado no meio da página em uma caixa cinza claro.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### Etapa 2: conceda à Fivetran acesso a um bucket S3 especificado {#step-2-give-fivetran-access-to-a-specified-s3-bucket}

##### Criação de uma política de IAM {#creating-an-iam-policy}

Abra o [Console do Amazon IAM](https://console.aws.amazon.com/iam/home#home) e navegue até **Policies > Create Policy**.

![Console do Amazon IAM com a lista de políticas.]({% image_buster /assets/img/fivetran_as3_iam.png %})

Em seguida, abra a guia **JSON** e cole a seguinte política. Substitua `{your-bucket-name}` pelo nome do seu bucket S3.

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

Por fim, selecione **Review Policy** e dê à política um nome e uma descrição exclusivos. Selecione **Create Policy** para criar sua política.

![Campos para nomear a política e fornecer uma descrição.]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### Criar uma função de IAM {#step-two}

Na AWS, navegue até **Roles** e selecione **Create New Role**.

![A página "Roles" com o botão para criar uma nova função.]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Selecione **Another AWS Account** e forneça o ID da conta Fivetran `834469178297`. Certifique-se de marcar a caixa de seleção **Require external ID**. Aqui você fornecerá o ID externo encontrado na etapa 1.

![O campo para inserir seu "Account ID", uma caixa de seleção para exigir o ID externo e uma caixa de texto em branco para inserir seu "External ID".]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Em seguida, selecione **Next: Permissions** para selecionar a política que você acabou de criar.

![Lista de políticas.]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Selecione **Next: Review**, nomeie sua nova função (como Fivetran) e selecione **Create Role**. Depois que a função for criada, selecione-a e anote o Role ARN exibido.

![O ARN do Amazon S3 listado na função.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Você pode especificar permissões para o Role ARN que designar para a Fivetran. A concessão de permissões seletivas a essa função permitirá que a Fivetran sincronize apenas o que tem permissão para ver.
{% endalert %}

#### Etapa 3: complete o conector Fivetran {#step-3-complete-the-fivetran-connector}

Na Fivetran, selecione **+ Connector** e, em seguida, selecione o conector **Braze** para abrir o formulário de configuração. No formulário, preencha os campos fornecidos com os valores apropriados:
- `Destination schema`: um nome de esquema exclusivo.
- `API URL`: seu endpoint da REST API da Braze.
- `API Key`: sua chave da API REST da Braze.
- `External ID`: o ID externo definido na [etapa 2](#step-two) das instruções de configuração do Currents. Esse ID é um valor fixo.
- `Bucket`: encontrado em sua conta Braze, navegando até **Integrações de parceiros** > **Exportação de dados** > nome do seu Current.
- `Role ARN`: o Role ARN pode ser encontrado na [etapa 1](#step-one) das instruções de configuração do Current.

{% alert important %}
Certifique-se de que **Amazon S3** esteja selecionado como a opção de **Cloud Storage**.
{% endalert %}

Por fim, selecione **Save & Test** e a Fivetran fará o resto, sincronizando com os dados da sua conta Braze!

### Configuração do Braze Currents para o Google Cloud Storage {#setting-up-braze-currents-for-google-cloud-storage}

#### Etapa 1: recupere seu e-mail da Fivetran no Google Cloud Storage {#step-one2}

No [dashboard da Fivetran](https://fivetran.com/dashboard), selecione **+ Connector** e, em seguida, selecione o conector **Braze** para iniciar o formulário de configuração. Em seguida, selecione **Google Cloud Storage**. Anote o endereço de e-mail que aparece.

![O formulário do conector Fivetran para a Braze. O campo de e-mail necessário para essa etapa está localizado no meio da página, em uma caixa cinza claro.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### Etapa 2: conceda acesso ao bucket {#step-2-grant-bucket-access}

Navegue até o [Google Storage Console](https://console.cloud.google.com/storage/browser), selecione o bucket com o qual você configurou o Braze Currents e selecione **Edit bucket permissions**.

![Os buckets disponíveis no Google Storage Console. Localize um bucket e selecione o ícone de três pontos verticais para abrir o menu suspenso que permite editar as permissões do bucket.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

Em seguida, conceda acesso de `Storage Object Viewer` ao e-mail da [etapa 1](#step-one2), adicionando-o como membro. Anote o nome do bucket; você precisará dele na próxima etapa para configurar a Fivetran.

![Bucket com permissões.]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### Etapa 3: complete o conector Fivetran

Na Fivetran, selecione **+ Connector** e, em seguida, selecione o conector **Braze** para abrir o formulário de configuração. No formulário, preencha os campos fornecidos com os valores apropriados:
- `Destination schema`: um nome de esquema exclusivo.
- `API URL`: seu endpoint da REST API da Braze.
- `API Key`: sua chave da API REST da Braze.
- `Bucket Name`: encontrado em sua conta Braze, navegando até **Integrações de parceiros** > **Exportação de dados** > nome do seu Current.
- `Folder`: encontrado em sua conta Braze, navegando até **Integrações de parceiros** > **Exportação de dados** > nome do seu Current.

{% alert important %}
Certifique-se de que **Google Cloud Storage** esteja selecionado como a opção de **Cloud Storage**.
{% endalert %}

Por fim, selecione **Save & Test** e a Fivetran fará o resto, sincronizando com os dados da sua conta Braze!