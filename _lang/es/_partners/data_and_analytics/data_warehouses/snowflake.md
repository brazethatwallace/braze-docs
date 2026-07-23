---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Este artículo describe la asociación entre Braze y Snowflake, cubriendo tanto el uso compartido de datos (de Braze a Snowflake) como la ingesta de datos de Cloud (de Snowflake a Braze)."
page_type: partner
search_tag: Partner

---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) es un almacén de datos SQL en la nube creado específicamente y proporcionado como software como servicio (SaaS). Snowflake proporciona un almacén de datos más rápido, fácil de usar y mucho más flexible que las ofertas tradicionales de almacén de datos. Con la arquitectura única y patentada de Snowflake, es fácil acumular todos tus datos, habilitar análisis rápidos y obtener información basada en datos para todos tus usuarios.

Braze ofrece dos integraciones con Snowflake. Juntas, proporcionan un pipeline de datos bidireccional completo entre tus entornos de Braze y Snowflake.

## Elegir una integración {#choosing-an-integration}

### Uso compartido de datos (de Braze a Snowflake) {#data-sharing-braze-to-snowflake}

[Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing) de Snowflake te da acceso seguro y en tiempo real a los datos de interacción y Campaign de Braze directamente en tu instancia de Snowflake. No se copian ni transfieren datos entre cuentas: toda la compartición se realiza a través de la capa de servicios y el almacén de metadatos únicos de Snowflake.

**Usa el uso compartido de datos cuando quieras:**
- Consultar datos de eventos y Campaign de Braze usando SQL de Snowflake
- Crear informes complejos y realizar modelos de atribución
- Unir datos de Braze con otros datos en tu almacén de Snowflake
- Comparar tus datos de interacción entre canales, sectores y plataformas de dispositivos

Para instrucciones de configuración, consulta [Uso compartido de datos con Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing).

### Ingesta de datos de Cloud (de Snowflake a Braze) {#cloud-data-ingestion-snowflake-to-braze}

