À compter du 1er juillet 2025, WhatsApp facture désormais par message. Les tarifs des messages sont basés à la fois sur l'indicatif pays du numéro de téléphone du destinataire et sur le type de message que vous envoyez. Le type de message est déterminé à partir du [modèle de message](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) que vous soumettez pour approbation dans WhatsApp gestionnaire.

{% alert note %}
Toutes les conversations initiées par l'entreprise sur la plateforme doivent commencer par un modèle de message approuvé.
{% endalert %}

{% if include.content == "h2" %}##{% else include.content == "h3" %}###{% endif %} Définitions des modèles de message

Voici les modèles de message que vous pouvez soumettre pour approbation dans WhatsApp gestionnaire :

| Modèle | Définition |
|----------|------------|
| **Modèle marketing**     | Ce modèle vous permet d'atteindre un large éventail d'objectifs, de la sensibilisation à la stimulation des ventes en passant par le reciblage des clients. Exemples : annonces de nouveaux produits, services ou fonctionnalités, promotions ou offres ciblées, et rappels d'abandon de panier. |
| **Modèle utilitaire**       | Ce modèle vous permet de donner suite aux actions ou demandes des utilisateurs, car ces messages sont généralement déclenchés par des actions utilisateur. Exemples : confirmation d'abonnement, gestion des commandes ou de la réception (comme les mises à jour de livraison), mises à jour ou alertes de compte (comme les rappels de paiement), ou enquêtes de satisfaction.<br><br>À compter du 1er juillet 2025 :<br>• Les modèles utilitaires doivent être non promotionnels et sans aucune intention persuasive.<br>• Les modèles utilitaires doivent être soit (1) spécifiques à l'utilisateur ou demandés par celui-ci, soit (2) essentiels ou critiques pour l'utilisateur. |
| **Modèle d'authentification** | Ce modèle vous permet de vérifier l'identité d'un utilisateur, potentiellement à différentes étapes du parcours client (comme la vérification de compte, la récupération de compte et les défis d'intégrité).<br><br>Les conversations d'authentification ne seront prises en charge qu'au cas par cas et Braze ne peut pas garantir de SLA spécifiques. De plus, Braze ne prend pas en charge la génération de codes PIN. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% if include.content == "h2" %}##{% else include.content == "h3" %}###{% endif %} Types de messages gratuits

Voici quelques scénarios dans lesquels votre message WhatsApp sera gratuit :

| Message | Détails |
|-------|-------|
| Toutes les conversations de service | _À compter du 1er novembre 2024_<br><br>Lorsqu'un utilisateur envoie un message à votre marque (ouvrant la fenêtre de service client de 24 heures), les messages de réponse non basés sur un modèle ne sont pas facturés. Remarque : si votre marque répond à l'utilisateur avec un modèle, vous serez tout de même facturé en fonction du type de modèle. |
| Modèles utilitaires envoyés pendant une fenêtre de service client de 24 heures | _À compter du 1er juillet 2025_<br><br>Une fenêtre de service client de 24 heures est créée lorsqu'un utilisateur final envoie un message à votre marque. Si votre marque répond avec un modèle utilitaire, celui-ci sera gratuit. Les modèles utilitaires envoyés en dehors d'une fenêtre de service client de 24 heures (par exemple, les modèles utilitaires envoyés de manière proactive par votre marque pour des rappels de compte ou des mises à jour du statut de la commande) seront toujours facturés. |
| Conversations gratuites par point d'entrée | Une conversation gratuite par point d'entrée est ouverte si 1) un utilisateur envoie un message à votre marque via une publicité Click to WhatsApp ou un bouton d'appel à l'action de page Facebook, et 2) votre marque répond dans les 24 heures. La conversation gratuite par point d'entrée est ouverte dès que votre marque répond et dure 72 heures. Pendant la fenêtre de 72 heures, votre marque peut envoyer des modèles de message aux utilisateurs gratuitement. Cependant, votre marque ne peut envoyer des messages non basés sur un modèle que s'il existe une fenêtre de service client de 24 heures ouverte. |
| Messages de réponse | L'envoi de messages de réponse permet à votre marque d'envoyer des messages non basés sur un modèle en réponse aux messages des utilisateurs. Les messages de réponse peuvent être envoyés lorsqu'il existe une fenêtre de service client de 24 heures ouverte, par exemple lorsqu'un utilisateur envoie un message à votre marque sur WhatsApp.<br><br>Gardez à l'esprit que le modèle de message qui initie la conversation sera toujours facturé, mais les messages de réponse suivants seront gratuits. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}