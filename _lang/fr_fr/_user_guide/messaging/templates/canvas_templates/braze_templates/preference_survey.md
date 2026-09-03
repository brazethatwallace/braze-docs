---
nav_title: Onboarding avec enquête de préférences
article_title: Onboarding avec enquête de préférences
page_order: 5.5
page_type: reference
description: "Cet article décrit comment utiliser un modèle Canvas de Braze pour favoriser l'adoption précoce grâce à un flux d'onboarding guidé qui présente votre marque aux nouveaux utilisateurs et collecte leurs préférences pour les maintenir engagés sur le long terme."
tool: Canvas
---

# Onboarding avec enquête de préférences {#onboarding-with-preferences-survey}

> Utilisez le modèle d'onboarding avec enquête de préférences pour créer un flux d'onboarding guidé qui cible les nouveaux utilisateurs. Présentez-leur votre marque, aidez-les à démarrer et collectez leurs préférences pour les maintenir engagés sur le long terme.

Cet article vous guidera à travers un cas d'utilisation du modèle **Onboarding with preferences survey**, conçu pour la phase de considération du cycle de vie utilisateur. À la fin, vous aurez créé un Canvas qui envoie des e-mails et des messages in-app aux utilisateurs lorsqu'ils démarrent une session et lorsqu'ils n'ont pas terminé leur onboarding.

## Conditions préalables {#prerequisites}

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un e-mail de bienvenue qui invite les utilisateurs à commencer l'onboarding.
- Un e-mail de suivi contenant des conseils pour démarrer avec l'application, destiné aux utilisateurs ayant effectué l'onboarding.
- Un e-mail de suivi pour inviter les utilisateurs à terminer leur onboarding.
- Une [enquête]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/simple_survey) contenant plusieurs questions pour déterminer les préférences des utilisateurs.

## Adapter le modèle à vos besoins {#tailoring-the-template-to-your-needs}

Imaginons que nous travaillons pour StyleRyde, une application de covoiturage à la demande qui emmène les gens là où ils doivent aller. Avant de créer le Canvas, nous [configurons une enquête simple]({{site.baseurl}}/user_guide/data/activation/catalogs/create) qui comprend une série de questions engageantes pour déterminer l'expérience et l'impression d'un utilisateur lors de sa première course avec l'application.

Pour accéder au modèle, lors de la création d'un nouveau Canvas, sélectionnez **Use a Canvas template** > **Braze templates**. Ensuite, à côté de **Onboarding with preferences survey**, sélectionnez **Apply Template**. Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Configurer les détails {#step-1-set-up-the-details}

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Edit** à côté du nom du modèle.

![Le titre et la description actuels du Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Mettez à jour le nom du Canvas pour indiquer qu'il cible les nouveaux utilisateurs lors de leur première utilisation de l'application.
3. Mettez à jour la description pour expliquer que ce Canvas contient des messages personnalisés.
4. Ajoutez l'étiquette **Onboarding** afin de pouvoir filtrer le Canvas sur la page d'accueil Canvas.

![Le nouveau nom, la description et l'étiquette du Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### Étape 2 : Affecter les événements de conversion {#step-2-assign-conversion-events}

Mettez à jour l'**événement de conversion principal - A** en sélectionnant **Performs Custom Event**. Ensuite, sélectionnez **Last Used App** pour l'événement personnalisé.

![Last Used App sélectionné comme nom d'événement personnalisé pour l'événement de conversion.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### Étape 3 : Adapter la planification d'entrée {#step-3-tailor-the-entry-schedule}

Conservons la planification d'entrée en mode **Action-Based** afin que les utilisateurs entrent dans notre Canvas lorsqu'ils démarrent une session dans l'application. De cette façon, nous pouvons commencer à construire notre relation avec un engagement opportun.

Nous apporterons une modification à cette section en ajustant la **fenêtre d'entrée** à la date et l'heure souhaitées.

![Section « Fenêtre d'entrée » avec l'heure de début fixée au 30 janvier 2025 à 12 h.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### Étape 4 : Sélectionner l'audience cible {#step-4-select-the-target-audience}

Nous conserverons l'audience cible telle quelle pour cibler nos utilisateurs qui ont utilisé l'application StyleRyde pour la première fois il y a moins d'un jour.

![Le filtre « A utilisé ces applications pour la première fois il y a moins de 1 jour » sélectionné pour cibler l'audience d'entrée.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### Étape 5 : Sélectionner vos paramètres d'envoi {#step-5-select-your-send-settings}

Nous conserverons les paramètres d'abonnement par défaut, de sorte que nous n'envoyons des messages qu'aux utilisateurs qui se sont abonnés ou ont opté pour la réception de messages ou de notifications, avec les heures calmes activées, et nous ignorerons les autres paramètres (limite de fréquence et groupes initiateurs).

![Section « Paramètres d'envoi » avec les paramètres d'abonnement pour les utilisateurs abonnés ou ayant opté pour la réception, avec les heures calmes activées entre 0 h et 20 h.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### Étape 6 : Personnaliser votre Canvas {#step-6-customize-your-canvas}

Maintenant, nous allons construire notre Canvas en personnalisant le contenu qui sera envoyé aux utilisateurs.

1. Pour la première étape de message **Welcome Email**, nous mettrons à jour cette étape pour inclure notre e-mail de bienvenue StyleRyde.
2. Ensuite, nous conserverons l'étape de parcours d'action telle quelle. Cette étape divise nos utilisateurs en deux groupes dans une fenêtre de trois jours :

- Les utilisateurs qui ont démarré une session ou cliqué sur l'e-mail d'onboarding
- Les utilisateurs qui n'ont pas démarré de session ni cliqué sur l'e-mail d'onboarding

![Une étape de parcours d'action divisée en deux chemins, l'un pour les utilisateurs ayant démarré une session et l'autre pour tous les autres.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

À partir de là, nous ciblerons nos utilisateurs et nos messages en fonction des groupes mentionnés ci-dessus.

#### Cibler vos utilisateurs engagés {#target-your-engaged-users}

Pour nos utilisateurs qui ont démarré une session ou interagi avec notre e-mail d'onboarding de la première étape de message, nous mettrons à jour l'étape de message **Getting Started Tips** pour inclure les conseils essentiels de voyage et de sécurité pour nos nouveaux utilisateurs StyleRyde.

Une fois qu'un utilisateur a terminé son onboarding, il quittera le Canvas.

Ensuite, mettez à jour l'étape de message **Content Preferences Survey** pour inclure notre enquête de préférences qui invite nos utilisateurs à sélectionner les sujets sur lesquels ils souhaitent recevoir des informations à l'avenir.

![Un aperçu de l'enquête de préférences qui invite les utilisateurs à sélectionner tous les centres d'intérêt qui s'appliquent.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### Relancer les utilisateurs qui n'ont pas commencé l'onboarding {#nudge-users-who-havent-started-onboarding}

Pour nos autres utilisateurs, nous mettrons à jour l'étape de message **Winback Nudge** avec notre e-mail de suivi pour inviter les utilisateurs à terminer leur onboarding.

En tant que dernière étape de réengagement, nous renommerons **Step 2** en **Final Winback Nudge** et mettrons à jour l'étape avec notre message in-app pour inviter nos nouveaux utilisateurs à terminer leur onboarding.

### Étape 7 : Tester et lancer votre Canvas {#step-7-test-and-launch-your-canvas}

Après avoir testé et vérifié notre Canvas pour nous assurer qu'il fonctionne comme prévu, nous le lancerons en sélectionnant **Launch Canvas**.

{% alert tip %}
Consultez notre [liste de vérification pré et post-lancement]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) pour les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}