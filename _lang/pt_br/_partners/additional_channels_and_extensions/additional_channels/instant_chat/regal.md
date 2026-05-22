---
nav_title: Regal
article_title: Regal
description: "Este artigo de referência descreve a parceria entre a Braze e a Regal, uma solução de vendas por telefone e SMS que permite usar dados de ambas as fontes para criar experiências personalizadas para seus clientes."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io) é a solução de vendas por telefone e SMS construída para gerar mais conversas, para que você possa atingir suas metas de crescimento muito mais rápido.

Ao integrar a Regal e a Braze, você pode criar uma experiência mais consistente e personalizada em todos os pontos de contato com o cliente.
- Envie o próximo melhor e-mail ou notificação por push da Braze com base no que foi dito em uma conversa telefônica na Regal.
- Dispare uma chamada na Regal quando um cliente de alto valor clica em um e-mail de marketing da Braze, mas não converte.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Regal | É necessário ter uma conta Regal para aproveitar essa parceria. |
| Chave de API da Regal | Uma chave de API da Regal permitirá o envio de eventos da Braze para a Regal.<br><br>Envie um e-mail para [support@regal.io](mailto:support@regal.io) para obter essa chave. |
| Transformação de dados da Braze | A Transformação de dados está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente da Braze se tiver interesse em participar do acesso antecipado. Isso é necessário para receber dados da Regal. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integração: envio de dados da Braze para a Regal {#integration-sending-data-from-braze-to-regal}

A seção a seguir descreve como usar a Braze como fonte para enviar o perfil do cliente e os dados de eventos para a Regal usando webhooks de Canvas ou Campaign da Braze.

### Etapa 1: Criar novos contatos na Regal {#step-1-create-new-contacts-in-regal}

Crie um Canvas ou uma Campaign que envie webhooks para a Regal sempre que um novo contato for criado na Braze e que você queira que esteja disponível para chamadas e mensagens de texto na Regal.

1. Crie um Canvas ou uma Campaign intitulada "Create New Contact for Regal" e selecione **Action-Based** como o tipo de entrada.

2. Defina a lógica do disparo como **Custom Event** e selecione o evento que é disparado quando um contato com um número de telefone é criado. A Regal também recomenda adicionar um filtro extra no campo do telefone para garantir que ele esteja definido.

3. Em seu novo modelo de webhook, preencha os seguintes campos:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **Request Body**: Raw Text

#### Cabeçalhos de solicitação e método {#request-headers-and-method}

A Regal.io também requer um cabeçalho HTTP para autorização e um método HTTP. O seguinte já estará incluído no modelo como um par de valores-chave na guia **Settings**:
{% raw %}
- **HTTP Method**: POST
- **Request Headers**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação {#request-body}

O único campo obrigatório abaixo é a propriedade `traits.phone`. O restante é opcional. No entanto, se você incluir `optIn`, deverá incluir `optIn.channel` e `optIn.subscribed`.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "email": "<email>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": true
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": true
            }
        ],
        "custom1": "<custom1>",
        "custom2": "<custom2>"
    },
    "eventSource": "braze"
}
```

O exemplo de carga útil acima pressupõe que todos os seus contatos aceitaram o opt-in para voz e SMS. Se isso não for válido para o seu caso, você pode remover a propriedade `optIn` do exemplo acima e configurar um Canvas ou uma Campaign separada para atualizar um contato na Regal quando o `optIn` for coletado.

### Etapa 2: Atualizar informações de opt-in {#step-2-update-opt-in-information}

Se o opt-in e o cancelamento puderem ocorrer em diferentes partes da experiência do usuário no app, é importante atualizar a Regal à medida que os usuários aceitarem ou cancelarem. Abaixo está um Canvas recomendado para enviar informações de opt-in atualizadas para a Regal. Ele pressupõe que você salva essas informações como campo de perfil na Braze. Se não for o caso, o disparo pode ser um evento na sua conta da Braze que represente o opt-in ou o cancelamento de inscrição de um usuário (o exemplo abaixo é para opt-in por telefone, mas você pode configurar um Canvas ou Campaign semelhante para opt-in por SMS, caso faça a coleta separadamente).

1. Crie um novo Canvas ou Campaign com o título "Send Opt In or Out to Regal".

2. Selecione uma das seguintes opções de disparo e escolha o campo que representa o status de opt-in do usuário. Se você disparar um evento para a Braze para representar o opt-in ou o cancelamento, use esse evento como o gatilho.
    - User Profile Field Updated
    - Update Subscription Group Status
    - Subscription Status

3. Em seu novo modelo de webhook, preencha os seguintes campos:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **Request Body**: Raw Text

#### Cabeçalhos de solicitação e método

A Regal.io também requer um cabeçalho HTTP para autorização e um método HTTP. O seguinte já estará incluído no modelo como um par de valores-chave, mas na guia **Settings**:
{% raw %}
- **HTTP Method**: POST
- **Request Headers**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação

Você também pode adicionar outros atributos de perfil de usuário nessa carga útil se quiser garantir que mais atributos sejam atualizados simultaneamente.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            }
        ]
    },
    "eventSource": "braze"
}
```

