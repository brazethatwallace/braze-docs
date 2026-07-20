---
nav_title: "Abonnements et désabonnements"
article_title: "Abonnements et désabonnements"
description: "Cet article de référence couvre les différentes méthodes d'abonnement et de désabonnement WhatsApp."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
---

# Abonnement et désabonnement {#opt-in-and-opt-out}

> La gestion des abonnements et désabonnements WhatsApp est cruciale, car WhatsApp surveille l'[évaluation de la qualité de votre numéro de téléphone](https://www.facebook.com/business/help/896873687365001), et une évaluation faible peut entraîner une réduction de vos limites d'envoi de messages. <br><br>L'un des moyens de maintenir une évaluation de qualité élevée est d'empêcher les utilisateurs de bloquer ou de signaler votre entreprise. Cela peut être réalisé en fournissant des [messages de haute qualité](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (apportant de la valeur à vos utilisateurs), en contrôlant la fréquence des messages et en permettant aux clients de se désabonner des communications futures. <br><br>Cette page explique comment configurer les abonnements et désabonnements, ainsi que les différences entre les modificateurs « expression régulière » et « est ».

Les abonnements peuvent provenir de sources externes ou de méthodes Braze, telles que les SMS ou les messages in-app et dans le navigateur. Les désabonnements peuvent être gérés à l'aide de mots-clés définis dans Braze et de boutons marketing WhatsApp. Consultez les méthodes suivantes pour obtenir des conseils sur la configuration des abonnements et désabonnements.

## Méthodes d'abonnement {#opt-in-methods}
- [Méthodes d'abonnement externes à Braze](#external-to-braze-opt-in-methods)
  - [Liste d'abonnement créée en externe](#externally-built-opt-in-list)
  - [Message sortant dans le canal de support client WhatsApp](#outbound-message-in-customer-support-whatsapp-channel)
  - [Message WhatsApp entrant](#inbound-whatsapp-message)
- [Méthodes d'abonnement via Braze](#braze-powered-opt-in-methods)

### Méthodes de désabonnement {#opt-out-methods}
- [Mots-clés de désabonnement généraux](#general-opt-out-keywords)
- [Sélection de désabonnement marketing](#marketing-opt-out-selection)

## Configurer les abonnements pour votre canal WhatsApp Braze {#set-up-opt-ins-for-your-braze-whatsapp-channel}

Pour les abonnements WhatsApp, vous devez respecter les [exigences de WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Vous devrez également fournir à Braze les informations suivantes :
- Un `external_id`, un [numéro de téléphone]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) et un statut d'abonnement mis à jour pour chaque utilisateur. Cela peut être fait en utilisant le [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) ou via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour mettre à jour le numéro de téléphone et le statut d'abonnement.

{% alert note %}
Braze a publié une amélioration de l'endpoint `/users/track` qui permet de mettre à jour le statut d'abonnement. Vous pouvez en savoir plus dans [Groupes d'abonnement]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status). Cependant, si vous avez déjà créé des protocoles d'abonnement en utilisant l'[endpoint `/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2), vous pouvez continuer à les utiliser.
{% endalert %}

### Méthodes d'abonnement externes à Braze {#external-to-braze-opt-in-methods}

Votre application ou site web (inscription de compte, page de paiement, paramètres du compte, terminal de carte bancaire) vers Braze.

Partout où vous disposez déjà du consentement marketing pour l'e-mail ou les SMS, incluez une section supplémentaire pour WhatsApp. Après qu'un utilisateur s'est abonné, il a besoin d'un `external_id`, d'un [numéro de téléphone]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) et d'un statut d'abonnement mis à jour. Pour ce faire, selon la configuration de votre installation Braze, utilisez soit l'[endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status), soit le [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Liste d'abonnement créée en externe {#externally-built-opt-in-list}

Si vous avez déjà utilisé WhatsApp, vous avez peut-être déjà constitué une liste d'utilisateurs avec des abonnements conformes aux exigences de WhatsApp. Dans ce cas, importez un CSV ou utilisez l'API avec les [informations suivantes]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) dans Braze.

#### Message sortant dans le canal de support client WhatsApp {#outbound-message-in-customer-support-whatsapp-channel}

Dans votre canal de support client, faites un suivi des problèmes résolus avec un message automatique demandant s'ils souhaitent s'abonner aux messages marketing. La fonctionnalité ici dépend des fonctionnalités disponibles dans l'outil de support client de votre choix et de l'endroit où vous conservez les informations utilisateur.

1. Fournissez un [lien de message](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) depuis votre numéro de téléphone WhatsApp Business.
2. Fournissez des [actions de réponse rapide]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies) où le client répond « Oui » pour indiquer son abonnement.
3. Configurez un déclencheur de mot-clé personnalisé.
4. Pour l'une ou l'autre de ces idées, vous devrez probablement terminer le parcours avec les éléments suivants :
	- Appeler l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour mettre à jour ou créer un utilisateur
	- Exploiter l'[endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) ou utiliser le [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### Message WhatsApp entrant {#inbound-whatsapp-message}

Demandez aux clients d'envoyer un message entrant au numéro WhatsApp.

Cela peut être configuré comme un Canvas ou une campagne, selon que vous souhaitez que l'utilisateur reçoive un message de confirmation sur le nouveau canal.

1. Créez une campagne avec le déclencheur de livraison par événement d'un message entrant.
2. Créez une campagne webhook. Pour un exemple de webhook, consultez [Groupes d'abonnement]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#step-2-update-the-users-profile).

{% alert tip %}
Notez que vous pouvez créer une URL ou un code QR pour rejoindre un canal WhatsApp depuis le [gestionnaire WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/) sous **Phone Number** > **Message Links**.<br>![Compositeur de code QR WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Méthodes d'abonnement via Braze {#braze-powered-opt-in-methods}

#### Message SMS {#sms-message}

Dans Canvas, configurez une campagne qui demande aux clients s'ils souhaitent s'abonner aux messages WhatsApp en utilisant l'une des méthodes suivantes :
- Segment de clients : groupe marketing abonné en dehors des États-Unis
- Configuration de déclencheur de mot-clé personnalisé

Découvrez comment mettre à jour le statut d'abonnement des profils utilisateur en consultant [Groupes d'abonnement]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

#### Message in-app ou dans le navigateur {#in-app-or-in-browser-message}

Créez un message in-app ou une fenêtre pop-up dans le navigateur invitant les clients à s'abonner à WhatsApp.

Utilisez un [message in-app HTML](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) avec le [pont JavaScript]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge) pour interagir avec le SDK Braze. Assurez-vous d'utiliser l'ID du groupe d'abonnement WhatsApp.

#### Formulaire de capture de numéro de téléphone {#phone-number-capture-form}

Utilisez le modèle de [formulaire de capture de numéro de téléphone]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture) dans l'éditeur par glisser-déposer pour les messages in-app afin de collecter les numéros de téléphone des utilisateurs et développer vos groupes d'abonnement WhatsApp.

## Configurer les désabonnements pour votre canal WhatsApp Braze {#set-up-opt-outs-for-your-braze-whatsapp-channel}

### Bouton « Offres et annonces » de WhatsApp {#whatsapp-offers-and-announcements-toggle}

WhatsApp propose un bouton « Offres et annonces » dans les paramètres de l'application qui permet aux utilisateurs de se désabonner des messages marketing. Ce bouton fonctionne indépendamment des groupes d'abonnement Braze :

- **Les groupes d'abonnement Braze** sont gérés via votre intégration Braze (API, centre de préférences ou SDK) et contrôlent les utilisateurs que vous ciblez pour l'envoi de messages.
- **Le bouton natif de WhatsApp** est contrôlé par Meta et appliqué au niveau de la plateforme, en dehors de Braze.

Ces deux couches ne se synchronisent pas automatiquement par conception. Lorsqu'un utilisateur désactive le bouton « Offres et annonces » dans WhatsApp, Meta bloque la distribution des messages marketing au niveau de la plateforme, même si le statut d'abonnement de l'utilisateur dans Braze indique « Subscribed ». La préférence de l'utilisateur est respectée au moment de la distribution.

{% alert note %}
Étant donné que Braze ne reçoit pas de signal de désabonnement tant qu'une tentative d'envoi n'a pas été effectuée et que Meta n'a pas renvoyé une erreur, les compteurs d'abonnement dans Braze peuvent ne pas refléter les utilisateurs qui se sont désabonnés via le bouton WhatsApp tant qu'un message n'a pas été tenté. Cela signifie que les estimations de portée peuvent être légèrement surestimées jusqu'à ce que cette boucle de rétroaction se produise.
{% endalert %}

### Mots-clés de désabonnement généraux {#general-opt-out-keywords}

Vous pouvez configurer une campagne ou un Canvas qui permet aux utilisateurs envoyant certains mots de se désabonner des futurs messages. Les Canvas peuvent être particulièrement utiles car ils vous permettent d'inclure un message de suivi confirmant le désabonnement réussi.

#### Étape 1 : Créer un Canvas avec un déclencheur « Message WhatsApp entrant » {#step-1-create-a-canvas-with-a-trigger-of-inbound-whatsapp-message}

![Étape d'entrée Canvas par événement qui fait entrer les utilisateurs qui envoient un message WhatsApp entrant.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Lors de la sélection des déclencheurs de mots-clés, incluez des mots comme « Stop » ou « Plus de message ». Si vous choisissez cette méthode, assurez-vous que vos clients connaissent vos mots de désabonnement. Par exemple, après avoir reçu l'abonnement initial, incluez une réponse de suivi comme « Pour vous désabonner de ces messages, envoyez "Stop" à tout moment. »

![Étape de message pour envoyer un message WhatsApp entrant où le corps du message est « STOP » ou « PLUS DE MESSAGE ».]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Étape 2 : Mettre à jour le profil de l'utilisateur {#step-2-update-the-users-profile}

Mettez à jour le profil de l'utilisateur en utilisant l'une des méthodes décrites dans [Groupes d'abonnement]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

### Sélection de désabonnement marketing {#marketing-opt-out-selection}

Dans le créateur de modèles de messages WhatsApp, vous pouvez inclure l'option « désabonnement marketing ». Chaque fois que vous incluez cette option, assurez-vous que le modèle est utilisé dans un Canvas avec une étape ultérieure pour un changement de groupe d'abonnement.

1. Créez un modèle de message avec la réponse rapide « désabonnement marketing ».<br>![Modèle de message avec une option de pied de page « Désabonnement marketing ».]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Section pour configurer un bouton de désabonnement marketing.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Créez un Canvas qui utilise ce modèle de message.<br><br>
3. Suivez les étapes de l'exemple précédent mais avec le texte déclencheur « STOP PROMOTIONS ».<br><br>
4. Mettez à jour le statut d'abonnement de l'utilisateur en utilisant l'une des méthodes décrites dans [Groupes d'abonnement]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

## Configurer les workflows d'abonnement et de désabonnement {#set-up-opt-in-and-opt-out-workflows}

Vous pouvez configurer des workflows de réponse aux mots-clés « START » et « STOP » pour WhatsApp avec ces deux méthodes :

- [Étape Mise à jour utilisateur](#user-update-step)
- [Campaign webhook pour déclencher une seconde campagne WhatsApp](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Étape Mise à jour utilisateur {#user-update-step}

L'[étape Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) peut ajouter le numéro de téléphone de l'utilisateur au groupe d'abonnement WhatsApp lorsque l'utilisateur envoie un mot-clé au numéro de téléphone du groupe d'abonnement.

L'étape Mise à jour utilisateur évite les conditions de concurrence car l'utilisateur ne passera pas à l'étape suivante du Canvas avant que son numéro de téléphone ne soit ajouté au groupe d'abonnement. Elle nécessite également moins d'étapes de configuration que les autres méthodes, c'est pourquoi Braze recommande généralement cette méthode.

1. Créez un Canvas avec l'étape par événement **Send a WhatsApp Inbound Message**. Sélectionnez **Where the message body** et saisissez « START » pour **Is**.

{% alert important %}
Pour les messages « STOP », inversez l'étape de message confirmant le désabonnement et l'étape Mise à jour utilisateur. Si vous ne le faites pas, l'utilisateur sera d'abord désabonné du groupe d'abonnement, puis ne sera plus éligible pour recevoir le message de confirmation.
{% endalert %}

![Une étape de message WhatsApp où le corps du message est « START ».]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. Dans le Canvas, créez une étape **Set Up User Update** et pour **Action**, sélectionnez **Advanced JSON Editor**. <br><br>![Étape Mise à jour utilisateur avec une action « Advanced JSON Editor ».]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3. Remplissez l'**objet User Update** avec le payload JSON suivant, en remplaçant `XXXXXXXXXXX` par l'ID de votre groupe d'abonnement :

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4. Ajoutez une étape de message WhatsApp ultérieure. <br><br>![Étape Mise à jour utilisateur dans un Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Considérations {#considerations}

La mise à jour peut s'effectuer à des vitesses variables car Braze regroupe les requêtes de l'[étape Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) par lots.

### Campaign webhook pour déclencher une seconde campagne WhatsApp {#webhook-campaign-to-trigger-a-second-whatsapp-campaign}

Une campagne webhook peut déclencher l'entrée dans une seconde campagne après avoir ajouté le numéro de téléphone de l'utilisateur au groupe d'abonnement WhatsApp lorsque l'utilisateur envoie un mot-clé au numéro de téléphone du groupe d'abonnement.

{% alert important %}
Vous n'avez pas besoin d'utiliser cette méthode pour les messages STOP. Le message de confirmation sera envoyé avant que l'utilisateur ne soit retiré du groupe d'abonnement, vous pouvez donc utiliser l'une des deux autres étapes.
{% endalert %}

1. Créez une campagne ou un Canvas avec une étape par événement **Send a WhatsApp Inbound Message**. Sélectionnez **Where the message body** et saisissez « START » pour **Is**.

![Étape de message WhatsApp où le corps du message est « START ».]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2. Dans la campagne ou le Canvas, créez une étape de message webhook et changez le **Request Body** en **Raw Text**.

![Étape de message pour un webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3. Saisissez l'[URL de l'endpoint]({{site.baseurl}}/api/basics) du client dans l'**URL du webhook**, suivie du lien de l'endpoint `campaigns/trigger/send`. Par exemple, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Champ URL du webhook sous la section « Rédiger le webhook ».]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4. Dans le texte brut, saisissez le payload JSON suivant et remplacez `XXXXXXXXXXX` par l'ID de votre groupe d'abonnement. Vous devrez remplacer le `campaign_id` après avoir créé votre seconde campagne.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5. Créez une campagne WhatsApp (votre seconde campagne) et définissez le déclencheur sur API. Assurez-vous de copier ce `campaign_id` dans le payload JSON de votre première campagne.

#### Considérations

- Les mises à jour d'attributs depuis le payload JSON du déclencheur API Canvas ne sont pas encore prises en charge, vous ne pouvez donc déclencher qu'une campagne WhatsApp pour le message de réponse WhatsApp (comme à l'étape 2).
- Un modèle WhatsApp doit être approuvé pour être envoyé comme message de réponse. En effet, une réponse rapide nécessite que le déclencheur de message entrant soit dans la même campagne ou le même Canvas. Si vous utilisez une [étape Mise à jour utilisateur](#user-update-step), vous pouvez envoyer un message de réponse rapide sans approbation de Meta.

## Comprendre la différence entre les modificateurs « expression régulière » et « est » {#understanding-the-difference-between-regex-and-is-modifiers}

Dans ce tableau, `STOP` est utilisé comme exemple de mot déclencheur pour illustrer le fonctionnement des modificateurs.

| Modificateur | Mot déclencheur | Action |
| --- | --- | --- |
| `Is` | `STOP` | Capture toute utilisation du mot entier « stop » quelle que soit la casse. Par exemple, cela capture « stop » mais pas « veuillez stop ». |
| `Matches regex` | `STOP` | Capture toute utilisation de « STOP » dans cette casse exacte. Par exemple, cela capture « STOP » et « VEUILLEZ STOP » mais pas « stop ». |
| `Matches regex` | `(?i)STOP(?-i)` | Capture toute utilisation de « STOP » quelle que soit la casse. Par exemple, cela capture « stop », « veuillez stop » et « n'arrêtez jamais de m'envoyer des messages ». |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comprendre la différence entre les modificateurs « expression régulière » et « est »" }