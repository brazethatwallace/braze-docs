---
nav_title: eコマース推奨イベントの使用
article_title: eコマース推奨イベントの使い方
page_type: reference
alias: /ecommerce_events/
description: "Brazeでeコマース推奨イベントを使用する方法について、サポートされている機能、主要な指標、セグメンテーション・メッセージング・レポートのベストプラクティスを含めて説明します。"
---

# eコマースイベントの使い方 {#how-to-use-ecommerce-events}

> eコマースの[推奨イベント]({{site.baseurl}}/recommended_events)は、共有された注文レベルのスキーマを使用しており、Brazeがeコマースデータの上に信頼性の高い機能を構築できるようにします。これには、ユーザープロファイル、セグメンテーション、メッセージング、レポート、AIを活用したレコメンデーションが含まれます。この記事の各セクションでは、Brazeで各機能を使用する方法について説明します。<br><br> プロパティの要件とデータタイプについては[イベントスキーマ]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas)を、イベントがバリデーションに失敗した場合の動作については[イベントのバリデーションとトラブルシューティング]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-validation-and-troubleshooting)を参照してください。

eコマースイベントは予測可能なスキーマに従っているため、Brazeは収益トラッキングや構築済みのCanvasテンプレートからAIを活用したレコメンデーションまで、信頼性の高い機能を構築できます。以下のセクションでは、各機能の概要と詳細ドキュメントへのリンクを紹介します。

{% alert note %}
Brazeのeコマースイベントとそのセグメント可能なイベントプロパティは、[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points)にカウントされません。
{% endalert %}

<a id="transactions-tab" aria-hidden="true"></a>

## コマースタブ {#commerce-tab}

各ユーザープロファイルの**コマース**タブは、**注文アクティビティ**（計算された収益と注文の指標）と**アクティブカート**（`ecommerce.cart_updated`イベントからの最新のカート）の2つのモジュールで構成されています。

### 注文アクティビティ {#order-activity}

**注文アクティビティ**モジュールは、イベントが処理されるとリアルタイムで更新される3つの計算指標を表示します。これらの計算の注文レベルモデルにより、製品価格と注文合計値が明確に分離されます。

{% alert note %}
eコマース推奨イベントは、**コマース**タブの**購入履歴**セクションには表示されません。購入履歴はレガシー購入イベントによって入力されます。推奨イベントからの収益と注文アクティビティについては、以下の表の指標を使用してください。
{% endalert %}

| 指標 | 計算式 |
| ----- | ----- |
| 合計収益 | sum (`order_placed.total_value`) − sum (`order_refunded.total_value`) |
| 合計注文数 | count (distinct `order_placed`) − count (distinct `order_cancelled`) |
| 合計返金額 | sum (`order_refunded.total_value`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="注文アクティビティの指標" }

### アクティブカート {#active-cart}

**アクティブカート**モジュールは、ユーザープロファイル上の最新のカートを表示します。このビューはテスト中に特に役立ちます。カートの内容を確認したり、カートベースのジャーニーを検証したり、`ecommerce.cart_updated`イベントが期待どおりにプロファイルを更新しているかを確認したりできます。

**アクティブカート**には以下が含まれます:

- **カートID** — 最後に`ecommerce.cart_updated`イベントを受信したカートの識別子。
- **最終更新日時** — 最新のカート更新のタイムスタンプ。
- **カート合計値** — 現在のカート内のラインアイテムの合計値。
- **製品を表示** — カート内の製品リストを開くリンク（最大50製品）。

## eコマースオーケストレーション {#ecommerce-orchestration}

### セグメンテーション {#segmentation}

Brazeは、eコマースデータに基づいてユーザーをセグメント化する3つの方法を提供しています:

