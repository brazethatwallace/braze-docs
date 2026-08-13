---
nav_title: "POST : Télécharger une ressource dans la bibliothèque multimédia"
article_title: "POST : Télécharger une ressource dans la bibliothèque multimédia"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article fournit des informations détaillées sur l'endpoint `POST /media_library/create`."
---

{% api %}
# Télécharger une ressource dans la bibliothèque multimédia {#upload-an-asset-to-the-media-library}
{% apimethod post %}
/media_library/create
{% endapimethod %}

> Utilisez cet endpoint pour ajouter une ressource à la [bibliothèque multimédia de Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) à l'aide d'une URL hébergée en externe (`asset_url`) ou de données de fichier binaire envoyées dans le corps de la requête (`asset_file`).

## Types de fichiers pris en charge {#supported-file-types}

Cet endpoint prend en charge les types de fichiers suivants :

| Type de fichier | Formats | Taille maximale | Remarques |
|-----------|---------|--------------|-------|
| Images | PNG, JPEG, GIF, SVG, WebP | 5 Mo | |
| Fichiers ZIP | .zip | 50 Mo au total ; 5 Mo par fichier dans le ZIP | Ne doit contenir que des images ou des SVG ; tous les fichiers doivent se trouver à la racine du ZIP (pas de sous-répertoires) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Types de fichiers pris en charge" }

{% alert note %}
Les fichiers de contact virtuels (.vcf) et les fichiers vidéo peuvent être téléchargés dans la bibliothèque multimédia, mais uniquement via l'interface du tableau de bord (**Content** > **Media Library**), et non via cet endpoint API.
{% endalert %}

