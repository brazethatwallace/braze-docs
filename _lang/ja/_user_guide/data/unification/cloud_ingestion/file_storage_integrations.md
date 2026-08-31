---
nav_title: ファイルストレージの連携
article_title: ファイルストレージの連携
description: "このページでは、Brazeクラウドデータ取り込みと、Amazon S3またはGoogle Cloud StorageからBrazeへの関連データの同期方法について説明します。"
page_order: 4
page_type: reference

---

# ファイルストレージの連携 {#file-storage-integrations}

> このページでは、クラウドデータ取り込みを設定し、Amazon S3またはGoogle Cloud StorageからBrazeにデータを同期する方法について説明します。

## 仕組み {#how-it-works}

Cloud Data Ingestion（CDI）を使用すると、クラウドアカウント内の1つ以上のストレージバケットをBrazeと直接統合できます。バケットに新しいファイルが追加されると、クラウドプロバイダーが通知を発行し、Braze Cloud Data Ingestionがデータを同期します。

通知の仕組みはプロバイダーによって異なります。

- **Amazon S3:** S3に新しいファイルが公開されると、Amazon Simple Queue Service（SQS）キューにメッセージが投稿され、Brazeがそのメッセージを消費して新しいファイルを取り込みます。
- **Google Cloud Storage（GCS）:** バケットで新しいファイルがファイナライズされると、GCSが`OBJECT_FINALIZE`通知をPub/Subトピックに発行します。BrazeはPub/Subサブスクリプションからそれらの通知を消費して新しいファイルを取り込みます。

Cloud Data Ingestionは以下をサポートしています。

- JSONファイル
- CSVファイル
- Parquetファイル
- 属性、カスタมイベント、購入イベント、ユーザー削除、およびカタログデータ

## クラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion}

設定手順はファイルストレージプロバイダーによって異なります。プロバイダーのタブを選択してから、続くセクションの共有設定を完了してください。

{% tabs %}
{% tab Amazon S3 %}

この連携には以下のリソースが必要です。

- データストレージ用のS3バケット
- 新しいファイル通知用のSQSキュー
- Brazeアクセス用のIAMロール

### AWSの定義 {#aws-definitions}

| 用語 | 定義 |
| --- | --- |
| Amazon リソースネーム (ARN) | ARNはAWSリソースの一意の識別子です。 |
| Identity and Access Management (IAM) | IAMはAWSリソースへのアクセスを安全に制御するためのWebサービスです。このチュートリアルでは、IAMポリシーを作成してIAMロールに割り当て、S3バケットをBrazeクラウドデータ取り込みと連携します。 |
| Amazon Simple Queue Service (SQS) | SQSは、分散型ソフトウェアシステムとコンポーネントを連携するためのホスト型キューです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="AWSの定義" }

## AWSでのクラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion-in-aws}

### ステップ1:ソースバケットを作成する {#step-1-create-a-source-bucket}

AWSアカウントでデフォルト設定の汎用S3バケットを作成します。S3バケットはフォルダが一意であれば、複数の同期で再利用できます。

デフォルト設定は以下のとおりです。

- ACL無効
- パブリックアクセスをすべてブロック
- バケットのバージョニングを無効化
- SSE-S3暗号化
  - SSE-S3は唯一サポートされているサーバーサイド暗号化タイプです。Amazon KMS暗号化はサポートされていません。

バケットを作成したリージョンをメモしてください。次のステップで同じリージョンにSQSキューを作成します。

### ステップ2:SQSキューを作成する {#step-2-create-sqs-queue}

作成したバケットにオブジェクトが追加されたことを追跡するためのSQSキューを作成します。現時点ではデフォルトの設定を使用してください。

SQSキューはグローバルに一意である必要があります（たとえば、1つのCDI同期にのみ使用でき、別のワークスペースで再利用することはできません）。

{% alert important %}
SQSはバケットを作成したリージョンと同じリージョンに作成してください。
{% endalert %}

SQSキューのARNとURLをメモしてください。この設定中に頻繁に必要になります。

