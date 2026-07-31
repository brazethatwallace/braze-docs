---
nav_title: Editor SQL
article_title: "Ingesta de datos de Cloud: editor SQL"
description: "Aprende a crear y validar sincronizaciones de Ingesta de datos de Cloud con consultas SQL."
page_order: 11
page_type: reference
toc_headers: h2
---

# Ingesta de datos de Cloud: editor SQL {#cloud-data-ingestion-sql-editor}

> Esta página explica cómo usar el editor SQL de Ingesta de datos de Cloud (CDI) de Braze para crear y validar sincronizaciones con consultas SQL.

El editor SQL de Ingesta de datos de Cloud te permite crear sincronizaciones escribiendo consultas SQL directamente contra tu almacén de datos. Esto elimina la necesidad de crear o mantener una tabla CDI dedicada, que antes era obligatoria en el [Paso 1.1 de integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

Usa el editor SQL cuando quieras:

- Sincronizar datos sin modificar las tablas de origen
- Trabajar con datos sin procesar en tu almacén
- Evitar construir una columna `PAYLOAD`
- Manejar casos de uso de datos más complejos con SQL

## Requisitos previos y limitaciones {#prerequisites-and-limitations}

El editor SQL tiene las siguientes limitaciones:

- Disponible solo para orígenes de almacén de datos: Snowflake, Redshift, BigQuery, Databricks y Fabric.
- Solo se admiten consultas de una sola sentencia y de solo lectura.

{% alert note %}
Braze solo ejecuta consultas de solo lectura contra tus datos y no modifica tus tablas subyacentes. Es posible que se creen objetos temporales durante la ejecución de la consulta, pero no se conservan de forma permanente.
{% endalert %}

## Crear una nueva sincronización con SQL Editor {#create-a-new-sql-editor-sync}

Sigue estos pasos para crear primero un origen y luego una sincronización con SQL Editor. Si ya configuraste un origen para CDI, puedes pasar directamente al paso 3.

{% alert note %}
Ten en cuenta que estos pasos usan un origen de Snowflake como ejemplo. El proceso de configuración para otros orígenes de almacén de datos es similar y se puede encontrar en [Paso 2: Crear un nuevo origen en el panel de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-2-create-a-new-source-in-the-braze-dashboard) de la documentación [Configuración de integraciones de almacén de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations).
{% endalert %}

### Paso 1: Configura tu rol, permisos, almacén y usuario de Snowflake {#step-1-set-up-your-snowflake-role-permissions-warehouse-and-user}

Antes de crear tu origen de Snowflake en CDI, asegúrate de que el usuario de Snowflake que usa Braze tenga acceso a los datos que deseas consultar y un almacén para ejecutar consultas.

#### Paso 1.1: (Opcional) Crea una base de datos y un esquema {#step-11-optional-create-a-database-and-schema}

Si es necesario, crea una base de datos y un esquema dedicados para tus datos de CDI:

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```

#### Paso 1.2: Configura el rol y los permisos de la base de datos {#step-12-set-up-role-and-database-permissions}

Otorga acceso a las tablas que deseas sincronizar:

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.MY_USER_TABLE TO ROLE BRAZE_INGESTION_ROLE;
```

También puedes otorgar acceso a múltiples tablas o tablas futuras, según tu caso de uso. Por ejemplo, para otorgar acceso a todas las tablas futuras en un esquema:

```sql
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
```

#### Paso 1.3: Configura el almacén y otorga acceso al rol de Braze {#step-13-set-up-the-warehouse-and-grant-access-to-the-braze-role}

Crea un almacén para que Braze ejecute consultas:

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
El almacén debe tener activada la opción de reanudación automática. Si no la tiene, otorga a Braze privilegios adicionales de `OPERATE` sobre el almacén para que Braze pueda activarlo cuando se ejecute la consulta.
{% endalert %}

#### Paso 1.4: Crea un usuario de Snowflake {#step-14-create-a-snowflake-user}

Crea un usuario para Braze y asigna el rol:

```sql
CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Usarás este usuario cuando configures tu origen de Snowflake en Braze.

### Paso 2: Crea un nuevo origen en el panel de Braze {#step-2-create-a-new-source-in-the-braze-dashboard}

En este paso, crea tu origen de Snowflake en Braze y valida la conexión.

#### Paso 2.1: Agrega un origen de Snowflake {#step-21-add-a-snowflake-source}

1. En el panel de Braze, ve a **Data Settings** > **Cloud Data Ingestion** > **Sources**.
2. Selecciona **Add data source**.
3. Selecciona **Snowflake**.

#### Paso 2.2: Ingresa los detalles de conexión {#step-22-enter-connection-details}

Elige un nombre para tu origen e ingresa tus credenciales y configuración de Snowflake.

{% alert note %}
Para el campo **Snowflake Account Locator**, ingresa tu [identificador de cuenta](https://docs.snowflake.com/en/user-guide/admin-account-identifier) de Snowflake, que normalmente sigue un formato como `xy12345.us-east-1.aws`. No es lo mismo que un nombre de base de datos o un nombre de almacén.
{% endalert %}

#### Paso 2.3: Completa la configuración de la clave RSA {#step-23-complete-rsa-key-setup}

Después de ingresar tus credenciales y configuración, selecciona **Save credentials** y genera una clave RSA. Luego regresa a Snowflake para completar la configuración. Agrega la clave pública que se muestra en el panel al usuario que creaste para que Braze se conecte a Snowflake.

Para obtener información adicional, consulta [Autenticación con par de claves de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth). Si deseas rotar las claves en algún momento, Braze puede generar un nuevo par de claves y proporcionar la nueva clave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```

De vuelta en Braze, selecciona **Test connection** para verificar el acceso al origen y luego crea el origen.

### Paso 3: Crea una nueva sincronización y escribe tu consulta SQL {#step-3-create-a-new-sync-and-write-your-sql-query}

1. Ve a **Data Settings** > **Cloud Data Ingestion** > **Syncs**.
2. Selecciona **Create data sync**.
3. Elige cualquier sincronización en **Data Type**.
4. Haz referencia al origen del paso 2.
5. Selecciona **SQL** y escribe una consulta SQL que devuelva datos de usuario desde tu almacén. Tu consulta SQL define los datos que se sincronizan con Braze. El resultado de la consulta se convierte en el esquema de tu sincronización.

Puedes usar el explorador de orígenes para buscar tablas y vistas disponibles desde las cuales sincronizar, o el generador de SQL con IA para obtener ayuda de Braze Operator con tu consulta SQL.

{% alert note %}
Solo se admiten consultas de solo lectura, incluidas las cláusulas `JOIN`. Para más detalles, consulta [Restricciones de SQL](#sql-constraints).
{% endalert %}

### Paso 4: Previsualiza y valida tu consulta {#step-4-preview-and-validate-your-query}

Selecciona **Preview and validate** para ejecutar tu consulta.

La vista previa:

- Muestra los resultados en formato de tabla
- Muestra hasta 100 filas
- Muestra hasta 250 columnas

Para validar correctamente, tu consulta SQL debe devolver varias columnas obligatorias:

| Tipo de datos de sincronización | Columnas obligatorias |
|---|---|
| Atributos | - Un identificador de usuario, uno de `external_id`, `braze_id`, `alias_name` y `alias_label`, correo electrónico o número de teléfono.<br>- `UPDATED_AT`.<br>- Al menos una columna adicional (atributo) para sincronizar. |
| Eliminar usuarios | - Un identificador de usuario, uno de `external_id`, `braze_id`, `alias_name` y `alias_label`, correo electrónico o número de teléfono.<br>- `UPDATED_AT`. |
| Canvas Triggers | - Un identificador de usuario, uno de `external_id`, `braze_id`, `alias_name` y `alias_label`, correo electrónico o número de teléfono.<br>- `UPDATED_AT`. |
| Eventos personalizados | - Un identificador de usuario, uno de `external_id`, `braze_id`, `alias_name` y `alias_label`, correo electrónico o número de teléfono.<br>- `UPDATED_AT`.<br>- `NAME` para representar el nombre del evento.<br>- `TIME` para representar la hora del evento. Si no está disponible, CDI usa `UPDATED_AT` como sustituto. |
| Eventos de compra | - Un identificador de usuario, uno de `external_id`, `braze_id`, `alias_name` y `alias_label`, correo electrónico o número de teléfono.<br>- `UPDATED_AT`.<br>- `PRODUCT_ID`.<br>- `CURRENCY`.<br>- `PRICE`.<br>- `TIME` para representar la hora del evento de compra. Si no está disponible, CDI usa `UPDATED_AT` como sustituto. |
| Catálogo | - `ID` para representar el identificador del elemento del catálogo.<br>- `UPDATED_AT`.<br>- Al menos una columna adicional (campo de catálogo) para sincronizar. |
| Cuentas | - `ID` para representar el identificador de la cuenta.<br>- `NAME` para representar el nombre de la cuenta.<br>- `UPDATED_AT`.<br>- Al menos una columna adicional (campo de cuenta) para sincronizar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 4: Previsualiza y valida tu consulta" }

Las columnas adicionales fuera de las columnas obligatorias se sincronizan como atributos, propiedades de contexto de Canvas, propiedades del evento, campos de catálogo y campos de cuenta, respectivamente. Consulta [Comportamiento de validación](#validation-behavior) y [Solución de problemas](#troubleshooting) para obtener consejos útiles sobre errores de vista previa y validación y cómo solucionarlos.

### Paso 5: Revisa el mapeado de atributos y crea la sincronización {#step-5-review-attribute-mapping-and-create-sync}

Cuando la validación sea exitosa, continúa a **Next: Notifications** y crea tu sincronización.

{% alert important %}
Una configuración SQL incorrecta puede generar resultados no deseados, incluido el consumo excesivo de puntos de datos y riesgos operativos más amplios. Eres responsable de asegurar que la lógica de tu consulta sea correcta y debes previsualizar cuidadosamente todos los resultados antes de activar una sincronización.
{% endalert %}

## Restricciones SQL {#sql-constraints}

### Usar solo consultas `SELECT` {#use-select-queries-only}

Solo se admiten consultas de solo lectura.

Puedes usar:

- `SELECT`
- `WITH` (CTEs)
- `JOIN`

No puedes usar:

- `INSERT`, `UPDATE` o `DELETE`
- `CREATE` o `DROP`
- Múltiples sentencias separadas por `;`

### Usar una sola sentencia {#use-a-single-statement}

Tu consulta debe ser una sola sentencia ejecutable.

## Comportamiento de validación {#validation-behavior}

El editor SQL valida tu consulta antes de permitirte continuar.

### Errores SQL {#sql-errors}

Si tu consulta contiene errores de sintaxis:

- La validación falla
- No aparece vista previa
- Tu almacén devuelve un mensaje de error

### Errores de compilación {#compilation-errors}

Si tu consulta hace referencia a tablas, columnas u objetos no válidos o no autorizados:

- La validación falla
- No aparece vista previa
- Tu almacén devuelve un mensaje de error

### Errores de conexión {#connection-errors}

Si Braze no puede conectarse a tu almacén:

- La validación falla
- No aparece vista previa
- Aparece un mensaje de error de conexión

### Tiempo de espera de consulta agotado {#query-timeout}

Si tu consulta tarda demasiado en ejecutarse:

- Braze termina la consulta
- La validación falla
- Aparece un error de tiempo de espera agotado

### Errores de esquema de tabla {#table-schema-errors}

Si tu consulta compila, la validación aún puede fallar si:

- No se encuentra una columna de identificador
- Falta `UPDATED_AT`
- Faltan otras columnas obligatorias

En este caso, la vista previa sigue apareciendo para ayudarte a avanzar hacia una validación exitosa. Consulta el [Paso 4 en la sección anterior](#step-4-preview-and-validate-your-query) para obtener detalles sobre las columnas obligatorias para cada tipo de datos de sincronización.

### Resultados con cero filas {#zero-row-results}

Si tu consulta devuelve cero filas:

- La validación **pasa**
- Aún puedes crear la sincronización
- No se actualizan usuarios hasta que se devuelvan filas

## Compatibilidad con PAYLOAD (heredado) {#payload-support-legacy}

El Editor SQL es compatible con [tablas CDI heredadas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-1-set-up-tables-or-views) en las que existe una columna `PAYLOAD`.

Si tu consulta incluye:

- Un identificador válido
- `UPDATED_AT`
- Una columna `PAYLOAD`
- Columnas adicionales

Entonces:

- Braze sincroniza solo la columna `PAYLOAD`
- Braze ignora las columnas adicionales

## Editar una sincronización SQL {#edit-a-sql-sync}

Al editar una sincronización existente:

- Cualquier cambio en SQL requiere revalidación
- No puedes guardar cambios no válidos
- Los cambios válidos surten efecto después de guardar

Si ya hay una ejecución de sincronización en curso, tus cambios surtirán efecto en la siguiente ejecución.

## Solución de problemas {#troubleshooting}

Esta sección incluye errores comunes y orientación sobre cómo solucionarlos.

### Vista previa no disponible {#no-preview-available}

Cuando ves "Vista previa no disponible", uno de los siguientes tipos de error subyacentes puede estar causándolo.

| Tipo de error | Pasos para resolver |
|---|---|
| "No preview available" | Lee el banner de error para obtener pistas. |
| "Unable to connect to the source" | Verifica el nombre de usuario configurado, el localizador de cuenta y la configuración de autenticación por par de claves RSA.<br>Verifica que el almacén esté en ejecución.<br>Confirma el acceso a la red. |
| "SQL syntax error" | Revisa tu sintaxis SQL. |
| "Object does not exist or not authorized" | Asegúrate de que el rol tenga acceso `SELECT` a la tabla.<br>Confirma los permisos de base de datos y esquema.<br>Verifica errores tipográficos en el nombre de la tabla. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vista previa no disponible" }

### Se requiere una columna de identidad {#identity-column-required}

Asegúrate de que tu consulta incluya un identificador válido, como `external_id`.

### Falta la columna `UPDATED_AT` {#updated_at-column-is-missing}

Añade una columna de marca de tiempo para la sincronización incremental.

### "Añade más columnas... No hay atributos/campos de catálogo/campos de cuenta para sincronizar" {#add-more-columns-there-are-no-attributescatalog-fieldsaccount-fields-to-sync}

Añade al menos una columna adicional además del identificador y `UPDATED_AT`.

### Se agotó el tiempo de espera de ejecución de la consulta {#query-execution-timed-out}

Optimiza tu consulta o usa un almacén más grande.