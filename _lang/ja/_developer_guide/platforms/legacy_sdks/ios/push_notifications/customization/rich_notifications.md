---
nav_title: リッチ通知の作成
article_title: iOS向けリッチプッシュ通知
platform: iOS
page_order: 3
description: "このリファレンス記事では、iOSアプリケーションにリッチプッシュ通知を実装する方法について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS 10リッチプッシュ通知 {#ios-10-rich-notifications}

iOS 10では、画像、GIF、動画を含むプッシュ通知を送信する機能が導入されました。この機能を有効にするには、クライアントが`Service Extension`を作成する必要があります。これは、プッシュペイロードが表示される前に変更を可能にする新しいタイプの拡張機能です。

## サービス拡張の作成 {#creating-a-service-extension}

[`Notification Service Extension`](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension)を作成するには、Xcodeで**File > New > Target**に移動し、**Notification Service Extension**を選択します。

![リッチ通知用のNotification Service Extensionを作成するXcodeのターゲット選択画面]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

アプリケーションに拡張機能を埋め込むように**Embed In Application**が設定されていることを確認します。

## サービス拡張の設定 {#setting-up-the-service-extension}

`Notification Service Extension`は、アプリにバンドルされる独自のバイナリです。[Apple Developer Portal](https://developer.apple.com)で独自のアプリIDとプロビジョニングプロファイルを使用して設定する必要があります。

`Notification Service Extension`のバンドルIDは、メインアプリターゲットのバンドルIDとは異なる必要があります。たとえば、アプリのバンドルIDが`com.company.appname`の場合、サービス拡張には`com.company.appname.AppNameServiceExtension`を使用できます。

### Brazeと連携するようにサービス拡張を設定する {#configuring-the-service-extension-to-work-with-braze}

Brazeは、リッチコンテンツの設定、ダウンロード、表示に使用する`ab`キーの下にあるAPNsペイロードで添付ペイロードを送信します。以下に例を示します。

```json
{
  "ab" :
    {
    ...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

関連するペイロード値は次のとおりです。

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

Brazeペイロードで手動でプッシュ通知を表示するには、`AppboyAPNSDictionaryAttachmentURLKey`の下の値からコンテンツをダウンロードし、`AppboyAPNSDictionaryAttachmentTypeKey`キーの下に格納されているファイルタイプのファイルとして保存し、通知の添付ファイルに追加します。

### サンプルコード {#example-code}

サービス拡張は、Objective-CまたはSwiftで記述できます。

Objective-Cサンプルコードを使用するには、`Notification Service Extension`ターゲットの自動生成された`NotificationService.m`の内容をAppboyの[`NotificationService.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m)の内容に置き換えます。

Swiftサンプルコードを使用するには、`Notification Service Extension`ターゲットの自動生成された`NotificationService.swift`の内容をAppboyの[`NotificationService.swift`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift)の内容に置き換えます。

## ダッシュボードでリッチプッシュ通知を作成する {#creating-a-rich-notification-in-your-dashboard}

Brazeダッシュボードでリッチプッシュ通知を作成するには、iOSプッシュを作成し、画像またはGIFを添付するか、画像、GIF、または動画をホストするURLを指定します。アセットはプッシュ通知の受信時にダウンロードされるため、コンテンツをホスティングしている場合は、リクエストが大規模に同期的に急増することを想定する必要があります。

サポートされているファイルタイプとサイズのリストについては、[`unnotificationattachment`](https://developer.apple.com/reference/usernotifications/unnotificationattachment)を参照してください。