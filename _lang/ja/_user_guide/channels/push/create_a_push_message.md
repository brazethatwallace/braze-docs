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

> プッシュ通知は、時間的制約のあるアクションの呼びかけや、しばらくアプリを利用していないユーザーの再エンゲージメントに最適です。成功するプッシュCampaignは、ユーザーをコンテンツに直接誘導し、アプリの価値を示します。プッシュ通知の例については、[Brazeのお客様事例](https://www.braze.com/customers)をご覧ください。

## ステップ 1: メッセージの作成場所を選択する {#create-new-campaign-push}

{% alert tip %}
Campaignを使うべきか、Canvasを使うべきか迷っていますか？Campaignsは単一のターゲットメッセージングに適しており、Canvasesは複数ステップのユーザージャーニーに適しています。
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. **Messaging** > **Campaigns**に移動し、**Create Campaign**を選択します。
2. 複数チャネルをターゲットとするCampaignsの場合は、**Multichannel**を選択します。それ以外の場合は、**Push notification**を選択します。
3. Campaignにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams/)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/)を追加します。

{% alert tip %}
タグを使うと、Campaignsの検索やレポートの作成が簡単になります。例えば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder/)を使用する際に、特定のタグでフィルタリングできます。
{% endalert %}

{: start="5"}
5. Campaignに必要な数のバリアントを追加し、名前を付けます。追加した各バリアントに対して、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing/)を参照してください。

{% alert tip %}
Campaign内のすべてのメッセージが類似している場合や同じコンテンツの場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**Add Variant**ドロップダウンから**Copy from Variant**を選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. Canvasコンポーザーを使用して[Canvasを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)します。
2. Canvasの設定が完了したら、Canvasビルダーでステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. [ステップスケジュール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay)を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルタリングします。Segmentsを指定し、追加のフィルターを追加することで、このステップの受信者をさらに絞り込むことができます。オーディエンスオプションは、メッセージ送信時に遅延後にチェックされます。
5. [進行動作]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/)を選択します。
6. メッセージと組み合わせたい他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ 2: プッシュプラットフォームを選択する {#step-2-select-push-platforms}

次に、プッシュを受信するプラットフォームとモバイルデバイスの組み合わせを選択します。この選択を使用して、プッシュ通知の配信を特定のアプリセットに制限します。

以前の選択に応じて、いくつかの方法があります。

| 以前の選択 | オプション |
| --- | --- |
| プッシュ通知Campaign | 1つ以上のプラットフォームとデバイスを選択します。複数のデバイスとプラットフォームをターゲットにすることを選んだ場合、選択したすべてのプラットフォーム向けに1つのメッセージを作成するために最適化された編集体験が提供されます。この編集体験の違いについては、[マルチプラットフォームプッシュ]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push/)を参照してください。 |
| マルチチャネルCampaign | **Add Messaging Channel**を選択して、追加のプッシュプラットフォームを追加します。プラットフォームの選択は各バリアントに固有であるため、プラットフォームごとのメッセージエンゲージメントをテストできます。 |
| Canvas | メッセージステップで、**+ Add more**を選択して、追加のプッシュプラットフォームを追加します。マルチチャネルCampaignsと同様に、プラットフォームの選択は各バリアントに固有です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2: プッシュプラットフォームを選択する" }

## ステップ 3: 通知タイプを選択する（iOSおよびAndroid） {#step-3-select-notification-type-ios-and-android}

マルチプラットフォームプッシュCampaignを作成しており、WebやKindleを選択した場合、通知タイプは自動的に**Standard Push**に設定され、変更できません。

![通知タイプの例としてStandard Pushが選択されている画面。]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

それ以外の場合、iOSおよびAndroidでは、通知タイプを選択します。

- 標準プッシュ
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories/)（AndroidとiOSでサポート）
- インライン画像（Androidのみ）

プッシュCampaignに画像を含めたい場合は、[iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/)または[Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/)のリッチプッシュ通知の作成に関するガイドを参照してください。

