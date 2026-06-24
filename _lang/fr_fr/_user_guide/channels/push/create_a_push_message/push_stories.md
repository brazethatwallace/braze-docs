---
nav_title: "Contenu push"
article_title: "Contenu push"
page_order: 2
page_type: reference
description: "Cet article de référence explique ce que sont les contenus push, comment en créer un, et répond à quelques questions fréquemment posées."
channel:
  - push

---

# Contenu push {#push-stories}

> Les contenus push reprennent la fonctionnalité de carrousel photo popularisée par Instagram et Facebook et permettent aux marketeurs de créer un carrousel de pages au sein d'une notification push qui raconte une histoire riche et cohérente. Ces pages se composent d'une image, d'une action au clic, d'un titre et d'une description. Vos utilisateurs peuvent faire défiler ces pages et découvrir l'histoire que vous leur racontez.

| Exemple Android (développé) | Exemple iOS (développé) |
| :-----: | :----------: |
| ![Aperçu des contenus push sur Android.]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![Aperçu des contenus push sur iOS]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Contenu push" }

{% alert note %}
À partir des versions 3.13.0+ du SDK iOS, en raison d'un changement dans la façon dont le SDK télécharge les images, une miniature de la première image ne s'affichera pas dans la vue condensée de la notification push. Assurez-vous que le texte de votre message incite les utilisateurs à développer la notification push pour voir les images.
{% endalert %}

## Conditions préalables {#prerequisites}

Les versions suivantes du SDK sont requises pour recevoir les contenus push :

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Comment utiliser les contenus push {#how-to-use-push-stories}

![Menu déroulant de l'éditeur de contenu push]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Pour utiliser les contenus push, procédez comme suit :

1. Créez une [campagne push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/).
2. Pour votre **Notification Type**, sélectionnez **Push Stories**.
3. Sélectionnez **iOS** ou **Android**. Notez que si vous sélectionnez les deux pour un message push, l'option de création d'un contenu push n'apparaîtra pas.

### Éditeur de contenu push {#push-story-composer}

Pour créer une page, effectuez les étapes suivantes :

1. Sélectionnez **Add new page** depuis l'éditeur principal.
2. Insérez une image pour chaque page, ainsi que le comportement au clic pour cette image.
3. Si vous le souhaitez, ajoutez un **Title** et une **Description** pour chaque page. Si vous utilisez un titre et une description pour une page, ils doivent être renseignés pour toutes les pages.

Les prévisualisations sont reflétées et interactives.

![Éditeur de contenu push]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
Si vous intégrez des images avec le [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/#about-connected-content), assurez-vous que l'URL de votre image commence par `https://`. L'utilisation de `http://` provoquera un plantage de votre application.
{% endalert %}

### Spécifications des images et du texte {#image-and-text-specifications}

Les spécifications suivantes concernant les images et le texte s'appliquent à la partie carrousel photo des contenus push. Pour plus d'informations sur la notification push de base avec laquelle les utilisateurs interagissent pour activer le contenu push, consultez [Formats des messages push et des images]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/).

{% tabs %}
{% tab Images %}

- **Ratio de l'image :** 2:1 (obligatoire)
- **Taille d'image recommandée :** 500 Ko
- **Taille d'image maximale :** 5 Mo
- **Types de fichiers :** PNG, JPEG

{% endtab %}
{% tab Texte %}

- **Titre :** 30 caractères (recommandé)
- **Description :** 30 caractères (recommandé)

{% alert note %}
Bien qu'il puisse y avoir des variations de longueur de caractères d'un appareil à l'autre, le titre et la description des contenus push sont limités à une seule ligne chacun. Le reste de votre message sera tronqué. Testez toujours votre message sur un appareil réel.
{% endalert %}

{% endtab %}
{% endtabs %}

### Segmentation des contenus push {#push-story-segmentation}

Lorsque vous créez une campagne ou un Canvas, vous pouvez filtrer les utilisateurs que vous souhaitez cibler en fonction de leur interaction avec une page de contenu push. Sélectionnez ensuite la campagne et la page que vous souhaitez utiliser pour cibler vos utilisateurs.

### Analyse des contenus push {#push-stories-analytics}

L'analyse sera très similaire à la section d'analyse actuelle des notifications push. Pour l'analyse des contenus push, vous pouvez développer l'indicateur **Ouvertures directes** pour afficher les clics par page.

![Tableau de performance push iOS avec des exemples d'analyse et des détails développés pour l'indicateur Ouvertures directes.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Résolution des problèmes {#troubleshooting}

### iOS

#### Je me suis envoyé un contenu push mais je n'ai pas reçu la notification {#i-sent-myself-a-push-story-but-didnt-receive-the-notification}

Apple a mis en place des règles spécifiques qui empêchent certains types de notifications d'être envoyées à un appareil en fonction de différents facteurs. Cela inclut l'évaluation du forfait de données des clients, la taille de la notification et la capacité de stockage des clients. Par conséquent, il arrive parfois qu'aucune notification ne soit envoyée à vos clients.

Ce sont des limitations imposées par Apple qui doivent être prises en compte lors de la conception de votre contenu push.

#### Je me suis envoyé un contenu push mais j'ai vu la vue condensée à la place {#i-sent-myself-a-push-story-but-saw-the-condensed-view-instead}

Dans certaines situations où toutes les pages ne se chargent pas, par exemple en raison d'une perte de connexion de données, le contenu push n'affichera que la notification condensée.

### Android

#### Le contenu push ne se ferme pas après avoir cliqué sur l'image {#push-story-doesnt-dismiss-after-clicking-the-image}

Par défaut, les contenus push ne se ferment pas sur Android après qu'un utilisateur a cliqué sur l'image. Si vous souhaitez fermer la notification, appelez [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721).