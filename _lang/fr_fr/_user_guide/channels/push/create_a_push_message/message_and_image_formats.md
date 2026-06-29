---
nav_title: "Formats de messages et d'images"
article_title: "Formats de messages et d'images"
page_order: 1
page_type: reference
description: "Cet article décrit les formats de messages et d'images pour les notifications push."
channel: push

---

# Formats de messages et d'images pour les notifications push {#push-message-and-image-formats}

> Cet article de référence décrit les formats de messages et d'images pour les notifications push.

Pour de meilleurs résultats, consultez les recommandations suivantes concernant la taille des images et la longueur des messages lors de la création de vos notifications push. Il peut y avoir des variations en fonction de la présence d'une image, de l'état de la notification (iOS) et des paramètres d'affichage de l'appareil de l'utilisateur, ainsi que de la taille de l'appareil. En cas de doute, gardez votre texte court et concis.

## Notifications push iOS et Android {#ios-and-android-push}

{% tabs local %}
{% tab Images %}

**Type d'image** | **Taille d'image recommandée** | **Taille d'image maximale** | **Types de fichiers**
--- | --- | --- | ---
(iOS) 2:1 *Recommandé* | 500&nbsp;Ko | 5&nbsp;Mo | PNG, JPEG, GIF
(Android) Icône push | 500&nbsp;Ko | 5&nbsp;Mo | PNG, JPEG
(Android) Notification étendue | 500&nbsp;Ko | 5&nbsp;Mo | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="iOS and Android push" }

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

{% endtab %}
{% tab Texte %}

| Type de message | Longueur de message recommandée (texte uniquement) | Longueur de message recommandée (enrichi)
--- | ---
(iOS) Écran de verrouillage | 160 caractères | 130 caractères
(iOS) Centre de notifications | 160 caractères | 130 caractères
(iOS) Alerte bannière | 80 caractères | 65 caractères
(Android) Écran de verrouillage | 49 caractères | N/A
(Android) Tiroir de notifications | 597 caractères | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS and Android push" }

Vous vous demandez combien de caractères vous pouvez utiliser dans une notification push iOS sans qu'elle soit tronquée ? Consultez nos [recommandations sur le nombre de caractères iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/#character-count).

{% endtab %}
{% tab Taille du payload %}

**Plateforme** | **Taille**
--- | ---
pré iOS 8 | 0,256 Ko
post iOS 8 | 2 Ko
Android (FCM) | 4 Ko
{: .reset-td-br-1 .reset-td-br-2 aria-label="iOS and Android push" }

{% endtab %}
{% tab Exemple d'image %}
{% subtabs %}
{% subtab iOS %}

![Notification push iOS avec un texte indiquant « Bonjour ! Ceci est une notification push iOS avec une image » accompagné d'un emoji. Une petite image est affichée à côté du texte.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notification push iOS en mode étendu avec le même texte que le message précédent et une image agrandie précédant le texte.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![Notification push Android avec une grande image sous le texte du message.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Les notifications avec de grandes images s'affichent au mieux avec une image d'au moins 600x300 pixels.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Exemple de texte %}
{% subtabs %}
{% subtab iOS %}

![Notification push iOS avec un texte indiquant « Bonjour ! Ceci est une notification push iOS ».]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
![Notification push Android affichée sur l'écran d'accueil.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Notification push Web {#web-push}

{% tabs local %}
{% tab Images %}

| **Navigateur** | **Taille d'icône recommandée**
| --- | ---
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web push" }
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (les icônes sont configurables par campagne avec Safari 16+ sur macOS 13+)
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web push" }

| **Navigateur** | **Plateforme** | **Taille de la grande image**
| --- | --- | ---
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web push" }
Chrome | Android | Rapport hauteur/largeur 2:1
Firefox | Android | N/A
Chrome | Windows | Rapport hauteur/largeur 2:1
Edge | Windows | Rapport hauteur/largeur 2:1
Firefox | Windows | N/A
Firefox | Windows | Rapport hauteur/largeur 2:1
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web push" }

{% endtab %}
{% tab Texte %}

| **Navigateur** | **Plateforme** | **Longueur maximale du titre**  | **Longueur maximale du corps du message**
| --- | --- | --- | ---
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Web push" }
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Web push" }

{% endtab %}
{% endtabs %}