## ステップ 4: プッシュメッセージを作成する {#step-4-compose-your-push-message}

いよいよプッシュメッセージを作成します！**Compose**タブでは、メッセージのコンテンツと動作のすべての側面を編集できます。

![プッシュ通知作成のComposeタブ。]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

**Compose**タブの内容は、前のステップで選択した通知タイプによって異なりますが、以下のオプションが含まれる場合があります。

### 通知チャネルまたはグループ（iOSおよびAndroid） {#notification-channel-or-group-ios-and-android}

プラットフォーム固有の通知オプションの詳細については、[iOS通知オプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/)または[Android通知オプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_options/)を参照してください。

### 言語 {#language}

**Add Languages**ボタンを使用して、複数の言語でコピーを追加します。コンテンツを作成する前に言語を選択し、Liquidの適切な場所にテキストを入力することをお勧めします。使用可能な言語の完全なリストについては、[サポートされている言語]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)を参照してください。

右から左に書く言語でコピーを追加する場合、右から左のメッセージの最終的な表示は、サービスプロバイダーのレンダリング方法に大きく依存します。できるだけ正確に表示される右から左のメッセージを作成するためのベストプラクティスについては、[右から左のメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/)を参照してください。

### タイトルと本文 {#title-and-body}

{% tabs local %}
{% tab ios %}
メッセージボックスに入力を開始すると、左側のプレビューボックスにプレビューが表示されます。プッシュメッセージはプレーンテキストでフォーマットする必要があります。

**Title**フィールドを使用して見出しを追加します。プッシュをパーソナライズしてターゲットを絞るために、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)を含めることができます。
{% endtab %}

{% tab android %}
メッセージボックスに入力を開始すると、左側のプレビューボックスにプレビューが表示されます。プッシュメッセージはプレーンテキストでフォーマットする必要があります。

プッシュをパーソナライズしてターゲットを絞るために、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)を含めることができます。

{% alert important %}
タイトルなしでAndroidプッシュメッセージを送信することは**できません**。ただし、代わりにスペースを1つ入力することは可能です。メッセージにスペースのみが含まれている場合、サイレントプッシュ通知として送信されることに注意してください。詳細については、[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
素晴らしいコピーの作成にお困りですか？[AIコピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/)をお試しください。製品名や説明を入力すると、AIがメッセージングに使用できる人間らしいマーケティングコピーを生成します。

![プッシュコンポーザーの本文フィールドにある「AIコピーライターを起動」ボタン。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

### 画像 {#image}

サポートされている場合、アプリアイコンがプッシュ通知の画像として自動的に追加されます。また、リッチプッシュ通知を送信するオプションもあり、コピー以外の追加コンテンツを追加してプッシュ通知をさらにカスタマイズできます。

プッシュ通知での画像の使用に関する追加のガイダンスについては、以下の記事を参照してください。

- [iOSのリッチプッシュ通知を作成する]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/)
- [Androidのリッチプッシュ通知を作成する]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### クリック時の動作 {#on-click-behavior}

**On-Click Behavior**で、ユーザーがプッシュ通知の本文を選択したときに何が起こるかを指定します。例えば、顧客にアプリケーションを開くよう促したり、指定したWeb URLにリダイレクトしたり、[ディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/)を使用してアプリケーションの特定のページを開いたりすることができます。

ここでは、プッシュ通知内にボタンプロンプトを設定することもできます。例えば：

- Accept/Decline
- Yes/No
- Confirm/Cancel
- More

### 送信オプション {#sending-options}

ユーザーが複数のデバイスにアプリをインストールしている場合、デフォルトでは、有効なプッシュトークンが割り当てられたすべてのデバイスにプッシュメッセージが送信されます。必要に応じて、**Most recently used device**を選択できます。

![ユーザーの最後に使用したデバイスにのみこのプッシュを送信するデバイスオプションのチェックボックス。]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

この設定にはいくつかのニュアンスがあります。このオプションが選択されている場合、Brazeは、iOSとAndroidの両方など、Campaignが複数のプラットフォームをターゲットにしている場合を除き、複数回の送信を制限します。ユーザーがiOSとAndroidの両方のデバイスにアプリを持っている場合、両方のプラットフォームのプッシュを受信します。ユーザーの最後に使用したデバイスが[プッシュ有効]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled)でない場合、メッセージは送信されません。

