---
nav_title: ワークスペース間のデータ移行
article_title: ワークスペースおよびインスタンス間のデータ移行
page_order: 1
page_type: reference
description: "ワークスペースデータの分離の仕組み、Brazeがワークスペース間でコピーまたはインポートできるもの、ステージング環境、本番環境、または別のダッシュボード環境間の移行を計画する方法について説明します。"
---

# ワークスペースおよびインスタンス間のデータ移行 {#migrate-data-between-workspaces-and-instances}

> ワークスペースはBrazeデータを分離して管理します。このページでは、その分離が移行にどのように影響するか、製品機能やAPIで移動できるもの、Braze外で再構築または対応が必要なものについて説明します。移行は通常、会社管理者だけのタスクではなく、部門横断的な取り組みです。管理者はワークスペースのセットアップとチャネル設定を担当し、開発者はSDKとAPIの変更を処理し、マーケターはセグメントの再構築やメッセージングコンテンツのコピーを行います。各ステップには、ソースおよび送信先ワークスペースでの適切な[権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)が必要です。

Brazeに保存するすべてのもの（ユーザープロファイル、セグメント、メッセージングコンテンツ、エンゲージメント履歴）はワークスペース内に存在します。Segment、Campaign、またはCanvasは、別のワークスペースのデータを読み取ったりターゲットにしたりすることはできません。ダッシュボードユーザーは、ステージングと本番環境、異なるブランド、または地域別の分割のために、同じ会社のダッシュボード上で複数のワークスペースを使用することがよくあります。このセットアップにより分離が実現しますが、ダッシュボード上のすべてのワークスペースデータを別のワークスペースや別のBrazeインスタンスに移動する単一のアクションは存在しません。

計画の参考として、[はじめに：ワークスペース]({{site.baseurl}}/user_guide/get_started/workspaces/)および[ワークスペースの作成と管理]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/)をご覧ください。

## Brazeがワークスペース間で自動移行しないもの {#what-braze-does-not-automatically-migrate-between-workspaces}

SDKやAPIを新しいワークスペース（または独自のワークスペースを持つ新しいBrazeダッシュボード環境）に向けた場合、以下は一括移行されません。

