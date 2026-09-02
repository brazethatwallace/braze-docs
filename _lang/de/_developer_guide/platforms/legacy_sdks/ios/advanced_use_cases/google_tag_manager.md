---
nav_title: Google Tag Manager:in
article_title: Google Tag Manager:in für iOS
platform: iOS
page_order: 7
description: "Dieser Artikel beschreibt, wie Sie den Google Tag Manager:in initialisieren, konfigurieren und in Ihre iOS-App implementieren."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Google Tag Manager:in für iOS {#google-tag-manager-for-ios}

## Initialisierung des SDK or Software-Development-Kit {#initializing-ios-google-tag-provider}

Das Braze iOS SDK or Software-Development-Kit kann durch Tags, die im [Google Tag Manager:in](https://tagmanager.google.com/) konfiguriert wurden, initialisiert und gesteuert werden.

Bevor Sie Google Tag Manager:in verwenden, müssen Sie zunächst die [SDK or Software-Development-Kit-Ersteinrichtung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) durchführen.

## Konfigurieren Ihres Google Tag Managers {#configuring-ios-google-tag-manager}

In diesem Beispiel tun wir so, als wären wir eine Musik-Streaming-App, die verschiedene Ereignisse protokollieren möchte, während Nutzer:innen Lieder anhören. Mit dem Google Tag Manager:in für iOS können wir steuern, welche unserer Drittanbieter dieses Ereignis erhalten, und Tags speziell für Braze erstellen.

### Angepasste Events {#custom-events}

Angepasste Events werden protokolliert, wenn `actionType` auf `logEvent` eingestellt ist. Der angepasste Tag-Anbieter von Braze erwartet in unserem Beispiel, dass der Name des angepassten Events mit `eventName` festgelegt wird.

Um zu beginnen, erstellen Sie einen Trigger or triggern, der nach einem „Event Name“ sucht, der gleich `played song` ist.

![Ein angepasster Trigger im Google Tag Manager, der für einige Events triggert, wenn „Ereignisname“ gleich „abgespielter Song“ ist.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Als Nächstes erstellen Sie ein neues Tag („Funktionsaufruf“) und geben den Klassenpfad Ihres [angepassten Tag-Anbieters](#adding-ios-google-tag-provider) ein, der weiter unten in diesem Artikel beschrieben wird.

Dieses Tag wird ausgelöst, wenn Sie das soeben erstellte Event `played song` protokollieren.

In den angepassten Parametern (Schlüssel-Wert-Paare) unseres Beispiel-Tags haben wir `eventName` auf `played song` gesetzt – das ist der Name des angepassten Events, der in Braze protokolliert wird.

{% alert important %}
Wenn Sie ein angepasstes Event senden, setzen Sie `actionType` auf `logEvent` und legen Sie einen Wert für `eventName` fest, wie im folgenden Beispiel gezeigt.

Der angepasste Tag-Anbieter in unserem Beispiel verwendet diese Schlüssel, um zu bestimmen, welche Aktion durchgeführt und welcher Event-Name an Braze gesendet werden soll, wenn er Daten vom Google Tag Manager:in erhält.
{% endalert %}

![Ein Tag im Google Tag Manager mit Klassenpfad- und Schlüssel-Wert-Paar-Feldern. Dieses Tag ist so eingestellt, dass es mit dem zuvor erstellten Trigger „played song“ ausgelöst wird.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Sie können dem Tag auch zusätzliche Schlüssel-Wert-Paar-Argumente hinzufügen, die als Event-Eigenschaften des angepassten Events an Braze gesendet werden. `eventName` und `actionType` werden für Event-Eigenschaften angepasster Events nicht ignoriert. Im folgenden Beispiel-Tag übergeben wir `genre`, das über eine Tag-Variable im Google Tag Manager:in definiert wurde und aus dem angepassten Event stammt, das wir in unserer App protokolliert haben.

Die Event-Eigenschaft `genre` wird als Variable „Firebase - Event Parameter“ an den Google Tag Manager:in gesendet, da Google Tag Manager:in für iOS Firebase als Datenebene verwendet.

![Eine Variable im Google Tag Manager, bei der „genre“ als Event-Parameter für das Tag „Braze - Played Song Event“ hinzugefügt wird.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Wenn Nutzer:innen schließlich einen Song in unserer App abspielen, protokollieren wir ein Ereignis über Firebase und den Google Tag Manager:in unter Verwendung des Firebase-Analytics-Event-Namens, der mit dem Trigger or triggern-Namen unseres Tags übereinstimmt: `played song`:

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Angepasste Attribute protokollieren {#logging-custom-attributes}

Angepasste Attribute werden über einen `actionType` gesetzt, der auf `customAttribute` eingestellt ist. Der angepasste Tag-Anbieter von Braze erwartet, dass der Schlüssel-Wert des angepassten Attributs über `customAttributeKey` und `customAttributeValue` gesetzt wird:

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favorite song",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Aufruf von changeUser {#calling-changeuser}

Aufrufe von `changeUser()` erfolgen über einen `actionType`, der auf `changeUser` eingestellt ist. Der angepasste Tag-Anbieter von Braze erwartet, dass die Braze-Nutzer-ID über das Schlüssel-Wert-Paar `externalUserId` in Ihrem Tag festgelegt wird:

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}
{% endtabs %}

## Angepasster Tag-Anbieter für das Braze SDK or Software-Development-Kit {#adding-ios-google-tag-provider}

Wenn die Tags und Trigger or triggern eingerichtet sind, müssen Sie auch den Google Tag Manager:in in Ihrer iOS-App implementieren. Informationen dazu finden Sie in der [Dokumentation](https://developers.google.com/tag-manager/ios/v5/) von Google.

Sobald Google Tag Manager:in in Ihrer App installiert ist, fügen Sie einen angepassten Tag-Anbieter hinzu, um Braze-SDK or Software-Development-Kit-Methoden auf der Grundlage der Tags aufzurufen, die Sie im Google Tag Manager:in konfiguriert haben.

Achten Sie darauf, den „Klassenpfad“ der Datei zu notieren – diesen geben Sie ein, wenn Sie ein Tag in der [Google Tag Manager:in](https://tagmanager.google.com/)-Konsole einrichten.

Dieses Beispiel zeigt eine von vielen Möglichkeiten, Ihren angepassten Tag-Anbieter zu strukturieren. Dabei bestimmen wir anhand des vom GTM-Tag gesendeten Schlüssel-Wert-Paares `actionType`, welche Braze-SDK or Software-Development-Kit-Methode aufgerufen werden soll.

Die `actionType`-Werte, die wir in unserem Beispiel unterstützen, sind `logEvent`, `customAttribute` und `changeUser`. Sie können jedoch ändern, wie Ihr Tag-Anbieter die Daten vom Google Tag Manager:in verarbeitet.

Fügen Sie den folgenden Code in Ihre Datei `BrazeGTMTagManager.h` ein:

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

Und fügen Sie den folgenden Code in Ihre Datei `BrazeGTMTagManager.m` ein:

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