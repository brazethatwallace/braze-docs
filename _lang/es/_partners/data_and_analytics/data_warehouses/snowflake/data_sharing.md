---
nav_title: "Uso compartido de datos"
article_title: Uso compartido de datos con Snowflake
page_order: 0
description: "Este artículo de referencia cubre la integración de Snowflake Secure Data Sharing, que te permite acceder a los datos de interacción y Campaign de Braze directamente en tu instancia de Snowflake."
page_type: partner
search_tag: Partner

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Uso compartido de datos con Snowflake {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsnowflake-secure-data-sharing-via-braze-stylefloatrightwidth120pxborder0-classnoimgbordersnowflake-data-sharing}

> [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) de Snowflake permite a Braze darte acceso seguro a los datos en nuestro portal de Snowflake sin preocuparte por fricciones o ralentizaciones en el flujo de trabajo, puntos de fallo y costes innecesarios que vienen con las relaciones típicas con proveedores de datos. El uso compartido de datos se puede configurar a través de la siguiente integración o a través de [cuentas de lectura de Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts).

El uso compartido de datos de Snowflake forma parte de la distribución de datos de Braze. Para un resumen completo de las opciones de distribución de datos, consulta [Distribución de datos]({{site.baseurl}}/user_guide/data/distribution).

{% alert tip %}
**¿Te interesa tener acceso a datos a nivel de Snowflake sin necesidad de una cuenta de Snowflake?**<br>Consulta las [cuentas de lectura de Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts). Con las cuentas de lectura, Braze creará y compartirá tus datos en una cuenta y te proporcionará credenciales para iniciar sesión y acceder a tus datos. Esto hará que toda la facturación del uso compartido de datos y del uso sea gestionada íntegramente por Braze.
{% endalert %}

## Derechos de Data Distribution {#data-distribution-entitlements}

Tu derecho de Data Distribution determina qué tipos de eventos están disponibles en tu recurso compartido de datos. Braze organiza los eventos en las siguientes categorías:

| Derecho | Categoría de evento | Descripción | Referencia del glosario de eventos |
|------------|----------------|-------------|--------------------------|
| **Engagement Events** | Eventos de interacción con mensajes | Eventos relacionados con envíos, entregas, aperturas, clics, rebotes y otras interacciones con canales de mensajería | [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) |
| **Customer Behavior Events** | Eventos de interacción con mensajes y eventos de comportamiento del cliente | Incluye todos los eventos de interacción con mensajes, además de eventos relacionados con compras, eventos personalizados, sesiones, atribución y acciones del usuario dentro de la aplicación | [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Eventos de comportamiento del cliente y del usuario]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) |
| **User Profiles and Attributes** | Eventos de interacción con mensajes, eventos de comportamiento del cliente y eventos de perfil de usuario | Incluye los eventos de interacción con mensajes y los eventos de comportamiento del cliente, además de eventos relacionados con cambios en los perfiles y atributos de los usuarios | [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Eventos de comportamiento del cliente y del usuario]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), [Eventos de perfil de usuario]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Derechos de Data Distribution" }

Si tienes preguntas sobre qué eventos están incluidos en tu derecho, ponte en contacto con tu administrador de cuenta o administrador de éxito de cliente de Braze.

## Acerca del intercambio seguro de datos {#about-secure-data-sharing}

Con el intercambio de datos, no se copian ni transfieren datos reales entre cuentas. Todo el intercambio se realiza a través de la capa de servicios y el almacén de metadatos exclusivos de Snowflake. Este es un concepto importante porque los datos compartidos no ocupan almacenamiento en tu cuenta y, por lo tanto, no contribuyen a tus cargos mensuales por almacenamiento de datos. Los **únicos** cargos son por los recursos informáticos (como los almacenes virtuales) utilizados para consultar los datos compartidos.

Además, mediante las capacidades integradas de roles y permisos de Snowflake, el acceso a los datos compartidos desde Braze se puede controlar y gestionar utilizando los controles de acceso ya existentes para tu cuenta de Snowflake y los datos que contiene. El acceso se puede restringir y supervisar de la misma manera que tus propios datos.

- **Reduce el tiempo para obtener información**<br>Despídete de los procesos ETL que tardan semanas en construirse. Las arquitecturas exclusivas de Braze y Snowflake hacen que todos los datos de interacción con los clientes y de Campaigns sean accesibles y consultables de forma inmediata desde el instante en que llegan al data lake. No se copian ni mueven datos, por lo que puedes ofrecer experiencias del cliente basadas únicamente en la información más relevante y actualizada.
- **Elimina los silos de datos**<br>Crea una visión holística de tus clientes en todos los canales y plataformas. El intercambio de datos facilita más que nunca la combinación de los datos de interacción con los clientes de Braze con todos tus demás datos de Snowflake, generando información más completa a través de una única fuente de verdad confiable.
- **Compara el rendimiento de tu participación**<br>Optimiza tus estrategias de interacción con los clientes con Braze Benchmarks. Esta herramienta interactiva, impulsada por Braze y Snowflake, te permite comparar los datos de participación de tu marca con puntos de referencia en canales, industria y plataformas de dispositivos.

