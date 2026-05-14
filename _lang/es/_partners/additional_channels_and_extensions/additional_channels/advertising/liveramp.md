---
nav_title: LiveRamp
article_title: LiveRamp
description: "Aprende a conectar LiveRamp, Snowflake y Braze para crear campañas de marketing altamente personalizadas y relevantes."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# Conecta LiveRamp, Snowflake y Braze {#connect-liveramp-snowflake-and-braze}

> Aprende a conectar LiveRamp, Snowflake y Braze para crear campañas de marketing altamente personalizadas y relevantes reduciendo el tiempo de obtención de información, eliminando los silos de datos y optimizando la interacción con los clientes. Esta integración mejora el marketing basado en datos al proporcionar información procesable basada en las personas y consolidar los puntos de intervención del consumidor para una mejor segmentación de la audiencia y campañas oportunas. También aprovecha los puntos de referencia de Snowflake para ayudarte a perfeccionar tus estrategias de marketing comparándolas con los estándares del sector.

{% alert important %}
El [intercambio seguro de datos](https://docs.snowflake.com/en/user-guide/data-sharing-intro) de Snowflake no transfiere datos entre LiveRamp, Snowflake y Braze. Los datos solo se comparten a través de los servicios y el almacén de metadatos de Snowflake, lo que significa que no se copian datos ni se producen cargos adicionales por almacenamiento. El acceso a los datos compartidos se controla y regula mediante los controles de acceso de tu cuenta de Snowflake.
{% endalert %}

## Casos de uso {#use-cases}

- **Minimización de datos:** La aplicación Activation de LiveRamp utiliza la característica Secure Data Share de Snowflake para leer eficazmente las tablas directamente desde tu instancia. No se mueven datos desde Snowflake hasta el punto de entrega al socio posterior.
- **Activación segura de 1.ª parte:** Al utilizar la aplicación de resolución de identidad mencionada anteriormente, la aplicación Activation de LiveRamp solo utilizará las tablas basadas en RampID en tu instancia de Snowflake, por lo que la PII nunca tendrá que salir de tus paredes.
- **Acelerar el tiempo en vivo:** Al resolver los datos a RampID directamente en tu entorno, la entrega a un destino final puede producirse en cuestión de horas, en comparación con varios días cuando se utiliza el enfoque más tradicional basado en archivos de LiveRamp. Esto aumenta enormemente la capacidad de optimizar el rendimiento de las campañas en el momento oportuno.
- **Ahorro operativo:** De forma similar a lo anterior, mediante el uso de la característica Secure Data Share de Snowflake, los clientes ahorran tiempo y dinero en comparación con la coordinación de la salida de archivos a LiveRamp o directamente a cualquier destino final.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Snowflake | Necesitas una cuenta de Snowflake con permisos de nivel de administrador. |
| Cuenta de LiveRamp | Ponte en contacto con tu equipo de cuentas de LiveRamp o con [snowflake@liveramp.com](mailto:snowflake@liveramp.com) para hablar de las aplicaciones de LiveRamp necesarias dentro de Snowflake. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Configuración de la integración {#setting-up-the-integration}

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

Los registros de eventos de Braze contienen identificadores que puedes utilizar dentro de la aplicación nativa de LiveRamp. Para obtener una lista completa de los identificadores disponibles para cada tipo de evento, descarga los [esquemas e identificadores de eventos de Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt).

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

## Solución de problemas {#troubleshooting}

{% alert note %}
Si tienes cuestiones o preguntas más específicas, ponte en contacto con [martech@liveramp.com](mailto:martech@liveramp.com).
{% endalert %}

### Regiones de Snowflake {#snowflake-regions}

Actualmente, esta aplicación solo está disponible para las siguientes regiones de EE. UU.:

  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### Privacidad y valores de columna {#privacy-column-values}

El proceso evalúa la combinación de todos los valores de columna por fila en busca de valores únicos. Si una determinada combinación de valores de columna aparece 3 o menos veces, las filas que contengan esos valores de columna no serán coincidentes y no se devolverán en la tabla de salida. Asimismo, para garantizar la privacidad, el servicio de LiveRamp evalúa la unicidad de las combinaciones de valores de columna, garantizando que si más del 5 % de las filas del archivo resultan no coincidentes debido a combinaciones raras, el trabajo fallará.

### Datos históricos {#historical-data}

Los datos históricos en Snowflake se remontan a abril de 2019, pero puede haber ligeras diferencias en los datos anteriores a agosto de 2019 debido a cambios en el producto.

### Velocidad, rendimiento y coste {#speed-performance-cost}

La velocidad y el coste de las consultas dependen del tamaño del almacén utilizado. Ten en cuenta tus necesidades de acceso a los datos a la hora de seleccionar el tamaño del almacén.

### Puntos de referencia de Braze {#braze-benchmarks}

Los puntos de referencia te permiten comparar tus métricas con los estándares del sector, disponibles directamente en Snowflake Data Exchange.

### Cambios con ruptura vs. cambios sin ruptura {#breaking-vs-non-breaking-changes}

Estate atento a los cambios que puedan afectar a tu integración. Los cambios con ruptura irán precedidos de un anuncio y de un periodo de migración.