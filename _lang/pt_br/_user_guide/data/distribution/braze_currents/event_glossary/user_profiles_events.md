---
nav_title: Perfis de usuário
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glossário lista as atualizações de perfil de usuário que a Braze pode rastrear e enviar para data warehouses escolhidos usando o Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% alert tip %}
Esses eventos também estão disponíveis como tabelas SQL no [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder), nas [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) e no [Compartilhamento de dados Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Para esquemas de tabelas SQL e detalhes de colunas, consulte a [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Para esquemas de Compartilhamento de dados Snowflake para visualizações de atributos de perfil de usuário, consulte [Atributos de perfil de usuário]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

Entre em contato com seu representante da Braze ou abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) se precisar de acesso a direitos de eventos adicionais. Se você não encontrar o que precisa nesta página, consulte a [Biblioteca de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), a [Biblioteca de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) ou os [exemplos de dados de amostra do Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicação da estrutura de eventos de atualização de perfil de usuário %}

### Estrutura do evento {#event-structure}

Esta análise de comportamento do cliente e eventos de usuário mostra que tipo de informação geralmente está incluída em um evento de atualização de perfil de usuário. Com uma compreensão sólida de seus componentes, seus desenvolvedores e a equipe de estratégia de business intelligence podem usar os dados de eventos recebidos do Currents para criar relatórios e gráficos orientados por dados, além de aproveitar outras métricas de dados valiosas.

{% alert important %}
Os esquemas de armazenamento se aplicam a dados de eventos em arquivo simples enviados para parceiros de armazenamento em data warehouse, como Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage. Algumas combinações de eventos e destinos listadas aqui ainda não estão disponíveis de forma geral. Para informações sobre eventos compatíveis por parceiro, consulte [parceiros disponíveis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) e as páginas de parceiros relacionadas.

O Currents descarta eventos com cargas úteis maiores que 900 KB.
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->


{% api %}
## Eventos de solicitação de exclusão de usuário {#user-delete-request-events}

{% apitags %}
User Delete Request
{% endapitags %}

Quando um usuário é excluído por solicitação do cliente.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.UserDeleteRequest

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.UserDeleteRequest

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de usuário órfão {#user-orphan-events}

{% apitags %}
User Orphan
{% endapitags %}

Quando um usuário se torna órfão, ou seja, o perfil do usuário é mesclado com o perfil de outro usuário.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.UserOrphan

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "orphaned_by_id" : "(required, string) BSON ID of the user whose profile was merged with the orphaned user's profile",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.UserOrphan

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "orphaned_by_id" : "(required, string) BSON ID of the user whose profile was merged with the orphaned user's profile"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de atualização de perfil de usuário {#user-profile-update-events}

{% apitags %}
Profile
{% endapitags %}

Isso representa as atualizações de perfil de um usuário.

{% alert important %}
O evento de atualização de perfil de usuário está em beta. Entre em contato com seu gerente de sucesso do cliente ou gerente de conta para obter acesso.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.profile.Update

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "archived" : "(optional, boolean) When set to True, indicates that this user was archived within Braze",
  "country" : "(optional, string) [PII] Country of the user",
  "custom_attributes" : "(optional, string) Valid JSON string of the updated custom attributes",
  "dob" : "(optional, string) [PII] Date of birth of the user in ISO-8601 format",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "first_name" : "(optional, string) [PII] First name of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "home_city" : "(optional, string) [PII] Home city of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "last_name" : "(optional, string) [PII] Last name of the user",
  "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "time_ms" : "(required, long) Time in milliseconds when the update happened",
  "timezone" : "(optional, string) Time zone of the user",
  "update_source" : "(required, string) The source of this update",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.profile.Update

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "archived" : "(optional, boolean) When set to True, indicates that this user was archived within Braze",
    "country" : "(optional, string) [PII] Country of the user",
    "custom_attributes" : "(optional, string) Valid JSON string of the updated custom attributes",
    "dob" : "(optional, string) [PII] Date of birth of the user in ISO-8601 format",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "first_name" : "(optional, string) [PII] First name of the user",
    "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
    "home_city" : "(optional, string) [PII] Home city of the user",
    "language" : "(optional, string) [PII] Language of the user",
    "last_name" : "(optional, string) [PII] Last name of the user",
    "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format",
    "time_ms" : "(required, long) Time in milliseconds when the update happened",
    "update_source" : "(required, string) The source of this update"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}
{% endtabs %}

{% endapi %}