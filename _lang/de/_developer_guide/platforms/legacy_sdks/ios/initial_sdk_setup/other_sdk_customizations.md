---
nav_title: Andere SDK-Anpassungen
article_title: Andere SDK-Anpassungen für iOS
platform: iOS
description: "Dieser Referenzartikel beschreibt die Anpassung des SDK, wie z. B. die Protokollstufe, die IDFA-Erfassung und andere Anpassungen."
page_order: 3

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Andere SDK-Anpassungen {#other-sdk-customizations}

## Braze-Protokollstufe {#braze-log-level}

Die Standard-Protokollstufe für das Braze iOS SDK ist minimal oder `8` im folgenden Chart. Diese Stufe unterdrückt den größten Teil der Protokollierung, sodass in einer für die Produktion freigegebenen Anwendung keine sensiblen Informationen protokolliert werden.

Die verfügbaren Protokollstufen sind der folgenden Liste zu entnehmen:

### Protokollstufen {#log-levels}

| Ebene    | Beschreibung |
|----------|-------------|
| 0        | Ausführlich. Alle Protokollinformationen werden in der iOS-Konsole protokolliert.  |
| 1        | Debug. Debug- und höhere Protokollinformationen werden in der iOS-Konsole protokolliert.  |
| 2        | Warnung. Warnungen und höhere Protokollinformationen werden in der iOS-Konsole protokolliert.  |
| 4        | Fehler. Fehler- und höhere Protokollinformationen werden in der iOS-Konsole protokolliert.  |
| 8        | Minimal. Minimale Informationen werden in der iOS-Konsole protokolliert. Die Standardeinstellung des SDK. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Protokollstufen" }

### Ausführliche Protokollierung {#verbose-logging}

Sie können die Protokollstufe auf jeden verfügbaren Wert einstellen. Die Einstellung der Protokollstufe auf „Ausführlich“ oder `0` kann jedoch bei der Fehlersuche in Ihrer Integration sehr nützlich sein. Diese Stufe ist nur für Entwicklungsumgebungen vorgesehen und sollte nicht in einer veröffentlichten Anwendung gewählt werden. Die ausführliche Protokollierung sendet keine zusätzlichen oder neuen Nutzerinformationen an Braze.

### Einstellung der Protokollstufe {#setting-log-level}

Die Protokollstufe kann entweder zur Kompilierzeit oder zur Laufzeit zugewiesen werden:

{% tabs local %}
{% tab Compile Time %}

Fügen Sie ein Wörterbuch mit dem Namen `Braze` zu Ihrer Datei `Info.plist` hinzu. Fügen Sie im Wörterbuch `Braze` den String-Untereintrag `LogLevel` hinzu und setzen Sie den Wert auf `0`.

{% alert note %}
Vor Braze iOS SDK v4.0.2 muss der Wörterbuchschlüssel `Appboy` anstelle von `Braze` verwendet werden.
{% endalert %}

Beispiel für `Info.plist`-Inhalte:

```
<key>Braze</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

{% endtab %}
{% tab Runtime %}

Fügen Sie `ABKLogLevelKey` im Parameter `appboyOptions` hinzu, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird. Setzen Sie seinen Wert auf die Ganzzahl `0`.

{% subtabs %}
{% subtab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKLogLevelKey] = @(0);
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endsubtab %}
{% subtab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKLogLevelKey : 0
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Zur Laufzeit kann die Protokollstufe nur mit Braze iOS SDK v4.4.0 oder neuer eingestellt werden. Wenn Sie eine frühere SDK-Version verwenden, legen Sie die Protokollstufe stattdessen bei der Kompilierung fest.
{% endalert %}

{% endtab %}
{% endtabs %}

## Optionale IDFV-Erhebung – Swift {#optional-idfv-collection-swift}

In früheren Versionen des Braze iOS Swift SDK wurde das Feld IDFV (Identifier for Vendors) automatisch als Geräte-ID der Nutzer:innen erfasst.

Ab Swift SDK v5.7.0 kann das IDFV-Feld optional deaktiviert werden. Stattdessen setzt Braze eine zufällige UUID als Geräte-ID. Weitere Informationen finden Sie unter [IDFV-Erhebung]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift).

## Optionale IDFA-Erfassung {#optional-idfa-collection}

Die IDFA-Erfassung ist im Braze SDK optional und standardmäßig deaktiviert. Die IDFA-Erfassung ist in Braze nur erforderlich, wenn Sie unsere [Install-Attribution-Integrationen]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/) verwenden möchten. Wenn Sie sich für die Speicherung Ihres IDFA entscheiden, speichern wir ihn kostenlos, sodass Sie die Vorteile dieser Optionen sofort nach der Veröffentlichung ohne zusätzliche Entwicklungsarbeit nutzen können.

Wir empfehlen daher, den IDFA weiterhin zu erfassen, wenn Sie eines der folgenden Kriterien erfüllen:

- Sie ordnen die Installation einer App einer zuvor geschalteten Werbung zu.
- Sie ordnen eine Aktion innerhalb der Anwendung einer zuvor geschalteten Anzeige zu.

### iOS 14.5 AppTrackingTransparency

Apple verlangt eine Genehmigungsabfrage zur IDFA-Erfassung, der die Nutzer:innen aktiv zustimmen müssen.

Zusätzlich zur Implementierung unseres `ABKIDFADelegate`-Protokolls muss Ihre Anwendung zur IDFA-Erfassung auch die Zustimmung der Nutzer:innen über Apples `ATTrackingManager` im App-Tracking-Transparenz-Framework einholen. Weitere Informationen finden Sie in Apples [Artikel zum Datenschutz](https://developer.apple.com/app-store/user-privacy-and-data-use/).

Die Genehmigungsabfrage im Rahmen der App-Tracking-Transparenz erfordert einen `Info.plist`-Eintrag, um Ihre Nutzung des Bezeichners zu erklären:

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### Implementieren der IDFA-Erfassung {#implementing-idfa-collection}

Gehen Sie zur Implementierung der IDFA-Erfassung wie folgt vor:

##### 1. Schritt: ABKIDFADelegate implementieren {#step-1-implement-abkidfadelegate}

Erstellen Sie eine Klasse, die dem Protokoll [`ABKIDFADelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h) entspricht:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
#import "IDFADelegate.h"
#import <AdSupport/ASIdentifierManager.h>
#import <AppTrackingTransparency/AppTrackingTransparency.h>

