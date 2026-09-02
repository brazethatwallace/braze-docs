---
nav_title: Zendesk
article_title: Zendesk Chat
description: "Découvrez comment intégrer Zendesk Chat à Braze et mettre en place une conversation SMS bidirectionnelle."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk Chat

> [Zendesk Chat](https://www.zendesk.com/service/messaging/) utilise les webhooks de chaque plateforme pour établir une conversation SMS bidirectionnelle. Lorsqu'un utilisateur demande de l'aide, un ticket est créé dans Zendesk. Les réponses des agents sont transmises à Braze par le biais d'une Campaign SMS déclenchée par l'API, et les réponses des utilisateurs sont renvoyées à Zendesk.

## Conditions préalables {#prerequisites}


| Prérequis | Description |
|---|---|
| Un compte Zendesk | Un compte Zendesk est nécessaire pour bénéficier de ce partenariat. |
| Un jeton d'autorisation de base Zendesk | Un jeton d'autorisation de base Zendesk est utilisé pour effectuer une requête webhook sortante de Braze vers Zendesk. |
| Une clé API REST de Braze | Une clé API REST de Braze avec les autorisations `campaigns.trigger.send`. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

Améliorez l'efficacité du support client en combinant les fonctionnalités SMS de Braze avec les réponses des agents en direct or en ligne/en production/instantané de Zendesk pour répondre rapidement aux demandes des utilisateurs avec un support humain.

## Intégration de Zendesk Chat {#integrating-zendesk-chat}

### Étape 1 : Créer un webhook dans Zendesk {#step-1-create-a-webhook-in-zendesk}

1. Dans la console de développement Zendesk, accédez aux webhooks : {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. Sous **Create Webhook**, sélectionnez **Trigger or automation**.
3. Pour l'**Endpoint URL**, ajoutez l'endpoint **/campaign/trigger/send**.
4. Sous **Authentication**, sélectionnez **Bearer token** et ajoutez la clé API REST de Braze avec les autorisations `campaigns.trigger.send`.

![Un exemple de webhook Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat1.png %}){: style="max-width:70%;"}

### Étape 2 : Créer une Campaign SMS sortante {#step-2-create-an-outbound-sms-campaign}

Ensuite, vous allez créer une Campaign SMS qui écoutera les webhooks de Zendesk et enverra une réponse SMS personnalisée à vos clients.

#### Étape 2.1 : Rédigez votre message {#step-21-compose-your-message}

Lorsque Zendesk envoie le contenu d'un message via l'API, il se présente dans le format suivant :

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

Nous devons donc extraire de cette chaîne de caractères les détails que nous voulons afficher dans le message, faute de quoi l'utilisateur verra tous les détails.

![Un exemple de SMS sans mise en forme.]({% image_buster /assets/img/zendesk/instant_chat/chat2.png %}){: style="max-width:40%;"}

Dans la zone de texte **Message**, ajoutez le code Liquid suivant ainsi que tout texte de désinscription ou autre contenu statique :

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk:
{{msg[2]}}

Feel free to respond directly to this number!
```
{% endraw %}

![Un exemple de SMS avec mise en forme.]({% image_buster /assets/img/zendesk/instant_chat/chat3.png %}){: style="max-width:70%;"}

#### Étape 2.2 : Planifier la distribution {#step-22-schedule-the-delivery}

Pour le type de distribution, sélectionnez **API-Triggered delivery**, puis copiez l'ID de la Campaign, qui sera utilisé dans les étapes suivantes.

![Livraison déclenchée par l'API]({% image_buster /assets/img/zendesk/instant_chat/chat4.png %}){: style="max-width:70%;"}

Enfin, sous **Delivery Controls**, activez la rééligibilité.

![Rééligibilité activée sous « Delivery Controls ».]({% image_buster /assets/img/zendesk/instant_chat/chat5.png %})

### Étape 3 : Créer un déclencheur dans Zendesk pour transmettre les réponses des agents à Braze {#step-3-create-a-trigger-in-zendesk-to-forward-agent-replies-to-braze}

Allez dans **Objects and rules** > **Business rules** > **Triggers**.

1. Créez une nouvelle **catégorie** (par exemple, **Trigger a message**).
2. Créez un nouveau **déclencheur** (par exemple, **Respond via SMS Braze**).
3. Sous **Conditions**, sélectionnez :
- **Ticket>Comment** est **Present and requester can see comment** afin que le message soit déclenché chaque fois qu'un nouveau commentaire public est inclus dans la mise à jour d'un ticket.
- **Ticket>Update** *n'est pas* **Web service (API)** afin que lorsqu'un utilisateur envoie un message depuis Braze, celui-ci ne soit pas renvoyé sur son téléphone portable. Seuls les messages provenant de Zendesk sont transférés.

![Respond via SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat6.png %}){: style="max-width:70%;"}

Sous **Actions**, sélectionnez **Notify by Webhook** et choisissez l'endpoint que vous avez créé à l'étape 1. Ensuite, spécifiez le corps de l'appel API. Saisissez le `campaign_id` de l'[étape 2.2](#step-22-schedule-the-delivery) dans le corps de la requête.

![Corps JSON pour Respond via SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat7.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### Étape 4 : Créer un déclencheur dans Zendesk pour mettre à jour un utilisateur lorsqu'un ticket est fermé {#step-4-create-a-trigger-in-zendesk-to-update-a-user-when-a-ticket-is-closed}

Si vous souhaitez informer l'utilisateur que le ticket a été fermé, créez une nouvelle Campaign dans Braze avec le corps de réponse modélisé.

![Mettre à jour un utilisateur lorsque le ticket est fermé.]({% image_buster /assets/img/zendesk/instant_chat/chat8.png %}){: style="max-width:70%;"}

Sélectionnez **API-Triggered delivery** et copiez l'ID de la Campaign.

Ensuite, configurez un déclencheur pour avertir Braze de la clôture du ticket :
- Catégorie : **Trigger a message**
- Sous Conditions, sélectionnez **Ticket>Ticket Status** et modifiez-le en **Solved**.

![Configuration d'un ticket résolu dans Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat9.png %}){: style="max-width:70%;"}

Sous **Actions**, sélectionnez **Notify by Webhook** et choisissez le deuxième endpoint que vous venez de créer. À partir de là, nous devons spécifier le corps de l'appel API :

![Corps JSON du ticket résolu.]({% image_buster /assets/img/zendesk/instant_chat/chat10.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### Étape 5 : Ajouter un champ utilisateur personnalisé dans Zendesk {#step-5-add-a-custom-user-field-in-zendesk}

Dans l'Admin Center, sélectionnez **People** dans la barre latérale, puis sélectionnez **Configuration** > **User fields**. Ajoutez le champ utilisateur personnalisé `braze_external_id`.

### Étape 6 : Configurer le transfert des SMS entrants {#step-6-set-up-inbound-sms-forwarding}

Ensuite, vous allez créer deux nouvelles Campaigns webhook dans Braze afin de pouvoir transférer les SMS entrants des clients vers la boîte de réception de Zendesk.

| Campaign | Objectif |
|--------------------|--------------------------------------------------------------------------------------|
| Campaign webhook 1 | Crée un nouveau ticket dans Zendesk. |
| Campaign webhook 2 | Transfère toutes les réponses SMS conversationnelles envoyées par le client vers Zendesk. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 6 : Configurer le transfert des SMS entrants" }

#### Étape 6.1 : Créer une catégorie de mots-clés SMS {#step-61-create-an-sms-keyword-category}

Dans le tableau de bord de Braze, allez dans **Audience**, choisissez votre **groupe d'abonnement SMS**, puis sélectionnez **Add Custom Keyword**. Remplissez les champs suivants pour créer une catégorie de mots-clés SMS exclusive pour Zendesk.

| Champ | Description |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Keyword Category | Le nom de votre catégorie de mots-clés, par exemple `ZendeskSMS1`. |
| Keywords | Vos mots-clés personnalisés, tels que `SUPPORT`. |
| Reply Message | Le message envoyé lorsqu'un mot-clé est détecté, par exemple « Un représentant du service client vous contactera sous peu. » |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 6.1 : Créer une catégorie de mots-clés SMS" }

![Un exemple de catégorie de mots-clés SMS dans Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat11.png %}){: style="max-width:70%;"}

#### Étape 6.2 : Créer votre première Campaign webhook {#step-62-create-your-first-webhook-campaign}

Dans le tableau de bord de Braze, créez votre première Campaign webhook. Ce message signalera à Zendesk qu'une demande d'assistance a été effectuée.

Dans le compositeur de webhook, remplissez les champs suivants :
- Webhook URL : {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- HTTP Method : POST
- Request Headers :
- Content-Type: application/json
- Authorization: Basic {{Token}}
- Request body :

{% raw %}
```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![Un exemple de requête avec les deux en-têtes requis.]({% image_buster /assets/img/zendesk/instant_chat/chat12.png %}){: style="max-width:70%;"}


#### Étape 6.3 : Planifier la première distribution {#step-63-schedule-the-first-delivery}

Pour **Schedule Delivery**, sélectionnez **Action-Based Delivery**, puis choisissez **Send an SMS Inbound Message** comme type de déclencheur. Ajoutez également le groupe d'abonnement SMS et la catégorie de mots-clés que vous avez définis précédemment.

![La page « Schedule Delivery » pour la première Campaign webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat13.png %})

Sous **Delivery Controls**, activez la rééligibilité.

![Rééligibilité sélectionnée sous « Delivery Controls » pour la première Campaign webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat14.png %})

#### Étape 6.4 : Créer votre deuxième Campaign webhook {#step-64-create-your-second-webhook-campaign}

Configurez une Campaign webhook pour transmettre les messages SMS restants de l'utilisateur à Zendesk :

Comme Zendesk envoie l'ID du ticket sous forme de chaîne de caractères, créez un bloc de contenu pour convertir la chaîne en un entier afin de pouvoir l'utiliser dans le webhook de Zendesk.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

Dans le compositeur de webhook :
- Webhook URL : {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- Request : PUT
- KVP :
    - Content-Type: application/JSON
    - Authorization: Basic {{Token}}

Exemple de corps :

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### Étape 6.5 : Terminer la configuration de la deuxième Campaign webhook {#step-65-complete-second-webhook-campaign-setup}
- Mettez en place un déclencheur basé sur une action pour les utilisateurs qui envoient un message entrant dans la catégorie « Other ».
- Définissez les critères de rééligibilité.
- Ajoutez les audiences concernées (dans ce cas, l'attribut personnalisé **zendesk_ticket_open** est **true**).

[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}