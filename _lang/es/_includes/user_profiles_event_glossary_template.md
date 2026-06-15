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

{% alert tip %}
Estos eventos también están disponibles como tablas SQL en el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/), las [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) y el [Uso compartido de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Para los esquemas de tablas SQL y detalles de columnas, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Ponte en contacto con tu representante de Braze o abre un [ticket de soporte]({{site.baseurl}}/braze_support/) si necesitas acceso a permisos de eventos adicionales. Si no encuentras lo que necesitas en esta página, consulta la [biblioteca de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/), la [biblioteca de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) o los [ejemplos de datos de muestra de Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicación de la estructura de eventos de actualización de perfiles de usuario %}

### Estructura de eventos {#event-structure}

Este desglose de eventos de comportamiento del cliente y de usuario muestra qué tipo de información se incluye generalmente en un evento de actualización de perfil de usuario. Con una comprensión sólida de sus componentes, tu equipo de desarrolladores y de estrategia de inteligencia empresarial puede utilizar los datos de eventos entrantes de Currents para crear informes y gráficos basados en datos, y aprovechar otras métricas de datos valiosas.

{% alert important %}
Los esquemas de almacenamiento se aplican a los datos de eventos en archivos planos enviados a socios de almacenamiento en almacenes de datos, como Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage. Algunas combinaciones de eventos y destinos enumeradas aquí aún no están disponibles de forma general. Para obtener información sobre los eventos compatibles por socio, consulta los [socios disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) y las páginas del socio relacionadas.

Currents descarta eventos con cargas útiles superiores a 900 KB.
{% endalert %}