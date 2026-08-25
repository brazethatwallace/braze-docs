---
nav_title: Importación CSV
article_title: Importación CSV
description: "Aprende a registrar y actualizar atributos de usuario y eventos personalizados mediante la importación CSV."
page_order: 1.2
---

# Importación CSV {#csv-import}

> Aprende a registrar y actualizar atributos de usuario y eventos personalizados mediante la importación CSV.

## Acerca de la importación en CSV {#about-csv-import}

Puedes usar la importación en CSV para registrar y actualizar los siguientes atributos de usuario y eventos personalizados. Braze acepta estos datos como archivos CSV estándar dentro de los tamaños máximos indicados en la siguiente tabla.

| Tipo | Definición | Ejemplo | Tamaño máximo de archivo |
|---|---|---|---|
| Atributos predeterminados | Atributos de usuario reservados reconocidos por Braze. | `first_name`, `email` | 500 MB |
| Atributos personalizados | Atributos de usuario exclusivos de tu negocio. | `last_destination_searched` | 500 MB |
| Eventos personalizados | Eventos exclusivos de tu negocio que representan acciones de los usuarios. | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Acerca de la importación en CSV" }

## Uso de la importación CSV {#using-csv-import}

### Paso 1: Descarga una plantilla CSV {#step-1-download-a-csv-template}

Para abrir la importación CSV, ve a **Audiencias** > **Importar usuarios**. Aquí encontrarás una tabla con los detalles de las importaciones más recientes, como la fecha de carga, el nombre de quien realizó la carga, el nombre del archivo, la disponibilidad de segmentación, el número de filas importadas y el estado de la importación.

Para empezar, selecciona **Atributos** o **Eventos** y descarga la plantilla correspondiente para construir tu archivo CSV para carga.

![La página "Importar usuarios" en el panel de Braze.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Paso 2: Elige un identificador {#choose-an-identifier}

El archivo CSV que importes necesita un identificador dedicado. Elige uno de los siguientes tipos de identificador para tu importación:

{% tabs local %}
<!-- TAB -->
{% tab ID externo %}
Al importar los datos de tus clientes, puedes usar un `external_id` como identificador único de cada cliente. Cuando proporcionas un `external_id` en tu importación, Braze actualiza cualquier usuario existente con el mismo `external_id` o crea un nuevo usuario identificado con ese `external_id` establecido si no se encuentra uno.

- Descarga: [Plantilla de importación de atributos CSV: ID externo]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Descarga: [Plantilla de importación de eventos CSV: ID externo](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Si estás cargando una mezcla de usuarios con un `external_id` y usuarios sin él, necesitas crear un CSV para cada importación. Un CSV no puede contener tanto `external_id` como alias de usuario.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab Alias de usuario %}
Para dirigirte a usuarios que no tienen un `external_id`, puedes importar una lista de usuarios con alias de usuario. Un alias sirve como identificador único alternativo del usuario y puede ser útil si estás intentando dirigirte a usuarios anónimos que no se han registrado ni han creado una cuenta en tu aplicación.

Si estás cargando o actualizando perfiles de usuario que son solo de alias, debes tener las siguientes dos columnas en tu CSV:

- `user_alias_name`: Un identificador único de usuario; una alternativa al `external_id`
- `user_alias_label`: Una etiqueta común para agrupar alias de usuario

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@example.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@example.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Paso 2: Elige un identificador" }

Cuando proporcionas tanto un `user_alias_name` como un `user_alias_label` en tu importación, Braze actualiza cualquier usuario existente con el mismo `user_alias_name` y `user_alias_label`. Si no se encuentra un usuario, Braze crea un nuevo usuario identificado con ese `user_alias_name` establecido.

{% alert important %}
No puedes usar una importación CSV para actualizar un usuario existente con un `user_alias_name` si ya tiene un `external_id`. En su lugar, esto crea un nuevo perfil de usuario con el `user_alias_name` asociado. Para asociar un usuario solo de alias con un `external_id`, usa el [endpoint Identificar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).
{% endalert %}

Descarga: [Plantilla de importación de atributos CSV: alias de usuario]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab ID de Braze %}
Para actualizar perfiles de usuario existentes en Braze usando un valor de ID interno de Braze en lugar de un `external_id` o un valor de `user_alias_name` y `user_alias_label`, especifica `braze_id` como encabezado de columna.

Esto puede ser útil si exportaste datos de usuario de Braze a través de nuestra opción de exportación CSV dentro de la segmentación y quieres añadir un nuevo atributo personalizado a esos usuarios existentes.

{% alert important %}
No puedes usar una importación CSV para crear un nuevo usuario usando `braze_id`. Este método solo se puede usar para actualizar usuarios preexistentes dentro de la plataforma Braze.
{% endalert %}

{% alert tip %}
El valor de `braze_id` podría estar etiquetado como `Appboy ID` en las exportaciones CSV del panel de Braze. Este ID será el mismo que el `braze_id` para un usuario, por lo que puedes renombrar esta columna a `braze_id` cuando reimportes el CSV.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab Dirección de correo electrónico y números de teléfono %}
Puedes omitir un ID externo o un alias de usuario y usar una dirección de correo electrónico o un número de teléfono para importar usuarios. Antes de importar un archivo CSV con direcciones de correo electrónico o números de teléfono, verifica lo siguiente:

