---
nav_title: "通知オプション"
article_title: iOS通知オプション
page_order: 2
page_layout: reference
description: "このリファレンス記事では、クリティカルアラート、サイレント通知、仮プッシュ通知など、iOSの通知オプションについて説明します。"

platform: iOS
channel:
  - push

---

# 通知オプション {#notification-options}

> AppleのiOS 12のリリースに伴い、Brazeは[通知グループ](#notification-groups)、[サイレント通知/仮認証](#provisional-push-authentication--quiet-notifications)、[クリティカルアラート](#critical-alerts)など、いくつかの機能をサポートしています。

## 通知グループ {#notification-groups}

メッセージをカテゴリ分けし、ユーザーの通知トレイでグループ化したい場合は、Brazeを通じてiOSの通知グループ機能を活用できます。

iOSプッシュキャンペーンを作成し、**設定**タブに移動して**通知グループ**ドロップダウンを開きます。

![「設定」タブに「通知グループ」ドロップダウンがあり、「Coupons」の値が選択されている画面。]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

ドロップダウンから通知グループを選択します。通知グループの設定が正しく機能しない場合、またはドロップダウンから**なし**を選択した場合、メッセージはワークスペース内の定義済みユーザー全員に通常どおり自動送信されます。

ここに通知グループが表示されていない場合は、iOSスレッドIDを使用して追加できます。追加したい通知グループごとに1つのiOSスレッドIDが必要です。次に、ドロップダウンの**Manage Notification Groups**をクリックし、表示される**Manage iOS Push Notification Groups**ウィンドウで必要なフィールドに入力して、通知グループに追加します。

![iOSプッシュ通知グループを管理するウィンドウ。]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

iOSプッシュキャンペーンを作成し、コンポーザーの上部を確認します。そこに**Notification Groups**というラベルのドロップダウンが表示されます。

### サマリー引数 {#summary-arguments}

スレッドIDによる通知のグループ化に加えて、Appleでは通知がグループ化された際に表示されるサマリーを編集できます。Brazeユーザーは、プッシュキャンペーンを作成する際に、サマリーカテゴリ、サマリーカウント、サマリー引数を指定できます。

{% alert tip %}
同じスレッドIDを持つ通知が通知トレイでどのようにグループ化されるかは、OSの制御下にあります。iOSは、最適と判断した内容に応じて、同じスレッドIDを持つ通知を個別に表示したり、グループ化して表示したりする場合があります。
{% endalert %}

**プッシュコンポーザー**の**Alert Options**ボックスにチェックを入れます。

次に、キーとして`summary-arg`と`summary-arg-count`を選択し、対応する列にそれらの値を入力します。`summary-arg`に値を設定しない場合、デフォルトで1になります。

### サマリーカテゴリ {#summary-categories}

サマリーカテゴリを使用すると、通知がグループ化された際に表示されるサマリー全体をカスタマイズできます。複数のカテゴリを作成して適用できます。

メッセージでカテゴリを使用するには、以下の例を参考にして開発者と連携して実装してください：

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
SDKの更新は必要ありません。
{% endalert %}

{% alert tip %}
`%u`と`%@`は、それぞれサマリーカウントとサマリー引数のフォーマット文字列です。サマリーが表示される際、これらのプレースホルダーは`summary-count`と`summary-arg`の値に置き換えられます。
{% endalert %}

アプリでの設定が完了したら、**Notification Buttons**ボックスにチェックを入れ、**Enter Pre-registered iOS Category**を選択して、サマリーカテゴリを使用します。

次に、アプリで設定したサマリーカテゴリ識別子を入力します。

### 仮プッシュ認証とサイレント通知 {#provisional-push}

Appleでは、ユーザーが正式に明示的にオプトインする前に、ユーザーの通知センターにサイレントプッシュ通知を送信するオプションをブランドに提供しており、メッセージの価値を早期に示す機会を得ることができます。必要なのは、アプリで[仮プッシュ通知を設定](#set-up-provisional-push-notifications)するだけです。仮プッシュトークンを持つすべてのユーザーがメッセージを受信します。

従来のiOSプッシュトークンとは異なり、仮プッシュトークンは「お試しパス」として機能し、ユーザーがAppleのネイティブプッシュオプトインプロンプトを見てクリックする前に、ブランドが新規ユーザーにリーチできるようにします。この機能により、プッシュ通知は新規ユーザーの通知トレイに直接配信され、今後の通知を「保持」または「オフにする」オプションが表示されます。「オプトイン」の体験ではなく、「オプトアウト」に近い体験をユーザーに提供します。

{% alert tip %}
仮認証はオプトイン率を大幅に向上させる可能性がありますが、ユーザーがメッセージに価値を感じる場合に限ります。[ユーザーセグメンテーション]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/)、[ロケーションターゲティング]({{site.baseurl}}/user_guide/audience/locations_and_geofences/)、[パーソナライゼーション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)機能を活用して、適切なユーザーが適切なタイミングでこれらの「お試し」通知を受け取れるようにしてください。その後、プッシュ通知がアプリ体験に価値を加えることを理解したユーザーに、完全なオプトインを促すことができます。
{% endalert %}

ユーザーがどちらのオプションを選択しても、適切なトークンまたは[サブスクリプションステータス]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/)がユーザープロファイルの**エンゲージメント**タブにある[連絡先設定]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#engagement-tab)に追加されます。

![プッシュ購読中ステータスが表示された連絡先設定。]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)を使用して、仮認証されているかどうかに基づいてユーザーをターゲットにできます。

![セグメントの詳細パネルに、ユーザーをターゲットにするためのサンプルセグメントフィルター「Provisionally Authorized on iOS Stopwatch (iOS) is true」が表示されている画面。]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
ユーザーが仮プッシュを「オフにする」ことを選択した場合、それ以降の仮プッシュメッセージは表示されなくなります。この機能を使用して送信するメッセージの内容と頻度には十分注意してください。
{% endalert %}

{% alert important %}
追加のプッシュプロンプトや[アプリ内プッシュプライマー](https://www.braze.com/resources/glossary/priming-for-push/)（プッシュ通知へのオプトインを促すアプリ内メッセージ）を使用している場合は、Brazeの担当者に追加のガイダンスについてお問い合わせください。
{% endalert %}

#### 仮プッシュ通知の設定 {#set-up-provisional-push-notifications}

Brazeでは、Braze iOS SDKの実装内のトークン登録スニペットでコードを更新することで、仮認証に登録できます。以下のスニペットを例として使用してください（開発者に送信するか、[統合プロセス中に仮プッシュ認証を実装]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)してもらってください）。

{% alert warning %}
仮プッシュ認証の実装はiOS 12以降のみをサポートしており、デプロイメントターゲットがそれ以前の場合はエラーが発生します。詳細については、[こちらの詳細な実装ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)をご覧ください。
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### 中断レベル（iOS 15以降） {#interruption-level}

iOS 15の新しい集中モードにより、ユーザーはアプリの通知がサウンドやバイブレーションで「中断」するタイミングをより細かく制御できるようになりました。

![iOSの通知設定ページ。通知が即時配信で有効になっており、時間的制約のある通知が有効になっている画面。]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

アプリは、通知の緊急度に基づいて、通知に含める中断レベルを指定できるようになりました。

iOSプッシュ通知の中断レベルを変更するには、**Settings**タブを選択し、**Interruption Level**ドロップダウンメニューから希望のレベルを選択します。

![中断レベルを選択するドロップダウン。]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

この機能にはSDKの最小バージョン要件はありませんが、iOS 15以降を実行しているデバイスにのみ適用されます。

ユーザーが最終的に集中モードを制御する立場にあることに留意してください。時間的制約のある通知が配信されても、ユーザーは集中モードを突破できないアプリを指定できます。

中断レベルとその説明については、以下の表を参照してください。

| 中断レベル | 説明 | 使用するタイミング | 集中モードの突破 |
|--|--|--|--|
| [パッシブ](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive) | サウンド、バイブレーション、画面の点灯なしで通知を送信します。 | 即時の注意を必要としない通知。 | いいえ |
| [アクティブ](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active)（デフォルト） | ユーザーが集中モードでない場合にのみ、サウンド、バイブレーション、画面の点灯を行います。 | ユーザーが集中モードを有効にしていない限り、即時の注意を必要とする通知。 | いいえ |
| [時間的制約あり](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive) | 集中モード中でもサウンド、バイブレーション、画面の点灯を行います。これには、Xcodeでアプリに**Time Sensitive Notifications capability**を追加する必要があります。 | ライドシェアや配達通知など、集中モードに関係なくユーザーに通知すべきタイムリーな通知。 | はい |
| [クリティカル](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical) | 電話の**おやすみモード**スイッチが有効になっていても、サウンド、バイブレーション、画面の点灯を行います。これには[Appleによる明示的な承認が必要です](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/)。 | 悪天候や安全警報などの緊急事態。 | はい |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 関連性スコア（iOS 15以降） {#relevance-score}

![「Your Evening Summary」というタイトルのiOS通知サマリーに3つの通知が表示されている画面。]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15では、1日を通じて指定した時間に複数の通知をダイジェストグループとしてスケジュールする新しい方法もユーザーに提供されています。これは、即時の注意を必要としない通知による1日中の絶え間ない中断を防ぐためのものです。

アプリは**Relevance Score**を設定することで、どのプッシュ通知が最も関連性が高いかを指定できます。Appleはこのスコアを使用して、スケジュールされた通知サマリーにどの通知を表示するかを決定し、残りの通知はユーザーがサマリーをクリックした際に利用可能になります。

すべての通知は、ユーザーの通知センターで引き続きアクセスできます。

iOS通知の関連性スコアを設定するには、**Settings**タブで`0.0`から`1.0`の間の値を入力します。たとえば、最も重要なメッセージは`1.0`で送信し、中程度の重要度のメッセージは`0.5`で送信します。

![関連性スコア「0.5」。]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

この機能にはSDKの最小バージョン要件はありませんが、iOS 15以降を実行しているデバイスにのみ適用されます。

さまざまなメッセージタイプの最大メッセージ長の詳細については、以下のリソースを参照してください：

- [画像とテキストの仕様]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)
- [iOS文字数ガイドライン]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/#character-count)