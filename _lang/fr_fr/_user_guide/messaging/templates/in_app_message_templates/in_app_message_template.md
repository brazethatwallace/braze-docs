---
nav_title: Créer un modèle de message in-app
article_title: Créer un modèle de message in-app
page_order: 0
description: "Cet article de référence explique comment créer, enregistrer et gérer des modèles de messages in-app depuis la section Contenu du tableau de bord de Braze, y compris les profils de couleurs et les modèles CSS pour l'éditeur traditionnel."
tool:
  - Templates
channel:
  - in-app messages
search_rank: 1
---

# Créer un modèle de message in-app {#create-an-in-app-message-template}

> Utilisez **Contenu** > **In-App Message** pour créer une bibliothèque réutilisable de mises en page de messages in-app et dans le navigateur. Vous pouvez enregistrer des conceptions depuis l'éditeur par glisser-déposer ou créer des ressources **Color Profile** et **CSS Template** pour l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

## Étape 1 : Ouvrir les modèles de messages in-app {#step-1-open-in-app-message-templates}

Dans le tableau de bord de Braze, accédez à **Contenu** > **In-App Message**.

## Étape 2 : Choisir comment créer un modèle {#step-2-choose-how-to-create-a-template}

La manière d'ajouter un modèle dépend de votre objectif :

| Objectif | Marche à suivre |
|----------|-----------------|
| Enregistrer une mise en page par glisser-déposer pour la réutiliser | Dans le [compositeur de messages in-app par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/), sélectionnez **Save as template** après avoir quitté l'éditeur (vous devez d'abord lancer la Campaign OU l'enregistrer en tant que brouillon). Le modèle apparaît dans **Templates** > **In-App Message Templates** pour votre prochain message. |
| Créer un profil de couleurs ou un modèle CSS (éditeur traditionnel) | Sur la page **In-App Message Templates**, sélectionnez **+ Create**, puis choisissez **Color Profile** ou **CSS Template**. Pour plus de détails, consultez [Profils de couleurs et modèles CSS](#reusable-color-profiles). |
| Personnaliser un modèle Braze | [Créez un message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) dans l'éditeur par glisser-déposer, choisissez un modèle Braze, effectuez vos personnalisations, puis sélectionnez **Save as template**. Pour les descriptions de chaque modèle Braze, consultez [Modèles de messages in-app]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Choose how to create a template" }

{% alert note %}
Les profils de couleurs et les modèles CSS s'appliquent à l'éditeur traditionnel. Si vous utilisez l'éditeur par glisser-déposer, utilisez les [paramètres de style]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/) pour la mise en forme au niveau du message.
{% endalert %}

## Étape 3 : Gérer vos modèles {#step-3-manage-your-templates}

Dans **Contenu** > **In-App Message**, filtrez, recherchez ou ouvrez un modèle pour le modifier. Vous pouvez [dupliquer]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/#duplicate-templates) et [archiver]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/#archive-templates) des modèles comme pour les autres types de modèles. Pour un aperçu des flux de travail liés aux modèles et aux médias, consultez [Modèles]({{site.baseurl}}/user_guide/messaging/templates/).

Pour accéder aux modèles de messages in-app, vous devez disposer des [autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) permettant de consulter ou de modifier les modèles de messages in-app.

### Créer des profils de couleurs et des modèles CSS {#reusable-color-profiles}

{% alert note %}
Les options suivantes s'appliquent à l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/). Si vous utilisez l'éditeur par glisser-déposer, utilisez les [paramètres de style]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/) à la place.
{% endalert %}

Vous pouvez modifier des modèles existants ou sélectionner **+ Create** et choisir **Color Profile** ou **CSS Template** pour créer de nouveaux modèles pour vos messages in-app.

#### Profil de couleurs {#color-profile}

Vous pouvez personnaliser le jeu de couleurs de votre modèle de message en saisissant un code couleur HEX ou en sélectionnant la case colorée et en choisissant une couleur avec le sélecteur de couleurs. Si vous souhaitez que ce profil soit appliqué par défaut lorsque vous créez de nouveaux messages in-app dans l'éditeur traditionnel, sélectionnez **Use as default profile**.

Sélectionnez **Save Color Profile** lorsque vous avez terminé.

![L'éditeur de modèle de profil de couleurs pour les messages in-app.]({% image_buster /assets/img/drag_and_drop/templates/color_profile_template.png %})

#### Modèle CSS {#in-app-message-templates}

Vous pouvez personnaliser un modèle CSS complet pour votre [message in-app de type fenêtre modale web](#web-modal-css).

Nommez et étiquetez votre modèle CSS, puis choisissez s'il sera votre modèle par défaut. Vous pouvez écrire votre propre CSS dans l'espace prévu. Cet espace est déjà prérempli avec le CSS affiché dans l'aperçu de votre message, et vous pouvez l'ajuster selon vos besoins.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

Vous pouvez tout modifier, de la couleur d'arrière-plan à la taille et à l'épaisseur de la police, et bien plus encore.

#### Fenêtre modale avec CSS (web uniquement) {#web-modal-css}

Si vous choisissez d'utiliser un message de type fenêtre modale web avec CSS (web uniquement), vous pouvez appliquer votre propre modèle ou écrire votre propre CSS dans l'espace prévu. Cet espace est déjà prérempli avec le CSS affiché dans l'aperçu de votre message, mais vous pouvez l'ajuster selon vos besoins.

Si vous choisissez d'appliquer votre propre modèle, sélectionnez **Apply Template** et choisissez dans la galerie de modèles de messages in-app. Si vous n'avez aucune option, vous pouvez ajouter un [modèle CSS](#in-app-message-templates) à l'aide du générateur de modèles CSS dans **Templates** > **In-App Message Templates**.