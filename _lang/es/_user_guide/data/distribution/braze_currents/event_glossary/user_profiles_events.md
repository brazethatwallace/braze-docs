---
nav_title: Perfiles de usuario
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glosario enumera las actualizaciones de perfiles de usuario que Braze puede rastrear y enviar a los almacenes de datos elegidos mediante Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% alert important %}
Los eventos de perfiles de usuario están en fase beta. Ponte en contacto con tu administrador del éxito del cliente o director de cuentas para obtener acceso.
{% endalert %}

{% alert tip %}
Estos eventos también están disponibles como tablas SQL en el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder), las [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) y el [Uso compartido de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Para los esquemas de tablas SQL y detalles de columnas, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/sql_segments/sql_segments_tables). Para los esquemas de Uso compartido de datos de Snowflake de las vistas de atributos de perfiles de usuario, consulta [Atributos de perfiles de usuario]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

Ponte en contacto con tu representante de Braze o abre un [ticket de soporte]({{site.baseurl}}/braze_support) si necesitas acceso a derechos de eventos adicionales. Si no encuentras lo que necesitas en esta página, consulta la [Biblioteca de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events), la [Biblioteca de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events) o los [ejemplos de datos de muestra de Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicación de la estructura de eventos de actualización de perfiles de usuario %}

### Estructura de eventos {#event-structure}

Este desglose de eventos de comportamiento del cliente y de usuario muestra qué tipo de información se incluye generalmente en un evento de actualización de perfil de usuario. Con una comprensión sólida de sus componentes, tus desarrolladores y el equipo de estrategia de inteligencia empresarial pueden utilizar los datos de eventos entrantes de Currents para crear informes y gráficos basados en datos, y aprovechar otras métricas de datos valiosas.

{% alert important %}
Los esquemas de almacenamiento se aplican a los datos de eventos de archivos planos enviados a socios de almacenamiento en almacenes de datos, como Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage. Algunas combinaciones de eventos y destinos enumeradas aquí aún no están disponibles de forma general. Para obtener información sobre los eventos compatibles por socio, consulta los [socios disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners) y las páginas del socio relacionadas.

Currents descarta los eventos con cargas útiles superiores a 900 KB.
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->

{% api %}
## Eventos de actualización de perfiles de usuario {#user-profile-update-events}

{% apitags %}
Profile
{% endapitags %}

Esto representa las actualizaciones de perfil de un usuario.

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
  "dob" : "(optional, string) [PII] Date of birth of the user in format \"YYYY-MM-DD\"",
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
{% endtabs %}

{% endapi %}