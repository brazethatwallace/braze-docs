---
nav_title: "DELETE: Dashboard-Nutzerkonto entfernen"
article_title: "DELETE: Dashboard-Nutzerkonto entfernen"
alias: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Braze-Endpunkt zum Entfernen eines Dashboard-Nutzerkontos."
---

{% api %}
# Dashboard-Nutzerkonto entfernen {#remove-dashboard-user-account}
{% apimethod delete %}
/scim/v2/Users/{id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine:n bestehende:n Dashboard-Nutzer:in dauerhaft zu löschen, indem Sie die Ressourcen-`id` angeben, die von der SCIM-Methode [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account) zurückgegeben wird.

Dies ist vergleichbar mit dem Löschen von Nutzer:innen im Bereich **Unternehmensnutzer:innen** des Braze-Dashboards.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9c7c71ea-afd6-414a-99d1-4eb1fe274f16 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie ein SCIM-Token. Verwenden Sie die Herkunft Ihres Dienstes als `X-Request-Origin`-Header. Weitere Informationen finden Sie unter [Automatisierte Nutzerbereitstellung]({{site.baseurl}}/scim/automated_user_provisioning).

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='delete dashboard user' %}

## Pfadparameter {#path-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `id` | Erforderlich | String | Die Ressourcen-ID der/des Nutzer:in. Dieser Parameter wird von den Methoden `POST` `/scim/v2/Users/` oder `GET` `/scim/v2/Users?filter=userName eq "user@example.com"` zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter" }

## Anfragekörper {#request-body}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

## Beispielanfrage {#example-request}
```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Antwort {#response}

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Wenn die/der Nutzer:in dauerhaft gelöscht wurde, gibt der Endpunkt Folgendes zurück:

```http
HTTP/1.1 204 No Content
```

### Beispiele für Fehlerantworten {#example-error-responses}

Wenn ein:e Entwickler:in mit dieser ID nicht in Braze existiert, antwortet der Endpunkt mit:
```http
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "User not found",
    "status": 404
}
```

Wenn Sie versuchen, die/den letzte:n verbleibende:n Unternehmensnutzer:in zu löschen, gibt der Endpunkt eine `500 Internal Server Error`-Antwort zurück und löscht die/den Nutzer:in nicht:

```http
HTTP/1.1 500 Internal Server Error
Content-Type: application/json

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "Failed to delete user",
    "status": 500
}
```

{% endapi %}