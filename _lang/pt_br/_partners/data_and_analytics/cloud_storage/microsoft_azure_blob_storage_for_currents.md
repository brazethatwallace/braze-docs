---
nav_title: Armazenamento de Blobs do Microsoft Azure
article_title: Armazenamento de Blobs do Microsoft Azure
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "Este artigo de referência descreve a parceria entre o Braze Currents e o Microsoft Azure Blob Storage, um armazenamento de objetos massivamente escalável para dados não estruturados."
page_type: partner
tool: Currents
search_tag: Partner

---

# Armazenamento de Blobs do Microsoft Azure {#microsoft-azure-blob-storage}

> O [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) é um armazenamento de objetos massivamente escalável para dados não estruturados oferecido pela Microsoft como parte do conjunto de produtos Azure.

{% alert important %}
Se estiver alternando entre provedores de armazenamento em nuvem, entre em contato com o gerente de sucesso do cliente da Braze para obter mais assistência na configuração e validação da nova integração.
{% endalert %}

A integração da Braze com o Microsoft Azure Blob Storage permite exportar dados de volta para o Azure e transmitir dados do Currents. Depois, você pode usar um processo ETL (Extract, Transform, Load) para transferir seus dados para outros locais.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Microsoft Azure e conta de armazenamento do Azure | Uma conta do Microsoft Azure e uma conta de armazenamento do Azure são necessárias para aproveitar essa parceria. |
| Currents | Para exportar dados para o Currents, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado para a sua conta. O Currents não é necessário se você estiver configurando apenas o arquivamento de mensagens. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para integrar com o Microsoft Azure Blob Storage, você deve ter uma conta de armazenamento e um contêiner para permitir que a Braze exporte dados de volta para o Azure ou transmita dados do Currents. A Braze oferece suporte a dois métodos de autenticação:

