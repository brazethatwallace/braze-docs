---
nav_title: Push-Benachrichtigungen
article_title: Push-Benachrichtigungen für Windows Universal
platform: Windows Universal
page_order: 1
description: "Dieser Artikel enthält Anweisungen zur Integration von Push-Benachrichtigungen für die Windows Universal-Plattform."
channel: push
hidden: true
---

# Integration von Push-Benachrichtigungen {#push-notification-integration}
{% multi_lang_include archive/windows_deprecation.md %}

![Ein Beispiel für einen Windows Universal Push.]({% image_buster /assets/img_archive/windows_uni_push_sample.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Eine Push-Benachrichtigung ist eine Benachrichtigung außerhalb der App, die auf dem Bildschirm der Nutzer:innen erscheint, wenn ein wichtiges Update erfolgt. Push-Benachrichtigungen sind eine wertvolle Möglichkeit, Ihre Nutzer:innen mit zeitkritischen und relevanten Inhalten zu versorgen oder sie erneut für Ihre App zu begeistern.

In unserer [Dokumentation]({{site.baseurl}}/user_guide/channels/push/best_practices/) finden Sie weitere Best Practices.

## 1. Schritt: Konfigurieren Sie Ihre Anwendung für Push {#step-1-configure-your-application-for-push}

Stellen Sie sicher, dass in Ihrer Datei `Package.appxmanifest` die folgenden Einstellungen konfiguriert sind:

Vergewissern Sie sich auf dem Tab **Application**, dass `Toast Capable` auf `YES` eingestellt ist.

## 2. Schritt: Konfigurieren Sie das Braze-Dashboard {#step-2-configure-the-braze-dashboard}

1. [Finden Sie Ihre SID und Ihr Client Secret](http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx)
2. Fügen Sie auf der Seite **Settings** des Braze-Dashboards die SID und das Client Secret zu Ihren Einstellungen hinzu.<br>![]({% image_buster /assets/img_archive/windows_sid.png %} "Windows SID dashboard")

## 3. Schritt: Update für die Protokollierung von Öffnungen im Hintergrund {#step-3-update-for-background-open-logging}

Fügen Sie in Ihrer Methode `OnLaunched` nach dem Aufruf von `OpenSession` das folgende Code-Snippet ein.

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);
}
```

## 4. Schritt: Event Handler erstellen {#step-4-creating-event-handlers}

Um auf Ereignisse zu hören, die ausgelöst werden, wenn der Push empfangen und aktiviert (von Nutzer:innen angeklickt) wird, erstellen Sie Event Handler und fügen Sie diese zu den `PushManager`-Ereignissen hinzu:

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

Ihre Event Handler sollten die folgenden Signaturen haben:

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## 5. Schritt: Deeplinking von Push in Ihre App {#step-5-deep-linking-from-push-into-your-app}

### Teil 1: Deeplinks für Ihre App erstellen {#part-1-creating-deep-links-for-your-app}

Deeplinks werden verwendet, um Nutzer:innen von außerhalb Ihrer Anwendung direkt zu einem bestimmten Bildschirm oder einer bestimmten Seite in Ihrer Anwendung zu leiten. In der Regel geschieht dies durch die Registrierung eines URL-Schemas (z. B. myapp://mypage) bei einem Betriebssystem und die Registrierung Ihrer Anwendung zur Handhabung dieses Schemas. Wenn das Betriebssystem aufgefordert wird, eine URL dieses Formats zu öffnen, überträgt es die Kontrolle an Ihre Anwendung.

Die Unterstützung von WNS-Deeplinks unterscheidet sich hiervon, da sie Ihre Anwendung mit Daten darüber startet, wohin die Nutzer:innen geschickt werden sollen. Wenn ein WNS-Push erstellt wird, kann er einen Launch String enthalten, der an die `OnLaunched`-Methode Ihrer Anwendung weitergegeben wird, wenn der Push angeklickt und Ihre Anwendung geöffnet wird. Wir verwenden diesen Launch String bereits für das Tracking von Kampagnen und geben Nutzer:innen die Möglichkeit, ihre eigenen Daten anzuhängen, die geparst und zur Navigation beim Start der App verwendet werden können.

Wenn Sie im Dashboard oder in der REST API einen zusätzlichen Launch String angeben, wird dieser am Ende des von uns erstellten Launch Strings nach dem Schlüssel „abextras=“ eingefügt. Ein Beispiel für einen Launch String könnte so aussehen: `ab_cn_id=_trackingid_abextras=page=settings`, wobei Sie `page=settings` im zusätzlichen Parameter für den Launch String angegeben haben, damit Sie ihn analysieren und die Nutzer:innen zur Einstellungsseite navigieren können.

### Teil 2: Deeplinking über das Dashboard {#part-2-deep-linking-through-the-dashboard}

Geben Sie in den Einstellungen für Push-Benachrichtigungen im Feld „Additional Launch String Configuration“ den String an, der an den Launch String angehängt werden soll.

![]({% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Deep Link Click Action")

### Teil 3: Deeplinking über die REST API {#part-3-deep-linking-through-the-rest-api}

Braze erlaubt es auch, Deeplinks über die REST API zu senden. [Windows Universal Push-Objekte]({{site.baseurl}}/api/objects_filters/) akzeptieren einen optionalen `extra_launch_string`-Parameter.