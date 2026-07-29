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

Envoyez ces informations à votre équipe de développement pour les utiliser dans la requête API, avec les éléments suivants :
- Contenu de la campagne
- Appartenance à l'audience
- Ressources

Après le début de la campagne, vous pouvez consulter les résultats dans le tableau de bord. Les campagnes API utilisent les [API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging) de Braze, qui disposent des mêmes options de reporting détaillé et de reciblage que les campagnes créées entièrement via le tableau de bord.

{% alert warning %}
Étant donné que les campagnes API sont généralement transactionnelles, tous les utilisateurs sont éligibles pour les campagnes API, y compris ceux de votre groupe de contrôle global. Un en-tête de [liste de désabonnement en un clic]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings#list-unsubscribe) n'est pas ajouté à ces envois par défaut. Pour ajouter un en-tête de liste de désabonnement en un clic à une campagne API, consultez [Ajouter la liste de désabonnement en un clic aux campagnes API](#add-one-click-list-unsubscribe-to-api-campaigns). Pour ajouter un en-tête de liste de désabonnement en un clic à toutes les campagnes API, contactez votre gestionnaire du succès des clients.
{% endalert %}

## Créer une nouvelle campagne {#create-a-new-campaign}

Accédez à **Messaging** > **Campaigns** et sélectionnez **Create Campaign**, puis sélectionnez **API Campaigns**. Vous pouvez maintenant passer à la configuration de votre campagne API.

Une [campagne déclenchée par l'API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) est différente d'une campagne API.

## Configurer votre campagne {#configure-your-campaign}

Pour configurer votre campagne, effectuez les étapes suivantes :

1. Ajoutez un titre descriptif afin de pouvoir retrouver les résultats sur la page des campagnes après l'envoi de vos messages.
2. Sélectionnez **Add Message** et ajoutez les types de messages inclus dans votre campagne API. Cela vous permet de générer un `campaign_id` et un ID de variante de message, qui diffère pour chaque canal que vous incluez.
3. Vous pouvez éventuellement ajouter un événement de conversion pour suivre les conversions des utilisateurs sur une action ou un objectif de campagne spécifique.
4. Sélectionnez **Save Campaign** pour lancer votre campagne API.

## Appels API {#api-calls}

Après avoir enregistré votre campagne API, incluez les éléments suivants dans votre requête API :

- Les champs `campaign_id` générés avec votre requête API, comme indiqué dans les [endpoints d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging).
- Un [objet message]({{site.baseurl}}/api/objects_filters#messaging-objects) pour chaque plateforme incluse dans la campagne. Dans l'objet message, fournissez l'ID de variante du message. Cela indique que les statistiques doivent être collectées et affichées sous cette variante. Les objets message suivants sont pris en charge : Android, Content Cards, e-mail, iOS, Kindle, SMS/MMS, notification push Web et webhook.

## Ajouter la liste de désabonnement en un clic aux campagnes API {#add-one-click-list-unsubscribe-to-api-campaigns}

{% raw %}
Par défaut, Braze n'ajoute pas l'en-tête de liste de désabonnement en un clic aux campagnes API. Vous pouvez ajouter cet en-tête à des envois individuels de campagnes API en incluant l'étiquette Liquid `{{${set_user_to_one_click_list_unsubscribe}}}` dans le champ des en-têtes d'e-mail de votre requête API.
{% endraw %}

Pour respecter la norme [RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058) relative à la liste de désabonnement en un clic, incluez les en-têtes `List-Unsubscribe` et `List-Unsubscribe-Post` dans votre requête API :

{% raw %}
```json
{
  "external_user_ids": ["user_id"],
  "messages": {
    "email": {
      "app_id": "your_app_id",
      "subject": "Your Subject",
      "from": "Sender Name <sender@example.com>",
      "body": "<p>Email body content</p>",
      "headers": {
        "List-Unsubscribe": "<{{${set_user_to_one_click_list_unsubscribe}}}>",
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
      }
    }
  }
}
```
{% endraw %}

{% alert note %}
L'inclusion de ces en-têtes ne garantit pas que le client de messagerie affiche un bouton de désabonnement. Les clients de messagerie décident d'afficher ou non l'option de désabonnement en fonction de facteurs tels que la réputation de l'expéditeur et le contenu du message.
{% endalert %}

### Ajouter des pièces jointes aux e-mails {#add-email-attachments}

Pour ajouter des pièces jointes aux e-mails d'une campagne API, incluez un tableau `attachments` dans l'[objet e-mail]({{site.baseurl}}/api/objects_filters/messaging/email_object). Vous pouvez référencer un modèle d'e-mail créé dans l'éditeur par glisser-déposer ou l'éditeur HTML en fournissant son `email_template_id` dans l'objet e-mail, puis ajouter des pièces jointes via l'appel API.

Pour plus de détails sur les pièces jointes, les limites de taille et les bonnes pratiques, consultez [Exemple d'objet e-mail avec pièce jointe]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment).