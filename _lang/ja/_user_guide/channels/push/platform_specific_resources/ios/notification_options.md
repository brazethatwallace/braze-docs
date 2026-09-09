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

iOSプッシュキャンペーンを作成し、**設定**タブに移動して**Notification group**ドロップダウンを開きます。

![「設定」タブにある「Notification group」ドロップダウンで「Coupons」が選択されている状態。]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

ドロップダウンからNotification Groupsを選択します。通知グループの設定が正常に機能しない場合、またはドロップダウンから**None**を選択した場合、メッセージは自動的にワークスペース内の定義されたすべてのユーザーに通常通り送信されます。

ここにNotification Groupsが表示されていない場合は、iOS Thread IDを使用して追加できます。追加したいNotification Groupごとに1つのiOS Thread IDが必要です。ドロップダウンの**Manage Notification Groups**をクリックし、表示される**Manage iOS Push Notification Groups**ウィンドウで必須フィールドに入力してNotification Groupsに追加します。

![iOSプッシュ通知グループを管理するウィンドウ。]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

iOSプッシュキャンペーンを作成し、コンポーザーの上部を確認します。そこに**Notification Groups**というラベルのドロップダウンが表示されます。

### サマリー引数 {#summary-arguments}

Thread IDによる通知のグループ化に加えて、Appleでは通知がグループ化された際に表示されるサマリーを編集できます。Brazeユーザーは、当社のツールを使用してプッシュキャンペーンを作成する際に、サマリーカテゴリ、サマリーカウント、サマリー引数を指定できます。

{% alert tip %}
同じThread IDを持つ通知が通知トレイでどのようにグループ化されるかはOSの制御下にあります。iOSは最適と判断した内容に応じて、同じThread IDを持つ通知を個別に表示する場合とグループ化して表示する場合があります。
{% endalert %}

**プッシュコンポーザー**の**Alert Options**ボックスにチェックを入れます。

次に、キーとして`summary-arg`と`summary-arg-count`を選択し、対応する列にそれらの値を入力します。`summary-arg`に値を設定しない場合、デフォルトで1になります。

### サマリーカテゴリ {#summary-categories}

サマリーカテゴリを使用すると、通知がグループ化された際に表示されるサマリー全体をカスタマイズできます。複数のカテゴリを作成して適用できます。

メッセージでカテゴリを使用するには、以下の例を参考に開発者と協力して実装してください：

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
この機能にSDKの更新は必要ありません。
{% endalert %}

{% alert tip %}
`%u`と`%@`はそれぞれサマリーカウントとサマリー引数のフォーマット文字列です。サマリーが表示される際、これらのプレースホルダーは`summary-count`と`summary-arg`の値に置き換えられます。
{% endalert %}

アプリでの設定が完了したら、**Notification Buttons**ボックスにチェックを入れ、**Enter Pre-registered iOS Category**を選択してサマリーカテゴリを使用します。

次に、アプリで設定したサマリーカテゴリの識別子を入力します。

### 仮承認プッシュとサイレント通知 {#provisional-push}

Appleでは、ブランドがユーザーに対して正式にオプトインする前に、通知センターにサイレントプッシュ通知を送信するオプションを提供しています。これにより、メッセージの価値を早い段階で示す機会が得られます。必要な作業はアプリで[仮承認プッシュ通知を設定](#set-up-provisional-push-notifications)するだけで、仮プッシュトークンを持つすべてのユーザーにメッセージが届きます。

従来のiOSプッシュトークンとは異なり、仮プッシュトークンは「お試しパス」として機能し、ユーザーがAppleのネイティブプッシュオプトインプロンプトを確認してクリックする前に、ブランドが新しいユーザーにリーチできます。この機能により、プッシュ通知は新しいユーザーの通知トレイに直接配信され、今後の通知を「Keep」するか「Turn Off」するかのオプションが表示されます。「オプトイン」のジャーニーではなく、「オプトアウト」に近いジャーニーを体験することになります。

{% alert tip %}
仮承認は、オプトイン率を大幅に向上させる可能性がありますが、ユーザーがメッセージに価値を感じる場合に限ります。[ユーザーセグメンテーション]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)、[位置情報ターゲティング]({{site.baseurl}}/user_guide/audience/locations_and_geofences)、[パーソナライゼーション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)機能を活用して、適切なユーザーに適切なタイミングでこれらの「お試し」通知が届くようにしてください。その後、プッシュ通知がアプリ体験に価値を加えることを理解した上で、ユーザーに完全なオプトインを促すことができます。
{% endalert %}

ユーザーがどちらのオプションを選択しても、適切なトークンまたは[購読ステータス]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states)がユーザープロファイルの**エンゲージメント**タブにある[コンタクト設定]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab)に追加されます。

