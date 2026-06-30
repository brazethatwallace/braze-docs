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

## Auswahl eines Link-Typs {#choosing-a-link-type}

Es gibt drei Möglichkeiten, Links aus Braze-Nachrichten in Ihrer iOS-App zu verarbeiten. Jede funktioniert anders und eignet sich für unterschiedliche Kanäle und Anwendungsfälle.

| Link-Typ | Beispiel | Am besten geeignet für | Öffnet ohne installierte App? |
|---|---|---|---|
| **Angepasstes Schema** | `myapp://products/123` | Push-Benachrichtigungen, In-App-Nachrichten, Content Cards | Nein – Link funktioniert nicht |
| **Universeller Link** | `https://myapp.com/products/123` | E-Mail, SMS, Kanäle mit Klick-Tracking | Ja – Fallback auf das Internet |
| **Web-URL in der App öffnen** | Jede `https://`-URL | Anzeige von Webinhalten in einem modalen WebView | Nicht zutreffend – wird im WebView angezeigt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Auswahl eines Link-Typs" }

### Deeplinks mit angepasstem Schema {#custom-scheme-deep-links}

Deeplinks mit angepasstem Schema (zum Beispiel `myapp://products/123`) öffnen Ihre App direkt auf einem bestimmten Bildschirm. Sie stellen die einfachste Option für Kanäle dar, bei denen Links nicht von Dritten verändert werden.

**Verwenden Sie Deeplinks mit angepasstem Schema, wenn:**
- Sie Push-Benachrichtigungen, In-App-Nachrichten oder Content Cards versenden
- Der Link nicht funktionieren muss, falls die App nicht installiert ist
- Sie kein Klick-Tracking benötigen (E-Mail-ESP-Link-Wrapping)

**Verwenden Sie keine Deeplinks mit angepasstem Schema, wenn:**
- Sie E-Mails versenden – ESPs verpacken Links für das Klick-Tracking, wodurch angepasste Schemata nicht mehr funktionieren
- Sie den Link als Fallback auf eine Webseite benötigen, falls die App nicht installiert ist

### Universelle Links {#universal-links}

Universelle Links (zum Beispiel `https://myapp.com/products/123`) sind Standard-HTTPS-URLs, die iOS an Ihre App weiterleiten kann, anstatt sie im Browser zu öffnen. Sie erfordern eine serverseitige Konfiguration (eine AASA-Datei) und eine appseitige Einrichtung (Berechtigung für zugehörige Domains).

**Verwenden Sie universelle Links, wenn:**
- Sie E-Mails versenden. Ihr ESP verpackt Links für das Klick-Tracking, daher müssen die Links HTTPS sein.
- Sie SMS oder andere Kanäle nutzen, bei denen Links umgebrochen oder gekürzt werden.
- Sie den Link als Fallback auf eine Webseite benötigen, wenn die App nicht installiert ist.
- Sie einen Drittanbieter für Verlinkungen wie Branch oder AppsFlyer nutzen.

**Verwenden Sie keine universellen Links, wenn:**
- Sie lediglich Deeplinks aus Push-Benachrichtigungen, In-App-Nachrichten oder Content Cards benötigen. Angepasste Schemata sind einfacher.

### „Web-URL in der App öffnen“ {#open-web-url-inside-app}

Diese Option öffnet eine Webseite in einem modalen WebView innerhalb Ihrer App. Dies wird vollständig vom Braze SDK mithilfe von `Braze.WebViewController` abgewickelt – Sie müssen keinen Code für die URL-Verarbeitung schreiben.

**Verwenden Sie „Web-URL in der App öffnen“, wenn:**
- Sie eine Webseite (z. B. eine Aktion oder einen Artikel) anzeigen möchten, ohne Ihre App zu verlassen.
- Die URL eine Standard-HTTPS-Webseite ist und kein Deeplink zu einem bestimmten App-Bildschirm.

**Verwenden Sie „Web-URL in der App öffnen“ nicht, wenn:**
- Sie zu einer bestimmten Ansicht in Ihrer App navigieren müssen. Verwenden Sie stattdessen ein angepasstes Schema oder einen universellen Link.
- Die Webseite eine Authentifizierung erfordert oder über Content-Security-Policy-Header verfügt, die die Einbettung verhindern.

## Was Sie für jeden Link-Typ benötigen {#what-you-need-for-each-link-type}

### Deeplinks mit angepasstem Schema

| Anforderung | Details |
|---|---|
| AASA-Datei | Nicht erforderlich |
| `Info.plist` | Registrieren Sie Ihr Schema unter `CFBundleURLTypes` und fügen Sie es zu `LSApplicationQueriesSchemes` hinzu |
| App-Delegate-Methode | Implementieren Sie `application(_:open:options:)`, um die URL zu parsen und die Navigation durchzuführen |
| Konfiguration des Braze SDK | Keine – das SDK öffnet standardmäßig URLs mit angepasstem Schema |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Deeplinks mit angepasstem Schema" }

### Universelle Links

| Anforderung | Details |
|---|---|
| AASA-Datei | Erforderlich – hosten Sie sie unter `https://yourdomain.com/.well-known/apple-app-site-association` |
| Zugehörige Domains | Fügen Sie `applinks:yourdomain.com` in Xcode unter **Signing & Capabilities** hinzu |
| App-Delegate-Methode | Implementieren Sie `application(_:continue:restorationHandler:)`, um `NSUserActivity` zu verarbeiten |
| Konfiguration des Braze SDK | Setzen Sie `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (optional) | Implementieren Sie `braze(_:shouldOpenURL:)` für angepasstes Routing (z. B. Branch) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Universelle Links" }

{% alert important %}
Wenn Sie E-Mails über Braze versenden, verpackt Ihr ESP (SendGrid, SparkPost oder Amazon SES) Links in eine Klick-Tracking-Domain. Sie müssen die AASA-Datei auch auf Ihrer Klick-Tracking-Domain hosten, nicht nur auf Ihrer primären Domain. Für die vollständige Einrichtung siehe [Universelle Links und App-Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).
{% endalert %}

### „Web-URL in der App öffnen“

| Anforderung | Details |
|---|---|
| AASA-Datei | Nicht erforderlich |
| App-Delegate-Methode | Nicht erforderlich – das SDK übernimmt dies automatisch |
| Konfiguration des Braze SDK | Keine – wählen Sie **Open Web URL Inside App** im Campaign-Composer aus |
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

Anweisungen zur AASA-Einrichtung finden Sie unter [Universelle Links und App-Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#setting-up-universal-links-and-app-links).

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