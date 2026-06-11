---
nav_title: セグメントデータ
article_title: セグメントデータのエクスポート
page_order: 4
page_type: reference
description: "このリファレンス記事では、セグメントデータを CSV にエクスポートする方法、必要なユーザーデータのエクスポート権限、キャンバスステップのエクスポート、およびエクスポートに含まれるフィールドについて説明します。"

---

# セグメントデータを CSV にエクスポート {#export-segment-data-to-csv}

> このページでは、セグメントからユーザーデータの CSV エクスポートをリクエストする方法と、エクスポートに含まれるデータについて説明します。

{% alert note %}
CSV エクスポートオプションは、そのワークスペースに対する[「ユーザーデータを CSV 形式でエクスポート」権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)を持つ会社ユーザーの場合にのみ、**User Data**ドロップダウンに表示されます。
{% endalert %}

セグメントデータを CSV にエクスポートするには、セグメントの編集中に**User Data**ドロップダウンを選択し、そのセグメントのユーザーデータまたはメールアドレスのいずれかをエクスポートするように選択します。

![「User Data」ドロップダウンにエクスポートオプションが表示されている「Segment Details」セクション。]({% image_buster /assets/img_archive/csvexport.png %})

メインの**Segments**ページから、セグメントの<i class="fas fa-gear" aria-label="設定メニューを開く"></i> **Settings**ドロップダウンを選択して、CSV エクスポートをリクエストすることもできます。

![メインのSegmentsページの「Settings」ドロップダウン。]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
すべてのユーザープロファイルからデータをエクスポートするには、フィルターなしでSegmentを作成し、CSV エクスポートをリクエストしてください。
{% endalert %}

CSV 出力には、エクスポート時にセグメントに含まれる各ユーザープロファイルのデータが含まれます。歯車アイコンを選択して CSV エクスポートを選択することで、任意のセグメントをエクスポートできます。Brazeはバックグラウンドでレポートを生成し、現在ログインしているユーザーにメールで送信します。

## セグメント CSV エクスポートの詳細 {#segment-csv-export-details}

{% alert note %}
ダッシュボードユーザーが CSV エクスポートオプションを使用するには、**ユーザーデータを CSV 形式でエクスポート**権限が必要です。この権限がない場合、CSV エクスポートオプションは表示されません。
{% endalert %}

**メールアドレスを CSV 形式でエクスポート**には、セグメント内でメールアドレスを持つユーザーの行のみが含まれます。例えば、セグメントに100,000人のユーザーがいても、メールアドレスを持つのが50,000人だけの場合、**メールアドレスを CSV 形式でエクスポート**では約50,000行が生成されます。**ユーザーデータを CSV 形式でエクスポート**では、そのセグメントのすべてのユーザーデータがエクスポートされます。

{% alert important %}
ファイルサイズの制限により、セグメントの推定サイズがユーザー数500,000人を超える場合、エクスポートに失敗する可能性があります。この制限は、セグメントの正確な計算ではなく推定サイズを使用することに注意してください。詳しくは、[大きなセグメントのエクスポート](#exporting-large-segments)を参照してください。
{% endalert %}

[Amazon S3 の認証情報]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration)をBrazeにリンクしている場合、CSV は代わりに S3 バケットのキー`segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`の下にアップロードされます。メールで届くダウンロードリンクにアクセスするには、ダッシュボードにログインしている必要があります。

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## エクスポートに含まれるデータ {#data-included-in-export}

以下のデータが、選択に応じてエクスポートに含まれます。

### ユーザーデータを CSV 形式でエクスポート {#csv-export-user-data}

