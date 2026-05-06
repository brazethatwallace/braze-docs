---
nav_title: Inscription par e-mail avec confirmation
article_title: Inscription par e-mail avec page de confirmation
alias: "/email_confirmation_page/"
page_order: 7
description: "Cette page explique comment utiliser l'éditeur par glisser-déposer de messages in-app pour créer un formulaire d'inscription par e-mail avec une page de confirmation."
---

# Inscription par e-mail avec page de confirmation {#email-sign-up-with-confirmation-page}

> Utilisez l'éditeur par glisser-déposer de messages in-app pour créer un formulaire d'inscription par e-mail avec une page de confirmation.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Créer un formulaire d'inscription par e-mail avec une page de confirmation {#creating-an-email-sign-up-form-with-a-confirmation-page}

### Étape 1 : Choisir votre modèle {#step-1-choose-your-template}

Lors de la création d'un message in-app par glisser-déposer, sélectionnez **Email sign-up with confirmation page** comme modèle, puis sélectionnez **Build message**. Ce modèle est pris en charge à la fois pour les applications mobiles et les navigateurs web.

![L'éditeur de messages in-app avec le modèle pour un formulaire d'inscription par e-mail avec page de confirmation.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %})

### Étape 2 : Configurer les styles de votre message {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Étape 3 : Personnaliser votre composant d'inscription par e-mail {#step-3-customize-your-email-sign-up-component}

Pour commencer à créer votre formulaire d'inscription par e-mail, sélectionnez l'élément de capture d'e-mail dans l'éditeur. Par défaut, les adresses e-mail collectées auront le groupe d'abonnement global **Subscribed**. Pour abonner des utilisateurs à des groupes d'abonnement spécifiques, consultez [Mettre à jour les états d'abonnement par e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions/#updating-email-subscription-states).

Vous pouvez personnaliser le texte de la marque substitutive et le texte du libellé de l'élément de capture d'e-mail.

![L'éditeur de messages in-app avec un menu latéral pour personnaliser l'élément de capture d'e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %})

#### Validation de l'e-mail {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Étape 4 : Ajouter un texte de clause de non-responsabilité (facultatif) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Étape 5 : Styliser votre message {#step-5-style-your-message}

Personnalisez l'apparence de votre formulaire d'inscription par e-mail et de votre page de confirmation à l'aide des [composants de messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#message-components) par glisser-déposer.

## Analyser les résultats {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Bonnes pratiques {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}