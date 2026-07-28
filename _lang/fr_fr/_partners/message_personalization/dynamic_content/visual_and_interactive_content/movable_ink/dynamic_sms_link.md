---
nav_title: Aperçu du lien SMS dynamique
article_title: Aperçu du lien SMS dynamique
description: "Cet article de référence explique comment activer et utiliser la fonctionnalité d'aperçu de lien SMS de Movable Ink."
page_type: partner
search_tag: Partner
---

# Aperçu du lien SMS dynamique {#dynamic-sms-link-preview}

> Avec l'aperçu de lien SMS dynamique de Movable Ink, vous pouvez tirer parti de l'immersion du MMS au même coût que le SMS. Cela vous permet d'utiliser Braze et Movable Ink pour offrir des expériences de communication riches, personnalisées et rentables.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Movable Ink | Un compte Movable Ink est nécessaire pour bénéficier de ce partenariat. |
| Source de données | Vous devez connecter une source de données à Movable Ink. Cela peut être fait via un fichier CSV, l'importation de site web ou une API. |
| Capacités d'envoi de MMS | Confirmez que vous êtes configuré pour le MMS via Braze. |
| [Raccourcissement de lien]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) | Confirmez que le raccourcissement des liens est activé. |
| Carte de contact | Votre marque (l'expéditeur) doit être enregistrée en tant que contact sur le téléphone de l'utilisateur pour que l'aperçu du lien fonctionne avec iOS. Cela peut être fait avec une carte de contact ou une autre méthode. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Suivez les étapes correspondantes dans cette section pour envoyer des liens SMS dynamiques pour les systèmes d'exploitation iOS et Android.

### iOS

{% alert important %}
Pour autoriser les images d'aperçu de lien sur iOS, les utilisateurs doivent ajouter votre marque (l'expéditeur) en tant que contact.
{% endalert %}

#### Étape 1 : Créer une campagne de carte de contact {#step-1-create-a-contact-card-campaign}

Une fois que les utilisateurs ont enregistré votre marque en tant que contact, que ce soit par le biais d'une [carte de contact]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card) ou d'une autre méthode, ils pourront voir les invites **Tap to Load Preview** et les liens Movable Ink.

![1]{: style="max-width:30%;"}

#### Étape 2 : Envoyer des liens Movable Ink {#step-2-send-movable-ink-links}

1. Créez une campagne SMS dans Movable Ink et générez votre URL de clic.
2. Dans le tableau de bord de Braze, accédez à **Campaigns** et configurez une nouvelle campagne SMS/MMS à partir du menu déroulant **Create Campaign**.
3. Dans le compositeur de campagne SMS :
    - Définissez votre groupe d'abonnement.
    - Saisissez votre message.
    - Ajoutez votre lien Movable Ink **en dernier**, après tout autre texte dans le corps du message. <br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
Consultez [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) pour un rappel sur la personnalisation Liquid.
{% endalert %}

{: start="4"}
4. Vous êtes prêt à tester et lancer votre campagne d'aperçu de lien SMS dynamique.

![3]{: style="max-width:70%;"}

Une fois que les utilisateurs ont chargé l'aperçu du lien, une image personnalisée s'affiche avec la possibilité de rediriger vers votre site web, votre application ou votre page de destination.

![4]{: style="max-width:30%;"}

### Android (appareils Google et Samsung) {#android-google-and-samsung-devices}

Les utilisateurs Android ne sont pas tenus d'enregistrer votre marque en tant que contact pour recevoir des aperçus de liens SMS dynamiques. Cependant, il est toujours recommandé de le faire afin que l'appareil puisse charger automatiquement les aperçus de liens.

![5]{: style="max-width:30%;"}

Les utilisateurs qui n'ont pas enregistré votre marque en tant que contact et qui ont activé les aperçus automatiques devront sélectionner **Tap to load preview** pour charger l'image d'aperçu.

![6]{: style="max-width:30%;"}

## Considérations {#considerations}

- N'incluez qu'un seul lien d'aperçu dans votre message. Le contenu ne sera pas généré avec plusieurs liens dans le corps de votre SMS.
- N'incluez aucun caractère après votre lien d'aperçu, sous peine de perturber l'expérience.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}