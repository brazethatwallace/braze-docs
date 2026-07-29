---
nav_title: FAQ
article_title: FAQ sur la bibliothèque multimédia
page_order: 2
page_type: FAQ
tool: Media
description: "Cet article répond aux questions fréquemment posées sur la bibliothèque multimédia dans Braze."

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cette page répond aux questions fréquemment posées sur la bibliothèque multimédia dans Braze.

## Général {#general}

### Existe-t-il des limites de stockage pour les images dans la bibliothèque multimédia ? {#are-there-storage-limits-for-images-within-the-media-library}

Non, il n'y a pas de limites de stockage pour les ressources dans la bibliothèque multimédia. Cependant, il existe des limites de taille pour les ressources (maximum 5 Mo).

### Les ressources téléchargées ont-elles une date d'expiration ? {#are-there-expiration-dates-for-uploaded-assets}

Non, les ressources téléchargées dans la bibliothèque multimédia sont conservées pendant toute la durée de votre contrat avec Braze.

### Puis-je télécharger des ressources vidéo ? {#can-i-upload-video-assets}

Non, la bibliothèque multimédia ne prend pas en charge les fichiers vidéo. Nous vous recommandons de les héberger en externe ou sur une plateforme telle que YouTube.

### Puis-je recadrer tous les types d'images ? {#can-i-crop-all-image-types}

Non, la bibliothèque multimédia ne prend pas en charge le recadrage des images GIF.

### Comment copier l'URL d'une image téléchargée dans la bibliothèque multimédia ? {#how-do-i-copy-the-url-of-an-image-uploaded-to-the-media-library}

Pour copier l'URL d'une image téléchargée dans la bibliothèque multimédia, accédez à **Contenu** > **Bibliothèque multimédia**. Survolez l'image que vous souhaitez référencer, puis sélectionnez l'icône **Copy Image URL** pour copier l'URL de l'image dans votre presse-papiers.

### Puis-je utiliser des images SVG dans les e-mails ? {#can-i-use-svg-images-in-email}

Les images SVG ne sont pas recommandées pour les e-mails en raison d'une prise en charge limitée par les clients de messagerie. Gmail et plusieurs autres fournisseurs de messagerie majeurs n'affichent pas les images SVG, ce qui peut entraîner des images cassées ou manquantes pour les destinataires. Pour un rendu fiable des e-mails, utilisez plutôt les formats PNG, JPEG ou GIF.

### Comment recadrer une image existante ? {#how-do-i-crop-an-existing-image}

Vous pouvez recadrer une image existante en la sélectionnant dans la bibliothèque multimédia et en cliquant sur **Crop & Save New Image**.

![Aperçu d'une image de la bibliothèque multimédia.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Vous serez ensuite redirigé vers un éditeur de recadrage où vous pourrez sélectionner votre type de ratio et modifier le nom de la nouvelle image. Lorsque vous sélectionnez **Save**, votre nouvelle image est prête à être utilisée.

![Fenêtre pour recadrer et enregistrer une image de la bibliothèque multimédia.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Mon image expire à chaque tentative de téléchargement. Que puis-je faire ? {#my-image-keeps-timing-out-when-i-try-to-upload-it-what-can-i-do-about-this}

Cela peut se produire pour diverses raisons, mais une solution courante consiste à optimiser votre image avant de tenter de la télécharger. Cela signifie passer votre image dans un optimiseur d'images tel que [ImageOptim](https://imageoptim.com/mac).

De plus, si votre image a été créée dans Photoshop (ou un logiciel similaire) et comporte de nombreux calques, fusionner et réduire le nombre de calques peut également aider.

### Je vois une « Erreur inattendue » lors du téléchargement d'une image alors qu'elle fait moins de 5 Mo et est dans un format pris en charge. Quel est le problème ? {#i-see-an-unexpected-error-when-uploading-an-image-even-though-its-under-5-mb-and-in-a-supported-format-whats-wrong}

Cela peut se produire pour deux raisons principales :

1. **Métadonnées invalides dans le fichier :** Le logiciel utilisé par Braze pour traiter les images peut rejeter les fichiers contenant des métadonnées invalides ou incompatibles. Dans certains cas, le fichier peut également être traité d'une manière qui le fait dépasser la limite de 5 Mo. Essayez d'utiliser une image différente (par exemple, réexportez ou réenregistrez l'image depuis votre éditeur d'images) ou une image provenant d'une autre source.
2. **Caractères spéciaux dans le nom du fichier :** Les noms de fichiers contenant des caractères spéciaux (tels que `&` ou `%`) peuvent provoquer l'échec du téléchargement. Renommez le fichier en utilisant uniquement des lettres, des chiffres, des tirets ou des underscores, puis réessayez le téléchargement.

### Pourquoi ne puis-je pas télécharger n'importe quelle image dans les éditeurs de notifications push ? {#why-cant-i-upload-any-image-i-want-into-the-push-composers}

C'est parce que la plupart des éditeurs imposent des restrictions sur le ratio d'image autorisé.

### Générer une image à l'aide de l'IA {#generate-an-image-using-ai}

Vous pouvez générer des images depuis **Contenu** > **Bibliothèque multimédia** en sélectionnant **AI Image Generator**. Vous devez disposer de la permission **Edit Media Library Assets**. Si vous ne voyez pas cette option, contactez votre équipe Braze. Pour les étapes et les détails de la politique, consultez [Générer des images avec BrazeAI]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-images) et [Générer des images avec BrazeAI]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#generate-ai).

### Puis-je créer des URL personnalisées pour les ressources d'images de la bibliothèque multimédia ? {#can-i-create-vanity-urls-for-media-library-image-assets}

Les URL personnalisées pour les ressources de la bibliothèque multimédia ne sont pas prises en charge, car des URL personnalisées interrompraient la distribution via le CDN. Vous pouvez remplacer une image à son URL existante lorsque des Campaigns font déjà référence à cette URL. Pour plus d'informations, consultez [Remplacer un fichier]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file).