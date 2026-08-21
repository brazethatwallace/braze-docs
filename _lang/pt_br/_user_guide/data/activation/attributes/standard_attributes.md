---
nav_title: Atributos padrão
article_title: Atributos padrão
page_order: 0.5
page_type: reference
description: "Este artigo de referência lista os atributos padrão de usuário da Braze (chaves reservadas) e os requisitos de sintaxe de cada um."
---

# Atributos padrão {#standard-attributes}

> Atributos padrão são campos predefinidos que a Braze reconhece em todos os perfis de usuário. Use esta página como referência rápida para o nome do campo, o tipo de dados e o formato esperado de cada atributo padrão.

Atributos padrão (às vezes chamados de *atributos default* ou *chaves reservadas*) são diferentes dos [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), que são exclusivos do seu negócio. Quando você envia dados para a Braze com um dos nomes de campo listados nesta página, a Braze armazena o valor no campo de perfil predefinido em vez de criar um novo atributo personalizado.

Você pode definir atributos padrão por qualquer um destes métodos:

- O [SDK da Braze]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)
- O [objeto de atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object) no [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- [Importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)

{% alert important %}
Os nomes dos atributos padrão diferenciam maiúsculas de minúsculas. Sempre use letras minúsculas (por exemplo, `first_name`, não `First_Name`). Se a grafia ou capitalização não corresponder exatamente, a Braze armazena o valor como um [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).
{% endalert %}

## Identificadores {#identifiers}

Os identificadores informam à Braze qual perfil de usuário deve ser atualizado ou criado. Toda solicitação de API e linha de CSV deve incluir pelo menos um identificador. Para saber mais sobre como escolher o identificador correto, consulte [Resolução de identificadores]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution).