| 領域 | 動作 |
| --- | --- |
| **ユーザープロファイル** | プロファイルはパッケージ化された単位として転送されません。送信先ワークスペースでユーザーを再作成またはインポートしてください（[ユーザープロファイルデータ](#user-profile-data)を参照）。 |
| **Segmentsとフィルター** | Segmentの定義はソースワークスペースに残ります。可能な限り同じロジックを使用して、送信先ワークスペースでSegmentsを再構築してください。 |
| **メッセージング履歴** | プロファイル上のCampaignおよびCanvasの受信履歴はソースワークスペースに紐づいています。[Brazeオンボーディングに関するFAQ]({{site.baseurl}}/user_guide/onboarding_faq/)に記載されているように、カスタム属性などを使用して自分でモデル化しない限り、別のワークスペースの新しいプロファイルには表示されません。 |
| **チャネル固有の設定** | 送信ドメイン、SMSサブスクリプション、WhatsApp番号、および同様の設定はワークスペースにスコープされています。該当する場合は、送信先ワークスペースで再設定してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Brazeがワークスペース間で自動移行しないもの" }

{% alert important %}
ステージングと本番環境で別々のワークスペースを使用している場合、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)コネクタはワークスペース間で共有されないことに注意してください。どのワークスペースが本番エクスポートを所有するかを計画してください。詳細については、[はじめに：ワークスペース]({{site.baseurl}}/user_guide/get_started/workspaces/#currents-connectors)をご覧ください。
{% endalert %}

## 移動または再作成できるもの {#what-you-can-move-or-recreate}

### CampaignおよびCanvasコンテンツ {#campaign-and-canvas-content}

多くのCampaignおよびCanvasの定義を下書きとして別のワークスペースにコピーできます。サポートされるチャネル、省略されるフィールド、およびLiquidに関する注意事項は、[ワークスペース間でのCampaignおよびCanvasのコピー]({{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces/)に記載されています。コピー後、起動する前にSegments、トリガー、およびワークスペース固有の参照を更新してください。

### ユーザープロファイルデータ {#user-profile-data}

一般的なアプローチ：

- **REST API：** [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、必要な識別子と属性で送信先ワークスペースにユーザーを作成または更新します。これは、履歴データをBrazeに取り込む際の[レガシーユーザーデータの移行]({{site.baseurl}}/developer_guide/getting_started/integration_overview/#migrating-legacy-user-data)で説明されているパターンと同じです。
- **CSVインポート：** マーケター主導のインポートについては、[ユーザーをインポートする]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/)および[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)をご覧ください。
- **クラウドデータ取り込み：** ウェアハウスから送信先ワークスペースに属性を同期するには、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)をご覧ください。
- **ソースワークスペースからのエクスポート：** [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)または[`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)を使用して移動が許可されているデータを抽出し、送信先用に`users/track`またはCSVにマッピングします。データのエクスポートおよび再読み込み時には、データ保持、プライバシー、および契約上の義務を遵守してください。

{% alert note %}
[ユーザーのマージ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)エンドポイントまたはダッシュボードの[重複ユーザー]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/)を使用した重複プロファイルのマージは、単一のワークスペース内で適用され、2つのワークスペース間では適用されません。
{% endalert %}

### 標準プロファイルAPIにマッピングされないユーザーエクスポートフィールド {#user-export-fields-that-dont-map-to-standard-profile-apis}

[ユーザーエクスポート]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)から送信先ワークスペースでユーザーを再構築する場合、一部のエクスポートフィールドは、REST APIやCSVを通じてBrazeの標準プロファイルフィールドに書き戻すことができません（SDKやサーバーがそれらを入力する方法とは異なります）。多くの場合、代わりにカスタム属性として値を保持できます。以下の制限に注意してください。

#### デバイス情報（`devices`） {#device-information-devices}

エクスポート内のデバイスレコードはSDKによって入力されます。REST APIを通じてBrazeの標準デバイスフィールドにそのデータを移行することはできません。

送信先ワークスペースをターゲットとするアプリでユーザーがセッションを開始する前にその情報が必要な場合は、ユーザーのインポート時にカスタム属性として送信してください。組み込みデバイスデータに依存する標準のセグメンテーションフィルターやLiquid参照は、ユーザーが新しいワークスペースに接続されたアプリインスタンスでセッションを開くまで（SDKが標準デバイスフィールドを更新するまで）、エクスポートされたデバイスペイロードを使用しません。

{% alert note %}
これは[プッシュトークンの移行](#push-tokens)とは別のものです。プッシュトークンの移行では、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)の`push_tokens`フィールドを使用します。
{% endalert %}

#### 合計セッション数およびアプリごとのセッションデータ（`apps`とネストされた`sessions`） {#total-sessions-and-per-app-session-data-apps-and-nested-sessions}

エクスポート内の`apps`オブジェクトからのセッション合計およびネストされたセッションデータは、同じ組み込みフィールドに再インポートすることはできません。レガシーカウント（例：ソースワークスペースからの合計セッション数）を保持するには、カスタム属性に保存し、送信先ワークスペースでそれらのフィールドでセグメンテーションを行ってください。

`date_of_first_session`と`date_of_last_session`は、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)またはCSVインポートを通じて設定できます。受け入れられる形式については、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)および[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)をご覧ください。

#### ランダムバケット（`random_bucket`） {#random-bucket-random_bucket}

各ユーザーには、ワークスペース内で[ランダムバケット番号]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/#random-bucket-number-update-events)が割り当てられます。この値は再インポートできません。ユーザーは送信先ワークスペースで新しいランダムバケットを取得します。

ホールドアウトやサンプリングのために古い番号に依存している場合（例：`random_bucket`がしきい値未満のユーザーを除外する場合）、エクスポートされた値をカスタム属性として保存し、組み込みのランダムバケットフィールドの代わりにその属性でSegmentsやフィルターを構築してください。

#### パートナーアトリビューションフィールド（`attributed_*`） {#partner-attribution-fields-attributed_}

パートナー連携からのアトリビューションフィールド（エクスポート内の`attributed_*`フィールド）は、REST APIを通じてBrazeの標準アトリビューションフィールドに設定することはできません。セグメンテーションやメッセージングのために保持する必要がある場合は、送信先ワークスペースでカスタム属性にマッピングしてください。

### プッシュトークン {#push-tokens}

ユーザーが以前のプロバイダーやアプリバージョンからのプッシュトークンを既に持っている場合、APIを通じてモバイルアプリ用のトークンをインポートするか、統合後にSDKに依存することができます。Webプッシュトークンには APIの制限があります。詳細と例については、[プッシュトークンの移行]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens)をご覧ください。

### WhatsApp

電話番号とサブスクリプショングループは、特定の転送フローを使用してワークスペース間で移動できます。[ワークスペース間でのWhatsApp電話番号とサブスクリプショングループの転送]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/transfer_between_workspaces/)をご覧ください。

### Braze外のエンゲージメントおよび分析データ {#engagement-and-analytics-data-outside-braze}

環境を統合する際に送信、開封、またはクリックの履歴レコードが必要な場合、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)およびその他のエクスポートが、そのデータをウェアハウスやツールに格納するためのサポートされた方法です。そのデータは、別のワークスペース上のネイティブなユーザーごとのメッセージ履歴としてBrazeに再取り込みされることはありません。

## SDKまたはAPIキーを変更する前に {#before-you-change-sdk-or-api-keys}

アプリやサイトを新しいワークスペースに向けた場合：

- アプリやサイトを開いたユーザーは、新しいワークスペースに新しいプロファイルを作成できます。以前のワークスペース固有の履歴は自動的に引き継がれません。
- 同じ人物が両方のワークスペースに存在する可能性がある場合、[重複のようなシナリオ]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/#should-i-create-a-new-workspace-when-im-releasing-an-updated-app)が発生する可能性があります（例：プッシュリーチの重複）。本番環境とステージング環境のキーを意図せず共有するのではなく、計画的なデータおよびターゲティング計画を優先してください。

{% alert tip %}
ワークスペースやアプリインスタンスの削除制限、特別なアカウント移動、または大規模な移行計画については、ダッシュボードのリンクとソースおよび送信先ワークスペースの概要を添えて[Brazeサポートにお問い合わせ]({{site.baseurl}}/user_guide/administer/personal/braze_support/)ください。
{% endalert %}