デフォルトでは、Brazeは有効なプッシュトークンを持つユーザーのすべてのデバイスにメッセージを送信します。iOSの場合、iPadデバイスのみ、またはiPhoneおよびiPodデバイスのみに通知を送信するように、リーチをさらに絞り込むことができます。

必要に応じて、プッシュの送信先を**Most recently used device**に設定できます。

#### 最後に使用したデバイス {#most-recently-used-device}

「最後に使用した」は技術的なステータスであり、行動的なものではありません。Brazeはデフォルトですべてのデバイスに送信するため、この設定に切り替えるとリーチが大幅に狭まり、最新のトークンを持つ単一のデバイスのステータスに完全に依存します。

最後に使用したデバイスは、最新のセッションがあったデバイスではなく、最も最近更新されたプッシュトークンを持つデバイスによって決定されます。
* 新しいデバイスのプッシュトークンがAPIを通じてユーザープロファイルに追加された場合、ユーザーがまだそのデバイスでセッションを開始していなくても、そのデバイスは即座に最後に使用したデバイスとみなされます。
* ユーザーの最後に使用したデバイスが[プッシュ有効]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled)でない場合、メッセージはまったく送信されません。

Campaignが異なるプラットフォーム（iOSとAndroidの両方など）をターゲットにしている場合、複数回の送信が発生する可能性があります。ユーザーが両方にアプリを持っている場合、両方のプラットフォームのプッシュを受信できます。

iOSの場合、iPadデバイスのみ、またはiPhoneおよびiPodデバイスのみにプッシュ通知を送信するように、メッセージングをさらに制限できます。

## ステップ 5: メッセージをプレビューしてテストする（オプション） {#step-5-preview-and-test-your-message-optional}

テストは間違いなく最も重要なステップの1つです。完璧なプッシュメッセージの作成が完了したら、送信前にテストしてください。**Test**タブを選択して、プッシュメッセージのテスト方法のオプションから選択します。**Test Recipients**で、コンテンツテストグループまたは個々のユーザーを選択できます。また、**Preview message as user**を使用して、ランダムなユーザー、既存のユーザー、カスタムユーザー、または多言語ユーザーとしてモバイルでメッセージがどのように表示されるかを確認できます。

詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=push)を参照してください。

## ステップ 6: CampaignまたはCanvasの残りを構築する {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Campaignの残りを構築します。プッシュ通知を構築するためのツールの最適な使用方法の詳細については、以下のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する {#choose-delivery-schedule-or-trigger}

プッシュメッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。詳細については、[Campaignのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/)を参照してください。

アクションベースの配信の場合、Campaignの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/)も設定できます。

このステップでは、ユーザーがCampaignを[再受信可能]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns)にすることや、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping)ルールを有効にするなど、配信コントロールを指定することもできます。

### ターゲットユーザーを選択する {#choose-users-to-target}

次に、Segmentsやフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/)する必要があります。おおよそのSegment人口のプレビューが自動的に表示されます。Campaignがターゲットとするチャネルの詳細なオーディエンス統計は、フッターで確認できます。ユーザー群のうちターゲットされている割合とこのSegmentのライフタイムバリューを確認するには、**Show Additional Stats**を選択します。

{% multi_lang_include target_audiences.md %}

{% details 到達可能なユーザーの合計指標がすべてのチャネルの合計と一致しないのはなぜですか？ %}

フィルタリングされたオーディエンスの到達可能なユーザーの合計を表示すると、個々の列の合計が到達可能なユーザーの合計よりも小さいことに気づく場合があります。このギャップは通常、CampaignのSegmentまたはフィルターの条件を満たしているが、プッシュ経由では到達できないユーザー（例えば、有効またはアクティブな[プッシュトークン]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle/#push-tokens)を持っていないため）が多数いることが原因です。