{% alert tip %}
Vous pouvez également appeler cet endpoint via le [serveur MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) en utilisant la fonction [`create_media_library_asset`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#media-library). Cela permet à des outils d'IA comme Claude et Cursor de télécharger des ressources dans votre bibliothèque multimédia via des instructions en langage naturel.
{% endalert %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `media_library.create`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## Corps de la requête {#request-body}

Lorsque vous incluez `asset_url`, l'endpoint télécharge le fichier à partir de l'URL. Lorsque vous incluez `asset_file`, l'endpoint utilise les données binaires dans le corps de la requête.

Exemple de corps de requête pour `asset_url` :

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

Exemple de corps de requête pour `asset_file` :

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

Le corps de la requête comprend les paramètres suivants :

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `asset_url` | Facultatif | Chaîne de caractères | Une URL accessible au public pour la ressource à télécharger dans Braze. |
| `asset_file` | Facultatif | Binaire | Données de fichier binaire. |
| `name` | Facultatif | Chaîne de caractères | Un nom qui apparaîtra dans la bibliothèque multimédia pour cette ressource. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Corps de la requête" }

{% alert important %}
`asset_url` et `asset_file` sont mutuellement exclusifs : vous devez n'inclure qu'un seul d'entre eux dans votre requête API.
{% endalert %}

### Noms des fichiers téléchargés {#uploaded-file-names}

Cette section explique comment l'endpoint attribue des noms aux fichiers téléchargés selon que vous incluez ou non le paramètre `name`.

#### Téléchargements de fichiers individuels {#single-file-uploads}

| Scénario | Résultat |
| --- | --- |
| `name` fourni | La valeur `name` est utilisée comme nom de la ressource dans la bibliothèque multimédia. |
| `name` exclu | Le nom de fichier original provenant de l'URL ou du fichier téléchargé est utilisé. |
{: .reset-td-br-1 .reset-td-br-2 style="table-layout: fixed; width: 100%;" aria-label="Téléchargements de fichiers individuels" }

#### Téléchargements de fichiers ZIP {#zip-file-uploads}

| Scénario | Résultat |
| --- | --- |
| `name` fourni | La valeur `name` est utilisée comme préfixe, avec un numéro incrémentiel ajouté comme suffixe (par exemple, « Mon fichier 1 », « Mon fichier 2 », « Mon fichier 3 »). |
| `name` exclu | Chaque fichier conserve son nom d'origine tel qu'il figurait dans le fichier ZIP. |
{: .reset-td-br-1 .reset-td-br-2 style="table-layout: fixed; width: 100%;" aria-label="Téléchargements de fichiers ZIP" }

## Exemple de requête {#example-request}

Cette section comprend deux exemples de requêtes `curl`, l'une pour ajouter une ressource à l'aide d'une URL et l'autre à l'aide de données de fichier binaire.

Cette requête illustre l'ajout d'une ressource à la bibliothèque multimédia à l'aide d'un `asset_url`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

Cette requête illustre l'ajout d'une ressource à la bibliothèque multimédia à l'aide d'un `asset_file`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### Réponses d'erreur {#error-responses}

Cette section répertorie les erreurs potentielles ainsi que les messages et descriptions correspondants.

#### Erreurs de validation {#validation-errors}

Les erreurs de validation renvoient une structure telle que celle-ci :

```json
{
  "message": (String) Human-readable error description
}
```

Ce tableau répertorie les erreurs de validation possibles.

| Statut HTTP | Message | Description |
| --- | --- | --- |
| 400 | "Either asset_url or asset_file must be provided." | Aucun paramètre de ressource n'a été fourni dans la requête. |
| 400 | "Both asset_url and asset_file cannot be provided. Please provide only one." | Les deux paramètres de ressource ont été fournis ; un seul est autorisé. |
| 403 | "Media Library Public APIs are not enabled for this company." | La fonctionnalité de bibliothèque multimédia n'est pas activée pour cet espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs de validation" }

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

| Code d'erreur | Statut HTTP | Description |
| --- | --- | --- |
| `UNSUPPORTED_FILE_TYPE` | 400 | Le type de fichier téléchargé n'est pas pris en charge. L'objet `meta` contient le `file_type` qui a été rejeté. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | Le fichier dépasse la taille maximale autorisée. Les images sont limitées à 5 Mo. |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | L'espace de travail a atteint son nombre maximal de ressources (200 par défaut pour les entreprises en essai gratuit, illimité dans les autres cas). L'objet `meta` inclut la `limit` actuelle. |
| `ASSET_UPLOAD_FAILED` | 400 | Le téléchargement de la ressource a échoué en raison de problèmes de traitement. |
| `INVALID_ASSET_URL` | 400 | La valeur `asset_url` n'est pas un URI valide. L'objet `meta` contient `asset_url`. |
| `ZIP_UPLOAD_ERROR` | 400 | Le fichier ZIP est endommagé ou n'a pas pu être ouvert. L'objet `meta` contient le message `original_error`. |
| `ZIP_FILE_TOO_LARGE` | 400 | La taille totale non compressée du fichier ZIP dépasse la limite de 5 Mo. L'objet `meta` comprend le `zip_file_name` et le `zip_file_size`. |
| `ZIPPED_ENTITY_HAS_NO_NAME` | 400 | Une entrée de fichier à l'intérieur du ZIP n'a pas de nom. Assurez-vous que le fichier ZIP n'est pas endommagé et attribuez un nom à toute entrée de fichier sans nom. |
| `ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY` | 400 | Le fichier ZIP contient des répertoires imbriqués, qui ne sont pas pris en charge. Tous les fichiers doivent se trouver à la racine du fichier ZIP. |
| `GENERIC_ERROR` | 500 | Une erreur imprévue s'est produite lors du téléchargement. L'objet `meta` contient le message `original_error` pour le débogage. Réessayez ou contactez l'[assistance]({{site.baseurl}}/support_contact). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs de traitement" }


## Réponse {#response}

Il existe cinq codes de statut de réponse pour cet endpoint : `200`, `400`, `403`, `429` et `500`.

Le JSON suivant présente la forme attendue de la réponse.

```json
{
    "new_assets": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "url": (String) the URL to access the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif")
        }
    ],
    "errors": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
            "error": (String) the error that occurred
        }
    ],
    "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}
```

{% endapi %}