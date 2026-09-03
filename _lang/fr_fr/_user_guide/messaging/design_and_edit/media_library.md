---
nav_title: Bibliothèque multimédia
article_title: Bibliothèque multimédia
page_order: 2
page_type: reference
description: "Cet article de référence présente la bibliothèque multimédia. Vous y découvrirez comment gérer vos ressources depuis un emplacement unique et centralisé, générer des images grâce à l'intelligence artificielle et accéder aux médias dans votre éditeur de messages."
tool: Media

---

# Bibliothèque multimédia {#media-library}

> La bibliothèque multimédia vous permet de gérer vos ressources depuis un emplacement unique et centralisé.

## Prérequis {#prerequisites}

| Exigences | Description |
|---|---|
| Permission « View Media Library Assets » | Consulter les ressources de la bibliothèque multimédia |
| Permission « Edit Media Library Assets » | Créer et mettre à jour les ressources de la bibliothèque multimédia |
| Permission « Delete Media Library Assets » | Supprimer les ressources de la bibliothèque multimédia depuis l'interface. Les ressources supprimées restent hébergées par Braze afin de ne pas interrompre les messages qui les référencent. Pour supprimer définitivement une ressource, contactez le support Braze. |
| Permission « Replace Media Library Assets » | Remplacer le fichier d'une ressource existante de la bibliothèque multimédia tout en conservant son URL et son ID de ressource |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissions de la bibliothèque multimédia" }

Pour plus d'informations, consultez [Permissions des utilisateurs]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Bibliothèque multimédia versus CDN {#media-library-versus-cdn}

L'utilisation de la bibliothèque multimédia plutôt qu'un réseau de diffusion de contenu (CDN) offre une meilleure mise en cache et de meilleures performances pour les messages in-app. Toutes les ressources de la bibliothèque multimédia présentes dans un message in-app sont pré-mises en cache pour un affichage plus rapide et sont disponibles pour un affichage hors ligne. De plus, la bibliothèque multimédia est intégrée aux compositeurs de Braze, ce qui vous permet de sélectionner ou d'étiqueter des images au lieu de copier-coller des URL d'images.

## Accéder à la bibliothèque multimédia {#accessing-the-media-library}

Dans la bibliothèque multimédia, vous pouvez voir le type de ressource, la taille, les dimensions, l'URL, la date d'ajout à la bibliothèque et d'autres informations. Pour accéder à votre bibliothèque multimédia Braze, allez dans **Contenu** > **Bibliothèque multimédia**. Vous pouvez y effectuer les actions suivantes :

