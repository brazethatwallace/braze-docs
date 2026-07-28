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

Para usar los datos de tu almacén de datos para la segmentación dentro de tu espacio de trabajo de Braze, necesitarás crear un [origen conectado]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) y luego crear un segmento CDI dentro de tus [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Las extensiones de segmento CDI te permiten escribir SQL que consulta directamente tu propio almacén de datos utilizando los datos disponibles a través de tus conexiones CDI, y crear un grupo de usuarios al que puedes dirigirte dentro de Braze.

## Crear un segmento CDI {#creating-a-cdi-segment}

### Paso 1: Configura tu origen {#step-1-set-up-your-source}

Antes de crear tu primera extensión de segmento CDI, configura un nuevo origen conectado con tu almacén de datos siguiendo los pasos en [Orígenes conectados]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources).

### Paso 2: Crea un segmento {#step-2-create-a-segment}

Primero, crea una nueva [extensión de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) y luego selecciona **Full refresh**.

![Ejemplo de ubicación del modal de tarjeta de contenido.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

Para tu origen de datos, elige **CDI Data Tables**.

![Captura de pantalla relacionada con el paso 2: crear un segmento.]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

Como parte de tu configuración CDI, puedes seleccionar entre diferentes conexiones para usar en las extensiones de segmento CDI. Cada conexión tiene un conjunto específico de tablas de datos. Tu equipo de desarrollo puede configurar tus conexiones y tablas de datos durante la configuración CDI.

Para ver las tablas de datos disponibles, incluyendo su esquema y cualquier descripción disponible, selecciona **Reference**. Cuando estés listo, selecciona una conexión.

![Para ver las tablas de datos disponibles, incluyendo su esquema y cualquier descripción disponible, selecciona Reference. Cuando estés listo, selecciona una conexión.]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

A continuación, escribe el SQL para tu segmento usando [la sintaxis SQL de Braze]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#step-2-write-your-sql).

Ten en cuenta que todas las extensiones de segmento CDI deben usar `external_user_id` como la columna seleccionada, y tu `external_user_id` debe coincidir con el configurado en Braze para los usuarios.

{% alert important %}
`external_user_id` debe ser un valor de tipo **cadena**. Si tu ID de origen está almacenado como un número (por ejemplo, `client_id` como un entero), [conviértelo a cadena en tu SQL](https://www.w3schools.com/sql/func_sqlserver_cast.asp) para que coincida con el tipo `external_id` en Braze.
{% endalert %}

Si los resultados de tu consulta incluyen usuarios que no existen en Braze, esos usuarios serán ignorados. Braze no crea nuevos usuarios basándose en la salida de tu extensión de segmento CDI.

{% alert tip %}
Para aprender cómo puedes previsualizar tus extensiones de segmento, administrarlas y ejecutar actualizaciones automáticas de membresía, consulta [Extensiones de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).
{% endalert %}

Finalmente, puedes [usar esta extensión de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment) dentro de un segmento de Braze para enviar una Campaign o Canvas a esta audiencia.

## Consideraciones {#considerations}

- Una extensión de segmento solo puede hacer referencia a datos de una conexión, no de varias.
- Una extensión de segmento puede usar uno de los siguientes como origen de datos: datos CDI o datos de Braze Snowflake (Currents). No puedes mezclar orígenes de datos dentro de una extensión de segmento, pero puedes crear múltiples extensiones de segmento para referenciarlas juntas dentro de un segmento.

## Solución de problemas {#troubleshooting}

- Tu consulta podría agotar el tiempo de espera cuando alcance tu tiempo máximo de ejecución, que se configura para cada sincronización de conexión en la página de **Cloud Data Ingestion**. El tiempo máximo de ejecución permitido es de 60 minutos.
- Asegúrate de que tu SQL esté escrito usando la sintaxis apropiada para tu almacén de datos.