![プッシュ購読済みステータスが表示されたコンタクト設定。]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を使用して、仮承認されているかどうかに基づいてユーザーをターゲティングできます。

![セグメント詳細パネルに「Provisionally Authorized on iOS Stopwatch (iOS) is true」というサンプルセグメントフィルターが表示されている状態。]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
ユーザーが仮プッシュの「Turn Off」を選択した場合、以降はあなたからの仮プッシュメッセージは表示されなくなります。この機能を使用して送信するメッセージの内容と頻度には十分配慮してください。
{% endalert %}

{% alert important %}
追加のプッシュプロンプトや[アプリ内プッシュプライマー](https://www.braze.com/resources/glossary/priming-for-push/)（プッシュ通知のオプトインを促すアプリ内メッセージ）を使用する場合は、Brazeの担当者に追加のガイダンスをお問い合わせください。
{% endalert %}

#### 仮承認プッシュ通知の設定 {#set-up-provisional-push-notifications}

Brazeでは、Braze iOS SDK実装内のトークン登録スニペットのコードを更新することで仮認証に登録できます。以下のスニペットを例として参考にしてください（開発者に送信するか、[統合プロセスで仮承認プッシュ認証を実装]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)するようにしてください）。

{% alert warning %}
仮承認プッシュ認証の実装はiOS 12以降のみをサポートしており、デプロイメントターゲットがそれ以前の場合はエラーが発生します。詳細については、[こちらの詳細な実装ドキュメント]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)をご覧ください。
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

iOS 15の新しい集中モードにより、ユーザーはアプリの通知がいつサウンドやバイブレーションで「中断」できるかをより細かくコントロールできるようになりました。

![通知が即座に配信されるよう設定され、タイムセンシティブ通知が有効化されたiOSの通知設定ページ。]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

アプリは、通知の緊急度に基づいて中断レベルを指定できます。

iOSプッシュ通知の中断レベルを変更するには、**設定**タブを選択し、**Interruption Level**ドロップダウンメニューから希望のレベルを選択します。

![中断レベルを選択するドロップダウン。]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

この機能に最小SDKバージョンの要件はありませんが、iOS 15以降を実行しているデバイスにのみ適用されます。

ユーザーが最終的に集中モードをコントロールしていることに留意してください。タイムセンシティブ通知が配信された場合でも、ユーザーはどのアプリが集中モードを突破できるかを指定できます。

中断レベルとその説明については、以下の表を参照してください。

|中断レベル|説明|使用するタイミング|集中モードを突破するか|
|--|--|--|--|
|[Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|サウンド、バイブレーション、画面の点灯なしで通知を送信します。|即座の注意を必要としない通知。|いいえ|
|[Active](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active)（デフォルト）|ユーザーが集中モードでない場合にのみ、サウンド、バイブレーション、画面の点灯を行います。|集中モードが有効でない限り、即座の注意が必要な通知。|いいえ|
|[Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|集中モード中でもサウンド、バイブレーション、画面の点灯を行います。Xcodeでアプリに**Time Sensitive Notifications capability**を追加する必要があります。|ライドシェアや配達通知など、集中モードに関係なくユーザーに通知すべきタイムリーな通知。|はい|
|[Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|電話の**おやすみモード**スイッチが有効でもサウンド、バイブレーション、画面の点灯を行います。[Appleの明示的な承認が必要](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/)です。|悪天候や安全アラートなどの緊急事態。|はい|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="中断レベル（iOS 15以降）" }

### 関連性スコア（iOS 15以降） {#relevance-score}

![「Your Evening Summary」というタイトルのiOS通知サマリーに3つの通知が表示されている状態。]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15では、ユーザーが1日を通して指定した時間に複数の通知をダイジェストとしてグループ化するスケジュールを任意で設定できる新しい方法も導入されました。これは、即座の注意を必要としない通知による絶え間ない中断を防ぐためのものです。

アプリは**関連性スコア**を設定することで、どのプッシュ通知が最も関連性が高いかを指定できます。Appleはこのスコアを使用して、スケジュールされた通知サマリーにどの通知を表示するかを決定し、残りの通知はユーザーがサマリーをクリックした際に表示されるようにします。

すべての通知は引き続きユーザーの通知センターでアクセスできます。

iOS通知の関連性スコアを設定するには、**設定**タブで`0.0`から`1.0`の間の値を入力します。たとえば、最も重要なメッセージは`1.0`で送信し、中程度の重要度のメッセージは`0.5`で送信します。

![関連性スコア「0.5」。]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

この機能に最小SDKバージョンの要件はありませんが、iOS 15以降を実行しているデバイスにのみ適用されます。

さまざまなメッセージタイプの最大メッセージ長の詳細については、以下のリソースを参照してください：

- [画像とテキストの仕様]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [iOS文字数ガイドライン]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count)