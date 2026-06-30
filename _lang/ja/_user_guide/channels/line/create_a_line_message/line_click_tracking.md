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

LINEクリックトラッキングの設定は、メッセージ作成中に**Settings**タブで管理できます。有効にすると、URLはデフォルトのBrazeドメイン（`https://brz.ai`）またはサブスクリプショングループに指定されたカスタムドメインを使用して短縮され、ユーザーごとにパーソナライズされます。

`http://`または`https://`で始まるURLはすべて短縮されます。1つのメッセージに最大25個のURLを含めることができます。Liquidパーソナライゼーション（ユーザーレベルのトラッキングやUTMパラメーターなど）を含む短縮URLは、2か月間有効です。

## クリックトラッキングの設定 {#setting-up-click-tracking}

### テキストメッセージ {#text-messages}

テキストメッセージのクリックトラッキングを設定するには：

1. **Text**メッセージを作成画面にドラッグし、テキストフィールドにURLを追加します。

![長いURLを含むTextメッセージが表示されたLINEメッセージ作成画面]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2. **Settings**タブに移動し、**Click Tracking**が有効になっていることを確認します。クリックトラッキングは、すべての新しいメッセージでデフォルトで有効になっています。

{% alert note %}
短縮リンクのプレビューは、**Settings**タブまたは**Preview & Test**タブで確認できます。メッセージの作成中は、作成画面に完全なリンクが表示されます。
{% endalert %}

![「Click Tracking」がオンに切り替えられたLINEメッセージ作成画面の「Settings」タブと、短縮URLを含むプレビューテキストメッセージ]({% image_buster /assets/img/line/click_tracking_settings.png %})

### リッチメッセージ {#rich-messages}

リッチメッセージのクリックトラッキングを設定するには：

1. **Rich message**を作成画面にドラッグし、テンプレートを選択します。
2. 該当するタップ可能な領域の**On-click behavior**で**URI**を選択します。
3. **Open URL**フィールドにURLを入力します。

![それぞれURLが設定された2つのタップ可能な領域を持つリッチメッセージが表示されたLINEメッセージ作成画面]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4. **Settings**タブに移動し、**Click Tracking**が有効になっていることを確認します。クリックトラッキングは、すべての新しいメッセージでデフォルトで有効になっています。

### カードベースメッセージ {#card-based-messages}

カードベースメッセージのクリックトラッキングを設定するには：

1. **Card-based message**を作成画面にドラッグします。
2. 該当するカードまたはボタン領域の**On-click behavior**で**URI**を選択します。

![それぞれURLが設定された2つのボタンを持つカードベースメッセージが表示されたLINEメッセージ作成画面]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3. **Settings**タブに移動し、**Click Tracking**が有効になっていることを確認します。クリックトラッキングは、すべての新しいメッセージでデフォルトで有効になっています。

{% alert note %}
**Title**または**Description**フィールドのURLは、LINE内でこれらのフィールドがクリック可能ではないため、短縮されません。
{% endalert %}

## カスタムドメイン {#custom-domains}

LINEクリックトラッキングでは、独自のドメインを使用して短縮URLの外観をパーソナライズし、一貫したブランドイメージを表現できます。詳細については、[カスタムドメイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains/)を参照してください。

## URLでのLiquidパーソナライゼーション {#liquid-personalization-in-urls}

Brazeの作成画面内で直接URLを動的に構築できるため、URLにダイナミックUTMパラメーターを追加したり、ユーザーに固有のリンクを送信したりできます（放棄カートへの誘導や、再入荷した特定の製品への誘導など）。URLは、サポートされているLiquidパーソナライゼーションタグを使用して動的に生成できます。

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

以下の例のように、カスタム定義のLiquid変数を短縮することもできます。

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Liquid変数でレンダリングされたURLの短縮 {#shorten-urls-rendered-by-liquid-variables}

Brazeは、APIトリガープロパティに含まれるURLも含め、LiquidでレンダリングされたURLを短縮します。たとえば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}が有効なURLを表す場合、LINEメッセージを送信する前にそのURLを短縮してトラッキングします。