@implementation IDFADelegate

- (NSString *)advertisingIdentifierString {
  return [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
}

- (BOOL)isAdvertisingTrackingEnabledOrATTAuthorized {
  if (@available(iOS 14, *)) {
    return [ATTrackingManager trackingAuthorizationStatus] == ATTrackingManagerAuthorizationStatusAuthorized;
  }
  return [[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled];
}

@end
```

{% endtab %}
{% tab swift %}

```swift
import Appboy_iOS_SDK
import AdSupport
import AppTrackingTransparency

class IDFADelegate: NSObject, ABKIDFADelegate {
   func advertisingIdentifierString() -> String {
    return ASIdentifierManager.shared().advertisingIdentifier.uuidString
  }

  func isAdvertisingTrackingEnabledOrATTAuthorized() -> Bool {
    if #available(iOS 14, *) {
      return ATTrackingManager.trackingAuthorizationStatus ==  ATTrackingManager.AuthorizationStatus.authorized
    }
    return ASIdentifierManager.shared().isAdvertisingTrackingEnabled
  }
}
```
{% endtab %}
{% endtabs %}

##### 2. Schritt: Delegaten während der Braze-Initialisierung festlegen {#step-2-set-the-delegate-during-braze-initialization}

Legen Sie in dem an `startWithApiKey:inApplication:withAppboyOptions:` übergebenen Wörterbuch `appboyOptions` den Schlüssel `ABKIDFADelegateKey` auf eine Instanz Ihrer mit `ABKIDFADelegate` konformen Klasse fest.

## Ungefähre Größe des iOS SDK {#ios-sdk-size}

Die ungefähre Größe der iOS-SDK-Framework-Datei beträgt 30&nbsp;MB. Die ungefähre .ipa-Größe (Ergänzung zur App-Datei) liegt zwischen 1&nbsp;MB und 2&nbsp;MB.

Braze misst die Größe unseres iOS SDK, indem es die Auswirkungen des SDK auf die `.ipa`-Größe beobachtet – gemäß Apples [Empfehlungen zur App-Größe](https://developer.apple.com/library/content/qa/qa1795/_index.html). Wenn Sie den Größenzuwachs Ihrer Anwendung durch das iOS SDK berechnen, empfehlen wir Ihnen, [einen Bericht zur App-Größe abzurufen](https://developer.apple.com/library/content/qa/qa1795/_index.html), um den Größenunterschied der `.ipa` vor und nach der Integration des Braze iOS SDK zu vergleichen. Wenn Sie die Größen aus dem Bericht zur App-Ausdünnung vergleichen, empfehlen wir Ihnen, auch die App-Größen für ausgedünnte `.ipa`-Dateien zu betrachten, da die universellen `.ipa`-Dateien größer sind als die Binärdateien, die aus dem App Store heruntergeladen und auf den Geräten der Nutzer:innen installiert werden.

{% alert note %}
Wenn Sie über CocoaPods mit `use_frameworks!` integrieren, stellen Sie `Enable Bitcode = NO` in den Build-Einstellungen des Ziels ein, um eine genaue Größenbestimmung zu erreichen.
{% endalert %}