- **eコマースフィルター:** セグメンターの**eコマース**カテゴリを使用します。このカテゴリには、eコマース推奨イベントを活用したフィルター（**Last Order Placed**、**Total Revenue**、**Average Order Value**など）が含まれています。利用可能なフィルターの完全なリストについては、[Segmentフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を参照してください。
- **カスタムイベントフィルター:** eコマースイベントはカスタムイベントと同様に動作するため、既存のカスタムイベントフィルターがすべてそのまま使用できます。例えば、「カスタムイベント`ecommerce.order_placed`をX回以上実行した」や「カスタムイベント`ecommerce.order_placed`を最初に実行した」でフィルタリングできます。
- **セグメントエクステンション:** ネストされた製品配列やメタデータオブジェクトのプロパティを含むネストされたイベントプロパティでセグメント化するには、ネストされたイベントプロパティフィルタリングを備えた[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)を使用してください。これにより、「過去90日間に製品SKU-123を購入したユーザー」のようなオーディエンスを構築したり、同じ注文の異なるプロパティにまたがる条件を組み合わせたりできます。

{% alert important %}
eコマース推奨イベント向けのセグメントエクステンションは有料機能であり、早期アクセス中です。早期アクセスへの参加に興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。ネストされたプロパティのセグメンテーションをチームに推奨する前に、お使いのプランにアクセス権が含まれていることを確認してください。
{% endalert %}

### トリガー {#triggering}

他のカスタムイベントと同様に、Braze全体でeコマースイベントを使用してカスタムイベント実行トリガーを設定できます。放棄カートフローの場合は、**Perform Cart Updated Event**トリガーを使用して、カートの更新を適切にキャプチャしてください。

さらに、Brazeは専用の**Places Order**トリガーを提供しており、任意の注文確定時、または特定の製品を含む注文時にジャーニーを開始したりアクションを実行したりできます。このトリガーは、製品名、`product_id`、または`variant_id`でフィルタリングして、特定の購入シナリオをターゲットにできます。詳細については、[アクションベースの配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)を参照してください。

![任意の注文を確定するオプションが選択されたPlaces Orderトリガー。]({% image_buster /assets/img/recommended_events/places_order_trigger.png %})

### Liquidパーソナライゼーション {#liquid-personalization}

eコマースイベントは、カスタムイベントと同じ方法で[Liquidパーソナライゼーション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)をサポートしています。メッセージング内でイベントプロパティを直接参照できます。製品画像、価格、その他のカタログデータをメッセージに取り込むには、`product_id`または`variant_id`をリンク識別子として使用して、カタログとイベントを結合してください。{% raw %}`{% shopping_cart %}`{% endraw %} Liquidタグを使用すると、放棄カートリマインダー、チェックアウト促進、注文確認のために、ユーザーの現在のカート内容をループ処理できます。すぐに使えるコードサンプルについては、[eコマースユースケース]({{site.baseurl}}/ecommerce_use_cases)を参照してください。

ノーコードの代替手段として、[ドラッグ＆ドロップ製品ブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks)が早期アクセスプログラムで利用可能です。

### eコマースCanvasテンプレート {#ecommerce-canvas-templates}

Brazeは、eコマース推奨イベントをエントリ、終了、コンバージョン条件として事前設定した、すぐに使えるCanvasテンプレートを提供しています。カスタムセットアップなしでライフサイクルフローを起動できます。各テンプレートにはドラッグ＆ドロップのメールデザインが含まれており、ドラッグ＆ドロップ製品ブロック（現在早期アクセス中）をサポートしています。詳細なユースケースとLiquidの例については、[eコマースユースケース]({{site.baseurl}}/ecommerce_use_cases)を参照してください。

これらのテンプレートは、最も一般的なeコマースライフサイクルフローをカバーしています。出発点として使用し、タイミング、チャネル、クリエイティブをオーディエンスに合わせてカスタマイズしてください。

{% tabs %}
{% tab 閲覧放棄 %}

製品を閲覧したがカートに追加しなかったユーザーを再エンゲージします。

最近閲覧したが行動しなかった製品を検討するようユーザーを呼び戻したい場合に、このテンプレートを使用してください。

| 設定 | 値 |
| --- | --- |
| エントリイベント | `ecommerce.product_viewed` |
| 終了イベント | `ecommerce.product_viewed`、`ecommerce.cart_updated`、`ecommerce.checkout_started`、Placed Order |
| コンバージョンイベント | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eコマースCanvasテンプレート" }

{% endtab %}
{% tab カート放棄 %}

カートにアイテムを追加したがチェックアウトを開始しなかったユーザーを回復します。

カート内のアイテムについてユーザーにリマインドし、チェックアウトを完了するよう促したい場合に、このテンプレートを使用してください。

| 設定 | 値 |
| --- | --- |
| エントリイベント | `ecommerce.cart_updated` |
| 終了イベント | `ecommerce.cart_updated`、`ecommerce.checkout_started`、Placed Order |
| コンバージョンイベント | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eコマースCanvasテンプレート" }

{% alert tip %}
`ecommerce.cart_updated`イベントはカート全体の置換（各イベントでカート全体を記述）またはオプションの`action`プロパティの`add`と`remove`の値を使用した増分更新をサポートしています。カートごとにいずれかのアプローチを選択し、同じ`cart_id`に対して置換と増分カート更新を混在させないでください。メッセージ内で{% raw %}`{% shopping_cart %}`{% endraw %} Liquidタグを使用して、送信時の現在のカート内容を動的に表示してください。
{% endalert %}

{% endtab %}
{% tab チェックアウト放棄 %}

チェックアウトを開始したが購入を完了しなかったユーザーを回復します。

ファネルの最も購入意欲が高い段階で購入を回復したい場合に、このテンプレートを使用してください。

| 設定 | 値 |
| --- | --- |
| エントリイベント | `ecommerce.checkout_started` |
| 終了イベント | Placed Order |
| コンバージョンイベント | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eコマースCanvasテンプレート" }

{% endtab %}
{% tab 注文確認とアンケート %}

購入の成功を確認し、レビュー収集と購入後のエンゲージメントを促進するフィードバックアンケートでフォローアップします。

購入後のコミュニケーションを効率化し、単一のワークフローで顧客フィードバックを収集したい場合に、このテンプレートを使用してください。

| 設定 | 値 |
| --- | --- |
| エントリイベント | `ecommerce.order_placed` |
| コンバージョンイベント | セッション開始または`ecommerce.product_viewed` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eコマースCanvasテンプレート" }

{% endtab %}
{% endtabs %}

#### テンプレートのカスタマイズ {#customize-templates}

これらのテンプレートは出発点として設計されています。一般的なカスタマイズには以下が含まれます:
  - **メールのカスタマイズ:** 各テンプレートには、ドラッグ＆ドロップエディターで構築された事前設定済みのメールが含まれており、ブランドやコンテンツに合わせて完全に編集可能です。
  - **チャネルの追加:** メールにプッシュ、SMS、またはアプリ内メッセージを組み合わせて、クロスチャネルの強化を図ります。
  - **遅延と条件分岐の追加:** 動作（例: 高額カートと低額カートの比較）やメッセージ間の待機期間でユーザーを分岐させます。
  - **クリエイティブの差し替え:** 含まれているメールテンプレートをブランドのビジュアルスタイルに置き換えます。
  - **製品ブロックの使用:** ドラッグ＆ドロップ製品ブロック（早期アクセスプログラム）を使用して、カスタムLiquidを記述せずに放棄カートの内容や閲覧した製品を動的にレンダリングできます。

より高度なライフサイクル戦略（Liquidパーソナライゼーションの例を含む）については、[eコマースユースケース]({{site.baseurl}}/ecommerce_use_cases)を参照してください。

## eコマースレポート {#ecommerce-reporting}

eコマース推奨イベントは、顧客が現在使用しているものと同じ収益サーフェスを強化します。統合がeコマースイベントを送信している場合、以下のレポートにeコマース収益が自動的に含まれます:

| レポート | 表示内容 |
|---------------------------------------------|-------------------------------------------|
| 収益レポート | 選択した日付範囲とアプリにおける、すべてのソースの合計収益、平均日次収益、日次購入数、ユーザーあたりの収益の推移。 |
| ラストタッチアトリビューション収益ダッシュボード | 注文確定前にユーザーが最後にインタラクションしたCampaignまたはCanvasに帰属する収益。タッチイベントには、メールクリック、プッシュ開封、コンテンツカードクリック、アプリ内メッセージクリック、SMSまたはWhatsAppショートリンククリックが含まれます。 |
| CampaignおよびCanvasの分析 | 1次コンバージョンウィンドウ内で特定のCampaignまたはCanvasに帰属する合計収益。 |
| コンバージョンレポート | CampaignおよびCanvasのコンバージョンイベントに紐づく収益。<br> **注:** `ecommerce.order_placed`の収益をカウントするには、CampaignまたはCanvasのコンバージョンイベントとして「Place Order」コンバージョンイベントタイプを使用する必要があります。 |
| セグメントインサイト | セグメントインサイトダッシュボードにおけるSegment間の収益比較。 |
| レポートビルダー | レポートビルダーで構築されたカスタムレポートの収益指標。 |
| ダッシュボードビルダー | ダッシュボードビルダーで構築されたカスタムダッシュボードの収益指標。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eコマースレポート" }

ユーザー以外の計算フィールド（例: CampaignまたはCanvasの収益）の場合、収益はすべてのレポートで同じ方法で計算されます。注文内の製品ごとに`price`に`quantity`を掛け、各`order_placed`イベント内の製品全体で合計します。

{% alert note %}
収益の二重カウントを避けるため、同じ注文に対してレガシー購入イベントとeコマース推奨イベントの両方を送信しないでください。レガシー購入から推奨イベントへの移行を計画している場合は、統合を変更する前にBrazeアカウントチームと調整してください。<br><br>
収益計算では、注文あたりの個別製品数量の上限が`1,000`ユニットに設定されています。製品の`quantity`フィールドが欠落している場合、デフォルトで`1`になります。元の`order_placed`イベントには送信した完全な数量が保持されます。収益計算のみに上限が適用されます。
{% endalert %}

### BrazeAI<sup>TM</sup>

[予測イベント]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events)、[解約予測]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn)、および[アイテムレコメンデーション]({{site.baseurl}}/user_guide/brazeai/item_recommendations)は、eコマースイベントをターゲットイベントおよびシグナルとしてサポートしており、専用の「Order Placed」オプションがあります。標準化されたスキーマにより、データがユーザー群全体で一貫しているため、これらのモデルの信頼性が向上します。

