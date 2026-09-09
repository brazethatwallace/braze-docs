---
nav_title: Extensiones de segmento CDI
article_title: Extensiones de segmento CDI
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool:
- Segments
description: "Este artículo explica cómo las extensiones de segmento CDI utilizan la ingesta de datos en la nube para consultar tu almacén de datos y definir audiencias en Braze."

---

# Extensiones de segmento CDI {#cdi-segment-extensions}

> Con la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) (CDI) de Braze, puedes configurar una conexión directa desde tu almacén de datos o sistema de almacenamiento de archivos a Braze para sincronizar datos relevantes de usuarios o catálogos de forma recurrente.

{% alert warning %}
Las extensiones de segmento CDI consultan tu almacén de datos directamente, por lo que incurrirás en todos los costos asociados con la ejecución de estas consultas en tu almacén de datos. Las extensiones de segmento CDI no consumen [créditos de segmentos SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#credits), no cuentan para tu límite de extensiones de segmento y no registran puntos de datos.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar los datos de tu almacén de datos para la segmentación dentro de tu espacio de trabajo de Braze, tendrás que crear un [origen conectado]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) y luego crear un segmento CDI dentro de tus [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Las extensiones de segmento CDI te permiten escribir SQL que consulta directamente tu propio almacén de datos utilizando los datos disponibles a través de tus conexiones CDI, y crear un grupo de usuarios al que se puede dirigir dentro de Braze.

## Creación de un segmento CDI {#creating-a-cdi-segment}

### Paso 1: Configura tu origen de datos {#step-1-set-up-your-source}

Antes de crear tu primera extensión de segmento CDI, configura un nuevo origen de datos conectado con tu almacén de datos siguiendo los pasos en [Orígenes de datos conectados]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources).

### Paso 2: Crea un segmento {#step-2-create-a-segment}

1. Ve a **Audiencia** > **Extensiones de segmento** y selecciona **Crear nueva extensión**.
2. En el menú **Selecciona tu experiencia de creación de extensión de segmento**, selecciona **Actualización completa (incluidos los segmentos CDI)**.

![El menú "Selecciona tu experiencia de creación de extensión de segmento" con las opciones de creación.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

{: start="3"}
3. En el menú **Selecciona el origen de datos para esta extensión de segmento**, elige **Tablas de datos CDI**. Este menú solo aparece después de que hayas configurado al menos un [origen de datos conectado]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources).

![El menú "Selecciona el origen de datos para esta extensión de segmento" con la opción Tablas de datos CDI.]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

{: start="4"}
4. Selecciona una conexión para usar y luego escribe tu consulta. Cada conexión tiene un conjunto específico de tablas de datos. Tu equipo de desarrollo puede configurar tus conexiones y tablas de datos durante la configuración de CDI.
5. Visualiza las tablas de datos disponibles, incluidos sus esquemas y cualquier descripción disponible, seleccionando **Explorador de origen**.

![El Explorador de origen mostrando las tablas de datos disponibles, incluidos sus esquemas y cualquier descripción disponible.]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

{: start="6"}
6. Escribe el SQL para tu segmento utilizando [la sintaxis SQL de Braze]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#step-2-write-your-sql). Ten en cuenta que todas las extensiones de segmento CDI deben usar `external_user_id` como la columna seleccionada, y tu `external_user_id` debe coincidir con el configurado en Braze para los usuarios.<br><br>
Si los resultados de tu consulta incluyen usuarios que no existen en Braze, esos usuarios se ignoran. Braze no crea nuevos usuarios basándose en el resultado de tu extensión de segmento CDI.

{% alert important %}
`external_user_id` debe ser un valor de cadena. Si tu ID de origen se almacena como un número (por ejemplo, `client_id` como un entero), [conviértelo a cadena en tu SQL](https://www.w3schools.com/sql/func_sqlserver_cast.asp) para que coincida con el tipo `external_id` en Braze.
{% endalert %}

{: start="7"}
7. [Usa esta extensión de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment) dentro de un Segment de Braze para enviar una Campaign o un Canvas a esta audiencia.

{% alert tip %}
Para aprender cómo puedes previsualizar tus extensiones de segmento, gestionar tus extensiones de segmento y ejecutar actualizaciones automatizadas de membresía, consulta [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).
{% endalert %}

## Consideraciones {#considerations}

- Una extensión de segmento solo puede hacer referencia a datos de una conexión, no de varias.
- Una extensión de segmento puede usar uno de los siguientes como origen de datos: datos de CDI o datos de Braze Snowflake (Currents). No puedes combinar orígenes de datos dentro de una extensión de segmento, pero puedes crear varias extensiones de segmento para hacer referencia a ellas de forma conjunta dentro de un Segment.

## Solución de problemas {#troubleshooting}

- Es posible que tu consulta agote el tiempo de espera cuando alcance el tiempo máximo de ejecución, que se configura para cada sincronización de conexión en la página de **Cloud Data Ingestion**. El tiempo máximo de ejecución permitido es de 60 minutos.
- Asegúrate de que tu SQL esté escrito con la sintaxis adecuada para tu almacén de datos.