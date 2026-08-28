---
nav_title: "POST : Suivre les événements d'analyse des bannières"
article_title: "POST : Suivre les événements d'analyse des bannières"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Utilisez cet endpoint pour suivre les événements d'impression et de clic pour les bannières."
hidden: true
---

{% api %}
# Suivre les événements d'analyse des bannières {#track-banner-analytics-events}
{% apimethod post %}
/v1/device-messaging/banners/track
{% endapimethod %}

> Utilisez cet endpoint pour enregistrer les événements d'impression et de clic pour les bannières.

Braze valide chaque événement séparément. Lorsqu'une requête contient à la fois des événements valides et invalides, Braze traite les événements valides et renvoie les détails des événements ignorés dans le tableau `errors`. Si aucun événement n'est valide, Braze renvoie un code de statut `400`.

{% alert important %}
Cette page est en version bêta. Les fonctionnalités et la documentation de l'API Device Messaging sont susceptibles d'évoluer. Contactez votre gestionnaire de compte Braze pour demander l'accès.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous avez besoin des éléments suivants :

- Un espace de travail avec les bannières activées
- Une [clé API REST côté client]({{site.baseurl}}/api/device_messaging_api/authentication) avec la permission `banners.track`
- L'[endpoint REST]({{site.baseurl}}/api/basics#endpoints) de votre instance Braze
- Un `id` de bannière renvoyé par l'[endpoint de récupération des bannières pour un utilisateur]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)

Incluez la clé API REST côté client dans l'en-tête `Authorization` en tant que jeton Bearer.

## Limite de débit {#rate-limit}

Les limites de débit s'appliquent par espace de travail. Si vous dépassez la limite de débit, Braze renvoie un code de statut `429`. Lorsqu'ils sont disponibles, utilisez les en-têtes de réponse `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` et `X-RateLimit-Retry-After` pour surveiller votre utilisation et déterminer quand réessayer.

Pour plus d'informations, consultez [Limites de débit de l'API Device Messaging]({{site.baseurl}}/api/device_messaging_api/rate_limits).

## Corps de la requête {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "{BANNER_ID}",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    }
  ]
}
```

## Paramètres de la requête {#request-parameters}

| Paramètre | Obligatoire | Type de données | Description | Exemple |
|---|---|---|---|---|
| `external_user_id` | Obligatoire | String | L'ID externe de l'utilisateur associé à tous les événements de la requête. La valeur encodée en UTF-8 doit être inférieure à 987 octets. | `user_abc123` |
| `app_id` | Obligatoire | String | L'[identifiant API de l'application]({{site.baseurl}}/api/identifier_types#app-identifier). Il doit identifier une application dans l'espace de travail authentifié. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | Obligatoire | String | La version de l'application hôte. Elle ne doit pas dépasser 255 caractères. | `1.0.0` |
| `events` | Obligatoire | Tableau d'objets | Un ou plusieurs événements d'analyse de bannière à enregistrer. | `[{"id":"bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E","event_type":"impression","timestamp":"2026-04-09T12:00:00Z"}]` |
| `events[].id` | Obligatoire | String | L'`id` de la bannière renvoyé par l'endpoint de récupération des bannières pour un utilisateur. Utilisez l'ID de la bannière, et non le `placement_id`, afin que Braze attribue l'événement à la bonne campagne et à la bonne variante. | `bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E` |
| `events[].event_type` | Obligatoire | String | Le type d'événement. Les valeurs possibles sont `impression` et `click`. | `impression` |
| `events[].timestamp` | Obligatoire | String | La date et l'heure auxquelles l'événement s'est produit, au format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | `2026-04-09T12:00:00Z` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Paramètres de la requête" }

## Exemple de requête {#example-request}

Remplacez *`YOUR_REST_API_URL`* par l'[endpoint REST]({{site.baseurl}}/api/basics#endpoints) de votre instance Braze.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/track' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    },
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "click",
      "timestamp": "2026-04-09T12:00:05Z"
    }
  ]
}'
```

## Paramètres de la réponse {#response-parameters}

| Paramètre | Type de données | Description |
|---|---|---|
| `events_processed` | Entier | Le nombre d'événements que Braze a validés et mis en file d'attente. |
| `message` | String | Le statut du lot d'événements accepté. |
| `errors` | Tableau d'objets | Détails sur les événements que Braze a ignorés. Ce tableau est absent lorsque Braze traite tous les événements. |
| `errors[].type` | String | L'erreur de validation pour l'événement ignoré. |
| `errors[].index` | Entier | L'index basé sur zéro de l'événement ignoré dans le tableau `events` de la requête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paramètres de la réponse" }

## Exemples de réponses {#example-responses}

### Tous les événements traités {#all-events-processed}

Lorsque Braze accepte tous les événements, il renvoie un code de statut `202`.

```json
{
  "events_processed": 2,
  "message": "success"
}
```

### Certains événements ignorés {#some-events-skipped}

Braze renvoie également un code de statut `202` lorsqu'il accepte au moins un événement valide. La réponse identifie les événements ignorés.

```json
{
  "events_processed": 2,
  "message": "success",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click.",
      "index": 2
    }
  ]
}
```

### Aucun événement valide {#no-valid-events}

Si Braze ne peut traiter aucun événement, il renvoie un code de statut `400`.

```json
{
  "message": "No valid events provided.",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click.",
      "index": 0
    },
    {
      "type": "'timestamp' is required",
      "index": 1
    }
  ]
}
```

## Codes de statut {#status-codes}

| Code de statut | Description |
|---|---|
| `202` | Braze a accepté au moins un événement. La réponse liste les événements ignorés. |
| `400` | La requête est mal formée, les champs obligatoires sont invalides ou aucun événement n'est valide. |
| `401` | La clé API REST côté client est manquante ou invalide. |
| `403` | La clé API REST côté client ne dispose pas de la permission `banners.track`. |
| `404` | La fonctionnalité de bannières n'est pas activée pour l'espace de travail. |
| `429` | L'espace de travail a dépassé sa limite de débit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Codes de statut" }

Pour plus d'informations, consultez [Gestion des erreurs et nouvelles tentatives de l'API Device Messaging]({{site.baseurl}}/api/device_messaging_api/error_handling).

{% endapi %}