![キューにアクセスできるユーザーを定義するJSONオブジェクトの例が表示された「Advanced」を選択した画面。]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### ステップ3:アクセスポリシーを設定する {#step-3-set-up-access-policy}

アクセスポリシーを設定するには、**Advanced options**を選択します。

以下のステートメントをキューのアクセスポリシーに追加します。`YOUR-BUCKET-NAME-HERE`をバケット名に、`YOUR-SQS-ARN`をSQSキューのARNに、`YOUR-AWS-ACCOUNT-ID`をAWSアカウントIDにそれぞれ置き換えてください。

``` json
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
}
```

### ステップ4:S3バケットにイベント通知を追加する {#step-4-add-an-event-notification-to-the-s3-bucket}

1. ステップ1で作成したバケットで、**Properties** > **Event notifications**に移動します。
2. 設定に名前を付けます。Brazeに取り込むファイルのサブセットのみを対象にしたい場合は、オプションでプレフィックスまたはサフィックスを指定します。
3. **Destination**で**SQS queue**を選択し、ステップ2で作成したSQSのARNを入力します。

{% alert note %}
S3バケットのルートフォルダにファイルをアップロードしてから、一部のファイルをバケット内の特定のフォルダに移動すると、予期しないエラーが発生する場合があります。代わりに、プレフィックス内のファイルのみに対してイベント通知を送信するように変更するか、そのプレフィックス外にS3バケットにファイルを配置しないようにするか、プレフィックスなしで連携を更新してすべてのファイルを取り込むようにしてください。
{% endalert %}

### ステップ5:IAMポリシーを作成する {#step-5-create-an-iam-policy}

Brazeがソースバケットとやり取りできるようにするためのIAMポリシーを作成します。開始するには、アカウント管理者としてAWS管理コンソールにサインインします。

