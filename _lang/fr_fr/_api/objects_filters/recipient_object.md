---
nav_title: "Objet destinataire"
article_title: Objet destinataire de l'API
page_order: 9
page_type: reference
description: "Cet article de référence explique les différents composants de l'objet destinataire de Braze."

---

# Objet destinataire {#recipients-object}

> L'objet destinataire vous permet de demander ou d'écrire des informations dans nos endpoints.

Vous devez inclure `external_user_id`, `user_alias`, `braze_id` ou `email` dans cet objet. **Les requêtes ne doivent en spécifier qu'un seul.**

L'objet destinataire vous permet de combiner l'[objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object), l'[objet propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object), l'[objet propriétés d'entrée Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) et l'[objet attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Corps de l'objet {#object-body}

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

Lorsque `send_to_existing_only` est défini sur `true`, Braze envoie le message uniquement aux utilisateurs existants. Cependant, il n'est pas possible d'utiliser ce paramètre avec les alias d'utilisateurs.

Lorsque `send_to_existing_only` est défini sur `false`, vous devez inclure un objet `attributes` sur le même destinataire. Ce paramètre ne remplace pas `attributes`. Braze utilise `attributes` pour la création ou la mise à jour du profil avant l'envoi (par exemple, l'ajout de champs `email` ou téléphone pour la distribution par e-mail ou SMS, ou la mise à jour des groupes d'abonnement). Sans cet objet, vous n'obtenez pas le comportement combiné attendu pour les nouveaux utilisateurs sur [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) ou [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

Ce profil doit tout de même respecter les règles d'audience et d'éligibilité au canal du message avant que Braze ne procède à l'envoi.

- [ID Braze]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [Alias d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases)
- [ID utilisateur externe]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [Priorisation]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers)
- [Objet attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object)

## Déduplication de l'objet destinataire {#recipient-object-deduping}

Lorsqu'un appel API est effectué avec l'objet destinataire, **s'il existe un destinataire en double ciblant la même adresse (c'est-à-dire e-mail, notification push), Braze procède à la déduplication de l'utilisateur**, ce qui signifie que les doublons sont supprimés et qu'un seul est conservé.

Par exemple, si vous utilisez le même `external_user_id`, l'utilisateur ne recevra qu'un seul message. Si vous avez besoin de contourner ce comportement, envisagez d'effectuer plusieurs appels API.

Lorsque le même `external_user_id` apparaît plusieurs fois dans le tableau des destinataires, Braze n'envoie qu'un seul message et utilise les propriétés du déclencheur de la dernière occurrence dans le tableau. Ce comportement est déterministe et basé sur l'ordre du tableau.

Dans l'exemple suivant, `userid1` reçoit un seul message avec `"name": "Beth Test 2"`, car cette entrée apparaît en dernier dans le tableau.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
