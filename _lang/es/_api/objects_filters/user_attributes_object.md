---
nav_title: "Objeto de atributos del usuario"
article_title: "Objeto de atributos del usuario"
page_order: 11
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto de atributos de usuario."
---

# Objeto de atributos del usuario {#user-attributes-object}

> Una solicitud API con cualquier campo del objeto de atributos crea o actualiza un atributo con ese nombre y el valor indicado en el perfil de usuario especificado.

Utiliza los nombres de campo de perfil de usuario de Braze (enumerados a continuación o cualquiera de los enumerados en la sección de [campos de perfil de usuario de Braze](#braze-user-profile-fields)) para actualizar esos valores especiales en el perfil de usuario en el panel o añade tus propios datos de atributos personalizados al usuario.

## Cuerpo del objeto {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
  // Braze User Profile Fields
  "first_name" : "Alex",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
  // Array of objects custom attribute
  "my_array_of_objects_attribute": [{"key": "value"}, {"key": "value"}],
  // Adding to an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$add": [{"key": "value"}] },
  // Removing from an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$remove": [{"$identifier_key": "key", "$identifier_value": "value"}] },
}
```

- [ID externo de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [Alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

{% alert note %}
Para atributos personalizados de matriz normales, usa `add` y `remove` (sin `$`).

Para matrices de objetos (atributos personalizados anidados), usa `$add`, `$remove` y `$update` en las cargas útiles de solicitudes `/users/track`. Estos operadores aplican cambios a nivel de objeto haciendo coincidir identificadores (`$identifier_key` e `$identifier_value`) y admiten actualizaciones in situ con `$new_object`.

Usa este formato cuando necesites agregar, eliminar o actualizar objetos dentro de una matriz existente conservando el resto del estado de la matriz. Para ejemplos completos de solicitudes, consulta [Ejemplo de API de matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) y [Ejemplo de SDK or kit de desarrollo de software de matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example).
{% endalert %}

Para eliminar un atributo de perfil, establécelo como `null`. Algunos campos, como `external_id` y `user_alias`, no se pueden eliminar después de ser añadidos a un perfil de usuario.

### Resolución de identificadores {#identifier-resolution}

A menos que estés realizando una [importación anónima de tokens de notificaciones push](#push-token-import), cada objeto de atributos de usuario debe incluir al menos un identificador: `external_id`, `user_alias`, `braze_id`, `email` o `phone`. Cuando sea posible, incluye solo un identificador por objeto para evitar ambigüedades sobre qué perfil de usuario se está actualizando o creando.

Ten en cuenta lo siguiente al usar identificadores:

- **`external_id` y `user_alias` son mutuamente excluyentes.** Incluir ambos en el mismo objeto de atributos de usuario devuelve un error. Para añadir un alias a un usuario que ya tiene un `external_id`, usa el [endpoint `/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias).
- **`email` tiene prioridad sobre `phone`.** Si tanto `email` como `phone` se incluyen en el mismo objeto, Braze usa `email` como identificador. Esto significa que los atributos se aplican al perfil de usuario asociado con esa dirección de correo electrónico, incluso si el número de teléfono pertenece a un perfil diferente.

{% alert important %}
Para evitar comportamientos inesperados, usa un solo identificador por objeto de atributos de usuario. Proporcionar múltiples identificadores que hagan referencia a diferentes perfiles de usuario puede provocar que los atributos se apliquen al perfil incorrecto.
{% endalert %}

#### Actualizar solo perfiles existentes {#update-existing-profiles-only}

Si deseas actualizar solo los perfiles de usuario existentes en Braze, debes pasar la clave `_update_existing_only` con un valor de `true` dentro del cuerpo de tu solicitud. Si se omite este valor, Braze crea un nuevo perfil de usuario si el `external_id` aún no existe.

{% alert note %}
Si estás creando un perfil de usuario solo con alias a través del endpoint `/users/track`, debes establecer `_update_existing_only` en `false`. Si omites este valor, Braze no crea el perfil solo con alias.
{% endalert %}

#### Importación de tokens de notificaciones push {#push-token-import}

Antes de importar tokens de notificaciones push a Braze, verifica si realmente lo necesitas. Cuando los SDK or kit de desarrollo de software de Braze están implementados, gestionan los tokens de notificaciones push automáticamente sin necesidad de cargarlos a través de la API.

