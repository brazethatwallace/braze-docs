---
nav_title: Ciclo de vida del perfil de usuario
article_title: Ciclo de vida del perfil de usuario
page_order: 2
page_type: reference
description: "Este artículo de referencia describe el ciclo de vida del perfil de usuario de Braze y las diversas formas en que un perfil de usuario puede ser identificado y referenciado."

---

# Ciclo de vida del perfil de usuario {#user-profile-lifecycle}

> Este artículo describe el ciclo de vida del perfil de usuario de Braze y las distintas formas de identificar y hacer referencia a un perfil de usuario. Si deseas comprender mejor el ciclo de vida de tus clientes, consulta nuestro curso de Braze Learning sobre [Mapeo de los ciclos de vida de los usuarios](https://learning.braze.com/mapping-customer-lifecycles).

Todos los datos persistentes asociados con un usuario se almacenan en su perfil de usuario. Después de crear un perfil de usuario, ya sea a través de la API o después de que el SDK reconozca a un usuario, puedes asignar una serie de parámetros a ese perfil para identificar y hacer referencia a ese usuario.

Estos parámetros incluyen:

* `braze_id` (asignado por Braze)
* `external_id`
* `email`
* `phone`
* Cualquier número de alias de usuario personalizados que establezcas

## Perfiles de usuario anónimos {#anonymous-user-profiles}

Cualquier usuario sin un `external_id` designado se denomina [usuario anónimo]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users). Por ejemplo, podrían ser usuarios que visitaron tu sitio web pero no se registraron, o usuarios que descargaron tu aplicación móvil pero no crearon un perfil.

Inicialmente, cuando el SDK reconoce a un usuario, se crea un perfil de usuario anónimo con un `braze_id` asociado: un identificador único que Braze asigna automáticamente, que no se puede editar y que es específico del dispositivo. Este identificador se puede utilizar para actualizar el perfil de usuario a través de la [API]({{site.baseurl}}/api/endpoints/user_data).

## Perfiles de usuario identificados {#identified-user-profiles}

Después de que un usuario sea reconocible en tu aplicación (proporcionando alguna forma de ID de usuario o dirección de correo electrónico), te recomendamos asignar un `external_id` al perfil de ese usuario mediante el método `changeUser` ([web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)). Un `external_id` te permite identificar el mismo perfil de usuario en múltiples dispositivos.

Entre los beneficios adicionales de utilizar un `external_id` se incluyen los siguientes:

- Proporcionar una experiencia de usuario consistente en múltiples dispositivos y plataformas (por ejemplo, no enviar notificaciones de usuario inactivo a la tableta Android de un usuario cuando es un usuario fiel de la aplicación en iPhone).
- Mejorar la precisión de tus análisis confirmando que los usuarios no están creando un nuevo perfil de usuario cada vez que desinstalan y reinstalan, o instalan la aplicación en un dispositivo diferente.
- Habilitar la importación de datos de usuario desde fuentes externas a la aplicación mediante los [endpoints de datos de usuario]({{site.baseurl}}/api/endpoints/user_data) y dirigirte a los usuarios con mensajes transaccionales utilizando nuestros [endpoints de mensajería]({{site.baseurl}}/api/endpoints/messaging).
- Buscar usuarios individuales utilizando nuestros [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) de "Testing" dentro del segmentador, y en la página [**Buscar usuarios**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

### Consideraciones para los ID externos {#considerations-for-external-ids}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

#### Riesgo de utilizar un correo electrónico o un correo electrónico cifrado como ID externo {#risk-of-using-an-email-or-hashed-email-as-an-external-id}

Utilizar una dirección de correo electrónico o una dirección de correo electrónico cifrada como tu ID externo de Braze puede simplificar la gestión de identidades en tus orígenes de datos; sin embargo, es importante considerar los riesgos potenciales para la privacidad del usuario y la seguridad de los datos.

- **Información fácil de adivinar:** las direcciones de correo electrónico son fáciles de adivinar, lo que las hace vulnerables a ataques.
- **Riesgo de explotación:** si un usuario malintencionado altera su navegador web para enviar la dirección de correo electrónico de otra persona como su ID externo, podría acceder a mensajes confidenciales o información de la cuenta.

### Qué sucede cuando identificas usuarios anónimos {#what-happens-when-you-identify-anonymous-users}

Pueden ocurrir dos escenarios cuando identificas usuarios anónimos:

1) **Un usuario anónimo se convierte en un nuevo usuario identificado:** <br>Si el `external_id` aún no existe en Braze, el usuario anónimo se convierte en un nuevo usuario identificado y conserva todos los mismos atributos e historial del usuario anónimo.

