---
nav_title: Buenas prácticas de recopilación
article_title: Buenas prácticas de recopilación
page_order: 4
page_type: reference
description: "El siguiente artículo ayuda a aclarar los distintos métodos y las buenas prácticas para recopilar datos de usuario nuevos y existentes."

---

# Buenas prácticas de recopilación {#collection-best-practices}

> Saber cuándo y cómo recopilar datos de usuarios conocidos y desconocidos puede ser un reto a la hora de prever el ciclo de vida del perfil de usuario de tus clientes. Este artículo ayuda a aclarar los diferentes métodos y las buenas prácticas para recopilar datos de usuarios nuevos y existentes guiándote a través de un caso de uso.

El siguiente ejemplo es un caso de uso de recopilación de datos por correo electrónico, pero la lógica se aplica a muchos escenarios diferentes de recopilación de datos. En este ejemplo, suponemos que ya has integrado un formulario de registro o una forma de recopilar información del usuario.

Después de que un usuario proporcione información para que la registres, te recomendamos que compruebes si los datos ya existen en tu base de datos y, cuando sea necesario, crees un perfil de alias de usuario o actualices el perfil de usuario existente.

Si un usuario desconocido visitara tu sitio y, más adelante, creara una cuenta o se identificara a través del registro por correo electrónico, la fusión de perfiles debe tratarse con cuidado. En función del método de fusión, es posible que se sobrescriba la información de los usuarios de solo alias o los datos anónimos.

## Captura de datos de usuario a través de un formulario web {#capturing-user-data-through-a-web-form}

### Paso 1: Comprueba si el usuario existe {#step-1-check-if-the-user-exists}

Cuando un usuario introduce contenido a través de un formulario web, comprueba si ya existe un usuario con ese correo electrónico en tu base de datos. Puedes hacerlo de una de las siguientes formas:

- **Comprueba la base de datos interna (recomendado):** Si tienes un registro externo o una base de datos que contiene la información del usuario proporcionada y que existe fuera de Braze, haz referencia a este en el momento del envío del correo electrónico o de la creación de la cuenta para confirmar que la información no se ha capturado previamente.
- **[Endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track):** Utiliza `email` como identificador, y se creará un nuevo perfil de usuario si la dirección de correo electrónico aún no existe.
- **[Endpoint `/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status):** Si recopilas correos electrónicos a través de un formulario personalizado y luego configuras la pertenencia a grupos de suscripción a través de la REST API, llama primero a este endpoint. Si no existe un perfil coincidente, crea o suscribe al usuario con el [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). De lo contrario, actualiza el perfil existente en lugar de crear un duplicado.

### Paso 2: Registra o actualiza el usuario {#step-2-log-or-update-user}

- **Si un usuario existe:**
  - No crees un nuevo perfil.
  - Registra un atributo personalizado (por ejemplo, `newsletter_subscribed: true`) en el perfil del usuario para indicar que ha enviado su correo electrónico a través de una suscripción a un boletín informativo. Si existen múltiples perfiles de usuario en Braze con la misma dirección de correo electrónico, se exportarán todos los perfiles.<br><br>
- **Si un usuario no existe:**
  - Crea un perfil de solo alias a través del [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Este endpoint aceptará un [objeto `user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object) y creará un perfil de solo alias cuando `update_existing_only` esté configurado como `false`. Establece el correo electrónico del usuario como alias de usuario para hacer referencia a ese usuario en el futuro (ya que el usuario no tendrá un `external_id`).

![Diagrama que muestra el proceso para actualizar un perfil de usuario de solo alias. Un usuario envía su dirección de correo electrónico y un atributo personalizado, su código postal, en una página de destino de marketing. Una flecha que apunta desde la recopilación de la página de destino a un perfil de usuario de solo alias muestra una solicitud de la API de Braze al endpoint Track user, con el cuerpo de la solicitud que contiene el nombre de alias del usuario, la etiqueta de alias, el correo electrónico y el código postal. El perfil tiene la etiqueta "Usuario de solo alias creado en Braze" con los atributos del cuerpo de la solicitud para reflejar los datos en el perfil recién creado.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## Captura de correos electrónicos de los usuarios a través de un formulario de captura de correo electrónico {#capturing-user-emails-through-an-email-capture-form}

Usa un formulario de captura de correo electrónico para solicitar a los usuarios que envíen su dirección de correo electrónico, que se añadirá a su perfil de usuario. Para más información sobre cómo configurar este formulario, consulta [Formulario de captura de correo electrónico]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form).

Si utilizas un formulario personalizado y configuras la pertenencia al grupo de suscripción a través de la REST API, comprueba si ya existe un perfil antes de crear un usuario. Consulta [Paso 1: Comprueba si el usuario existe](#step-1-check-if-user-exists).

## Identificación de usuarios solo con alias {#identifying-alias-only-users}

Al identificar usuarios durante la creación de cuentas, los usuarios solo con alias pueden ser identificados y asignados un ID externo a través del [endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) fusionando el usuario solo con alias con el perfil conocido.

Para comprobar si un usuario es solo con alias, [verifica si el usuario existe](#step-1-check-if-user-exists) en tu base de datos.
- Si existe un registro externo, puedes llamar al endpoint `/users/identify/`.
- Si el [endpoint `/users/export/id`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) devuelve un `external_id`, puedes llamar al endpoint `/users/identify/`.
- Si el endpoint no devuelve nada, no se debe realizar una llamada a `/users/identify/`.

## Captura de datos de usuario cuando ya existe información de usuario de solo alias {#capturing-user-data-when-alias-only-user-information-is-already-present}

Cuando un usuario crea una cuenta o se identifica a través del registro por correo electrónico, puedes fusionar los perfiles. Para obtener una lista de los campos que se pueden fusionar, consulta [Comportamiento de actualización de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

### Fusión de perfiles de usuario duplicados {#merging-duplicate-user-profiles}

A medida que tus datos de usuario crecen, puedes fusionar perfiles de usuario duplicados desde el panel de Braze. Estos perfiles duplicados deben encontrarse utilizando la misma consulta de búsqueda. Para obtener más información sobre cómo duplicar perfiles de usuario, consulta [Fusionar usuarios duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

También puedes utilizar el [endpoint Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) para fusionar un perfil de usuario en otro.

{% alert note %}
Una vez fusionados los perfiles de usuario, esta acción no se puede deshacer.
{% endalert %}

## Recursos adicionales {#additional-resources}
- Consulta nuestro artículo sobre el [ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) de Braze para obtener contexto adicional.<br>
- Revisa nuestra documentación sobre cómo configurar los ID de usuario y llamar al método `changeUser()` para [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#suggested-user-id-naming-convention) y [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).