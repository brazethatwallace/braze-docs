---
nav_title: Comportamiento del cliente y eventos de los usuarios
article_title: Comportamiento del cliente y eventos de los usuarios
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glosario enumera los distintos eventos de comportamiento del cliente y del usuario que Braze puede rastrear y enviar a los almacenes de datos elegidos mediante Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details Alcance del esquema y recursos relacionados %}

Los esquemas de almacenamiento se aplican a los datos de eventos de archivos planos que enviamos a los socios de almacenamiento en almacenes de datos (Google Cloud Storage, Amazon S3 y Microsoft Azure Blob Storage). Algunas combinaciones de eventos y destinos que figuran aquí aún no están disponibles de forma general. Para saber qué eventos son compatibles con los distintos socios, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) y revisa sus respectivas páginas.

{% alert tip %}
Estos eventos también están disponibles como tablas SQL en el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), las [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) y el [Uso compartido de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Para los esquemas de tablas SQL y detalles de columnas, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Ponte en contacto con tu representante de Braze o abre un [ticket de soporte]({{site.baseurl}}/braze_support/) si necesitas acceder a derechos de eventos adicionales. Si no encuentras lo que necesitas en esta página, consulta nuestra [biblioteca de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) o nuestros [ejemplos de datos de muestra de Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explicación de la estructura de eventos de comportamiento del cliente y del usuario, y valores de plataforma %}

### Estructura del evento {#event-structure}

Este desglose del comportamiento del cliente y de los eventos del usuario muestra qué tipo de información se incluye generalmente en un evento de comportamiento del cliente o del usuario. Con una sólida comprensión de sus componentes, tus desarrolladores y el equipo de estrategia de inteligencia empresarial pueden utilizar los datos de eventos entrantes de Currents para elaborar informes y gráficos basados en datos, y aprovechar otras valiosas métricas de datos.

![Desglose de un evento de usuario que muestra un evento de compra con las propiedades enumeradas agrupadas por propiedades específicas del usuario, propiedades específicas del comportamiento y propiedades específicas del dispositivo]({% image_buster /assets/img/customer_engagement_event.png %})

El comportamiento del cliente y los eventos del usuario se componen de propiedades **específicas del usuario**, propiedades **específicas del comportamiento** y propiedades **específicas del dispositivo**.

### Valores de la plataforma {#platform-values}

Algunos eventos devuelven un valor `platform` que especifica la plataforma del dispositivo del usuario.
<br>La siguiente tabla detalla los posibles valores devueltos:

| Dispositivo del usuario | Valor de la plataforma |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Platform values" }

{% enddetails %}

{% details Consideraciones sobre el comportamiento del cliente y los eventos del usuario %}

- Currents descarta los eventos con cargas útiles excesivamente grandes, superiores a 900&nbsp;KB.
- Muchos de los eventos de este glosario son iniciados por el SDK. Algunos eventos, como `token_state_change`, pueden ser iniciados tanto por el SDK como por el backend (por ejemplo, en respuesta a un rebote de push). Los campos `sdk_version`, `gender`, `language` y `country` solo se establecen para eventos iniciados por el SDK; para eventos iniciados por el backend, o cuando esa información no está disponible o no se ha configurado para el usuario, estos campos pueden ser `null`.

{% enddetails %}

</div>

<!--overview-end-->