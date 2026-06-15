---
nav_title: Swym
article_title: Swym
description: "Cet article de référence présente le partenariat entre Braze et Swym, qui permet aux acheteurs d'enregistrer des produits et de poursuivre sans heurts leur parcours sur les sites web, les applications mobiles et les magasins physiques."
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# Swym

> [Swym](https://getswym.com/) aide les marques d'e-commerce à capturer l'intention d'achat grâce aux listes de souhaits, à la fonctionnalité Enregistrer pour plus tard, au registre de cadeaux et aux alertes de retour en stock. En exploitant des données riches et basées sur les autorisations, vous pouvez élaborer des campagnes hyperciblées et proposer des expériences d'achat personnalisées qui stimulent l'engagement, augmentent les conversions et renforcent la fidélisation.

*Cette intégration est maintenue par Swym.*

## À propos de l'intégration {#about-the-integration}

L'intégration de Swym et Braze vous permet de proposer des campagnes marketing personnalisées et événementielles qui convertissent l'intention des acheteurs en ventes. Utilisez l'intégration pour que les acheteurs puissent reprendre là où ils se sont arrêtés, collaborer avec d'autres personnes tout au long de leur parcours d'achat et recevoir des campagnes de reciblage performantes.

## Conditions préalables {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Prérequis | Description |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym | Les applications Swym Wishlist Plus, Back in Stock, ou les deux doivent être installées sur votre plateforme e-commerce (Shopify ou BigCommerce), et vous devez disposer du plan Enterprise. |
| Une clé REST API de Braze | Une clé REST API de Braze avec les autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Un endpoint REST de Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'utilisation {#use-cases}

En connectant les applications Wishlist Plus et Back in Stock Alerts de Swym avec Braze, vous pouvez envoyer automatiquement les événements liés à l'activité des acheteurs — tels que les ajouts à la liste de souhaits, les abonnements de retour en stock, les alertes de baisse de prix et les rappels — dans Braze en tant qu'événements personnalisés. Ces événements peuvent ensuite être utilisés pour déclencher des messages automatisés dans Braze, facilitant ainsi une communication opportune, pertinente et engageante qui incite les acheteurs à revenir pour effectuer un achat.

## Intégration de Swym {#integrating-swym}

### Étape 1 : Connecter votre application Swym à Braze {#step-1-connect-your-swym-app-to-braze}

Actuellement, l'intégration de Braze avec Swym est une intégration gérée et n'est pas en libre-service. Pour commencer, contactez l'équipe d'assistance de Swym à l'adresse [support@getswym.com](mailto:support@getswym.com) et fournissez les informations suivantes afin que Swym puisse mettre en place l'intégration en votre nom :

1. Générez une [clé REST API]({{site.baseurl}}/api/basics/#about-rest-api-keys) dans votre tableau de bord de Braze avec l'autorisation `users.track`.

![Génération d'une clé API dans Braze.]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
Pour protéger vos clés API, Swym vous recommande de partager les identifiants de manière sécurisée à l'aide d'un outil de lien unique et autodestructeur (par exemple, [OneTimeSecret](https://onetimesecret.com/)).
{% endalert %}

{: start="2"}
2. Braze gère plusieurs instances pour son tableau de bord et ses endpoints REST. Fournissez l'[endpoint REST]({{site.baseurl}}/api/basics/#endpoints) correspondant à l'instance qui vous a été attribuée.

3. Une fois la clé API et l'URL de l'instance partagées avec l'équipe d'assistance de Swym, celle-ci mettra en place l'intégration pour vous et vous enverra une confirmation.

4. Une fois la configuration terminée, les événements personnalisés de Swym seront automatiquement enregistrés dans Braze. Vous pouvez consulter la liste des événements Swym enregistrés dans le tableau de bord de Braze en accédant à **Paramètres des données** > **Événements personnalisés**.

5. Consultez les propriétés de chaque événement Swym en sélectionnant **Gérer les propriétés** pour l'événement personnalisé correspondant. Ces propriétés contiennent les valeurs d'événement qui peuvent être utilisées pour personnaliser vos messages.

![Propriétés personnalisées dans Braze.]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### Étape 2 : S'abonner aux événements que vous souhaitez envoyer à Braze {#step-2-subscribe-to-events-you-want-to-send-to-braze}

Depuis votre application Wishlist Plus, accédez à l'onglet **Marketing** et trouvez la section **Automations**. Vous pouvez y sélectionner les événements auxquels vous souhaitez vous abonner.

![Événements auxquels s'abonner.]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Événements de l'application Swym Wishlist Plus {#swym-wishlist-plus-app-events}

| Nom de l'événement | Quand cet événement est déclenché |
|------------|------------------------------|
| Share Wishlist | Lorsqu'un acheteur partage une liste de souhaits avec quelqu'un d'autre |
| Add to Wishlist | Lorsqu'un acheteur ajoute un article à sa liste de souhaits |
| Wishlist Reminder | Rappel concernant les articles figurant dans la liste de souhaits d'un acheteur |
| Saved for Later Reminder | Rappel concernant les articles enregistrés pour plus tard d'un acheteur |
| Price Drop alert | Un produit d'une liste de souhaits est mis en promotion |
| Low Stock alert | Un produit d'une liste de souhaits est bientôt en rupture de stock |
| Back in Stock alert | Un produit d'une liste de souhaits est réapprovisionné |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Événements de l'application Swym Wishlist Plus" }

#### Événements de l'application Swym Back in Stock Alerts {#swym-back-in-stock-alerts-app-events}

| Nom de l'événement | Quand cet événement est déclenché |
|------------|------------------------------|
| Back in Stock Acknowledgment | L'acheteur s'abonne pour être informé du retour en stock d'un produit |
| Restock Alert | Le produit pour lequel un acheteur a demandé une alerte de retour en stock est réapprovisionné |
| Restock Reminder | Alerte de suivi (généralement environ 24 heures après la première alerte de réapprovisionnement, configurable) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Événements de l'application Swym Back in Stock Alerts" }

### Étape 3 : Créer une campagne ou un Canvas dans Braze {#step-3-create-a-braze-campaign-or-canvas}

Pour automatiser la distribution de messages personnalisés à vos acheteurs, vous devez créer une campagne ou un Canvas distinct dans Braze pour chaque événement auquel vous êtes abonné. Chaque campagne ou Canvas doit être configuré pour se déclencher en fonction de l'événement spécifique et utiliser les propriétés d'événement correspondantes pour alimenter le contenu dynamique de vos messages. Pour des instructions étape par étape, vous pouvez consulter [Premiers pas : campagnes et Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases/).

![Un événement basé sur une action.]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

Pour plus de détails, consultez le [centre d'aide de Swym](https://help.getswym.com/en/articles/12344153-braze-integration) ou contactez l'équipe d'assistance de Swym à l'adresse [support@getswym.com](mailto:support@getswym.com).