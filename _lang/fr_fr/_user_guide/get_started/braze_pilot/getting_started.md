---
nav_title: Démarrage
article_title: Commencer avec Braze Pilot
page_order: 2
page_type: reference
description: "Cet article de référence présente brièvement les étapes d'intégration requises de la part de vos ingénieurs ou développeurs."
---

# Commencer avec Braze Pilot {#get-started-with-braze-pilot}

> Cet article explique comment débuter avec Braze Pilot. Nous vous guiderons tout au long du téléchargement de l'application, de l'initialisation de la connexion avec votre tableau de bord de Braze et de la finalisation de la configuration.

## Étape 1 : Télécharger Braze Pilot {#step-1-download-braze-pilot}

Pour commencer à utiliser Braze Pilot, vous devez d'abord télécharger l'application depuis l'App Store d'Apple ou le Google Play Store. Vous pouvez rechercher l'application dans le store ou scanner les codes QR ci-dessous pour accéder à la page de l'application correspondant à votre appareil.

## Étape 2 : Accepter les conditions générales {#step-2-accept-the-terms-and-conditions}

Acceptez ensuite les conditions générales, puis saisissez votre e-mail professionnel dans le formulaire. Votre e-mail sera utilisé uniquement à des fins d'analyse de l'utilisation de l'application et ne sera pas utilisé à des fins marketing.

![Page d'accueil de Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![Option pour saisir votre adresse e-mail professionnelle.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Étape 3 : Initialiser la connexion avec le SDK Braze {#step-3-initialize-the-connection-with-the-braze-sdk}

Braze Pilot vous permet d'initialiser le SDK Braze sur n'importe quel tableau de bord de Braze. Une fois le SDK initialisé, Pilot commencera à envoyer des données d'engagement à Braze et vous permettra de déclencher tout envoi de messages lancé depuis ce tableau de bord de Braze.

Il existe deux méthodes pour configurer la connexion au SDK dans Pilot : les codes QR de démonstration et l'assistant de configuration.

{% tabs local %}
{% tab Demo QR codes %}

### Méthode 1 : Codes QR de démonstration {#method-1-demo-qr-codes}

Scannez un code QR contenant toutes les informations nécessaires pour initialiser le SDK, créer votre profil utilisateur et vous rediriger via un lien profond vers une simulation d'application spécifique dans Braze Pilot. Les codes QR de démonstration sont affichés dans le tiroir associé à certaines campagnes de démonstration de votre essai gratuit.

| Pilot pour Android | Pilot pour iOS |
| --- | --- |
| ![Code QR pour Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![Code QR pour iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Méthode 1 : Codes QR de démonstration" }

{% endtab %}
{% tab Setup wizard %}

### Méthode 2 : Assistant de configuration {#method-2-setup-wizard}

Suivez le guide étape par étape pour initialiser la connexion avec votre espace de travail depuis la page **Paramètres des applications** de votre tableau de bord de Braze.

![Étape 1 de l'assistant de configuration de Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Cette connexion est spécifique à l'espace de travail. Autrement dit, si vous initialisez la connexion depuis l'espace de travail de démonstration, puis basculez vers l'espace de travail en production dans votre tableau de bord d'essai gratuit, vous devrez réinitialiser le SDK depuis cet espace de travail pour recevoir les campagnes qui y sont lancées.

![Le menu déroulant de l'espace de travail dans le tableau de bord de Braze avec « Demo - Braze » sélectionné comme espace de travail actif.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Étape 4 : Autoriser les notifications push {#step-4-allow-push-permissions}

Enfin, il est recommandé d'autoriser l'application à vous envoyer des notifications push si vous souhaitez tester les fonctionnalités push via l'application. Vous pouvez accorder ces autorisations de différentes manières : en mettant à jour les paramètres de l'application dans les réglages de votre appareil, ou en lançant un message d'amorce push depuis Braze vers l'application.

{% tabs local %}
{% tab Update the settings for the app %}

Ouvrez les paramètres de votre appareil et localisez Braze Pilot. Mettez ensuite à jour les paramètres pour autoriser l'affichage des notifications sur votre écran de verrouillage.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Launch a push primer message %}

Vous pouvez utiliser un message in-app de Braze pour demander les autorisations push pour l'application, comme vous le feriez pour vos propres utilisateurs. Pour découvrir comment créer ce type de message dans Braze, consultez [Messages in-app d'amorce push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Étape 5 : Découvrir l'envoi de messages Braze dans Pilot {#step-5-experience-braze-messaging-in-pilot}

Vous êtes maintenant prêt à recevoir des campagnes et des Canvas depuis votre tableau de bord de Braze en tant qu'utilisateur de Braze Pilot ! Consultez l'une des campagnes lancées dans votre espace de travail de démonstration pour une démonstration rapide des cas d'utilisation de Braze, puis rendez-vous dans votre espace de travail en production pour commencer à envoyer les vôtres.

Pour en savoir plus sur la mise en place de campagnes et de Canvas dans Braze, consultez [Démarrer avec les campagnes et les Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases/).