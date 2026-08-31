---
nav_title: LINE メッセージの作成
article_title: LINE メッセージの作成
page_order: 1
description: "LINEメッセージを作成し、チャネル固有のメッセージタイプ、フィールド、クリックトラッキング、配信設定、および動作を設定します。"
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - LINE
alias: /line/create/
---

# LINE メッセージの作成 {#create-a-line-message}

> キャンペーンやキャンバスでパーソナライズされたLINEメッセージを作成します。テキスト、画像、リッチ、カードベースのメッセージから選択し、1回の送信で最大5つのメッセージを組み合わせることができます。

## 前提条件 {#prerequisites}

始める前に、以下の要件を満たしていることを確認してください。

| 要件 | 説明 |
| --- | --- |
| LINE接続 | [LINE設定]({{site.baseurl}}/user_guide/channels/line/line_setup)を完了し、チャネルのポリシー、制限、コンテンツルールを確認してください。 |
| キャンペーンまたはキャンバス | 単一のターゲットメッセージにはキャンペーンを、マルチステップのユーザージャーニーにはキャンバスを使用します。 |
| メッセージプラン | コンテンツ、画像、リンク、購読グループを準備します。 |
| メッセージクレジットまたはアクションクレジット | アカウントにクレジットの残高があることを確認してください。BrazeからLINEメッセージを送信するにはこれらのクレジットが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINEメッセージの前提条件" }

## メッセージの作成 {#create-a-message}

### ステップ1：メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **LINE**を選択するか、複数のチャネルをターゲットとするキャンペーンの場合は**マルチチャネルキャンペーン**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、キャンペーンをより簡単に見つけ、レポートで活用できます。
5. キャンペーンのバリアントを追加して名前を付けます。各バリアントでは異なるメッセージタイプとレイアウトを使用できます。詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーンのバリアントに類似したコンテンツが含まれる場合は、最初のメッセージを作成してからバリアントを追加してください。**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### ステップ2：購読グループを選択する {#step-2-select-a-subscription-group}

メッセージを送信するLINEチャネルに関連付けられた**購読グループ**を選択します。エディターを起動する前に購読グループが必要です。

LINEキャンペーンのすべてのバリアントは同じ購読グループを使用する必要があります。LINEの購読ステータスの詳細については、[LINE購読グループ]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups)を参照してください。

### ステップ3：LINEメッセージを作成する {#step-3-compose-your-line-message}

**エディターを起動**を選択し、メッセージタイプをエディターにドラッグします。1回の送信で最大5つのメッセージを組み合わせ、ユーザーが受信する順序に並べ替えることができます。

![プレビューにメッセージが表示されたLINEコンポーザー。]({% image_buster /assets/img/line/line_composer.png %})

#### メッセージタイプ {#message-types}

| メッセージタイプ | フィールドと設定 | 制限と動作 |
| --- | --- | --- |
| **テキスト** | 絵文字、Liquid、URLを含むメッセージ本文 | 最大5,000文字。 |
| **画像** | メディアライブラリまたはURL（ダイナミックURLを含む）からの画像 | 画像URLには最大2,000文字を含められます。スタンドアロンの画像メッセージはクリックアクションをサポートしません。 |
| **リッチメッセージ** | 画像、代替テキスト、テンプレート、およびURIアクションを持つタップ可能領域 | 代替テキストには最大400文字を含められます。1～50個のタップ可能領域を追加できます。アクションラベルには最大100文字、各URIには最大1,000文字を含められます。 |
| **カードベースメッセージ** | オプションの画像とヘッダー、必須の本文、およびURIアクションを持つ最大10枚のカード | 代替テキストには最大400文字を含められます。ヘッダーには最大40文字を含められます。本文には画像またはヘッダーがある場合は最大60文字、どちらもない場合は最大120文字を含められます。各カードには最大20文字のラベルを持つ1～3個のアクションが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="LINEメッセージタイプ、フィールド、制限" }

文字制限にはLiquid構文は含まれません。

画像の仕様、リッチメッセージテンプレート、カルーセル画像の設定、および例については、[LINEメッセージタイプ]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/message_types)を参照してください。

{% alert note %}
カードベースメッセージでは、同じオプションフィールドとアクション数がすべてのカードに適用されます。たとえば、1つのカードに画像と2つのアクションを含める場合、すべてのカードに画像と2つのアクションを含める必要があります。
{% endalert %}

