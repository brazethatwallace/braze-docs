---
nav_title: "Objeto destinatários"
article_title: Objeto de destinatários da API or interface de programação do aplicativo (API)
page_order: 9
page_type: reference
description: "Este artigo de referência explica os diferentes componentes do objeto de destinatários da Braze."

---

# Objeto destinatários {#recipients-object}

> O objeto de destinatários permite que você solicite ou grave informações em nossos endpoints.

Você deve incluir um dos seguintes neste objeto: `external_user_id`, `user_alias`, `braze_id` ou `email`. **As solicitações devem especificar apenas um.**

O objeto de destinatários permite combinar o [objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object), o [objeto de propriedades do gatilho]({{site.baseurl}}/api/objects_filters/trigger_properties_object), o [objeto de propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) e o [objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Corpo do objeto {#object-body}

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

Quando `send_to_existing_only` é `true`, a Braze envia a mensagem apenas para usuários existentes. No entanto, você não pode usar esse flag com aliases de usuário.

Quando `send_to_existing_only` é `false`, você deve incluir um objeto `attributes` no mesmo destinatário. O flag não substitui `attributes`. A Braze usa `attributes` para a criação ou atualização de perfil antes do envio (por exemplo, adicionar campos de `email` ou telefone para entrega de e-mail ou SMS, ou atualizar grupos de inscrições). Sem esse objeto, você não obtém o comportamento combinado esperado para novos usuários em [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) ou [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

Esse perfil ainda precisa atender às regras de público e elegibilidade de canal da mensagem antes que a Braze faça o envio.

- [Braze ID]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [Aliases de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)
- [ID de usuário externo]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [Priorização]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers)
- [Objeto de atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object)

## Deduplicação do objeto de destinatário {#recipient-object-deduping}

Ao fazer uma chamada de API or interface de programação do aplicativo (API) com o objeto de destinatário, **se existir um destinatário duplicado direcionado ao mesmo endereço (ou seja, e-mail, push), a Braze faz a deduplicação do usuário**, o que significa que a Braze remove os usuários idênticos, mantendo apenas um.

Por exemplo, se você usar o mesmo `external_user_id`, o usuário receberá apenas uma mensagem. Considere fazer várias chamadas de API or interface de programação do aplicativo (API) se precisar de uma solução alternativa para esse comportamento.

Quando o mesmo `external_user_id` aparece várias vezes no array de destinatários, a Braze envia apenas uma mensagem e usa as propriedades de disparo da última ocorrência no array. Esse comportamento é determinístico e baseado na ordem do array.

No exemplo a seguir, `userid1` recebe uma mensagem usando `"name": "Beth Test 2"` porque essa entrada aparece por último no array.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
