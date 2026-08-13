---
nav_title: ファイルストレージの連携
article_title: ファイルストレージの連携
description: "このページでは、Brazeクラウドデータ取り込みと、S3からBrazeへの関連データの同期方法について説明します。"
page_order: 4
page_type: reference

---

# ファイルストレージの連携 {#file-storage-integrations}

> このページでは、クラウドデータ取り込みのサポートを設定し、S3からBrazeに関連データを同期する方法について説明します。

## 仕組み {#how-it-works}

Cloud Data Ingestion (CDI) for S3を使用すると、AWSアカウント内の1つ以上のS3バケットをBrazeと直接統合できます。新しいファイルがS3に公開されると、SQSにメッセージが投稿され、Braze Cloud Data Ingestionがそれらの新しいファイルを取り込みます。

Cloud Data Ingestionは以下をサポートしています。

- JSONファイル
- CSVファイル
- Parquetファイル
- 属性、カスタムイベント、購入イベント、ユーザー削除、およびカタログデータ

## 前提条件 {#prerequisites}

この統合には以下のリソースが必要です。

 - データストレージ用のS3バケット
 - 新しいファイル通知用のSQSキュー
 - Brazeアクセス用のIAMロール

### AWSの定義 {#aws-definitions}

まず、このタスクで使用する用語を定義します。

| 用語 | 定義 |
| --- | --- |
| Amazon Resource Name (ARN) | ARNは、AWSリソースの一意の識別子です。 |
| Identity and Access Management (IAM) | IAMは、AWSリソースへのアクセスを安全に制御できるWebサービスです。このチュートリアルでは、IAMポリシーを作成してIAMロールに割り当て、S3バケットをBraze Cloud Data Ingestionと統合します。 |
| Amazon Simple Queue Service (SQS) | SQSは、分散ソフトウェアシステムやコンポーネントを統合できるホスト型キューです。 |
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

## BrazeでのCloud Data Ingestionの設定 {#setting-up-cloud-data-ingestion-in-braze}

1. まず、Brazeダッシュボードで新しいソースを作成します。**データ設定** > **Cloud Data Ingestion** > **ソース**に移動し、**データソースを追加**を選択してから、**Amazon S3**を選択します。
2. ソースの名前を選択し、AWSの設定プロセスで取得した情報を入力して新しいソースを作成します。以下を指定します。

  - ロール ARN
  - External ID
  - バケット名
  - リージョン

