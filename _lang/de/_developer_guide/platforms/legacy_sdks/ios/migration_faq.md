---
nav_title: Migrations-FAQ
article_title: iOS SDK Migrations-FAQ
platform: iOS
page_order: 12
description: "Diese Seite beantwortet häufig gestellte Fragen zur Migration vom Appboy iOS SDK (Objective-C) zum Braze Swift SDK."
noindex: true
---

# iOS SDK Migrations-FAQ {#ios-sdk-migration-faq}

> Diese Seite beantwortet häufig gestellte Fragen zur Migration vom älteren Appboy iOS SDK (auch bekannt als Objective-C SDK) zum Braze Swift SDK.

{% multi_lang_include deprecations/objective-c.md %}

## Versionsunterstützung und End-of-Life {#version-support-and-end-of-life}

### Ist das Appboy iOS SDK 4.7.0 End-of-Life? {#is-appboy-ios-sdk-470-end-of-life}

Ja, das Appboy iOS SDK 4.7.0 (und alle 4.x-Versionen) hat das End-of-Life erreicht. Es werden keine Sicherheitskorrekturen oder kritischen Fehlerbehebungen bereitgestellt. Obwohl Messaging und Analytics weiterhin normal funktionieren, sollte Version 4.7.0 aus Sicherheitsperspektive als nicht unterstützt betrachtet werden.

### Was ist die Mindestversion des Swift SDK für den Produktionssupport? {#what-is-the-minimum-swift-sdk-version-for-production-support}

Aktuelle Hauptversionen (16.x und höher) sind das Ziel für laufenden Support, Fehlerbehebungen und neue Features. Ältere Nebenversionen erhalten möglicherweise keine fortlaufende Wartung.

## Kompatibilitätsbibliotheken {#compatibility-libraries}

### Werden BrazeKitCompat und BrazeUICompat für den Produktiveinsatz mit Swift SDK 17.x unterstützt? {#are-brazekitcompat-and-brazeuicompat-supported-for-production-use-on-swift-sdk-17x}

Ja, `BrazeKitCompat` und `BrazeUICompat` werden während der Migration für den Produktiveinsatz unterstützt. Sie dienen als „Zwischenschritt“ mit minimalem Migrationsaufwand, um Ihnen den Wechsel vom Appboy SDK zum Swift SDK mit möglichst wenigen Codeänderungen zu erleichtern – nicht als langfristige Lösung. Obwohl sie offiziell unterstützt werden und weiterhin Fehlerbehebungen erhalten, ist die Absicht, letztendlich von diesen Kompatibilitätsbibliotheken auf die modernen Swift SDK APIs umzusteigen.

### Wann werden BrazeKitCompat und BrazeUICompat entfernt? {#when-will-brazekitcompat-and-brazeuicompat-be-removed}

Das Swift SDK-Team plant, die `BrazeKitCompat`-Bibliothek einzustellen, aber es wurde noch kein konkreter Zeitplan angekündigt. Es wird empfohlen, eine vollständige Migration zu den modernen Swift SDK APIs (`BrazeKit`, `BrazeUI`) zu planen, anstatt sich auf unbestimmte Zeit auf die Kompatibilitätsbibliotheken zu verlassen.

## Verzögerte Initialisierung {#delayed-initialization}

### Kann ich die SDK-Initialisierung verzögern, bis die Nutzer:innen-Einwilligung vorliegt? {#can-i-delay-sdk-initialization-until-after-user-consent}

Ja. Das Swift SDK unterstützt die verzögerte Initialisierung, was für Apps nützlich ist, die vor dem Start des SDK auf die Einwilligung der Nutzer:innen warten müssen. Rufen Sie `Braze.prepareForDelayedInitialization()` (optional mit einem `analyticsBehavior`-Parameter) frühzeitig in `application(_:didFinishLaunchingWithOptions:)` auf und initialisieren Sie das SDK später, indem Sie den Standard-Braze-Initializer aufrufen, nachdem die Einwilligung eingeholt wurde.

Ausführliche Informationen zur Implementierung finden Sie unter [Verzögerte Initialisierung einrichten]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_step-2-set-up-delayed-initialization-optional).

### Welche Swift-SDK-Mindestversion ist für die verzögerte Initialisierung erforderlich? {#what-is-the-minimum-swift-sdk-version-required-for-delayed-initialization}

Swift SDK 11.2.0 ist die Mindestversion für die verzögerte Initialisierung. Die Robustheit von Push und Deeplinks bei verzögerter Initialisierung wurde in Version 14.1.0 weiter verbessert. Swift SDK 17.0.0 liegt deutlich über beiden Schwellenwerten.

