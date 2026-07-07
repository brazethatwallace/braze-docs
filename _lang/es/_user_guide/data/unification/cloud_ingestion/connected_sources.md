---
nav_title: Fuentes conectadas
article_title: Fuentes conectadas
description: "Esta página explica cómo utilizar la Ingesta de datos de Cloud de Braze para sincronizar datos relevantes con tu integración de Snowflake, Redshift, BigQuery y Databricks."
page_order: 2
page_type: reference

---

# Fuentes conectadas {#connected-sources}

> Las fuentes conectadas son una alternativa de copia cero a la sincronización directa de datos con la función de Ingesta de datos de Cloud (CDI) de Braze. Una fuente conectada consulta directamente tu almacén de datos para crear nuevos segmentos sin copiar ninguno de los datos subyacentes a Braze.

Después de añadir una fuente conectada a tu espacio de trabajo de Braze, puedes crear un segmento CDI dentro de las Extensiones de segmento. Las Extensiones de segmento CDI te permiten escribir SQL que consulta directamente tu almacén de datos (utilizando los datos disponibles a través de tu fuente conectada CDI) y crea y mantiene un grupo de usuarios a los que puedes dirigirte dentro de Braze.

Para obtener más información sobre cómo crear un segmento con esta fuente, consulta [Extensiones de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).

{% alert warning %}
Dado que las fuentes conectadas se ejecutan directamente en tu almacén de datos, incurrirás en todos los costes asociados a la ejecución de estas consultas en tu almacén de datos. Las fuentes conectadas no registran puntos de datos y las Extensiones de segmento CDI no consumen créditos de segmento SQL.
{% endalert %}

## Integración de fuentes conectadas {#integrating-connected-sources}

### Paso 1: Conecta tus recursos {#step-1-connect-your-resources}

Las fuentes conectadas de Ingesta de datos de Cloud requieren cierta configuración en Braze y en tu instancia. Sigue estos pasos para configurar la integración&#8722;algunos pasos se realizarán en tu almacén de datos y otros en el panel de Braze.

{% tabs %}
{% tab Snowflake %}
**En tu almacén de datos**
1. Crea un rol y otorga permisos para consultar y crear tablas en un esquema.
2. Configura tu almacén y da acceso a ese rol.
3. Crea un usuario para ese rol.
4. Dependiendo de tu configuración, puede que necesites permitir las IP de Braze en tu política de red de Snowflake.

**En el panel de Braze**

{: start="5"}
5. Crea una nueva fuente conectada en el panel de Braze.
6. Configura los detalles de sincronización de la fuente conectada.
7. Recupera la clave pública proporcionada en el panel de Braze.

**En tu almacén de datos**