- Comprueba que no tengas ningún ID externo ni alias de usuario para estos perfiles en tu archivo CSV. Si los tienes, Braze priorizará el uso del ID externo o el alias de usuario antes que la dirección de correo electrónico para identificar perfiles.
- Confirma que tu archivo CSV tiene el formato correcto.

{% alert note %}
Si incluyes tanto direcciones de correo electrónico como números de teléfono en tu archivo CSV, la dirección de correo electrónico tiene prioridad sobre el número de teléfono al buscar perfiles.
{% endalert %}

Si un perfil existente tiene esa dirección de correo electrónico o número de teléfono, ese perfil se actualiza y Braze no crea un nuevo perfil. Si hay múltiples perfiles con la misma dirección de correo electrónico, Braze usará la misma lógica que el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), donde se actualizará el perfil modificado más recientemente.

Si no existe un perfil con esa dirección de correo electrónico o número de teléfono, Braze crea un nuevo perfil con ese identificador. Puedes usar el [endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) para identificar este perfil posteriormente. Para eliminar un perfil de usuario, también puedes usar el [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete).
{% endtab %}
{% endtabs %}

### Paso 3: Construye tu archivo CSV {#step-3-build-your-csv-file}

Puedes cargar cualquiera de los siguientes tipos de datos como un único archivo CSV. Para cargar más de un tipo de datos, carga múltiples archivos CSV.

- **Atributos de usuario:** Incluye tanto atributos de usuario predeterminados como personalizados. Los atributos de usuario predeterminados son claves reservadas en Braze (como `first_name` o `email`) y los atributos personalizados son atributos de usuario únicos de tu negocio (como `last_destination_searched`).
- **Eventos personalizados:** Son únicos de tu negocio y reflejan acciones que un usuario ha realizado, como `trip_booked` para una aplicación de reserva de viajes.

Cuando estés listo para empezar a construir tu archivo CSV, consulta la siguiente información:

{% tabs local %}
<!-- TAB -->
{% tab Atributos de usuario %}
#### Identificadores requeridos {#required-identifiers-attributes}

Aunque `external_id` no es obligatorio, tu archivo CSV debe incluir un identificador de usuario que pueda mapearse a **uno** de los siguientes identificadores. Para más detalles sobre cada uno, revisa [Elige un identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **y** `user_alias_label`
- `email`
- `phone`

#### Atributos personalizados {#custom-attributes}

Los siguientes tipos de datos se pueden usar como atributos personalizados para la importación CSV. Los encabezados de columna que no coincidan exactamente con un [atributo predeterminado](#default-attributes) se importan como atributos personalizados en Braze, a menos que se cambien durante el paso de mapeado.

| Tipo de datos | Descripción |
|---|---|
| Datetime | Debe almacenarse en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). |
| Boolean | Acepta `true` o `false`. |
| Número | Debe ser un entero o flotante sin espacios ni comas. Los flotantes deben usar un punto (`.`) como separador decimal. |
| Cadena | Puede contener comas si el valor está envuelto en comillas dobles (`""`). |
| En blanco | Los valores en blanco no sobrescribirán los valores existentes en el perfil de usuario, y no necesitas incluir todos los atributos de usuario existentes en tu archivo CSV. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados" }

{% alert important %}
Los tipos de datos de arrays, tokens de notificaciones push y eventos personalizados no son compatibles con la importación de usuarios, ya que las comas en tu archivo CSV se interpretarán como un separador de columna y causarán errores al analizar tu archivo.<br><br>Para cargar este tipo de valores, usa el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) o [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) en su lugar.
{% endalert %}

#### Atributos predeterminados {#default-attributes}

{% alert important %}
Al importar atributos predeterminados, los encabezados de columna que uses deben coincidir exactamente con la ortografía y las mayúsculas de los atributos de usuario predeterminados. De lo contrario, Braze los detectará como [atributos personalizados](#custom-attributes).
{% endalert %}

{% alert tip %}
Para la lista completa de atributos estándar que Braze reconoce (a través de SDK, API, CSV y Cloud Data Ingestion), consulta [Atributos estándar]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes). La siguiente tabla cubre solo el subconjunto que se puede establecer mediante la importación CSV.
{% endalert %}

Los siguientes atributos predeterminados están disponibles para la importación de usuarios.