### Was passiert mit Ereignissen, die vor der SDK-Initialisierung empfangen werden? {#what-happens-to-events-received-before-the-sdk-is-initialized}

Wenn das SDK initialisiert wird, werden die in der Warteschlange befindlichen Elemente verarbeitet. Das Verhalten variiert jedoch je nach Kanal:

| Kanal | Verhalten vor der Initialisierung |
|---------|----------------------------|
| Push-Token | In die Warteschlange eingereiht; bei Initialisierung verarbeitet |
| Push-Öffnungen/Analytics | Standardmäßig in die Warteschlange eingereiht (konfigurierbar zum Verwerfen über `analyticsBehavior`) |
| Deeplinks | In die Warteschlange eingereiht; bei Initialisierung verarbeitet |
| In-App Messages | Vor der Initialisierung nicht gepuffert; erfordern ein laufendes SDK |
| Content Cards | Vor der Initialisierung nicht gepuffert; nach der Initialisierung vom Server synchronisiert |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
In-App Messages und Content Cards, die vor der Initialisierung empfangen werden, werden nicht garantiert zugestellt. Stellen Sie sicher, dass das SDK initialisiert ist, bevor Sie versuchen, diese Kanäle anzuzeigen.
{% endalert %}

## Ressourcen-Bundles und SPM-Integration {#resource-bundles-and-spm-integration}

### Warum erhalte ich einen Laufzeitfehler wegen fehlendem `braze-swift-sdk_BrazeUI.bundle`? {#why-am-i-seeing-a-runtime-error-about-missing-braze-swift-sdk_brazeuibundle}

Dies ist kein bekannter SDK-Bug und liegt wahrscheinlich an einer fehlerhaften Integrationskonfiguration. Ab Swift SDK 12.0.0 enthalten statische XCFrameworks Ressourcen direkt, anstatt auf externe Ressourcen-Bundles angewiesen zu sein.

### Welche SPM-/Xcode-/Archivierungsanforderungen gelten für die Ressourceneinbettung? {#what-are-the-spmxcodearchive-requirements-for-resource-embedding}

Ab Swift SDK 12.0.0 müssen Sie in Ihren Xcode-Projekteinstellungen **Embed & Sign** für die Braze XCFrameworks auswählen – dies gilt sowohl für statische als auch für dynamische Varianten. Dies ist die häufigste Ursache für fehlende Bundle-Fehler beim Archivieren oder Veröffentlichen.

### Wie überschreibe ich Ressourcen-Bundles für nicht standardmäßige Build-Systeme? {#how-do-i-override-resource-bundles-for-non-standard-build-systems}

Für nicht standardmäßige Build-Systeme (Tuist, Bazel, Buck, CI) verwenden Sie die genehmigten Override-APIs:

- `BrazeKit.overrideResourcesBundle` (beachten Sie den Plural „Resources“)
- `BrazeUI.overrideResourcesBundle` (beachten Sie den Plural „Resources“)

Die Singularform `overrideResourceBundle` wurde in Swift SDK 8.1.0 als veraltet markiert und sollte nicht mehr verwendet werden.

## Nutzeridentität und Push-Token {#user-identity-and-push-tokens}

### Gibt es eine Validierungs-Checkliste zur Bewahrung von Profilen, Gerätezuordnungen und Push-Token? {#is-there-a-validation-checklist-for-preserving-profiles-device-associations-and-push-tokens}

In der Dokumentation existiert keine offizielle migrationsspezifische Checkliste. Wir empfehlen, die folgenden Validierungsschritte durchzuführen:

1. Bestätigen Sie, dass `registerDeviceToken` oder die Push-Automatisierung nach der Migration korrekt eingerichtet ist.
2. Überprüfen Sie die Anzahl der Push-registrierten Nutzer:innen im Dashboard vor und nach dem Rollout.
3. Prüfen Sie stichprobenartig einige spezifische externe IDs, um sicherzustellen, dass die Gerätezuordnungen intakt bleiben.

### Garantiert `changeUser`, dass Push-Token dem neuen/der neuen Nutzer:in folgen? {#does-changeuser-guarantee-that-push-tokens-follow-the-new-user}

Es gibt keine explizite schriftlich dokumentierte Garantie. Die Designabsicht ist jedoch, dass Push-Token dem Gerät folgen, nicht dem/der Nutzer:in. Der Aufruf von `changeUser` sollte das vorhandene Geräte-Token mit dem neuen Nutzerprofil neu verknüpfen. Sie sollten `changeUser` testen, das Dashboard überprüfen und bestätigen, dass das Token im neuen Profil erscheint, bevor Sie einen Massen-Rollout durchführen.