---
nav_title: Campagnes API
article_title: Campagnes API
page_order: 5
description: "Cet article de référence explique comment générer un campaign_id à inclure dans vos appels API et comment configurer cette campagne."
page_type: reference
tool: Campaigns

---
# Campagnes API {#api-campaigns}

> Cet article de référence explique comment générer un `campaign_id` à inclure dans vos appels API et comment configurer cette campagne.

Les campagnes API sont généralement utilisées pour l'envoi de messages transactionnels. Lors de la création de campagnes API (et non de [campagnes déclenchées par l'API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)), le tableau de bord de Braze n'est utilisé que pour générer un `campaign_id`, qui vous permet de suivre l'analytique pour les rapports de campagne. Vous pouvez également générer un ID de variante de message, qui est différent pour chaque variante de votre campagne.

Vous enverrez ensuite ces informations à votre équipe de développement pour les utiliser dans la requête API, avec les éléments suivants :
- Contenu de la campagne
- Appartenance à l'audience
- Ressources

Après le début de la campagne, vous pouvez consulter les résultats dans le tableau de bord. Les campagnes API utilisent les [API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging) de Braze, qui disposent des mêmes options de reporting détaillé et de reciblage que les campagnes créées entièrement via le tableau de bord.

{% alert warning %}
Étant donné que les campagnes API sont généralement transactionnelles, tous les utilisateurs sont éligibles pour les campagnes API, y compris ceux de votre groupe de contrôle global. Un en-tête de [liste de désabonnement en un clic]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings#list-unsubscribe) n'est pas ajouté à ces envois. Si vous souhaitez ajouter un en-tête de liste de désabonnement en un clic à toutes les campagnes API, contactez votre gestionnaire du succès des clients.
{% endalert %}

## Créer une nouvelle campagne {#create-a-new-campaign}

Accédez à **Messaging** > **Campaigns** et sélectionnez **Create Campaign**, puis sélectionnez **API Campaigns**. Vous pouvez maintenant passer à la configuration de votre campagne API.

Une [campagne déclenchée par API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) est différente d'une campagne API.

## Configurer votre Campaign {#configure-your-campaign}

Pour configurer votre Campaign, effectuez les étapes suivantes :

1. Ajoutez un titre descriptif afin de pouvoir retrouver les résultats sur la page des Campaigns après l'envoi de vos messages.
2. Sélectionnez **Add Message** et ajoutez les types de messages inclus dans votre Campaign API. Cela vous permet de générer un `campaign_id` et un ID de variante de message, qui diffère pour chaque canal que vous incluez.
3. Vous pouvez éventuellement ajouter un événement de conversion pour suivre les conversions des utilisateurs sur une action ou un objectif de Campaign spécifique.
4. Sélectionnez **Save Campaign** et vous êtes prêt à lancer votre Campaign API !

## Appels API {#api-calls}

Après avoir enregistré votre Campaign API, incluez les éléments suivants dans votre requête API :
- Les champs `campaign_id` générés avec votre requête API, comme indiqué dans les [endpoints d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging).
- Un [objet message]({{site.baseurl}}/api/objects_filters#messaging-objects) pour chaque plateforme incluse dans la Campaign. Dans l'objet message, fournissez l'ID de variante du message. Cela indique que les statistiques doivent être collectées et affichées sous cette variante. Les objets message suivants sont pris en charge : Android, Content Cards, e-mail, iOS, Kindle, SMS/MMS, notification push Web et webhook.

### Ajouter des pièces jointes aux e-mails {#adding-email-attachments}

Pour ajouter des pièces jointes aux e-mails d'une Campaign API, incluez un tableau `attachments` dans l'[objet e-mail]({{site.baseurl}}/api/objects_filters/messaging/email_object). Vous pouvez référencer un modèle d'e-mail créé dans l'éditeur par glisser-déposer ou l'éditeur HTML en fournissant son `email_template_id` dans l'objet e-mail, puis ajouter des pièces jointes via l'appel API.

Pour plus de détails sur les pièces jointes, les limites de taille et les bonnes pratiques, consultez [Exemple d'objet e-mail avec pièce jointe]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment).