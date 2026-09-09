---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la ingesta de datos en la nube
page_order: 10
page_type: FAQ
description: "Esta página responde a las preguntas más frecuentes sobre la ingesta de datos en la nube."
toc_headers: h2
---

# Preguntas más frecuentes {#frequently-asked-questions}

> Esta página contiene respuestas a algunas preguntas frecuentes sobre la ingesta de datos en la nube.

## ¿Por qué recibí un correo electrónico con el mensaje "Error in CDI Sync"? {#why-was-i-emailed-error-in-cdi-sync}

Este tipo de correo electrónico suele significar que hay un problema con tu configuración de CDI. A continuación se presentan algunos problemas comunes y cómo solucionarlos:

### CDI no puede acceder al almacén de datos o a la tabla con tus credenciales {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

Esto podría significar que las credenciales en CDI son incorrectas o están mal configuradas en el almacén de datos. Para obtener más información, consulta [Integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

### No se puede encontrar la tabla {#the-table-cannot-be-found}

Intenta actualizar tu integración con la configuración de base de datos correcta o crea los recursos correspondientes en el almacén de datos, como `database/table`.

### No se puede encontrar el catálogo {#the-catalog-cannot-be-found}

El catálogo configurado en la integración no existe en el catálogo de Braze. Un catálogo puede eliminarse después de que la integración se haya configurado. Para resolver el problema, actualiza la integración para utilizar un catálogo diferente o crea un nuevo catálogo que coincida con el nombre del catálogo en la integración.

## ¿Por qué recibí un correo electrónico con el asunto "Row errors in your CDI sync"? {#why-was-i-emailed-row-errors-in-your-cdi-sync}

Este tipo de correo electrónico significa que algunos de tus datos no pudieron procesarse durante la sincronización. Para conocer el error específico, puedes revisar los registros en Braze en **CDI** > **Sync Log**.

## ¿Cómo soluciono el error "Time must be string in ISO8601 Format" en la configuración de CDI? {#how-do-i-fix-time-must-be-string-in-iso8601-format-in-cdi-setup}

Este error significa que el valor de `time` del evento en tu carga útil de CDI no está en un formato de fecha y hora compatible.

Para las cargas útiles de eventos y compras, formatea `time` como:

- Una cadena ISO 8601, o
- `yyyy-MM-dd'T'HH:mm:ss:SSSZ`

Si se omite `time`, Braze utiliza `UPDATED_AT` como la hora del evento.

Para conocer todos los requisitos de la carga útil, consulta [Configuración de tablas para la ingesta de datos en el cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

## ¿Cómo soluciono errores de Probar conexión y correos electrónicos de soporte? {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### Probar conexión se ejecuta lentamente {#test-connection-runs-slow}

Probar conexión se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. Usar una instancia SQL serverless minimizará el tiempo de arranque y mejorará el rendimiento de las consultas, pero puede resultar en costes de integración ligeramente más altos.

### Error al conectar a la instancia de Snowflake: Incoming request with IP is not allowed to access Snowflake {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

Intenta añadir las IP oficiales de Braze a tu lista de IP permitidas. Para más información, consulta [Integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations), o permite las IP relevantes:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Error al ejecutar SQL debido a la configuración del cliente: 002003 (42S02): SQL compilation error: does not exist or not authorized {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

Si la tabla no existe, créala. Si la tabla existe, verifica que el usuario y el rol tengan permisos para leer de la tabla.

### Could not use schema {#could-not-use-schema}

Si recibes este error, concede acceso a ese esquema para el usuario o rol especificado.

### Could not use role {#could-not-use-role}

Si recibes este error, permite que ese usuario utilice el rol especificado.

### User access disabled {#user-access-disabled}

Si recibes este error, permite el acceso de ese usuario a tu cuenta de Snowflake.

### Error al conectar a la instancia de Snowflake con la clave actual y la anterior {#error-connecting-to-snowflake-instance-with-current-and-old-key}

Si recibes este error, asegúrate de que el usuario esté usando la clave pública actual tal como se muestra en tu panel de Braze.
{% endtab %}

{% tab Redshift %}
### Probar conexión se ejecuta lentamente

Probar conexión se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. Usar una instancia SQL serverless minimizará el tiempo de arranque y mejorará el rendimiento de las consultas, pero puede resultar en costes de integración ligeramente más altos.

### Permission denied for relation {table_name} {#permission-denied-for-relation-table_name}

Si recibes este error:

  - Concede el permiso `usage` en el esquema para ese usuario.
  - Concede el permiso `select` en la tabla para ese usuario.

### Create Connection Error {#create-connection-error}

Si recibes este error, verifica que el endpoint y el puerto de Redshift sean correctos.

### Create SSH Tunnel Error {#create-ssh-tunnel-error}

Si recibes este error:

  - Verifica que la clave pública en tu panel de Braze esté en el host ec2 utilizado para el túnel SSH.
  - Verifica que tu nombre de usuario sea correcto.
  - Verifica que el túnel SSH sea correcto.
{% endtab %}

{% tab BigQuery %}
### Probar conexión se ejecuta lentamente

Probar conexión se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. Usar una instancia SQL serverless minimizará el tiempo de arranque y mejorará el rendimiento de las consultas, pero puede resultar en costes de integración ligeramente más altos.

### User does not have permission to query table {#user-does-not-have-permission-to-query-table}

Si recibes este error, añade permisos de usuario para consultar la tabla.

### Your usage exceeded the custom quota {#your-usage-exceeded-the-custom-quota}

Si recibes este error, tu cuota necesita actualizarse para que puedas seguir sincronizando a tu tasa actual.

### Table was not found in location {region} Location {#table-was-not-found-in-location-region-location}

Si recibes este error, verifica que tu tabla esté en el proyecto y el conjunto de datos correctos.

### Invalid JWT Signature {#invalid-jwt-signature}

Si recibes este error, comprueba que el servicio de API de BigQuery esté habilitado para tu cuenta.
{% endtab %}

{% tab Databricks %}
### Probar conexión se ejecuta lentamente

Probar conexión se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. Para Databricks, puede haber de dos a cinco minutos de tiempo de arranque cuando Braze se conecta a instancias SQL Classic y Pro, lo que generará retrasos durante la configuración y prueba de la conexión, así como al inicio de las sincronizaciones programadas. Usar una instancia SQL serverless minimizará el tiempo de arranque y mejorará el rendimiento de las consultas, pero puede resultar en costes de integración ligeramente más altos.

### Command failed because warehouse was stopped {#command-failed-because-warehouse-was-stopped}

Si recibes este error, asegúrate de que el almacén de Databricks esté en ejecución.

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden

Si recibes este error, consulta [Databricks: Forbidden error while accessing S3 data](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## ¿Cómo actualizo mis preferencias de alerta por correo electrónico para las integraciones de CDI? {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

Cada integración tiene sus propias preferencias de notificación. Ve a la página de CDI y selecciona el nombre de la integración que deseas actualizar. En la sección **Notification preferences** puedes actualizar cómo recibes alertas sobre la integración seleccionada.

## ¿Por qué aparece el error "Incorrect Integration Object"? {#why-am-i-seeing-an-incorrect-integration-object-error}

Este error ocurre cuando intentas actualizar las preferencias de notificación de una integración CDI y dos o más espacios de trabajo tienen integraciones apuntando al mismo contenedor o carpeta de almacenamiento en el cloud. Cada ubicación de almacenamiento en el cloud solo puede ser utilizada por una integración a la vez.

Para resolverlo:

1. Identifica qué otro espacio de trabajo tiene una integración CDI usando la misma ubicación de almacenamiento.
2. Elimina o reconfigura la integración en conflicto en el otro espacio de trabajo.
3. Después de eliminar el conflicto, podrás actualizar las preferencias de notificación.

El error ya no debería aparecer y deberías poder actualizar tus preferencias de notificación correctamente. Si sigues teniendo problemas, [abre un ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## ¿Qué ocurre si se sincroniza un `UPDATED_AT` futuro con una integración? {#what-happens-if-a-future-updated_at-gets-synced-with-an-integration}

CDI utiliza `UPDATED_AT` para determinar qué datos son nuevos. Después de que se sincroniza un `UPDATED_AT` futuro, cualquier dato anterior a esa fecha y hora futura no se procesará. Para solucionar esto:

1. Corrige `UPDATED_AT`.
2. Elimina cualquier dato antiguo que ya se haya sincronizado con Braze.
3. Crea una nueva integración para procesar esa tabla de nuevo.

## ¿Por qué "Rows Synced" no coincide con el número en mi almacén de datos? {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

CDI utiliza `UPDATED_AT` para decidir qué registros recoger durante una sincronización. Consulta [esta ilustración]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion#how-it-works) para ver cómo funciona. Al inicio de una ejecución de sincronización, CDI consulta tu almacén de datos para obtener todos los registros con `UPDATED_AT` posterior al valor de `UPDATED_AT` previamente procesado. Los registros que se encuentran exactamente en la marca de tiempo límite también pueden volver a sincronizarse si nuevas filas comparten esa marca de tiempo. Cualquier registro recogido en el momento en que se ejecuta la consulta se sincroniza en Braze. Estos son los casos comunes en los que un registro podría no sincronizarse:

- Estás añadiendo registros a la tabla con un valor de `UPDATED_AT` que ya ha sido procesado.
- Estás actualizando valores de registros después de que hayan sido procesados por una sincronización, pero dejando `UPDATED_AT` sin cambios.
- Estás añadiendo o actualizando registros mientras una sincronización está en curso. Dependiendo de cuándo se ejecute la consulta de CDI, podrían existir condiciones de carrera que provoquen que los registros no sean recogidos.

{% alert tip %}
Para evitar estos comportamientos en el futuro, te recomendamos usar valores de `UPDATED_AT` que aumenten de forma monótona y no actualizar la tabla durante la ejecución de sincronización programada.
{% endalert %}

## ¿Necesito valores `UPDATED_AT` mayoritariamente distintos para importaciones CDI grandes? {#do-i-need-mostly-distinct-updated_at-values-for-large-cdi-imports}

Sí. Para ejecuciones de alto volumen (por ejemplo, más de aproximadamente 10 millones de filas), asegúrate de que tus datos de origen tengan valores `UPDATED_AT` mayoritariamente distintos. Si demasiadas filas comparten la misma marca de tiempo, es más probable que CDI vuelva a seleccionar filas en las marcas de tiempo límite en ejecuciones posteriores. Esto puede aumentar las sincronizaciones duplicadas y el consumo de puntos de datos.

Para obtener más información sobre el comportamiento de límite de CDI, consulta [Evitar la resincronización de filas con marcas de tiempo duplicadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps).

### ¿Dónde ejecuto estas comprobaciones SQL? {#where-do-i-run-these-sql-checks}

Ejecuta las comprobaciones directamente en el editor SQL de tu almacén de datos, contra la misma tabla o vista utilizada por tu integración CDI:

- Snowflake: **Projects** > **Worksheets** (para obtener más información, consulta [Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs))
- Redshift: Query Editor v2 (para obtener más información, consulta [Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html))
- BigQuery: BigQuery Studio SQL workspace (para obtener más información, consulta [BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction))
- Databricks: SQL editor (SQL warehouse) (para obtener más información, consulta [Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/))
- Fabric: SQL query editor

Usa este proceso antes de habilitar o escalar una sincronización grande:

1. Identifica la tabla o vista de origen CDI exacta y la ventana de sincronización que deseas validar.
2. Abre el editor SQL de tu almacén de datos y selecciona la misma base de datos y esquema utilizados por CDI, luego usa un rol con acceso de lectura a la tabla o vista de origen.
3. Ejecuta la consulta de conteo de marcas de tiempo distintas para medir cuántos valores `UPDATED_AT` distintos existen en esa ventana.
4. Ejecuta la consulta que agrupa por `UPDATED_AT` y cuenta filas para encontrar marcas de tiempo con conteos de filas inusualmente altos.
5. Si muchas filas comparten marcas de tiempo idénticas, ajusta tu proceso de ingesta para que los lotes consecutivos utilicen valores `UPDATED_AT` progresivamente más recientes, o aumenta la precisión de las marcas de tiempo para que las filas estén más distribuidas.
6. Vuelve a ejecutar ambas consultas hasta que la concentración se reduzca, luego lanza o escala tu sincronización.
7. Después del lanzamiento, monitorea **CDI** > **Sync Log** para detectar volúmenes de resincronización inesperados en las marcas de tiempo límite.

Usa comprobaciones como estas en tu almacén de datos:

```sql
SELECT
  COUNT(*) AS total_rows,
  COUNT(DISTINCT UPDATED_AT) AS distinct_timestamps,
  ROUND(COUNT(*) * 1.0 / NULLIF(COUNT(DISTINCT UPDATED_AT), 0), 2) AS avg_rows_per_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP);
```

```sql
SELECT
  UPDATED_AT,
  COUNT(*) AS rows_at_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP)
GROUP BY UPDATED_AT
ORDER BY rows_at_timestamp DESC
LIMIT 20;
```

Si tu almacén de datos no admite `LIMIT` (por ejemplo, Fabric), usa una sintaxis equivalente como `TOP`.

## ¿Por qué una sincronización de CDI con un número pequeño de filas puede tardar varios minutos? {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

Una sincronización de CDI incluye un periodo de inicio fijo antes de que comience el procesamiento de filas. Dado que este tiempo de inicio es similar independientemente del tamaño de la sincronización, una sincronización pequeña puede tardar varios minutos y parecer más lenta en filas por minuto. El tiempo total de sincronización sigue dependiendo de la complejidad de tu consulta de origen, la forma de los datos y la capacidad disponible en tu almacén de datos. Para más información, consulta [Integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Durante una sincronización, ¿se preserva el orden si varios registros comparten el mismo ID? {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

El orden de procesamiento no es 100 % predecible. Por ejemplo, si hay varias filas con el mismo `EXTERNAL_ID` en la tabla durante una sincronización, no podemos garantizar qué valor terminará en el perfil final. Si estás actualizando el mismo `EXTERNAL_ID` con diferentes atributos en la columna de carga útil, todos los cambios se reflejan cuando se completa la sincronización.

## ¿Por qué no se crean nuevos usuarios a partir de mi sincronización CDI? {#why-are-new-users-not-being-created-from-my-cdi-sync}

Si tu integración CDI tiene habilitada la opción **Update existing users only**, solo se actualizan los usuarios que ya existen en Braze, y no se crean nuevos usuarios. Esto significa que si una fila en tu tabla de sincronización hace referencia a un `EXTERNAL_ID` que no coincide con ningún usuario existente en Braze, esa fila se omite.

Para crear nuevos usuarios a través de CDI, desactiva la opción **Update existing users only** en la configuración de tu integración. Ve a **Data Settings** > **Cloud Data Ingestion** y selecciona una integración.

## ¿Cuáles son las medidas de seguridad para CDI? {#what-are-the-security-measures-for-cdi}

### Nuestras medidas {#our-measures}

Braze tiene las siguientes medidas implementadas para CDI:

- Todas las credenciales están cifradas en nuestra base de datos, y solo determinados empleados tienen acceso autenticado a ellas.
- Utilizamos conexiones cifradas para enviar datos a los almacenes de datos de los clientes.
- Realizamos solicitudes a los endpoints de la API de Braze utilizando las mismas claves de API y conexiones TLS que recomendamos a nuestros clientes.
- Actualizamos periódicamente nuestras bibliotecas y aplicamos los parches de seguridad disponibles.

### Tus medidas {#your-measures}

Te recomendamos que tú y tu equipo configuren las siguientes medidas de seguridad de su lado:

- Restringe el acceso a las credenciales al mínimo necesario para que CDI funcione. Esto se debe a que necesitamos poder ejecutar select (y count) en las tablas y vistas específicas.
- Restringe las IP que pueden acceder a las tablas a las [IP de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views) publicadas oficialmente.