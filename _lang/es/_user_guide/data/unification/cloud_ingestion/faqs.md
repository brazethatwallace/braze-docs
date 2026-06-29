---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la Ingesta de datos de Cloud
page_order: 10
page_type: FAQ
description: "Esta página responde a las preguntas más frecuentes sobre la Ingesta de datos de Cloud."
toc_headers: h2
---

# Preguntas más frecuentes {#frequently-asked-questions}

> Esta página contiene respuestas a algunas preguntas frecuentes sobre la Ingesta de datos de Cloud.

## ¿Por qué me enviaron un correo electrónico: "Error in CDI Sync"? {#why-was-i-emailed-error-in-cdi-sync}

Este tipo de correo electrónico suele significar que hay un problema con tu configuración de CDI. Aquí tienes algunos problemas comunes y cómo solucionarlos:

### CDI no puede acceder al almacén de datos o a la tabla utilizando tus credenciales {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

Esto podría significar que las credenciales en CDI son incorrectas o están mal configuradas en el almacén de datos. Para más información, consulta [Integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

### No se encuentra la tabla {#the-table-cannot-be-found}

Intenta actualizar tu integración con la configuración correcta de la base de datos o crea recursos coincidentes en el almacén de datos, como `database/table`.

### No se encuentra el catálogo {#the-catalog-cannot-be-found}

El catálogo configurado en la integración no existe en el catálogo de Braze. Se puede eliminar un catálogo después de configurar la integración. Para resolver el problema, actualiza la integración para utilizar un catálogo diferente o crea un catálogo nuevo que coincida con el nombre del catálogo en la integración.

## ¿Por qué me enviaron un correo electrónico: "Row errors in your CDI sync"? {#why-was-i-emailed-row-errors-in-your-cdi-sync}

Este tipo de correo significa que algunos de tus datos no pudieron ser procesados durante la sincronización. Para averiguar el error concreto, puedes revisar los registros en Braze yendo a **CDI** > **Sync Log**.

## ¿Cómo corrijo los errores de Test Connection y de los correos electrónicos de asistencia? {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### La conexión de prueba va lenta {#test-connection-runs-slow}

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.

### Error al conectar con la instancia de Snowflake: la solicitud entrante con IP no tiene autorización para acceder a Snowflake {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

Intenta añadir las IP oficiales de Braze a tu lista de IP permitidas. Para obtener más información, consulta [Integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/) o permite las direcciones IP pertinentes:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Error al ejecutar SQL debido a la configuración del cliente: 002003 (42S02): error de compilación SQL: no existe o no está autorizado {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

Si la tabla no existe, créala. Si la tabla existe, comprueba que el usuario y el rol tienen permisos para leer la tabla.

### No se ha podido utilizar el esquema {#could-not-use-schema}

Si recibes este error, concede acceso a ese esquema para el usuario o rol especificado.

### No se ha podido utilizar el rol {#could-not-use-role}

Si recibes este error, permite que ese usuario utilice el rol especificado.

### Acceso de usuario desactivado {#user-access-disabled}

Si recibes este error, permite a ese usuario el acceso a tu cuenta de Snowflake.

### Error al conectarse a la instancia de Snowflake con la clave actual y la antigua {#error-connecting-to-snowflake-instance-with-current-and-old-key}

Si recibes este error, asegúrate de que el usuario está utilizando la clave pública actual que se muestra en tu panel de Braze.
{% endtab %}

{% tab Redshift %}
### La conexión de prueba va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.

### Permiso denegado para la relación {table_name} {#permission-denied-for-relation-tablename}

Si recibes este error:

  - Concede el permiso `usage` en el esquema para ese usuario.
  - Concede el permiso `select` en la tabla para ese usuario.

### Error al crear conexión {#create-connection-error}

Si recibes este error, comprueba que el punto de conexión y el puerto de Redshift son correctos.

### Error al crear túnel SSH {#create-ssh-tunnel-error}

Si recibes este error:

  - Comprueba que la clave pública de tu panel de Braze está en el host ec2 utilizado para el túnel SSH.
  - Comprueba que tu nombre de usuario es correcto.
  - Comprueba que el túnel SSH es correcto.
{% endtab %}

{% tab BigQuery %}
### La conexión de prueba va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.

### El usuario no tiene permiso para consultar la tabla {#user-does-not-have-permission-to-query-table}

Si recibes este error, añade permisos de usuario para consultar la tabla.

### Tu uso ha superado la cuota personalizada {#your-usage-exceeded-the-custom-quota}

Si recibes este error, es necesario actualizar tu cuota para que puedas seguir sincronizando al ritmo actual.

### No se ha encontrado la tabla en la ubicación {region} {#table-was-not-found-in-location-region-location}

Si recibes este error, comprueba que la tabla se encuentra en el proyecto y el conjunto de datos correctos.

### Firma JWT no válida {#invalid-jwt-signature}

Si recibes este error, comprueba que el servicio de API de BigQuery está habilitado para tu cuenta.
{% endtab %}

{% tab Databricks %}
### La conexión de prueba va lenta

Test Connection se ejecuta en tu almacén de datos, por lo que aumentar la capacidad del almacén puede mejorar su velocidad. En el caso de Databricks, puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecta a instancias Classic y Pro SQL, lo que provocará retrasos durante la configuración y las pruebas de conexión, así como al inicio de las sincronizaciones programadas. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.

### El comando ha fallado porque el almacén estaba detenido {#command-failed-because-warehouse-was-stopped}

Si recibes este error, asegúrate de que el almacén de Databricks está en ejecución.

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden {#service-amazon-s3-status-code-403-error-code-403-forbidden}

Si recibes este error, consulta [Databricks: Forbidden error while accessing S3 data](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## ¿Cómo actualizo mis preferencias de alertas por correo electrónico para las integraciones CDI? {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

Cada integración tiene sus propias preferencias de notificación. Ve a la página CDI y selecciona el nombre de la integración que deseas actualizar. En la sección **Notification preferences** puedes actualizar cómo recibes las alertas relativas a la integración seleccionada.

## ¿Qué sucede si un `UPDATED_AT` futuro se sincroniza con una integración? {#what-happens-if-a-future-updatedat-gets-synced-with-an-integration}

CDI utiliza `UPDATED_AT` para decidir qué datos son nuevos. Después de sincronizar un `UPDATED_AT` futuro, no se procesarán los datos anteriores a esa fecha y hora futuras. Para solucionarlo:

1. Corrige `UPDATED_AT`.
2. Elimina los datos antiguos que ya estén sincronizados con Braze.
3. Crea una nueva integración para procesar de nuevo esa tabla.

## ¿Por qué "Rows Synced" no coincide con el número de mi almacén? {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

CDI utiliza `UPDATED_AT` para decidir qué registros recoger durante una sincronización. Mira [esta ilustración]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/#what-gets-synced) para ver cómo funciona. Al inicio de una sincronización, CDI realiza una consulta en tu almacén para obtener todos los registros con `UPDATED_AT` posterior al valor `UPDATED_AT` procesado anteriormente. Los registros que se encuentren exactamente en la marca de tiempo límite también pueden volver a sincronizarse si nuevas filas comparten esa marca de tiempo. Cualquier registro recogido en el momento en que se ejecuta la consulta se sincroniza en Braze. Estos son los casos habituales en los que un registro puede no sincronizarse:

- Estás añadiendo registros a la tabla con un valor `UPDATED_AT` que ya ha sido procesado.
- Estás actualizando los valores de los registros después de que hayan sido procesados por una sincronización, pero dejando `UPDATED_AT` sin cambios.
- Estás añadiendo o actualizando registros mientras se realiza una sincronización. Dependiendo del momento en que se ejecute la consulta CDI, puede haber condiciones de carrera que provoquen que no se recojan los registros.

{% alert tip %}
Para evitar estos comportamientos en el futuro, recomendamos utilizar valores `UPDATED_AT` que aumenten monotónicamente y no actualizar la tabla durante la ejecución de la sincronización programada.
{% endalert %}

## ¿Necesito valores `UPDATED_AT` mayoritariamente distintos para importaciones CDI grandes? {#do-i-need-mostly-distinct-updatedat-values-for-large-cdi-imports}

Sí. Para ejecuciones de gran volumen (por ejemplo, más de aproximadamente 10 millones de filas), asegúrate de que tus datos de origen tengan valores `UPDATED_AT` mayoritariamente distintos. Si demasiadas filas comparten la misma marca de tiempo, es más probable que CDI vuelva a seleccionar filas en las marcas de tiempo límite en ejecuciones posteriores. Esto puede aumentar las sincronizaciones duplicadas y el consumo de puntos de datos.

Para más información sobre el comportamiento de CDI en los límites, consulta [Evitar la resincronización de filas con marcas de tiempo duplicadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices/#avoid-resyncing-rows-with-duplicate-timestamps).

### ¿Dónde ejecuto estas comprobaciones SQL? {#where-do-i-run-these-sql-checks}

Ejecuta las comprobaciones directamente en el editor SQL de tu almacén de datos, contra la misma tabla o vista utilizada por tu integración CDI:

- Snowflake: **Projects** > **Worksheets** (para más información, consulta [Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs))
- Redshift: Query Editor v2 (para más información, consulta [Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html))
- BigQuery: BigQuery Studio SQL workspace (para más información, consulta [BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction))
- Databricks: SQL editor (SQL warehouse) (para más información, consulta [Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/))
- Fabric: SQL query editor

Sigue este proceso antes de habilitar o escalar una sincronización grande:

1. Identifica la tabla o vista de origen CDI exacta y la ventana de sincronización que deseas validar.
2. Abre el editor SQL de tu almacén y selecciona la misma base de datos y esquema utilizados por CDI, luego usa un rol con acceso de lectura a la tabla o vista de origen.
3. Ejecuta la consulta de recuento de marcas de tiempo distintas para medir cuántos valores `UPDATED_AT` distintos existen en esa ventana.
4. Ejecuta la consulta que agrupa por `UPDATED_AT` y cuenta filas para encontrar marcas de tiempo con recuentos de filas inusualmente altos.
5. Si muchas filas comparten marcas de tiempo idénticas, ajusta tu proceso de ingesta para que los lotes consecutivos utilicen valores `UPDATED_AT` progresivamente más recientes, o aumenta la precisión de las marcas de tiempo para que las filas estén más distribuidas.
6. Vuelve a ejecutar ambas consultas hasta que la concentración se reduzca, luego lanza o escala tu sincronización.
7. Después del lanzamiento, monitoriza **CDI** > **Sync Log** para detectar un volumen de resincronización inesperado en las marcas de tiempo límite.

Usa comprobaciones como estas en tu almacén:

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

Si tu almacén no admite `LIMIT` (por ejemplo, Fabric), usa una sintaxis equivalente como `TOP`.

## ¿Por qué una sincronización CDI con un número pequeño de filas puede tardar varios minutos? {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

Una sincronización CDI incluye un periodo de inicio fijo antes de que comience el procesamiento de filas. Dado que este tiempo de inicio es similar independientemente del tamaño de la sincronización, una sincronización pequeña puede tardar varios minutos y parecer más lenta en filas por minuto. El tiempo total de sincronización sigue dependiendo de la complejidad de la consulta de origen, la forma de los datos y la capacidad disponible en tu almacén de datos. Para más información, consulta [Integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

## Durante una sincronización, ¿se mantiene el orden si varios registros comparten el mismo ID? {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

El orden de procesamiento no es 100 % predecible. Por ejemplo, si hay varias filas con el mismo `EXTERNAL_ID` en la tabla durante una sincronización, no podemos garantizar qué valor acabará en el perfil final. Si actualizas el mismo `EXTERNAL_ID` con diferentes atributos en la columna de carga útil, todos los cambios se reflejarán cuando se complete la sincronización.

## ¿Por qué no se crean nuevos usuarios a partir de mi sincronización CDI? {#why-are-new-users-not-being-created-from-my-cdi-sync}

Si tu integración CDI tiene habilitada la opción **Update existing users only**, solo se actualizarán los usuarios que ya existen en Braze y no se crearán nuevos usuarios. Esto significa que si una fila de tu tabla de sincronización hace referencia a un `EXTERNAL_ID` que no coincide con ningún usuario existente de Braze, esa fila se omite.

Para crear nuevos usuarios a través de CDI, desactiva la opción **Update existing users only** en la configuración de la integración. Ve a **Data Settings** > **Cloud Data Ingestion** y selecciona una integración.

## ¿Cuáles son las medidas de seguridad de CDI? {#what-are-the-security-measures-for-cdi}

### Nuestras medidas {#our-measures}

Braze cuenta con las siguientes medidas para CDI:

- Todas las credenciales están cifradas dentro de nuestra base de datos, y solo determinados empleados tienen acceso autenticado a ellas.
- Utilizamos conexiones cifradas para obtener los datos de los almacenes de los clientes.
- Realizamos solicitudes a los puntos finales de la API de Braze utilizando las mismas claves de API y conexiones TLS que recomendamos utilizar a nuestros clientes.
- Actualizamos regularmente nuestras bibliotecas y aplicamos todos los parches de seguridad.

### Tus medidas {#your-measures}

Te recomendamos que tú y tu equipo establezcan las siguientes medidas de seguridad:

- Restringe el acceso a las credenciales al mínimo necesario para el funcionamiento de CDI. Esto se debe a que necesitamos poder ejecutar select (y count) en las tablas y vistas específicas.
- Restringe las IP que pueden acceder a las tablas a las [IP de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) publicadas oficialmente.