---
nav_title: Canaux
article_title: Canaux
page_order: 5
layout: dev_guide
guide_top_header: "Canaux"
guide_top_text: "Atteignez vos utilisateurs via le bon canal au bon moment. Choisissez parmi les canaux intégrés au produit comme les messages in-app, les Content Cards et les bannières, ou les canaux externes comme les notifications push, les e-mails, les SMS et WhatsApp."

page_type: landing
description: "Atteignez vos utilisateurs via les canaux de communication intégrés au produit et externes dans Braze."

guide_featured_title: "Canaux intégrés au produit"
guide_featured_list:
  - name: Messages in-app
    link: /docs/user_guide/channels/in_app_messages
    image: /assets/img/braze_icons/phone-02.svg
  - name: Content Cards
    link: /docs/user_guide/channels/content_cards
    image: /assets/img/braze_icons/sticker-square.svg
  - name: Bannières
    link: /docs/user_guide/channels/banners
    image: /assets/img/braze_icons/layout-top.svg

guide_menu_title: "Canaux externes"
guide_menu_list:
  - name: E-mail
    link: /docs/user_guide/channels/email
    image: /assets/img/braze_icons/mail-01.svg
  - name: E-mail transactionnel
    link: /docs/user_guide/channels/transactional_email
    image: /assets/img/braze_icons/bank-note-02.svg
  - name: Pages d'accueil
    link: /docs/user_guide/messaging/landing_pages
    image: /assets/img/braze_icons/file-02.svg
  - name: LINE
    link: /docs/user_guide/channels/line
    image: /assets/img/braze_icons/message-chat-circle.svg
  - name: Notifications en direct
    link: /docs/developer_guide/live_notifications
    image: /assets/img/braze_icons/phone-02.svg
  - name: Push
    link: /docs/user_guide/channels/push
    image: /assets/img/braze_icons/marker-pin-05.svg
  - name: "SMS, MMS et RCS"
    link: /docs/user_guide/channels/sms_mms_and_rcs
    image: /assets/img/braze_icons/message-text-circle-01.svg
  - name: Webhooks
    link: /docs/user_guide/channels/webhooks
    image: /assets/img/braze_icons/brackets.svg
  - name: WhatsApp
    link: /docs/user_guide/channels/whatsapp
    image: /assets/img/braze_icons/whatsapp.svg
---

## Choisir un canal de communication {#choosing-a-message-channel}

Lorsque vous déterminez quel canal de communication est le plus adapté à vos Campaigns et Canvas, pensez toujours au contenu et à l'urgence de votre message :

- Le **contenu** correspond au degré d'attrait visuel de votre message. Vous pouvez ajouter des éléments multimédias et d'autres ressources à votre texte pour enrichir votre contenu.
- L'**urgence** mesure la rapidité avec laquelle un message peut notifier votre utilisateur et capter son attention. Les notifications que l'utilisateur peut consulter immédiatement ont une urgence élevée, tandis que les messages nécessitant une connexion à votre application ont une urgence faible.

La matrice de communication de Braze simplifie le choix du canal en croisant la **complexité du contenu** avec l'**urgence de réception**. En équilibrant ces deux facteurs, vous permettez à votre message de résonner plutôt que d'interrompre.

![Les notifications push mobile/web sont du contenu simple à urgence élevée ; les e-mails sont du contenu riche à urgence élevée ; les messages in-app/navigateur sont du contenu simple à urgence faible ; les Content Cards sont du contenu riche à urgence faible]({% image_buster /assets/img_archive/messaging_matrix.png %})

Bien que la matrice mette en avant les canaux principaux, elle reste adaptable : les SMS et WhatsApp, par exemple, sont des outils à urgence élevée qui peuvent évoluer vers du contenu riche grâce aux formats multimédias. Pour en savoir plus sur l'utilisation de cette matrice, consultez notre cours d'apprentissage Braze sur la [communication cross-canal](https://learning.braze.com/cross-channel-messaging).

## Ressources d'accessibilité {#accessibility-resources}

Vous pouvez utiliser Braze pour créer des campagnes de communication accessibles sur chaque canal. Collaborez avec vos équipes techniques pour vous assurer de respecter les normes d'accessibilité dans votre implémentation. Si vous souhaitez des conseils supplémentaires, nous vous recommandons :

- [Fondamentaux de la communication accessible](https://learning.braze.com/accessible-messaging-foundations) : apprenez les principes fondamentaux de l'accessibilité applicables aux communications de marque dans ce cours d'apprentissage Braze.
- [Créer des messages accessibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility) : découvrez comment ajouter du texte alternatif et structurer votre contenu pour les technologies d'assistance directement dans Braze.

Si vous avez des retours sur l'accessibilité de Braze ou des messages envoyés depuis Braze, nous serions ravis de vous entendre. Ouvrez le menu **Assistance** dans l'en-tête global et sélectionnez **Partager un commentaire** pour nous faire part de vos remarques.