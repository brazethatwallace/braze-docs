---
nav_title: Front
article_title: Front
description: "BrazeとFrontを統合する方法を学びます"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> Frontの統合により、各プラットフォームからBrazeデータ変換とwebhookを活用して、双方向の会話型SMSパイプラインを設定できます。

Frontからの受信webhookには、ライブエージェントが送信したメッセージを含むペイロードが含まれています。リクエストは、Brazeのエンドポイントで受け入れられるようにするため、事前に再フォーマットしておく必要があります。Frontデータ変換テンプレートによりペイロードが再フォーマットされ、イベントプロパティとして渡されるメッセージ本文とともに**Outbound SMS Sent**というタイトルのカスタムイベントがユーザープロファイルに書き込まれます。

Brazeで新しい変換を設定する前に、[データ変換]({{site.baseurl}}/user_guide/data/unification/data_transformation)ドキュメントの各ティアのサポートマトリックスを確認することをお勧めします。無料およびProティアでは、月ごとのアクティブな変換と受信リクエストの数が異なります。現在のプランがユースケースをサポートできるか確認してください。

## 前提条件 {#prerequisites}

開始する前に、次のものが必要です。

| 前提条件 | 説明 |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Frontアカウント | このパートナーシップを利用するには、Frontアカウントが必要です。|
| Brazeデータ変換Webhook URL | [Brazeデータ変換]({{site.baseurl}}/user_guide/data/unification/data_transformation)は、Frontからの受信webhookを再フォーマットして、Brazeの/users/trackエンドポイントで受け入れられるようにするために使用されます。|
| Front REST APIキー | Front REST APIキーを使用して、BrazeからFrontへのアウトバウンドWebhookリクエストを行います。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

- Brazeの自動SMSメッセージングを使用してリード生成プロセスを合理化し、ユーザーの好みを特定し、ライブ販売エージェントがフォローアップして販売を完了できるようにします。
- 自動SMS応答とライブチャットサポートによりセールスコンバージョンを促進することで、ショッピングカートを放棄した顧客を再エンゲージします。

## Frontの統合 {#integrating-front}

### ステップ1:データ変換を作成する {#step-1-create-a-data-transformation}

まず、Brazeで新しいデータ変換を作成します。次のステップは簡略化されています。完全な手順については、[変換の作成]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation)を参照してください。

1. Brazeで、**データ設定** > **データ変換**に移動し、**変換を作成**を選択します。
2. **編集エクスペリエンス**で、**ゼロから始める**を選択します。
3. **送信先を選択**で、**POST: Track Users**を選択します。
4. 次の変換テンプレートをコピーして貼り付け、エンドポイントを保存してアクティブ化します。
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    変換は上記のJavaScript例に沿うようにし、プロパティ名とパスをFrontのwebhookペイロードに合わせて調整してください。

{% alert tip %}
このテンプレートを変更して、特定のニーズに合わせることができます。例えば、プリセットのカスタムイベント名をカスタマイズできます。詳細については、[データ変換の概要]({{site.baseurl}}/user_guide/data/unification/data_transformation)を参照してください。
{% endalert %}

### ステップ2:アウトバウンドSMSキャンペーンを作成する {#step-2-create-an-outbound-sms-campaign}

次に、Frontからのwebhookをリッスンし、顧客にカスタムSMS応答を送信するSMSキャンペーンを作成します。

#### ステップ2.1:メッセージを作成する {#step-21-compose-your-message}

**メッセージ**テキストボックスに、次のLiquidコード、およびオプトアウト言語やその他の静的コンテンツを追加します。

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

メッセージは次のようになります。

