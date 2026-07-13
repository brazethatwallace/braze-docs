---
nav_title: Sendbird
article_title: Sendbird
description: "Este artigo de referência descreve a parceria entre a Braze e o Sendbird, uma solução líder de envio de mensagens no app que permite que os usuários recebam notificações no app na plataforma Sendbird."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> O [Sendbird](https://sendbird.com/) Notifications oferece aos profissionais de marketing e gerentes de produtos um novo e poderoso canal de envio de mensagens persistentes e interativas no app para se comunicar com seus clientes. Essas mensagens podem ser usadas para qualquer comunicação e são mais comumente usadas para fins promocionais e transacionais.

_Essa integração é mantida pela Sendbird._

## Sobre a integração {#about-the-integration}

A integração da Braze e do Sendbird permite que os usuários da empresa:
* Utilizem os recursos de segmentação e disparo da Braze para iniciar notificações personalizadas no app.
* Criem notificações personalizadas no app na plataforma Sendbird Notifications, que são então entregues no ambiente do app, aumentando o engajamento do usuário.

Ao aproveitar os recursos conjuntos da Braze e do Sendbird Notifications, as empresas podem elevar o engajamento do cliente e aumentar as taxas de conversão por meio de estratégias eficazes de notificação no app.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Sendbird | É necessário ter uma conta Sendbird para aproveitar essa parceria. |
| Sendbird UIKit | Você deve ter o Sendbird UIKit instalado em seu app para [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) ou [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit). |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

![Diagrama resumindo os casos de uso da integração Braze e Sendbird Notifications para envio de mensagens de marketing e transacionais.]({% image_buster /assets/img/sendbird/use-cases.png %})

A integração da Braze e do Sendbird Notifications oferece uma variedade de casos de uso para aumentar o engajamento do cliente e proporcionar uma experiência excepcional ao usuário:

- **Marketing**: Aprimore campanhas direcionadas com promoções personalizadas e recomendações adaptadas às preferências dos usuários, como descontos exclusivos baseados no histórico de navegação ou em compras anteriores.
- **Transacional**: Eleve a comunicação com o cliente por meio de atualizações em tempo real sobre pedidos, entregas, faturamento e pagamentos, incluindo notificações sobre o status do pedido, detalhes de remessa e prazos de entrega estimados.

## Integração {#integration}

### Etapa 1: Criar um modelo de notificação {#step-1-create-a-notification-template}

[Os modelos do Sendbird](https://sendbird.com/docs/notifications/v1/templates) permitem que você envie notificações personalizadas no app, criando e usando vários modelos para cada canal. Os modelos podem ser criados e personalizados no Sendbird Dashboard sem a necessidade de escrever código.

![Editor de modelos do dashboard do Sendbird para criação de modelos de notificação.]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### Etapa 2: Configure a integração da Braze no dashboard do Sendbird {#step-2-set-up-the-braze-integration-on-sendbird-dashboard}

No **Sendbird Dashboard**, selecione seu aplicativo, navegue até **Notifications > Integrations** e clique em **Add** na seção **Braze**. Aqui você precisará da sua chave da API REST da Braze e do endpoint REST da Braze.

Depois de fornecer todos os campos, clique em **Save** para concluir a integração e acessar os endpoints de integração e o token da API.

### Etapa 3: Instale o Sendbird Notification Builder {#step-3-install-sendbird-notification-builder}

Em seguida, você deve instalar o [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji). Essa extensão do Google Chrome permite enviar notificações personalizadas pelo Sendbird no dashboard da Braze.

![Painel da extensão Sendbird Notification Builder para Chrome no dashboard da Braze.]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Adicione as credenciais do Sendbird à extensão {#add-sendbird-credentials-to-the-extension}

Depois que a extensão for instalada, clique no ícone do Sendbird na barra de ferramentas do navegador e selecione **Settings**. Agora forneça o ID do app e o token da API encontrados no **Sendbird Notification Builder**.

### Etapa 4: Mapear o ID de usuário do Sendbird para o ID de usuário da Braze {#step-4-map-sendbird-user-id-to-braze-user-id}

Um ID de usuário Sendbird deve ser adicionado a um perfil de usuário da Braze como um [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) para que a integração seja usada. É possível fazer upload e atualizar perfis de usuários por meio de arquivos CSV na página [Importação de usuários]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv). Como alternativa, você pode usar o ID de usuário da Braze como o ID de usuário do Sendbird.

### Etapa 5: Configure seu modelo de webhook {#step-5-set-up-your-webhook-template}

Na Braze, em **Modelos e mídia**, acesse **Modelos de webhook** e escolha o **modelo Sendbird Webhook**. Observe que esse modelo só ficará disponível se você tiver instalado a extensão Sendbird Notification Builder.

{% raw %}
1. Forneça um nome de modelo e adicione equipes e tags conforme necessário.
2. Copie um endpoint em tempo real ou em lote do dashboard do Sendbird para a **URL do Webhook**.
3. No campo **Receiver**, clique no ícone <i class="fas fa-plus"></i> e insira o atributo de usuário mapeado para o ID de usuário do Sendbird.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` se estiver usando um atributo personalizado `sendbird_id` como o ID de usuário do Sendbird.
    - `{{ '{{' }}${user_id}}}` se estiver usando o ID de usuário da Braze como ID de usuário do Sendbird.
4. Na guia **Settings**, substitua `SENDBIRD_API_TOKEN` pelo token da API de notificações do dashboard do Sendbird.
5. Salve o modelo.
{% endraw %}

## Usando essa integração {#using-this-integration}

### Campaigns

1. No dashboard da Braze, na página **Campaigns**, clique em **Create Campaign** > **Webhook**.
2. Selecione o modelo de webhook que você criou acima. É altamente recomendável usar o endpoint Batch para Campaigns.
3. Personalize o modelo editando suas variáveis na guia **Compose**.

### Canvas

1. Em um Canvas novo ou existente, adicione um componente **Message**.
2. Abra o componente e selecione **Webhook** nos **Messaging Channels**.
3. Selecione o modelo de webhook que você criou acima. É altamente recomendável usar o endpoint em tempo real para Canvas.
4. Personalize o modelo editando suas variáveis na guia **Compose**.

## Personalização {#customization}

### Rastreamento do status de entrega e de abertura {#track-delivery-and-open-status}

Para integrar a entrega das notificações e o evento de status de abertura com a métrica de conversão de uma campanha, adicione um evento personalizado no dashboard da Braze.

1. No dashboard da Braze, acesse **Configurações** > **Gerenciar configurações** > **Eventos personalizados** e clique em **+ Add Custom Event**.
2. Depois de criar um evento personalizado, clique em **Manage Properties**, adicione uma propriedade chamada "status" e escolha "String" como o tipo de propriedade.
3. Ao criar uma notificação em Campaigns ou Canvas, insira o nome do evento personalizado no campo **Event Name**.

Esse evento personalizado será disparado duas vezes para cada notificação: quando uma mensagem for enviada e quando um usuário abrir a mensagem.
- Quando uma mensagem é enviada, um evento personalizado é disparado com o status `SENT`.
- Quando uma mensagem é lida, um evento personalizado é disparado com o status `READ`.