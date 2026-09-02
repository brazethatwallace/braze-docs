---
nav_title: LiveRamp
article_title: LiveRamp
description: "Aprende a conectar LiveRamp y Braze a través de Snowflake Data Sharing o Braze Currents para crear campañas de marketing altamente personalizadas y relevantes."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# LiveRamp

> Aprende a conectar LiveRamp y Braze a través de Snowflake Data Sharing o Braze Currents para crear campañas de marketing altamente personalizadas y relevantes reduciendo el tiempo de obtención de información, eliminando los silos de datos y optimizando la interacción con los clientes. Esta integración mejora el marketing basado en datos al proporcionar información procesable basada en las personas y consolidar los puntos de intervención del consumidor para una mejor segmentación de la audiencia y campañas oportunas.

## Opciones de integración {#integration-options}

Puedes integrar LiveRamp con Braze utilizando uno de dos métodos:

- **Snowflake Data Sharing:** Comparte datos de Braze directamente a través de los Secure Data Shares de Snowflake sin mover datos. Este método aprovecha los puntos de referencia de Snowflake para ayudarte a perfeccionar tus estrategias de marketing comparándolas con los estándares del sector.
- **Braze Currents:** Transmite datos de interacción a nivel de evento en tiempo real desde Braze a un destino de almacenamiento en la nube (Amazon S3, Google Cloud Storage o Microsoft Azure Blob Storage), luego carga esos datos en tu almacén de datos y utiliza las funciones de resolución de identidad de LiveRamp en tu entorno en la nube.

