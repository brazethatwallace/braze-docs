---
title: Glossário de API ou código
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "Esta é a descrição da Pesquisa Google. Caracteres com mais de 160 são truncados, portanto, seja breve."
page_type: glossary
#Use if applicable

tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: remove noindex and this alert from template

excerpt_separator: ""
---
{% api %}
## 1 Criar modelo de e-mail {#1-create-email-template}
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
Post,Email,Create,Template,REST,API
{% endapitags %}

Use as REST APIs de modelo de e-mail para gerenciar programaticamente os modelos de e-mail que você armazenou nos dashboards da Braze, na página Modelos e mídia. A Braze oferece dois endpoints para criar e atualizar seus modelos de e-mail.

A resposta desse endpoint inclui um campo para `email_template_id`, que pode ser usado para atualizar o modelo em chamadas subsequentes à API.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPO DA SOLICITAÇÃO {#request-body}
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### EXEMPLO DE RESPOSTA {#example-response}
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### DETALHES DOS PARÂMETROS {#parameter-details}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `modified_after`  | Não | String em ISO 8601 | Recupera apenas modelos atualizados no momento ou após o momento determinado. |
| `modified_before`  |  Não | String em ISO 8601 | Recupera apenas modelos atualizados no momento ou antes do momento determinado. |
| `limit` | Não | Número positivo | Número máximo de modelos a serem recuperados; o padrão é 100 se não for fornecido; o valor máximo aceitável é 1000. |
| `offset`  |  Não | Número positivo | Número de modelos a serem ignorados antes de retornar o restante dos modelos que atendem aos critérios de pesquisa. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Detalhes dos parâmetros" }


{% endapi %}
{% api %}
## 2 Listar modelos de e-mail disponíveis {#2-list-available-email-template}
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
Get,Email,Template,List,REST
{% endapitags %}

Use os seguintes endpoints para obter uma lista de modelos disponíveis.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPO DA SOLICITAÇÃO
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}

```

#### EXEMPLO DE RESPOSTA
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}
```


#### DETALHES DOS PARÂMETROS

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `email_template_id`  | Sim | String | O identificador de API do seu modelo de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Detalhes dos parâmetros" }

{% endapi %}


{% api %}
## 3 Envio disparado de Campaigns {#3-campaigns-trigger-send}
{% apimethod post %}campaigns/trigger/send{% endapimethod %}
{% apitags %}Post, Campaigns, Trigger,Send{% endapitags %}

O envio disparado por API permite que você armazene o conteúdo da mensagem dentro do dashboard da Braze e, ao mesmo tempo, determine quando a mensagem será enviada e para quem por meio da sua API.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPO DA SOLICITAÇÃO
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties)
    },
    ...
  ]
}

```

#### EXEMPLO DE RESPOSTA
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (required, string) see Canvas Identifier,
  "context": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "context": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent context)
    },
    ...
  ]
}
```


#### DETALHES DOS PARÂMETROS

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `email_template_id`  | Sim | String | O identificador de API do seu modelo de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Detalhes dos parâmetros" }

{% endapi %}


{% api %}
## 4 Envio disparado de Campaigns {#4-campaigns-trigger-send}
{% apimethod put %}users/track{% endapimethod %}
{% apitags %}PUT, Campaigns, Trigger, Send{% endapitags %}

Esse endpoint pode ser usado para registrar eventos personalizados, atributos de usuário e compras para usuários. Você pode incluir até 75 objetos de Atributos, Eventos e Compras por solicitação. Ou seja, só é possível postar atributos para até 75 usuários por vez, mas na mesma chamada de API também é possível fornecer até 75 eventos e até 75 compras.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPO DA SOLICITAÇÃO
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}

```

#### EXEMPLO DE RESPOSTA
```
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean).
  // Braze User Profile Fields
  "first_name" : "Alex",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

#### DETALHES DOS PARÂMETROS

| Campo de perfil do usuário | Especificação do tipo de dados |
| ---| --- |
| country | (string) Exigimos que os códigos de país sejam transmitidos à Braze no [padrão ISO-3166-1 alfa-2][17]. |
| current_location | (objeto) Com o formato {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (data em que o usuário usou o app pela primeira vez) String no formato ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| date_of_last_session | (data em que o usuário usou o app pela última vez) String no formato ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| dob | (data de nascimento) String no formato "AAAA-MM-DD", por exemplo, 1980-12-21. |
| email | (string) |
| email_subscribe | (string) Os valores disponíveis são "opted_in" (registrado explicitamente para receber mensagens de e-mail), "unsubscribed" (cancelou explicitamente a inscrição para receber mensagens de e-mail) e "subscribed" (nem optou por receber nem por não receber).  |
| external_id | (string) Do identificador exclusivo do usuário. |
| facebook | hash contendo qualquer um dos seguintes itens: `id` (string), `likes` (vetor de strings), `num_friends` (inteiro). |
| first_name | (string) |
| gender | (string) "M", "F", "O" (outro), "N" (não aplicável), "P" (prefere não dizer) ou nil (desconhecido). |
| home_city | (string) |
| image_url | (string) URL da imagem a ser associada ao perfil do usuário. |
| language | (string) Exigimos que o idioma seja passado para a Braze no [padrão ISO-639-1][24]. <br>[Lista de idiomas aceitos](/docs/user_guide/data_and_analytics/user_data_collection/language_codes/)|
| last_name | (string) |
| marked_email_as_spam_at | (string) Data em que o e-mail do usuário foi marcado como spam. Aparece no formato ISO 8601 ou no formato yyyy-MM-dd'T'HH:mm:ss:SSSZ. |
| phone | (string) |
| push_subscribe | (string) Os valores disponíveis são "opted_in" (registrado explicitamente para receber mensagens push), "unsubscribed" (cancelou explicitamente a aceitação de mensagens push) e "subscribed" (nem optou por receber nem por não receber).  |
| push_tokens | Vetor de objetos com `app_id` e `token` string. Como opção, você pode fornecer um `device_id` para o dispositivo ao qual esse token está associado, por exemplo, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Se o `device_id` não for fornecido, um será gerado aleatoriamente. |
| time_zone | (string) Nome do fuso horário do [banco de dados de fuso horário da IANA][26] (por exemplo, "America/New_York" ou "Eastern Time (US & Canada)"). Somente os valores válidos de fuso horário serão definidos. |
| twitter | Hash contendo qualquer um dos seguintes itens: `id` (inteiro), `screen_name` (string, identificador do X (antigo Twitter)), `followers_count` (inteiro), `friends_count` (inteiro), `statuses_count` (inteiro). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhes dos parâmetros" }

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/