---
nav_title: Cómo utiliza Braze Currents
article_title: Cómo utiliza Braze Currents
page_order: 6
page_type: tutorial
description: "Este artículo práctico de Currents te guiará por el proceso básico para configurar las entradas adecuadas para los datos de eventos, así como para trasladarlos a una base de datos y a una herramienta de inteligencia empresarial (BI)."
tool: Currents

---

# Cómo utiliza Braze Currents

> Braze utiliza Currents internamente con [socios]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) seleccionados.

Filtramos nuestros datos de campañas de correo electrónico y push en una herramienta de inteligencia empresarial, Looker, pero para llegar a ella hay que seguir un camino ligeramente distinto. Utilizamos una versión invertida de la metodología Extraer, Transformar, Cargar (ETL), cambiando el orden a Extraer, Cargar, Transformar (ELT).

## Paso 1: Datos de entrada y de eventos agregados

Después de lanzar campañas utilizando cualquiera de nuestras herramientas de interacción (como campañas o Canvas), hacemos un seguimiento de los datos del evento utilizando nuestro propio sistema, así como algunos de nuestros socios de correo electrónico. Algunos de estos datos se agregan y se muestran en el dashboard, pero a nosotros nos interesaba profundizar en ellos.

## Paso 2: Enviar datos de eventos a un socio de almacenamiento de datos

Configuramos Currents para que envíe los datos de eventos de Braze a Amazon S3 para su almacenamiento y extracción. Ahora sabemos que puedes utilizar [Athena](https://aws.amazon.com/athena/) para controlar el S3 y ejecutar consultas. Es una gran solución a corto plazo. Pero queríamos una solución a largo plazo utilizando una base de datos relacional y una herramienta de inteligencia empresarial/análisis. (Te recomendamos lo mismo.)

S3 proporciona opciones flexibles de almacenamiento y enrutamiento para mover, pivotar y analizar datos. No transformamos los datos en S3 porque mantenemos una estructura específica para ellos.

## Paso 3: Transformar datos de eventos con una base de datos relacional

Desde S3, elegimos un almacén de datos ([Snowflake Data Sharing](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) o Snowflake Reader Accounts, en nuestro caso). Los transformamos allí y luego los trasladamos a Looker, donde tenemos bloques configurados que estructuran y organizan nuestros datos.

Snowflake no es la única opción de almacén de datos. Otras opciones incluyen [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE), ¡y más!

### Snowflake Reader Accounts

Snowflake Reader Accounts ofrece a los usuarios acceso a los mismos datos y funcionalidades que [Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/), todo sin necesidad de tener una cuenta de Snowflake ni una relación de cliente con Snowflake. Con Reader Accounts, Braze creará y compartirá tus datos en una cuenta y te proporcionará credenciales para iniciar sesión y acceder a tus datos. Esto significa que toda la facturación del uso compartido de datos y del uso será gestionada íntegramente por Braze.

Para obtener más información, ponte en contacto con tu administrador del éxito del cliente.

#### Recursos adicionales
Para recursos útiles de monitorización del uso, consulta los artículos de Snowflake sobre [Resource Monitors](https://docs.snowflake.com/en/user-guide/resource-monitors.html) y [Viewing Warehouse Credit Usage](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account).

## Paso 4: Usar una herramienta de inteligencia empresarial (BI) para manipular tus datos

Por último, utilizamos una herramienta de BI para analizar nuestros datos, convertirlos en gráficos y otras herramientas visuales, y más, usando [Looker y bloques de Looker](https://www.marketplace.looker.com/) para no tener que hacer ETL o ELT de los datos cada vez que se mueven desde Currents.

¿Te animas a hacer lo mismo? Consulta los siguientes documentos para obtener más información sobre estos recursos y cómo puedes utilizarlos para construir tu base de datos.

- [Bloque de comportamiento del usuario](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Bloque de interacción con mensajes](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)