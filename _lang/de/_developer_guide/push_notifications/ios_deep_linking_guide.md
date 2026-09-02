---
page_order: 1.1
nav_title: Leitfaden für Deeplinking unter iOS
article_title: Leitfaden für Deeplinking unter iOS
description: "Erfahren Sie, welche Art von Deeplink Sie für Ihre iOS-App verwenden sollten, wann Sie eine AASA-Datei benötigen und welche App-Delegate-Methoden Sie implementieren müssen."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Leitfaden für Deeplinking unter iOS {#ios-deep-linking-guide}

> Dieser Leitfaden unterstützt Sie bei der Auswahl der geeigneten Deeplinking-Strategie für Ihre iOS-App – abhängig davon, welchen Messaging-Kanal Sie verwenden und ob Sie einen Drittanbieter für Links wie Branch nutzen.

Für Details zur Implementierung siehe [Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift). Informationen zur Fehlerbehebung finden Sie unter [Fehlerbehebung bei Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

## Auswahl eines Linktyps {#choosing-a-link-type}

Es gibt drei Möglichkeiten, Links aus Braze-Nachrichten in Ihrer iOS-App zu verarbeiten. Jede funktioniert unterschiedlich und eignet sich für verschiedene Kanäle und Anwendungsfälle.

| Linktyp | Beispiel | Geeignet für | Öffnet ohne installierte App? |
|---|---|---|---|
| **Custom Scheme** | `myapp://products/123` | Push, In-App Messages, Content Cards | Nein — Link schlägt fehl |
| **Universal Link** | `https://myapp.com/products/123` | E-Mail, SMS, Kanäle mit Klick-Tracking | Ja — Fallback auf Web |
| **Web-URL in der App öffnen** | Jede `https://`-URL | Anzeige von Web-Inhalten in einem modalen WebView | N/A — wird im WebView angezeigt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Auswahl eines Linktyps" }

### Custom-Scheme-Deeplinks {#custom-scheme-deep-links}

Custom-Scheme-Deeplinks (zum Beispiel `myapp://products/123`) öffnen Ihre App direkt auf einem bestimmten Bildschirm. Sie sind die einfachste Option für Kanäle, bei denen Links nicht von Dritten verändert werden.

**Verwenden Sie Custom-Scheme-Deeplinks, wenn:**
- Sie Push-Benachrichtigungen, In-App Messages oder Content Cards senden
- Der Link nicht funktionieren muss, wenn die App nicht installiert ist
- Sie kein Klick-Tracking benötigen (Link-Wrapping durch den E-Mail-E-Mail-Anbieter)

**Verwenden Sie Custom-Scheme-Deeplinks nicht, wenn:**
- Sie E-Mails senden — ESPs wrappen Links für das Klick-Tracking, was Custom Schemes bricht
- Der Link auf eine Webseite zurückfallen soll, wenn die App nicht installiert ist

### Universal Links {#universal-links}

Universal Links (zum Beispiel `https://myapp.com/products/123`) sind Standard-HTTPS-URLs, die iOS an Ihre App weiterleiten kann, anstatt sie in einem Browser zu öffnen. Sie erfordern eine serverseitige Konfiguration (eine AASA-Datei) und ein App-seitiges Setup (Associated-Domains-Entitlement).

**Verwenden Sie Universal Links, wenn:**
- Sie E-Mails senden. Ihr E-Mail-Anbieter wrappt Links für das Klick-Tracking, daher müssen Links HTTPS sein.
- Sie SMS oder andere Kanäle nutzen, bei denen Links gewrappt oder gekürzt werden.
- Der Link auf eine Webseite zurückfallen soll, wenn die App nicht installiert ist.
- Sie einen Drittanbieter für Linking wie Branch oder Appsflyer verwenden.

**Verwenden Sie Universal Links nicht, wenn:**
- Sie nur Deeplinks aus Push, In-App Messages oder Content Cards benötigen. Custom Schemes sind einfacher.

### „Web-URL in der App öffnen“ {#open-web-url-inside-app}

Diese Option öffnet eine Webseite in einem modalen WebView innerhalb Ihrer App. Sie wird vollständig vom Braze SDK über `Braze.WebViewController` verarbeitet — Sie müssen keinen Code zur URL-Verarbeitung schreiben.

**Verwenden Sie „Web-URL in der App öffnen“, wenn:**
- Sie eine Webseite (z. B. eine Aktion oder einen Artikel) anzeigen möchten, ohne Ihre App zu verlassen.
- Die URL eine Standard-HTTPS-Webseite ist und kein Deeplink zu einem bestimmten App-Bildschirm.

**Verwenden Sie „Web-URL in der App öffnen“ nicht, wenn:**
- Sie zu einer bestimmten Ansicht in Ihrer App navigieren müssen. Verwenden Sie stattdessen ein Custom Scheme oder einen Universal Link.
- Die Webseite eine Authentifizierung erfordert oder Content-Security-Policy-Header hat, die das Einbetten blockieren.

## Was Sie für jeden Linktyp benötigen {#what-you-need-for-each-link-type}

### Benutzerdefinierte Deeplinks mit eigenem Schema

| Anforderung | Details |
|---|---|
| AASA-Datei | Nicht erforderlich |
| `Info.plist` | Registrieren Sie Ihr Schema unter `CFBundleURLTypes` und fügen Sie es zu `LSApplicationQueriesSchemes` hinzu |
| App-Delegate-Methode | Implementieren Sie `application(_:open:options:)`, um die URL zu analysieren und zu navigieren |
| Braze SDK-Konfiguration | Keine – das SDK öffnet URLs mit benutzerdefiniertem Schema standardmäßig |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Benutzerdefinierte Deeplinks mit eigenem Schema" }

### Universal Links

| Anforderung | Details |
|---|---|
| AASA-Datei | Erforderlich – hosten Sie sie unter `https://yourdomain.com/.well-known/apple-app-site-association` |
| Associated Domains | Fügen Sie `applinks:yourdomain.com` in Xcode unter **Signing & Capabilities** hinzu |
| App-Delegate-Methode | Implementieren Sie `application(_:continue:restorationHandler:)`, um `NSUserActivity` zu verarbeiten |
| Braze SDK-Konfiguration | Setzen Sie `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (optional) | Implementieren Sie `braze(_:shouldOpenURL:)` für benutzerdefiniertes Routing (z. B. Branch) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Universal Links" }

{% alert important %}
Wenn Sie E-Mails über Braze versenden, umschließt Ihr E-Mail-Anbieter (SendGrid, SparkPost oder Amazon SES) Links mit einer Klick-Tracking-Domain. Sie müssen die AASA-Datei auch auf Ihrer Klick-Tracking-Domain hosten, nicht nur auf Ihrer primären Domain. Die vollständige Einrichtung finden Sie unter [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links). Falls jeder E-Mail-Link die App öffnet, lesen Sie [Jeder E-Mail-Link öffnet die App]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting#every-email-link-opens-the-app).
{% endalert %}

### „Web-URL in der App öffnen“

| Anforderung | Details |
|---|---|
| AASA-Datei | Nicht erforderlich |
| App-Delegate-Methode | Nicht erforderlich – das SDK übernimmt dies automatisch |
| Braze SDK-Konfiguration | Keine – wählen Sie **Open Web URL Inside App** im Campaign-Composer aus |
{: .reset-td-br-1 .reset-td-br-2 aria-label="„Web-URL in der App öffnen“" }

## Wann Sie eine AASA-Datei benötigen {#when-aasa}

Eine Apple App Site Association (AASA)-Datei ist nur erforderlich, wenn Sie **universelle Links** verwenden. Sie teilt iOS mit, welche URLs Ihre App verarbeiten kann.

Sie benötigen eine AASA-Datei, wenn:

- Sie Deeplinks in E-Mail-Campaigns versenden (da ESPs Links in HTTPS-Klick-Tracking-URLs einbinden).
- Sie Deeplinks in SMS-Campaigns versenden (da Links möglicherweise zu HTTPS-URLs gekürzt werden).
- Sie Branch, AppsFlyer oder einen anderen Linking-Anbieter verwenden (da diese ihre eigenen HTTPS-Domains nutzen).
- Sie universelle Links aus Push-Benachrichtigungen, In-App-Nachrichten oder Content Cards verwenden (weniger verbreitet, aber möglich mit `forwardUniversalLinks = true`).

Sie benötigen keine AASA-Datei, wenn:

- Sie ausschließlich Deeplinks mit angepasstem Schema (z. B. `myapp://`) aus Push-Benachrichtigungen, In-App-Nachrichten oder Content Cards verwenden.
- Sie die Option **Web-URL in der App öffnen** nutzen.

Anweisungen zur AASA-Einrichtung finden Sie unter [Universelle Links und App-Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

## Wann Sie App-Code zur Verarbeitung von Links benötigen {#when-app-code}

Welche Delegate-Methode Sie implementieren, hängt von der Art des verwendeten Links ab:

| Delegate-Methode | Verarbeitet | Wann implementieren |
|---|---|---|
| `application(_:open:options:)` | Deeplinks mit angepasstem Schema (`myapp://`) | Sie verwenden Deeplinks mit angepasstem Schema aus einem beliebigen Kanal |
| `application(_:continue:restorationHandler:)` | Universelle Links (`https://`) | Sie verwenden universelle Links aus E-Mail, SMS oder mit `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | Alle vom SDK geöffneten URLs | Sie benötigen eine angepasste Routing-Logik (z. B. Branch, bedingte Verarbeitung, Analytics) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Wann Sie App-Code zur Verarbeitung von Links benötigen" }

{% alert tip %}
Wenn Sie einen Drittanbieter für Verlinkungen wie Branch verwenden, implementieren Sie `BrazeDelegate.braze(_:shouldOpenURL:)`, um URLs abzufangen und an das SDK des Anbieters weiterzuleiten. Ein vollständiges Beispiel finden Sie unter [Branch für Deeplinking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking).
{% endalert %}

## Verwendung von Branch mit Braze {#branch}

Wenn Sie [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) als Ihren Linking-Anbieter verwenden, sind für Ihre Einrichtung einige zusätzliche Schritte erforderlich, die über die Standardkonfiguration für universelle Links hinausgehen:

1. **Branch SDK**: Integrieren Sie das Branch SDK gemäß der [Dokumentation von Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Zugehörige Domains**: Fügen Sie Ihre Branch-Domain (z. B. `applinks:yourapp.app.link`) in Xcode unter **Signing & Capabilities** hinzu.
3. **BrazeDelegate**: Implementieren Sie `braze(_:shouldOpenURL:)`, um Branch-Links an das Branch SDK weiterzuleiten, anstatt sie direkt von Braze verarbeiten zu lassen.
4. **Universelle Links weiterleiten**: Setzen Sie `configuration.forwardUniversalLinks = true` in Ihrer Braze-SDK-Konfiguration.

Implementierungsdetails und Anleitungen zur Fehlerbehebung finden Sie unter [Branch für Deeplinking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking).