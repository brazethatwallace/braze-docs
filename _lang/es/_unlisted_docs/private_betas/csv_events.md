---
nav_title: Importar datos de usuario y eventos CSV
article_title: Importar datos de usuario y eventos CSV
permalink: "/csv_events/"
description: "Este artículo de referencia cubre cómo importar datos de usuario y cómo importar eventos personalizados utilizando archivos CSV."
page_type: reference
---

# Importar datos de usuario (acceso anticipado a eventos CSV) {#importing-user-data-csv-events-early-access}

> Braze ofrece diversas formas de importar datos de usuario a la plataforma: SDK, API, ingesta de datos en la nube, integraciones de partners tecnológicos y archivos CSV. Este artículo proporciona instrucciones detalladas sobre cómo importar datos de usuario, incluyendo cómo [importar eventos personalizados a través de archivos CSV (acceso anticipado)](#importing-custom-events).

{% alert important %}
No envíes correos transaccionales legalmente obligatorios a pasarelas SMS, ya que existe una alta probabilidad de que esos correos electrónicos no se entreguen.

Aunque los correos electrónicos que envías usando un número de teléfono y el dominio de pasarela de correo electrónico a SMS del proveedor (MM3) pueden resultar en que el correo electrónico se reciba como un mensaje SMS (texto), algunos proveedores de correo electrónico no admiten este comportamiento. Por ejemplo, si envías un correo electrónico a un número de teléfono de T-Mobile (como "9999999999@tmomail.net"), tu mensaje SMS se enviaría a quien sea propietario de ese número de teléfono en la red de T-Mobile.

Aunque estos correos electrónicos no se entreguen a la pasarela SMS, siguen contando para tu facturación de correo electrónico. Para evitar enviar correos electrónicos a pasarelas no compatibles, revisa la [lista de nombres de dominio de pasarelas no compatibles](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}


Antes de continuar, ten en cuenta que Braze no sanea (valida ni formatea correctamente) los datos HTML durante la importación. Esto significa que las etiquetas de script deben eliminarse de todos los datos de importación destinados a la personalización web.

## REST API

Puedes usar el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para registrar eventos personalizados, atributos de usuario y compras para los usuarios.

## Importación CSV {#csv-import}

Puedes cargar y actualizar perfiles de usuario mediante archivos CSV desde **Audiencia** > **Importar usuarios**.

La importación de datos de usuario mediante archivos CSV permite registrar y actualizar atributos de usuario como nombre y correo electrónico, además de atributos personalizados como la talla de zapato. Puedes importar un CSV especificando uno de los dos identificadores de usuario únicos: un `external_id` o un alias de usuario.

{% alert important %}
La importación de usuarios también permite registrar y actualizar eventos personalizados de usuario. De forma similar a los atributos de usuario, puedes importar con un `external_id`, `braze_id` o con `user_alias_name` junto con `user_alias_label`. Para más detalles, consulta [Importar eventos personalizados](#importing-custom-events).
{% endalert %}

{% alert note %}
Si estás cargando una mezcla de usuarios con un `external_id` y usuarios sin él, necesitas crear un archivo CSV para cada importación. Un archivo CSV no puede contener tanto `external_ids` como alias de usuario.
{% endalert %}

### Importar con ID externo {#importing-with-external-id}

Al importar tus datos de clientes, necesitarás especificar el identificador único de cada cliente, también conocido como `external_id`. Antes de comenzar tu importación CSV, es importante que tu equipo de ingeniería te explique cómo se identificarán los usuarios en Braze. Normalmente, se trata de un ID interno de base de datos. Esto debe estar alineado con la forma en que los usuarios serán identificados por el SDK de Braze en móvil y web, y está diseñado para que cada cliente tenga un único perfil de usuario en Braze en todos sus dispositivos. Lee más sobre el [ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle) de Braze.

Cuando proporcionas un `external_id` en tu importación, Braze actualizará cualquier usuario existente con el mismo `external_id` o creará un nuevo usuario identificado con ese `external_id` establecido si no se encuentra uno.

- **Descargar:** [Plantilla de importación de atributos CSV][import_template]
- **Descargar:** [Plantilla de importación de eventos CSV][events_template]

### Importar con alias de usuario {#importing-with-user-alias}

Para dirigirte a usuarios que no tienen un `external_id`, puedes importar una lista de usuarios con alias de usuario. Un alias sirve como identificador de usuario único alternativo y puede ser útil si intentas hacer marketing a usuarios anónimos que no se han registrado o creado una cuenta en tu aplicación.

Si estás cargando o actualizando perfiles de usuario que solo tienen alias, debes tener las siguientes dos columnas en tu CSV:

- `user_alias_name`: Un identificador de usuario único; una alternativa al `external_id`
- `user_alias_label`: Una etiqueta común para agrupar alias de usuario

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Cuando proporcionas tanto un `user_alias_name` como un `user_alias_label` en tu importación, Braze actualizará cualquier usuario existente con el mismo `user_alias_name` y `user_alias_label`. Si no se encuentra un usuario, Braze creará un nuevo usuario identificado con ese `user_alias_name` establecido.

{% alert important %}
No puedes usar una importación CSV para actualizar un usuario existente con un `user_alias_name` si ya tiene un `external_id`. En su lugar, esto creará un nuevo perfil de usuario con el `user_alias_name` asociado. Para asociar un usuario de solo alias con un `external_id`, usa el [endpoint Identificar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).
{% endalert %}

- **Descargar:** [Plantilla de importación de atributos de alias CSV][template_alias_attributes]
- **Descargar:** [Plantilla de importación de eventos de alias CSV][template_alias_events]

### Importar con Braze ID {#importing-with-braze-id}

Para actualizar perfiles de usuario existentes en Braze usando un valor de Braze ID interno en lugar de un valor de `external_id` o `user_alias_name` y `user_alias_label`, especifica `braze_id` como encabezado de columna.

Esto puede ser útil si exportaste datos de usuario de Braze a través de nuestra opción de exportación CSV dentro de la segmentación y deseas añadir un nuevo atributo personalizado a esos usuarios existentes.

{% alert important %}
No puedes usar una importación CSV para crear un nuevo usuario usando `braze_id`. Este método solo se puede usar para actualizar usuarios preexistentes en la plataforma Braze.
{% endalert %}

{% alert tip %}
El valor de `braze_id` puede estar etiquetado como `Appboy ID` en las exportaciones CSV del panel de Braze. Este ID será el mismo que el `braze_id` de un usuario, por lo que puedes renombrar esta columna a `braze_id` cuando reimportes el CSV.
{% endalert %}

### Importar atributos predeterminados {#importing-default-attributes}

Para importar atributos predeterminados de usuarios, ve a **Importar usuarios** > **Atributos**. Los atributos predeterminados de usuario son claves reservadas en Braze. Por ejemplo, `first_name` o `email`. Los atributos personalizados son propios de tu negocio. Por ejemplo, una aplicación de reserva de viajes puede tener un atributo personalizado llamado `last_destination_searched`.

{% alert important %}
Al importar datos de clientes como atributos, los encabezados de columna que uses deben coincidir exactamente con la ortografía y la capitalización de los atributos predeterminados de usuario. De lo contrario, Braze creará automáticamente un atributo personalizado en el perfil de ese usuario.
{% endalert %}

#### Encabezados de columna de datos de usuario predeterminados {#default-user-data-column-headers}

| CAMPO DEL PERFIL DE USUARIO | TIPO DE DATOS | INFORMACIÓN | OBLIGATORIO |
|---|---|---|---|
| `external_id` | Cadena | Un identificador de usuario único para tu cliente. | Sí, consulta la [nota siguiente](#about-external-ids). |
| `user_alias_name` | Cadena | Un identificador de usuario único para usuarios anónimos. Una alternativa al `external_id`. | No, consulta la [nota siguiente](#about-external-ids). |
| `user_alias_label` | Cadena | Una etiqueta común para agrupar alias de usuario. | Sí, si se usa `user_alias_name`. |
| `first_name` | Cadena | El nombre de tus usuarios tal como lo han indicado (por ejemplo, `Jane`). | No |
| `last_name` | Cadena | El apellido de tus usuarios tal como lo han indicado (por ejemplo, `Doe`). | No |
| `email` | Cadena | El correo electrónico de tus usuarios tal como lo han indicado (por ejemplo, `jane.doe@braze.com`). | No |
| `country` | Cadena | Los códigos de país deben pasarse a Braze en el estándar ISO-3166-1 alfa-2 (por ejemplo, `GB`). | No |
| `dob` | Cadena | Debe pasarse en el formato "AAAA-MM-DD" (por ejemplo, `1980-12-21`). Esto importará la fecha de nacimiento de tu usuario y te permitirá dirigirte a usuarios cuyo cumpleaños sea "hoy". | No |
| `gender` | Cadena | "M", "F", "O" (otro), "N" (no aplicable), "P" (prefiere no decir), o nil (desconocido). | No |
| `home_city` | Cadena | La ciudad de residencia de tus usuarios tal como la han indicado (por ejemplo, `London`). | No |
| `language` | Cadena | El idioma debe pasarse a Braze en el estándar ISO-639-1 (por ejemplo, `en`). <br>Consulta nuestra [lista de idiomas aceptados]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes). | No |
| `phone` | Cadena | Un número de teléfono indicado por tus usuarios, en formato `E.164` (por ejemplo, `+442071838750`). <br> Consulta [Números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers) para orientación sobre el formato. | No |
| `email_open_tracking_disabled` | Booleano | Se acepta true o false. Establécelo en true para deshabilitar la adición del píxel de seguimiento de apertura a todos los correos electrónicos futuros enviados a este usuario. | No |
| `email_click_tracking_disabled` | Booleano | Se acepta true o false. Establécelo en true para deshabilitar el seguimiento de clics en todos los enlaces de un correo electrónico futuro enviado a este usuario. | No |
| `email_subscribe` | Cadena | Los valores disponibles son `opted_in` (registrado explícitamente para recibir mensajes de correo electrónico), `unsubscribed` (canceló explícitamente la suscripción a mensajes de correo electrónico) y `subscribed` (ni optó por recibir ni canceló la suscripción). | No |
| `push_subscribe` | Cadena | Los valores disponibles son `opted_in` (registrado explícitamente para recibir mensajes push), `unsubscribed` (canceló explícitamente la suscripción a mensajes push) y `subscribed` (ni optó por recibir ni canceló la suscripción). | No |
| `time_zone` | Cadena | La zona horaria debe pasarse a Braze en el mismo formato que la base de datos de zonas horarias de la IANA (por ejemplo, `America/New_York` o `Eastern Time (US & Canada)`). | No |
| `date_of_first_session` <br><br> `date_of_last_session`| Cadena | Puede pasarse en uno de los siguientes formatos ISO-8601: {::nomarkdown} <ul> <li> "AAAA-MM-DD" </li> <li> "AAAA-MM-DDTHH:MM:SS+00:00" </li> <li> "AAAA-MM-DDTHH:MM:SSZ" </li> <li> "AAAA-MM-DDTHH:MM:SS" (por ejemplo, 2019-11-20T18:38:57) </li> </ul> {:/} | No |
| `subscription_group_id` | Cadena | El `id` de tu grupo de suscripción. Este identificador se puede encontrar en la página del grupo de suscripción de tu panel. | No |
| `subscription_state` | Cadena | El estado de suscripción para el grupo de suscripción especificado por `subscription_group_id`. Los valores permitidos son `unsubscribed` (no está en el grupo de suscripción) o `subscribed` (está en el grupo de suscripción). | No, pero se recomienda encarecidamente si se usa `subscription_group_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### Acerca de los ID externos {#about-external-ids}

Aunque `external_id` no es obligatorio, **debes** incluir uno de estos campos:
- `external_id`: Un identificador de usuario único para tu cliente, **o**
- `braze_id`: Un identificador de usuario único obtenido para usuarios existentes de Braze, **o**
- `user_alias_name` y `user_alias_label`: Un identificador de usuario único para un usuario anónimo

### Importar atributos personalizados {#importing-custom-attributes}

Puedes importar atributos personalizados para usuarios yendo a **Importar usuarios** > **Atributos**. Cualquier encabezado que no coincida exactamente con los atributos predeterminados creará un atributo personalizado en Braze.

Los siguientes tipos de datos se aceptan en la importación de usuarios:

| Tipo de datos | Descripción |
|-----------|-------------|
| Datetime | Debe almacenarse en formato ISO-8601 |
| Booleano | TRUE o FALSE |
| Número | Entero o flotante sin espacios ni comas, los flotantes deben usar un punto (.) como separador decimal |
| Cadena | Puede contener comas siempre que haya comillas dobles rodeando el valor de la columna |
| En blanco | Los valores en blanco no sobrescribirán los valores existentes en el perfil de usuario, y no necesitas incluir todos los atributos de usuario existentes en tu archivo CSV |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Los arreglos y los tokens de notificaciones push no son compatibles con la importación de usuarios. Especialmente para los arreglos, las comas en tu archivo CSV se interpretarán como separadores de columna, por lo que cualquier coma en los valores causará errores al analizar el archivo. <br>Para cargar este tipo de valores, usa el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) o [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion).
{% endalert %}

### Actualizar el estado del grupo de suscripción {#updating-subscription-group-status}

Puedes añadir usuarios a grupos de suscripción de correo electrónico o SMS mediante la importación de usuarios. Esto es particularmente útil para SMS, ya que un usuario debe estar inscrito en un grupo de suscripción de SMS para recibir mensajes por el canal de SMS. Para más información, consulta [Grupos de suscripción de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#subscription-group-mms-enablement).

Si estás actualizando el estado del grupo de suscripción, debes tener las siguientes dos columnas en tu CSV:

- `subscription_group_id`: El `id` del [grupo de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups).
- `subscription_state`: Los valores disponibles son `unsubscribed` (no está en el grupo de suscripción) o `subscribed` (está en el grupo de suscripción).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="Actualizar el estado del grupo de suscripción">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
</tbody>
</table>

{% alert important %}
Solo se puede establecer un único `subscription_group_id` por fila en la importación de usuarios. Las diferentes filas pueden tener distintos valores de `subscription_group_id`. Sin embargo, si necesitas inscribir a los mismos usuarios en varios grupos de suscripción, tendrás que realizar múltiples importaciones.
{% endalert %}

### Importar eventos personalizados (acceso anticipado) {#importing-custom-events}

{% alert important %}
La importación de eventos personalizados se encuentra actualmente en acceso anticipado. Contacta a tu director de cuentas de Braze si te interesa participar en el acceso anticipado.
{% endalert %}

Para importar eventos personalizados de tus usuarios, ve a **Importar usuarios** > **Eventos**.

Los eventos personalizados son propios de tu negocio. Por ejemplo, una aplicación de streaming puede tener un evento personalizado llamado rented_movie. Tu CSV debe tener encabezados de columna para:

- Uno de los siguientes:
  - `external_id`, **o**
  - `braze_id`, **o**
  - `user_alias_name` y `user_alias_label`
- Name
- Time

Los eventos personalizados pueden tener propiedades del evento. Por ejemplo, el evento personalizado rented_movie puede tener las propiedades title y genre. Estas propiedades del evento deben tener un encabezado de columna de `<event_name>.properties.<property name>`. Un ejemplo es `rented_movie.properties.title`.

| CAMPO DEL PERFIL DE USUARIO                | TIPO DE DATOS | INFORMACIÓN                                                                                                                                                                                                             | OBLIGATORIO                                                                                     |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id`                           | Cadena    | Un identificador de usuario único para tu usuario.                                                                                                                                                                      | Sí, se requiere uno de `external_id`, `braze_id`, o `user_alias_name` y `user_alias_label`. |
| `braze_id`                              | Cadena    | Un identificador asignado por Braze para tu usuario.                                                                                                                                                                    | Sí, se requiere uno de `external_id`, `braze_id`, o `user_alias_name` y `user_alias_label`. |
| `user_alias_name`                       | Cadena    | Un identificador de usuario único para usuarios anónimos. Una alternativa al external_id.                                                                                                                               | Sí, se requiere uno de `external_id`, `braze_id`, o `user_alias_name` y `user_alias_label`. |
| `user_alias_label`                      | Cadena    | Una etiqueta común para agrupar alias de usuario.                                                                                                                                                                       | Sí, se requiere uno de `external_id`, `braze_id`, o `user_alias_name` y `user_alias_label`. |
| `name`                                  | Cadena    | Un evento personalizado de tus usuarios.                                                                                                                                                                                | Sí                                                                                             |
| `time`                                  | Cadena    | La hora del evento. Puede pasarse en uno de los siguientes formatos ISO-8601: {::nomarkdown} <ul> <li> "AAAA-MM-DD" </li> <li> "AAAA-MM-DDTHH:MM:SS+00:00" </li> <li> "AAAA-MM-DDTHH:MM:SSZ" </li> <li> "AAAA-MM-DDTHH:MM:SS" (por ejemplo, 2019-11-20T18:38:57) </li> </ul> {:/} | Sí                                                                                             |
| `<event name>.properties.<property name>` | Múltiple  | Una propiedad del evento asociada a un evento personalizado. Un ejemplo es `rented_movie.properties.title`                                                                                                              | No                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Aunque external_id en sí no es obligatorio, debes incluir uno de los siguientes campos: <br>- `external_id`: Un identificador de usuario único para tu cliente <br>- `braze_id`: Un identificador de usuario único obtenido para usuarios existentes de Braze <br>- `user_alias_name`: Un identificador de usuario único para un usuario anónimo
{% endalert %}

#### Tamaño del CSV {#csv-size}

Braze acepta datos de usuario en el formato CSV estándar de archivos de hasta 500 MB de tamaño. Para descargar una de nuestras plantillas de archivo CSV, consulta [Importar con ID externo](#importing-with-external-id) o [Importar con alias de usuario](#importing-with-user-alias).

#### Consideraciones de puntos de datos {#data-point-considerations}

Cada dato de cliente importado a través de CSV sobrescribirá el valor existente en los perfiles de usuario y contará como un punto de datos, excepto los ID externos y los valores en blanco.

- Los ID externos cargados mediante importación CSV no consumirán puntos de datos. Si estás cargando un archivo CSV para segmentar usuarios existentes de Braze cargando solo ID externos, esto se puede hacer sin consumir puntos de datos. Si añadieras datos adicionales como el correo electrónico o el número de teléfono de un usuario en tu importación, eso sobrescribiría los datos de usuario existentes y consumiría tus puntos de datos.
    - Las importaciones CSV para fines de segmentación (importaciones realizadas con `external_id`, `braze_id` o `user_alias_name` como único campo) no consumirán puntos de datos.
- Los valores en blanco no sobrescribirán los valores existentes en el perfil de usuario, y no necesitas incluir todos los atributos de usuario o eventos personalizados existentes en tu archivo CSV.
- Actualizar `email_subscribe`, `push_subscribe`, `subscription_group_id` o `subscription_state` no contará para el consumo de puntos de datos.

{% alert important %}
Establecer el idioma o el país de un usuario a través de importación CSV o API evitará que Braze capture automáticamente esta información a través del SDK.
{% endalert %}

## Importar un CSV {#importing-a-csv}

Para importar tu archivo CSV:
1. Ve a **Audiencia** > **Importar usuarios**.
2. Selecciona **Examinar archivos** y selecciona el archivo que te interese, luego selecciona **Iniciar importación**. Braze cargará tu archivo y comprobará los encabezados de columna, así como los tipos de datos de cada columna.

{% alert important %}
Las importaciones de CSV distinguen entre mayúsculas y minúsculas. Esto significa que las letras mayúsculas en las importaciones de CSV escribirán el campo como un atributo personalizado en lugar de uno estándar. Por ejemplo, "email" es correcto, pero "Email" se escribiría como un atributo personalizado.
{% endalert %}

![La opción "Events" está seleccionada como el tipo de información de usuario a importar.][5]

Una vez completada la carga, puedes ver una vista previa del contenido de tu archivo. La información de la tabla se basa en los valores de las filas superiores de tu archivo CSV.

Puedes hacer seguimiento del progreso en la página **Importar usuarios**, que se actualiza cada cinco segundos, o cuando seleccionas **Actualizar tabla**. Puedes seguir utilizando el resto del panel de Braze durante la importación, y recibirás notificaciones cuando la importación comience y finalice.

También puedes ver tus importaciones más recientes, sus nombres de archivo, tipo de CSV, número de líneas en el archivo, número de líneas importadas correctamente, total de líneas en cada archivo y el estado de cada importación.

Puedes importar más de un archivo CSV a la vez. Las importaciones de CSV se ejecutarán simultáneamente, lo que significa que no se garantiza que el orden de las actualizaciones sea secuencial. Si necesitas que las importaciones de CSV se ejecuten una tras otra, debes esperar a que una importación de CSV haya finalizado antes de cargar una segunda.

Si el proceso de importación encuentra un error, aparecerá un icono de advertencia junto al número total de líneas del archivo. Puedes pasar el cursor sobre el icono para ver detalles sobre por qué fallaron ciertas líneas. Una vez completada la importación, todos los datos se añadirán a los perfiles existentes, o se crearán perfiles nuevos.

![Carga de archivo CSV completada con errores que involucran tipos de datos mixtos en una sola columna][4]{: style="max-width:70%"}

### Consideraciones {#considerations}

Si Braze detecta algo con formato incorrecto en las filas superiores de tu archivo durante la carga, estos errores se mostrarán con el resumen. Por ejemplo, si tu archivo incluye una fila con formato incorrecto, este error se indicará en la vista previa cuando importes el archivo. Aunque un archivo puede importarse con errores, se recomienda que corrijas dichos errores en tu archivo antes de continuar con la importación.

Además, es importante examinar el archivo CSV completo antes de cargarlo, ya que Braze no analiza cada fila del archivo de entrada para la vista previa. Esto significa que pueden existir errores que Braze no detecta al generar esta vista previa.

Las filas con formato incorrecto y las filas que carecen de un ID externo no se importarán. Todos los demás errores pueden importarse, pero podrían interferir con el filtrado al crear un Segment. Para más información, consulta la sección [Solución de problemas](#troubleshooting).

{% alert warning %}
Los errores se basan únicamente en el tipo de datos y la estructura del archivo. Por ejemplo, una dirección de correo electrónico con formato incorrecto se importaría de todos modos, ya que aún puede analizarse como una cadena.
{% endalert %}

### Importación Lambda de CSV de usuarios {#lambda-user-csv-import}

Puedes utilizar nuestro script Lambda serverless de importación de CSV desde S3 para cargar atributos de usuario en la plataforma. Esta solución funciona como un cargador de CSV en el que colocas tus archivos CSV en un contenedor de S3, y los scripts los cargan a través de nuestra API.

Los tiempos de ejecución estimados para un archivo con un millón de filas deberían ser de aproximadamente cinco minutos. Para más información, consulta [Importación de CSV de atributos de usuario a Braze]({{site.baseurl}}/user_csv_lambda).

## Segmentación {#segmenting}

La importación de usuarios crea y actualiza perfiles de usuario, y también se puede utilizar para crear Segments. Para crear un Segment, selecciona **Generar automáticamente un segmento a partir de los usuarios que se importan desde este CSV** antes de iniciar la importación.

Puedes establecer el nombre del segmento o aceptar el predeterminado, que es el nombre de tu archivo. Los archivos que se utilizaron para crear un segmento tendrán un enlace para ver el segmento una vez que se haya completado la importación.

El filtro utilizado para crear el segmento selecciona a los usuarios que fueron creados o actualizados en una importación seleccionada y está disponible junto con todos los demás filtros en la página de edición de segmentos.

## Solución de problemas {#troubleshooting}

### Filas faltantes {#missing-rows}

Hay algunas razones por las que el número de usuarios importados podría no coincidir con el total de filas en tu archivo CSV:

- **ID externos duplicados:** Si hay columnas de ID externo duplicadas, esto puede causar filas mal formadas o no importadas incluso si las filas están correctamente formateadas. En algunos casos, esto puede no reportar un error específico. Verifica si hay ID externos duplicados en tu CSV. Si es así, elimina los duplicados e intenta cargar de nuevo.
- **Caracteres acentuados:** Tu archivo CSV puede tener nombres o atributos que incluyen acentos. Asegúrate de que tu archivo esté codificado en UTF-8 para evitar cualquier problema.

### Fila mal formada {#malformed-row}

Debes incluir una fila de encabezado en tu archivo CSV para importar correctamente tus datos. Cada fila debe tener el mismo número de celdas que la fila de encabezado. Las filas con más o menos valores que la fila de encabezado se excluirán de la importación. Las comas en un valor se interpretarán como un separador y pueden provocar este error. Además, todos los datos deben estar codificados en UTF-8.

Si tu archivo CSV tiene filas en blanco e importa menos filas que el total de líneas en el archivo CSV, esto puede no indicar un problema con la importación, ya que las filas en blanco no necesitarían importarse. Verifica el número de líneas que se importaron correctamente y asegúrate de que coincida con el número de usuarios que intentas importar.

### Múltiples tipos de datos {#multiple-data-types}

Braze espera que cada valor en una columna sea del mismo tipo de datos. Los valores que no coincidan con el tipo de datos de su atributo causarán errores en la segmentación.

### Fechas con formato incorrecto {#incorrectly-formatted-dates}

Las fechas que no estén en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) no se leerán como fechas y horas en la importación.

### Comillas en cadenas {#string-quotation}

Los valores encapsulados en comillas simples ('') o dobles ("") se leerán como cadenas en la importación.

### Datos importados como atributo personalizado {#data-imported-as-custom-attribute}

Si ves que un dato de usuario predeterminado (por ejemplo, `email` o `first_name`) se importó como un atributo personalizado, verifica las mayúsculas y los espacios de tu archivo CSV. Por ejemplo, `First_name` se importaría como un atributo personalizado, mientras que `first_name` se importaría correctamente en el campo "first name" del perfil de un usuario.

[import_template]: {% image_buster /assets/unlisted_docs/download_file/braze-user-import-template-csv.xlsx %}
[events_template]: {% image_buster /assets/unlisted_docs/download_file/braze-csv-events-import-template.csv %}
[template_alias_attributes]: {% image_buster /assets/unlisted_docs/download_file/braze-user-import-alias-template-csv.xlsx %}
[template_alias_events]: {% image_buster /assets/unlisted_docs/download_file/braze-events-csv-example-user-alias.csv %}
[3]: {% image_buster /assets/unlisted_docs/img/importcsv5.png %}
[4]: {% image_buster /assets/unlisted_docs/img/importcsv2.png %}
[5]: {% image_buster /assets/unlisted_docs/img/importcsv3.png %}
[7]: {% image_buster /assets/unlisted_docs/img/segment-imported-users.png %}
[8]: {% image_buster /assets/unlisted_docs/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/unlisted_docs/img/subscription_group_import.png %}