- [Método de string de conexão](#connection-string-auth-method)
- [Método de entidade de serviço com certificado](#certificate-service-principal-auth-method) (somente Currents)

## Método de autenticação por string de conexão {#connection-string-auth-method}

### Etapa 1: Criar uma conta de armazenamento {#step-1-create-a-storage-account}

No Microsoft Azure, navegue até **Storage Accounts** na barra lateral e clique em **+ Add** para criar uma nova conta de armazenamento. Em seguida, forneça um nome para a conta de armazenamento. As outras configurações padrão não precisarão ser atualizadas. Por fim, selecione **Review + create**.

Mesmo que você já tenha uma conta de armazenamento, recomendamos criar uma nova especificamente para os dados da Braze.

![A página de criação de conta de armazenamento do Microsoft Azure na guia Basics, com o campo de nome da conta de armazenamento em destaque.]({% image_buster /assets/img/azure-currents-step-1.png %})

### Etapa 2: Obter a string de conexão {#step-2-get-the-connection-string}

Depois que a conta de armazenamento for implantada, navegue até o menu **Access Keys** na conta de armazenamento e anote a string de conexão.

A Microsoft fornece duas chaves de acesso para manter conexões usando uma chave enquanto regenera a outra. Você só precisa da string de conexão de uma delas.

{% alert note %}
A Braze usa a string de conexão desse menu, não a chave.
{% endalert %}

![A página Access keys de uma conta de armazenamento do Azure, com o campo de string de conexão em key1 em destaque.]({% image_buster /assets/img/azure-currents-step-2.png %})

### Etapa 3: Criar um contêiner de serviço de blob {#step-3-create-a-blob-service-container}

Navegue até o menu **Blobs** na seção **Blob Service** da sua conta de armazenamento. Crie um contêiner de serviço de blob dentro da conta de armazenamento que você criou anteriormente.

Forneça um nome para o contêiner de serviço de blob. As outras configurações padrão não precisarão ser atualizadas.

![A página Blobs de uma conta de armazenamento do Azure em Blob Service, com a opção de adicionar um contêiner.]({% image_buster /assets/img/azure-currents-step-3.png %})

### Etapa 4: Configurar o Currents {#step-4-set-up-currents}

Na Braze, navegue até **Currents > + Create Current > Azure Blob Data Export** e forneça o nome da integração e o e-mail de contato.

Em seguida, forneça sua string de conexão, o nome do contêiner e o prefixo de BlobStorage (opcional).

![A página de Currents do Microsoft Azure Blob Storage na Braze. Nesta página, existem campos para nome da integração, e-mail de contato, string de conexão, nome do contêiner e prefixo.]({% image_buster /assets/img/maz.png %})

Por fim, role até o final da página e selecione quais eventos de engajamento com mensagem ou eventos de comportamento do cliente você deseja exportar. Quando concluído, inicie seu Current.

### Etapa 5: Configurar a exportação de dados do Azure {#step-5-set-up-azure-data-export}

A seguir, são configuradas as credenciais usadas para:
1. Exportações de Segment pela API
2. Exportações CSV (exportação de dados de usuários de Campaign, Segment e Canvas pelo dashboard)
3. Relatórios de engajamento

Na Braze, navegue até **Partner Integrations** > **Technology Partners** > **Microsoft Azure** e forneça sua string de conexão, o nome do contêiner de armazenamento do Azure e o prefixo de armazenamento do Azure.

Em seguida, verifique se a caixa **Make this the default data export destination** está marcada para garantir que seus dados exportados sejam enviados para o Azure. Quando concluído, salve sua integração.

![A página de exportação de dados do Microsoft Azure na Braze. Nesta página, existem campos para string de conexão, nome do contêiner e prefixo.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
É importante manter sua string de conexão atualizada. Se as credenciais do conector expirarem, ele deixará de enviar eventos. Se isso persistir por mais de 48 horas, os eventos do conector serão descartados e os dados serão permanentemente perdidos.
{% endalert %}

## Método de autenticação por entidade de serviço com certificado {#certificate-service-principal-auth-method}

Este método autentica no Microsoft Entra ID usando um certificado e, em seguida, grava no seu contêiner usando o controle de acesso baseado em função (RBAC) do Azure, sem uma chave de conta compartilhada. Está disponível apenas para o Braze Currents.

{% alert note %}
Você faz upload apenas do certificado público no Microsoft Entra ID — sua chave privada nunca é enviada ao Azure. A Braze armazena seu certificado e chave privada criptografados em repouso, concede acesso apenas por meio da função [Storage Blob Data Contributor](#cert-sp-4) que você atribui, e você pode revogar esse acesso a qualquer momento removendo o certificado do registro do seu app no Azure.
{% endalert %}

Antes de começar, [crie uma conta de armazenamento](#step-1-create-a-storage-account) e um [contêiner de serviço de blob](#step-3-create-a-blob-service-container) conforme descrito no [Método de string de conexão](#connection-string-auth-method).

### Etapa 1: Registrar um aplicativo {#cert-sp-1}

No Microsoft Azure, acesse **Microsoft Entra ID** > **App registrations** > **+ New registration**. Forneça um nome (por exemplo, `braze-currents`) e selecione **Register**. Para etapas detalhadas, consulte a documentação da Microsoft [Registrar um aplicativo na plataforma de identidade da Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).

Na página **Overview** do registro do seu novo app, anote os seguintes valores. Você fornecerá ambos à Braze na [Etapa 6](#cert-sp-6).

- **Application (client) ID**
- **Directory (tenant) ID**

### Etapa 2: Criar um certificado {#cert-sp-2}

A Braze autentica usando um certificado: você faz upload do **certificado público** no Azure e fornece à Braze o **certificado junto com sua chave privada**.

Para gerar um certificado autoassinado e uma chave privada RSA de 2048 bits sem criptografia, execute:

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem \
  -days 730 -nodes -subj "/CN=braze-currents"
```

Isso cria dois arquivos:

| Arquivo | Finalidade |
| ---- | ------- |
| `cert.pem` | Seu certificado público. Faça upload dele no Azure na próxima etapa. |
| `key.pem` | Sua chave privada. Nunca faça upload dela no Azure. Você a fornecerá à Braze na [Etapa 6](#cert-sp-6). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Arquivos de certificado" }

{% alert important %}
A chave privada deve estar sem criptografia — ela não pode ser protegida por uma senha. Faça upload apenas do certificado público no Azure; nunca faça upload da sua chave privada.
{% endalert %}

**Já tem um certificado?** Se você já possui um certificado como arquivo `.pfx` — por exemplo, do Azure Key Vault, da sua autoridade certificadora ou do [método PowerShell da Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-self-signed-certificate) — converta-o para o formato que a Braze exige em vez de gerar um novo:

```bash
# The public certificate to upload to Azure (Step 3)
openssl pkcs12 -in your-cert.pfx -nokeys -out cert.pem

# The certificate and its unencrypted private key to give to Braze (Step 6)
openssl pkcs12 -in your-cert.pfx -nodes -out braze-currents.pem
```

Insira a senha do seu `.pfx` quando solicitado. A flag `-nodes` exporta a chave privada sem criptografia, conforme exigido pela Braze.

### Etapa 3: Fazer upload do certificado {#cert-sp-3}

No registro do seu app, acesse **Certificates & secrets** > **Certificates** > **Upload certificate** e faça upload do arquivo `cert.pem` que você criou na etapa anterior. Adicione uma descrição e selecione **Add**. Para etapas detalhadas, consulte a documentação da Microsoft [Adicionar e gerenciar credenciais de app no Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials).

Anote a data de expiração do seu certificado. Consulte [Atualizando credenciais do Azure para o Currents](#updating-currents-credentials).

### Etapa 4: Conceder acesso à sua conta de armazenamento {#cert-sp-4}

Em seguida, conceda ao registro do seu app permissão para gravar no seu contêiner.

Acesse sua conta de armazenamento e selecione **Access Control (IAM)** > **+ Add** > **Add role assignment**. Então:

1. Na guia **Role**, selecione **[Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-contributor)**.
2. Na guia **Members**, selecione **User, group, or service principal**, selecione **+ Select members** e pesquise pelo nome do registro do app que você criou na [Etapa 1](#cert-sp-1).
3. Selecione **Review + assign**.

Para etapas detalhadas, consulte a documentação da Microsoft [Atribuir uma função do Azure para acesso a dados de blob](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access).

![A guia de atribuições de função do Access Control (IAM) de uma conta de armazenamento, mostrando uma entidade de serviço e um grupo com a função Storage Blob Data Contributor atribuída.]({% image_buster /assets/img/azure-currents-cert-sp-1.png %})

{% alert note %}
Atribua a função no nível da **conta de armazenamento** em vez de em um contêiner individual.
{% endalert %}

{% alert important %}
Sem essa atribuição de função, a Braze pode autenticar no Microsoft Entra ID, mas não conseguirá gravar no seu contêiner.
{% endalert %}

### Etapa 5: Obter o endpoint da sua conta {#cert-sp-5}

Na sua conta de armazenamento, acesse **Settings** > **Endpoints** e anote o endpoint do **Blob service**. Ele se parece com `https://<your-storage-account>.blob.core.windows.net`.

![A página de Endpoints da conta de armazenamento com o endpoint do Blob service destacado.]({% image_buster /assets/img/azure-currents-cert-sp-2.png %})

{% alert note %}
A autenticação por entidade de serviço com certificado é compatível apenas com a nuvem pública do Azure. Seu endpoint de blob deve terminar em `.blob.core.windows.net`.
{% endalert %}

### Etapa 6: Configurar o Currents {#cert-sp-6}

A Braze precisa de um único arquivo PEM contendo seu certificado e sua chave privada sem criptografia. Se você gerou um novo certificado na [Etapa 2](#cert-sp-2), combine os dois arquivos em um:

```bash
cat cert.pem key.pem > braze-currents.pem
```

Se você converteu um `.pfx` existente na [Etapa 2](#cert-sp-2), você já tem esse arquivo `braze-currents.pem`.

Na Braze, acesse **Currents** > **+ Create Current** > **Azure Blob Data Export** e forneça o nome da sua integração e o e-mail de contato. Em **Credentials**, selecione **Certificate Service Principal** e forneça o seguinte:

| Campo | Valor |
| ----- | ----- |
| Tenant ID | O **Directory (tenant) ID** da [Etapa 1](#cert-sp-1). |
| Client ID | O **Application (client) ID** da [Etapa 1](#cert-sp-1). |
| Account Endpoint | O endpoint do **Blob service** da [Etapa 5](#cert-sp-5). |
| Certificate | O arquivo `braze-currents.pem` contendo seu certificado e sua chave privada sem criptografia. |
| Container Name | O nome do seu contêiner de blob. |
| Prefix | Opcional. Um prefixo de caminho para seus dados exportados dentro do contêiner. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos da entidade de serviço com certificado" }

![A página Azure Blob Data Export na Braze com Certificate Service Principal selecionado, mostrando os campos Tenant ID, Client ID, Account Endpoint, Certificate, Container Name e Prefix.]({% image_buster /assets/img/azure-currents-cert-sp-3.png %})

Ao salvar, a Braze valida as credenciais que você inseriu.

Por fim, role até o final da página e selecione quais eventos de engajamento com mensagem ou eventos de comportamento do cliente você deseja exportar. Quando concluído, inicie seu Current.

## Atualização das credenciais do Azure para o Currents {#updating-currents-credentials}

Você pode atualizar as credenciais do Azure em um conector existente do Braze Currents sem interromper a integração ou perder dados já exportados para o seu contêiner.

Para atualizar as credenciais — ou alternar entre os métodos **Connection String** e **Certificate Service Principal** — conclua as etapas do lado do Azure para o método escolhido anteriormente neste artigo. Em seguida, na Braze, acesse **Currents**, localize seu conector Azure Blob na lista, selecione **Edit Current**, atualize as **Credentials** e selecione **Update Current**. A Braze valida as credenciais inseridas; seu conector continua funcionando e os dados já presentes no contêiner permanecem disponíveis. Para saber mais, consulte [Atualização do Currents em Configurar o Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents).

{% alert important %}
É importante manter seu certificado atualizado. Se o certificado expirar, o conector para de enviar eventos até que você forneça um certificado válido, e uma interrupção prolongada pode resultar em perda de dados.
{% endalert %}

## Comportamento de exportação {#export-behavior}

Usuários que integraram uma solução de armazenamento de dados em nuvem e estão tentando exportar APIs, relatórios do dashboard ou relatórios CSV terão a seguinte experiência:

- Todas as exportações de API não retornarão uma URL de download no corpo da resposta e devem ser recuperadas por meio do armazenamento de dados.
- Todos os relatórios do dashboard e relatórios CSV serão enviados para o e-mail do usuário para download (sem necessidade de permissões de armazenamento) e terão backup no armazenamento de dados.

{% alert important %}
**Requisito de formato JSON**: Para exportações JSON, a Braze usa o formato [JSONL](https://jsonlines.org/) (JSON delimitado por nova linha), em que cada linha contém um objeto JSON separado. Esse formato difere do JSON padrão, que é um único array ou objeto JSON. Cada linha no arquivo exportado é um objeto JSON válido, mas o arquivo como um todo não é um único documento JSON válido. Ao processar esses arquivos, analise cada linha individualmente como um objeto JSON separado, em vez de tentar analisar o arquivo inteiro como um único documento JSON. <br><br> As exportações do Currents usam o formato [Apache Avro](https://avro.apache.org/) (arquivos `.avro`), não JSON. Esse requisito de formato JSON se aplica a exportações de dados do dashboard e exportações de API que usam formato JSON.
{% endalert %}

## Perguntas frequentes {#faq}

### A Braze pode fornecer endereços IP para lista de permissões do armazenamento Azure Blob? {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

A Braze não publica uma lista fixa de IPs permitidos para Currents ou exportações do dashboard para o armazenamento Azure Blob. A Braze grava no seu contêiner usando as credenciais e o nome do contêiner que você fornece, e o Azure controla o acesso à rede por meio das configurações da sua conta de armazenamento (por exemplo, regras de firewall na conta de armazenamento ou endpoints privados).

Se sua equipe de segurança exigir restrições baseadas em IP, use os recursos de rede do Azure na sua conta de armazenamento em vez de uma lista de IPs da Braze. Para as etapas de configuração, consulte a [documentação da Microsoft sobre como proteger o Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security).