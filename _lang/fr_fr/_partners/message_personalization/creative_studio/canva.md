---
nav_title: Canva
article_title: Canva
description: "Cet article de référence décrit le partenariat entre Braze et Canva pour envoyer des ressources multimédias dans la bibliothèque multimédia de Braze et publier des conceptions d'e-mails Canva en tant que modèles d'e-mail Braze."
alias: /partners/canva/
page_type: partner
search_tag: Partner

---

# Canva

> [Canva](https://www.canva.com/) est une plateforme et un outil de conception graphique qui vous permet de créer du contenu visuel pour les publications sur les réseaux sociaux, les présentations, les vidéos et bien plus encore. L'application Braze dans Canva prend également en charge l'exportation de conceptions d'**e-mails** en tant que modèles d'e-mail Braze, en plus de l'envoi de conceptions statiques vers votre bibliothèque multimédia.

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Canva prend en charge deux chemins d'exportation :

| Type d'exportation | Description |
| --- | --- |
| **Image ou conception vers la bibliothèque multimédia** | Envoie votre conception en tant que ressource dans la bibliothèque multimédia de Braze. |
| **Conception d'e-mail vers Braze** | Publie un document **E-mail** Canva en tant que modèle d'e-mail Braze, y compris les métadonnées de la ligne d'objet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="À propos de l'intégration" }

## Intégrer Braze avec Canva {#integrate-braze-with-canva}

### Étape 1 : Installer l'application Braze dans Canva {#step-1-install-the-braze-app-in-canva}

Vous pouvez trouver l'application Braze dans le [Canva Apps Marketplace](https://www.canva.com/your-apps/AAG1cO7kIyc).

Après avoir installé l'application, elle est disponible dans une conception, sous le menu **Apps**.

![Application Braze dans le menu Apps de Canva.]({% image_buster /assets/img/canva_integration/braze-canva-app.png %}){: style="max-width:50%;"}

### Étape 2 : Autoriser votre compte Braze {#step-2-authorize-your-braze-account}

La première fois que vous utilisez l'application Braze — que vous l'ouvriez depuis le menu **Apps** (exportation vers la bibliothèque multimédia) ou depuis le menu **Share** (exportation d'e-mail) — sélectionnez **Connect** pour lancer l'autorisation. Cela permet à Canva de lister les espaces de travail Braze auxquels vous avez accès et de créer des ressources dans la bibliothèque multimédia en votre nom.

Pour les exportations d'**e-mails**, Canva peut vous demander de vous reconnecter et d'approuver des accès supplémentaires, y compris l'autorisation de **créer des modèles d'e-mail**. Acceptez ces autorisations pour terminer la publication des conceptions d'e-mails vers Braze.

![Bouton Connect et flux d'autorisation pour relier Canva à Braze.]({% image_buster /assets/img/canva_integration/canva-connect-panel.jpg %})

## Exporter des images vers la bibliothèque multimédia {#export-images-to-the-media-library}

Utilisez ce flux pour les conceptions Canva standard lorsque vous souhaitez obtenir un fichier dans la bibliothèque multimédia de Braze.

Les vidéos suivantes montrent comment envoyer des conceptions depuis Canva vers votre bibliothèque multimédia Braze.

Vidéo : Ouvrir l'application Braze dans Canva et lancer une exportation vers la bibliothèque multimédia.

{% multi_lang_include video.html id="uf5krks2cx" source="wistia" %}

Vidéo : Choisir un espace de travail Braze et terminer l'exportation vers la bibliothèque multimédia.
{% multi_lang_include video.html id="3d09tafx7c" source="wistia" %}

1. Depuis le menu **Apps** dans votre conception, ouvrez l'application Braze. Si vous n'êtes pas encore connecté, sélectionnez **Connect** et suivez les étapes décrites dans [Autoriser votre compte Braze](#step-2-authorize-your-braze-account).
2. Choisissez votre espace de travail de destination, saisissez éventuellement un nom de fichier, puis sélectionnez **Start Export**.

![Écran d'exportation Canva avec l'espace de travail de destination et le bouton Start Export.]({% image_buster /assets/img/canva_integration/canva-upload-screen.jpg %})

{: start="3"}
3. Lorsque votre exportation est terminée, votre nouvelle ressource est disponible dans la **Bibliothèque multimédia**, avec la source « Canva ».

![Ressource Canva exportée dans la bibliothèque multimédia de Braze.]({% image_buster /assets/img/canva_integration/media-library-source.jpg %})

## Exporter des conceptions d'e-mails en tant que modèles Braze {#export-email-designs-as-braze-templates}

Utilisez ce flux lorsque votre fichier Canva est un type de conception **E-mail**. Il publie le HTML vers Braze en tant que modèle (métadonnées similaires au flux d'images, mais vous commencez depuis **Share** au lieu de **Apps**).

1. Dans Canva, créez ou ouvrez une conception **E-mail**. Créez votre message de zéro ou utilisez un modèle d'e-mail Canva.
2. Cliquez sur **Share** en haut à droite de l'éditeur et sélectionnez **Braze**. Si Braze n'apparaît pas dans la liste, ouvrez **See more**, puis faites défiler jusqu'à **More options** pour trouver Braze.

![Autres moyens de publier dans Canva avec Braze sous More options.]({% image_buster /assets/img/canva_integration/canva-share-more-options-braze.png %})

{: start="3"}
3. Si vous êtes invité à vous connecter ou à vous reconnecter, sélectionnez **Connect** dans le panneau Braze (ou complétez le flux de connexion dans le navigateur) afin que Canva puisse créer des modèles dans votre espace de travail.

![Barre latérale Braze dans Canva invitant à se connecter pour l'exportation d'e-mails.]({% image_buster /assets/img/canva_integration/canva-email-connect-sidebar.png %})

{: start="4"}
4. Dans le panneau Braze, sélectionnez la page **E-mail** à publier (si la conception comporte plusieurs pages), choisissez votre **espace de travail Braze**, saisissez un **nom de modèle** et une **ligne d'objet**, puis sélectionnez **Publish now**. Canva affiche la progression pendant la publication de votre conception.

![Panneau Braze dans Canva avec l'espace de travail, le nom du modèle, la ligne d'objet et Publish now.]({% image_buster /assets/img/canva_integration/canva-email-publish-fields.png %})

{: start="5"}
5. Lorsque la publication est terminée, un message de succès apparaît. Sélectionnez **Check it out** pour ouvrir le modèle d'e-mail dans Braze.

![Message de succès après la publication d'une conception d'e-mail Canva vers Braze, avec Check it out.]({% image_buster /assets/img/canva_integration/canva-email-publish-success.png %})

{: start="6"}
6. Dans Braze, finalisez les paramètres d'e-mail requis — tels que l'adresse **From**, l'accroche et un lien de désabonnement — avant d'utiliser le modèle dans une campagne ou un Canvas.

![Modèle d'e-mail dans Braze ouvert depuis Canva, avec les informations d'envoi et la prévisualisation.]({% image_buster /assets/img/canva_integration/braze-email-template-from-canva.png %})