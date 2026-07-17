---
nav_title: Comportamento do cliente e eventos de usuário
article_title: Comportamento do cliente e eventos de usuário
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glossário lista os vários eventos de comportamento do cliente e do usuário que a Braze pode rastrear e enviar para os data warehouses escolhidos usando Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details Escopo do esquema e recursos relacionados %}

Os esquemas de armazenamento se aplicam aos dados de eventos de arquivo simples que enviamos aos parceiros de armazenamento de data warehouse (Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage). Algumas combinações de eventos e destinos listadas aqui ainda não estão disponíveis para todos. Para saber quais eventos são compatíveis com os vários parceiros, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) e verifique suas respectivas páginas.

{% alert tip %}
Esses eventos também estão disponíveis como tabelas SQL no [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder), nas [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) e no [Compartilhamento de dados Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Para esquemas de tabelas SQL e detalhes das colunas, consulte a [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).
{% endalert %}

Fale com seu representante da Braze ou abra um [ticket de suporte]({{site.baseurl}}/braze_support) se precisar de acesso a direitos de eventos adicionais. Se não encontrar o que precisa nesta página, consulte nossa [Biblioteca de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) ou nossos [exemplos de dados de amostra do Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explicação da estrutura de eventos de comportamento do cliente e do usuário e valores de plataforma %}

## Estrutura do evento {#event-structure}

Esse detalhamento do comportamento do cliente e dos eventos do usuário mostra que tipo de informação é geralmente incluído em um evento de comportamento do cliente ou do usuário. Com uma boa compreensão de seus componentes, seus desenvolvedores e a equipe de estratégia de business intelligence podem usar os dados de eventos do Currents recebidos para criar relatórios e gráficos orientados por dados e aproveitar outras métricas de dados valiosas.

![Análise de um evento de usuário mostrando um evento de compra com as propriedades listadas agrupadas por propriedades específicas do usuário, propriedades específicas de comportamento e propriedades específicas do dispositivo]({% image_buster /assets/img/customer_engagement_event.png %})

O comportamento do cliente e os eventos do usuário são compostos por propriedades **específicas do usuário**, propriedades **específicas do comportamento** e propriedades **específicas do dispositivo**.

### Valores da plataforma {#platform-values}

Certos eventos retornam um valor `platform` que especifica a plataforma do dispositivo do usuário.
<br>A tabela a seguir detalha os possíveis valores retornados:

| Dispositivo do usuário | Valor da plataforma |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Valores da plataforma" }

{% enddetails %}

{% details Considerações sobre eventos de comportamento do cliente e do usuário %}

- O Currents descarta eventos com cargas úteis excessivamente grandes, superiores a 900&nbsp;KB.
- Muitos dos eventos neste glossário são iniciados pelo SDK. Alguns eventos, como `token_state_change`, podem ser iniciados pelo SDK ou pelo backend (por exemplo, em resposta a um bounce de push). Os campos `sdk_version`, `gender`, `language` e `country` são definidos apenas para eventos iniciados pelo SDK; para eventos iniciados pelo backend, ou quando essas informações não estão disponíveis ou não foram definidas para o usuário, esses campos podem ser `null`.

{% enddetails %}

</div>

<!--overview-end-->

{% api %}
## Eventos de atualização de número de bucket aleatório {#random-bucket-number-update-events}

{% apitags %}
Random Bucket Number
{% endapitags %}

Esse evento de usuário ocorre sempre que um novo usuário é criado no espaço de trabalho. Durante esse evento, cada novo usuário recebe um número de bucket aleatório que você pode usar para criar segmentos de usuários aleatórios uniformemente distribuídos. Use isso para agrupar uma faixa de valores de número de bucket aleatório e comparar o desempenho entre suas campanhas e variantes de campanha.

{% alert important %}
Este evento do Currents está disponível apenas para clientes que adquiriram um "conector de todos os eventos" e está disponível apenas para conectores de eventos de armazenamento (como Amazon S3, Microsoft Azure e Google Cloud Storage).
<br><br>Para ativar esse evento e programar o backfill dos números de bucket aleatórios dos usuários existentes no seu espaço de trabalho, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.RandomBucketNumberUpdate

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "prev_random_bucket_number" : "(optional, int) Previous random bucket number",
  "random_bucket_number" : "(required, int) New random bucket number",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos personalizados {#custom-events}

{% apitags %}
Custom Events
{% endapitags %}

Esse evento ocorre quando um evento personalizado específico é disparado. Use isso para rastrear quando os usuários realizam eventos personalizados no seu aplicativo.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.CustomEvent

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "name" : "(required, string) Name of the custom event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.behaviors.CustomEvent

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "name" : "(required, string) Name of the custom event",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// users.behaviors.CustomEvent

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "name" : "(required, string) Name of the custom event"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

### Detalhes da propriedade {#property-details}

- Para eventos personalizados, a carga útil também será preenchida com quaisquer [propriedades de evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) associadas ao evento.
- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de anúncio do Google Android por meio dos SDKs nativos. Saiba mais aqui: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_google-advertising-id).
- Se você estiver usando Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), entre em contato com seu gerente de sucesso do cliente ou gerente de conta para ativar o feature flipper para enviar `ad_id`.