La [ingesta de datos de Cloud (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) te permite sincronizar datos desde tu instancia de Snowflake directamente en Braze. Esto te permite mantener los atributos de usuario, eventos y compras en Braze actualizados con tu almacén de datos como fuente de la verdad.

**Usa la ingesta de datos de Cloud cuando quieras:**
- Sincronizar atributos de usuario desde Snowflake a perfiles de usuario de Braze
- Enviar datos de eventos o compras desde Snowflake a Braze
- Mantener Braze sincronizado con las transformaciones de datos que ocurren en tu almacén
- Evitar construir y mantener pipelines ETL personalizados de Snowflake a Braze

Para saber más sobre el uso compartido de datos de Snowflake, consulta [Introducción a Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Requisitos previos {#prerequisites}

Antes de poder utilizar esta característica, tendrás que completar lo siguiente:

| Requisito | Descripción |
| ----------- | ----------- |
| Acceso a Braze | Para acceder a esta característica en Braze, tendrás que ponerte en contacto con tu administrador de cuenta o administrador de éxito de cliente de Braze. |
| Cuenta de Snowflake | Una cuenta de Snowflake con permisos `admin`. Para clientes que no son HIPAA, se admite Snowflake Standard o Enterprise Edition. Para el uso compartido de datos conforme a HIPAA, se requiere Business Critical Edition. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Configuración de la compartición segura de datos {#setting-up-secure-data-sharing}

En Snowflake, los datos se comparten entre un [proveedor de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) y un [consumidor de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). En este contexto, tu cuenta de Braze es el proveedor de datos porque crea y envía el datashare&#8212;mientras que tu cuenta de Snowflake es el consumidor de datos porque utiliza el datashare para crear una base de datos. Para más detalles, consulta [Snowflake: Consumir datos compartidos](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Paso 1: Enviar el datashare desde Braze {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Paso 2: Crear la base de datos en Snowflake {#step-2-create-the-database-in-snowflake}

1. Al cabo de unos minutos, deberías recibir el datashare de entrada en tu cuenta de Snowflake.
2. Utilizando el datashare de entrada, crea una base de datos para ver y consultar las tablas. Por ejemplo:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Concede privilegios para consultar la nueva base de datos.

{% alert warning %}
Si eliminas y vuelves a crear un recurso compartido en el panel de Braze, debes eliminar la base de datos creada anteriormente y volver a crearla utilizando `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` para consultar el recurso compartido de entrada.
Si tienes varios espacios de trabajo que comparten datos con la misma cuenta de Snowflake, consulta las [preguntas frecuentes sobre el uso compartido de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) para obtener orientación sobre la gestión de configuraciones con varios espacios de trabajo.
{% endalert %}

## Uso y visualización {#usage-and-visualization}

Una vez aprovisionado el recurso compartido de datos, tendrás que crear una base de datos a partir del recurso compartido de datos de entrada, para que todas las tablas compartidas aparezcan en tu instancia de Snowflake y puedan consultarse como cualquier otro dato que almacenes en tu instancia. Sin embargo, ten en cuenta que los datos compartidos son de solo lectura y solo pueden consultarse, pero no modificarse ni eliminarse de ninguna manera.

De forma similar a Currents, puedes utilizar tu compartición segura de datos de Snowflake para:

{% multi_lang_include partners/data_sharing_use_cases.md %}

Para obtener una lista completa de las tablas y columnas disponibles, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). El uso compartido de datos de Snowflake incluye todas las tablas de esa referencia, además de tablas exclusivas de Snowflake para instantáneas, registros de cambios de Campaign y Canvas, eventos de la consola de agentes y eventos de reintentos de mensajes.

También puedes [descargar los esquemas de las tablas sin procesar](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) como archivo de texto.

### Esquema de ID de usuario {#user-id-schema}

Ten en cuenta las siguientes diferencias entre las convenciones de nomenclatura de Braze y Snowflake para los ID de usuario.

| Esquema de Braze | Esquema de Snowflake | Descripción |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | El identificador único que asigna automáticamente Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | El identificador único del perfil de un usuario configurado por el cliente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de ID de usuario" }

## Información importante y limitaciones {#important-information-and-limitations}

### Cambios de ruptura frente a cambios sin ruptura {#breaking-versus-non-breaking-changes}

#### Cambios sin ruptura {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Dado que las columnas nuevas se consideran cambios sin ruptura, Braze recomienda encarecidamente enumerar explícitamente las columnas de interés en cada consulta, en lugar de utilizar consultas `SELECT *`. Otra posibilidad es crear vistas que nombren explícitamente las columnas y luego consultar esas vistas en lugar de las tablas directamente.
{% endalert %}

#### Cambios de ruptura {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Regiones de Snowflake {#snowflake-regions}

Braze aloja actualmente todos los datos de usuario en las regiones de Snowflake AWS US East-1, EU-Central (Frankfurt), AP-Northeast-1 (Tokio), AP-Southeast-2 (Sídney) y AP-Southeast-3 (Yakarta). Para los usuarios de fuera de esas regiones, Braze puede proporcionar datos compartidos a clientes conjuntos que alojen su infraestructura de Snowflake en cualquier región de AWS, Azure o GCP.

### Retención de datos {#data-retention}

#### Política de retención {#retention-policy}

Los datos que tengan más de dos años se archivarán y se trasladarán a un almacenamiento a largo plazo. Como parte del proceso de archivo, todos los eventos se anonimizan y se elimina cualquier campo confidencial de información personal identificable (PII) (esto incluye campos PII opcionales como `properties`). Los datos archivados siguen conteniendo el campo `user_id`, que permite el análisis por usuario de todos los datos de eventos.

Podrás consultar los datos de los dos últimos años de cada evento en la vista correspondiente `USERS_*_SHARED`. Además, cada evento tendrá una vista `USERS_*_SHARED_ALL` que puede consultarse para obtener datos tanto anonimizados como no anonimizados.

#### Datos históricos {#historical-data}

El archivo de datos históricos de eventos en Snowflake se remonta a abril de 2019. Durante los primeros meses en los que Braze almacenó datos en Snowflake, se realizaron cambios en el producto que pueden haber provocado que algunos de esos datos tengan un aspecto ligeramente diferente o algunos valores nulos (ya que en ese momento no pasábamos datos a todos los campos disponibles). Es mejor asumir que cualquier resultado que incluya datos anteriores a agosto de 2019 puede ser ligeramente diferente de lo esperado.

### Cumplimiento del Reglamento General de Protección de Datos (RGPD) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Consulta de datos compartidos: `TIME` y rendimiento de consultas {#querying-shared-data-time-and-query-performance}

Los datos de eventos en las vistas de uso compartido de datos (por ejemplo, `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) están **agrupados por el campo `TIME`**. Cuando filtres por **cuándo ocurrió el evento**, usa **`TIME`** como filtro preferido. Las consultas que restringen filas usando **`TIME`** son generalmente **más eficientes** que las consultas que filtran por **`SF_CREATED_AT`**, porque la agrupación se alinea con el momento del evento.

| Campo | Significado |
| ----- | ------- |
| `TIME` | Marca de tiempo unix en la que ocurrió el evento. Usa este campo preferentemente cuando filtres por momento de ocurrencia. |
| `SF_CREATED_AT` | Marca de tiempo en la que la fila se cargó en Snowflake (momento de ingesta). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consulta de datos compartidos: TIME y rendimiento de consultas" }

### Velocidad, rendimiento y coste de las consultas {#speed-performance-cost-of-queries}

La velocidad, el rendimiento y el coste de cualquier consulta realizada sobre los datos vienen determinados por el tamaño del almacén que utilices para consultar los datos. En algunos casos, dependiendo de la cantidad de datos a los que accedas para el análisis, puede que necesites utilizar un almacén de mayor tamaño para que la consulta tenga éxito. Snowflake dispone de excelentes recursos sobre la mejor forma de determinar qué tamaño utilizar, entre los que se incluyen [Resumen de los almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) y [Consideraciones sobre los almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Para consultar un conjunto de consultas de ejemplo como referencia para configurar Snowflake, echa un vistazo a nuestros ejemplos de [consultas de ejemplo]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) y de [configuración del canal de eventos ETL]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup).

Para instrucciones de configuración, consulta [Ingesta de datos de Cloud: integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).