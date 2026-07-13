---
nav_title: "Vidéo en HTML personnalisé"
article_title: "Vidéo en HTML personnalisé"
page_order: 4
page_type: reference
description: "Cet article décrit comment intégrer des vidéos dans vos messages in-app HTML."
channel:
  - in-app messages
---

# Vidéo dans les messages in-app en HTML personnalisé {#video}

> Cet article s'applique aux [messages HTML personnalisés]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) dans l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

## Intégrer des vidéos {#embed-videos}

Pour lire une vidéo dans un message in-app HTML, incluez l'élément `<video>` suivant dans votre HTML et remplacez les noms de vidéo par le nom de votre fichier (ou l'URL de la ressource distante). Vous trouverez d'autres options `<video>` possibles sur [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

Pour utiliser une ressource vidéo locale, veillez à inclure ce fichier lors du téléchargement des ressources vers votre campagne.

{% alert note %}
Le contenu vidéo n'est disponible que lorsque l'appareil dispose d'une vitesse réseau raisonnable, sauf si la vidéo est hébergée localement sur l'appareil.
{% endalert %}

## Considérations pour Android {#android-considerations}

Pour intégrer de la vidéo et d'autres contenus HTML5 dans les messages in-app HTML sur Android, l'accélération matérielle doit être activée dans l'Activity où le message in-app est affiché. Pour plus d'informations, consultez le [guide du développeur Android]({{site.baseurl}}/developer_guide/in_app_messages/html_messages#android_embedding-youtube-content).

**Lecture automatique** : même avec l'accélération matérielle activée, les WebViews Android peuvent nécessiter un geste de l'utilisateur pour démarrer la lecture multimédia. Si vous avez besoin de la lecture automatique, configurez la WebView utilisée pour afficher les messages in-app HTML afin de désactiver l'exigence de geste utilisateur en définissant [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). Cela nécessite une personnalisation au niveau du SDK de la façon dont les messages in-app HTML sont affichés. Pour des conseils de configuration, consultez [Personnaliser les messages in-app pour le SDK Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android).

## Considérations pour iOS {#ios-considerations}

Pour prendre en charge les appareils iOS :

- Vous devez inclure l'attribut `playsinline` car la lecture en plein écran n'est pas prise en charge.
- **La lecture automatique n'est pas garantie sur iOS**. Le comportement de lecture sur iOS dépend de `WKWebView` et des politiques multimédia au niveau du système d'exploitation, et peut nécessiter un geste de l'utilisateur même lorsque `autoplay` et `muted` sont définis. Testez votre message in-app HTML sur vos versions et appareils iOS cibles.

Si la lecture automatique est requise et que vos tests montrent qu'elle ne fonctionne pas par défaut, vous pouvez personnaliser la `WKWebViewConfiguration` utilisée par les messages in-app HTML pour ajuster l'exigence d'action utilisateur pour la lecture multimédia, par exemple en définissant la propriété `mediaTypesRequiringUserActionForPlayback`. Cela nécessite une personnalisation au niveau du SDK. Pour les ressources Swift, consultez [Personnaliser les messages in-app pour le SDK Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=swift) et [Ajouter l'interface JavaScript de Braze aux WebViews pour Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages?sdktab=swift).

## Considérations pour le Web {#web-considerations}

La plupart des navigateurs modernes n'autorisent la lecture automatique que sous certaines conditions (généralement lorsque la vidéo est en sourdine). Si vous utilisez `autoplay` dans un message in-app web, incluez `muted` et testez sur l'ensemble de vos navigateurs et appareils pris en charge, car les politiques des navigateurs varient et peuvent toujours nécessiter un geste de l'utilisateur dans certains cas.

Pour lire automatiquement des vidéos YouTube dans un message in-app web, ajoutez le paramètre d'URL `&autoplay=1`. Par exemple, la vidéo suivante sera lue automatiquement, sera en sourdine (`&mute=1`) et n'affichera pas de contrôles (`&controls=0`) :

```html
<iframe class="video" src="https://www.youtube.com/embed/VPIPAc4oQqw?autoplay=1&mute=1&controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Affichage des vidéos YouTube {#how-youtube-videos-display}

- Les messages in-app avec vidéo YouTube intégrée peuvent s'afficher directement dans l'application ou dans un onglet séparé au sein de l'application, selon la plateforme.
- Le texte du message in-app peut ne pas s'afficher lorsque l'intégration YouTube est visible.

## Résolution des problèmes {#troubleshooting}

Si votre message in-app n'affiche pas votre vidéo :

- Vérifiez que votre URL est valide.
- Vérifiez qu'il ne manque pas la déclaration `type="video/mp4"` (pour les vidéos autres que YouTube).
- Ajoutez les balises fermantes manquantes et corrigez les fautes de frappe.