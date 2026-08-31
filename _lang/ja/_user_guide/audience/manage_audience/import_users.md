---
nav_title: ユーザーをインポートする
article_title: ユーザーをインポートする
page_order: 3
description: "CSVインポート、REST API、クラウドデータ取り込みなど、Brazeのさまざまなユーザーインポートオプションについて説明します。"

---
# ユーザーをインポートする {#import-users}

> CSVインポート、REST API、クラウドデータ取り込みなど、Brazeのさまざまなユーザーインポートオプションについて説明します。

## インポートオプション {#import-options}

BrazeのCSVインポート、サーバーレスS3 Lambda CSVインポートスクリプト、直接API呼び出し、またはデータウェアハウスからのCloud Data Ingestionを通じて、ユーザー属性とイベントをアップロードできます。

### Braze CSVインポート {#braze-csv-import}

CSVインポートを使用して、以下のユーザー属性とカスタムイベントを記録・更新できます。開始するには、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)を参照してください。

| タイプ | 定義 | 例 | 最大ファイルサイズ |
|---|---|---|---|
| デフォルト属性 | Brazeが認識する予約済みユーザー属性。 | `first_name`、`email` | 500 MB |
| カスタム属性 | ビジネスに固有のユーザー属性。 | `last_destination_searched` | 500 MB |
| カスタムイベント | ユーザーアクションを表す、ビジネスに固有のイベント。 | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Braze CSVインポート" }

#### CSVの構成 {#constructing-your-csv}

Brazeは標準CSV形式のユーザーデータを受け付けます。デフォルト属性およびカスタム属性のインポートは最大500 MBのファイルをサポートしています。カスタムイベントのインポートは最大50 MBのファイルをサポートしています。識別子、列ヘッダー、バリデーションルール、および例については、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)を参照してください。

ダッシュボードの**ユーザーをインポート**から大きなCSVをアップロードすると、Brazeがファイルを受信して計算ステップを実行している間、ページが応答しないように見えたり、応答が遅くなることがあります。アップロードと計算が完了するまでお待ちください。合計時間はファイルサイズに応じて数分から数時間かかり、ファイルが大きいほど計算に時間がかかります。

{% alert note %}
プロパティ付きのカスタムイベントをインポートする場合、CSVの列ヘッダーにドット表記を使用する必要があります。カスタムイベントのフォーマットの詳細については、[カスタムイベントのフォーマットについて]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import?tab=custom%20events#understanding-custom-event-formatting)を参照してください。
{% endalert %}

### Lambda ユーザーCSVインポート {#lambda-user-csv-import}

サーバーレスS3 Lambda CSVインポートスクリプトを使用して、ユーザー属性をBrazeにアップロードできます。このソリューションはCSVアップローダーとして機能し、CSVをS3バケットにドロップすると、スクリプトがAPIを通じてアップロードします。

1,000,000行のファイルの推定実行時間は約5分です。詳細については、[ユーザー属性CSVからBrazeへのインポート]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を参照してください。

### REST API

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、ユーザーのカスタムイベント、ユーザー属性、および購入を記録できます。

### Cloud Data Ingestion {#cloud-data-ingestion}

Brazeの[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用して、ユーザー属性をインポートおよび管理できます。

## HTMLバリデーション {#html-validation}

Brazeはインポート中にHTMLデータのサニタイズ、バリデーション、または再フォーマットを行わないため、Webパーソナライゼーションに使用するすべてのインポートデータからスクリプトタグを削除する必要があります。

Brazeにインポートするデータが特にWebブラウザーでのパーソナライゼーションを目的としている場合は、HTML、JavaScript、またはWebブラウザーでレンダリングされた際に悪意のある形で利用される可能性のあるスクリプトタグがすべて除去されていることを確認してください。

また、HTMLについては、BrazeのLiquidフィルター（`strip_html`）を使用して、レンダリングされたテキストからHTMLを除去することもできます。例：

{% tabs local %}
{% tab 入力 %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}