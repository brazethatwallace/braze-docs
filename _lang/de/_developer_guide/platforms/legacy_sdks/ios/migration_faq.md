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

### Hat das Appboy iOS SDK 4.7.0 das End-of-Life erreicht? {#is-appboy-ios-sdk-470-end-of-life}

Ja, das Appboy iOS SDK 4.7.0 (und alle 4.x-Versionen) hat das End-of-Life erreicht. Es werden keine Sicherheitskorrekturen oder kritischen Fehlerbehebungen mehr bereitgestellt. Obwohl Messaging und Analytics weiterhin normal funktionieren, sollte Version 4.7.0 aus Sicherheitsperspektive als nicht unterstützt betrachtet werden.

### Welche Swift SDK-Mindestversion wird für den Produktionsbetrieb unterstützt? {#what-is-the-minimum-swift-sdk-version-for-production-support}

Aktuelle Hauptversionen (16.x und höher) sind das Ziel für laufende Unterstützung, Fehlerbehebungen und neue Features. Ältere Nebenversionen erhalten möglicherweise keine fortlaufende Wartung.

## Kompatibilitätsbibliotheken {#compatibility-libraries}

### Werden BrazeKitCompat und BrazeUICompat für den Produktionseinsatz mit Swift SDK 17.x unterstützt? {#are-brazekitcompat-and-brazeuicompat-supported-for-production-use-on-swift-sdk-17x}

Ja, `BrazeKitCompat` und `BrazeUICompat` werden während der Migration für den Produktionseinsatz unterstützt. Sie sind als „Stepping Stone“ mit minimalem Migrationsaufwand konzipiert, um Ihnen den Wechsel vom Appboy SDK zum Swift SDK mit minimalen Codeänderungen zu erleichtern – nicht als langfristige Lösung. Obwohl sie offiziell unterstützt werden und weiterhin Fehlerbehebungen erhalten, ist das Ziel, letztendlich von diesen Kompatibilitätsbibliotheken zu den modernen Swift SDK APIs zu migrieren.

### Wann werden BrazeKitCompat und BrazeUICompat entfernt? {#when-will-brazekitcompat-and-brazeuicompat-be-removed}

Das Swift SDK-Team plant, die `BrazeKitCompat`-Bibliothek einzustellen, aber es wurde noch kein konkreter Zeitplan angekündigt. Es wird empfohlen, eine vollständige Migration zu den modernen Swift SDK APIs (`BrazeKit`, `BrazeUI`) zu planen, anstatt sich auf unbestimmte Zeit auf die Kompatibilitätsbibliotheken zu verlassen.

## Verzögerte Initialisierung {#delayed-initialization}

### Kann ich die SDK-Initialisierung bis nach der Einwilligung der Nutzer:innen verzögern? {#can-i-delay-sdk-initialization-until-after-user-consent}

Ja. Das Swift SDK unterstützt eine verzögerte Initialisierung, die für Apps nützlich ist, die auf die Einwilligung der Nutzer:innen warten müssen, bevor das SDK gestartet wird. Rufen Sie `Braze.prepareForDelayedInitialization()` (optional mit einem `analyticsBehavior`-Parameter) frühzeitig in `application(_:didFinishLaunchingWithOptions:)` auf und initialisieren Sie das SDK dann später, indem Sie den Standard-Braze-Initializer aufrufen, nachdem die Einwilligung eingeholt wurde.

Für eine detaillierte Implementierung siehe [Verzögerte Initialisierung einrichten]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#step-2-set-up-delayed-initialization-optional).

### Welche Swift SDK-Mindestversion ist für die verzögerte Initialisierung erforderlich? {#what-is-the-minimum-swift-sdk-version-required-for-delayed-initialization}

Swift SDK 11.2.0 ist die Mindestversion für die verzögerte Initialisierung. Die Robustheit von Push und Deeplinks bei verzögerter Initialisierung wurde in Version 14.1.0 weiter verbessert. Swift SDK 17.0.0 liegt deutlich über beiden Schwellenwerten.

### Was passiert mit Ereignissen, die vor der SDK-Initialisierung empfangen werden? {#what-happens-to-events-received-before-the-sdk-is-initialized}

Wenn das SDK initialisiert wird, werden die in der Warteschlange befindlichen Elemente verarbeitet. Das Verhalten variiert jedoch je nach Kanal:

