---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: Comportamiento del cliente y eventos de usuario
article_title: Comportamiento del cliente y eventos de usuario
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glosario enumera los diversos eventos de comportamiento del cliente y de usuario que Braze puede rastrear y enviar a los almacenes de datos elegidos mediante Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details Alcance del esquema y recursos relacionados %}

Los esquemas de almacenamiento se aplican a los datos de eventos en archivos planos que enviamos a los partners de almacenamiento en almacenes de datos (Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage). Algunas combinaciones de eventos y destinos enumeradas aquí aún no están disponibles de forma general. Para obtener información sobre qué eventos son compatibles con los distintos partners, consulta nuestra lista de [partners disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) y revisa sus páginas respectivas.

{% alert tip %}
Estos eventos también están disponibles como tablas SQL en el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder), las [extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) y el [intercambio de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Para los esquemas de tablas SQL y detalles de columnas, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).
{% endalert %}

Ponte en contacto con tu representante de Braze o abre un [ticket de soporte]({{site.baseurl}}/braze_support) si necesitas acceso a derechos de eventos adicionales. Si no encuentras lo que necesitas en esta página, consulta nuestra [biblioteca de eventos de participación en mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) o nuestros [ejemplos de datos de muestra de Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explicación de la estructura de eventos de comportamiento del cliente y de usuario, y valores de plataforma %}

## Estructura de eventos {#event-structure}

Este desglose de eventos de comportamiento del cliente y de usuario muestra qué tipo de información se incluye generalmente en un evento de comportamiento del cliente o de usuario. Con una comprensión sólida de sus componentes, tus desarrolladores y tu equipo de estrategia de inteligencia empresarial pueden utilizar los datos de eventos entrantes de Currents para crear informes y gráficos basados en datos, y aprovechar otras métricas de datos valiosas.

![Desglose de un evento de usuario que muestra un evento de compra con las propiedades enumeradas agrupadas por propiedades específicas del usuario, propiedades específicas del comportamiento y propiedades específicas del dispositivo]({% image_buster /assets/img/customer_engagement_event.png %})

Los eventos de comportamiento del cliente y de usuario se componen de propiedades **específicas del usuario**, propiedades **específicas del comportamiento** y propiedades **específicas del dispositivo**.

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

{% details Consideraciones para eventos de comportamiento del cliente y de usuario %}

- Currents descarta eventos con cargas útiles excesivamente grandes de más de 900&nbsp;KB.
- Muchos de los eventos en este glosario son iniciados por el SDK. Algunos eventos, como `token_state_change`, pueden ser iniciados por el SDK o por el backend (por ejemplo, en respuesta a un rebote de push). Los campos `sdk_version`, `gender`, `language` y `country` solo se establecen para eventos iniciados por el SDK; para eventos iniciados por el backend, o cuando esa información no está disponible o no se ha establecido para el usuario, estos campos pueden ser `null`.

{% enddetails %}

</div>

<!--overview-end-->