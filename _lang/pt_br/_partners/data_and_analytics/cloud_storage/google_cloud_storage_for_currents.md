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
| Conta do Google Cloud Storage | É necessário ter uma conta do Google Cloud Storage para aproveitar essa parceria. |
| Currents | Para exportar dados de volta para o Google Cloud Storage, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado para a sua conta. O Currents não é necessário se você estiver configurando apenas o arquivamento de mensagens. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para integrar com o Google Cloud Storage, você deve configurar as credenciais apropriadas que permitam à Braze obter informações sobre os buckets de armazenamento que estão sendo gravados (`storage.buckets.get`) e criar objetos dentro desse bucket (`storage.objects.create`).

{% alert note %}
O Workload Identity Federation (WIF) não é compatível como método de autenticação para o Currents. Você deve usar uma conta de serviço com uma chave privada JSON.
{% endalert %}

Isso pode ser feito usando as instruções a seguir, que orientam você na criação de uma função e conta de serviço que gerará uma chave privada para uso na sua integração com o Currents.

### Etapa 1: Criar função {#step-1-create-role}

Crie uma nova função no console do Google Cloud Platform navegando até **IAM & admin** > **Roles** > **+ Create Role**.

![Página de funções IAM do Google Cloud com a ação Create Role.]({% image_buster /assets/img/gcs1.png %})

Dê um nome à função, selecione **+Add Permissions** e escolha as seguintes:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
A permissão `storage.objects.delete` é opcional. Ela permite que a Braze limpe arquivos incompletos.<br><br>Em circunstâncias raras, o Google Cloud pode encerrar conexões antecipadamente, resultando na gravação de arquivos incompletos pela Braze no Google Cloud Storage. Na maioria dos casos, a Braze tentará novamente e criará um novo arquivo com os dados corretos, deixando o arquivo antigo no Google Cloud Storage.
{% endalert %}

