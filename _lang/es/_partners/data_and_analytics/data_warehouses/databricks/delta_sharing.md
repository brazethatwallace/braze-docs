---
nav_title: "Delta Sharing"
article_title: Databricks Delta Sharing
page_order: 0
description: "Este artículo de referencia cubre Databricks Delta Sharing con Braze (beta cerrada), que te permite acceder a los datos de participación y Campaign de Braze en tu cuenta de Databricks."
page_type: partner
search_tag: Partner
permalink: /delta_sharing/
hidden: true
---

# Databricks Delta Sharing

> Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html) te permite compartir de forma segura datos en vivo de participación y Campaign de Braze en tu entorno de Databricks. Este artículo describe cómo funciona el uso compartido desde Braze como proveedor de datos hacia tu cuenta de Databricks como destinatario, y cómo consultar las tablas compartidas.

{% alert important %}
Databricks Delta Sharing con Braze está en **beta cerrada**. La disponibilidad, las regiones compatibles y el comportamiento del producto pueden cambiar. Ponte en contacto con tu CSM de Braze para participar o para confirmar si esta característica está habilitada para tu espacio de trabajo.
{% endalert %}

Databricks Delta Sharing forma parte de Braze Data Distribution. Para un resumen completo de las opciones de Data Distribution, consulta [Data Distribution]({{site.baseurl}}/user_guide/data/distribution).

## Configurar Delta Sharing {#set-up-delta-sharing}