Para obtener más información sobre el intercambio de datos de Snowflake, consulta [Introducción al intercambio seguro de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Acceso a Braze | Ponte en contacto con tu administrador de cuenta Braze o con tu administrador de éxito de cliente para configurar el uso compartido de datos. |
| Permisos de espacio de trabajo de Braze | [Ver integraciones de Currents]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para ver el uso compartido de datos. [Editar integraciones de Currents]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para crear, actualizar o eliminar un uso compartido de datos. |
| Cuenta de Snowflake | Una cuenta de Snowflake con permisos de `admin`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Configurar el uso compartido seguro de datos {#setting-up-secure-data-sharing}

Para Snowflake, el uso compartido de datos se realiza entre un [proveedor de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) y un [consumidor de datos](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). En este contexto, tu cuenta de Braze es el proveedor de datos porque crea y envía el recurso compartido de datos&#8212;mientras que tu cuenta de Snowflake es el consumidor de datos porque utiliza el recurso compartido de datos para crear una base de datos. Para más detalles, consulta [Snowflake: Consumo de datos compartidos](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Paso 1: Enviar el recurso compartido de datos desde Braze {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Paso 2: Crear la base de datos en Snowflake {#step-2-create-the-database-in-snowflake}

1. Después de unos minutos, deberías recibir el recurso compartido de datos entrante en tu cuenta de Snowflake.
2. Usando el recurso compartido de datos entrante, crea una base de datos para ver y consultar las tablas. Por ejemplo:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. Otorga privilegios para consultar la nueva base de datos.

{% alert warning %}
Si eliminas y vuelves a crear un recurso compartido en el panel de Braze, debes eliminar la base de datos creada anteriormente y recrearla usando `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` para consultar el recurso compartido entrante.
Si tienes varios espacios de trabajo compartiendo datos con la misma cuenta de Snowflake, consulta las [Preguntas frecuentes sobre el uso compartido de datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) para obtener orientación sobre la gestión de configuraciones con múltiples espacios de trabajo.
{% endalert %}

## Uso y visualización {#usage-and-visualization}

Una vez provisionado el uso compartido de datos, crea una base de datos a partir del uso compartido de datos entrante, haciendo que todas las tablas compartidas aparezcan en tu instancia de Snowflake y sean consultables como cualquier otro dato que estés almacenando en tu instancia. Sin embargo, ten en cuenta que los datos compartidos son de solo lectura y solo se pueden consultar, pero no modificar ni eliminar de ninguna manera.

De manera similar a Currents, puedes usar tu Snowflake Secure Data Sharing para:

{% multi_lang_include partners/data_sharing_use_cases.md %}

[Descarga los esquemas de tablas sin procesar.](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)

{% alert note %}
La descarga del esquema sin procesar no incluye las vistas de atributos del perfil de usuario. Para obtener los esquemas completos y la guía de uso de `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`, `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` y las vistas de atributos de usuario relacionadas, consulta [Atributos del perfil de usuario]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

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
Dado que las nuevas columnas se consideran cambios sin ruptura, Braze recomienda encarecidamente enumerar explícitamente las columnas de interés en cada consulta en lugar de usar consultas `SELECT *`. Alternativamente, podrías crear vistas que nombren explícitamente las columnas y luego consultar esas vistas en lugar de las tablas directamente.
{% endalert %}

#### Cambios con ruptura {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Regiones de Snowflake {#snowflake-regions}

Actualmente, Braze aloja todos los datos a nivel de usuario en estas regiones de Snowflake en AWS:

 - US East-1
 - EU-Central (Fráncfort)
 - AP-Northeast-1 (Tokio)
 - AP-Southeast-2 (Sídney)
 - AP-Southeast-3 (Yakarta)

Para los usuarios fuera de esas regiones, Braze puede proporcionar el uso compartido de datos a clientes conjuntos que alojen su infraestructura de Snowflake en cualquier región de AWS, Azure o GCP.

### Retención de datos {#data-retention}

#### Política de retención {#retention-policy}

Cualquier dato con más de dos años de antigüedad se archivará y trasladará a almacenamiento a largo plazo. Como parte del proceso de archivado, todos los eventos se anonimizan y se eliminan los campos sensibles de información de identificación personal (PII) (esto incluye campos PII opcionales como `properties`). Los datos archivados aún contienen el campo `user_id`, lo que permite realizar análisis por usuario en todos los datos de eventos.

Podrás consultar los datos más recientes de dos años para cada evento en la vista `USERS_*_SHARED` correspondiente. Además, cada evento tendrá una vista `USERS_*_SHARED_ALL` que se puede consultar para obtener tanto datos anonimizados como no anonimizados.

#### Datos históricos {#historical-data}

El archivo de datos históricos de eventos en Snowflake se remonta a abril de 2019. En los primeros meses en que Braze almacenó datos en Snowflake, se realizaron cambios en el producto que pueden haber dado lugar a que algunos de esos datos se vean ligeramente diferentes o tengan algunos valores nulos (ya que no estábamos pasando datos a todos los campos disponibles en ese momento). Es mejor asumir que cualquier resultado que incluya datos anteriores a agosto de 2019 puede verse ligeramente diferente de lo esperado.

### Cumplimiento del Reglamento General de Protección de Datos (RGPD) {#general-data-protection-regulation-gdpr-compliance}

{% include partners/snowflake_pii_gdpr.md %}

### Velocidad, rendimiento y coste de las consultas {#speed-performance-cost-of-queries}

La velocidad, el rendimiento y el coste de cualquier consulta ejecutada sobre los datos están determinados por el tamaño del almacén que utilices para consultar los datos. En algunos casos, dependiendo de la cantidad de datos a los que accedas para tus análisis, es posible que necesites usar un almacén de mayor tamaño para que la consulta se ejecute correctamente. Snowflake dispone de excelentes recursos sobre cómo determinar el tamaño más adecuado, incluyendo [Descripción general de los almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) y [Consideraciones sobre almacenes](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

{% alert tip %}
Para consultar un conjunto de consultas de ejemplo al configurar Snowflake, revisa nuestros ejemplos de [consultas de muestra]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) y [configuración del pipeline de eventos ETL]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup).
{% endalert %}