{% alert important %}
El [intercambio seguro de datos](https://docs.snowflake.com/en/user-guide/data-sharing-intro) de Snowflake no transfiere datos entre LiveRamp, Snowflake y Braze. Los datos solo se comparten a través de los servicios y el almacén de metadatos de Snowflake, lo que significa que no se copian datos ni se producen cargos adicionales por almacenamiento. El acceso a los datos compartidos se controla y regula mediante los controles de acceso de tu cuenta de Snowflake.
{% endalert %}

## Casos de uso {#use-cases}

Esta integración admite los siguientes casos de uso en todos los entornos de almacén de datos:

- **Minimización de datos:** Las soluciones de LiveRamp utilizan características de intercambio seguro de datos o resolución de identidad nativa en la nube para leer tablas directamente desde tu almacén de datos. No se mueven datos hasta el punto de entrega al socio posterior.
- **Activación segura de datos propios:** Al utilizar la resolución de identidad de LiveRamp, la aplicación de activación de LiveRamp solo utiliza las tablas basadas en RampID en tu almacén de datos, por lo que la PII nunca tiene que salir de tu entorno.
- **Acelerar el tiempo en vivo:** Al resolver los datos a RampID directamente en tu entorno, la entrega a un destino final puede producirse en cuestión de horas, en comparación con varios días cuando se utiliza el enfoque más tradicional basado en archivos de LiveRamp. Esto aumenta enormemente la capacidad de optimizar el rendimiento de las campañas en el momento oportuno.
- **Ahorro operativo:** Mediante el intercambio seguro de datos o la resolución de identidad nativa en la nube, ahorras tiempo y dinero en comparación con la coordinación de la salida de archivos a LiveRamp o directamente a cualquier destino final.

## Integración con Snowflake Data Sharing {#integration-with-snowflake-data-sharing}

Los siguientes pasos describen cómo integrar LiveRamp con Braze a través de Snowflake Data Sharing.

### Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Snowflake | Necesitas una cuenta de Snowflake con permisos de nivel de administrador. |
| Cuenta de LiveRamp | Ponte en contacto con tu equipo de cuentas de LiveRamp o con [snowflake@liveramp.com](mailto:snowflake@liveramp.com) para hablar de las aplicaciones de LiveRamp necesarias dentro de Snowflake. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

### Paso 1: Solicitar un intercambio de datos a Braze {#step-1-request-a-data-share-from-braze}

En primer lugar, ponte en contacto con tu director de cuentas de Braze o tu administrador del éxito del cliente para adquirir un conector Snowflake Data Share para tu cuenta de Braze. Cuando solicites un intercambio de datos, Braze aprovisionará el recurso compartido desde los espacios de trabajo en los que se adquirió. Una vez aprovisionado el recurso compartido, se puede acceder inmediatamente a todos los datos desde tu instancia de Snowflake en forma de recurso compartido de datos entrantes. Una vez que el recurso compartido sea visible en tu instancia, crea una base de datos a partir de él para poder ver y consultar las tablas.

Para obtener un tutorial completo, consulta la [guía de integración de Snowflake con Braze]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### Paso 2: Configurar la aplicación LiveRamp en Snowflake {#step-2-set-up-the-liveramp-app-in-snowflake}

Las funciones de traducción y resolución de identidades están disponibles en Snowflake a través de la aplicación nativa LiveRamp Identity Resolution and Translation, que crea un recurso compartido en tu cuenta y abre una vista para consultar el conjunto de datos de referencia desde tu propio entorno de Snowflake.

Para configurar la aplicación nativa, sigue estos pasos en la documentación de LiveRamp: [Configurar la aplicación nativa LiveRamp en Snowflake](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). Cuando hayas terminado, continúa con el siguiente paso.

### Paso 3: Crear una tabla de datos {#step-3-create-a-data-table}

{% alert warning %}
Antes de preparar cualquier tabla basada en PII, asegúrate de entender [el filtro de privacidad de LiveRamp](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) que se ejecuta durante los trabajos para garantizar que las columnas de atributos (no identificadores) en tus tablas de entrada no contengan valores demasiado únicos. Esto es fundamental para mantener la privacidad del consumidor y evitar la reidentificación.
{% endalert %}

A continuación, crea una tabla de datos con el [formato requerido](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) que se invocará contra la aplicación nativa de LiveRamp. Consulta las siguientes categorías para determinar cuáles de tus identificadores son elegibles para resolución:

| Tipo de identificador | Descripción |
|---|---|
| PII completo | La información de identificación personal (PII) incluye el nombre, la dirección postal, el correo electrónico y el número de teléfono del usuario. **Nota:** No todos los identificadores son necesarios para todos los registros. |
| Solo correo electrónico | Las direcciones de correo electrónico del usuario, como `alex-lee@email.com`. |
| Dispositivo | Esto incluye cookies de terceros, Mobile Advertising IDs (MAIDs), Connected TV IDs (CTV IDs) y RampIDs (resueltos a un Household RampID). |
| CID | Se trata de identificadores de un socio de la plataforma o de una sincronización de identidad con LiveRamp, como tu ID de cliente interno. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Crear una tabla de datos" }

#### Identificadores de Braze {#braze-identifiers}

Los registros de eventos de Braze contienen identificadores que puedes utilizar dentro de la aplicación nativa de LiveRamp. Para obtener una lista completa de los identificadores disponibles para cada tipo de evento, descarga los [esquemas e identificadores de eventos de Braze](/docs/assets/download_file/data-sharing-raw-table-schemas.txt).

| Tipo de identificador | Descripción |
|---|---|
| `AD_ID` | Identificadores de publicidad, como `ios_idfa`, `google_ad_id`, `roku_ad_id`, capturados dentro de determinados tipos de eventos, que pueden utilizarse junto con los servicios de resolución de dispositivos de LiveRamp. De forma predeterminada, los ID de publicidad no se recopilan&#8212;sin embargo, puedes habilitar el seguimiento siguiendo la [documentación de Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default). |
| `EMAIL_ADDRESS` | Dirección de correo electrónico que puede utilizarse junto con los servicios de resolución solo por correo electrónico de LiveRamp. |
| `TO_PHONE_NUMBER` | Número de teléfono, que puede utilizarse junto con los servicios de resolución PII de LiveRamp. |
| `EXTERNAL_USER_ID` | El ID externo asociado a un usuario, que puede utilizarse junto con los servicios de resolución de dispositivos (CID) de LiveRamp. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identificadores de Braze" }

{% alert important %}
El uso de cualquier identificador personalizado específico del cliente o de la marca dentro de la aplicación de LiveRamp requiere una [sincronización de identidad con LiveRamp](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html).
{% endalert %}

### Paso 4: Establece tus variables {#step-4-set-your-variables}

A continuación, establece tus variables para el trabajo en la hoja de cálculo de pasos de ejecución que se proporciona en la aplicación. Esto incluye detalles como la base de datos de destino, las tablas asociadas (datos de entrada, métricas, registro) y la definición del nombre de la tabla de salida. Para un recorrido completo, consulta [LiveRamp: Especifica las variables](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727).

### Paso 5: Crear la tabla de metadatos para la resolución PII {#step-5-create-the-metadata-table-for-pii-resolution}

Ahora que tus variables están configuradas, crea la tabla de metadatos para la resolución PII. Esto proporcionará detalles sobre el tipo de trabajo específico que debe ejecutarse en función de la categoría de los identificadores implicados. Para un recorrido completo, consulta [LiveRamp: Crear la tabla de metadatos](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### Paso 6: Realizar la operación de resolución de identidad {#step-6-perform-the-identity-resolution-operation}

Por último, realiza la operación de resolución de identidad. Para un recorrido completo, consulta [LiveRamp: Realizar la operación de resolución de identidad](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

{% tabs local %}
{% tab example input %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab example output %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Próximos pasos {#next-steps}

Con tus datos ahora seudonimizados a tu codificación dedicada de RampID, tienes la capacidad de compartir las tablas basadas en RampID con la aplicación Managed Activation de LiveRamp para la entrega optimizada a tus socios clave de plataformas publicitarias. La aplicación Activation incluye una interfaz fácil de usar para usuarios de negocio que permite la segmentación adicional y la selección/configuración de socios de destino posteriores. Para más detalles sobre la aplicación, ponte en contacto con el equipo de tu cuenta de LiveRamp o con [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Integración con Braze Currents {#integration-with-braze-currents}

Braze Currents proporciona un flujo en tiempo real de eventos de interacción que se pueden exportar a destinos de almacenamiento en la nube. Puedes usar Currents con LiveRamp para transmitir datos de eventos de Braze al almacenamiento en la nube, cargarlos en tu almacén de datos y luego aplicar las funciones de resolución de identidad de LiveRamp dentro de tu entorno en la nube.

### Cómo funciona {#how-it-works}

1. **Braze proporciona datos a nivel de evento en tiempo real:** Braze transmite datos de interacción sin procesar a tu almacén de datos o destino de almacenamiento a través de Currents.
2. **LiveRamp conecta los datos a RampID:** LiveRamp elimina la PII y conecta tus datos al identificador universal de tu marca, RampID.
3. **Activar y medir:** Los datos propios de Braze se pueden combinar con otros datos de terceros para crear segmentos de clientes más precisos para publicidad. Las audiencias seudonimizadas se envían a LiveRamp para la activación posterior en socios de plataformas, y LiveRamp recibe datos de exposición publicitaria de los socios para la medición a nivel de personas.

### Plataformas en la nube compatibles {#supported-cloud-platforms}

Las funciones de resolución de identidad de LiveRamp están disponibles en los siguientes entornos en la nube:

| Plataforma | Solución de LiveRamp | Descripción |
|----------|------------------|-------------|
| Google BigQuery | [LiveRamp Embedded Identity en BigQuery](https://docs.liveramp.com/identity/en/liveramp-embedded-identity-in-bigquery.html#liveramp-embedded-identity-in-bigquery) | Realiza la resolución de identidad y la traducción de RampID de forma nativa en BigQuery utilizando el BigQuery Entity Resolution Framework. Carga los datos de Currents desde Google Cloud Storage en BigQuery antes de ejecutar la resolución de identidad. |
| AWS | [LiveRamp Identity en AWS](https://docs.liveramp.com/identity/en/liveramp-identity-in-aws.html#liveramp-identity-in-aws) | Resuelve identificadores a RampIDs y realiza la traducción de identidad utilizando AWS Entity Resolution o a través de Amazon Data Exchange (ADX) de forma independiente. Carga los datos de Currents desde Amazon S3 antes de ejecutar la resolución de identidad. |
| Microsoft Azure | Ponte en contacto con LiveRamp | Azure Blob Storage es compatible como destino de Currents. Ponte en contacto con tu representante de LiveRamp para obtener soluciones de resolución de identidad específicas de Azure. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Plataformas en la nube compatibles" }

{% alert note %}
LiveRamp Embedded Identity en BigQuery se encuentra actualmente en versión beta. Ponte en contacto con [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com) para hablar sobre la participación en el programa.
{% endalert %}

### Requisitos previos

| Requisito | Descripción |
|-------------|-------------|
| Braze Currents | Para transmitir datos de eventos al almacenamiento en la nube, necesitas tener [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) configurado para tu cuenta. |
| Cuenta de almacenamiento en la nube | Necesitas una cuenta de almacenamiento en la nube (Amazon S3, Google Cloud Storage o Microsoft Azure Blob Storage) donde Currents transmita tus datos. |
| Cuenta de LiveRamp | Ponte en contacto con tu equipo de cuentas de LiveRamp o con [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com) para configurar la resolución de identidad de LiveRamp en tu entorno en la nube. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

### Paso 1: Configurar Braze Currents {#step-1-set-up-braze-currents}

Primero, configura Braze Currents para transmitir tus datos de interacción a tu destino de almacenamiento en la nube. Consulta las siguientes guías según la plataforma que hayas elegido:

- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)

Configura Currents para exportar los eventos que contengan los identificadores que necesitas para la resolución de identidad de LiveRamp. Para obtener una lista completa de los identificadores disponibles para cada tipo de evento, consulta los glosarios de [eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) y [eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

### Paso 2: Configurar la resolución de identidad de LiveRamp {#step-2-set-up-liveramp-identity-resolution}

Una vez que Currents esté transmitiendo datos a tu almacenamiento en la nube, trabaja con tu representante de LiveRamp para configurar la resolución de identidad en tu entorno en la nube:

- **Para BigQuery:** Sigue la guía de configuración de [LiveRamp Embedded Identity en BigQuery](https://docs.liveramp.com/identity/en/liveramp-embedded-identity-in-bigquery.html#liveramp-embedded-identity-in-bigquery) para habilitar la resolución de identidad y la traducción de RampID. Coordínate con tu representante de LiveRamp para completar los pasos de acuerdo y aprovisionamiento requeridos para el programa beta.
- **Para AWS:** Sigue la guía de configuración de [LiveRamp Identity en AWS](https://docs.liveramp.com/identity/en/liveramp-identity-in-aws.html#liveramp-identity-in-aws) para configurar la resolución de identidad de RampID utilizando AWS Entity Resolution o ADX de forma independiente.

### Paso 3: Cargar y transformar tus datos {#step-3-load-and-transform-your-data}

Crea un proceso ETL or extraer, transformar, cargar (ETL or extraer, transformar, cargar or extraer, transformar, cargar) para:

1. Cargar los datos de Currents desde tu almacenamiento en la nube en las tablas de tu almacén de datos.
2. Transformar los datos al formato requerido por el servicio de resolución de identidad de LiveRamp.
3. Preparar las tablas de entrada con los identificadores necesarios para la resolución de LiveRamp (como direcciones de correo electrónico, ID de dispositivos o ID de usuario externos).

### Paso 4: Realizar la resolución de identidad {#step-4-perform-identity-resolution}

Utiliza la resolución de identidad nativa en la nube de LiveRamp para resolver tus identificadores de Braze a RampIDs. El proceso:

1. Resuelve los identificadores proporcionados (PII o dispositivo) al identificador seudonimizado basado en personas de LiveRamp, RampID.
2. Escribe las tablas de salida con RampIDs de vuelta en tu almacén de datos, con los datos PII eliminados.

### Paso 5: Activar tus audiencias {#step-5-activate-your-audiences}

Con tus datos ahora seudonimizados a RampID, puedes:

- Combinar datos propios de Braze con otros orígenes de datos para crear segmentos de clientes más precisos.
- Activar audiencias seudonimizadas a través de la plataforma de activación de LiveRamp para campañas publicitarias.
- Recibir datos de exposición publicitaria de los socios para la medición a nivel de personas.

Para más detalles sobre la activación, ponte en contacto con tu equipo de cuentas de LiveRamp o con [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com).

## Solución de problemas {#troubleshooting}

{% alert note %}
Si tienes cuestiones o preguntas más específicas, ponte en contacto con [martech@liveramp.com](mailto:martech@liveramp.com) o [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com).
{% endalert %}

### Regiones de Snowflake {#snowflake-regions}

Actualmente, la aplicación nativa de Snowflake solo está disponible para las siguientes regiones de EE. UU.:

  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### Privacidad y valores de columna {#privacy-column-values}

El proceso de resolución de identidad de LiveRamp evalúa la combinación de todos los valores de columna por fila en busca de valores únicos. Si una determinada combinación de valores de columna aparece 3 o menos veces, las filas que contengan esos valores de columna no serán coincidentes y no se devolverán en la tabla de salida. Asimismo, para garantizar la privacidad, el servicio de LiveRamp evalúa la unicidad de las combinaciones de valores de columna, garantizando que si más del 5 % de las filas del archivo resultan no coincidentes debido a combinaciones raras, el trabajo fallará.

### Datos históricos {#historical-data}

Los datos históricos en Snowflake se remontan a abril de 2019, pero puede haber ligeras diferencias en los datos anteriores a agosto de 2019 debido a cambios en el producto.

### Velocidad, rendimiento y coste {#speed-performance-cost}

La velocidad y el coste de las consultas dependen del tamaño del almacén utilizado. Ten en cuenta tus necesidades de acceso a los datos a la hora de seleccionar el tamaño del almacén.

### Puntos de referencia de Braze {#braze-benchmarks}

Los puntos de referencia te permiten comparar tus métricas con los estándares del sector, disponibles directamente en Snowflake Data Exchange.

### Cambios con ruptura vs. cambios sin ruptura {#breaking-vs-non-breaking-changes}

Estate atento a los cambios que puedan afectar a tu integración. Los cambios con ruptura irán precedidos de un anuncio y de un periodo de migración.