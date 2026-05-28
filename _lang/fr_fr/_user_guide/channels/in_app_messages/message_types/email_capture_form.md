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

Ce type de message est disponible dans l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

## Fonctionnement {#how-it-works}

Lorsqu'un utilisateur final saisit son adresse e-mail dans ce formulaire, Braze ajoute l'adresse e-mail à son profil utilisateur.

- Pour les [utilisateurs anonymes]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#anonymous-user-profiles) qui n'ont pas encore de compte, l'adresse e-mail est conservée dans le profil utilisateur anonyme lié à l'appareil de l'utilisateur.
- Si une adresse e-mail existe déjà dans le profil utilisateur, la nouvelle adresse saisie remplace l'adresse existante.
- Si l'utilisateur connu possède une adresse e-mail signalée comme ayant subi un [échec d'envoi définitif]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary/#hard-bounce), Braze vérifie si la nouvelle adresse e-mail saisie diffère de celle présente dans son profil Braze. Si l'adresse e-mail fournie est différente, Braze met à jour l'adresse e-mail et supprime le statut d'échec d'envoi définitif.
- Si un utilisateur saisit une adresse e-mail invalide, il voit le message d'erreur : « Veuillez saisir une adresse e-mail valide. »
    - Adresses e-mail invalides :
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Adresses e-mail valides :
        - `example@gmail.com`
        - `example@gnail.com` (avec une faute de frappe)
    - Pour plus d'informations sur la validation des e-mails dans Braze, consultez les [Directives techniques et notes relatives aux e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/).

{% details En savoir plus sur les utilisateurs identifiés et anonymes %}

Le formulaire de capture d'e-mail définit l'adresse e-mail sur le profil utilisateur actuellement actif dans Braze. Le comportement diffère selon que l'utilisateur est identifié (connecté, `changeUser` appelé) ou non.

Si un utilisateur anonyme saisit son adresse e-mail dans le formulaire et le soumet, Braze ajoute l'adresse e-mail à son profil. Si `changeUser` est appelé ultérieurement au cours de son parcours web et qu'un nouvel `external_id` est attribué (par exemple lorsqu'un nouvel utilisateur s'inscrit au service), toutes les données du profil utilisateur anonyme sont fusionnées, y compris l'adresse e-mail.

Si `changeUser` est appelé avec un `external_id` existant, le profil utilisateur anonyme est orphelin et les [champs de données spécifiques du profil utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) qui n'existent pas encore dans le profil de l'utilisateur identifié sont fusionnés, mais les champs qui existent déjà sont perdus, y compris l'adresse e-mail.

Pour plus d'informations, consultez le [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/).

{% enddetails %}

## Étape 1 : Créer une Campaign de message in-app {#step-1-create-an-in-app-message-campaign}

Pour accéder à cette option, vous devez créer une Campaign de message in-app. Ensuite, selon votre cas d'utilisation, définissez **Send To** sur **Web Browsers**, **Mobile Apps** ou **Both Mobile Apps & Web Browsers**, puis sélectionnez **Email Capture Form** comme **Message Type**.

{% alert note %}
**Vous ciblez des utilisateurs web ?** <br>Pour activer les messages in-app HTML via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, par exemple `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Ceci est nécessaire pour des raisons de sécurité, car les messages in-app HTML peuvent exécuter du JavaScript, et un responsable du site doit donc les activer.
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

Si vous avez besoin de personnalisations supplémentaires, choisissez **Custom Code** comme **Message Type**. Utilisez ce [modèle de fenêtre modale de capture d'e-mail](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) du dépôt GitHub [Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) comme code de départ.

## Étape 3 : Définir votre audience d'entrée {#step-3-set-your-entry-audience}

Si vous utilisez un message in-app pour capturer les adresses e-mail des utilisateurs, vous souhaiterez peut-être limiter l'audience aux utilisateurs qui n'ont pas encore fourni cette information.

- **Pour cibler les utilisateurs sans adresse e-mail :** Utilisez le filtre `Email Available` avec la valeur `false`. Cela permet d'afficher le formulaire uniquement aux utilisateurs qui n'ont pas d'adresse e-mail enregistrée, évitant ainsi les invites redondantes pour les utilisateurs connus.
- **Pour cibler les utilisateurs anonymes sans ID externe :** Utilisez le filtre `External User ID` `is blank`. Cela est utile lorsque vous souhaitez identifier les utilisateurs qui ne se sont pas encore authentifiés ou inscrits.

Vous pouvez également combiner les deux filtres avec une logique `AND`, si vous le souhaitez. Cela permet d'afficher le formulaire uniquement aux utilisateurs qui n'ont ni adresse e-mail ni ID utilisateur externe, ce qui est idéal pour capturer de nouveaux prospects ou inciter à la création de compte.

## Étape 4 : Cibler les utilisateurs ayant rempli le formulaire (facultatif) {#step-4-target-users-who-filled-out-the-form-optional}

Après avoir lancé le formulaire de capture d'e-mail et collecté les adresses e-mail de vos utilisateurs, vous pouvez cibler les utilisateurs ayant rempli le formulaire.

1. Dans n'importe quel filtre de segment dans Braze, sélectionnez le filtre `Clicked/Opened Campaign`.
2. Dans le menu déroulant, sélectionnez `clicked in-app message button 1`.
3. Sélectionnez la Campaign de votre formulaire de capture d'e-mail.