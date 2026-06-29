---
nav_title: Atributos estándar
article_title: Atributos estándar
page_order: 0.5
page_type: reference
description: "Este artículo de referencia enumera los atributos estándar de usuario de Braze (claves reservadas) y los requisitos de sintaxis de cada uno."
---

# Atributos estándar {#standard-attributes}

> Los atributos estándar son campos predefinidos que Braze reconoce en cada perfil de usuario. Utiliza esta página como referencia rápida para el nombre del campo, el tipo de datos y el formato esperado de cada atributo estándar.

Los atributos estándar (a veces llamados *atributos predeterminados* o *claves reservadas*) son diferentes de los [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), que son exclusivos de tu empresa. Cuando envías datos a Braze con uno de los nombres de campo que aparecen en esta página, Braze los almacena en el campo de perfil predefinido en lugar de crear un nuevo atributo personalizado.

Puedes establecer atributos estándar a través de cualquiera de estos métodos:

- El [SDK de Braze]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)
- El [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) en el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- [Importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)
- [Ingesta de datos de Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)

{% alert important %}
Los nombres de los atributos estándar distinguen entre mayúsculas y minúsculas. Utiliza siempre minúsculas (por ejemplo, `first_name`, no `First_Name`). Si la ortografía o las mayúsculas no coinciden exactamente, Braze almacena el valor como un [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).
{% endalert %}

## Identificadores {#identifiers}

