---
nav_title: "GET : Exporter des attributs personnalisés"
article_title: "GET : Exporter des attributs personnalisés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze Exporter des attributs personnalisés."

---
{% api %}
# Exporter des attributs personnalisés {#export-custom-attributes}
{% apimethod get %}
/custom_attributes
{% endapimethod %}

> Utilisez cet endpoint pour exporter une liste d'attributs personnalisés enregistrés pour votre application. Les attributs sont renvoyés par groupes de 50, triés par ordre alphabétique.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `custom_attributes.get`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='custom_attributes' %}

## Paramètres de requête {#query-parameters}

Notez que chaque appel à cet endpoint renverra 50 attributs. Pour plus de 50 attributs, utilisez l'en-tête `Link` pour récupérer les données de la page suivante, comme le montre l'exemple de réponse suivant.

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `cursor` | Facultatif | Chaîne de caractères | Détermine la pagination des attributs personnalisés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemples de requêtes {#example-requests}

### Sans curseur {#without-cursor}

```
curl --location --request GET 'https://rest.iad-01.braze.com/custom_attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Avec curseur {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/custom_attributes?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "attributes" : [
        {
            "array_length": 100, (number) the maximum array length, or null if not applicable,
            "data_type": "Number", (string) the data type,
            "description": "The attribute description", (string) the attribute description,
            "name": "The attribute name", (string) the attribute name,
            "status": "Active", (string) the attribute status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the attribute formatted as strings,
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