{% enddetails %}

![到達可能なユーザーの詳細なオーディエンス統計テーブル。]({% image_buster /assets/img_archive/multi_channel_footer.png %})

正確なSegmentメンバーシップは、メッセージが送信される前に常に計算されることに注意してください。

また、購読中やプッシュにオプトインしているユーザーなど、特定の[サブスクリプションステータス]({{site.baseurl}}/user_guide/channels/email/subscriptions/)を持つユーザーにのみCampaignを送信することもできます。

オプションとして、Segment内の指定された数のユーザーに配信を制限したり、Campaignの繰り返し時にユーザーが同じメッセージを2回受信できるようにすることもできます。

#### メールとプッシュのマルチチャネルCampaign {#multichannel-campaigns-with-email-and-push}

メールとプッシュの両方のチャネルをターゲットとするマルチチャネルCampaignsの場合、明示的にオプトインしたユーザーのみがメッセージを受信するようにCampaignを制限したい場合があります（購読中または配信停止のユーザーを除外）。例えば、異なるオプトインステータスを持つ3人のユーザーがいるとします。

- **ユーザーA**はメールを購読中で、プッシュが有効です。このユーザーはメールを受信しませんが、プッシュを受信します。
- **ユーザーB**はメールにオプトインしていますが、プッシュは有効ではありません。このユーザーはメールを受信しますが、プッシュは受信しません。
- **ユーザーC**はメールにオプトインしており、プッシュも有効です。このユーザーはメールとプッシュの両方を受信します。

これを行うには、**Audience Summary**で、このCampaignを「オプトインしたユーザーのみ」に送信するように選択します。このオプションにより、オプトインしたユーザーのみがメールを受信し、Brazeはデフォルトでプッシュが有効なユーザーにのみプッシュを送信します。

{% alert important %}
この設定では、**Target Audiences**ステップに、オーディエンスを単一のチャネルに制限するフィルター（例えば、`Foreground Push Enabled = True`や`Email Subscription = Opted-In`）を含めないでください。
{% endalert %}

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、Campaignを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/)）を実行する頻度を追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間の期間を設定するオプションがあります。

{% endtab %}

{% tab Canvas %}

まだ完了していない場合は、Canvasコンポーネントの残りのセクションを完了してください。Canvasの残りの構築方法、多変量テストとインテリジェントセレクションの実装などの詳細については、Canvasドキュメントの[Canvasを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ 7: 確認してデプロイする {#review-and-deploy-push}

CampaignまたはCanvasの最後の構築が完了したら、その詳細を確認します。Campaignsの場合、最終ページにはデザインしたCampaignの概要が表示されます。関連するすべての詳細を確認し、メッセージをテストしたことを確認してから送信し、データが届くのを見守りましょう！

次に、[プッシュレポート]({{site.baseurl}}/user_guide/channels/push/reporting/)を確認して、プッシュCampaignの結果にアクセスする方法を学びましょう。プッシュ通知では、送信数、配信数、バウンス数、開封数、直接開封数の統計を確認できます。

### トラブルシューティング {#troubleshooting}

#### クリック時の動作

SDKバージョンのデフォルトのクリック時の動作を使用しており、Web URLを含むプッシュ通知を選択するとWebブラウザではなくアプリ内で開く場合は、以下の統合ガイドを確認してプッシュ通知の処理を確認してください。

- [Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities)
- [Android]({{site.baseurl}}/developer_guide/push_notifications/#android_step-1-register-braze-firebase-messaging-service)

{% alert important %}
アプリの起動が完了する前に、`application:didFinishLaunchingWithOptions:`内で`center.delegate = self`を使用してデリゲートオブジェクトを同期的に割り当てる必要があります。そうしないと、アプリが受信プッシュ通知を見逃す可能性があります。詳細については、Appleの[`UNUserNotificationCenterDelegate`ドキュメント](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate)を参照してください。
{% endalert %}