---
nav_title: Autres personnalisations du SDK
article_title: Autres personnalisations du SDK pour iOS
platform: iOS
description: "Cet article de référence couvre les personnalisations du SDK telles que le niveau de journalisation, la collecte d'IDFA et d'autres personnalisations."
page_order: 3

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Autres personnalisations du SDK {#other-sdk-customizations}

## Niveau de journalisation de Braze {#braze-log-level}

Le niveau de journalisation par défaut du SDK Braze pour iOS est minimal, soit `8` dans le tableau suivant. Ce niveau supprime la majeure partie de la journalisation afin qu'aucune information sensible ne soit consignée dans une application publiée en production.

Consultez la liste suivante des niveaux de journalisation disponibles :

### Niveaux de journalisation {#log-levels}

| Niveau   | Description |
|----------|-------------|
| 0        | Prolixe. Toutes les informations de journalisation seront consignées dans la console iOS.  |
| 1        | Débogage. Les informations de débogage et de niveau supérieur seront consignées dans la console iOS.  |
| 2        | Avertissement. Les informations d'avertissement et de niveau supérieur seront consignées dans la console iOS.  |
| 4        | Erreur. Les informations d'erreur et de niveau supérieur seront consignées dans la console iOS.  |
| 8        | Minimal. Les informations minimales seront consignées dans la console iOS. Paramètre par défaut du SDK. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveaux de journalisation" }

### Journalisation prolixe {#verbose-logging}

Vous pouvez configurer le niveau de journalisation sur n'importe quelle valeur disponible. Cependant, définir le niveau de journalisation sur prolixe, soit `0`, peut s'avérer très utile pour déboguer les problèmes liés à votre intégration. Ce niveau est uniquement destiné aux environnements de développement et ne doit pas être activé dans une application publiée. La journalisation prolixe n'enverra aucune information supplémentaire ou nouvelle sur l'utilisateur à Braze.

### Réglage du niveau de journalisation {#setting-log-level}

Le niveau de journalisation peut être défini soit au moment de la compilation, soit au moment de l'exécution :

{% tabs local %}
{% tab Compile Time %}

Ajoutez un dictionnaire nommé `Braze` à votre fichier `Info.plist`. À l'intérieur du dictionnaire `Braze`, ajoutez la sous-entrée de type chaîne de caractères `LogLevel` et définissez la valeur sur `0`.

{% alert note %}
Avant le SDK Braze pour iOS v4.0.2, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.
{% endalert %}

Exemple de contenu `Info.plist` :

```
<key>Braze</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

{% endtab %}
{% tab Runtime %}

Ajoutez `ABKLogLevelKey` dans le paramètre `appboyOptions` transmis à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez sa valeur sur l'entier `0`.

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
Le niveau de journalisation ne peut être défini au moment de l'exécution qu'avec le SDK Braze pour iOS v4.4.0 ou version ultérieure. Si vous utilisez une version antérieure du SDK, définissez plutôt le niveau de journalisation au moment de la compilation.
{% endalert %}

{% endtab %}
{% endtabs %}

## Collecte IDFV facultative - Swift {#optional-idfv-collection-swift}

Dans les versions antérieures du SDK Swift iOS de Braze, le champ IDFV (identifiant du fournisseur) était automatiquement collecté en tant qu'ID d'appareil de l'utilisateur.

À partir du SDK Swift v5.7.0, le champ IDFV peut être désactivé de manière facultative et Braze générera à la place un UUID aléatoire en tant qu'ID d'appareil. Pour plus d'informations, reportez-vous à la section [Collecte de l'IDFV]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift).

## Collecte IDFA facultative {#optional-idfa-collection}

La collecte IDFA est facultative dans le SDK Braze et désactivée par défaut. La collecte IDFA n'est requise dans Braze que si vous avez l'intention d'utiliser nos [intégrations d'attribution d'installation]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/). Si vous choisissez de stocker votre IDFA, nous le stockerons gratuitement, afin que vous puissiez profiter de ces options dès leur disponibilité sans travail de développement supplémentaire.

Par conséquent, nous vous recommandons de continuer à collecter l'IDFA si vous remplissez l'un des critères suivants :

- Vous attribuez l'installation de l'application à une publicité déjà diffusée
- Vous attribuez une action dans l'application à une publicité déjà diffusée

### iOS 14.5 AppTrackingTransparency

Apple exige que les utilisateurs donnent leur consentement via une invite d'autorisation pour collecter l'IDFA.

Pour collecter l'IDFA, outre l'implémentation de notre protocole `ABKIDFADelegate`, votre application devra demander l'autorisation de l'utilisateur en utilisant le `ATTrackingManager` d'Apple dans le cadre de transparence du suivi des applications. Pour plus d'informations, reportez-vous à l'article d'Apple sur la [protection de la vie privée des utilisateurs](https://developer.apple.com/app-store/user-privacy-and-data-use/).

L'invite d'autorisation de transparence du suivi des applications nécessite une entrée `Info.plist` pour expliquer votre utilisation de l'identifiant :

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### Implémentation de la collecte IDFA {#implementing-idfa-collection}

Suivez ces étapes pour implémenter la collecte IDFA :

##### Étape 1 : Implémenter ABKIDFADelegate {#step-1-implement-abkidfadelegate}

Créez une classe conforme au protocole [`ABKIDFADelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h) :

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

##### Étape 2 : Définir le délégué lors de l'initialisation de Braze {#step-2-set-the-delegate-during-braze-initialization}

Dans le dictionnaire `appboyOptions` transmis à `startWithApiKey:inApplication:withAppboyOptions:`, définissez la clé `ABKIDFADelegateKey` sur une instance de votre classe conforme à `ABKIDFADelegate`.

## Taille approximative du SDK iOS {#ios-sdk-size}

La taille approximative du fichier du framework du SDK iOS est de 30&nbsp;Mo, et la taille approximative du .ipa (ajout au fichier de l'application) est comprise entre 1&nbsp;Mo et 2&nbsp;Mo.

Braze mesure la taille de son SDK iOS en observant l'effet du SDK sur la taille du `.ipa`, conformément aux [recommandations d'Apple sur le dimensionnement des applications](https://developer.apple.com/library/content/qa/qa1795/_index.html). Si vous calculez l'ajout de taille du SDK iOS à votre application, nous vous recommandons de suivre [Obtenir un rapport sur la taille de l'application](https://developer.apple.com/library/content/qa/qa1795/_index.html) pour comparer la différence de taille de votre `.ipa` avant et après l'intégration du SDK Braze pour iOS. Lorsque vous comparez les tailles à partir du rapport d'amincissement des applications, nous vous recommandons également d'examiner les tailles d'applications pour les fichiers `.ipa` allégés, car les fichiers `.ipa` universels seront plus volumineux que les binaires téléchargés depuis l'App Store et installés sur les appareils des utilisateurs.

{% alert note %}
Si vous intégrez via CocoaPods avec `use_frameworks!`, définissez `Enable Bitcode = NO` dans les paramètres de compilation de la cible pour obtenir des tailles précises.
{% endalert %}