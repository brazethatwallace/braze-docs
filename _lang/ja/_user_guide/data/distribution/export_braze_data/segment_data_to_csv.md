---
nav_title: セグメントデータ
article_title: セグメントデータのエクスポート
page_order: 4
page_type: reference
description: "このリファレンス記事では、セグメントデータをCSVにエクスポートする方法、必要なユーザーデータのエクスポート権限、キャンバスステップのエクスポート、およびエクスポートに含まれるフィールドについて説明します。"
---

# セグメントデータをCSVにエクスポート {#export-segment-data-to-csv}

> このページでは、セグメントからユーザーデータのCSVエクスポートをリクエストする方法と、エクスポートに含まれるデータについて説明します。

{% alert note %}
CSVエクスポートオプションは、そのワークスペースに対する[「ユーザーデータのエクスポート」権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持つ会社ユーザーの場合にのみ、**User Data**ドロップダウンに表示されます。
{% endalert %}

セグメントデータをCSVにエクスポートするには、セグメントの編集中に**User Data**ドロップダウンを選択し、そのセグメントのユーザーデータまたはメールアドレスのいずれかをエクスポートするように選択します。

![「User Data」ドロップダウンにエクスポートオプションが表示されている「セグメント Details」セクション。]({% image_buster /assets/img_archive/csvexport.png %})

メインの**セグメント**ページから、セグメントの<i class="fas fa-gear" aria-label="設定メニューを開く"></i> **Settings**ドロップダウンを選択して、CSVエクスポートをリクエストすることもできます。

![メインのセグメントページの「Settings」ドロップダウン。]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
すべてのユーザープロファイルからデータをエクスポートするには、フィルターなしでセグメントを作成し、CSVエクスポートをリクエストしてください。
{% endalert %}

CSV出力には、エクスポート時にセグメントに含まれる各ユーザープロファイルのデータが含まれます。歯車アイコンを選択してCSVエクスポートを選択することで、任意のセグメントをエクスポートできます。Brazeはバックグラウンドでレポートを生成し、現在ログインしているユーザーにメールで送信します。

## セグメントCSVエクスポートの詳細 {#segment-csv-export-details}

{% alert note %}
ダッシュボードユーザーがCSVエクスポートオプションを使用するには、**ユーザーデータのエクスポート**権限が必要です。この権限がない場合、CSVエクスポートオプションは表示されません。
{% endalert %}

**メールアドレスのCSVエクスポート**には、セグメント内でメールアドレスを持つユーザーの行のみが含まれます。たとえば、セグメントに100,000人のユーザーがいても、メールアドレスを持つのが50,000人のみの場合、**メールアドレスのCSVエクスポート**では約50,000行が生成されます。**ユーザーデータのCSVエクスポート**では、セグメントのすべてのユーザーデータがエクスポートされます。

{% alert important %}
ファイルサイズの制限により、セグメントの推定サイズが500,000ユーザーを超える場合、エクスポートが失敗することがあります。この制限はセグメントの推定サイズを使用しており、正確な計算ではないことに注意してください。詳細については、[大規模セグメントのエクスポート](#exporting-large-segments)を参照してください。
{% endalert %}

[Amazon S3認証情報]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration)をBrazeにリンクしている場合、CSVは代わりにS3バケットのキー`segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`にアップロードされます。ダウンロードリンクが記載されたメールにアクセスするには、ダッシュボードにログインしている必要があります。

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## エクスポートに含まれるデータ {#data-included-in-export}

選択内容に応じて、以下のデータがエクスポートに含まれます。

### CSV エクスポートのユーザーデータ {#csv-export-user-data}

| フィールド名                  | 説明                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | 内部ID（変更不可）                           |
| country                     | 国                                    |
| created_at                  | ユーザープロファイルが作成された日時                   |
| created_from                | ユーザープロファイルの作成方法（例：REST API、SDK、CSVインポート）         |
| devices                     | デバイス情報                           |
| date_of_birth               | 生年月日                                            |
| email                       | メールアドレス                                            |
| unsubscribed_from_emails_at | メールの購読解除日                            |
| user_id                     | external ID                                              |
| first_name                  | 名                                               |
| first_session               | 最初のセッションの日時                           |
| gender                      | 性別                                                   |
| google_ad_ids               | ユーザーに関連付けられたGoogle広告ID                      |
| city                        | 市区町村                                     |
| IDFAs                       | 広告識別子（IDFA）の値                 |
| IDFVs                       | ベンダー識別子（IDFV）の値                      |
| language                    | ISO-639-1規格の言語                                        |
| last_app_version_used       | 最後に使用されたアプリのバージョン                             |
| last_name                   | 姓                                                |
| last_session                | 最後のセッションの日時                            |
| number_of_google_ad_ids     | 関連付けられたGoogle広告IDの数               |
| number_of_IDFAs             | 関連付けられたIDFAの数                                |
| number_of_IDFVs             | 関連付けられたIDFVの数                                |
| number_of_push_tokens       | 関連付けられたプッシュ通知トークンの数             |
| number_of_roku_ad_ids       | 関連付けられたRoku広告IDの数                 |
| number_of_windows_ad_ids    | 関連付けられたWindows広告IDの数              |
| phone_number                | 電話番号                                             |
| opted_into_push_at          | プッシュ通知のオプトイン日                       |
| unsubscribed_from_push_at   | プッシュ通知の購読解除日                |
| random_bucket               | ランダムバケット番号                                 |
| roku_ad_ids                 | Roku広告ID                          |
| session_count               | セッションの合計数                                 |
| timezone                    | IANAタイムゾーンデータベースと同じ形式のユーザーのタイムゾーン                                         |
| in_app_purchase_total       | アプリ内購入の合計金額                   |
| user_aliases                | ユーザーエイリアス（ある場合）                                          |
| windows_ad_ids              | Windows広告ID                       |
| Custom events               | エクスポート時の選択に基づく                             |
| カスタム属性           | エクスポート時の選択に基づく                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSVエクスポートのユーザーデータ" }

{% alert note %}
キャンバスステップからユーザーデータをエクスポートする場合、CSVにはそのキャンバスステップの全期間にわたってそのステップに含まれたすべてのユーザーが含まれます。日付範囲やその他の時間枠でエクスポートを制限することはできません。これらのエクスポートの実行方法については、[キャンバスデータのエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data)を参照してください。
{% endalert %}

### CSV エクスポートのメールアドレス {#csv-export-email-addresses}

| フィールド名                  | 説明            |
| --------------------------- | ---------------------- |
| user_id                     | ユーザーのexternal ID     |
| first_name                  | 名             |
| last_name                   | 姓              |
| email                       | メール                  |
| unsubscribed_from_emails_at | メールの購読解除日 |
| opted_in_to_emails_at       | メールのオプトイン日      |
| user_aliases                | ユーザーエイリアス（ある場合）   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSVエクスポートのメールアドレス" }

{% alert tip %}
CSVおよびAPIエクスポートに関するサポートについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)の記事をご覧ください。
{% endalert %}

