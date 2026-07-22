---
nav_title: Fuentes conectadas
article_title: Fuentes conectadas
description: "Esta página explica cómo utilizar la ingesta de datos en la nube de Braze para sincronizar datos relevantes con tu integración de Snowflake, Redshift, BigQuery y Databricks."
page_order: 2
page_type: reference

---

# Fuentes conectadas {#connected-sources}

> Las fuentes conectadas son una alternativa de copia cero a la sincronización directa de datos con la función de ingesta de datos en la nube (CDI) de Braze. Una fuente conectada consulta directamente tu almacén de datos para crear nuevos segmentos sin copiar ninguno de los datos subyacentes a Braze.

Después de añadir una fuente conectada a tu espacio de trabajo de Braze, puedes crear un segmento CDI dentro de las extensiones de segmento. Las extensiones de segmento CDI te permiten escribir SQL que consulta directamente tu almacén de datos (utilizando los datos disponibles a través de tu fuente conectada CDI) y crea y mantiene un grupo de usuarios a los que puedes dirigirte dentro de Braze.

Para obtener más información sobre cómo crear un segmento con esta fuente, consulta [Extensiones de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).

{% alert warning %}
Dado que las fuentes conectadas se ejecutan directamente en tu almacén de datos, incurrirás en todos los costes asociados a la ejecución de estas consultas en tu almacén de datos. Las fuentes conectadas no registran puntos de datos y las extensiones de segmento CDI no consumen créditos de segmento SQL.
{% endalert %}

## Integración de fuentes conectadas {#integrating-connected-sources}

### Paso 1: Conecta tus recursos {#step-1-connect-your-resources}

Las fuentes conectadas de Cloud Data Ingestion requieren cierta configuración en Braze y en tu instancia. Sigue estos pasos para configurar la integración&#8722;algunos pasos se realizarán en tu almacén de datos y otros se realizarán en tu panel de Braze.

{% tabs %}
{% tab Snowflake %}
**En tu almacén de datos**
1. Crea un rol y otorga permisos para consultar y crear tablas en un esquema.
2. Configura tu almacén y da acceso a ese rol.
3. Crea un usuario para ese rol.
4. Dependiendo de tu configuración, es posible que necesites permitir las IP de Braze en tu política de red de Snowflake.

**En el panel de Braze**

{: start="5"}
5. Crea una nueva fuente conectada en el panel de Braze.
6. Configura los detalles de sincronización para la fuente conectada.
7. Recupera la clave pública proporcionada en el panel de Braze.

**En tu almacén de datos**

