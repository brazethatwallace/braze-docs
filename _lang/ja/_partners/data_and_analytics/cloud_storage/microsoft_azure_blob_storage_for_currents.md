---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "このリファレンス記事では、Braze CurrentsとMicrosoft Azure Blob Storageのパートナーシップについて説明します。Microsoft Azure Blob Storageは、非構造化データのための大規模拡張可能オブジェクトストレージです。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) は、MicrosoftがAzure製品群の一部として提供する、非構造化データのための大規模拡張可能オブジェクトストレージです。

{% alert important %}
クラウドストレージプロバイダーを切り替える場合は、Brazeカスタマーサクセスマネージャーに連絡し、新しい統合の設定と検証についてサポートを受けてください。
{% endalert %}

BrazeとMicrosoft Azure Blob Storageの統合により、データをAzureにエクスポートし、Currentsデータをストリーミングできます。その後、ETLプロセス（抽出、変換、読み込み）を使用してデータを他の場所に転送できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Microsoft AzureとAzureストレージアカウント | このパートナーシップを利用するには、Microsoft AzureとAzureストレージアカウントが必要です。 |
| Currents | Currentsにデータをエクスポートするには、アカウントに対して[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定しておく必要があります。メッセージのアーカイブの設定のみの場合、Currentsは必要ありません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Microsoft Azure Blob Storageと統合するには、BrazeがデータをAzureにエクスポートするか、Currentsデータをストリーミングするためのストレージアカウントと接続文字列を用意しておく必要があります。

### ステップ1:ストレージアカウントを作成する {#step-1-create-a-storage-account}

Microsoft Azureで、サイドバーの**Storage Accounts**に移動し、**+ Add**をクリックして新しいストレージアカウントを作成します。次に、ストレージアカウント名を指定します。その他のデフォルト設定は更新する必要はありません。最後に**Review + create**を選択します。

すでにストレージアカウントをお持ちの場合でも、Brazeデータ専用に新しいストレージアカウントを作成することをお勧めします。

![Microsoft Azureのストレージアカウント作成ページの「基本」タブ。ストレージアカウント名フィールドがハイライトされています。]({% image_buster /assets/img/azure-currents-step-1.png %})

### ステップ2:接続文字列を取得する {#step-2-get-the-connection-string}

ストレージアカウントがデプロイされたら、ストレージアカウントから**Access Keys**メニューに移動し、接続文字列を書きとめておきます。

Microsoftは2つのアクセスキーを提供しています。1つのキーを再生成する際に、もう1つのキーを使用して接続を維持します。必要なのはどちらか一方の接続文字列だけです。

{% alert note %}
Brazeはキーではなく、このメニューの接続文字列を使用します。
{% endalert %}

![Azureストレージアカウントのアクセスキーページ。key1の下にある接続文字列フィールドがハイライトされています。]({% image_buster /assets/img/azure-currents-step-2.png %})

### ステップ3:Blobサービスコンテナーを作成する {#step-3-create-a-blob-service-container}

ストレージアカウントの**Blob Service**セクションにある**Blobs**メニューに移動します。先ほど作成したストレージアカウント内にBlobサービスコンテナーを作成します。

Blobサービスコンテナーの名前を指定します。その他のデフォルト設定は更新する必要はありません。

![AzureストレージアカウントのBlob Serviceの下にあるBlobsページ。コンテナーを追加するオプションが表示されています。]({% image_buster /assets/img/azure-currents-step-3.png %})

### ステップ4:Currentsを設定する {#step-4-set-up-currents}

Brazeで**Currents** > **+ Create Current** > **Azure Blob Data Export**に移動し、統合名と連絡先のメールアドレスを入力します。

次に、接続文字列、コンテナー名、BlobStorage接頭辞（オプション）を指定します。

![BrazeのMicrosoft Azure Blob Storage Currentsページ。このページには、統合名、連絡先メール、接続文字列、コンテナー名、接頭辞のフィールドがあります。]({% image_buster /assets/img/maz.png %})

最後に、ページの一番下までスクロールし、エクスポートしたいメッセージエンゲージメントイベントまたは顧客行動イベントを選択します。完了したら、Currentを起動します。

### ステップ5:Azureデータエクスポートを設定する {#step-5-set-up-azure-data-export}

次の目的で使用する認証情報を設定する手順を以下で説明します。
1. APIを通じたセグメントのエクスポート
2. CSVエクスポート（キャンペーン、セグメント、キャンバスのユーザーデータをダッシュボード経由でエクスポート）
3. エンゲージメントレポート

Brazeで**パートナー連携** > **テクノロジーパートナー** > **Microsoft Azure**に移動し、接続文字列、Azureストレージコンテナー名、Azureストレージ接頭辞を入力します。

次に、**Make this the default data export destination**ボックスがオンになっていることを確認します。これにより、エクスポートしたデータが確実にAzureに送信されます。完了したら、統合を保存します。

![BrazeのMicrosoft Azureデータエクスポートページ。このページには、接続文字列、コンテナー名、接頭辞のフィールドがあります。]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
接続文字列を最新の状態に維持することが重要です。コネクターの認証情報の有効期限が切れると、コネクターはイベントの送信を停止します。この状態が**48時間**以上続くと、コネクターのイベントは削除され、データは永久に失われます。
{% endalert %}

## エクスポートの動作 {#export-behavior}

クラウドデータストレージソリューションを統合しており、API、ダッシュボードレポート、またはCSVレポートをエクスポートする場合、次のような状況が発生します。

- すべてのAPIエクスポートでは、応答本文でダウンロードURLが返されないため、データストレージから取得する必要があります。
- すべてのダッシュボードレポートとCSVレポートは、ダウンロード用にユーザーのメールに送信され（ストレージの権限は不要）、データストレージにバックアップされます。

{% alert important %}
**JSONフォーマットの要件**：JSONエクスポートでは、Brazeは[JSONL](https://jsonlines.org/)（改行区切りのJSON）フォーマットを使用し、各行に個別のJSONオブジェクトが含まれます。このフォーマットは、単一のJSON配列またはオブジェクトである標準的なJSONとは異なります。エクスポートされたファイルの各行は有効なJSONオブジェクトですが、ファイル全体としては1つの有効なJSONドキュメントではありません。これらのファイルを処理するときは、ファイル全体を1つのJSONドキュメントとしてパースするのではなく、各行を個別のJSONオブジェクトとしてパースしてください。<br><br>Currentsのエクスポートは、JSONではなく[Apache Avro](https://avro.apache.org/)フォーマット（`.avro`ファイル）を使用します。このJSONフォーマットの要件は、JSONフォーマットを使用するダッシュボードデータエクスポートおよびAPIエクスポートに適用されます。
{% endalert %}

## FAQ

### BrazeはAzure Blob Storageの許可リストに追加するIPアドレスを提供できますか？ {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

Brazeは、Azure Blob StorageへのCurrentsまたはダッシュボードエクスポート用の固定IP許可リストを公開していません。Brazeは、お客様が提供する接続文字列とコンテナー名を使用してコンテナーに書き込みを行い、Azureはストレージアカウントの設定（ストレージアカウントのファイアウォールルールやプライベートエンドポイントなど）を通じてネットワークアクセスを制御します。

セキュリティチームがIPベースの制限を必要とする場合は、Brazeからのリストではなく、ストレージアカウントのAzureネットワーキング機能を使用してください。設定手順については、[Azure Storageのセキュリティに関するMicrosoftのドキュメント](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)を参照してください。