---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "Este artigo de referência descreve a parceria entre a Braze e o Amazon S3, um sistema de armazenamento altamente escalável oferecido pela Amazon Web Services."
page_type: partner
search_tag: Partner

---

# Amazon S3

> O [Amazon S3](https://aws.amazon.com/s3/) é um sistema de armazenamento altamente escalável oferecido pela Amazon Web Services.

{% alert important %}
Se estiver alternando entre provedores de armazenamento em nuvem, entre em contato com o seu CSM da Braze para obter mais assistência na configuração e validação da nova integração.
{% endalert %}

A integração da Braze com o Amazon S3 apresenta duas estratégias de integração:

- Alavancar o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), que permite armazenar dados até que você queira conectá-los a outras plataformas, ferramentas e locais.
- Usar exportações de dados do dashboard (como exportações CSV e relatórios de engajamento).

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Amazon S3 | Você precisa de uma conta Amazon S3 para aproveitar essa parceria. |
| Bucket S3 dedicado | Antes de integrar com o Amazon S3, você deve criar um bucket S3 para o seu app.<br><br>Se você já tem um bucket S3, ainda recomendamos criar um novo bucket especificamente para a Braze, para que você possa limitar as permissões. Consulte as instruções a seguir sobre como criar um novo bucket. |
| Currents | Para exportar dados de volta para o Amazon S3, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) configurado para a sua conta. O Currents não é necessário se você estiver configurando apenas o arquivamento de mensagens. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Criando um novo bucket S3 {#creating-a-new-s3-bucket}

Para criar um bucket para o seu app, faça o seguinte:

1. Abra o [console do Amazon S3](https://console.aws.amazon.com/s3/) e siga as instruções para **Sign in** ou **Create an Account with AWS**.
2. Após fazer login, selecione **S3** na categoria **Storage & Content Delivery**.
3. Selecione **Create Bucket** na tela seguinte.
4. Quando solicitado, crie seu bucket e selecione uma região AWS.

A Braze não permite que você escolha ou configure uma região no dashboard. A região AWS é fixada pelo local onde você cria o bucket no console da AWS. A integração envia dados para o nome do bucket que você fornecer, e a AWS roteia automaticamente as solicitações para a região do bucket. Se o seu conector tentar se conectar a uma região diferente da desejada (por exemplo, `eu-west-1` em vez de `eu-central-1`), crie ou use um bucket S3 na região desejada na AWS. Não há nada para alterar no lado da Braze.

{% alert note %}
O Currents não oferece suporte a buckets com [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) configurado.
{% endalert %}

## Integração {#integration}

A Braze tem duas estratégias de integração diferentes com o Amazon S3—uma para o [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) e outra para todas as exportações de dados do dashboard (como exportações de CSV ou relatórios de engajamento). Ambas as integrações suportam dois métodos diferentes de autenticação ou autorização:

- [Método de chave de acesso secreta da AWS](#aws-secret-key-auth-method)
- [Método de ARN de função da AWS](#aws-role-arn-auth-method)

## Método de autenticação por chave secreta da AWS {#aws-secret-key-auth-method}

Esse método de autenticação gera uma chave secreta e um ID de chave de acesso que permite à Braze se autenticar como um usuário na sua conta AWS para gravar dados no seu bucket.

### Etapa 1: Criar usuário {#secret-key-1}

{% alert note %}
Se você está configurando apenas o arquivamento de mensagens, siga as etapas na guia **Dashboard Data Export**.
{% endalert %}

Para recuperar seu ID de chave de acesso e sua chave de acesso secreta, [crie um usuário IAM e um grupo de administradores na AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Etapa 2: Obter credenciais {#secret-key-2}

Após criar um novo usuário, selecione **Show User Security Credentials** para revelar seu ID de chave de acesso e sua chave de acesso secreta. Em seguida, anote essas credenciais em algum lugar ou selecione o botão **Download Credentials**, pois você precisará inseri-las no dashboard da Braze posteriormente.

![Página de credenciais de segurança do usuário AWS IAM mostrando o ID da chave de acesso e a chave de acesso secreta.]({% image_buster /assets/img_archive/S3_Credentials.png %})

### Etapa 3: Criar política {#secret-key-3}

Navegue até **Policies** > **Get Started** > **Create Policy** para adicionar permissões ao seu usuário. Em seguida, selecione **Create Your Own Policy**. Isso concede permissões limitadas, de forma que a Braze só possa acessar os buckets especificados.

![Tela de criação de política do AWS IAM com opções de política para a integração com o S3.]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Diferentes políticas são necessárias para Currents e Dashboard Data Export. `s3:GetObject` é necessário para permitir que o backend da Braze realize o tratamento de erros.
{% endalert %}

Especifique um nome de política de sua preferência e insira o seguinte trecho de código na seção **Policy Document**. Certifique-se de substituir `INSERTBUCKETNAME` pelo nome do seu bucket. Sem essas permissões, a integração falha na verificação de credenciais e não será criada.

{% alert note %}
Se você está configurando apenas o arquivamento de mensagens, use o trecho de código na guia **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Dashboard Data Export %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### Etapa 4: Vincular política {#secret-key-4}

Após criar uma nova política, acesse **Users** e selecione o usuário específico. Na guia **Permissions**, selecione **Attach Policy** e escolha a nova política que você criou. Agora, você está pronto para vincular suas credenciais da AWS à sua conta Braze.

![Guia de permissões do usuário AWS IAM com a ação Attach Policy selecionada.]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### Etapa 5: Vincular a Braze à AWS {#secret-key-5}

{% alert note %}
Se você está configurando apenas o arquivamento de mensagens, siga as etapas na guia **Dashboard Data Export**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Na Braze, acesse **Partner Integrations** > **Currents**.

Em seguida, selecione **Create New Current** e depois **Amazon S3 Data Export**.

Dê um nome ao seu Current. Na seção **Credentials**, verifique se **AWS Secret Access Key** está selecionado e insira seu ID de acesso S3, a chave de acesso secreta da AWS e o nome do bucket AWS S3 nos campos designados.

{% multi_lang_include currents/contact_email_notifications.md %}

![Formulário de criação de novo Current na Braze para Amazon S3 com campos de credenciais de chave secreta da AWS.]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Mantenha seu ID de chave de acesso e sua chave de acesso secreta da AWS sempre atualizados. Se as credenciais do seu conector expirarem, o conector para de enviar eventos. Se isso persistir por mais de **5 dias**, os eventos do conector são descartados e os dados são permanentemente perdidos.
{% endalert %}

Você também pode adicionar as seguintes personalizações conforme sua necessidade:

- **Folder jornada:** O padrão é `currents`. Se essa pasta não existir, a Braze cria uma automaticamente para você.
- **Server-Side, At-Rest AES-256 Encryption:** O padrão é DESATIVADO e inclui o cabeçalho `x-amz-server-side-encryption`.

Selecione **Launch Current** para continuar.

Uma notificação informa se suas credenciais foram validadas com sucesso. O AWS S3 está agora configurado para o Braze Currents.

{% endtab %}
{% tab Dashboard Data Export %}

Na Braze, acesse **Partner Integrations** > **Technology Partners** e selecione **Amazon S3**.

Na página **AWS Credentials**, verifique se **AWS Secret Access Key** está selecionado e insira seu ID de acesso da AWS, a chave de acesso secreta da AWS e o nome do bucket AWS S3 nos campos designados. Ao inserir sua chave secreta, selecione **Test Credentials** primeiro para garantir que suas credenciais funcionam e, em seguida, selecione **Save** quando a validação for bem-sucedida.

![Página de credenciais da parceira de tecnologia Amazon S3 na Braze com ações de teste e salvamento.]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Você pode recuperar novas credenciais a qualquer momento navegando até o seu usuário e selecionando **Create Access Key** na guia **Security Credentials** no console da AWS.
{% endalert %}

Uma notificação informa se suas credenciais foram validadas com sucesso. O AWS S3 está agora integrado à sua conta Braze.

{% endtab %}
{% endtabs %}

## Método de autenticação por ARN de função da AWS {#aws-role-arn-auth-method}

Esse método de autenticação gera um Amazon Resource Name (ARN) de função que permite que a conta Amazon da Braze se autentique como membro da função que você criou para gravar dados no seu bucket.

### Etapa 1: Criar política {#role-arn-1}

Para começar, faça login no console de gerenciamento da AWS como administrador de conta. Navegue até a seção IAM do Console da AWS, selecione **Policies** na barra de navegação e selecione **Create Policy**.

![Página de políticas do AWS IAM com o botão Create Policy selecionado.]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Políticas diferentes são necessárias para o Currents e para a exportação de dados do dashboard. O `s3:GetObject` é necessário para permitir que o backend da Braze realize o tratamento de erros.
{% endalert %}

Abra a guia **JSON** e insira o trecho de código a seguir na seção **Policy Document**. Substitua `INSERTBUCKETNAME` pelo nome do seu bucket. Selecione **Review Policy** quando terminar.

{% alert note %}
Se você estiver configurando apenas o arquivamento de mensagens, use o trecho de código na guia **Exportação de dados do dashboard**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Exportação de dados do dashboard %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

Em seguida, dê um nome e uma descrição para a política e selecione **Create Policy**.

![Etapa de revisão de política do AWS IAM com campos para nome e descrição da política.]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![Lista de políticas do AWS IAM mostrando a política S3 recém-criada.]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Etapa 2: Criar função {#role-arn-2}

Na mesma seção IAM do console, selecione **Roles** > **Create Role**.

![Página de funções do AWS IAM com o botão Create Role selecionado.]({{site.baseurl}}/assets/img/create_role_1_list.png)

Obtenha o ID da conta e o ID externo da Braze na sua conta da Braze:

- **Currents:** Na Braze, acesse **Integrações com parceiros** > **Currents**. Em seguida, selecione **Create New Current** e depois **Amazon S3 Data Export**. Lá, você encontrará os identificadores necessários para criar sua função.
- **Exportação de dados do dashboard:** Na Braze, acesse **Integrações com parceiros** > **Parceiros de tecnologia** e selecione **Amazon S3**. Lá, você encontrará os identificadores necessários para criar sua função. (Crie suas funções aqui se estiver configurando apenas o arquivamento de mensagens.)

De volta ao Console da AWS, selecione **Another AWS Account** como tipo de entidade confiável no seletor. Forneça o ID da sua conta da Braze, marque a caixa **Require external ID** e insira o ID externo da Braze. Selecione **Next** quando terminar.

![A página "Create Role" do S3. Esta página tem campos para nome da função, descrição da função, entidades confiáveis, políticas e limite de permissões.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Etapa 3: Vincular política {#role-arn-3}

Em seguida, vincule a política que você criou anteriormente à função. Pesquise a política na barra de pesquisa e marque a caixa de seleção ao lado da política para vinculá-la. Selecione **Next** quando terminar.

![ARN da função]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Dê um nome e uma descrição para a função e selecione **Create Role**.

![ARN da função]({{site.baseurl}}/assets/img/create_role_4_name.png)

Agora você verá a função recém-criada na lista.

### Etapa 4: Vincular ao AWS da Braze {#role-arn-4}

No Console da AWS, encontre a função recém-criada na lista. Selecione o nome para abrir os detalhes dessa função.

![Página de detalhes da função do AWS IAM para a função recém-criada.]({{site.baseurl}}/assets/img/create_role_5_created.png)

Anote o **Role ARN** na parte superior da página de resumo da função.

![Resumo da função do AWS IAM mostrando o valor do Role ARN.]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Volte para a sua conta da Braze e copie o ARN da função no campo fornecido.

{% alert note %}
Se você estiver configurando apenas o arquivamento de mensagens, siga as etapas na guia **Exportação de dados do dashboard**.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Na Braze, acesse **Integrações com parceiros** > **Currents**. Em seguida, selecione **Create New Current** e selecione **Amazon S3 Data Export**.

![Tela de configuração do Braze Currents para Amazon S3 com campos de AWS Role ARN e bucket.]({{site.baseurl}}/assets/img/currents-role-arn.png)

Dê um nome ao seu Current. Em seguida, na seção **Credenciais**, verifique se **AWS Role ARN** está selecionado e forneça o ARN da função e o nome do bucket AWS S3 nos campos designados.

{% multi_lang_include currents/contact_email_notifications.md %}

Você também pode adicionar as seguintes personalizações conforme suas necessidades:

- Caminho da pasta (o padrão é `currents`)
- Criptografia AES-256 no lado do servidor em repouso (o padrão é DESLIGADO) - Inclui o header `x-amz-server-side-encryption`

Selecione **Launch Current** para continuar. Uma notificação indica se suas credenciais foram validadas com sucesso. O AWS S3 agora está configurado para o Braze Currents.

{% alert important %}
Se você receber um erro "S3 credentials are invalid", isso pode ter ocorrido por integrar rápido demais após criar uma função na AWS. Aguarde e tente novamente. Se a mensagem mencionar acesso `PutObject` ou criptografia no lado do servidor em exportações de dados do dashboard, consulte [Solução de problemas de erros de credenciais do S3](#troubleshooting).
{% endalert %}

{% endtab %}
{% tab Exportação de dados do dashboard %}

Na Braze, acesse a página **Parceiros de tecnologia** em **Integrações** e selecione **Amazon S3**.

![Página da parceira de tecnologia Amazon S3 na Braze com credenciais AWS Role ARN selecionadas.]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Na página **AWS Credentials**, verifique se o botão de opção **AWS Role ARN** está selecionado e insira o ARN da função e o nome do bucket AWS S3 nos campos designados. Selecione **Test Credentials** primeiro para confirmar que suas credenciais funcionam corretamente e, em seguida, selecione **Save** quando for bem-sucedido.

{% alert tip %}
Você pode recuperar novas credenciais a qualquer momento navegando até seu usuário e selecionando **Create Access Key** na guia **Security Credentials** dentro do Console da AWS.
{% endalert %}

Uma notificação informa se suas credenciais foram validadas com sucesso. O AWS S3 agora está integrado à sua conta da Braze.

{% endtab %}
{% endtabs %}

## Atualização das credenciais do Amazon S3 para Currents {#updating-currents-credentials}

Você pode atualizar as credenciais do Amazon S3 em um conector Braze Currents existente sem interromper a integração ou perder dados já exportados para o seu bucket.

Para atualizar as credenciais — ou para alternar entre **AWS Secret Access Key** e **AWS Role ARN** — conclua as etapas do lado do IAM e da AWS para o método escolhido descritas anteriormente neste artigo (políticas, usuário ou função e identificadores conforme necessário).

Quando terminar de preparar as credenciais na AWS, acesse **Integrações de parceiros** > **Currents** na Braze, localize seu conector Amazon S3 na lista, selecione **Edit**, atualize as **Credentials** e selecione **Update Current**. A Braze valida as credenciais inseridas; seu conector continua funcionando e os dados já no seu bucket permanecem disponíveis. Para saber mais, consulte [Atualização de Currents em Configurar Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents).

## Comportamento de exportação {#export-behavior}

Usuários que integraram uma solução de armazenamento de dados em nuvem e APIs de exportação, relatórios do dashboard ou relatórios CSV terão o seguinte comportamento:

- Todas as exportações de API não retornam uma URL de download no corpo da resposta e devem ser recuperadas por meio do armazenamento de dados.
- Todos os relatórios do dashboard e relatórios CSV são enviados para o e-mail do usuário para download (sem necessidade de permissões de armazenamento) e têm backup no armazenamento de dados.

### Erro `Unable to connect to S3, please validate that your credentials are correct` {#unable-to-connect-to-s3-please-validate-that-your-credentials-are-correct-error}

Se esse erro aparecer ao fazer download de uma exportação CSV, abra a integração do [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) na página **Parceiros de tecnologia** e selecione **Test Credentials**. O resultado explica o que falhou na validação — por exemplo, a chave pode estar sem a permissão `GetObject`, o que impede a Braze de gerar links de download.

Atualize sua política IAM para que o usuário ou a role de integração possa chamar `s3:GetObject` no bucket S3 e no caminho do objeto configurado na sua integração com a Braze. Para saber mais sobre problemas de exportação, consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).

{% alert important %}
**Requisito de formato JSON:** Para exportações JSON, a Braze utiliza o formato JSONL (JSON delimitado por nova linha), em que cada linha contém um objeto JSON separado. Esse formato difere do JSON padrão, que é um único array ou objeto JSON. Cada linha no arquivo exportado é um objeto JSON válido, mas o arquivo como um todo não é um documento JSON único e válido. Ao processar esses arquivos, analise cada linha individualmente como um objeto JSON separado, em vez de tentar analisar o arquivo inteiro como um único documento JSON.

As exportações do Currents usam o formato Apache Avro (arquivos `.avro`), e não JSON. Esse requisito de formato JSON se aplica a exportações de dados do dashboard e exportações de API.
{% endalert %}

## Múltiplos conectores {#multiple-connectors}

Se você pretende criar mais de um conector do Currents para enviar dados ao seu bucket S3, pode usar as mesmas credenciais, mas deve especificar um caminho de pasta diferente para cada um. Você pode criá-los no mesmo espaço de trabalho ou dividi-los e criá-los em vários espaços de trabalho. Também é possível criar uma política separada para cada integração ou criar uma única política que cubra ambas as integrações.

Se você planeja usar o mesmo bucket S3 tanto para o Currents quanto para exportações de dados, será necessário criar duas políticas separadas, pois cada integração requer permissões diferentes.

## Solução de problemas {#troubleshooting}

### Erro: A conta não tem acesso a `PutObject` {#error-account-does-not-have-putobject-access}

Se você ver o seguinte erro ao salvar credenciais do Amazon S3 para exportações de dados do dashboard, pode ser devido a permissões incorretas ou configurações de criptografia no lado do servidor.

```
S3 Credentials are invalid because this account does not have 'PutObject access'. Please check the permissions and ensure that this key has access to 'PutObject' in the 'CUSTOMER-BUCKET-HERE' bucket.
```

Para resolver esse problema, verifique as seguintes áreas.

#### Política de bucket incorreta {#incorrect-bucket-policy}

Confirme se você criou uma política com as permissões corretas, conforme descrito em [Integração com o Amazon S3](#integration) (use a política de **Dashboard Data Export** para o seu método de autenticação).

#### Criptografia no lado do servidor {#server-side-encryption}

```
User: arn:aws:sts::XXX:assumed-role/braze-iam-role/braze is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:XXX because no identity-based policy allows the kms:GenerateDataKey action
```

Se você receber essa mensagem de erro do [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou nos logs do AWS, seu bucket S3 está configurado com criptografia AWS Key Management Service (SSE-KMS). A Braze não oferece suporte a SSE-KMS para Currents ou exportações de dados do dashboard. Para resolver isso, desative o SSE-KMS no seu bucket S3.

{% alert note %}
A Braze oferece suporte à criptografia no lado do servidor usando chaves gerenciadas pelo S3 (SSE-S3), que é compatível tanto com Currents quanto com exportações de dados do dashboard.
{% endalert %}

#### Verificar permissões adicionais {#check-additional-permissions}

Certifique-se de que você tem as permissões necessárias, incluindo `s3:GetBucketLocation` e `s3:PutObject`.