Para Databricks, el uso compartido de datos ocurre entre un proveedor de datos y un destinatario de datos. Tu cuenta de Braze es el **proveedor de datos** porque crea y envía el recurso compartido, y tu cuenta de Databricks es el **destinatario de datos** porque consume el recurso compartido para crear un catálogo que puedes consultar. Para más detalles, consulta la documentación de Databricks sobre [lectura de datos compartidos mediante Databricks-to-Databricks Delta Sharing (para destinatarios)](https://docs.databricks.com/en/delta-sharing/read-data-databricks.html).

### Paso 1: Configurar el uso compartido desde Braze {#step-1-configure-sharing-from-braze}

1. En Braze, ve a **Integraciones de socios** > **Uso compartido de datos** > **Databricks Delta Sharing**.
2. Introduce tu identificador de uso compartido de Databricks.
3. Cuando hayas terminado, selecciona **Create Datashare**. Braze envía el recurso compartido a tu cuenta de Databricks.

### Paso 2: Crear un catálogo en Databricks {#step-2-create-a-catalog-in-databricks}

1. Después de unos minutos, deberías recibir el recurso compartido de entrada en tu cuenta de Databricks.
2. Usando el recurso compartido de entrada, crea un catálogo para ver y consultar las tablas. Por ejemplo:
    {% raw %}
    ```sql
    CREATE CATALOG [IF NOT EXISTS] <catalog-name> USING SHARE braze.<share-name>;
    ```
    {% endraw %}
3. Otorga privilegios para que los usuarios y grupos adecuados puedan consultar el nuevo catálogo.

{% alert warning %}
Los datos compartidos son de solo lectura en tu espacio de trabajo de Databricks. Puedes consultarlos como cualquier otro dato, pero no puedes modificar ni eliminar filas en las tablas compartidas a través del recurso compartido.
{% endalert %}

## Uso y visualización {#usage-and-visualization}

Una vez que el recurso compartido de datos esté aprovisionado, crea un catálogo a partir del recurso compartido entrante para que las tablas compartidas aparezcan en tu espacio de trabajo de Databricks y se puedan consultar como cualquier otro dato que almacenes allí. Los datos compartidos permanecen como solo lectura.

De forma similar a Currents, puedes usar Databricks Delta Sharing para:

{% multi_lang_include partners/data_sharing_use_cases.md %}

Para obtener una lista completa de tablas y columnas disponibles en Databricks, [descarga los esquemas de tablas sin procesar de Databricks](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt) como archivo de texto. Este archivo refleja el esquema de Databricks Delta Sharing (por ejemplo, `DB_CREATED_AT` para el tiempo de ingesta). No es intercambiable con los [esquemas de tablas sin procesar de Snowflake](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) ni con la [referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables), que describen la nomenclatura y los campos de Snowflake.

{% alert note %}
Durante la beta cerrada, es posible que no todas las tablas listadas en el archivo de esquema de Databricks estén disponibles en tu recurso compartido. Los nombres y tipos de columnas también pueden diferir de Snowflake Data Sharing (por ejemplo, `DB_CREATED_AT` en lugar de `SF_CREATED_AT`). Ponte en contacto con tu CSM de Braze si necesitas la lista actual de tablas para tu espacio de trabajo.
{% endalert %}

### Esquema de ID de usuario {#user-id-schema}

Ten en cuenta las siguientes diferencias entre las convenciones de nomenclatura de Braze y Databricks para los ID de usuario.

| Esquema de Braze | Esquema de Databricks | Descripción |
| ----------- | ----------- | ----------- |
| `braze_id` | `USER_ID` | El identificador único que Braze asigna automáticamente. |
| `external_id` | `EXTERNAL_USER_ID` | El identificador único del perfil de un usuario que tú configuras en Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de ID de usuario" }

## Información importante y limitaciones {#important-information-and-limitations}

### Disponibilidad de la beta cerrada {#closed-beta-availability}

Durante la beta cerrada, es posible que tu recurso compartido no incluya todas las tablas del archivo de [esquemas de tablas sin procesar de Databricks](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt). Los datos compartidos también pueden diferir de Snowflake Data Sharing en nombres y tipos de columnas. Por ejemplo, los recursos compartidos de Databricks usan `DB_CREATED_AT` para el tiempo de ingesta, mientras que los recursos compartidos de Snowflake usan `SF_CREATED_AT`.

### Cambios con ruptura frente a cambios sin ruptura {#breaking-versus-non-breaking-changes}

#### Cambios sin ruptura {#non-breaking-changes}

Los cambios sin ruptura pueden ocurrir en cualquier momento y generalmente proporcionan funcionalidad adicional. Ejemplos de cambios sin ruptura:

- Agregar una nueva tabla o vista
- Agregar una columna a una tabla o vista existente

{% alert important %}
Dado que las nuevas columnas se consideran cambios sin ruptura, Braze recomienda encarecidamente listar explícitamente las columnas de interés en cada consulta en lugar de usar consultas `SELECT *`. Alternativamente, crea vistas que nombren explícitamente las columnas y consulta esas vistas en lugar de consultar las tablas compartidas directamente.
{% endalert %}

#### Cambios con ruptura {#breaking-changes}

Cuando es posible, los cambios con ruptura van precedidos de un anuncio y un período de migración. Ejemplos de cambios con ruptura incluyen:

- Eliminar una tabla o vista
- Eliminar una columna de una tabla o vista existente
- Cambiar el tipo o la nulabilidad de una columna existente

### Regiones de Databricks {#databricks-regions}

Durante la beta cerrada, los proveedores de nube y las regiones compatibles pueden variar según el espacio de trabajo y el despliegue. Ponte en contacto con tu CSM de Braze para conocer las opciones que aplican a tu cuenta.

### Política de retención {#retention-policy}

Durante la beta cerrada, el relleno histórico más allá de la ventana de retención estándar puede estar limitado.

Puedes consultar los datos más recientes de dos años para cada evento en la vista `USERS_*_SHARED` correspondiente.

### Cumplimiento del Reglamento General de Protección de Datos (RGPD) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Consulta de datos compartidos: `TIME` y rendimiento de consultas {#querying-shared-data-time-and-query-performance}

Los datos de eventos en las vistas de uso compartido de datos (por ejemplo, `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) están agrupados en el campo `TIME`. Cuando filtres por el momento en que ocurrió el evento, usa `TIME` como filtro preferido. Las consultas que restringen filas usando `TIME` generalmente tienen mejor rendimiento que las consultas que filtran por `DB_CREATED_AT`, porque la agrupación se alinea con el tiempo del evento.

| Campo | Significado |
| ----- | ------- |
| `TIME` | Marca de tiempo unix en la que ocurrió el evento. Prefiere este campo al filtrar por tiempo de ocurrencia. |
| `DB_CREATED_AT` | Marca de tiempo en la que la fila se cargó en Databricks (tiempo de ingesta). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consulta de datos compartidos: TIME y rendimiento de consultas" }

### Velocidad, rendimiento y costo de las consultas {#speed-performance-and-cost-of-queries}

La velocidad, el rendimiento y el costo de cualquier consulta que ejecutes sobre los datos dependen del tamaño del almacén SQL que utilices. Dependiendo de la cantidad de datos a los que accedas, es posible que necesites un almacén más grande para que la consulta se complete correctamente. Para más información, consulta la documentación de Databricks sobre [creación y configuración de un almacén SQL](https://docs.databricks.com/en/compute/sql-warehouse/create.html) (incluyendo tamaño del clúster y escalado).