#### クリック時の動作 {#on-click-behavior}

リッチメッセージとカードのタップ可能領域については、**クリック時の動作**で**URI**を選択し、**URLを開く**にリンク先を入力します。URLをLINE内で開くかどうかを選択します。

#### パーソナライゼーション {#personalization}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)または[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)を使用して、テキスト、画像、URLをパーソナライズします。Liquidパーソナライゼーションにはデフォルト値を含めて、不完全なデータを持つプロファイルが空白のコンテンツを受信しないようにしてください。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

右から左に書く言語については、[右から左のメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

### ステップ4：クリックトラッキングを設定する {#step-4-configure-click-tracking}

**Settings**タブで、**Click Tracking**を使用して送信時にリンクを短縮およびトラッキングします。クリックトラッキングは新しいメッセージではデフォルトで有効になっており、テキスト、リッチ、カードベースメッセージのHTTPおよびHTTPS URLに適用されます。

Brazeは`https://brz.ai`または購読グループに設定されたカスタムドメインを使用します。トラッキングURLはLiquidでパーソナライズできます。メッセージタイプ別の設定、テスト動作、カスタムドメイン、リターゲティングについては、[LINEクリックトラッキング]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/line_click_tracking)を参照してください。

### ステップ5：メッセージをプレビューしてテストする {#step-5-preview-and-test-your-message}

**Preview & Test**タブに移動して、ユーザーとしてメッセージをプレビューするか、コンテンツテストグループまたは個々のユーザーにテストLINEメッセージを送信します。

![テストメッセージのプレビューが表示されたPreview & Testタブ。]({% image_buster /assets/img/line/test_preview.png %})

テスト要件と手順については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line)を参照してください。

### ステップ6：キャンペーンまたはキャンバスの残りを構築する {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

#### 配信スケジュールまたはトリガーを選択する {#choose-a-delivery-schedule-or-trigger}

LINEメッセージをスケジュールされた時間に配信するか、アクションまたはAPIトリガーに応じて配信します。スケジュールとトリガーのオプションについては、[キャンペーンのスケジュール]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

[再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility)や[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)などの配信コントロールを設定します。アクションベースの配信の場合は、キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定します。

#### ターゲットユーザーを選択する {#choose-users-to-target}

セグメントとフィルターを選択して[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)します。Brazeはメッセージを送信する前に正確なセグメントメンバーシップを計算します。

LINEは各ユーザーの購読ステータスを制御します。ユーザーがメッセージを受信するには、`native_line_id`を持ち、選択した購読グループに関連付けられたLINEチャネルをフォローしている必要があります。詳細については、[LINE購読ステータス]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#line)を参照してください。

#### コンバージョンイベントを選択する {#choose-conversion-events}

[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)を使用して、ユーザーがキャンペーンを受信した後のアクションを測定します。最大30日間のコンバージョンウィンドウを設定します。

{% endtab %}
{% tab キャンバス %}

キャンバスの残りのセクションを完成させます。エントリスケジュール、オーディエンス設定、送信コントロールについては、[キャンバスの作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)を参照してください。

インバウンドLINEメッセージを使用して、トリガーワードに基づいてキャンバスを開始または分岐させることができます。動作と大文字小文字の要件については、[LINEユーザーへのメッセージング]({{site.baseurl}}/user_guide/channels/line/message_users)を参照してください。

{% endtab %}
{% endtabs %}

### ステップ7：確認してデプロイする {#step-7-review-and-deploy}

キャンペーンまたはキャンバスの構築が完了したら、詳細を確認し、送信前にメッセージをテストしてください。

ローンチ後は、[LINEレポート]({{site.baseurl}}/user_guide/channels/line/reporting)を使用してメッセージのパフォーマンスを確認します。

## 知っておくべきこと {#things-to-know}

- LINEメッセージには、1つから5つのメッセージバブルを含めることができます。
- 購読グループは1つのLINEチャネルにマッピングされ、キャンペーン内のすべてのバリアントは同じ購読グループを使用する必要があります。
- LINEが購読ステータスの信頼できる情報源です。選択したLINEチャネルをフォローしていないユーザーにはメッセージが配信されません。
- LINEは、特定の日に20人以上のユーザーがイベントを実行した場合にのみ、開封およびクリック関連の統計を計算します。