* Télécharger plusieurs images en une seule fois
* Télécharger des fichiers de contacts virtuels (.vcf)
* Télécharger des fichiers vidéo pour les utiliser dans les messages WhatsApp
* Télécharger un dossier contenant vos images (jusqu'à 50 images)
* [Générer une image à l'aide de l'IA](#generate-ai) et la stocker dans la bibliothèque multimédia
* Recadrer une image existante pour créer le bon ratio pour vos messages
* Remplacer le fichier d'une ressource existante tout en conservant son URL stable
* Ajouter des tags ou des équipes pour mieux organiser vos images
* Rechercher par tags ou par équipes dans la grille de la bibliothèque multimédia
* Glisser-déposer des images ou des dossiers à télécharger
* Supprimer des images

![Page de la bibliothèque multimédia comprenant une section « Télécharger dans la bibliothèque » pour glisser-déposer ou télécharger des fichiers. On y trouve également une liste du contenu téléchargé dans la bibliothèque multimédia.]({% image_buster /assets/img_archive/media_library_main.png %})

Par la suite, lors de la rédaction d'un message dans Braze, vous pouvez intégrer vos images depuis la bibliothèque multimédia.

![Deux façons courantes d'accéder à la bibliothèque multimédia selon le compositeur de messages. L'une montre l'éditeur glisser-déposer pour les e-mails avec le titre « Images et GIF » et un bouton « Ajouter depuis la bibliothèque multimédia ». L'autre montre les éditeurs standard, tels que les notifications push et les messages in-app, avec le titre « Média » et un bouton « Ajouter une image ».]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Pour plus d'aide concernant la bibliothèque multimédia, consultez notre [FAQ sur la bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq). {% endalert %}

## Téléchargement de fichiers ZIP {#zip-file-uploads}

Lorsque vous téléchargez un fichier ZIP dans la bibliothèque multimédia, tous les fichiers doivent se trouver à la racine du dossier ZIP — n'incluez pas de sous-répertoires.

Cela s'applique à tous les fichiers de l'archive, y compris les fichiers de polices (`.ttf`, `.woff`, `.otf`, `.woff2`), HTML, CSS, JavaScript et les images. Placez chaque fichier à la racine du ZIP, aux côtés des autres.

Vous pouvez également télécharger les ressources individuellement dans la bibliothèque multimédia sans les compresser.

## Remplacer un fichier {#replace-a-file}

Vous pouvez remplacer le fichier d'une ressource existante dans la bibliothèque multimédia tout en conservant son URL et son ID de ressource. Comme l'URL ne change pas, tout message ou toute Campaign qui fait référence à cette ressource — y compris les e-mails déjà envoyés — reflète automatiquement le fichier mis à jour. Cela est utile lorsque vous souhaitez mettre à jour une ressource partagée (comme un logo) à un seul endroit plutôt que de mettre à jour chaque Campaign individuellement.

Pour remplacer une ressource, vous devez disposer de la permission « Replace Media Library Assets » :

1. Accédez à **Contenu** > **Bibliothèque multimédia**.
2. Sélectionnez la ressource que vous souhaitez remplacer.
3. Dans la fenêtre modale, sélectionnez **Replace file**.
4. Téléchargez le fichier de remplacement.

![Fenêtre modale de modification de la bibliothèque multimédia affichant les boutons Replace file, Crop image et Delete pour une ressource.]({% image_buster /assets/img_archive/media_library_replace_file.png %}){: style="max-width:60%;border:none"}

### Exigences et limitations {#requirements-and-limitations}

- Le fichier de remplacement doit avoir la même extension de fichier que l'original. Par exemple, vous ne pouvez pas remplacer une ressource `.png` par un fichier `.jpg`.
- Les ressources vidéo ne peuvent pas être remplacées.
- Après le remplacement, le fichier mis à jour peut mettre un certain temps à s'afficher pour tous les utilisateurs en raison de la mise en cache du CDN.

### Canaux avec des copies d'images optimisées {#channels-with-processed-image-copies}

Certains canaux créent une copie optimisée de l'image lors de la configuration du message, ce qui génère une URL distincte. Cela s'applique que l'image ait été ajoutée depuis la bibliothèque multimédia ou via une URL externe (par exemple, depuis un compartiment S3). Le remplacement de la ressource d'origine dans la bibliothèque multimédia ne met pas à jour ce que les utilisateurs voient pour les messages créés à l'aide de ces canaux, y compris les Content Cards, les notifications push et les bannières.

Les messages in-app traditionnels (fenêtre modale, contextuel et plein écran) suivent également ce comportement. Cependant, les messages in-app HTML et les messages in-app par glisser-déposer ne le font pas. Pour ces types, Braze ne met pas l'image en cache, donc modifier ou supprimer l'URL de l'image d'origine casse l'image dans les Campaigns en cours.

Vous pouvez également remplacer une ressource de manière programmatique à l'aide de l'endpoint [`PUT /media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file).

## Spécifications des images {#image-specifications}

Toutes les images téléchargées dans la bibliothèque multimédia doivent peser moins de 5&nbsp;Mo. Les types de fichiers pris en charge sont PNG, JPEG, GIF, SVG et WebP. Pour connaître les tailles et spécifications d'images recommandées par canal de communication, consultez [Spécifications des images]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications).

{% alert important %}
Les GIF avec des formes très allongées (par exemple, 3000 x 2 pixels) ou comportant 300 images ou plus peuvent échouer lors du téléchargement, même si la taille totale du fichier est faible.
{% endalert %}

## Générer des images avec BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Avant d'utiliser cette fonctionnalité, consultez [comment vos données sont utilisées et envoyées à OpenAI]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#data-privacy-and-security).
{% endalert %}

Si vous ne voyez pas **Générer avec Operator** sur la page **Bibliothèque multimédia**, vérifiez que vous disposez de l'autorisation « Edit Media Library Assets ». Si l'option est toujours absente, contactez votre équipe Braze pour confirmer que votre espace de travail a accès à la génération d'images BrazeAI. Si la génération échoue, consultez la [politique de contenu d'OpenAI]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#data-privacy-and-security).