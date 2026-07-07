---
nav_title: Administración de usuarios
article_title: Administración de usuarios de LINE
page_order: 0
description: "Este artículo cubre el ID de usuario de LINE y cómo configurarlo."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# Administración de usuarios de LINE {#line-user-management}

> El ID de usuario de LINE se almacena en el atributo del perfil de usuario llamado `native_line_id`, que se utiliza para enviar mensajes a un usuario en el canal de LINE. Este artículo cubre cómo configurar y encontrar el atributo `native_line_id`.

Los datos de usuario del cliente se representan en un [perfil de usuario de Braze]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle). Un perfil de usuario almacena información y atributos sobre los usuarios de una empresa, como nombres y direcciones de correo electrónico.

Cuando envías mensajes de LINE a través de Braze, Braze utiliza el atributo `native_line_id` para identificar a qué usuarios enviar el mensaje. Cuando LINE envía eventos de webhook a Braze, como cuando un usuario sigue un canal o responde a un mensaje, se utiliza el `native_line_id` para buscar el perfil de usuario correspondiente.

{% alert note %}
Los ID de usuario de LINE son distintos por proveedor de LINE. Un usuario específico tendrá diferentes ID de usuario de LINE para cada proveedor que siga. Es poco probable que los usuarios conozcan su ID de LINE (a diferencia de su correo electrónico o número de teléfono), ya que cambian para cada marca que siguen.
{% endalert %}

## Configurar el atributo `native_line_id` {#setting-the-native_line_id-attribute}

Hay varios escenarios en los que se establece `native_line_id` en el perfil de usuario, que se describen a continuación.

| Escenario | Si existe un perfil de usuario con `native_line_id` | Resultado |
| --- | --- | --- |
| Un usuario sigue un canal de LINE | No | Se crea un perfil de usuario anónimo (será necesario fusionar):<br> - `native_line_id` se establece con el ID de LINE del usuario <br>- El alias de usuario `line_id` se establece con el ID de LINE del usuario<br>- El usuario se suscribe al grupo de suscripción de Braze del canal |
| Un usuario sigue un canal de LINE | Sí | Todos los perfiles de usuario con el `native_line_id`:<br>- Se suscriben al grupo de suscripción de Braze del canal |
| La empresa utiliza la carga de CSV de usuarios con una columna `native_line_id` | No | Si no existe un perfil de usuario para el `external_id` o alias de usuario especificado:<br>- `native_line_id` se establece con el valor especificado<br> - Todos los demás atributos especificados en el CSV se establecen en el perfil de usuario |
| La empresa utiliza la carga de CSV de usuarios con una columna `native_line_id` | Sí | Si existe un perfil de usuario para el `external_id` o alias de usuario especificado:<br>- `native_line_id` se establece con el valor especificado<br>- Todos los demás atributos especificados en el CSV se establecen en el perfil de usuario<br>- Múltiples perfiles tienen el mismo `native_line_id` |
| La empresa utiliza el punto de conexión `/users/track` y especifica el atributo `native_line_id` | No | Si no existe un perfil de usuario para el usuario especificado ([especificado por `external_id`, `user_alias`, `braze_id` o `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens)):<br>- `native_line_id` se establece con el valor especificado<br>- Todos los demás atributos especificados en la solicitud se establecen en el perfil de usuario |
| La empresa utiliza el punto de conexión `/users/track` y especifica el atributo `native_line_id` | Sí | Si existe un perfil de usuario para el usuario especificado ([especificado por `external_id`, `user_alias`, `braze_id` o `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens)):<br>- `native_line_id` se establece con el valor especificado<br>- Todos los demás atributos especificados en la solicitud se establecen en el perfil de usuario<br>- Múltiples perfiles tienen el mismo `native_line_id` |
| La empresa solicita a Braze que ejecute el sincronizador de estado de suscripción | No | Si se devuelve un ID de usuario de LINE desde LINE que no tiene un perfil de usuario correspondiente en Braze, se crea un perfil de usuario anónimo:<br>- `native_line_id` se establece con el ID de LINE del usuario<br>- El alias de usuario `line_id` se establece con el ID de LINE del usuario<br>- El usuario se suscribe al grupo de suscripción de Braze del canal<br><br>Ten en cuenta que si posteriormente se crea un usuario con el mismo ID de LINE, habrá usuarios duplicados, pero ambos tendrán el estado de suscripción de LINE correcto. La fusión de usuarios puede limpiar tu base de usuarios en estos casos. |
| La empresa solicita a Braze que ejecute el sincronizador de estado de suscripción | Sí | Si se devuelve un ID de usuario de LINE desde LINE que tiene un perfil de usuario correspondiente en Braze:<br>- El usuario se suscribe al grupo de suscripción de Braze del canal |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Configurar el atributo nativelineid" }

## Encontrar el `native_line_id` {#finding-the-native_line_id}

Al ver un perfil de usuario en el panel de Braze, puedes comprobar si tiene el atributo `native_line_id` establecido yendo a la pestaña **Engagement** > sección **Contact Settings** > sección **LINE**.

Si se ha establecido el `native_line_id`, se mostrará en **LINE User ID**. De lo contrario, no aparecerá.

![Configuración de contacto de LINE en la pestaña Engagement.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}