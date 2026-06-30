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

## Captura de datos del usuario a través de un formulario web {#capturing-user-data-through-a-web-form}

### Paso 1: Comprobar si el usuario existe {#step-1-check-if-the-user-exists}

Cuando un usuario introduce contenido a través de un formulario web, comprueba si ya existe un usuario con ese correo electrónico en tu base de datos. Esto puede hacerse de dos maneras:

- **Comprueba la base de datos interna (recomendado):** Si tienes un registro externo o una base de datos que contenga la información del usuario proporcionada y que exista fuera de Braze, haz referencia a ella en el momento del envío por correo electrónico o de la creación de la cuenta para confirmar que la información no se ha capturado ya.
- **[Punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track):** Utiliza `email` como identificador, y se creará un nuevo perfil de usuario si la dirección de correo electrónico aún no existe.

### Paso 2: Registrar o actualizar usuario {#step-2-log-or-update-user}

- **Si existe un usuario:**
  - No crees un perfil nuevo.
  - Registra un atributo personalizado (por ejemplo, `newsletter_subscribed: true`) en el perfil del usuario para indicar que ha enviado su correo electrónico a través de una suscripción al boletín. Si existen varios perfiles de usuario de Braze con la misma dirección de correo electrónico, se exportarán todos los perfiles.<br><br>
- **Si un usuario no existe:**
  - Crea un perfil de solo alias a través del [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Este punto de conexión aceptará un [objeto `user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object) y creará un perfil de solo alias cuando `update_existing_only` esté configurado como `false`. Establece el correo electrónico del usuario como el alias de usuario para hacer referencia a ese usuario en el futuro (ya que el usuario no tendrá un `external_id`).

![Diagrama que muestra el proceso para actualizar un perfil de usuario de solo alias. Un usuario envía su dirección de correo electrónico y un atributo personalizado, su código postal, en una página de destino de marketing. Una flecha que apunta desde la recopilación de la página de destino a un perfil de usuario de solo alias muestra una solicitud de la API de Braze al punto de conexión Track user, con el cuerpo de la solicitud que contiene el nombre de alias del usuario, la etiqueta de alias, el correo electrónico y el código postal. El perfil tiene la etiqueta "Usuario de solo alias creado en Braze" con los atributos del cuerpo de la solicitud para mostrar los datos reflejados en el perfil recién creado.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## Captura de correos electrónicos de usuarios a través de un formulario de captura de correo electrónico {#capturing-user-emails-through-an-email-capture-form}

Utiliza un formulario de captura de correo electrónico para pedir a los usuarios que envíen su dirección de correo electrónico, que se añadirá a su perfil de usuario. Para obtener más información sobre cómo configurar este formulario, consulta [Formulario de captura de correo electrónico]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form).

## Identificación de usuarios de solo alias {#identifying-alias-only-users}

Al identificar a los usuarios en el momento de la creación de la cuenta, se puede identificar a los usuarios de solo alias y asignarles un ID externo a través del [punto de conexión `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) fusionando el usuario de solo alias con el perfil conocido.

Para comprobar si un usuario es de solo alias, [comprueba si el usuario existe](#step-1-check-if-user-exists) en tu base de datos.
- Si existe un registro externo, puedes llamar al punto de conexión `/users/identify/`.
- Si el [punto de conexión `/users/export/id`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) devuelve un `external_id`, puedes llamar al punto de conexión `/users/identify/`.
- Si el punto de conexión no devuelve nada, no debe hacerse una llamada a `/users/identify/`.

## Captura de datos de usuario cuando ya existe información de usuario de solo alias {#capturing-user-data-when-alias-only-user-information-is-already-present}

Cuando un usuario crea una cuenta o se identifica mediante el registro por correo electrónico, puedes fusionar los perfiles. Para obtener una lista de los campos que pueden fusionarse, consulta [Comportamiento de las actualizaciones de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge_updates-behavior).

### Fusión de perfiles de usuario duplicados {#merging-duplicate-user-profiles}

A medida que crezcan tus datos de usuario, podrás fusionar perfiles de usuario duplicados desde el dashboard de Braze. Estos perfiles duplicados deben encontrarse utilizando la misma consulta de búsqueda. Para más información sobre cómo fusionar perfiles de usuario, consulta [Fusionar perfiles]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#merge-profiles).

También puedes utilizar el [punto de conexión Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) para fusionar un perfil de usuario en otro.

{% alert note %}
Una vez fusionados los perfiles de usuario, esta acción no puede deshacerse.
{% endalert %}

## Recursos adicionales {#additional-resources}
- Consulta nuestro artículo sobre el [ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) de Braze para obtener más información.<br>
- Consulta nuestra documentación sobre la configuración de ID de usuario y la llamada al método `changeUser()` para [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#suggested-user-id-naming-convention) y [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).