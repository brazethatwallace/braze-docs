---
nav_title: Arquivamento de mensagem
article_title: Arquivamento de mensagem
alias: "/message_archiving/"
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o arquivamento de mensagem, um recurso que permite salvar uma cópia das mensagens enviadas aos usuários."

---

# Arquivamento de mensagem {#message-archiving}

> O arquivamento de mensagem permite que você salve uma cópia das mensagens enviadas aos usuários para fins de arquivamento ou conformidade em seu bucket S3 da AWS, contêiner de Blob Storage do Azure ou bucket do Google Cloud Storage. <br><br> Este artigo aborda como configurar o arquivamento de mensagem, referências de carga útil JSON e perguntas frequentes.

O arquivamento de mensagem está disponível como um recurso complementar. Para começar a usar o arquivamento de mensagem, entre em contato com seu gerente de sucesso do cliente da Braze.

## Como funciona {#how-it-works}

Quando esse recurso está ativado, a Braze grava um arquivo JSON compactado em gzip para cada mensagem enviada a um usuário através dos canais selecionados (e-mail, SMS/MMS ou push). A Braze grava esses arquivos no seu destino padrão de exportação de dados. Isso inclui todos os tipos de Campaign para cada canal, como Campaigns de e-mail de transação enviadas através da [API de E-mail de transação]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email).

