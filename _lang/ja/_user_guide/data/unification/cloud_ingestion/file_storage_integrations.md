---
nav_title: ファイルストレージの連携
article_title: ファイルストレージの連携
description: "このページでは、Braze クラウドデータ取り込みと、S3 から Braze への関連データの同期方法について説明します。"
page_order: 4
page_type: reference

---

# ファイルストレージの連携 {#file-storage-integrations}

> このページでは、クラウドデータ取り込みのサポートを設定し、S3 から Braze に関連データを同期する方法について説明します。

## 仕組み {#how-it-works}

S3 用のクラウドデータ取り込み (CDI) を使用して、AWS アカウントの1つ以上の S3 バケットをBraze と直接統合できます。新規ファイルが S3 にパブリッシュされると、メッセージが SQS に投稿され、Braze のクラウドデータ取り込みがそれらの新規ファイルを取り込みます。

クラウドデータ取り込みは、以下をサポートしています。

- JSON ファイル
- CSVファイル
- Parquet ファイル
- 属性、カスタムイベント、購入イベント、ユーザー削除、カタログデータ

## 前提条件 {#prerequisites}

連携には次のリソースが必要です。

 - データストレージ用の S3 バケット
 - 新規ファイル通知用の SQS キュー
 - Braze アクセス用の IAM ロール

### AWS の定義 {#aws-definitions}

まず、この作業で使用される用語を定義します。

| 用語 | 定義 |
| --- | --- |
| Amazon リソースネーム (ARN) | ARN は、AWS リソースの一意の識別子です。 |
| アイデンティティとアクセス管理 (IAM) | IAM は、AWS リソースへのアクセスを安全にコントロールできる Web サービスです。このチュートリアルでは、IAM ポリシーを作成し、それを IAM ロールに割り当てて、S3 バケットをBraze クラウドデータ取り込みと統合します。 |
| Amazon Simple Queue Service (SQS) | SQS は、分散ソフトウェアシステムとコンポーネントを統合できるホストキューです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="AWS の定義" }

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
2. 設定に名前を付けます。オプションで、ファイルのサブセットのみをBraze で取り込む場合は、対象とするプレフィックスまたはサフィックスを指定します。
3. **Destination** で **SQS queue** を選択し、ステップ 2 で作成した SQS の ARN を指定します。

{% alert note %}
S3 バケットのルートフォルダーにファイルをアップロードした後、一部のファイルをバケット内の特定のフォルダーに移動すると、予期しないエラーが発生することがあります。代わりに、イベント通知をプレフィックス内のファイルについてのみ送信するように変更するか、プレフィックス外のファイルを S3 バケットに入れないようにするか、またはプレフィックスなしで連携を更新すること（すべてのファイルが取り込まれる）ができます。
{% endalert %}

### ステップ 5: IAM ポリシーの作成 {#step-5-create-an-iam-policy}

ソースバケットの操作をBraze に許可する IAM ポリシーを作成します。まず、アカウント管理者として AWS 管理コンソールにサインインします。

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

1. まず、Braze ダッシュボードで新しいソースを作成します。**データ設定** > **クラウドデータ取り込み** > **ソース**に移動し、**データソースを追加**を選択して、**Amazon S3** を選択します。
2. ソースの名前を選択し、AWS の設定プロセスからの情報を入力して新しいソースを作成します。次の項目を指定します。

  - ロールの ARN
  - External ID
  - バケット名
  - リージョン

