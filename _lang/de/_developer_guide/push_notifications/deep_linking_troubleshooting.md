---
nav_title: Fehlerbehebung bei Deeplinking
article_title: Fehlerbehebung bei Deeplinking
description: "Diagnostizieren Sie iOS-Deeplinking-Probleme mithilfe eines Symptomverzeichnisses, eines standardmäßigen Untersuchungspfads und plattformspezifischer Prüfungen."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Fehlerbehebung bei Deeplinking {#troubleshoot-deep-linking}

> Verwenden Sie diese Seite, um häufige Deeplinking-Probleme unter iOS zu diagnostizieren. Hilfe bei der Auswahl des richtigen Linktyps finden Sie im [iOS-Deeplinking-Leitfaden]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Für Details zur Implementierung siehe [Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift).

## Starten Sie hier: Finden Sie Ihr Symptom {#start-here-match-your-symptom}

Suchen Sie das Verhalten, das Sie beobachten, in der Tabelle und folgen Sie dann den Schritten des entsprechenden Abschnitts. Wenn Sie nicht sicher sind, welcher Abschnitt zutrifft, verwenden Sie den [Standard-Untersuchungspfad](#standard-investigation-path).

| Symptom | Gehe zu |
| --- | --- |
| Link mit benutzerdefiniertem Schema öffnet die App, aber den falschen Bildschirm | [Deeplink mit benutzerdefiniertem Schema öffnet nicht die richtige Ansicht](#custom-scheme-deep-link-does-not-open-the-correct-view) |
| Universal Link öffnet Safari statt der App | [Universal Link öffnet Safari statt der App](#universal-link-opens-in-safari-instead-of-the-app) |
| E-Mail-Link öffnet die App nicht | [Deeplink aus E-Mail öffnet die App nicht](#deep-link-from-email-does-not-open-the-app) |
| Jeder E-Mail-Link öffnet die App | [Jeder E-Mail-Link öffnet die App](#every-email-link-opens-the-app) |
| Funktioniert über Push, aber nicht über In-App-Nachricht (oder umgekehrt) | [Deeplink funktioniert über Push, aber nicht über In-App-Nachricht](#deep-link-works-from-push-but-not-from-in-app-message) |
| „Open Web URL Inside App“ zeigt eine leere WebView | [„Open Web URL Inside App“ zeigt eine leere oder fehlerhafte Seite](#open-web-url-inside-app-shows-a-blank-or-broken-page) |
| Branch-Link öffnet die App nicht oder leitet nicht korrekt weiter | [Fehlerbehebung für Branch mit Braze](#branch) |
| Deeplink schlägt ohne erkennbare Ursache fehl | [Allgemeine Debugging-Tipps](#general-debugging-tips) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deeplinking-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow für jeden Deeplinking-Vorfall. Beginnen Sie bei Schritt 1.

1. Testen Sie den Link außerhalb von Braze. Für benutzerdefinierte Schemata führen Sie `xcrun simctl openurl booted "<URL>"` im Terminal aus (zum Beispiel `xcrun simctl openurl booted "myapp://products/123"`). Für Universal Links fügen Sie die URL in die Notizen-App auf einem physischen Gerät ein und tippen Sie darauf.
2. [Aktivieren Sie das ausführliche Logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) und reproduzieren Sie das Problem. Suchen Sie nach `Opening '<URL>':` Einträgen mit `channel`, `useWebView` und `isUniversalLink`.
3. Überprüfen Sie bei Universal Links Ihre AASA-Datei und die Associated-Domains-Berechtigung.
4. Bestätigen Sie bei E-Mail-Links, dass die Klick-Tracking-Domain eine gültige AASA-Datei hostet.
5. Wenn Sie `BrazeDelegate.braze(_:shouldOpenURL:)` implementieren, stellen Sie sicher, dass Links kanalübergreifend konsistent behandelt werden.
6. Wenn das Problem weiterhin besteht, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) mit ausführlichen Logs und der Link-URL.

## Deeplink mit benutzerdefiniertem Schema öffnet nicht die richtige Ansicht {#custom-scheme-deep-link-does-not-open-the-correct-view}

**Symptom:** Ein Deeplink mit benutzerdefiniertem Schema (zum Beispiel `myapp://products/123`) öffnet Ihre App, navigiert aber nicht zum gewünschten Bildschirm.

1. **Überprüfen Sie, ob das Schema registriert ist.** Prüfen Sie in Xcode, ob Ihr Schema unter `CFBundleURLTypes` in `Info.plist` aufgeführt ist.
2. **Überprüfen Sie Ihren Handler.** Setzen Sie einen Breakpoint in `application(_:open:options:)`, um zu bestätigen, dass die Methode aufgerufen wird, und inspizieren Sie den `url`-Parameter.
3. **Testen Sie den Link unabhängig.** Führen Sie den folgenden Befehl im Terminal aus, um den Deeplink außerhalb von Braze zu testen:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   Wenn der Link hier nicht funktioniert, liegt das Problem in der URL-Verarbeitung Ihrer App – nicht in Braze.
4. **Überprüfen Sie das URL-Format.** Stellen Sie sicher, dass die URL in Ihrer Campaign mit dem übereinstimmt, was Ihr Handler erwartet. Häufige Fehler sind fehlende Pfadkomponenten oder falsche Groß-/Kleinschreibung.

## Universal Link öffnet in Safari statt in der App {#universal-link-opens-in-safari-instead-of-the-app}

**Symptom:** Ein Universal Link (z. B. `https://myapp.com/products/123`) öffnet in Safari statt in Ihrer App.

### Überprüfen Sie die Associated-Domains-Berechtigung {#verify-the-associated-domains-entitlement}

Öffnen Sie in Xcode Ihr App-Ziel > **Signing & Capabilities** und prüfen Sie, ob `applinks:yourdomain.com` unter **Associated Domains** aufgeführt ist.

### Validieren Sie die AASA-Datei {#validate-the-aasa-file}

Ihre Apple App Site Association (AASA)-Datei muss an einem der folgenden Orte gehostet werden:

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

Überprüfen Sie Folgendes:

- Die Datei wird über HTTPS mit einem gültigen Zertifikat bereitgestellt.
- Der `Content-Type` ist `application/json`.
- Die Dateigröße liegt unter 128 KB.
- Die `appID` stimmt mit Ihrer Team-ID und Bundle-ID überein (z. B. `ABCDE12345.com.example.myapp`).
- Das `paths`- oder `components`-Array enthält die erwarteten URL-Muster.

Sie können Ihre AASA mit dem [Suchvalidierungstool von Apple](https://search.developer.apple.com/appsearch-validation-tool/) oder durch Ausführen des folgenden Befehls validieren:

```bash
swcutil dl -d yourdomain.com
```

### Überprüfen Sie den `AppDelegate` {#check-the-appdelegate}

Stellen Sie sicher, dass `application(_:continue:restorationHandler:)` in Ihrem `AppDelegate` implementiert ist und die `NSUserActivity` korrekt verarbeitet:

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Überprüfen Sie die Braze-SDK-Konfiguration {#verify-braze-sdk-configuration}

Wenn Sie Universal Links aus Push-Benachrichtigungen, In-App-Nachrichten oder Content Cards von Braze verwenden, stellen Sie sicher, dass `forwardUniversalLinks` aktiviert ist:

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
Die Weiterleitung von Universal Links erfordert Zugriff auf die Anwendungsberechtigungen. Bei der Ausführung in einem Simulator sind diese Berechtigungen nicht direkt verfügbar. Um in einem Simulator zu testen, fügen Sie die `.entitlements`-Datei zur Build-Phase **Copy Bundle Resources** hinzu.
{% endalert %}

### Überprüfen Sie das Problem mit langem Drücken {#check-for-the-long-press-issue}

Wenn Sie einen Universal Link lange gedrückt halten und **Öffnen** auswählen, kann iOS die Universal-Link-Zuordnung für diese Domain „aufheben“. Dies ist ein bekanntes iOS-Verhalten. Um es zurückzusetzen, drücken Sie erneut lange auf den Link und wählen Sie **In [App-Name] öffnen**.

## Deeplink aus E-Mail öffnet die App nicht {#deep-link-from-email-does-not-open-the-app}

**Symptom:** Ein Link in einer E-Mail öffnet Ihre App nicht über den Universal Link.

E-Mail-Links durchlaufen das Klick-Tracking-System Ihres ESP, das Links in eine Tracking-Domain einbettet (zum Beispiel `https://click.yourdomain.com/...`). Damit Universal Links aus E-Mails funktionieren, müssen Sie die AASA-Datei auf Ihrer Klick-Tracking-Domain konfigurieren – nicht nur auf Ihrer primären Domain.

### AASA der Klick-Tracking-Domain überprüfen {#verify-click-tracking-domain-aasa}

1. Identifizieren Sie Ihre Klick-Tracking-Domain in den Einstellungen Ihres ESP (SendGrid, SparkPost oder Amazon SES).
2. Hosten Sie die AASA-Datei unter `https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. Bestätigen Sie, dass die AASA-Datei auf der Klick-Tracking-Domain dieselbe `appID` und gültige Pfadmuster enthält.

ESP-spezifische Einrichtungsanweisungen finden Sie unter [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

### Weiterleitungskette prüfen {#check-the-redirect-chain}

Einige ESPs führen eine Weiterleitung von der Klick-Tracking-URL zu Ihrer endgültigen URL durch. Universal Links funktionieren nur, wenn iOS die *initiale* Domain (die Klick-Tracking-Domain) als mit Ihrer App verknüpft erkennt. Wenn die Weiterleitung die AASA-Prüfung umgeht, wird der Link in Safari geöffnet.

So testen Sie:

1. Senden Sie sich selbst eine Test-E-Mail.
2. Halten Sie den Link lange gedrückt und prüfen Sie die URL – dies ist die Klick-Tracking-URL.
3. Überprüfen Sie, ob diese Domain eine gültige AASA-Datei hat.

## Jeder E-Mail-Link öffnet die App {#every-email-link-opens-the-app}

**Symptom:** Jeder Link in einer E-Mail öffnet Ihre App, einschließlich Links, die Sie erwarten würden, im Browser zu öffnen.

Ihre AASA-Datei auf der Klick-Tracking-Domain verwendet `paths`, die jede URL auf dieser Domain abdecken (zum Beispiel `*` oder `/*`). iOS behandelt dann jeden klickgetrackten E-Mail-Link als universellen Link.

Beschränken Sie `paths` auf die URLs, die die App öffnen sollen. Für SendGrid matchen Sie `/uni/` und fügen Sie `universal="true"` nur bei diesen Links hinzu.

Informationen zur ESP-spezifischen Einrichtung, einschließlich Android-`pathPrefix`-Werte, finden Sie unter [Universelle Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#universal-links-app-links-and-click-tracking).

## Deeplink funktioniert über Push, aber nicht über In-App-Nachricht (oder umgekehrt) {#deep-link-works-from-push-but-not-from-in-app-message}

**Symptom:** Derselbe Deeplink funktioniert über einen Braze-Kanal, aber nicht über einen anderen.

### BrazeDelegate überprüfen {#check-the-brazedelegate}

Wenn Sie `BrazeDelegate.braze(_:shouldOpenURL:)` implementieren, stellen Sie sicher, dass Links kanalübergreifend einheitlich behandelt werden. Der Parameter `context` enthält den Quellkanal. Achten Sie auf bedingte Logik, die Links aus bestimmten Kanälen versehentlich herausfiltern könnte.

### Ausführliches Logging aktivieren {#enable-verbose-logging}

[Aktivieren Sie ausführliches Logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) und reproduzieren Sie das Problem. Suchen Sie nach dem `Opening`-Logeintrag:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Vergleichen Sie die Logausgabe des funktionierenden Kanals mit der des nicht funktionierenden Kanals. Unterschiede bei `useWebView` oder `isUniversalLink` zeigen, wie das SDK den Link unterschiedlich interpretiert.

### Angepasste Display-Delegates überprüfen {#check-for-custom-display-delegates}

Wenn Sie einen angepassten In-App-Nachrichten-Display-Delegate oder Content-Card-Klick-Handler verwenden, stellen Sie sicher, dass Link-Ereignisse korrekt an das Braze SDK zur Verarbeitung weitergeleitet werden.

## „Web-URL in App öffnen“ zeigt eine leere oder fehlerhafte Seite {#open-web-url-inside-app-shows-a-blank-or-broken-page}

**Symptom:** Die Auswahl von **Open Web URL Inside App** führt zu einer leeren oder fehlerhaften WebView.

1. **Überprüfen Sie, ob die URL HTTPS verwendet.** Die WebView des SDK erfordert ATS-konforme URLs. HTTP-Links schlagen ohne Fehlermeldung fehl.
2. **Überprüfen Sie die Content-Security-Policy-Header.** Wenn die Zielwebseite `X-Frame-Options: DENY` oder eine restriktive `Content-Security-Policy` setzt, wird die Darstellung in einer WebView blockiert.
3. **Überprüfen Sie Weiterleitungen zu benutzerdefinierten Schemata.** Wenn die Webseite zu einem benutzerdefinierten Schema weiterleitet (z. B. `myapp://`), kann die WebView dies nicht verarbeiten.
4. **Testen Sie die URL in Safari.** Wenn die Seite in Safari auf dem Gerät nicht geladen wird, wird sie auch in der WebView nicht geladen.

## Fehlerbehebung bei Branch mit Braze {#branch}

Wenn Sie [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) als Ihren Linking-Anbieter verwenden:

### Überprüfen Sie, ob der BrazeDelegate an Branch weiterleitet {#verify-the-brazedelegate-routes-to-branch}

Ihr `BrazeDelegate` muss Branch-Links abfangen und an das Branch SDK weiterleiten. Überprüfen Sie Folgendes:

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

Wenn `shouldOpenURL` für Branch-Links `true` zurückgibt, verarbeitet Braze diese direkt, anstatt sie an Branch weiterzuleiten.

### Überprüfen Sie die Branch-Link-Domain {#check-branch-link-domain}

Stellen Sie sicher, dass die Branch-Domain in Ihrem `BrazeDelegate` mit Ihrer tatsächlichen Branch-Link-Domain übereinstimmt. Branch verwendet mehrere Domain-Formate:

- `yourapp.app.link` (Standard)
- `yourapp-alternate.app.link` (alternativ)
- Angepasste Domains (sofern im Branch-Dashboard konfiguriert)

### Aktivieren Sie die Protokollierung beider SDKs {#enable-both-sdks-logging}

Um festzustellen, wo der Link in der Kette unterbrochen wird:

1. Aktivieren Sie die [ausführliche Protokollierung von Braze]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Suchen Sie nach `Opening '<URL>':`-Einträgen, um sicherzustellen, dass das SDK den Link erhalten hat.
2. Aktivieren Sie den [Branch-Testmodus](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking). Überprüfen Sie das Branch-Dashboard auf Link-Klick-Ereignisse.
3. Wenn Braze den Link protokolliert, Branch jedoch keinen Klick erkennt, liegt das Problem wahrscheinlich an der `BrazeDelegate`-Weiterleitungslogik.

### Überprüfen Sie die Branch-Dashboard-Konfiguration {#check-branch-dashboard-configuration}

Überprüfen Sie im Branch-Dashboard Folgendes:

- Die **Bundle-ID** und **Team-ID** Ihrer App stimmen mit Ihrem Xcode-Projekt überein.
- Ihre **Associated Domains** enthalten die Branch-Link-Domain.
- Ihre Branch-AASA-Datei ist gültig (Branch hostet diese automatisch auf `app.link`-Domains).

### Testen Sie Branch-Links unabhängig {#test-branch-links-independently}

Testen Sie den Branch-Link außerhalb von Braze, um das Problem einzugrenzen:

1. Öffnen Sie den Branch-Link in Safari auf Ihrem Gerät. Wenn die App nicht geöffnet wird, liegt das Problem in Ihrer Branch- oder AASA-Konfiguration – nicht bei Braze.
2. Fügen Sie den Branch-Link in die Notizen-App ein und tippen Sie darauf. Universal Links funktionieren über die Notizen-App zuverlässiger als über die Adressleiste von Safari.

## Allgemeine Tipps zur Fehlerbehebung {#general-debugging-tips}

### Ausführliche Protokollierung verwenden {#use-verbose-logging}

[Aktivieren Sie die ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), um genau zu sehen, wie das SDK Links verarbeitet. Wichtige Einträge, auf die Sie achten sollten:

| Protokolleintrag | Bedeutung |
|---|---|
| `Opening '<URL>': - channel: notification` | Das SDK verarbeitet einen Link aus einer Push-Benachrichtigung |
| `Opening '<URL>': - channel: inAppMessage` | Das SDK verarbeitet einen Link aus einer In-App-Nachricht |
| `Opening '<URL>': - channel: contentCard` | Das SDK verarbeitet einen Link aus einer Content-Card |
| `useWebView: true` | Das SDK öffnet die URL in der In-App-WebView |
| `isUniversalLink: true` | Das SDK hat die URL als Universal Link identifiziert |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ausführliche Protokollierung verwenden" }

Weitere Informationen zum Lesen dieser Protokolle finden Sie unter [Ausführliche Protokolle lesen]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

### Links isoliert testen {#test-links-in-isolation}

Bevor Sie über Braze testen, überprüfen Sie, ob Ihr Deeplink oder Universal Link eigenständig funktioniert:

- **Custom Scheme**: Führen Sie `xcrun simctl openurl booted "myapp://path"` im Terminal aus.
- **Universal Link**: Fügen Sie die URL in die Notizen-App auf einem physischen Gerät ein und tippen Sie darauf. Testen Sie nicht über die Safari-Adressleiste, da iOS eingetippte URLs anders behandelt als angetippte Links.
- **Branch-Link**: Öffnen Sie den Branch-Link über die Notizen-App auf einem Gerät.

### Auf einem physischen Gerät testen {#test-on-a-physical-device}

Universal Links werden im iOS-Simulator nur eingeschränkt unterstützt. Testen Sie für genaue Ergebnisse immer auf einem physischen Gerät. Falls Sie im Simulator testen müssen, fügen Sie die `.entitlements`-Datei zur Build-Phase **Copy Bundle Resources** hinzu.