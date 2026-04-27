---
nav_title: Eventos de interacción con mensajes
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Este glosario enumera los distintos eventos de interacción con mensajes que Braze puede rastrear y enviar a los almacenes de datos elegidos mediante Currents."
tool: Currents
search_rank: 6
---

Los esquemas de almacenamiento se aplican a los datos de eventos de archivos planos que enviamos a los socios de almacenamiento en almacén de datos (Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage). Para los esquemas que se aplican a los demás socios, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) y revisa sus respectivas páginas.

{% alert tip %}
Estos eventos también están disponibles como tablas SQL en el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), las [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) y el [Uso compartido de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Para los esquemas de tablas SQL y detalles de columnas, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Ponte en contacto con tu director de cuentas o abre un [ticket de soporte]({{site.baseurl}}/braze_support/) si necesitas acceso a derechos de eventos adicionales. Si no encuentras lo que necesitas en este artículo, consulta nuestra [biblioteca de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) o nuestros [ejemplos de datos de muestra de Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicación de la estructura de eventos de interacción con mensajes y valores de plataforma %}

### Estructura del evento {#event-structure}

Este desglose de eventos muestra qué tipo de información se incluye generalmente en un evento de interacción con mensajes. Con una comprensión sólida de sus componentes, tus desarrolladores y el equipo de estrategia de inteligencia empresarial pueden utilizar los datos de eventos entrantes de Currents para elaborar informes y gráficos basados en datos, y aprovechar otras métricas de datos valiosas.

![Desglose de un evento de interacción con un mensaje que muestra un evento de cancelación de suscripción de correo electrónico con las propiedades enumeradas agrupadas por propiedades específicas del usuario, propiedades de seguimiento de Campaign o Canvas y propiedades específicas del evento]({% image_buster /assets/img/message_engagement_event.png %})

Los eventos de interacción con mensajes se componen de propiedades **específicas del usuario**, propiedades de **seguimiento de Campaign/Canvas** y propiedades **específicas del evento**.

### Esquema de ID de usuario {#user-id-schema}

Ten en cuenta las convenciones de nomenclatura para los ID de usuario.

| Esquema de Braze | Esquema de Currents | Descripción |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | El identificador único que Braze asigna automáticamente. |
| `external_id` | `"EXTERNAL_USER_ID"` | El identificador único del perfil de un usuario configurado por el cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Valores de plataforma {#platform-values}

Algunos eventos devuelven un valor `platform` que especifica la plataforma del dispositivo del usuario.
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
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Currents descartará los eventos con cargas útiles excesivamente grandes, superiores a 900&nbsp;KB.
{% endalert %}

{% alert note %}
Los objetos relacionados con Canvas Flow tienen ID que pueden utilizarse para agrupar y traducirse a nombres legibles mediante el [punto de conexión Exportar detalles de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).
{% endalert %}

{% alert note %}
Algunos campos pueden tardar más en mostrar su estado más reciente después de actualizar una campaña o Canvas. Estos campos son:
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
Si se requiere una coherencia total, te recomendamos esperar una hora desde la última actualización de estos campos antes de enviar la mensajería a tus usuarios.
{% endalert %}