| フィールド名                  | 説明                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | 内部 ID（変更不可）                           |
| country                     | 国                                    |
| created_at                  | ユーザープロファイルが作成された日時                   |
| created_from                | ユーザープロファイルの作成に使用された方法（例：REST API、SDK、CSV インポート）         |
| devices                     | デバイス情報                           |
| date_of_birth               | 生年月日                                            |
| email                       | メールアドレス                                            |
| unsubscribed_from_emails_at | メールの配信停止日                            |
| user_id                     | external ID                                              |
| first_name                  | 名                                               |
| first_session               | 初回セッションの日時                           |
| gender                      | 性別                                                   |
| google_ad_ids               | ユーザーに関連付けられた Google 広告 ID                      |
| city                        | 市区町村                                     |
| IDFAs                       | 広告用識別子（IDFA）の値                 |
| IDFVs                       | ベンダー識別子（IDFV）の値                      |
| language                    | ISO-639-1 規格の言語                                        |
| last_app_version_used       | 最後に使用したアプリのバージョン                             |
| last_name                   | 姓                                                |
| last_session                | 最終セッションの日時                            |
| number_of_google_ad_ids     | 関連する Google 広告 ID の数               |
| number_of_IDFAs             | 関連する IDFA の数                                |
| number_of_IDFVs             | 関連する IDFV の数                                |
| number_of_push_tokens       | 関連するプッシュ通知トークンの数             |
| number_of_roku_ad_ids       | 関連する Roku 広告 ID の数                 |
| number_of_windows_ad_ids    | 関連する Windows 広告 ID の数              |
| phone_number                | 電話番号                                             |
| opted_into_push_at          | プッシュ通知にオプトインした日付                       |
| unsubscribed_from_push_at   | プッシュ通知の配信停止日                |
| random_bucket               | ランダムバケット番号                                 |
| roku_ad_ids                 | Roku 広告 ID                          |
| session_count               | セッションの総数                                 |
| timezone                    | IANA タイムゾーンデータベースと同じフォーマットによるユーザーのタイムゾーン                                         |
| in_app_purchase_total       | アプリ内購入の支出総額                   |
| user_aliases                | ユーザーエイリアスがある場合                                          |
| windows_ad_ids              | Windows 広告 ID                       |
| カスタムイベント               | エクスポート時の選択に基づく                             |
| カスタム属性           | エクスポート時の選択に基づく                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV export user data" }

{% alert note %}
キャンバスステップからユーザーデータをエクスポートすると、CSV にはそのキャンバスステップの全期間にわたってそのステップに含まれたすべてのユーザーが含まれます。エクスポートを日付範囲やその他の時間枠に制限することはできません。これらのエクスポートの実行方法については、[Canvasデータのエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/)を参照してください。
{% endalert %}

### メールアドレスを CSV 形式でエクスポート {#csv-export-email-addresses}

| フィールド名                  | 説明            |
| --------------------------- | ---------------------- |
| user_id                     | ユーザーの external ID     |
| first_name                  | 名             |
| last_name                   | 姓              |
| email                       | メール                  |
| unsubscribed_from_emails_at | メール配信停止日 |
| opted_in_to_emails_at       | メールオプトイン日      |
| user_aliases                | ユーザーエイリアスがある場合   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV Export Email Addresses" }

{% alert tip %}
CSV と API のエクスポートについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/)の記事を参照してください。
{% endalert %}

{% alert note %}
サブスクリプショングループのデータは、セグメントエクスポートでは利用できません。サブスクリプションステータスでユーザーを特定するには、サブスクリプショングループのメンバーシップに基づいて別のセグメントを作成し、そのセグメントをエクスポートしてください。
{% endalert %}

## 大きなセグメントのエクスポート {#exporting-large-segments}

500,000人を超えるユーザーを含む大規模なユーザーセグメントをエクスポートするには、いくつかの方法があります。

{% tabs %}
{% tab 複数のセグメント %}

大きなセグメントを小さなセグメントに分割し、それぞれの小さなセグメントをBrazeからエクスポートできます。

{% endtab %}
{% tab ランダムバケット番号 %}

また、[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/)を使用して、ユーザー群を複数のセグメントに分割し、エクスポート後にそれらを組み合わせることもできます。例えば、セグメントを2つの異なるセグメントに分割する必要がある場合は、次のフィルターを使用できます。
- セグメント 1：ランダムバケット番号が5000未満（0～4999を含む）
- セグメント 2：ランダムバケット番号が4999より大きい（5000～9999を含む）

{% endtab %}
{% tab エンドポイント %}

また、次のエンドポイントを利用して、特定のセグメントのユーザーデータをエクスポートすることもできます。これらのエンドポイントはデータ制限および[レート制限]({{site.baseurl}}/api/basics/)の対象となりますのでご注意ください。
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

[Amazon S3 の認証情報]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration)を接続している場合、[セグメント CSV エクスポートの詳細](#segment-csv-export-details)で説明されているように、メールで届くダウンロードリンクに加えて、大規模なエクスポートをバケットに配信できます。

{% endtab %}
{% endtabs %}