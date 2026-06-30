---
nav_title: "POST : Envoyer des e-mails transactionnels via la distribution déclenchée par l'API"
article_title: "POST : Envoyer des e-mails transactionnels via la distribution déclenchée par l'API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze Envoyer des e-mails transactionnels via la distribution déclenchée par l'API."

---

{% api %}
# Envoyer des e-mails transactionnels via la distribution déclenchée par l'API {#send-transactional-emails-using-api-triggered-delivery}
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Utilisez cet endpoint pour envoyer des messages transactionnels immédiats et ponctuels à un utilisateur désigné.

Cet endpoint est utilisé parallèlement à la création d'une [Campaign d'e-mails transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) Braze et de l'ID de Campaign correspondant.

{% alert important %}
L'e-mail transactionnel est actuellement disponible dans certains forfaits Braze. Contactez votre gestionnaire de la satisfaction client Braze pour plus de détails.
{% endalert %}

Similaire à l'[endpoint d'envoi de Campaign déclenchée]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns), ce type de Campaign vous permet d'héberger le contenu du message dans le tableau de bord de Braze tout en dictant quand et à qui un message est envoyé via votre API. Contrairement à l'endpoint d'envoi de Campaign déclenchée, qui accepte une audience ou un segment auquel envoyer des messages, une requête à cet endpoint doit spécifier un utilisateur unique par `external_user_id` ou `user_alias`, car ce type de Campaign est conçu pour l'envoi de messages 1:1 d'alertes telles que des confirmations de commande ou des réinitialisations de mot de passe.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous devrez générer une clé API avec l'autorisation `transactional.send`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## Paramètres de chemin {#path-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `campaign_id` | Requis | Chaîne de caractères | ID de la Campaign |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin" }

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
}
```

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `external_send_id` | Facultatif | Chaîne de caractères | Une chaîne de caractères compatible Base64. Validée par rapport à l'expression régulière suivante :<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>Ce champ facultatif vous permet de transmettre un identifiant interne pour cet envoi particulier, qui est inclus dans les événements envoyés à partir du postback d'événement HTTP transactionnel. Une fois transmis, cet identifiant est également utilisé comme clé de déduplication, que Braze conserve pendant 24 heures. <br><br>Transmettre le même identifiant dans une autre requête n'entraîne pas la création d'une nouvelle instance d'envoi par Braze pendant 24 heures. |
| `trigger_properties` | Facultatif | Objet | Voir les [propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object). Paires clé-valeur de personnalisation qui s'appliquent à l'utilisateur dans cette requête. |
| `recipient` | Requis | Objet | L'utilisateur que vous ciblez avec ce message. Peut contenir des `attributes` et un seul `external_user_id` ou `user_alias`.<br><br>Notez que si vous fournissez un ID externe qui n'existe pas encore dans Braze, le fait de transmettre des champs à l'objet `attributes` crée ce profil utilisateur dans Braze et envoie ce message à l'utilisateur nouvellement créé. <br><br>Si vous envoyez plusieurs requêtes au même utilisateur avec des données différentes dans l'objet `attributes`, les attributs `first_name`, `last_name` et `email` sont mis à jour de manière synchrone et intégrés dans votre message. Les attributs personnalisés ne bénéficient pas de cette même protection ; procédez donc avec prudence lors de la mise à jour d'un utilisateur via cette API et de la transmission de différentes valeurs d'attributs personnalisés en succession rapide. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## Réponse {#response}

L'endpoint d'envoi d'e-mails transactionnels répond avec le `dispatch_id` du message, qui représente l'instance de cet envoi de message. Cet identifiant peut être utilisé avec les événements du postback d'événement HTTP transactionnel pour suivre le statut d'un e-mail individuel envoyé à un utilisateur unique.

### Exemples de réponses {#example-responses}

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## Résolution des problèmes {#troubleshooting}

L'endpoint peut également renvoyer, dans certains cas, un code d'erreur et un message lisible par un être humain, qui sont le plus souvent des erreurs de validation. Voici quelques erreurs courantes que vous pouvez obtenir lorsque vous effectuez des requêtes invalides.

| Erreur | Résolution des problèmes |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | L'ID de Campaign fourni ne correspond pas à une Campaign transactionnelle. |
| `The external reference has been queued.  Please retry to obtain send_id.` | L'external_send_id a été créé récemment, essayez un nouvel external_send_id si vous souhaitez envoyer un nouveau message. |
| `Campaign does not exist` | L'ID de Campaign fourni ne correspond pas à une Campaign existante. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | L'ID de Campaign fourni correspond à une Campaign archivée. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | L'ID de Campaign fourni correspond à une Campaign en pause. |
| `campaign_id must be a string of the campaign api identifier` | L'ID de Campaign fourni n'est pas dans un format valide. |
| `Error authenticating credentials` | La clé API fournie est invalide. |
| `Invalid whitelisted IPs `| L'adresse IP qui envoie la requête ne figure pas sur la liste blanche des adresses IP (si elle est utilisée). |
| `You do not have permission to access this resource` | La clé API utilisée n'a pas la permission d'effectuer cette action. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

La plupart des endpoints de Braze disposent d'une implémentation de limite de débit qui renvoie un code de réponse 429 si vous effectuez un nombre excessif de requêtes. L'endpoint d'envoi transactionnel dispose d'un quota horaire payant mesuré en unités (par exemple, 50 000 unités par heure, selon votre forfait). Il n'existe pas de limite de débit distincte par endpoint pour cet endpoint : vous pouvez envoyer au-delà du volume qui vous est alloué, mais seul ce volume est couvert par le SLA ; les requêtes dépassant cette allocation sont toujours envoyées, mais ne sont pas couvertes par le SLA. Les requêtes adressées à cet endpoint sont prises en compte dans votre [limite de débit globale de l'API externe]({{site.baseurl}}/api/api_limits). Si vous dépassez cette limite (par exemple, 250 000 requêtes par heure sur l'ensemble des endpoints), Braze renvoie un code 429 et limite les requêtes jusqu'à ce que la limite soit réinitialisée. Le compteur de volume transactionnel est réinitialisé toutes les heures. Contactez l'assistance Braze si vous avez besoin de plus amples informations sur cette fonctionnalité.

## Postback d'événement HTTP transactionnel {#transactional-http-event-postback}

{% multi_lang_include channels/transactional_email/http_event_postback.md %}

{% endapi %}