| Campo del perfil de usuario | Tipo de datos | Descripción | ¿Obligatorio? |
| :---- | :---- | :---- | :---- |
| `external_id` | Cadena | Un identificador único de usuario para tu cliente. | Condicional. Consulta [Identificadores requeridos](#required-identifiers-attributes). |
| `user_alias_name` | Cadena | Un identificador único de usuario para usuarios anónimos que es una alternativa al `external_id`. Debe usarse con `user_alias_label`. | Condicional. Consulta [Identificadores requeridos](#required-identifiers-attributes). |
| `user_alias_label` | Cadena | Una etiqueta común para agrupar alias de usuario. Debe usarse con `user_alias_name`. | Condicional. Consulta [Identificadores requeridos](#required-identifiers-attributes). |
| `first_name` | Cadena | El nombre de tus usuarios según lo han indicado (por ejemplo, `Jane`). | No |
| `last_name` | Cadena | El apellido de tus usuarios según lo han indicado (por ejemplo, `Doe`). | No |
| `email` | Cadena | El correo electrónico de tus usuarios según lo han indicado (por ejemplo, `jane.doe@example.com`). | No |
| `country` | Cadena | Los códigos de país deben pasarse a Braze en el estándar ISO-3166-1 alfa-2 (por ejemplo, `GB`). | No |
| `dob` | Cadena | Debe pasarse en el formato "YYYY-MM-DD" (por ejemplo, `1980-12-21`). Esto importa la fecha de nacimiento de tu usuario y te permite dirigirte a usuarios cuyo cumpleaños sea "hoy". | No |
| `gender` | Cadena | "M", "F", "O" (otro), "N" (no aplica), "P" (prefiere no decir), o nil (desconocido). | No |
| `home_city` | Cadena | La ciudad de residencia de tus usuarios según lo han indicado (por ejemplo, `London`). | No |
| `language` | Cadena | El idioma debe pasarse a Braze en el estándar ISO-639-1 (por ejemplo, `en`). Consulta nuestra [lista de idiomas aceptados]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes). | No |
| `phone` | Cadena | Un número de teléfono indicado por tus usuarios, en formato `E.164` (por ejemplo, `+442071838750`). Consulta [Números de teléfono de usuario]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers) para orientación sobre el formato. | No |
| `email_open_tracking_disabled` | Boolean | Se acepta true o false. Establece como true para desactivar el píxel de seguimiento de apertura en todos los correos electrónicos futuros enviados a este usuario. | No |
| `email_click_tracking_disabled` | Boolean | Se acepta true o false. Establece como true para desactivar el seguimiento de clics en todos los enlaces dentro de un correo electrónico futuro enviado a este usuario. | No |
| `email_subscribe` | Cadena | Los valores disponibles son `opted_in` (registrado explícitamente para recibir mensajes de correo electrónico), `unsubscribed` (rechazó explícitamente los mensajes de correo electrónico) y `subscribed` (ni optó ni rechazó). | No |
| `push_subscribe` | Cadena | Los valores disponibles son `opted_in` (registrado explícitamente para recibir mensajes push), `unsubscribed` (rechazó explícitamente los mensajes push) y `subscribed` (ni optó ni rechazó). | No |
| `time_zone` | Cadena | La zona horaria debe pasarse a Braze en el mismo formato que la base de datos de zonas horarias de IANA (por ejemplo, `America/New_York` o `Eastern Time (US & Canada)`). | No |
| `date_of_first_session`  `date_of_last_session` | Cadena | Puede pasarse en uno de los siguientes formatos ISO 8601: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (por ejemplo, 2019-11-20T18:38:57) | No |
| `subscription_group_id` | Cadena | El `id` de tu grupo de suscripción. Este identificador se puede encontrar en la página de grupos de suscripción de tu panel. | No |
| `subscription_state` | Cadena | El estado de suscripción para el grupo de suscripción especificado por `subscription_group_id`. Los valores permitidos son `unsubscribed` (no está en el grupo de suscripción) o `subscribed` (está en el grupo de suscripción). | No, pero se recomienda encarecidamente si se usa `subscription_group_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Atributos predeterminados" }

#### Actualización del estado del grupo de suscripción (opcional) {#updating-subscription-group-status-optional}

Adicionalmente, puedes añadir usuarios a grupos de suscripción de correo electrónico o SMS a través de la importación de usuarios. Esto es particularmente útil para SMS, ya que un usuario debe estar inscrito en un grupo de suscripción SMS para recibir mensajes del canal SMS. Para más información, consulta [Grupos de suscripción SMS]({{site.baseurl}}/sms_rcs_subscription_groups#subscription-group-mms-enablement).

Si estás actualizando estados de grupos de suscripción, debes tener las siguientes dos columnas en tu CSV:

- `subscription_group_id`: El `id` del [grupo de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).
- `subscription_state`: Los valores disponibles son `unsubscribed` (no está en el grupo de suscripción) o `subscribed` (está en el grupo de suscripción).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Actualización del estado del grupo de suscripción (opcional)" }

{% alert note %}
Solo se puede establecer un único `subscription_group_id` por fila en la importación de usuarios. Diferentes filas pueden tener diferentes valores de `subscription_group_id`. Sin embargo, si necesitas inscribir a los mismos usuarios en múltiples grupos de suscripción, tendrás que realizar múltiples importaciones.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab Eventos personalizados %}
#### Identificadores requeridos {#required-identifiers-custom-events}

Aunque `external_id` no es obligatorio, tu archivo CSV debe incluir un identificador de usuario que se mapee a **uno** de los siguientes identificadores. Para más detalles sobre cada uno, revisa [Elige un identificador](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **y** `user_alias_label`
- `email`
- `phone`

#### Campos de eventos personalizados {#custom-event-fields}

Además de los campos estándar listados en la siguiente tabla, tu CSV también puede contener encabezados de columna adicionales para propiedades de evento. Estas propiedades deben tener un encabezado de columna de `<event_name>.properties.<property name>` o `<property name>`.

Por ejemplo, el evento personalizado `trip_booked` puede tener las propiedades `destination` y `duration`. Puedes importarlas usando los encabezados de columna `trip_booked.properties.destination` y `trip_booked.properties.duration`. También puedes representar las propiedades en los encabezados como `<property name>`. Braze detecta las propiedades relevantes para cada evento en función de si hay un valor en la celda CSV correspondiente.

| Campo del perfil de usuario | Tipo de datos | Información | ¿Obligatorio? |
| :---- | :---- | :---- | :---- |
| `external_id` | Cadena | Un identificador único de usuario para tu usuario. | Condicional. Consulta [Identificadores requeridos](#required-identifiers-custom-events). |
| `braze_id` | Cadena | Un identificador asignado por Braze para tu usuario. | Condicional. Consulta [Identificadores requeridos](#required-identifiers-custom-events). |
| `user_alias_name` | Cadena | Un identificador único de usuario para usuarios anónimos, que es una alternativa al `external_id`. Debe usarse con `user_alias_label`. | Condicional. Consulta [Identificadores requeridos](#required-identifiers-custom-events). |
| `user_alias_label` | Cadena | Una etiqueta común para agrupar alias de usuario. Debe usarse con `user_alias_name`. | Condicional. Consulta [Identificadores requeridos](#required-identifiers-custom-events). |
| `email` | Cadena | El correo electrónico de tus usuarios según lo han indicado (por ejemplo, `jane.doe@example.com`). | No, y solo se puede usar en ausencia de otros identificadores. Consulta la siguiente nota. |
| `phone` | Cadena | Un número de teléfono indicado por tus usuarios, en formato `E.164` (por ejemplo, `+442071838750`). Consulta [Números de teléfono de usuario]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers) para orientación sobre el formato. | No, y solo se puede usar en ausencia de otros identificadores. Consulta la siguiente nota. |
| `name` | Cadena | Un evento personalizado de tus usuarios. | Sí |
| `time` | Cadena | La hora del evento. Puede pasarse en uno de los siguientes formatos ISO-8601: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (por ejemplo, 2019-11-20T18:38:57) | Sí |
| `<event name>.properties.<property name>` | Múltiple | Una propiedad de evento asociada con un evento personalizado. Un ejemplo es `trip_booked.properties.destination` | No |
| `<property name>` | Múltiple | Una propiedad de evento que puedes usar en múltiples tipos de eventos. Un ejemplo es `destination`. Esta propiedad se asocia con un evento cuando hay un valor no nulo en la celda CSV correspondiente. | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campos de eventos personalizados" }

#### Requisitos de formato para eventos personalizados {#format-requirements-for-custom-events}

Al importar eventos personalizados usando CSV, debes formatear tu archivo según los siguientes requisitos para una importación de datos exitosa.

##### Comprensión del formato de eventos personalizados {#understanding-custom-event-formatting}

Formatea correctamente tu CSV de eventos personalizados usando notación de punto, o con un valor no nulo en la celda correspondiente, para que Braze mapee cada propiedad al evento final. Si el formato es incorrecto, las propiedades pueden descartarse o la importación puede fallar, especialmente cuando se incluyen múltiples tipos de eventos en un solo archivo.

##### Usa notación de punto para propiedades de eventos {#use-dot-notation-for-event-properties}

Usa notación de punto para definir la relación jerárquica entre un evento personalizado y sus propiedades. Esta convención de formato te permite importar datos de eventos estructurados que incluyen atributos específicos para cada evento.

El formato de notación de punto sigue esta estructura: `event_name.properties.property_name`

La notación de punto funciona en la siguiente secuencia:

1. El nombre del evento va primero
2. Seguido de `.properties.` para indicar que lo que sigue es una propiedad del evento
3. Finalmente, el nombre específico de la propiedad

**Ejemplo:**

Para un evento personalizado llamado `rented_movie` con las propiedades `movie_name` y `genre`, tus encabezados de columna CSV serían:

- `rented_movie.properties.movie_name`
- `rented_movie.properties.genre`

Esta notación le indica a Braze que cree un evento personalizado llamado `rented_movie` y adjunte las propiedades `movie_name` y `genre` a esa instancia específica del evento.

Si usas una combinación de notación de punto y notación sin punto para importar propiedades, tu carga CSV puede fallar porque Braze detecta encabezados duplicados. Esto ocurre cuando tienes los encabezados `rented_movie.properties.movie_name` y `movie_name` dentro del mismo archivo. Para evitar esto, usa solo un formato de propiedades para tus encabezados.

##### Un evento por fila {#one-event-per-row}

Cada fila en tu CSV representa un único evento personalizado para un único usuario. Si un usuario tiene múltiples eventos, debes incluir una fila separada para cada evento, incluso si comparten el mismo identificador de usuario.

{% alert important %}
Cuando una fila contiene datos para un evento específico, solo completa las columnas de las propiedades de ese evento. Deja en blanco las columnas de otros eventos.
{% endalert %}

##### Ejemplo de estructura CSV {#example-csv-structure}

La siguiente tabla muestra el formato correcto para importar eventos personalizados con propiedades. Este ejemplo muestra dos usuarios que realizaron diferentes eventos: uno alquiló una película y otro compró una película.

| external_id | name | time | rented_movie.properties.movie_name | rented_movie.properties.genre | bought_movie.properties.movie_name | bought_movie.properties.genre |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 123 | rented_movie | 2024-06-10T12:00:00Z | Ghostbusters | Action | | |
| 456 | bought_movie | 2024-06-12T12:00:00Z | | | Ghostbusters | Action |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Ejemplo de estructura CSV" }

En este ejemplo:

- El usuario `123` desencadenó el evento `rented_movie` con las propiedades `movie_name` (Ghostbusters) y `genre` (Action)
- El usuario `456` desencadenó el evento `bought_movie` con las propiedades `movie_name` (Ghostbusters) y `genre` (Action)
- Cada evento solo completa sus columnas de propiedades relevantes, dejando en blanco las columnas de propiedades de otros eventos

{% endtab %}
{% endtabs %}

### Paso 4: Carga tu archivo {#step-4-upload-your-file}

Para cargar tu archivo, selecciona **Atributos** o **Eventos**, haz clic en **Examinar archivos** y carga tu CSV. Braze muestra una vista previa de las primeras filas y un resumen de los campos detectados.

Para archivos grandes (hasta 500 MB para atributos predeterminados y atributos personalizados, o 50 MB para eventos personalizados), el panel puede parecer temporalmente sin respuesta mientras el archivo se carga y Braze calcula la importación. Estas cargas y cálculos pueden tardar más en completarse que con archivos más pequeños. Deja que este paso se complete. Para más contexto sobre límites de archivos y tiempos, consulta [Construcción de tu CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#constructing-your-csv).

Antes de cargar tu archivo CSV, renómbralo con el nombre de importación que quieres ver en Braze. No puedes editar el nombre de importación después de la carga.

{% alert note %}
La vista previa del archivo solo muestra las primeras filas de tu archivo. Para verificar cada fila antes de importar, usa la [validación de archivo](#file-validation).
{% endalert %}

{% alert important %}
Las importaciones de usuarios CSV están disponibles para descarga desde el panel durante 14 días después de la carga. Después de este período, el archivo se elimina del almacenamiento y ya no es accesible.
{% endalert %}

### Paso 5: Mapea tus campos {#csv-data-mapping}

Después de la vista previa, puedes mapear los encabezados de tu CSV a atributos, eventos o propiedades de eventos de Braze. Braze mapea automáticamente los campos de tu archivo CSV a atributos, eventos o propiedades de eventos con nombres idénticos, y crea nuevos campos cuando es necesario. También tendrás la flexibilidad de ajustar manualmente las sugerencias o seleccionar diferentes atributos, eventos o propiedades.

Para las propiedades de eventos, Braze detecta las propiedades y las asocia con los eventos relevantes en función de si una celda CSV contiene un valor no nulo, o a partir de encabezados que usan notación de punto en el formato `<event name>.properties.<property name>`.

![La página de mapeado de columnas.]({% image_buster /assets/img/csv_import/column_mapping_mapped.png %})

#### Estados de mapeado {#mapping-statuses}

La columna de estado de mapeado indica la acción que ocurre cuando se importa tu archivo CSV y puede ser cualquiera de los siguientes.

| Estado de mapeado | Qué significa |
|:---|:---|
| **Mapeado** | Campo mapeado a un atributo, evento o identificador existente. |
| **Nuevo atributo**, **Nuevo evento** o **Nueva propiedad de evento** | Braze crea un nuevo atributo o evento en la importación. Puedes editarlo seleccionando el botón **Editar nuevo atributo**, **Editar nuevo evento** o **Editar nueva propiedad**. |
| **Discrepancia de tipo de datos** | El tipo de datos detectado de la columna CSV no coincide con el tipo de datos del atributo, evento o identificador existente. Braze intenta convertir el tipo de datos en la importación para que coincida con el atributo existente. Braze descarta el valor si esto no es posible. |
| **Atributo en lista de bloqueo** o **Evento en lista de bloqueo** | El campo CSV coincide con el nombre de un atributo o evento en la lista de bloqueo. Selecciona un atributo o evento diferente para mapear, o no se importará. |
| **Atributo duplicado** | Hay uno o más campos con el mismo nombre en tu archivo CSV. Mapea las columnas con el mismo nombre a diferentes atributos o solo se importará la primera columna. |
| **Clave de evento reservada** | El nombre de tu propiedad de evento coincide con una clave de evento reservada en Braze, como `time` o `event_name`. Ingresa un nombre diferente o selecciona una propiedad diferente para mapear, o se descartará. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de mapeado" }


#### Edición de nuevos atributos, eventos y propiedades {#editing-new-attributes-events-and-properties}

Cuando un atributo, evento o propiedad de evento coincidente no existe en tu espacio de trabajo, Braze intenta crear un nuevo atributo, evento o propiedad en la importación usando el nombre del campo CSV y el tipo de datos detectado. Puedes editar este nuevo campo antes de la importación seleccionando el botón **Editar nuevo atributo**, **Editar nuevo evento** o **Editar nueva propiedad** junto al estado de mapeado.

![El botón de editar nuevo atributo en la página de mapeado de columnas.]({% image_buster /assets/img/csv_import/column_mapping_edit_attribute_button.png %})


{% alert note %}
No puedes avanzar más allá del paso de mapeado hasta que se mapee un identificador. Braze mapea automáticamente un identificador cuando es posible. Para eventos personalizados, también debes mapear las columnas `name` y `time`. Consulta la sección **Campos requeridos** para más información.
{% endalert %}

### Paso 6: Elige las preferencias de segmentación {#targeting-preferences}

Después del mapeado, puedes elegir entre las siguientes preferencias de segmentación en la página de configuración de importación. Si no necesitas crear un nuevo filtro de segmentación o Segment a partir de tu importación, selecciona **No hacer que esta lista esté disponible como filtro de segmentación**.

| Opción | Descripción |
|---|---|
| Filtro de segmentación | Para convertir tu archivo CSV en una opción de reorientación al construir Segments de usuario, elige tu archivo del menú desplegable **Actualizado/Importado desde CSV** y luego selecciona **Crear filtro de segmentación**. |
| Nuevos Segments | Para también crear un nuevo Segment a partir de tu nuevo filtro de segmentación, selecciona **Crear filtro de segmentación y añadir a nuevo Segment**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 6: Elige las preferencias de segmentación" }

![Un grupo de filtros con el filtro "Actualizado/Importado desde CSV" que incluye un archivo CSV titulado "Halloween season fun".]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Paso 7: Valida tu archivo (opcional) {#file-validation}

Antes de iniciar tu importación, puedes ejecutar la validación de archivo para verificar cada fila en busca de errores y advertencias. Para validar tu archivo, selecciona **Validar archivo antes de importar** en la página de configuración de importación y luego selecciona **Siguiente**.

La validación puede tardar hasta 2 minutos para archivos del tamaño máximo permitido. Mientras se ejecuta la validación, puedes seleccionar **Omitir validación** para saltarla y proceder inmediatamente.

#### Resultados de la validación {#validation-results}

Cuando se completa la validación, aparece uno de los siguientes resultados.

| Resultado | Qué significa | Paso siguiente |
|---|---|---|
| **Validación completa** | No se encontraron problemas. | Selecciona **Importar datos**. |
| **Problemas encontrados** | Algunas filas tienen errores o advertencias. | Descarga el informe de errores para revisarlos y luego selecciona **Importar de todos modos** para proceder o **Cancelar** para corregir tu archivo primero. |
| **Tiempo de validación agotado** | La validación se quedó sin tiempo. Las filas que se verificaron no tenían problemas. | Selecciona **Importar datos**. Un informe completo estará disponible en unos minutos. |
| **Tiempo de validación agotado con problemas** | La validación se quedó sin tiempo y encontró errores en algunas de las filas que verificó. | Descarga el informe parcial para revisar lo que se encontró y luego selecciona **Importar de todos modos** o **Cancelar**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Resultados de la validación" }

![La página de resumen mostrando la sección de problemas encontrados, con un conteo de filas con errores y advertencias, con opciones para volver atrás, descargar el informe de errores o iniciar la importación.]({% image_buster /assets/img/csv_import/summary_page_validation_results.png %})

#### Comprensión del informe de errores {#understanding-the-error-report}

El informe de errores es un archivo CSV que contiene cada fila marcada junto con sus datos originales y una descripción del problema.

| Tipo de problema | Descripción |
|---|---|
| **Error** | La fila se omitirá completamente durante la importación. |
| **Advertencia** | La fila se importará, pero algunos valores se descartarán. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprensión del informe de errores" }

Después de revisar el informe, puedes corregir los problemas en tu archivo original y volver a cargarlo, o proceder con la importación y aceptar los resultados parciales.



### Paso 8: Inicia tu importación CSV {#step-8-start-your-csv-import}

Cuando estés listo, selecciona **Iniciar importación**. Puedes seguir el progreso actual en la página **Importar usuarios**, que se actualiza automáticamente cada 5 segundos.
El procesamiento puede tardar de unos minutos a unas horas dependiendo del tamaño de tu CSV. Durante este tiempo, el panel puede parecer sin respuesta o responder lentamente, pero la importación sigue ejecutándose.

{% alert note %}
Puedes importar más de un CSV al mismo tiempo. Las importaciones CSV se ejecutan concurrentemente, por lo que el orden de las actualizaciones no se garantiza que sea serial. Si necesitas que las importaciones CSV se ejecuten una tras otra, espera a que una importación CSV finalice antes de cargar una segunda.
{% endalert %}

#### Estados de importación {#import-statuses}

Después de iniciar tu importación, puedes verificar su estado en la página **Importar usuarios**.

| Estado | Descripción |
|---|---|
| **Completa** | Todas las filas se importaron correctamente. |
| **Éxito parcial** | Algunas filas fallaron. Selecciona el menú de tres puntos junto a la importación para descargar un informe de errores o el CSV cargado original. |
| **En progreso** | La importación se está ejecutando actualmente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de importación" }

![La página Importar usuarios mostrando un estado de éxito parcial con el menú contextual abierto, mostrando las opciones Descargar informe de errores y Descargar CSV cargado.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

El informe de errores posterior a la importación incluye filas que fallaron por razones que la validación no cubre, como cuando un usuario no existe en Braze.

{% alert important %}
Los archivos CSV cargados previamente están disponibles para descarga desde la página **Importar usuarios** durante 14 días después de la fecha de carga. Después de 14 días, el archivo se elimina permanentemente y ya no se puede acceder a él.
{% endalert %}

## Consideraciones sobre puntos de datos {#data-point-considerations}

Cada dato de cliente importado desde un archivo CSV sobrescribe el valor existente en los perfiles de usuario y registra un punto de datos, excepto los ID externos y los valores en blanco. Si tienes alguna pregunta sobre los matices de los puntos de datos de Braze, tu director de cuentas de Braze puede responderlas.

| Consideración | Detalles |
|---|---|
| ID externos | Cargar un archivo CSV con solo `external_id` no registra puntos de datos. Esto te permite segmentar a los usuarios existentes de Braze sin afectar los límites de datos. Sin embargo, incluir campos como `email` o `phone` sobrescribe los datos de usuario existentes y **sí** registra puntos de datos. <br><br>Las importaciones de CSV usadas solo para segmentación no registran puntos de datos, como aquellas que contienen solo `external_id`, `braze_id` o `user_alias_name`. |
| Valores en blanco | Los valores en blanco en tu archivo CSV no sobrescribirán los datos existentes del perfil de usuario. No necesitas incluir todos los atributos de usuario o eventos personalizados al importar. |
| Estados de suscripción | Actualizar `email_subscribe`, `push_subscribe`, `subscription_group_id` o `subscription_state` **no** cuenta para el uso de punto de datos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consideraciones sobre puntos de datos" }

{% alert important %}
Establecer `language` o `country` en un usuario a través de importación de CSV o API impide que Braze capture automáticamente esta información a través del SDK.
{% endalert %}

## Solución de problemas {#troubleshooting}

Si usaste la [validación de archivos](#file-validation), comienza con el informe de errores, ya que incluye el problema específico para cada fila marcada y una descripción de cómo solucionarlo. Para las filas que fallaron durante la importación en lugar de la validación, descarga el informe de errores pasando el cursor sobre la fila y seleccionando el botón <i class="fas fa-download" title="Descargar"></i> en la página **Importar usuarios**.

Para solucionar problemas de importación de CSV, revisa estos problemas comunes en las siguientes secciones.

### Importación de CSV atascada en Calculando {#csv-import-stuck-on-calculating}

En **Importar usuarios**, `Calculating` significa que Braze aún está preparando el archivo para su procesamiento. Durante este paso, el conteo de filas puede mostrarse como `0 / Calculating` hasta que la preparación termine.

Si tu importación parece atascada en Calculando:

- Deja que la importación continúe. No canceles ni vuelvas a cargar a menos que soporte de Braze te lo indique.
- Confirma que tu archivo está dentro de los límites admitidos en [Construir tu CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#import-options).
- Revisa el [Paso 4: Cargar tu archivo](#step-4-upload-your-file) y el [Paso 8: Iniciar tu importación de CSV](#step-8-start-your-csv-import) para conocer el comportamiento esperado del panel y los tiempos de procesamiento.
- Contacta a soporte de Braze si `Calculating` dura mucho más de lo esperado para el tamaño de tu archivo después de haber confirmado esas verificaciones.

### Usar correo electrónico como `external_id` {#use-email-as-external_id}

Braze no recomienda usar una dirección de correo electrónico como `external_id`. Si usas correo electrónico como `external_id`, incluye tanto las columnas `external_id` como `email` en tu CSV para que los usuarios sigan siendo segmentables en el canal de correo electrónico. Usa una coma (`,`) como delimitador de columna, no dos puntos (`:`).

### Caracteres de comillas en valores de `external_id` {#quote-characters-in-external_id-values}

Si una celda de `external_id` contiene una comilla doble, escápala duplicando el carácter (`""`), como se describe en [Comillas dobles sin escapar o desbalanceadas](#missing-row). La importación de CSV no usa escape con barra invertida.

### La importación de CSV no está disponible como filtro de Segment {#csv-import-isnt-available-as-a-segment-filter}

Solo puedes usar una importación de CSV como filtro de Segment si habilitaste una preferencia de segmentación durante la carga.

Para verificar si la disponibilidad de segmentación está habilitada para una importación existente:

1. En la página **Importar usuarios**, busca tu importación de CSV.
2. Verifica si aparece **Ir a Segment** para esa importación.
3. Si aparece **Ir a Segment**, tu CSV está disponible en el filtro de Segment `Updated/Imported from CSV`.
4. Si **Ir a Segment** no aparece, la disponibilidad de segmentación no se habilitó para esa importación.

No puedes habilitar la disponibilidad de segmentación después de que se complete una carga de CSV. Para usar ese CSV como filtro de Segment, vuelve a cargar el archivo y, en el [Paso 6: Elegir preferencias de segmentación](#step-6-choose-targeting-preferences), selecciona **Crear filtro de segmentación** o **Crear filtro de segmentación y añadir a nuevo Segment**.

Si tu objetivo es crear un Segment sin actualizar los datos del perfil, carga un CSV que incluya solo columnas de identificador (por ejemplo, `external_id` o columnas de identificador de alias), luego selecciona **Crear filtro de segmentación y añadir a nuevo Segment**.

### Problemas de formato del archivo {#file-formatting-issues}

#### Fila malformada {#malformed-row}

Si tu carga se completó con errores, puede haber una fila malformada en tu archivo CSV.

Para importar datos correctamente, debe haber una fila de encabezado. Cada fila debe tener el mismo número de celdas que la fila de encabezado. Las filas con más o menos valores que la fila de encabezado serán excluidas de la importación. Las comas dentro de un valor se interpretarán como separadores y pueden provocar este error.

Además, todos los datos deben estar codificados en UTF-8. Si el archivo se guarda con una codificación heredada (por ejemplo, algunos valores predeterminados de Excel), los caracteres especiales y las URL en las celdas pueden corromperse y aparecer como signos de interrogación (`?`) en Braze o en los mensajes enviados.

Si tu archivo CSV tiene filas en blanco e importa menos filas que el total de líneas en el archivo CSV, esto puede no indicar un problema con la importación, ya que las filas en blanco no necesitarían importarse. Verifica el número de líneas que se importaron correctamente y asegúrate de que coincida con el número de usuarios que intentas importar.

#### Fila faltante {#missing-row}

Hay algunas razones por las que el número de usuarios importados podría no coincidir con el total de filas en tu archivo CSV:

| Problema | Resolución |
|---|---|
| ID externos, alias de usuario, ID de Braze, direcciones de correo electrónico o números de teléfono duplicados | Si hay columnas de ID externo duplicadas, esto puede causar filas malformadas o no importadas incluso si las filas están formateadas correctamente. En algunos casos, esto puede no reportar un error específico. Verifica si hay duplicados y elimínalos antes de volver a cargar. |
| Caracteres acentuados | Tu CSV puede incluir nombres o atributos con acentos. Asegúrate de que el archivo esté codificado en UTF-8 para evitar problemas de importación. |
| El ID de Braze pertenece a un usuario huérfano | Si un usuario fue fusionado con otro y Braze no puede asociar el ID de Braze con el perfil restante, la fila no se importará. |
| Fila vacía | Las filas en blanco en el CSV pueden causar errores de datos malformados. Verifica usando un editor de texto plano, no Excel ni Sheets. |
| Comillas dobles sin escapar o desbalanceadas (`"`) | Las comillas dobles envuelven valores de cadena que contienen comas. Si un valor en sí contiene una comilla doble, escápala duplicándola (`""`). Las comillas dobles sin escapar o desbalanceadas causan una fila malformada. |
| Saltos de línea inconsistentes | Los saltos de línea mixtos (por ejemplo, `\n` y `\r\n`) pueden hacer que la primera fila de datos se trate como parte del encabezado. Usa un editor hexadecimal o de texto avanzado para inspeccionar y corregir. |
| Archivo codificado incorrectamente | Aunque se permitan acentos, el archivo debe estar codificado en UTF-8. Otras codificaciones pueden funcionar parcialmente pero no son totalmente compatibles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fila faltante" }

#### Comillas en cadenas {#string-quotation}

Los valores encapsulados en comillas simples (`''`) o dobles (`""`) se leerán como cadenas durante la importación.

#### Fechas con formato incorrecto {#incorrectly-formatted-dates}

Las fechas que no estén en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) no se leerán como `datetimes` durante la importación.

