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

Cloud Data Ingestion (CDI) を使用して、クラウドアカウント内の1つ以上のストレージバケットをBrazeと直接統合できます。バケットに新しいファイルが追加されると、クラウドプロバイダーが通知を発行し、Braze Cloud Data Ingestionがデータを同期します。

通知メカニズムはプロバイダーによって異なります。

- **Amazon S3:** 新しいファイルがS3に公開されると、Amazon Simple Queue Service (SQS) キューにメッセージが投稿され、Brazeがそのメッセージを消費して新しいファイルを取り込みます。
- **Google Cloud Storage (GCS):** バケット内で新しいファイルがファイナライズされると、GCSがPub/Subトピックに`OBJECT_FINALIZE`通知を発行します。BrazeはPub/Subサブスクリプションからこれらの通知を消費して新しいファイルを取り込みます。

Cloud Data Ingestionは以下をサポートしています。

- JSONファイル
- CSVファイル
- Parquetファイル
- 属性、カスタムイベント、購入イベント、ユーザー削除、およびカタログデータ

## クラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion}

設定手順はファイルストレージプロバイダーによって異なります。お使いのプロバイダーのタブを選択し、その後に続く共通設定セクションを完了してください。

{% tabs %}
{% tab Amazon S3 %}

この連携には以下のリソースが必要です。

- データストレージ用の S3 バケット
- 新しいファイル通知用の SQS キュー
- Braze アクセス用の IAM ロール

### AWS の定義 {#aws-definitions}

| 用語 | 定義 |
| --- | --- |
| Amazon リソースネーム (ARN) | ARN は AWS リソースの一意の識別子です。 |
| Identity and Access Management (IAM) | IAM は、AWS リソースへのアクセスを安全に制御できる Web サービスです。このチュートリアルでは、IAM ポリシーを作成し、それを IAM ロールに割り当てて、S3 バケットを Braze クラウドデータ取り込みと連携させます。 |
| Amazon Simple Queue Service (SQS) | SQS は、分散ソフトウェアシステムやコンポーネントを統合できるホスト型キューです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="AWSの定義" }

## AWS でのクラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion-in-aws}

### ステップ 1: ソースバケットの作成 {#step-1-create-a-source-bucket}

AWS アカウントでデフォルト設定の汎用 S3 バケットを作成します。S3 バケットは、フォルダーが一意である限り、同期間で再利用できます。

デフォルト設定は次のとおりです。

- ACL 無効
- すべてのパブリックアクセスをブロック
- バケットのバージョン管理を無効化
- SSE-S3 暗号化
  - SSE-S3 はサポートされている唯一のサーバーサイド暗号化方式です。Amazon KMS の暗号化はサポートされていません。

バケットを作成したリージョンをメモしておいてください。次のステップでは同じリージョンに SQS キューを作成します。

### ステップ 2: SQS キューの作成 {#step-2-create-sqs-queue}

作成したバケットにオブジェクトが追加されたときに追跡する SQS キューを作成します。ここでは、デフォルトの設定を使用します。

SQS キューはグローバルに一意でなければなりません（例えば、CDI 同期には1つしか使用できず、別のワークスペースで再利用することはできません）。

{% alert important %}
この SQS は、バケットを作成したリージョンと同じリージョンに必ず作成してください。
{% endalert %}

この設定では ARN と SQS の URL を頻繁に使用するため、それらを必ずメモしてください。

![「詳細設定」を選択し、例として JSON オブジェクトを用いて、キューにアクセスできるユーザーを定義する画面。]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### ステップ 3: アクセスポリシーの設定 {#step-3-set-up-access-policy}

アクセスポリシーを設定するには、**詳細オプション**を選択します。

次のステートメントをキューのアクセスポリシーに追加します。`YOUR-BUCKET-NAME-HERE` をバケット名に、`YOUR-SQS-ARN` を SQS キューの ARN に、`YOUR-AWS-ACCOUNT-ID` を AWS アカウント ID にそれぞれ置き換えてください。

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

### ステップ 4: S3 バケットへのイベント通知の追加 {#step-4-add-an-event-notification-to-the-s3-bucket}