{% endapi %}

{% api %}
## Eventos de atribuição de instalação {#install-attribution-events}

{% apitags %}
Attribution
{% endapitags %}

Esse evento ocorre quando a instalação de um app é atribuída a uma fonte. Use isso para rastrear de onde estão vindo as instalações do seu app.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.InstallAttribution

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "source" : "(required, string) The source of the attribution",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "source" : "(optional, string) The source of the attribution"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.behaviors.InstallAttribution

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "source" : "(optional, string) The source of the attribution"
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

{% tab Mixpanel %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "source" : "(optional, string) The source of the attribution",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "source" : "(required, string) The source of the attribution"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de localização {#location-events}

{% apitags %}
Locations
{% endapitags %}

Esse evento é disparado quando um usuário visita um local especificado. Use isso para rastrear os usuários que disparam eventos de localização no seu app.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.Location

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
  "altitude" : "(optional, float) [PII] Altitude of recorded location",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "latitude" : "(required, float) [PII] Latitude of recorded location",
  "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
  "longitude" : "(required, float) [PII] Longitude of recorded location",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Location (users.behaviors.Location)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.behaviors.Location

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
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

{% tab Mixpanel %}
```json
// Location (users.behaviors.Location)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Location (users.behaviors.Location)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

### Detalhes da propriedade

- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de anúncio do Google Android por meio dos SDKs nativos. Saiba mais aqui: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_google-advertising-id).
- Se você estiver usando Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), entre em contato com seu gerente de sucesso do cliente ou gerente de conta para ativar o feature flipper para enviar `ad_id`.

{% endapi %}

{% api %}
## Eventos de compra {#purchase-events}

{% apitags %}
Purchases
{% endapitags %}

Esse evento ocorre quando um usuário faz uma compra. Use esses dados para rastrear quando os usuários compram algo no aplicativo.

{% alert tip %}
As compras são eventos personalizados especiais e vêm com uma string codificada em JSON de propriedades de eventos personalizados, da mesma forma que os eventos personalizados.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.Purchase

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "currency" : "(required, string) Currency of the purchase",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "price" : "(required, float) Price of the purchase",
  "product_id" : "(required, string) ID of the product purchased",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Purchase (users.behaviors.Purchase)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "price" : "(required, float) Price of the purchase",
  "productId" : "(required, string) ID of the product purchased",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.behaviors.Purchase

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased"
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

{% tab Mixpanel %}
```json
// Purchase (users.behaviors.Purchase)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Purchased (users.behaviors.Purchase)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

### Detalhes da propriedade

- Para eventos de compra, a carga útil também será preenchida com quaisquer [propriedades de evento de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#purchase-properties) associadas ao evento.
- Para `ad_id`, `ad_id_type` e `ad_tracking_enabled`, você precisa coletar explicitamente o IDFA do iOS e o ID de anúncio do Google Android por meio dos SDKs nativos. Saiba mais aqui: [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_google-advertising-id).
- Se você estiver usando Kafka para ingerir dados do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), entre em contato com seu gerente de sucesso do cliente ou gerente de conta para ativar o feature flipper para enviar `ad_id`.

{% endapi %}

{% api %}
## Eventos de primeira sessão {#first-session-events}

{% apitags %}
Sessions
{% endapitags %}

Esse evento ocorre quando um usuário inicia a primeira sessão no seu aplicativo. Use esses dados para rastrear quando os usuários iniciam sessões.

{% alert tip %}
Quando um usuário inicia sua primeira sessão, são disparados os eventos `FirstSession` e `SessionStart`.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.app.FirstSession

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "country" : "(optional, string) [DEPRECATED]",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [DEPRECATED]",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [DEPRECATED]",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "sdk_version" : "(optional, string) [DEPRECATED]",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.behaviors.app.FirstSession

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de fim de sessão {#session-end-events}

{% apitags %}
Sessions
{% endapitags %}

Esse evento ocorre quando um usuário sai do aplicativo, encerrando a sessão atual. Use esses dados para rastrear quando as sessões terminam e, junto com o evento de início de sessão correspondente, calcular a duração do tempo em uma sessão.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.app.SessionEnd

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "duration" : "(optional, float) Duration of the session in seconds",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "duration" : "(optional, float) Duration of the session in seconds",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.behaviors.app.SessionEnd

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "duration" : "(optional, float) Duration of the session in seconds",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
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

{% tab Mixpanel %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "duration" : "(optional, float) Duration of the session in seconds",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Session Ended (users.behaviors.app.SessionEnd)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "duration" : "(optional, float) Duration of the session in seconds",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de início de sessão {#session-start-events}

{% apitags %}
Sessions
{% endapitags %}

Esse evento ocorre quando um usuário inicia uma sessão. Use esses dados para rastrear quando os usuários iniciam sessões.

{% alert tip %}
Quando um usuário inicia sua primeira sessão, são disparados os eventos `FirstSession` e `SessionStart`.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.app.SessionStart

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Session Start (users.behaviors.app.SessionStart)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.behaviors.app.SessionStart

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
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

{% tab Mixpanel %}
```json
// Session Start (users.behaviors.app.SessionStart)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Session Started (users.behaviors.app.SessionStart)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de mudança de token Push To Start de Live Activity {#live-activity-push-to-start-token-change-events}

{% apitags %}
Live Activity, Push To Start Token
{% endapitags %}

Este evento ocorre quando a Braze sincroniza o token Push To Start de Live Activity com o usuário.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.liveactivity.PushToStartTokenChange

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.behaviors.liveactivity.PushToStartTokenChange

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
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

{% tab Mixpanel %}
```json
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Push To Start Token Changed (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

### Detalhes da propriedade

- A Braze emite um evento "update" com `push_token_state_change_type` definido como `"update"` quando um usuário anônimo é identificado no mesmo perfil e os tokens Push To Start de Live Activity do iOS existentes permanecem nesse perfil. Nesse caso, `user_id` não muda, e `external_user_id` é definido como o ID externo do usuário identificado. Isso inclui a identificação por meio do endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) e do SDK `changeUser` quando ele atribui um ID externo ao perfil anônimo no dispositivo.

{% endapi %}

{% api %}
## Eventos de mudança de token de atualização de Live Activity {#live-activity-update-token-change-events}

{% apitags %}
Live Activity, Update Token
{% endapitags %}

Este evento ocorre quando a Braze sincroniza o token de atualização de Live Activity com o usuário.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.liveactivity.UpdateTokenChange

{
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.behaviors.liveactivity.UpdateTokenChange

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
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

{% tab Mixpanel %}
```json
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Update Token Changed (users.behaviors.liveactivity.UpdateTokenChange)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eventos de mudança de estado do token de notificação por push {#push-notification-token-state-change-events}

{% apitags %}
Push, Token State Change
{% endapitags %}

Este evento ocorre quando um token por push é inserido, atualizado ou removido. Use isso para rastrear os estados dos tokens por push.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.pushnotification.TokenStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "platform" : "(optional, string) Platform of the device",
  "push_token" : "(optional, string) Push token of the event",
  "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
  "push_token_device_id" : "(optional, string) Device id of the push token",
  "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
  "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "time_ms" : "(optional, long) Time in milliseconds when the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
  "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
  "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time_ms" : "(optional, long) Time in milliseconds when the event happened",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.behaviors.pushnotification.TokenStateChange

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time_ms" : "(optional, long) Time in milliseconds when the event happened",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "time_ms" : "(optional, long) Time in milliseconds when the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Token State Changed (users.behaviors.pushnotification.TokenStateChange)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time_ms" : "(optional, long) Time in milliseconds when the event happened",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

### Detalhes da propriedade

- O campo `push_token_foreground_push_disabled` indica se o token por push pode receber push em primeiro plano ou em segundo plano.
  - Se o usuário permitiu explicitamente a permissão de notificação por push no dispositivo, o valor será `false`, e o token poderá receber notificações por push em primeiro plano.
  - Se o usuário negou explicitamente a permissão de notificação por push no dispositivo, o valor será `true`, e o token só poderá receber notificações por push em segundo plano.
  - Se a permissão de push ainda não foi determinada (por exemplo, o usuário ainda não respondeu ao prompt do sistema operacional), o valor será `true`, e o token só poderá receber notificações por push em segundo plano.
  - Esse campo pode ser `null` (ou vazio, dependendo do formato do destino) para registros de token de SDK mais antigos que ainda não reportaram o status de permissão e para tokens de web push. Trate `null` da mesma forma que `false` (habilitado para push em primeiro plano), pois a Braze ainda tenta enviar notificações por push em primeiro plano para esses tokens.
  - Uma tentativa de envio de push não atualiza esse campo. Se um envio for bem-sucedido, nenhum evento `TokenStateChange` é emitido. Se um envio sofrer bounce porque o token é inválido, a Braze emite um evento "remove" e exclui o token.
  - Esse campo só muda quando a Braze recebe uma atualização de estado do token do SDK (por exemplo, uma sincronização de sessão posterior que reporta o status de permissão de push).
- O campo `push_token_provisionally_opted_in` se aplica apenas a tokens por push do iOS.
  - Se você tiver a [Autorização Provisória]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push) configurada, os tokens provisórios terão este campo definido como `true`. Todos os outros tokens por push serão `false`.
- O campo `sdk_version` só será preenchido se a mudança de estado do token for iniciada pelo SDK.
  - Se houver um evento SDK `changeUser` que aciona a movimentação do token de um usuário para outro, o campo `sdk_version` será preenchido.
  - Se houver um bounce de push (por exemplo, devido à desinstalação), o campo `sdk_version` ficará em branco.
- Sempre que um token por push entra na Braze, seus eventos de ciclo de vida são registrados. Existem três tipos de eventos de mudança de token ("add", "update" e "remove") registrados no campo `push_token_state_change_type`.

#### Tipos de eventos {#event-types}

##### Add {#add}

Um evento "add" é registrado quando um novo token é cadastrado. Isso acontece quando um usuário abre o app em um novo dispositivo pela primeira vez, ou quando um token é definido por meio do endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) com `push_tokens` para um usuário que não tinha um anteriormente. O campo `time_ms` indica quando o evento de adição aconteceu.

{% alert note %}
Para o iOS Swift SDK 13.3.0 e posterior, e Android SDK 40.0.0 e posterior, o status de permissão de push e o token por push são enviados juntos. Para novos registros desses SDKs, `push_token_foreground_push_disabled` é preenchido no evento "add" (normalmente `false` quando as notificações estão ativadas).<br><br>

Registros de token mais antigos ainda podem ter esse campo como `null` até que o SDK reporte posteriormente o status de permissão de push. Tokens de web push também podem ter esse campo como `null` por design.
{% endalert %}

##### Update {#update}

Um evento "update" é registrado quando uma propriedade muda em um token existente sem que a string do token em si mude. O token tem a mesma string, mesmo usuário e mesmo app, mas um ou mais dos seguintes campos mudaram: `foreground_push_disabled`, gateway APNs, chaves de web push, `provisionally_opted_in` ou `device_id`. Essas atualizações vêm de eventos de sincronização de estado do token (por exemplo, quando o SDK reporta um novo estado de permissão), não de resultados de envio de push. O campo `time_ms` indica quando o evento de atualização aconteceu.

A Braze também emite um evento "update" com `push_token_state_change_type` definido como `"update"` quando um usuário anônimo é identificado no mesmo perfil e os tokens por push existentes permanecem nesse perfil. Nesse caso, `user_id` não muda, e `external_user_id` é definido como o ID externo do usuário identificado. Isso inclui a identificação por meio do endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) e do SDK `changeUser` quando ele atribui um ID externo ao perfil anônimo no dispositivo.

{% alert note %}
Na maioria dos casos, a reinstalação do app ou a restauração de backup resulta em um novo evento "add" com um novo `push_token` e novo `device_id` (porque o SDK gera um novo `device_id` e o sistema operacional fornece uma nova string de token por push). Isso cria duas entradas separadas de token e dispositivo no perfil do usuário, e a entrada mais antiga é removida posteriormente por meio do Uninstall Tracking ou envio de campanha.<br><br>

Seria extremamente raro que apenas o `device_id` mudasse sem que o `push_token` mudasse (isso exigiria que o sistema operacional retornasse a mesma string de token após a reinstalação).
{% endalert %}

##### Remove {#remove}

Um evento "remove" independente é registrado quando a Braze remove um token. Isso pode acontecer por várias razões:

- Bounce de push (APNs, FCM ou HMS reporta o token como inválido ou expirado)
- Detecção de desinstalação por meio de push silencioso
- Token removido por meio da REST API ou serviço de feedback APNs

Quando um bounce de push aciona a remoção do token, a Braze emite `push_token_state_change_type = "remove"` para esse token. Ela não emite um evento "update" que altera `push_token_foreground_push_disabled`.

O campo `time_ms` indica quando o evento de remoção aconteceu.

{% alert note %}
Para eventos "remove", os seguintes campos de propriedade do token não são preenchidos: `push_token_created_at`, `push_token_updated_at`, `push_token_foreground_push_disabled`, `push_token_provisionally_opted_in`, `ios_push_token_apns_gateway`, `web_push_token_public_key`, `web_push_token_user_auth` e `web_push_token_vapid_public_key`.
{% endalert %}

##### Pares de add e remove {#add-and-remove-pairs}

Pares de add e remove são dois eventos de estado de token vinculados para a mesma transição: um evento "add" e um evento "remove".
Os pares de add e remove se enquadram em duas categorias:

**Atualização da string do token (mesmo usuário):** O sistema operacional rotaciona a string do token no mesmo dispositivo (por exemplo, rotação de token APNs ou FCM). O evento "add" (novo token) e o evento "remove" (token antigo) têm o mesmo `user_id`, mesmo `device_id`, `push_token` diferente e `time_ms` idêntico.

**Token se move entre usuários:** Um token se move de um usuário para outro. O evento "add" (novo usuário) e o evento "remove" (usuário antigo) têm `user_id` diferentes, mesmo `device_id`, mesmo `push_token` e `time_ms` diferentes (tipicamente menos de 100 milissegundos de diferença). Isso é acionado por qualquer um dos seguintes cenários:

- O SDK chama `changeUser` de um perfil anônimo para um perfil identificado. O evento "remove" terá um `external_user_id` vazio.
- O SDK chama `changeUser` de um perfil identificado para outro. Ambos os eventos terão um `external_user_id` não vazio.
- O endpoint [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) ou a limpeza de usuários duplicados move os tokens do usuário órfão para o usuário sobrevivente.

{% alert note %}
A identificação no mesmo perfil por meio do endpoint REST [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) ou do SDK `changeUser` atribuindo um ID externo ao perfil anônimo não altera o `user_id` e não emite pares de eventos add e remove. Em vez disso, a Braze emite um evento "update" para cada token por push existente e define `external_user_id` como o ID externo do usuário identificado. Quando `changeUser` move tokens de um perfil de usuário para outro, a Braze ainda emite os pares de eventos add e remove descritos na lista anterior.
{% endalert %}

#### Consultando o estado mais recente do token ativo {#querying-for-the-latest-active-token-state}

Para determinar o estado atual do token por push de cada usuário, particione os eventos de mudança de estado do token por `push_token`, `user_id` e `app_id`, depois ordene por `time_ms` em ordem decrescente e filtre os eventos "remove". Internamente, um token é indexado pela sua string de token e `app_id` por usuário. Usar `device_id` como chave de partição não é recomendado porque `device_id` é um atributo mutável, e particionar por ele pode dividir o ciclo de vida de um único token entre várias partições.

A seguinte consulta SQL retorna o estado mais recente do token ativo por usuário no Snowflake:

```sql
WITH latest_token_state AS (
  SELECT *,
    ROW_NUMBER() OVER (
      PARTITION BY PUSH_TOKEN, USER_ID, APP_ID
      ORDER BY COALESCE(TIME_MS, TIME * 1000) DESC
    ) AS rn
  FROM USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE
)
SELECT
  PUSH_TOKEN, USER_ID, EXTERNAL_USER_ID, PUSH_TOKEN_DEVICE_ID,
  PUSH_TOKEN_STATE_CHANGE_TYPE, PUSH_TOKEN_FOREGROUND_PUSH_DISABLED,
  TIME_MS, PLATFORM, APP_ID
FROM latest_token_state
WHERE rn = 1
  AND PUSH_TOKEN_STATE_CHANGE_TYPE != 'remove';
```


{% endapi %}