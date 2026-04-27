---
nav_title: FAQ
article_title: FAQ sur la bibliothèque multimédia
page_order: 2
page_type: FAQ
tool: Media
description: "Cet article répond aux questions fréquemment posées sur la bibliothèque multimédia dans Braze."

---

# Questions fréquemment posées

> Cette page répond aux questions fréquemment posées sur la bibliothèque multimédia dans Braze.

### Y a-t-il des limites de stockage pour les images dans la bibliothèque multimédia ?

Non, il n'y a pas de limites de stockage pour les ressources dans la bibliothèque multimédia. En revanche, il existe des limites de taille par ressource (5 Mo maximum).

### Les ressources importées ont-elles une date d'expiration ?

Non, les ressources importées dans la bibliothèque multimédia sont conservées pendant toute la durée de votre contrat avec Braze.

### Puis-je importer des ressources vidéo ?

Non, la bibliothèque multimédia ne prend pas en charge les fichiers vidéo. Nous vous recommandons de les héberger en externe, ou sur une plateforme telle que YouTube.

### Puis-je recadrer tous les types d'images ?

Non, la bibliothèque multimédia ne prend pas en charge le recadrage des images GIF.

### Comment recadrer une image existante ?

Vous pouvez recadrer une image existante en la sélectionnant dans la bibliothèque multimédia, puis en cliquant sur **Crop & Save New Image**.

![Prévisualisation d'une image de la bibliothèque multimédia.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Vous serez ensuite redirigé vers un éditeur de recadrage où vous pourrez sélectionner le type de ratio et modifier le nom de la nouvelle image. Lorsque vous cliquez sur **Save**, votre nouvelle image est prête à être utilisée.

![Fenêtre de recadrage et d'enregistrement d'une image de la bibliothèque multimédia.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Mon image expire à chaque tentative d'import. Que puis-je faire ?

Cela peut se produire pour diverses raisons, mais une solution courante consiste à optimiser votre image avant de tenter de l'importer. Vous pouvez par exemple utiliser un outil d'optimisation d'images tel que [ImageOptim](https://imageoptim.com/mac).

De plus, si votre image a été créée dans Photoshop (ou un logiciel similaire) et comporte de nombreux calques, fusionner et réduire le nombre de calques peut également aider.

### Je vois une « Erreur inattendue » lors de l'import d'une image alors qu'elle fait moins de 5 Mo et est dans un format pris en charge. Quel est le problème ?

Cela peut se produire pour deux raisons principales :

1. **Métadonnées invalides dans le fichier :** Le logiciel utilisé par Braze pour traiter les images peut rejeter les fichiers contenant des métadonnées invalides ou incompatibles. Dans certains cas, le fichier peut également être traité d'une manière qui le fait dépasser la limite de 5 Mo. Essayez d'utiliser une image différente (par exemple, réexportez ou réenregistrez l'image depuis votre éditeur d'images) ou une image provenant d'une autre source.
2. **Caractères spéciaux dans le nom du fichier :** Les noms de fichiers contenant des caractères spéciaux (tels que `&` ou `%`) peuvent provoquer l'échec de l'import. Renommez le fichier en utilisant uniquement des lettres, des chiffres, des tirets ou des underscores, puis réessayez l'import.

### Pourquoi ne puis-je pas importer n'importe quelle image dans les éditeurs de notifications push ?

Cela s'explique par le fait que la plupart des éditeurs imposent des restrictions sur le ratio d'image autorisé.