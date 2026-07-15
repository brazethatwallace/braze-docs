---
nav_title: IAM Studio
article_title: IAM Studio
description: "Cet article de référence décrit le partenariat entre Braze et IAM Studio, une plateforme de personnalisation de messages qui vous permet de créer des expériences personnalisées et riches dans l'application et de les diffuser via Braze."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com) est une plateforme de personnalisation de messages sans code qui vous permet de créer des expériences personnalisées et riches dans l'application et de les diffuser via Braze.

_Cette intégration est maintenue par IAM Studio._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et d'IAM Studio vous permet d'insérer facilement des modèles de messages in-app personnalisables dans vos messages in-app Braze, offrant le remplacement d'images, la modification de texte, la définition de paramètres de deep link, d'attributs personnalisés et de paramètres d'événement. En utilisant IAM Studio, vous pouvez réduire le temps de production de messages et consacrer plus de temps à la planification du contenu.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte IAM Studio | Un [compte IAM Studio](https://www.inappmessage.com/register) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Cas d'usage {#use-cases}

- Encourager l'achat de biens
- Collecte d'informations utilisateur
- Augmentation du nombre de membres inscrits
- Informations sur l'émission de coupons

## Intégration {#integration}

### Étape 1 : Choisir un modèle {#step-1-choose-a-template}

Choisissez un modèle de message in-app que vous souhaitez utiliser dans la galerie de modèles de messages in-app.

![La galerie de modèles IAM Studio montre différents modèles tels que « carousel slide modal », « simple icon modal », « modal full image », et plus encore.]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### Étape 2 : Personnaliser le modèle {#step-2-customize-the-template}

Tout d'abord, personnalisez l'image, le texte et le bouton de votre contenu. Assurez-vous de connecter **Deeplink** pour l'image et le bouton.

{% tabs local %}
{% tab Image %}
![L'interface utilisateur d'IAM Studio montrant les options pour personnaliser l'image. Ces options incluent l'image, le rayon de l'image et l'image atténuée.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Texte %}
![L'interface utilisateur d'IAM Studio montrant les options pour personnaliser le titre et le sous-titre de votre message. Ces options incluent le texte, la mise en forme et la police.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Bouton %}
![L'interface utilisateur d'IAM Studio montrant les options pour personnaliser le bouton principal, gauche et droit. Ces options incluent la couleur, le deep link, le texte et la mise en forme.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

Ensuite, créez votre message in-app personnalisé en ajoutant des polices personnalisées et en utilisant des étiquettes Liquid. Pour activer la journalisation et le suivi, sélectionnez **Log data and track user behavior**.

{% tabs local %}
{% tab Polices %}
![L'interface utilisateur d'IAM Studio montrant les options pour ajouter du Liquid. Ces options comprennent la création de phrases personnalisées.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![L'interface utilisateur d'IAM Studio montrant les options pour personnaliser la journalisation des événements et attributs. Ces options comprennent l'enregistrement du comportement de l'utilisateur.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Journalisation et suivi %}
![L'interface utilisateur d'IAM Studio montrant les options pour personnaliser la police. Ces options permettent notamment à l'utilisateur de personnaliser le style de la police.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### Étape 3 : Exporter le modèle {#step-3-export-the-template}

Une fois toutes les modifications terminées, exportez le modèle en cliquant sur **Export**. Après l'exportation, le code HTML du message in-app sera généré. Copiez ce code en cliquant sur le bouton **Copy code**.

![Boîte de dialogue d'exportation IAM Studio avec le code HTML du message in-app généré et l'action de copie du code.]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### Étape 4 : Utiliser le code dans Braze {#step-4-use-code-in-braze}

Accédez à Braze, et dans votre message in-app, collez le code personnalisé dans la zone **HTML Input**. Assurez-vous de tester votre message pour vérifier qu'il s'affiche correctement.

![Éditeur de Campaign de message in-app Braze avec le code HTML d'IAM Studio collé dans la zone HTML Input.]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}