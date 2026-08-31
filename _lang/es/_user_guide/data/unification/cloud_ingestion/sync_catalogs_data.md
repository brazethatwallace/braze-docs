---
nav_title: Sincronizar y eliminar datos del catálogo
article_title: Sincronizar y eliminar datos del catálogo
page_order: 6
page_type: reference
description: "Esta página ofrece un resumen de cómo sincronizar los datos del catálogo."

---

# Sincronizar y eliminar datos del catálogo {#sync-and-delete-catalog-data}

> En esta página se explica cómo sincronizar los datos del catálogo.

## Paso 1: Crear un nuevo catálogo {#step-1-create-a-new-catalog}

Antes de crear una nueva integración de ingesta de datos en la nube (CDI) para [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs), necesitas crear un nuevo catálogo o identificar un catálogo existente que quieras usar para la integración. Hay varias formas de crear un nuevo catálogo y cualquiera de ellas funcionará para la integración CDI:
- Cargar un [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- Crear un catálogo en el [panel de Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/create) o durante la configuración de CDI.
- Crear un catálogo mediante el [endpoint Crear catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)

Cualquier cambio en el esquema del catálogo (por ejemplo, agregar nuevos campos o cambiar el tipo de campo) debe realizarse a través del panel de catálogos antes de que los datos actualizados se sincronicen mediante CDI. Recomendamos realizar estas actualizaciones cuando la sincronización esté pausada o no esté programada para ejecutarse, con el fin de evitar conflictos entre los datos de tu almacén de datos y el esquema en Braze.

## Paso 2: Integrar la ingesta de datos en la nube con datos del catálogo {#step-2-integrate-cloud-data-ingestion-with-catalog-data}
La configuración de una sincronización de catálogo sigue de cerca el proceso de las [integraciones de CDI de datos de usuario]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

{% tabs %}
{% tab Snowflake %}

1. Configura una tabla de origen en Snowflake. Puedes usar los nombres del siguiente ejemplo o elegir tus propios nombres de base de datos, esquema y tabla. También puedes usar una vista o una vista materializada en lugar de una tabla.
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the catalog item to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Catalog fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The catalog item associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. Configura un rol, un almacén y un usuario, y otorga los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen del catálogo.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Si tu cuenta de Snowflake tiene políticas de red, añade las IP de Braze a la lista de permitidos para que el servicio de CDI pueda conectarse. Para consultar la lista de IP, consulta la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).
4. En el panel de Braze, ve a **Partners tecnológicos** > **Snowflake** y crea una nueva sincronización.
5. Introduce los datos de conexión (o reutiliza credenciales existentes) y la tabla de origen.
6. Continúa al paso 2 del flujo de configuración, selecciona el tipo de sincronización "Catalogs" e introduce el nombre de la integración y la programación. Ten en cuenta que el nombre de la integración debe **coincidir exactamente** con el nombre del catálogo que creaste anteriormente.
7. Elige una frecuencia de sincronización y continúa al siguiente paso.
8. Añade la clave pública que aparece en el panel al usuario que creaste para que Braze se conecte a Snowflake. Para completar este paso, necesitarás a alguien con acceso `SECURITYADMIN` o superior en Snowflake.
9. Selecciona **Probar conexión** para comprobar que todo funciona como se espera.
10. Guarda la sincronización y usa los datos del catálogo sincronizado para todos tus casos de personalización.
{% endtab %}
{% tab Redshift %}

