---
nav_title: "GET : Lister les applications de l'espace de travail"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "Cet article présente les détails de l'endpoint Braze permettant de lister les applications de l'espace de travail."
---
{% api %}
# Lister les applications de l'espace de travail {#list-workspace-apps}
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> Utilisez cet endpoint pour lister le nom et l'identifiant unique (`api_key`) des applications d'un espace de travail.

L'appel de cet endpoint renvoie un tableau d'objets appelé `apps`. Chaque objet dans `apps` contient le nom et l'identifiant unique de l'application.

{% apiref postman %}  {% endapiref %}

## Limite de débit {#rate-limit}

Cet endpoint a une limite de débit de 100 requêtes par jour (24 heures).

## Paramètres de la requête {#request-parameters}

Cette requête ne prend aucun paramètre.

## Exemple de requête {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse {#response}

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

### Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `401: Unauthorized` | La clé API ne dispose pas des autorisations requises. Assurez-vous que votre clé API dispose des autorisations `apps.get`. |
| `403: Forbidden` | Le feature flipper n'est pas activé pour cette société. Contactez votre gestionnaire de la satisfaction client pour obtenir de l'aide. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}