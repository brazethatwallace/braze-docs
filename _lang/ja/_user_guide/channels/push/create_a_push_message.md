---
nav_title: "プッシュメッセージを作成する"
article_title: "プッシュメッセージを作成する"
page_order: 1
page_type: tutorial
description: "このチュートリアルページでは、設定、送信、ターゲティングなど、プッシュメッセージの作成に関わるさまざまなコンポーネントについて説明します。"
channel: push
tool:
  - Campaigns




---

# プッシュメッセージを作成する {#create-a-push-message}

> プッシュ通知は、時間的制約のあるアクションの呼びかけや、しばらくアプリを利用していないユーザーの再エンゲージメントに最適です。成功するプッシュキャンペーンは、ユーザーをコンテンツに直接誘導し、アプリの価値を示します。プッシュ通知の例については、[Brazeのお客様事例](https://www.braze.com/customers)をご覧ください。

## ステップ1:メッセージの作成場所を選択する {#create-new-campaign-push}

{% alert tip %}
キャンペーンを使うべきか、キャンバスを使うべきか迷っていますか？キャンペーンは単一のターゲットメッセージングに適しており、キャンバスは複数ステップのユーザージャーニーに適しています。
{% endalert %}

{% tabs %}
{% tab キャンペーン %}
1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. 複数チャネルをターゲットとするキャンペーンの場合は、**マルチチャネル**を選択します。それ以外の場合は、**プッシュ通知**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。

{% alert tip %}
タグを使うと、キャンペーンの検索やレポートの作成が簡単になります。例えば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する際に、特定のタグでフィルタリングできます。
{% endalert %}

{: start="5"}
5. キャンペーンに必要な数のバリアントを追加し、名前を付けます。追加した各バリアントに対して、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している場合や同じコンテンツの場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}
{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## ステップ2: プッシュプラットフォームを選択する {#step-2-select-push-platforms}

次に、プッシュ通知を受信するプラットフォームとモバイルデバイスの組み合わせを選択します。この選択を使用して、プッシュ通知の配信を特定のアプリセットに限定します。

以前の選択内容に応じて、いくつかの方法があります。

| 以前の選択 | オプション |
| --- | --- |
| プッシュ通知キャンペーン | 1つまたは複数のプラットフォームとデバイスを選択します。複数のデバイスとプラットフォームをターゲットにすることを選択した場合、選択したすべてのプラットフォーム向けに1つのメッセージを作成するために編集エクスペリエンスが最適化されます。この編集エクスペリエンスの違いについては、[マルチプラットフォームプッシュ]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push)を参照してください。 |
| マルチチャネルキャンペーン | **メッセージングチャネルを追加**を選択して、追加のプッシュプラットフォームを追加します。プラットフォームの選択は各バリアントに固有であるため、プラットフォームごとのメッセージエンゲージメントをテストできます。 |
| キャンバス | メッセージステップで、**+ さらに追加**を選択して、追加のプッシュプラットフォームを追加します。マルチチャネルキャンペーンと同様に、プラットフォームの選択は各バリアントに固有です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2: プッシュプラットフォームを選択する" }

## ステップ3：通知タイプを選択する（iOSおよびAndroid） {#step-3-select-notification-type-ios-and-android}

マルチプラットフォームプッシュキャンペーンを作成し、Webやkindleを選択した場合、通知タイプは自動的に**Standard push**に設定され、変更できません。

![通知タイプの例としてStandard Pushが選択されている画面。]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

それ以外の場合、iOSおよびAndroidでは通知タイプを選択します。

- Standard push
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)（Android + iOSでサポート）
- Inline image（Androidのみ）

プッシュキャンペーンに画像を含めたい場合は、[iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications)または[Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications)のリッチプッシュ通知の作成に関するガイドを参照してください。

## ステップ4：プッシュメッセージを作成する {#step-4-compose-your-push-message}

いよいよプッシュメッセージを作成します！**作成**タブでは、メッセージのコンテンツと動作のすべての要素を編集できます。

![プッシュ通知作成の「作成」タブ。]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

**作成**タブの内容は、前のステップで選択した通知タイプによって異なりますが、以下のオプションが含まれる場合があります。

### 通知チャネルまたはグループ（iOSおよびAndroid） {#notification-channel-or-group-ios-and-android}

プラットフォーム固有の通知オプションについて詳しくは、[iOS通知オプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options)または[Android通知オプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_options)を参照してください。

### 言語 {#language}

**言語を追加**ボタンを使用して、複数の言語でコピーを追加します。コンテンツを入力する前に言語を選択し、Liquidの適切な場所にテキストを入力することをお勧めします。利用可能な言語の一覧については、[サポートされている言語]({{site.baseurl}}/developer_guide/localization?tab=android)を参照してください。

右から左に書く言語のコピーを追加する場合、右から左へのメッセージの最終的な表示はサービスプロバイダーのレンダリング方法に大きく依存することに注意してください。右から左へのメッセージをできるだけ正確に表示するためのベストプラクティスについては、[右から左へのメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

### タイトルと本文 {#title-and-body}

{% tabs local %}
{% tab iOS %}
メッセージボックスに入力を開始すると、隣のプレビューボックスにプレビューが表示されます。プッシュメッセージはプレーンテキストで書式設定する必要があります。

**タイトル**フィールドを使用して見出しを追加します。プッシュをパーソナライズしてターゲットを絞るために、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を含めることができます。
{% endtab %}

{% tab Android %}
メッセージボックスに入力を開始すると、隣のプレビューボックスにプレビューが表示されます。プッシュメッセージはプレーンテキストで書式設定する必要があります。

プッシュをパーソナライズしてターゲットを絞るために、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を含めることができます。

{% alert important %}
タイトルなしでAndroidプッシュメッセージを送信することは**できません**。ただし、代わりにスペースを1つ入力することは可能です。メッセージにスペースのみが含まれている場合、サイレントプッシュ通知として送信されることに注意してください。詳しくは、[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android)を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
素晴らしいコピーの作成にお困りですか？[AIコピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)をお試しください。商品名や説明を入力すると、AIがメッセージングに使用できる人間らしいマーケティングコピーを生成します。

![プッシュコンポーザーの本文フィールドにある「AIコピーライターを起動」ボタン。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

### 画像 {#image}

サポートされている場合、アプリアイコンがプッシュ通知の画像として自動的に追加されます。また、リッチ通知を送信するオプションもあり、コピー以外の追加コンテンツを追加してプッシュ通知をさらにカスタマイズできます。

プッシュ通知での画像の使用に関する追加のガイダンスについては、以下の記事を参照してください。

- [iOSのリッチ通知を作成する]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications)
- [Androidのリッチ通知を作成する]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### クリック時の動作 {#on-click-behavior}

**クリック時の動作**を使用して、ユーザーがプッシュ通知の本文を選択したときの動作を指定します。たとえば、顧客にアプリを開くよう促したり、指定したWeb URLに顧客をリダイレクトしたり、[ディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls)を使用してアプリの特定のページを開いたりすることができます。

ここでは、プッシュ通知内にボタンプロンプトを設定することもできます。例：

- 承認/辞退
- はい/いいえ
- 確認/キャンセル
- その他

### 送信オプション {#sending-options}

ユーザーが複数のデバイスにアプリをインストールしている場合、デフォルトでは有効なプッシュトークンが割り当てられたすべてのデバイスにプッシュメッセージが送信されます。必要に応じて、**最後に使用したデバイス**を選択できます。

![ユーザーの最後に使用したデバイスにのみプッシュを送信するデバイスオプションのチェックボックス。]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

この設定にはいくつかのニュアンスがあります。このオプションを選択した場合、Brazeはキャンペーンが iOSとAndroidの両方など複数のプラットフォームをターゲットにしている場合を除き、複数送信を制限します。ユーザーがiOSとAndroidの両方のデバイスにアプリを持っている場合、両方のプラットフォームでプッシュを受信します。ユーザーの最後に使用したデバイスが[プッシュ有効]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled)でない場合、メッセージは送信されません。

