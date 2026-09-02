---
nav_title: OneTrust
article_title: OneTrust
description: "Este artigo de referência descreve a parceria entre a Braze e a OneTrust, um provedor de software de privacidade e segurança de dados, permitindo que você use o criador de fluxos de trabalho da OneTrust para criar fluxos de trabalho de segurança para o seu produto."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> A [OneTrust](https://www.onetrust.com/) é um provedor de software de privacidade e segurança que fornece a visibilidade necessária para entender melhor seu cenário de confiança, ações para aproveitar insights poderosos e automação para manter sua empresa à frente da concorrência.

_Esta integração é mantida pela OneTrust._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a OneTrust permite que você use o construtor de fluxo de trabalho da OneTrust para criar fluxos de trabalho de segurança para o seu produto.

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Conta OneTrust | Uma conta [OneTrust](https://www.onetrust.com/) para aproveitar esta parceria. |
| Chave de API or interface de programação do aplicativo (API) da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as permissões necessárias para o endpoint que sua ação da OneTrust usará.<br><br>Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Instância da Braze | Sua instância da Braze pode ser obtida com seu gerente de integração da Braze ou pode ser encontrada na [página de visão geral da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

A seguinte integração fornece orientação sobre como criar um fluxo de trabalho de atualização de consentimento do usuário e um fluxo de trabalho de exclusão de usuário. Para mais detalhes sobre os endpoints adicionais suportados pela Braze, consulte [Outras ações suportadas](#Other-supported-actions).

### Adicione credenciais da Braze ao OneTrust {#add-braze-credentials-to-onetrust}

No menu **Integrations** da OneTrust, navegue até **Credentials** > botão **Add New** para abrir a tela **Select System**. Encontre **Braze** e clique no botão **Next**.

Siga as instruções na tela **Enter Credential Details** e forneça as seguintes informações. Salve suas credenciais quando terminar.
  - Nome da credencial
  - Defina o tipo de conector para **Web App**
  - Nome do host: `<your-braze-instance-url>`
  - **Cabeçalho da solicitação**:
    - **Authorization**: Bearer
    - **Content-Type**: application/json
  - Token: `<your-braze-api-key>`

### Adicionar a Braze como um sistema {#add-braze-as-a-system}

#### Etapa 1: Criar um fluxo de trabalho {#step-1-create-a-workflow}

{% tabs %}
{% tab User Consent Update %}
1. No menu de integrações da OneTrust, navegue até **Gallery** > **Braze** > **Add** para criar um novo fluxo de trabalho.![Galeria da OneTrust mostrando a integração com a Braze e um botão Add.]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Forneça um nome e um e-mail de notificação no modal de fluxo de trabalho. Clique no botão **Create**. Na criação, você será direcionado ao construtor de fluxo de trabalho. Seu fluxo de trabalho da Braze será preenchido com chamadas de API or interface de programação do aplicativo (API) e ações que podem ser usadas para processar solicitações de exclusão. <br><br>
3. No construtor de fluxo de trabalho, escolha a ação que você deseja disparar no fluxo de trabalho.<br>![Construtor de fluxo de trabalho da OneTrust para um evento de atualização de consentimento do titular dos dados.]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab User Deletion %}

1. No menu de integrações da OneTrust, navegue até **Gallery** > **Braze** > **Add** para criar um novo fluxo de trabalho.![Galeria da OneTrust mostrando a integração com a Braze e um botão Add.]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Forneça um nome e um e-mail de notificação no modal de fluxo de trabalho. Clique no botão **Create**. Na criação, você será direcionado ao construtor de fluxo de trabalho. Seu fluxo de trabalho da Braze será preenchido com chamadas de API or interface de programação do aplicativo (API) e ações que podem ser usadas para processar solicitações de exclusão. <br><br>
3. No construtor de fluxo de trabalho, escolha a ação que você deseja disparar no fluxo de trabalho.<br>![Construtor de fluxo de trabalho da OneTrust para um evento de exclusão do titular dos dados.]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### Etapa 2: Selecionar ação {#step-2-select-action}
{% tabs %}
{% tab User Consent Update %}

1. Quando terminar, clique em **Done** e escolha **Add Action**. A ação que você escolher dependerá do tipo de preferência que está sendo atualizada e do seu endpoint preferido.
- Para atualizar as preferências globais de inscrição de um usuário, escolha a ação **POST User track - attributes**.
- Para atualizar as preferências do grupo de inscrições de um usuário, escolha a ação **POST User Track - Attributes** ou a ação **POST Set Users Subscription Group Status**.<br>![Menu Add Action da OneTrust mostrando POST User track - attributes.]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. Escolha a ação desejada, selecione suas credenciais da Braze criadas anteriormente e clique em **Next**.<br>![Seleção de credenciais da OneTrust para uma ação POST User track - attributes.]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab User Deletion %}

1. Quando terminar, clique em **Done** e escolha **Add Action**.
- Para excluir um usuário da Braze, escolha a ação **POST User Delete Action**.
<br>![Menu Add Action da OneTrust mostrando POST User Delete.]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. Escolha a ação desejada, selecione suas credenciais da Braze criadas anteriormente e clique em **Next**.<br>![Seleção de credenciais da OneTrust para uma ação POST User Delete.]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### Etapa 3: Atualizar o corpo da solicitação {#step-3-update-request-body}
{% tabs %}
{% tab User Consent Update %}

1. Atualize o corpo para incluir quaisquer valores dinâmicos necessários. Confira se o corpo da ação corresponde ao [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) e ao [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).
2. Personalize o fluxo de trabalho com parâmetros adicionais ou lógica condicional para atender às necessidades da sua organização.
3. Quando terminar de editar, clique em **Finish** e depois em **Activate** para ativar o fluxo de trabalho.

{% alert note %}
Ao usar os fluxos de trabalho da OneTrust para atualizar as preferências do grupo de inscrições na Braze, o `subscription_group_id` deve corresponder ao ID definido pela Braze quando o grupo de inscrições foi criado. Você pode acessar o `subscription_group_id` de um grupo de inscrições navegando até a página **Subscription Group** no dashboard da Braze.
{% endalert %}

![Corpo da solicitação da OneTrust para POST User track - attributes com campos de grupo de inscrições.]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab User Deletion %}

1. Atualize o corpo para incluir quaisquer valores dinâmicos necessários. Confira se o corpo da ação corresponde ao [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
2. Quando terminar de editar, selecione **Finish** e depois **Activate** para ativar o fluxo de trabalho.

![Corpo da solicitação da OneTrust para POST User Delete com um campo external_id.]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### Atualizar o fluxo de trabalho da solicitação do titular dos dados {#update-the-data-subject-request-workflow}
1. No menu **Privacy Rights Automation**, selecione **Workflows**.
2. Selecione o fluxo de trabalho que você deseja atualizar com a integração da Braze.
3. Selecione o botão **Edit** para ativar a edição.
4. Em seguida, selecione a etapa do fluxo de trabalho para adicionar a integração da Braze e clique em **Add Connection**.
5. Adicione o fluxo de trabalho da Braze criado anteriormente como uma subtarefa do sistema.

{% endtab %}
{% endtabs %}

## Outras ações suportadas {#other-supported-actions}

Além das ações **POST User track - Attributes**, **POST Set Users Subscription Group Status** e **POST User Delete**, a Braze oferece outros endpoints que podem ser usados para criar fluxos de trabalho personalizados e usados como subtarefas dentro de fluxos de trabalho existentes.

Para ver uma lista completa de ações suportadas:
1. Na OneTrust, clique em **Systems** no menu **Integrations**.
2. Escolha o sistema **Braze**.
3. Navegue até a guia **Actions**.

![Guia Actions do sistema Braze na OneTrust listando as ações de API suportadas.]({% image_buster /assets/img/onetrust/onetrust7.png %})