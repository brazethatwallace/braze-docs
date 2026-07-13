---
nav_title: 放棄インテント
article_title: 放棄インテント
page_order: 1
page_type: reference
description: "この記事では、Braze Canvasテンプレートを使用して、ユーザーにリアルタイムでエンゲージし、購入を完了するよう促す方法について説明します。"
tool: Canvas
---

# 放棄インテント {#abandoned-intent}

> ユーザーにリアルタイムでエンゲージし、製品がまだ記憶に新しいうちに購入を完了するよう促しましょう。このAPIトリガーテンプレートは、ユーザーがカートを放棄した直後にエントリさせ、最適なチャネル（メール、SMS、またはアプリ内メッセージ）でタイムリーなリマインダーを送信し、ジャーニーの2つのポイントで購入完了を確認し、コンバージョンしなかったユーザーをリターゲティング用の広告オーディエンスに同期します。

この記事では、ユーザーライフサイクルの検討段階を対象とした**Abandoned Intent**テンプレートのユースケースについて説明します。この記事を読み終えると、カートにアイテムを追加した後に購入を完了していないユーザーに購入を促すユーザージャーニーをカスタマイズできるようになります。

{% alert tip %}
[BrazeAI Operator<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/operator)を使用して、このテンプレートの設定とカスタマイズを行いましょう。キャンバスの作成または編集中に、ユーザープロファイルの横にある**BrazeAI Operator<sup>TM</sup>**を選択します。次に、「カートを放棄したユーザーに再エンゲージするためにAbandoned Intentテンプレートを設定するのを手伝ってください」などの目標を記述します。
{% endalert %}

## 前提条件 {#prerequisites}

このテンプレートを正しく使用するには、以下が必要です。

- このキャンバスで購入するとユーザーがキャンバスを退出するため、購入後のユーザージャーニー用の別のキャンバス。
- 使用するパートナーとオーディエンスで設定済みの[Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync)。

## テンプレートをニーズに合わせてカスタマイズする {#tailoring-the-template-to-your-needs}

キッチン用品を専門とする小売ブランド「Kitchenerie」で働いていて、最新製品「Enormous Paper Plate」をカートに追加したが購入を完了していないユーザーに再エンゲージすることが目標だとしましょう。

キャンバスを作成する前に、[Braze Audience Sync to Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync)インテグレーションを設定し、BrazeのユーザーデータをFacebookオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいた広告を配信できるようにします。

**Abandoned Intent**テンプレートは次のフローに従います：購入確認、即時リマインダー送信、待機、最適チャネルへのルーティング、フォローアップ、再確認、非コンバージョンユーザーのリターゲティング。以下のステップが含まれます。

| キャンバスステップ | テンプレートのステップ名 | 目的 |
|---|---|---|
| アクションパス | Made purchase? | 最初の完了確認。すでに購入したユーザーはキャンバスを退出します。 |
| メッセージ | Itemized Reminder | エントリ直後に送信される即時カートリマインダー。 |
| 遅延 | Delay | 製品がまだ記憶に新しいうちにフォローアップが届くよう、30分間の待機。 |
| オーディエンスパス | Intelligent Channel split | [インテリジェントチャネル]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel)ランキングに基づいて、ユーザーをメールまたはSMSにルーティングします。 |
| メッセージ | Abandoned Cart Email、Abandoned Cart SMS、Abandoned Cart In-App Message | チャネル別のフォローアップ。インテリジェントチャネルがメールとSMSを選択し、アプリ内メッセージはテンプレート内の別のパスで送信されます。 |
| アクションパス | Made purchase? (2) | リターゲティング前の2回目の完了確認。 |
| Audience Sync | Ad Retargeting | 非コンバージョンユーザーをオフチャネルリターゲティング用の広告オーディエンス（Facebookなど）に同期します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Abandoned Intentテンプレートのステップ" }

### ステップ 1: 詳細を設定する {#step-1-set-up-the-details}

キャンバステンプレートを適用し、目標に合わせて詳細を更新しましょう。

1. **メッセージング** > **キャンバス**に移動します。
2. **Create キャンバス** > **Use a Canvas Template**を選択します。
3. **Braze templates**タブを選択し、**Abandoned Intent**の横にある**Apply Template**を選択します。
4. 説明を更新して、最新の季節限定キッチン用品の発売から購入を完了するようユーザーに促すキャンバスであることを明示します。
5. **Intent**タグを追加して、キャンバスホームページでフィルタリングできるようにします。

![キャンバスの新しい名前、説明、タグ。]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### ステップ 2: コンバージョンイベントを割り当てる {#step-2-assign-your-conversion-events}

テンプレートでは、**Primary Conversion Event - A**が**Makes Purchase (Legacy)**に設定されており、デフォルトで**Make any purchase (Legacy)**が選択されています。「Enormous Paper Plate」製品に焦点を当てているため、コンバージョンイベントを以下のようにカスタマイズします。

1. **Make a specific purchase (Legacy)**を選択します。
2. **Product name**に**Enormous Paper Plate**と入力します。

![1次コンバージョンイベント - A。コンバージョンタイプは「Makes Purchase」で、製品名は「Enormous Paper Plate」。コンバージョン期限は3日間。]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