### Problemas de estructura de datos {#data-structure-issues}

#### Direcciones de correo electrónico no válidas {#invalid-email-addresses}

Si tu carga se completó con errores, puede haber una o más direcciones de correo electrónico cifradas no válidas. Confirma que todas las direcciones de correo electrónico estén cifradas correctamente antes de importarlas a Braze.

- **Al [actualizar o importar direcciones de correo electrónico]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption#step-3-import-and-update-users)** en Braze, usa el valor hash del correo electrónico donde se incluya un correo electrónico. Estos valores hash de correo electrónico son proporcionados por tu equipo interno.
- **Al crear un nuevo usuario**, debes añadir `email_encrypted` con el valor cifrado del correo electrónico del usuario. De lo contrario, Braze no creará al usuario. De manera similar, si estás añadiendo una dirección de correo electrónico a un usuario existente que no tiene correo electrónico, debes añadir `email_encrypted`. De lo contrario, Braze no actualizará al usuario.

#### Datos importados como atributo personalizado {#data-imported-as-custom-attribute}

Si un dato de usuario predeterminado (como `email` o `first_name`) se importa como atributo personalizado, verifica las mayúsculas y los espacios de tu archivo CSV. Por ejemplo, `First_name` se importa como atributo personalizado, mientras que `first_name` se importa correctamente en el campo "nombre" del perfil de un usuario.

