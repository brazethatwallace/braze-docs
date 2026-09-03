---
nav_title: "Objeto de atribuições do usuário"
article_title: "Objeto de atribuições do usuário"
page_order: 11
page_type: reference
description: "Este artigo de referência explica os diferentes componentes do objeto de atribuições do usuário."
---

# Objeto de atribuições do usuário {#user-attributes-object}

> Uma solicitação de API com quaisquer campos no objeto de atributos cria ou atualiza um atributo desse nome com o valor dado no perfil de usuário especificado.

Use os nomes de campo do perfil de usuário da Braze (listados a seguir ou qualquer outro listado na seção de [campos de perfil de usuário da Braze](#braze-user-profile-fields)) para atualizar esses valores especiais no perfil de usuário no dashboard ou adicionar seus próprios dados de atributo personalizado ao usuário.

## Corpo do objeto {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
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
  // Array of objects custom attribute
  "my_array_of_objects_attribute": [{"key": "value"}, {"key": "value"}],
  // Adding to an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$add": [{"key": "value"}] },
  // Removing from an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$remove": [{"$identifier_key": "key", "$identifier_value": "value"}] },
}
```

- [ID externo do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [Aliases de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

{% alert note %}
Para atributos personalizados de array comum, use `add` e `remove` (sem `$`).

Para arrays de objetos (atributos personalizados aninhados), use `$add`, `$remove` e `$update` nas cargas úteis de requisição `/users/track`. Esses operadores aplicam alterações no nível do objeto por meio da correspondência de identificadores (`$identifier_key` e `$identifier_value`) e suportam atualizações in-place com `$new_object`.

Use esse formato quando precisar adicionar, remover ou atualizar objetos dentro de um array existente, preservando o restante do estado do array. Para exemplos completos de requisição, consulte [Exemplo de API de array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) e [Exemplo de SDK de array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example).
{% endalert %}

Para remover um atributo de perfil, defina-o como `null`. Alguns campos, como `external_id` e `user_alias`, não podem ser removidos após serem adicionados a um perfil de usuário.

### Resolução de identificadores {#identifier-resolution}

A menos que você esteja realizando uma [importação anônima de token por push](#push-token-import), cada objeto de atributos de usuário deve incluir pelo menos um identificador: `external_id`, `user_alias`, `braze_id`, `email` ou `phone`. Sempre que possível, inclua apenas um identificador por objeto para evitar ambiguidade sobre qual perfil de usuário está sendo atualizado ou criado.

Tenha em mente o seguinte ao usar identificadores:

- **`external_id` e `user_alias` são mutuamente exclusivos.** Incluir ambos no mesmo objeto de atributos de usuário retorna um erro. Para adicionar um alias a um usuário que já possui um `external_id`, use o [endpoint `/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias).
- **`email` tem precedência sobre `phone`.** Se `email` e `phone` forem incluídos no mesmo objeto, a Braze usa `email` como identificador. Isso significa que os atributos são aplicados ao perfil de usuário associado a esse endereço de e-mail, mesmo que o número de telefone pertença a um perfil diferente.

{% alert important %}
Para evitar comportamentos inesperados, use um único identificador por objeto de atributos de usuário. Fornecer vários identificadores que fazem referência a perfis de usuário diferentes pode levar a atributos sendo aplicados ao perfil errado.
{% endalert %}

#### Atualizar apenas perfis existentes {#update-existing-profiles-only}

Se você deseja atualizar apenas perfis de usuário já existentes na Braze, passe a chave `_update_existing_only` com o valor `true` no corpo da sua requisição. Se esse valor for omitido, a Braze cria um novo perfil de usuário caso o `external_id` ainda não exista.

{% alert note %}
Se você estiver criando um perfil de usuário somente com alias por meio do endpoint `/users/track`, deve definir `_update_existing_only` como `false`. Se você omitir esse valor, a Braze não cria o perfil somente com alias.
{% endalert %}

#### Importação de token por push {#push-token-import}