1. ステップ 1 で作成したバケットで、**Properties** > **Event notifications** に移動します。
2. 設定に名前を付けます。オプションで、ファイルのサブセットのみを Braze で取り込む場合は、対象とするプレフィックスまたはサフィックスを指定します。
3. **Destination** で **SQS queue** を選択し、ステップ 2 で作成した SQS の ARN を指定します。

{% alert note %}
S3 バケットのルートフォルダーにファイルをアップロードした後、一部のファイルをバケット内の特定のフォルダーに移動すると、予期しないエラーが発生することがあります。代わりに、イベント通知をプレフィックス内のファイルについてのみ送信するように変更するか、プレフィックス外のファイルを S3 バケットに入れないようにするか、またはプレフィックスなしで連携を更新すること（すべてのファイルが取り込まれる）ができます。
{% endalert %}

### ステップ 5: IAM ポリシーの作成 {#step-5-create-an-iam-policy}

ソースバケットの操作を Braze に許可する IAM ポリシーを作成します。まず、アカウント管理者として AWS 管理コンソールにサインインします。

1. AWS コンソールの [IAM] セクションに移動し、ナビゲーションバーの **Policies** を選択してから **Create Policy** を選択します。<br><br>![AWS コンソールの「Create policy」ボタン。]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. **JSON** タブを開き、**Policy Document** セクションに以下のコードスニペットを入力します。`YOUR-BUCKET-NAME-HERE` をバケット名に、`YOUR-SQS-ARN-HERE` を SQS キュー名にそれぞれ置き換えてください。

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
3. 入力が終わったら、**Review Policy** を選択します。

4. ポリシーの名前と説明を指定し、**Create Policy** を選択します。

![「new-policy-name」という名前のポリシーの例。]({% image_buster /assets/img/create_policy_3_name.png %})

![ポリシーの説明フィールド。]({% image_buster /assets/img/create_policy_4_created.png %})

### ステップ 6: IAM ロールの作成 {#step-6-create-an-iam-role}

AWS での設定を完了するには、IAM ロールを作成し、ステップ 5 の IAM ポリシーをそれにアタッチします。

1. IAM ポリシーを作成したコンソールの同じ [IAM] セクションで、**Roles** > **Create Role** に移動します。

![「Create role」ボタン。]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. AWS で、信頼できるエンティティセレクターのタイプとして **Another AWS Account** を選択します。Braze アカウント ID を入力します。**Require external ID** チェックボックスを選択します。
3. Braze で、**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択して、ファイルソースセクションから **Amazon S3** を選択します。
4. 自動生成された **Braze アカウント ID** をコピーします。

![ソース名と S3 接続詳細セクションが表示された「新しいソースの追加」ページ。]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. AWS で、アカウント ID を貼り付けてから **Next** を選択します。

![S3 の「Create Role」ページ。このページには、ロール名、ロールの説明、信頼できるエンティティ、ポリシー、および権限境界のフィールドがあります。]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. ステップ 4 で作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横のチェックマークを選択してアタッチします。完了したら **Next** を選択します。

![新しいポリシー名が選択されたロール ARN。]({% image_buster /assets/img/create_role_3_attach.png %})

ロールに名前と説明を指定し、**Create Role** を選択します。

![「new-role-name」という名前のロールの例。]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. 作成したロールの ARN と生成した External ID をメモしておいてください。クラウドデータ取り込みの連携を作成する際に必要になります。

## Braze でのクラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion-in-braze}

1. まず、Braze ダッシュボードで新しいソースを作成します。**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択してから **Amazon S3** を選択します。
2. ソースの名前を選択し、AWS の設定プロセスで取得した情報を入力して新しいソースを作成します。以下を指定してください。

  - ロール ARN
  - External ID
  - バケット名
  - リージョン

