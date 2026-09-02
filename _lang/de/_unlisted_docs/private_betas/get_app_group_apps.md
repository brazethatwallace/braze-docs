---
nav_title: "GET: Workspace-Apps auflisten"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Workspace-Apps auflisten“."
---
{% api %}
# Workspace-Apps auflisten {#list-workspace-apps}
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Namen und den eindeutigen Bezeichner (`api_key`) für Apps in einem Workspace aufzulisten.

Der Aufruf dieses Endpunkts gibt ein Objekt-Array namens `apps` zurück. Jedes Objekt in `apps` enthält den Namen und den eindeutigen Bezeichner für die App.

{% apiref postman %}  {% endapiref %}

## Rate-Limits {#rate-limit}

Dieser Endpunkt hat ein Rate-Limit von 100 Anfragen pro Tag (24 Stunden).

## Anfrageparameter {#request-parameters}

Diese Anfrage nimmt keine Parameter entgegen.

## Beispielanfrage {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Antwort {#response}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### Fehlerbehebung {#troubleshooting}

Die folgende Tabelle listet mögliche zurückgegebene Fehler und die zugehörigen Schritte zur Fehlerbehebung auf.

| Fehler | Fehlerbehebung |
| --- | --- |
| `401: Unauthorized` | Der API-Schlüssel verfügt nicht über die erforderlichen Berechtigungen. Stellen Sie sicher, dass Ihr API-Schlüssel über die Berechtigung `apps.get` verfügt. |
| `403: Forbidden` | Der Feature-Flipper ist für dieses Unternehmen nicht aktiviert. Wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in, um Unterstützung zu erhalten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}