1. Configura una tabla de origen en Redshift. Puedes usar los nombres del siguiente ejemplo o elegir tus propios nombres de base de datos, esquema y tabla. También puedes usar una vista o una vista materializada en lugar de una tabla.
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the catalog item to be created or updated
       id varchar not null,
       --Catalog fields and values that should be added or updated
       payload varchar(max),
       --The catalog item associated with this ID should be deleted
       deleted boolean
    )
    ```
2. Configura un usuario y otorga los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen del catálogo.
    {% raw %}
    ```sql
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. Si tienes un firewall u otras políticas de red, debes otorgar a Braze acceso de red a tu instancia de Redshift. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze. Para consultar la lista de IP, consulta la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. Opcionalmente, configura un nuevo proyecto o conjunto de datos para alojar tu tabla de origen.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o más tablas para usar en tu integración de CDI con los siguientes campos:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| NOMBRE DEL CAMPO | TIPO | MODO |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | OBLIGATORIO |
| PAYLOAD | JSON | OBLIGATORIO |
| ID | STRING | OBLIGATORIO |
| DELETED | BOOLEAN | OPCIONAL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2: Integrar la ingesta de datos en la nube con datos del catálogo" }

{:start="2"}

2. Configura un usuario y otorga los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen del catálogo.
La cuenta de servicio debe tener los permisos de la siguiente sección:
- BigQuery Connection User: esto permitirá a Braze establecer conexiones.
- BigQuery User: esto proporcionará a Braze acceso para ejecutar consultas, leer metadatos del conjunto de datos y listar tablas.
- BigQuery Data Viewer: esto proporcionará a Braze acceso para ver los conjuntos de datos y su contenido.
- BigQuery Job User: esto proporcionará a Braze acceso para ejecutar trabajos.<br><br>Después de crear la cuenta de servicio y otorgar los permisos, genera una clave JSON. Consulta [Crear y eliminar claves](https://cloud.google.com/iam/docs/keys-create-delete) para más información. Actualizarás esto en el panel de Braze más adelante.

{:start="3"}
3. Si tienes políticas de red configuradas, debes otorgar a Braze acceso de red a tu instancia de BigQuery. Para consultar la lista de IP, consulta la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Configura una tabla de origen en Databricks. Puedes usar los nombres del siguiente ejemplo o elegir tus propios nombres de catálogo, esquema y tabla. También puedes usar una vista o una vista materializada en lugar de una tabla.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  id STRING,
  deleted BOOLEAN,
  payload STRING, STRUCT, or MAP
);
```

| NOMBRE DEL CAMPO | TIPO | MODO |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | OBLIGATORIO |
| PAYLOAD | STRING, STRUCT, or MAP | OBLIGATORIO |
| ID | STRING | OBLIGATORIO |
| DELETED | BOOLEAN | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2: Integrar la ingesta de datos en la nube con datos del catálogo" }

{:start="2"}

2. Crea un token de acceso personal en tu espacio de trabajo de Databricks.

- a. Selecciona tu nombre de usuario de Databricks y luego selecciona **User Settings** en el menú desplegable.
- b. En la pestaña **Access tokens**, selecciona **Generate new token**.
- c. Introduce un comentario que te ayude a identificar este token, como "Braze CDI".
- d. Cambia la duración del token a sin duración dejando el campo **Lifetime (days)** en blanco. Selecciona **Generate**.
- e. Copia el token que aparece y luego selecciona **Done**.
- f. Guarda el token en un lugar seguro hasta que necesites introducirlo durante el paso de creación de credenciales en el panel de Braze.

{:start="3"}
3. Si tienes políticas de red configuradas, debes otorgar a Braze acceso de red a tu instancia de Databricks. Para consultar la lista de IP, visita la página de [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Microsoft Fabric %}

Crea una o más tablas para usar en tu integración de CDI con los siguientes campos:

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  ID VARCHAR NOT NULL,
  DELETED BIT
)
GO
```

{:start="2"}