{% alert note %}
ワークスペースで**Places order**コンバージョンイベントを使用している場合、購入関連のオプションにラベルで**(Legacy)**と表示されることがあります。この記事のステップでは、レガシーの購入コンバージョンフローを使用しています。
{% endalert %}

### ステップ 3: エントリスケジュールを設定する {#step-3-set-an-entry-schedule}

**Abandoned Intent**テンプレートは**API-Triggered**エントリスケジュールを使用しているため、ユーザーがカートを放棄した直後にキャンバスにエントリさせることができます。製品がまだ記憶に新しいうちに対応したいため、このユースケースに適しています。

1. エントリスケジュールタイプとして**API-Triggered**をそのまま使用します。
2. キャンバス IDを確認し、[`/canvas/trigger/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)を使用して、アプリまたはWebサイトがカート放棄を検出した際にユーザーを追加します。
3. オプションで、[コンテキスト変数]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)（製品名やカートの詳細など）を渡して、下流のメッセージをパーソナライズできます。

アクションベースのエントリを希望する場合は、**Action-Based**を選択し、ブランドがカート放棄を追跡する方法に合ったトリガーを選択します。たとえば、ログに記録された`abandoned_cart`イベントに対して**Perform Custom Event**を選択します。

### ステップ 4: キャンバスにエントリするユーザーを決定する {#step-4-determine-who-enters-the-canvas}

次に、過去90日間にオンラインのみで買い物をしたユーザーをターゲットオーディエンスとして定義しましょう。これにより、製品にエンゲージしていることがわかっているユーザーにオーディエンスを絞り込むことができます。

![このキャンバスでターゲットにするユーザーのセグメントとして「Online Shoppers セグメント - 90 Days」。]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

エントリコントロールはそのままにしておきます。ユーザーがこのキャンバスに再エントリすることは許可されず、このキャンバスにエントリできる人数に制限はありません。

テンプレートではデフォルトでグローバル退出条件は設定されていません。代わりに、ユーザーは**Made purchase?**アクションパスステップで購入した際に退出します。これはステップ6でカスタマイズします。

### ステップ 5: 送信設定を選択する {#step-5-select-your-send-settings}

デフォルトのサブスクリプション設定をそのまま使用し、メッセージや通知の受信を購読またはオプトインしたユーザーにのみ送信します。その他の設定もそのままにしておきます。

### ステップ 6: キャンバスをカスタマイズする {#step-6-customize-your-canvas}

ユーザーが体験する順序でキャンバスステップをカスタマイズします。

#### エントリ時の購入確認 {#check-for-purchase-at-entry}

1. **Made purchase?**アクションパスステップを選択し、**Made purchase**アクショングループを選択します。
2. **Make Purchase**で、**Make a specific purchase (Legacy)**を選択し、製品として**Enormous Paper Plate**を選択します。この製品を購入したユーザーはキャンバスを退出します。

#### 即時リマインダーの送信 {#send-the-immediate-reminder}

1. **Itemized Reminder**メッセージステップを選択し、**Edit message**を選択して最初のリマインダーメールをカスタマイズします。このメッセージは遅延の前、エントリ直後に送信されます。
2. **Delay**ステップはそのままにしておきます。テンプレートでは、フォローアップメッセージの送信前に30分の遅延を使用しており、製品がまだ記憶に新しいうちにユーザーがチェックアウトを完了する時間を確保します。

{% alert tip %}
[キャンバスコンテキストプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)を使用して、参照している製品に基づいてキャンバス内のメッセージをカスタマイズできます。
{% endalert %}

#### 最適チャネルへのルーティング {#route-to-the-optimal-channel}

1. **Intelligent Channel split**オーディエンスパスステップを確認します。これにより、[インテリジェントチャネル]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel)ランキングに基づいて、ユーザーを**Abandoned Cart Email**または**Abandoned Cart SMS**にルーティングします。必要に応じてパスを調整します。
2. **Abandoned Cart Email**、**Abandoned Cart SMS**、**Abandoned Cart In-App Message**ステップをカスタマイズします。各ステップで**Edit message**を選択して、そのチャネルのコピーとメッセージを更新します。アプリ内メッセージはインテリジェントチャネル分割とは別のパスで実行され、インテリジェントチャネルランキングでは選択されません。

#### 非コンバージョンユーザーのリターゲティング {#retarget-non-converters}

1. **Made purchase? (2)**アクションパスステップを選択し、**Made purchase**アクショングループを選択します。
2. **Make a specific purchase (Legacy)**を選択し、製品として**Enormous Paper Plate**を選択します。ここで購入したユーザーは、リターゲティングに到達する前にキャンバスを退出します。
3. **Ad Retargeting** Audience Syncステップを選択し、Facebookに同期するように設定します。このステップに到達したユーザーは購入していないため、オフチャネルリターゲティング用の広告オーディエンスに同期します。

### ステップ 7: キャンバスをテストして起動する {#step-7-test-and-launch-the-canvas}

キャンバスをテストして確認し、期待どおりに動作することを確認したら、**Launch キャンバス**を選択してキャンバスを起動します。これで、パーソナライズされたユーザージャーニーでユーザーに的確にターゲティングし、カートに追加した製品のチェックアウトを促すことができます！

{% alert tip %}
キャンバスの起動前後に考慮すべき事項については、[起動前後のチェックリスト]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch)をご確認ください。
{% endalert %}