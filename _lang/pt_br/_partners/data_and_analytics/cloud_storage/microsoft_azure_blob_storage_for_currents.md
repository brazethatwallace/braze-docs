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
| Microsoft Azure e conta de armazenamento do Azure | Uma conta Microsoft Azure e uma conta de armazenamento do Azure são necessárias para aproveitar esta parceria. |
| Currents | Para exportar dados para o Currents, você deve ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado na sua conta. O Currents não é necessário se você estiver configurando apenas o arquivamento de mensagens. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para integrar com o Microsoft Azure Blob Storage, você deve ter uma conta de armazenamento e uma string de conexão para permitir que a Braze exporte dados de volta para o Azure ou transmita dados do Currents.

### Etapa 1: Criar uma conta de armazenamento {#step-1-create-a-storage-account}

No Microsoft Azure, navegue até **Storage Accounts** na barra lateral e clique em **+ Add** para criar uma nova conta de armazenamento. Em seguida, forneça um nome para a conta de armazenamento. As outras configurações padrão não precisarão ser atualizadas. Por fim, selecione **Review + create**.

Mesmo que você já tenha uma conta de armazenamento, recomendamos criar uma nova especificamente para seus dados da Braze.

![Página de criação de conta de armazenamento do Microsoft Azure na aba Básico, com o campo Nome da conta de armazenamento destacado.]({% image_buster /assets/img/azure-currents-step-1.png %})

### Etapa 2: Obter a string de conexão {#step-2-get-the-connection-string}

Depois que a conta de armazenamento for implantada, navegue até o menu **Access Keys** da conta de armazenamento e anote a string de conexão.

A Microsoft fornece duas chaves de acesso para manter as conexões usando uma chave enquanto regenera a outra. Você só precisa da string de conexão de uma delas.

{% alert note %}
A Braze usa a string de conexão deste menu, não a chave.
{% endalert %}

![Página de chaves de acesso de uma conta de armazenamento do Azure, com o campo de string de conexão sob key1 destacado.]({% image_buster /assets/img/azure-currents-step-2.png %})

### Etapa 3: Criar um contêiner de serviço de blob {#step-3-create-a-blob-service-container}

Navegue até o menu **Blobs** na seção **Blob Service** da sua conta de armazenamento. Crie um contêiner de Blob Service na conta de armazenamento que você criou anteriormente.

Forneça um nome para o seu contêiner de Blob Service. As outras configurações padrão não precisarão ser atualizadas.

![Página de Blobs de uma conta de armazenamento do Azure em Blob Service, com a opção de adicionar um contêiner.]({% image_buster /assets/img/azure-currents-step-3.png %})

### Etapa 4: Configurar o Currents {#step-4-set-up-currents}

Na Braze, navegue até **Currents > + Create Current > Azure Blob Data Export** e forneça o nome da sua integração e o e-mail de contato.

Em seguida, forneça a string de conexão, o nome do contêiner e o prefixo do BlobStorage (opcional).

![A página do Currents do armazenamento do Microsoft Azure Blob na Braze. Nessa página, há campos para nome da integração, e-mail de contato, string de conexão, nome do contêiner e prefixo.]({% image_buster /assets/img/maz.png %})

Por fim, role até a parte inferior da página e selecione quais eventos de engajamento com mensagem ou eventos de comportamento do cliente você gostaria de exportar. Quando concluído, lance seu Current.

### Etapa 5: Configurar a exportação de dados do Azure {#step-5-set-up-azure-data-export}

A seguir, configure as credenciais que são usadas para:
1. Exportações de Segment pela API
2. Exportações CSV (Campaign, Segment, exportação de dados de usuários do Canvas pelo dashboard)
3. Relatórios de engajamento

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** > **Microsoft Azure** e forneça sua string de conexão, o nome do contêiner de armazenamento do Azure e o prefixo de armazenamento do Azure.

Em seguida, confira se a caixa **Make this the default data export destination** está marcada, pois isso garantirá que seus dados exportados sejam enviados para o Azure. Quando concluído, salve sua integração.

![A página de exportação de dados do Microsoft Azure na Braze. Nessa página, há campos para string de conexão, nome do contêiner e prefixo.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
É importante manter sua string de conexão atualizada. Se as credenciais do seu conector expirarem, o conector parará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão permanentemente perdidos.
{% endalert %}

## Comportamento de exportação {#export-behavior}

Os usuários que integraram uma solução de armazenamento de dados na nuvem e estão tentando exportar APIs, relatórios do dashboard ou relatórios CSV terão a seguinte experiência:

- Todas as exportações de API não retornarão um URL de download no corpo da resposta e devem ser recuperadas pelo armazenamento de dados.
- Todos os relatórios do dashboard e relatórios CSV serão enviados para o e-mail do usuário para download (sem necessidade de permissões de armazenamento) e terão backup no armazenamento de dados.

{% alert important %}
**Requisito de formato JSON**: Para exportações JSON, a Braze usa o formato [JSONL](https://jsonlines.org/) (JSON delimitado por nova linha), em que cada linha contém um objeto JSON separado. Esse formato é diferente do JSON padrão, que é um único array ou objeto JSON. Cada linha do arquivo exportado é um objeto JSON válido, mas o arquivo como um todo não é um único documento JSON válido. Ao processar esses arquivos, analise cada linha individualmente como um objeto JSON separado, em vez de tentar analisar o arquivo inteiro como um único documento JSON. <br><br> As exportações do Currents usam o formato [Apache Avro](https://avro.apache.org/) (arquivos `.avro`), não JSON. Esse requisito de formato JSON se aplica às exportações de dados do dashboard e às exportações de API que usam o formato JSON.
{% endalert %}

## Perguntas frequentes {#faq}

### A Braze pode fornecer endereços IP para lista de permissões do Azure Blob Storage? {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

A Braze não publica uma lista fixa de IPs permitidos para Currents ou exportações do dashboard para o Azure Blob Storage. A Braze grava no seu contêiner usando a string de conexão e o nome do contêiner que você fornece, e o Azure controla o acesso à rede por meio das configurações da sua conta de armazenamento (por exemplo, regras de firewall na conta de armazenamento ou endpoints privados).

Se sua equipe de segurança exigir restrições baseadas em IP, use os recursos de rede do Azure na sua conta de armazenamento em vez de uma lista de IPs da Braze. Para ver as etapas de configuração, consulte a [documentação da Microsoft sobre como proteger o Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security).