2. Configura un principal de servicio y otorga los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen del catálogo. Para obtener más información sobre cómo crear un nuevo principal de servicio y credenciales, consulta la página de [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{:start="3"}
3. Si tienes políticas de red configuradas, debes otorgar a Braze acceso de red a tu instancia de Microsoft Fabric. Para consultar la lista de IP, visita la página de [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab S3 %}
Crea archivos de origen en S3 usando formato JSON o CSV. Cada archivo debe incluir los siguientes campos:

| Campo | ¿Obligatorio? | Descripción |
| --- | --- | --- |
| `ID` | Sí | El ID del elemento del catálogo a crear o actualizar. |
| `PAYLOAD` | Sí | Una cadena JSON de los campos a sincronizar con el elemento del catálogo en Braze. |
| `DELETED` | Opcional | Cuando se establece como `true`, el elemento del catálogo correspondiente se elimina del catálogo. |
| `UPDATED_AT` | *No soportado* | El almacenamiento de archivos no admite columnas `UPDATED_AT`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2: Integrar la ingesta de datos en la nube con datos del catálogo" }

{% alert note %}
Los nombres de archivo deben seguir las reglas de AWS y ser únicos. Añade marcas de tiempo para asegurar la unicidad.
{% endalert %}

La configuración completa de S3 requiere un contenedor de S3, una cola de Amazon SQS y un rol y política de AWS IAM. Braze solo procesa archivos cargados después de crear la sincronización, así que vuelve a cargar los archivos existentes que quieras ingestar.

Para el flujo completo de configuración de S3, consulta [Integraciones de almacenamiento de archivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations), especialmente:

- [Configurar la ingesta de datos en la nube en AWS]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-aws)
- [Configurar la ingesta de datos en la nube en Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze)
- [Solución de problemas]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#troubleshooting)

Para problemas comunes de notificaciones y permisos en el lado de AWS, consulta [Conceder permisos para publicar mensajes de notificación de eventos en un destino](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html).

Los siguientes ejemplos muestran formatos JSON y CSV válidos para sincronizar datos de catálogo desde el almacenamiento de archivos.

{% subtabs %}
{% subtab JSON Catalogs %}
```jsonl
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"86","payload":"{\"product_name\":\"Product 86\",\"price\":86.86}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```

{% alert important %}
Cada línea en tu archivo de origen debe contener un JSON válido o el archivo se omitirá.
{% endalert %}
{% endsubtab %}
{% subtab CSV Catalogs with Delete %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
86,"{""product_name"": ""Product 86"", ""price"": 86.86}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
{% endsubtab %}
{% subtab CSV Catalogs without Delete %}
```plaintext
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}"
86,"{""product_name"": ""Product 86"", ""price"": 86.86}"
```
{% endsubtab %}
{% endsubtabs %}

Para ejemplos adicionales de archivos, consulta [Integraciones de almacenamiento de archivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).

{% endtab %}
{% endtabs %}

## Cómo funciona la integración {#how-the-integration-works}

{% alert note %}
Las vistas de sincronización en esta sección se aplican únicamente a integraciones con almacenes de datos. Para el almacenamiento de archivos en S3, Braze procesa los archivos nuevos a medida que se cargan en tu contenedor. Consulta [Integraciones de almacenamiento de archivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations) para más detalles.
{% endalert %}

Cada vez que se ejecuta la sincronización, Braze extrae todas las filas en las que `UPDATED_AT` es posterior al último valor sincronizado. Las filas que se encuentran exactamente en la marca de tiempo del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo. Recomendamos crear una vista en tu almacén de datos a partir de los datos de tu catálogo para configurar una tabla de origen que se actualice completamente cada vez que se ejecute una sincronización. Con las vistas, no necesitarás reescribir la consulta cada vez.

Por ejemplo, si tienes una tabla de datos de productos (`product_catalog_1`) con `product_id` y tres atributos adicionales, podrías sincronizar la siguiente vista:

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    product_id as id,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    Product_id as id,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [braze].[user_update_example]
AS SELECT
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- Los datos obtenidos de la integración se utilizarán para crear o actualizar elementos en el catálogo de destino según el `id` proporcionado.
- Si DELETED se establece en `true`, el elemento de catálogo correspondiente se eliminará.
- La sincronización no registrará puntos de datos, pero todos los datos sincronizados contarán para el uso total de tu catálogo; este uso se mide en función del total de datos almacenados, por lo que no necesitas preocuparte por sincronizar solo los datos que hayan cambiado.