---
nav_title: その他のSDKカスタマイズ
article_title: iOS向けのその他のSDKカスタマイズ
platform: iOS
description: "この参照記事では、ログレベル、IDFA収集、その他のカスタマイズなどのSDKカスタマイズについて説明します。"
page_order: 3

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# その他のSDKカスタマイズ {#other-sdk-customizations}

## Brazeログレベル {#braze-log-level}

Braze iOS SDKのデフォルトのログレベルは最小（次の表では `8`）です。このレベルではほとんどのロギングが抑制されるため、本番リリースのアプリケーションで機密情報がログに記録されることはありません。

次の使用可能なログレベルのリストを参照してください。

### ログレベル {#log-levels}

| レベル    | 説明 |
|----------|-------------|
| 0        | 詳細。すべてのログ情報がiOSコンソールに記録されます。  |
| 1        | デバッグ。デバッグ以上のログ情報がiOSコンソールに記録されます。  |
| 2        | 警告。警告以上のログ情報がiOSコンソールに記録されます。  |
| 4        | エラー。エラー以上のログ情報がiOSコンソールに記録されます。  |
| 8        | 最小限。最小限の情報がiOSコンソールに記録されます。SDKのデフォルト設定です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Log levels" }

### 詳細なログ記録 {#verbose-logging}

ログレベルは、使用可能な任意の値に設定できます。ただし、ログレベルをverbose（`0`）に設定すると、統合に関する問題のデバッグに非常に役立ちます。このレベルは開発環境のみを対象としており、リリースされたアプリケーションでは設定しないでください。詳細なログ記録では、追加のユーザー情報や新しいユーザー情報がBrazeに送信されることはありません。

### ログレベルの設定 {#setting-log-level}

ログレベルはコンパイル時または実行時に割り当てることができます。

{% tabs local %}
{% tab Compile Time %}

`Braze` という名前の辞書を `Info.plist` ファイルに追加します。`Braze` 辞書内で、`LogLevel` 文字列サブエントリを追加し、値を `0` に設定します。

{% alert note %}
Braze iOS SDK v4.0.2より前では、辞書キー `Appboy` を `Braze` の代わりに使用する必要があります。
{% endalert %}

`Info.plist` コンテンツの例:

```
<key>Braze</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

{% endtab %}
{% tab Runtime %}

`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡される `appboyOptions` パラメーター内に `ABKLogLevelKey` を追加します。その値を整数 `0` に設定します。

{% subtabs %}
{% subtab OBJECTIVE-C %}

`````````objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKLogLevelKey] = @(0);
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endsubtab %}
{% subtab swift %}

`````````swift
let appboyOptions: [AnyHashable: Any] = [
  ABKLogLevelKey : 0
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
ログレベルは、Braze iOS SDK v4.4.0以降で実行時にのみ設定できます。それ以前のバージョンのSDKを使用している場合は、代わりにコンパイル時にログレベルを設定してください。
{% endalert %}

{% endtab %}
{% endtabs %}

## オプションのIDFV収集 - Swift {#optional-idfv-collection-swift}

Braze iOS Swift SDKの以前のバージョンでは、IDFV（Identifier for Vendor）フィールドがユーザーのデバイスIDとして自動的に収集されていました。

Swift SDK v5.7.0以降では、IDFVフィールドをオプションで無効にすることができ、代わりにBrazeはランダムなUUIDをデバイスIDとして設定します。詳細については、「[IDFVの収集]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift)」を参照してください。

## オプションのIDFA収集 {#optional-idfa-collection}

IDFA収集はBraze SDK内ではオプションであり、デフォルトでは無効になっています。IDFA収集は、[インストールアトリビューション統合]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/)を利用する場合にのみBraze内で必要になります。IDFAを保存することを選択した場合は、無料で保存されるため、追加の開発作業を行わずに、リリース後すぐにこれらのオプションを利用できます。

そのため、次の基準のいずれかを満たしている場合は、引き続きIDFAを収集することをお勧めします。

- アプリのインストールが以前に配信された広告に起因している
- アプリケーション内のアクションが以前に配信された広告に起因している

### iOS 14.5 AppTrackingTransparency

Appleは、IDFAを収集するためにユーザーが許可プロンプトを通じてオプトインすることを要求しています。

IDFAを収集するには、`ABKIDFADelegate` プロトコルを実装するだけでなく、アプリケーションではApp Tracking Transparencyフレームワークで Appleの `ATTrackingManager` を使用してユーザーから承認を要求する必要があります。詳細については、Appleの[ユーザープライバシーに関する記事](https://developer.apple.com/app-store/user-privacy-and-data-use/)を参照してください。

App Tracking Transparency承認のプロンプトには、識別子の使用法を説明する `Info.plist` エントリが必要です。

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### IDFA収集の実装 {#implementing-idfa-collection}

IDFA収集を実装するには、次のステップに従います。

##### ステップ 1:ABKIDFADelegateを実装する {#step-1-implement-abkidfadelegate}

[`ABKIDFADelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h) プロトコルに準拠したクラスを作成します。

{% tabs %}
{% tab OBJECTIVE-C %}

`````````objc
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

`````````swift
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

##### ステップ 2:Brazeの初期化中にデリゲートを設定する {#step-2-set-the-delegate-during-braze-initialization}

`startWithApiKey:inApplication:withAppboyOptions:` に渡される `appboyOptions` 辞書で、`ABKIDFADelegateKey` キーを `ABKIDFADelegate` 準拠クラスのインスタンスに設定します。

## iOS SDKのおおよそのサイズ {#ios-sdk-size}

iOS SDKフレームワークファイルのおおよそのサイズは30&nbsp;MBで、.ipa（アプリファイルへの追加）のおおよそのサイズは1&nbsp;MB～2&nbsp;MBです。

Brazeは、[アプリのサイズ設定に関するAppleの推奨事項](https://developer.apple.com/library/content/qa/qa1795/_index.html)に従って、SDKが `.ipa` のサイズに与える影響を観察することで、iOS SDKのサイズを測定しています。アプリケーションに追加されるiOS SDKのサイズを計算する場合は、[アプリサイズレポートの取得](https://developer.apple.com/library/content/qa/qa1795/_index.html)に従って、Braze iOS SDKを統合する前と後の `.ipa` のサイズの違いを比較することをお勧めします。App Thinningサイズレポートからサイズを比較する場合は、Thinningされた `.ipa` ファイルのアプリサイズを確認することもお勧めします。ユニバーサル `.ipa` ファイルは、App Storeからダウンロードしてユーザーのデバイスにインストールされたバイナリーよりも大きくなるためです。

{% alert note %}
CocoaPods経由で `use_frameworks!` と統合する場合は、正確なサイズ測定のためにターゲットのビルド設定で `Enable Bitcode = NO` を設定してください。
{% endalert %}