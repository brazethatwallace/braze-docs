---
nav_title: Rokt Calendar
article_title: Rokt Calendar
description: "Este artigo de referência descreve a parceria entre a Braze e o Rokt Calendar, uma tecnologia dinâmica de marketing de calendário que permite às marcas enviar eventos e comunicações promocionais 1:1 na forma de eventos de calendário e notificações."
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Rokt Calendar

> O [Rokt Calendar](https://www.rokt.com/rokt-calendar/) é uma tecnologia dinâmica de marketing de calendário que permite às marcas enviar eventos 1:1 e comunicações promocionais na forma de eventos de calendário e notificações.

_Essa integração é mantida pelo Rokt Calendar._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Rokt Calendar permite que os assinantes do Rokt Calendar e seus dados sejam enviados para a Braze por meio de webhooks da Braze. Você pode então usar esses dados em Canvas da Braze para direcionamento de jornada e segmentação de público usando qualquer um dos seguintes [atributos personalizados do Rokt Calendar](#audience-segmentation).

## Pré-requisitos {#prerequisites}

| Requisito  | Descrição |
| ------------ | ----------- |
| Conta Rokt Calendar | É necessário ter uma conta Rokt Calendar específica do cliente para aproveitar essa parceria. Entre em contato com [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) para falar com um gerente de contas  |
| Configuração do Rokt Calendar | Seu gerente de conta do Rokt Calendar trabalhará com você para configurar o calendário da forma mais adequada às suas necessidades, incluindo configurações como:<br>- Flag de mesclagem<br>- Flag de fallback de SubscriberID<br>- Captura de e-mail, se necessário |
| Credenciais OAuth do Rokt Calendar | Essa chave, fornecida pelo gerente da sua conta Rokt Calendar, permitirá conectar suas contas da Braze e do Rokt Calendar.<br><br>Isso pode ser criado no dashboard da Braze em **Settings** > **Connected Content**. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. Você precisará fornecer essa chave ao seu gerente de conta do Rokt Calendar.<br><br> Isso pode ser criado no dashboard da Braze em **Settings** > **API Keys**. |
| [Endpoint REST da Braze]({{site.baseurl}}/api/basics/#endpoints) | A URL do seu endpoint REST. Seu endpoint dependerá da URL da Braze para a sua instância. |
| ID do assinante externo | Esse é o identificador usado pelo processo de inscrição do Rokt Calendar para fazer a correspondência entre o assinante do calendário e o usuário da Braze. Isso é algo que você passa para o Rokt Calendar.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Segmentação de público {#audience-segmentation}

Quando o Rokt Calendar cria um novo usuário ou faz a correspondência de um assinante existente com um usuário da Braze, o Rokt Calendar enviará os seguintes atributos personalizados de inscrição que você pode filtrar na Braze:

| Atributo personalizado  | Definição       | Exemplo          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Código da conta do Rokt Calendar | `brazetest/f5733866ade2` e `brazetest/ff10919f1078` |
| `rokt:account_id` | ID da conta do Rokt Calendar | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Nome da conta do Rokt Calendar | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Código do calendário Rokt Calendar | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | ID do calendário Rokt Calendar | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Título do calendário Rokt Calendar | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | Código do país relacionado à inscrição criada | `AU/f5733866ade2` |
| `rokt:device_name` | Tipo de dispositivo relacionado à inscrição criada | `Desktop/f5733866ade2` |
| `rokt:geo_country` | País de origem relacionado à inscrição criada | `Australia/f5733866ade2` |
| `rokt:optIn1` | Se o usuário fez opt-in na primeira de duas opções de opt-in relacionadas à inscrição criada | `True/f5733866ade2` |
| `rokt:optIn2` | Se o usuário fez opt-in na segunda de duas opções de opt-in relacionadas à inscrição criada | `True/f5733866ade2` |
| `rokt:source` | A origem da inscrição criada | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | O endereço de e-mail inserido pelo usuário durante o processo de inscrição | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | O ID da inscrição, que serve como identificador único, relacionado à inscrição criada | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | Método de inscrição (webcal/Google) relacionado à inscrição criada. | `WebCal/f5733866ade2` |
| `rokt:tags` | Tags de calendário usadas relacionadas à inscrição criada. | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Audience segmentation #audience-segmentation" }

O Rokt Calendar também acionará um evento personalizado `subscribe` assim que o usuário se inscrever no seu calendário Rokt, que pode ser usado na segmentação da Braze ou como gatilho para uma Campaign ou componente do Canvas.

## Integração {#integration}

### Etapa 1: crie um público de assinantes do calendário {#step-1-building-an-audience-of-calendar-subscribers}

Para enviar eventos de calendário a partir do Canvas, você precisa primeiro ter um calendário Rokt configurado com usuários já inscritos. Para isso, será necessário informar aos seus usuários onde e como se inscrever no calendário. O Rokt Calendar recomenda que você:

#### Forneça pontos de integração de inscrição {#provide-subscription-integration-points}
Para criar um público de assinantes do calendário, você precisará oferecer um destino para o qual o usuário possa navegar e se inscrever. Alguns exemplos de pontos de integração de inscrição incluem:
  - Adicionar um botão de calendário ao seu site
  - Adicionar um link de calendário em um e-mail ou SMS
  - Adicionar um botão de calendário ao seu app
  - Adicionar um link de calendário nas redes sociais

#### Promova o calendário {#promote-the-calendar}
Para criar um público de assinantes, você precisará promover o calendário para o seu público, para que eles saibam como se inscrever. Alguns exemplos de promoção de calendário incluem:
  - Publicações em redes sociais
  - Newsletters e atualizações por e-mail
  - Publicações no blog
  - Notificações no app

### Etapa 2: crie um webhook do Rokt Calendar na Braze {#step-2-create-a-rokt-calendar-webhook-in-braze}

Na Braze, você pode configurar uma campanha de webhook ou um webhook dentro de um Canvas para:

- Enviar um novo evento personalizado: permitir que novos eventos sejam adicionados aos calendários de um Segment de assinantes.
- Atualizar um evento personalizado: permitir que uma atualização seja feita em um evento existente nos calendários dos assinantes.

Para criar um modelo de webhook do Rokt Calendar para usar em futuras Campaigns ou Canvas, navegue até **Templates** > **Webhook Templates** na plataforma Braze.

Se quiser criar uma campanha de webhook única do Rokt Calendar ou usar um modelo existente, selecione **Webhook** na Braze ao criar uma nova campanha.

{% tabs %}
{% tab Send a new event %}
Depois de selecionar o modelo de webhook do Rokt Calendar, você verá o seguinte:
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Request Body**: Raw Text
{% endtab %}
{% tab Update an existing event %}
Depois de selecionar o modelo de webhook do Rokt Calendar, você verá o seguinte:
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Request Body**: Raw Text
{% endtab %}
{% endtabs %}

#### Cabeçalhos e método da solicitação {#request-headers-and-method}

O Rokt Calendar requer um `HTTP Header` para autorização que inclua o nome da sua credencial de Conteúdo conectado do Rokt Calendar. Os itens a seguir já estarão incluídos no modelo como pares de chave-valor, mas na guia **Settings**, você deve substituir `<Rokt-Calendar-API>` pelo nome da credencial encontrado em `Manage Settings > Connected Content > Credential`.

{% raw %}
- **HTTP Method**: POST
- **Request Header**:
  - **Authorization**: Bearer `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação {#request-body}

{% tabs local %}
{% tab Send a new event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab Update an existing event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab Event details %}
Os campos a seguir incluem informações que podem ser personalizadas no nível do evento.

| Campo             | Definição       | Exemplo          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>***Obrigatório** | Um identificador único para o evento a ser adicionado ou atualizado | `Event_00001`
| `eventTitle` <br>***Obrigatório** | O título do evento como apareceria no calendário | Summer Sale 2019
| `eventDescr` | A descrição do evento como apareceria no calendário | The sale is on for three days; click this link `www.mybusiness.com/sale` to see the offers. |
| `eventLocation` | O local do evento como apareceria no calendário. Note que isso é frequentemente usado como uma segunda chamada para ação, complementar ao eventTitle. | Open the event to get 50% off |
| `eventStart` <br>***Obrigatório**  | A data e a hora de início do evento como apareceriam no calendário | `2019-02-21T15:00:00` |
| `eventEnd` <br>***Obrigatório**  | A data e a hora de término do evento como apareceriam no calendário | `2019-02-21T16:00:00` |
| `eventTz` <br>***Obrigatório**  | O fuso horário do evento como apareceria no calendário. Note que a lista de fusos horários aplicáveis pode ser encontrada [aqui](https://roktcalendar-api.readme.io/docs/timezones). | `Eastern Standard Time` |
| `notifyBefore` <br>***Obrigatório**  | O horário do lembrete do evento como apareceria no calendário. Note que isso é expresso em minutos | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Request body" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Para obter uma lista de fusos horários válidos, consulte [https://roktcalendar-api.readme.io/reference/timezones](https://roktcalendar-api.readme.io/reference/timezones).
{% endalert %}

### Etapa 3: pré-visualize sua solicitação {#step-3-preview-your-request}

Pré-visualize a solicitação no painel **prévia** ou navegue até a guia **Test**, onde é possível selecionar um usuário aleatório, um usuário existente ou personalizar o seu próprio para testar o webhook.

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Saved Webhook Templates** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}