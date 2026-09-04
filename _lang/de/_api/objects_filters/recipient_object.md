---
nav_title: "Empfänger:innen-Objekt"
article_title: "API-Empfänger:innen-Objekt"
page_order: 9
page_type: reference
description: "Dieser Referenzartikel erläutert die verschiedenen Komponenten des Braze Empfänger:innen-Objekts."

---

# Empfänger:innen-Objekt {#recipients-object}

> Das Empfänger:innen-Objekt erlaubt es Ihnen, Informationen in unseren Endpunkten anzufragen oder zu schreiben.

Sie müssen in diesem Objekt eines der folgenden Felder angeben: `external_user_id`, `user_alias`, `braze_id` oder `email`. **In der Anfrage darf nur eines angegeben werden.**

Mit dem Empfänger:innen-Objekt können Sie das [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object), das [Trigger-Eigenschaften-Objekt]({{site.baseurl}}/api/objects_filters/trigger_properties_object), das [Canvas-Entry-Eigenschaften-Objekt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) und das [Nutzerattribute-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object) kombinieren.

## Objektkörper {#object-body}

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

Wenn `send_to_existing_only` auf `true` gesetzt ist, sendet Braze die Nachricht nur an bestehende Nutzer:innen. Dieses Flag kann jedoch nicht mit Nutzer-Aliases verwendet werden.

Wenn `send_to_existing_only` auf `false` gesetzt ist, müssen Sie ein `attributes`-Objekt für denselben Empfänger bzw. dieselbe Empfängerin angeben. Das Flag ersetzt nicht `attributes`. Braze verwendet `attributes` für die Profilerstellung oder -aktualisierung vor dem Versand (z. B. das Hinzufügen von `email`- oder Telefonnummernfeldern für die E-Mail- oder SMS-Zustellung oder die Aktualisierung von Abo-Gruppen). Ohne dieses Objekt erhalten Sie nicht das beabsichtigte kombinierte Verhalten für völlig neue Nutzer:innen bei [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) oder [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

Das Profil muss weiterhin die Zielgruppen- und Kanalberechtigungsregeln der Nachricht erfüllen, bevor Braze die Nachricht sendet.

- [Braze-ID]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [Nutzer-Aliases]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)
- [Externe Nutzer-ID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [Priorisierung]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers)
- [Nutzerattribute-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object)

## Deduplizierung des Empfänger:innen-Objekts {#recipient-object-deduping}

Wenn Sie einen API-Aufruf mit dem Empfänger:innen-Objekt durchführen und **ein doppelter Empfänger bzw. eine doppelte Empfängerin vorhanden ist, der/die dieselbe Adresse anspricht (d. h. E-Mail, Push), dedupliziert Braze die Nutzer:innen** – das bedeutet, Braze entfernt identische Nutzer:innen und behält nur eine Person bei.

Wenn Sie beispielsweise dieselbe `external_user_id` verwenden, erhält die nutzende Person nur eine Nachricht. Erwägen Sie mehrere API-Aufrufe, wenn Sie dieses Verhalten umgehen müssen.

Wenn dieselbe `external_user_id` mehrmals im Empfänger:innen-Array vorkommt, sendet Braze nur eine Nachricht und verwendet die Trigger-Eigenschaften aus dem letzten Vorkommen im Array. Dieses Verhalten ist deterministisch und basiert auf der Reihenfolge im Array.

Im folgenden Beispiel erhält `userid1` eine Nachricht mit `"name": "Beth Test 2"`, da dieser Eintrag als letzter im Array steht.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
