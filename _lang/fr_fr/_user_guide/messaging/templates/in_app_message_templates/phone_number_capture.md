---
nav_title: Formulaire d'inscription SMS, RCS et WhatsApp
article_title: Formulaire d'inscription SMS, RCS et WhatsApp
alias: "/phone_number_capture/"
page_order: 2
description: "Cette page explique comment créer un formulaire d'inscription SMS, RCS et WhatsApp avec l'éditeur par glisser-déposer pour les messages in-app."
---

# Formulaire d'inscription SMS, RCS et WhatsApp {#sms-rcs-and-whatsapp-sign-up-form}

> Les formulaires d'inscription SMS, RCS et WhatsApp sont des modèles disponibles dans l'éditeur par glisser-déposer pour les messages in-app. Utilisez ces modèles pour collecter les numéros de téléphone des utilisateurs et développer vos groupes d'abonnement SMS, MMS, RCS et WhatsApp.

![Trois exemples de messages in-app créés à l'aide du modèle de formulaire d'inscription par téléphone.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Créer un formulaire d'inscription par numéro de téléphone {#creating-a-phone-number-sign-up-form}

### Étape 1 : Choisir votre modèle {#step-1-choose-your-template}

Lors de la création d'un message in-app par glisser-déposer, sélectionnez **SMS sign-up** (cela prend également en charge l'inscription RCS) ou **WhatsApp sign-up** comme modèle, puis sélectionnez **Build message**. Ces modèles sont pris en charge à la fois pour les applications mobiles et les navigateurs web.

![Fenêtre modale pour sélectionner SMS sign-up ou WhatsApp sign-up comme modèle lors de la création d'un message in-app.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### Étape 2 : Configurer les styles de votre message {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![Processus de téléchargement et de sélection d'une police personnalisée.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### Étape 3 : Personnaliser le composant de saisie du numéro de téléphone {#step-3-customize-your-phone-number-input-component}

Pour commencer à créer votre formulaire d'inscription, sélectionnez le composant de saisie du numéro de téléphone dans l'éditeur.

![Zone de prévisualisation lors de la création d'un formulaire d'inscription avec le composant de saisie du numéro de téléphone sélectionné.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

Depuis le menu latéral, spécifiez le groupe d'abonnement pour lequel ce modèle collectera les numéros de téléphone. Pour respecter les bonnes pratiques de conformité, vous ne pouvez collecter le consentement que pour un seul groupe d'abonnement par formulaire d'inscription. Cependant, si vous le souhaitez, vous pouvez utiliser plusieurs formulaires pour collecter le consentement pour d'autres groupes d'abonnement.

![Menu déroulant des groupes d'abonnement avec un groupe d'abonnement sélectionné.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

Par défaut, nous collectons les numéros à l'échelle mondiale, mais vous pouvez limiter le nombre de pays à partir desquels collecter les numéros. Cela est utile si vous avez l'intention de n'envoyer des messages qu'aux utilisateurs dont les numéros de téléphone sont dans des pays spécifiques, et cela peut contribuer à la propreté de votre liste. Pour ce faire, désactivez **Collect numbers from all countries** et utilisez le menu déroulant pour sélectionner des pays spécifiques. Vos utilisateurs ne pourront sélectionner que les pays que vous avez explicitement ajoutés.

![Menu déroulant des pays pour sélectionner les pays à partir desquels vous souhaitez collecter les numéros.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Numéros de téléphone invalides {#invalid-phone-numbers}

Si vos utilisateurs saisissent un numéro de téléphone contenant des caractères spéciaux non acceptés, ils verront un indicateur d'erreur générique qui n'est pas personnalisable et ne pourront pas soumettre le formulaire. Vous pouvez visualiser le comportement d'erreur dans l'onglet **Preview & Test** et sur votre appareil de test. Consultez cet article pour découvrir [comment Braze formate les numéros de téléphone]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#import-phone-numbers).

### Étape 4 : Ajouter une clause de non-responsabilité (pour les formulaires d'inscription SMS et RCS) {#step-4-add-disclaimer-language-for-sms-and-rcs-sign-up-forms}

Pour les formulaires d'inscription SMS et RCS, il est important de communiquer clairement le type de SMS ou de RCS que vous enverrez. Assurez-vous que la croissance de votre liste est conforme en incluant les informations suivantes dans votre formulaire :

- Description des types de messages SMS et RCS que vos clients peuvent s'attendre à recevoir (rappels de panier, promotions et offres, rappels de rendez-vous, etc.). Vous n'avez pas besoin de lister chaque cas d'usage, mais vous devez fournir une description des types de messages que votre marque enverra.
- Mention que le consentement n'est pas une condition d'achat (le cas échéant).
- Fréquence des messages et rappel que des frais de messagerie et de données s'appliquent. Si vous ne connaissez pas la fréquence exacte des messages, vous pouvez indiquer que la fréquence peut varier.
- Liens vers vos conditions générales et votre politique de confidentialité SMS et RCS.
- Rappel des mots-clés d'aide et de désinscription (HELP pour obtenir de l'aide ; STOP pour annuler).

Nous avons fourni une marque substitutive de clause de non-responsabilité dans le modèle, uniquement à titre d'exemple — elle ne constitue pas un avis juridique et ne doit pas être utilisée à des fins de conformité. Il est important de travailler avec votre équipe juridique pour élaborer un texte adapté à votre marque.

{% alert note %}
Cette documentation n'est pas destinée à fournir, et ne peut pas être considérée comme fournissant, des conseils juridiques.
{% endalert %}

Pour plus d'informations sur la conformité SMS et RCS, consultez [Lois et réglementations pour les SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### Étape 5 : Styliser votre message {#step-5-style-your-message}

Personnalisez l'apparence de votre message à l'aide des [composants de messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) par glisser-déposer.

## Analyser les résultats {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

![Panneau de performance des messages in-app affichant les clics pour chaque lien dans le message in-app.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})