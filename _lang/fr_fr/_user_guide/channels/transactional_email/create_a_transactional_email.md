---
nav_title: "Créer un e-mail transactionnel"
article_title: "Créer un e-mail transactionnel"
page_order: 1

description: "Cet article de référence explique comment créer et configurer une nouvelle campagne d'e-mail transactionnel Braze."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Créer un e-mail transactionnel {#create-a-transactional-email}

> Les e-mails transactionnels Braze sont envoyés pour faciliter une transaction convenue entre un expéditeur et le destinataire. Cet article de référence explique comment créer une campagne d'e-mail transactionnel dans le tableau de bord de Braze et générer un `campaign_id` à inclure dans vos appels API pour notre [endpoint `/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/).

{% alert important %}
L'e-mail transactionnel Braze est uniquement disponible dans le cadre de certains forfaits Braze. Contactez votre gestionnaire de la satisfaction client Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) pour plus de détails.
{% endalert %}

Le type de campagne d'e-mail transactionnel est spécialement conçu pour envoyer des messages e-mail automatisés et non promotionnels afin de faciliter une transaction convenue entre vous et vos clients. Cela inclut des informations telles que :

- Les confirmations de commande
- Les réinitialisations de mot de passe
- Les alertes de facturation
- Les alertes d'expédition

En résumé, vous pouvez utiliser les e-mails transactionnels pour envoyer des notifications critiques provenant de votre service à un seul utilisateur, lorsque la rapidité est de la plus haute importance.

{% alert important %}
Les e-mails transactionnels diffèrent des campagnes transactionnelles, qui peuvent être utilisées pour cibler vos utilisateurs sans coûts supplémentaires. Les campagnes transactionnelles peuvent, par exemple, inclure des messages envoyés après qu'un utilisateur a ajouté un article à son panier. Consultez les [options de ciblage d'audience]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) pour plus d'informations.
{% endalert %}

{% alert note %}
Les envois via l'API d'e-mail transactionnel prennent en charge l'archivage des messages. Si l'archivage des messages est activé pour les e-mails dans votre espace de travail, Braze enregistre une copie rendue de chaque envoi d'e-mail transactionnel. Pour plus d'informations, consultez [Archivage des messages]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving/).
{% endalert %}

## Étape 1 : Créer une nouvelle campagne {#step-1-create-a-new-campaign}

Pour créer une nouvelle campagne d'e-mail transactionnel, créez une campagne et sélectionnez **Transactional Email** comme canal de communication.

![Menu déroulant Créer une campagne avec l'option e-mail transactionnel mise en évidence.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Vous pouvez maintenant passer à la configuration de votre campagne d'e-mail transactionnel.

## Étape 2 : Configurer votre campagne {#step-2-configure-your-campaign}

Le flux de création de campagne pour les campagnes d'e-mail transactionnel est simplifié par rapport à celui d'une [campagne e-mail standard]({{site.baseurl}}/user_guide/channels/email/html_editor/) afin de garantir que vos e-mails transactionnels critiques puissent atteindre tous les utilisateurs.

Par conséquent, vous remarquerez que plusieurs paramètres que vous connaissez peut-être d'autres types de campagnes Braze ne sont pas requis lors de la configuration de ce type de campagne :

- L'étape **Delivery** a été simplifiée pour supprimer les options de planification. Les e-mails transactionnels seront toujours déclenchés via la REST API Braze en utilisant l'ID de campagne affiché sur la page **Delivery**. Des paramètres supplémentaires, comme les contrôles de rééligibilité et les paramètres de limite de fréquence, ont également été supprimés pour confirmer que tous les utilisateurs sont joignables pour ces alertes transactionnelles critiques lorsque votre service déclenche une demande d'envoi.
- L'étape **Target Audiences** a été supprimée. Comme les e-mails transactionnels inscrivent l'ensemble de votre base d'utilisateurs comme éligible (y compris les utilisateurs désabonnés), il n'est pas nécessaire de spécifier des filtres ou des segments. Par conséquent, si vous avez une logique à appliquer pour déterminer qui doit recevoir ce message, nous vous recommandons d'appliquer cette logique avant de décider s'il faut effectuer la requête API à Braze pour déclencher le message à un utilisateur spécifique.
- L'étape **Conversions** a été supprimée. Les e-mails transactionnels ne prennent pas en charge le suivi des événements de conversion pour le moment.

![Flux de travail Rédiger, Réception et Confirmer pour créer une campagne d'e-mail transactionnel.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

Pour configurer votre campagne d'e-mail transactionnel, suivez ces étapes :

1. Ajoutez un nom descriptif afin de pouvoir retrouver les résultats sur votre page **Campaigns** après l'envoi de vos messages.
2. Rédigez votre e-mail ou sélectionnez un modèle.
3. Notez votre `campaign_id`. Après avoir enregistré votre campagne API, vous devez inclure les champs `campaign_id` générés dans votre requête API, comme indiqué dans l'article sur l'[endpoint d'e-mail transactionnel]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/).
4. Cliquez sur **Save Campaign**, et vous êtes prêt à lancer votre campagne API !

{% alert note %}
Le paramètre de désabonnement en un clic pour les campagnes d'e-mail transactionnel est défini par défaut sur **Use workspace default**, comme pour les autres campagnes e-mail. Comme il s'agit d'un envoi de messages transactionnels, Braze n'ajoute pas de désabonnement en un clic. Pour ajouter un désabonnement en un clic à ce type de campagne, [modifiez ce paramètre]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#message-level-one-click-list-unsubscribe) sous **Sending Info**.
{% endalert %}

### Étiquettes non autorisées dans les e-mails transactionnels {#disallowed-tags-in-transactional-emails}

Les étiquettes Liquid `Connected Content` et `Promotion Code` ne sont pas disponibles dans les campagnes d'e-mail transactionnel.

L'utilisation de l'étiquette `Connected Content` nécessite que Braze effectue une requête API sortante pendant notre processus d'envoi, ce qui peut ralentir le processus d'envoi des messages si le service externe sollicité connaît de la latence. De même, l'étiquette `Promotion Code` nécessite que Braze effectue un traitement supplémentaire pour évaluer la disponibilité d'un code de promotion avant l'envoi, ce qui peut ralentir le processus d'envoi si aucun code n'est disponible.

Par conséquent, nous ne prenons pas en charge l'inclusion des étiquettes `Connected Content` ou `Promotion Code` dans aucun champ de votre campagne d'e-mail transactionnel.