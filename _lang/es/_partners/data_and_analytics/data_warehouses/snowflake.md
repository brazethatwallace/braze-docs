---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Este artículo describe la asociación entre Braze y Snowflake, cubriendo tanto el uso compartido de datos (de Braze a Snowflake) como la ingesta de datos en la nube."
page_type: partner
search_tag: Partner
---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) es un almacén de datos SQL en la nube creado específicamente y proporcionado como software como servicio (software como servicio (SaaS)). Snowflake proporciona un almacén de datos más rápido, fácil de usar y mucho más flexible que las ofertas tradicionales de almacén de datos. Con la arquitectura única y patentada de Snowflake, es fácil acumular todos tus datos, habilitar análisis rápidos y obtener información basada en datos para todos tus usuarios.

Braze ofrece dos integraciones con Snowflake. Juntas, proporcionan un pipeline de datos bidireccional completo entre tus entornos de Braze y Snowflake.

## Cómo elegir una integración {#choosing-an-integration}

### Uso compartido de datos (de Braze a Snowflake) {#data-sharing-braze-to-snowflake}

[Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing) de Snowflake te da acceso seguro y en tiempo real a los datos de participación y Campaign de Braze directamente en tu instancia de Snowflake. No se copian ni transfieren datos entre cuentas: todo el uso compartido se realiza a través de la capa de servicios y el almacén de metadatos exclusivos de Snowflake.

**Usa el uso compartido de datos cuando quieras:**
- Consultar datos de eventos y Campaign de Braze usando SQL de Snowflake
- Crear informes complejos y realizar modelos de atribución
- Combinar datos de Braze con otros datos en tu almacén de datos de Snowflake
- Comparar tus datos de participación entre canales, industrias y plataformas de dispositivos

Para obtener instrucciones de configuración, consulta [Uso compartido de datos con Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing).

### Ingesta de datos en la nube (de Snowflake a Braze) {#cloud-data-ingestion-snowflake-to-braze}