![認証情報（AWS 設定と Braze 設定）および設定フィールドが表示された S3 接続詳細セクション。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. **接続テスト**を選択して、Braze がバケットにアクセスできることを確認します。テストが成功したら、**ソースに接続**を選択します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{: start="4"}
4. 次に、新しい同期を作成します。**データ設定** > **クラウドデータ取り込み** > **同期**に移動し、**データ同期を作成**を選択します。

{: start="5"}
5. 同期の名前を選択します。次に、アクティブな S3 ソースを選択し、同期のソーステーブルを入力します。データタイプを選択し、**接続テスト**を選択します。

![データプレビュー付きの接続テストオプション。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. AWS の設定プロセスで取得した残りの情報を入力します。以下を指定してください。
- SQS URL（新しい連携ごとに一意である必要があります）
- フォルダーパス（オプション、ワークスペース内の同期間で一意である必要があります）

7. データタイプを選択し、**接続テスト**を選択して、Braze が取り込み可能なファイルの一覧を取得できることを確認します（ファイル内のデータではありません）。成功したら、**次へ: 通知**を選択します。
8. アクセスや権限の問題で同期が中断された場合の通知用に、連絡先メールアドレスを追加します。オプションで、ユーザーレベルのエラーや同期成功の通知を有効にできます。
9. 同期を作成します。

{% endtab %}
{% tab Google Cloud Storage %}

この連携には以下のリソースが必要です。

- データストレージ用の Cloud Storage バケット
- 新しいファイル通知用の Pub/Sub トピックとサブスクリプション
- JSON キーを Braze にアップロードするサービスアカウント

### GCP の定義 {#gcp-definitions}

| 用語 | 定義 |
| --- | --- |
| Google Cloud プロジェクト | プロジェクトは、すべての Google Cloud リソースを整理するもので、一意のプロジェクト ID とプロジェクト番号で識別されます。 |
| Cloud Storage バケット | バケットは、Braze に取り込ませたいデータファイルを保持するコンテナです。 |
| Pub/Sub トピック | トピックは、Cloud Storage バケットから新しいファイル通知を受信する名前付きリソースです。 |
| Pub/Sub サブスクリプション | サブスクリプションはトピックにアタッチされ、そのメッセージを配信します。Braze はプルサブスクリプションから新しいファイル通知を取得します。 |
| サービスアカウント | サービスアカウントは、Braze がバケットとサブスクリプションにアクセスするために使用する非人間 ID です。その JSON キーを Braze にアップロードします。 |
| IAM ロール | Identity and Access Management (IAM) ロールは、バケットとサブスクリプションに対してサービスアカウントに付与する権限のコレクションです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="GCPの定義" }

## Google Cloud でのクラウドデータ取り込みの設定 {#setting-up-cloud-data-ingestion-in-google-cloud}

### ステップ 1: Cloud Storage バケットの作成 {#step-1-create-a-cloud-storage-bucket}

Google Cloud コンソールで、**Cloud Storage** > **Buckets** > **Create** に移動します。プロジェクト ID とバケット名をメモしておいてください。Braze でソースを設定する際に必要になります。IAM で権限を管理できるように、均一なバケットレベルアクセスを有効にすることをお勧めします。

または、gcloud でバケットを作成することもできます。

```shell
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=YOUR-REGION \
  --uniform-bucket-level-access
```

### ステップ 2: Pub/Sub トピックとサブスクリプションの作成 {#step-2-create-a-pubsub-topic-and-subscription}

Google Cloud コンソールで、**Pub/Sub** > **Topics** > **Create topic** に移動します。Google にデフォルトのサブスクリプションを作成させるか、別途作成できます。次に、そのトピックに**プル**サブスクリプションを作成します。

または、gcloud を使用します。

```shell
gcloud pubsub topics create YOUR-TOPIC --project=YOUR-PROJECT-ID
gcloud pubsub subscriptions create YOUR-SUBSCRIPTION \
  --topic=YOUR-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
```

**サブスクリプション ID** をメモしておいてください。同期を作成する際、Braze にはサブスクリプション（トピックではなく）が必要です。サブスクリプションはプルサブスクリプションである必要があります。

### ステップ 3: バケット通知をトピックに送信する {#step-3-send-bucket-notifications-to-the-topic}

{% alert important %}
Cloud Storage から Pub/Sub への通知の作成は、Google Cloud コンソールでは利用できません。gcloud（ここに示す方法）、Terraform、または JSON API を使用する必要があります。詳しくは、Google Cloud ドキュメントの [Cloud Storage の Pub/Sub 通知を設定する](https://cloud.google.com/storage/docs/reporting-changes#enabling)を参照してください。
{% endalert %}

まず、Cloud Storage サービスエージェントにトピックへの公開権限を付与し、次に `OBJECT_FINALIZE` の通知を作成します。`OBJECT_FINALIZE` イベントは、バケット内で新しいオブジェクトが作成またはファイナライズされるたびに発生します。

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

- `YOUR-PROJECT-ID`: Google Cloud プロジェクト ID。人間が読める識別子です（例: `my-gcp-project`）。
- `YOUR-TOPIC`: [ステップ 2](#step-2-create-a-pubsub-topic-and-subscription) で作成した Pub/Sub トピック。
- `YOUR-BUCKET-NAME`: Cloud Storage バケット名。
- `YOUR-PROJECT-NUMBER`: プロジェクト番号。Cloud Storage サービスエージェントのメールアドレスに使用される数値識別子です。プロジェクト ID とは異なります。Google Cloud コンソールの**ダッシュボード**で確認するか、以下のコマンドを実行してください。

```shell
gcloud projects describe YOUR-PROJECT-ID --format="value(projectNumber)"
```

### ステップ 4: サービスアカウントの作成 {#step-4-create-a-service-account}

Google Cloud コンソールで、**IAM & Admin** > **Service Accounts** > **Create service account** に移動します。

または、gcloud を使用します。

```shell
gcloud iam service-accounts create braze-cdi-gcs \
  --project=YOUR-PROJECT-ID \
  --display-name="Braze CDI GCS"
```

### ステップ 5: 権限の付与 {#step-5-grant-permissions}

コネクターには、バケットに対する `storage.buckets.get`、`storage.objects.get`、`storage.objects.list` の権限と、サブスクリプションに対する `pubsub.subscriptions.consume` の権限が正確に必要です。カスタムロールまたは事前定義ロールのいずれかで付与できます。

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

**事前定義ロール:** バケットに `roles/storage.objectViewer` と `roles/storage.legacyBucketReader` を、サブスクリプションに `roles/pubsub.subscriber` を付与します。`objectViewer` ロールは `storage.objects.get` と `storage.objects.list` を提供し、`legacyBucketReader` は `storage.buckets.get` を提供します。

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

### ステップ 6: JSON キーの作成 {#step-6-create-a-json-key}

Google Cloud コンソールで、サービスアカウントを開き、**Keys** > **Add key** > **Create new key** に移動して、**JSON** を選択します。

または、gcloud を使用します。

```shell
gcloud iam service-accounts keys create braze-cdi-gcs-key.json \
  --iam-account=braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com
```

## Braze でのクラウドデータ取り込みの設定

1. Braze で、**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択してから **Google Cloud Storage** を選択します。

![データソースの一覧から Google Cloud Storage が選択された「新しいソースの追加」画面。]({% image_buster /assets/img/cloud_ingestion/gcs_source_picker.png %})

{: start="2"}
2. ソースのフィールドを入力します。
    - **Bucket** — バケット名
    - **Project ID** — GCP プロジェクト ID
    - **Service account JSON key** — ステップ 6 のキーファイルをアップロードし、認証情報に名前を付けます

![バケット、プロジェクト ID、認証情報アップロードフィールドが表示された Google Cloud Storage ソースフォーム。]({% image_buster /assets/img/cloud_ingestion/gcs_source_form.png %})

{: start="3"}
3. **接続テスト**を選択してから、**ソースに接続**を選択します。
4. 同期を作成します。**データ設定** > **クラウドデータ取り込み** > **同期**に移動し、**データ同期を作成**を選択します。同期名と**データタイプ**（**ユーザー属性**、**カスタムイベント**、**購入イベント**、**カタログ**、**ユーザーの削除**など）を選択してから、**次へ**を選択します。
5. **データ定義**ステップで、GCS ソースを選択し、以下を指定します。
    - **Pub/Sub サブスクリプション ID** — ステップ 2 のサブスクリプション ID（トピックではありません）
    - **フォルダーパス**（オプション）— バケット内のパスプレフィックス（[共有バケット内のフォルダーの同期](#syncing-a-folder-in-a-shared-bucket)を参照）

![Pub/Sub サブスクリプション ID とフォルダーパスフィールドが表示された Google Cloud Storage 同期フォーム。]({% image_buster /assets/img/cloud_ingestion/gcs_sync_form.png %})

{: start="6"}
6. **プレビューと検証**を選択して、Braze がサブスクリプションに到達し、取り込み可能なファイルの一覧を取得できることを確認します。テストが成功すると、バケット内の既存ファイルが一覧表示されますが、それらのファイルは自動的に同期されません。
7. エラー通知用の連絡先メールアドレスを追加します。Google Cloud Storage の同期はイベント駆動型のため、スケジュールは不要です。Braze は新しいファイルがアップロードされると自動的に取り込みます。サマリーを確認してから、**同期を作成**を選択します。

### 共有バケット内のフォルダーの同期 {#syncing-a-folder-in-a-shared-bucket}

1つのバケットを複数の同期で再利用できますが、各同期は異なるフォルダーをターゲットにし、**かつ**専用の Pub/Sub サブスクリプションを持つ必要があります。


{% alert important %}
同じソースバケットを共有する複数の同期では、フォルダーパスとサブスクリプションの両方がワークスペース内の同期間で一意である必要があります。
{% endalert %}

共有バケット内で同期したいフォルダーごとに、以下を行います。

1. 同期の**フォルダー**フィールドにパスプレフィックスを設定します（例: `attributes/`）。Braze はそのプレフィックスで始まるパスのオブジェクトのみを一覧表示し、取り込みます。
2. そのフォルダー用に専用のトピックとプレフィックスにスコープされた通知を作成し、次にそのトピックにサブスクリプションを作成します。

    ```shell
    # フォルダーごとに1つのトピック
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Cloud Storage サービスエージェントにトピックへの publisher 権限を付与する
    gcloud pubsub topics add-iam-policy-binding YOUR-ATTRIBUTES-TOPIC \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
      --role="roles/pubsub.publisher"

    # --object-prefix でフォルダーにスコープされた通知
    gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
      --topic=YOUR-ATTRIBUTES-TOPIC --event-types=OBJECT_FINALIZE \
      --payload-format=json --object-prefix=attributes/

    # 同期ごとに1つのサブスクリプション
    gcloud pubsub subscriptions create YOUR-ATTRIBUTES-SUBSCRIPTION \
      --topic=YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
    ```

3. [ステップ 5](#step-5-grant-permissions) と同様に、Braze サービスアカウントにそのサブスクリプションの consume 権限を付与します。

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    [ステップ 5](#step-5-grant-permissions) でカスタムロールを作成した場合は、代わりに `--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"` を使用してください。
4. Braze で同期を作成する際に、このフォルダーの新しい **Pub/Sub サブスクリプション ID** と**フォルダーパス**を入力して、そのフォルダーのファイルのみを取り込むようにします。


{% endtab %}
{% endtabs %}

## 必須ファイル形式 {#required-file-formats}

必須ファイル形式は Amazon S3 と Google Cloud Storage で共通です。クラウドデータ取り込みは JSON、CSV、Parquet ファイルをサポートしています。必須カラムはデータタイプによって異なります。

- ユーザーデータ（属性、カスタムイベント、購入イベント）はユーザー識別子とペイロードを使用します
- カタログデータはカタログ識別子を使用します

ファイルストレージをカタログデータに使用する場合は、このページと[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を併せて参照し、カタログ固有の要件と動作を確認してください。

Braze はファイルストレージプロバイダーが適用する制約以外に、追加のファイル名要件を設けていません。ファイル名は一意である必要があります。タイムスタンプを付加すると一意性を確保しやすくなります。

サポートされているすべてのファイルタイプ（属性、カスタムイベント、購入、カタログ、ユーザー削除）の例については、[braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage) のサンプルファイルを参照してください。

### ユーザー識別子 {#user-identifiers}

ユーザーデータの同期（属性、カスタムイベント、購入イベント）では、ソースファイルの各行にユーザー識別子が1つと `PAYLOAD` カラムが必要です。ソースファイルには異なる識別子タイプの行を含めることができますが、各行で使用する識別子は1つだけにしてください。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | 更新対象のユーザーを識別します。Brazeで使用される `external_id` の値と一致する必要があります。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | この2つのカラムでユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子で、`alias_label` はエイリアスの種類を指定します。ユーザーは異なるラベルで複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つだけです。 |
| `BRAZE_ID` | Brazeユーザー識別子です。Braze SDKによって生成され、クラウドデータ取り込みを通じてBraze IDで新規ユーザーを作成することはできません。新規ユーザーを作成するには、external IDまたはユーザーエイリアスを指定してください。 |
| `EMAIL` | ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最後に更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、Brazeはメールを主要な識別子として使用します。 |
| `PHONE` | ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最後に更新されたプロファイルが優先されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー識別子" }

識別子に加えて、各行にはBrazeのユーザーに同期するフィールドのJSON文字列を含む `PAYLOAD` カラムが必要です。

{% alert note %}
データウェアハウスソースとは異なり、`UPDATED_AT` カラムはファイルストレージ同期では不要であり、サポートもされていません。
{% endalert %}

### カタログ識別子 {#catalog-identifiers}

カタログ同期では、ソースファイルに以下のカラムが必要です。カタログファイルはユーザーデータファイルとは異なる識別子を使用します。

| カラム | 必須 | 説明 |
| --- | --- | --- |
| `ID` | はい | カタログアイテムの一意の識別子です。Brazeでアイテムの作成、更新、削除に使用されます。 |
| `PAYLOAD` | はい | 同期するカタログフィールドと値のJSON文字列です。Brazeのカタログスキーマと一致する必要があります。 |
| `DELETED` | いいえ | `true` の場合、一致する `ID` のカタログアイテムがBrazeのカタログから削除されます。作成または更新操作の場合は、このカラムを省略するか `false` に設定してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カタログ識別子" }

### 例 {#examples}

{% tabs %}
{% tab JSON属性 %}
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
ソースファイルの各行には有効なJSONが含まれている必要があります。含まれていない場合、そのファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSONカスタムイベント %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
ソースファイルの各行には有効なJSONが含まれている必要があります。含まれていない場合、そのファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSON購入イベント %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
ソースファイルの各行には有効なJSONが含まれている必要があります。含まれていない場合、そのファイルはスキップされます。
{% endalert %}

{% endtab %}
{% tab CSV属性 %}
```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSVカタログ %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
オプションの `DELETED` カラムを含めることができます。`DELETED` が `true` の場合、そのカタログアイテムはBrazeのカタログから削除されます。必須カラムの一覧については、[カタログ識別子](#catalog-identifiers)を参照してください。削除の動作については、[カタログアイテムの削除](#deleting-catalog-items)を参照してください。エンドツーエンドのカタログ設定フロー（対象カタログの作成と同期動作を含む）については、[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を参照してください。
{% endtab %}

{% endtabs %}

## データの削除 {#deleting-data}

ファイルストレージ向けのCloud Data Ingestionは、ファイルアップロードによるユーザーおよびカタログアイテムの削除をサポートしています。それぞれに個別の同期とファイル形式を使用してください。

- **[ユーザーの削除](#deleting-users)** – データタイプ**Delete Users**で同期を作成し、ユーザー識別子のみを含むファイル（ペイロードなし）をアップロードします。
- **[カタログアイテムの削除](#deleting-catalog-items)** – 既存のカタログ同期を使用し、`deleted`（または`DELETED`）列を追加して削除対象のアイテムをマークします。

### ユーザーの削除 {#deleting-users}

ソースバケット内のファイルを使用してBrazeのユーザープロファイルを削除するには：

1. 新しいCloud Data Ingestion同期を作成します（他の同期と同じ設定です）。
2. Brazeで同期を設定する際、**Data Type**を**Delete Users**に設定します。
3. ユーザー識別子列のみを含むファイルをソースバケットにアップロードします。`PAYLOAD`列は含めないでください。誤った削除を防ぐため、ペイロードが存在すると同期は失敗します。

ファイルの各行は、以下のいずれかを使用して正確に1人のユーザーを識別する必要があります。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | Brazeで使用される`external_id`と一致します。 |
| `ALIAS_NAME`と`ALIAS_LABEL` | 両方の列を組み合わせてエイリアスでユーザーを識別します。 |
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

ファイルストレージを使用してカタログからアイテムを削除するには：

1. [カタログデータを同期する]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)ために使用しているのと同じ同期（データタイプ**Catalogs**）を使用します。
2. CSVまたはJSONファイルに、オプションの**`deleted`**（または**`DELETED`**）列を追加します。
3. Brazeのカタログから削除したいカタログアイテムの`deleted`を`true`に設定します。

各行には引き続き`ID`と`PAYLOAD`が必要です。削除対象としてマークされた行のペイロードは最小限で構いません。Brazeは`ID`でアイテムを削除します。

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

同期が実行されると、`deleted: true`の行に対応するカタログアイテムがBrazeで削除されます。カタログの同期と削除の動作の詳細については、[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を参照してください。

## 知っておくべきこと {#things-to-know}

- ソースバケットに追加するファイルは512&nbsp;MBを超えないようにしてください。この制限はAmazon S3とGoogle Cloud Storageの両方に適用されます。512&nbsp;MBを超えるファイルはエラーとなり、Brazeに同期されません。
- 1ファイルあたりの行数に追加の制限はありませんが、同期の実行速度を向上させるために、より小さなファイルを使用することをお勧めします。例えば、500&nbsp;MBのファイル1つを取り込むよりも、100&nbsp;MBのファイル5つに分けた方がかなり速く処理できます。
- 一定期間内にアップロードできるファイル数に追加の制限はありません。
- ファイル内およびファイル間での順序付けはサポートされていません。予想される競合を監視している場合は、更新を定期的にバッチ処理することをお勧めします。

## トラブルシューティング {#troubleshooting}

### ファイルのアップロードと処理 {#uploading-files-and-processing}

CDIは、同期が作成された後に追加されたファイルのみを処理します。このプロセスでは、Brazeは新しいファイルの追加を検知し、新しい通知をトリガーします。これにより、新しいファイルを処理するための新しい同期が開始されます。Amazon S3の場合、通知はSQSへのメッセージです。Google Cloud Storageの場合、Pub/Subへの`OBJECT_FINALIZE`メッセージです。

既存のファイルを使用して、Brazeがバケットにアクセスし、取り込むファイルを検出できるかどうかを検証できますが、それらのファイルはBrazeに同期されません。CDIでそれらを処理するには、同期したい既存のファイルをソースバケットに再アップロードする必要があります。

### 予期しないファイルエラーの処理（Amazon S3） {#handling-unexpected-file-errors-amazon-s3}

多数のエラーや失敗したファイルが発生している場合、CDIのターゲットフォルダー以外のフォルダーにファイルを追加する別のプロセスがS3バケットに存在する可能性があります。

ファイルがソースバケットにアップロードされたがソースフォルダーにない場合、CDIはSQS通知を処理しますが、そのファイルに対してアクションを実行しないため、エラーとして表示される場合があります。

問題がS3通知またはSQS送信先の権限に関連している場合（例：送信先の検証エラー）、AWSのドキュメントを参照してください：

- [Amazon S3コンソールを使用したイベント通知の有効化と設定](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [送信先にイベント通知メッセージを公開する権限の付与](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Amazon SQSの問題のトラブルシューティング](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### 予期しないファイルエラーの処理（Google Cloud Storage） {#handling-unexpected-file-errors-google-cloud-storage}

Amazon S3と同様に、CDIは同期が作成された後にアップロードされたファイルのみを処理します。新しいオブジェクトごとに、Pub/Subトピックへの`OBJECT_FINALIZE`メッセージがトリガーされます。バケットに既に存在するファイルを取り込むには、それらを再アップロードしてください。

ファイルが取り込まれない場合は、以下を確認してください：

- バケット通知が存在すること。`gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME`でバケットの通知を一覧表示できます。
- Cloud Storageサービスエージェントがトピックに対して`roles/pubsub.publisher`を持っていること。
- Brazeサービスアカウントがサブスクリプションに対する消費権限（`pubsub.subscriptions.consume`、カスタムロールまたは`roles/pubsub.subscriber`を通じて付与）を持っていること。

詳細については、Google Cloudドキュメントの[Cloud StorageのPub/Sub通知](https://cloud.google.com/storage/docs/pubsub-notifications)を参照してください。