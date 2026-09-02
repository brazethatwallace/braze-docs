---
nav_title: "Einrichtung"
article_title: Push-Einrichtung
page_order: 0
layout: dev_guide
guide_top_header: "Push-Einrichtung"
guide_top_text: "Erfahren Sie mehr über den Push-Token-Lebenszyklus und Abo-Status, damit Ihre Push-Benachrichtigungen die richtigen Nutzer:innen erreichen."

page_type: landing
description: "Erfahren Sie mehr über den Push-Token-Lebenszyklus und Abo-Status für Push-Benachrichtigungen in Braze."

guide_featured_title: "Artikel in diesem Abschnitt"
guide_featured_list:
  - name: Lebenszyklus von Push-Token
    link: /docs/user_guide/channels/push/push_setup/push_token_lifecycle
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: Push-Abo-Status
    link: /docs/user_guide/channels/push/push_setup/push_subscription_states
    image: /assets/img/braze_icons/users-01.svg
---

## Voraussetzungen {#prerequisites}

Bevor Sie Push-Nachrichten mit Braze erstellen und senden können, müssen Sie mit Ihren Entwickler:innen zusammenarbeiten, um Push in Ihre Website oder App zu integrieren. Detaillierte Schritte finden Sie in unseren Integrationsleitfäden für jede Plattform:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android)
- [Internet]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)

## Push-Priming {#push-priming}

Beachten Sie, dass Nutzer:innen Push aktivieren müssen, um Ihre Nachrichten zu empfangen. Daher ist es sinnvoll, In-App-Nachrichten zu verwenden, um Ihren Kund:innen zu erklären, warum Sie ihnen Push-Benachrichtigungen senden möchten und wie die Aktivierung von Push ihnen nützt. Dieser Prozess wird als [Push-Priming]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) bezeichnet.