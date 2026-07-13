---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "このリファレンス記事では、BrazeとGoogle Cloud Storageのパートナーシップについて説明します。Google Cloud Storageは、非構造化データのための大規模拡張可能オブジェクトストレージです。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/)は、GoogleがCloud Computing製品群の一部として提供する、非構造化データのための大規模拡張可能オブジェクトストレージです。

{% alert important %}
クラウドストレージプロバイダーを切り替える場合は、Brazeカスタマーサクセスマネージャーに連絡し、新しい統合の設定と検証についてさらにサポートを受けてください。
{% endalert %}

BrazeとGoogle Cloud Storageの統合により、CurrentsデータをGoogle Cloud Storageにストリーミングできます。その後、ETLプロセス（抽出、変換、読み込み）を使用して、データをGoogle BigQueryなどの他の場所に転送できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Google Cloud Storageアカウント | このパートナーシップを活用するには、Google Cloud Storageアカウントが必要です。 |
| Currents | データをGoogle Cloud Storageにエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)を設定する必要があります。メッセージのアーカイブの設定のみの場合、Currentsは必要ありません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Google Cloud Storageと統合するには、Brazeが書き込み先のストレージバケットに関する情報を取得し（`storage.buckets.get`）、そのバケット内にオブジェクトを作成（`storage.objects.create`）できるように、適切な認証情報を設定する必要があります。

{% alert note %}
ワークロードIDフェデレーション（WIF）は、Currentsの認証方法としてサポートされていません。JSON秘密キーを持つサービスアカウントを使用する必要があります。
{% endalert %}

これを行うには次の手順に従います。この手順では、Currents統合で使用する秘密キーを生成するロールとサービスアカウントを作成する方法を説明します。

### ステップ1:ロールを作成する {#step-1-create-role}

Google Cloud Platform Consoleで、**IAM & admin** > **Roles** > **+ Create Role** に移動し、新しいロールを作成します。

![ロール作成アクションが表示されたGoogle Cloud IAMロールページ。]({% image_buster /assets/img/gcs1.png %})

ロールに名前を付け、**+Add Permissions** を選択して、以下を選択します。

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
`storage.objects.delete`権限はオプションです。これによりBrazeは不完全なファイルをクリーンアップできます。<br><br>まれにGoogle Cloudが接続を早期に終了し、BrazeがGoogle Cloud Storageに不完全なファイルを書き込むことがあります。ほとんどの場合、Brazeは再試行して正しいデータで新しいファイルを作成し、古いファイルはGoogle Cloud Storageに残ります。
{% endalert %}

完了したら、**Create** を選択します。

![ストレージ権限が選択されたGoogle Cloudカスタムロールエディター。]({% image_buster /assets/img/gcs2.png %})

### ステップ2:新しいサービスアカウントを作成する {#step-2-create-a-new-service-account}

#### ステップ2.1:サービスアカウントを作成する {#step-21-create-the-service-account}

Google Cloud Platform Consoleで、**IAM & admin** > **Service Accounts** に移動し、**Create Service Account** を選択して新しいサービスアカウントを作成します。

![Create Service Accountが選択されたGoogle Cloudサービスアカウントページ。]({% image_buster /assets/img/gcs3.png %})

次に、サービスアカウントに名前を付け、新しく作成したカスタムロールへのアクセス権を付与します。

![Google Cloud Platformのサービス作成ページで、「Select a Role」フィールドにロールの名前を入力します。]({% image_buster /assets/img/gcs4.png %})

#### ステップ2.2:キーを作成する {#step-22-create-a-key}

ページ下部の **Create Key** ボタンを使用して、Brazeで使用する **JSON** 秘密キーを作成します。キーが作成されると、マシンにダウンロードされます。

![JSONキータイプに設定されたGoogle Cloudサービスアカウントキー作成ダイアログ。]({% image_buster /assets/img/gcs5.png %})

### ステップ3:BrazeでCurrentsを設定する {#step-3-set-up-currents-in-braze}

