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

クラウドデータ取り込み（CDI）を使用して、クラウドアカウントの1つ以上のストレージバケットをBrazeと直接統合できます。新規ファイルがバケットに追加されると、クラウドプロバイダーが通知を発行し、Brazeクラウドデータ取り込みがデータを同期します。

通知メカニズムはプロバイダーによって異なります。

- **Amazon S3:** 新規ファイルがS3にパブリッシュされると、Amazon Simple Queue Service（SQS）キューにメッセージが投稿され、Brazeがそのメッセージを消費して新規ファイルを取り込みます。
- **Google Cloud Storage（GCS）:** 新規ファイルがバケットでファイナライズされると、GCSがPub/Subトピックに`OBJECT_FINALIZE`通知を発行します。BrazeはPub/Subサブスクリプションからそれらの通知を消費して新規ファイルを取り込みます。

クラウドデータ取り込みは、以下をサポートしています。

- JSONファイル
- CSVファイル
- Parquetファイル
- 属性、カスタムイベント、購入イベント、ユーザー削除、カタログデータ

## クラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion}

設定手順はファイルストレージプロバイダーによって異なります。お使いのプロバイダーのタブを選択し、その後に続く共通設定セクションを完了してください。

{% tabs %}
{% tab Amazon S3 %}

連携には次のリソースが必要です。

- データストレージ用のS3バケット
- 新規ファイル通知用のSQSキュー
- Brazeアクセス用のIAMロール

### AWSの定義 {#aws-definitions}

| 用語 | 定義 |
| --- | --- |
| Amazon リソースネーム（ARN） | ARNは、AWSリソースの一意の識別子です。 |
| アイデンティティとアクセス管理（IAM） | IAMは、AWSリソースへのアクセスを安全にコントロールできるWebサービスです。このチュートリアルでは、IAMポリシーを作成し、それをIAMロールに割り当てて、S3バケットをBrazeクラウドデータ取り込みと統合します。 |
| Amazon Simple Queue Service（SQS） | SQSは、分散ソフトウェアシステムとコンポーネントを統合できるホストキューです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="AWSの定義" }

## AWSでのクラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion-in-aws}

### ステップ1:ソースバケットの作成 {#step-1-create-a-source-bucket}

AWSアカウントでデフォルト設定の汎用S3バケットを作成します。S3バケットは、フォルダーが一意である限り、同期間で再利用できます。

デフォルト設定は次のとおりです。

- ACL無効
- すべてのパブリックアクセスをブロック
- バケットのバージョン管理を無効化
- SSE-S3暗号化
  - SSE-S3はサポートされている唯一のサーバーサイド暗号化方式です。Amazon KMSの暗号化はサポートされていません。

バケットを作成したリージョンをメモしておいてください。次のステップでは同じリージョンにSQSキューを作成します。

### ステップ2:SQSキューの作成 {#step-2-create-sqs-queue}

作成したバケットにオブジェクトが追加されたときに追跡するSQSキューを作成します。ここでは、デフォルトの設定を使用します。

SQSキューはグローバルに一意でなければなりません（例えば、CDI同期には1つしか使用できず、別のワークスペースで再利用することはできません）。

{% alert important %}
このSQSは、バケットを作成したリージョンと同じリージョンに必ず作成してください。
{% endalert %}

この設定ではARNとSQSのURLを頻繁に使用するため、それらを必ずメモしてください。

![「詳細設定」を選択し、例としてJSONオブジェクトを用いて、キューにアクセスできるユーザーを定義する画面。]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### ステップ3:アクセスポリシーの設定 {#step-3-set-up-access-policy}

アクセスポリシーを設定するには、**詳細オプション**を選択します。

次のステートメントをキューのアクセスポリシーに追加します。`YOUR-BUCKET-NAME-HERE`をバケット名に、`YOUR-SQS-ARN`をSQSキューのARNに、`YOUR-AWS-ACCOUNT-ID`をAWSアカウントIDにそれぞれ置き換えてください。

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

### ステップ4:S3バケットへのイベント通知の追加 {#step-4-add-an-event-notification-to-the-s3-bucket}

