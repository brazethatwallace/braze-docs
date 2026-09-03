---
nav_title: LINEクリックトラッキング
article_title: LINEクリックトラッキング
page_order: 2
description: "このページでは、LINEメッセージでクリックトラッキングを有効にする方法、短縮リンクのテスト、トラッキングリンクでのカスタムドメインの使用などについて説明します。"
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# LINEクリックトラッキング {#line-click-tracking}

> このページでは、LINEメッセージでクリックトラッキングを有効にする方法、短縮リンクのテスト、トラッキングリンクでのカスタムドメインの使用などについて説明します。


LINEクリックトラッキングを有効にすると、BrazeはURLを自動的に短縮し、トラッキングメカニズムを追加して、クリックをリアルタイムで記録します。LINEは集計クリックデータを提供しますが、Brazeはタイムリーでアクション可能な詳細なユーザー情報を提供します。このデータにより、クリック動作に基づくユーザーのセグメンテーションや、特定のクリックに応じたメッセージのトリガーなど、よりターゲットを絞ったセグメンテーションおよびリターゲティング戦略を作成できます。

LINEクリックトラッキングは、テキスト、リッチ、カードベースのメッセージで使用できます。ボタン内のリンクや、クリック時のアクションとしてURLが設定されたイメージマップ領域をサポートしています。また、Liquidやカスタムドメインを使用してURLをパーソナライズすることもできます。

## 仕組み {#how-it-works}

LINE のクリックトラッキング設定は、メッセージ作成中に**設定**タブで管理できます。オンにすると、URLはデフォルトのBrazeドメイン（`https://brz.ai`）または購読グループに指定されたカスタムドメインを使用して短縮され、ユーザーごとにパーソナライズされます。

`http://` または `https://` で始まるURLはすべて短縮されます。1つのメッセージに最大25個のURLを含めることができます。Liquidパーソナライゼーション（ユーザーレベルのトラッキングやUTMパラメーターなど）を含む短縮URLは、2か月間有効です。

## クリックトラッキングの設定 {#setting-up-click-tracking}

### テキストメッセージ {#text-messages}

テキストメッセージのクリックトラッキングを設定するには:

1. **テキスト**メッセージをメッセージ作成画面にドラッグし、テキストフィールドにURLを追加します。

![短縮前の長いURLを含むテキストメッセージが表示されたLINEメッセージ作成画面。]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2. **設定**タブに移動し、**クリックトラッキング**がオンになっていることを確認します。クリックトラッキングは、すべての新しいメッセージでデフォルトでオンになっています。

{% alert note %}
短縮リンクのプレビューは、**設定**タブまたは**プレビューとテスト**タブで確認できます。メッセージの作成中は、メッセージ作成画面に完全なリンクが表示されます。
{% endalert %}

