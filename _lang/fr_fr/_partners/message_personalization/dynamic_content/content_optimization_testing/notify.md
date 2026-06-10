---
nav_title: Notify
article_title: Notify
description: "Cet article de référence présente le partenariat entre Braze et Notify, une solution de personnalisation omnicanale en temps réel qui offre une personnalisation tout au long du cycle de vie du client."
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Notify

> [Notify](https://fr.notify-group.com/) est une solution logicielle basée sur l'intelligence artificielle qui s'intègre de façon fluide aux outils de gestion de la relation client afin d'améliorer les stratégies marketing et de faciliter l'engagement sur plusieurs canaux.

L'intégration de Braze et Notify permet aux marketeurs de stimuler efficacement l'engagement sur différentes plateformes. Au lieu de s'appuyer sur les méthodes de marketing traditionnelles, une Campaign Braze déclenchée par API peut utiliser les capacités de Notify pour diffuser des messages personnalisés via plusieurs canaux, notamment les e-mails, les SMS, les notifications push, etc.

## Conditions préalables {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

| Exigence | Description |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Clé REST API Braze | Une clé REST API Braze avec les autorisations `users.export.segment` et `campaigns.trigger.send`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Configuration du CNAME | Un sous-domaine doit être créé pour le pixel de suivi utilisé dans l'e-mail afin que Notify puisse suivre l'engagement des utilisateurs avec les messages et ainsi alimenter le modèle. Partagez l'URL du sous-domaine avec Notify après sa création. |
| Exportation de la base de données d'abonnement | Envoyez à Notify les données relatives aux campagnes et aux achats de l'année écoulée (12 mois). ​Cette exportation sera utilisée pour entraîner le modèle prédictif de Notify. <br><br> **Champs :** <br><br> **E-mail :** Un hachage SHA256 de l'e-mail, converti en minuscules et dont les espaces de début et de fin ont été supprimés.<br><br>**Segment :** Les informations de segment définissant le niveau d'activité (actif ou inactif).<br><br>**Sous-segment :** Toute autre information pertinente sur l'activité, telle que le niveau d'activité d'achat.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Créer votre Campaign {#step-1-create-your-campaign}

Créez une [Campaign déclenchée par API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) dans Braze. Partagez ensuite l'identifiant `api_identifier` de la Campaign avec Notify.

### Étape 2 : Créer votre segment dans Braze {#step-2-create-your-segment-in-braze}

Ensuite, créez le segment d'utilisateurs que vous souhaitez cibler avec la Campaign créée à l'[étape 1](#step-1-create-your-campaign). Partagez ensuite l'ID du segment avec Notify.

### Étape 3 : Récupérer votre segment {#step-3-fetch-your-segment}

Notify exportera alors les utilisateurs du segment rattaché à la Campaign.

### Étape 4 : Notify déclenche la Campaign {#step-4-notify-triggers-the-campaign}

À l'aide de l'endpoint `/campaigns/trigger/send`, l'intelligence artificielle de Notify déclenche la Campaign Braze créée à l'[étape 1](#step-1-create-your-campaign) pour l'envoyer aux utilisateurs au moment jugé le plus propice à l'engagement.