1. ステップ1で作成したバケットで、**Properties** > **Event notifications**に移動します。
2. 設定に名前を付けます。オプションで、ファイルのサブセットのみをBrazeで取り込む場合は、対象とするプレフィックスまたはサフィックスを指定します。
3. **Destination**で**SQS queue**を選択し、ステップ2で作成したSQSのARNを指定します。

{% alert note %}
S3バケットのルートフォルダーにファイルをアップロードした後、一部のファイルをバケット内の特定のフォルダーに移動すると、予期しないエラーが発生することがあります。代わりに、イベント通知をプレフィックス内のファイルについてのみ送信するように変更するか、プレフィックス外のファイルをS3バケットに入れないようにするか、またはプレフィックスなしで連携を更新すること（すべてのファイルが取り込まれる）ができます。
{% endalert %}

### ステップ5:IAMポリシーの作成 {#step-5-create-an-iam-policy}

ソースバケットの操作をBrazeに許可するIAMポリシーを作成します。まず、アカウント管理者としてAWS管理コンソールにサインインします。

1. AWSコンソールのIAMセクションに移動し、ナビゲーションバーの**Policies**を選択してから**Create Policy**を選択します。<br><br>![AWSコンソールの「Create policy」ボタン。]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. **JSON**タブを開き、**Policy Document**セクションに以下のコードスニペットを入力します。`YOUR-BUCKET-NAME-HERE`をバケット名に、`YOUR-SQS-ARN-HERE`をSQSキュー名にそれぞれ置き換えてください。

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
3. 入力が終わったら、**Review Policy**を選択します。

4. ポリシーの名前と説明を指定し、**Create Policy**を選択します。

![「new-policy-name」という名前のポリシーの例。]({% image_buster /assets/img/create_policy_3_name.png %})

![ポリシーの説明フィールド。]({% image_buster /assets/img/create_policy_4_created.png %})

### ステップ6:IAMロールの作成 {#step-6-create-an-iam-role}

AWSでの設定を完了するには、IAMロールを作成し、ステップ5のIAMポリシーをそれにアタッチします。

1. IAMポリシーを作成したコンソールの同じIAMセクションで、**Roles** > **Create Role**に移動します。

![「Create role」ボタン。]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. AWSで、信頼できるエンティティセレクターのタイプとして**Another AWS Account**を選択します。BrazeアカウントIDを入力します。**Require external ID**チェックボックスを選択します。
3. Brazeで、**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択して、ファイルソースセクションから**Amazon S3**を選択します。
4. 自動生成された**BrazeアカウントID**をコピーします。

![ソース名とS3接続詳細セクションが表示された「新しいソースの追加」ページ。]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. AWSで、アカウントIDを貼り付けてから**Next**を選択します。

![S3の「Create Role」ページ。このページには、ロール名、ロールの説明、信頼できるエンティティ、ポリシー、および権限境界のフィールドがあります。]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. ステップ4で作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横のチェックマークを選択してアタッチします。完了したら**Next**を選択します。

![新しいポリシー名が選択されたロールARN。]({% image_buster /assets/img/create_role_3_attach.png %})

ロールに名前と説明を指定し、**Create Role**を選択します。

![「new-role-name」という名前のロールの例。]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. 作成したロールのARNと生成したExternal IDをメモしておいてください。クラウドデータ取り込みの連携を作成する際に必要になります。

## Brazeでのクラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion-in-braze}

1. まず、Brazeダッシュボードで新しいソースを作成します。**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択して、**Amazon S3**を選択します。
2. ソースの名前を選択し、AWSの設定プロセスからの情報を入力して新しいソースを作成します。次の項目を指定します。

  - ロールのARN
  - External ID
  - バケット名
  - リージョン

![認証情報（AWS設定とBraze設定）および設定フィールドが表示されたS3接続詳細セクション。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. **Test connection**を選択して、Brazeがバケットにアクセスできることを確認します。テストが成功したら、**Connect to Source**を選択します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{: start="4"}
4. 次に、新しい同期を作成します。**データ設定** > **クラウドデータ取り込み** > **同期**に移動し、**データ同期を作成**を選択します。

{: start="5"}
5. 同期の名前を選択します。次に、アクティブなS3ソースを選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection**を選択します。

![データプレビューで接続をテストするオプション。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. AWSの設定プロセスからの残りの情報を入力します。次の項目を指定します。
- SQS URL（新しい連携ごとに一意である必要があります）
- フォルダーパス（オプション、ワークスペース内の同期間で一意である必要があります）

7. データタイプを選択し、**Test Connection**を選択して、Brazeが取り込み可能なファイル（ファイル内のデータではなく）を一覧表示できることを確認します。成功したら、**Next: Notifications**を選択します。
8. アクセスや権限の問題で同期が中断した場合に通知を受け取る連絡先メールアドレスを追加します。オプションで、ユーザーレベルのエラーと同期の成功の通知をオンにします。
9. 同期を作成します。

{% endtab %}
{% tab Google Cloud Storage %}

連携には次のリソースが必要です。

- データストレージ用のCloud Storageバケット
- 新規ファイル通知用のPub/Subトピックとサブスクリプション
- JSONキーをBrazeにアップロードするサービスアカウント

### GCPの定義 {#gcp-definitions}

| 用語 | 定義 |
| --- | --- |
| Google Cloudプロジェクト | プロジェクトは、すべてのGoogle Cloudリソースを整理するもので、一意のプロジェクトIDとプロジェクト番号で識別されます。 |
| Cloud Storageバケット | バケットは、Brazeに取り込ませたいデータファイルを保持するコンテナです。 |
| Pub/Subトピック | トピックは、Cloud Storageバケットから新規ファイル通知を受け取る名前付きリソースです。 |
| Pub/Subサブスクリプション | サブスクリプションはトピックにアタッチされ、そのメッセージを配信します。Brazeはプルサブスクリプションから新規ファイル通知を消費します。 |
| サービスアカウント | サービスアカウントは、Brazeがバケットとサブスクリプションにアクセスするために使用する非人間IDです。そのJSONキーをBrazeにアップロードします。 |
| IAMロール | Identity and Access Management（IAM）ロールは、バケットとサブスクリプションに対してサービスアカウントに付与する権限のコレクションです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="GCPの定義" }

## Google Cloudでのクラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion-in-google-cloud}

### ステップ1:Cloud Storageバケットの作成 {#step-1-create-a-cloud-storage-bucket}

Google Cloudコンソールで、**Cloud Storage** > **Buckets** > **Create**に移動します。プロジェクトIDとバケット名をメモしておいてください。Brazeでソースを設定する際に必要になります。権限をIAMで管理できるように、均一なバケットレベルアクセスを有効にすることをお勧めします。

または、gcloudでバケットを作成します。

```shell
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=YOUR-REGION \
  --uniform-bucket-level-access
```

### ステップ2:Pub/Subトピックとサブスクリプションの作成 {#step-2-create-a-pubsub-topic-and-subscription}

Google Cloudコンソールで、**Pub/Sub** > **Topics** > **Create topic**に移動します。Googleにデフォルトのサブスクリプションを作成させるか、別途作成できます。次に、そのトピックに**プル**サブスクリプションを作成します。

または、gcloudを使用します。

```shell
gcloud pubsub topics create YOUR-TOPIC --project=YOUR-PROJECT-ID
gcloud pubsub subscriptions create YOUR-SUBSCRIPTION \
  --topic=YOUR-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
```

**サブスクリプションID**をメモしておいてください。Brazeで同期を作成する際に必要なのはサブスクリプション（トピックではなく）です。サブスクリプションはプルサブスクリプションである必要があります。

### ステップ3:バケット通知をトピックに送信する {#step-3-send-bucket-notifications-to-the-topic}

{% alert important %}
Cloud StorageからPub/Subへの通知の作成は、Google Cloudコンソールでは利用できません。gcloud（ここに示す方法）、Terraform、またはJSON APIを使用する必要があります。詳細については、Google Cloudドキュメントの[Cloud StorageのPub/Sub通知を設定する](https://cloud.google.com/storage/docs/reporting-changes#enabling)を参照してください。
{% endalert %}

まず、Cloud Storageサービスエージェントにトピックへの発行権限を付与し、次に`OBJECT_FINALIZE`の通知を作成します。`OBJECT_FINALIZE`イベントは、バケットに新しいオブジェクトが作成またはファイナライズされるたびに発火します。

```shell
# Get the Cloud Storage service agent for your project
gcloud storage service-agent --project=YOUR-PROJECT-ID

# Grant it Pub/Sub Publisher on the topic
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

これらのコマンドで以下のプレースホルダーを置き換えてください。

- `YOUR-PROJECT-ID`:Google CloudプロジェクトID。人間が読める識別子です（例:`my-gcp-project`）。
- `YOUR-TOPIC`:[ステップ2](#step-2-create-a-pubsub-topic-and-subscription)で作成したPub/Subトピック。
- `YOUR-BUCKET-NAME`:Cloud Storageバケット名。
- `YOUR-PROJECT-NUMBER`:プロジェクト番号。Cloud Storageサービスエージェントのメールアドレスに使用される数値識別子です。プロジェクトIDとは異なります。Google Cloudコンソールの**ダッシュボード**で確認するか、次のコマンドを実行してください。

```shell
gcloud projects describe YOUR-PROJECT-ID --format="value(projectNumber)"
```

### ステップ4:サービスアカウントの作成 {#step-4-create-a-service-account}

Google Cloudコンソールで、**IAM & Admin** > **Service Accounts** > **Create service account**に移動します。

または、gcloudを使用します。

```shell
gcloud iam service-accounts create braze-cdi-gcs \
  --project=YOUR-PROJECT-ID \
  --display-name="Braze CDI GCS"
```

### ステップ5:権限の付与 {#step-5-grant-permissions}

コネクターには、バケットに対する`storage.buckets.get`、`storage.objects.get`、`storage.objects.list`と、サブスクリプションに対する`pubsub.subscriptions.consume`の権限が正確に必要です。カスタムロールまたは事前定義ロールのいずれかで付与できます。

**カスタムロール:** これらの権限を正確に持つカスタムロールを作成し、バケットとサブスクリプションにバインドします。

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

**事前定義ロール:** バケットに`roles/storage.objectViewer`と`roles/storage.legacyBucketReader`を、サブスクリプションに`roles/pubsub.subscriber`を付与します。`objectViewer`ロールは`storage.objects.get`と`storage.objects.list`を提供し、`legacyBucketReader`は`storage.buckets.get`を提供します。

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

### ステップ6:JSONキーの作成 {#step-6-create-a-json-key}

Google Cloudコンソールで、サービスアカウントを開き、**Keys** > **Add key** > **Create new key**に移動して、**JSON**を選択します。

または、gcloudを使用します。

```shell
gcloud iam service-accounts keys create braze-cdi-gcs-key.json \
  --iam-account=braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com
```

## Brazeでのクラウドデータ取り込みの設定

1. Brazeで、**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択して、**Google Cloud Storage**を選択します。

![データソースの一覧からGoogle Cloud Storageが選択された「新しいソースの追加」画面。]({% image_buster /assets/img/cloud_ingestion/gcs_source_picker.png %})

{: start="2"}
2. ソースのフィールドを入力します。
    - **Bucket** — バケット名
    - **Project ID** — GCPプロジェクトID
    - **Service account JSON key** — ステップ6のキーファイルをアップロードし、認証情報に名前を付けます

![バケット、プロジェクトID、認証情報アップロードフィールドが表示されたGoogle Cloud Storageソースフォーム。]({% image_buster /assets/img/cloud_ingestion/gcs_source_form.png %})

{: start="3"}
3. **Test connection**を選択し、次に**Connect to Source**を選択します。
4. 同期を作成します。**データ設定** > **クラウドデータ取り込み** > **同期**に移動し、**データ同期を作成**を選択します。同期名と**データタイプ**（**User Attributes**、**Custom Events**、**Purchase Events**、**Catalog**、**Delete Users**など）を選択し、**Next**を選択します。
5. **Data definition**ステップで、GCSソースを選択し、次の項目を指定します。
    - **Pub/Sub subscription ID** — ステップ2のサブスクリプションID（トピックではなく）
    - **Folder path**（オプション）— バケット内のパスプレフィックス（[共有バケット内のフォルダーの同期](#syncing-a-folder-in-a-shared-bucket)を参照）

![Pub/SubサブスクリプションIDとフォルダーパスフィールドが表示されたGoogle Cloud Storage同期フォーム。]({% image_buster /assets/img/cloud_ingestion/gcs_sync_form.png %})

{: start="6"}
6. **Preview and validate**を選択して、Brazeがサブスクリプションに到達し、取り込み可能なファイルを一覧表示できることを確認します。テストが成功すると、バケット内の既存ファイルが一覧表示されますが、それらのファイルは自動的に同期されません。
7. エラー通知用の連絡先メールアドレスを追加します。Google Cloud Storageの同期はイベント駆動型のため、スケジュールは不要です。Brazeは新規ファイルがアップロードされると取り込みます。サマリーを確認し、**Create sync**を選択します。

### 共有バケット内のフォルダーの同期 {#syncing-a-folder-in-a-shared-bucket}

1つのバケットを複数の同期で再利用できますが、各同期は異なるフォルダーをターゲットにし、**かつ**専用のPub/Subサブスクリプションを持つ必要があります。


{% alert important %}
同じソースバケットを共有する複数の同期では、フォルダーパスとサブスクリプションの両方がワークスペース内の同期間で一意である必要があります。
{% endalert %}

共有バケット内で同期したいフォルダーごとに、以下を行います。

1. 同期の**Folder**フィールドにパスプレフィックスを設定します（例:`attributes/`）。Brazeはそのプレフィックスで始まるパスのオブジェクトのみを一覧表示し、取り込みます。
2. そのフォルダー用に専用のトピックとプレフィックススコープの通知を作成し、次にそのトピックにサブスクリプションを作成します。

    ```shell
    # フォルダーごとに1つのトピック
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Cloud StorageサービスエージェントにトピックへのPublisherを付与
    gcloud pubsub topics add-iam-policy-binding YOUR-ATTRIBUTES-TOPIC \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
      --role="roles/pubsub.publisher"

    # --object-prefixでフォルダーにスコープを限定した通知
    gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
      --topic=YOUR-ATTRIBUTES-TOPIC --event-types=OBJECT_FINALIZE \
      --payload-format=json --object-prefix=attributes/

    # 同期ごとに1つのサブスクリプション
    gcloud pubsub subscriptions create YOUR-ATTRIBUTES-SUBSCRIPTION \
      --topic=YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
    ```

3. [ステップ5](#step-5-grant-permissions)と同様に、Brazeサービスアカウントにそのサブスクリプションのconsume権限を付与します。

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    [ステップ5](#step-5-grant-permissions)でカスタムロールを作成した場合は、代わりに`--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"`を使用してください。
4. Brazeで同期を作成する際に、このフォルダーの新しい**Pub/Sub subscription ID**と**Folder path**を入力して、そのフォルダーのファイルのみを取り込むようにします。


{% endtab %}
{% endtabs %}

## 必要なファイル形式 {#required-file-formats}

必要なファイル形式はAmazon S3とGoogle Cloud Storageで共通です。クラウドデータ取り込みは、JSON、CSV、およびParquetのファイルをサポートしています。必要な列はデータタイプによって異なります。

- ユーザーデータ（属性、カスタムイベント、購入イベント）はユーザー識別子とペイロードを使用します
- カタログデータはカタログ識別子を使用します

ファイルストレージをカタログデータに使用している場合は、このページと[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を併せて参照し、カタログ固有の要件と動作を確認してください。

Brazeは、ファイルストレージプロバイダーによって強制される以上の追加のファイル名要件を強制しません。ファイル名は一意でなければなりません。一意性を確保するためにタイムスタンプを付加することを推奨します。

サポートされているすべてのファイルタイプ（属性、カスタムイベント、購入、カタログ、ユーザー削除）の例については、[braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage)のサンプルファイルを参照してください。

### ユーザー識別子 {#user-identifiers}

ユーザーデータの同期（属性、カスタムイベント、購入イベント）では、ソースファイルの各行に正確に1つのユーザー識別子と`PAYLOAD`列が必要です。ソースファイルには異なる識別子タイプの行を含めることができますが、各行では1つの識別子のみを使用する必要があります。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | 更新したいユーザーを識別します。これはBrazeで使用されている`external_id`値と一致する必要があります。 |
| `ALIAS_NAME`と`ALIAS_LABEL` | これら2つの列は、ユーザーエイリアスオブジェクトを作成します。`alias_name`は一意の識別子でなければならず、`alias_label`はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label`ごとに`alias_name`は1つしか持てません。 |
| `BRAZE_ID` | Brazeのユーザー識別子です。これはBraze SDKによって生成されます。クラウドデータ取り込み経由でBraze IDを使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、external IDまたはユーザーエイリアスを指定します。 |
| `EMAIL` | ユーザーのメールアドレスです。同じメールアドレスを持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。メールと電話の両方を含める場合は、Brazeはメールをプライマリ識別子として使用します。 |
| `PHONE` | ユーザーの電話番号です。同じ電話番号を持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー識別子" }

識別子に加えて、各行にはBrazeのユーザーに同期させたいフィールドのJSON文字列を含む`PAYLOAD`列が必要です。

{% alert note %}
データウェアハウスソースとは異なり、`UPDATED_AT`列はファイルストレージ同期では必須ではなく、サポートもされていません。
{% endalert %}

### カタログ識別子 {#catalog-identifiers}

カタログ同期では、ソースファイルに以下の列を含める必要があります。カタログファイルはユーザーデータファイルとは異なる識別子を使用します。

| 列 | 必須 | 説明 |
| --- | --- | --- |
| `ID` | はい | カタログアイテムの一意の識別子です。Brazeでアイテムの作成、更新、または削除に使用されます。 |
| `PAYLOAD` | はい | 同期するカタログフィールドと値のJSON文字列です。Brazeのカタログのスキーマと一致する必要があります。 |
| `DELETED` | いいえ | `true`の場合、一致する`ID`のカタログアイテムがBrazeのカタログから削除されます。作成または更新操作の場合は、この列を省略するか`false`に設定します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カタログ識別子" }

### 例 {#examples}

{% tabs %}
{% tab JSON Attributes %}
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
ソースファイルのすべての行に有効なJSONが含まれている必要があります。含まれていない場合、ファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
ソースファイルのすべての行に有効なJSONが含まれている必要があります。含まれていない場合、ファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
ソースファイルのすべての行に有効なJSONが含まれている必要があります。含まれていない場合、ファイルはスキップされます。
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
オプションの`DELETED`列を含めます。`DELETED`が`true`の場合、そのカタログアイテムはBrazeのカタログから削除されます。必要な列の完全なリストについては、[カタログ識別子](#catalog-identifiers)を参照してください。削除の動作については、[カタログアイテムの削除](#deleting-catalog-items)を参照してください。エンドツーエンドのカタログ設定フロー（ターゲットカタログの作成と同期の動作を含む）については、[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を参照してください。
{% endtab %}

{% endtabs %}

## データの削除 {#deleting-data}

ファイルストレージ向けクラウドデータ取り込みは、ファイルアップロードを通じてユーザーとカタログアイテムの削除をサポートしています。それぞれに別々の同期とファイル形式を使用します。

- **[ユーザーの削除](#deleting-users)** – データタイプ**Delete Users**で同期を作成し、ユーザー識別子のみを含むファイル（ペイロードなし）をアップロードします。
- **[カタログアイテムの削除](#deleting-catalog-items)** – 既存のカタログ同期を使用し、削除対象のアイテムをマークする`deleted`（または`DELETED`）列を追加します。

### ユーザーの削除 {#deleting-users}

ソースバケット内のファイルを使ってBrazeでユーザープロファイルを削除するには：

1. 新しいクラウドデータ取り込み同期を作成します（他の同期と同じ設定を使用します）。
2. Brazeで同期を設定する際、**Data Type**を**Delete Users**に設定します。
3. ソースバケットに、ユーザー識別子列のみを含むファイルをアップロードします。`PAYLOAD`列を含めないでください。ペイロードが存在すると、誤削除を防ぐために同期が失敗します。

ファイルの各行は、次のいずれかを使用して正確に1人のユーザーを識別する必要があります。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | Brazeで使用される`external_id`と一致します。 |
| `ALIAS_NAME`と`ALIAS_LABEL` | 両方の列を合わせて、ユーザーをエイリアスで識別します。 |
| `BRAZE_ID` | Brazeが生成したユーザーID（既存ユーザーのみ）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーの削除" }

{% alert important %}
ユーザーの削除は永続的で元に戻すことはできません。削除する予定のユーザーのみを含めてください。詳細については、[クラウドデータ取り込みを使用したユーザーの削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users)を参照してください。
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

同期が実行されると、Brazeはバケット内の新規ファイルを処理し、対応するユーザープロファイルを削除します。

### カタログアイテムの削除 {#deleting-catalog-items}

ファイルストレージを使用してカタログからアイテムを削除するには：

1. [カタログデータの同期]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)（データタイプ：**Catalogs**）に使用するのと同じ同期を使用します。
2. CSVファイルやJSONファイルに、オプションの**`deleted`**（または**`DELETED`**）列を追加します。
3. Brazeのカタログから削除したいカタログアイテムには、`deleted`を`true`に設定します。

各行にはまだ`ID`と`PAYLOAD`が必要です。削除対象の行については、ペイロードは最小限で構いません。Brazeは`ID`でアイテムを削除します。

**例 – JSON（カタログアイテム削除）：**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**例 – CSV（カタログアイテム削除）：**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

同期が実行されると、`deleted: true`の行に対応するカタログアイテムがBrazeから削除されます。カタログデータの完全な同期と削除の動作については、[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を参照してください。

## 知っておくべきこと {#things-to-know}

- ソースバケットに追加するファイルは512&nbsp;MBを超えてはなりません。この制限はAmazon S3とGoogle Cloud Storageの両方に適用されます。512&nbsp;MBを超えるファイルはエラーになり、Brazeに同期されません。
- 1ファイルあたりの行数に追加の制限はありませんが、同期の速度を向上させるために、小さなファイルを使用することをお勧めします。例えば、500&nbsp;MBのファイルの取り込みは、100&nbsp;MBのファイルを5つに分けて取り込む場合よりもかなり時間がかかります。
- 一定期間内にアップロードできるファイルの数に追加の制限はありません。
- ファイル内やファイル間の順序付けはサポートされていません。競合が予想される状況を監視している場合は、定期的に更新をバッチ処理することをお勧めします。

## トラブルシューティング {#troubleshooting}

### ファイルのアップロードと処理 {#uploading-files-and-processing}

CDIは、同期が作成された後に追加されたファイルのみを処理します。このプロセスでは、Brazeが新しいファイルの追加を検知し、新しい通知がトリガーされます。これにより、新しいファイルを処理するための新しい同期が開始されます。Amazon S3の場合、通知はSQSへのメッセージです。Google Cloud Storageの場合、Pub/Subへの`OBJECT_FINALIZE`メッセージです。

既存のファイルを使って、Brazeがバケットにアクセスでき、取り込むファイルを検出できることを確認できますが、それらのファイルはBrazeに同期されません。CDIがそれらを処理するには、同期したい既存のファイルをソースバケットに再アップロードする必要があります。

### 予期しないファイルエラーの処理（Amazon S3） {#handling-unexpected-file-errors-amazon-s3}

エラーや失敗ファイルが多い場合は、CDIのターゲットフォルダー以外のフォルダーにあるS3バケットに、別のプロセスがファイルを追加している可能性があります。

ファイルがソースバケットにアップロードされたがソースフォルダーには含まれていない場合、CDIはSQS通知を処理しますが、ファイルに対してアクションを実行しないため、エラーとして表示されることがあります。

問題がS3通知やSQS送信先の権限に関連している場合（例えば、送信先の検証エラー）は、AWSのドキュメントを参照してください。

- [Amazon S3コンソールを使用したイベント通知の有効化と設定](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [送信先へのイベント通知メッセージの発行権限の付与](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Amazon SQSの問題のトラブルシューティング](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### 予期しないファイルエラーの処理（Google Cloud Storage） {#handling-unexpected-file-errors-google-cloud-storage}

Amazon S3と同様に、CDIは同期が作成された後にアップロードされたファイルのみを処理します。新しいオブジェクトごとにPub/Subトピックへの`OBJECT_FINALIZE`メッセージがトリガーされます。バケットに既に存在するファイルを取り込むには、再アップロードしてください。

ファイルが取り込まれない場合は、以下を確認してください。

- バケット通知が存在すること。`gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME`でバケットの通知を一覧表示できます。
- Cloud Storageサービスエージェントがトピックに対して`roles/pubsub.publisher`を持っていること。
- Brazeサービスアカウントがサブスクリプションに対するconsume権限（`pubsub.subscriptions.consume`、カスタムロールまたは`roles/pubsub.subscriber`で付与）を持っていること。

詳細については、Google Cloudドキュメントの[Cloud StorageのPub/Sub通知](https://cloud.google.com/storage/docs/pubsub-notifications)を参照してください。