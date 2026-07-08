---
nav_title: Abo-Gruppen
article_title: Endpunkte für Abo-Gruppen
page_order: 7
layout: dev_guide

#Required
description: "Auf dieser Landing-Page werden die Braze-Endpunkte für Abo-Gruppen für E-Mail und SMS erklärt und aufgelistet."
page_type: landing
search_tag: Endpoint

guide_top_header: "Endpunkte für Abo-Gruppen"
guide_top_text: "Verwenden Sie die REST APIs für Abo-Gruppen, um die Abo-Gruppen, die Sie im Braze-Dashboard auf der Seite **Abo-Gruppe** gespeichert haben, programmatisch zu verwalten. Dies gilt sowohl für SMS- als auch für E-Mail-Abo-Gruppen.<br><br> Sie suchen eine Anleitung zur Erstellung von Abo-Gruppen? Sehen Sie sich unsere Artikel für <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group'>SMS-Abo-Gruppen</a> und <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions'>E-Mail-Abo-Gruppen</a> an."

guide_featured_title: ""
guide_featured_list:
  - name: "GET: Abo-Gruppenstatus von Nutzer:innen auflisten"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Abo-Gruppen von Nutzer:innen auflisten"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_groups
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Abo-Gruppenstatus von Nutzer:innen aktualisieren"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status
    image: /assets/img/braze_icons/user-plus-01.svg
  - name: "POST: Abo-Gruppenstatus von Nutzer:innen aktualisieren V2"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2
    image: /assets/img/braze_icons/user-edit.svg
---
<br>
<br>


## Zeitreihen von Abo-Gruppen verstehen {#understand-subscription-group-timeseries}

Auf der Seite **Abo-Gruppe** zeigen Zeitreihen-Charts Folgendes an:

- **Größe der Abo-Gruppe:** Nutzer:innen, die an einem bestimmten Datum bei dieser Gruppe abonniert sind
- **Abgemeldete Größe der Abo-Gruppe:** Nutzer:innen, die sich an einem bestimmten Datum von dieser Gruppe abgemeldet haben

Informationen zur Dashboard-Nutzung finden Sie unter [Größen von Abo-Gruppen anzeigen]({{site.baseurl}}/user_guide/channels/email/subscriptions#viewing-subscription-group-sizes).

Diese Metriken sind gruppenspezifisch. Sie können sich vom Segment-Filter `Email Subscription Status is Unsubscribed` unterscheiden, der den globalen E-Mail-Abo-Status widerspiegelt und nicht den einer einzelnen Abo-Gruppe. Bei sehr großen Workspaces zeigt Braze möglicherweise geschätzte Werte an, wenn exakte Zahlen nicht verfügbar sind.

## Doppelte Nutzer:innen aus E-Mail-Erfassungsformularen vermeiden {#avoid-duplicate-users-from-email-capture-forms}

Bevor Sie eine Nutzer:in aus einem E-Mail-Erfassungsformular erstellen, rufen Sie [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) auf, um zu prüfen, ob das Profil bereits existiert. Wenn die Antwort „User not found“ lautet, erstellen Sie die Nutzer:in mit [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Andernfalls aktualisieren Sie das bestehende Profil, anstatt ein Duplikat zu erstellen.

## Snowflake-`USERS_MESSAGES_EMAIL_UNSUBSCRIBE`-Ereignisse {#snowflake-users_messages_email_unsubscribe-events}

Die Snowflake-Tabelle `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` protokolliert E-Mail-Abmeldungen auf Nachrichtenebene, die von der Empfängerseite ausgehen – das Klicken auf einen Abmeldelink, die Ein-Klick-List-Unsubscribe-Funktion des E-Mail-Clients, Einreichungen über das Präferenzzentrum und vom ESP gemeldete Abmeldungen. Abmeldungen über die REST API sind in dieser Tabelle nicht enthalten; diese erzeugen stattdessen [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events)- oder [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events)-Ereignisse.

## SMS-Testnachrichten und Abo-Gruppen {#sms-test-messages-and-subscription-groups}

Um eine SMS-Testnachricht zu erhalten, muss die Empfänger:in der SMS-Abo-Gruppe angehören, die Sie beim Senden des Tests auswählen.