Brazeで **Currents** > **+ Create Current** > **Google Cloud Storage Data Export** に移動し、統合名と連絡先メールを入力します。

次に、**GCS JSON Credentials** の下にJSON秘密キーをアップロードし、GCSバケット名とGCSプレフィックス（オプション）を入力します。この認証情報は、前のステップで説明したように、Google Cloud Platformを通じて生成する必要があります。

{% alert important %}
認証情報ファイルを最新の状態に維持することが重要です。コネクターの認証情報の有効期限が切れると、コネクターはイベントの送信を停止します。この状態が**5日間**以上続くと、コネクターのイベントは削除され、データは永久に失われます。
{% endalert %}

![BrazeのGoogle Cloud Storage Currentsページ。このページには、統合名、連絡先メール、GCS JSON認証情報、GCSバケット名、プレフィックスのフィールドがあります。]({% image_buster /assets/img/gcs6.png %})

最後に、ページの一番下までスクロールし、エクスポートしたいメッセージエンゲージメントイベントまたは顧客行動イベントを選択します。完了したら、Currentを起動します。

### ステップ4:Google Cloud Storageのエクスポートを設定する {#step-4-set-up-google-cloud-storage-exports}

Google Cloud Storage（GCS）エクスポートを設定するには、**テクノロジーパートナー** > **Google Cloud Storage** に移動し、GCS認証情報を入力し、**Make this the default data export destination** を選択します。

エクスポートされたファイルの構成と内容は、AWS S3、Microsoft Azure、Google Cloud Storageの統合間で同一であることに留意してください。

{% alert important %}
必ず、[Google Cloudで生成された](https://cloud.google.com/iam/docs/keys-create-delete)JSONの値をすべて入力してください。
{% endalert %}

![BrazeダッシュボードのGoogle Cloud Storageページ。]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### ステップ5:サービスアカウントの認証情報をテストする（オプション） {#step-5-test-your-service-account-credentials-optional}

Google Cloud IAMサービスアカウントには以下の権限が必要です。

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Brazeダッシュボードでこれらの権限を確認するには、**Google Cloud Storage** ページに移動して、**Test Credentials** を選択します。

![BrazeダッシュボードのGoogle Cloud Storage認証情報セクション。]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## エクスポートの動作 {#export-behavior}

クラウドデータストレージソリューションを統合し、API、ダッシュボードレポート、またはCSVレポートをエクスポートしようとしているユーザーには、以下の動作が適用されます。

- すべてのAPIエクスポートでは、応答本文でダウンロードURLが返されないため、データストレージから取得する必要があります。
- すべてのダッシュボードレポートとCSVレポートは、ユーザーのメールに送信されてダウンロードされ（ストレージ権限不要）、データストレージにバックアップされます。

{% alert important %}
**JSONフォーマットの要件**：JSONエクスポートでは、BrazeはJSONL（改行区切りのJSON）フォーマットを使用し、各行に個別のJSONオブジェクトが含まれます。このフォーマットは、単一のJSON配列またはオブジェクトである標準的なJSONとは異なります。エクスポートされたファイルの各行は有効なJSONオブジェクトですが、ファイル全体としては1つの有効なJSONドキュメントではありません。これらのファイルを処理するときは、ファイル全体を1つのJSONドキュメントとしてパースするのではなく、各行を個別のJSONオブジェクトとしてパースしてください。

Currentsのエクスポートは、JSONではなく、Apache Avroフォーマット（`.avro`ファイル）を使用します。このJSONフォーマットの要件は、JSONフォーマットを使用するダッシュボードデータエクスポートおよびAPIエクスポートに適用されます。
{% endalert %}

## トラブルシューティング {#troubleshooting}

### Google Cloud Storageの認証情報が無効である {#google-cloud-storage-credentials-are-invalid}

認証情報を入力しようとしたときに以下のエラーが表示される場合：

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Google Cloud IAMサービスアカウントに以下の権限があることを確認してください。

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

確認後、[Brazeダッシュボードで認証情報をテスト](#step-5-test-your-service-account-credentials-optional)できます。