![認証情報（AWS 設定とBraze 設定）および設定フィールドが表示された S3 接続詳細セクション。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. **Test connection** を選択して、Braze がバケットにアクセスできることを確認します。テストが成功したら、**Connect to Source** を選択します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{: start="4"}
4. 次に、新しい同期を作成します。**データ設定** > **クラウドデータ取り込み** > **同期**に移動し、**データ同期を作成**を選択します。

{: start="5"}
5. 同期の名前を選択します。次に、アクティブな S3 ソースを選択し、同期のソーステーブルを入力します。データタイプを選択し、**Test Connection** を選択します。

![データプレビューで接続をテストするオプション。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. AWS の設定プロセスからの残りの情報を入力します。次の項目を指定します。
- SQS URL（新しい連携ごとに一意である必要があります）
- フォルダーパス（オプション、ワークスペース内の同期間で一意である必要があります）

7. データタイプを選択し、**Test Connection** を選択して、Braze が取り込み可能なファイル（ファイル内のデータではなく）を一覧表示できることを確認します。成功したら、**Next: Notifications** を選択します。
8. アクセスや権限の問題で同期が中断した場合に通知を受け取る連絡先メールアドレスを追加します。オプションで、ユーザーレベルのエラーと同期の成功の通知をオンにします。
9. 同期を作成します。


## 必要なファイル形式 {#required-file-formats}

クラウドデータ取り込みは、JSON、CSV、および Parquet のファイルをサポートしています。必要な列はデータタイプによって異なります。

- ユーザーデータ（属性、カスタムイベント、購入イベント）はユーザー識別子とペイロードを使用します
- カタログデータはカタログ識別子を使用します

S3 をカタログデータに使用している場合は、このページと[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を併せて参照し、カタログ固有の要件と動作を確認してください。

Braze は、AWS によって強制される以上の追加のファイル名要件を強制しません。ファイル名は一意でなければなりません。一意性を確保するためにタイムスタンプを付加することを推奨します。

サポートされているすべてのファイルタイプ（属性、カスタムイベント、購入、カタログ、ユーザー削除）の例については、[braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage) のサンプルファイルを参照してください。

### ユーザー識別子 {#user-identifiers}

ユーザーデータの同期（属性、カスタムイベント、購入イベント）では、ソースファイルの各行に正確に1つのユーザー識別子と `PAYLOAD` 列が必要です。ソースファイルには異なる識別子タイプの行を含めることができますが、各行では1つの識別子のみを使用する必要があります。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | 更新したいユーザーを識別します。これはBraze で使用されている `external_id` 値と一致する必要があります。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | これら2つの列は、ユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子でなければならず、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つしか持てません。 |
| `BRAZE_ID` | Braze のユーザー識別子です。これはBraze SDKによって生成されます。クラウドデータ取り込み経由でBraze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、external ID またはユーザーエイリアスを指定します。 |
| `EMAIL` | ユーザーのメールアドレスです。同じメールアドレスを持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。メールと電話の両方を含める場合は、Braze はメールをプライマリ識別子として使用します。 |
| `PHONE` | ユーザーの電話番号です。同じ電話番号を持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー識別子" }

識別子に加えて、各行にはBraze のユーザーに同期させたいフィールドの JSON 文字列を含む `PAYLOAD` 列が必要です。

{% alert note %}
データウェアハウスソースとは異なり、`UPDATED_AT` 列はファイルストレージ同期では必須ではなく、サポートもされていません。
{% endalert %}

### カタログ識別子 {#catalog-identifiers}

カタログ同期では、ソースファイルに以下の列を含める必要があります。カタログファイルはユーザーデータファイルとは異なる識別子を使用します。

| 列 | 必須 | 説明 |
| --- | --- | --- |
| `ID` | はい | カタログアイテムの一意の識別子です。Braze でアイテムの作成、更新、または削除に使用されます。 |
| `PAYLOAD` | はい | 同期するカタログフィールドと値の JSON 文字列です。Braze のカタログのスキーマと一致する必要があります。 |
| `DELETED` | いいえ | `true` の場合、一致する `ID` のカタログアイテムがBraze のカタログから削除されます。作成または更新操作の場合は、この列を省略するか `false` に設定します。 |
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
ソースファイルのすべての行に有効な JSON が含まれている必要があります。含まれていない場合、ファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
ソースファイルのすべての行に有効な JSON が含まれている必要があります。含まれていない場合、ファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
ソースファイルのすべての行に有効な JSON が含まれている必要があります。含まれていない場合、ファイルはスキップされます。
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
オプションの `DELETED` 列を含めます。`DELETED` が `true` の場合、そのカタログアイテムはBraze のカタログから削除されます。必要な列の完全なリストについては、[カタログ識別子](#catalog-identifiers)を参照してください。削除の動作については、[カタログアイテムの削除](#deleting-catalog-items)を参照してください。エンドツーエンドのカタログ設定フロー（ターゲットカタログの作成と同期の動作を含む）については、[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を参照してください。
{% endtab %}

{% endtabs %}

## データの削除 {#deleting-data}

S3 向けクラウドデータ取り込みは、ファイルアップロードを通じてユーザーとカタログアイテムの削除をサポートしています。それぞれに別々の同期とファイル形式を使用します。

- **[ユーザーの削除](#deleting-users)** – データタイプ **Delete Users** で同期を作成し、ユーザー識別子のみを含むファイル（ペイロードなし）をアップロードします。
- **[カタログアイテムの削除](#deleting-catalog-items)** – 既存のカタログ同期を使用し、削除対象のアイテムをマークする `deleted`（または `DELETED`）列を追加します。

### ユーザーの削除 {#deleting-users}

S3 のファイルを使ってBraze でユーザープロファイルを削除するには：

1. 新しいクラウドデータ取り込み同期を作成します（他の同期と同じ [AWS とBraze の設定](#setting-up-cloud-data-ingestion-in-aws)を使用します）。
2. Braze で同期を設定する際、**Data Type** を **Delete Users** に設定します。
3. S3 バケットに、ユーザー識別子列のみを含むファイルをアップロードします。`PAYLOAD` 列を含めないでください。ペイロードが存在すると、誤削除を防ぐために同期が失敗します。

ファイルの各行は、次のいずれかを使用して正確に1人のユーザーを識別する必要があります。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | Braze で使用される `external_id` と一致します。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | 両方の列を合わせて、ユーザーをエイリアスで識別します。 |
| `BRAZE_ID` | Braze が生成したユーザー ID（既存ユーザーのみ）。 |
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

同期が実行されると、Braze はバケット内の新規ファイルを処理し、対応するユーザープロファイルを削除します。

### カタログアイテムの削除 {#deleting-catalog-items}

ファイルストレージを使用してカタログからアイテムを削除するには：

1. [カタログデータの同期]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)（データタイプ：**Catalogs**）に使用するのと同じ S3 同期を使用します。
2. CSV ファイルや JSON ファイルに、オプションの **`deleted`**（または **`DELETED`**）列を追加します。
3. Braze のカタログから削除したいカタログアイテムには、`deleted` を `true` に設定します。

各行にはまだ `ID` と `PAYLOAD` が必要です。削除対象の行については、ペイロードは最小限で構いません。Braze は `ID` でアイテムを削除します。

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

同期が実行されると、`deleted: true` の行に対応するカタログアイテムがBraze から削除されます。カタログデータの完全な同期と削除の動作については、[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を参照してください。

## 知っておくべきこと {#things-to-know}

- S3 ソースバケットに追加するファイルは 512&nbsp;MB を超えてはなりません。512&nbsp;MB を超えるファイルはエラーになり、Braze に同期されません。
- 1ファイルあたりの行数に追加の制限はありませんが、同期の速度を向上させるために、小さなファイルを使用することをお勧めします。例えば、500&nbsp;MB のファイルの取り込みは、100&nbsp;MB のファイルを5つに分けて取り込む場合よりもかなり時間がかかります。
- 一定期間内にアップロードできるファイルの数に追加の制限はありません。
- ファイル内やファイル間の順序付けはサポートされていません。競合が予想される状況を監視している場合は、定期的に更新をバッチ処理することをお勧めします。

## トラブルシューティング {#troubleshooting}

### ファイルのアップロードと処理 {#uploading-files-and-processing}

CDI は、同期が作成された後に追加されたファイルのみを処理します。このプロセスでは、Braze が新しいファイルの追加を検知し、SQS への新しいメッセージがトリガーされます。これにより、新しいファイルを処理するための新しい同期が開始されます。

既存のファイルを使って、Braze がバケットにアクセスでき、取り込むファイルを検出できることを確認できますが、それらのファイルはBraze に同期されません。CDI がそれらを処理するには、同期したい既存のファイルを S3 に再アップロードする必要があります。

### 予期しないファイルエラーの処理 {#handling-unexpected-file-errors}

エラーや失敗ファイルが多い場合は、CDI のターゲットフォルダー以外のフォルダーにある S3 バケットに、別のプロセスがファイルを追加している可能性があります。

ファイルがソースバケットにアップロードされたがソースフォルダーには含まれていない場合、CDI は SQS 通知を処理しますが、ファイルに対してアクションを実行しないため、エラーとして表示されることがあります。

問題が S3 通知や SQS 送信先の権限に関連している場合（例えば、送信先の検証エラー）は、AWS のドキュメントを参照してください。

- [Amazon S3 コンソールを使用したイベント通知の有効化と設定](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [送信先へのイベント通知メッセージの発行権限の付与](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Amazon SQS の問題のトラブルシューティング](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)