---
nav_title: KakaoTalk メッセージの作成
article_title: KakaoTalk メッセージの作成
description: "このリファレンス記事では、KakaoTalk メッセージの作成方法について説明します。"
page_order: 1
alias: /create_kakaotalk_message/
channel:
  - KakaoTalk
---

# KakaoTalk メッセージの作成 {#create-a-kakaotalk-message}

> [KakaoTalk メッセージングチャネル]({{site.baseurl}}/kakaotalk)を使用して、KakaoTalkプラットフォームを通じてユーザーに直接リーチできます。Liquidやその他のダイナミックなコンテンツを使用してパーソナライズされたユーザー体験を作成し、ブランドとの豊かなユーザー体験を促進・強化する環境を構築しましょう。<br><br>KakaoTalk メッセージングチャネルの設定については、[KakaoTalk のセットアップ]({{site.baseurl}}/kakaotalk_setup)を参照してください。

## ステップ 1:メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

KakaoTalkはキャンペーンとキャンバスの両方でサポートされています。キャンペーンは単一のメッセージングキャンペーンに最適であり、キャンバスはマルチステップ、マルチチャネルのユーザージャーニーをオーケストレーションできます。

{% tabs local %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン** に移動し、**キャンペーンを作成**を選択します。
2. 単一チャネルのキャンペーンの場合は **KakaoTalk** を、複数チャネルのキャンペーンの場合は **Multichannel キャンペーン** を選択します。

![メッセージングチャネルを選択するオプションのパネル。]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. キャンペーンにバリアントを追加して、異なるメッセージタイプやレイアウトを選択できます。詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% endtab %}
{% tab キャンバス %}

1. [キャンバスを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. キャンバスビルダーでメッセージステップを追加し、**KakaoTalk** を選択します。

![キャンバスメッセージングチャネルの選択。]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## ステップ 2:KakaoTalk メッセージを作成する {#step-2-compose-your-kakaotalk-message}

1. **KakaoTalk チャネル**ドロップダウンを選択すると、テクノロジーパートナーページで設定したKakaoTalkチャネルのリストが表示されます。メッセージの送信に使用するKakaoTalkチャネルを選択します。
2. 送信するメッセージタイプを選択します:
- テキスト
- 画像
- リストアイテム
    - ナロー
    - ワイド

![3種類のメッセージから選択できるKakaoTalkバリアントセクション。]({% image_buster /assets/img/kakaotalk/kakaotalk_variants.png %})

{% tabs local %}
{% tab テキスト %}

KakaoTalkテキストメッセージは、最もシンプルなコミュニケーション形式で、標準的なテキストメッセージです。

### 仕様 {#specifications}

| 項目 | 仕様 |
| --- | --- |
| コンテンツ | 絵文字やLiquidパーソナライゼーションを含むテキストコンテンツ |
| テキスト容量 | 最大1,000文字 |
| ボタン | 最大5つのオプションボタン。現在、クリック時にURLを開く用途にのみ使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="仕様" }

![コンポーザーでのKakaoTalkテキストメッセージ。]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

{% endtab %}
{% tab 画像 %}

画像メッセージは、ビジュアル要素とサポートテキストを組み合わせたメッセージです。BrazeはKakaoTalkサーバーへの画像アップロードを自動的に処理します。

### 一般仕様 {#general-specifications}

| 項目 | 仕様 |
| --- | --- |
| コンテンツ | 1つの画像とサポートテキスト |
| 対応ファイル形式 | JPEGまたはPNG |
| 推奨幅 | 500px |
| ファイルサイズ | 最大500kb |
| アスペクト比 | 2:1（ワイド）から3:4（トール）の間 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="一般仕様" }

ナロー画像メッセージとワイド画像メッセージでは、文字数とボタンの考慮事項が異なります。

{% subtabs %}
{% subtab ナロー画像 %}

#### ナロー画像 {#narrow-image}