### Etapa 3: Enviar eventos personalizados {#step-3-send-custom-events}

Por fim, configure um Canvas ou uma Campaign para cada um dos principais eventos que deseja enviar à Regal. A Regal recomenda o envio de quaisquer eventos que sejam importantes para disparar SMS e chamadas na Regal (como um evento em cada etapa do fluxo de inscrição ou compra) ou que sejam usados como critérios de saída para que os contatos saiam das Campaigns da Regal.

Por exemplo, abaixo está um fluxo de trabalho para enviar um evento à Regal quando um usuário conclui a primeira etapa de uma aplicação.

1. Crie um novo Canvas ou Campaign com o nome "Send Application Step 1 Completed Event to Regal".

2. Defina a lógica do nó de gatilho como **Custom Event** e selecione o nome do evento que deseja enviar à Regal, como "Application Step 1 Completed".

3. Em seu novo modelo de webhook, preencha os seguintes campos:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **Request Body**: Raw Text

#### Cabeçalhos de solicitação e método

A Regal.io também requer um cabeçalho HTTP para autorização e um método HTTP. O seguinte já estará incluído no modelo como um par de valores-chave, mas na guia **Settings**:
{% raw %}
- **HTTP Method**: POST
- **Request Headers**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação

Você pode adicionar outros atributos de perfil de usuário nessa carga útil se quiser garantir que mais atributos sejam atualizados simultaneamente.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "custom1": "<custom1>",
        "custom2": "<custom2>",
        "custom3": "<custom3>"
    },
    "name": "Application Step 1 Completed",
    "properties": {
      "educationalLevel": "<educationalLevel>",
      "preferredLocation": "<preferredLocation>",
      "preferredSubject": "<preferredSubject>",
      "readytoCommit": true
    },
    "eventSource": "braze"
}
```

#### Atributos de contato atualizados {#up-to-date-contact-attributes}

Embora não seja necessário, a Regal recomenda também enviar quaisquer campos de dados de perfil de usuário importantes nas cargas úteis dos fluxos de trabalho de eventos para garantir que a Regal tenha acesso aos atributos de contato mais atualizados no momento em que os eventos importantes estiverem disponíveis.

{% alert note %}
Se tiver dúvidas sobre quais eventos são importantes para enviar à Regal ou sobre a melhor forma de configurar esses Canvas e Campaigns, entre em contato pelo e-mail support@regal.io.
{% endalert %}

## Integração: envio de dados da Regal para a Braze {#integration-sending-data-from-regal-to-braze}

Esta seção descreve como obter eventos de relatórios da Regal, como `SMS.sent` e `call.completed`, na Braze para que eles possam aparecer em seus perfis da Braze e estar disponíveis na ferramenta de segmentação da Braze, no Canvas e nas Campaigns. Essa integração usa os webhooks de relatórios da Regal e a Transformação de dados da Braze para automatizar o fluxo de dados.

### Etapa 1: Criar uma Transformação de dados na Braze {#step-1-create-a-data-transformation-in-braze}

{% alert important %}
A Transformação de dados está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente da Braze se tiver interesse em participar do acesso antecipado.
{% endalert %}

A Braze recomenda criar uma transformação para cada webhook da Regal que você planeja enviar à Braze.

Para criar uma Transformação de dados:
1. Navegue até a página **Transformations** no dashboard da Braze.
2. Dê um nome à sua transformação e clique em **Create transformation**.
3. Na lista de transformações, clique em <i class="fa-solid fa-ellipsis-vertical" title="Exibir ações"></i> e selecione **Copy webhook URL**.

![]({% image_buster /assets/img/regal/copy_webhook_url.png %})

### Etapa 2: Ativar webhooks de relatórios na Regal {#step-2-enable-reporting-webhooks-in-regal}

Para configurar webhooks de relatórios:
1. Acesse o app da Regal e abra a página **Settings**.

2. Na seção **Reporting Webhooks**, clique em **Create Webhooks**.

3. Na entrada do endpoint do webhook, adicione a URL do webhook da Transformação de dados da Braze para a transformação de dados associada.

![]({% image_buster /assets/img/regal/edit_webhook.png %}){: style="max-width:60%;"}

#### Atualização de um endpoint {#updating-an-endpoint}
Quando você edita um endpoint, pode levar até 5 minutos para que o cache seja atualizado e envie eventos para o novo endpoint.
#### Tentativas {#retries}
Atualmente, não há novas tentativas nesses eventos. Se uma resposta não for recebida em 5 segundos, o evento será descartado e não passará por novas tentativas. A Regal adicionará novas tentativas em uma versão futura.
#### Eventos {#events}
O [guia de webhooks de relatórios](https://developer.regal.io/docs/reporting-webhooks#events) da Regal inclui a lista completa de eventos de relatório que eles publicam. Lá você pode ver definições de propriedades e exemplos de cargas úteis.

### Etapa 3: Transformar os eventos da Regal em eventos da Braze {#step-3-transform-regal-events-into-braze-events}

O recurso [Transformação de dados]({{site.baseurl}}/data_transformation/) da Braze permite que você mapeie eventos recebidos da Regal no formato necessário para serem adicionados como atributos, eventos ou compras na Braze.

1. Dê um nome à sua Transformação de dados. Recomenda-se configurar uma Transformação de dados por webhook de evento.

2. Para testar a conexão, crie uma chamada de saída do Regal Agent Desktop para seu celular e envie o formulário de resumo da conversa para criar um evento call.completed.

3. Determine quais identificadores serão usados para mapear seus contatos da Regal para seus perfis da Braze. Os identificadores disponíveis nos eventos da Regal incluem:
   - `userId` — somente definido em eventos se você tiver enviado anteriormente esse identificador para um contato
   - `traits.phone`
   - `traits.email` — somente definido em eventos se você tiver enviado anteriormente esse identificador para um contato

#### Identificadores compatíveis com a Braze {#braze-supported-identifiers}
- A Braze não oferece suporte a números de telefone como identificador. Para usar isso como um identificador, o número de telefone pode ser definido como um [alias de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) na Braze.
- Ao usar a Transformação de dados da Braze, o endereço de e-mail pode ser usado como identificador. Se o endereço de e-mail existir como perfil na Braze, o perfil existente será atualizado. Se o endereço de e-mail ainda não existir na Braze, será criado um perfil somente de e-mail.

## Casos de uso {#use-cases}

{% tabs %}
{% tab Trigger an email %}

**Disparar um e-mail da Braze com base em uma disposição de chamada na Regal**

Abaixo está um exemplo de carga útil para um evento `call.completed` na Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Rebecca",
    "agent_fullname": "Rebecca Greene",
    "agent_id": "xxxx@yourbrand.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+19545558563",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+17625555555",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

Abaixo está um exemplo de Transformação de dados para mapear isso para um evento personalizado na Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Update profile attributes %}

**Atualizar os atributos do perfil na Braze com base nos eventos `contact.attribute.edited` da Regal**

Abaixo está um exemplo de carga útil para um evento `contact.attribute.edited` na Regal. Esse evento é disparado sempre que um de seus agentes aprende algo novo em uma conversa e atualiza um atributo no perfil do contato.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@yourbrand.com",
    "contact_phone": "+17625555555",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

Abaixo está um exemplo de Transformação de dados para mapear os novos valores de propriedades personalizadas para os atributos relevantes em seus perfis da Braze:

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Keep your experiments in sync %}

**Mantenha seus experimentos na Braze e na Regal em sincronia usando os eventos `contact.experiment.assigned`**

Abaixo está um exemplo de carga útil para um evento `contact.experiment.assigned` na Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

Abaixo está um exemplo de Transformação de dados para mapear isso para um evento personalizado na Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab Unsubscribe a contact %}

**Cancelar inscrição de um contato na Braze com base em um `contact.unsubscribed` da Regal**

Abaixo está um exemplo de carga útil para um evento `contact.unsubscribed` na Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

Abaixo está um exemplo de Transformação de dados para cancelar a inscrição do contato na Braze.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% endtabs %}