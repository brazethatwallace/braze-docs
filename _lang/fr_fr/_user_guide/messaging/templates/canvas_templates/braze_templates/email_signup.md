---
nav_title: Inscription par e-mail avec double abonnement
article_title: Inscription par e-mail avec double abonnement
page_order: 2
page_type: reference
description: "Cet article décrit comment utiliser un modèle Canvas de Braze pour élargir votre portée grâce à des inscriptions par e-mail vérifiées."
tool: Canvas
---

# Inscription par e-mail avec double abonnement {#email-sign-up-with-double-opt-in}

> Utilisez le modèle d'inscription par e-mail avec double abonnement pour élargir votre portée grâce à des inscriptions par e-mail vérifiées. Ciblez les nouveaux utilisateurs pour capturer leur e-mail, confirmer leur abonnement et recevoir un code de promotion, le tout dans un parcours fluide.

Cet article vous guidera à travers un cas d'utilisation du modèle **Inscription par e-mail avec double abonnement**, conçu pour la phase de considération du cycle de vie de l'utilisateur. À la fin, vous aurez créé un Canvas qui envoie des e-mails et des messages in-app aux utilisateurs lorsqu'ils démarrent une session ou lorsqu'ils n'ont pas terminé leur onboarding.

## Conditions préalables {#prerequisites}

Pour utiliser ce modèle avec succès, vous avez besoin des éléments suivants :

- Un [message in-app multi-pages]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/#multi-page) avec une page pour capturer les e-mails de vos utilisateurs et une autre pour communiquer un message de confirmation.
- Un e-mail de confirmation pour que les utilisateurs vérifient leur adresse e-mail.
- Un e-mail de bienvenue avec un code de promotion exclusif pour les utilisateurs qui effectuent le double abonnement.

## Adapter le modèle à vos besoins {#tailoring-the-template-to-your-needs}

Imaginons que vous travaillez pour Steppington, une application de santé connue pour ses fonctionnalités telles que le suivi des calories, les cours d'exercice numériques et les marathons flash-mob. Avant de créer le Canvas, vous [configurez des messages in-app et dans le navigateur multi-pages]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/#multi-page) qui incluent une série de questions engageantes pour déterminer l'expérience et l'impression d'un utilisateur lors de sa première utilisation de l'application.

Pour accéder au modèle, lors de la création d'un nouveau Canvas, sélectionnez **Use a Canvas template** > **Braze templates**. Ensuite, à côté de **Email sign-up with double opt-in**, sélectionnez **Apply Template**. Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Configurer les détails {#step-1-set-up-the-details}

Ajustez les détails du Canvas pour refléter votre objectif.

1. Sélectionnez **Edit** à côté du nom du modèle.