![「クリックトラッキング」がオンに切り替えられたLINEメッセージ作成画面の「設定」タブと、短縮URL（https://olaf.brz.ai/p/9rcfdqdD）を含むプレビューテキストメッセージ。]({% image_buster /assets/img/line/click_tracking_settings.png %})

### リッチメッセージ {#rich-messages}

リッチメッセージのクリックトラッキングを設定するには:

1. **リッチメッセージ**をメッセージ作成画面にドラッグし、テンプレートを選択します。
2. 該当するタップ可能エリアの**クリック時の動作**で**URI**を選択します。
3. **URLを開く**フィールドにURLを入力します。

![それぞれURLが設定された2つのタップ可能エリアを持つリッチメッセージが表示されたLINEメッセージ作成画面。]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4. **設定**タブに移動し、**クリックトラッキング**がオンになっていることを確認します。クリックトラッキングは、すべての新しいメッセージでデフォルトでオンになっています。

### カードベースメッセージ {#card-based-messages}

カードベースメッセージのクリックトラッキングを設定するには:

1. **カードベースメッセージ**をメッセージ作成画面にドラッグします。
2. 該当するカードまたはボタンエリアの**クリック時の動作**で**URI**を選択します。

![それぞれURLが設定された2つのボタンを持つカードベースメッセージが表示されたLINEメッセージ作成画面。]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3. **設定**タブに移動し、**クリックトラッキング**がオンになっていることを確認します。クリックトラッキングは、すべての新しいメッセージでデフォルトでオンになっています。

{% alert note %}
**タイトル**フィールドまたは**説明**フィールドのURLは、LINE内でこれらのフィールドがクリック可能ではないため、短縮されません。
{% endalert %}

## カスタムドメイン {#custom-domains}

LINEクリックトラッキングでは、独自のドメインを使用して短縮URLの外観をパーソナライズし、一貫したブランドイメージを表現できます。詳細については、[カスタムドメイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains)を参照してください。

## URLにおけるLiquidパーソナライゼーション {#liquid-personalization-in-urls}

Brazeの作成画面内でURLを動的に構築できるため、URLにダイナミックなUTMパラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートへの誘導や、再入荷した特定の商品へのリンクなど）。
サポートされている任意のLiquidパーソナライゼーションタグを使用して、URLを動的に生成できます。

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

また、次の例に示すように、カスタム定義のLiquid変数を短縮することもできます。

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Liquid変数でレンダリングされるURLの短縮 {#shorten-urls-rendered-by-liquid-variables}

Brazeは、APIトリガープロパティに含まれるものも含め、LiquidによってレンダリングされるURLを短縮します。例えば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}が有効なURLを表す場合、LINEメッセージの送信前にそのURLを短縮しトラッキングします。

## テスト {#testing}

キャンペーンやキャンバスを開始する前に、まずメッセージをプレビューしてテストすることがベストプラクティスです。これを行うには、**テスト**タブに移動して、コンテンツテストグループまたは個々のユーザーに LINE メッセージをプレビューして送信します。

このプレビューは、関連するパーソナライゼーションと短縮 URL で更新されます。

{% alert important %}
アクティブなキャンバス内で下書きが作成された場合、短縮 URL は生成されません。実際の短縮 URL は、キャンバスの下書きがアクティブになったときに生成されます。
{% endalert %}

## レポート {#reporting}

LINEパフォーマンステーブルには、バリアントごとのクリックイベント数と関連するクリック率を示す**合計クリック数**列が含まれています。LINEの指標について詳しくは、[LINEメッセージパフォーマンス]({{site.baseurl}}/user_guide/channels/line/reporting)を参照してください。

![LINEキャンバスステップのパフォーマンス。]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

クリックデータは分析ダッシュボードに自動的にレポートされます。

![LINEパフォーマンス分析ダッシュボード。]({% image_buster /assets/img/line/line_performance.png %})

## ユーザーのリターゲティング {#retargeting-users}

以下のセグメンテーションフィルターとトリガーを使用して、LINEメッセージ内のURLをクリックしたユーザーをリターゲティングできます。

- アクションベースのトリガー
    - キャンペーンに反応
    - ステップに反応

![LINEのアクションベースの配信トリガー。]({% image_buster /assets/img/line/line_action_based.png %})

- セグメンテーションフィルター
    - キャンペーンをクリック/開封
    - タグ付きのキャンペーンまたはキャンバスをクリック/開封
    - ステップをクリック/開封

![「キャンペーンをクリック/開封」、「タグ付きのキャンペーンまたはキャンバスをクリック/開封」、「ステップをクリック/開封」の3つのセグメンテーションフィルターを表示しているフィルターグループ。]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## よくある質問 {#frequently-asked-questions}

### テスト送信時に受け取るリンクは実際のURLですか？ {#are-the-links-i-receive-when-test-sending-real-urls}

はい、テスト送信時に実際のURLが生成されます。ただし、配信済みのキャンペーンで送信されるURLは、テスト送信で送信されるURLと異なる場合があります。

### URLが短縮される前にUTMパラメータを追加できますか？ {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

はい、静的パラメータとダイナミックなパラメータの両方を追加できます。

### 短縮URLはどのくらいの期間有効ですか？ {#how-long-do-shortened-urls-remain-valid}

パーソナライズされたURLは、URL登録時から2か月間有効です。

### URLを短縮するためにBraze SDKをインストールする必要がありますか？ {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

いいえ、クリックトラッキングはSDKの統合なしで機能します。

### どのユーザーがURLをクリックしたか確認できますか？ {#do-i-know-which-individual-users-are-clicking-on-a-url}

はい。クリックトラッキングがオンになっている場合、[LINEリターゲティングフィルター](#retargeting-users)を使用して、URLをクリックしたユーザーをリターゲティングできます。

### クリックトラッキングはディープリンクやユニバーサルリンクで機能しますか？ {#does-click-tracking-work-with-deep-links-or-universal-links}

クリックトラッキングはディープリンクでは機能しません。BranchやAppsFlyer などのプロバイダーからのユニバーサルリンクを短縮することはできますが、その際に発生する可能性のある問題（アトリビューションの破損やリダイレクトの失敗など）について、Brazeはトラブルシューティングを行うことができません。

### LINEアプリでのプレビューはクリックとしてカウントされますか？ {#do-previews-on-the-line-app-count-as-clicks}

いいえ、LINEメッセージのクリック率には含まれません。