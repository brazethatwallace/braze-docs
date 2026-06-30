---
nav_title: "Benachrichtigungsoptionen"
article_title: Android-Benachrichtigungsoptionen
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt verschiedene Android-spezifische Benachrichtigungsoptionen und wie Sie diese in Braze Campaigns optimal einsetzen können."

platform: Android
channel:
  - Push

---

# Benachrichtigungsoptionen {#notification-options}

> Dies sind einige der Android-spezifischen Push-Benachrichtigungsoptionen, die über Braze verfügbar sind.

## Stille Benachrichtigungen {#silent-notifications}

Wenn Sie [Ihre Push-Benachrichtigung verfassen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message?tab=android#step-4-compose-your-push-message), können Sie eine Android-Push-Nachricht **nicht** ohne Titel senden&#8212;Sie können jedoch stattdessen ein einzelnes Leerzeichen eingeben. Beachten Sie, dass eine Nachricht, die nur ein einzelnes Leerzeichen enthält, als stille Push-Benachrichtigung gesendet wird. Weitere Informationen finden Sie unter [Stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android).

## Benachrichtigungsgruppen {#notification-groups}

Wenn Sie Ihre Nachrichten kategorisieren und in der Benachrichtigungsleiste Ihrer Nutzer:innen gruppieren möchten, können Sie die Android-Benachrichtigungskanal-Funktion über Braze nutzen.

Erstellen Sie zunächst Ihre Android-Push-Campaign und suchen Sie dann oben im Tab **Compose** nach dem Dropdown-Menü **Notification Channel**.

![Erstellen Sie zunächst Ihre Android-Push-Campaign und suchen Sie dann oben im Tab „Compose“ nach dem Dropdown-Menü „Notification Channel“.]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

Wählen Sie Ihren Benachrichtigungskanal aus dem Dropdown-Menü aus. Sie müssen außerdem einen Fallback-Kanal auswählen, falls Ihre Benachrichtigungskanal-Einstellungen nicht ordnungsgemäß funktionieren.

Wenn hier keine [Benachrichtigungskanäle]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels) aufgelistet sind, können Sie einen über die Benachrichtigungskanal-ID hinzufügen. Kontaktieren Sie Ihre Entwickler:innen, um Ihre Benachrichtigungskanal-IDs zu ermitteln oder bei Bedarf neue IDs zu erstellen.

Um eine Benachrichtigungs-ID zu Ihrem Benachrichtigungskanal hinzuzufügen, klicken Sie im Dropdown-Menü **Notification Channel** auf **Manage Notification Channel** und füllen Sie die erforderlichen Felder aus. Benachrichtigungskanäle müssen in der App definiert werden, bevor sie in der Braze-Plattform verwendet werden können.

![Um eine Benachrichtigungs-ID zu Ihrem Benachrichtigungskanal hinzuzufügen, klicken Sie im Dropdown-Menü „Notification Channel“ auf „Manage Notification Channel“ und füllen Sie die erforderlichen Felder aus. Benachrichtigungskanäle müssen in der App definiert werden, bevor sie in der Braze-Plattform verwendet werden können.]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }