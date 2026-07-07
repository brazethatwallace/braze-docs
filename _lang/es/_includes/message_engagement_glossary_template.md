---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: Eventos de interacción con mensajes
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Este glosario enumera los diversos eventos de interacción con mensajes que Braze puede rastrear y enviar a los almacenes de datos elegidos mediante Currents."
tool: Currents
search_rank: 6
lazy_partner_tabs: true
---

<div class="api-glossary-preamble" markdown="1">

{% details Alcance del esquema y recursos relacionados %}

Los esquemas de almacenamiento se aplican a los datos de eventos en archivos planos que enviamos a los partners de almacenamiento en almacenes de datos (Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage). Para los esquemas que se aplican a los demás partners, consulta nuestra lista de [partners disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) y revisa sus páginas respectivas.

{% alert tip %}
Estos eventos también están disponibles como tablas SQL en el [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), las [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) y [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Para los esquemas de tablas SQL y detalles de columnas, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).
{% endalert %}

Ponte en contacto con tu director de cuentas o abre un [ticket de soporte]({{site.baseurl}}/braze_support) si necesitas acceso a derechos de eventos adicionales. Si no encuentras lo que necesitas en este artículo, consulta nuestra [biblioteca de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) o nuestros [ejemplos de datos de muestra de Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explicación de la estructura de eventos de interacción con mensajes y valores de plataforma %}

## Estructura de eventos {#event-structure}

Este desglose de eventos muestra qué tipo de información se incluye generalmente en un evento de interacción con mensajes. Con una comprensión sólida de sus componentes, tus desarrolladores y tu equipo de estrategia de inteligencia empresarial pueden utilizar los datos de eventos entrantes de Currents para crear informes y gráficos basados en datos, y aprovechar otras métricas de datos valiosas.

![Desglose de un evento de interacción con mensajes que muestra un evento de cancelación de suscripción de correo electrónico con las propiedades enumeradas agrupadas por propiedades específicas del usuario, propiedades de seguimiento de Campaign o Canvas, y propiedades específicas del evento]({% image_buster /assets/img/message_engagement_event.png %})

Los eventos de interacción con mensajes se componen de propiedades **específicas del usuario**, propiedades de **seguimiento de Campaign/Canvas** y propiedades **específicas del evento**.

### Esquema de ID de usuario {#user-id-schema}

Ten en cuenta las convenciones de nomenclatura para los ID de usuario.

| Esquema de Braze | Esquema de Currents | Descripción |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | El identificador único que Braze asigna automáticamente. |
| `external_id` | `"EXTERNAL_USER_ID"` | El identificador único del perfil de un usuario que establece el cliente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de ID de usuario" }

### Valores de plataforma {#platform-values}

Ciertos eventos devuelven un valor `platform` que especifica la plataforma del dispositivo del usuario.
<br>La siguiente tabla detalla los posibles valores devueltos:

| Dispositivo del usuario | Valor de plataforma |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Valores de plataforma" }

{% enddetails %}

{% details Consideraciones para los eventos de interacción con mensajes %}

- Currents descarta los eventos con cargas útiles superiores a 900&nbsp;KB.
- Los objetos relacionados con Canvas Flow tienen ID que puedes usar para agrupar y traducir a nombres legibles a través del [endpoint Exportar detalles de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details).
- Es posible que ciertos campos no muestren su estado más reciente inmediatamente después de actualizar una campaña o un Canvas:
  - `campaign_name`
  - `canvas_name`
  - `canvas_step_name`
  - `conversion_behavior`
  - `canvas_variation_name`
  - `experiment_split_name`
  - `message_variation_name`
- Si necesitas una consistencia completa para estos campos, espera una hora después de la última actualización antes de enviar mensajes a tus usuarios.

{% enddetails %}

</div>

<!--overview-end-->