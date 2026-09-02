---
nav_title: Integraciones de almacenes de datos
article_title: Integraciones de almacenamiento de almacén de datos
alias: /partners/databricks/
description: "Esta página explica cómo utilizar la ingesta de datos de Cloud de Braze para sincronizar datos relevantes con tu integración de Snowflake, Redshift, BigQuery y Databricks."
page_order: 3
page_type: reference
---

# Integraciones de almacenamiento de almacén de datos {#data-warehouse-storage-integrations}

> Esta página explica cómo utilizar la ingesta de datos de Cloud (CDI) de Braze para sincronizar datos relevantes con tu integración de Snowflake, Redshift, BigQuery y Databricks.

## Configuración de integraciones de almacén de datos {#setting-up-data-warehouse-integrations}

Las integraciones de ingesta de datos en la nube requieren cierta configuración del lado de Braze y en tu instancia de almacén de datos. Sigue estos pasos para configurar la integración:

{% tabs %}
{% tab Snowflake %}
1. En tu instancia de Snowflake, configura las tablas o vistas que quieras sincronizar con Braze.
2. Crea un nuevo origen de Snowflake en el panel de Braze.
3. Obtén la clave pública proporcionada en el panel de Braze y [añádela al usuario de Snowflake para la autenticación](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Crea una sincronización en el panel de Braze, prueba la integración e inicia la sincronización.

{% alert tip %}
La [guía de inicio rápido de Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) proporciona código de ejemplo y describe los pasos necesarios para crear una canalización automatizada utilizando Snowflake Streams y CDI para sincronizar datos con Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Asegúrate de que Braze tenga acceso permitido a las tablas de Redshift que deseas sincronizar. Braze se conecta a Redshift a través de internet.
2. En tu instancia de Redshift, configura las tablas o vistas que quieras sincronizar con Braze.
3. Crea un nuevo origen y sincronización en el panel de Braze.
4. Prueba la integración e inicia la sincronización.

{% alert note %}
Las filas procesadas por sincronización dependen del rendimiento de tu almacén de datos, la latencia de red y la cantidad de datos nuevos que coincidan con la consulta de sincronización. Utiliza el **Historial de sincronización** de la integración en el panel para ver la duración y el recuento de filas de las ejecuciones recientes.
{% endalert %}
{% endtab %}
{% tab BigQuery %}
1. Crea una cuenta de servicio y permite el acceso al(los) proyecto(s) y conjunto(s) de datos de BigQuery que contengan los datos que deseas sincronizar.
2. En tu cuenta de BigQuery, configura las tablas o vistas que quieras sincronizar con Braze.
3. Crea un nuevo origen y sincronización en el panel de Braze.
4. Prueba la integración e inicia la sincronización.
{% endtab %}
{% tab Databricks %}
1. Crea una cuenta de servicio y permite el acceso al(los) proyecto(s) y conjunto(s) de datos de Databricks que contengan los datos que deseas sincronizar.
2. En tu cuenta de Databricks, configura las tablas o vistas que quieras sincronizar con Braze.
3. Crea un nuevo origen y sincronización en el panel de Braze.
4. Prueba la integración e inicia la sincronización.

{% alert important %}
Puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecta a instancias SQL Classic y Pro, lo que puede provocar retrasos durante la configuración y prueba de la conexión, así como al inicio de las sincronizaciones programadas. Usar una instancia SQL sin servidor minimiza el tiempo de calentamiento y mejora el rendimiento de las consultas, pero puede resultar en costes de integración ligeramente más elevados.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Crea un principal de servicio y otorga acceso a las API de Fabric.
2. Configura un espacio de trabajo compartido y otorga acceso al principal de servicio.
3. En el espacio de trabajo compartido de Fabric, configura las tablas o vistas que quieras sincronizar con Braze.
4. Crea un nuevo origen y sincronización en el panel de Braze.
5. Prueba la integración e inicia la sincronización.
{% endtab %}
{% endtabs %}

### Paso 1: Configurar tablas o vistas {#step-1-set-up-tables-or-views}

Antes de empezar, revisa [Configuración de tablas para la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup) para comprender los requisitos de la tabla de origen en comparación con los requisitos de formato de `PAYLOAD`.

{% alert note %}
Tu tabla o vista de origen puede incluir columnas que no figuran para tu almacén de datos en las pestañas de la siguiente sección (por ejemplo, auditoría o hashing). Braze solo lee las columnas descritas en esas pestañas; las demás columnas no se utilizan durante las sincronizaciones de ingesta de datos en la nube.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

#### Paso 1.1: Configurar la tabla {#step-11-set-up-the-table}

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Puedes nombrar la base de datos, el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora en la que se actualizó o agregó esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificación de usuario** - Tu tabla puede contener una o más columnas de identificación de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze.
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y `alias_label` especifica el tipo de alias. Los usuarios pueden tener múltiples alias con diferentes etiquetas, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Es generado por el SDK or kit de desarrollo de software de Braze, y no se pueden crear nuevos usuarios usando un Braze ID a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen múltiples perfiles con la misma dirección de correo electrónico, se prioriza el perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, el correo electrónico se utiliza como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen múltiples perfiles con el mismo número de teléfono, se prioriza el perfil actualizado más recientemente.
- `PAYLOAD` - Es una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.

#### Paso 1.2: Configurar el rol y los permisos de la base de datos {#step-12-set-up-the-role-and-database-permissions}

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Actualiza los nombres según sea necesario, pero los permisos deben coincidir con el ejemplo anterior.

#### Paso 1.3: Configurar el almacén y dar acceso al rol de Braze {#step-13-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
El almacén necesita tener la opción **auto-resume** activada. Si no es así, otorga a Braze privilegios adicionales de `OPERATE` en el almacén para que Braze pueda activarlo cuando se ejecute la consulta.
{% endalert %}

#### Paso 1.4: Configurar el usuario {#step-14-set-up-the-user}

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Después de este paso, comparte la información de conexión con Braze para recibir una clave pública que se añadirá al usuario.

{% alert note %}
Al conectar diferentes espacios de trabajo a la misma cuenta de Snowflake, debes crear un usuario único para cada espacio de trabajo de Braze donde estés creando una integración. Dentro de un espacio de trabajo, puedes reutilizar el mismo usuario en distintas integraciones, pero la creación de la integración falla si un usuario en la misma cuenta de Snowflake está duplicado entre espacios de trabajo.
{% endalert %}

#### Paso 1.5: Permitir las IP de Braze en la política de red de Snowflake (opcional) {#step-15-allow-braze-ips-in-snowflake-network-policy-optional}

Dependiendo de la configuración de tu cuenta de Snowflake, es posible que necesites permitir las siguientes direcciones IP en tu política de red de Snowflake. Para más información sobre cómo habilitar esto, consulta la documentación relevante de Snowflake sobre [modificar una política de red](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Paso 1.1: Configurar la tabla

Opcionalmente, configura una nueva base de datos y un nuevo esquema para alojar tu tabla de origen.
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Crea una tabla (o vista) para usar en tu integración CDI.
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Puedes nombrar la base de datos, el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora en la que se actualizó o agregó esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificación de usuario** - Tu tabla puede contener una o más columnas de identificación de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze.
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y `alias_label` especifica el tipo de alias. Los usuarios pueden tener múltiples alias con diferentes etiquetas, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Es generado por el SDK or kit de desarrollo de software de Braze, y no se pueden crear nuevos usuarios usando un Braze ID a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen múltiples perfiles con la misma dirección de correo electrónico, se prioriza el perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, el correo electrónico se utiliza como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen múltiples perfiles con el mismo número de teléfono, se prioriza el perfil actualizado más recientemente.
- `PAYLOAD` - Es una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.

#### Paso 1.2: Crear el usuario y otorgar permisos {#step-12-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Estos son los permisos mínimos requeridos para este usuario. Si creas múltiples integraciones CDI, puede que quieras otorgar permisos a un esquema o gestionar los permisos mediante un grupo.

#### Paso 1.3: Permitir el acceso a las IP de Braze {#step-13-allow-access-to-braze-ips}

Si tienes un cortafuegos u otras políticas de red, debes otorgar a Braze acceso de red a tu instancia de Redshift. Un ejemplo de endpoint URL de Redshift es "example-cluster.ap-northeast-2.redshift.amazonaws.com".

Algunas cosas importantes que debes saber:
- Es posible que también necesites cambiar tus grupos de seguridad para permitir que Braze acceda a tus datos en Redshift.
- Asegúrate de permitir explícitamente el tráfico entrante en las IP de la tabla y en el puerto utilizado para consultar tu clúster de Redshift (el predeterminado es 5439). Debes permitir explícitamente la conectividad TCP de Redshift en este puerto incluso si las reglas de entrada están configuradas para "permitir todo".
- El endpoint del clúster de Redshift debe ser accesible públicamente para que Braze pueda conectarse a tu clúster.
     - Si no deseas que tu clúster de Redshift sea accesible públicamente, puedes configurar un VPC y una instancia EC2 para utilizar un túnel SSH para acceder a los datos de Redshift. Para más información, consulta la [publicación del Centro de Conocimiento de AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).

Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Paso 1.1: Configurar la tabla

Opcionalmente, configura un nuevo proyecto o conjunto de datos para alojar tu tabla de origen.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o más tablas para usar en tu integración CDI con los siguientes campos:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT` | TIMESTAMP | REQUIRED |
| `PAYLOAD` | JSON | REQUIRED |
| `EXTERNAL_ID` | STRING | NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
| `BRAZE_ID` | STRING | NULLABLE |
| `EMAIL` | STRING | NULLABLE |
| `PHONE` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 1.1: Configurar la tabla" }

Puedes nombrar el proyecto, el conjunto de datos y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora en la que se actualizó o agregó esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificación de usuario** - Tu tabla puede contener una o más columnas de identificación de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze.
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y `alias_label` especifica el tipo de alias. Los usuarios pueden tener múltiples alias con diferentes etiquetas, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Es generado por el SDK or kit de desarrollo de software de Braze, y no se pueden crear nuevos usuarios usando un Braze ID a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen múltiples perfiles con la misma dirección de correo electrónico, se prioriza el perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, el correo electrónico se utiliza como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen múltiples perfiles con el mismo número de teléfono, se prioriza el perfil actualizado más recientemente.
- `PAYLOAD` - Es una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.

{% alert important %}
**Particionado de BigQuery**

CDI admite particiones en BigQuery. Si particionas por una función de `UPDATED_AT` (por ejemplo, con granularidad de día, semana u hora, según el tamaño de tu conjunto de datos), BigQuery puede reducir la cantidad de datos que necesita escanear. Esto mejora el rendimiento y la eficiencia para tablas muy grandes.

No particione por otros campos. Prueba diferentes configuraciones para encontrar la mejor opción para tus datos específicos.

Todas las consultas CDI filtran por `UPDATED_AT`, pero este comportamiento podría cambiar. Diseña el esquema de tu tabla para que _no_ requiera que las consultas incluyan esta cláusula.

Para más información, consulta la [documentación de particionado de BigQuery](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).
{% endalert %}

#### Paso 1.2: Crear una cuenta de servicio y otorgar permisos {#step-12-create-a-service-account-and-grant-permissions}

Crea una cuenta de servicio en GCP para que Braze la utilice para conectarse y leer datos de tu(s) tabla(s). La cuenta de servicio debe tener los siguientes permisos:

- **BigQuery Connection User:** Permite a Braze realizar conexiones.
- **BigQuery User:** Proporciona a Braze acceso para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- **BigQuery Data Viewer:** Proporciona a Braze acceso para ver conjuntos de datos y su contenido.
- **BigQuery Job User:** Proporciona a Braze acceso para ejecutar trabajos.

Después de crear la cuenta de servicio y otorgar los permisos, genera una clave JSON. Para más información, consulta [Crear y eliminar claves de cuentas de servicio](https://cloud.google.com/iam/docs/keys-create-delete). Carga esta clave en el panel de Braze en un paso posterior.

#### Paso 1.3: Permitir el acceso a las IP de Braze

Si tienes políticas de red implementadas, debes otorgar a Braze acceso de red a tu instancia de BigQuery. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Paso 1.1: Configurar la tabla

Opcionalmente, configura un nuevo catálogo o esquema para alojar tu tabla de origen.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o más tablas para usar en tu integración CDI con los siguientes campos:


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT` | TIMESTAMP | REQUIRED |
| `PAYLOAD` | STRING, STRUCT, or MAP | REQUIRED |
| `EXTERNAL_ID` | STRING | NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
| `BRAZE_ID` | STRING | NULLABLE |
| `EMAIL` | STRING | NULLABLE |
| `PHONE` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 1.1: Configurar la tabla" }

Puedes nombrar el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora en la que se actualizó o agregó esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificación de usuario** - Tu tabla puede contener una o más columnas de identificación de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze.
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y `alias_label` especifica el tipo de alias. Los usuarios pueden tener múltiples alias con diferentes etiquetas, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Es generado por el SDK or kit de desarrollo de software de Braze, y no se pueden crear nuevos usuarios usando un Braze ID a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen múltiples perfiles con la misma dirección de correo electrónico, se prioriza el perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, el correo electrónico se utiliza como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen múltiples perfiles con el mismo número de teléfono, se prioriza el perfil actualizado más recientemente.
- `PAYLOAD` - Es una cadena o estructura de los campos que deseas sincronizar con el usuario en Braze.

#### Paso 1.2: Crear un token de acceso {#step-12-create-an-access-token}

Para que Braze pueda acceder a Databricks, es necesario crear un token de acceso personal.

1. En tu espacio de trabajo de Databricks, selecciona tu nombre de usuario de Databricks en la barra superior y luego selecciona **User Settings** en el menú desplegable.
2. En la pestaña Access tokens, selecciona **Generate new token**.
3. Introduce un comentario que te ayude a identificar este token, como "Braze CDI", y cambia la duración del token a sin fecha de caducidad dejando el campo Lifetime (days) vacío (en blanco).
4. Selecciona **Generate**.
5. Copia el token mostrado y luego selecciona **Done**.

Conserva el token en un lugar seguro hasta que necesites introducirlo en el panel de Braze durante el paso de creación de credenciales.

#### Paso 1.3: Permitir el acceso a las IP de Braze

Si tienes políticas de red implementadas, debes otorgar a Braze acceso de red a tu instancia de Databricks. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Paso 1.1: Configurar el principal de servicio y otorgar acceso {#step-11-set-up-the-service-principal-and-grant-access}
Braze se conecta a tu almacén de Fabric mediante un principal de servicio con autenticación de Entra ID. Crea un nuevo principal de servicio para que Braze lo utilice, y otorga acceso a los recursos de Fabric según sea necesario. Braze necesita los siguientes datos para conectarse:

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azure no permite una caducidad ilimitada en los secretos de los principales de servicio. Recuerda actualizar las credenciales antes de que caduquen para mantener el flujo de datos hacia Braze.
{% endalert %}

#### Paso 1.2: Otorgar acceso a los recursos de Fabric {#step-12-grant-access-to-fabric-resources}
Proporciona acceso para que Braze se conecte a tu instancia de Fabric. En tu portal de administración de Fabric, ve a **Configuración** > **Gobernanza e información** > **Portal de administración** > **Configuración de inquilino**.

* En **Configuración de desarrollador**, habilita **Los principales de servicio pueden usar las API de Fabric** para que Braze pueda conectarse usando Microsoft Entra ID.
* En **Configuración de OneLake**, habilita **Los usuarios pueden acceder a datos almacenados en OneLake con aplicaciones externas a Fabric** para que el principal de servicio pueda acceder a datos desde una aplicación externa.

#### Paso 1.3: Configurar un espacio de trabajo compartido y otorgar acceso {#step-13-set-up-a-shared-workspace-and-grant-access}

Todos los recursos de Fabric que desees conectar a Braze deben ubicarse en un espacio de trabajo compartido. Si solo has estado usando el espacio de trabajo predeterminado **My Workspace**, crea un nuevo espacio de trabajo compartido:

1. En el menú de navegación, selecciona **Workspaces** y luego selecciona **+ New workspace**.
2. Introduce un **Nombre** para el espacio de trabajo y luego selecciona **Apply**.

Una vez que tengas un espacio de trabajo compartido, otorga acceso al principal de servicio:

1. Selecciona el espacio de trabajo y luego selecciona **Manage Access**.
2. Selecciona **+ Add people or groups**.
3. Busca y selecciona el nombre del principal de servicio que creaste en el paso 1.1. Si no aparece, confirma que has habilitado la configuración **Los principales de servicio pueden usar las API de Fabric** en el paso 1.2.
4. En el menú desplegable de roles, selecciona **Contributor**.

El principal de servicio ahora puede acceder a los recursos del almacén de Fabric en este espacio de trabajo a través de sus endpoints SQL, incluido el almacén que se usará para Braze.

#### Paso 1.4: Configurar la tabla {#step-14-set-up-the-table}
Braze admite tanto tablas como vistas en almacenes de Fabric. Si necesitas crear un nuevo almacén, créalo dentro del espacio de trabajo compartido del paso 1.3. Ve a **Create > Data Warehouse > Warehouse** en la consola de Fabric.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Puedes nombrar el almacén, el esquema y la tabla o vista como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora en la que se actualizó o agregó esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificación de usuario** - Tu tabla puede contener una o más columnas de identificación de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze.
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y `alias_label` especifica el tipo de alias. Los usuarios pueden tener múltiples alias con diferentes etiquetas, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Es generado por el SDK or kit de desarrollo de software de Braze, y no se pueden crear nuevos usuarios usando un Braze ID a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen múltiples perfiles con la misma dirección de correo electrónico, se prioriza el perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, el correo electrónico se utiliza como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen múltiples perfiles con el mismo número de teléfono, se prioriza el perfil actualizado más recientemente.
- `PAYLOAD` - Es una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.


#### Paso 1.5: Obtener la cadena de conexión del almacén {#step-15-get-warehouse-connection-string}
Para obtener el endpoint SQL de tu almacén, ve al **espacio de trabajo** en Fabric, pasa el cursor sobre el nombre del almacén en la lista de elementos y selecciona **Copy SQL connection string**.

![La página de la consola de Fabric en Microsoft Azure, donde los usuarios deben obtener la cadena de conexión SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Paso 1.6: Permitir las IP de Braze en el cortafuegos (opcional) {#step-16-allow-braze-ips-in-firewall-optional}

Dependiendo de la configuración de tu cuenta de Microsoft Fabric, es posible que necesites permitir las siguientes direcciones IP en tu cortafuegos para permitir el tráfico desde Braze. Para más información sobre cómo habilitar esto, consulta la documentación relevante sobre [acceso condicional de Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Paso 2: Crear un nuevo origen en el panel de Braze {#step-2-create-a-new-source-in-the-braze-dashboard}


{% tabs %}
{% tab Snowflake %}

En el panel de Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Orígenes**, selecciona **Añadir origen de datos** y luego selecciona **Snowflake**.

#### Paso 2.1: Añadir información de conexión de Snowflake {#step-21-add-snowflake-connection-information}

Elige un nombre para tu origen e introduce tus credenciales y configuración de Snowflake, luego continúa al siguiente paso.

Antes de continuar, confirma el valor que introduces en **Snowflake Account Locator**.

Para el campo **Snowflake Account Locator**, introduce tu [identificador de cuenta](https://docs.snowflake.com/en/user-guide/admin-account-identifier) de Snowflake. Introduce solo el valor del identificador de cuenta, como `myorganization-myaccount`. No incluyas `https://`, `.snowflakecomputing.com` ni ninguna ruta.

Para encontrar tu identificador de cuenta de Snowflake:

1. En Snowsight, selecciona el menú de tu cuenta.
2. Selecciona **View account details**.
3. Copia el valor de **Account identifier**.
4. Si copias desde una URL de Snowflake, usa solo el valor antes de `.snowflakecomputing.com`.

#### Paso 2.2: Añadir una clave pública al usuario de Braze {#step-22-add-a-public-key-to-the-braze-user}

Después de introducir tus credenciales y configuración, haz clic en **Save credentials** y genera una clave RSA, luego vuelve a Snowflake para completar la configuración. Añade la clave pública que se muestra en el panel al usuario que creaste para que Braze se conecte a Snowflake.

Para información adicional sobre cómo hacerlo, consulta la [documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si deseas rotar las claves en cualquier momento, Braze puede generar un nuevo par de claves y proporcionar la nueva clave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

En el panel de Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Orígenes**, selecciona **Añadir origen de datos** y luego selecciona **Amazon Redshift**.

#### Paso 2.1: Añadir información de conexión de Redshift y tabla de origen {#step-21-add-redshift-connection-information-and-source-table}

Elige un nombre para tu origen e introduce tus credenciales y configuración de Redshift. Si estás usando un túnel de red privada, activa el interruptor e introduce la información del túnel. Luego, continúa al siguiente paso.

{% alert note %}
En el panel de Braze, el campo **Database name** solo acepta letras (A–Z, a–z), números (0–9) y guiones bajos (_), aunque Amazon Redshift admite caracteres adicionales en los identificadores de bases de datos.
{% endalert %}

#### Paso 2.2: Probar la conexión y conectar al origen {#step-22-test-connection-and-connect-to-source}

A continuación, selecciona **Test connection**. Una vez exitosa, finaliza la configuración restante y haz clic en **Connect to Source**. Si la conexión falla, aparece un mensaje de error para ayudar a solucionar el problema.

#### Solución de problemas: identificador de instantánea no válido {#troubleshooting-invalid-snapshot-identifier}

Si Braze devuelve un error `Invalid snapshot identifier` durante **Test connection** o la configuración de sincronización, Redshift no puede resolver la referencia de instantánea utilizada cuando se consulta tu objeto de origen.

En Redshift, una instantánea es una copia de seguridad en un punto en el tiempo de un clúster. Cada instantánea tiene un identificador único que Redshift utiliza para hacer referencia a ese estado de copia de seguridad. Para más información, consulta [Instantáneas y copias de seguridad de Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html).

Este error puede ocurrir cuando los metadatos cambian mientras Braze valida el objeto de origen, por ejemplo, durante operaciones de copia, restauración o replicación de instantáneas. Para más información, consulta [copiar instantáneas a otra región de AWS](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html) y [restaurar un clúster a partir de una instantánea](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-cluster-from-snapshot.html).

Para solucionar el problema:

1. Verifica la configuración del origen en Braze, incluyendo el endpoint del clúster, la base de datos, el esquema y el nombre del objeto.
2. Ejecuta la misma consulta directamente en Redshift para confirmar que la tabla o vista es legible y estable.
3. Vuelve a intentarlo después de que finalice cualquier actividad activa de instantánea, restauración, redimensionamiento o replicación.
4. Si el problema persiste, consulta una vista materializada en lugar de una tabla base que cambia con frecuencia.

Una vista materializada almacena resultados de consulta precomputados que puedes actualizar en un horario programado, lo que puede hacer que las lecturas sean más estables para las sincronizaciones CDI. Para más información, consulta [vistas materializadas en Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html).

Ejemplo:

```sql
CREATE MATERIALIZED VIEW ingestion.users_attributes_mv AS
SELECT updated_at, external_id, alias_label, alias_name, braze_id, email, phone, payload
FROM ingestion.users_attributes_sync;

REFRESH MATERIALIZED VIEW ingestion.users_attributes_mv;
```

Después de crear la vista materializada, usa el nombre de la vista materializada como objeto de origen en tu sincronización CDI de Braze en lugar de la tabla base.
{% endtab %}
{% tab BigQuery %}

En el panel de Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Orígenes**, selecciona **Añadir origen de datos** y luego selecciona **Google BigQuery**.

#### Paso 2.1: Añadir información de conexión de BigQuery y tabla de origen {#step-21-add-bigquery-connection-information-and-source-table}

Elige un nombre para tu origen. Luego, carga la clave JSON y proporciona un nombre para la cuenta de servicio. Después, introduce los campos de configuración restantes.

#### Paso 2.2: Probar la conexión y conectar al origen

A continuación, selecciona **Test connection**. Una vez exitosa, finaliza la configuración restante y haz clic en **Connect to Source**. Si la conexión falla, aparece un mensaje de error para ayudar a solucionar el problema.

{% endtab %}
{% tab Databricks %}

En el panel de Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Orígenes**, selecciona **Añadir origen de datos** y luego selecciona **Databricks**.

#### Paso 2.1: Añadir información de conexión de Databricks y tabla de origen {#step-21-add-databricks-connection-information-and-source-table}

Elige un nombre para tu origen e introduce tus credenciales y configuración de Databricks. Luego, continúa al siguiente paso.

#### Paso 2.2: Probar la conexión y conectar al origen

A continuación, selecciona **Test connection**. Una vez exitosa, finaliza la configuración restante y haz clic en **Connect to Source**. Si la conexión falla, aparece un mensaje de error para ayudar a solucionar el problema.

{% alert note %}
Debes probar con éxito un origen antes de que pueda crearse. Si cierras la página de creación, tu origen no se guarda.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

En el panel de Braze, ve a Configuración de datos > Ingesta de datos en la nube > Orígenes, selecciona **Añadir origen de datos** y luego selecciona **Microsoft Fabric**.

#### Paso 2.1: Configurar una sincronización de ingesta de datos en la nube {#step-21-set-up-a-cloud-data-ingestion-sync}

Elige un nombre para tu origen e introduce tus credenciales y configuración de Microsoft Fabric.
- **Credentials Name** es una etiqueta para estas credenciales en Braze; puedes establecer un valor descriptivo aquí.
- Consulta los pasos de la sección 1 para obtener detalles sobre cómo recuperar el Tenant ID, Principal ID, Client Secret y Connection String.

#### Paso 2.2: Probar la conexión y conectar al origen

A continuación, selecciona **Test connection**. Una vez exitosa, finaliza la configuración restante y haz clic en **Connect to Source**. Si la conexión falla, aparece un mensaje de error para ayudar a solucionar el problema.

{% alert note %}
Debes probar con éxito un origen antes de que pueda crearse. Si cierras la página de creación, tu origen no se guarda.
{% endalert %}

{% endtab %}

{% endtabs %}

### Paso 3: Crear una nueva sincronización en el panel de Braze {#step-3-create-a-new-sync-in-the-braze-dashboard}
Ve a **Configuración de datos** > **Ingesta de datos en la nube** > **Sincronizaciones** y selecciona **Crear sincronización de datos**.

{% tabs %}
{% tab Snowflake %}

#### Paso 3.1: Configurar los detalles de la sincronización y probar la conexión {#step-31-configure-sync-details-and-test-connection}
Elige un nombre para tu sincronización. Luego, selecciona cualquier origen activo e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y haz clic en **Test Connection**.

Una vez exitosa, aparece una vista previa de los datos. Selecciona **Next: Notifications** para continuar. Si la conexión falla, aparece un mensaje de error para ayudar a solucionar el problema.

{% alert note %}
Debes probar con éxito una sincronización antes de avanzar a los siguientes pasos. Si necesitas cerrar la página de creación de sincronización, haz clic en **Save as draft** para guardar tu progreso.
{% endalert %}

#### Paso 3.2: Añadir preferencias de notificación {#step-32-add-notification-preferences}
Introduce la(s) dirección(es) de correo electrónico de contacto para notificaciones de errores de sincronización. Braze utiliza esta información de contacto para enviar notificaciones sobre errores de integración, como la pérdida inesperada de acceso a la tabla.

Los correos de contacto solo reciben notificaciones de errores globales o a nivel de sincronización, como tablas faltantes, permisos y otros. No reciben problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que las sincronizaciones se ejecuten.

Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Solo para sincronizaciones de catálogos) El nivel del catálogo no tiene espacio

#### Paso 3.3: Programación {#step-33-scheduling}
Por último, configura tu sincronización como no recurrente o recurrente.

Las sincronizaciones no recurrentes se pueden activar manualmente o a través de la API.

Las sincronizaciones recurrentes pueden tener una frecuencia desde cada 15 minutos hasta una vez al mes. Braze programa la sincronización recurrente en la zona horaria UTC.

{% endtab %}

{% tab Redshift %}

#### Paso 3.1: Configurar los detalles de la sincronización y probar la conexión
Elige un nombre para tu sincronización. Luego, selecciona cualquier origen activo e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y haz clic en **Test Connection**.

Una vez exitosa, aparece una vista previa de los datos. Selecciona **Next: Notifications** para continuar. Si la conexión falla, aparece un mensaje de error para ayudar a solucionar el problema.

{% alert note %}
Debes probar con éxito una sincronización antes de avanzar a los siguientes pasos. Si necesitas cerrar la página de creación de sincronización, haz clic en **Save as draft** para guardar tu progreso.
{% endalert %}

#### Paso 3.2: Añadir preferencias de notificación
Introduce la(s) dirección(es) de correo electrónico de contacto para notificaciones de errores de sincronización. Braze utiliza esta información de contacto para enviar notificaciones sobre errores de integración, como la pérdida inesperada de acceso a la tabla.

Los correos de contacto solo reciben notificaciones de errores globales o a nivel de sincronización, como tablas faltantes, permisos y otros. No reciben problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que las sincronizaciones se ejecuten.

Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos

(Solo para sincronizaciones de catálogos) El nivel del catálogo no tiene espacio

#### Paso 3.3: Programación
Por último, configura tu sincronización como no recurrente o recurrente.

Las sincronizaciones no recurrentes se pueden activar manualmente o a través de la API.

Las sincronizaciones recurrentes pueden tener una frecuencia desde cada 15 minutos hasta una vez al mes. Braze programa la sincronización recurrente en la zona horaria UTC.

{% endtab %}

{% tab BigQuery %}

#### Paso 3.1: Configurar los detalles de la sincronización y probar la conexión
Elige un nombre para tu sincronización. Luego, selecciona cualquier origen activo e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y haz clic en **Test Connection**.

Una vez exitosa, aparece una vista previa de los datos. Selecciona **Next: Notifications** para continuar. Si la conexión falla, aparece un mensaje de error para ayudar a solucionar el problema.

{% alert note %}
Debes probar con éxito una sincronización antes de avanzar a los siguientes pasos. Si necesitas cerrar la página de creación de sincronización, haz clic en **Save as draft** para guardar tu progreso.
{% endalert %}

#### Paso 3.2: Añadir preferencias de notificación
Introduce la(s) dirección(es) de correo electrónico de contacto para notificaciones de errores de sincronización. Braze utiliza esta información de contacto para enviar notificaciones sobre errores de integración, como la pérdida inesperada de acceso a la tabla.

Los correos de contacto solo reciben notificaciones de errores globales o a nivel de sincronización, como tablas faltantes, permisos y otros. No reciben problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que las sincronizaciones se ejecuten. Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos

(Solo para sincronizaciones de catálogos) El nivel del catálogo no tiene espacio

#### Paso 3.3: Programación
Por último, configura tu sincronización como no recurrente o recurrente.

Las sincronizaciones no recurrentes se pueden activar manualmente o a través de la API.

Las sincronizaciones recurrentes pueden tener una frecuencia desde cada 15 minutos hasta una vez al mes. Braze programa la sincronización recurrente en la zona horaria UTC.

{% endtab %}

{% tab Databricks %}

#### Paso 3.1: Configurar los detalles de la sincronización y probar la conexión
Elige un nombre para tu sincronización. Luego, selecciona cualquier origen activo e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y haz clic en **Test Connection**.

Una vez exitosa, aparece una vista previa de los datos. Selecciona **Next: Notifications** para continuar. Si la conexión falla, aparece un mensaje de error para ayudar a solucionar el problema.

{% alert note %}
Debes probar con éxito una sincronización antes de avanzar a los siguientes pasos. Si necesitas cerrar la página de creación de sincronización, haz clic en **Save as draft** para guardar tu progreso.
{% endalert %}

#### Paso 3.2: Añadir preferencias de notificación
Introduce la(s) dirección(es) de correo electrónico de contacto para notificaciones de errores de sincronización. Braze utiliza esta información de contacto para enviar notificaciones sobre errores de integración, como la pérdida inesperada de acceso a la tabla.

Los correos de contacto solo reciben notificaciones de errores globales o a nivel de sincronización, como tablas faltantes, permisos y otros. No reciben problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que las sincronizaciones se ejecuten.

Estos problemas pueden incluir lo siguiente:
- Problemas de conectividad
- Falta de recursos
- Problemas de permisos

(Solo para sincronizaciones de catálogos) El nivel del catálogo no tiene espacio

#### Paso 3.3: Programación
Por último, configura tu sincronización como no recurrente o recurrente.

Las sincronizaciones no recurrentes se pueden activar manualmente o a través de la API.

Las sincronizaciones recurrentes pueden tener una frecuencia desde cada 15 minutos hasta una vez al mes. Braze programa la sincronización recurrente en la zona horaria UTC.

{% endtab %}
{% tab Microsoft Fabric %}

#### Paso 3.1: Configurar los detalles de la sincronización y probar la conexión

Elige un nombre para tu sincronización. Luego, selecciona cualquier origen activo e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y haz clic en **Test Connection**.

Una vez exitosa, aparece una vista previa de los datos. Selecciona **Next: Notifications** para continuar. Si la conexión falla, aparece un mensaje de error para ayudar a solucionar el problema.

{% alert note %}
Debes probar con éxito una sincronización antes de avanzar a los siguientes pasos. Si necesitas cerrar la página de creación de sincronización, haz clic en **Save as draft** para guardar tu progreso.
{% endalert %}

#### Paso 3.2: Añadir preferencias de notificación
Introduce la(s) dirección(es) de correo electrónico de contacto para notificaciones de errores de sincronización. Braze utiliza esta información de contacto para enviar notificaciones sobre errores de integración, como la pérdida inesperada de acceso a la tabla.

Los correos de contacto solo reciben notificaciones de errores globales o a nivel de sincronización, como tablas faltantes, permisos y otros. No reciben problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que las sincronizaciones se ejecuten.

Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos

(Solo para sincronizaciones de catálogos) El nivel del catálogo no tiene espacio

#### Paso 3.3: Programación
Por último, configura tu sincronización como no recurrente o recurrente.

Las sincronizaciones no recurrentes se pueden activar manualmente o a través de la API.

Las sincronizaciones recurrentes pueden tener una frecuencia desde cada 15 minutos hasta una vez al mes. Braze programa la sincronización recurrente en la zona horaria UTC.

{% endtab %}
{% endtabs %}

{% alert note %}
Debes probar con éxito una integración antes de que pueda pasar del estado Borrador al estado Activo. Si cierras la página de creación, tu integración se guarda y puedes volver a la página de detalles para hacer cambios y probar.
{% endalert %}

## Configurar integraciones o usuarios adicionales (opcional) {#set-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Puedes configurar múltiples integraciones con Braze, pero cada integración debe estar configurada para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Snowflake.

Si reutilizas el mismo usuario y rol en todas las integraciones, no necesitas volver a añadir la clave pública.
{% endtab %}
{% tab Redshift %}
Puedes configurar múltiples integraciones con Braze, pero cada integración debe estar configurada para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Snowflake o Redshift.

Si reutilizas el mismo usuario en todas las integraciones, no puedes eliminar el usuario en el panel de Braze hasta que se haya eliminado de todas las sincronizaciones activas.
{% endtab %}
{% tab BigQuery %}

Puedes configurar múltiples integraciones con Braze, pero cada integración debe estar configurada para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de BigQuery.

Si reutilizas el mismo usuario en todas las integraciones, no puedes eliminar el usuario en el panel de Braze hasta que se haya eliminado de todas las sincronizaciones activas.

{% endtab %}
{% tab Databricks %}

Puedes configurar múltiples integraciones con Braze, pero cada integración debe estar configurada para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Databricks.

Si reutilizas el mismo usuario en todas las integraciones, no puedes eliminar el usuario en el panel de Braze hasta que se haya eliminado de todas las sincronizaciones activas.

{% endtab %}
{% tab Microsoft Fabric %}

Puedes configurar múltiples integraciones con Braze, pero cada integración debe estar configurada para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Fabric.

Si reutilizas el mismo usuario en todas las integraciones, no puedes eliminar el usuario en el panel de Braze hasta que se haya eliminado de todas las sincronizaciones activas.

{% endtab %}
{% endtabs %}

## Ejecución de la sincronización {#running-the-sync}

{% tabs %}
{% tab Snowflake %}
Cuando se activa, tu sincronización se ejecuta según el programa configurado durante la configuración. Si deseas ejecutar la sincronización fuera del programa de pruebas normal o para obtener los datos más recientes, selecciona **Sync Now**. Esta ejecución no afecta a las futuras sincronizaciones programadas de forma regular.

{% endtab %}
{% tab Redshift %}
Cuando se activa, tu sincronización se ejecuta según el programa configurado durante la configuración. Si deseas ejecutar la sincronización fuera del programa de pruebas normal o para obtener los datos más recientes, selecciona **Sync Now**. Esta ejecución no afecta a las futuras sincronizaciones programadas de forma regular.

{% endtab %}
{% tab BigQuery %}

Cuando se activa, tu sincronización se ejecuta según el programa configurado durante la configuración. Si deseas ejecutar la sincronización fuera del programa de pruebas normal o para obtener los datos más recientes, selecciona **Sync Now**. Esta ejecución no afecta a las futuras sincronizaciones programadas de forma regular.

{% endtab %}
{% tab Databricks %}

Cuando se activa, tu sincronización se ejecuta según el programa configurado durante la configuración. Si deseas ejecutar la sincronización fuera del programa de pruebas normal o para obtener los datos más recientes, selecciona **Sync Now**. Esta ejecución no afecta a las futuras sincronizaciones programadas de forma regular.

{% endtab %}
{% tab Microsoft Fabric %}

Cuando se activa, tu sincronización se ejecuta según el programa configurado durante la configuración. Si deseas ejecutar la sincronización fuera del programa de pruebas normal o para obtener los datos más recientes, selecciona **Sync Now**. Esta ejecución no afecta a las futuras sincronizaciones programadas de forma regular.

{% endtab %}

{% endtabs %}