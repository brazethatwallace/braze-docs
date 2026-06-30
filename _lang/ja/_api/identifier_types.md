---
nav_title: "API識別子タイプ"
article_title: "API識別子タイプ"
page_order: 2.2
toc_headers: h2
description: "このリファレンス記事では、Brazeダッシュボードに存在するさまざまな種類のAPI識別子、それらの場所、およびそれらの使用用途について説明します。"
page_type: reference

---

# API識別子タイプ {#api-identifier-types}

> このリファレンスガイドでは、Brazeダッシュボード内で見つけることができるさまざまな種類のAPI識別子、それらの目的、それらを見つける場所、およびそれらが通常どのように使用されるかについて説明します。REST APIキーまたはワークスペースAPIキーに関する情報については、[API概要]({{site.baseurl}}/api/api_key)を参照してください。

次の識別子を使用して、Braze外部APIからテンプレート、Canvas、Campaign、またはSegmentにアクセスできます。すべてのメッセージは[UTF-8](https://en.wikipedia.org/wiki/UTF-8)エンコーディングに従う必要があります。

## アプリ識別子 {#app-identifier}

アプリ識別子または`app_id`は、ワークスペース内の特定のアプリとアクティビティを関連付けるパラメーターです。これにより、ワークスペース内のどのアプリと対話するかが指定されます。例えば、iOSアプリ用の`app_id`、Androidアプリ用の`app_id`、Webインテグレーション用の`app_id`があります。Brazeでは、Brazeがサポートするさまざまなプラットフォームタイプにわたって、同じプラットフォーム用の複数のアプリを持っていることがあります。

### どこで見つけられますか？ {#where-can-i-find-it}

`app_id`を見つける方法は2つあります。

{% tabs local %}
{% tab App Identifiers %}
**設定** > **APIキー** > **アプリ識別子**の順に進みます。各アプリのAPIキーは**識別子**欄に記載されています。
{% endtab %}

{% tab App Settings %}
**設定** > **アプリ設定**に移動します。設定セクションの**APIキー**フィールドの横にAPIキーが表示されます。

{% endtab %}
{% endtabs %}

### どのように使用できますか？ {#what-can-it-be-used-for}

Brazeのアプリ識別子は、SDKを統合するときに使用され、REST API呼び出しで特定のアプリを参照するのにも使用されます。`app_id`を使用すると、特定のアプリで発生したカスタムイベントのデータを引き出したり、特定のアプリのアンインストール統計、新規ユーザー統計、DAU統計、セッション開始統計などを取得したりすることができます。

{% alert tip %}
場合によっては、`app_id`の入力を求められることがありますが、アプリを使用していない場合は、特定のプラットフォームに固有のレガシーフィールドであるため、このフィールドを省略できます。この必須パラメーターのプレースホルダーとして任意の文字列を含めてください。
{% endalert %}

### 複数のアプリ識別子 {#multiple-app-identifiers}

SDKのセットアップ中、複数のアプリ識別子の最も一般的なユースケースは、デバッグビルドバリアントとリリースビルドバリアントの識別子を分離することです。

ビルド内の複数のアプリ識別子を簡単に切り替えるには、関連する[ビルドバリアント](https://developer.android.com/studio/build/build-variants.html)ごとに個別の`braze.xml`ファイルを作成することをお勧めします。ビルドバリアントは、ビルドタイプと製品フレーバーの組み合わせです。デフォルトでは、新しいAndroidプロジェクトは`debug`および`release`のビルドタイプで構成され、プロダクトフレーバーはありません。

関連するビルドバリアントごとに、新しい`braze.xml`を`src/<build variant name>/res/values/`に作成します。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
ビルドバリアントがコンパイルされると、新しい識別子が使用されます。

## テンプレート識別子 {#template-identifier}

[テンプレート]({{site.baseurl}}/api/endpoints/templates)識別子またはテンプレートIDは、ダッシュボード内の特定のテンプレートに対してBrazeによって生成されるランダムキーです。テンプレートIDは各テンプレートごとに一意であり、APIを通じてテンプレートを参照するために使用できます。

テンプレートは、会社がCampaignsのためにHTMLデザインを外注する場合に最適です。テンプレートが作成された後、特定のCampaignに限定されないテンプレートができあがりますが、ニュースレターのような一連のCampaignsに適用することができます。

### どこで見つけられますか？

テンプレートIDを見つける方法は2つあります。

{% tabs local %}
{% tab テンプレート %}
**テンプレート**に移動し、テンプレートページを選択して、既存のテンプレートを選択します。テンプレートがまだ存在しない場合は、新しいテンプレートを作成して保存してください。個々のテンプレートページの下部に、テンプレート識別子が表示されます。
{% endtab %}

{% tab APIキー %}
**設定** > **APIキー**に進みます。ここで、Brazeは**追加のAPI識別子**検索を提供しており、特定の識別子を検索できます。

{% endtab %}
{% endtabs %}

### どのように使用できますか？

- APIを使ってテンプレートを更新する
- 特定のテンプレートに関する情報を取得する

## Canvas識別子 {#canvas-identifier}

[Canvas]({{site.baseurl}}/user_guide/messaging/canvas)識別子またはCanvas IDは、ダッシュボード内の特定のCanvasに対してBrazeによって生成されるランダムキーです。Canvas IDは各Canvasに固有であり、APIを介してCanvasを参照するために使用できます。

Canvasにバリアントがある場合、全体のCanvas IDと、メインCanvasの下にネストされた個々のバリアントCanvas IDが存在することに注意してください。

### どこで見つけられますか？

ダッシュボードでCanvas IDを見つけることができます。**メッセージング** > **Canvas**に移動し、既存のCanvasを選択します。Canvasがまだ存在しない場合は、作成して保存してください。個々のCanvasページの下部で、**Analyze Variants**をクリックします。ウィンドウが表示され、Canvas API識別子が下部に表示されます。

### どのように使用できますか？

- 特定のメッセージの分析を追跡する
- Canvasのパフォーマンスに関する集計統計の概要を取得する
- 特定のCanvasの詳細を取得する
- Currentsを使用して、ユーザーレベルのデータを取り込み、Canvasesに対する「大局的な視点」アプローチを実現する
- APIトリガー配信により、トランザクションメッセージの統計を収集する

## Campaign識別子 {#campaign-identifier}

[Campaign]({{site.baseurl}}/user_guide/messaging/campaigns)識別子またはCampaign IDは、ダッシュボード内の特定のCampaignに対してBrazeによって生成されるランダムキーです。Campaign IDは各Campaignに固有であり、APIを通じてCampaignsを参照するために使用できます。

Campaignにバリアントがある場合、全体のCampaign IDと、メインCampaignの下にネストされた個々のバリアントCampaign IDの両方が存在することに注意してください。

### どこで見つけられますか？

Campaign IDを見つける方法は2つあります。

{% tabs local %}
{% tab Campaigns %}
**メッセージング** > **Campaigns**に移動し、既存のCampaignを選択します。Campaignがまだ存在しない場合は、新しいCampaignを作成して保存してください。個々のCampaignページの下部に、**Campaign API Identifier**が記載されています。

{% endtab %}

{% tab APIキー %}
**設定** > **APIキー**に進みます。ここで、Brazeは**追加のAPI識別子**検索を提供しており、特定の識別子を検索できます。

{% endtab %}
{% endtabs %}

### どのように使用できますか？

- 特定のメッセージの分析を追跡する
- Campaignのパフォーマンスに関する高レベルの集計統計を取得する
- 特定のCampaignに関する詳細を取得する
- Currentsを使用して、ユーザーレベルのデータを取り込み、Campaignsに対する「大局的な」アプローチを実現する
- APIトリガー配信により、トランザクションメッセージの統計を収集する
- **Campaigns**ページでフィルター`api_id:YOUR_API_ID`を使用して[特定のCampaignを検索する]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns#search-syntax)

## Segment識別子 {#segment-identifier}

[Segment]({{site.baseurl}}/user_guide/audience/segments)識別子またはSegment IDは、ダッシュボード内の特定のSegmentに対してBrazeによって生成されるランダムキーです。Segment IDは各Segmentに固有であり、APIを通じてSegmentsを参照するために使用できます。

### どこで見つけられますか？

Segment IDを見つける方法は2つあります。

{% tabs local %}
{% tab Segments %}
**オーディエンス** > **Segments**に移動し、既存のSegmentを選択します。Segmentがまだ存在しない場合は、新しいSegmentを作成して保存してください。個々のSegmentページの下部に、Segment識別子が表示されます。

{% endtab %}

{% tab APIキー %}
**設定** > **APIキー**に進みます。ここで、Brazeは**追加のAPI識別子**検索を提供しており、特定の識別子を検索できます。

{% endtab %}
{% endtabs %}

### どのように使用できますか？

- 特定のSegmentの詳細を取得する
- 特定のSegmentの分析を取得する
- 特定のSegmentに対してカスタムイベントが記録された回数を取得する
- API内からSegmentのメンバーにCampaignを指定して送信する

## 送信識別子 {#send-identifier}

送信識別子、または送信IDは、分析を追跡する必要がある特定のメッセージ送信に対してBrazeによって生成されるか、またはユーザーによって作成されるキーです。送信識別子を使用すると、[`/sends/data_series`エンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics)を介してCampaign送信の特定のインスタンスの分析を取得できます。

### どこで見つけられますか？

ブロードキャストとして送信されるAPIおよびAPIトリガーCampaignsでは、送信識別子が提供されない場合、送信識別子が自動的に生成されます。独自の送信識別子を指定したい場合は、まず[`/sends/id/create`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)から作成する必要があります。識別子はすべてASCII文字で、最大64文字である必要があります。同じCampaignの複数の送信にわたって送信識別子を再利用して、それらの送信の分析をグループ化することができます。

### どのように使用できますか？
送信ごとにCampaignを作成することなく、プログラムでメッセージのパフォーマンスを送信および追跡します。

## サブスクリプショングループ識別子 {#subscription-group-identifier}

サブスクリプショングループ識別子、またはサブスクリプショングループIDは、特定のサブスクリプショングループのためにBrazeによって生成されたキーです。IDは各サブスクリプショングループに固有であり、APIを通じてサブスクリプショングループを参照するために使用できます。

### どこで見つけられますか？

**オーディエンス** > **サブスクリプション**に移動し、該当するサブスクリプショングループの横にあるIDをコピーします。

### どのように使用できますか？

- ユーザーのサブスクリプショングループをリストする
- ユーザーのサブスクリプショングループステータスを取得する
- ユーザーのサブスクリプショングループステータスを更新する