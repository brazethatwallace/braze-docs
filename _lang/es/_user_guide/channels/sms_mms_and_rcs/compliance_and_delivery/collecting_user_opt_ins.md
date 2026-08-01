---
nav_title: "Recopilar adhesiones voluntarias de usuarios"
article_title: Buenas prácticas para recopilar adhesiones voluntarias de usuarios por SMS
page_order: 3
description: "Este artículo de referencia cubre tres buenas prácticas para recopilar adhesiones voluntarias de usuarios."
page_type: reference
channel:
  - SMS


---

# Recopilar adhesiones voluntarias de usuarios {#collect-user-opt-ins}

> El siguiente artículo enumera algunos métodos comunes de adhesión voluntaria por SMS.

## Opción 1: Pedir a los usuarios que envíen un mensaje de texto a tu código corto o código largo {#option-1-ask-users-to-text-your-short-or-long-code}

Pide a los usuarios que envíen "START", "UNSTOP", "YES" o una palabra clave de adhesión voluntaria personalizada a tu número para añadirlos automáticamente a tu grupo de suscripción. En tu sitio web, aplicación móvil o incluso en publicidad, puedes solicitar a los usuarios que hagan esto para la adhesión voluntaria, y puedes ofrecer un incentivo si resulta útil.

## Opción 2: Los usuarios se suscriben a través de un mensaje dentro de la aplicación {#option-2-users-opt-in-via-in-app-message}

Para permitir que los usuarios se suscriban a SMS desde un mensaje dentro de la aplicación, utiliza el [formulario de captura de número de teléfono]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture) proporcionado por Braze para crear un formulario con tu marca que te permita recopilar números de teléfono y hacer crecer tu lista de SMS.

![Creador de mensajes dentro de la aplicación con una plantilla para la captura de número de teléfono.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze recomienda que también utilices la característica de [doble adhesión voluntaria de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in). Esta característica funciona automáticamente con el formulario de captura de número de teléfono del mensaje dentro de la aplicación, solicitando a los usuarios que confirmen su intención después de enviar su número de teléfono a través del formulario.

## Opción 3: Flujo de registro {#option-3-sign-up-flow}

Cuando un nuevo usuario se registra en el sitio web o la aplicación, solicita su número de teléfono y correo electrónico. Incluye una casilla de verificación para recibir correos electrónicos y SMS promocionales.

Después de que el usuario se registre, haz lo siguiente:

1. Usa el [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) para crear el usuario y guardar sus atributos.

{% raw %}
```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```
{% endraw %}

{: start="2"}
2. Usa el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para suscribir al usuario a SMS.

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```
{% endraw %}

{% alert note %}
Para incluir a los usuarios en el flujo de trabajo de [doble adhesión voluntaria de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) al suscribirlos a través de la REST API, establece `use_double_opt_in_logic` en `true` en tu solicitud. Este parámetro es compatible con [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status), [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2) y [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).
<br><br>
Las actualizaciones de suscripción a través de la REST API no desencadenan automáticamente mensajes de bienvenida. Para enviar un mensaje de bienvenida, crea una Campaign basada en acciones con el desencadenador [Actualizar estado del grupo de suscripción]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#update-subscription-group-status) y establece la fuente de actualización en **REST API**.
{% endalert %}