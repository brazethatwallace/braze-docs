---
nav_title: Profils de couleurs et modèles CSS
article_title: Profils de couleurs et modèles CSS
page_order: 3
page_type: reference
description: "Cet article fournit un aperçu des profils de couleurs et des modèles CSS pour les messages in-app."
channel:
  - in-app messages
---

# Profils de couleurs et modèles CSS {#reusable-color-profiles}

> Vous pouvez enregistrer des modèles de messages in-app et de messages dans le navigateur sur le tableau de bord afin de créer rapidement de nouvelles campagnes et de nouveaux messages en utilisant votre style. Cet article s'applique à l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/). Si vous utilisez l'éditeur par glisser-déposer, consultez plutôt [Paramètres de style]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/).

Accédez à **Modèles** > **Modèles de messages in-app**.

Depuis cette page, vous pouvez modifier des modèles existants ou cliquer sur **+ Créer** et choisir **Profil de couleurs** ou **Modèle CSS** pour créer de nouveaux modèles à utiliser dans vos messages in-app.

## Profil de couleurs {#color-profile}

Vous pouvez personnaliser le jeu de couleurs de votre modèle de message en saisissant un code couleur HEX ou en cliquant sur la case colorée et en sélectionnant une couleur avec le sélecteur de couleurs.

Cliquez sur **Enregistrer le profil de couleurs** lorsque vous avez terminé.

### Gestion des profils de couleurs {#managing-color-profiles}

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) et [archiver]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) des modèles ! Pour en savoir plus sur la création et la gestion des modèles et du contenu créatif, consultez [Modèles et médias]({{site.baseurl}}/user_guide/messaging/templates/).

## Modèle CSS {#in-app-message-templates}

Vous pouvez personnaliser un modèle CSS complet pour votre [message in-app de type fenêtre modale web](#web-modal-css).

Nommez et étiquetez votre modèle CSS, puis choisissez s'il sera ou non votre modèle par défaut. Vous pouvez écrire votre propre CSS dans l'espace prévu à cet effet. Cet espace est déjà prérempli avec le CSS affiché dans la prévisualisation de votre message, et vous pouvez l'ajuster librement pour répondre à vos besoins.

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

Comme vous pouvez le constater, vous pouvez modifier la couleur d'arrière-plan, la taille et l'épaisseur de la police, et bien plus encore.

### Gestion des modèles CSS {#managing-css-templates}

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) et [archiver]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) des modèles ! Pour en savoir plus sur la création et la gestion des modèles et du contenu créatif, consultez [Modèles et médias]({{site.baseurl}}/user_guide/messaging/templates/).

## Fenêtre modale avec CSS (web uniquement) {#web-modal-css}

Si vous choisissez d'utiliser un message de type fenêtre modale web avec CSS (web uniquement), vous pouvez appliquer votre propre modèle ou écrire votre propre CSS dans l'espace prévu à cet effet. Cet espace est déjà prérempli avec le CSS affiché dans la prévisualisation de votre message, mais n'hésitez pas à l'ajuster pour répondre à vos besoins.

Si vous choisissez d'appliquer votre propre modèle, cliquez sur **Appliquer le modèle** et choisissez dans la galerie de modèles de messages in-app. Si vous n'avez aucune option disponible, vous pouvez télécharger un [modèle CSS]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/color_profiles_and_css_templates/#in-app-message-templates) à l'aide du générateur de modèles CSS.