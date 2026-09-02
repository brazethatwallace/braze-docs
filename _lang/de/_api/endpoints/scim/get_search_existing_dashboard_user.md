---
nav_title: "GET: Bestehendes Dashboard-Nutzerkonto per E-Mail durchsuchen"
article_title: "GET: Bestehendes Dashboard-Nutzerkonto per E-Mail durchsuchen"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Braze-Endpunkt zum Durchsuchen eines bestehenden Dashboard-Nutzerkontos per E-Mail."
---

{% api %}
# Bestehendes Dashboard-Nutzerkonto per E-Mail durchsuchen {#search-existing-dashboard-user-account-by-email}
{% apimethod get %}
scim/v2/Users?filter=userName%20eq%20"user%40test.com"
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein bestehendes Dashboard-Nutzerkonto zu suchen, indem Sie die E-Mail-Adresse im Filter-Abfrageparameter angeben.

Beachten Sie, dass der Abfrageparameter in URL-kodierter Form wie folgt aussieht:

`/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie ein SCIM-Token / Textbaustein. Verwenden Sie die Herkunft Ihres Dienstes als `X-Request-Origin`-Header. Weitere Informationen finden Sie unter [Automatisierte Bereitstellung von Nutzer:innen]({{site.baseurl}}/scim/automated_user_provisioning).

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## Abfrageparameter {#query-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `filter` | Erforderlich | String | SCIM-Filterausdruck zur Suche per E-Mail. Braze unterstützt ausschließlich `userName eq "user@example.com"`. Der E-Mail-Wert muss in doppelte Anführungszeichen eingeschlossen sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter" }

{% alert important %}
Braze unterstützt nur exakte Übereinstimmungsfilter auf `userName` mit dem Operator `eq`. Andere SCIM-Filterfelder oder -Operatoren geben eine `400`-Antwort zurück.
{% endalert %}

## Anfrageparameter {#request-parameters}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
Wenn Sie eine `401`-Antwort erhalten, überprüfen Sie, ob Sie ein SCIM-Token / Textbaustein (keinen Representational State Transfer-API-Schlüssel) verwenden, ob `X-Request-Origin` mit Ihrer Dienst-Herkunft übereinstimmt und ob Ihre IP-Adresse in der SCIM-Zulassungsliste enthalten ist. Weitere Informationen finden Sie unter [Automatisierte Bereitstellung von Nutzer:innen]({{site.baseurl}}/scim/automated_user_provisioning).
{% endalert %}

## Beispielanfrage {#example-request}
```bash
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Antwort {#response}
```json
{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
    "totalResults": 1,
    "Resources": [
        {
            "userName": "user@example.com",
            "id": "dfa245b7-24195aec-887bb3ad-602b3340",
            "name": {
                "givenName": "Test",
                "familyName": "User"
            },
            "department": "finance",
            "createdAt": "2024 Nov 11, 4:20 PM",
            "lastSignInAt": "N/A",
            "permissions": {
                "companyPermissions": ["manage_company_settings"],
                "appGroup": [
                    {
                        "appGroupId": "241adcd25789fabcded",
                        "appGroupName": "Test Workspace",
                        "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                        "team": [
                            {
                                "teamId": "241adcd25789fabcded",
                                "teamName": "Test Team",
                                "teamPermissions": ["admin"]
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

## Antwortparameter {#response-parameters}

| Parameter | Datentyp | Beschreibung |
|---|---|---|
| `schemas` | String-Array | SCIM-Listenantwortschema. |
| `totalResults` | Integer | Anzahl der übereinstimmenden Dashboard-Nutzer:innen (0, wenn keine Übereinstimmung). |
| `Resources` | Array | Array von Nutzerobjekten. Jedes Objekt verwendet dieselben Felder wie [GET: Bestehendes Dashboard-Nutzerkonto nachschlagen]({{site.baseurl}}/get_see_user_account_information). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Antwortparameter" }

### Felder des Nutzerobjekts {#user-object-fields}

| Parameter | Datentyp | Beschreibung |
|---|---|---|
| `id` | String | Die Ressourcen-ID der/des Nutzer:in. |
| `userName` | String | Die E-Mail-Adresse der/des Nutzer:in. |
| `name` | Object | Enthält `givenName` und `familyName`. |
| `department` | String | Die Abteilung der/des Nutzer:in, falls festgelegt. |
| `createdAt` | String | Zeitpunkt der Erstellung des Nutzerkontos. Gibt `N/A` zurück, wenn nicht festgelegt; ansonsten im Format `YYYY Mon DD, H:MM AM/PM`. |
| `lastSignInAt` | String | Zeitpunkt der letzten Anmeldung der/des Nutzer:in. Gibt `N/A` zurück, wenn sich die/der Nutzer:in noch nie angemeldet hat; ansonsten im Format `YYYY Mon DD, H:MM AM/PM`. |
| `permissions` | Object | Berechtigungen für Unternehmen, Workspace, Team und Rolle. Siehe das [Berechtigungsobjekt]({{site.baseurl}}/api/objects_filters/scim_api_appendix). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Felder des Nutzerobjekts" }

### Fehlerzustände {#error-states}

Wenn der `filter`-Parameter fehlt oder fehlerhaft ist, gibt der Endpunkt Folgendes zurück:

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "status": 400,
  "detail": "Request is unparsable, syntactically incorrect, or violates schema."
}
```

{% endapi %}