---
nav_title: Bibliothèque multimédia
article_title: Bibliothèque multimédia
page_order: 2
page_type: reference
description: "Cet article de référence présente la bibliothèque multimédia. Vous y découvrirez comment gérer vos ressources depuis un emplacement unique et centralisé, générer des images grâce à l'intelligence artificielle et accéder aux médias dans votre éditeur de messages."
tool: Media

---

# Bibliothèque multimédia

> La bibliothèque multimédia vous permet de gérer vos ressources depuis un emplacement unique et centralisé.

## Bibliothèque multimédia et réseau de diffusion de contenu {#media-library-versus-cdn}

L'utilisation de la bibliothèque multimédia plutôt qu'un réseau de diffusion de contenu (CDN) offre une meilleure mise en cache et de meilleures performances pour les messages in-app. Toutes les ressources de la bibliothèque multimédia présentes dans un message in-app seront pré-cachées pour un affichage plus rapide et seront disponibles hors ligne. De plus, la bibliothèque multimédia est intégrée aux éditeurs de Braze, ce qui permet aux marketeurs de sélectionner ou d'étiqueter des images au lieu de copier-coller des URL d'images.

## Accéder à la bibliothèque multimédia {#accessing-the-media-library}

Dans la bibliothèque multimédia, vous pouvez voir le type de ressource, sa taille, ses dimensions, son URL, la date à laquelle elle a été ajoutée à la bibliothèque, ainsi que d'autres informations. Pour accéder à votre bibliothèque multimédia Braze, allez dans **Modèles** > **Bibliothèque multimédia**. Vous pouvez y effectuer les actions suivantes :

* Charger plusieurs images en une seule fois
* Charger des fichiers de contacts virtuels (.vcf)
* Charger des fichiers vidéo à utiliser dans les messages WhatsApp
* Charger un dossier contenant vos images (jusqu'à 50 images)
* [Générer une image grâce à l'intelligence artificielle](#generate-ai) et la stocker dans la bibliothèque multimédia
* Recadrer une image existante pour obtenir le bon ratio pour vos messages
* Ajouter des étiquettes ou des équipes pour mieux organiser vos images
* Rechercher par étiquettes ou par équipes dans la grille de la bibliothèque multimédia
* Glisser-déposer des images ou des dossiers à charger
* Supprimer des images

![Page de la bibliothèque multimédia comprenant une section « Charger dans la bibliothèque » permettant de glisser-déposer ou de charger des fichiers. On y trouve également une liste des contenus chargés dans la bibliothèque multimédia.]({% image_buster /assets/img_archive/media_library_main.png %})

Par la suite, lorsque vous rédigez un message dans Braze, vous pouvez intégrer vos images depuis la bibliothèque multimédia.

![Deux façons courantes d'accéder à la bibliothèque multimédia selon l'éditeur de messages. L'une montre l'éditeur par glisser-déposer pour les e-mails avec le titre « Images et GIF » et un bouton « Ajouter depuis la bibliothèque multimédia ». L'autre montre les éditeurs standard, tels que ceux pour les notifications push et les messages in-app, avec le titre « Média » et un bouton « Ajouter image ».]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Pour en savoir plus sur la bibliothèque multimédia, consultez notre [FAQ sur la bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq/). {% endalert %}

## Spécifications des images {#image-specifications}

Toutes les images chargées dans la bibliothèque multimédia doivent peser moins de 5&nbsp;Mo. Les types de fichiers pris en charge sont PNG, JPEG, GIF, SVG et WebP. Pour connaître les tailles et spécifications d'images recommandées par canal de communication, consultez les [Spécifications des images]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/).

{% alert important %}
Les GIF aux proportions très allongées (par exemple, 3000 × 2 pixels) ou comportant 300 images ou plus peuvent échouer au chargement, même si la taille totale du fichier est faible.
{% endalert %}

## Générer des images avec BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Avant d'utiliser cette fonctionnalité, consultez [comment vos données sont utilisées et envoyées à OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}