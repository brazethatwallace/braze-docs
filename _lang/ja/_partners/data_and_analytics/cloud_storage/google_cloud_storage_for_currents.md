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

| 要件 | 説明 |
| ----------- | ----------- |
| Google Cloud Storageアカウント | このパートナーシップを利用するには、Google Cloud Storageアカウントが必要です。 |
| Currents | Google Cloud Storageにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)を設定する必要があります。メッセージアーカイブのみを設定する場合、Currentsは必要ありません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

Google Cloud Storageと連携するには、Brazeが書き込み先のストレージバケットに関する情報を取得（`storage.buckets.get`）し、そのバケット内にオブジェクトを作成（`storage.objects.create`）できるようにするための適切な認証情報を設定する必要があります。

{% alert note %}
Workload Identity Federation（WIF）は、Currentsの認証方法としてサポートされていません。JSON秘密キーを持つサービスアカウントを使用する必要があります。
{% endalert %}

以下の手順に従って設定できます。この手順では、Currents連携で使用する秘密キーを生成するロールとサービスアカウントの作成方法を説明します。

### ステップ1:ロールを作成する {#step-1-create-role}

Google Cloud Platformコンソールで**IAM & admin** > **Roles** > **+ Create Role**に移動して、新しいロールを作成します。

![ロール作成アクションが表示されたGoogle Cloud IAMロールページ。]({% image_buster /assets/img/gcs1.png %})

ロールに名前を付け、**+Add Permissions**を選択して以下を選択します。

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
`storage.objects.delete`権限はオプションです。これにより、Brazeが不完全なファイルをクリーンアップできるようになります。<br><br>まれに、Google Cloudが接続を早期に終了し、BrazeがGoogle Cloud Storageに不完全なファイルを書き込むことがあります。ほとんどの場合、Brazeはリトライして正しいデータで新しいファイルを作成し、古いファイルはGoogle Cloud Storageに残ります。
{% endalert %}

{% alert important %}
バケットが[階層型名前空間](https://cloud.google.com/storage/docs/hns-overview)を使用している場合は、`storage.folders.create`権限も追加する必要があります。これらのバケットではフォルダーがマネージドリソースであるため、Brazeがエクスポートファイルのフォルダー構造を作成するにはこの権限が必要です。この権限がないと、Brazeはバケットに書き込めず、連携によるデータエクスポートが失敗します。
{% endalert %}

完了したら、**Create**を選択します。

![ストレージ権限が選択されたGoogle Cloudカスタムロールエディター。]({% image_buster /assets/img/gcs2.png %})

### ステップ2:新しいサービスアカウントを作成する {#step-2-create-a-new-service-account}

#### ステップ2.1:サービスアカウントを作成する {#step-21-create-the-service-account}

Google Cloud Platformコンソールで**IAM & admin** > **Service Accounts**に移動し、**Create Service Account**を選択して、新しいサービスアカウントを作成します。

![「Create Service Account」が選択されたGoogle Cloudサービスアカウントページ。]({% image_buster /assets/img/gcs3.png %})

次に、サービスアカウントに名前を付け、新しく作成したカスタムロールへのアクセスを付与します。

![Google Cloud Platformのサービス作成ページで、「Select a Role」フィールドにロール名を入力します。]({% image_buster /assets/img/gcs4.png %})

#### ステップ2.2:キーを作成する {#step-22-create-a-key}

ページの下部にある**Create Key**ボタンを使用して、Brazeで使用する**JSON**秘密キーを作成します。キーが作成されると、マシンにダウンロードされます。

![キータイプがJSONに設定されたGoogle Cloudサービスアカウントキー作成ダイアログ。]({% image_buster /assets/img/gcs5.png %})

### ステップ3:BrazeでCurrentsを設定する {#step-3-set-up-currents-in-braze}

Brazeで**Currents** > **+ Create Current** > **Google Cloud Storage Data Export**に移動し、連携名と連絡先メールアドレスを入力します。

次に、**GCS JSON Credentials**でJSON秘密キーをアップロードし、GCSバケット名とGCSプレフィックス（オプション）を入力します。これらの認証情報は、前のステップで説明したとおり、Google Cloud Platformで生成する必要があります。

{% alert important %}
認証情報ファイルを最新の状態に保つことが重要です。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を停止します。この状態が**5日間**以上続くと、コネクターのイベントは破棄され、データは永久に失われます。
{% endalert %}

![BrazeのGoogle Cloud Storage Currentsページ。このページには、連携名、連絡先メール、GCS JSON認証情報、GCSバケット名、プレフィックスのフィールドがあります。]({% image_buster /assets/img/gcs6.png %})

最後に、ページの下部までスクロールし、エクスポートするメッセージエンゲージメントイベントまたは顧客行動イベントを選択します。完了したら、Currentを起動します。

### ステップ4:Google Cloud Storageエクスポートを設定する {#step-4-set-up-google-cloud-storage-exports}

Google Cloud Storage（GCS）エクスポートを設定するには、**テクノロジーパートナー** > **Google Cloud Storage**に移動し、GCS認証情報を入力して、**Make this the default data export destination**を選択します。

エクスポートされるファイルの構成と内容は、AWS S3、Microsoft Azure、Google Cloud Storageの連携間で同一であることに留意してください。

{% alert important %}
[Google Cloudで生成された](https://cloud.google.com/iam/docs/keys-create-delete)完全なJSON値を入力してください。
{% endalert %}

![BrazeダッシュボードのGoogle Cloud Storageページ。]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### ステップ5:サービスアカウントの認証情報をテストする（オプション） {#step-5-test-your-service-account-credentials-optional}

Google Cloud IAMサービスアカウントには、以下の権限が必要です。

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

これらの権限をBrazeダッシュボードで確認するには、**Google Cloud Storage**ページに移動し、**Test Credentials**を選択します。

![BrazeダッシュボードのGoogle Cloud Storage認証情報セクション。]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## エクスポートの動作 {#export-behavior}

クラウドデータストレージソリューションを統合し、APIエクスポート、ダッシュボードレポート、またはCSVレポートをエクスポートしようとしているユーザーは、以下の動作を経験します。

- すべてのAPIエクスポートは、レスポンスボディにダウンロードURLを返さず、データストレージから取得する必要があります。
- すべてのダッシュボードレポートとCSVレポートは、ダウンロード用にユーザーのメールに送信され（ストレージ権限は不要）、データストレージにバックアップされます。

{% alert important %}
**JSON形式の要件**：JSONエクスポートの場合、BrazeはJSONL（改行区切りJSON）形式を使用します。各行には個別のJSONオブジェクトが含まれます。この形式は、単一のJSON配列またはオブジェクトである標準JSONとは異なります。エクスポートされたファイルの各行は有効なJSONオブジェクトですが、ファイル全体は単一の有効なJSONドキュメントではありません。これらのファイルを処理する際は、ファイル全体を単一のJSONドキュメントとして解析しようとするのではなく、各行を個別のJSONオブジェクトとして解析してください。

Currentsエクスポートは、JSONではなくApache Avro形式（`.avro`ファイル）を使用します。このJSON形式の要件は、ダッシュボードデータエクスポートおよびJSON形式を使用するAPIエクスポートに適用されます。
{% endalert %}

## トラブルシューティング {#troubleshooting}

### Google Cloud Storageの認証情報が無効 {#google-cloud-storage-credentials-are-invalid}

認証情報を入力しようとした際に以下のエラーが表示された場合:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Google Cloud IAMサービスアカウントに以下の権限があることを確認してください:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

確認後、[Brazeダッシュボードで認証情報をテスト](#step-5-test-your-service-account-credentials-optional)できます。