![Liquidコードを使ったメッセージの例。]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 配信をスケジュールする {#22-schedule-the-delivery}

配信タイプには**アクションベースの配信**を選択し、カスタムイベントトリガーには**Outbound SMS Sent**を選択します。

![「配信をスケジュール」ページ。]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
このカスタムイベントは、ユーザーのプロファイルに書き込むデータ変換です。エージェントメッセージはこのイベントのイベントプロパティとして保存されます。
{% endalert %}

最後に、**配信コントロール**で再適格性を有効にします。

![「配信コントロール」で再適格性が有効になっている。]({% image_buster /assets/img/front/braze_reeligibility.png %})

### ステップ3:カスタムチャネルを作成する {#step-3-create-a-custom-channel}

Frontのダッシュボードで、**設定** > **チャネル** > **チャネルを追加**に移動し、**カスタムチャネル**を選択して、新しいBrazeチャネルの名前を入力します。

![FrontダッシュボードのBraze用カスタムチャネル。]({% image_buster /assets/img/front/front_custom_channel.png %})

### ステップ4:設定を構成する {#step-4-configure-the-settings}

アウトバウンドAPIエンドポイントフィールドに、[以前に作成した](#step-1-set-up-a-data-transformation-in-braze)データ変換Webhook URLを入力します。新しいBrazeチャネルでのライブエージェントからのすべてのアウトバウンドメッセージはここに送信されます。このチャネルは、BrazeがSMSメッセージを転送するためのエンドポイントURLも**Incoming URL**フィールドに提供します。

このURLをメモしておいてください。後で必要になります。

![Frontに新しく作成されたBrazeチャネルのチャネル設定。]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### ステップ5:インバウンドSMS転送の設定 {#step-5-set-up-inbound-sms-forwarding}

次に、Brazeで2つの新しいWebhookキャンペーンを作成します。これにより、顧客からのインバウンドSMSをFrontの受信トレイに転送できます。

| 番号 | 目的 |
|---|---|
| Webhookキャンペーン1 | ライブチャットの会話が要求されていることをFrontに通知します。|
| Webhookキャンペーン2 | 顧客からインバウンドで送信されたすべての会話型SMS応答をFrontの受信トレイに転送します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ5:インバウンドSMS転送の設定" }

#### ステップ5.1:SMSキーワードカテゴリを作成する {#step-51-create-an-sms-keyword-category}

Brazeのダッシュボードで、**オーディエンス**に移動し、**SMS購読グループ**を選択して、**カスタムキーワードを追加**を選択します。Front専用のSMSキーワードカテゴリを作成するには、次のフィールドに記入してください。

| フィールド | 説明 |
|---|---|
| キーワードカテゴリ | キーワードカテゴリの名前（例：`FrontSMS1`）。|
| キーワード | カスタムキーワード（例：`TIMETOMOW`）。一般的な言葉を避けて、誤ってトリガーされないようにしてください。キーワードは大文字と小文字を区別しないため、`lawn`は`LAWN`と一致します。|
| 返信メッセージ | キーワードが検出されたときに送信されるメッセージ（例：「造園業者からまもなく連絡があります」）。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ5.1:SMSキーワードカテゴリを作成する" }

![BrazeのSMSキーワードカテゴリの例。]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### ステップ5.2:最初のWebhookキャンペーンを作成する {#step-52-create-your-first-webhook-campaign}

Brazeのダッシュボードで、[以前に作成した](#step-3-configure-the-settings-for-your-new-custom-braze-channel)URLを使用して最初のWebhookキャンペーンを作成します。

![Brazeで最初に作成すべきWebhookキャンペーンの例。]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

次の内容をリクエストボディに追加してください：

{% raw %}
```liquid
{
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

設定タブで、`Authorization`、`Content-Type`、および`accept`のリクエストヘッダーを構成します。

![3つの必須ヘッダーを持つリクエストの例。]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### ステップ5.3:最初の配信をスケジュールする {#step-53-schedule-the-first-delivery}

**配信をスケジュール**で、**アクションベースの配信**を選択し、トリガータイプとして**SMSインバウンドメッセージを送信する**を選択します。また、[以前に設定した](#step-51-create-an-sms-keyword-category)SMS購読グループとキーワードカテゴリを追加します。

![最初のWebhookキャンペーンの「配信をスケジュール」ページ。]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

**配信コントロール**で再適格性を有効にします。

![最初のWebhookキャンペーンの「配信コントロール」で再適格性が選択されている。]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### ステップ5.4:2番目のWebhookキャンペーンを作成する {#step-54-create-your-second-webhook-campaign}

2つ目のWebhookキャンペーンは1つ目と同じ内容なので、[1つ目を複製して名前を変更する]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-or-campaigns)ことができます。

#### ステップ5.5:2回目の配信をスケジュールする {#step-55-schedule-the-second-delivery}

**配信をスケジュール**で、**アクションベースのトリガー**と**SMS購読グループ**を[最初の配信](#step-53-schedule-the-first-delivery)と同じに設定します。ただし、**キーワードカテゴリ**には**Other**を選択してください。

![2つ目のWebhookキャンペーンの「配信をスケジュール」ページ。キーワードカテゴリとして「Other」が選択されている。]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### ステップ5.6:オーディエンスフィルターを追加する {#step-56-add-an-audience-filter}

これで、Webhookキャンペーンが顧客からのインバウンドSMS応答を転送できるようになりました。ライブチャット用のメッセージのみが転送されるようにSMS応答をフィルタリングするには、**特定キャンペーンからの最終受信メッセージ**セグメンテーションフィルターを**ターゲットオーディエンス**ステップに追加します。

![「特定キャンペーンからの最終受信メッセージ」を選択したオーディエンスフィルター。]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

次に、フィルターを設定します：

1. **キャンペーン**には、[以前に作成した](#step-2-create-an-outbound-sms-campaign)SMSキャンペーンを選択します。
2. **オペレーター**には、**Less Than**を選択します。
3. **タイムウィンドウ**には、顧客からの応答がない状態でチャットを開いたままにしておく期間を選択します。

![選択したオーディエンスフィルターの設定。]({% image_buster /assets/img/front/front_target_audience.png %})

## 考慮事項 {#considerations}

### 課金対象セグメント {#billable-segments}

- BrazeでのSMSメッセージはメッセージセグメントごとに課金されます。何がセグメントを定義し、どのようにメッセージが分割されるかを理解することは、メッセージの請求方法を理解するうえで重要です。詳細については、当社の[ドキュメント]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)をご覧ください。
- エージェントの応答が長いと、課金対象セグメントの消費が増加します。

### データポイントの記録 {#logging-data-points}

現在、この統合では、ライブエージェントがFrontからSMSを送信するたびに、ユーザープロファイルにカスタムイベントを書き込む必要があります。これは、2、3メッセージで終わるような素早いやりとりには適しているかもしれませんが、会話が長くなればなるほど、データポイントへの影響も大きくなります。Brazeのデータポイントのニュアンスについてご質問があれば、Brazeアカウントマネージャーがお答えします。

### SMSメッセージにリンクを含める {#including-links-in-sms-messages}

Frontライブチャットからリンクを送信すると、追加のHTMLタグとともにレンダリングされます。

### Frontから画像ファイルを添付する {#attaching-image-file-from-front}

Brazeから送信されたSMSメッセージでは、Frontの画像ファイルは表示されません。

### オプトアウト {#opt-outs}

会話型メッセージでは、あいまいなオプトアウトとして認識される可能性のある言葉（「stop」など）が含まれるリスクが高くなります。