![Le titre et la description actuels du Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Mettez à jour le nom du Canvas pour préciser que le Canvas cible les nouveaux utilisateurs lors de leur première utilisation de l'application.
3. Mettez à jour la description pour expliquer que ce Canvas contient des messages personnalisés pour que les utilisateurs effectuent le double abonnement.
4. Ajoutez l'étiquette **Email** afin de pouvoir filtrer le Canvas sur la page d'accueil Canvas.

![Le nouveau nom, la description et l'étiquette du Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Étape 2 : Affecter les événements de conversion {#step-2-assign-conversion-events}

Ensuite, affectez vos événements de conversion. Les événements de conversion sont un type d'indicateur que vous pouvez utiliser pour mesurer le succès du Canvas. Pour **Conversion event type**, sélectionnez **Performs Custom Event**. Ensuite, sélectionnez **email_opt_in** pour le **Custom event name**.

![Section « Assign Conversion Events » pour le type d'événement de conversion d'abonnement par e-mail.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Conservez la date limite de conversion de trois jours du modèle, car vous souhaitez cibler vos utilisateurs les plus récents.

### Étape 3 : Adapter la planification d'entrée {#step-3-tailor-the-entry-schedule}

Conservez la planification d'entrée sur **Action-Based** afin que les utilisateurs entrent dans votre Canvas lorsqu'ils démarrent une session dans l'application. De cette façon, vous pouvez commencer à construire votre relation avec un engagement opportun.

Envisagez également de conserver les **Action Based Options** telles quelles afin que les utilisateurs n'entrent dans le Canvas que lorsqu'ils démarrent une session.

![Une planification d'entrée basée sur l'action pour faire entrer dans le Canvas les utilisateurs qui démarrent une session.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Pour la **Entry Window**, mettez à jour le **Started Time (Required)** à la date et l'heure souhaitées.

![Une fenêtre d'entrée avec l'heure de début le 16 janvier 2025 à 12h30. Les utilisateurs entreront dans ce message dans leur fuseau horaire local.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Étape 4 : Sélectionner l'audience cible {#step-4-select-the-target-audience}

Définissez votre audience cible comme les utilisateurs de Steppington qui n'ont pas d'adresse e-mail dans leur profil utilisateur en conservant le [filtre de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) par défaut du modèle `Email Available is false`.

![Audience d'entrée avec le filtre « Email Available is false ».]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Étape 5 : Sélectionner vos paramètres d'envoi {#step-5-select-your-send-settings}

Conservez les paramètres d'abonnement par défaut, afin d'envoyer uniquement aux utilisateurs qui se sont abonnés ou qui ont accepté de recevoir des messages ou des notifications, et ignorez les autres paramètres (limite de fréquence, heures calmes et groupes initiateurs).

![Options d'envoi par défaut pour envoyer uniquement aux utilisateurs abonnés ou ayant accepté.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Étape 6 : Personnaliser votre Canvas {#step-6-customize-your-canvas}

Ensuite, créez le Canvas en personnalisant les canaux et le contenu que vous souhaitez envoyer aux utilisateurs. Comme vous vous concentrez sur la vérification des inscriptions par e-mail, vous n'avez pas besoin d'ajouter ou de supprimer des étapes ou des canaux du modèle Canvas.

1. Sélectionnez la première étape Message nommée **Email Sign-up**. C'est ici que vous mettez à jour le modèle pour utiliser notre message in-app (et dans le navigateur) multi-pages.

- La page 1 capture les e-mails.
- La page 2 affiche un message de confirmation.

![Deux pages d'un message in-app pour capturer les e-mails des utilisateurs et afficher un message de confirmation.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2. À partir de là, conservez l'étape de parcours d'action **Subscribed** telle quelle. Cette étape divise nos utilisateurs en deux groupes dans une fenêtre d'un jour :

- Les utilisateurs qui se sont abonnés à Steppington avec leur e-mail
- Les utilisateurs qui ne se sont pas abonnés à Steppington avec leur e-mail

{:start="3"}
3. Ensuite, remplacez le corps de l'e-mail par notre e-mail de confirmation de marque pour l'étape Message **Verify Email**. Cela enverra un e-mail à nos utilisateurs abonnés et les invitera à confirmer leur adresse e-mail et à s'abonner à nos messages.
4. Conservez l'étape de parcours d'action **Confirm Subscription** telle quelle. Cette étape divise davantage nos utilisateurs entre ceux qui ont confirmé leur e-mail et ceux qui ne l'ont pas fait, avec une fenêtre d'une semaine.
5. Enfin, mettez à jour l'étape Message **Welcome + Discount** avec notre e-mail de confirmation qui inclut un code de promotion exclusif.

{% alert note %}
L'étape Message **Verify Email** est déclenchée lors de la deuxième session de l'utilisateur. En effet, le premier événement de démarrage de session déclenche le Canvas, mais un deuxième démarrage de session après que l'utilisateur a atteint la première étape Message **Email Sign-up** est nécessaire pour que l'utilisateur soit éligible au déclenchement du deuxième message in-app.
{% endalert %}

### Étape 7 : Tester et lancer votre Canvas {#step-7-test-and-launch-your-canvas}

Après avoir testé et vérifié votre Canvas pour vous assurer qu'il fonctionne comme prévu, lancez-le en sélectionnant **Launch Canvas**.

{% alert tip %}
Consultez notre [liste de vérification pré et post-lancement]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) pour les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}