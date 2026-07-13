---
nav_title: "GET : Lister les détails de plusieurs produits du catalogue"
article_title: "GET : Lister les détails de plusieurs produits du catalogue"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Lister les détails de plusieurs produits du catalogue."

---
{% api %}
# Lister les détails de plusieurs produits du catalogue {#list-multiple-catalog-item-details}
{% apimethod get %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utilisez cet endpoint pour retourner plusieurs produits du catalogue et leur contenu.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#63a19dd5-10e0-4649-bdf0-097216748bbb {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `catalogs.get_items`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Paramètres de chemin {#path-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | Chaîne de caractères | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin" }

## Paramètres de requête {#query-parameters}

Notez que chaque appel à cet endpoint retournera 50 produits. Pour un catalogue comportant plus de 50 produits, utilisez l'en-tête `Link` pour récupérer les données de la page suivante, comme indiqué dans l'exemple de réponse ci-dessous.

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `cursor` | Facultatif | Chaîne de caractères | Détermine la pagination des produits du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Paramètres de demande {#request-parameters}

Cet endpoint n'a pas de corps de demande.

## Exemples de requêtes {#example-requests}

### Sans curseur {#without-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Avec curseur {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse {#response}

Trois codes de statut de réponse existent pour cet endpoint : `200`, `400` et `404`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait retourner l'en-tête et le corps de réponse suivants.

{% alert note %}
L'en-tête `Link` n'existera pas si le catalogue possède 50 produits ou moins. Pour les appels sans curseur, `prev` ne s'affichera pas. Lors de la consultation de la dernière page de produits, `next` ne s'affichera pas.
{% endalert %}

```
Link: </catalogs/all_restaurants/items?cursor=c2tpcDow>; rel="prev",</catalogs/all_restaurants/items?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": false,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### Exemple de réponse échouée {#example-error-response}

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la section [Résolution des problèmes](#troubleshooting) pour plus d'informations concernant les erreurs que vous pourriez rencontrer.

```json
{
  "errors": [
    {
      "id": "invalid-cursor",
      "message": "'cursor' is not valid",
      "parameters": [
        "cursor"
      ],
      "parameter_values": [
        "bad-cursor"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `invalid-cursor` | Vérifiez que votre `cursor` est valide. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

{% endapi %}