2) **Un usuario anónimo se identifica como un usuario ya existente:** <br>Si el `external_id` ya existe en Braze, entonces este usuario fue previamente identificado como un usuario en el sistema de alguna otra manera, como a través de otro dispositivo (como una tableta) o datos de usuario importados.

En otras palabras, ya tienes un perfil de usuario para este usuario. En este caso, Braze hará lo siguiente:
1. Convertir en huérfano al usuario anónimo
2. Fusionar los [campos específicos del perfil de usuario]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) que aún no existan en el perfil del usuario identificado desde el perfil anónimo
3. Eliminar el perfil anónimo de tu base de usuarios para que los recuentos de usuarios no se inflen

Si tanto el usuario anónimo como el usuario conocido tienen un nombre, se mantiene el nombre del usuario conocido. Si el usuario conocido tiene un valor nulo y el usuario anónimo tiene un valor, el valor del usuario anónimo se fusiona en el perfil del usuario conocido si el valor se encuentra dentro de estos [campos específicos del perfil de usuario]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

{% alert important %}
No todos los datos se fusionan desde el perfil anónimo. Los tokens de notificaciones push y el historial de mensajes se transfieren, y los atributos personalizados, eventos personalizados y el historial de compras del perfil anónimo se fusionan en el usuario identificado solo cuando esos campos aún no existen en el perfil del usuario identificado. Cuando hay datos en conflicto, se mantienen los valores del usuario identificado. Consulta el [comportamiento de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) para ver la lista completa de campos que se transfieren y los que no.
{% endalert %}

Para obtener información sobre cómo configurar un `external_id` en un perfil de usuario, consulta nuestra documentación ([iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)).

### Informes y perfiles fusionados {#reporting-and-merged-profiles}