| Kanal | Verhalten vor der Initialisierung |
|---------|----------------------------|
| Push-Token | In Warteschlange gestellt; bei Initialisierung verarbeitet |
| Push-Öffnungen/Analytics | Standardmäßig in Warteschlange gestellt (konfigurierbar zum Verwerfen über `analyticsBehavior`) |
| Deeplinks | In Warteschlange gestellt; bei Initialisierung verarbeitet |
| In-App Messages | Werden vor der Initialisierung nicht gepuffert; erfordern ein laufendes SDK |
| Content Cards | Werden vor der Initialisierung nicht gepuffert; nach der Initialisierung vom Server synchronisiert |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
In-App Messages und Content Cards, die vor der Initialisierung empfangen werden, werden nicht garantiert zugestellt. Stellen Sie sicher, dass das SDK initialisiert ist, bevor Sie versuchen, diese Kanäle anzuzeigen.
{% endalert %}

## Ressourcen-Bundles und SPM-Integration {#resource-bundles-and-spm-integration}

### Warum sehe ich einen Laufzeitfehler wegen fehlendem `braze-swift-sdk_BrazeUI.bundle`? {#why-am-i-seeing-a-runtime-error-about-missing-braze-swift-sdk_brazeuibundle}

Dies ist kein bekannter SDK-Fehler und liegt wahrscheinlich an einer fehlerhaften Integrationskonfiguration. Ab Swift SDK 12.0.0 enthalten statische XCFrameworks Ressourcen direkt, anstatt sich auf externe Ressourcen-Bundles zu stützen.

### Welche SPM/Xcode/Archiv-Anforderungen gelten für die Ressourceneinbettung? {#what-are-the-spmxcodearchive-requirements-for-resource-embedding}

Ab Swift SDK 12.0.0 müssen Sie **Embed & Sign** für die Braze XCFrameworks in Ihren Xcode-Projekteinstellungen auswählen – dies gilt sowohl für statische als auch für dynamische Varianten. Dies ist die häufigste Ursache für fehlende Bundle-Fehler beim Archivieren oder Veröffentlichen.

### Wie überschreibe ich Ressourcen-Bundles für nicht standardmäßige Build-Systeme? {#how-do-i-override-resource-bundles-for-non-standard-build-systems}

Für nicht standardmäßige Build-Systeme (Tuist, Bazel, Buck, CI) verwenden Sie die genehmigten Override-APIs:

- `BrazeKit.overrideResourcesBundle` (beachten Sie den Plural „Resources“)
- `BrazeUI.overrideResourcesBundle` (beachten Sie den Plural „Resources“)

Der Singular `overrideResourceBundle` wurde in Swift SDK 8.1.0 als veraltet markiert und sollte nicht mehr verwendet werden.

## Nutzer:innen-Identität und Push-Token {#user-identity-and-push-tokens}

### Gibt es eine Validierungscheckliste zur Beibehaltung von Profilen, Gerätezuordnungen und Push-Token? {#is-there-a-validation-checklist-for-preserving-profiles-device-associations-and-push-tokens}

Es gibt keine offizielle migrationsspezifische Checkliste in der Dokumentation. Wir empfehlen, die folgenden Validierungsschritte durchzuführen:

1. Bestätigen Sie, dass `registerDeviceToken` oder die Push-Automatisierung nach der Migration korrekt eingerichtet ist.
2. Überprüfen Sie die Anzahl der Push-registrierten Nutzer:innen im Dashboard vor und nach dem Rollout.
3. Prüfen Sie stichprobenartig einige spezifische externe IDs, um zu bestätigen, dass die Gerätezuordnungen intakt bleiben.

### Garantiert `changeUser`, dass Push-Token dem neuen Nutzerprofil folgen? {#does-changeuser-guarantee-that-push-tokens-follow-the-new-user}

Es gibt keine explizite schriftlich dokumentierte Garantie. Die Designabsicht ist jedoch, dass Push-Token dem Gerät folgen, nicht den Nutzer:innen. Der Aufruf von `changeUser` sollte das vorhandene Geräte-Token mit dem neuen Nutzerprofil neu verknüpfen. Sie sollten `changeUser` testen, das Dashboard überprüfen und bestätigen, dass das Token im neuen Profil erscheint, bevor Sie einen Massen-Rollout durchführen.