![認証情報（AWSの設定とBrazeの設定）および構成フィールドを表示するS3接続詳細セクション。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. **接続をテスト**を選択して、Brazeがバケットにアクセスできることを確認します。テストが成功したら、**ソースに接続**を選択します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{: start="4"}
4. 次に、新しい同期を作成します。**データ設定** > **Cloud Data Ingestion** > **同期**に移動し、**データ同期を作成**を選択します。

{: start="5"}
5. 同期の名前を選択します。次に、アクティブなS3ソースを選択し、同期用のソーステーブルを入力します。データタイプを選択し、**接続をテスト**を選択します。

![データプレビュー付きの接続テストオプション。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. AWSの設定プロセスで取得した残りの情報を入力します。以下を指定します。
- SQS URL（新しいインテグレーションごとに一意である必要があります）
- フォルダパス（オプション、ワークスペース内の同期間で一意である必要があります）

7. データタイプを選択し、**接続をテスト**を選択して、Brazeが取り込み可能なファイルの一覧を取得できることを確認します（ファイル内のデータではありません）。成功したら、**次へ：通知**を選択します。
8. アクセスや権限の問題で同期が中断した場合の通知用に、連絡先メールアドレスを追加します。オプションで、ユーザーレベルのエラーや同期成功の通知を有効にすることもできます。
9. 同期を作成します。

## 必須ファイル形式 {#required-file-formats}

クラウドデータインジェスションは、JSON、CSV、Parquet ファイルをサポートしています。必須カラムはデータタイプによって異なります。

- ユーザーデータ（属性、カスタムイベント、購入イベント）はユーザー識別子とペイロードを使用します
- カタログデータはカタログ識別子を使用します

カタログデータに S3 を使用している場合は、このページと[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を併せて参照し、カタログ固有の要件と動作を確認してください。

Braze は、AWS が適用する要件以外に追加のファイル名要件を適用しません。ファイル名は一意である必要があります。タイムスタンプを付加すると一意性を確保しやすくなります。

サポートされているすべてのファイルタイプ（属性、カスタムイベント、購入、カタログ、ユーザー削除）の例については、[braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage) のサンプルファイルを参照してください。

### ユーザー識別子 {#user-identifiers}

ユーザーデータの同期（属性、カスタムイベント、購入イベント）では、ソースファイルの各行にユーザー識別子が1つと `PAYLOAD` カラムが必要です。ソースファイルには異なる識別子タイプの行を含めることができますが、各行では1つの識別子のみを使用してください。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | 更新するユーザーを識別します。Brazeで使用される `external_id` の値と一致する必要があります。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | この2つのカラムでユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子で、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つだけです。 |
| `BRAZE_ID` | Brazeユーザー識別子です。Braze SDKによって生成され、クラウドデータインジェスションを通じてBraze IDで新しいユーザーを作成することはできません。新しいユーザーを作成するには、external IDまたはユーザーエイリアスを指定してください。 |
| `EMAIL` | ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、Brazeはメールをプライマリ識別子として使用します。 |
| `PHONE` | ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー識別子" }

識別子に加えて、各行にはBrazeのユーザーに同期するフィールドのJSON文字列を含む `PAYLOAD` カラムが必要です。

{% alert note %}
データウェアハウスソースとは異なり、`UPDATED_AT` カラムはファイルストレージ同期では必須でもサポートされてもいません。
{% endalert %}

### カタログ識別子 {#catalog-identifiers}

カタログの同期では、ソースファイルに以下のカラムが必要です。カタログファイルはユーザーデータファイルとは異なる識別子を使用します。

| カラム | 必須 | 説明 |
| --- | --- | --- |
| `ID` | はい | カタログアイテムの一意の識別子です。Brazeでアイテムの作成、更新、削除に使用されます。 |
| `PAYLOAD` | はい | 同期するカタログフィールドと値のJSON文字列です。Brazeのカタログのスキーマと一致する必要があります。 |
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
オプションの `DELETED` カラムを含めることができます。`DELETED` が `true` の場合、そのカタログアイテムはBrazeのカタログから削除されます。必須カラムの完全なリストについては、[カタログ識別子](#catalog-identifiers)を参照してください。削除の動作については、[カタログアイテムの削除](#deleting-catalog-items)を参照してください。エンドツーエンドのカタログ設定フロー（ターゲットカタログの作成と同期動作を含む）については、[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を参照してください。
{% endtab %}

{% endtabs %}

## データの削除 {#deleting-data}

S3向けのCloud Data Ingestionは、ファイルアップロードによるユーザーおよびカタログアイテムの削除をサポートしています。それぞれに個別の同期とファイル形式を使用してください。

- **[ユーザーの削除](#deleting-users)** – データタイプを**Delete Users**に設定した同期を作成し、ユーザー識別子のみを含むファイル（ペイロードなし）をアップロードします。
- **[カタログアイテムの削除](#deleting-catalog-items)** – 既存のカタログ同期を使用し、`deleted`（または`DELETED`）列を追加して削除対象のアイテムをマークします。

### ユーザーの削除 {#deleting-users}

S3内のファイルを使用してBrazeのユーザープロファイルを削除するには：

1. 新しいCloud Data Ingestion同期を作成します（他の同期と同じ[AWSおよびBrazeの設定](#setting-up-cloud-data-ingestion-in-aws)を使用します）。
2. Brazeで同期を設定する際に、**Data Type**を**Delete Users**に設定します。
3. ユーザー識別子の列のみを含むファイルをS3バケットにアップロードします。`PAYLOAD`列は含めないでください。誤った削除を防ぐため、ペイロードが存在すると同期は失敗します。

ファイルの各行は、以下のいずれかを使用して正確に1人のユーザーを識別する必要があります。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | Brazeで使用される`external_id`と一致します。 |
| `ALIAS_NAME`と`ALIAS_LABEL` | 両方の列を組み合わせて、エイリアスでユーザーを識別します。 |
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

1. [カタログデータの同期]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)に使用しているのと同じS3同期（データタイプ**Catalogs**）を使用します。
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

## 注意事項 {#things-to-know}

- S3ソースバケットに追加するファイルは512&nbsp;MBを超えないようにしてください。512&nbsp;MBを超えるファイルはエラーとなり、Brazeに同期されません。
- ファイルあたりの行数に追加の制限はありませんが、同期の実行速度を向上させるために、より小さなファイルを使用することをお勧めします。たとえば、500&nbsp;MBのファイル1つを取り込むよりも、100&nbsp;MBのファイル5つに分割した方がかなり速く処理できます。
- 一定期間内にアップロードできるファイル数に追加の制限はありません。
- ファイル内およびファイル間での順序付けはサポートされていません。予想される競合を監視している場合は、更新を定期的にバッチ処理することをお勧めします。

## トラブルシューティング {#troubleshooting}

### ファイルのアップロードと処理 {#uploading-files-and-processing}

CDIは、同期が作成された後に追加されたファイルのみを処理します。このプロセスでは、Brazeは新しいファイルの追加を検知し、SQSへの新しいメッセージをトリガーします。これにより、新しいファイルを処理するための新しい同期が開始されます。

既存のファイルを使用して、Brazeがバケットにアクセスし、取り込むファイルを検出できるかどうかを検証できますが、それらのファイルはBrazeに同期されません。CDIでそれらを処理するには、同期したい既存のファイルをS3に再アップロードする必要があります。

### 予期しないファイルエラーの処理 {#handling-unexpected-file-errors}

多数のエラーや失敗したファイルが発生している場合、CDIのターゲットフォルダー以外のフォルダーにファイルを追加する別のプロセスが存在する可能性があります。

ファイルがソースバケットにアップロードされたがソースフォルダーにない場合、CDIはSQS通知を処理しますが、そのファイルに対してアクションを実行しないため、エラーとして表示されることがあります。

問題がS3通知やSQS送信先の権限に関連している場合（例えば、送信先の検証エラーなど）、AWSのドキュメントを参照してください。

- [Amazon S3コンソールを使用したイベント通知の有効化と設定](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [送信先へのイベント通知メッセージの公開権限の付与](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Amazon SQSの問題のトラブルシューティング](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)