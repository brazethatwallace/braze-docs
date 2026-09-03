---
nav_title: "POST: Nutzer-Alias aktualisieren"
article_title: "POST: Nutzer-Alias aktualisieren"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Nutzer-Aliase aktualisieren“."
---
{% api %}
# Nutzer-Alias aktualisieren {#update-user-alias}
{% apimethod post %}
/users/alias/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um bestehende Nutzer-Aliase zu aktualisieren.

Pro Anfrage können bis zu 50 Nutzer-Aliase angegeben werden.

Um einen Nutzer-Alias zu aktualisieren, müssen `alias_label`, `old_alias_name` und `new_alias_name` im Objekt „Nutzer-Alias aktualisieren“ enthalten sein. Wenn kein Nutzer-Alias mit `alias_label` und `old_alias_name` verknüpft ist, wird kein Alias aktualisiert. Wenn die angegebenen `alias_label` und `old_alias_name` gefunden werden, wird `old_alias_name` auf `new_alias_name` aktualisiert.

{% alert note %}
Dieser Endpunkt garantiert nicht die Reihenfolge, in der die `alias_updates`-Objekte aktualisiert werden.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key) mit der Berechtigung `users.alias.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | Erforderlich | Array von Nutzer-Alias-Aktualisierungsobjekten | Siehe [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object).<br><br> Weitere Informationen zu `old_alias_name`, `new_alias_name` und `alias_label` finden Sie unter [Nutzer-Aliase]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

### Anfragetext des Endpunkts mit Spezifikation des Nutzer-Alias-Aktualisierungsobjekts {#endpoint-request-body-with-update-user-alias-object-specification}

```json
{
  "alias_label" : (required, string),
  "old_alias_name" : (required, string),
  "new_alias_name" : (required, string)
}
```

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

{% endapi %}