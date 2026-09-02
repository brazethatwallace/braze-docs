---
nav_title: "Objeto de destinatarios"
article_title: Objeto de destinatarios de la API
page_order: 9
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto de destinatarios de Braze."

---

# Objeto de destinatarios {#recipients-object}

> El objeto de destinatarios te permite solicitar o escribir información en nuestros endpoints.

Debes incluir uno de `external_user_id`, `user_alias`, `braze_id` o `email` en este objeto. **Las solicitudes deben especificar solo uno.**

El objeto de destinatarios te permite combinar el [objeto de alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object), el [objeto de propiedades del desencadenador]({{site.baseurl}}/api/objects_filters/trigger_properties_object), el [objeto de propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) y el [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Cuerpo del objeto {#object-body}

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "braze_id": (optional, string) see Braze ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "context": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas context object,
  "send_to_existing_only": (optional, boolean) defaults to true; cannot be used with user aliases; if set to `false`, an `attributes` object must also be included,
  "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
}]
```

Cuando `send_to_existing_only` es `true`, Braze solo envía el mensaje a usuarios existentes. Sin embargo, no puedes usar este indicador con alias de usuario.

Cuando `send_to_existing_only` es `false`, debes incluir un objeto `attributes` en el mismo destinatario. El indicador no reemplaza a `attributes`. Braze utiliza `attributes` para la creación o actualización del perfil previa al envío (por ejemplo, agregar campos de `email` o teléfono para la entrega por correo electrónico o servicio de mensajes cortos, o actualizar grupos de suscripción). Sin ese objeto, no obtienes el comportamiento combinado esperado para usuarios nuevos en [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) o [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

Ese perfil aún debe cumplir con las reglas de audiencia y elegibilidad de canal del mensaje antes de que Braze lo envíe.

- [ID de Braze]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [Alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)
- [ID de usuario externo]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [Priorización]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers)
- [Objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object)

## Deduplicación del objeto de destinatario {#recipient-object-deduping}

Al realizar una llamada a la API con el objeto de destinatario, **si existe un destinatario duplicado dirigido a la misma dirección (es decir, correo electrónico, push), Braze deduplica al usuario**, lo que significa que Braze elimina los usuarios idénticos, dejando solo uno.

Por ejemplo, si usas el mismo `external_user_id`, el usuario recibe solo un mensaje. Considera realizar múltiples llamadas a la API si necesitas una solución alternativa para este comportamiento.

Cuando el mismo `external_user_id` aparece varias veces en el array de destinatarios, Braze envía solo un mensaje y utiliza
las propiedades de desencadenamiento de la última aparición en el array. Este comportamiento es determinista y se basa en el orden del array.

En el siguiente ejemplo, `userid1` recibe un mensaje con `"name": "Beth Test 2"` porque esa entrada aparece en último lugar en el array.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
