---
nav_title: "GET : Rechercher un compte utilisateur de tableau de bord existant par e-mail"
article_title: "GET : Rechercher un compte utilisateur de tableau de bord existant par e-mail"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze permettant de rechercher un compte utilisateur du tableau de bord existant par e-mail."
---

{% api %}
# Rechercher un compte utilisateur de tableau de bord existant par e-mail {#search-existing-dashboard-user-account-by-email}
{% apimethod get %}
scim/v2/Users?filter=userName%20eq%20"user%40test.com"
{% endapimethod %}

> Utilisez cet endpoint pour rechercher un compte utilisateur de tableau de bord existant en spécifiant son e-mail dans le paramètre de requête du filtre.

Notez que lorsque le paramètre de requête est encodé en URL, il s'affiche ainsi :

`/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'un jeton SCIM. Vous utiliserez l'origine de votre service comme en-tête `X-Request-Origin`. Pour plus d'informations, consultez la section [Provisionnement automatisé des utilisateurs]({{site.baseurl}}/scim/automated_user_provisioning).

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## Paramètres de requête {#query-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `filter` | Requis | Chaîne de caractères | Expression de filtre SCIM pour la recherche par e-mail. Braze ne prend en charge que `userName eq "user@example.com"`. La valeur de l'e-mail doit être encadrée par des guillemets doubles. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

{% alert important %}
Braze ne prend en charge que les filtres de correspondance exacte sur `userName` avec l'opérateur `eq`. Les autres champs ou opérateurs de filtre SCIM renvoient une réponse `400`.
{% endalert %}

## Paramètres de la requête {#request-parameters}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
Si vous recevez une réponse `401`, vérifiez que vous utilisez un jeton SCIM (et non une clé API REST), que `X-Request-Origin` correspond à l'origine de votre service et que votre adresse IP figure sur la liste d'autorisation SCIM. Pour plus de détails, consultez la section [Provisionnement automatisé des utilisateurs]({{site.baseurl}}/scim/automated_user_provisioning).
{% endalert %}

## Exemple de requête {#example-request}
```bash
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Réponse {#response}
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

## Paramètres de réponse {#response-parameters}

| Paramètre | Type de données | Description |
|---|---|---|
| `schemas` | Tableau de chaînes de caractères | Schéma de réponse de liste SCIM. |
| `totalResults` | Entier | Nombre d'utilisateurs du tableau de bord correspondants (0 si aucune correspondance). |
| `Resources` | Tableau | Tableau d'objets utilisateur. Chaque objet utilise les mêmes champs que [GET : Consulter un compte utilisateur de tableau de bord existant]({{site.baseurl}}/get_see_user_account_information). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paramètres de réponse" }

### Champs de l'objet utilisateur {#user-object-fields}

| Paramètre | Type de données | Description |
|---|---|---|
| `id` | Chaîne de caractères | L'ID de ressource de l'utilisateur. |
| `userName` | Chaîne de caractères | L'adresse e-mail de l'utilisateur. |
| `name` | Objet | Contient `givenName` et `familyName`. |
| `department` | Chaîne de caractères | Le département de l'utilisateur, s'il est défini. |
| `createdAt` | Chaîne de caractères | Date de création du compte utilisateur. Renvoie `N/A` si non définie ; sinon formatée comme `YYYY Mon DD, H:MM AM/PM`. |
| `lastSignInAt` | Chaîne de caractères | Date de la dernière connexion de l'utilisateur. Renvoie `N/A` si l'utilisateur ne s'est jamais connecté ; sinon formatée comme `YYYY Mon DD, H:MM AM/PM`. |
| `permissions` | Objet | Autorisations de l'entreprise, de l'espace de travail, de l'équipe et des rôles. Consultez l'[objet des autorisations]({{site.baseurl}}/scim_api_appendix). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Champs de l'objet utilisateur" }

### États d'erreur {#error-states}

Si le paramètre `filter` est manquant ou mal formé, l'endpoint renvoie :

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