1. AWSコンソールのIAMセクションに移動し、ナビゲーションバーで**Policies**を選択してから、**Create Policy**を選択します。<br><br>![AWSコンソールの「Create policy」ボタン。]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. **JSON**タブを開き、以下のコードスニペットを**Policy Document**セクションに入力します。`YOUR-BUCKET-NAME-HERE`をバケット名に、`YOUR-SQS-ARN-HERE`をSQSキュー名にそれぞれ置き換えてください。

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```

{: start="3"}
3. 完了したら**Review Policy**を選択します。

4. ポリシーに名前と説明を付けてから、**Create Policy**を選択します。

![「new-policy-name」という名前のポリシーの例。]({% image_buster /assets/img/create_policy_3_name.png %})

![ポリシーの説明フィールド。]({% image_buster /assets/img/create_policy_4_created.png %})

### ステップ6:IAMロールを作成する {#step-6-create-an-iam-role}

AWSでの設定を完了するには、IAMロールを作成し、ステップ5のIAMポリシーをアタッチします。

1. IAMポリシーを作成したコンソールの同じIAMセクションで、**Roles** > **Create Role**に移動します。

![「Create role」ボタン。]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. AWSで、信頼されたエンティティセレクタータイプとして**Another AWS Account**を選択します。BrazeアカウントIDを入力します。**Require external ID**チェックボックスを選択します。
3. Brazeで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択してから、ファイルソースセクションで**Amazon S3**を選択します。
4. 自動生成された**Braze Account ID**をコピーします。

![ソース名とS3接続詳細セクションが表示された「Add New Source」ページ。]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. AWSでアカウントIDを貼り付けてから、**Next**を選択します。

![S3の「Create Role」ページ。このページにはロール名、ロールの説明、信頼されたエンティティ、ポリシー、アクセス許可の境界のフィールドがあります。]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. ステップ4で作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横にあるチェックマークを選択してアタッチします。完了したら**Next**を選択します。

![new-policy-nameが選択されたロールARN。]({% image_buster /assets/img/create_role_3_attach.png %})

ロールに名前と説明を付けてから、**Create Role**を選択します。

![「new-role-name」という名前のロールの例。]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. 作成したロールのARNと生成した外部IDをメモしてください。クラウドデータ取り込み連携の作成に必要になります。

## Brazeでのクラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion-in-braze}

1. まず、Brazeダッシュボードで新しいソースを作成します。**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択してから、**Amazon S3**を選択します。
2. ソースの名前を選択し、AWSの設定プロセスで取得した情報を入力して新しいソースを作成します。以下を指定してください。

  - ロールARN
  - 外部ID
  - バケット名
  - リージョン

![認証情報（AWSの設定とBrazeの設定）と設定フィールドが表示されたS3接続詳細セクション。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. **Test connection**を選択して、Brazeがバケットにアクセスできることを確認します。テストが成功したら、**Connect to Source**を選択します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{: start="4"}
4. 次に、新しい同期を作成します。**Data Settings** > **Cloud Data Ingestion** > **Syncs**に移動し、**Create data sync**を選択します。

{: start="5"}
5. 同期の名前を選択します。次に、アクティブなS3ソースを選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**を選択します。

![データプレビュー付きの接続テストオプション。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. AWSの設定プロセスで取得した残りの情報を入力します。以下を指定してください。
- SQS URL（新しい連携ごとに一意である必要があります）
- フォルダパス（オプション、ワークスペース内の同期間で一意である必要があります）

7. データタイプを選択し、**Test Connection**を選択して、Brazeが取り込み可能なファイルを一覧表示できることを確認します（ファイル内のデータではありません）。成功したら、**Next: Notifications**を選択します。
8. アクセスや権限の問題で同期が中断された場合の通知用に、連絡先メールアドレスを追加します。オプションで、ユーザーレベルのエラーや同期成功の通知を有効にできます。
9. 同期を作成します。

{% endtab %}
{% tab Google Cloud Storage %}

この連携には以下のリソースが必要です。

- データストレージ用のCloud Storageバケット
- 新しいファイル通知用のPub/Subトピックとサブスクリプション
- JSONキーをBrazeにアップロードするサービスアカウント

### GCPの定義 {#gcp-definitions}

| 用語 | 定義 |
| --- | --- |
| Google Cloudプロジェクト | プロジェクトはすべてのGoogle Cloudリソースを整理するもので、一意のプロジェクトIDとプロジェクト番号で識別されます。 |
| Cloud Storageバケット | バケットは、Brazeに取り込むデータファイルを保持するコンテナです。 |
| Pub/Subトピック | トピックは、Cloud Storageバケットから新しいファイルの通知を受け取る名前付きリソースです。 |
| Pub/Subサブスクリプション | サブスクリプションはトピックにアタッチされ、メッセージを配信します。Brazeはプルサブスクリプションから新しいファイルの通知を受け取ります。 |
| サービスアカウント | サービスアカウントは、Brazeがバケットとサブスクリプションにアクセスするために使用する非人間IDです。JSONキーをBrazeにアップロードします。 |
| IAMロール | Identity and Access Management (IAM) ロールは、バケットとサブスクリプションのサービスアカウントに割り当てる権限の集合です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="GCPの定義" }

## Google Cloudでのクラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion-in-google-cloud}

### ステップ1:Cloud Storageバケットを作成する {#step-1-create-a-cloud-storage-bucket}

Google Cloudコンソールで、**Cloud Storage** > **Buckets** > **Create**に移動します。プロジェクトIDとバケット名をメモしてください。Brazeでソースを設定する際に必要になります。権限がIAMで管理されるように、均一なバケットレベルアクセスを有効にすることをお勧めします。

または、gcloudでバケットを作成できます。

```shell
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=YOUR-REGION \
  --uniform-bucket-level-access
```

### ステップ2:Pub/Subトピックとサブスクリプションを作成する {#step-2-create-a-pubsub-topic-and-subscription}

Google Cloudコンソールで、**Pub/Sub** > **Topics** > **Create topic**に移動します。Googleにデフォルトのサブスクリプションを作成させるか、別途作成できます。次に、そのトピックに**プル**サブスクリプションを作成します。

または、gcloudを使用します。

```shell
gcloud pubsub topics create YOUR-TOPIC --project=YOUR-PROJECT-ID
gcloud pubsub subscriptions create YOUR-SUBSCRIPTION \
  --topic=YOUR-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
