---
nav_title: Envoyer des messages SMS
article_title: Envoi de messages SMS à l'aide de la REST API
page_order: 2
page_type: reference
description: "Cet article de référence explique comment envoyer des messages SMS à l'aide de la REST API Braze et d'une campagne API."
channel:
  - SMS
---

# Envoi de messages SMS à l'aide de la REST API {#sending-sms-messages-using-the-rest-api}

> Utilisez la REST API Braze pour envoyer des messages SMS transactionnels depuis votre backend en temps réel. Cette approche vous permet de créer un service qui envoie des SMS de manière programmatique tout en suivant les analyses de distribution parallèlement à vos autres Campaigns et Canvas dans le tableau de bord de Braze.

Cela peut s'avérer particulièrement utile pour l'envoi de messages transactionnels à haut volume dont le contenu est défini dans vos systèmes backend. Par exemple, vous pouvez informer les consommateurs lorsqu'ils reçoivent un message d'un autre utilisateur, en les invitant à visiter votre site web et à consulter leur boîte de réception.

Grâce à cette approche, vous pouvez :

- Déclencher l'envoi de SMS depuis votre backend en temps réel.
- Suivre les analyses parallèlement à toutes vos Campaigns et Canvas marketing.
- Étendre le champ d'application avec des fonctionnalités Braze supplémentaires, telles que les retards de message, le reciblage de suivi et les tests A/B.
- Optionnellement, passer à la [distribution déclenchée par API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) afin de définir vos modèles de message dans le tableau de bord de Braze tout en continuant à déclencher les envois depuis votre backend.

Pour envoyer un SMS via la REST API, vous devez configurer une campagne API dans le tableau de bord de Braze, puis utiliser l'endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) pour envoyer le message.

## Conditions préalables {#prerequisites}

Pour suivre ce guide, vous aurez besoin des éléments suivants :

| Condition | Description |
| --- | --- |
| Clé de REST API Braze | Une clé avec l'autorisation `messages.send`. Pour en créer une, rendez-vous dans **Paramètres** > **Clés API**. |
| Groupe d'abonnement SMS | Un groupe d'abonnement SMS configuré dans votre espace de travail Braze. |
| Service backend | Un service backend ou un environnement de script capable d'effectuer des requêtes HTTP POST vers la REST API Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Étape 1 : Créer une campagne API {#step-1-create-an-api-campaign}

1. Dans le tableau de bord de Braze, rendez-vous dans **Messaging** > **Campaigns**.
2. Sélectionnez **Create Campaign**, puis **API Campaigns**.
3. Saisissez un nom et une description pour votre campagne, par exemple « Notification par SMS ».
4. Ajoutez des étiquettes pertinentes pour l'identification et le suivi.
5. Sélectionnez **Add Messaging Channel**, puis choisissez **SMS**.
6. Notez l'**ID de la campagne** et l'**ID de la variante du message** affichés sur la page de la campagne. Vous aurez besoin de ces deux valeurs pour construire votre requête API.

## Étape 2 : Envoyer un message SMS à l'aide de l'API {#step-2-send-an-sms-message-using-the-api}

Construisez une requête POST vers l'endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Incluez l'ID de la campagne, l'ID utilisateur externe du destinataire et le contenu du SMS dans le payload de la requête.

{% alert important %}
Chaque destinataire mentionné dans `external_user_ids` doit déjà exister dans Braze. Les envois via API uniquement ne créent pas de nouveaux profils utilisateur. Si vous devez créer des utilisateurs dans le cadre d'un envoi, utilisez d'abord [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), ou optez pour une [campagne déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

### Exemple de requête {#example-request}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Remplacez `YOUR_REST_ENDPOINT` par l'[URL de l'endpoint REST]({{site.baseurl}}/api/basics/#endpoints) de votre espace de travail.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

Remplacez les valeurs de marque substitutive par vos ID réels. Le champ `body` prend en charge la [personnalisation Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/), ce qui vous permet d'adapter le contenu du message à chaque destinataire. Pour obtenir la liste complète des paramètres pris en charge par l'objet d'envoi de messages SMS, consultez [l'objet SMS]({{site.baseurl}}/api/objects_filters/messaging/sms_object/).

Une fois la requête construite, envoyez la requête POST depuis votre service backend vers la REST API Braze.

## Étape 3 : Vérifier votre intégration {#step-3-verify-your-integration}

Une fois la configuration terminée, vérifiez votre intégration :

1. Envoyez une requête API comme indiqué à l'[étape 2](#step-2-send-an-sms-message-using-the-api), en utilisant votre propre ID utilisateur comme destinataire.
2. Vérifiez que le message SMS a bien été reçu sur votre téléphone.
3. Dans le tableau de bord de Braze, rendez-vous sur la page des résultats de la campagne et confirmez que l'envoi a bien été enregistré.
4. Surveillez attentivement les résultats à mesure que vous développez votre campagne.

## Considérations {#considerations}

- Assurez-vous que vos campagnes SMS sont conformes aux réglementations applicables et aux exigences des opérateurs. Incluez les instructions de désabonnement (par exemple, « Envoyez STOP pour vous désabonner ») dans chaque message. Pour plus d'informations, consultez [les lois et réglementations relatives aux SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/) ainsi que [les mots-clés d'abonnement et de désabonnement]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/).
- Utilisez les [fonctionnalités de personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/) de Braze pour adapter le contenu des SMS à chaque consommateur, notamment grâce à du contenu dynamique et des données spécifiques à l'utilisateur.
- La REST API Braze propose des [endpoints d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) supplémentaires pour la planification de messages, le déclenchement de campagnes et bien plus encore.