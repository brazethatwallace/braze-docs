---
nav_title: "Configuration"
article_title: "Configuration de WhatsApp"
alias: /partners/whatsapp/
description: "Cet article explique comment configurer le canal WhatsApp de Braze, y compris les conditions préalables et les prochaines étapes suggérées."
page_type: partner
search_tag: Partner
page_order: 0
channel:
  - WhatsApp
search_rank: 2
---

# Configuration de WhatsApp {#whatsapp-setup}

> [WhatsApp](https://www.whatsapp.com/) Business messaging est une plateforme populaire de messagerie pair-à-pair utilisée dans le monde entier, offrant aux entreprises une messagerie basée sur la conversation.

## Conditions préalables {#prerequisites}

Prenez connaissance des éléments suivants avant de procéder à l'intégration :

- **Politique d'abonnement :** WhatsApp exige que les entreprises obtiennent le consentement de leurs clients pour l'envoi de messages.
- **Règles de contenu WhatsApp :** WhatsApp a mis en place plusieurs [règles de contenu](https://www.whatsapp.com/legal/commerce-policy?l=en) qui doivent être respectées.
- **Conformité :** Respectez toute la documentation applicable de Braze et de Meta ainsi que toutes les [politiques Meta](https://www.whatsapp.com/legal/?lang=en) applicables.
- **Limites de conversation de 24 heures :** Après qu'une entreprise envoie un premier message basé sur un modèle ou qu'un utilisateur envoie un message, une fenêtre de 24 heures s'ouvre pendant laquelle les deux parties peuvent échanger des messages.
- **Initiation de la conversation :** Les utilisateurs peuvent initier une conversation à tout moment. Une entreprise ne peut initier une conversation que par le biais d'un modèle de message approuvé.
<br><br>

| Condition | Description |
| --- | --- |
| Compte Meta Business Manager | Un compte Meta Business est requis pour tirer parti de ce canal de communication. |
| Compte WhatsApp Business | Un compte WhatsApp Business est requis pour tirer parti de ce canal de communication. |
| Numéro de téléphone WhatsApp | Vous devez disposer d'un numéro de téléphone conforme aux exigences de WhatsApp pour l'[API Cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou l'[API On-Premises](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) afin d'utiliser le canal de communication. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Connecter WhatsApp Messenger à Braze {#step-1-connect-whatsapp-messenger-to-braze}

Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et recherchez **WhatsApp**.

Sur la page partenaire WhatsApp, sélectionnez **Begin Integration**.

![Page partenaire WhatsApp avec un bouton pour commencer l'intégration.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

Dans la fenêtre qui s'ouvre, sélectionnez **Next** jusqu'à ce que le bouton **Begin Integration** apparaisse. Sélectionnez le bouton pour lancer le processus d'intégration.

![Instructions pour connecter Braze à WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Étape 2 : Configuration de WhatsApp {#step-2-whatsapp-setup}

Ensuite, le flux de configuration de Braze vous guidera. Pour un guide étape par étape, consultez [Inscription intégrée WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

Au cours de ce flux, vous allez :
1. Créer ou sélectionner vos comptes Meta et WhatsApp Business. Assurez-vous de consulter les [directives relatives au nom d'affichage WhatsApp](https://www.facebook.com/business/help/757569725593362). <br><br>Il est probable que vous ayez déjà au moins un compte Meta Business existant dans votre entreprise. Si c'est le cas, sélectionnez celui dans lequel vous souhaitez héberger votre compte WhatsApp Business. Les autorisations utilisateur et la vérification de l'entreprise pour WhatsApp seront gérées de manière centralisée dans votre compte Meta Business.<br><br>
2. Créer votre profil WhatsApp Business.
3. Vérifier votre numéro WhatsApp Business.<br><br>

Une fois la configuration terminée, un [groupe d'abonnement WhatsApp]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#whatsapp-subscription-groups) dédié est créé pour vos utilisateurs.

### Étape 3 : Créer des modèles WhatsApp {#step-3-create-whatsapp-templates}

Seuls les modèles de messages WhatsApp approuvés peuvent être utilisés pour initier des conversations avec les clients. Les modèles WhatsApp peuvent être créés dans le [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343). Pour obtenir la liste des fonctionnalités de messagerie WhatsApp prises en charge par Braze, consultez [Fonctionnalités WhatsApp prises en charge]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#supported-whatsapp-features).

1. **Accédez au [gestionnaire de modèles](https://business.facebook.com/wa/manage/message-templates)**<br>
Dans le Meta Business Manager, sous **Account Tools**, sélectionnez **Message Templates**.
Ensuite, sélectionnez **Create Templates**.<br><br>![Gestionnaire WhatsApp avec une liste de modèles de messages.]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Paramètres du message**<br>
Dans le nouveau compositeur de modèles de messages, sélectionnez la catégorie de votre message, nommez votre modèle et choisissez les langues que vous souhaitez prendre en charge. Vous pouvez supprimer ou ajouter des langues ultérieurement.<br><br>
	Les catégories de modèles de messages disponibles sont les suivantes :
	- Marketing : envoyez des offres promotionnelles, des annonces de produits et plus encore pour accroître la visibilité et l'engagement.
	- Utilitaire : envoyez des mises à jour de compte, des mises à jour de commande, des alertes et plus encore pour partager des informations importantes.
	- Authentification : envoyez des codes permettant à vos clients d'accéder à leurs comptes.<br><br>
	![Compositeur de modèles de messages avec les catégories marketing, utilitaire et authentification.]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Modifier le modèle**<br>
Ensuite, créez votre modèle de message. <br><br>Vous pouvez fournir un en-tête texte ou média, le corps du texte, un pied de page et des boutons. Notez que les en-têtes vidéo et document ne sont pas disponibles actuellement, et les en-têtes doivent être de type texte ou image. Tout média que vous ajoutez sert d'exemple pour le processus de validation et **n'est pas** inclus dans le modèle de message. Les médias doivent être ajoutés dans Braze. Un aperçu de votre message s'affichera dans un panneau. <br><br>Bien que Meta ne prenne pas en charge Liquid, vous pouvez insérer des variables qui pourront être remplacées ultérieurement dans Braze par des variables Liquid. Sélectionnez le bouton **+ Add variable** pour ce faire.<br><br>![Compositeur de modèles.]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

Une fois votre modèle terminé, appuyez sur **Submit**.

#### Délai d'approbation des modèles {#template-approval-time}

Vous pouvez vérifier le statut d'approbation de votre modèle de message soit dans la page **Message Template** du Meta Business Manager, soit lors de la création d'une campagne ou d'un Canvas dans Braze. De plus, vous pouvez être notifié par e-mail par l'équipe WhatsApp en fonction de vos autorisations de notification.

{% alert note %}
Les modèles approuvés peuvent être utilisés dans autant de Campaigns et de Canvas que vous le souhaitez. Ils peuvent également être envoyés à autant d'utilisateurs abonnés que vous le souhaitez. Cela reste vrai tant que la qualité du modèle ne diminue pas.
{% endalert %}

### Étape 4 : Créer une campagne WhatsApp {#step-4-create-a-whatsapp-campaign}

Une fois les modèles WhatsApp approuvés, vous pouvez vous rendre sur le tableau de bord pour créer un [Canvas ou une campagne WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

{% alert note %}
Une fois votre compte WhatsApp Business créé, Meta déterminera votre limite de messages initiale. Pour en savoir plus, consultez la section [débit]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc#throughput).
{% endalert %}

## Étapes suivantes {#next-steps}

Après avoir terminé l'intégration, nous vous recommandons de compléter les deux processus Meta suivants :
- [Vérification de l'entreprise](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Vous disposez peut-être déjà de la vérification de l'entreprise si vous avez utilisé un Meta Business Manager existant.
- [Compte professionnel officiel](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

Nous vous recommandons également de consulter la documentation sur les [numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) et d'ajouter tous les utilisateurs qui auront besoin d'un accès pour créer des [modèles de messages au sein de votre organisation](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143).

### Stockage local de l'API Cloud WhatsApp {#whatsapp-cloud-api-local-storage}

Braze prend en charge le [stockage local de l'API Cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) de WhatsApp. Pour activer cette fonctionnalité, contactez votre gestionnaire du support client Braze.