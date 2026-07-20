---
nav_title: "GET : Exporter des événements personnalisés"
article_title: "GET : Exporter des événements personnalisés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze Exporter des événements personnalisés."

---
{% api %}
# Exporter des événements personnalisés {#export-custom-events}
{% apimethod get %}
/events
{% endapimethod %}

> Utilisez cet endpoint pour exporter une liste d'événements personnalisés enregistrés pour votre application. Les événements sont renvoyés par groupes de 50, triés par ordre alphabétique.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `events.get`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='events' %}

## Paramètres de requête {#query-parameters}

Notez que chaque appel à cet endpoint renverra 50 événements. Pour plus de 50 événements, utilisez l'en-tête `Link` pour récupérer les données de la page suivante, comme le montre l'exemple de réponse suivant.

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `cursor` | Facultatif | Chaîne de caractères | Détermine la pagination des événements personnalisés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemples de requêtes {#example-requests}

### Sans curseur {#without-cursor}

```
curl --location --request GET 'https://rest.iad-01.braze.com/events' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Avec curseur {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/events?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        {
            "name": "The event name", (string) the event name,
            "description": "The event description", (string) the event description,
            "included_in_analytics_report": false, (boolean) the analytics report inclusion,
            "status": "Active", (string) the event status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the event formatted as strings,
        },
        ...
    ]
}
```

### Codes de réponse des erreurs fatales {#fatal-export}

Pour connaître les codes d'état et les messages d'erreur associés qui seront renvoyés si votre requête rencontre une erreur fatale, reportez-vous à la section [Erreurs fatales]({{site.baseurl}}/api/errors#fatal-errors).

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}