Si determinas que necesitas cargarlos a través de la API, se pueden cargar para usuarios identificados o usuarios anónimos. Esto significa que se necesita un `external_id` presente, o los usuarios anónimos deben tener el indicador `push_token_import` establecido en `true`.

{% alert note %}
Al importar tokens de notificaciones push desde otros sistemas, un `external_id` no siempre está disponible. Para mantener la comunicación con estos usuarios durante tu transición a Braze, puedes importar los tokens heredados para usuarios anónimos sin proporcionar `external_id` especificando `push_token_import` como `true`.
{% endalert %}

Al especificar `push_token_import` como `true`:

* `external_id` y `braze_id` **no** deben especificarse
* El objeto de atributos **debe** contener un token de notificaciones push
* Si el token ya existe en Braze, la solicitud se ignora; de lo contrario, Braze crea un perfil de usuario temporal y anónimo para cada token, lo que te permite seguir enviando mensajes a estas personas

Después de la importación, a medida que cada usuario lance la versión de tu aplicación habilitada con Braze, Braze mueve automáticamente su token de notificaciones push importado a su perfil de usuario de Braze y limpia el perfil temporal.

Braze verifica una vez al mes para encontrar cualquier perfil anónimo con el indicador `push_token_import` que no tenga un token de notificaciones push. Si el perfil anónimo ya no tiene un token de notificaciones push, Braze elimina el perfil. Sin embargo, si el perfil anónimo aún tiene un token de notificaciones push, lo que sugiere que el usuario real aún no ha iniciado sesión en el dispositivo con dicho token de notificaciones push, Braze no realiza ninguna acción.

