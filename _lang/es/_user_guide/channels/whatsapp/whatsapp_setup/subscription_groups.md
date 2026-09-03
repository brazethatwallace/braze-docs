---
nav_title: "Grupos de suscripción"
article_title: "Grupos de suscripción"
page_order: 4
description: "Este artículo describe los grupos de suscripción de WhatsApp, qué estados de suscripción se ofrecen y cómo se configuran los grupos de suscripción."
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp

---

# Grupos de suscripción de WhatsApp {#whatsapp-subscription-groups}

> Los grupos de suscripción de WhatsApp se crean al integrar WhatsApp con tu aplicación a través del **portal de socios tecnológicos**. Para un resumen multicanal de los grupos de suscripción, consulta [Grupos de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## Estados de suscripción de WhatsApp {#whatsapp-subscription-states}

Para conocer las definiciones de los estados de suscripción de WhatsApp y cómo se relacionan con los requisitos de adhesión voluntaria de Meta, consulta [Estado de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp).

### Configurar los grupos de suscripción de WhatsApp de los usuarios {#setting-users-whatsapp-subscription-groups}

- **REST API:** Los perfiles de usuario pueden configurarse de forma programática mediante el [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) usando la REST API de Braze.
- **SDK Web:** Los usuarios pueden añadirse a un grupo de suscripción de correo electrónico, SMS o WhatsApp con el método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) o [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Importación de usuarios**: Los usuarios pueden añadirse a grupos de suscripción de correo electrónico o SMS a través de **Importar usuarios**. Al actualizar el estado del grupo de suscripción, debes tener estas dos columnas en tu CSV: `subscription_group_id` y `subscription_state`. Consulta [Importación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) para más información.

### Comprobar el grupo de suscripción de WhatsApp de un usuario {#checking-a-users-whatsapp-subscription-group}

- **Perfil de usuario:** Se puede acceder a los perfiles de usuario individuales a través del panel de Braze en **Audiencia** > **Buscar usuarios**. Aquí puedes buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID de usuario externo. Dentro del perfil de un usuario, en la pestaña **Interacción**, puedes ver el grupo de suscripción de WhatsApp de un usuario y su estado.

- **REST API:** El grupo de suscripción de un perfil de usuario individual puede consultarse a través del [endpoint Lista de grupos de suscripción de usuarios]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) o del [endpoint Lista de estados de grupos de suscripción de usuarios]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) usando la REST API de Braze.

## Archivar grupos de suscripción {#archive-subscription-groups}

Si necesitas dejar de usar un grupo de suscripción de WhatsApp, puedes archivarlo para marcarlo como inactivo.

Archivar un grupo de suscripción lo marca como inactivo, pero no lo elimina de tu espacio de trabajo. Si necesitas eliminar un número de teléfono de WhatsApp o un grupo de suscripción por completo, primero debes archivar el grupo de suscripción en el Administrador de grupos de suscripción antes de solicitar la eliminación a soporte de Braze.

Para archivar un grupo de suscripción:

1. Ve a **Audiencia** > **Administración del grupo de suscripción**.
2. Busca el grupo de suscripción de WhatsApp que deseas archivar.
3. Pasa el cursor sobre el estado del grupo de suscripción y selecciona <i class="fa-solid fa-box-archive" aria-label="Archivar"></i> **Archivar**.

## Proceso de adhesión y cancelación de suscripción de WhatsApp {#whatsapp-opt-in-and-opt-out-process}

Para obtener un resumen del estado de suscripción de WhatsApp, los requisitos de adhesión voluntaria y el comportamiento de cancelación de suscripción, consulta [Estado de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp).

Actualmente, los usuarios pueden suscribirse y [adherirse y cancelar su suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) a la mensajería de WhatsApp de varias maneras, incluyendo [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), a través de un sitio web, un hilo de WhatsApp, por teléfono o en persona. Ten en cuenta que las adhesiones voluntarias son obligatorias.

Las palabras clave de adhesión voluntaria no son compatibles actualmente con el canal de WhatsApp, por lo que eres responsable de mantener una lista de usuarios. WhatsApp tiene un enfoque retrospectivo en cuanto a las adhesiones voluntarias y los límites de velocidad: si los usuarios empiezan a reportarte o bloquearte, tu límite de velocidad se reduce.

## Actualizar el estado de suscripción de un usuario en un Canvas de WhatsApp {#update-subscription-status}

Independientemente de los métodos de adhesión y cancelación de suscripción que utilices, puedes actualizar el estado de suscripción de los perfiles de usuario con uno de los siguientes métodos de actualización:

- Crea un [webhook de Braze a Braze]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#considerations) que actualice el estado de suscripción a través de la REST API, como en el siguiente ejemplo:

![Creador de webhook con un mensaje que utiliza el método POST.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

Para evitar condiciones de carrera, cualquier mensaje de seguimiento después del webhook debe estar contenido en un segundo Canvas que se desencadene por los resultados del primer Canvas (como que un usuario haya entrado en una variante de Canvas y esté en un grupo de suscripción de WhatsApp).

- Usa el editor JSON avanzado para actualizar el perfil de usuario con la siguiente plantilla:

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

![Paso de actualización de usuario con un paso del editor JSON avanzado.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
Las actualizaciones del estado de suscripción de un usuario pueden tardar hasta 60 segundos.
{% endalert %}