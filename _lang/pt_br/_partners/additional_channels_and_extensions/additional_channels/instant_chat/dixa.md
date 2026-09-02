---
nav_title: Dixa
article_title: Dixa
description: "Este artigo descreve a parceria entre a Braze e a Dixa."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> A [Dixa](https://www.dixa.com/) é uma plataforma de atendimento ao cliente projetada para aprimorar as experiências de suporte unificando canais de comunicação como chat, e-mail, telefone e redes sociais em uma única interface. Ela ajuda as empresas a melhorar a satisfação e a eficiência do cliente por meio de roteamento inteligente, automação e insights de desempenho em tempo real.

A integração da Braze com a Dixa oferece uma visão melhor de todos os seus usuários, fornecendo aos agentes de atendimento ao cliente dados da Braze em tempo real.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta da Dixa | É necessário ter uma conta de administrador da Dixa para aproveitar essa parceria. |
| Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as permissões `users.export.ids` e `email.status`.<br><br> Ela pode ser criada no dashboard da Braze em **Settings** > **API or interface de programação do aplicativo (API) Keys**. |
| Um endpoint REST or transferir estado representacional da Braze | [URL do seu endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Exiba os dados da Braze na visualização do agente de atendimento ao cliente enquanto se comunica com seus usuários em diferentes canais de comunicação, como e-mail, Messenger ou chat. Além disso, use a Transformação de Dados da Braze para enviar dados da Dixa para a Braze e pausar o marketing enquanto resolve o problema de um usuário, ou use as pesquisas de satisfação da Dixa para segmentação.

## Integração {#integration}

Você deve ser um administrador da Dixa para configurar as integrações dentro da Dixa. Para a integração com a Braze, na Dixa, acesse **Settings** > **Integrations** > **Braze**.

![A página Create Braze widget na Dixa, onde você insere o nome do widget, a URL da API e a chave de API.]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### Etapa 1: Criar a integração na Dixa {#step-1-create-the-integration-in-dixa}

Na página **Create Braze widget**, preencha os seguintes campos obrigatórios para criar a integração:

- **Widget name:** Esse é o nome da integração que será usado posteriormente na barra lateral da conversa como título.
- **API or interface de programação do aplicativo (API) URL:** Essa é a URL do endpoint da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze para sua instância.
- **API or interface de programação do aplicativo (API) Key:** Essa é a chave de API or interface de programação do aplicativo (API) da Braze que você criou nos pré-requisitos.

### Etapa 2: Configurar a integração {#step-2-configure-the-integration}

Em seguida, configure a integração da Braze com a Dixa. Escolha uma das seguintes opções para ajustar a visualização do widget da Braze na barra lateral da conversa.

#### Mostrar o widget na barra lateral da conversa {#show-the-widget-in-the-conversation-sidebar}

Essa configuração mostra ou oculta toda a integração na barra lateral da conversa na Dixa.

Se estiver configurando ativamente a integração, recomendamos desativar essa opção enquanto preenche os campos obrigatórios. Quando terminar a configuração, você poderá ativá-la novamente e os agentes da Dixa poderão usar a integração.

#### Exibir detalhes do cliente {#display-customer-details}

Escolha mostrar ou ocultar os detalhes do usuário. Os detalhes contêm dados sobre local, e-mail, número de telefone, estado da inscrição de e-mail, estado da inscrição de notificação por push e a duração da associação na Braze.

#### Exibir o botão para alterar o estado da inscrição de e-mail {#display-the-button-to-change-the-email-subscription-state}

Os botões são baseados em um dos três estados de inscrição da Braze: `subscribed`, `opted-in` e `unsubscribed`. Se um usuário for `subscribed`, o agente poderá optar por `opt-in` ou `unsubscribe`. Quando um usuário é `opted-in` ou `unsubscribed`, só é possível alternar entre os dois.

#### Exibir uma lista de atributos personalizados {#display-a-list-of-custom-attributes}

Escolha mostrar ou ocultar os atributos personalizados do usuário na Braze.

#### Exibir uma lista de eventos personalizados {#display-a-list-of-custom-events}

Escolha mostrar ou ocultar os eventos personalizados do usuário na Braze.

#### Exibir uma lista de compras {#display-a-list-of-purchases}

Escolha mostrar ou ocultar uma lista de produtos que o usuário comprou. Aqui, você pode ver quantas vezes o usuário comprou o produto. Para ver a data da primeira e da última compra, passe o mouse sobre o item.

### Exemplo de integração {#example-integration}

Veja a seguir um exemplo da integração:

![A integração da Braze com a Dixa na Dixa que exibe o estado de inscrição de e-mail do usuário, atributos personalizados, eventos personalizados e compras.]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}

## Ferramenta de transformação de dados {#data-transformation-tool}

A Dixa usa webhooks para enviar dados para a Braze. Você deve ser um administrador da Dixa para configurar webhooks.

### Rastrear conversas na Dixa {#track-conversations-in-dixa}

A primeira etapa é criar uma transformação de dados na Braze.

1. Acesse **Data Settings** > **Data Transformations** > **Create transformation**.
2. Selecione **Start from scratch**, selecione o destino **POST: Track Users** e selecione **Create transformation**.
3. No editor de transformação, copie o código de exemplo de **Exemplo de ferramenta de transformação** nesta seção e insira-o no campo **Transformation code**. Selecione **Save**, copie a **Webhook URL** e abra a Dixa.
4. Na Dixa, acesse **Settings** > **Integrations** > **Webhooks** > **+ Outbound webhook**.
5. Na página de configurações do webhook, cole a URL da Braze e ative os eventos que deseja rastrear. **Conversation created** é um bom ponto de partida para rastrear as conversas dos clientes.
6. Selecione **Save** para concluir a configuração da Dixa.

### Exemplo de ferramenta de transformação {#example-transformation-tool}

```js
// Transforming the provided payload to match Braze /users/track endpoint specifications.

// Extracting necessary details from the payload
const requester = payload.data.conversation.requester;
const event = payload.data.conversation;

// Defining user attributes based on the provided payload, prioritizing email if available.
const userAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  _update_existing_only: false, // Set to false to create or update user profiles when identified by email
  organization: payload.organization.name, // Including an additional attribute for demonstration
};

// Defining event attributes based on the provided payload.
const eventAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  name: payload.event_fqn, // The name of the event
  time: event.created_at, // ISO 8601 datetime format
  properties: { // Including additional event properties
    event_version: payload.event_version,
    conversation_status: event.status,
    conversation_channel: event.channel
  },
  _update_existing_only: false // Set to false to create or update user profiles when identified by email
};

// Constructing the final object to match Braze /users/track endpoint schema
const brazecall = {
  attributes: [userAttributes], // Wrapping userAttributes in an array as per specifications
  events: [eventAttributes] // Wrapping eventAttributes in an array as per specifications
};

// Returning the transformed data
return brazecall;
```

### Usar a pontuação CSAT na Braze {#use-csat-score-in-braze}

1. Acesse **Data Settings** > **Data Transformations** > **Create transformation**.
2. Selecione **Start from scratch**, selecione o destino **POST: Track Users** e selecione **Create transformation**.
3. No editor de transformação, copie o código de exemplo de **Rastrear pontuação CSAT** nesta seção e insira-o no campo **Transformation code**. Selecione **Save**, copie a **Webhook URL** e abra a Dixa.
4. Na Dixa, acesse **Settings** > **Integrations** > **Webhooks** > **+ Outbound webhook**.
5. Na página de configurações do webhook, cole a URL da Braze e ative os eventos que deseja rastrear. **Conversation created** é um bom ponto de partida para rastrear as conversas dos clientes.
6. Selecione **Save** para concluir a configuração da Dixa.

#### Rastrear pontuação CSAT {#track-csat-score}

```js
const body = payload?.data;

// values from your webhook
const score = body.score;         // number
const comment = body.comment;     // string
const type = body.type;           // string
const ratedAt = body.event_timestamp;   // ISO 8601 string
const contactemail = body.conversation.requester.email;

// ALWAYS identify by email
const email = contactemail;

if (!email) {
  // Can't identify a user without email
  return { attributes: [] };
}


let brazecall = {
  "attributes": [
    {
      // Using the Dixa user email as the external_id to identify the user in Braze
      "email": contactemail,
      "_update_existing_only": true,

      // Your new custom object attribute
      "last_csat": {
        "score": score,
        "comment": comment,
        "type": type,
        "rated_at": ratedAt
      }
    }
  ]
};

return brazecall;
```
