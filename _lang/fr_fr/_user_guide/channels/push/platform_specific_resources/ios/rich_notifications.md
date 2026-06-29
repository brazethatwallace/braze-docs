---
nav_title: Créer des notifications enrichies
article_title: "Création de notifications push enrichies pour iOS"
page_order: 3
page_type: tutorial
description: "Ce tutoriel explique les conditions requises et les étapes pour créer des notifications enrichies iOS pour vos campagnes Braze."

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Créer des notifications push enrichies pour iOS {#create-rich-push-notifications-for-ios}

> Les notifications enrichies permettent une plus grande personnalisation de vos notifications push en ajoutant du contenu supplémentaire au-delà du simple texte. Les notifications Android incluent des images dans les notifications push depuis un certain temps déjà, sous la forme d'une « image de notification étendue ». À partir d'iOS 10, vos clients peuvent recevoir des notifications push iOS contenant des GIF, des images, des vidéos ou de l'audio.

## Conditions préalables {#prerequisites}

Avant de créer une notification push enrichie pour iOS, notez les détails suivants :

- Pour vous assurer que votre application peut envoyer des notifications enrichies, suivez les instructions d'[intégration push iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications), car votre développeur devra ajouter une extension de service à votre application.
- Les types de fichiers que nous prenons actuellement en charge pour le téléchargement direct dans notre tableau de bord sont JPEG, PNG ou GIF. Ces fichiers peuvent également être saisis dans le champ d'URL modélisable, ainsi que les types de fichiers supplémentaires suivants : AIF, M4A, MP3, MP4 ou WAV.
- Consultez la [documentation d'Apple](https://developer.apple.com/reference/usernotifications/unnotificationattachment) pour les limitations et spécifications des médias.
- iOS redimensionne les images pour les adapter à l'écran et redimensionne les images enrichies pour l'affichage actif ou verrouillé.

{% alert note %}
Depuis janvier 2020, les notifications push enrichies iOS peuvent gérer des images de 1038x1038 de moins de 10&nbsp;Mo, mais nous recommandons d'utiliser la taille de fichier la plus petite possible. En pratique, l'envoi de fichiers volumineux peut entraîner un stress réseau inutile et rendre les délais d'expiration de téléchargement plus fréquents.
{% endalert %}

{% alert important %}
Les images des notifications push peuvent ne pas s'afficher comme prévu si la taille du fichier image est trop importante, si le rapport hauteur/largeur est incorrect, si le texte dépasse la longueur maximale du message ou si le texte du titre dépasse la longueur maximale du titre.
{% endalert %}

### Nombre de caractères {#character-count}

Bien que nous ne puissions pas fournir de règle stricte sur le nombre précis de caractères à inclure dans une notification push, nous [fournissons quelques recommandations]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/) à prendre en compte lors de la conception de messages iOS. Il peut y avoir des variations en fonction de la présence d'une image, de l'état de la notification et des paramètres d'affichage de l'appareil de l'utilisateur, ainsi que de la taille de l'appareil. En cas de doute, restez bref et concis.

En tant que bonne pratique, Braze recommande de limiter chaque ligne de texte, tant pour le titre optionnel que pour le corps du message, à environ 30 à 40 caractères dans une notification push mobile.

#### États de notification {#notification-states}

Vos utilisateurs peuvent voir les notifications push dans différentes situations et peuvent voir des longueurs de texte différentes comme suit.

<table aria-label="États de notification">
  <caption>États de notification</caption>
<thead>
  <tr>
    <th>Écran de verrouillage ou Centre de notifications</th>
    <th>Étendue</th>
    <th>Appareil actif</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">C'est le scénario le plus courant.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 4 lignes de texte<br><b>Image :</b> miniature carrée</td>
    <td width="33%">Lorsqu'un utilisateur appuie longuement sur un message.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 7 lignes de texte<br><b>Image :</b> rapport hauteur/largeur 2:1 (recommandé, voir la note suivante)</td>
    <td width="33%">Lorsqu'un utilisateur reçoit une notification push alors que son téléphone est déverrouillé et actif.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 2 lignes de texte</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="États de notification" }

![Exemples de notifications push affichées sur l'écran de verrouillage, en mode étendu et lorsque l'appareil est actif.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Bien que nous recommandions un rapport hauteur/largeur de 2:1 pour les notifications push étendues, presque tous les rapports hauteur/largeur sont pris en charge. Les images s'étendent toujours sur toute la largeur de la notification, et la hauteur s'ajuste en conséquence.
{% endalert %}

#### Variables dans la troncature du texte {#variables-in-text-truncation}

Lors de la création de contenu, tenez compte des scénarios suivants qui peuvent affecter la quantité de texte affichée.

{% tabs %}
{% tab Horodatage %}

Selon le moment où un utilisateur interagit avec une notification push, l'horodatage peut raccourcir le texte du titre.

![Exemple de notification push avec un horodatage « maintenant » et un nombre de caractères du titre de 35.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Nombre de caractères du titre : **35**

![Exemple de notification push avec un horodatage « il y a 3 h » et un nombre de caractères du titre de 33.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Nombre de caractères du titre : **33**

![Exemple de notification push avec un horodatage « Hier, 8 h 37 » et un nombre de caractères du titre de 22.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Nombre de caractères du titre : **22**

{% endtab %}
{% tab Images %}

Le texte du corps est raccourci d'environ 10 caractères par ligne lorsqu'une image est présente.

![Exemple de notification push sans image et un nombre de caractères du corps de 179.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Nombre de caractères du corps : **179**

![Exemple de notification push avec une image et un nombre de caractères du corps de 154.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Nombre de caractères du corps : **154**

{% endtab %}
{% tab Niveau d'interruption %}

Pour iOS 15, les mentions « Urgent » et « Critique » poussent le titre sur une nouvelle ligne sans l'horodatage, lui donnant un peu plus d'espace.

![Exemple de notification push sans mention « Urgent » ou « Critique » et un nombre de caractères du titre de 35.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Nombre de caractères du titre : **35**

![Exemple de notification push avec une mention « Urgent » et un nombre de caractères du titre de 39.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Nombre de caractères du titre : **39**

{% endtab %}
{% tab Autres %}

Les détails suivants peuvent également affecter la troncature du texte :

- **Paramètres d'affichage du téléphone :** un utilisateur peut augmenter ou diminuer la taille globale de la police de l'interface sur son téléphone, généralement pour des raisons d'accessibilité.
- **Largeur de l'appareil :** le message peut être affiché sur un petit téléphone ou un iPad large.
- **Types de contenu :** les emojis et les caractères larges comme « m » et « w » prennent plus de place que « i » ou « t », et les mots longs comme « engagement » peuvent être coupés plus brusquement que les mots courts.

{% endtab %}
{% endtabs %}

## Configurer votre notification enrichie iOS {#setting-up-your-ios-rich-notification}

### Étape 1 : Créer une campagne push {#step-1-create-a-push-campaign}

Suivez les [étapes de la campagne]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/#creating-a-push-message) pour composer une notification push pour iOS. Vous utiliserez le même composeur que celui que vous utilisez pour configurer des notifications push qui ne contiennent pas de contenu enrichi.

### Étape 2 : Ajouter des médias {#step-2-add-media}

Ajoutez votre fichier image, GIF, audio ou vidéo dans le champ **iOS Notification Image** du composeur de message. Consultez les [conditions requises](#requirements) pour savoir comment ajouter vos fichiers de contenu.

![Exemple de texte de résumé pour une notification push.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

Vous pouvez également limiter ce message aux seuls utilisateurs disposant d'un appareil fonctionnant sous iOS 10. Pour les utilisateurs qui n'ont pas mis à jour vers iOS 10, la notification apparaîtra sous forme de texte uniquement, sans le contenu enrichi, si vous laissez l'option **Only send to devices with Rich Notification support** décochée.

![La section d'image de notification étendue où vous pouvez ajouter une image ou saisir une URL d'image.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### Étape 3 : Continuer la création de votre campagne {#step-3-continue-creating-your-campaign}

Une fois votre contenu de notification enrichie téléchargé dans le tableau de bord, vous pouvez continuer à [planifier votre campagne]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/#schedule-push-campaign).

Lorsqu'un utilisateur reçoit la notification push, il peut appuyer fermement sur le message pour agrandir l'image.

![Un utilisateur reçoit une notification push et appuie fermement sur le message pour afficher une image agrandie qui dit « Hello! ».]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }