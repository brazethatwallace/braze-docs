---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "このリファレンス記事では、Amazon Web Servicesが提供する高度にスケーラブルなストレージシステムであるBrazeとAmazon S3の連携について説明します。"
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/)は、Amazon Web Servicesが提供する高度にスケーラブルなストレージシステムです。

{% alert important %}
クラウドストレージプロバイダーを切り替える場合は、Brazeカスタマーサクセスマネージャーに連絡し、新しい連携の設定と検証についてサポートを受けてください。
{% endalert %}

BrazeとAmazon S3の連携には、2つの統合戦略があります。

- [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)を活用すると、他のプラットフォーム、ツール、ロケーションに接続するまでデータを保存できます。
- ダッシュボードのデータエクスポート（CSVエクスポートやエンゲージメントレポートなど）を使用します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Amazon S3アカウント | この連携を利用するには、Amazon S3アカウントが必要です。 |
| 専用S3バケット | Amazon S3と統合する前に、アプリ用のS3バケットを作成する必要があります。<br><br>すでにS3バケットがある場合でも、Braze専用の新しいバケットを作成して権限を制限することをお勧めします。新しいバケットの作成方法については、以下の手順を参照してください。 |
| Currents | Amazon S3にデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)を設定する必要があります。メッセージアーカイブの設定のみの場合、Currentsは必要ありません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 新しいS3バケットの作成 {#creating-a-new-s3-bucket}

アプリのバケットを作成するには、以下の手順を実行します。

1. [Amazon S3コンソール](https://console.aws.amazon.com/s3/)を開き、指示に従ってAWSに**サインイン**または**アカウントを作成**します。
2. サインイン後、**Storage & Content Delivery**カテゴリーから**S3**を選択します。
3. 次の画面で**Create Bucket**を選択します。
4. プロンプトが表示されたら、バケットを作成し、AWSリージョンを選択します。

Brazeでは、ダッシュボードでリージョンを選択または設定することはできません。AWSリージョンは、AWSコンソールでバケットを作成した場所によって固定されます。統合は指定したバケット名にデータを送信し、AWSが自動的にリクエストをバケットのリージョンにルーティングします。コネクタが希望するリージョンとは異なるリージョンに接続しようとする場合（例えば、`eu-central-1`ではなく`eu-west-1`に接続する場合）、AWSで希望するリージョンにS3バケットを作成または使用してください。Braze側で変更する必要はありません。

{% alert note %}
Currentsは、[Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)が設定されたバケットには対応していません。
{% endalert %}

## 統合 {#integration}

BrazeにはAmazon S3に関する2種類の統合戦略があります。1つは[Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)用、もう1つはすべてのダッシュボードデータエクスポート（CSVエクスポートやエンゲージメントレポートなど）用です。どちらの統合も、2種類の認証/許可方法をサポートしています。

- [AWSシークレットアクセスキー方式](#aws-secret-key-auth-method)
- [AWSロールARN方式](#aws-role-arn-auth-method)

## AWSシークレットキー認証方式 {#aws-secret-key-auth-method}

この認証方式は、シークレットキーとアクセスキーIDを生成し、BrazeがAWSアカウントのユーザーとして認証してバケットにデータを書き込めるようにします。

### ステップ1:ユーザーを作成する {#secret-key-1}

{% alert note %}
メッセージアーカイブの設定のみを行う場合は、**Dashboard Data Export**タブのステップに従ってください。
{% endalert %}

アクセスキーIDとシークレットアクセスキーを取得するには、[AWSでIAMユーザーと管理者グループを作成](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)します。

### ステップ2:認証情報を取得する {#secret-key-2}

新しいユーザーの作成後に、**Show User Security Credentials**を選択して、アクセスキーIDとシークレットアクセスキーを表示します。次に、これらの認証情報をどこかにメモしておくか、**Download Credentials**ボタンを選択してください。後でBrazeダッシュボードに入力する必要があります。

![アクセスキーIDとシークレットアクセスキーが表示されたAWS IAMユーザーセキュリティ認証情報ページ。]({% image_buster /assets/img_archive/S3_Credentials.png %})

### ステップ3:ポリシーを作成する {#secret-key-3}

**Policies** > **Get Started** > **Create Policy**に移動して、ユーザーの権限を追加します。次に、**Create Your Own Policy**を選択します。これにより限定的な権限が付与され、Brazeは指定されたバケットにのみアクセスできます。

![S3統合のポリシーオプションが表示されたAWS IAMポリシー作成画面。]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
CurrentsとDashboard Data Exportには異なるポリシーが必要です。Brazeバックエンドがエラー処理を実行できるようにするには、`s3:GetObject`が必要です。
{% endalert %}

任意のポリシー名を指定し、**Policy Document**セクションに以下のコードスニペットを入力します。`INSERTBUCKETNAME`は必ずバケット名に置き換えてください。これらの権限がないと、認証情報のチェックに失敗し、統合は作成されません。

{% alert note %}
メッセージアーカイブの設定のみを行う場合は、**Dashboard Data Export**タブのコードスニペットを使用してください。
{% endalert %}

{% tabs %}
{% tab Braze Currents %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Dashboard Data Export %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### ステップ4:ポリシーをアタッチする {#secret-key-4}

新しいポリシーの作成後に、**Users**に移動し、特定のユーザーを選択します。**Permissions**タブで**Attach Policy**を選択し、作成した新しいポリシーを選択します。これで、AWS認証情報をBrazeアカウントにリンクする準備ができました。

![Attach Policyアクションが選択されたAWS IAMユーザー権限タブ。]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### ステップ5:BrazeをAWSにリンクする {#secret-key-5}

{% alert note %}
メッセージアーカイブの設定のみを行う場合は、**Dashboard Data Export**タブのステップに従ってください。
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Brazeで、**パートナー連携** > **Currents**に移動します。

次に、**Create New Current**を選択し、**Amazon S3 Data Export**を選択します。

Currentに名前を付けます。**Credentials**セクションで、**AWS Secret Access Key**が選択されていることを確認し、指定されたフィールドにS3アクセスID、AWSシークレットアクセスキー、およびAWS S3バケット名を入力します。

![AWSシークレットキー認証情報フィールドが表示されたBrazeのAmazon S3用Create New Currentフォーム。]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
AWSアクセスキーIDとシークレットアクセスキーを最新の状態に保ってください。コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止します。この状態が**5日間**以上続くと、コネクタのイベントは削除され、データは永久に失われます。
{% endalert %}

必要に応じて、次のカスタマイズを追加することもできます。

- **フォルダーパス：**デフォルトは`currents`です。このフォルダーが存在しない場合、Brazeが自動的に作成します。
- **サーバーサイド保管時AES-256暗号化：**デフォルトはオフで、`x-amz-server-side-encryption`ヘッダーが含まれます。

**Launch Current**を選択して続行します。

認証情報が正常に検証されたかどうかが通知されます。AWS S3がBraze Currents用に設定されました。

{% endtab %}
{% tab Dashboard Data Export %}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Amazon S3**を選択します。

**AWS Credentials**ページで、**AWS Secret Access Key**が選択されていることを確認し、指定されたフィールドにAWSアクセスID、AWSシークレットアクセスキー、およびAWS S3バケット名を入力します。シークレットキーを入力する際は、まず**Test Credentials**を選択して認証情報が機能することを確認し、成功したら**Save**を選択します。

![テストと保存のアクションが表示されたBrazeのAmazon S3テクノロジーパートナー認証情報ページ。]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
ユーザーに移動し、AWSコンソールの**Security Credentials**タブで**Create Access Key**を選択することで、いつでも新しい認証情報を取得できます。
{% endalert %}

認証情報が正常に検証されたかどうかが通知されます。AWS S3がBrazeアカウントに統合されました。

{% endtab %}
{% endtabs %}

## AWSロールARN認証方式 {#aws-role-arn-auth-method}

この認証方式は、ロールAmazon Resource Name（ARN）を生成し、BrazeのAmazonアカウントがバケットにデータを書き込むために作成したロールのメンバーとして認証できるようにします。

### ステップ1:ポリシーを作成する {#role-arn-1}

まず、アカウント管理者としてAWS管理コンソールにサインインします。AWSコンソールのIAMセクションに移動し、ナビゲーションバーで**Policies**を選択してから、**Create Policy**を選択します。

![Create Policyボタンが選択されたAWS IAM Policiesページ。]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
CurrentsとDashboard Data Exportには異なるポリシーが必要です。Brazeバックエンドがエラー処理を実行できるようにするには、`s3:GetObject`が必要です。
{% endalert %}

**JSON**タブを開き、**Policy Document**セクションに以下のコードスニペットを入力します。`INSERTBUCKETNAME`は必ずバケット名に置き換えてください。入力が終わったら、**Review Policy**を選択します。

{% alert note %}
メッセージアーカイブの設定のみを行う場合は、**Dashboard Data Export**タブのコードスニペットを使用してください。
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Dashboard Data Export %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

次に、ポリシーに名前と説明を指定し、**Create Policy**を選択します。

![ポリシー名と説明のフィールドが表示されたAWS IAMポリシーレビューステップ。]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![新しく作成されたS3ポリシーが表示されたAWS IAMポリシーリスト。]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### ステップ2:ロールを作成する {#role-arn-2}

コンソールの同じIAMセクションで、**Roles** > **Create Role**を選択します。

![Create Roleボタンが選択されたAWS IAM Rolesページ。]({{site.baseurl}}/assets/img/create_role_1_list.png)

BrazeアカウントからBrazeアカウントIDとexternal IDを取得します。

- **Currents：**Brazeで、**パートナー連携** > **Currents**に移動します。次に、**Create New Current**を選択し、**Amazon S3 Data Export**を選択します。ここで、ロールの作成に必要な識別子を確認できます。
- **ダッシュボードデータエクスポート：**Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Amazon S3**を選択します。ここで、ロールの作成に必要な識別子を確認できます。（メッセージアーカイブの設定のみを行う場合は、ここでロールを作成してください。）

AWSコンソールに戻り、信頼できるエンティティセレクターのタイプとして**Another AWS Account**を選択します。BrazeアカウントIDを入力し、**Require external ID**チェックボックスをオンにして、Brazeのexternal IDを入力します。完了したら**Next**を選択します。

![S3の「Create Role」ページ。このページには、ロール名、ロールの説明、信頼できるエンティティ、ポリシー、および権限境界のフィールドがあります。]({{site.baseurl}}/assets/img/create_role_2_another.png)

### ステップ3:ポリシーをアタッチする {#role-arn-3}

次に、以前に作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横にチェックマークを付けてアタッチします。完了したら**Next**を選択します。

![ロールARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

ロールに名前と説明を指定し、**Create Role**を選択します。

![ロールARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

新しく作成したロールがリストに表示されます。

### ステップ4:Braze AWSにリンクする {#role-arn-4}

AWSコンソールで、新しく作成したロールをリストから見つけます。名前を選択して、そのロールの詳細を開きます。

![新しく作成されたロールの詳細が表示されたAWS IAMロール詳細ページ。]({{site.baseurl}}/assets/img/create_role_5_created.png)

ロール概要ページの上部にある**Role ARN**をメモします。

![ロールARN値が表示されたAWS IAMロール概要。]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Brazeアカウントに戻り、提供されたフィールドにロールARNをコピーします。

{% alert note %}
メッセージアーカイブの設定のみを行う場合は、**Dashboard Data Export**タブのステップに従ってください。
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Brazeで、**パートナー連携** > **Currents**に移動します。次に、**Create New Current**を選択し、**Amazon S3 Data Export**を選択します。

![AWSロールARNとバケットフィールドが表示されたBraze CurrentsのAmazon S3設定画面。]({{site.baseurl}}/assets/img/currents-role-arn.png)

Currentに名前を付けます。次に、**Credentials**セクションで**AWS Role ARN**が選択されていることを確認し、ロールARNとAWS S3バケット名を所定のフィールドに入力します。

必要に応じて、次のカスタマイズを追加することもできます。

- フォルダーパス（デフォルトは`currents`）
- サーバーサイド保管時AES-256暗号化（デフォルトはオフ）- `x-amz-server-side-encryption`ヘッダーを含みます

**Launch Current**を選択して続行します。認証情報が正常に検証されると通知が表示されます。AWS S3がBraze Currents用に設定されました。

{% alert important %}
「S3の認証情報が無効です」というエラーが表示された場合、AWSでロールを作成した直後に統合を行ったことが原因である可能性があります。しばらく待ってから再試行してください。メッセージに`PutObject`アクセスまたはダッシュボードデータエクスポートのサーバーサイド暗号化について記載されている場合は、[S3認証情報エラーのトラブルシューティング](#troubleshooting)を参照してください。
{% endalert %}

{% endtab %}
{% tab Dashboard Data Export %}

Brazeで、**統合**の**テクノロジーパートナー**ページに移動し、**Amazon S3**を選択します。

![AWSロールARN認証情報が選択されたBrazeのAmazon S3テクノロジーパートナーページ。]({{site.baseurl}}/assets/img/data-export-role-arn.png)

**AWS Credentials**ページで、**AWS Role ARN**ラジオボタンが選択されていることを確認し、ロールARNとAWS S3バケット名を所定のフィールドに入力します。まず**Test Credentials**を選択して認証情報が正しく動作することを確認し、成功したら**Save**を選択します。

{% alert tip %}
ユーザーに移動し、AWSコンソールの**Security Credentials**タブで**Create Access Key**を選択することで、いつでも新しい認証情報を取得できます。
{% endalert %}

認証情報が正常に検証されたかどうかが通知されます。AWS S3がBrazeアカウントに統合されました。

{% endtab %}
{% endtabs %}

## Currents用のAmazon S3認証情報の更新 {#updating-currents-credentials}

既存のBraze Currentsコネクタで、統合を停止したり、すでにバケットにエクスポートされたデータを失ったりすることなく、Amazon S3認証情報を更新できます。

認証情報を更新する場合、または**AWS Secret Access Key**と**AWS Role ARN**を切り替える場合は、この記事の前半で説明した選択した方式のIAMおよびAWS側のステップ（ポリシー、ユーザーまたはロール、必要に応じて識別子）を完了してください。

AWSで認証情報の準備が完了したら、Brazeで**パートナー連携** > **Currents**に移動し、リストからAmazon S3コネクタを見つけて**Edit**を選択し、**Credentials**を更新して**Update Current**を選択します。Brazeは入力された認証情報を検証します。コネクタは引き続き実行され、バケット内のデータは引き続き利用可能です。詳細については、[Currentsの設定でのCurrentsの更新]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents)を参照してください。

## エクスポートの動作 {#export-behavior}

クラウドデータストレージソリューションを統合し、API、ダッシュボードレポート、またはCSVレポートをエクスポートしているユーザーは、以下のような動作になります。

- すべてのAPIエクスポートは、レスポンスボディにダウンロードURLを返さず、データストレージを通じて取得する必要があります。
- すべてのダッシュボードレポートとCSVレポートは、ユーザーのメールに送信されてダウンロードされ（ストレージ権限不要）、データストレージにバックアップされます。

### `Unable to connect to S3, please validate that your credentials are correct`エラー {#unable-to-connect-to-s3-please-validate-that-your-credentials-are-correct-error}

CSVエクスポートのダウンロード時にこのエラーが表示された場合は、**テクノロジーパートナー**ページで[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)統合を開き、**Test Credentials**を選択してください。結果には検証に失敗した内容が表示されます。例えば、キーに`GetObject`権限がないため、Brazeがダウンロードリンクを生成できない場合があります。

IAMポリシーを更新して、統合ユーザーまたはロールがBraze統合で設定されたS3バケットとオブジェクトパスに対して`s3:GetObject`を呼び出せるようにしてください。エクスポートに関するその他の問題については、[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)を参照してください。

{% alert important %}
**JSONフォーマットの要件：**JSONエクスポートでは、BrazeはJSONL（改行区切りのJSON）フォーマットを使用し、各行に個別のJSONオブジェクトが含まれます。このフォーマットは、単一のJSON配列またはオブジェクトである標準的なJSONとは異なります。エクスポートされたファイルの各行は有効なJSONオブジェクトですが、ファイル全体としては1つの有効なJSONドキュメントではありません。これらのファイルを処理する際は、ファイル全体を1つのJSONドキュメントとしてパースするのではなく、各行を個別のJSONオブジェクトとしてパースしてください。

Currentsのエクスポートは、JSONではなくApache Avroフォーマット（`.avro`ファイル）を使用します。このJSONフォーマットの要件は、ダッシュボードデータエクスポートとAPIエクスポートに適用されます。
{% endalert %}

## 複数のコネクター {#multiple-connectors}

S3バケットに送信するCurrentsコネクタを複数作成する場合は、同じ認証情報を使用できますが、それぞれに異なるフォルダーパスを指定する必要があります。同じワークスペースで作成することも、複数のワークスペースに分割して作成することもできます。また、統合ごとに1つのポリシーを作成するか、両方の統合をカバーする1つのポリシーを作成するかを選択できます。

Currentsとデータエクスポートの両方に同じS3バケットを使用する場合は、それぞれの統合に異なる権限が必要なため、2つの別々のポリシーを作成する必要があります。

## トラブルシューティング {#troubleshooting}

### エラー:アカウントに`PutObject`アクセスがありません {#error-account-does-not-have-putobject-access}

ダッシュボードデータエクスポート用のAmazon S3認証情報を保存する際に以下のエラーが表示された場合、権限の設定が正しくないか、サーバーサイド暗号化の設定に問題がある可能性があります。

```
S3 Credentials are invalid because this account does not have 'PutObject access'. Please check the permissions and ensure that this key has access to 'PutObject' in the 'CUSTOMER-BUCKET-HERE' bucket.
```

この問題を解決するには、以下の点を確認してください。

#### バケットポリシーが正しくない {#incorrect-bucket-policy}

[Amazon S3統合](#integration)で説明されている正しい権限でポリシーを作成したことを確認してください（認証方式に応じた**Dashboard Data Export**ポリシーを使用してください）。

#### サーバーサイド暗号化 {#server-side-encryption}

```
User: arn:aws:sts::XXX:assumed-role/braze-iam-role/braze is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:XXX because no identity-based policy allows the kms:GenerateDataKey action
```

[Brazeサポート]({{site.baseurl}}/braze_support)またはAWSログでこのエラーメッセージが表示された場合、S3バケットがAWS Key Management Service（SSE-KMS）暗号化で設定されています。BrazeはCurrentsやダッシュボードデータエクスポートでSSE-KMSをサポートしていません。この問題を解決するには、S3バケットでSSE-KMSを無効にしてください。

{% alert note %}
BrazeはS3マネージドキーによるサーバーサイド暗号化（SSE-S3）をサポートしており、Currentsとダッシュボードデータエクスポートの両方と互換性があります。
{% endalert %}

#### 追加の権限を確認する {#check-additional-permissions}

`s3:GetBucketLocation`や`s3:PutObject`など、必要な権限があることを確認してください。