Cuando los perfiles anónimos e identificados se fusionan después de un envío, los resúmenes de Campaign en el panel atribuyen ese envío al perfil superviviente (identificado). [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) y la pestaña [Historial de mensajes]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) siguen atribuyendo el envío al ID de usuario del perfil huérfano, es decir, el ID en el momento del envío. Esto es lo esperado. Para ver la lista completa de campos que se transfieren, consulta el [comportamiento de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

Para encontrar ese envío en Currents, Query Builder o el historial de mensajes, busca el `braze_id` del perfil huérfano. Una consulta que utilice solo el `braze_id` del usuario identificado no devuelve el envío anterior a la fusión.

{% alert note %}
Los usuarios huérfanos no son elegibles para recibir mensajes.
{% endalert %}

### Fusionar usuarios duplicados {#merging-duplicate-users}

Cuando identifies perfiles de usuario duplicados en tu espacio de trabajo, puedes fusionarlos utilizando la REST API. Para obtener más información sobre la fusión de usuarios y los métodos disponibles, consulta [Fusionar usuarios duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

## Alias de usuario {#user-aliases}

Para referirse a los usuarios mediante identificadores distintos del `external_id` de Braze, establece alias de usuario en un perfil de usuario. Cualquier alias establecido en un perfil de usuario actuará de forma adicional al `braze_id` o `external_id` del usuario, en lugar de sustituirlo. No hay límite en la cantidad de alias que puedes establecer en un perfil de usuario.

Cada alias funciona como un par clave-valor que consta de dos partes: un `alias_label`, que define la clave del alias, y un `alias_name`, que define el valor. Un `alias_name` para cualquier etiqueta individual debe ser único en toda tu base de usuarios (igual que con `external_id`). Si intentas actualizar un segundo perfil de usuario con una combinación de etiqueta y nombre preexistente, el perfil de usuario no se actualizará.

### Actualización de alias de usuario {#updating-user-aliases}

Un alias puede actualizarse con un nuevo nombre para una etiqueta determinada después de haberse establecido, ya sea utilizando nuestros [endpoints de datos de usuario]({{site.baseurl}}/api/endpoints/user_data) o pasando un nuevo nombre a través del SDK. El alias de usuario será entonces visible al exportar los datos de ese usuario.

![Dos perfiles de usuario diferentes para usuarios distintos con la misma etiqueta de alias de usuario pero diferentes nombres de alias]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Etiquetado de usuarios anónimos {#tagging-anonymous-users}

Los alias de usuario también te permiten etiquetar a los usuarios anónimos con un identificador. Por ejemplo, si un usuario proporciona su dirección de correo electrónico a tu sitio de comercio electrónico pero aún no se ha suscrito, la dirección de correo electrónico puede utilizarse como alias para ese usuario anónimo. Estos usuarios pueden exportarse utilizando sus alias o referenciarse a través de la API.

### Comportamiento de los alias en perfiles de usuario anónimos {#behavior-of-aliases-on-anonymous-user-profiles}

Si un perfil de usuario anónimo con un alias es reconocido posteriormente con un `external_id`, será tratado como un perfil de usuario identificado normal, pero conservará su alias existente y podrá seguir siendo referenciado por dicho alias.

### Búsqueda de un alias de usuario {#searching-for-a-user-alias}

Si conoces el nombre y la etiqueta del alias de un usuario, puedes encontrarlo en **Buscar usuarios** con el formato `alias_label:alias_name`. Por ejemplo, si tienes un perfil de solo alias con el nombre `alias_name: bobby_alias` y la etiqueta `alias_label: m4pzOndtA-CnO0u`, puedes encontrar a este usuario introduciendo `m4pzOndtA-CnO0u:bobby_alias`.

Si no conoces esta información, puedes llamar al [endpoint `Export user profile by identifier`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) y encontrar el alias de usuario en la respuesta de la API.

### Establecimiento de alias en perfiles de usuario conocidos {#setting-aliases-on-known-user-profiles}

También se puede establecer un alias de usuario en un perfil de usuario conocido para hacer referencia a un usuario conocido mediante otro ID externo conocido. Por ejemplo, un usuario puede tener un ID de herramienta de inteligencia empresarial (como un ID de Amplitude) que desees referenciar dentro de Braze.

Para obtener información sobre cómo establecer un alias de usuario, consulta nuestra documentación para cada plataforma ([iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)).

![Diagrama de flujo del ciclo de vida de un perfil de usuario en Braze. Cuando se llama a changeUser() para un usuario anónimo, ese usuario se convierte en un usuario identificado y los datos se migran a su perfil de usuario identificado. El usuario identificado tiene un ID de Braze y un ID externo. En este punto, si un segundo usuario anónimo tiene una llamada a changeUser(), los campos de datos de usuario que aún no existan en el usuario identificado se fusionarán. Si el usuario identificado tiene un alias añadido a su perfil de usuario existente, no se verán afectados los datos, pero se convertirá en un usuario identificado con alias. Si un tercer usuario anónimo con la misma etiqueta de alias que el usuario identificado pero un nombre de alias diferente tiene una llamada a changeUser(), cualquier campo que no exista en el usuario identificado se fusionará y la etiqueta de alias en el perfil del usuario identificado se mantendrá.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
¿Tienes dificultades para visualizar cómo puede verse esto en el ciclo de vida del perfil de usuario de tus clientes? Visita [Buenas prácticas]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices) para consultar las mejores prácticas de recopilación de datos de usuario.
{% endalert %}

## Caso de uso avanzado {#advanced-use-case}

Puedes establecer un nuevo alias de usuario para perfiles de usuario identificados existentes a través de nuestro SDK y nuestra API utilizando los [endpoints de datos de usuario]({{site.baseurl}}/api/endpoints/user_data). Sin embargo, los alias de usuario no se pueden establecer a través de la API para un perfil de usuario desconocido existente.

Los alias de usuario también se fusionan en el proceso. Sin embargo, si tanto el usuario que va a quedar huérfano como el usuario de destino tienen un alias con la misma etiqueta, solo se mantiene el alias del usuario de destino.

Desinstalar y reinstalar una aplicación generará un nuevo `braze_id` anónimo para ese usuario.

### Solución de problemas con los ID de usuario {#troubleshooting-with-user-ids}

Todos los ID de usuario se pueden utilizar para buscar e identificar usuarios en tu panel para realizar pruebas. Para buscar a tu usuario en el panel de Braze, consulta [Añadir usuarios de prueba]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users).

{% alert important %}
Braze bloquea los perfiles de usuario que crecen de forma anormalmente grande ("usuarios ficticios"), ya que estos perfiles son generalmente el resultado de una integración incorrecta. Un perfil se bloquea cuando supera cualquiera de los siguientes umbrales:

- Más de 5.000.000 de sesiones
- Más de 20.000 nombres de eventos personalizados distintos
- Más de 20.000 nombres de productos distintos en compras

Después de que un perfil es bloqueado, Braze deja de ingerir todos los datos entrantes para ese perfil, tanto de los SDK como de la REST API. Si descubres que esto le ha ocurrido a un usuario legítimo, ponte en contacto con tu director de cuentas de Braze. Para obtener más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_archival).
{% endalert %}