---
nav_title: iOS 15 アップグレードガイド
article_title: iOS 15 SDKアップグレードガイド
page_order: 7
platform: iOS
description: "このリファレンス記事では、新しい iOS 15 OSの更新、必要なSDKの更新、および新機能について説明します。"
hidden: true
noindex: true
---

# iOS 15 SDKアップグレードガイド {#ios-15-sdk-upgrade-guide}

> このガイドでは、iOS 15 (WWDC21) で導入された変更点と、Braze iOS SDK統合に必要なアップグレードステップについて説明します。iOS 15の新しい更新の完全なリストについては、Appleの[iOS 15 リリースノート](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes)を参照してください。


## UIナビゲーションの透明性に関する変更 {#transparency-changes-to-ui-navigations}

iOSベータ版の年次テストの一環として、特定のUIナビゲーションバーが不透明ではなく透明に表示されるAppleによる変更を確認しました。これは、Content Cards用のBrazeデフォルトUIを使用している場合、またはWebディープリンクが別のブラウザアプリではなくアプリ内で開かれている場合に、iOS 15で表示されます。

iOS 15でのこの視覚的な変更を回避するために、ユーザーが新しいiOS 15オペレーティングシステムにアップグレードを開始する前に、できるだけ早く[Braze iOS SDK v4.3.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2)にアップグレードすることを強くお勧めします。

## 新しい通知設定 {#notification-settings}

iOS 15では新しい通知機能が導入され、ユーザーが1日を通して集中力を保ち、頻繁な中断を避けることができるようになりました。これらの新機能のサポートを提供できることを嬉しく思います。これらの機能は追加のSDKアップグレードを必要とせず、iOS 15デバイスのユーザーにのみ適用されます。

### フォーカスモード {#focus-mode}

iOS 15のユーザーは「フォーカスモード」を作成できるようになりました。これは、フォーカスを中断して目立つように表示する通知を指定するためのカスタムプロファイルです。

![]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### 割り込みレベル {#interruption-levels}

iOS 15では、プッシュ通知は次の4つの割り込みレベルのいずれかで送信できます。

* **パッシブ**（新規）- サウンドなし、バイブレーションなし、画面のスリープ解除なし、フォーカス設定の突破なし。
* **アクティブ**（デフォルト）- サウンド、バイブレーション、画面のスリープ解除を許可し、フォーカス設定の突破は許可しません。
* **時間的制約**（新規）- サウンド、バイブレーション、画面のスリープ解除を許可し、許可されている場合はシステムコントロールを突破できます。
* **重大** - サウンド、バイブレーション、画面のスリープ解除を許可し、システムコントロールを突破し、サイレントスイッチをバイパスできます。

iOSプッシュでこのオプションを設定する方法の詳細については、[iOS通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level)を参照してください。

### 通知の概要 {#notification-summary}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15では、ユーザーは（オプションで）1日の中で特定の時間を選択して、通知の概要を受け取ることができます。即時の注意を必要としない通知（「パッシブ」として送信されたり、ユーザーがフォーカスモード中に送信されたりするもの）は、1日を通じて絶えず中断されないようにグループ化されます。

送信する通知ごとに、「関連性スコア」を指定して、どの通知を概要の先頭に表示するかをコントロールできるようになります。

通知の「関連性スコア」の設定方法については、[iOS通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score)を参照してください。

## 位置情報ボタン {#location-buttons}

iOS 15では、ユーザーがアプリ内で位置情報へのアクセスを一時的に許可する新しい便利な方法が導入されています。

新しい位置情報ボタンは、既存の「1度のみ許可」権限を基にしており、同じセッションで複数回クリックするユーザーに繰り返しプロンプトを表示することはありません。

詳細については、今年の世界開発者会議（WWDC）でのAppleの動画[Meet the Location Button](https://developer.apple.com/videos/play/wwdc2021/10102/)をご覧ください。

{% alert tip %}
この機能により、ユーザーに権限を要求する追加の機会が得られます。iOS 15より前に位置情報の許可を拒否したことがあるユーザーには、位置情報ボタンをクリックした際に、拒否状態から権限をリセットする最後の機会としてプロンプトが表示されます。
{% endalert %}

### Brazeで位置情報ボタンを利用する {#using-location-buttons-with-braze}

Brazeで位置情報ボタンを使用する場合、追加の統合は必要ありません。アプリは、通常どおり（権限が付与されたら）ユーザーの位置情報を渡し続ける必要があります。

Appleによると、すでにバックグラウンドでの位置情報へのアクセスを共有しているユーザーについては、iOS 15にアップグレードした後も「アプリの使用中」オプションで引き続きそのレベルの権限が付与されます。

## Appleメール {#mail}

今年、Appleはメールのトラッキングとプライバシーに関する多くの更新を発表しました。詳細については、[ブログ投稿](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature)をご覧ください。

## SafariのIPアドレスによる位置情報 {#safari-ip-address-location}

iOS 15では、ユーザーはIPアドレスから特定された位置情報を匿名化または一般化するようにSafariを設定できます。ロケーションベースのターゲティングまたはセグメンテーションを使用する場合は、このことに留意してください。