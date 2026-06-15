---
nav_title: Formulaire d'inscription par e-mail
article_title: Formulaire d'inscription par e-mail
alias: "/email_capture/"
page_order: 3
description: "Cette page explique comment créer un formulaire d'inscription par e-mail avec l'éditeur par glisser-déposer de messages in-app."
---

# Formulaire d'inscription par e-mail {#email-sign-up-form}

> Utilisez le modèle de message in-app par glisser-déposer pour l'inscription par e-mail afin de collecter les adresses e-mail des utilisateurs et de développer vos groupes d'abonnement.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Créer un formulaire d'inscription par e-mail {#creating-an-email-sign-up-form}

### Étape 1 : Choisir votre modèle {#step-1-choose-your-template}

Lors de la création d'un message in-app par glisser-déposer, sélectionnez **Email sign-up** comme modèle, puis sélectionnez **Build message**. Ce modèle est pris en charge à la fois pour les applications mobiles et les navigateurs web.

![L'éditeur de messages in-app avec le modèle pour un formulaire de capture d'e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### Étape 2 : Configurer les styles de votre message {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Étape 3 : Personnaliser votre composant d'inscription par e-mail {#step-3-customize-your-email-sign-up-component}

Pour commencer à créer votre formulaire d'inscription par e-mail, sélectionnez l'élément de capture d'e-mail dans l'éditeur. Par défaut, les adresses e-mail collectées auront le groupe d'abonnement global **Abonné**. Pour inscrire des utilisateurs à des groupes d'abonnement spécifiques, consultez [Mettre à jour les états d'abonnement aux e-mails]({{site.baseurl}}/user_guide/channels/email/subscriptions/#updating-email-subscription-states).

Vous pouvez personnaliser le texte de la marque substitutive et le texte du libellé de l'élément de capture d'e-mail.

![L'éditeur de messages in-app avec un menu latéral pour personnaliser l'élément de capture d'e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### Validation des e-mails {#email-validation}

Si l'utilisateur saisit une adresse e-mail contenant des caractères spéciaux non acceptés, il verra un indicateur d'erreur générique et ne pourra pas envoyer le formulaire. Ce message d'erreur n'est pas personnalisable. Vous pouvez visualiser le comportement d'erreur dans l'onglet **Preview & Test** et sur votre appareil de test. Pour en savoir plus sur la façon dont Braze formate les adresses e-mail, consultez [Validation des e-mails]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/).

### Étape 4 : Ajouter une clause de non-responsabilité (facultatif) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Étape 5 : Styliser votre message {#step-5-style-your-message}

Personnalisez l'apparence de votre formulaire d'inscription à l'aide des [composants de messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#message-components) par glisser-déposer.

## Analyser les résultats {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Bonnes pratiques {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}