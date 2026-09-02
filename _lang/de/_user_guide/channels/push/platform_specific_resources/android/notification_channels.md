---
nav_title: "Benachrichtigungskanäle"
article_title: Push-Benachrichtigungskanäle
page_order: 4
page_type: reference
description: "Dieser Referenzartikel behandelt Themen zu Android-Push-Benachrichtigungskanälen wie den Übergang zu Android O, das Hinzufügen eines Kanals zu Braze, das Einrichten eines Fallback-Kanals und mehr."
platform: Android
channel:
  - push
---

# Benachrichtigungskanäle {#notification-channels}

> [Benachrichtigungskanäle](https://www.braze.com/blog/android-o-push-notifications-channels/) sind eine Möglichkeit, Push-Benachrichtigungen zu organisieren, die mit Android O eingeführt wurden. Ab Android O müssen alle Push-Benachrichtigungen einen Benachrichtigungskanal haben, der den Nachrichtentyp angibt (zum Beispiel „Chat-Benachrichtigungen“ oder „Folge-Benachrichtigungen“). Ihre Nutzer:innen können dann Aspekte ihrer Benachrichtigungen steuern (zum Beispiel Schlummern, Ton-/Vibrationseinstellungen oder Abmeldung usw.) basierend auf einzelnen Kanälen.

Benachrichtigungskanäle können nur im Code Ihrer Anwendung erstellt werden und nicht programmatisch im Braze-Dashboard. Wir empfehlen, dass Ihr Entwicklerteam mit Ihren Marketern zusammenarbeitet, um sicherzustellen, dass die gewünschten Benachrichtigungskanäle ordnungsgemäß zum Dashboard hinzugefügt werden.

Ab API-Level 26 (Android O) benötigen Push-Benachrichtigungen einen gültigen Kanal zur Anzeige. Wenn Ihre App auf Android O oder höher abzielt, müssen Sie Braze SDK Version 2.1.0 oder höher verwenden. Ihr Entwicklerteam sollte die Kanäle definieren, die Sie verwenden möchten, sowie empfohlene Benachrichtigungseinstellungen (zum Beispiel Wichtigkeit, Ton, Lichter) für jeden Kanal in Ihrem Anwendungscode. Weitere Informationen finden Sie in der [Android-Entwicklerdokumentation](https://developer.android.com/preview/features/notification-channels.html) und der [Braze-Entwicklerdokumentation]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android).

{% alert note %}
Android unterstützt die Lokalisierung von Kanalnamen, sodass Sie im Code Ihrer Anwendung eine Kanal-ID mit mehreren Übersetzungen eines Kanalnamens verknüpfen können.
{% endalert %}

Sobald diese Kanäle erstellt sind, müssen Ihre Entwickler:innen die zugehörigen Kanal-IDs an Ihr Marketing-Team weitergeben. Ihr Team sollte Ihre Kanalnamen und Kanal-IDs im Braze-Dashboard eingeben, um sie in Ihren Campaigns und Canvases zu verwenden.

Um einen Kanal zum Braze-Dashboard hinzuzufügen, navigieren Sie zum Android-Push-Editor, wählen Sie das Feld für Benachrichtigungskanäle aus und wählen Sie dann **Kanäle verwalten**.
{% alert important %}
Nur Nutzer:innen mit Berechtigungen, die „Apps verwalten“ umfassen, können Kanäle verwalten.
{% endalert %}

## SDK-Standardkanal {#sdk-default-channel}

Android erfordert einen gültigen Kanal, um Push-Benachrichtigungen ab API-Level 26 (Android O) oder höher anzuzeigen. Das Braze Android SDK 2.1.0 enthält einen Standardkanal namens „General“, der erstellt und verwendet wird, wenn Sie keine zusätzlichen Kanäle im Dashboard angeben oder versuchen, an einen ungültigen Kanal zu senden. Sie können diese Bezeichnung im SDK umbenennen und eine Beschreibung des Kanals angeben. Wir empfehlen, dies in Betracht zu ziehen, um eine bessere Nutzererfahrung zu bieten.

Sobald ein Kanal zu Ihrer App hinzugefügt wurde, können Sie ihn entfernen. Allerdings können Verbraucher:innen immer die Anzahl der Kanäle sehen, die Sie [entfernt][3] haben. Das Braze-Dashboard bietet keine Unterstützung für die programmatische Erstellung von Kanälen – Kanäle müssen im Code Ihrer App erstellt und definiert werden, um ein nahtloses Erlebnis zu gewährleisten.

Auch hier empfehlen wir, sich mit Ihrem Entwicklerteam abzustimmen, um einen reibungslosen Übergang zum Targeting von Android O sicherzustellen.

## Dashboard-Fallback-Kanal {#dashboard-fallback-channel}

Braze ermöglicht es Ihnen, einen Dashboard-Fallback-Kanal festzulegen. Der Zweck des Dashboard-Fallback-Kanals besteht darin, eine Kanal-ID für ältere Push-Nachrichten bereitzustellen, die keine explizite Kanalauswahl haben. Unter Kanalauswahl verstehen wir die Auswahl eines Kanals in unserem Android-Push-Composer.

Nachrichten, für die kein Kanal ausgewählt wurde, werden mit der Kanal-ID des Dashboard-Fallback-Kanals gesendet. Wenn Sie Ihren Dashboard-Fallback-Kanal ändern, werden alle Nachrichten, für die nicht explizit ein Kanal ausgewählt wurde, mit der ID des neuen Fallback-Kanals gesendet.

Hier ist ein Beispiel für das erwartete Verhalten des Dashboard-Fallback-Kanals:

Ihr Dashboard-Fallback-Kanal heißt „Marketing“ und Sie haben 10 Android-Push-Nachrichten, für die Sie nie einen Kanal ausgewählt haben. Diese Campaigns werden über den Kanal „Marketing“ gesendet, da der Kanal „Marketing“ der Dashboard-Fallback-Kanal ist.

Außerdem haben Sie 15 Nachrichten, die Sie für den Versand über den Kanal „Social Notifications“ ausgewählt haben, und fünf Nachrichten, die Sie für den Versand über den Kanal „Marketing“ ausgewählt haben.

Sie entscheiden sich dann, Ihren Dashboard-Standardkanal von „Marketing“ auf „Updates“ zu ändern.

In dieser Situation werden alle 10 Campaigns ohne Kanalauswahl, die zuvor über den Kanal „Marketing“ gesendet wurden, nun über den Kanal „Updates“ gesendet, da diese Nachrichten über den Fallback-Kanal gesendet werden. Die 15 Nachrichten, die über den Kanal „Social Notifications“ gesendet wurden, werden weiterhin über den Kanal „Social Notifications“ gesendet. Die fünf Nachrichten, die über den Kanal „Marketing“ gesendet wurden, werden weiterhin über den Kanal „Marketing“ gesendet.

Falls Braze eine ungültige Kanal-ID übermittelt wird (z. B. wenn Sie eine Kanal-ID angeben, die Ihre Entwickler:innen nicht im SDK erstellt haben), wird die Benachrichtigung über Ihren SDK-Standardkanal zugestellt. Daher empfehlen wir Ihnen dringend, Ihre Benachrichtigungskanäle während der Entwicklung im Braze-Dashboard zu testen.

Um das erwartete Verhalten für Kanäle besser zu verstehen, lesen Sie die folgende Tabelle:

| Szenario | Ergebnis |
| --- | --- |
| **Firma ABC** aktualisiert auf ein SDK, das Android O unterstützt<br>**Firma ABC** fügt dem Braze-Dashboard keine Kanäle hinzu<br>**Firma ABC** benennt ihren SDK-Standardkanal nicht um | Push-Benachrichtigungen, die an Android-O-Geräte gesendet werden, erstellen einen Kanal namens „General“ und Benachrichtigungen werden über den Kanal „General“ gesendet |
| **Firma XYZ** aktualisiert auf ein SDK, das Android O unterstützt<br>**Firma XYZ** fügt dem Braze-Dashboard keine Kanäle hinzu<br>**Firma XYZ** benennt ihren SDK-Standardkanal in „Marketing“ um | Push-Benachrichtigungen, die an Android-O-Geräte gesendet werden, erstellen einen Kanal namens „Marketing“ und Benachrichtigungen werden über den Kanal „Marketing“ gesendet |
| **Firma LMN** aktualisiert auf ein SDK, das Android O unterstützt<br>**Firma LMN** definiert zwei Kanäle in ihrem Anwendungscode: „Promotions“ und „Order Updates“<br>**Firma LMN** fügt die Kanal-IDs für „Promotions“ und „Order Updates“ dem Braze-Dashboard hinzu<br>**Firma LMN** legt „Promotions“ als Dashboard-Fallback-Kanal fest<br>**Firma LMN** benennt ihren SDK-Standardkanal in „Marketing“ um | Push-Benachrichtigungen, die an Android-O-Geräte gesendet werden, erstellen keinen Kanal<br><br>Sofern der Marketer nicht explizit angibt, dass Benachrichtigungen über den Kanal „Order Updates“ oder „Marketing“ gesendet werden sollen, werden alle Benachrichtigungen, die vor dem Hinzufügen der Kanäle zum Dashboard erstellt wurden, über den Kanal „Promotions“ gesendet<br><br>Der SDK-Standardkanal „Marketing“ wird nur erstellt und verwendet, wenn die Firma versucht, eine Benachrichtigung über eine ungültige Kanal-ID zu senden oder wenn er explizit ausgewählt wird |
| **Firma HIJ** aktualisiert auf Android O, aber nicht auf Braze Android SDK 2.1.0 oder höher | Benachrichtigungen, die an Nutzer:innen gesendet werden, die Android O oder höher verwenden, werden nicht angezeigt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dashboard-Fallback-Kanal" }

## Kanäle zum Braze-Dashboard hinzufügen {#adding-channels-to-the-braze-dashboard}

1. Öffnen oder erstellen Sie eine beliebige Campaign oder ein Canvas, das einen Android-Push enthält.
2. Navigieren Sie zum Android-Push-Nachrichten-Editor.
3. Wählen Sie **Manage Notification Channels** aus. Alle hier hinzugefügten Kanäle stehen global für alle Campaigns und Canvases zur Verfügung. Sie benötigen die [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) „Manage Apps“ für Ihren Workspace, um Kanäle verwalten zu können.

Wenn Sie einen Benachrichtigungskanal auf eine bestimmte Campaign oder einen bestimmten Canvas-Schritt anwenden, scheint sich die Anzahl der **erreichbaren Nutzer:innen** (im Schritt „Zielgruppe“) für Android-Push nicht zu ändern. Allerdings sehen nur Nutzer:innen, die den ausgewählten Benachrichtigungskanal abonniert haben, die Nachricht, und Ihre Campaign-Analytics (wie Klicks) werden auf Basis dieser Zielgruppe gemessen.

![Android-Push-Editor mit „Manage Notification Channels“ und einer Liste konfigurierter Kanäle.]({% image_buster /assets/img_archive/push_notification_channels.png %})

{:start="4"}
4. Wählen Sie **Add Notification Channel** aus.
5. Geben Sie den Namen und die ID des Benachrichtigungskanals ein, den Sie hinzufügen möchten.<br><br>![Dialog „Add Notification Channel“ mit Feldern für Kanalname und Kanal-ID.]({% image_buster /assets/img_archive/push_notifications_channels_manage.png %})<br><br>
6. Wiederholen Sie die Schritte 4 und 5 für jeden Benachrichtigungskanal, den Sie hinzufügen möchten.
7. Wählen Sie **Save** aus, um Ihre Änderungen zu speichern.

## Festlegen Ihres Fallback-Kanals {#specifying-your-fallback-channel}

Ihr Fallback-Kanal ist der Kanal, über den Braze versucht, Ihre Android-Nachricht zu senden, wenn Sie keinen Kanal für die Nachricht ausgewählt haben. Die einzigen Campaigns und Canvases, die Android-Nachrichten ohne Kanalauswahl enthalten, sind Campaigns und Canvases, die erstellt wurden, bevor Ihr Team Kanäle zum Braze-Dashboard hinzugefügt hat. Wenn Sie Ihren Fallback-Kanal ändern, wird die Änderung global auf alle Campaigns und Canvases ohne explizite Kanalauswahl angewendet.

1. Öffnen Sie eine bestehende Campaign oder ein bestehendes Canvas.
2. Navigieren Sie zum Android-Push-Editor.
3. Wählen Sie **Manage Notification Channels** aus, nachdem Sie die Benachrichtigungskanal-Optionen erweitert haben.
4. Fügen Sie den Kanal zum Dashboard hinzu (falls er noch nicht hinzugefügt wurde).
5. Wählen Sie das Optionsfeld neben dem Kanal aus, den Sie als Fallback-Kanal festlegen möchten.
6. Speichern Sie Ihre Änderungen. Ihre Änderungen werden global angewendet.

## Kanäle zu Ihren Android-Push-Nachrichten hinzufügen {#adding-channels-to-your-android-push-messages}

1. Navigieren Sie zum Android-Push-Editor in einer beliebigen Campaign oder einem Canvas.
2. Wählen Sie den gewünschten Kanal aus dem Dropdown-Menü aus. Wenn Sie kein Dropdown-Menü sehen, sondern die folgende Ansicht, müssen Sie zuerst Kanäle hinzufügen, bevor Sie sie für Campaigns auswählen können.

![Editor für Push-Benachrichtigungskanäle.]({% image_buster /assets/img_archive/push_notifications_channels_composer.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels