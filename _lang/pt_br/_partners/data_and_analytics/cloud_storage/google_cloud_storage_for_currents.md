---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "Este artigo de referência descreve a parceria entre a Braze e o Google Cloud Storage, um armazenamento de objetos altamente escalável para dados não estruturados."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> O [Google Cloud Storage](https://cloud.google.com/storage/) é um armazenamento de objetos altamente escalável para dados não estruturados oferecido pelo Google como parte do conjunto de produtos de computação em nuvem.

{% alert important %}
Se você estiver trocando entre provedores de armazenamento em nuvem, entre em contato com seu gerente de sucesso do cliente da Braze para obter mais assistência na configuração e validação da sua nova integração.
{% endalert %}

A integração entre a Braze e o Google Cloud Storage permite enviar dados do Currents para o Google Cloud Storage. Em seguida, é possível usar um processo ETL (Extrair, Transformar, Carregar) para transferir seus dados para outros locais, como o Google BigQuery.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Google Cloud Storage | É necessário ter uma conta do Google Cloud Storage para usar essa parceria. |
| Currents | Para exportar dados de volta para o Google Cloud Storage, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado para sua conta. O Currents não é necessário se você estiver apenas configurando o arquivamento de mensagens. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

Para integrar-se ao Google Cloud Storage, é necessário configurar as credenciais apropriadas que permitem que a Braze obtenha informações sobre os buckets de armazenamento gravados (`storage.buckets.get`) e crie objetos dentro desse bucket (`storage.objects.create`).

{% alert note %}
A Federação de Identidade de Carga de Trabalho (WIF) não é compatível como método de autenticação para o Currents. Você deve usar uma conta de serviço com uma chave privada JSON.
{% endalert %}

Isso pode ser feito usando as instruções a seguir, que orientam na criação de uma função e de uma conta de serviço que gerará uma chave privada para ser usada na sua integração com o Currents.

### Etapa 1: Criar função {#step-1-create-role}

Crie uma nova função no Console do Google Cloud Platform navegando até **IAM & admin** > **Roles** > **+ Create Role**.

![]({% image_buster /assets/img/gcs1.png %})

Dê um nome à função, selecione **+Add Permissions** e escolha as seguintes permissões:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
A permissão `storage.objects.delete` é opcional. Ela permite que a Braze limpe arquivos incompletos.<br><br>Em raras circunstâncias, o Google Cloud pode encerrar as conexões antes do previsto, o que faz com que a Braze grave arquivos incompletos no Google Cloud Storage. Na maioria dos casos, a Braze tentará novamente e criará um novo arquivo com os dados corretos, deixando o arquivo antigo no Google Cloud Storage.
{% endalert %}

Quando terminar, selecione **Create**.

![]({% image_buster /assets/img/gcs2.png %})

### Etapa 2: Crie uma nova conta de serviço {#step-2-create-a-new-service-account}

#### Etapa 2.1: Crie a conta de serviço {#step-21-create-the-service-account}

Crie uma nova conta de serviço no Console do Google Cloud Platform navegando até **IAM & admin** > **Service Accounts** e selecionando **Create Service Account**.

![]({% image_buster /assets/img/gcs3.png %})

Em seguida, dê um nome à conta de serviço e conceda a ela acesso à função personalizada recém-criada.

![Na Google Cloud Platform, na página de criação de serviços, digite o nome da sua função no campo "Select a Role".]({% image_buster /assets/img/gcs4.png %})

#### Etapa 2.2: Criar uma chave {#step-22-create-a-key}

Na parte inferior da página, use o botão **Create Key** para criar uma chave privada **JSON** para usar na Braze. Depois que a chave for criada, ela será baixada na sua máquina.

![]({% image_buster /assets/img/gcs5.png %})

### Etapa 3: Configurar o Currents na Braze {#step-3-set-up-currents-in-braze}

Na Braze, navegue até **Currents** > **+ Create Current** > **Google Cloud Storage Data Export** e forneça o nome da integração e o e-mail de contato.

Em seguida, faça upload da sua chave privada JSON em **GCS JSON Credentials** e forneça o nome do bucket do GCS e o prefixo do GCS (opcional). Observe que você deve gerar essas credenciais pelo Google Cloud Platform, conforme descrito nas etapas anteriores.

{% alert important %}
É importante manter seu arquivo de credenciais atualizado. Se as credenciais do conector expirarem, o conector deixará de enviar eventos. Se isso persistir por mais de **5 dias**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

![A página do Google Cloud Storage Currents na Braze. Nessa página, há campos para o nome da integração, o e-mail de contato, a credencial JSON do GCS, o nome do bucket do GCS e o prefixo.]({% image_buster /assets/img/gcs6.png %})

Por fim, role até a parte inferior da página e selecione quais eventos de engajamento com mensagem ou eventos de comportamento do cliente você gostaria de exportar. Quando concluído, inicie seu Current.

### Etapa 4: Configure as exportações do Google Cloud Storage {#step-4-set-up-google-cloud-storage-exports}

Para configurar as exportações do Google Cloud Storage (GCS), acesse **Parceiros de tecnologia** > **Google Cloud Storage**, insira suas credenciais do GCS e selecione **Make this the default data export destination**.

Tenha em mente que a organização e o conteúdo de quaisquer arquivos exportados serão idênticos nas integrações do AWS S3, Microsoft Azure e Google Cloud Storage.

{% alert important %}
Certifique-se de inserir o valor JSON completo que é [gerado pelo Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete).
{% endalert %}

![A página do Google Cloud Storage no dashboard da Braze.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### Etapa 5: Teste suas credenciais de conta de serviço (opcional) {#step-5-test-your-service-account-credentials-optional}

Sua conta de serviço do Google Cloud IAM deve ter as seguintes permissões:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Para verificar essas permissões no dashboard da Braze, acesse a página **Google Cloud Storage** e selecione **Test Credentials**.

![A seção de credenciais do Google Cloud Storage no dashboard da Braze.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Comportamento de exportação {#export-behavior}

Usuários que integraram uma solução de armazenamento de dados em nuvem e estão tentando exportar APIs, relatórios do dashboard ou relatórios CSV terão a seguinte experiência:

- Todas as exportações da API não retornarão um URL de download no corpo da resposta e devem ser recuperadas por meio do armazenamento de dados.
- Todos os relatórios do dashboard e relatórios CSV serão enviados para o e-mail do usuário para download (nenhuma permissão de armazenamento necessária) e terão backup no armazenamento de dados.

{% alert important %}
**Requisito de formato JSON**: Para exportações JSON, a Braze usa o formato JSONL (JSON delimitado por nova linha), onde cada linha contém um objeto JSON separado. Esse formato difere do JSON padrão, que é um único array ou objeto JSON. Cada linha no arquivo exportado é um objeto JSON válido, mas o arquivo como um todo não é um único documento JSON válido. Ao processar esses arquivos, analise cada linha individualmente como um objeto JSON separado, em vez de tentar analisar o arquivo inteiro como um único documento JSON.

As exportações do Currents usam o formato Apache Avro (arquivos `.avro`), não JSON. Esse requisito de formato JSON se aplica a exportações de dados do dashboard e exportações de API que usam o formato JSON.
{% endalert %}

## Solução de problemas {#troubleshooting}

### As credenciais do Google Cloud Storage são inválidas {#google-cloud-storage-credentials-are-invalid}

Se você receber o seguinte erro ao tentar inserir suas credenciais:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Certifique-se de que sua conta de serviço do Google Cloud IAM tenha as seguintes permissões:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Após a verificação, você pode [testar suas credenciais no dashboard da Braze](#step-5-test-your-service-account-credentials-optional).