### データのエクスポート {#export-data}

Brazeは、データウェアハウス、BIツール、またはダウンストリームシステムで使用するためにeコマースイベントデータをエクスポートするいくつかの方法を提供しています。eコマース推奨イベントは、他のイベントデータと同じチャネルを通じてエクスポートされます。

| エクスポートパス | 含まれる内容 |
|------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) | eコマースイベントはカスタムイベントとしてストリーミングされます。`ecommerce.*`名前空間で検索してください。各注文の製品は購入として利用可能です。 |
| [Snowflakeデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing) | eコマースイベントはカスタムイベントとして共有されます。`ecommerce.*`名前空間で検索してください。各注文の製品は購入テーブルで利用可能です。 |
| [セグメントデータをCSVにエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) | セグメントメンバーのCSVエクスポートです。eコマースイベントを含めるには、カスタムイベントドロップダウンから名前で選択してください。 |
| [セグメントごとのユーザープロファイルをエクスポート（API）]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#prerequisites) | セグメントメンバーのユーザープロファイルデータがAPI経由で返されます。eコマースイベントはカスタムイベントとして含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="データのエクスポート" }

### 特定の製品でユーザーをセグメント化するにはどうすればよいですか？ {#how-do-i-segment-users-by-a-specific-product}

セグメンターでは、ユーザーがeコマースイベントを実行した回数でフィルタリングできます。特定の製品プロパティ（`product_id`や`product_name`など）でフィルタリングするには、ネストされたイベントプロパティフィルタリングをサポートする[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)を使用してください。例えば、過去90日間に製品「SKU-123」を購入したすべてのユーザーを見つけることができます。