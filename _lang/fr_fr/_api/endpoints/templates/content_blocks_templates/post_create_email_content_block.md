---
nav_title: "POST : Créer un bloc de contenu"
article_title: "POST : Créer un bloc de contenu"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Créer des Content Blocks."

---
{% api %}
# Créer un bloc de contenu {#create-content-block}
{% apimethod post %}
/content_blocks/create
{% endapimethod %}

> Utilisez cet endpoint pour créer un [bloc de contenu]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks).

{% alert tip %}
Vous pouvez également appeler cet endpoint via le [serveur MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) en utilisant la fonction [`create_content_block`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#content-blocks). Cela permet à des outils d'intelligence artificielle comme Claude et Cursor de créer des blocs de contenu via des requêtes en langage naturel.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f1cefa8b-7a28-4e64-b579-198a4610d0a5 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key) avec l'autorisation `content_blocks.create`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "name": (required, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (required, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `name` | Requis | Chaîne de caractères | Nom du bloc de contenu. Doit contenir moins de 100 caractères. |
| `description` | Facultatif | Chaîne de caractères | Description du bloc de contenu. Doit contenir moins de 250 caractères. |
| `content` | Requis | Chaîne de caractères | Contenu HTML ou texte dans le bloc de contenu. |
| `state` | Facultatif | Chaîne de caractères | Choisissez `active` ou `draft`. Défini par défaut sur `active` si non spécifié. |
| `tags` | Facultatif | Tableau de chaînes de caractères | Les [étiquettes]({{site.baseurl}}/user_guide/messaging/governance/tags) doivent déjà exister. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
```bash
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## Réponse {#response}

```json
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `Content cannot be blank` | |
| `Content must be a string` | Assurez-vous que votre contenu est encadré par des guillemets (`""`). |
| `Content must be smaller than 50kb` | Le contenu de votre bloc de contenu doit être inférieur à 50 Ko au total. |
| `Content contains malformed liquid` | Le Liquid fourni n'est pas valide ou analysable. Réessayez avec du Liquid valide ou contactez l'assistance. |
| `Content Block cannot be referenced within itself` | |
| `Content Block description cannot be blank` | |
| `Content Block description must be a string` | Assurez-vous que la description de votre bloc de contenu est encadrée par des guillemets (`""`). |
| `Content Block description must be shorter than 250 characters` | |
| `Content Block name cannot be blank` | |
| `Content Block name must be shorter than 100 characters` | |
| `Content Block name can only contain alphanumeric characters` | Les noms de bloc de contenu peuvent comprendre l'un des caractères suivants : les lettres (majuscules ou minuscules) de `A` à `Z`, les chiffres de `0` à `9`, les tirets `-` et les traits de soulignement `_`. Ils ne peuvent pas contenir de caractères non alphanumériques comme des émojis, `!`, `@`, `~`, `&` et d'autres caractères « spéciaux ». |
| `Content Block with this name already exists` | Essayez un autre nom. |
| `Content Block state must be either active or draft` | |
| `Tags must be an array` | Les étiquettes doivent être formatées sous forme de tableau de chaînes de caractères, par exemple `["marketing", "promotional", "transactional"]`. | |
| `All tags must be strings` | Assurez-vous que vos étiquettes sont encadrées par des guillemets (`""`). |
| `Some tags could not be found` | Pour ajouter une étiquette lors de la création d'un bloc de contenu, l'étiquette doit déjà exister dans Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }


{% endapi %}