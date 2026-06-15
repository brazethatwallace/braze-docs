---
nav_title: "POST: Neuen Nutzer-Alias erstellen"
article_title: "POST: Neuen Nutzer-Alias erstellen"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Neuen Nutzer-Alias erstellen“."

---
{% api %}
# Neuen Nutzer-Alias erstellen {#create-new-user-alias}
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um neue Nutzer-Aliase für bestehende identifizierte Nutzer:innen hinzuzufügen oder um neue nicht identifizierte Nutzer:innen zu erstellen.

Pro Anfrage können bis zu 50 Nutzer-Aliase angegeben werden.

**Um einen Nutzer-Alias für bestehende Nutzer:innen hinzuzufügen**, muss eine `external_id` im neuen Nutzer-Alias-Objekt enthalten sein. Wenn die `external_id` im Objekt vorhanden ist, es aber keine Nutzer:innen mit dieser `external_id` gibt, wird der Alias keinen Nutzer:innen hinzugefügt. Wenn keine `external_id` vorhanden ist, werden Nutzer:innen trotzdem erstellt, müssen aber später identifiziert werden. Dazu können Sie den Endpunkt „Nutzer:innen identifizieren“ und den Endpunkt `users/identify` verwenden.

**Um neue Nutzer:innen zu erstellen, die nur über einen Alias verfügen**, muss die `external_id` im neuen Nutzer-Alias-Objekt weggelassen werden. Nachdem die Nutzer:innen erstellt wurden, verwenden Sie den Endpunkt `/users/track`, um die Alias-Nutzer:innen mit Attributen, Ereignissen und Käufen zu verknüpfen, und den Endpunkt `/users/identify`, um die Nutzer:innen mit einer `external_id` zu identifizieren.

## Wenn `alias_label` und `alias_name` bereits existieren {#when-alias_label-and-alias_name-already-exist}

Die Kombination aus `alias_label` und `alias_name` muss in Ihrer Nutzerbasis eindeutig sein. Weitere Informationen finden Sie unter [Nutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

Wenn Sie eine Anfrage senden, bei der das Paar aus `alias_label` und `alias_name` bereits für Nutzer:innen existiert (ob bei denselben oder anderen Nutzer:innen), gibt der Endpunkt trotzdem eine erfolgreiche Antwort zurück (z. B. `"aliases_processed": 1`, `"message": "success"`). In diesem Fall wird den Nutzer:innen in der Anfrage kein neuer Alias hinzugefügt. Da das Paar aus `alias_label` und `alias_name` bereits verwendet wird, nimmt die Anfrage keine Änderungen vor, und es kann so aussehen, als ob der Alias den betreffenden Nutzer:innen nie hinzugefügt wurde.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.alias.new`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Erforderlich | Array mit neuen Nutzer-Alias-Objekten | Siehe [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Weitere Informationen zu `alias_name` und `alias_label` finden Sie in unserer Dokumentation zu [Nutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Anfragetext des Endpunkts mit Spezifikation des neuen Nutzer-Alias-Objekts {#endpoint-request-body-with-new-user-alias-object-specification}

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## Antwort {#response}

Wenn ein Alias übersprungen wird, weil dieselbe Kombination aus `alias_label` und `alias_name` bereits für Nutzer:innen existiert, kann der Antworttext trotzdem Erfolg anzeigen. Weitere Details finden Sie unter [Wenn Alias-Label und -Name bereits existieren](#when-the-alias-label-and-name-already-exist).

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```


{% endapi %}