{% alert note %}
購読グループのデータはセグメントのエクスポートでは取得できません。購読ステータスでユーザーを特定するには、購読グループのメンバーシップに基づいて別のセグメントを作成し、そのセグメントをエクスポートしてください。
{% endalert %}

## 大規模セグメントのエクスポート {#exporting-large-segments}

500,000人を超えるユーザーを含む大規模なユーザーセグメントをエクスポートするには、いくつかの方法があります。

{% tabs %}
{% tab 複数のセグメント %}

大規模なセグメントを小さなセグメントに分割し、それぞれの小さなセグメントをBrazeからエクスポートできます。

{% endtab %}
{% tab ランダムバケット番号 %}

[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)を使用してユーザー群を複数のセグメントに分割し、エクスポート後にそれらを結合することもできます。たとえば、セグメントを2つの異なるセグメントに分割する必要がある場合、次のフィルターを使用できます。
- セグメント1: ランダムバケット番号が5000未満（0〜4999を含む）
- セグメント2: ランダムバケット番号が4999より大きい（5000〜9999を含む）

{% endtab %}
{% tab エンドポイント %}

以下のエンドポイントを活用して、特定のセグメントのユーザーデータをエクスポートすることもできます。これらのエンドポイントにはデータ制限と[レート制限]({{site.baseurl}}/api/basics)が適用されることに注意してください。
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)

[Amazon S3の認証情報]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration)を接続している場合、[セグメントCSVエクスポートの詳細](#segment-csv-export-details)に記載されているように、メールのダウンロードリンクに加えて、大規模なエクスポートをバケットに配信できます。

{% endtab %}
{% endtabs %}