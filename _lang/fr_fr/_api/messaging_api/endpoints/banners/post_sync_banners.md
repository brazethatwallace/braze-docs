---
nav_title: "POST : Récupérer les bannières pour un utilisateur"
article_title: "POST : Récupérer les bannières pour un utilisateur"
permalink: /api/device_messaging_api/endpoints/banners/post_sync_banners
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Utilisez cet endpoint pour récupérer les bannières éligibles pour un utilisateur."
hidden: true
---

{% api %}
# Récupérer les bannières pour un utilisateur {#retrieve-banners-for-a-user}
{% apimethod post %}
/v1/device-messaging/banners/sync
{% endapimethod %}

{% alert important %}
Cette page est en version bêta. Les fonctionnalités et la documentation de l'API Device Messaging sont susceptibles d'être modifiées.
{% endalert %}

> Utilisez cet endpoint pour récupérer la bannière éligible pour chaque emplacement demandé pour un utilisateur.

La réponse contient des propriétés de bannière structurées que vous pouvez utiliser pour créer une interface personnalisée. Elle ne contient pas de HTML rendu.

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous avez besoin des éléments suivants :

- Un espace de travail avec les bannières activées
- Une [clé API REST côté client]({{site.baseurl}}/api/device_messaging_api/authentication) avec la permission `banners.sync`
- L'[endpoint REST]({{site.baseurl}}/api/basics#endpoints) de votre instance Braze

Incluez la clé API REST côté client dans l'en-tête `Authorization` en tant que jeton Bearer.

## Limite de débit {#rate-limit}

Les limites de débit s'appliquent par espace de travail. Si vous dépassez la limite de débit, Braze renvoie un code de statut `429`. Lorsqu'ils sont disponibles, utilisez les en-têtes de réponse `X-RateLimit-Limit`, `X-RateLimit-Remaining` et `X-RateLimit-Reset` pour surveiller votre utilisation.

Pour plus d'informations, consultez [Limites de débit de l'API Device Messaging]({{site.baseurl}}/api/device_messaging_api/rate_limits).

## Corps de la requête {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}
```

## Paramètres de requête {#request-parameters}

| Paramètre | Obligatoire | Type de données | Description | Exemple |
|---|---|---|---|---|
| `external_user_id` | Obligatoire | String | L'ID externe de l'utilisateur. | `user_abc123` |
| `app_id` | Obligatoire | String | L'[identifiant API de l'application]({{site.baseurl}}/api/identifier_types#app-identifier). Il doit identifier une application dans l'espace de travail authentifié. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | Obligatoire | String | La version de l'application hôte. Elle ne doit pas dépasser 255 caractères. | `1.0.0` |
| `placements` | Obligatoire | Tableau de chaînes de caractères | Un ou plusieurs identifiants d'emplacement pour lesquels récupérer les bannières. Incluez au moins un identifiant d'emplacement. | `["home_hero", "sidebar_promo"]` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

Remplacez *`YOUR_REST_API_URL`* par l'[endpoint REST]({{site.baseurl}}/api/basics#endpoints) de votre instance Braze.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/sync' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}'
```

## Paramètres de réponse {#response-parameters}

| Paramètre | Type de données | Description |
|---|---|---|
| `banners` | Objet | Une correspondance entre chaque identifiant d'emplacement demandé et sa bannière résolue. La valeur est `null` lorsqu'aucune bannière n'est éligible pour un emplacement. |
| `banners.{placement_id}.id` | String | L'identifiant unique de la bannière. Utilisez cette valeur pour signaler les événements d'impression et de clic. |
| `banners.{placement_id}.placement_id` | String | L'identifiant d'emplacement associé à la bannière. |
| `banners.{placement_id}.is_control` | Booléen | Indique si la bannière est une variante du groupe de contrôle. |
| `banners.{placement_id}.is_test_send` | Booléen | Indique si la bannière provient d'un envoi de test. La valeur par défaut est `false`. |
| `banners.{placement_id}.expires_at` | Entier | L'horodatage Unix, en secondes, après lequel vous ne devez plus afficher la bannière. Une valeur de `-1` signifie que la bannière n'expire pas. |
| `banners.{placement_id}.properties` | Objet ou null | Propriétés définies par le marketeur pour la bannière. Chaque propriété contient un `type` et une `value`. |
| `banners.{placement_id}.properties.{property}.type` | String | Le type de la propriété. Les valeurs possibles sont `number`, `string`, `boolean`, `image`, `jsonobject` et `datetime`. |
| `banners.{placement_id}.properties.{property}.value` | Nombre, chaîne de caractères, booléen ou objet | La valeur de la propriété. Son type JSON correspond au `type`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paramètres de réponse" }

## Exemple de réponse {#example-response}

Une requête réussie renvoie un code de statut `200` et la bannière résolue pour chaque emplacement demandé.

```json
{
  "banners": {
    "home_hero": {
      "id": "this_banner_is_a_stub_01",
      "placement_id": "home_hero",
      "is_control": false,
      "is_test_send": false,
      "expires_at": 1735689600,
      "properties": {
        "headline": {
          "type": "string",
          "value": "Level Up Your Game"
        },
        "cta_label": {
          "type": "string",
          "value": "Shop Now"
        }
      }
    },
    "sidebar_promo": null
  }
}
```

## Codes de statut {#status-codes}

| Code de statut | Description |
|---|---|
| `200` | Braze a résolu les données de bannière pour chaque emplacement demandé. |
| `400` | La requête contient des paramètres manquants ou invalides. |
| `401` | La clé API REST côté client est manquante, invalide ou ne dispose pas de la permission `banners.sync`. |
| `404` | L'endpoint n'est pas disponible. Cette réponse ne fait pas la distinction entre une clé API manquante ou invalide et une fonctionnalité de bannières désactivée. |
| `429` | L'espace de travail a dépassé sa limite de débit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Codes de statut" }

Pour plus d'informations, consultez [Gestion des erreurs et nouvelles tentatives de l'API Device Messaging]({{site.baseurl}}/api/device_messaging_api/error_handling).

{% endapi %}