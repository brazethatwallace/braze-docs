---
nav_title: Formulaire de capture d'e-mail
article_title: Formulaire de capture d'e-mail
page_order: 5
page_type: reference
description: "Cet article présente un aperçu du type de message in-app de capture d'e-mail."
channel:
  - in-app messages
---

# Formulaire de capture d'e-mail {#email-capture-form}

> Les messages de capture d'e-mail vous permettent d'inviter les utilisateurs de votre site à soumettre leur adresse e-mail. Braze ajoute l'adresse à leur profil utilisateur pour l'utiliser dans toutes vos campagnes de communication.

Ce type de message est disponible dans l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

Si vous collectez les adresses e-mail via un formulaire personnalisé plutôt que ce type de message in-app, puis définissez l'appartenance au groupe d'abonnement via la REST API, vérifiez si un profil existe déjà avant de créer un utilisateur. Consultez les [bonnes pratiques de collecte]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices#step-1-check-if-the-user-exists).

## Fonctionnement {#how-it-works}

Lorsqu'un utilisateur final saisit son adresse e-mail dans ce formulaire, Braze ajoute l'adresse e-mail à son profil utilisateur.

- Pour les [utilisateurs anonymes]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) qui ne possèdent pas encore de compte, l'adresse e-mail est stockée sur le profil utilisateur anonyme lié à l'appareil de l'utilisateur.
- Si une adresse e-mail existe déjà sur le profil utilisateur, l'adresse e-mail nouvellement saisie remplace l'adresse e-mail existante.
- Si l'utilisateur connu possède une adresse e-mail signalée comme ayant subi un [échec d'envoi définitif]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#hard-bounce), Braze vérifie si l'adresse e-mail nouvellement saisie diffère de l'adresse enregistrée sur son profil Braze. Si l'adresse e-mail fournie est différente, Braze met à jour l'adresse e-mail et supprime le statut d'échec d'envoi définitif.
- Si un utilisateur saisit une adresse e-mail invalide, il voit le message d'erreur : « Please enter a valid email. »
    - Adresses e-mail invalides :
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Adresses e-mail valides :
        - `example@gmail.com`
        - `example@gnail.com` (avec une faute de frappe)
    - Pour plus d'informations sur la validation des e-mails dans Braze, consultez [Directives techniques et notes relatives aux e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation).

{% details En savoir plus sur les utilisateurs identifiés et anonymes %}

Le formulaire de capture d'e-mail définit l'adresse e-mail sur le profil utilisateur actuellement actif dans Braze. Le comportement diffère selon que l'utilisateur est identifié (connecté, `changeUser` appelé) ou non.

Si un utilisateur anonyme saisit son adresse e-mail dans le formulaire et le soumet, Braze ajoute l'adresse e-mail à son profil. Si `changeUser` est appelé plus tard au cours de son parcours web et qu'un nouvel `external_id` est attribué (par exemple lorsqu'un nouvel utilisateur s'inscrit au service), toutes les données du profil utilisateur anonyme sont fusionnées, y compris l'adresse e-mail.

Si `changeUser` est appelé avec un `external_id` existant, le profil utilisateur anonyme est orphelin et les [champs de données spécifiques du profil utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) qui n'existent pas encore sur l'utilisateur identifié sont fusionnés, mais tous les champs qui existent déjà sont perdus, y compris l'adresse e-mail.

Pour plus d'informations, consultez le [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle).

{% enddetails %}

## Étape 1 : Créer une campagne de message in-app {#step-1-create-an-in-app-message-campaign}

Pour accéder à cette option, vous devez créer une campagne de message in-app. Ensuite, en fonction de votre cas d'usage, définissez **Send To** sur **Web Browsers**, **Mobile Apps** ou **Both Mobile Apps & Web Browsers**, puis sélectionnez **Email Capture Form** comme **Message Type**.

{% alert note %}
**Vous ciblez des utilisateurs web ?** <br>Pour activer les messages in-app HTML via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, par exemple `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Ceci est requis pour des raisons de sécurité, car les messages in-app HTML peuvent exécuter du JavaScript. Un responsable du site doit donc les activer.
{% endalert %}

## Étape 2 : Personnaliser le formulaire {#customizable-features}

Ensuite, personnalisez votre formulaire selon vos besoins. Vous pouvez personnaliser les éléments suivants pour votre formulaire de capture d'e-mail :

- Texte de l'en-tête, du corps et du bouton d'envoi
- Une image facultative
- Un lien facultatif vers les « Conditions d'utilisation »
- Différentes couleurs pour le texte de l'en-tête et du corps, les boutons et l'arrière-plan
- Paires clé-valeur
- Style du texte de l'en-tête et du corps, des boutons, de la couleur de bordure des boutons, de l'arrière-plan et de la superposition
- Bouton d'envoi
    - Notez que le bouton d'envoi n'apparaît qu'après la saisie d'une adresse e-mail valide par l'utilisateur. Cela vous aide à collecter des adresses e-mail complètes.

![Éditeur pour le formulaire de capture d'e-mail.]({% image_buster /assets/img/email_capture.png %})

Si vous avez besoin de personnalisations supplémentaires, choisissez **Custom Code** comme **Type de message**. Utilisez ce [modèle de fenêtre modale de capture d'e-mail](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) du dépôt GitHub [Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) comme code de départ.

## Étape 3 : Définir votre audience d'entrée {#step-3-set-your-entry-audience}

Si vous utilisez un message in-app pour capturer les e-mails des utilisateurs, vous pouvez limiter l'audience aux utilisateurs qui n'ont pas encore fourni cette information.

- **Pour cibler les utilisateurs sans adresse e-mail :** Utilisez le filtre `Email Available` avec la valeur `false`. Le formulaire n'apparaîtra ainsi qu'aux utilisateurs qui n'ont pas d'e-mail enregistré, ce qui vous évite d'afficher des invites redondantes pour les utilisateurs déjà connus.
- **Pour cibler les utilisateurs anonymes sans ID externe :** Utilisez le filtre `External User ID` `is blank`. Cela est utile lorsque vous souhaitez identifier les utilisateurs qui ne se sont pas encore authentifiés ou inscrits.

Vous pouvez également combiner les deux filtres avec une logique `AND`, si vous le souhaitez. Le formulaire n'apparaîtra alors qu'aux utilisateurs auxquels il manque à la fois une adresse e-mail et un ID externe — idéal pour capturer de nouveaux prospects ou inciter à la création de compte.

## Étape 4 : Cibler les utilisateurs ayant rempli le formulaire (facultatif) {#step-4-target-users-who-filled-out-the-form-optional}

Après avoir lancé le formulaire de capture d'e-mail et collecté les adresses e-mail de vos utilisateurs, vous pouvez cibler les utilisateurs ayant rempli le formulaire.

1. Dans n'importe quel filtre de Segment dans Braze, sélectionnez le filtre `Clicked/Opened Campaign`.
2. Dans le menu déroulant, sélectionnez `clicked in-app message button 1`.
3. Sélectionnez votre Campaign de formulaire de capture d'e-mail.