{% alert important %}
Se o seu bucket usa [namespace hierárquico](https://cloud.google.com/storage/docs/hns-overview), você também deve adicionar a permissão `storage.folders.create`. Nesses buckets, as pastas são recursos gerenciados, então a Braze precisa dessa permissão para criar a estrutura de pastas dos seus arquivos exportados. Sem ela, a Braze não consegue gravar no bucket e a integração falha ao exportar dados.
{% endalert %}

Quando terminar, selecione **Create**.

![Editor de função personalizada do Google Cloud com permissões de armazenamento selecionadas.]({% image_buster /assets/img/gcs2.png %})

### Etapa 2: Criar uma nova conta de serviço {#step-2-create-a-new-service-account}

#### Etapa 2.1: Criar a conta de serviço {#step-21-create-the-service-account}

Crie uma nova conta de serviço no console do Google Cloud Platform navegando até **IAM & admin** > **Service Accounts** e selecionando **Create Service Account**.

![Página de contas de serviço do Google Cloud com Create Service Account selecionado.]({% image_buster /assets/img/gcs3.png %})

Em seguida, dê um nome à conta de serviço e conceda a ela acesso à função personalizada recém-criada.

![No Google Cloud Platform, na página de criação de serviços, digite o nome da sua função no campo "Select a Role".]({% image_buster /assets/img/gcs4.png %})

#### Etapa 2.2: Criar uma chave {#step-22-create-a-key}

Na parte inferior da página, use o botão **Create Key** para criar uma chave privada **JSON** para uso na Braze. Após a criação da chave, ela será baixada na sua máquina.

![Caixa de diálogo de criação de chave da conta de serviço do Google Cloud configurada para o tipo de chave JSON.]({% image_buster /assets/img/gcs5.png %})

### Etapa 3: Configurar o Currents na Braze {#step-3-set-up-currents-in-braze}

Na Braze, navegue até **Currents** > **+ Create Current** > **Google Cloud Storage Data Export** e forneça o nome da integração e o e-mail de contato.

{% multi_lang_include currents/contact_email_notifications.md %}

Em seguida, faça o upload da sua chave privada JSON em **GCS JSON Credentials** e forneça o nome do bucket GCS e o prefixo GCS (opcional). Observe que você deve gerar essas credenciais pelo Google Cloud Platform, conforme descrito nas etapas anteriores.

{% alert important %}
É importante manter seu arquivo de credenciais atualizado. Se as credenciais do seu conector expirarem, o conector deixará de enviar eventos. Se isso persistir por mais de **5 dias**, os eventos do conector serão descartados e os dados serão permanentemente perdidos.
{% endalert %}

![Página do Google Cloud Storage Currents na Braze. Nesta página existem campos para nome da integração, e-mail de contato, credencial JSON do GCS, nome do bucket GCS e prefixo.]({% image_buster /assets/img/gcs6.png %})

Por fim, role até a parte inferior da página e selecione quais eventos de engajamento com mensagem ou eventos de comportamento do cliente você deseja exportar. Quando concluído, inicie seu Current.

### Etapa 4: Configurar exportações do Google Cloud Storage {#step-4-set-up-google-cloud-storage-exports}

Para configurar exportações do Google Cloud Storage (GCS), acesse **Technology Partners** > **Google Cloud Storage**, insira suas credenciais do GCS e selecione **Make this the default data export destination**.

Tenha em mente que a organização e o conteúdo de quaisquer arquivos exportados serão idênticos nas integrações com AWS S3, Microsoft Azure e Google Cloud Storage.

{% alert important %}
Certifique-se de inserir o valor JSON completo que é [gerado pelo Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete).
{% endalert %}

![Página do Google Cloud Storage no dashboard da Braze.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### Etapa 5: Testar as credenciais da sua conta de serviço (opcional) {#step-5-test-your-service-account-credentials-optional}

Sua conta de serviço IAM do Google Cloud deve ter as seguintes permissões:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Para verificar essas permissões no dashboard da Braze, acesse a página **Google Cloud Storage** e selecione **Test Credentials**.

![Seção de credenciais do Google Cloud Storage no dashboard da Braze.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Comportamento de exportação {#export-behavior}

Os usuários que integraram uma solução de armazenamento de dados em nuvem e estão tentando exportar APIs, relatórios do dashboard ou relatórios CSV terão a seguinte experiência:

- Todas as exportações de API não retornarão uma URL de download no corpo da resposta e devem ser recuperadas por meio do armazenamento de dados.
- Todos os relatórios do dashboard e relatórios CSV serão enviados para o e-mail do usuário para download (sem necessidade de permissões de armazenamento) e terão backup no armazenamento de dados.

{% alert important %}
**Requisito de formato JSON**: Para exportações JSON, a Braze usa o formato JSONL (JSON delimitado por nova linha), em que cada linha contém um objeto JSON separado. Esse formato difere do JSON padrão, que é um único array ou objeto JSON. Cada linha no arquivo exportado é um objeto JSON válido, mas o arquivo como um todo não é um único documento JSON válido. Ao processar esses arquivos, analise cada linha individualmente como um objeto JSON separado, em vez de tentar analisar o arquivo inteiro como um único documento JSON.

As exportações do Currents usam o formato Apache Avro (arquivos `.avro`), não JSON. Esse requisito de formato JSON se aplica a exportações de dados do dashboard e exportações de API que usam formato JSON.
{% endalert %}

## Solução de problemas {#troubleshooting}

### As credenciais do Google Cloud Storage são inválidas {#google-cloud-storage-credentials-are-invalid}

Se você receber o seguinte erro ao tentar inserir suas credenciais:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Verifique se a conta de serviço IAM do Google Cloud tem as seguintes permissões:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Após a verificação, você pode [testar suas credenciais no dashboard da Braze](#step-5-test-your-service-account-credentials-optional).