La [ingesta de datos en la nube (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) te permite sincronizar datos desde tu instancia de Snowflake directamente en Braze. Esto te permite mantener los atributos de usuario, eventos y compras en Braze actualizados con tu almacén de datos de referencia.

**Usa la ingesta de datos en la nube cuando quieras:**
- Sincronizar atributos de usuario desde Snowflake a perfiles de usuario de Braze
- Enviar datos de eventos o compras desde Snowflake a Braze
- Mantener Braze sincronizado con las transformaciones de datos que ocurren en tu almacén de datos
- Evitar crear y mantener canalizaciones ETL personalizadas de Snowflake a Braze

Para obtener más información sobre el uso compartido de datos de Snowflake, consulta [Introducción a Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Requisitos previos {#prerequisites}

Antes de poder utilizar esta característica, deberás completar lo siguiente:

| Requisito | Descripción |
| ----------- | ----------- |
| Acceso a Braze | Para acceder a esta característica en Braze, deberás contactar a tu administrador de cuenta de Braze o administrador de éxito de cliente. |
| Permisos del espacio de trabajo de Braze | [Ver integraciones de Currents]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para ver el uso compartido de datos. [Editar integraciones de Currents]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para crear, actualizar o eliminar un recurso compartido de datos. |
| Cuenta de Snowflake | Una cuenta de Snowflake con permisos de `admin`. Para clientes que no son HIPAA, se admite Snowflake Standard o Enterprise Edition. Para el uso compartido de datos compatible con HIPAA, se requiere Business Critical Edition. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Configuración de Secure Data Sharing {#setting-up-secure-data-sharing}

Para Snowflake, el uso compartido de datos se produce entre un [proveedor de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) y un [consumidor de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). En este contexto, tu cuenta de Braze es el proveedor de datos porque crea y envía el recurso compartido de datos, mientras que tu cuenta de Snowflake es el consumidor de datos porque utiliza el recurso compartido de datos para crear una base de datos. Para más detalles, consulta [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Paso 1: Envía el recurso compartido de datos desde Braze {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Paso 2: Crea la base de datos en Snowflake {#step-2-create-the-database-in-snowflake}

1. Después de unos minutos, deberías recibir el recurso compartido de datos entrante en tu cuenta de Snowflake.
2. Usando el recurso compartido de datos entrante, crea una base de datos para ver y consultar las tablas. Por ejemplo:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Concede privilegios para consultar la nueva base de datos.

{% alert warning %}
Si eliminas y vuelves a crear un recurso compartido en el panel de Braze, debes eliminar la base de datos creada previamente y volver a crearla usando `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` para consultar el recurso compartido entrante.
Si tienes varios espacios de trabajo compartiendo datos con la misma cuenta de Snowflake, consulta las [preguntas frecuentes sobre el uso compartido de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) para obtener orientación sobre la gestión de configuraciones con varios espacios de trabajo.
{% endalert %}

## Uso y visualización {#usage-and-visualization}

Después de aprovisionar el recurso compartido de datos, tendrás que crear una base de datos a partir del recurso compartido de datos entrante, de manera que todas las tablas compartidas aparezcan en tu instancia de Snowflake y se puedan consultar como cualquier otro dato que almacenes en tu instancia. Sin embargo, ten en cuenta que los datos compartidos son de solo lectura y solo se pueden consultar, pero no modificar ni eliminar de ninguna manera.

De forma similar a Currents, puedes usar Snowflake Secure Data Sharing para:

{% multi_lang_include partners/data_sharing_use_cases.md %}

Para obtener una lista completa de las tablas y columnas disponibles, consulta la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Snowflake Data Sharing incluye todas las tablas de esa referencia, además de tablas exclusivas de Snowflake adicionales para instantáneas, registros de cambios de Campaign y Canvas, eventos de la consola de agentes y eventos de reintento de mensajes.

También puedes [descargar los esquemas de tablas sin procesar](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) como archivo de texto.

### Esquema de ID de usuario {#user-id-schema}

Ten en cuenta las siguientes diferencias entre las convenciones de nomenclatura de Braze y Snowflake para los ID de usuario.

| Esquema de Braze | Esquema de Snowflake | Descripción |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | El identificador único que Braze asigna automáticamente. |
| `external_id` | `"EXTERNAL_USER_ID"` | El identificador único del perfil de un usuario que establece el cliente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de ID de usuario" }

## Información importante y limitaciones {#important-information-and-limitations}

### Cambios con ruptura frente a cambios sin ruptura {#breaking-versus-non-breaking-changes}

#### Cambios sin ruptura {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Dado que las columnas nuevas se consideran cambios sin ruptura, Braze recomienda encarecidamente enumerar explícitamente las columnas de interés en cada consulta en lugar de usar consultas `SELECT *`. Alternativamente, puedes crear vistas que nombren explícitamente las columnas y luego consultar esas vistas en lugar de las tablas directamente.
{% endalert %}

#### Cambios con ruptura {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Regiones de Snowflake {#snowflake-regions}

Actualmente, Braze aloja todos los datos a nivel de usuario en las regiones de Snowflake AWS US East-1, EU-Central (Fráncfort), AP-Northeast-1 (Tokio), AP-Southeast-2 (Sídney) y AP-Southeast-3 (Yakarta). Para los usuarios fuera de esas regiones, Braze puede proporcionar uso compartido de datos a clientes conjuntos que alojen su infraestructura de Snowflake en cualquier región de AWS, Azure o GCP.

### Retención de datos {#data-retention}

#### Política de retención {#retention-policy}

Cualquier dato con más de dos años de antigüedad se archivará y se trasladará a almacenamiento a largo plazo. Como parte del proceso de archivado, todos los eventos se anonimizan y los campos sensibles de información de identificación personal (PII) se eliminan (esto incluye campos opcionalmente PII como `properties`). Los datos archivados siguen conteniendo el campo `user_id`, lo que permite análisis por usuario en todos los datos de eventos.

Podrás consultar los dos años más recientes de datos para cada evento en la vista `USERS_*_SHARED` correspondiente. Además, cada evento tendrá una vista `USERS_*_SHARED_ALL` que se puede consultar para devolver tanto datos anonimizados como no anonimizados.

#### Datos históricos {#historical-data}

El archivo de datos históricos de eventos en Snowflake se remonta a abril de 2019. En los primeros meses en que Braze almacenó datos en Snowflake, se realizaron cambios en el producto que pueden haber provocado que algunos de esos datos se vean ligeramente diferentes o tengan algunos valores nulos (ya que no estábamos pasando datos a todos los campos disponibles en ese momento). Es mejor asumir que cualquier resultado que incluya datos anteriores a agosto de 2019 puede verse ligeramente diferente de lo esperado.

### Cumplimiento del Reglamento General de Protección de Datos (RGPD) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Consulta de datos compartidos: `TIME` y rendimiento de consultas {#querying-shared-data-time-and-query-performance}

Los datos de eventos en las vistas de uso compartido de datos (por ejemplo, `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) están **agrupados por el campo `TIME`**. Cuando filtres por **cuándo ocurrió el evento**, usa **`TIME`** como filtro preferido. Las consultas que restringen filas usando **`TIME`** son generalmente **más eficientes** que las consultas que filtran por **`SF_CREATED_AT`**, porque la agrupación se alinea con el momento del evento.

| Campo | Significado |
| ----- | ----------- |
| `TIME` | Marca de tiempo Unix en la que ocurrió el evento. Se prefiere este campo para filtrar por momento de ocurrencia. |
| `SF_CREATED_AT` | Marca de tiempo en la que la fila se cargó en Snowflake (momento de ingesta). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consulta de datos compartidos: TIME y rendimiento de consultas" }

### Velocidad, rendimiento y coste de las consultas {#speed-performance-cost-of-queries}

La velocidad, el rendimiento y el coste de cualquier consulta ejecutada sobre los datos están determinados por el tamaño del almacén que uses para consultar los datos. En algunos casos, dependiendo de la cantidad de datos a los que accedas para tus análisis, puede que necesites usar un almacén de mayor tamaño para que la consulta se ejecute correctamente. Snowflake tiene excelentes recursos disponibles sobre cómo determinar mejor qué tamaño usar, incluyendo [Descripción general de los almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) y [Consideraciones sobre los almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Para un conjunto de consultas de ejemplo que puedes usar como referencia al configurar Snowflake, consulta nuestros ejemplos de [consultas de muestra]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) y de [configuración del canal de eventos ETL]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup).

Para obtener instrucciones de configuración, consulta [Ingesta de datos en la nube: integraciones de almacenes de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).