{: start="8"}
8. Añade la clave pública del panel de Braze al [usuario de Snowflake para autenticación](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Cuando hayas terminado, puedes usar la fuente conectada para crear una o más extensiones de segmento CDI.
{% endtab %}

{% tab Redshift %}
1. Configura los datos de origen y los recursos necesarios en tu entorno de Redshift.
2. Crea una nueva fuente conectada en el panel de Braze.
3. Prueba la integración.
4. Usa la fuente conectada para crear una o más extensiones de segmento CDI.
{% endtab %}

{% tab BigQuery %}
1. Configura los datos de origen y los recursos necesarios en tu entorno de BigQuery.
2. Crea una cuenta de servicio y permite el acceso a los proyectos y conjuntos de datos de BigQuery que contienen los datos que deseas sincronizar.
3. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Usa la fuente conectada para crear una o más extensiones de segmento CDI.
{% endtab %}

{% tab Databricks %}
1. Configura los datos de origen y los recursos necesarios en tu entorno de Databricks.
2. Crea una cuenta de servicio y permite el acceso a los proyectos y conjuntos de datos de Databricks que contienen los datos que deseas sincronizar.
3. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Usa la fuente conectada para crear una o más extensiones de segmento CDI.

{% alert important %}
Puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecta a instancias SQL Classic y Pro, lo que provocará retrasos durante la configuración y prueba de la conexión, así como durante la creación y actualización de extensiones de segmento CDI. Usar una instancia SQL serverless minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede resultar en costos de integración ligeramente más altos.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Crea un principal de servicio y permite el acceso al espacio de trabajo de Fabric que se utilizará para tu integración.
2. En tu espacio de trabajo de Fabric, configura los datos de origen y otorga permisos a tu principal de servicio.
3. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Usa la fuente conectada para crear una o más extensiones de segmento CDI.
{% endtab %}

{% endtabs %}

### Paso 2: Configura tu almacén de datos {#step-2-set-up-your-data-warehouse}

Configura los datos de origen y los recursos necesarios en tu entorno de almacén de datos. La fuente conectada puede hacer referencia a una o más tablas, así que asegúrate de que tu usuario de Braze tenga permiso para acceder a todas las tablas que desees en la fuente conectada.

{% tabs %}
{% tab Snowflake %}
#### Paso 2.1: Crea un rol y otorga permisos {#step-21-create-a-role-and-grant-permissions}

Crea un rol para que lo use tu fuente conectada. Este rol se utilizará para generar la lista de tablas disponibles en tus extensiones de segmento CDI y para consultar tablas de origen con el fin de crear nuevos segmentos. Después de crear la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de origen.

Puedes optar por otorgar acceso a todas las tablas de un esquema, o conceder privilegios solo a tablas específicas. Las tablas a las que el rol de Braze tenga acceso estarán disponibles para consultar en la extensión de segmento CDI.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de tu extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, y la tabla solo persistirá mientras Braze esté actualizando el segmento.

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### Paso 2.2: Configura el almacén y da acceso al rol de Braze {#step-22-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
El almacén necesita tener activada la opción **auto-resume**. Si no lo está, deberás otorgar a Braze privilegios adicionales de `OPERATE` en el almacén para que Braze pueda activarlo cuando sea momento de ejecutar la consulta.
{% endalert %}

#### Paso 2.3: Configura el usuario {#step-23-set-up-the-user}
```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Compartirás la información de conexión con Braze y recibirás una clave pública para añadir al usuario en un paso posterior.

{% alert note %}
Al conectar diferentes espacios de trabajo a la misma cuenta de Snowflake, debes crear un usuario único para cada espacio de trabajo de Braze donde estés creando una integración. Dentro de un espacio de trabajo, puedes reutilizar el mismo usuario en distintas integraciones, pero la creación de la integración fallará si un usuario en la misma cuenta de Snowflake está duplicado en varios espacios de trabajo.
{% endalert %}

#### Paso 2.4: Permite las IP de Braze en tu política de red de Snowflake (opcional) {#step-24-allow-braze-ips-in-your-snowflake-network-policy-optional}

Dependiendo de la configuración de tu cuenta de Snowflake, es posible que necesites permitir las siguientes direcciones IP en tu política de red de Snowflake. Para más información sobre cómo hacerlo, consulta la documentación relevante de Snowflake sobre [modificar una política de red](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Paso 2.1: Crea un usuario y otorga permisos {#step-21-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Crea un usuario para que lo use tu fuente conectada. Este usuario se utilizará para generar la lista de tablas disponibles en tus extensiones de segmento CDI y para consultar tablas de origen con el fin de crear nuevos segmentos. Después de crear la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de origen. Si creas múltiples integraciones CDI, es posible que desees otorgar permisos a un esquema o gestionar permisos usando un grupo.

Puedes optar por otorgar acceso a todas las tablas de un esquema, o conceder privilegios solo a tablas específicas. Las tablas a las que el rol de Braze tenga acceso estarán disponibles para consultar en la extensión de segmento CDI. Asegúrate de otorgar acceso a cualquier tabla nueva al usuario cuando se creen, o establece permisos predeterminados para el usuario.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de tu extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, que solo persistirá mientras Braze actualice el segmento.


#### Paso 2.2: Permite el acceso a las IP de Braze {#step-22-allow-access-to-braze-ips}

Si tienes un firewall u otras políticas de red, debes dar a Braze acceso de red a tu instancia de Redshift. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.

También es posible que necesites cambiar tus grupos de seguridad para permitir el acceso de Braze a tus datos en Redshift. Asegúrate de permitir explícitamente el tráfico entrante en las IP de la siguiente sección y en el puerto utilizado para consultar tu clúster de Redshift (el predeterminado es 5439). Debes permitir explícitamente la conectividad TCP de Redshift en este puerto incluso si las reglas de entrada están configuradas como "permitir todo". Además, es importante que el endpoint del clúster de Redshift sea accesible públicamente para que Braze pueda conectarse a tu clúster.

Si no deseas que tu clúster de Redshift sea accesible públicamente, puedes configurar una VPC y una instancia EC2 para usar un túnel SSH para acceder a los datos de Redshift. Para más información, consulta [AWS: ¿Cómo accedo a un clúster privado de Amazon Redshift desde mi máquina local?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Paso 2.1: Crea una cuenta de servicio y otorga permisos {#step-21-create-a-service-account-and-grant-permissions}

Crea una cuenta de servicio en GCP para que Braze la use para conectarse y leer datos de tus tablas. La cuenta de servicio debe tener los siguientes permisos:

- **BigQuery Connection User:** Permite a Braze realizar conexiones.
- **BigQuery User:** Proporciona a Braze acceso para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- **BigQuery Data Viewer:** Proporciona a Braze acceso para ver conjuntos de datos y su contenido.
- **BigQuery Job User:** Proporciona a Braze acceso para ejecutar trabajos.
- **bigquery.tables.create** Proporciona a Braze acceso para crear tablas temporales durante la actualización de segmentos.

Crea una cuenta de servicio para que la use tu fuente conectada. Este usuario se utilizará para generar la lista de tablas disponibles en tus extensiones de segmento CDI y para consultar tablas de origen con el fin de crear nuevos segmentos. Después de crear la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de origen.

Puedes optar por otorgar acceso a todas las tablas de un conjunto de datos, o conceder privilegios solo a tablas específicas. Las tablas a las que el rol de Braze tenga acceso estarán disponibles para consultar en la extensión de segmento CDI.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de tu extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, y la tabla solo persistirá mientras Braze esté actualizando el segmento.

Después de crear la cuenta de servicio y otorgar permisos, genera una clave JSON. Para más información, consulta [Google Cloud: Crear y eliminar claves de cuentas de servicio](https://cloud.google.com/iam/docs/keys-create-delete). La subirás al panel de Braze más adelante.

#### Paso 2.2: Permite el acceso a las IP de Braze

Si tienes políticas de red implementadas, debes dar a Braze acceso de red a tu instancia de BigQuery. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Paso 2.1: Crea un token de acceso {#step-21-create-an-access-token}

Para que Braze acceda a Databricks, es necesario crear un token de acceso personal.

1. En tu espacio de trabajo de Databricks, selecciona tu nombre de usuario de Databricks en la barra superior y luego selecciona **User Settings** en el menú desplegable.
2. Asegúrate de que la cuenta de servicio tenga privilegios de `CREATE TABLE` en el esquema utilizado para la fuente conectada.
3. En la pestaña **Access tokens**, selecciona **Generate new token**.
4. Introduce un comentario que te ayude a identificar este token, como "Braze CDI", y cambia la vida útil del token a sin límite dejando el campo Lifetime (days) vacío (en blanco).
5. Selecciona **Generate**.
6. Copia el token mostrado y luego selecciona **Done**.

Este token se utilizará para generar la lista de tablas disponibles en tus extensiones de segmento CDI y para consultar tablas de origen con el fin de crear nuevos segmentos. Después de crear la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de origen.

Puedes optar por otorgar acceso a todas las tablas de un esquema, o conceder privilegios solo a tablas específicas. Las tablas a las que el rol de Braze tenga acceso estarán disponibles para consultar en la extensión de segmento CDI.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de tu extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, que solo persistirá mientras Braze actualice el segmento.

Guarda el token en un lugar seguro hasta que necesites ingresarlo en el panel de Braze durante el paso de creación de credenciales.

#### Paso 2.2: Permite el acceso a las IP de Braze

Si tienes políticas de red implementadas, debes dar a Braze acceso de red a tu instancia de Databricks. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Paso 2.1: Otorga acceso a los recursos de Fabric {#step-21-grant-access-to-fabric-resources}
Braze se conectará a tu almacén de Fabric usando un principal de servicio con autenticación de Entra ID. Crearás un nuevo principal de servicio para que Braze lo use y otorgarás acceso a los recursos de Fabric según sea necesario. Braze necesitará los siguientes datos para conectarse:

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azure no permite caducidad ilimitada en los secretos de principales de servicio. Recuerda actualizar las credenciales antes de que caduquen para mantener el flujo de datos hacia Braze.
{% endalert %}

#### Paso 2.2: Otorga acceso a los recursos de Fabric {#step-22-grant-access-to-fabric-resources}
Proporcionarás acceso para que Braze se conecte a tu instancia de Fabric. En tu portal de administración de Fabric, navega a **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* En **Developer settings** habilita "Service principals can use Fabric APIs" para que Braze pueda conectarse usando Microsoft Entra ID.
* En **OneLake settings** habilita "Users can access data stored in OneLake with apps external to Fabric" para que el principal de servicio pueda acceder a datos desde una aplicación externa.

#### Paso 2.3: Obtén la cadena de conexión del almacén {#step-23-get-warehouse-connection-string}

Necesitarás el endpoint SQL de tu almacén para que Braze pueda conectarse. Para recuperar el endpoint SQL, ve al **espacio de trabajo** en Fabric y, en la lista de elementos, pasa el cursor sobre el nombre del almacén y selecciona **Copy SQL connection string**.
Mantén este valor disponible para la configuración de credenciales en el paso 3.

#### Paso 2.4: Permite las IP de Braze en el firewall (opcional) {#step-24-allow-braze-ips-in-firewall-optional}

Dependiendo de la configuración de tu cuenta de Microsoft Fabric, es posible que necesites permitir las siguientes direcciones IP en tu firewall para permitir el tráfico desde Braze. Para más información sobre cómo habilitar esto, consulta la documentación relevante sobre [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Paso 3: Crea una fuente conectada en el panel de Braze {#step-3-create-a-connected-source-in-the-braze-dashboard}

{% tabs %}
{% tab Snowflake %}
#### Paso 3.1: Añade la información de conexión de Snowflake y la tabla de origen {#step-31-add-snowflake-connection-information-and-source-table}

Crea una fuente conectada en el panel de Braze. Ve a **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, selecciona **Add data source** y luego selecciona **Snowflake**.

En **Setup source**, introduce lo siguiente:
- **Credentials:** **Account Locator**, **Username** y **Role**
- **Configuration:** **Warehouse**, **Database** y **Schema**

Si estás creando nuevas credenciales de Snowflake, selecciona **Save credentials and generate RSA key** antes de probar la conexión.

#### Paso 3.2: Configura los detalles de sincronización {#step-32-configure-sync-details}

Elige un nombre para la fuente conectada. Este nombre se usará en la lista de fuentes disponibles cuando crees una nueva extensión de segmento CDI.

Configura un tiempo máximo de ejecución para esta fuente. Braze cancelará automáticamente cualquier consulta que exceda el tiempo máximo de ejecución. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución menor reducirá los costos incurridos en tu cuenta de Snowflake. Esta configuración se aplica a las consultas ejecutadas a través de esta fuente, incluyendo sincronizaciones y extensiones de segmento CDI que la utilicen.

{% alert note %}
Si las consultas se agotan constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de tus consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

#### Paso 3.3: Anota la clave pública {#step-33-note-the-public-key}

En el paso **Test connection**, toma nota de la clave pública RSA. La necesitarás para completar la integración en Snowflake.

{% endtab %}
{% tab Redshift %}
#### Paso 3.1: Añade la información de conexión de Redshift y la tabla de origen {#step-31-add-redshift-connection-information-and-source-table}

Crea una fuente conectada en el panel de Braze. Ve a **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, selecciona **Add data source** y luego selecciona **Amazon Redshift**.

En **Setup source**, introduce lo siguiente:
- **Credentials:** **Redshift Host URL**, **Username**, **Password** y **Port**
- **Configuration:** **Database** y **Schema**

Si es necesario, habilita **Connect with SSH Tunnel** e introduce **Tunnel Host**, **Tunnel Port** y **Tunnel Username**.

#### Paso 3.2: Configura los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se usará en la lista de fuentes disponibles cuando crees una nueva extensión de segmento CDI.

Configura un tiempo máximo de ejecución para esta fuente. Braze cancelará automáticamente cualquier consulta que exceda el tiempo máximo de ejecución. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución menor reducirá los costos incurridos en tu cuenta de Redshift.
Esta configuración se aplica a las consultas ejecutadas a través de esta fuente, incluyendo sincronizaciones y extensiones de segmento CDI que la utilicen.

{% alert note %}
Si las consultas se agotan constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de tus consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

#### Paso 3.3: Anota la clave pública (opcional) {#step-33-note-the-public-key-optional}

Si tus credenciales tienen **Connect with SSH Tunnel** seleccionado, toma nota de la clave pública RSA en el paso **Test connection**. La necesitarás para completar la integración en Redshift.

{% endtab %}
{% tab BigQuery %}
#### Paso 3.1: Añade la información de conexión de BigQuery y la tabla de origen {#step-31-add-bigquery-connection-information-and-source-table}

Crea una fuente conectada en el panel de Braze. Ve a **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, selecciona **Add data source** y luego selecciona **Google BigQuery**.

En **Setup source**, introduce lo siguiente:
- **Credentials:** **Credential name** y sube tu **JSON key**
- **Configuration:** **Project** y **Dataset**

#### Paso 3.2: Configura los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se usará en la lista de fuentes disponibles cuando crees una nueva extensión de segmento CDI.

Configura un tiempo máximo de ejecución para esta fuente. Braze cancelará automáticamente cualquier consulta que exceda el tiempo máximo de ejecución. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución menor reducirá los costos incurridos en tu cuenta de BigQuery. Esta configuración se aplica a las consultas ejecutadas a través de esta fuente, incluyendo sincronizaciones y extensiones de segmento CDI que la utilicen.

{% alert note %}
Si las consultas se agotan constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de tus consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

#### Paso 3.3: Prueba la conexión {#step-33-test-the-connection}

Selecciona **Test Connection** para verificar que la lista de tablas visibles para el usuario sea la que esperas, y luego selecciona **Done**. Tu fuente conectada ya está creada y lista para usar en extensiones de segmento CDI.

{% endtab %}
{% tab Databricks %}
#### Paso 3.1: Añade la información de conexión de Databricks y la tabla de origen {#step-31-add-databricks-connection-information-and-source-table}

Crea una fuente conectada en el panel de Braze. Ve a **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, selecciona **Add data source** y luego selecciona **Databricks**.

En **Setup source**, introduce lo siguiente:
- **Credentials:** **Credential Name**, **Hostname**, **HTTP Path** y **Access Token**
- **Configuration:** **Catalog** y **Schema**

#### Paso 3.2: Configura los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se usará en la lista de fuentes disponibles cuando crees una nueva extensión de segmento CDI.

Configura un tiempo máximo de ejecución para esta fuente. Braze cancelará automáticamente cualquier consulta que exceda el tiempo máximo de ejecución. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución menor reducirá los costos incurridos en tu cuenta de Databricks. Esta configuración se aplica a las consultas ejecutadas a través de esta fuente, incluyendo sincronizaciones y extensiones de segmento CDI que la utilicen.

{% alert note %}
Si las consultas se agotan constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de tus consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

#### Paso 3.3: Prueba la conexión

Selecciona **Test Connection** para verificar que la lista de tablas visibles para el usuario sea la que esperas, y luego selecciona **Done**. Tu fuente conectada ya está creada y lista para usar en extensiones de segmento CDI.

{% endtab %}
{% tab Microsoft Fabric %}
#### Paso 3.1: Añade la información de conexión de Microsoft Fabric y la tabla de origen {#step-31-add-microsoft-fabric-connection-information-and-source-table}

Crea una fuente conectada en el panel de Braze. Ve a **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, selecciona **Add data source** y luego selecciona **Microsoft Fabric**.

En **Setup source**, introduce lo siguiente:
- **Credentials:** **Credentials Name**, **Tenant ID**, **Principal ID**, **Client Secret** y **Connection String**
- **Configuration:** **Database** y **Schema**

Si **Connect with SSH Tunnel** está disponible en tu espacio de trabajo y es necesario para tu configuración, introduce también **Tunnel Host**, **Tunnel Port** y **Tunnel Username**.

#### Paso 3.2: Configura los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se usará en la lista de fuentes disponibles cuando crees una nueva extensión de segmento CDI.

Configura un tiempo máximo de ejecución para esta fuente. Braze cancelará automáticamente cualquier consulta que exceda el tiempo máximo de ejecución. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución menor reducirá los costos incurridos en tu cuenta de Microsoft Fabric. Esta configuración se aplica a las consultas ejecutadas a través de esta fuente, incluyendo sincronizaciones y extensiones de segmento CDI que la utilicen.

{% alert note %}
Si las consultas se agotan constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de tus consultas o escalar la capacidad de Fabric.
{% endalert %}

#### Paso 3.3: Prueba la conexión

Selecciona **Test Connection** para verificar que la lista de tablas visibles para el usuario sea la que esperas, y luego selecciona **Done**. Tu fuente conectada ya está creada y lista para usar en extensiones de segmento CDI.

{% endtab %}
{% endtabs %}

### Paso 4: Finaliza la configuración del almacén de datos {#step-4-finalize-the-data-warehouse-configuration}

{% tabs %}
{% tab Snowflake %}
Añade la clave pública que anotaste durante el último paso a tu usuario en Snowflake. Esto permitirá que Braze se conecte a Snowflake. Para más detalles sobre cómo hacerlo, consulta la [documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).

Si deseas rotar las claves en algún momento, puedes crear una nueva clave pública yendo a **Data Access Management** en **Cloud Data Ingestion** y seleccionando **Generate New Key** para la cuenta correspondiente.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Después de añadir la clave al usuario en Snowflake, selecciona **Test Connection** en Braze y luego selecciona **Done**. Tu fuente conectada ya está creada y lista para usar en extensiones de segmento CDI.
{% endtab %}

{% tab Redshift %}
Si te conectas con un túnel SSH, añade la clave pública que anotaste durante el último paso al usuario del túnel SSH.

Después de añadir la clave al usuario, selecciona **Test Connection** en Braze y luego selecciona **Done**. Tu fuente conectada ya está creada y lista para usar en extensiones de segmento CDI.

{% endtab %}
{% tab BigQuery %}
Esto no aplica para BigQuery.

{% endtab %}
{% tab Databricks %}
Esto no aplica para Databricks.

{% endtab %}
{% tab Microsoft Fabric %}
Esto no aplica para Microsoft Fabric.

{% endtab %}
{% endtabs %}

{% alert note %}
Debes probar exitosamente una fuente antes de que pueda pasar del estado "borrador" al estado "activo". Si necesitas cerrar la página de creación, tu integración se guardará y podrás volver a la página de detalles para hacer cambios y probar.
{% endalert %}

## Configuración de integraciones o usuarios adicionales (opcional) {#setting-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Puedes configurar múltiples integraciones con Braze, pero cada integración debe estar configurada para conectarse a un esquema diferente. Al crear conexiones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Snowflake.

Si reutilizas el mismo usuario y rol en todas las integraciones, no necesitarás añadir la clave pública de nuevo.
{% endtab %}

{% tab Redshift %}
Puedes configurar múltiples orígenes de datos con Braze, pero cada origen debe estar configurado para conectarse a un esquema diferente. Al crear orígenes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Redshift.
{% endtab %}

{% tab BigQuery %}
Puedes configurar múltiples orígenes de datos con Braze, pero cada origen debe estar configurado para conectarse a un conjunto de datos diferente. Al crear orígenes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de BigQuery.
{% endtab %}

{% tab Databricks %}
Puedes configurar múltiples orígenes de datos con Braze, pero cada origen debe estar configurado para conectarse a un esquema diferente. Al crear orígenes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Databricks.
{% endtab %}

{% tab Microsoft Fabric %}
Puedes configurar múltiples orígenes de datos con Braze, pero cada origen debe estar configurado para conectarse a un esquema diferente. Al crear orígenes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Azure.
{% endtab %}
{% endtabs %}

## Uso del origen conectado {#using-the-connected-source}

Después de crear el origen, puedes utilizarlo para crear una o más extensiones de segmento CDI. Para más información sobre cómo crear un segmento con este origen, consulta la [documentación de extensiones de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).

{% alert note %}
Si las consultas agotan el tiempo de espera de forma constante y has establecido un tiempo máximo de ejecución de 60 minutos, considera optimizar el tiempo de ejecución de tus consultas o dedicar más recursos de cómputo (como un almacén de datos más grande) al usuario de Braze.
{% endalert %}