---
nav_title: "POST : Créer des champs de catalogue"
article_title: "POST : Créer des champs de catalogue"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze Créer des champs de catalogue."

---
{% api %}
# Créer des champs de catalogue {#create-catalog-fields}
{% apimethod post %}
/catalogs/{catalog_name}/fields
{% endapimethod %}

> Utilisez cet endpoint pour créer plusieurs champs dans votre catalogue.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `catalogs.create_fields`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## Paramètres de chemin {#path-parameters}

| Paramètre      | Requis | Type de données | Description          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Requis | Chaîne de caractères    | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin" }

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description                                                                                                  |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `fields`  | Requis | Tableau     | Un tableau contenant des objets de champ. Les objets de champ doivent contenir le nom et le type des nouveaux champs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "fields": [
    {
      "name": "Name",
      "type": "string"
    },
    {
      "name": "Ratings",
      "type": "number"
    },
    {
      "name": "Loyalty_Program",
      "type": "boolean"
    },
    {
      "name": "Created_At",
      "type": "time"
    },
    {
      "name": "Location",
      "type": "geo"
    }
  ]
}'
```

{% alert note %}
Vous devez fournir les valeurs des champs de géolocalisation sous forme de tableau `[longitude, latitude]`, par exemple `[-73.988103, 40.779109]`. La latitude doit être comprise entre -90 et 90 ; la longitude doit être comprise entre -180 et 180.
{% endalert %}

## Réponse {#response}

Trois codes de statut sont possibles pour cet endpoint : `202`, `400` et `404`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `202` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse en erreur {#example-error-response}

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la section [Résolution des problèmes](#troubleshooting) pour plus d'informations sur les erreurs que vous pourriez rencontrer.

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées.

| Erreur                                | Résolution                                                                                        |
|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `arbitrary-error`                    | Une erreur arbitraire est survenue. Veuillez réessayer ou contacter l'[assistance]({{site.baseurl}}/support_contact). |
| `catalog-not-found`                  | Vérifiez que le nom du catalogue est valide.                                                                  |
| `company-size-limit-already-reached` | La limite de taille de stockage du catalogue est atteinte.                                                             |
| `request-includes-too-many-fields`   | Chaque requête peut contenir jusqu'à 50 nouveaux champs.                                                          |
| `catalog-exceeds-fields-limit`       | Le catalogue ne peut pas comporter plus de 500 champs.                                                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

{% endapi %}