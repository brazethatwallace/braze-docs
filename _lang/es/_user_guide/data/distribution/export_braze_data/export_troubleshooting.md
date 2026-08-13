---
nav_title: Solución de problemas
article_title: Solución de problemas de exportación
page_order: 6
page_type: reference
description: "Diagnostica fallos en exportaciones CSV y API usando un índice de síntomas, una ruta de investigación estándar y orientación de errores específica por almacenamiento."
---

# Solución de problemas de exportación {#export-troubleshooting}

> Usa esta página para diagnosticar problemas de exportación CSV y API en el panel y las API de exportación. Para flujos de trabajo y límites de exportación, consulta [Exportar datos de segmento a CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) y [API de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_apis).

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

Busca el comportamiento que estás observando en la tabla y luego ve a esa sección para comprobaciones específicas.

| Síntoma | Ir a |
| --- | --- |
| El enlace de descarga del CSV devuelve `AccessDenied`, `ExpiredToken` o "file doesn't exist" | [Exportación predeterminada: errores CSV](#defaultexport_csv-exports) o [Almacenamiento en el cloud: errores CSV](#csv-exports-1) |
| La URL de descarga de la exportación API devuelve `403 Forbidden` | [No se puede descargar un ZIP de segmento exportado](#cant-download-an-exported-segment-zip-from-a-braze-url) |
| La exportación de segmento falla o indica que el segmento es demasiado grande | [El segmento es demasiado grande](#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users) |
| No se recibe el correo electrónico de exportación de segmento | [No se reciben correos de exportación de segmento](#not-receiving-segment-export-emails) |
| El recuento de filas del CSV no coincide con los análisis de Campaign | [Discrepancia en análisis de Campaign y Canvas](#number-of-users-in-csv-export-doesnt-match-messages-sent-or-unique-recipients) |
| Faltan columnas esperadas en el archivo de exportación | [Columnas faltantes](#expected-columns-are-missing-from-a-segment-export-file) |
| La exportación a almacenamiento en el cloud muestra `AccessDenied` o `ExpiredToken` | [Almacenamiento en el cloud conectado: errores de API](#common-errors-1) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de exportación" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo para cada incidencia de exportación. Empieza en el paso 1.

1. Confirma si estás exportando al contenedor de S3 predeterminado de Braze o a un partner de almacenamiento en el cloud conectado. La expiración de enlaces y el comportamiento de reintentos difieren entre ambos.
2. Para exportaciones CSV del panel, confirma que has iniciado sesión en Braze al abrir el enlace de descarga. Los enlaces del contenedor predeterminado requieren una sesión activa en el panel.
3. Comprueba cuánto tiempo ha pasado desde que se completó la exportación. Los enlaces de descarga enviados por correo electrónico desde el panel caducan a las cuatro horas, tanto si usas el contenedor predeterminado de Braze como si tienes un partner de almacenamiento conectado. Cuando hay un partner de almacenamiento conectado, Braze también entrega una copia a tu contenedor; esa copia sigue tus políticas de retención y puede seguir disponible después de que el enlace del correo caduque.
4. Para exportaciones de segmentos grandes, confirma que la audiencia está por debajo del límite de 500 000 usuarios para exportaciones CSV del panel. Las estimaciones del constructor de segmentos pueden diferir de la evaluación del pipeline de exportación.
5. Para exportaciones por API, espera a que el procesamiento termine antes de descargar. Usa `callback_endpoint` en [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) o consulta con retirada exponencial en lugar de solicitar la URL de inmediato.
6. Si sigues bloqueado, contacta con [soporte de Braze]({{site.baseurl}}/braze_support) indicando el tipo de exportación (CSV o API), el ID de segmento o Campaign, la marca de tiempo (con zona horaria) y el mensaje de error exacto.

## Destinos de almacenamiento {#cloud-storage-connected}

Usa las pestañas para seleccionar si estás exportando al contenedor de S3 predeterminado de Braze o a un partner de almacenamiento en el cloud. Para orientación sobre almacenamiento en el cloud, abre la pestaña **Almacenamiento en el cloud conectado** y revisa las secciones de CSV y API.

{% sdktabs %}
{% sdktab Default export %}

Cuando no tienes un partner de almacenamiento marcado como destino de exportación predeterminado, Braze utiliza su propio contenedor de Amazon S3 para almacenar tus archivos de exportación. Los archivos en esta configuración son temporales y caducan a las cuatro horas.

### Exportaciones CSV {#csv-exports}

Síntoma: llega un correo electrónico de exportación CSV del panel, pero el enlace de descarga falla, o la exportación nunca se completa.


Cuando exportas un CSV desde el panel, Braze envía por correo electrónico un enlace de descarga al usuario que ha iniciado sesión. Ese enlace apunta a un archivo ZIP alojado en el contenedor de S3 de Braze. Dentro del ZIP hay varios archivos más pequeños que, juntos, conforman tu exportación.

Debes haber iniciado sesión en el panel de Braze para usar el enlace, y el archivo solo está disponible durante cuatro horas. Después de eso, el enlace deja de funcionar y los datos se eliminan. Si se producen fallos repetidos con exportaciones muy grandes (más de 500 000 usuarios), la exportación puede fallar. En ese caso, intenta dividir tu exportación en grupos o campos más pequeños, o considera configurar un partner de almacenamiento.

#### Errores comunes {#common-errors}

- Si ves un error `AccessDenied`, es posible que el archivo ya haya caducado o que hayas intentado abrirlo antes de que estuviera listo. Los informes más grandes tardan más en generarse, así que espera unos minutos y vuelve a intentarlo.
- Un error `ExpiredToken` significa que el plazo de cuatro horas ha vencido. Vuelve a ejecutar la exportación para generar un nuevo enlace.
- El mensaje `Looks like the file doesn't exist anymore` suele aparecer cuando se envía el correo electrónico, pero el archivo no ha terminado de cargarse en S3. Por lo general, esperar unos minutos resuelve el problema.
- Los apóstrofos que se añaden al principio de ciertos campos (como `-`, `=`, `+` o `@`) son un comportamiento esperado. Por ejemplo, `-1943` se convierte en `'-1943` en el CSV. Braze hace esto para evitar que los programas de hojas de cálculo interpreten erróneamente los datos. Esto no se aplica a las exportaciones JSON, como las devueltas por el [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### Exportaciones API {#api-exports}

Síntoma: una llamada a la API de exportación tiene éxito, pero la URL de descarga falla o devuelve datos vacíos.


Cuando exportas a través de las API de exportación sin almacenamiento en el cloud, Braze escribe los archivos en su contenedor de S3. No recibirás ningún correo electrónico; en su lugar, la respuesta de la API incluye una URL de descarga temporal. La exportación se presenta como un archivo ZIP que contiene varios archivos JSON, cada uno con un usuario por línea.

Al igual que las exportaciones CSV, los enlaces de la API caducan a las cuatro horas. Si abres el enlace demasiado pronto, es posible que aparezcan errores porque el archivo aún no está listo. Puedes proporcionar un `callback_endpoint` en tu solicitud si deseas que Braze te avise cuando el archivo esté disponible.

Las exportaciones API de gran tamaño también pueden agotar el tiempo de espera. Si eso ocurre, intenta realizar solicitudes más pequeñas o conecta un partner de almacenamiento para gestionar el volumen.

#### Errores comunes

- `AccessDenied` o `ExpiredToken` normalmente significan que el enlace ha caducado o aún no estaba listo. Vuelve a ejecutar la exportación o espera un poco más.

{% endsdktab %}

{% sdktab Cloud storage connected %}

Cuando conectas un partner de almacenamiento (como Amazon S3, Google Cloud Storage o Azure Blob) y lo marcas como tu destino de exportación predeterminado desde la página **Partners tecnológicos** del panel, Braze escribe tus exportaciones directamente en tu contenedor. Esta configuración suele ser más fiable para exportaciones de mayor tamaño.

### Exportaciones CSV {#csv-exports-1}

Síntoma: el enlace CSV enviado por correo electrónico falla, pero los archivos aparecen (o no aparecen) en tu contenedor conectado.


Con las exportaciones CSV, Braze te envía un enlace de descarga por correo electrónico. Ese enlace caduca tras un breve periodo de tiempo (normalmente unas cuatro horas). Cuando tienes un partner de almacenamiento conectado y marcado como tu destino de exportación predeterminado, Braze también entrega una copia de la exportación a tu contenedor conectado. Esa copia reside en tu propia infraestructura, donde la caducidad y la retención siguen tus políticas de almacenamiento.

En el almacenamiento en el cloud, las exportaciones CSV se agrupan en un archivo ZIP. Dentro del ZIP hay varios archivos CSV más pequeños. Las exportaciones grandes suelen dividirse en fragmentos (por ejemplo, unos 5000 usuarios cada uno), y el tamaño de los fragmentos puede variar. Los archivos más pequeños no indican que falten datos. Si el enlace enviado por correo electrónico falla, pero la copia en tu almacenamiento funciona, siempre puedes recuperar tus datos directamente desde tu contenedor.

#### Errores comunes

- `AccessDenied` significa que Braze no pudo escribir en tu contenedor. Comprueba que tus credenciales y permisos siguen siendo válidos.
- `ExpiredToken` aparece si Braze ha perdido el acceso a tu contenedor. Actualiza tus credenciales en el panel de Braze.
- Si algunos archivos parecen más pequeños de lo esperado, es un comportamiento normal. El proceso de exportación divide los archivos intencionadamente para garantizar la estabilidad.
- Los apóstrofos que se añaden al principio de ciertos campos (como `-`, `=`, `+` o `@`) son un comportamiento esperado. Por ejemplo, `-1943` se convierte en `'-1943` en el CSV. Braze hace esto para evitar que los programas de hojas de cálculo interpreten erróneamente los datos. Esto no se aplica a las exportaciones JSON, como las devueltas por el [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### Exportaciones API

Síntoma: las exportaciones API no aparecen en tu contenedor o los archivos están incompletos.


Cuando exportas datos a través de las API con un partner de almacenamiento conectado, los archivos exportados se escriben en tu contenedor. No se envía ningún correo electrónico. Los objetos subyacentes permanecen en tu almacenamiento y siguen tu configuración de retención, aunque las URL de descarga que devuelve Braze puedan seguir teniendo una duración limitada.

Los archivos suelen aparecer en tu contenedor a medida que se ejecuta la exportación, por lo que no necesitas esperar a que finalice todo el trabajo para acceder a resultados parciales. Braze carga cada lote completado de forma incremental en lugar de retener todo hasta el final. Las exportaciones grandes se dividen en varios archivos comprimidos (ZIP o GZIP), cada uno con objetos JSON, uno por línea. Esto hace que este método sea más fiable para exportaciones pesadas.

#### Errores comunes {#common-errors-1}

- `AccessDenied` ocurre cuando Braze no puede escribir en tu contenedor o los objetos se han eliminado posteriormente. Comprueba los permisos y confirma que ningún elemento externo esté borrando archivos.
- `ExpiredToken` significa que las credenciales de acceso de Braze a tu contenedor están desactualizadas. Actualízalas en el panel.
- Si faltan archivos o son más pequeños de lo esperado, primero confirma que nada fuera de Braze esté eliminando objetos. Los tamaños de archivo más pequeños son un comportamiento esperado.

{% endsdktab %}
{% endsdktabs %}

## Análisis de Campaign y Canvas {#campaign-and-canvas-analytics}

### El número de usuarios en la exportación CSV no coincide con *Messages Sent* o *Unique Recipients* {#number-of-users-in-csv-export-doesnt-match-messages-sent-or-unique-recipients}

Síntoma: la exportación CSV de una Campaign muestra un recuento de usuarios diferente al de *Messages Sent* o *Unique Recipients* en la página de análisis.


La exportación CSV de una Campaign puede mostrar un número de usuarios diferente al de *Messages Sent* y *Unique Recipients* por las siguientes razones:

#### La reelegibilidad está activada {#re-eligibility-is-turned-on}

Si los usuarios pueden (o pudieron en algún momento) recibir la Campaign más de una vez, las cifras de análisis de la Campaign y el número de filas en la exportación de datos de usuario no coinciden. *Messages Sent* cuenta cada envío, incluso cuando el mismo usuario recibe el mensaje más de una vez. La descarga de **CSV Export User Data** enumera usuarios únicos: una fila por perfil que recibió la Campaign, no una fila por envío. Por ejemplo, si *Messages Sent* es 12 y el CSV tiene 10 filas, esos 12 envíos se dirigieron a 10 usuarios distintos (algunos usuarios recibieron la Campaign más de una vez).

#### Se eliminaron o fusionaron usuarios desde que se envió la Campaign o el Canvas {#users-were-deleted-or-merged-since-the-campaign-or-canvas-sent}

La exportación CSV ofrece una instantánea de los usuarios existentes que recibieron una Campaign o un Canvas determinados. Dado que los usuarios pueden eliminarse o fusionarse, el recuento de la exportación CSV puede ser inferior al de destinatarios únicos. Por ejemplo, si 1000 usuarios reciben una Campaign, esta muestra 1000 destinatarios únicos y la exportación CSV de ese mismo día también muestra 1000 usuarios. Si un mes después se eliminan 50 de esos 1000 usuarios, la exportación CSV contiene 950 usuarios, mientras que el recuento acumulado de destinatarios únicos sigue siendo 1000.

## Correos electrónicos de exportación de segmentos del panel {#dashboard-segment-export-emails}

### El segmento es demasiado grande o la exportación falla cuando mi segmento parece tener menos de 500 000 usuarios {#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users}

Síntoma: la exportación de segmento del panel falla o muestra un error de tamaño aunque la estimación del segmento parece aceptable.


El **tamaño de un segmento del panel es una estimación**. La exportación CSV utiliza esa estimación para aplicar el [límite de exportación de 500 000 usuarios]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details); el pipeline de exportación también puede evaluar el tamaño de forma diferente a la interfaz del constructor de segmentos. Si las exportaciones fallan para un segmento cercano a ese umbral, usa [números de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) o divide la audiencia en segmentos más pequeños, o usa el [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) como se describe en [Exportar segmentos grandes]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#exporting-large-segments).

### ¿Por qué no recibo los correos electrónicos de exportación de segmentos? {#not-receiving-segment-export-emails}

Síntoma: se activó una exportación CSV de segmento, pero no llegó ningún correo electrónico.


Primero, revisa tu carpeta de correo no deseado en busca de un correo electrónico de `no-reply@alerts.braze.com`. Si el correo está ahí, añade esa dirección a tu lista de remitentes seguros para que los futuros mensajes de exportación no se filtren.

Si el correo no está en tu carpeta de correo no deseado, comprueba si otra persona de tu equipo puede recibir la exportación. Si tampoco puede, considera el tamaño de tu exportación. El tiempo de entrega varía según el tamaño de la exportación, pero si el correo no ha llegado después de una hora, contacta con [soporte]({{site.baseurl}}/braze_support).

## Descargas de la API de exportación de segmentos {#segment-export-api-downloads}

### No se puede descargar un ZIP de segmento exportado desde una URL de Braze {#cant-download-an-exported-segment-zip-from-a-braze-url}

Síntoma: un error `403 Forbidden` al descargar desde la URL de respuesta de `/users/export/segment`.


Si obtienes un error `403 Forbidden` al usar el [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment), es posible que el archivo aún no esté listo. Las exportaciones grandes pueden tardar un tiempo en procesarse. Espera hasta una hora antes de intentar la descarga de nuevo.

Si usas un script automatizado para recuperar el archivo, también puedes recibir un error `403 Forbidden` cuando solicitas la URL demasiado pronto. Si exportas datos de segmentos de forma regular, considera conectar tu propia integración con un contenedor de S3 y pasar los archivos a tu propio pipeline de extracción, transformación y carga (ETL).

Las exportaciones tardan en completarse, por lo que el acceso inmediato desde un script suele fallar. Puedes:

- Consultar la URL de descarga con retirada exponencial, o
- Usar el [parámetro `callback_endpoint`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#request-parameters) y apuntarlo a un servicio que ejecute tu script cuando la exportación esté lista.

## Campos de la API de exportación de segmentos y usuarios {#segment-and-user-export-api-fields}

### Faltan columnas esperadas en un archivo de exportación de segmento {#expected-columns-are-missing-from-a-segment-export-file}

Síntoma: una exportación por API o del panel no incluye campos que esperabas.


La descarga de **CSV Export User Data** del panel desde un segmento utiliza un conjunto fijo de columnas (consulta [Exportar datos de segmento a CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#data-included-in-export)). No incluye una columna ni un parámetro `fields_to_export`.

Para las exportaciones de segmentos por API, debes pasar `fields_to_export` en el cuerpo de la solicitud. Algunos campos extraen datos relacionados automáticamente; por ejemplo, solicitar `canvases_received` también requiere datos de resumen de recorrido en el perfil de usuario. Consulta la referencia del [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para conocer los nombres de campo válidos y los requisitos.

Si faltan columnas en un archivo ZIP de exportación por API, confirma que el array `fields_to_export` de tu solicitud incluye todos los campos que necesitas y que tu espacio de trabajo cuenta con los permisos de exportación necesarios.

## Cuándo contactar con soporte {#when-to-contact-support}

Contacta con [soporte de Braze]({{site.baseurl}}/braze_support) si has completado la [ruta de investigación estándar](#standard-investigation-path) y aún necesitas ayuda. Incluye el tipo de exportación, el ID de segmento o Campaign, la marca de tiempo (con zona horaria) y el mensaje de error exacto o el código de estado HTTP.