{: start="8"}
8. Añade la clave pública del panel de Braze al [usuario de Snowflake para la autenticación](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Cuando hayas terminado, puedes utilizar la fuente conectada para crear una o varias Extensiones de segmento CDI.
{% endtab %}

{% tab Redshift %}
1. Configura los datos de origen y los recursos necesarios en tu entorno de Redshift.
2. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Utiliza la fuente conectada para crear una o varias Extensiones de segmento CDI.
{% endtab %}

{% tab BigQuery %}
1. Configura los datos de origen y los recursos necesarios en tu entorno de BigQuery.
2. Crea una cuenta de servicio y permite el acceso a los proyectos y conjuntos de datos de BigQuery que contienen los datos que deseas sincronizar.
3. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Utiliza la fuente conectada para crear una o varias Extensiones de segmento CDI.
{% endtab %}

{% tab Databricks %}
1. Configura los datos de origen y los recursos necesarios en tu entorno de Databricks.
2. Crea una cuenta de servicio y permite el acceso a los proyectos y conjuntos de datos de Databricks que contienen los datos que deseas sincronizar.
3. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Utiliza la fuente conectada para crear una o varias Extensiones de segmento CDI.

{% alert important %}
Puede haber un tiempo de calentamiento de entre dos y cinco minutos cuando Braze se conecta a instancias Classic y Pro SQL, lo que provocará retrasos durante la configuración y las pruebas de conexión, así como durante la creación y actualización de las Extensiones de segmento CDI. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Crea un principal de servicio y permite el acceso al espacio de trabajo de Fabric que se utilizará para tu integración.
2. En tu espacio de trabajo de Fabric, configura los datos de origen y concede permisos a tu principal de servicio.
3. Crea una nueva fuente conectada en el panel de Braze.
4. Prueba la integración.
5. Utiliza la fuente conectada para crear una o varias Extensiones de segmento CDI.
{% endtab %}

{% endtabs %}

### Paso 2: Configura tu almacén de datos {#step-2-set-up-your-data-warehouse}

Configura los datos de origen y los recursos necesarios en tu entorno de almacén de datos. La fuente conectada puede hacer referencia a una o más tablas, así que asegúrate de que tu usuario de Braze tiene permiso para acceder a todas las tablas que quieras en la fuente conectada.

{% tabs %}
{% tab Snowflake %}
#### Paso 2.1: Crea un rol y concede permisos {#step-21-create-a-role-and-grant-permissions}

Crea un rol para que lo utilice tu fuente conectada. Este rol se utilizará para generar la lista de tablas disponibles en tus Extensiones de segmento CDI y para consultar las tablas de origen con el fin de crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente.

Puedes elegir conceder acceso a todas las tablas de un esquema, o conceder privilegios solo a tablas específicas. Las tablas a las que tenga acceso el rol de Braze estarán disponibles para consulta en las Extensiones de segmento CDI.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de la Extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, y la tabla solo persistirá mientras Braze esté actualizando el segmento.

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
El almacén debe tener activada la opción de **reanudación automática**. Si no lo está, tendrás que conceder a Braze privilegios adicionales de `OPERATE` en el almacén para que Braze lo active cuando llegue el momento de ejecutar la consulta.
{% endalert %}

#### Paso 2.3: Configura el usuario {#step-23-set-up-the-user}
```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Compartirás la información de conexión con Braze y recibirás una clave pública para añadir al usuario en un paso posterior.

{% alert note %}
Cuando conectes diferentes espacios de trabajo a la misma cuenta de Snowflake, debes crear un usuario único para cada espacio de trabajo de Braze en el que estés creando una integración. Dentro de un espacio de trabajo, puedes reutilizar el mismo usuario en todas las integraciones, pero la creación de la integración fallará si un usuario de la misma cuenta de Snowflake se duplica en distintos espacios de trabajo.
{% endalert %}

#### Paso 2.4: Permite las IP de Braze en tu política de red de Snowflake (opcional) {#step-24-allow-braze-ips-in-your-snowflake-network-policy-optional}

Dependiendo de la configuración de tu cuenta de Snowflake, puede que necesites permitir las siguientes direcciones IP en tu política de red de Snowflake. Para más información sobre cómo hacerlo, consulta la documentación correspondiente de Snowflake sobre la [modificación de una política de red](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Paso 2.1: Crea un usuario y concede permisos {#step-21-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Crea un usuario para que lo utilice tu fuente conectada. Este usuario se utilizará para generar la lista de tablas disponibles en tus Extensiones de segmento CDI y para consultar las tablas de origen con el fin de crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente. Si creas varias integraciones CDI, puede que desees conceder permisos a un esquema o gestionar los permisos mediante un grupo.

Puedes elegir conceder acceso a todas las tablas de un esquema, o conceder privilegios solo a tablas específicas. Las tablas a las que tenga acceso el rol de Braze estarán disponibles para consulta en las Extensiones de segmento CDI. Asegúrate de conceder acceso a las nuevas tablas al usuario cuando se creen, o establece permisos predeterminados para el usuario.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de la Extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, que solo persistirá mientras Braze actualice el segmento.


#### Paso 2.2: Permite el acceso a las IP de Braze {#step-22-allow-access-to-braze-ips}

Si tienes un cortafuegos u otras políticas de red, debes dar acceso de red a Braze a tu instancia de Redshift. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.

Es posible que también tengas que cambiar tus grupos de seguridad para permitir el acceso de Braze a tus datos en Redshift. Asegúrate de permitir explícitamente el tráfico entrante en las IP indicadas a continuación y en el puerto utilizado para consultar tu clúster de Redshift (por defecto es 5439). Debes permitir explícitamente la conectividad TCP de Redshift en este puerto incluso si las reglas de entrada están configuradas para "permitir todo". Además, es importante que el punto de conexión del clúster de Redshift sea de acceso público para que Braze pueda conectarse a tu clúster.

Si no quieres que tu clúster de Redshift sea de acceso público, puedes configurar una VPC y una instancia EC2 para que utilicen un túnel SSH para acceder a los datos de Redshift. Para más información, consulta [AWS: ¿Cómo accedo a un clúster privado de Amazon Redshift desde mi máquina local?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Paso 2.1: Crea una cuenta de servicio y concede permisos {#step-21-create-a-service-account-and-grant-permissions}

Crea una cuenta de servicio en GCP para que Braze la utilice para conectarse y leer datos de tus tablas. La cuenta de servicio debe tener los siguientes permisos:

- **BigQuery Connection User:** permite a Braze realizar conexiones.
- **BigQuery User:** proporciona a Braze acceso para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- **BigQuery Data Viewer:** proporciona a Braze acceso para ver conjuntos de datos y su contenido.
- **BigQuery Job User:** proporciona a Braze acceso para ejecutar trabajos.
- **bigquery.tables.create** proporciona a Braze acceso para crear tablas temporales durante la actualización de segmentos.

Crea una cuenta de servicio para que la utilice tu fuente conectada. Este usuario se utilizará para generar la lista de tablas disponibles en tus Extensiones de segmento CDI y para consultar las tablas de origen con el fin de crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente.

Puedes optar por conceder acceso a todas las tablas de un conjunto de datos, o conceder privilegios solo a tablas específicas. Las tablas a las que tenga acceso el rol de Braze estarán disponibles para consulta en las Extensiones de segmento CDI.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de la Extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, y la tabla solo persistirá mientras Braze esté actualizando el segmento.

Tras crear la cuenta de servicio y conceder los permisos, genera una clave JSON. Para más información, consulta [Google Cloud: Creación y eliminación de claves de cuentas de servicio](https://cloud.google.com/iam/docs/keys-create-delete). Más tarde la cargarás en el panel de Braze.

#### Paso 2.2: Permite el acceso a las IP de Braze

Si tienes políticas de red en vigor, debes dar acceso de red a Braze a tu instancia de BigQuery. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Paso 2.1: Crea un token de acceso {#step-21-create-an-access-token}

Para que Braze acceda a Databricks, es necesario crear un token de acceso personal.

1. En tu espacio de trabajo de Databricks, selecciona tu nombre de usuario de Databricks en la barra superior y, a continuación, selecciona **User Settings** en el desplegable.
2. Asegúrate de que la cuenta de servicio tenga privilegios de `CREATE TABLE` sobre el esquema utilizado para la fuente conectada.
3. En la pestaña **Access tokens**, selecciona **Generate new token**.
4. Introduce un comentario que te ayude a identificar este token, como "Braze CDI", y cambia la vida útil del token a sin vida útil dejando la casilla Lifetime (days) vacía (en blanco).
5. Selecciona **Generate**.
6. Copia el token mostrado y selecciona **Done**.

Este token se utilizará para generar la lista de tablas disponibles en tus Extensiones de segmento CDI y para consultar las tablas de origen con el fin de crear nuevos segmentos. Una vez creada la fuente conectada, Braze descubrirá los nombres y la descripción de todas las tablas disponibles para el usuario en el esquema de la fuente.

Puedes elegir conceder acceso a todas las tablas de un esquema, o conceder privilegios solo a tablas específicas. Las tablas a las que tenga acceso el rol de Braze estarán disponibles para consulta en las Extensiones de segmento CDI.

El permiso `create table` es necesario para que Braze pueda crear una tabla con los resultados de la consulta de la Extensión de segmento CDI antes de actualizar el segmento en Braze. Braze creará una tabla temporal por segmento, que solo persistirá mientras Braze actualice el segmento.

Guarda el token en un lugar seguro hasta que necesites introducirlo en el panel de Braze durante el paso de creación de credenciales.

#### Paso 2.2: Permite el acceso a las IP de Braze

Si tienes políticas de red en vigor, debes dar acceso de red a Braze a tu instancia de Databricks. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Paso 2.1: Concede acceso a los recursos de Fabric {#step-21-grant-access-to-fabric-resources}
Braze se conectará a tu almacén de Fabric utilizando un principal de servicio con autenticación Entra ID. Crearás un nuevo principal de servicio para que lo utilice Braze y concederás acceso a los recursos de Fabric según sea necesario. Braze necesitará los siguientes datos para conectarse:

* Tenant ID (también llamado directorio) de tu cuenta de Azure
* Principal ID (también llamado ID de aplicación) del principal de servicio
* Secreto de cliente para que Braze se autentique

1. En el portal de Azure, ve al centro de administración de Microsoft Entra y, a continuación, a **App Registrations**.
2. Selecciona **+ New registration** en **Identity > Applications > App registrations**.
3. Introduce un nombre y selecciona `Accounts in this organizational directory only` como tipo de cuenta admitido. A continuación, selecciona **Register**.
4. Selecciona la aplicación (principal de servicio) que acabas de crear y, a continuación, ve a **Certificates & secrets > + New client secret**.
5. Introduce una descripción para el secreto y establece un periodo de caducidad para el secreto. Después, selecciona **Add**.
6. Toma nota del secreto de cliente creado para utilizarlo en la configuración de Braze.

{% alert note %}
Azure no permite la caducidad ilimitada de los secretos de principal de servicio. Recuerda actualizar las credenciales antes de que caduquen para mantener el flujo de datos a Braze.
{% endalert %}

#### Paso 2.2: Concede acceso a los recursos de Fabric {#step-22-grant-access-to-fabric-resources}
Proporcionarás acceso para que Braze se conecte a tu instancia de Fabric. En tu portal de administración de Fabric, ve a **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* En **Developer settings**, habilita "Service principals can use Fabric APIs" para que Braze pueda conectarse utilizando Microsoft Entra ID.
* En **OneLake settings**, habilita "Users can access data stored in OneLake with apps external to Fabric" para que el principal de servicio pueda acceder a los datos desde una aplicación externa.

#### Paso 2.3: Obtén la cadena de conexión del almacén {#step-23-get-warehouse-connection-string}

Necesitarás el punto de conexión SQL de tu almacén para que Braze pueda conectarse. Para recuperar el punto de conexión SQL, ve al **espacio de trabajo** en Fabric y, en la lista de elementos, pasa el ratón por encima del nombre del almacén y selecciona **Copy SQL connection string**.

![La página "Fabric Console" en Microsoft Azure, donde los usuarios deben recuperar la cadena de conexión SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})

#### Paso 2.4: Permite las IP de Braze en el cortafuegos (opcional) {#step-24-allow-braze-ips-in-firewall-optional}

Dependiendo de la configuración de tu cuenta de Microsoft Fabric, puede que necesites permitir las siguientes direcciones IP en tu cortafuegos para permitir el tráfico desde Braze. Para más información sobre cómo habilitarlo, consulta la documentación correspondiente sobre [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Paso 3: Crea una fuente conectada en el panel de Braze {#step-3-create-a-connected-source-in-the-braze-dashboard}

{% tabs %}
{% tab Snowflake %}
#### Paso 3.1: Añade la información de conexión de Snowflake y la tabla de origen {#step-31-add-snowflake-connection-information-and-source-table}

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos de Cloud** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Snowflake Import**.

![Página de fuentes conectadas con opciones para crear una nueva sincronización de datos.]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tu almacén de datos de Snowflake y el esquema de origen, y pasa al siguiente paso.

![Campos de conexión de Snowflake para el almacén y el esquema de origen.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### Paso 3.2: Configura los detalles de sincronización {#step-32-configure-sync-details}

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees una nueva Extensión de segmento CDI.

Configura un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta de Snowflake.

{% alert note %}
Si las consultas se interrumpen constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de las consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

![Configuración del nombre de sincronización y tiempo máximo de ejecución de Snowflake.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### Paso 3.3: Toma nota de la clave pública {#step-33-note-the-public-key}

En el paso **Test connection**, toma nota de la clave pública RSA. La necesitarás para completar la integración en Snowflake.

![Paso de prueba de conexión de Snowflake que muestra la clave pública RSA.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### Paso 3.1: Añade la información de conexión de Redshift y la tabla de origen {#step-31-add-redshift-connection-information-and-source-table}

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos de Cloud** > **Fuentes conectadas** y, a continuación, selecciona **Crear conexión de datos** > **Amazon Redshift Import**.

![Página de fuentes conectadas con opciones para crear una nueva sincronización de datos.]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tu almacén de datos de Redshift y el esquema de origen, y pasa al siguiente paso.

![Campos de conexión de Redshift para el almacén y el esquema de origen.]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### Paso 3.2: Configura los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees una nueva Extensión de segmento CDI.

Configura un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta de Redshift.

{% alert note %}
Si las consultas se interrumpen constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de las consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

![Configuración del nombre de sincronización y tiempo máximo de ejecución de Redshift.]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### Paso 3.3: Toma nota de la clave pública (opcional) {#step-33-note-the-public-key-optional}

Si tus credenciales tienen seleccionada la opción **Connect with SSH Tunnel**, toma nota de la clave pública RSA en el paso **Test connection**. La necesitarás para completar la integración en Redshift.

![Paso de prueba de conexión de Redshift que muestra la clave pública RSA.]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### Paso 3.1: Añade la información de conexión de BigQuery y la tabla de origen {#step-31-add-bigquery-connection-information-and-source-table}

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos de Cloud** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Google BigQuery Import**.

![Página de fuentes conectadas con opciones para crear una nueva sincronización de datos.]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tu proyecto de BigQuery y del conjunto de datos, y pasa al siguiente paso.

![Captura de pantalla relacionada con el paso 3.1: añadir la información de conexión de BigQuery y la tabla de origen.]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### Paso 3.2: Configura los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees una nueva Extensión de segmento CDI.

Configura un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta de BigQuery.

{% alert note %}
Si las consultas se interrumpen constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de las consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

![Captura de pantalla relacionada con el paso 3.2: configurar los detalles de sincronización.]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### Paso 3.3: Prueba la conexión {#step-33-test-the-connection}

Selecciona **Test Connection** para comprobar que la lista de tablas visibles para el usuario es la que esperas y, a continuación, selecciona **Done**. Tu fuente conectada ya está creada y lista para usar en las Extensiones de segmento CDI.

![Paso de prueba de conexión que muestra las tablas disponibles para la fuente conectada.]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### Paso 3.1: Añade la información de conexión de Databricks y la tabla de origen {#step-31-add-databricks-connection-information-and-source-table}

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos de Cloud** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Databricks Import**.

![Página de fuentes conectadas con opciones para crear una nueva sincronización de datos.]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tus credenciales de Databricks y, opcionalmente, el catálogo y el esquema de origen, y pasa al siguiente paso.

![Campos de conexión de Databricks para credenciales y esquema de origen.]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### Paso 3.2: Configura los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees una nueva Extensión de segmento CDI.

Configura un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta de Databricks.

{% alert note %}
Si las consultas se interrumpen constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de las consultas o dedicar un almacén más grande al usuario de Braze.
{% endalert %}

![Configuración del nombre de sincronización y tiempo máximo de ejecución de Databricks.]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### Paso 3.3: Prueba la conexión

Selecciona **Test Connection** para comprobar que la lista de tablas visibles para el usuario es la que esperas y, a continuación, selecciona **Done**. Tu fuente conectada ya está creada y lista para usar en las Extensiones de segmento CDI.

![Paso de prueba de conexión que muestra las tablas disponibles para la fuente conectada.]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Microsoft Fabric %}
#### Paso 3.1: Añade la información de conexión de Microsoft Fabric y la tabla de origen {#step-31-add-microsoft-fabric-connection-information-and-source-table}

Crea una fuente conectada en el panel de Braze. Ve a **Configuración de datos** > **Ingesta de datos de Cloud** > **Fuentes conectadas** y, a continuación, selecciona **Crear nueva sincronización de datos** > **Microsoft Fabric Import**.

![Página de fuentes conectadas con opciones para crear una nueva sincronización de datos.]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Introduce la información de tus credenciales de Microsoft Fabric, así como el almacén de origen y el esquema, y pasa al siguiente paso.

![Campos de conexión de Microsoft Fabric para credenciales y esquema de origen.]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_1.png %})

#### Paso 3.2: Configura los detalles de sincronización

Elige un nombre para la fuente conectada. Este nombre se utilizará en la lista de fuentes disponibles cuando crees una nueva Extensión de segmento CDI.

Configura un tiempo máximo de ejecución para esta fuente. Braze abortará automáticamente cualquier consulta que supere el tiempo máximo de ejecución cuando esté creando o actualizando un segmento. El tiempo máximo de ejecución permitido es de 60 minutos; un tiempo de ejecución inferior reducirá los costes incurridos en tu cuenta de Microsoft Fabric.

{% alert note %}
Si las consultas se interrumpen constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de las consultas o escalar la capacidad de Fabric.
{% endalert %}

![Configuración del nombre de sincronización y tiempo máximo de ejecución de Microsoft Fabric.]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_2.png %})

#### Paso 3.3: Prueba la conexión

Selecciona **Test Connection** para comprobar que la lista de tablas visibles para el usuario es la que esperas y, a continuación, selecciona **Done**. Tu fuente conectada ya está creada y lista para usar en las Extensiones de segmento CDI.

![Paso de prueba de conexión que muestra las tablas disponibles para la fuente conectada.]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Finaliza la configuración del almacén de datos {#step-4-finalize-the-data-warehouse-configuration}

{% tabs %}
{% tab Snowflake %}
Añade la clave pública que anotaste en el último paso a tu usuario en Snowflake. Esto permitirá a Braze conectarse a Snowflake. Para saber cómo hacerlo, consulta la [documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).

Si quieres rotar las claves en cualquier momento, puedes crear una nueva clave pública yendo a **Gestión de acceso a datos** en **Ingesta de datos de Cloud** y seleccionando **Generar nueva clave** para la cuenta correspondiente.

![Gestión del acceso a datos para las credenciales de acceso a datos de Snowflake, con un botón para generar una nueva clave.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Después de añadir la clave al usuario en Snowflake, selecciona **Test Connection** en Braze y, a continuación, selecciona **Done**. Tu fuente conectada ya está creada y lista para usar en las Extensiones de segmento CDI.
{% endtab %}

{% tab Redshift %}
Si te conectas con un túnel SSH, añade la clave pública que anotaste en el último paso al usuario del túnel SSH.

Después de añadir la clave al usuario, selecciona **Test Connection** en Braze y, a continuación, selecciona **Done**. Tu fuente conectada ya está creada y lista para usar en las Extensiones de segmento CDI.

{% endtab %}
{% tab BigQuery %}
Esto no se aplica a BigQuery.

{% endtab %}
{% tab Databricks %}
Esto no se aplica a Databricks.

{% endtab %}
{% tab Microsoft Fabric %}
Esto no se aplica a Microsoft Fabric.

{% endtab %}
{% endtabs %}

{% alert note %}
Debes probar con éxito una fuente antes de que pueda pasar del estado "borrador" al estado "activo". Si necesitas salir de la página de creación, tu integración se guardará y podrás volver a visitar la página de detalles para realizar cambios y pruebas.
{% endalert %}

## Configuración de integraciones o usuarios adicionales (opcional) {#setting-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para conectar un esquema diferente. Al crear conexiones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Snowflake.

Si reutilizas el mismo usuario y rol en distintas integraciones, no tendrás que volver a añadir la clave pública.
{% endtab %}

{% tab Redshift %}
Puedes configurar varias fuentes con Braze, pero cada fuente debe configurarse para conectar un esquema diferente. Al crear fuentes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Redshift.
{% endtab %}

{% tab BigQuery %}
Puedes configurar varias fuentes con Braze, pero cada fuente debe configurarse para conectar un conjunto de datos diferente. Al crear fuentes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de BigQuery.
{% endtab %}

{% tab Databricks %}
Puedes configurar varias fuentes con Braze, pero cada fuente debe configurarse para conectar un esquema diferente. Al crear fuentes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Databricks.
{% endtab %}

{% tab Microsoft Fabric %}
Puedes configurar varias fuentes con Braze, pero cada fuente debe configurarse para conectar un esquema diferente. Al crear fuentes adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Azure.
{% endtab %}
{% endtabs %}

## Utilizar la fuente conectada {#using-the-connected-source}

Una vez creada la fuente, puedes utilizarla para crear una o varias Extensiones de segmento CDI. Para obtener más información sobre cómo crear un segmento con esta fuente, consulta la [documentación de Extensiones de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).

{% alert note %}
Si las consultas se interrumpen constantemente y has establecido un tiempo máximo de ejecución de 60 minutos, considera intentar optimizar el tiempo de ejecución de las consultas o dedicar más recursos de computación (como un almacén más grande) al usuario de Braze.
{% endalert %}