---
nav_title: Spécifications des images
article_title: Spécifications des images
page_order: 1
page_type: reference
description: "Cet article de référence décrit les tailles et spécifications d'images recommandées pour chaque type de canal."
tool:
  - Templates
  - Media

---

# Spécifications des images {#image-specifications}

> En général, les images plus petites et de haute qualité se chargent plus rapidement. Nous vous recommandons donc d'utiliser la ressource la plus légère possible pour obtenir le résultat souhaité. Pour optimiser l'utilisation de vos images dans des canaux spécifiques, consultez les détails de cet article.

Vous devriez toujours [prévisualiser et tester vos messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) sur différents appareils pour vérifier que les zones les plus importantes de votre image et de votre message s'affichent comme prévu.

## Comportement des images {#image-behavior}

{% multi_lang_include channels/image_specs.md variable_name='image behavior' %}

## Vidéo {#video}

Les vidéos téléchargées dans la bibliothèque multimédia ne peuvent être utilisées que dans les messages WhatsApp. Pour plus d'informations, consultez [Créer un message WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#outbound-messages).

## GIF {#gifs}

Les GIF sont pris en charge dans les notifications push iOS, les messages in-app, les e-mails, les Content Cards et les messages MMS ou RCS. Les GIF avec des formes très allongées (par exemple, 3000 x 2 pixels) ou comportant 300 images ou plus peuvent échouer lors du téléchargement, même si la taille totale du fichier est faible.

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

## Recommandations par canal {#channel-guidance}

### Content Cards

{% multi_lang_include channels/image_specs.md variable_name='content cards' %}

### E-mail {#email}

{% multi_lang_include channels/image_specs.md variable_name='email' %}

### Messages in-app {#in-app-messages}

{% multi_lang_include channels/image_specs.md variable_name='in-app messages' %}

{% alert tip %} Créez vos ressources en toute confiance ! Nos modèles d'images pour les messages in-app et nos superpositions de zones sûres sont conçus pour s'adapter parfaitement aux appareils de toutes tailles. [Télécharger le ZIP des modèles de conception]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

Pour en savoir plus, consultez les [détails créatifs des messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize).

#### Font Awesome

Braze prend en charge l'utilisation de [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) pour les icônes des messages in-app de type fenêtre modale.

### Notifications push {#push-notifications}

{% multi_lang_include channels/image_specs.md variable_name='payload size' %}

{% multi_lang_include channels/image_specs.md variable_name='push notifications' %}

#### Longueurs de message recommandées {#recommended-message-lengths}

Pour de meilleurs résultats, consultez les recommandations de longueur de message suivantes lors de la rédaction de vos notifications push. Il peut y avoir des variations en fonction de la présence d'une image, de l'état de la notification (iOS) et du paramètre d'affichage de l'appareil de l'utilisateur, ainsi que de la taille de l'appareil.

| Type de message | Longueur recommandée (texte uniquement) | Longueur recommandée (enrichi) |
| --- | --- | --- |
| Écran de verrouillage iOS | 160 caractères | 130 caractères |
| Centre de notifications iOS | 160 caractères | 130 caractères |
| Bannière d'alerte iOS | 80 caractères | 65 caractères |
| Écran de verrouillage Android | 49 caractères | N/A |
| Tiroir de notifications Android | 597 caractères | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Longueurs de message recommandées" }

Pour en savoir plus sur le nombre de caractères iOS, consultez les [recommandations de nombre de caractères iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count).

#### Notification push Web {#web-push}

{% tabs %}
{% tab Images %}

| Navigateur | Taille d'icône recommandée |
| --- | --- |
| Chrome | 192 x 192 px ou plus |
| Firefox | 192 x 192 px ou plus |
| Safari | 192 x 192 px ou plus (configurable par Campaign avec Safari 16 sur macOS 13+) |
| Opera | 192 x 192 px ou plus |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Notification push Web" }

| Navigateur | Plateforme | Taille de la grande image |
| --- | --- | --- |
| Chrome | Android | Rapport hauteur/largeur 2:1 |
| Firefox | Android | N/A |
| Chrome | Windows | Rapport hauteur/largeur 2:1 |
| Edge | Windows | Rapport hauteur/largeur 2:1 |
| Firefox | Windows | N/A |
| Opera | Windows | Rapport hauteur/largeur 2:1 |
| Chrome | macOS | N/A |
| Safari | macOS | N/A |
| Firefox | macOS | N/A |
| Opera | macOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notification push Web" }

{% endtab %}
{% tab Texte %}

| Navigateur | Plateforme | Longueur maximale du titre | Longueur maximale du corps |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Notification push Web" }

{% endtab %}
{% endtabs %}

#### Exemples de notifications push {#push-notification-examples}

{% tabs %}
{% tab iOS %}

![Notification push iOS avec un texte indiquant : « Hi! This is an iOS Push with an image » accompagné d'un emoji. Une petite image est affichée à côté du texte.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notification push iOS en mode étendu avec le même texte que le message précédent et une image agrandie précédant le texte.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![Notification push Android avec une grande image sous le texte du message.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Les notifications avec de grandes images s'affichent au mieux avec une image d'au moins 600 x 300 pixels.
{% endalert %}

{% endtab %}
{% endtabs %}

Pour des ressources supplémentaires, consultez les [spécifications d'images et de texte pour les notifications push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats).

### SMS et MMS {#sms-and-mms}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

Pour composer des messages MMS, consultez [Créer un message SMS, MMS ou RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create).