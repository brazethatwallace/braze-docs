---
nav_title: "GET: Ein bestehendes Dashboard-Nutzerkonto suchen"
article_title: "GET: Ein bestehendes Dashboard-Nutzerkonto suchen"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts zum Suchen eines bestehenden Dashboard-Nutzerkontos anhand der Ressourcen-ID."
---

{% api %}
# Ein bestehendes Dashboard-Nutzerkonto anhand der Ressourcen-ID suchen {#look-up-an-existing-dashboard-user-account-by-resource-id}
{% apimethod get %}
/scim/v2/Users/{id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein bestehendes Dashboard-Nutzerkonto zu suchen, indem Sie die Ressource `id` angeben, die von der SCIM-Methode [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account) zurückgegeben wird.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie ein SCIM-Token. Verwenden Sie Ihre Dienst-Herkunft als `X-Request-Origin`-Header. Weitere Informationen finden Sie unter [Automatisierte Nutzerbereitstellung]({{site.baseurl}}/scim/automated_user_provisioning).

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## Pfad-Parameter {#path-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `id` | Erforderlich | String | Die Ressourcen-ID der Nutzer:in. Dieser Parameter wird von den Methoden `POST` `/scim/v2/Users/` oder `GET` `/scim/v2/Users?filter=userName eq "user@example.com"` zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfad-Parameter" }

## Anfrage-Body {#request-body}
```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## Beispielanfrage {#example-request}
```bash
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## Antwort {#response}
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "dfa245b7-24195aec-887bb3ad-602b3340",
    "userName": "user@example.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "Thursday, January 1, 1970 12:00:00 AM",
    "createdAt": "Thursday, January 1, 1970 12:00:00 AM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Another Test Role",
                "roleId": "23125dad23dfaae7",
                "appGroup": [
                    {
                        "appGroupId": "241adcd25adfabcded",
                        "appGroupName": "Production Workspace",
                        "appGroupPermissionSets": [
                            {
                                "appGroupPermissionSetName": "A Permission Set",
                                "appGroupPermissionSetId": "dfa385109bc38",
                                "permissions": ["basic_access","publish_cards"]
                            }
                        ]
                    }
                ]
            }
        ],
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
```

{% endapi %}