ナロー画像メッセージは、やや縦長のナロー画像と、より充実したテキストおよびボタンオプションを備えています。

##### 仕様

| 項目 | 仕様 |
| --- | --- |
| コンテンツ | 1つの画像とサポートテキスト |
| テキスト容量 | 最大500文字 |
| ボタン | 最大5つのオプションボタン |
| 画像ソース | Brazeメディアライブラリまたは直接URLから画像を追加できます |
| カスタマイズ | 画像のクリック時の動作を指定できます |
{: .reset-td-br-1 .reset-td-br-2 aria-label="仕様" }

![KakaoTalkナローメッセージ。]({% image_buster /assets/img/kakaotalk/narrow_image.png %})

{% endsubtab %}
{% subtab ワイド画像 %}

#### ワイド画像 {#wide-image}

ワイド画像メッセージは、インパクトの高いビジュアルコミュニケーションに適した目立つワイド画像と、最小限のサポートテキストを備えています。

##### 仕様

| 項目 | 仕様 |
| --- | --- |
| コンテンツ | 1つの画像とサポートテキスト |
| テキスト容量 | 最大76文字 |
| ボタン | 最大2つのオプションボタン |
| 画像ソース | Brazeメディアライブラリまたは直接URLから画像を追加できます |
| カスタマイズ | 画像のクリック時の動作を指定できます |
{: .reset-td-br-1 .reset-td-br-2 aria-label="仕様" }

![KakaoTalkワイドメッセージ。]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### 画像の追加 {#add-images}

Brazeメディアライブラリを通じて、またはJPEGやPNGファイルをホストするURLを貼り付けて画像を追加できます。画像のクリック時の動作を指定して、クリックしたユーザーを特定のURLにリダイレクトすることもできます。

BrazeはKakaoTalkの画像アップロード要件をすべて自動的に処理するため、メッセージ送信前にKakaoTalkプロバイダーに画像をアップロードする必要は**ありません**。画像をアップロードして、Brazeから直接メッセージを送信するだけです！

![ナロー画像を追加するためのアイコンが選択されたセクション。]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab リストアイテム %}


KakaoTalkアイテムリストメッセージは、コンテンツアイテムのリストを明確な縦型フォーマットで表示するように設計されています。

リストアイテムメッセージは、ヘッダー、アイテムリストセクション、およびオプションのボタンエリアで構成されます。

#### 仕様

| 項目 | 仕様 |
| --- | --- |
| アイテム数 | 最低2つまたは3つのアイテムが必要 |
| ボタン | 最大5つのオプションボタン |
| ヘッダー | 最大250文字 |
| アイテムタイトル | 最大25文字 |
| WebサイトURL（アイテムごと） | 最大250文字 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="仕様" }

![KakaoTalkリストアイテムメッセージ。]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% endtabs %}


## ステップ 3:クリックトラッキングを設定する {#step-3-set-up-click-tracking}

KakaoTalkクリックトラッキングをオンにすると、BrazeはURLを自動的に短縮し、トラッキングメカニズムを追加して、リアルタイムでクリックを記録します。このデータにより、クリック動作に基づくユーザーのセグメンテーションや、特定のクリックに応じたメッセージのトリガーなど、よりターゲットを絞ったセグメンテーションおよびリターゲティング戦略を作成できます。

クリックトラッキングは、テキスト、画像、リストアイテムメッセージでサポートされています。ボタン内のリンクと画像のクリック時アクションをサポートしています。Liquidやカスタムドメインを使用してURLをパーソナライズすることもできます。

クリックトラッキングを有効にするには、コンポーザーの**リンクオプション**セクションで**クリックトラッキング**にチェックを入れます。URLはデフォルトのBrazeドメイン（`https://brz.ai`）またはサブスクリプショングループに指定されたカスタムドメインを使用して短縮され、ユーザーごとにパーソナライズされます。

