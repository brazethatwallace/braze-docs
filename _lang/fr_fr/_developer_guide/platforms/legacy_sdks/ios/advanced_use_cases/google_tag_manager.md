---
nav_title: Google Tag gestionnaire
article_title: Google Tag gestionnaire pour iOS
platform: iOS
page_order: 7
description: "Cet article explique comment initialiser, configurer et déployer Google Tag gestionnaire dans votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Google Tag gestionnaire pour iOS {#google-tag-manager-for-ios}

## Initialisation du SDK {#initializing-ios-google-tag-provider}

Le SDK iOS de Braze peut être initialisé et contrôlé par des balises configurées dans [Google Tag gestionnaire](https://tagmanager.google.com/).

Avant d'utiliser Google Tag gestionnaire, veillez à suivre notre [configuration initiale du SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview).

## Configuration de votre Google Tag gestionnaire {#configuring-ios-google-tag-manager}

Dans cet exemple, nous allons simuler une application de streaming musical qui souhaite journaliser différents événements au fur et à mesure que les utilisateurs écoutent des chansons. À l'aide de Google Tag gestionnaire pour iOS, nous pouvons contrôler quels fournisseurs tiers reçoivent cet événement et créer des balises spécifiques à Braze.

### Événements personnalisés {#custom-events}

Les événements personnalisés sont enregistrés avec `actionType` réglé sur `logEvent`. Le fournisseur d'étiquettes personnalisées de Braze, dans notre exemple, attend que le nom de l'événement personnalisé soit défini à l'aide de `eventName`.

Pour commencer, créez un déclencheur qui recherche un « nom de l'événement » qui équivaut à `played song`.

![Un déclencheur personnalisé dans Google Tag Manager défini pour déclencher certains événements lorsque « nom de l'événement » est égal à « played song ».]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Ensuite, créez une nouvelle étiquette (« Appel de fonction ») et saisissez le chemin de classe de votre [fournisseur d'étiquettes personnalisées](#adding-ios-google-tag-provider) décrit plus loin dans cet article.

Cette étiquette sera déclenchée lorsque vous enregistrerez l'événement `played song` que nous venons de créer.

Dans les paramètres personnalisés de notre exemple d'étiquette (paires clé-valeur), nous avons défini `eventName` sur `played song`, qui sera le nom de l'événement personnalisé enregistré dans Braze.

{% alert important %}
Lorsque vous envoyez un événement personnalisé, définissez `actionType` sur `logEvent` et définissez une valeur pour `eventName` comme illustré dans l'exemple suivant.

Le fournisseur d'étiquettes personnalisées dans notre exemple utilisera ces clés pour déterminer l'action à effectuer et le nom de l'événement à envoyer à Braze lorsqu'il reçoit des données de Google Tag gestionnaire.
{% endalert %}

![Une étiquette dans Google Tag Manager avec des champs de chemin de classe et de paires clé-valeur. Cette étiquette est définie pour se déclencher avec le déclencheur « played song » créé précédemment.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Vous pouvez également inclure des arguments de paires clé-valeur supplémentaires à l'étiquette, qui seront envoyés en tant que propriétés d'événement personnalisé à Braze. `eventName` et `actionType` ne seront pas ignorés pour les propriétés d'événement personnalisé. Dans l'exemple d'étiquette suivant, nous allons transmettre `genre`, qui a été défini à l'aide d'une variable d'étiquette dans Google Tag gestionnaire, issue de l'événement personnalisé que nous avons enregistré dans notre application.

La propriété d'événement `genre` est envoyée à Google Tag gestionnaire en tant que variable « Firebase - paramètre de l'événement », étant donné que Google Tag gestionnaire pour iOS utilise Firebase comme couche de données.

![Une variable dans Google Tag Manager où « genre » est ajouté en tant que paramètre de l'événement pour l'étiquette « Braze - Played Song Event ».]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Enfin, lorsqu'un utilisateur joue une chanson dans notre application, nous enregistrons un événement via Firebase et Google Tag gestionnaire en utilisant le nom d'événement d'analyse Firebase qui correspond au nom de déclencheur de notre étiquette, `played song` :

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Enregistrement des attributs personnalisés {#logging-custom-attributes}

Les attributs personnalisés sont définis via un `actionType` réglé sur `customAttribute`. Le fournisseur d'étiquettes personnalisées de Braze attend que la paire clé-valeur de l'attribut personnalisé soit définie via `customAttributeKey` et `customAttributeValue` :

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favorite song",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Appeler changeUser {#calling-changeuser}

Les appels à `changeUser()` sont effectués via un `actionType` réglé sur `changeUser`. Le fournisseur d'étiquettes personnalisées de Braze attend que l'ID utilisateur Braze soit défini via une paire clé-valeur `externalUserId` dans votre étiquette :

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}
{% endtabs %}

## Fournisseur d'étiquettes personnalisées du SDK Braze {#adding-ios-google-tag-provider}

Une fois les étiquettes et les déclencheurs configurés, vous devrez également implémenter Google Tag gestionnaire dans votre application iOS, comme décrit dans la [documentation](https://developers.google.com/tag-manager/ios/v5/) de Google.

Une fois Google Tag gestionnaire installé dans votre application, ajoutez un fournisseur d'étiquettes personnalisées pour appeler les méthodes du SDK Braze en fonction des étiquettes que vous avez configurées dans Google Tag gestionnaire.

Veillez à noter le « chemin de classe » du fichier : c'est ce que vous indiquerez lorsque vous configurerez une étiquette dans la console de [Google Tag gestionnaire](https://tagmanager.google.com/).

Cet exemple montre l'une des nombreuses façons de structurer votre fournisseur d'étiquettes personnalisées, dans laquelle nous déterminons quelle méthode du SDK Braze appeler en fonction de la paire clé-valeur `actionType` envoyée depuis l'étiquette GTM.

Les `actionType` que nous avons pris en charge dans notre exemple sont `logEvent`, `customAttribute` et `changeUser`, mais vous pouvez modifier la manière dont votre fournisseur d'étiquettes gère les données de Google Tag gestionnaire.

Ajoutez le code suivant à votre fichier `BrazeGTMTagManager.h` :

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

{% endtab %}
{% endtabs %}

Et ajoutez le code suivant à votre fichier `BrazeGTMTagManager.m` :

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "Appboy-iOS-SDK/AppboyKit.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventActionType = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeActionType = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserActionType = @"changeUser";
static NSString *const ChangeUserExternalUserId = @"externalUserId";

@implementation BrazeGTMTagManager

- (NSObject *)executeWithParameters:(NSDictionary *)parameters {
  NSMutableDictionary *mutableParameters = [parameters mutableCopy];

  NSString *actionType = mutableParameters[ActionTypeKey];
  if (!actionType) {
    NSLog(@"There is no Braze action type key in this call. Doing nothing.", nil);
    return nil;
  }

  [mutableParameters removeObjectForKey:ActionTypeKey];

  if ([actionType isEqualToString:LogEventActionType]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeActionType]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserActionType]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];

  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                             andStringValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                                 andBOOLValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                              andIntegerValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDoubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Appboy custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [[Appboy sharedInstance].user setCustomAttributeArrayWithKey:customAttributeKey
                                                           array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [[Appboy sharedInstance] changeUser:userId];
}

@end
```

{% endtab %}
{% endtabs %}