---
nav_title: Kanäle
article_title: Kanäle
page_order: 5
layout: dev_guide
guide_top_header: "Kanäle"
guide_top_text: "Erreichen Sie Ihre Nutzer:innen über den richtigen Kanal zum richtigen Zeitpunkt. Wählen Sie zwischen In-Produkt-Kanälen wie In-App-Nachrichten, Content Cards und Bannern oder externen Kanälen wie Push, E-Mail, SMS und WhatsApp."

page_type: landing
description: "Erreichen Sie Ihre Nutzer:innen über In-Produkt- und externe Messaging-Kanäle in Braze."

guide_featured_title: "In-Produkt-Kanäle"
guide_featured_list:
  - name: In-App-Nachrichten
    link: /docs/user_guide/channels/in_app_messages
    image: /assets/img/braze_icons/phone-02.svg
  - name: Content Cards
    link: /docs/user_guide/channels/content_cards
    image: /assets/img/braze_icons/sticker-square.svg
  - name: Banner
    link: /docs/user_guide/channels/banners
    image: /assets/img/braze_icons/layout-top.svg

guide_menu_title: "Externe Kanäle"
guide_menu_list:
  - name: E-Mail
    link: /docs/user_guide/channels/email
    image: /assets/img/braze_icons/mail-01.svg
  - name: Transaktions-E-Mails
    link: /docs/user_guide/channels/transactional_email
    image: /assets/img/braze_icons/bank-note-02.svg
  - name: Landing-Pages
    link: /docs/user_guide/messaging/landing_pages
    image: /assets/img/braze_icons/file-02.svg
  - name: LINE
    link: /docs/user_guide/channels/line
    image: /assets/img/braze_icons/message-chat-circle.svg
  - name: Live-Benachrichtigungen
    link: /docs/developer_guide/live_notifications
    image: /assets/img/braze_icons/phone-02.svg
  - name: Push
    link: /docs/user_guide/channels/push
    image: /assets/img/braze_icons/marker-pin-05.svg
  - name: "SMS, MMS und RCS"
    link: /docs/user_guide/channels/sms_mms_and_rcs
    image: /assets/img/braze_icons/message-text-circle-01.svg
  - name: Webhooks
    link: /docs/user_guide/channels/webhooks
    image: /assets/img/braze_icons/brackets.svg
  - name: WhatsApp
    link: /docs/user_guide/channels/whatsapp
    image: /assets/img/braze_icons/whatsapp.svg
---

## Den richtigen Messaging-Kanal wählen {#choosing-a-message-channel}

Wenn Sie entscheiden, welcher Messaging-Kanal für Ihre Campaigns und Canvases am besten geeignet ist, sollten Sie immer den Inhalt und die Dringlichkeit Ihrer Nachricht berücksichtigen:

- **Inhalt** beschreibt, wie visuell ansprechend Ihre Nachricht ist. Sie können Multimedia und andere Assets zu Ihrem Text hinzufügen, um Ihren Inhalt reichhaltiger zu gestalten.
- **Dringlichkeit** gibt an, wie schnell eine Nachricht Ihre Nutzer:innen erreichen und deren Aufmerksamkeit gewinnen kann. Benachrichtigungen, die sofort sichtbar sind, haben eine hohe Dringlichkeit, während Nachrichten, bei denen sich Nutzer:innen erst in Ihre App einloggen müssen, eine niedrige Dringlichkeit haben.

Die Braze Messaging-Matrix vereinfacht die Kanalauswahl, indem sie **Inhaltskomplexität** gegen **Zustellungsdringlichkeit** abbildet. Durch die Abwägung dieser beiden Faktoren können Sie dafür sorgen, dass Ihre Nachricht Resonanz erzeugt, anstatt zu stören.

![Mobile-/Web-Push sind einfacher Inhalt mit hoher Dringlichkeit; E-Mails sind reichhaltiger Inhalt mit hoher Dringlichkeit; In-App-/Browser-Nachrichten sind einfacher Inhalt mit niedriger Dringlichkeit; Content Cards sind niedrige Dringlichkeit mit reichhaltigem Inhalt]({% image_buster /assets/img_archive/messaging_matrix.png %})

Die Matrix hebt zwar die wichtigsten Kanäle hervor, ist aber anpassbar: SMS und WhatsApp beispielsweise sind Kanäle mit hoher Dringlichkeit, die durch Multimedia-Formate auch reichhaltigen Inhalt ermöglichen. Um mehr darüber zu erfahren, wie Sie diese Matrix nutzen können, schauen Sie sich unseren Braze-Lernkurs zu [kanalübergreifendem Messaging](https://learning.braze.com/cross-channel-messaging) an.

## Barrierefreiheits-Ressourcen {#accessibility-resources}

Sie können Braze nutzen, um barrierefreie Messaging-Kampagnen über jeden Kanal zu erstellen. Arbeiten Sie mit Ihrem Entwicklungsteam zusammen, um sicherzustellen, dass Sie die Barrierefreiheitsstandards in Ihrer Implementierung einhalten. Wenn Sie zusätzliche Orientierung wünschen, empfehlen wir:

- [Grundlagen barrierefreier Nachrichten](https://learning.braze.com/accessible-messaging-foundations): Lernen Sie in diesem Braze-Lernkurs grundlegende Barrierefreiheitsprinzipien kennen, die für Markenkommunikation gelten.
- [Barrierefreie Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility): Erfahren Sie, wie Sie Alt-Text hinzufügen und Ihre Inhalte für assistive Technologien direkt in Braze strukturieren.

Wenn Sie Feedback zur Barrierefreiheit von Braze oder über Braze versendeten Nachrichten haben, freuen wir uns, von Ihnen zu hören. Öffnen Sie das **Support**-Menü in der globalen Kopfzeile und wählen Sie **Feedback teilen**, um uns Ihre Gedanken mitzuteilen.