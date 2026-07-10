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
Los eventos de perfiles de usuario están en fase beta. Ponte en contacto con tu administrador de éxito de cliente o director de cuentas para obtener acceso.
{% endalert %}

{% alert tip %}
Estos eventos también están disponibles como tablas SQL en el [generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder), las [extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) y el [intercambio de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Para los esquemas de tablas SQL y los detalles de las columnas, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/sql_segments/sql_segments_tables). Para los esquemas de intercambio de datos de Snowflake de las vistas de atributos de perfiles de usuario, consulta [Atributos de perfiles de usuario]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

Ponte en contacto con tu representante de Braze o abre un [ticket de soporte]({{site.baseurl}}/braze_support) si necesitas acceso a derechos de eventos adicionales. Si no encuentras lo que necesitas en esta página, consulta la [biblioteca de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events), la [biblioteca de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events) o los [ejemplos de datos de muestra de Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicación de la estructura de eventos de actualización de perfiles de usuario %}

### Estructura de eventos {#event-structure}

Este desglose de eventos de comportamiento del cliente y de usuario muestra qué tipo de información se incluye generalmente en un evento de actualización de perfil de usuario. Con una comprensión sólida de sus componentes, tus desarrolladores y tu equipo de estrategia de inteligencia empresarial pueden utilizar los datos de eventos entrantes de Currents para crear informes y gráficos basados en datos, y aprovechar otras métricas de datos valiosas.

{% alert important %}
Los esquemas de almacenamiento se aplican a los datos de eventos de archivos planos enviados a los partners de almacenamiento en el cloud, como Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage. Algunas combinaciones de eventos y destinos enumeradas aquí aún no están disponibles de forma general. Para obtener información sobre los eventos compatibles por partner, consulta los [partners disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners) y las páginas del partner relacionadas.

Currents descarta los eventos con cargas útiles superiores a 900 KB.
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->