## テスト {#testing}

キャンペーンまたはキャンバスを起動する前に、まずメッセージをプレビューしてテストすることがベストプラクティスです。これを行うには、**Test**タブに移動して、コンテンツテストグループまたは個々のユーザーにLINEメッセージをプレビューして送信します。

このプレビューは、関連するパーソナライゼーションと短縮URLで更新されます。

{% alert important %}
アクティブなキャンバス内で下書きが作成された場合、短縮URLは生成されません。実際の短縮URLは、キャンバスの下書きがアクティブになったときに生成されます。
{% endalert %}

## レポート {#reporting}

LINEパフォーマンステーブルには、バリアントごとのクリックイベント数と関連するクリック率を示す**Total Clicks**列が含まれています。LINE指標の詳細については、[LINEメッセージパフォーマンス]({{site.baseurl}}/user_guide/channels/line/reporting/)を参照してください。

![LINEキャンバスステップのパフォーマンス]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

クリックデータは分析ダッシュボードに自動的にレポートされます。

![LINEパフォーマンス分析ダッシュボード]({% image_buster /assets/img/line/line_performance.png %})

## ユーザーのリターゲティング {#retargeting-users}

LINEメッセージ内のURLをクリックしたユーザーを、以下のセグメンテーションフィルターとトリガーを使用してリターゲティングできます。

- アクションベースのトリガー
    - キャンペーンとのインタラクション
    - ステップとのインタラクション

![LINEアクションベースの配信トリガー]({% image_buster /assets/img/line/line_action_based.png %})

- セグメンテーションフィルター
    - キャンペーンのクリック/開封
    - タグ付きキャンペーンまたはキャンバスのクリック/開封
    - ステップのクリック/開封

![「キャンペーンのクリック/開封」、「タグ付きキャンペーンまたはキャンバスのクリック/開封」、「ステップのクリック/開封」の3つのセグメンテーションフィルターを表示するフィルターグループ]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## よくある質問 {#frequently-asked-questions}

### テスト送信で受け取るリンクは実際のURLですか？ {#are-the-links-i-receive-when-test-sending-real-urls}

はい、テスト送信時に実際のURLが生成されます。ただし、起動されたキャンペーンで送信される正確なURLは、テスト送信で送信されたものとは異なる場合があります。

### URLが短縮される前にUTMパラメーターを追加できますか？ {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

はい、静的パラメーターとダイナミックパラメーターの両方を追加できます。

### 短縮URLはどのくらいの期間有効ですか？ {#how-long-do-shortened-urls-remain-valid}

パーソナライズされたURLは、URL登録時から2か月間有効です。

### URLを短縮するためにBraze SDKをインストールする必要がありますか？ {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

いいえ、クリックトラッキングはSDK統合なしで機能します。

### URLをクリックした個々のユーザーを特定できますか？ {#do-i-know-which-individual-users-are-clicking-on-a-url}

はい。クリックトラッキングが有効になっている場合、[LINEリターゲティングフィルター](#retargeting-users)を使用して、URLをクリックしたユーザーをリターゲティングできます。

### クリックトラッキングはディープリンクやユニバーサルリンクで機能しますか？ {#does-click-tracking-work-with-deep-links-or-universal-links}

クリックトラッキングはディープリンクでは機能しません。BranchやAppsFlyerなどのプロバイダーからのユニバーサルリンクを短縮することはできますが、その際に発生する可能性のある問題（アトリビューションの破損やリダイレクトの失敗など）についてBrazeはトラブルシューティングできません。

### LINEアプリでのプレビューはクリックとしてカウントされますか？ {#do-previews-on-the-line-app-count-as-clicks}

いいえ、LINEメッセージのクリック率には寄与しません。