Los identificadores indican a Braze qué perfil de usuario actualizar o crear. Cada solicitud de API y cada fila de CSV debe incluir al menos un identificador. Para más detalles sobre cómo elegir el adecuado, consulta [Resolución de identificadores]({{site.baseurl}}/api/objects_filters/user_attributes_object/#identifier-resolution).

| Campo | Tipo de datos | Formato y notas |
|---|---|---|
| `external_id` | Cadena | Un identificador de usuario único que tú asignas. Una vez establecido en un perfil, Braze lo utiliza para reconocer al usuario en todos los dispositivos. No se puede eliminar una vez añadido. |
| `braze_id` | Cadena | Un identificador asignado por Braze que se crea cuando el SDK detecta un dispositivo por primera vez. Solo lectura. No se puede editar. |
| `user_alias` | Objeto | Un objeto con `alias_name` (cadena) y `alias_label` (cadena), utilizado para identificar usuarios sin un `external_id`. Mutuamente excluyente con `external_id` en la misma solicitud. |
| `email` | Cadena | Se puede utilizar como identificador cuando `external_id` y `user_alias` están ausentes. Tiene prioridad sobre `phone` si se envían ambos. |
| `phone` | Cadena | Se puede utilizar como identificador cuando `external_id`, `user_alias` y `email` están ausentes. Usa el formato [E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/#recommended-format) (por ejemplo, `+14155552671`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Campos de perfil {#profile-fields}

Estos campos capturan datos demográficos, de contacto y de configuración regional sobre tus usuarios.

| Campo | Tipo de datos | Formato y notas |
|---|---|---|
| `first_name` | Cadena | El nombre del usuario (por ejemplo, `Jane`). |
| `last_name` | Cadena | El apellido del usuario (por ejemplo, `Doe`). |
| `email` | Cadena | La dirección de correo electrónico del usuario (por ejemplo, `jane.doe@braze.com`). |
| `phone` | Cadena | El número de teléfono del usuario. Usa el formato [E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/#recommended-format) (por ejemplo, `+14155552671`). |
| `dob` | Cadena | Fecha de nacimiento en formato `YYYY-MM-DD` (por ejemplo, `1988-02-14`). Permite la segmentación por cumpleaños. |
| `gender` | Cadena | Uno de `M`, `F`, `O` (otro), `N` (no aplica), `P` (prefiere no decir) o `null` (desconocido). |
| `country` | Cadena | Un código de país en formato [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1) (por ejemplo, `US`, `GB`). Establecer `country` a través de importación CSV o API impide que el SDK lo capture automáticamente. |
| `home_city` | Cadena | La ciudad de residencia del usuario (por ejemplo, `London`). |
| `language` | Cadena | Un código de idioma en formato [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (por ejemplo, `en`). Consulta la [lista de idiomas aceptados]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes/). Establecer `language` a través de importación CSV o API impide que el SDK lo capture automáticamente. |
| `time_zone` | Cadena | Un nombre de zona horaria de la [base de datos de zonas horarias de IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por ejemplo, `America/New_York` o `Eastern Time (US & Canada)`). |
| `current_location` | Objeto | Un objeto que contiene `longitude` y `latitude` (por ejemplo, `{"longitude": -73.991443, "latitude": 40.753824}`). |
| `image_url` | Cadena | Una URL de la imagen de perfil del usuario. Hasta 1024 caracteres. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Suscripción y consentimiento {#subscription-and-consent}

Estos campos gestionan cómo un usuario recibe mensajes a través de los canales. Actualizarlos no cuenta para tu uso de puntos de datos.

| Campo | Tipo de datos | Formato y notas |
|---|---|---|
| `email_subscribe` | Cadena | Uno de `opted_in` (registrado explícitamente para recibir correo electrónico), `unsubscribed` (canceló explícitamente la suscripción al correo electrónico) o `subscribed` (ni optó por recibir ni canceló). |
| `push_subscribe` | Cadena | Uno de `opted_in`, `unsubscribed` o `subscribed`. Mismas definiciones que `email_subscribe`. |
| `subscription_groups` | Matriz de objetos | Una matriz donde cada objeto tiene un `subscription_group_id` (cadena) y un `subscription_state` (`subscribed` o `unsubscribed`). Por ejemplo: `[{"subscription_group_id": "abc-123", "subscription_state": "subscribed"}]`. |
| `email_open_tracking_disabled` | Booleano | `true` o `false`. Establece `true` para desactivar el píxel de seguimiento de apertura de correo electrónico para este usuario. Disponible solo para SparkPost y SendGrid. |
| `email_click_tracking_disabled` | Booleano | `true` o `false`. Establece `true` para desactivar el seguimiento de clics en correo electrónico para este usuario. Disponible solo para SparkPost y SendGrid. |
| `marked_email_as_spam_at` | Cadena | Marca de tiempo en la que el correo electrónico del usuario fue marcado como correo no deseado. Usa el formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para más detalles sobre la configuración de grupos de suscripción, consulta [Grupos de suscripción]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-groups).

## Sesiones e interacción {#sessions-and-engagement}

Estos campos capturan cuándo el usuario interactuó por primera o última vez con tu aplicación. El SDK los registra automáticamente; normalmente solo los estableces a través de API o CSV cuando migras desde otra plataforma.

| Campo | Tipo de datos | Formato y notas |
|---|---|---|
| `date_of_first_session` | Cadena | La fecha en que el usuario usó la aplicación por primera vez. Usa el formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) o uno de: `yyyy-MM-ddTHH:mm:ss:SSSZ`, `yyyy-MM-ddTHH:mm:ss`, `yyyy-MM-dd HH:mm:ss`, `yyyy-MM-dd`, `MM/dd/yyyy` o `ddd MM dd HH:mm:ss.TZD YYYY`. |
| `date_of_last_session` | Cadena | La fecha en que el usuario usó la aplicación por última vez. Mismos formatos aceptados que `date_of_first_session`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Tokens de notificaciones push {#push-tokens}

Usa estos campos cuando migres tokens de notificaciones push desde otra plataforma. Después de integrar el SDK de Braze, los tokens de notificaciones push se capturan automáticamente. Para orientación sobre la migración, consulta [Migración de tokens de notificaciones push]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens).

| Campo | Tipo de datos | Formato y notas |
|---|---|---|
| `push_tokens` | Matriz de objetos | Una matriz donde cada objeto tiene un `app_id` (cadena) y un `token` (cadena). Opcionalmente incluye un `device_id` (cadena). Por ejemplo: `[{"app_id": "YOUR_APP_ID", "token": "abcd", "device_id": "optional_device_id"}]`. |
| `push_token_import` | Booleano | Indicador de nivel superior (no anidado en `attributes`). Establece `true` para importar tokens de notificaciones push heredados para usuarios anónimos sin un `external_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Perfil social {#social-profile}

Estos campos almacenan datos de integraciones con redes sociales.

| Campo | Tipo de datos | Formato y notas |
|---|---|---|
| `facebook` | Objeto | Un objeto que contiene cualquiera de `id` (cadena), `likes` (matriz de cadenas) o `num_friends` (entero). |
| `twitter` | Objeto | Un objeto que contiene cualquiera de `id` (entero), `screen_name` (cadena, nombre de usuario en X), `followers_count` (entero), `friends_count` (entero) o `statuses_count` (entero). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Ejemplo de API {#api-example}

La siguiente solicitud establece atributos estándar en dos usuarios a través del [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
    {
      "external_id": "user1",
      "first_name": "Jane",
      "last_name": "Doe",
      "email": "jane.doe@example.com",
      "country": "US",
      "language": "en",
      "time_zone": "America/New_York",
      "dob": "1988-02-14",
      "email_subscribe": "opted_in"
    },
    {
      "external_id": "user2",
      "first_name": "Alex",
      "phone": "+14155552671",
      "current_location": {
        "longitude": -73.991443,
        "latitude": 40.753824
      },
      "subscription_groups": [
        {
          "subscription_group_id": "abc-123",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```

Para el contrato completo de la API, consulta el [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/).

## Ejemplo de CSV {#csv-example}

El siguiente CSV actualiza atributos estándar para dos usuarios. Los encabezados de columna deben coincidir exactamente con los nombres de campo de este artículo. Los encabezados que no coincidan (por ejemplo, `First_name` en lugar de `first_name`) se importan como atributos personalizados.

```plaintext
external_id,first_name,last_name,email,country,language,dob,email_subscribe
user1,Jane,Doe,jane.doe@example.com,US,en,1988-02-14,opted_in
user2,Alex,Smith,alex.smith@example.com,GB,en,1992-09-30,subscribed
```

No puedes establecer algunos atributos estándar a través de la importación CSV. Debes enviar matrices, tokens de notificaciones push y objetos anidados a través de la API o la [Ingesta de datos de Cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/). Para la lista completa de campos compatibles con CSV y los pasos de importación, consulta [Atributos predeterminados]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/#default-attributes).

## Consideraciones {#considerations}

Ten en cuenta estos puntos al trabajar con atributos estándar:

- **Los nombres de campo distinguen entre mayúsculas y minúsculas.** Utiliza siempre minúsculas. Un encabezado o clave que no coincida exactamente con el nombre de un atributo estándar se trata como un atributo personalizado.
- **La captura automática del SDK se suprime cuando estableces valores a través de API o CSV.** Cuando estableces `country` o `language` a través de API o CSV, Braze deja de capturar automáticamente esos campos desde el SDK para ese usuario.
- **`null` elimina un valor.** Establece un atributo estándar como `null` para eliminarlo del perfil. Algunos campos, incluidos `external_id` y `user_alias`, no se pueden eliminar una vez establecidos.
- **Los valores en blanco del CSV no sobrescriben.** Una celda vacía en una importación CSV mantiene el valor existente en el perfil. Para borrar un valor, usa la API.
- **Las zonas horarias se establecen en UTC de forma predeterminada.** Las cadenas de fecha sin un desplazamiento se interpretan como medianoche UTC y se muestran en la zona horaria de tu espacio de trabajo. Para especificar una zona horaria, añade un desplazamiento UTC (por ejemplo, `2024-11-10T18:00:00-05:00`).

## Páginas relacionadas {#related-pages}

- [Objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) — Contrato completo de la API para el objeto de atributos.
- [Punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) — Punto de conexión REST para crear y actualizar perfiles de usuario.
- [Establecer atributos de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/) — Métodos del SDK para establecer atributos estándar y personalizados.
- [Importación CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/) — Carga atributos estándar a través de un archivo CSV.
- [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) — Define atributos exclusivos de tu empresa.
- [Tipos de datos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/) — Referencia de los tipos de datos compatibles.