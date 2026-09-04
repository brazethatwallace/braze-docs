---
nav_title: Ingesta de datos de Cloud
article_title: Ingesta de datos de Cloud de Braze
alias: /cloud_ingestion/
description: "Este artículo de referencia cubre las fuentes de Ingesta de datos de Cloud de Braze y las recomendaciones de configuración de datos."
page_order: 1
toc_headers: h2
---

# Ingesta de datos de Cloud de Braze {#braze-cloud-data-ingestion}

> La Ingesta de datos de Cloud (CDI) de Braze te permite configurar una conexión directa desde tu solución de almacenamiento de datos para sincronizar datos de usuario relevantes y otros datos no relacionados con los usuarios con Braze. Estos datos pueden utilizarse para la personalización o segmentación con el fin de potenciar tus casos de uso de marketing. La integración flexible de la Ingesta de datos de Cloud admite estructuras de datos complejas, incluyendo JSON anidados y matrices de objetos.

## Cómo funciona {#how-it-works}

Con la ingesta de datos en la nube (CDI) de Braze, configuras una integración entre tu instancia de almacén de datos y tu espacio de trabajo de Braze para sincronizar datos de forma recurrente. Esta sincronización se ejecuta según un calendario que tú defines, y cada integración puede tener un calendario diferente. Las sincronizaciones pueden ejecutarse con una frecuencia de hasta cada 15 minutos o tan esporádicamente como una vez al mes. Si necesitas que las sincronizaciones se produzcan con más frecuencia que cada 15 minutos, ponte en contacto con tu administrador de éxito de cliente o considera usar llamadas a la REST API para la ingesta de datos en tiempo real.

Las integraciones de almacenamiento de archivos de Amazon S3 están controladas por eventos. Braze ingiere los nuevos archivos cuando llegan las notificaciones de S3/SQS. Para obtener más detalles sobre la configuración, consulta [Integraciones de almacenamiento de archivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).

{% alert note %}
La frecuencia de sincronización en el panel controla con qué frecuencia Braze ejecuta una sincronización (por ejemplo, opciones como ejecuciones cada hora o más frecuentes dentro de una hora). No establece un intervalo personalizado superior a una hora entre ejecuciones. Para ejecutar una sincronización fuera de la cadencia programada, como bajo demanda después de que se complete la carga de tu almacén de datos, usa el endpoint [Desencadenar una sincronización]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) con tu ID de integración.
{% endalert %}

Cuando se ejecuta una sincronización, Braze se conecta directamente a tu instancia de almacén de datos, recupera todos los datos nuevos de la tabla especificada y actualiza los datos correspondientes en tu panel de Braze. Cada vez que se ejecuta la sincronización, cualquier dato actualizado se refleja en Braze.

### Encontrar tu ID de integración {#finding-your-integration-id}

