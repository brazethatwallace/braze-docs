---
nav_title: "WhatsApp et systèmes externes"
article_title: "WhatsApp et systèmes externes"
page_order: 2
description: "Cet article de référence fournit un guide étape par étape pour intégrer Braze et WhatsApp avec un système externe d'IA ou de communication."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Intégrer Braze et WhatsApp avec un système externe d'IA ou de communication {#integrate-braze-and-whatsapp-with-an-external-ai-or-communication-system}

> Tirez parti de la puissance des chatbots IA et des transferts vers des agents en direct sur le canal WhatsApp pour rationaliser vos opérations de support client. En automatisant les demandes courantes et en passant de façon fluide à des agents humains lorsque nécessaire, vous pouvez améliorer considérablement les temps de réponse et enrichir l'expérience client globale.

## Conditions préalables {#prerequisites}

| Exigences | Description |
| - | - |
| Système externe | Un système tiers d'IA ou de communication capable de créer et gérer des chatbots, des systèmes automatisés de service client utilisant des API, ou les deux. |
| Intégration Braze et WhatsApp | Un numéro WhatsApp géré par Braze |
| Clé API REST Braze | Une clé API REST avec les autorisations `campaigns.trigger.send`. Celle-ci peut être créée dans le tableau de bord de Braze en accédant à **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Comment ça fonctionne {#how-it-works}

L'intégration entre Braze et le système externe d'IA ou de communication fonctionne comme une voie à double sens, où Braze est le canal de communication et le système externe est l'« intelligence » qui traite les messages et formule les réponses.

Le flux de travail de l'intégration peut être divisé en deux flux clés :
**Flux entrant :** Le message d'un utilisateur arrive dans Braze, puis est transmis à votre système externe pour traitement.
**Flux sortant :** Après avoir traité le message, votre système externe envoie une réponse à Braze, qui délivre ensuite le message à l'utilisateur final.

Pour automatiser efficacement cette communication, cette intégration utilise deux fonctionnalités clés de Braze : les [campagnes webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) et les [campagnes déclenchées par API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

![Architecture de l'intégration entre le canal WhatsApp de Braze et un système externe.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
## Configuration de l'intégration {#configuring-the-integration}

### Étape 1 : Créer une campagne webhook pour les messages entrants {#step-1-create-a-webhook-campaign-for-inbound-messages}

Commencez par créer une campagne webhook pour établir un moyen d'envoyer les messages WhatsApp reçus par Braze à votre système externe.

1. Dans Braze, créez une campagne webhook.
2. Dans le compositeur de webhook, sélectionnez **Compose webhook**.
3. Dans le champ **Webhook URL**, saisissez l'endpoint API (URL) du système externe qui recevra le message.
4. Sélectionnez **Raw text** pour le corps de la requête et saisissez un payload avec une personnalisation contenant l'`external_id` et le numéro de téléphone de l'utilisateur, le contenu du message et d'autres informations pertinentes, comme :

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5. À l'étape **Schedule Delivery** du compositeur de votre campagne, sélectionnez **Action-Based** pour le type de livraison et **Send a WhatsApp inbound message** pour le déclencheur de la campagne.

![Livraison par événement avec un déclencheur d'envoi d'un message WhatsApp entrant.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6. Terminez la composition de votre campagne, puis enregistrez et lancez-la. Après le lancement, chaque fois qu'un message est reçu, Braze envoie un webhook à votre système externe.

### Étape 2 : Créer une campagne déclenchée par API pour les messages sortants {#step-2}

Ensuite, créez une campagne déclenchée par API pour permettre à votre système externe d'envoyer des messages aux utilisateurs via WhatsApp.

1. Dans Braze, créez une campagne WhatsApp.
2. Dans le compositeur de messages, sélectionnez soit **WhatsApp Template Message** soit **Response Message**, puis sélectionnez le modèle ou la disposition du message de réponse. Vous pouvez sélectionner n'importe quelle disposition de message de réponse, car le message entrant a ouvert la fenêtre WhatsApp de 24 heures.

![Compositeur de messages avec des options pour sélectionner le type de message et la disposition du message.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3. Ajoutez la propriété de déclencheur API au corps du message, comme {% raw %}`{{api_trigger_properties.${external_system_msg+body}}}`{% endraw %}. Cela permet à votre système d'IA de remplir le message qui sera envoyé.

![Compositeur de messages avec un corps de message contenant des propriétés de déclencheur.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4. À l'étape **Schedule Delivery** du compositeur de votre campagne, sélectionnez **Action-Based** pour le type de livraison.
5. Enregistrez la campagne, puis notez le `campaign_id` unique que Braze génère pour cette campagne. Vous aurez besoin de cet ID pour l'étape suivante.

### Étape 3 : Connecter le système externe à la campagne déclenchée par API {#step-3-connect-the-external-system-to-the-api-triggered-campaign}

Enfin, configurez votre système externe pour appeler Braze et envoyer la réponse.

1. Dans le code de votre système externe, après avoir traité le message reçu et généré la réponse, effectuez une requête POST vers l'endpoint Braze `/messages/send`.
2. Dans le corps de la requête `/messages/send`, incluez le `campaign_id` de l'[étape 2](#step-2), l'`external_id` de l'utilisateur et le contenu de la réponse du système externe.
3. Utilisez la propriété de déclencheur API de l'[étape 2](#step-2) pour insérer la réponse du système externe, et n'oubliez pas d'inclure votre clé API dans l'en-tête de la requête pour l'authentification, comme dans cet exemple cURL :

{% raw %}
```bash
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

Vous disposez maintenant d'une base solide pour créer un flux de travail de chatbot IA !

### Personnaliser votre flux de travail {#customizing-your-workflow}

Vous pouvez étendre la logique de votre intégration pour :
- Utiliser différents mots-clés pour déclencher des campagnes webhook distinctes.
- Créer des flux de conversation plus complexes avec des campagnes déclenchées par API en plusieurs étapes.
- Enregistrer les informations de chat dans Braze en tant qu'attributs personnalisés pour enrichir le profil utilisateur et segmenter les futures campagnes.