Esse arquivo conterá os campos definidos em [Referências de arquivo](#file-references) e refletirá as mensagens finais com modelo aplicado enviadas ao usuário. Todos os valores de modelo definidos na sua Campaign (por exemplo, {% raw %}`{{${first_name}}}`{% endraw %}) mostrarão o valor final que o usuário recebeu com base nas informações do perfil. Isso permite que você retenha uma cópia da mensagem enviada para atender aos requisitos de conformidade, auditoria ou suporte ao cliente.

Se você configurar credenciais para vários provedores de armazenamento em nuvem, o arquivamento de mensagem só será exportado para aquele marcado como o destino padrão de exportação de dados. Se nenhum padrão explícito for definido e um bucket S3 da AWS estiver conectado, o arquivamento de mensagem fará upload para esse bucket.

{% alert important %}
Ativar esse recurso impactará a velocidade de entrega das suas mensagens, pois o upload do arquivo é realizado imediatamente antes do envio da mensagem para manter a precisão. A latência introduzida pelo arquivamento de mensagem dependerá do provedor de armazenamento em nuvem e da taxa de transferência e tamanho dos documentos salvos.
{% endalert %}

O JSON será salvo em seu bucket de armazenamento usando a seguinte estrutura de chave:

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

Um arquivo de exemplo pode ter a seguinte aparência:

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
O digest MD5 só pode ser calculado usando um endereço de e-mail, um token por push ou um número de telefone E.164 conhecidos e em minúsculas. Um digest MD5 conhecido não pode ser revertido para obter o endereço de e-mail, o token por push ou o número de telefone E.164.
{% endalert %}

{% alert tip %}
**Está tendo problemas para encontrar seus tokens por push nos seus buckets?**<br>
A Braze converte seus tokens por push para minúsculas antes de fazer o hash. Isso faz com que o token por push `Test_Push_Token12345` seja convertido para `test_push_token12345` no caminho da chave com o hash `32b802170652af2b5624b695f34de089`.
{% endalert %}

## Configuração do arquivamento de mensagem {#setting-up-message-archiving}

Esta seção orienta você na configuração do arquivamento de mensagem para o seu espaço de trabalho. Antes de continuar, confirme se sua empresa comprou e ativou o arquivamento de mensagem.

### Etapa 1: Conecte um bucket de armazenamento em nuvem {#step-1-connect-a-cloud-storage-bucket}

Se ainda não tiver feito isso, conecte um bucket de armazenamento em nuvem à Braze. Para ver as etapas, consulte a documentação de nossos parceiros sobre o [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3), o [Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) ou o [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents).

{% alert note %}
Você não precisa configurar o Currents para o arquivamento de mensagem, então pode pular esse pré-requisito na documentação do parceiro.
{% endalert %}

### Etapa 2: Selecione canais para o arquivamento de mensagem {#step-2-select-channels-for-message-archiving}

A página de configurações de **Arquivamento de mensagem** controla quais canais salvarão uma cópia das mensagens enviadas no seu bucket de armazenamento em nuvem.

Para selecionar canais:

1. Acesse **Configurações** > **Arquivamento de mensagem**.
2. Selecione seus canais.
3. Selecione **Salvar alterações**.

![A página de Arquivamento de mensagem tem três canais para seleção: E-mail, Push e SMS.]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
Se você não vir **Arquivamento de mensagem** em **Configurações**, confirme se sua empresa comprou e ativou o arquivamento de mensagem.
{% endalert %}

## Lista de permissões de IP {#ip-allowlisting}

Quando o arquivamento de mensagem faz upload de arquivos para o seu bucket de armazenamento em nuvem, a Braze faz solicitações de rede dos nossos servidores para o seu endpoint do AWS S3, Azure Blob Storage ou Google Cloud Storage. Com a lista de permissões de IP, você pode verificar se essas solicitações estão vindo da Braze, adicionando uma camada de segurança.

A Braze envia os uploads de arquivamento de mensagem a partir dos mesmos endereços IP usados para Conteúdo conectado e Currents. Para a lista completa de IPs por instância, consulte [Lista de permissões de IP de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting).

## Referências de arquivo {#file-references}

A seguir estão as referências da carga útil JSON entregue ao seu bucket de armazenamento em nuvem cada vez que uma mensagem é enviada. Consulte nosso repositório de exemplos de código para ver os [arquivos de amostra de arquivamento de mensagem](https://github.com/braze-inc/braze-examples/tree/main/message-archiving).

{% tabs %}
{% tab E-mail %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@example.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Hash of key-value pairs from Email Extras configured in the email editor,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessageVariationApiId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

O campo `extras` contém os pares chave-valor configurados no campo **Email Extras** ao compor um e-mail no editor de HTML. Os extras de e-mail funcionam para todos os prestadores de serviço de e-mail (incluindo SendGrid e SparkPost) e estão incluídos nas mensagens arquivadas, independentemente de qual provedor é utilizado. Para saber mais sobre como configurar os extras de e-mail, veja [Criando uma campanha de e-mail]({{site.baseurl}}/user_guide/channels/email/html_editor#adding-email-extras). Para enviar dados de volta ao Currents, consulte [Extras de mensagens]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras).

![Seção Email Extras do criador de e-mail com campos de chave e valor e opção Adicionar novo extra.]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS/MMS %}

```json
{
  "version": 1 //numerical version of the JSON structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString, // indicates a message is MMS
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": one of "android_push" | "ios_push" | "kindle_push" | "web_push",
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from a Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

### Variações na estrutura da carga útil de push {#push-payload-structure-variations}

{% alert important %}
O campo de nível superior `payload` nos arquivos de notificação por push contém toda a carga útil do provedor conforme enviada ao dispositivo. Dentro desse JSON, chaves como `aps` (para APNs) ou `notification` e `data` (para FCM) podem variar significativamente dependendo do tipo de mensagem, da plataforma e da configuração.
{% endalert %}

O arquivamento de mensagem captura a carga útil da mensagem em si, mas não inclui os metadados de entrega enviados para FCM ou APNs. Os metadados de entrega incluem:

- Tokens de dispositivo
- Configurações de prioridade
- Tempo de vida (TTL)
- IDs de colapso
- Cabeçalhos APNs
- Carimbos de expiração
- Outros campos de configuração de entrega

Esses campos atuam como instruções de entrega para o provedor de push e geralmente não são considerados parte do conteúdo da mensagem.

Por exemplo:

- **Notificações por push no iOS** podem ter estruturas diferentes para notificações Rich (onde `aps.alert` é um objeto contendo campos como `title` e `body`) em comparação com notificações simples (onde `aps.alert` é uma string).
- **Notificações por push no Android** (por exemplo, FCM) usam mensagens de dados com chaves personalizadas. A estrutura da carga útil pode incluir diferentes campos opcionais dependendo da configuração da mensagem, como botões de push, carrosséis ou metadados adicionais.

Além disso, envios de teste pelo dashboard podem produzir estruturas de carga útil diferentes das mensagens de produção.

O formato da carga útil JSON pode variar entre mensagens e pode mudar ao longo do tempo. Ao analisar cargas úteis de push arquivadas, não assuma uma estrutura fixa nem espere que os mesmos campos estejam sempre presentes. Implemente uma lógica de análise flexível que lide com vários formatos de carga útil.

{% endtab %}
{% endtabs %}

## Perguntas frequentes {#frequently-asked-questions}

### Quais modelos não estão incluídos na carga útil? {#what-templating-is-not-included-in-the-payload}

As modificações feitas depois que a mensagem sai da Braze não serão refletidas no arquivo salvo em seu bucket de armazenamento em nuvem. Isso inclui modificações feitas por nossos parceiros de entrega de e-mail, como o encapsulamento de links para rastreamento de cliques e a inserção de pixels de rastreamento.

### O que são mensagens com o valor "unassociated" no caminho da Campaign? {#what-are-messages-under-the-unassociated-value-in-the-campaign-path}

Quando uma mensagem é enviada fora de uma Campaign ou Canvas, o ID da Campaign no nome do arquivo será "unassociated". Isso acontece quando você envia mensagens de teste pelo dashboard, quando a Braze envia respostas automáticas de SMS/MMS ou quando mensagens enviadas pela API não especificam um ID de Campaign.

### Como faço para obter mais informações sobre esse envio? {#how-do-i-find-more-information-about-this-send}

Você pode usar o `external_id` ou o `dispatch_id` em conjunto com o `user_id` para cruzar a mensagem com modelo aplicado com os dados do Currents e encontrar mais informações, como o carimbo de data/hora da entrega, se o usuário abriu ou clicou na mensagem, entre outros.

### Como as novas tentativas são tratadas? {#how-are-retries-handled}

Se seu bucket de armazenamento em nuvem não puder ser acessado, a Braze tentará novamente até três vezes com um [jitter de backoff](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). As novas tentativas de limite de taxa do AWS S3 são tratadas automaticamente pela Braze.

### O que acontece se minhas credenciais forem inválidas? {#what-happens-if-my-credentials-are-invalid}

Se suas credenciais de armazenamento em nuvem se tornarem inválidas em algum momento, a Braze não poderá salvar nenhuma mensagem no seu bucket de armazenamento em nuvem, e essas mensagens serão perdidas. Recomendamos configurar suas [preferências de notificação]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) para Amazon Web Services, Google Cloud Services ou Azure (Microsoft Cloud Services) para que você receba alertas sobre quaisquer problemas de credenciais.

### Por que o carimbo de data/hora `sent_at` do meu arquivo é ligeiramente diferente do carimbo de data/hora de envio no Currents? {#why-does-my-archive-files-sent_at-timestamp-differ-slightly-from-the-sent-timestamp-in-currents}

A cópia renderizada é enviada por upload imediatamente antes do envio da mensagem ao usuário. Devido aos tempos de upload do armazenamento em nuvem, pode haver um atraso de alguns segundos entre o carimbo de data/hora `sent_at` na cópia renderizada e a hora real em que o envio ocorre.

### Posso criar um novo bucket especificamente para arquivamento de mensagem enquanto mantenho o bucket atual usado para dados do Currents? {#can-i-create-a-new-bucket-specifically-for-message-archiving-while-keeping-the-current-bucket-used-for-currents-data}

Não. Se você tiver interesse em criar esses buckets específicos, envie [feedback sobre o produto]({{site.baseurl}}/user_guide/administer/personal/product_portal).

### Os dados arquivados são gravados em uma pasta dedicada em um bucket existente, semelhante à forma como as exportações de dados do Currents são estruturadas? {#is-archived-data-written-to-a-dedicated-folder-in-an-existing-bucket-similar-to-how-currents-data-exports-are-structured}

Os dados são gravados em uma seção `sent_messages` do bucket. Consulte [Como funciona](#how-it-works) para mais detalhes.

### Posso usar o arquivamento de mensagem para agrupar arquivos em diferentes espaços de trabalho? {#can-i-use-message-archiving-to-group-files-into-different-workspaces}

Não. O arquivamento de mensagem não oferece suporte ao agrupamento de arquivos com base em espaços de trabalho. Em vez disso, você pode identificar a qual espaço de trabalho o ID da API da Campaign ou da etapa do Canvas pertence e agrupá-los com base nessa informação.