Puedes encontrar tu ID de integración en la URL cuando visualizas una integración en el panel de Braze. Ve a **Data Settings** > **Cloud Data Ingestion** y selecciona una integración. El ID de integración aparece en la URL con el formato `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Por ejemplo, si tu URL es `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`, tu ID de integración es `abc123xyz`. Puedes usar este ID al realizar llamadas a la API para desencadenar sincronizaciones o comprobar el estado de la sincronización.

## Ejemplos {#use-cases}

Con las funcionalidades de ingesta de datos en la nube de Braze, puedes:

- Crear una integración sencilla directamente desde tu almacén de datos o solución de almacenamiento de archivos a Braze en solo unos minutos.
- Sincronizar de forma segura datos de usuario, incluidos atributos, eventos y compras, desde tu almacén de datos a Braze.
- Cerrar el ciclo de datos con Braze combinando la ingesta de datos en la nube con Currents o Snowflake Data Sharing.

Además, las [fuentes conectadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) son una alternativa de copia cero. Puedes hacer que Braze consulte directamente tu almacén de datos o solución de almacenamiento de archivos para construir segmentos CDI &#8212;todo sin copiar los datos subyacentes a Braze.

## Orígenes de datos compatibles {#supported-data-sources}

La ingesta de datos en la nube puede sincronizar datos desde:

   - Amazon Redshift
   - Databricks
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Tipos de datos compatibles {#supported-data-types}

La ingesta de datos en la nube admite los siguientes tipos de datos:

### Datos de usuario {#user-data}
- Atributos de usuario, incluyendo:
   - Atributos personalizados anidados
   - Matrices de objetos
   - Estados de suscripción
- Eventos personalizados
- Eventos de compra
- Solicitudes de eliminación de usuarios

### Objetos que no son de usuario {#non-user-objects}
- Elementos de catálogo

### Mensajería de copia cero {#zero-copy-messaging}
- Fuentes conectadas

## Identificadores de usuario para la ingesta de datos {#user-identifiers-for-data-ingestion}

Al sincronizar datos de usuario a través de la ingesta de datos en la nube, puedes identificar a los usuarios utilizando uno o más de los siguientes tipos de identificadores. Cada fila de tu tabla de origen debe contener un valor para un solo tipo de identificador a la vez, pero tu tabla puede incluir columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.

| Identificador | Descripción |
|------------|-------------|
| `EXTERNAL_ID` | El ID externo que identifica el perfil de usuario que se va a crear o actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y `alias_label` especifica el tipo de alias. Los usuarios pueden tener múltiples alias con diferentes etiquetas, pero solo un `alias_name` por cada `alias_label`. |
| `BRAZE_ID` | El identificador de usuario de Braze generado por el SDK de Braze. No se pueden crear nuevos usuarios utilizando un Braze ID a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID externo de usuario o un alias de usuario. |
| `EMAIL` | La dirección de correo electrónico del usuario. Si existen múltiples perfiles con la misma dirección de correo electrónico, se prioriza para las actualizaciones el perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, el correo electrónico se utiliza como identificador principal. |
| `PHONE` | El número de teléfono del usuario. Si existen múltiples perfiles con el mismo número de teléfono, se prioriza para las actualizaciones el perfil actualizado más recientemente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identificadores de usuario para la ingesta de datos" }

Para obtener información detallada sobre la configuración de columnas de tabla y los requisitos de formato de la carga útil, consulta [Configuración de tablas para la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

Para instrucciones de configuración específicas de cada origen y ejemplos de SQL, consulta [Integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Uso de puntos de datos {#data-point-usage}

Para los clientes con facturación basada en puntos de datos, la facturación de puntos de datos para la ingesta de datos en la nube es equivalente a la facturación de las actualizaciones a través del [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Consulta [Puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points) para obtener más información.

{% alert important %}
La ingesta de datos en la nube de Braze cuenta para el límite de velocidad disponible, por lo que si estás enviando datos mediante otro método, el límite de velocidad se combina entre la API de Braze y la ingesta de datos en la nube.
{% endalert %}

## Limitaciones del producto {#product-limitations}

| Limitación | Descripción |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integraciones | No hay límite en la cantidad de integraciones que puedes configurar. Sin embargo, solo puedes configurar una integración por tabla o vista. |
| Número de filas | De forma predeterminada, cada ejecución puede sincronizar hasta 500 millones de filas. Cualquier sincronización con más de 500 millones de filas nuevas se detiene. Si necesitas un límite más alto, ponte en contacto con tu administrador de éxito de cliente de Braze o con soporte de Braze. |
| Atributos por fila | Cada fila debe contener un único ID de usuario y un objeto JSON con un máximo de 250 atributos. Cada clave del objeto JSON cuenta como un atributo (es decir, un array cuenta como un atributo). |
| Tamaño de la carga útil | Cada fila puede contener una carga útil de hasta 1 MB. Las cargas útiles superiores a 1 MB se rechazan, y el error "Payload was greater than 1MB" se registra en el registro de sincronización junto con el ID externo asociado y la carga útil truncada. |
| Tipo de datos | Puedes sincronizar atributos de usuario, eventos personalizados, eventos de compra, elementos de catálogo, solicitudes de eliminación de usuarios y desencadenantes de Canvas a través de la ingesta de datos de Cloud. |
| Región de Braze | Este producto está disponible en todas las regiones de Braze. Cualquier región de Braze puede conectarse a cualquier región de origen de datos. |
| Región de origen | Braze se conecta a tu almacén de datos o entorno en la nube en cualquier región o proveedor de nube. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitaciones del producto" }