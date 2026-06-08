---
nav_title: "PUT : Remplacer une ressource dans la bibliothèque multimédia"
article_title: "PUT : Remplacer une ressource dans la bibliothèque multimédia"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint `PUT /media_library/replace_file`."
---

{% api %}
# Remplacer une ressource dans la bibliothèque multimédia {#replace-an-asset-in-the-media-library}
{% apimethod put %}
/media_library/replace_file
{% endapimethod %}

> Utilisez cet endpoint pour remplacer le fichier d'une ressource existante dans la [bibliothèque multimédia de Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) tout en conservant son ID et son URL. Vous pouvez fournir le fichier de remplacement à l'aide d'une URL hébergée en externe (`asset_url`) ou de données de fichier binaire envoyées dans le corps de la requête (`asset_file`).

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec la permission `media_library.replace`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## Corps de la requête {#request-body}

Lorsque vous incluez `asset_url`, l'endpoint télécharge le fichier depuis l'URL. Lorsque vous incluez `asset_file`, l'endpoint utilise les données binaires dans le corps de la requête.

Exemple de corps de requête pour `asset_url` :

```json
{
  "asset_id": "your-asset-id",
  "asset_url": "https://cdn.example.com/assets/cat.jpg"
}
```

Exemple de corps de requête pour `asset_file` :

```json
{
  "asset_id": "your-asset-id",
  "asset_file": <BINARY FILE DATA>
}
```

Le corps de la requête inclut les paramètres suivants :

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `asset_id` | Requis | Chaîne de caractères | L'ID de la ressource à remplacer. |
| `asset_url` | Facultatif | Chaîne de caractères | Une URL accessible publiquement pour le fichier de remplacement. |
| `asset_file` | Facultatif | Binaire | Données de fichier binaire pour le fichier de remplacement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request body" }

{% alert important %}
`asset_url` et `asset_file` sont mutuellement exclusifs : vous ne devez en inclure qu'un seul dans votre requête API.
{% endalert %}

### Exigences relatives au fichier de remplacement {#replacement-file-requirements}

- L'extension du fichier de remplacement doit correspondre exactement à l'extension de la ressource existante. Par exemple, vous ne pouvez pas remplacer une ressource `.png` par un fichier `.jpg`.
- Le remplacement de fichier est pris en charge pour les images, les SVG, les documents, les polices, les cartes de contact et les fichiers de code. Les ressources vidéo ne peuvent pas être remplacées.

## Exemple de requête {#example-request}

Cette section comprend deux exemples de requêtes `curl` : l'une pour remplacer une ressource à l'aide d'une URL et l'autre à l'aide de données de fichier binaire.

Cette requête montre un exemple de remplacement d'une ressource dans la bibliothèque multimédia à l'aide d'un `asset_url`.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_url": "https://cdn.example.com/assets/cat.jpg"}'
```

Cette requête montre un exemple de remplacement d'une ressource dans la bibliothèque multimédia à l'aide d'un `asset_file`.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_file":<BINARY FILE DATA>}'
```

### Réponses d'erreur {#error-responses}

Cette section répertorie les erreurs potentielles ainsi que leurs messages et descriptions correspondants.

#### Erreurs de validation {#validation-errors}

Les erreurs de validation renvoient une structure comme celle-ci :

```json
{
  "message": (String) Human-readable error description
}
```

Ce tableau répertorie les erreurs de validation possibles.

| État HTTP | Message | Description |
| --- | --- | --- |
| 400 | "asset_id is required." | Aucun ID de ressource n'a été fourni dans la requête. |
| 400 | "Either file or asset_url is required." | Ni `asset_file` ni `asset_url` n'a été fourni ; l'un des deux est requis. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Validation errors" }

#### Erreurs de traitement {#processing-errors}

Les erreurs de traitement renvoient une réponse différente avec des codes d'erreur :

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

Ce tableau répertorie les erreurs de traitement possibles.

| Code d'erreur | État HTTP | Description |
| --- | --- | --- |
| `ASSET_NOT_FOUND` | 404 | Aucune ressource avec l'`asset_id` donné n'existe dans cet espace de travail. L'objet `meta` inclut `asset_id`. |
| `INVALID_ASSET_URL` | 400 | La valeur `asset_url` n'est pas un URI valide. L'objet `meta` inclut `asset_url`. |
| `EXTENSION_MISMATCH` | 400 | L'extension du fichier de remplacement ne correspond pas à l'extension de la ressource existante. L'objet `meta` inclut `expected_extension` et `received_extension`. |
| `UNSUPPORTED_ASSET_TYPE_FOR_REPLACE` | 400 | Le remplacement de fichier n'est pas pris en charge pour ce type de ressource (par exemple, vidéo). L'objet `meta` inclut `asset_type`. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | Le fichier dépasse la taille maximale autorisée. L'objet `meta` inclut `size_limit_bytes` et `file_size_bytes`. |
| `CORRUPT_FILE` | 400 | Le fichier image est corrompu ou illisible. L'objet `meta` inclut `file_name`. |
| `GENERIC_ERROR` | 500 | Une erreur inattendue s'est produite lors du remplacement du fichier. L'objet `meta` inclut `original_error` pour le débogage. Réessayez ou contactez l'[Assistance]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Processing errors" }

## Réponse {#response}

Il existe cinq codes de statut de réponse pour cet endpoint : `200`, `400`, `404`, `429` et `500`.

Le JSON suivant montre la structure attendue de la réponse.

```json
{
  "info": "Asset file updated successfully.",
  "new_image_asset": {
    "name": (String) the name of the asset,
    "size": (Integer) the byte size of the asset,
    "url": (String) the URL to access the asset,
    "ext": (String) the file extension (e.g., "png", "jpg", "gif")
  }
}
```

{% endapi %}