Antes de importar tokens por push para a Braze, verifique se isso é realmente necessário. Quando os SDKs da Braze estão implementados, eles gerenciam os tokens por push automaticamente, sem necessidade de fazer upload pela API.

Se você constatar que precisa fazer upload pela API, os tokens podem ser enviados para usuários identificados ou usuários anônimos. Isso significa que um `external_id` precisa estar presente ou os usuários anônimos devem ter o sinalizador `push_token_import` definido como `true`.

{% alert note %}
Ao importar tokens por push de outros sistemas, nem sempre um `external_id` está disponível. Para manter a comunicação com esses usuários durante sua transição para a Braze, você pode importar os tokens legados para usuários anônimos sem fornecer `external_id`, especificando `push_token_import` como `true`.
{% endalert %}

Ao especificar `push_token_import` como `true`:

* `external_id` e `braze_id` **não** devem ser especificados
* O objeto de atributo **deve** conter um token por push
* Se o token já existir na Braze, a requisição é ignorada; caso contrário, a Braze cria um perfil de usuário temporário e anônimo para cada token, permitindo que você continue enviando mensagens a esses indivíduos

Após a importação, à medida que cada usuário lança a versão do seu app habilitada para a Braze, a Braze move automaticamente o token por push importado para o perfil de usuário da Braze correspondente e limpa o perfil temporário.

A Braze verifica uma vez por mês se há perfis anônimos com o sinalizador `push_token_import` que não possuem um token por push. Se o perfil anônimo não tiver mais um token por push, a Braze exclui o perfil. No entanto, se o perfil anônimo ainda tiver um token por push, indicando que o usuário real ainda não fez login no dispositivo com esse token, a Braze não faz nada.

