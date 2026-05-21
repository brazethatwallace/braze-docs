---
nav_title: Envoyer les messages
article_title: Envoi de messages à l'aide de la REST API
page_order: 1
page_type: reference
description: "Cet article de référence présente les deux méthodes permettant d'envoyer des messages de manière programmatique à l'aide de la REST API Braze."
---

# Envoi de messages à l'aide de la REST API {#sending-messages-using-the-rest-api}

> Vous pouvez envoyer des messages depuis votre backend en temps réel à l'aide de deux endpoints Braze différents. Chacun a une forme de requête différente : l'un nécessite le contenu complet du message dans la requête ; l'autre nécessite un ID de Campaign et envoie le contenu défini dans le tableau de bord.

Cette approche est compatible avec tous les canaux de communication pris en charge par l'API (WhatsApp, e-mail, SMS, notifications push, Content Cards, webhooks, etc.).

## Deux méthodes d'envoi {#two-ways-to-send}

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) |
| --- | --- | --- |
| **ID de Campaign** | Facultatif. Omettez-le pour envoyer sans suivi de Campaign dans le tableau de bord, ou fournissez un ID de Campaign API ainsi que `message_variation_id` dans chaque message pour effectuer le suivi dans le tableau de bord. | Requis. |
| **Contenu du message** | Vous devez inclure un objet `messages` dans la requête (par exemple, `messages.whats_app`, `messages.email`). | Non accepté. Le contenu du message est défini dans la Campaign sur le tableau de bord de Braze. |
| **Cas d'utilisation** | Envoyer un message dont le contenu est entièrement spécifié dans la requête API. | Déclencher une Campaign préconfigurée (contenu dans le tableau de bord) vers des destinataires spécifiques via l'API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Two ways to send" }

Pour obtenir tous les détails relatifs aux requêtes et aux réponses, consultez les références des endpoints [Envoyer des messages immédiatement (API uniquement)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) et [Envoyer des Campaigns à l'aide d'une réception/distribution déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

---

## Option 1 : Envoyer avec le contenu du message dans la requête (`/messages/send`) {#option-1-send-with-message-content-in-the-request-messagessend}

Utilisez cet endpoint lorsque vous souhaitez spécifier le contenu complet du message dans la requête API. Vous **devez** inclure un objet `messages` (par exemple, `messages.whats_app`, `messages.email` ou `messages.sms`). Vous pouvez omettre `campaign_id` pour envoyer sans suivi de Campaign, ou inclure un ID de Campaign API et `message_variation_id` dans chaque message afin de suivre les envois dans le tableau de bord (consultez la [référence de l'endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) pour plus de détails).

**Requis :** clé API avec la permission `messages.send`.

{% alert important %}
Chaque destinataire dans `external_user_ids` doit déjà exister dans Braze. Pour créer des utilisateurs dans le cadre d'un envoi, utilisez d'abord [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), ou utilisez l'[option 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) (Campaign déclenchée par l'API) à la place.
{% endalert %}

### Exemple : modèle de message WhatsApp {#example-whatsapp-template-message}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

Pour obtenir la spécification complète de l'objet WhatsApp, consultez [Objet WhatsApp]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object/).

{% alert note %}
L'endpoint `/messages/send` ne prend en charge que les modèles WhatsApp avec des en-têtes TEXT ou IMAGE. Pour les types d'en-tête DOCUMENT, VIDEO ou autres types de médias, utilisez l'[endpoint de Campaign déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) ou le tableau de bord de Braze.
{% endalert %}

### Exemple : e-mail {#example-email}

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

Pour les autres canaux, consultez [Objets d'envoi de messages]({{site.baseurl}}/api/objects_filters/#messaging-objects).

---

## Option 2 : Déclencher une Campaign avec du contenu dans le tableau de bord (`/campaigns/trigger/send`) {#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend}

Utilisez cet endpoint lorsque le contenu du message est créé dans le tableau de bord de Braze (Campaign déclenchée par API). Vous envoyez un `campaign_id` **requis** et les destinataires ; vous n'envoyez **pas** d'objet `messages`.

**Requis :** clé API avec la permission `campaigns.trigger.send`.

### Étape 1 : Créer une Campaign déclenchée par API {#step-1-create-an-api-triggered-campaign}

1. Dans le tableau de bord de Braze, accédez à **Messaging** > **Campaigns**.
2. Sélectionnez **Create Campaign**, puis **API-Triggered Campaign** (et non « API Campaign »).
3. Ajoutez votre canal de communication (WhatsApp, e-mail, SMS, etc.) et créez le contenu du message dans le tableau de bord.
4. Notez l'**ID de Campaign** (et l'**ID d'envoi** si vous utilisez plusieurs variantes de message). Vous les utiliserez dans la requête API.

Pour en savoir plus sur la création de Campaigns déclenchées par API, consultez [Réception/distribution déclenchée par API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/).

### Étape 2 : Déclencher la Campaign via l'API {#step-2-trigger-the-campaign-via-the-api}

Envoyez une requête POST à `/campaigns/trigger/send` avec `campaign_id` et `recipients` (ou `broadcast`/`audience`). N'incluez pas d'objet `messages` — le contenu provient de la Campaign.

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

Pour obtenir le corps complet de la requête (y compris `trigger_properties`, `send_to_existing_only`, `attributes`, etc.), consultez la référence de l'endpoint [Envoyer des Campaigns à l'aide d'une réception/distribution déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body).

---

## Vérifier votre intégration {#verify-your-integration}

1. Envoyez une requête en utilisant l'une des options ci-dessus, en indiquant votre propre ID utilisateur comme destinataire.
2. Confirmez que le message a bien été distribué.
3. Si vous utilisez l'option 2, vérifiez la Campaign dans le tableau de bord de Braze pour confirmer que l'envoi a bien été enregistré.

## Considérations {#considerations}

- Utilisez les [fonctionnalités de personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/) de Braze pour adapter le contenu lorsque cela est possible.
- Assurez-vous que vos envois de messages sont conformes aux réglementations applicables et qu'ils incluent les options de désabonnement et les avis de confidentialité requis.
- Pour d'autres endpoints (planification, déclencheurs Canvas, etc.), consultez [Endpoints d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/).