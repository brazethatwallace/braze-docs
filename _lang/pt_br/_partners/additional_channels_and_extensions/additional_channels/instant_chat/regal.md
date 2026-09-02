---
nav_title: Regal
article_title: Regal
description: "Este artigo de referência descreve a parceria entre a Braze e a Regal, uma plataforma de agentes de IA por voz que ajuda você a orquestrar jornadas personalizadas e omnicanal para clientes usando dados da Braze e conversas da Regal."
alias: /partners/regal/
page_type: partner
search_tag: Partner
---

# Regal

> [Regal.io](https://regal.io) é uma plataforma de agentes de IA por voz que ajuda empresas a oferecer melhores experiências ao cliente por meio de conversas inteligentes e em tempo real em diversos canais.

_Essa integração é mantida pela Regal._

Ao integrar a Regal com a Braze, você pode unificar dados comportamentais e IA conversacional para orquestrar jornadas personalizadas e omnicanal para clientes. A Braze captura sinais ao longo do ciclo de vida do cliente, que a Regal usa para alimentar conversas com agentes de IA, roteamento e decisões em tempo real.

Use dados da Braze para definir o que seus agentes de IA dizem, como respondem e quando interagir. Envie resultados e insights de conversas de volta para a Braze para melhorar o direcionamento e o marketing de ciclo de vida. Dispare chamadas e SMS com IA em momentos-chave da jornada do cliente e faça o acompanhamento na Braze com base no que acontece em cada conversa.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Regal | Uma conta Regal é necessária para aproveitar esta parceria. |
| Chave de API Regal | Uma chave de API Regal permite que você envie eventos da Braze para a Regal.<br><br>Envie um e-mail para [support@regal.io](mailto:support@regal.io) para obter essa chave. |
| Transformação de Dados da Braze | Uma [Transformação de Dados]({{site.baseurl}}/user_guide/data/unification/data_transformation) é necessária para receber dados da Regal. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração: Enviando dados da Braze para a Regal {#integration-sending-data-from-braze-to-regal}

Use webhooks de Canvas ou Campaign da Braze para enviar dados de perfil de usuário e eventos da Braze para a Regal.

### Etapa 1: Criar novos contatos na Regal {#step-1-create-new-contacts-in-regal}

Crie um Canvas ou Campaign que envie webhooks para a Regal sempre que um novo perfil da Braze for criado e precisar estar disponível para chamadas e mensagens de texto na Regal.

1. Crie um Canvas ou Campaign intitulado "Create New Contact for Regal" e selecione **Action-Based** como tipo de entrada.

2. Defina a lógica de disparo como **Custom Event** e selecione o evento que é acionado quando um perfil com número de telefone é criado. A Regal também recomenda adicionar um filtro para confirmar que o campo de telefone está preenchido.

3. No novo modelo de webhook, preencha os seguintes campos:
   - **URL do webhook**: <https://events.regalvoice.com/events>
   - **Corpo da solicitação**: Raw Text

#### Cabeçalhos e método da solicitação {#request-headers-and-method}

A Regal também requer um cabeçalho HTTP para autorização e um método HTTP. Os seguintes estão incluídos no modelo como pares de chave-valor na guia **Settings**:
{% raw %}
- **Método HTTP**: POST
- **Cabeçalhos da solicitação**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação {#request-body}

O único identificador obrigatório é um número de telefone dentro de `traits.phones`. Use o objeto `traits.phones` para associar um ou mais números de telefone a um contato. Cada número de telefone pode armazenar seu próprio rótulo, designação principal e status de aceitação de voz e SMS. Essa estrutura é especialmente útil quando um contato possui vários números de telefone.

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "custom1": "<custom1>",
    "custom2": "<custom2>"
  },
  "eventSource": "braze"
}
```

Este exemplo de carga útil presume que os números de telefone listados incluem o status atual de consentimento de voz e SMS. Se esse não for o caso, você pode omitir `voiceOptIn` e `smsOptIn` ao criar o contato e configurar um Canvas ou Campaign separado para atualizar o consentimento no número de telefone relevante quando a aceitação for coletada.

### Etapa 2: Atualizar informações de aceitação {#step-2-update-opt-in-information}

Se a aceitação e a recusa podem ocorrer em diferentes momentos do seu app, atualize a Regal quando os usuários alterarem o status da inscrição.

A Regal recomenda usar o esquema `traits.phones` para que você possa gerenciar a aceitação e a recusa por número de telefone, em vez de no nível do contato.

Use a seguinte configuração de Canvas para enviar informações de aceitação atualizadas para a Regal.

1. Crie um novo Canvas ou Campaign intitulado "Send Opt In or Out to Regal".

2. Selecione uma das seguintes opções de disparo e, em seguida, selecione o campo que representa o status de aceitação do usuário:
    - **User Profile Field Updated**
    - **Update Subscription Group Status**
    - **Subscription Status**

3. No novo modelo de webhook, preencha os seguintes campos:
   - **URL do webhook**: <https://events.regalvoice.com/events>
   - **Corpo da solicitação**: Raw Text

#### Cabeçalhos e método da solicitação

A Regal também requer um cabeçalho HTTP para autorização e um método HTTP. Os seguintes estão incluídos no modelo como pares de chave-valor na guia **Settings**:
{% raw %}
- **Método HTTP**: POST
- **Cabeçalhos da solicitação**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<phoneNumber>": {
        "voiceOptIn": {
          "subscribed": "<voice_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": "<sms_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    }
  },
  "eventSource": "braze"
}
```

Você também pode incluir atributos adicionais do perfil de usuário nessa carga útil para manter outros atributos atualizados ao mesmo tempo.

### Etapa 3: Enviar eventos personalizados {#step-3-send-custom-events}

Configure um Canvas ou Campaign para cada evento-chave que você deseja enviar para a Regal.

Esses eventos fazem mais do que disparar ações de alcance (por exemplo, um texto de confirmação quando um lead conclui a inscrição). Eles fornecem o contexto em tempo real que impulsiona a forma como os agentes de IA da Regal falam, tomam decisões e direcionam conversas ao longo da jornada do cliente. Ao enviar dados de eventos e atributos da Braze, você permite que os agentes de IA adaptem as conversas com base no comportamento, nas preferências e na etapa do ciclo de vida de cada usuário.

Por exemplo, eventos e atributos da Braze podem ser usados na Regal para:

- **Personalizar a fala do agente de IA**: Fazer referência a comportamentos recentes ou interesses de produto diretamente nas conversas.
  - Exemplo: Se um usuário explorou opções de seguro de vida, o agente pode fazer referência a `contact.firstName` e `contact.brazeProductInterest` na conversa.
- **Conduzir lógica dinâmica de conversa**: Ajustar o que o agente prioriza em tempo real.
  - Exemplo: Se `contact.brazeAge` for maior que 65, priorizar a cobertura Medicare; caso contrário, focar em planos ACA e no status atual do seguro.
- **Possibilitar roteamento e escalonamento inteligentes**: Direcionar conversas com base em valor ou intenção.
  - Exemplo: Se `contact.brazeLeadTier` for "High Value", transferir para um agente sênior após a qualificação; caso contrário, continuar com o agente de IA.
- **Alinhar mensagens e ofertas**: Personalizar o que o agente apresenta com base no contexto da Campaign.
  - Exemplo: Se `contact.brazeCampaignName` for "Spring Mortgage Promo", destacar a oferta promocional durante a conversa.

Crie um novo Canvas ou Campaign intitulado "Send Product Interest Event to Regal."

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "brazeProductInterest": "Life Insurance",
    "brazeAge": 68,
    "brazeLeadTier": "High Value",
    "brazeCampaignName": "Spring Insurance Promo"
  },
  "name": "Product Interest Captured",
  "properties": {
    "action": "Viewed Product Comparison",
    "productCategory": "Life Insurance",
    "intentScore": "High",
    "lastPage": "Compare Life Insurance Plans",
    "readyToCommit": true
  },
  "eventSource": "braze"
}
```

#### Atributos de contato atualizados {#up-to-date-contact-attributes}

A Regal também recomenda enviar atributos-chave do perfil de usuário nas cargas úteis de eventos para que a Regal tenha atributos de contato atualizados quando eventos importantes ocorrerem.

{% alert note %}
Se você tiver dúvidas sobre quais eventos enviar para a Regal ou como configurar esses Canvas e Campaigns, envie um e-mail para [support@regal.io](mailto:support@regal.io).
{% endalert %}

## Integração: Enviando dados da Regal para a Braze {#integration-sending-data-from-regal-to-braze}

Use os Webhooks de Relatório da Regal e a Transformação de Dados da Braze para enviar eventos de relatório da Regal (como `SMS.sent` e `call.completed`) para a Braze. Depois de mapear esses eventos, eles aparecem nos perfis de usuário e ficam disponíveis para segmentação, Canvas e Campaigns.

### Etapa 1: Criar uma Transformação de Dados na Braze {#step-1-create-a-data-transformation-in-braze}

Crie uma Transformação de Dados para cada webhook da Regal que você planeja enviar para a Braze.

Para criar uma Transformação de Dados:
1. Acesse a página **Transformations** no seu dashboard da Braze.
2. Dê um nome à sua transformação e clique em **Create transformation**.
3. Na lista de transformações, selecione <i class="fa-solid fa-ellipsis-vertical" title="Ver ações"></i> **View actions** e selecione **Copy webhook URL**.

### Etapa 2: Ativar webhooks de relatório na Regal {#step-2-enable-reporting-webhooks-in-regal}

Para configurar webhooks de relatório:
1. Acesse o app da Regal e abra a página **Settings**.

2. Na seção **Reporting Webhooks**, clique em **Create Webhooks**.

3. No campo de entrada do endpoint do webhook, adicione a URL do webhook de Transformação de Dados da Braze para a Transformação de Dados associada.

#### Atualizando um endpoint {#updating-an-endpoint}

Quando você edita um endpoint, pode levar até 5 minutos para o cache ser atualizado e enviar eventos para o seu novo endpoint.

#### Tentativas {#retries}

Atualmente, a Regal não realiza novas tentativas para esses eventos. Se a Braze não responder em 5 segundos, a Regal descarta o evento. A Regal planeja adicionar novas tentativas em uma versão futura.

#### Eventos {#events}
Para a lista completa de eventos de relatório, definições de propriedades e cargas úteis de exemplo, consulte o [guia de Webhooks de Relatório](https://developer.regal.io/docs/reporting-webhooks#events) da Regal.

### Etapa 3: Transformar eventos da Regal em eventos da Braze {#step-3-transform-regal-events-into-braze-events}

O recurso de [Transformação de Dados]({{site.baseurl}}/user_guide/data/unification/data_transformation) da Braze permite mapear eventos recebidos da Regal no formato necessário para serem adicionados como atributos, eventos ou compras na Braze.

1. Dê um nome à sua Transformação de Dados. É recomendado configurar uma Transformação de Dados por webhook de evento.

2. Para testar a conexão, crie uma chamada de saída a partir do Agent Desktop da Regal para o seu telefone e envie o formulário de Resumo da Conversa para criar um evento `call.completed`.

3. Determine quais identificadores você usará para mapear seus contatos da Regal aos seus perfis na Braze. Os identificadores disponíveis nos eventos da Regal incluem:
   - `userId` - definido nos eventos apenas se você tiver enviado esse identificador para um contato anteriormente
   - `traits.phone`
   - `traits.email` - definido nos eventos apenas se você tiver enviado esse identificador para um contato anteriormente

Nas cargas úteis de eventos da Braze para a Regal, a Regal recomenda usar `traits.phones` para dar suporte a múltiplos números de telefone e consentimento em nível de telefone. Nos eventos de relatório da Regal enviados de volta para a Braze, `traits.phone` ainda pode aparecer como identificador nas cargas úteis de eventos.

#### Identificadores compatíveis com a Braze {#braze-supported-identifiers}
- A Braze não aceita números de telefone como identificador. Para usar isso como identificador, o número de telefone pode ser definido como um [alias de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) na Braze.
- Ao usar a Transformação de Dados da Braze, o endereço de e-mail pode ser usado como identificador. Se o endereço de e-mail já existir como um perfil na Braze, o perfil existente será atualizado. Se o endereço de e-mail ainda não existir na Braze, um perfil somente com e-mail será criado.

## Casos de uso {#use-cases}

{% tabs %}
{% tab Disparar um e-mail %}

**Disparar um e-mail da Braze com base em uma disposição de chamada no Regal**

A carga útil de exemplo a seguir mostra um evento `call.completed` no Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Alex",
    "agent_fullname": "Alex Lee",
    "agent_id": "xxxx@example.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+15555550200",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+15555550123",
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

A Transformação de Dados de exemplo a seguir mapeia isso para um evento personalizado na Braze.

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
{% tab Atualizar atributos de perfil %}

**Atualizar atributos de perfil na Braze com base em eventos `contact.attribute.edited` do Regal**

A carga útil de exemplo a seguir mostra um evento `contact.attribute.edited` no Regal. O Regal envia esse evento quando um agente atualiza um atributo no perfil de um contato durante uma conversa.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@example.com",
    "contact_phone": "+15555550123",
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

A Transformação de Dados de exemplo a seguir mapeia os novos valores de propriedade personalizada para os atributos relevantes nos seus perfis da Braze:

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
{% tab Manter seus experimentos sincronizados %}

**Mantenha seus experimentos na Braze e no Regal sincronizados usando eventos `contact.experiment.assigned`**

A carga útil de exemplo a seguir mostra um evento `contact.experiment.assigned` no Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
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

A Transformação de Dados de exemplo a seguir mapeia isso para um evento personalizado na Braze.

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
{% tab Cancelar inscrição de um contato %}

**Cancelar a inscrição de um contato na Braze com base em eventos `contact.unsubscribed` do Regal**

A carga útil de exemplo a seguir mostra um evento `contact.unsubscribed` no Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com",
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

A Transformação de Dados de exemplo a seguir cancela a inscrição do contato na Braze.

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
{% tab Disparar acompanhamento a partir da análise da chamada %}

**Dispare jornadas de acompanhamento personalizadas na Braze com base em eventos `call.analysis.available` do Regal**

Use o evento `call.analysis.available` do Regal para identificar o motivo principal pelo qual um cliente não converteu e disparar uma jornada de acompanhamento personalizada na Braze.

Por exemplo:

- Quando a objeção principal for preço, envie um e-mail de acompanhamento orientado a valor.
- Quando a objeção principal for timing, coloque o usuário em uma sequência de nutrição para reconsideração posterior.
- Quando a objeção principal for confiança, envie depoimentos, avaliações ou garantias de conformidade.
- Quando `needs_human_agent` for verdadeiro, notifique a equipe de vendas ou suporte e suprima o envio de mensagens automatizadas adicionais.

A carga útil de exemplo a seguir mostra um evento `call.analysis.available` no Regal.

```json
{
  "traits": {
    "phone": "+1XXXXXXXXXX",
    "email": "xxx@example.com"
  },
  "name": "call.analysis.available",
  "brand": "circle-bank",
  "contact_email": "xxx@example.com",
  "contact_phone": "+1XXXXXXXXXX",
  "created_at": "1754079836",
  "entity_type": "event",
  "event_id": "9f5d8dbb2973b0e2359c6fd34111111",
  "event_type": "regal_voice_event",
  "external_id": "41dd1aa2-1111-f011-a2d5-00505611111",
  "original_timestamp": "1754079835",
  "profile_id": "62653af1111111173af128291e92",
  "properties": {
    "agent_email": "xxx@example.com",
    "call_analysis": {
      "purchase_intent": "medium",
      "primary_objection": "price",
      "secondary_objection": "needs_to_compare",
      "product_interest": "Life Insurance",
      "follow_up_required": true,
      "follow_up_email_text": "Thanks for speaking with us today. I know cost is top of mind, so I wanted to send over a simple summary of the life insurance options we discussed and what may fit your budget.",
      "recommended_next_action": "send_value_oriented_follow_up",
      "needs_human_agent": false,
      "customer_sentiment_label": "interested_but_hesitant"
    },
    "contact_phone": "+1XXXXXXXXXX",
    "incoming_sip_headers": {
      "Via": "SIP/2.0/UDP srv1.example.com;branch=z9hG4bK776asdhds",
      "From": "<sip:customer@example.com>;tag=1928301774",
      "Call-ID": "a84b4c76e66710"
    },
    "is_ai_agent": true,
    "outgoing_sip_headers": {
      "Via": "SIP/2.0/TCP srv2.example.com;branch=z9hG4bKgsdh7723",
      "To": "<sip:agent@example.com>",
      "User-Agent": "RegalVoiceAI/1.0"
    },
    "task_id": "WT7f3ea47fa6e6055aa847f0a62111111"
  },
  "originalTimestamp": "1754079835",
  "source": "Regal Voice"
}
```

Use uma Transformação de Dados para mapear os campos de `call_analysis` (como `primary_objection` e `needs_human_agent`) para eventos personalizados ou atributos de perfil na Braze. Em seguida, crie a lógica de Canvas ou Campaign na Braze com ramificações baseadas nesses valores.

{% endtab %}
{% tab Armazenar links de transcrição de chamada %}

**Atualizar atributos de perfil com links de transcrição a partir de eventos `call.transcript.available`**

Use o evento `call.transcript.available` para enviar um link para a transcrição completa da chamada à Braze. Mapeie a URL da transcrição para um atributo de perfil de usuário da Braze com uma Transformação de Dados, para que sua equipe possa acessar e revisar as conversas a partir do perfil de usuário.

A carga útil de exemplo a seguir mostra um evento `call.transcript.available` no Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "call.transcript.available",
  "properties": {
    "agent_email": "xxx@example.com",
    "task_id": "WT953358e8822dd9333fc38dfbac25e1e1",
    "call_summary": "The agent Yuri explained insurance options to Alex and he said he'll need to think about it before moving forward Agent politely ended the call.",
    "contact_name": "Alex Smith",
    "contact_phone": "+15555550123",
    "is_voicemail": false,
    "moments_count": 18,
    "recording_id": "RE0118052841b7299d0630d1dff610c1fb",
    "recording_link": "https://api.twilio.com/2010-04-01/Accounts/ACxxx/Recordings/xxx.mp3",
    "recording_duration": 78.75987,
    "request_timestamp": 1657799128,
    "response_timestamp": 1657799136,
    "sentiments": {
      "contact_sentiment": 70,
      "agent_sentiment": 75,
      "agent_sentiment_reason": "Yuri was polite and attentive, effectively gathering information and providing a resource, which contributed to a positive interaction.",
      "contact_sentiment_reason": "Alex was satisfied with the information provided but may have wanted more assistance regarding insurance options."
    },
    "trackers": [
      {
        "tracker_id": "4be87957-9140-4451-894a-bdbaed1f2460",
        "tracker_name": "Refinance"
      },
      {
        "tracker_id": "eb2577c6-5e23-4c65-9e04-5cc5d49eee7e",
        "tracker_name": "High Intent"
      }
    ],
    "transcript": "[handling agent]: Hi Alex, this is Yuri with BrightCover Insurance. I'll be going over some insurance options with you today. [contact]: Sounds good. [handling agent]: Before we start, I'm going to transfer you to a specialist for a moment. One sec. [transfer agent]: Hi Alex, this is Lee. Just verifying a few details before sending you back to Yuri. [contact]: Okay. [handling agent]: Thanks, Alex. Based on what you shared, here are some plan options... [contact]: I'll need to think about it. [handling agent]: Totally understandable. Feel free to reach out anytime. Have a great day! END OF TRANSCRIPT",
    "transcript_is_truncated": false,
    "transcript_url": "https://app.regalvoice.com/transcripts/WT953358e8822dd9333fc38dfbac25e1e1"
  },
  "originalTimestamp": "1657843308",
  "eventSource": "Regal Voice",
  "eventId": "f49a3cf9cb1336683bd5f19dwe4c61147"
}
```

{% endtab %}
{% endtabs %}