クリックトラッキング、カスタムドメイン、URLでのLiquidパーソナライゼーション、レポート、リターゲティングの詳細については、[KakaoTalkクリックトラッキング]({{site.baseurl}}/kakaotalk_click_tracking)を参照してください。

### ユーザーのリターゲティング {#retargeting-users}

以下のセグメンテーションフィルターとトリガーを使用して、KakaoTalkメッセージ内のURLをクリックしたユーザーをリターゲティングできます。

- アクションベースのトリガー
    - キャンペーンとのインタラクション
    - ステップとのインタラクション

- セグメンテーションフィルター
    - キャンペーンのクリック/開封
    - タグ付きキャンペーンまたはキャンバスのクリック/開封
    - ステップのクリック/開封

## ステップ 4:KakaoTalk メッセージをプレビューしてテストする {#step-4-preview-and-test-your-kakaotalk-message}

KakaoTalkメッセージを作成すると、メッセージプレビューが自動的に更新されます。テストの準備ができたら、**テスト**タブに移動して、コンテンツテストグループまたは個々のユーザーにテストメッセージを送信するか、Braze内で既存のユーザーまたはカスタムユーザーとしてメッセージをプレビューします。

テストユーザーを選択した後、**テスト送信**を選択します。テスト送信の結果を示す通知が表示されます。CJ OliveNetworksの場合、「C100」レスポンスが返されます。別のエラーが表示された場合は、[CJ KakaoTalkユーザードキュメント](https://developers.kakao.com/docs/latest/en/index)を参照してください。

![KakaoTalkメッセージのプレビューウィンドウ。]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
既存のユーザーにテストメッセージをプレビューおよび送信するには、「View PII」権限が必要です。カスタムユーザーへのテストメッセージのプレビューと送信には、この権限は不要です。
{% endalert %}

送信結果の確認や問題のトラブルシューティングを行うには、**設定** > **メッセージアクティビティログ**に移動します。詳細については、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)を参照してください。

## ステップ 5:キャンペーンまたはキャンバスの残りの部分を構築する {#step-5-build-the-remainder-of-your-campaign-or-canvas}

KakaoTalkメッセージを構築するためのツールの最適な使用方法については、以下のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する {#choose-delivery-schedule-or-trigger}

KakaoTalkメッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。スケジュールとトリガーオプションの詳細については、[キャンペーンのスケジュール]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)または[エントリスケジュールタイプ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#entry-schedule-types)（キャンバスの場合）を参照してください。

ユーザーがキャンペーンを再度受信できるようにしたり、フリークエンシーキャップルールをオンにしたりするなど、配信コントロールを指定できます。アクションベースの配信では、キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)も設定できます。

### ターゲットユーザーを選択する {#choose-users-to-target}

セグメントやフィルターを選択してオーディエンスを絞り込み、ユーザーをターゲットにします。現時点では、KakaoTalkはチャネルのフレンドにのみメッセージを送信できます。チャネルフレンドを示すカスタム属性を設定して、ユーザーを適切にセグメンテーションし、受信できないユーザーへのKakaoTalkメッセージ送信を回避することをお勧めします。

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（コンバージョンイベント）を実行する頻度をトラッキングできます。ユーザーが指定されたアクションを実行した場合にコンバージョンとしてカウントされる最大30日間の時間枠を設定するオプションがあります。

コンバージョンイベントは、キャンペーンの成功を測定するのに役立ちます。たとえば、ユーザーにアプリの使用を促進しようとしている場合、コンバージョンイベントを**Starts Session**に設定します。

特定のユースケースに基づいてカスタムコンバージョンイベントを設定することもできます。クリエイティブに考えて、キャンペーンの成功をどのように測定したいかを検討してください。

## ステップ 6:確認してデプロイする {#step-6-review-and-deploy}

キャンペーンまたはキャンバスの最後の構築が完了したら、詳細を確認し、テストして、送信しましょう！