Para más información, consulta [Migración de tokens de notificaciones push](#migrate-push-tokens).

#### Tipos de datos de atributos personalizados {#custom-attribute-data-types}

Los siguientes tipos de datos se pueden almacenar como un atributo personalizado:

| Tipo de datos | Notas |
| --- | --- |
| Matrices | Las matrices de atributos personalizados son compatibles. Cuando agregas un elemento, se añade al final de la matriz. Si el elemento ya existe, se mueve de su posición actual al final.<br><br>Solo se almacenan valores únicos. Por ejemplo, importar `['hotdog','hotdog','hotdog','pizza']` resulta en `['hotdog', 'pizza']`.<br><br>Puedes establecer una matriz directamente (por ejemplo, `"my_array_custom_attribute":[ "Value1", "Value2" ]`), agregar a una matriz existente con `"my_array_custom_attribute" : { "add" : ["Value3"] }`, o eliminar valores con `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`.<br><br>La cantidad predeterminada y máxima de elementos en una matriz es 500. Puedes actualizar la cantidad máxima de matrices en el panel de Braze, en **Configuración de datos** > **Atributos personalizados**. Para más información, consulta [Matrices]({{site.baseurl}}/developer_guide/analytics#arrays). |
| Matriz de objetos | Usa una matriz de objetos para definir una lista de objetos donde cada objeto contiene un conjunto de atributos. Usa este tipo para almacenar múltiples conjuntos de datos relacionados para un usuario, como estancias en hoteles, historial de compras o preferencias. <br><br>Por ejemplo, define un atributo personalizado llamado `hotel_stays` en un perfil de usuario como una matriz donde cada objeto representa una estancia separada, con atributos como `hotel_name`, `check_in_date` y `nights_stayed`.<br><br>Las matrices de objetos no tienen límite en la cantidad de elementos, pero sí tienen un tamaño máximo de 100&nbsp;KB. Si una actualización hace que la matriz supere este límite, Braze descarta la actualización y el atributo permanece sin cambios.<br><br>Para cargas útiles de `/users/track` y SDK or kit de desarrollo de software, usa `$add`, `$remove` y `$update` para operaciones con matrices de objetos. Usa `add` y `remove` (sin `$`) para atributos personalizados de matrices normales que contienen valores escalares. Para más detalles, consulta [Ejemplo de API de matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example), [Ejemplo de SDK or kit de desarrollo de software de matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example) y [Ejemplo de matriz de objetos](#array-of-objects-example). |
| Booleanos | `true` o `false` |
| Fechas | Almacena las fechas en formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (recomendado) o en cualquiera de estos formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Ten en cuenta que "T" es un designador de hora, no un marcador de posición, y no debe cambiarse ni eliminarse. <br><br>Los valores de fecha que no coinciden con ninguno de los formatos enumerados se almacenan como cadenas en el perfil de usuario en lugar del tipo de datos Time. Esto significa que los filtros de segmentación basados en el tiempo (como "antes de", "después de" o "en los últimos X días") no funcionan para esos atributos. Por ejemplo, `Mar 26 2026 06:12 PM +00:00` se almacena como cadena porque no coincide con un formato compatible. Para evitar esto, usa el formato ISO 8601 (como `2026-03-26T18:12:00Z`). <br><br>Los atributos de hora sin zona horaria predeterminan a medianoche UTC (y se muestran en el panel como el equivalente de la medianoche UTC en la zona horaria de la empresa). Para especificar una zona horaria, añade un desplazamiento UTC a la marca de tiempo (por ejemplo, `2024-11-10T18:00:00-05:00` para EST). Si el desplazamiento de zona horaria falta o tiene un formato incorrecto, el valor predetermina a UTC. <br><br>Las horas se muestran en el panel en la zona horaria de tu empresa. Por ejemplo, `2024-11-10T18:00:00-05:00` (6:00 PM EST) aparecería como la hora equivalente en la zona horaria configurada de tu empresa. <br><br>Los eventos con marcas de tiempo en el futuro predeterminan a la hora actual. <br><br>Para atributos personalizados regulares, si el año es menor que 0 o mayor que 3000, Braze almacena el valor como cadena en el perfil de usuario. |
| Flotantes | Los atributos personalizados de tipo flotante son números positivos o negativos con punto decimal. Por ejemplo, puedes usar flotantes para almacenar saldos de cuenta o calificaciones de usuarios para productos o servicios. |
| Enteros | Puedes incrementar atributos personalizados de tipo entero asignando un objeto con el campo "inc" y la cantidad a agregar. <br><br>Ejemplo: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Atributos personalizados anidados | Los atributos personalizados anidados definen un conjunto de atributos como propiedad de otro atributo. Cuando defines un objeto de atributo personalizado, agregas un conjunto de atributos a ese objeto. Para más información, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support). |
| Cadenas | Los atributos personalizados de tipo cadena son secuencias de caracteres utilizadas para almacenar datos de texto. Por ejemplo, puedes usar cadenas para almacenar nombres y apellidos, direcciones de correo electrónico o preferencias. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de datos de atributos personalizados" }

{% alert tip %}
Para orientación sobre cuándo usar un evento personalizado frente a un atributo personalizado, consulta [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) y [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).
{% endalert %}

##### Ejemplo de matriz de objetos {#array-of-objects-example}

Esta matriz de objetos te permite crear Segments basados en criterios específicos dentro de las estancias y personalizar tus mensajes utilizando los datos de cada estancia con plantillas Liquid.

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

Para ejemplos de matrices de objetos que usan `$add`, `$remove` y `$update`, consulta [Ejemplo de API de matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) y [Ejemplo de SDK or kit de desarrollo de software de matriz de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example).

#### Campos de perfil de usuario de Braze {#braze-user-profile-fields}

{% alert important %}
Los siguientes campos de perfil de usuario distinguen entre mayúsculas y minúsculas, así que asegúrate de hacer referencia a estos campos en minúsculas.
{% endalert %}

{% alert tip %}
Para una referencia de atributos estándar orientada al cliente, organizada por categoría e incluye orientación para SDK or kit de desarrollo de software, API, CSV e ingesta de datos en la nube, consulta [Atributos estándar]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes).
{% endalert %}

| Campo del perfil de usuario | Especificación del tipo de datos |
| ---| --- |
| alias_name | (cadena) |
| alias_label | (cadena) |
| braze_id | (cadena, opcional) Cuando el SDK or kit de desarrollo de software reconoce un perfil de usuario, se crea un perfil de usuario anónimo con un `braze_id` asociado. El `braze_id` es asignado automáticamente por Braze, no se puede editar y es específico del dispositivo. |
| country | (cadena) Requerimos que los códigos de país se pasen a Braze en el [estándar ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1). Nuestra API hace su mejor esfuerzo para mapear países recibidos en diferentes formatos. Por ejemplo, "Australia" puede mapearse a "AU". Sin embargo, si la entrada no coincide con un [estándar ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1) dado, el valor del país se establece como `NULL`. <br><br>Establecer `country` en un usuario mediante importación CSV o API impide que Braze capture automáticamente esta información a través del SDK or kit de desarrollo de software. |
| current_location | (objeto) De la forma {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (fecha en la que el usuario usó la aplicación por primera vez) Cadena en formato ISO 8601 o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (fecha en la que el usuario usó la aplicación por última vez) Cadena en formato ISO 8601 o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (fecha de nacimiento) Cadena en formato "YYYY-MM-DD", por ejemplo, 1980-12-21. |
| email | (cadena) |
| email_subscribe | (cadena) Los valores disponibles son "opted_in" (registrado explícitamente para recibir mensajes de correo electrónico), "unsubscribed" (canceló explícitamente la suscripción a los mensajes de correo electrónico) y "subscribed" (ni optó por participar ni por no hacerlo).  |
| email_open_tracking_disabled | (booleano) Se acepta `true` o `false`. Establécelo en `true` para desactivar la adición del píxel de seguimiento de apertura a todos los correos electrónicos futuros enviados a este usuario.|
| email_click_tracking_disabled | (booleano) Se acepta `true` o `false`. Establécelo en `true` para desactivar el seguimiento de clics en todos los enlaces dentro de un correo electrónico futuro enviado a este usuario.|
| external_id | (cadena) Un identificador único para un perfil de usuario. Después de asignar un `external_id`, Braze identifica el perfil de usuario a través de los dispositivos del usuario. En la primera instancia de asignación de un external_id a un perfil de usuario desconocido, Braze migra todos los datos del perfil de usuario existente al nuevo perfil de usuario. |
| Facebook | Hash que contiene cualquiera de `id` (cadena), `likes` (matriz de cadenas), `num_friends` (entero). |
| first_name | (cadena) |
| gender | (cadena) "M", "F", "O" (otro), "N" (no aplica), "P" (prefiere no decirlo) o null (desconocido). |
| home_city | (cadena) |
| language | (cadena) Requerimos que el idioma se pase a Braze en el [estándar ISO-639-1](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Para idiomas compatibles, consulta nuestra [lista de idiomas aceptados]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes).<br><br>Establecer `language` en un usuario mediante importación CSV o API impide que Braze capture automáticamente esta información a través del SDK or kit de desarrollo de software. |
| last_name | (cadena) |
| marked_email_as_spam_at | (cadena) Fecha en la que el correo electrónico del usuario fue marcado como correo no deseado. Aparece en formato ISO 8601 o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (cadena) Recomendamos proporcionar números de teléfono en formato [E.164](https://en.wikipedia.org/wiki/E.164). Para más detalles, consulta [Números de teléfono de usuario]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format).|
| push_subscribe | (cadena) Los valores disponibles son "opted_in" (registrado explícitamente para recibir mensajes push), "unsubscribed" (canceló explícitamente la suscripción a los mensajes push) y "subscribed" (ni optó por participar ni por no hacerlo).  |
| push_tokens | Matriz de objetos con cadenas `app_id` y `token`. Opcionalmente puedes proporcionar un `device_id` para el dispositivo con el que este token está asociado, por ejemplo, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Si no se proporciona un `device_id`, se genera uno aleatoriamente. |
| subscription_groups| Matriz de objetos con cadena `subscription_group_id` y `subscription_state`, por ejemplo, `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Los valores disponibles para `subscription_state` son "subscribed" y "unsubscribed".|
| time_zone | (cadena) Nombre de zona horaria de la [base de datos de zonas horarias IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por ejemplo, "America/New_York" o "Eastern Time (US & Canada)"). Solo se establecen valores de zona horaria válidos. |
| twitter | Hash que contiene cualquiera de `id` (entero), `screen_name` (cadena, nombre de usuario de X (anteriormente Twitter)), `followers_count` (entero), `friends_count` (entero), `statuses_count` (entero). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de perfil de usuario de Braze" }

Los valores de idioma que se establecen explícitamente a través de esta API tienen prioridad sobre la información de configuración regional que Braze recibe automáticamente del dispositivo.

####  Ejemplo de solicitud de atributos de usuario {#user-attribute-example-request}

Este ejemplo contiene cuatro objetos de atributos de usuario, de un total de 75 objetos de atributos permitidos por llamada a la API.

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Alex",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Lee",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Yuri",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

## Migrar tokens de notificaciones push {#migrate-push-tokens}

Si estabas enviando notificaciones push antes de integrar Braze, ya sea por tu cuenta o a través de otro proveedor, la migración de tokens de notificaciones push te permite seguir enviando notificaciones push a tus usuarios con tokens de notificaciones push registrados.

### Migración automática a través del SDK or kit de desarrollo de software {#automatic-migration-through-sdk}

Después de [integrar el SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/developer_guide/sdk_integration), los tokens de notificaciones push de tus usuarios con adhesión voluntaria se migran automáticamente la próxima vez que abran tu aplicación. Hasta entonces, no puedes enviar notificaciones push a esos usuarios a través de Braze.

Como alternativa, puedes [migrar tus tokens de notificaciones push manualmente](#manual-migration-through-api), lo que te permite volver a interactuar con tus usuarios de forma más rápida.

#### Consideraciones sobre tokens web {#web-token-considerations}

Debido a la naturaleza de los tokens de notificaciones push web, asegúrate de tener en cuenta lo siguiente al implementar push para web:

|Consideración|Detalles|
|----------------------|------------|
| **Prestadores de servicios** | De forma predeterminada, el SDK or kit de desarrollo de software web busca un prestador de servicios en `./service-worker` a menos que se especifique otra opción, como `manageServiceWorkerExternally` o `serviceWorkerLocation`. Si tu prestador de servicios no está configurado correctamente, puede provocar tokens de notificaciones push caducados para tus usuarios. |
| **Tokens caducados** | Si un usuario no ha iniciado una sesión web en 60 días, su token de notificaciones push caduca. Dado que Braze no puede migrar tokens de notificaciones push caducados, debes enviar un [aviso previo de push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) para volver a interactuar con ellos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Consideraciones sobre tokens web" }

### Migración manual a través de la API {#manual-migration-through-api}

La migración manual de tokens de notificaciones push es el proceso de importar estas claves creadas previamente en tu plataforma Braze a través de la API.

Migra programáticamente tokens de iOS (APNs) y Android (FCM) a tu plataforma utilizando el [endpoint `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Puedes migrar tanto usuarios identificados (usuarios con un ID externo asociado) como usuarios anónimos (usuarios sin un ID externo).

Especifica el `app_id` de tu aplicación durante la migración de tokens de notificaciones push para asociar el token de notificaciones push adecuado con la aplicación correspondiente. Cada aplicación (iOS, Android, etc.) tiene su propio `app_id`, que se puede encontrar en la sección **Identificación** de la página de [claves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Asegúrate de utilizar el `app_id` de la plataforma correcta.

{% alert important %}
No es posible migrar tokens de notificaciones push web a través de la API. Esto se debe a que los tokens de notificaciones push web no se ajustan al mismo esquema que otras plataformas.

<br>Si estás intentando migrar tokens de notificaciones push web de forma programática, podrías ver un error como el siguiente: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
Como alternativa a la migración por API, te recomendamos que integres el SDK or kit de desarrollo de software y permitas que tu base de tokens se repueble de forma natural.
{% endalert %}

{% tabs local %}
{% tab ID externo presente %}
Para usuarios identificados, establece la marca `push_token_import` en `false` (u omite el parámetro) y especifica los valores de `external_id`, `app_id` y `token` en el objeto de `attributes` del usuario.

Por ejemplo:

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab ID externo ausente %}
Al importar tokens de notificaciones push desde otros sistemas, no siempre se dispone de un `external_id`. En esta circunstancia, establece tu marca `push_token_import` como `true` y especifica los valores de `app_id` y `token`. Braze crea un perfil de usuario temporal y anónimo para cada token con el fin de que puedas seguir enviando mensajes a estas personas. Si el token ya existe en Braze, la solicitud se ignora.

Por ejemplo:

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
    {
      "push_token_import" : true,
      "email": "braze.test1@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },

    {
      "push_token_import" : true,
      "email": "braze.test2@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    }
  ]
}'
```

Después de la importación, cuando el usuario anónimo ejecute la versión de tu aplicación habilitada para Braze, Braze moverá automáticamente su token de notificaciones push importado a su perfil de usuario de Braze y eliminará el perfil temporal.

Braze comprueba una vez al mes si hay algún perfil anónimo con la marca `push_token_import` que no tenga un token de notificaciones push. Si el perfil anónimo ya no tiene un token de notificaciones push, Braze elimina el perfil. Sin embargo, si el perfil anónimo todavía tiene un token de notificaciones push, lo que sugiere que el usuario real aún no ha iniciado sesión en el dispositivo con dicho token de notificaciones push, Braze no realiza ninguna acción.
{% endtab %}
{% endtabs %}

### Importar tokens de notificaciones push de iOS {#import-ios-push-tokens}

Al migrar tokens de notificaciones push de iOS con `/users/track`, el campo `gateway` no se establece en el token de notificaciones push. Braze asume que los tokens importados a través de la API son tokens de push en primer plano válidos, pero no puede determinar a qué entorno de APNs pertenece el token.

Sin el campo de gateway, Braze utiliza la configuración del entorno alternativo configurado en tu aplicación al enviar notificaciones push. Esto puede provocar errores `BadDeviceToken` si el entorno real del token difiere del alternativo configurado. Por ejemplo, un token de desarrollo enviado a través del gateway de producción fallará.

Para evitar problemas de entrega:

- Asegúrate de que la configuración del entorno de tu aplicación en el panel de Braze coincida con los tokens que estás importando.
- Para aplicaciones en producción, importa solo tokens de producción.
- Para entornos de prueba, verifica que tanto la configuración de tu aplicación como los tokens importados utilicen el entorno de desarrollo.

{% alert note %}
Los tokens registrados a través del SDK or kit de desarrollo de software de Braze incluyen automáticamente el campo de gateway, ya que el SDK or kit de desarrollo de software detecta el entorno a partir de los permisos de tu aplicación.
{% endalert %}

### Importar tokens de notificaciones push de Android {#import-android-push-tokens}

{% alert important %}
La siguiente consideración se aplica solo para aplicaciones de Android. Las aplicaciones de iOS no requieren estos pasos porque esa plataforma tiene un solo framework para mostrar push, y las notificaciones push se renderizan inmediatamente siempre que Braze tenga los tokens de notificaciones push y certificados necesarios.
{% endalert %}

Si debes enviar notificaciones push de Android a tus usuarios antes de que se complete la integración del SDK or kit de desarrollo de software de Braze, utiliza pares clave-valor para validar las notificaciones push.

Debes tener un receptor para gestionar y mostrar las cargas útiles de push. Para notificar al receptor de la carga útil de push, añade los pares clave-valor necesarios a la Campaign de push. Los valores de estos pares dependen del partner de push específico que hayas utilizado antes de Braze.

{% alert note %}
Para algunos proveedores de notificaciones push, Braze necesita aplanar los pares clave-valor para que puedan interpretarse correctamente. Para aplanar los pares clave-valor de una aplicación de Android específica, ponte en contacto con tu CSM or administrador de éxito de cliente or administrador de éxito de cliente.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo encuentro usuarios tratados como correo no deseado o bloqueados para la mensajería? {#how-do-i-find-users-treated-as-spam-or-blocked-from-messaging}

Braze no proporciona una lista de correo no deseado dedicada en el panel. Braze bloquea perfiles de usuario individuales ("usuarios ficticios") con más de cinco millones de sesiones, más de 20 000 nombres de eventos personalizados distintos o más de 20 000 nombres de productos distintos en compras, y deja de ingerir todos los datos entrantes para ese perfil tanto de los SDK or kit de desarrollo de software como de la REST or transferencia de estado representacional API. Si un identificador está bloqueado, [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) puede devolver el error `"provided external_id is blacklisted and disallowed"`. Esta redacción se toma textualmente de la respuesta de la API. Para encontrar perfiles bloqueados por sesiones excesivas, crea un [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) con el filtro **Session Count** configurado en **more than 5,000,000**, exporta el Segment como CSV y verifica los campos de perfil en **Engagement** > **Search users** o con el endpoint [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier). No existe un filtro equivalente para nombres de eventos personalizados o nombres de productos distintos, por lo que debes contactar a tu director de cuentas de Braze para identificar los perfiles bloqueados por esas razones. Para más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_archival).