```

**サブスクリプションID**をメモしてください。Brazeでは同期作成時にサブスクリプション（トピックではなく）が必要です。サブスクリプションはプルサブスクリプションである必要があります。

{% alert warning %}
このサブスクリプションにデッドレターキューを設定しないでください。Brazeはクラウドデータ取り込みサブスクリプションのデッドレターキューをサポートしていません。詳しくは、Google Cloudドキュメントの[デッドレタートピック](https://cloud.google.com/pubsub/docs/dead-letter-topics)を参照してください。
{% endalert %}

### ステップ3:バケット通知をトピックに送信する {#step-3-send-bucket-notifications-to-the-topic}

{% alert important %}
Cloud StorageからPub/Subへの通知の作成は、Google Cloudコンソールでは利用できません。gcloud（ここに示す）、Terraform、またはJSON APIを使用する必要があります。詳しくは、Google Cloudドキュメントの[Cloud StorageのPub/Sub通知を設定する](https://cloud.google.com/storage/docs/reporting-changes#enabling)を参照してください。
{% endalert %}

まず、Cloud Storageサービスエージェントにトピックへの公開権限を割り当ててから、`OBJECT_FINALIZE`の通知を作成します。`OBJECT_FINALIZE`イベントは、バケットに新しいオブジェクトが作成またはファイナライズされるたびに発火します。

```shell
# Get the Cloud Storage service agent for your project
gcloud storage service-agent --project=YOUR-PROJECT-ID

# Assign it Pub/Sub Publisher on the topic
gcloud pubsub topics add-iam-policy-binding YOUR-TOPIC \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"

# Create the OBJECT_FINALIZE notification (optionally scope to a folder with --object-prefix)
gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
  --topic=YOUR-TOPIC \
  --event-types=OBJECT_FINALIZE \
  --payload-format=json
```

これらのコマンドの以下のプレースホルダーを置き換えてください。

- `YOUR-PROJECT-ID`: Google CloudプロジェクトID。人間が読める識別子です（例: `my-gcp-project`）。
- `YOUR-TOPIC`: [ステップ2](#step-2-create-a-pubsub-topic-and-subscription)で作成したPub/Subトピック。
- `YOUR-BUCKET-NAME`: Cloud Storageバケット名。
- `YOUR-PROJECT-NUMBER`: プロジェクト番号。Cloud Storageサービスエージェントのメールアドレスで使用される数値の識別子です。プロジェクトIDとは異なります。Google Cloudコンソールの**Dashboard**で確認するか、以下のコマンドを実行してください。

```shell
gcloud projects describe YOUR-PROJECT-ID --format="value(projectNumber)"
```

### ステップ4:サービスアカウントを作成する {#step-4-create-a-service-account}

Google Cloudコンソールで、**IAM & Admin** > **Service Accounts** > **Create service account**に移動します。

または、gcloudを使用します。

```shell
gcloud iam service-accounts create braze-cdi-gcs \
  --project=YOUR-PROJECT-ID \
  --display-name="Braze CDI GCS"
```

### ステップ5:権限を割り当てる {#step-5-assign-permissions}

コネクタには次の権限が必要です: バケットに対する`storage.buckets.get`、`storage.objects.get`、`storage.objects.list`、およびサブスクリプションに対する`pubsub.subscriptions.consume`。カスタムロールまたは事前定義ロールで割り当てることができます。

**カスタムロール:** これらの権限を持つカスタムロールを作成し、バケットとサブスクリプションにバインドします。

```shell
gcloud iam roles create brazeCdiGcs --project=YOUR-PROJECT-ID \
  --title="Braze CDI GCS" \
  --permissions=storage.buckets.get,storage.objects.get,storage.objects.list,pubsub.subscriptions.consume \
  --stage=GA

gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"

gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"
```

**事前定義ロール:** バケットに`roles/storage.objectViewer`と`roles/storage.legacyBucketReader`を、サブスクリプションに`roles/pubsub.subscriber`を割り当てます。`objectViewer`ロールは`storage.objects.get`と`storage.objects.list`を提供し、`legacyBucketReader`は`storage.buckets.get`を提供します。

```shell
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.legacyBucketReader"
gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber"
```

### ステップ6:JSONキーを作成する {#step-6-create-a-json-key}

Google Cloudコンソールでサービスアカウントを開き、**Keys** > **Add key** > **Create new key**に移動して、**JSON**を選択します。

または、gcloudを使用します。

```shell
gcloud iam service-accounts keys create braze-cdi-gcs-key.json \
  --iam-account=braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com
```

## Brazeでのクラウドデータ取り込みの設定

1. Brazeで、**Data Settings** > **Cloud Data Ingestion** > **Sources**に移動し、**Add data source**を選択してから、**Google Cloud Storage**を選択します。

![データソースの一覧からGoogle Cloud Storageが選択された「Add New Source」画面。]({% image_buster /assets/img/cloud_ingestion/gcs_source_picker.png %})

{: start="2"}
2. ソースフィールドに入力します。
    - **Bucket** — バケット名
    - **Project ID** — GCPプロジェクトID
    - **Service account JSON key** — ステップ6のキーファイルをアップロードし、認証情報に名前を付けます

![バケット、プロジェクトID、認証情報アップロードフィールドが表示されたGoogle Cloud Storageソースフォーム。]({% image_buster /assets/img/cloud_ingestion/gcs_source_form.png %})

{: start="3"}
3. **Test connection**を選択してから、**Connect to Source**を選択します。
4. 同期を作成します。**Data Settings** > **Cloud Data Ingestion** > **Syncs**に移動し、**Create data sync**を選択します。同期名と**Data Type**（**User Attributes**、**Custom Events**、**Purchase Events**、**Catalog**、**Delete Users**など）を選択してから、**Next**を選択します。
5. **Data definition**ステップで、GCSソースを選択してから、以下を指定します。
    - **Pub/Sub subscription ID** — ステップ2のサブスクリプションID（トピックではありません）
    - **Folder path**（オプション）— バケット内のパスプレフィックス（[共有バケット内のフォルダを同期する](#syncing-a-folder-in-a-shared-bucket)を参照）

![Pub/SubサブスクリプションIDとフォルダパスフィールドが表示されたGoogle Cloud Storage同期フォーム。]({% image_buster /assets/img/cloud_ingestion/gcs_sync_form.png %})

{: start="6"}
6. **Preview and validate**を選択して、Brazeがサブスクリプションにアクセスし、取り込み可能なファイルを一覧表示できることを確認します。テストが成功すると、バケット内の既存ファイルが一覧表示されますが、それらのファイルは自動的に同期されません。
7. エラー通知用の連絡先メールアドレスを追加します。Google Cloud Storageの同期はイベント駆動型であるため、スケジュールは必要ありません。Brazeはファイルがアップロードされると取り込みます。サマリーを確認してから、**Create sync**を選択します。

### 共有バケット内のフォルダを同期する {#syncing-a-folder-in-a-shared-bucket}

1つのバケットを複数の同期で再利用できますが、各同期は個別のフォルダを対象とし、**かつ**専用のPub/Subサブスクリプションを持つ必要があります。


{% alert important %}
フォルダパスとサブスクリプションは、同じソースバケットを共有する複数の同期のワークスペース内で一意である必要があります。[ステップ2](#step-2-create-a-pubsub-topic-and-subscription)と同様に、これらのサブスクリプションにデッドレターキューを設定しないでください。
{% endalert %}

共有バケット内で同期したいフォルダごとに:

1. 同期の**Folder**フィールドをパスプレフィックスに設定します（例: `attributes/`）。Brazeはそのプレフィックスで始まるパスのオブジェクトのみを一覧表示して取り込みます。
2. そのフォルダ用に専用のトピックとプレフィックススコープの通知を作成し、そのトピックにサブスクリプションを作成します。

    ```shell
    # One topic per folder
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Assign the Cloud Storage service agent publisher on the topic
    gcloud pubsub topics add-iam-policy-binding YOUR-ATTRIBUTES-TOPIC \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
      --role="roles/pubsub.publisher"

    # Notification scoped to the folder with --object-prefix
    gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
      --topic=YOUR-ATTRIBUTES-TOPIC --event-types=OBJECT_FINALIZE \
      --payload-format=json --object-prefix=attributes/

    # One subscription per sync
    gcloud pubsub subscriptions create YOUR-ATTRIBUTES-SUBSCRIPTION \
      --topic=YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
    ```

3. [ステップ5](#step-5-assign-permissions)と同様に、Brazeサービスアカウントにそのサブスクリプションの消費権限を割り当てます。

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    [ステップ5](#step-5-assign-permissions)でカスタムロールを作成した場合は、代わりに`--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"`を使用してください。
4. Brazeで同期を作成する際に、このフォルダの新しい**Pub/Sub subscription ID**と**Folder path**を入力して、そのフォルダのファイルのみを取り込むようにします。


