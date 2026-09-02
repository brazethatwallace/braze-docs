---
nav_title: "Push-Abo-Status"
article_title: "Push-Abo-Status"
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt die Konzepte der Push-Aktivierung und der Push-Abo-Status in Braze, einschließlich der grundlegenden Verhaltensunterschiede zwischen iOS, Android und Web."
channel:
  - push

---

# Push-Aktivierung und Push-Abo {#push-enablement-and-push-subscription}

> Dieser Referenzartikel behandelt die Konzepte der Push-Aktivierung und der Push-Abo-Status in Braze, einschließlich der grundlegenden Verhaltensunterschiede zwischen iOS, Android und Web.

{% multi_lang_include push/subscription_states.md %}

## Wo Push-Registrierung und -Status angezeigt werden {#where-push-registration-and-status-appear}

Sie können den Push-Abo-Status, die Registrierung und die Aktivierung an drei Hauptstellen in Braze überprüfen:

1. **[Nutzerprofile](#user-profiles-and-push-changelog)** im Tab **Engagement**
2. **[Segmentierung](#segmentation-and-push-filters)** im Segment-Builder
3. **[Campaign- und Canvas-Analytics](#campaign-and-canvas-analytics)** auf der Analytics-Seite jeder Nachricht

### Nutzerprofile und Push-Änderungsprotokoll {#user-profiles-and-push-changelog}

Im Profil von Nutzer:innen ([**Nutzer:innen suchen**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) > Nutzer:in auswählen > Tab **Engagement**) listet **Contact Settings** den Push-Abo-Status auf, **Push Registered For** (welche Apps und Plattformen Braze zum Senden von Vordergrund-Push an dieses Profil verwenden kann) und das **Push-Änderungsprotokoll** für Token-Verschiebungen, Fehler und Registrierungsupdates. Informationen zum Lesen von **Push Registered For** und zur Vordergrund- vs. Hintergrund-Autorisierung finden Sie unter [Push-Registrierungsstatus überprüfen]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#checking-push-registration-status).

Unter iOS und Android kann das Push-Änderungsprotokoll einen Eintrag wie „Push-Token was updated from foreground push enabled to foreground push disabled“ enthalten, wenn ein Gerät von der Vordergrund-Push-Autorisierung zur reinen Hintergrund-Autorisierung wechselt (z. B. nachdem Nutzer:innen Benachrichtigungen in den Systemeinstellungen deaktiviert haben und das SDK die Änderung meldet).

Nachdem Sie neue SDK-Daten erwarten (z. B. direkt nach einer Testsitzung), wählen Sie **Refresh** im Kundenprofil, wenn die Werte veraltet erscheinen. Es kann eine kurze Verzögerung zwischen dem Senden der SDK-Daten und der Aktualisierung des Profils mit der neuesten Push-Registrierung geben.

Für Nutzer:innen, die Sie einer [internen Gruppe]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups) hinzufügen, wählen Sie **Record User Events for group members** in den **Internal Group Settings** für diese Gruppe, damit SDK-Anfragen im Protokoll erscheinen. Öffnen Sie dann das [Event-Nutzerprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) unter **Einstellungen** > **Event User Log**, suchen Sie die SDK-Anfragen der Nutzer:innen und erweitern Sie den Roh-Payload. Sie können Felder wie `remote_notification_enabled` überprüfen, um zu validieren, ob das Gerät Remote-Benachrichtigungen als aktiviert oder deaktiviert meldet.

### Segmentierung und Push-Filter {#segmentation-and-push-filters}

Im Segment-Builder verwenden Sie Filter wie **`Foreground Push Enabled`**, **`Foreground Push Enabled for App`**, **`Background or Foreground Push Enabled`** und Push-Abo-Filter, um Nutzer:innen nach Präferenz und Autorisierung auf Geräteebene anzusprechen oder zu prüfen. Unter iOS hängt es davon ab, ob Nutzer:innen die Betriebssystem-Aufforderung abgeschlossen, Einstellungen geändert oder [provisorische Autorisierung](#provisional-push) verwenden, wie diese Filter für bestimmte Nutzer:innen gelesen werden; siehe [iOS-Nutzer:innenaktionen und Push-Status](#ios-user-actions-push-status) und [Weitere plattformspezifische Szenarien](#foreground-push-enabled).

### Campaign- und Canvas-Analytics {#campaign-and-canvas-analytics}

Auf der Analytics-Seite einer Push-**Campaign** oder eines **Canvas** spiegeln Metriken wie *Gesendet*, *Bounces* und *Öffnungen* die Zustellung und das Engagement für diesen Versand wider. Um diese Zahlen mit einzelnen Profilen abzugleichen, exportieren Sie Empfänger:innen aus **Campaign Details** oder **Canvas Details** über **User Data** (CSV). Schritte und Berechtigungen finden Sie unter [Campaign-Daten exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data) und [Canvas-Daten exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data). Wenn die Zahlen zwischen Analytics und einem Export nicht übereinstimmen, siehe [Campaign- und Canvas-Analytics]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting#campaign-and-canvas-analytics) in der Export-Fehlerbehebung.

## iOS-Nutzer:innenaktionen und Push-Status {#ios-user-actions-push-status}

Die folgende Tabelle zeigt, wie verschiedene Nutzer:innenaktionen die iOS-Push-Aktivierung, die Vordergrund- oder Hintergrund-Push-Registrierung und den Push-Abo-Status in Braze beeinflussen. Wenn Nutzer:innen Ihre App installieren und ihre erste Sitzung starten, ist ihr Status in der Regel wie in der ersten Zeile dargestellt. Jede nachfolgende Aktion kann einige dieser Werte aktualisieren, andere jedoch nicht.

| Nutzer:innenaktion | `Foreground Push Enabled` | `Foreground Push Enabled for App` | Push-Registrierungstyp | Push-Abo-Status |
| --- | --- | --- | --- | --- |
| Nutzer:in installiert die App und protokolliert eine Sitzung | `false`* | Nicht aktualisiert | Hintergrund | `Subscribed` |
| Nutzer:in erhält die native iOS-Push-Abfrage und wählt **Allow** | `true` | `true` | Vordergrund | `Opted-In`** |
| Nutzer:in erhält die native iOS-Push-Abfrage und wählt **Don't Allow** | `false` | Nicht aktualisiert | Hintergrund | Nicht aktualisiert |
| Nutzer:in aktiviert Push in den Geräteeinstellungen und protokolliert eine Sitzung | `true` | `true` | Vordergrund | `Opted-In`** |
| Nutzer:in deaktiviert Push in den Geräteeinstellungen und protokolliert eine Sitzung | `false` | `false` | Hintergrund | Nicht aktualisiert |
| Nutzer:in löscht die App | Nicht aktualisiert | Aktualisiert, wenn Push-Token zurückgezogen wird | Aktualisiert, wenn Push-Token zurückgezogen wird | Nicht aktualisiert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="iOS-Nutzer:innenaktionen und Push-Status" }

<sup>* Wenn die App kein provisorisches Push verwendet, ist `Foreground Push Enabled` `false`, bis Nutzer:innen Push-Benachrichtigungen erlauben. Wenn die App provisorisches Push verwendet, ist `Foreground Push Enabled` zu Beginn der ersten Sitzung `true`. Weitere Informationen finden Sie unter [Provisorische Autorisierung und stilles Push](#provisional-push).</sup>

<sup>** Ab [Braze Swift SDK Version 7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0) steuert die Konfigurationseigenschaft `optInWhenPushAuthorized`, ob der Push-Abo-Status automatisch auf `Opted-In` gesetzt wird, wenn die Push-Berechtigung autorisiert wird. Weitere Informationen finden Sie unter [Push-Token](#push-tokens).</sup>

## Push-Berechtigung {#push-permission}

Alle Push-fähigen Plattformen – iOS, Web und Android – erfordern ein explizites Opt-in über eine Systemaufforderung auf Betriebssystemebene, mit einigen geringfügigen Unterschieden, die im folgenden Abschnitt beschrieben werden.

Da die Entscheidung der Nutzer:innen endgültig ist und Sie nach einer Ablehnung nicht erneut fragen können, ist die Verwendung von [Push-Primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)-In-App-Nachrichten eine wichtige Strategie zur Steigerung Ihrer Opt-in-Raten.

**Native Push-Berechtigungsaufforderungen des Betriebssystems**

| Plattform | Screenshot | Beschreibung |
|--|--|--|
| iOS | ![Eine native iOS-Push-Aufforderung mit der Frage „My App would like to send you notifications“ und zwei Buttons „Don't Allow“ und „Allow“ am unteren Rand der Nachricht.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | Dies gilt nicht bei der Anforderung einer [provisorischen Push](#provisional-push)-Berechtigung. |
| Android | ![Eine Android-Push-Nachricht mit der Frage „Allow Kitchenerie to send you notifications?“ und zwei Buttons „Allow“ und „Don't allow“ am unteren Rand der Nachricht.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Diese Push-Berechtigung wurde in Android 13 eingeführt. Vor Android 13 war keine Berechtigung zum Senden von Push erforderlich. |
| Web | ![Eine native Push-Aufforderung des Webbrowsers mit der Frage „Braze.com wants to show notification“ und zwei Buttons „Block“ und „Allow“ am unteren Rand der Nachricht.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push-Berechtigung" }

### Android

Vor Android 13 war keine Berechtigung zum Senden von Push-Benachrichtigungen erforderlich. Unter Android 12 und niedriger werden alle Nutzer:innen bei ihrer ersten Sitzung als `Subscribed` betrachtet, wenn Braze automatisch ein Push-Token anfordert. Zu diesem Zeitpunkt sind die Nutzer:innen **Push-aktiviert** mit einem gültigen Push-Token für dieses Gerät und einem Standard-Abo-Status von `Subscribed`.

Ab [Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13) muss die Push-Berechtigung von den Nutzer:innen angefragt und erteilt werden. Ihre App kann die Berechtigung manuell zu geeigneten Zeitpunkten anfordern. Falls nicht, werden die Nutzer:innen automatisch aufgefordert, wenn Ihre App einen [Benachrichtigungskanal](https://developer.android.com/reference/android/app/NotificationChannel) erstellt.

### iOS

![Eine Benachrichtigung im System-Benachrichtigungscenter mit einer Nachricht am unteren Rand, die fragt: „Keep receiving notifications from the Yachtr app?“ mit zwei Buttons „Keep“ und „Turn Off“]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Ihre App kann provisorisches Push oder autorisiertes Push anfordern.

Autorisiertes Push erfordert eine explizite Genehmigung der Nutzer:innen, bevor Benachrichtigungen gesendet werden, während [provisorisches Push](https://www.braze.com/resources/articles/mastering-provisional-push) es Ihnen ermöglicht, Benachrichtigungen __still__ direkt an das Benachrichtigungscenter zu senden, ohne Ton oder Hinweis.

#### Provisorische Autorisierung und stilles Push {#provisional-push}

Vor iOS 12 (veröffentlicht 2018) mussten alle Nutzer:innen explizit dem Empfang von Push-Benachrichtigungen zustimmen.

In iOS 12 führte Apple die [provisorische Autorisierung](https://www.braze.com/resources/articles/mastering-provisional-push) ein, die es Marken ermöglicht, stille Push-Benachrichtigungen an das Benachrichtigungscenter ihrer Nutzer:innen zu senden, bevor diese explizit zustimmen, und Ihnen so die Möglichkeit gibt, den Wert Ihrer Nachrichten frühzeitig zu demonstrieren. Weitere Informationen finden Sie unter [Provisorische Autorisierung]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push).

### Web {#web}

Für Web müssen Sie ein explizites Opt-in der Nutzer:innen über den nativen Browser-Berechtigungsdialog anfordern.

Im Gegensatz zu iOS und Android, bei denen Ihre App die Berechtigungsaufforderung jederzeit anzeigen kann, zeigen einige moderne Browser die Aufforderung nur an, wenn sie durch eine „Nutzer:innengeste“ (Mausklick oder Tastendruck) ausgelöst wird. Wenn Ihre Website versucht, die Push-Benachrichtigungsberechtigung beim Laden der Seite anzufordern, wird dies wahrscheinlich vom Browser ignoriert oder unterdrückt.

Daher sollten Sie die Berechtigung nur anfordern, wenn Nutzer:innen irgendwo auf Ihrer Website klicken, und nicht zufällig beim Laden einer Seite.

## Push-Token {#push-tokens}

[Push-Token]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle) sind eindeutige anonyme Bezeichner, die vom Gerät der Nutzer:innen generiert und an Braze gesendet werden, um zu identifizieren, wohin die Benachrichtigung der jeweiligen Empfänger:innen gesendet werden soll.

Es gibt zwei Arten, wie ein [Push-Token]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle) klassifiziert werden kann, die für das Verständnis, wie eine Push-Benachrichtigung an Ihre Nutzer:innen gesendet werden kann, wesentlich sind.

1. **Vordergrund-Push** bietet die Möglichkeit, reguläre sichtbare Push-Benachrichtigungen an den Vordergrund des Geräts der Nutzer:innen zu senden.
2. **Hintergrund-Push** ist unabhängig davon verfügbar, ob ein bestimmtes Gerät dem Empfang von Push-Benachrichtigungen dieser Marke zugestimmt hat. Hintergrund-Push ermöglicht es Marken, stille Push-Benachrichtigungen – Benachrichtigungen, die absichtlich nicht angezeigt werden – an Geräte zu senden, um wichtige Funktionen wie [Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking) zu unterstützen.

Wenn ein Kundenprofil ein gültiges Vordergrund-Push-Token hat, das mit einer App verknüpft ist, betrachtet Braze die Nutzer:innen als „Push-registriert“ für die jeweilige App. Braze bietet dann einen spezifischen Segmentierungsfilter, `Foreground Push Enabled for App,`, um diese Nutzer:innen zu identifizieren.

{% alert note %}
Der Filter `Foreground Push Enabled for App` berücksichtigt nur das Vorhandensein eines gültigen Vordergrund- und Hintergrund-Push-Tokens für die jeweilige App. Der allgemeinere Filter [`Foreground Push Enabled`](#foreground-push-enabled) segmentiert jedoch Nutzer:innen, die Push-Benachrichtigungen für beliebige Apps in Ihrem Workspace explizit aktiviert haben. Diese Zählung umfasst nur Vordergrund-Push und schließt Nutzer:innen aus, die sich abgemeldet haben. Weitere Informationen zu diesen und anderen Filtern finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

Bei einem kleinen Prozentsatz von Nutzer:innen können Verarbeitungsverzögerungen zu einer kurzfristigen Diskrepanz führen: Nutzer:innen haben möglicherweise ein gültiges Vordergrund-Push-Token in ihrem Profil, stimmen aber dennoch nicht mit dem Filter `Foreground Push Enabled` überein. Ihr Profil kann kurzzeitig anzeigen, dass Vordergrund-Push nicht aktiviert ist, obwohl ein Token vorhanden ist. Dies klärt sich in der Regel, sobald die Verarbeitung aufgeholt hat.
{% endalert %}

### Mehrere Nutzer:innen auf einem Gerät {#multiple-users-on-one-device}

Push-Token sind sowohl geräte- als auch app-spezifisch, sodass es nicht möglich ist, Push-Token zur Unterscheidung mehrerer Nutzer:innen zu verwenden, die dasselbe Gerät nutzen.

Angenommen, Sie haben zwei Nutzer:innen: Charlie und Kim. Wenn Charlie Push-Benachrichtigungen für Ihre App auf seinem Telefon aktiviert hat und Kim Charlies Telefon verwendet, um sich aus Charlies Profil abzumelden und sich in ihr eigenes einzuloggen, wird das Push-Token Kims Profil zugewiesen. Das Push-Token bleibt dann auf diesem Gerät Kims Profil zugewiesen, bis sie sich abmeldet und Charlie sich wieder einloggt.

Eine App oder Website kann nur ein Push-Abo pro Gerät haben. Wenn sich also Nutzer:innen von einem Gerät oder einer Website abmelden und neue Nutzer:innen sich einloggen, wird das Push-Token den neuen Nutzer:innen zugewiesen. Dies wird im Kundenprofil im Abschnitt **Contact Settings** des Tabs **Engagement** angezeigt:

![Push-Token-Änderungsprotokoll im Tab „Engagement“ eines Nutzerprofils, das zeigt, wann das Push-Token zu anderen Nutzer:innen verschoben wurde und um welches Token es sich handelt.]({% image_buster /assets/img/push_token_changelog.png %})

Da es für Push-Anbieter (APNs/FCM) keine Möglichkeit gibt, zwischen mehreren Nutzer:innen auf einem Gerät zu unterscheiden, übergeben wir das Push-Token an die zuletzt eingeloggten Nutzer:innen, um zu bestimmen, welche Nutzer:innen auf dem Gerät für Push angesprochen werden sollen.

### Mehrere Geräte und ein:e Nutzer:in {#multiple-devices-and-one-user}

Der Push-Abo-Status ist nutzer:innenbasiert und nicht spezifisch für eine einzelne App. Der Status des Push-Abos ist der zuletzt gesetzte Wert. Wenn Nutzer:innen also Push-Benachrichtigungen zugestimmt haben, ist ihr Push-Abo-Status auf allen berechtigten Geräten `Opted-In`. Wenn Nutzer:innen sich später explizit über Ihre Anwendung oder andere von Ihrer Marke bereitgestellte Methoden von Push-Benachrichtigungen abmelden, wird ihr Push-Abo-Status auf `Unsubscribed` aktualisiert und keine Push-registrierten Geräte können Push-Benachrichtigungen empfangen.

## Filter „Foreground Push Enabled“ {#foreground-push-enabled}

`Foreground Push Enabled` ist ein Segmentierungsfilter in Braze, der es Marketern ermöglicht, einfach Nutzer:innen zu identifizieren, die Braze das Senden von Push-Benachrichtigungen erlauben, sowie Nutzer:innen, die keine Präferenz geäußert haben, keine Push-Benachrichtigungen zu erhalten.

Der Filter `Foreground Push Enabled` berücksichtigt Folgendes:
- Die Fähigkeit von Braze, eine Push-Benachrichtigung zu senden (Vordergrund-Push-Token)
- Die allgemeine Präferenz der Nutzer:innen, Push auf einem ihrer Geräte zu empfangen (Push-Abo-Status)

![Ein Screenshot des Dashboards, der zeigt, dass Nutzer:innen „Push Registered for Marketing (iOS)“ sind.]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Nutzer:innen gelten als „Push-aktiviert“ oder „Push-registriert“, wenn sie ein aktives Vordergrund-Push-Token für eine App in Ihrem Workspace haben, was bedeutet, dass der Push-Aktivierungsstatus app-spezifisch ist.

{% alert note %}
Informationen zur Überprüfung des Push-Registrierungsstatus finden Sie unter [Push-Registrierungsstatus]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#checking-push-registration-status).
{% endalert %}

## Informationen zur Push-Registrierung und zum Änderungsprotokoll finden {#finding-push-registration-and-changelog-information}

Im Dashboard finden Sie Informationen zur Push-Registrierung und zu Push-Änderungsprotokollen unter:

- **Segmentierung** – Filtern Sie nach Abo-Status, Aktivierungsstatus sowie Vordergrund- und Hintergrund-Aktivierungsstatus der Nutzer:innen.
- **Campaign Analytics** – Zeigen Sie Push-Statistiken und Feedback für eine einzelne Campaign oder ein einzelnes Canvas an.
- **Kundenprofil (Tab „Engagement“)** – Zeigen Sie **Contact Settings** und das Push-Änderungsprotokoll für bestimmte Nutzer:innen an.

Bei der Überprüfung des Push-Aktivierungsstatus zeigt **Push Registered for** an, für welche Plattformen Braze Vordergrund-Push an diese Nutzer:innen senden kann. Unter iOS und Android wird, wenn Nutzer:innen von Vordergrund-Push-aktiviert zu Hintergrund-Push-aktiviert (`remote_notification_enabled`) wechseln, dies im Push-Änderungsprotokoll als „Push-Token was updated from foreground push enabled to foreground push disabled“ dokumentiert.

Wenn Nutzer:innen als Testnutzer:innen hinzugefügt werden, zeigt das Kundenprofil unter **Entwicklungskonsole** > **User Event Log** eine SDK-Anfrage mit `remote_notification_enabled` als `true` oder `false` an. Möglicherweise müssen Sie das Kundenprofil aktualisieren, um die Updates zu sehen, da es eine kurze Verzögerung gibt, bis SDK-Updates das Kundenprofil erreichen.

**Segmentierungsfilter für den iOS-Push-Status:**

- **iOS Vordergrund- und Hintergrund-Push deaktiviert:** Die Nutzer:innen haben noch keine Push-Aufforderung erhalten.
- **iOS Hintergrund aktiviert:** Die Nutzer:innen haben die Push-Aufforderung erhalten und abgelehnt, oder zugestimmt und später Push-Benachrichtigungen in ihren Geräteeinstellungen deaktiviert (wird nach einer Sitzung der Nutzer:innen aktualisiert).
- **iOS Vordergrund aktiviert:** Die Nutzer:innen haben die Push-Aufforderung erhalten und sind berechtigt, Vordergrund-Push zu empfangen.

Campaign Analytics spiegeln die Push-Statistiken entsprechend den weiter oben in diesem Abschnitt beschriebenen Details wider. Sie können auch die Nutzerprofile herunterladen, die in die Campaign oder das Canvas eingetreten sind, um Nutzerprofile abzugleichen.

## Weitere plattformspezifische Szenarien {#other-platform-specific-scenarios}

{% tabs %}
{% tab Web %}

Wenn Nutzer:innen die native Push-Berechtigungsaufforderung akzeptieren, wird ihr Abo-Status auf `opted in` geändert.

Um Abos zu verwalten, können Sie die Nutzer:innenmethode [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) verwenden, um eine Einstellungsseite für Präferenzen auf Ihrer Website zu erstellen, nach der Sie Nutzer:innen nach Opt-out-Status im Dashboard filtern können.

Wenn Nutzer:innen Benachrichtigungen in ihrem Browser deaktivieren, wird die nächste an diese Nutzer:innen gesendete Push-Benachrichtigung bouncen, und Braze wird das Push-Token der Nutzer:innen entsprechend aktualisieren. Dies wird verwendet, um die Berechtigung für die Push-aktivierten Filter (`Background or Foreground Push Enabled`, `Foreground Push Enabled` und `Foreground Push Enabled for App`) zu verwalten. Der im Kundenprofil gesetzte Abo-Status ist eine Einstellung auf Nutzer:innenebene und ändert sich nicht, wenn ein Push bounct.

### 410 Web-Push-Token-Fehler {#410-web-push-token-errors} {#410-web-push-token-errors}

Wenn Sie einen `410: Gone`-Fehler erhalten, kann dies auftreten, wenn Nutzer:innen Web-Push-Benachrichtigungen über die Browsereinstellungen in ihrem Betriebssystem deaktivieren, sich als andere Nutzer:innen auf demselben Gerät einloggen oder die Website seit einiger Zeit nicht mehr besucht haben.

Wenn Sie einen `410: Endpoint Not Valid`-Fehler erhalten, kann dies bedeuten, dass das Web-Push-Token (im Wesentlichen die URL) abgelaufen ist. Dies kann auftreten, wenn Nutzer:innen die Website nie wieder besuchen oder der Browser das Token ungültig macht. Es kann auch periodisch auftreten (oft alle paar Monate), abhängig vom Browser. Wenn Nutzer:innen die Website erneut besuchen und ihr Browser weiterhin auf „Allow“ eingestellt ist, erfasst Braze automatisch ein neues Token für das Gerät. Dies setzt voraus, dass die [`disablePushTokenMaintenance`-Initialisierungsoption](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions) während der SDK-Initialisierung nicht verwendet wird.

{% alert note %}
Web-Plattformen erlauben kein Hintergrund- oder stilles Push.
{% endalert %}
{% endtab %}
{% tab Android %}

Wenn Push-aktivierte Nutzer:innen Push in ihren Betriebssystemeinstellungen deaktivieren, geschieht zu Beginn der nächsten Sitzung Folgendes:
- Braze markiert sie als Vordergrund-Push-deaktiviert und versucht nicht mehr, ihnen Push-Nachrichten zu senden.
- Der Filter `Foreground Push Enabled for App (Android)` und der Segmentierungsfilter `Foreground Push Enabled` (vorausgesetzt, keine anderen Apps im Kundenprofil haben ein gültiges Vordergrund-Push-Token) geben `false` zurück.

In diesem Szenario können Sie, da ein Hintergrund-Push-Token weiterhin existiert, weiterhin Hintergrund-(stille) Push-Benachrichtigungen mit dem Segmentierungsfilter `Background or Foreground Push Enabled = true` senden.

Für Android betrachtet Braze Nutzer:innen als Push-deaktiviert, wenn:

- Nutzer:innen die App von ihrem Gerät deinstallieren.
- Eine Push-Nachricht aufgrund eines Bounces nicht zugestellt werden kann. Dies wird häufig durch eine Deinstallation verursacht, kann aber auch durch App-Updates, eine neue Push-Token-Version oder ein neues Format bedingt sein.
- Die Push-Registrierung bei Firebase Cloud Messaging fehlschlägt (manchmal verursacht durch schlechte Netzwerkverbindungen oder einen Fehler bei der Verbindung zu oder von FCM, um ein gültiges Token zurückzugeben).
- Nutzer:innen Push-Benachrichtigungen für die App in ihren Geräteeinstellungen blockieren und anschließend eine Sitzung protokollieren.

{% alert note %}
Sie können eine Android-Push-Benachrichtigung nur abfangen, wenn die App im Vordergrund oder Hintergrund läuft (aber noch aktiv ist). Sie können Benachrichtigungen nicht abfangen, wenn die App beendet oder vollständig geschlossen wurde.
{% endalert %}

{% endtab %}
{% tab iOS %}

Unabhängig davon, ob Nutzer:innen die Vordergrund-Push-Opt-in-Aufforderung akzeptieren, können Sie weiterhin Hintergrund-Push senden, wenn Sie Remote-Benachrichtigungen in Xcode aktiviert haben und Ihre App [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications) aufruft.

Wenn Ihre App provisorisch autorisiert ist oder die Nutzer:innen Push zugestimmt haben, erhalten sie ein Vordergrund-Push-Token, mit dem Sie ihnen alle Arten von Push senden können. Innerhalb von Braze betrachten wir Nutzer:innen unter iOS, die Vordergrund-Push-aktiviert sind, als Push-aktiviert, entweder explizit (auf App-Ebene) oder provisorisch (auf Geräteebene).

Wenn Nutzer:innen den Empfang von Push-Benachrichtigungen auf Betriebssystemebene ablehnen, ist ihr Push-Abo-Status `Subscribed`, und ihr Profil zeigt nicht an, dass ein Vordergrund-Push-Token registriert wurde.

In dem Szenario, dass Nutzer:innen, die zunächst auf Betriebssystemebene zugestimmt haben, Push-Benachrichtigungen in ihren Betriebssystemeinstellungen deaktivieren, geschieht beim nächsten Sitzungsstart Folgendes:
- Braze markiert sie als Vordergrund-Push-deaktiviert und versucht nicht mehr, Push-Nachrichten zu senden.
- Der Filter `Foreground Push Enabled for App (iOS)` und der Segmentierungsfilter `Foreground Push Enabled` (vorausgesetzt, keine anderen Apps im Kundenprofil haben ein gültiges Vordergrund-Push-Token) geben `false` zurück.

In diesem Szenario können Sie, da ein Hintergrund-Push-Token weiterhin existiert, weiterhin Hintergrund-(stille) Push-Benachrichtigungen mit dem Segmentierungsfilter `Background or Foreground Push Enabled = true` senden.

{% alert note %}
iOS erlaubt es Apps nicht, eine Push-Benachrichtigung abzufangen, bevor sie angezeigt wird. Das bedeutet, dass Apps (und Braze) keine Kontrolle darüber haben, ob die Benachrichtigung angezeigt oder ausgeblendet wird. Nutzer:innen können Push-Benachrichtigungen für eine App in den Geräteeinstellungen deaktivieren, aber dies wird vom Betriebssystem gesteuert.
{% endalert %}

{% endtab %}
{% endtabs %}

## Best Practices {#best-practices}

Detaillierte Anleitungen zur Optimierung Ihrer Push-Nutzung bei Braze finden Sie in unserem speziellen Artikel zu [Push-Best-Practices]({{site.baseurl}}/user_guide/channels/push/best_practices).