Para saber mais, consulte [Migração de tokens por push](#migrate-push-tokens).

#### Tipos de dados de atributos personalizados {#custom-attribute-data-types}

Os seguintes tipos de dados podem ser armazenados como um atributo personalizado:

| Tipo de dado | Notas |
| --- | --- |
| Arrays | Arrays de atributos personalizados são suportados. Ao adicionar um elemento, ele é anexado ao final do array. Se o elemento já existir, ele é movido da posição atual para o final.<br><br>Somente valores únicos são armazenados. Por exemplo, importar `['hotdog','hotdog','hotdog','pizza']` resulta em `['hotdog', 'pizza']`.<br><br>Você pode definir um array diretamente (por exemplo, `"my_array_custom_attribute":[ "Value1", "Value2" ]`), adicionar a um array existente com `"my_array_custom_attribute" : { "add" : ["Value3"] }` ou remover valores com `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`.<br><br>O número padrão e máximo de elementos em um array é 500. Você pode atualizar o número máximo de arrays no dashboard da Braze, em **Data Settings** > **Custom Attributes**. Para saber mais, consulte [Arrays]({{site.baseurl}}/developer_guide/analytics#arrays). |
| Array de objetos | Use um array de objetos para definir uma lista de objetos em que cada objeto contém um conjunto de atributos. Use esse tipo para armazenar vários conjuntos de dados relacionados para um usuário, como estadias em hotéis, histórico de compras ou preferências. <br><br>Por exemplo, defina um atributo personalizado chamado `hotel_stays` em um perfil de usuário como um array em que cada objeto representa uma estadia separada, com atributos como `hotel_name`, `check_in_date` e `nights_stayed`.<br><br>Arrays de objetos não têm limite no número de itens, mas possuem um tamanho máximo de 100&nbsp;KB. Se uma atualização fizer o array exceder esse limite, a Braze descarta a atualização e o atributo permanece inalterado.<br><br>Para cargas úteis de `/users/track` e SDK, use `$add`, `$remove` e `$update` para operações de array de objetos. Use `add` e `remove` (sem `$`) para atributos personalizados de array comum que contêm valores escalares. Para mais detalhes, consulte [Exemplo de API de array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example), [Exemplo de SDK de array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example) e [Exemplo de array de objetos](#array-of-objects-example). |
| Booleanos | `true` ou `false` |
| Datas | Armazene datas no formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (recomendado) ou em qualquer um destes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Observe que "T" é um designador de horário, não um espaço reservado, e não deve ser alterado ou removido. <br><br>Valores de data que não correspondem a nenhum dos formatos listados são armazenados como strings no perfil de usuário em vez do tipo de dado Time. Isso significa que filtros de segmentação baseados em tempo (como "antes de", "depois de" ou "nos últimos X dias") não funcionam para esses atributos. Por exemplo, `Mar 26 2026 06:12 PM +00:00` é armazenado como string porque não corresponde a um formato suportado. Para evitar isso, use o formato ISO 8601 (como `2026-03-26T18:12:00Z`). <br><br>Atributos de horário sem fuso horário são padronizados para meia-noite UTC (e são formatados no dashboard como o equivalente à meia-noite UTC no fuso horário da empresa). Para especificar um fuso horário, anexe um deslocamento UTC ao timestamp (por exemplo, `2024-11-10T18:00:00-05:00` para EST). Se o deslocamento de fuso horário estiver ausente ou formatado incorretamente, o valor é padronizado para UTC. <br><br>Os horários são exibidos no dashboard no fuso horário da sua empresa. Por exemplo, `2024-11-10T18:00:00-05:00` (18:00 EST) seria exibido como o horário equivalente no fuso horário configurado da sua empresa. <br><br>Eventos com timestamps no futuro são padronizados para o horário atual. <br><br>Para atributos personalizados comuns, se o ano for menor que 0 ou maior que 3000, a Braze armazena o valor como uma string no perfil de usuário. |
| Floats | Atributos personalizados do tipo float são números positivos ou negativos com ponto decimal. Por exemplo, você pode usar floats para armazenar saldos de conta ou avaliações de usuários para produtos ou serviços. |
| Inteiros | Você pode incrementar atributos personalizados do tipo inteiro atribuindo um objeto com o campo "inc" e o valor a ser adicionado. <br><br>Exemplo: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Atributos personalizados aninhados | Atributos personalizados aninhados definem um conjunto de atributos como propriedade de outro atributo. Ao definir um objeto de atributo personalizado, você adiciona um conjunto de atributos a esse objeto. Para saber mais, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support). |
| Strings | Atributos personalizados do tipo string são sequências de caracteres usadas para armazenar dados de texto. Por exemplo, você pode usar strings para armazenar nomes, endereços de e-mail ou preferências. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de dados de atributos personalizados" }

{% alert tip %}
Para orientações sobre quando usar um evento personalizado versus um atributo personalizado, consulte [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) e [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).
{% endalert %}

##### Exemplo de array de objetos {#array-of-objects-example}

Esse array de objetos permite criar Segments com base em critérios específicos dentro das estadias, e personalizar suas mensagens usando os dados de cada estadia com modelos Liquid.

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

Para exemplos de array de objetos que usam `$add`, `$remove` e `$update`, consulte [Exemplo de API de array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) e [Exemplo de SDK de array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example).

#### Campos do perfil de usuário da Braze {#braze-user-profile-fields}

{% alert important %}
Os seguintes campos do perfil de usuário são sensíveis a maiúsculas e minúsculas, portanto certifique-se de referenciá-los em minúsculas.
{% endalert %}

{% alert tip %}
Para uma referência voltada ao cliente sobre atributos padrão, organizada por categoria e com orientações para SDK, API, CSV e Cloud Data Ingestion, consulte [Atributos padrão]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes).
{% endalert %}

| Campo do perfil de usuário | Especificação do tipo de dado |
| ---| --- |
| alias_name | (string) |
| alias_label | (string) |
| braze_id | (string, opcional) Quando um perfil de usuário é reconhecido pelo SDK, um perfil de usuário anônimo é criado com um `braze_id` associado. O `braze_id` é atribuído automaticamente pela Braze, não pode ser editado e é específico do dispositivo. |
| country | (string) Exigimos que os códigos de país sejam passados para a Braze no padrão [ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1). Nossa API faz o melhor esforço para mapear países recebidos em diferentes formatos. Por exemplo, "Australia" pode ser mapeado para "AU". No entanto, se a entrada não corresponder a um determinado padrão [ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1), o valor do país é definido como `NULL`. <br><br>Definir `country` em um usuário por importação CSV ou API impede que a Braze capture automaticamente essa informação por meio do SDK. |
| current_location | (objeto) No formato {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (data em que o usuário usou o app pela primeira vez) String no formato ISO 8601 ou em qualquer um dos seguintes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (data em que o usuário usou o app pela última vez) String no formato ISO 8601 ou em qualquer um dos seguintes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (data de nascimento) String no formato "YYYY-MM-DD", por exemplo, 1980-12-21. |
| email | (string) |
| email_subscribe | (string) Os valores disponíveis são "opted_in" (registrado explicitamente para receber mensagens de e-mail), "unsubscribed" (optou explicitamente por não receber mensagens de e-mail) e "subscribed" (nem optou por receber nem por não receber).  |
| email_open_tracking_disabled |(boolean) `true` ou `false` aceitos. Defina como `true` para desativar a adição do pixel de rastreamento de abertura em todos os futuros e-mails enviados a este usuário.|
| email_click_tracking_disabled |(boolean) `true` ou `false` aceitos. Defina como `true` para desativar o rastreamento de cliques em todos os links dentro de um futuro e-mail enviado a este usuário.|
| external_id | (string) Um identificador único para um perfil de usuário. Após a atribuição de um `external_id`, a Braze identifica o perfil de usuário em todos os dispositivos do usuário. Na primeira instância de atribuição de um external_id a um perfil de usuário desconhecido, a Braze migra todos os dados existentes do perfil de usuário para o novo perfil. |
| facebook | hash contendo qualquer um de `id` (string), `likes` (array de strings), `num_friends` (inteiro). |
| first_name | (string) |
| gender | (string) "M", "F", "O" (outro), "N" (não aplicável), "P" (prefiro não dizer) ou null (desconhecido). |
| home_city | (string) |
| language | (string) Exigimos que o idioma seja passado para a Braze no padrão [ISO-639-1](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Para idiomas suportados, consulte nossa [lista de idiomas aceitos]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes).<br><br>Definir `language` em um usuário por importação CSV ou API impede que a Braze capture automaticamente essa informação por meio do SDK. |
| last_name | (string) |
| marked_email_as_spam_at | (string) Data em que o e-mail do usuário foi marcado como SPAM. Aparece no formato ISO 8601 ou em qualquer um dos seguintes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (string) Recomendamos fornecer números de telefone no formato [E.164](https://en.wikipedia.org/wiki/E.164). Para mais detalhes, consulte [Números de telefone dos usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format).|
| push_subscribe | (string) Os valores disponíveis são "opted_in" (registrado explicitamente para receber mensagens push), "unsubscribed" (optou explicitamente por não receber mensagens push) e "subscribed" (nem optou por receber nem por não receber).  |
| push_tokens | Array de objetos com `app_id` e string `token`. Opcionalmente, você pode fornecer um `device_id` para o dispositivo ao qual esse token está associado, por exemplo, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Se um `device_id` não for fornecido, um será gerado aleatoriamente. |
| subscription_groups| Array de objetos com `subscription_group_id` e string `subscription_state`, por exemplo, `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Os valores disponíveis para `subscription_state` são "subscribed" e "unsubscribed".|
| time_zone | (string) Nome do fuso horário do [Banco de dados de fusos horários IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por exemplo, "America/New_York" ou "Eastern Time (US & Canada)"). Somente valores de fuso horário válidos são definidos. |
| twitter | Hash contendo qualquer um de `id` (inteiro), `screen_name` (string, identificador do X (antigo Twitter)), `followers_count` (inteiro), `friends_count` (inteiro), `statuses_count` (inteiro). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos do perfil de usuário da Braze" }

Valores de idioma definidos explicitamente por meio desta API têm precedência sobre as informações de localidade que a Braze recebe automaticamente do dispositivo.

#### Exemplo de requisição de atributo de usuário {#user-attribute-example-request}

Este exemplo contém quatro objetos de atributos de usuário, de um total de 75 objetos de atributo permitidos por chamada de API.

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Alex",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Lee",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Yuri",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

## Migrar tokens por push {#migrate-push-tokens}

Se você já enviava notificações por push antes de integrar a Braze, seja por conta própria ou por meio de outro provedor, a migração de tokens por push permite que você continue enviando notificações por push para seus usuários com tokens por push registrados.

### Migração automática pelo SDK {#automatic-migration-through-sdk}

Depois que você [integrar o SDK da Braze]({{site.baseurl}}/developer_guide/sdk_integration), os tokens por push dos seus usuários que aceitaram receber notificações são migrados automaticamente na próxima vez que eles abrirem o app. Até lá, não é possível enviar notificações por push para esses usuários pela Braze.

Como alternativa, você pode [migrar seus tokens por push manualmente](#manual-migration-through-api), permitindo reengajar seus usuários mais rapidamente.

#### Considerações sobre tokens web {#web-token-considerations}

Devido à natureza dos tokens por push para web, leve em consideração o seguinte ao implementar push para web:

|Consideração|Detalhes|
|----------------------|------------|
| **Service workers**  | Por padrão, o SDK para web procura um service worker em `./service-worker`, a menos que outra opção seja especificada, como `manageServiceWorkerExternally` ou `serviceWorkerLocation`. Se o service worker não estiver configurado corretamente, os tokens por push dos seus usuários poderão expirar. |
| **Tokens expirados**   | Se um usuário não iniciar uma sessão web em 60 dias, o token por push dele expira. Como a Braze não consegue migrar tokens por push expirados, você deve enviar um [push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) para reengajá-los. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Considerações sobre tokens web" }

### Migração manual pela API {#manual-migration-through-api}

A migração manual de tokens por push é o processo de importar essas chaves criadas anteriormente para a plataforma da Braze por meio da API.

Migre programaticamente tokens iOS (APNs) e Android (FCM) para a sua plataforma usando o [endpoint `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). É possível migrar tanto usuários identificados (usuários com um ID externo associado) quanto usuários anônimos (usuários sem um ID externo).

Especifique o `app_id` do seu app durante a migração de tokens por push para associar o token por push correto ao app correspondente. Cada app (iOS, Android, etc.) tem seu próprio `app_id`, que pode ser encontrado na seção **Identification** da página [API Keys]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Use o `app_id` da plataforma correta.

{% alert important %}
Não é possível migrar tokens por push para web pela API. Isso ocorre porque os tokens por push para web não seguem o mesmo esquema das outras plataformas.

<br>Se você estiver tentando migrar tokens por push para web de forma programática, poderá ver um erro como o seguinte: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
Como alternativa à migração pela API, recomendamos que você integre o SDK e permita que sua base de tokens se repopule naturalmente.
{% endalert %}

{% tabs local %}
{% tab ID externo presente %}
Para usuários identificados, defina o sinalizador `push_token_import` como `false` (ou omita o parâmetro) e especifique os valores `external_id`, `app_id` e `token` no objeto `attributes` do usuário.

Por exemplo:

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab ID externo ausente %}
Ao importar tokens por push de outros sistemas, nem sempre um `external_id` está disponível. Nesse caso, defina o sinalizador `push_token_import` como `true` e especifique os valores `app_id` e `token`. A Braze cria um perfil de usuário temporário e anônimo para cada token, permitindo que você continue enviando mensagens para esses indivíduos. Se o token já existir na Braze, a solicitação é ignorada.

Por exemplo:

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
    {
      "push_token_import" : true,
      "email": "braze.test1@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },

    {
      "push_token_import" : true,
      "email": "braze.test2@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    }
  ]
}'
```

Após a importação, quando o usuário anônimo iniciar a versão do app com a Braze integrada, a Braze automaticamente move o token por push importado para o perfil de usuário na Braze e limpa o perfil temporário.

A Braze verifica uma vez por mês se há algum perfil anônimo com o sinalizador `push_token_import` que não possua um token por push. Se o perfil anônimo não tiver mais um token por push, a Braze exclui o perfil. No entanto, se o perfil anônimo ainda tiver um token por push, indicando que o usuário real ainda não fez login no dispositivo com esse token por push, a Braze não realiza nenhuma ação.
{% endtab %}
{% endtabs %}

### Importar tokens por push do iOS {#import-ios-push-tokens}

Ao migrar tokens por push do iOS com `/users/track`, o campo `gateway` não é definido no token por push. A Braze assume que os tokens importados pela API são tokens por push válidos em primeiro plano, mas não consegue determinar a qual ambiente APNs o token pertence.

Sem o campo gateway, a Braze usa a configuração de ambiente de fallback do seu app ao enviar notificações por push. Isso pode causar erros `BadDeviceToken` se o ambiente real do token for diferente do fallback configurado. Por exemplo, um token de desenvolvimento enviado pelo gateway de produção falhará.

Para evitar problemas de entrega:

- Verifique se a configuração de ambiente do seu app no dashboard da Braze corresponde aos tokens que você está importando.
- Para apps em produção, importe apenas tokens de produção.
- Para ambientes de teste, confirme que tanto a configuração do app quanto os tokens importados utilizam o ambiente de desenvolvimento.

{% alert note %}
Os tokens registrados pelo SDK da Braze incluem o campo gateway automaticamente, pois o SDK detecta o ambiente a partir dos entitlements do seu app.
{% endalert %}

### Importar tokens por push do Android {#import-android-push-tokens}

{% alert important %}
A consideração a seguir se aplica apenas a apps Android. Apps iOS não exigem essas etapas, pois essa plataforma possui apenas um framework para exibir push, e as notificações por push são renderizadas imediatamente desde que a Braze tenha os tokens por push e certificados necessários.
{% endalert %}

Se você precisar enviar notificações por push para Android aos seus usuários antes que a integração do SDK da Braze esteja concluída, use pares de chave-valor para validar as notificações por push.

Você deve ter um receptor para gerenciar e exibir as cargas úteis de push. Para notificar o receptor sobre a carga útil de push, adicione os pares de chave-valor necessários à Campaign de push. Os valores desses pares dependem do parceiro de push específico que você utilizava antes da Braze.

{% alert note %}
Para alguns provedores de notificação por push, a Braze precisa achatar os pares de chave-valor para que possam ser interpretados corretamente. Para achatar pares de chave-valor de um app Android específico, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Como encontro usuários tratados como spam ou bloqueados para envio de mensagens? {#how-do-i-find-users-treated-as-spam-or-blocked-from-messaging}

A Braze não disponibiliza uma lista dedicada de spam no dashboard. A Braze bloqueia perfis de usuários individuais ("dummy users") que possuem mais de cinco milhões de sessões, mais de 20.000 nomes distintos de eventos personalizados ou mais de 20.000 nomes distintos de produtos em compras, e interrompe a ingestão de todos os dados de entrada para aquele perfil, tanto dos SDKs quanto da REST API. Se um identificador for bloqueado, [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) poderá retornar o erro `"provided external_id is blacklisted and disallowed"`. Esse texto é reproduzido exatamente como aparece na resposta da API. Para encontrar perfis bloqueados por excesso de sessões, crie um [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) com o filtro **Session Count** definido como **more than 5,000,000**, exporte o Segment como CSV e verifique os campos do perfil em **Engajamento** > **Pesquisar usuários** ou com o endpoint [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier). Não existe um filtro equivalente para nomes distintos de eventos personalizados ou nomes de produtos. Nesse caso, entre em contato com o gerente de conta da Braze para identificar os perfis bloqueados por esses motivos. Para saber mais, consulte [Bloqueio de spam]({{site.baseurl}}/user_archival).