| Campo | Tipo de dados | Formato e notas |
|---|---|---|
| `external_id` | String | Um identificador de usuário exclusivo que você atribui. Depois de definido em um perfil, a Braze o utiliza para reconhecer o usuário em diferentes dispositivos. Não pode ser removido após ser adicionado. |
| `braze_id` | String | Um identificador atribuído pela Braze, criado quando o SDK detecta um dispositivo pela primeira vez. Somente leitura. Não pode ser editado. |
| `user_alias` | Objeto | Um objeto com `alias_name` (string) e `alias_label` (string), usado para identificar usuários sem um `external_id`. Mutuamente exclusivo com `external_id` na mesma solicitação. |
| `email` | String | Pode ser usado como identificador quando `external_id` e `user_alias` estão ausentes. Tem precedência sobre `phone` se ambos forem enviados. |
| `phone` | String | Pode ser usado como identificador quando `external_id`, `user_alias` e `email` estão ausentes. Use o formato [E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format) (por exemplo, `+14155552671`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Campos de perfil {#profile-fields}

Esses campos capturam dados demográficos, de contato e de localidade sobre seus usuários.

| Campo | Tipo de dados | Formato e notas |
|---|---|---|
| `first_name` | String | O nome do usuário (por exemplo, `Jane`). |
| `last_name` | String | O sobrenome do usuário (por exemplo, `Doe`). |
| `email` | String | O endereço de e-mail do usuário (por exemplo, `jane.doe@braze.com`). |
| `phone` | String | O número de telefone do usuário. Use o formato [E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format) (por exemplo, `+14155552671`). |
| `dob` | String | Data de nascimento no formato `YYYY-MM-DD` (por exemplo, `1988-02-14`). Permite o direcionamento por aniversário. |
| `gender` | String | Um dos valores: `M`, `F`, `O` (outro), `N` (não aplicável), `P` (prefere não dizer) ou `null` (desconhecido). |
| `country` | String | Um código de país no formato [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1) (por exemplo, `US`, `GB`). Definir `country` por importação de CSV ou API impede que o SDK o capture automaticamente. |
| `home_city` | String | A cidade do usuário (por exemplo, `London`). |
| `language` | String | Um código de idioma no formato [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (por exemplo, `en`). Consulte a [lista de idiomas aceitos]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes). Definir `language` por importação de CSV ou API impede que o SDK o capture automaticamente. |
| `time_zone` | String | Um nome de fuso horário do [Banco de Dados de Fusos Horários da IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por exemplo, `America/New_York` ou `Eastern Time (US & Canada)`). |
| `current_location` | Object | Um objeto contendo `longitude` e `latitude` (por exemplo, `{"longitude": -73.991443, "latitude": 40.753824}`). |
| `image_url` | String | Uma URL para a imagem de perfil do usuário. Até 1.024 caracteres. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Inscrição e consentimento {#subscription-and-consent}

Esses campos gerenciam como um usuário recebe mensagens em diferentes canais. Atualizá-los não conta para o seu uso de pontos de dados.

| Campo | Tipo de dados | Formato e notas |
|---|---|---|
| `email_subscribe` | String | Um dos seguintes: `opted_in` (registrado explicitamente para receber e-mail), `unsubscribed` (optou explicitamente por não receber e-mail) ou `subscribed` (nem optou por receber nem por não receber). |
| `push_subscribe` | String | Um dos seguintes: `opted_in`, `unsubscribed` ou `subscribed`. Mesmas definições de `email_subscribe`. |
| `subscription_groups` | Array de objetos | Um array em que cada objeto tem um `subscription_group_id` (string) e um `subscription_state` (`subscribed` ou `unsubscribed`). Por exemplo: `[{"subscription_group_id": "abc-123", "subscription_state": "subscribed"}]`. |
| `email_open_tracking_disabled` | Booleano | `true` ou `false`. Defina como `true` para desativar o pixel de rastreamento de abertura de e-mail para este usuário. |
| `email_click_tracking_disabled` | Booleano | `true` ou `false`. Defina como `true` para desativar o rastreamento de cliques em e-mail para este usuário. |
| `marked_email_as_spam_at` | String | Registro de data e hora em que o e-mail do usuário foi marcado como SPAM. Use o formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para mais detalhes sobre a configuração de grupos de inscrições, consulte [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups).

## Sessões e engajamento {#sessions-and-engagement}

Esses campos capturam quando o usuário usou seu app pela primeira ou última vez. O SDK os registra automaticamente; normalmente, você os define apenas por API ou CSV ao migrar de outra plataforma.

| Campo | Tipo de dados | Formato e notas |
|---|---|---|
| `date_of_first_session` | String | A data em que o usuário usou o app pela primeira vez. Use o formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou um dos seguintes: `yyyy-MM-ddTHH:mm:ss:SSSZ`, `yyyy-MM-ddTHH:mm:ss`, `yyyy-MM-dd HH:mm:ss`, `yyyy-MM-dd`, `MM/dd/yyyy` ou `ddd MM dd HH:mm:ss.TZD YYYY`. |
| `date_of_last_session` | String | A data em que o usuário usou o app pela última vez. Aceita os mesmos formatos que `date_of_first_session`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Tokens por push {#push-tokens}

Use esses campos ao migrar tokens por push de outra plataforma. Após integrar o SDK da Braze, os tokens por push são capturados automaticamente. Para orientações sobre migração, consulte [Migração de tokens por push]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens).

| Campo | Tipo de dados | Formato e notas |
|---|---|---|
| `push_tokens` | Array de objetos | Um array em que cada objeto tem um `app_id` (string) e um `token` (string). Opcionalmente, inclua um `device_id` (string). Por exemplo: `[{"app_id": "YOUR_APP_ID", "token": "abcd", "device_id": "optional_device_id"}]`. |
| `push_token_import` | Booleano | Flag de nível superior (não aninhada em `attributes`). Defina como `true` para importar tokens por push legados para usuários anônimos sem um `external_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Perfil social {#social-profile}

Esses campos armazenam dados de integrações com redes sociais.

| Campo | Tipo de dados | Formato e notas |
|---|---|---|
| `facebook` | Objeto | Um objeto contendo qualquer combinação de `id` (string), `likes` (array de strings) ou `num_friends` (inteiro). |
| `twitter` | Objeto | Um objeto contendo qualquer combinação de `id` (inteiro), `screen_name` (string, identificador do X), `followers_count` (inteiro), `friends_count` (inteiro) ou `statuses_count` (inteiro). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Exemplo de API {#api-example}

A solicitação a seguir define atributos padrão em dois usuários por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
    {
      "external_id": "user1",
      "first_name": "Alex",
      "last_name": "Doe",
      "email": "jane.doe@example.com",
      "country": "US",
      "language": "en",
      "time_zone": "America/New_York",
      "dob": "1988-02-14",
      "email_subscribe": "opted_in"
    },
    {
      "external_id": "user2",
      "first_name": "Alex",
      "phone": "+14155552671",
      "current_location": {
        "longitude": -73.991443,
        "latitude": 40.753824
      },
      "subscription_groups": [
        {
          "subscription_group_id": "abc-123",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```

Para ver o contrato completo da API, consulte o [Objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Exemplo de CSV {#csv-example}

O CSV a seguir atualiza atributos padrão para dois usuários. Os cabeçalhos das colunas devem corresponder exatamente aos nomes dos campos neste artigo. Cabeçalhos que não correspondem (por exemplo, `First_name` em vez de `first_name`) são importados como atributos personalizados.

```plaintext
external_id,first_name,last_name,email,country,language,dob,email_subscribe
user1,Jane,Doe,jane.doe@example.com,US,en,1988-02-14,opted_in
user2,Alex,Smith,alex.smith@example.com,GB,en,1992-09-30,subscribed
```

Não é possível definir alguns atributos padrão por meio da importação de CSV. Você deve enviar arrays, tokens por push e objetos aninhados pela API ou pela [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion). Para ver a lista completa de campos compatíveis com CSV e as etapas de importação, consulte [Atributos padrão]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#default-attributes).

## Considerações {#considerations}

Leve em conta estes pontos ao trabalhar com atributos padrão:

- **Os nomes dos campos diferenciam maiúsculas de minúsculas.** Sempre use letras minúsculas. Um cabeçalho ou chave que não corresponda exatamente ao nome de um atributo padrão será tratado como um atributo personalizado.
- **A captura automática do SDK é suprimida quando você define valores por API ou CSV.** Quando você define `country` ou `language` por API ou CSV, a Braze para de capturar automaticamente esses campos do SDK para esse usuário.
- **`null` remove um valor.** Defina um atributo padrão como `null` para removê-lo do perfil. Alguns campos, incluindo `external_id` e `user_alias`, não podem ser removidos depois de definidos.
- **Valores em branco no CSV não sobrescrevem.** Uma célula em branco em uma importação de CSV mantém o valor existente no perfil. Para limpar um valor, use a API.
- **Os fusos horários são UTC por padrão.** Strings de data sem um deslocamento são interpretadas como meia-noite UTC e exibidas no fuso horário do seu espaço de trabalho. Para especificar um fuso horário, adicione um deslocamento UTC (por exemplo, `2024-11-10T18:00:00-05:00`).

## Páginas relacionadas {#related-pages}

- [Objeto de atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object) — Contrato completo da API para o objeto de atributos.
- [Endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) — Endpoint REST para criar e atualizar perfis de usuário.
- [Definir atributos de usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes) — Métodos do SDK para definir atributos padrão e personalizados.
- [Importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) — Faça upload de atributos padrão por meio de um arquivo CSV.
- [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) — Defina atributos exclusivos para o seu negócio.
- [Tipos de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types) — Referência dos tipos de dados compatíveis.