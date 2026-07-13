---
nav_title: Branch für Deeplinking
article_title: Branch für Deeplinking
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Branch und wie Sie diese nutzen können, um Ihre Deeplinking-Praktiken zu unterstützen."
search_tag: Partner

---

# Branch für Deeplinking {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://branch.io/) ist eine mobile Verknüpfungsplattform für die Akquise, das Engagement und die Messung über Geräte, Kanäle und Plattformen hinweg, die einen ganzheitlichen Blick auf die Touchpoints der Nutzer:innen bietet.

_Diese Integration wird von Branch gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Branch ermöglicht es Ihnen, Ihren Kund:innen bessere Erlebnisse zu bieten, indem Sie den Beginn ihrer User Journey richtig [attributieren]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/) und sie über Deeplinks mit dem gewünschten Zielort verbinden können.

{% alert tip %}
Hilfe bei der Wahl des richtigen Deeplinking-Ansatzes für Ihren Anwendungsfall finden Sie im [iOS-Deeplinking-Leitfaden]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/).
{% endalert %}

## Integration

Folgen Sie dem [Leitfaden zur SDK-Integration von Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview), um Ihre Branch-Integration zum Laufen zu bringen. Im Folgenden finden Sie weitere Anwendungsfälle.

### Unterstützung von iOS Universal Links {#support-ios-universal-links}

Zur Unterstützung des Versendens von iOS Universal Links als Deeplinks aus Braze heraus:

#### 1. Schritt: Branch Universal Links einrichten {#step-1-set-up-branch-universal-links}

Folgen Sie der Dokumentation von Branch, um [Universal Links](https://help.branch.io/developers-hub/docs/ios-universal-links) einzurichten. Im Rahmen dieser Einrichtung hostet Branch die AASA-Datei automatisch auf Ihrer Branch-Link-Domain (zum Beispiel `yourapp.app.link`).

#### 2. Schritt: Associated Domains konfigurieren {#step-2-configure-associated-domains}

Navigieren Sie in Xcode zu Ihrem App-Target > **Signing & Capabilities** und fügen Sie Ihre Branch-Link-Domain unter **Associated Domains** hinzu:

```
applinks:yourapp.app.link
applinks:yourapp-alternate.app.link
```

Falls Sie eine benutzerdefinierte Branch-Domain verwenden, fügen Sie diese ebenfalls hinzu.

#### 3. Schritt: Universal Links in Braze weiterleiten {#step-3-forward-universal-links-in-braze}

Setzen Sie `forwardUniversalLinks` in Ihrer Braze-SDK-Konfiguration auf `true`, damit das SDK Universal Links an den `AppDelegate` Ihrer App weiterleitet:

{% tabs %}
{% tab swift %}
```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
let braze = Braze(configuration: configuration)
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
configuration.forwardUniversalLinks = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endtab %}
{% endtabs %}

#### 4. Schritt: Branch-Links mit BrazeDelegate routen {#step-4-route-branch-links-with-brazedelegate}

Implementieren Sie [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate), um Branch-Links abzufangen, bevor Braze sie verarbeitet. So kann Branch den Link verarbeiten und sein eigenes Routing durchführen:

{% tabs %}
{% tab swift %}
```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host,
     host.contains("app.link") || host.contains("yourdomain.com") {
    // Let Branch handle this link
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle all other links
  return true
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  NSString *host = context.url.host;
  if (host && ([host containsString:@"app.link"] || [host containsString:@"yourdomain.com"])) {
    [[Branch getInstance] handleDeepLink:context.url];
    return NO;
  }
  return YES;
}
```
{% endtab %}
{% endtabs %}

Ersetzen Sie `yourdomain.com` gegebenenfalls durch Ihre benutzerdefinierte Branch-Domain.

### Deeplinking in E-Mails {#deep-linking-in-email}

Lesen Sie die Dokumentation zu [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/)
oder die [Dokumentation von Branch](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work), um Deeplinking aus E-Mails einzurichten, die über Braze gesendet werden.

Das Verknüpfen mit Telefonnummern (Anhängen von `tel` an `href`) wird in der Gmail-App für iOS nicht unterstützt, es sei denn, Nutzer:innen gewähren der App Anrufberechtigungen.

Abhängig von Ihrem ESP sind möglicherweise zusätzliche Anpassungen erforderlich, um Universal Links mit Klick-Tracking zu unterstützen. Diese Informationen finden Sie in unserem entsprechenden Artikel. Sie können auch die folgenden Referenzen heranziehen, um mehr zu erfahren:

- [SendGrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)

## Fehlerbehebung {#troubleshooting}

Wenn Branch-Links aus Braze-Campaigns nicht wie erwartet funktionieren, folgen Sie diesen Schritten.

### Überprüfen, ob der Link außerhalb von Braze funktioniert {#verify-the-link-works-outside-of-braze}

Öffnen Sie den Branch-Link aus der Notizen-App auf einem physischen iOS-Gerät. Wenn Ihre App nicht geöffnet wird:

- Das Problem liegt in Ihrer Branch- oder AASA-Konfiguration, nicht bei Braze.
- Validieren Sie Ihre Branch-AASA unter `https://yourapp.app.link/.well-known/apple-app-site-association`.
- Prüfen Sie, ob Ihre Bundle-ID und Team-ID im Branch-Dashboard übereinstimmen.

### Duales Logging aktivieren {#enable-dual-logging}

1. **Braze**: [Aktivieren Sie ausführliches Logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) und suchen Sie nach `Opening '<URL>':`-Einträgen. Dies bestätigt, dass das SDK den Link empfangen hat.
2. **Branch**: Aktivieren Sie den [Branch-Testmodus](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) und prüfen Sie das Branch-Dashboard auf Link-Klick-Ereignisse.
3. **Vergleich**: Wenn Braze den Link protokolliert, Branch aber keinen Klick registriert, fängt die `BrazeDelegate`-Routing-Logik den Link wahrscheinlich nicht korrekt ab. Prüfen Sie, ob der Domain-Abgleich in `shouldOpenURL` Ihre Branch-Domain enthält.

### Häufige Probleme {#common-issues}

| Symptom | Wahrscheinliche Ursache | Lösung |
|---|---|---|
| Branch-Link öffnet sich in Safari | AASA ungültig oder auf der Branch-Domain nicht vorhanden | Associated Domains und AASA-Datei überprüfen |
| Branch-Link öffnet sich, landet aber auf dem falschen Bildschirm | Branch-Link-Daten falsch konfiguriert | Routing-Regeln im Branch-Dashboard prüfen |
| Link funktioniert über Push, aber nicht per E-Mail | Klick-Tracking-Domain fehlt AASA | AASA auf der Klick-Tracking-Domain Ihres ESP hosten; siehe [E-Mail-Einrichtung](#deep-linking-in-email) |
| `shouldOpenURL` wird für Branch-Links nie ausgelöst | `forwardUniversalLinks` nicht aktiviert | `configuration.forwardUniversalLinks = true` setzen |
| Branch-Link funktioniert aus Notizen, aber nicht aus Braze | `BrazeDelegate` gibt `true` für Branch-URLs zurück | Domain-Prüfung in `shouldOpenURL` überprüfen, ob sie Ihre Branch-Domain enthält |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Häufige Probleme" }

Weitere Szenarien zur Deeplinking-Fehlerbehebung finden Sie unter [Deeplinking-Fehlerbehebung]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting/).