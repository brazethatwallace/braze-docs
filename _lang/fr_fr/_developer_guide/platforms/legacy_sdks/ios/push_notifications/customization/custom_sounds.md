---
nav_title: Sons personnalisés
article_title: Sons de notification push personnalisés pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence explique comment implémenter des sons personnalisés dans vos notifications push iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Sons personnalisés {#custom-sounds}

## Étape 1 : Héberger les sons dans l'application {#step-1-hosting-the-sound-in-the-app}

Les sons des notifications push personnalisées doivent être hébergés localement dans le lot principal de l'application client. Les formats de données audio suivants sont acceptés :

- Linear PCM
- MA4
- µLaw
- aLaw

Vous pouvez regrouper les données audio dans un fichier AIFF, WAV ou CAF. Dans Xcode, ajoutez le fichier audio à votre projet comme ressource non localisée du lot d'applications.

Vous pouvez utiliser l'outil afconvert pour convertir les sons. Par exemple, pour convertir le son système PCM linéaire 16 bits Submarine.aiff en audio IMA4 dans un fichier CAF, utilisez la commande suivante dans le terminal :

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

Vous pouvez inspecter un son pour déterminer son format de données en l'ouvrant dans QuickTime Player et en choisissant **Show Movie Inspector** dans le menu **Movie**.

Les sons personnalisés doivent durer moins de 30 secondes lorsqu'ils sont joués. Si un son personnalisé dépasse cette limite, le son système par défaut est joué à la place.

## Étape 2 : Fournir au tableau de bord une URL de protocole pour le son {#step-2-providing-the-dashboard-with-a-protocol-url-for-the-sound}

Votre son doit être hébergé localement dans l'application. Vous devez spécifier une URL de protocole pointant vers l'emplacement du fichier audio dans l'application, dans le champ **Sound** du compositeur de notifications push. Indiquer « default » dans ce champ jouera le son de notification par défaut sur l'appareil. Ce paramètre peut être défini via notre [API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging) ou dans notre tableau de bord sous **Settings** dans le compositeur de notifications push, comme illustré dans la capture d'écran suivante :

![Votre son doit être hébergé localement dans l'application. Vous devez spécifier une URL de protocole pointant vers l'emplacement du fichier audio dans l'application, dans le champ Sound du compositeur de notifications push. Indiquer « default » dans ce champ jouera le son de notification par défaut sur l'appareil. Ce paramètre peut être défini via notre API d'envoi de messages ou dans notre tableau de bord sous Settings dans le compositeur de notifications push, comme illustré dans la capture d'écran suivante.]({% image_buster /assets/img_archive/sound_push_ios.png %})

Si le fichier audio spécifié n'existe pas ou si le mot-clé « default » est saisi, Braze utilisera le son d'alerte par défaut de l'appareil. En dehors de notre tableau de bord, le son peut également être configuré via notre [API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging). Pour plus d'informations, consultez la documentation du développeur Apple concernant [la préparation de sons d'alerte personnalisés](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html).