デフォルトでは、Brazeは有効なプッシュトークンを持つユーザーのすべてのデバイスにメッセージを送信します。iOSの場合、iPadデバイスのみ、またはiPhoneおよびiPodデバイスのみに通知を送信するよう、さらにリーチを絞り込むことができます。

必要に応じて、プッシュの送信先を**最後に使用したデバイス**に設定できます。

#### 最後に使用したデバイス {#most-recently-used-device}

「最後に使用した」は技術的なステータスであり、行動に基づくものではありません。Brazeはデフォルトですべてのデバイスに送信するため、この設定に切り替えるとリーチが大幅に狭まり、最新のトークンを持つ単一デバイスのステータスに完全に依存します。

最後に使用したデバイスは、最新のセッションを持つデバイスではなく、プッシュトークンが最も最近更新されたデバイスによって決定されます。
* 新しいデバイスのプッシュトークンがAPIを通じてユーザープロファイルに追加された場合、そのユーザーがまだそのデバイスでセッションを開始していなくても、そのデバイスは即座に最後に使用したデバイスとみなされます。
* ユーザーの最後に使用したデバイスが[プッシュ有効]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled)でない場合、メッセージはまったく送信されません。

キャンペーンがiOSとAndroidなど異なるプラットフォームをターゲットにしている場合、複数送信が発生する可能性があります。ユーザーが両方のプラットフォームにアプリを持っている場合、両方のプラットフォームでプッシュを受信できます。

iOSの場合、iPadデバイスのみ、またはiPhoneおよびiPodデバイスのみにプッシュ通知を送信するよう、さらにメッセージングを制限できます。

## ステップ5：メッセージのプレビューとテスト（オプション） {#step-5-preview-and-test-your-message-optional}

テストは間違いなく最も重要なステップの1つです。完璧なプッシュメッセージを作成したら、送信前にテストを行いましょう。**テスト**タブを選択して、プッシュメッセージのテスト方法のオプションから選択します。**テスト受信者**では、コンテンツテストグループまたは個々のユーザーを選択できます。また、**ユーザーとしてメッセージをプレビュー**を使用して、ランダムなユーザー、既存のユーザー、カスタムユーザー、または多言語ユーザーとして、モバイルでメッセージがどのように表示されるかを確認することもできます。

詳しくは、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=push)を参照してください。

## ステップ6: キャンペーンまたはキャンバスの残りの部分を構築する {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

キャンペーンの残りの部分を構築します。プッシュ通知を構築するためのツールの最適な使用方法については、以下のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する {#choose-delivery-schedule-or-trigger}

プッシュメッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。詳細については、[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

アクションベースの配信では、キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定することもできます。

このステップでは、ユーザーがキャンペーンを[再度受信可能]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility)にする設定や、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)ルールの有効化など、配信コントロールを指定することもできます。

### ターゲットユーザーを選択する {#choose-users-to-target}

次に、セグメントまたはフィルターを選択してオーディエンスを絞り込み、[ターゲットユーザー]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)を設定する必要があります。そのおおよそのセグメント人口のプレビューが自動的に表示されます。キャンペーンがターゲットとするチャネルの詳細なオーディエンス統計は、フッターに表示されます。ユーザー群のうちターゲットされている割合と、このセグメントの生涯価値を確認するには、**Show Additional Stats** を選択してください。

{% multi_lang_include audience/target_audiences.md %}

{% details 到達可能なユーザーの合計がすべてのチャネルの合計と一致しないのはなぜですか？ %}

