---
nav_title: Exportação de eventos de segurança com S3
article_title: Exportação de Configurações de Segurança com S3
page_order: 1
page_type: reference
description: "Este artigo de referência cobre como exportar automaticamente eventos de segurança todos os dias à meia-noite UTC para o Amazon S3."
---

# Exportação de eventos de segurança com Amazon S3

> Você pode exportar automaticamente eventos de segurança para o Amazon S3, um provedor de armazenamento em nuvem, com um trabalho diário que é executado à meia-noite UTC. Após a configuração, você não precisa exportar manualmente eventos de segurança do dashboard. O trabalho exporta os eventos de segurança das últimas 24 horas em formato CSV para o seu armazenamento S3 configurado. O arquivo CSV tem a mesma estrutura que um relatório exportado manualmente.

{% alert note %}
O limite de 10.000 linhas se aplica apenas ao download manual do relatório CSV do dashboard. As exportações de eventos de segurança para S3 não estão sujeitas a esse limite de linhas.
{% endalert %}

Braze suporta dois métodos diferentes de autenticação e autorização S3 para configurar a exportação do Amazon S3:

- Método da chave de acesso secreta da AWS
- Método ARN da função AWS

## Método da chave de acesso secreta da AWS

Este método gera uma chave secreta e um ID de chave de acesso que permite à Braze se autenticar como um usuário na sua conta AWS para gravar dados no seu bucket.

### Etapa 1: Crie um usuário de Gerenciamento de Identidade e Acesso (IAM)

Para recuperar sua chave de acesso secreta e ID de chave de acesso, você precisará criar um usuário IAM, seguindo as instruções em [Configurando sua conta AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Etapa 2: Obtenha as credenciais

1. Após criar um novo usuário, gere a chave de acesso e baixe seu ID de chave de acesso e chave de acesso secreta.

![Uma página de resumo para uma função chamada "liyu-chen-test".]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2. Anote essas credenciais em algum lugar ou baixe os arquivos de credenciais, pois você precisará inseri-las na Braze posteriormente.

![Campos contendo a chave de acesso e a chave de acesso secreta.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Etapa 3: Crie uma política

1. Acesse **IAM** (Gerenciamento de Identidade e Acesso) > **Policies** > **Create Policy** para adicionar permissões ao seu usuário.
2. Selecione **Create Your Own Policy**, que concede permissões limitadas para que a Braze possa acessar apenas os buckets especificados.
3. Especifique um nome de política de sua escolha.
4. Insira o seguinte trecho de código na seção **Policy Document**. Certifique-se de substituir "INSERTBUCKETNAME" pelo nome do seu bucket. Sem essas permissões, a integração falhará na verificação de credenciais e não será criada.

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

### Etapa 4: Anexe a política

1. Após criar uma nova política, acesse **Users** e selecione seu usuário específico.
2. Na guia **Permissions**, selecione **Add Permissions**, anexe diretamente a política e selecione essa política.

Agora você está pronto para vincular suas credenciais AWS à sua conta da Braze!

### Etapa 5: Vincule a Braze à AWS

1. Na Braze, acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança** e role até a seção **Security Event Download**.
2. Ative **Export to AWS S3** em **Export to cloud storage** e selecione **AWS secret access key**, que ativa a exportação S3.
3. Insira as seguintes informações:
- ID da chave de acesso AWS
- Chave de acesso secreta AWS
    - Ao inserir essa chave, primeiro selecione **Test Credentials** para confirmar que suas credenciais funcionam.
- Nome do bucket AWS

![A página "Security Event Download" com os campos de conta da Braze e IDs externos da Braze preenchidos.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4. Selecione **Salvar alterações**.

![Botão "Salvar alterações".]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

Você integrou o AWS S3 à sua conta da Braze!

## Método ARN da função AWS

O método ARN da função AWS gera um Nome de Recurso Amazon (ARN) de função que permite à conta Amazon da Braze se autenticar como membro dessa função.

### Etapa 1: Crie uma política

1. Faça login no console de gerenciamento da AWS como administrador da conta.
2. No console da AWS, acesse a seção **IAM** (Gerenciamento de Identidade e Acesso) > **Policies** e selecione **Create Policy**.

![Uma página com uma lista de políticas e um botão para "Create policy".]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3. Abra a guia **JSON** e insira o seguinte trecho de código na seção **Policy Document**. Certifique-se de substituir `INSERTBUCKETNAME` pelo nome do seu bucket.

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

{: start="4"}
4. Selecione **Next** após revisar a política.

![Uma página que permite revisar sua política e, opcionalmente, adicionar permissões.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5. Dê um nome e uma descrição à política e selecione **Create Policy**.

![Uma página para revisar e criar sua política.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Etapa 2: Crie uma função

1. Na Braze, acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança** e role até a seção **Security Event Download**.
2. Selecione **AWS Role ARN**.
3. Anote os identificadores, o ID da conta da Braze e o ID externo da Braze necessários para criar sua função.

![A página "Security Event Download" com os campos de conta da Braze e IDs externos da Braze preenchidos.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. No console da AWS, acesse a seção **IAM** (Gerenciamento de Identidade e Acesso) > **Roles** > **Create Role**.
5. Selecione **Another AWS Account** como o tipo de seletor de entidade confiável.
6. Forneça o ID da sua conta da Braze, marque a caixa **Require external ID** e insira o ID externo da Braze.
7. Selecione **Next** quando concluir.

![Uma página com opções para selecionar um tipo de entidade confiável e fornecer informações sobre sua conta AWS.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Etapa 3: Anexe a política

1. Pesquise a política que você criou anteriormente na barra de pesquisa e marque a caixa de seleção ao lado da política para anexá-la.
2. Selecione **Next**.

![Uma lista de políticas com colunas para tipo e descrição.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3. Dê um nome e uma descrição à função e selecione **Create Role**.

![Campos para fornecer detalhes da função, como nome, descrição, política de confiança, permissões e tags.]({% image_buster /assets/img/security_export/name_review_create.png %})

Sua função recém-criada aparecerá na lista!

### Etapa 4: Vincule à Braze AWS

1. No console da AWS, encontre sua função recém-criada na lista. Selecione o nome para abrir os detalhes dessa função e anote o **ARN**.

![A página de resumo para uma função chamada "security-event-export-olaf".]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2. Na Braze, acesse **Configurações** > **Configurações da empresa** > **Configurações de administrador** > **Configurações de segurança** e role até a seção **Security Event Download**.

![Seção "Security Event Download" com a opção "Export to AWS S3" ativada.]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3. Certifique-se de que **AWS role ARN** esteja selecionado e insira o ARN da sua função e o nome do bucket AWS S3 nos campos designados.
4. Selecione **Test Credentials** para confirmar que suas credenciais funcionam corretamente.
5. Selecione **Salvar alterações**.

![Botão "Salvar alterações".]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

Você integrou o AWS S3 à sua conta da Braze!