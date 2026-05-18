---
nav_title: ユーザーをインポートする
article_title: ユーザーをインポートする
page_order: 3
description: "CSVインポート、REST API、クラウドデータ取り込みなど、Brazeのさまざまなユーザーインポートオプションについて説明します。"

---
# ユーザーをインポートする {#import-users}

> CSVインポート、REST API、クラウドデータ取り込みなど、Brazeのさまざまなユーザーインポートオプションについて説明します。

## インポートオプション {#import-options}

BrazeでのCSVインポート、サーバーレスS3 Lambda CSVインポートスクリプト、直接APIコール、またはデータウェアハウスからのクラウドデータ取り込みを通じて、ユーザー属性やイベントをアップロードできます。

### Braze CSVインポート {#braze-csv-import}

CSVインポートを使用して、以下のユーザー属性やカスタムイベントを記録・更新できます。開始するには、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)を参照してください。

| タイプ | 定義 | 例 | 最大ファイルサイズ |
|---|---|---|---|
| デフォルト属性 | Brazeが認識する予約済みのユーザー属性。 | `first_name`、`email` | 500 MB |
| カスタム属性 | ビジネス固有のユーザー属性。 | `last_destination_searched` | 500 MB |
| カスタムイベント | ユーザーのアクションを表すビジネス固有のイベント。 | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Braze CSV import" }

#### CSVの構成 {#constructing-your-csv}

Brazeは標準CSV形式のユーザーデータを受け付けます。デフォルト属性とカスタム属性のインポートは最大500 MBのファイルをサポートし、カスタムイベントのインポートは最大50 MBのファイルをサポートします。識別子、列ヘッダー、バリデーションルール、および例については、[CSVインポート]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import/)を参照してください。

ダッシュボードの**Import Users**から大きなCSVをアップロードすると、Brazeがファイルを受信して計算ステップを実行している間、ページが応答しないか、応答が遅くなることがあります。アップロードと計算が完了するまでお待ちください。合計時間はファイルサイズに応じて数分から数時間の範囲で、ファイルが大きいほど計算に時間がかかります。

{% alert note %}
プロパティ付きのカスタムイベントをインポートする場合、CSVの列ヘッダーにドット表記を使用する必要があります。カスタムイベントのフォーマットの詳細については、[カスタムイベントのフォーマットについて]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/?tab=custom%20events#understanding-custom-event-formatting)を参照してください。
{% endalert %}

### Lambda ユーザーCSVインポート {#lambda-user-csv-import}

サーバーレスS3 Lambda CSVインポートスクリプトを使用して、ユーザー属性をBrazeにアップロードできます。このソリューションはCSVアップローダーとして機能し、CSVをS3バケットにドロップすると、スクリプトがAPIを通じてアップロードします。

1,000,000行のファイルの推定実行時間は約5分です。詳細については、[ユーザー属性CSVからBrazeへのインポート](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion)を参照してください。

### REST API

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、ユーザーのカスタムイベント、ユーザー属性、および購入を記録できます。

### クラウドデータ取り込み {#cloud-data-ingestion}

Brazeの[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)を使用して、ユーザー属性をインポートおよび管理できます。

## HTMLバリデーション {#html-validation}

Brazeはインポート時にHTMLデータのサニタイズ、バリデーション、または再フォーマットを行わないため、Webパーソナライゼーションに使用するすべてのインポートデータからスクリプトタグを削除する必要があることに注意してください。

Webブラウザでのパーソナライゼーション用途を目的としたデータをBrazeにインポートする場合、Webブラウザでレンダリングされた際に悪意を持って利用される可能性のあるHTML、JavaScript、またはその他のスクリプトタグが除去されていることを確認してください。

あるいは、HTMLの場合、Braze Liquidフィルター（`strip_html`）を使用して、レンダリングされたテキストからHTMLを除去できます。例：

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
`````````liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}