{% endtab %}
{% endtabs %}

## 必要なファイル形式 {#required-file-formats}

必要なファイル形式は Amazon S3 と Google Cloud Storage で共通です。Cloud Data Ingestion は JSON、CSV、Parquet ファイルをサポートしています。必要なカラムはデータタイプによって異なります。

- ユーザーデータ（属性、カスタムイベント、購入イベント）はユーザー識別子とペイロードを使用します
- カタログデータはカタログ識別子を使用します

カタログデータにファイルストレージを使用している場合は、このページと[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を併せて参照し、カタログ固有の要件と動作を確認してください。

Braze は、ファイルストレージプロバイダーが適用する要件以外に、追加のファイル名要件を適用しません。ファイル名は一意である必要があります。タイムスタンプを付加すると一意性を確保しやすくなります。

サポートされているすべてのファイルタイプ（属性、カスタムイベント、購入、カタログ、ユーザー削除）の例については、[braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage) のサンプルファイルを参照してください。

### ユーザー識別子 {#user-identifiers}

ユーザーデータの同期（属性、カスタムイベント、購入イベント）では、ソースファイルの各行に正確に1つのユーザー識別子と `PAYLOAD` カラムが必要です。ソースファイルには異なる識別子タイプの行を含めることができますが、各行では1つの識別子のみを使用してください。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | 更新するユーザーを識別します。Brazeで使用される `external_id` の値と一致する必要があります。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | この2つのカラムでユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子で、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに設定できる `alias_name` は1つだけです。 |
| `BRAZE_ID` | Brazeユーザー識別子です。Braze SDKによって生成され、Cloud Data Ingestion を通じて Braze ID で新しいユーザーを作成することはできません。新しいユーザーを作成するには、external ID またはユーザーエイリアスを指定してください。 |
| `EMAIL` | ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最後に更新されたプロファイルが優先されます。メールと電話番号の両方を含む場合、Brazeはメールを主要な識別子として使用します。 |
| `PHONE` | ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最後に更新されたプロファイルが優先されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー識別子" }

識別子に加えて、各行には Braze のユーザーに同期するフィールドの JSON 文字列を含む `PAYLOAD` カラムが必要です。

{% alert note %}
データウェアハウスソースとは異なり、`UPDATED_AT` カラムはファイルストレージ同期では必要なく、サポートもされていません。
{% endalert %}

### カタログ識別子 {#catalog-identifiers}

カタログ同期の場合、ソースファイルには以下のカラムが必要です。カタログファイルはユーザーデータファイルとは異なる識別子を使用します。

| カラム | 必須 | 説明 |
| --- | --- | --- |
| `ID` | はい | カタログアイテムの一意の識別子です。Brazeでのアイテムの作成、更新、削除に使用されます。 |
| `PAYLOAD` | はい | 同期するカタログフィールドと値の JSON 文字列です。Brazeのカタログのスキーマと一致する必要があります。 |
| `DELETED` | いいえ | `true` の場合、一致する `ID` のカタログアイテムが Braze のカタログから削除されます。作成または更新操作ではこのカラムを省略するか、`false` に設定してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カタログ識別子" }

### 例 {#examples}

{% tabs %}
{% tab JSON 属性 %}
``` json
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```
{% alert important %}
ソースファイルの各行には有効な JSON が含まれている必要があります。含まれていない場合、そのファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSON カスタムイベント %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
ソースファイルの各行には有効な JSON が含まれている必要があります。含まれていない場合、そのファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSON 購入イベント %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
ソースファイルの各行には有効な JSON が含まれている必要があります。含まれていない場合、そのファイルはスキップされます。
{% endalert %}

{% endtab %}
{% tab CSV 属性 %}
```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV カタログ %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
オプションの `DELETED` カラムを含めることができます。`DELETED` が `true` の場合、そのカタログアイテムは Braze のカタログから削除されます。必要なカラムの完全なリストについては、[カタログ識別子](#catalog-identifiers)を参照してください。削除の動作については、[カタログアイテムの削除](#deleting-catalog-items)を参照してください。エンドツーエンドのカタログ設定フロー（対象カタログの作成と同期動作を含む）については、[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を参照してください。
{% endtab %}

{% endtabs %}

## データの削除 {#deleting-data}

ファイルストレージ向けのCloud Data Ingestionでは、ファイルアップロードを通じてユーザーやカタログアイテムを削除できます。それぞれ別の同期とファイル形式を使用してください。

- **[ユーザーの削除](#deleting-users)** – データタイプを**Delete Users**に設定した同期を作成し、ユーザー識別子のみを含むファイル（ペイロードなし）をアップロードします。
- **[カタログアイテムの削除](#deleting-catalog-items)** – 既存のカタログ同期を使用し、`deleted`（または`DELETED`）カラムを追加して削除対象のアイテムをマークします。

### ユーザーの削除 {#deleting-users}

ソースバケット内のファイルを使用してBrazeのユーザープロファイルを削除するには、次の手順を実行します。

1. 新しいCloud Data Ingestion同期を作成します（他の同期と同じ設定です）。
2. Brazeで同期を構成する際、**Data Type**を**Delete Users**に設定します。
3. ユーザー識別子カラムのみを含むファイルをソースバケットにアップロードします。`PAYLOAD`カラムは含めないでください。誤った削除を防ぐため、ペイロードが存在すると同期が失敗します。

ファイル内の各行は、以下のいずれかを使用して正確に1人のユーザーを識別する必要があります。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | Brazeで使用される`external_id`と一致します。 |
| `ALIAS_NAME`と`ALIAS_LABEL` | 両方のカラムを組み合わせて、エイリアスでユーザーを識別します。 |
| `BRAZE_ID` | Brazeが生成したユーザーID（既存ユーザーのみ）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーの削除" }

{% alert important %}
ユーザーの削除は永続的であり、元に戻すことはできません。削除する予定のユーザーのみを含めてください。詳細については、[Cloud Data Ingestionでユーザーを削除する]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users)を参照してください。
{% endalert %}

**例 – JSON（ユーザー削除）：**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**例 – CSV（ユーザー削除）：**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

同期が実行されると、Brazeはバケット内の新しいファイルを処理し、対応するユーザープロファイルを削除します。

### カタログアイテムの削除 {#deleting-catalog-items}

ファイルストレージを使用してカタログからアイテムを削除するには、次の手順を実行します。

1. [カタログデータの同期]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)に使用しているものと同じ同期（データタイプ**Catalogs**）を使用します。
2. CSVまたはJSONファイルに、オプションの**`deleted`**（または**`DELETED`**）カラムを追加します。
3. Brazeのカタログから削除したいカタログアイテムに対して、`deleted`を`true`に設定します。

各行には引き続き`ID`と`PAYLOAD`が必要です。削除対象としてマークされた行については、ペイロードは最小限で構いません。Brazeは`ID`によってアイテムを削除します。

**例 – JSON（カタログアイテムの削除）：**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**例 – CSV（カタログアイテムの削除）：**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

同期が実行されると、`deleted: true`が設定された行に対応するカタログアイテムがBrazeで削除されます。カタログの同期と削除の動作の詳細については、[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を参照してください。

## 知っておくべきこと {#things-to-know}

- ソースバケットに追加するファイルは512&nbsp;MBを超えないようにしてください。この制限はAmazon S3とGoogle Cloud Storageの両方に適用されます。512&nbsp;MBを超えるファイルはエラーとなり、Brazeに同期されません。
- 1ファイルあたりの行数に追加の制限はありませんが、同期の実行速度を向上させるために、より小さいファイルを使用することをお勧めします。例えば、500&nbsp;MBのファイル1つを取り込むよりも、100&nbsp;MBのファイル5つに分割した方がかなり速くなります。
- 一定時間内にアップロードできるファイル数に追加の制限はありません。
- ファイル内およびファイル間での順序付けはサポートされていません。予想される競合を監視している場合は、定期的に更新をバッチ処理することをお勧めします。

## トラブルシューティング {#troubleshooting}

### ファイルのアップロードと処理 {#uploading-files-and-processing}

CDIは、同期が作成された後に追加されたファイルのみを処理します。このプロセスでは、Brazeが新しいファイルの追加を検出し、新しい通知をトリガーします。これにより、新しいファイルを処理するための新しい同期が開始されます。Amazon S3の場合、通知はSQSへのメッセージです。Google Cloud Storageの場合、Pub/Subへの`OBJECT_FINALIZE`メッセージです。

既存のファイルを使用して、Brazeがバケットにアクセスし、取り込むファイルを検出できることを検証できますが、それらのファイルはBrazeに同期されません。CDIでそれらを処理するには、同期したい既存のファイルをソースバケットに再アップロードする必要があります。

### 予期しないファイルエラーの処理（Amazon S3） {#handling-unexpected-file-errors-amazon-s3}

多数のエラーや失敗したファイルが発生している場合、CDIのターゲットフォルダ以外のフォルダでS3バケットにファイルを追加している別のプロセスが存在する可能性があります。

ファイルがソースバケットにアップロードされたがソースフォルダ内ではない場合、CDIはSQS通知を処理しますが、そのファイルに対してアクションを実行しないため、エラーとして表示される場合があります。

問題がS3通知やSQS送信先の権限に関連している場合（送信先の検証エラーなど）、AWSのドキュメントを参照してください：

- [Amazon S3コンソールを使用したイベント通知の有効化と設定](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [送信先にイベント通知メッセージを公開する権限の付与](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Amazon SQSの問題のトラブルシューティング](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### 予期しないファイルエラーの処理（Google Cloud Storage） {#handling-unexpected-file-errors-google-cloud-storage}

Amazon S3と同様に、CDIは同期が作成された後にアップロードされたファイルのみを処理します。新しいオブジェクトごとにPub/Subトピックへの`OBJECT_FINALIZE`メッセージがトリガーされます。バケットに既に存在するファイルを取り込むには、それらを再アップロードしてください。

ファイルが取り込まれない場合は、以下を確認してください：

- バケット通知が存在すること。`gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME`を使用してバケットの通知を一覧表示できます。
- Cloud Storageサービスエージェントがトピックに対して`roles/pubsub.publisher`の権限を持っていること。
- Brazeサービスアカウントがサブスクリプションに対する使用権限（`pubsub.subscriptions.consume`、カスタムロールまたは`roles/pubsub.subscriber`を通じて割り当て）を持っていること。
- サブスクリプションにデッドレターキューが設定されていないこと。BrazeはCloud Data Ingestionサブスクリプションのデッドレターキューをサポートしていません。

詳細については、Google Cloudドキュメントの[Cloud StorageのPub/Sub通知](https://cloud.google.com/storage/docs/pubsub-notifications)を参照してください。