---
nav_title: Google Tag Manager
article_title: Google Tag Manager for iOS
platform: iOS
page_order: 7
description: "この記事では、Google Tag Managerの初期化、設定、およびiOSアプリへの実装方法について説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Google Tag Manager for iOS {#google-tag-manager-for-ios}

## SDKの初期化 {#initializing-ios-google-tag-provider}

Braze iOS SDKは、[Google Tag Manager](https://tagmanager.google.com/)で設定されたタグによって初期化および制御することができます。

Google Tag Managerを使用する前に、まず[SDKの初期設定]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)を行ってください。

## Google Tag Managerの設定 {#configuring-ios-google-tag-manager}

この例では、ユーザーが曲を聴いている間に別のイベントをロギングする必要がある音楽ストリーミングアプリを想定しています。Google Tag Manager for iOSを使用して、どのサードパーティベンダーがこのイベントを受信するかをコントロールし、Braze固有のタグを作成できます。

### カスタムイベント {#custom-events}

カスタムイベントは、`logEvent` に設定した `actionType` によってログに記録されます。この例のBrazeカスタムタグプロバイダーは、`eventName` を使用してカスタムイベント名を設定することを想定しています。

最初に、`played song` である「イベント名」を検索するトリガーを作成します。

![「eventName」が「played song」である場合に一部のイベントに対してトリガーするよう設定されたGoogle Tag Managerのカスタムトリガー。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

次に、新しいタグ（「Function Call」とも呼ばれます）を作成し、この記事で後述する[カスタムタグプロバイダー](#adding-ios-google-tag-provider)のクラスパスを入力します。

このタグは、先ほど作成した `played song` イベントをロギングするとトリガーされます。

サンプルタグのカスタムパラメーター（キーと値のペア）では、`eventName` を `played song` に設定しました。これが、Brazeにロギングされるカスタムイベント名になります。

{% alert important %}
カスタムイベントの送信時に、`actionType` を `logEvent` に設定し、次の例のように `eventName` の値を設定します。

この例のカスタムタグプロバイダーは、これらのキーを使用して、Google Tag Managerからデータを受信した際に実行するアクションとBrazeに送信するイベント名を決定します。
{% endalert %}

![classpathフィールドと、キーと値のペアフィールドを含むGoogle Tag Managerのタグ。このタグは、以前に作成された「再生された曲」トリガーでトリガーされるように設定されています。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

また、追加のキーと値のペア引数をタグに含めることもできます。この引数は、カスタムイベントプロパティとしてBrazeに送信されます。`eventName` および `actionType` は、カスタムイベントプロパティでは無視されません。次のサンプルタグでは、`genre` を渡します。これは、Google Tag Managerでタグ変数を使用して定義されており、アプリでロギングしたカスタムイベントから取得されます。

`genre` イベントプロパティは、「Firebase - Event Parameter」変数としてGoogle Tag Managerに送信されます。Google Tag Manager for iOSでは、Firebaseがデータレイヤーとして使用されるためです。

![「genre」が「Braze - Played Song Event」タグのイベントパラメーターとして追加されるGoogle Tag Managerの変数。]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

最後に、ユーザーがアプリで曲を再生すると、タグのトリガー名 `played song` と一致するFirebase分析イベント名を使用し、FirebaseとGoogle Tag Managerを介してイベントがロギングされます。

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### カスタム属性のロギング {#logging-custom-attributes}

カスタム属性は、`customAttribute` に設定された `actionType` を介して設定されます。Brazeカスタムタグプロバイダーは、カスタム属性のキーと値が `customAttributeKey` および `customAttributeValue` を介して設定されることを想定しています。

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favorite song",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### changeUserの呼び出し {#calling-changeuser}

`changeUser()` の呼び出しは、`changeUser` に設定された `actionType` を介して行われます。Brazeカスタムタグプロバイダーは、BrazeユーザーIDがタグ内のキーと値のペア `externalUserId` を介して設定されることを想定しています。

{% tabs %}
{% tab OBJECTIVE-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}
{% endtabs %}

## Braze SDKカスタムタグプロバイダー {#adding-ios-google-tag-provider}

タグとトリガーが設定されたら、iOSアプリにGoogle Tag Managerを実装する必要もあります。これについては、Googleの[ドキュメント](https://developers.google.com/tag-manager/ios/v5/)に記載されています。

Google Tag Managerがアプリにインストールされたら、カスタムタグプロバイダーを追加し、Google Tag Manager内で設定したタグに基づいてBraze SDKメソッドを呼び出します。

ファイルへの「Class Path」を必ず書き留めておいてください。[Google Tag Manager](https://tagmanager.google.com/)コンソールでタグを設定するときに入力する内容です。

この例は、カスタムタグプロバイダーを構築する多くの方法の1つを示しています。ここでは、GTMタグから送信されたキーと値のペア `actionType` に基づいて、呼び出すBraze SDKメソッドを決定します。

この例でサポートされている `actionType` は `logEvent`、`customAttribute`、`changeUser` ですが、タグプロバイダーによるGoogle Tag Managerからのデータの処理方法を変更することもできます。

以下のコードを `BrazeGTMTagManager.h` ファイルに追加します。

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

以下のコードを `BrazeGTMTagManager.m` ファイルに追加します。

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