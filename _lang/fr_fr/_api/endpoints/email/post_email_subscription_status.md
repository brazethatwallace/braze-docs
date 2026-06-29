---
nav_title: "POST : Modifier le statut d'abonnement aux e-mails"
article_title: "POST : Modifier le statut d'abonnement aux e-mails"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Modifier le statut d'abonnement aux e-mails de l'utilisateur."

---
{% api %}
# Modifier le statut d'abonnement aux e-mails {#change-email-subscription-status}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/status
{% endapimethod %}

> Utilisez cet endpoint pour définir l'état d'abonnement aux e-mails de vos utilisateurs.

Les utilisateurs peuvent avoir le statut `opted_in`, `unsubscribed` ou `subscribed` (sans confirmation d'abonnement ou de désabonnement spécifique).

Vous pouvez définir l'état d'abonnement aux e-mails pour une adresse e-mail qui n'est pas encore associée à l'un de vos utilisateurs dans Braze. Lorsque cette adresse e-mail est ensuite associée à un utilisateur, l'état d'abonnement aux e-mails que vous avez importé sera automatiquement appliqué.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `email.status`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `email` | Requis | Chaîne de caractères ou tableau | Adresse e-mail sous forme de chaîne de caractères à modifier, ou un tableau contenant jusqu'à 50 adresses e-mail à modifier. |
| `subscription_state` | Requis | Chaîne de caractères | « subscribed », « unsubscribed » ou « opted_in ». |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Résolution des problèmes de blocage d'e-mails SendGrid {#troubleshooting-sendgrid-email-blocks}

Lorsque SendGrid bloque un destinataire, mettez à jour le statut d'abonnement avec cet endpoint et vérifiez l'engagement à l'aide des filtres de segment. Utilisez les événements de rebond temporaire de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) pour surveiller la livrabilité, et confirmez l'état d'abonnement avant de relancer les envois.

## Exemple de requête {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}