#### Cambiar el tipo de datos de un atributo personalizado {#change-a-custom-attributes-data-type}

Si necesitas cambiar el tipo de datos de un atributo personalizado existente (por ejemplo, de cadena a booleano), actualiza el tipo de datos en la página [**Atributos personalizados**]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data) del panel antes de importar tu CSV. Si el tipo de datos en tu CSV no coincide con el tipo de datos definido actualmente para el atributo, la importación fallará con un error.

#### Múltiples tipos de datos {#multiple-data-types}

Braze espera que cada valor en una columna sea del mismo tipo de datos. Los valores que no coincidan con el tipo de datos de su atributo causarán errores en la segmentación.

Además, comenzar un atributo numérico con cero causará problemas porque los números que empiezan con ceros se consideran cadenas. Cuando Braze convierte esa cadena, puede tratarla como un valor octal (que usa dígitos del cero al siete), lo que significa que se convierte a su valor decimal correspondiente. Por ejemplo, si el valor en el archivo CSV es 0130, el perfil de Braze muestra 88. Para evitar este problema, usa atributos con tipos de datos de cadena. Sin embargo, este tipo de datos no está disponible en la comparación numérica de segmentación.

#### Tipos de atributos predeterminados {#default-attribute-types}

Algunos atributos predeterminados solo pueden aceptar ciertos valores como válidos para actualizaciones de usuario. Para orientación, consulta [Construir tu CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).

Los espacios finales y las diferencias en las mayúsculas pueden causar que un valor se interprete como no válido. Por ejemplo, en el siguiente archivo CSV, solo el usuario en la primera fila (`brazetest1`) tiene sus estados de correo electrónico y push actualizados correctamente porque los valores aceptados son `unsubscribed`, `subscribed` y `opted_in`.

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@example.com,unsubscribed,unsubscribed
brazetest2,test2@example.com,Unsubscribed,Unsubscribed
```

### "Select CSV File" no funciona {#select-csv-file-is-not-working}

Hay varias razones por las que el botón **Select CSV File** puede no funcionar:

| Problema | Resolución |
|---|---|
| Bloqueador de ventanas emergentes | Esto puede evitar que la página se muestre. Confirma que tu navegador permite ventanas emergentes en el sitio web del panel de Braze. |
| Navegador desactualizado | Asegúrate de que tu navegador esté actualizado; si no, actualízalo a la última versión. |
| Procesos en segundo plano | Cierra todas las instancias del navegador y luego reinicia tu computadora. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="\"Select CSV File\" no funciona" }