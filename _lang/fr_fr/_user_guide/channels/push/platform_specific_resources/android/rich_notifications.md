---
nav_title: Créer des notifications enrichies
article_title: "Création de notifications push enrichies pour Android"
page_order: 3
page_layout: tutorial
description: "Ce tutoriel explique comment configurer les notifications enrichies Android pour vos campagnes Braze."
platform: Android
channel:
  - Push
tool:
  - Campaigns

---

# Créer des notifications push enrichies pour Android {#create-rich-push-notifications-for-android}

> Les notifications enrichies permettent une plus grande personnalisation de vos notifications push en ajoutant du contenu supplémentaire au-delà du simple texte. Les notifications Android incluent depuis un certain temps des images dans les notifications push, appelées « image de notification étendue ».

## Conditions préalables {#prerequisites}

Avant de créer une notification push enrichie pour Android, notez les détails suivants :

- Les images de notification étendue Android doivent avoir un rapport hauteur/largeur de 2:1, mais n'ont pas de limite de taille.
- Android permet également de définir une image distincte pour la vue de notification standard. Voici les tailles d'images recommandées :
  - **Petite :** 512x256
  - **Moyenne :** 1024x512
  - **Grande :** 2048x1024
- Actuellement, les notifications enrichies Android ne prennent en charge que les images statiques, y compris les formats d'image JPEG et PNG. Les GIF et autres formats d'image ne sont pas encore pris en charge.
- L'ajout de boutons d'action à votre notification push peut affecter la zone de l'image affichable. Testez avec la prévisualisation du tableau de bord et des appareils réels pour confirmer que les résultats correspondent à vos attentes.
- Le SDK Braze pour Android doit être activé pour que l'image s'affiche.

{% alert note %}
Bien que Braze fournisse des instructions sur la configuration des notifications push enrichies, le rendu réel de ces notifications peut varier en fonction de facteurs externes tels que le rapport hauteur/largeur de l'appareil, la version d'Android, les contraintes spécifiques au fabricant, etc. Nous recommandons d'effectuer un envoi test vers plusieurs appareils Android pour vous assurer que vos notifications push enrichies s'affichent comme prévu.
{% endalert %}

## Configuration de votre notification enrichie Android {#setting-up-your-android-rich-notification}

### Étape 1 : Créer une campagne push {#step-1-create-a-push-campaign}

Suivez les étapes pour [créer une campagne]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#creating-a-push-message) afin de composer une notification push pour Android. Vous utiliserez le même composeur pour configurer les notifications push qui ne contiennent pas de contenu enrichi.

### Étape 2 : Ajouter un sous-titre {#step-2-add-captioning}

Ajoutez le **Summary Text** que vous souhaitez afficher avant l'image dans la notification.

![Une notification push enrichie provenant d'une application de nourriture pour animaux appelée Dog indiquant qu'il est temps de commander plus de nourriture pour Spot avec un texte de résumé.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Étape 3 : Ajouter un média {#step-3-add-media}

Ajoutez votre image dans le champ **Android Notification Image** dans le composeur du message. Les images peuvent être téléchargées directement via le tableau de bord ou en spécifiant une URL de contenu hébergée ailleurs.

Pour plus de détails sur les images prises en charge, consultez les [spécifications d'image]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#push).

![La section d'image de notification Android où vous pouvez ajouter une image ou saisir une URL d'image.]({% image_buster /assets/img_archive/android_rich_image.png %})

### Étape 4 : Continuer la création de votre campagne {#step-4-continue-creating-your-campaign}

Une fois le contenu de votre notification enrichie téléchargé dans le tableau de bord, vous pouvez continuer à [planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).