フィルタリングされたオーディエンスの到達可能なユーザーの合計を表示すると、個々の列の合計が到達可能なユーザーの合計よりも少ない場合があります。このギャップは通常、キャンペーンのセグメントまたはフィルターの条件を満たしているが、プッシュを通じて到達できないユーザーが一定数存在するためです（たとえば、有効またはアクティブな[プッシュトークン]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#push-tokens)を持っていないなど）。

{% enddetails %}

![到達可能なユーザーの詳細なオーディエンス統計のテーブル。]({% image_buster /assets/img_archive/multi_channel_footer.png %})

正確なセグメントメンバーシップは、メッセージが送信される前に常に計算されることに留意してください。

特定の[購読ステータス]({{site.baseurl}}/user_guide/channels/email/subscriptions)を持つユーザー（プッシュに購読済みでオプトインしているユーザーなど）にのみキャンペーンを送信することも選択できます。

オプションとして、セグメント内の指定した数のユーザーに配信を制限したり、キャンペーンが繰り返された場合にユーザーが同じメッセージを2回受信できるようにすることもできます。

#### メールとプッシュのマルチチャネルキャンペーン {#multichannel-campaigns-with-email-and-push}

メールとプッシュの両方のチャネルをターゲットとするマルチチャネルキャンペーンでは、明示的にオプトインしたユーザーのみがメッセージを受信するようにキャンペーンを制限することをお勧めします（購読済みまたは購読解除済みのユーザーを除外）。たとえば、異なるオプトインステータスを持つ3人のユーザーがいるとします。

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

これを行うには、**オーディエンスの概要** で、このキャンペーンを「オプトインしたユーザーのみ」に送信するように選択します。このオプションにより、オプトインしたユーザーのみがメールを受信し、Brazeはデフォルトでプッシュが有効なユーザーにのみプッシュを送信します。

{% alert important %}
この設定では、**ターゲットオーディエンス** ステップにオーディエンスを単一チャネルに制限するフィルター（たとえば `Foreground Push Enabled = True` や `Email Subscription = Opted-In`）を含めないでください。
{% endalert %}

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）をどの程度の頻度で実行するかを追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間のウィンドウを設定するオプションがあります。

{% endtab %}

{% tab キャンバス %}

まだ完了していない場合は、キャンバスコンポーネントの残りのセクションを完成させてください。キャンバスの残りの構築方法（多変量テストや[BrazeAI<sup>TM</sup>による最適化]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai)など）の詳細については、[キャンバスの構築]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas)を参照してください。

{% endtab %}
{% endtabs %}

## ステップ7:確認してデプロイする {#review-and-deploy-push}

キャンペーンまたはキャンバスの最後の構築が完了したら、その詳細を確認します。キャンペーンの場合、最終ページにはデザインしたキャンペーンの概要が表示されます。関連するすべての詳細を確認し、メッセージをテストしたことを確認してから送信し、データが届くのを見守りましょう！

次に、[プッシュレポート]({{site.baseurl}}/user_guide/channels/push/reporting)を確認して、プッシュキャンペーンの結果にアクセスする方法を学びましょう。プッシュ通知では、送信数、配信数、バウンス数、開封数、直接開封数の統計を確認できます。

### トラブルシューティング {#troubleshooting}

#### クリック時の動作

SDKバージョンのデフォルトのクリック時の動作を使用しており、Web URLを含むプッシュ通知を選択するとWebブラウザではなくアプリ内で開く場合は、以下の統合ガイドを確認してプッシュ通知の処理を確認してください。

- [Swift]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#swift_step-2-enable-push-capabilities)
- [Android]({{site.baseurl}}/developer_guide/push_notifications#android_step-1-register-braze-firebase-messaging-service)

{% alert important %}
アプリの起動が完了する前に、`application:didFinishLaunchingWithOptions:`内で`center.delegate = self`を使用してデリゲートオブジェクトを同期的に割り当てる必要があります。そうしないと、アプリが受信プッシュ通知を見逃す可能性があります。詳細については、Appleの[`UNUserNotificationCenterDelegate`ドキュメント](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate)を参照してください。
{% endalert %}