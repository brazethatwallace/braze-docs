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

| 要件 | 説明 |
| ----------- | ----------- |
| Amazon S3 アカウント | このパートナーシップを利用するには、Amazon S3 アカウントが必要です。 |
| 専用 S3 バケット | Amazon S3 と連携する前に、アプリ用の S3 バケットを作成する必要があります。<br><br>すでに S3 バケットをお持ちの場合でも、権限を制限できるよう、Braze 専用の新しいバケットを作成することをお勧めします。新しいバケットの作成方法については、以下の手順を参照してください。 |
| Currents | データを Amazon S3 にエクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) を設定する必要があります。メッセージアーカイブの設定のみを行う場合、Currentsは必要ありません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 新しい S3 バケットの作成 {#creating-a-new-s3-bucket}

アプリ用のバケットを作成するには、以下の手順に従ってください。

1. [Amazon S3 コンソール](https://console.aws.amazon.com/s3/)を開き、指示に従って**サインイン**するか、**AWS のアカウントを作成**します。
2. サインイン後、**Storage & Content Delivery** カテゴリから **S3** を選択します。
3. 次の画面で **Create Bucket** を選択します。
4. プロンプトが表示されたら、バケットを作成し、AWS リージョンを選択します。

Braze では、ダッシュボードでリージョンを選択または設定することはできません。AWS リージョンは、AWS コンソールでバケットを作成した場所によって固定されます。連携では、指定したバケット名にデータを送信し、AWS がバケットのリージョンにリクエストを自動的にルーティングします。コネクターが希望と異なるリージョン（たとえば `eu-central-1` ではなく `eu-west-1`）に接続しようとする場合は、AWS で希望するリージョンに S3 バケットを作成するか、そのリージョンの既存バケットを使用してください。Braze 側で変更する項目はありません。

{% alert note %}
Currentsは、[Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) が設定されたバケットをサポートしていません。
{% endalert %}

## 連携 {#integration}

Brazeには、Amazon S3との連携戦略が2つあります。1つは[Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)用、もう1つはすべてのダッシュボードデータエクスポート（CSVエクスポートやエンゲージメントレポートなど）用です。どちらの連携も、2つの異なる認証方法をサポートしています。

- [AWSシークレットアクセスキー方式](#aws-secret-key-auth-method)
- [AWSロールARN方式](#aws-role-arn-auth-method)

## AWSシークレットキー認証方式 {#aws-secret-key-auth-method}

この認証方式ではシークレットキーとアクセスキーIDが生成され、BrazeがAWSアカウント上のユーザーとして認証を行い、バケットにデータを書き込めるようになります。

### ステップ1:ユーザーを作成する {#secret-key-1}

{% alert note %}
メッセージのアーカイブのみを設定する場合は、**ダッシュボードデータエクスポート**タブの手順に従ってください。
{% endalert %}

アクセスキーIDとシークレットアクセスキーを取得するには、[AWSでIAMユーザーと管理者グループを作成](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)してください。

### ステップ2:認証情報を取得する {#secret-key-2}

新しいユーザーを作成した後、**Show User Security Credentials**を選択してアクセスキーIDとシークレットアクセスキーを表示します。次に、これらの認証情報をメモするか、**Download Credentials**ボタンを選択してください。後でBrazeダッシュボードに入力する必要があります。

![アクセスキーIDとシークレットアクセスキーが表示されたAWS IAMユーザーセキュリティ認証情報ページ。]({% image_buster /assets/img_archive/S3_Credentials.png %})

### ステップ3:ポリシーを作成する {#secret-key-3}

**Policies** > **Get Started** > **Create Policy**に移動して、ユーザーにアクセス許可を追加します。次に、**Create Your Own Policy**を選択します。これにより権限が制限され、Brazeは指定されたバケットにのみアクセスできるようになります。

![S3連携のポリシーオプションが表示されたAWS IAMポリシー作成画面。]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Currentsとダッシュボードデータエクスポートでは異なるポリシーが必要です。`s3:GetObject`は、Brazeバックエンドでエラーハンドリングを行うために必要です。
{% endalert %}

任意のポリシー名を指定し、以下のコードスニペットを**Policy Document**セクションに入力します。`INSERTBUCKETNAME`をバケット名に置き換えてください。これらの権限がないと、連携の認証情報チェックに失敗し、作成されません。

{% alert note %}
メッセージのアーカイブのみを設定する場合は、**ダッシュボードデータエクスポート**タブのコードスニペットを使用してください。
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
{% tab ダッシュボードデータエクスポート %}
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

新しいポリシーを作成した後、**Users**に移動して特定のユーザーを選択します。**Permissions**タブで**Attach Policy**を選択し、作成した新しいポリシーを選択します。これで、AWSの認証情報をBrazeアカウントにリンクする準備が整いました。

![Attach Policyアクションが選択されたAWS IAMユーザーのPermissionsタブ。]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### ステップ5:BrazeをAWSにリンクする {#secret-key-5}

{% alert note %}
メッセージのアーカイブのみを設定する場合は、**ダッシュボードデータエクスポート**タブの手順に従ってください。
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Brazeで、**パートナー連携** > **Currents**に移動します。

次に、**Create New Current**を選択し、**Amazon S3 Data Export**を選択します。

Currentに名前を付けます。**Credentials**セクションで、**AWS Secret Access Key**が選択されていることを確認し、S3アクセスID、AWSシークレットアクセスキー、およびAWS S3バケット名を指定のフィールドに入力します。

{% multi_lang_include currents/contact_email_notifications.md %}

![AWSシークレットキー認証情報フィールドが表示されたBrazeのAmazon S3用Create New Currentフォーム。]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
AWSアクセスキーIDとシークレットアクセスキーを常に最新の状態に保ってください。コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止します。この状態が**5日間**以上続くと、コネクタのイベントはドロップされ、データが永久に失われます。
{% endalert %}

また、必要に応じて以下のカスタマイズを追加できます：

- **フォルダパス：**デフォルトは`currents`です。このフォルダが存在しない場合、Brazeが自動的に作成します。
- **サーバーサイドのAES-256保存時暗号化：**デフォルトはOFFで、`x-amz-server-side-encryption`ヘッダーが含まれます。

**Launch Current**を選択して続行します。

認証情報が正常に検証されたかどうかの通知が表示されます。これでAWS S3がBraze Currentsに設定されました。

{% endtab %}
{% tab ダッシュボードデータエクスポート %}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Amazon S3**を選択します。

**AWS Credentials**ページで、**AWS Secret Access Key**が選択されていることを確認し、AWSアクセスID、AWSシークレットアクセスキー、およびAWS S3バケット名を指定のフィールドに入力します。シークレットキーを入力する際は、まず**Test Credentials**を選択して認証情報が正しく機能することを確認し、成功したら**Save**を選択します。

![テストおよび保存アクションが表示されたBrazeのAmazon S3テクノロジーパートナー認証情報ページ。]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
ユーザーに移動し、AWSコンソール内の**Security Credentials**タブで**Create Access Key**を選択することで、いつでも新しい認証情報を取得できます。
{% endalert %}

認証情報が正常に検証されたかどうかの通知が表示されます。これでAWS S3がBrazeアカウントに統合されました。

{% endtab %}
{% endtabs %}

## AWS ロール ARN 認証方法 {#aws-role-arn-auth-method}

この認証方法では、ロール Amazon リソースネーム (ARN) を生成します。これにより、Braze の Amazon アカウントが、バケットにデータを書き込むために作成したロールのメンバーとして認証できるようになります。

### ステップ1:ポリシーの作成 {#role-arn-1}

まず、アカウント管理者として AWS マネジメントコンソールにサインインします。AWS コンソールの IAM セクションに移動し、ナビゲーションバーで **Policies** を選択し、**Create Policy** を選択します。

![「Create Policy」ボタンが選択された AWS IAM ポリシーページ。]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Currentsとダッシュボードデータエクスポートには異なるポリシーが必要です。`s3:GetObject` は、Braze バックエンドがエラーハンドリングを実行するために必要です。
{% endalert %}

**JSON** タブを開き、以下のコードスニペットを **Policy Document** セクションに入力します。`INSERTBUCKETNAME` は必ずご自身のバケット名に置き換えてください。完了したら **Review Policy** を選択します。

{% alert note %}
メッセージアーカイブのみを設定する場合は、**ダッシュボードデータエクスポート**タブのコードスニペットを使用してください。
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
{% tab ダッシュボードデータエクスポート %}

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

次に、ポリシーに名前と説明を付けて、**Create Policy** を選択します。

![ポリシー名と説明のフィールドが表示された AWS IAM ポリシーレビューステップ。]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![新しく作成された S3 ポリシーが表示された AWS IAM ポリシー一覧。]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### ステップ2:ロールの作成 {#role-arn-2}

コンソールの同じ IAM セクションで、**Roles** > **Create Role** を選択します。

![「Create Role」ボタンが選択された AWS IAM ロールページ。]({{site.baseurl}}/assets/img/create_role_1_list.png)

Braze アカウントから Braze アカウント ID と外部 ID を取得します:

- **Currents:** Brazeで、**パートナー連携** > **Currents** に移動します。次に、**Create New Current** を選択し、**Amazon S3 Data Export** を選択します。ここでロールの作成に必要な識別子を確認できます。
- **ダッシュボードデータエクスポート:** Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Amazon S3** を選択します。ここでロールの作成に必要な識別子を確認できます。（メッセージアーカイブのみを設定する場合は、ここでロールを作成してください。）

AWS コンソールに戻り、信頼されるエンティティの選択タイプとして **Another AWS Account** を選択します。Braze アカウント ID を入力し、**Require external ID** チェックボックスをオンにして、Braze の外部 ID を入力します。完了したら **Next** を選択します。

![S3 の「Create Role」ページ。ロール名、ロールの説明、信頼されるエンティティ、ポリシー、アクセス許可の境界のフィールドがあります。]({{site.baseurl}}/assets/img/create_role_2_another.png)

### ステップ3:ポリシーのアタッチ {#role-arn-3}

次に、先ほど作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横にチェックマークを入れてアタッチします。完了したら **Next** を選択します。

![ロール ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

ロールに名前と説明を付けて、**Create Role** を選択します。

![ロール ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

新しく作成されたロールが一覧に表示されます。

### ステップ4:Braze AWS へのリンク {#role-arn-4}

AWS コンソールで、一覧から新しく作成したロールを見つけます。名前を選択して、そのロールの詳細を開きます。

![新しく作成されたロールの AWS IAM ロール詳細ページ。]({{site.baseurl}}/assets/img/create_role_5_created.png)

ロール概要ページの上部にある **Role ARN** を確認してください。

![ロール ARN の値が表示された AWS IAM ロール概要。]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Braze アカウントに戻り、指定されたフィールドにロール ARN をコピーします。

{% alert note %}
メッセージアーカイブのみを設定する場合は、**ダッシュボードデータエクスポート**タブの手順に従ってください。
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Brazeで、**パートナー連携** > **Currents** に移動します。次に、**Create New Current** を選択し、**Amazon S3 Data Export** を選択します。

![AWS ロール ARN とバケットフィールドが表示された Braze Currents Amazon S3 設定画面。]({{site.baseurl}}/assets/img/currents-role-arn.png)

Current に名前を付けます。次に、**認証情報**セクションで **AWS Role ARN** が選択されていることを確認し、指定されたフィールドにロール ARN と AWS S3 バケット名を入力します。

{% multi_lang_include currents/contact_email_notifications.md %}

また、必要に応じて以下のカスタマイズを追加できます:

- フォルダーパス（デフォルトは `currents`）
- サーバーサイド保存時 AES-256 暗号化（デフォルトは OFF）- `x-amz-server-side-encryption` ヘッダーが含まれます

**Launch Current** を選択して続行します。認証情報が正常に検証されたかどうかを示す通知が表示されます。これで Braze Currentsに AWS S3 が設定されました。

{% alert important %}
「S3 credentials are invalid」エラーが表示された場合、AWS でロールを作成した直後に連携を行ったことが原因である可能性があります。しばらく待ってから再試行してください。メッセージに `PutObject` アクセスやダッシュボードデータエクスポートのサーバーサイド暗号化に関する内容が記載されている場合は、[S3 認証エラーのトラブルシューティング](#troubleshooting)を参照してください。
{% endalert %}

{% endtab %}
{% tab ダッシュボードデータエクスポート %}

Brazeで、**連携**の下にある**テクノロジーパートナー**ページに移動し、**Amazon S3** を選択します。

![AWS ロール ARN 認証情報が選択された Braze Amazon S3 テクノロジーパートナーページ。]({{site.baseurl}}/assets/img/data-export-role-arn.png)

**AWS Credentials** ページで、**AWS Role ARN** ラジオボタンが選択されていることを確認し、指定されたフィールドにロール ARN と AWS S3 バケット名を入力します。まず **Test Credentials** を選択して認証情報が正しく動作することを確認し、成功したら **Save** を選択します。

{% alert tip %}
いつでもユーザーに移動し、AWS コンソール内の **Security Credentials** タブで **Create Access Key** を選択することで、新しい認証情報を取得できます。
{% endalert %}

認証情報が正常に検証されたかどうかを通知でお知らせします。これで AWS S3 が Braze アカウントに統合されました。

{% endtab %}
{% endtabs %}

## Currents用のAmazon S3認証情報の更新 {#updating-currents-credentials}

既存のBraze Currentsコネクタで、統合を停止したり、すでにバケットにエクスポートされたデータを失ったりすることなく、Amazon S3認証情報を更新できます。

認証情報を更新する場合、または**AWS Secret Access Key**と**AWS Role ARN**を切り替える場合は、この記事の前半で説明した選択した方式のIAMおよびAWS側のステップ（ポリシー、ユーザーまたはロール、必要に応じて識別子）を完了してください。

AWSで認証情報の準備が完了したら、Brazeで**パートナー連携** > **Currents**に移動し、リストからAmazon S3コネクタを見つけて**Edit**を選択し、**Credentials**を更新して**Update Current**を選択します。Brazeは入力された認証情報を検証します。コネクタは引き続き実行され、バケット内のデータは引き続き利用可能です。詳細については、[Currentsの設定でのCurrentsの更新]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents)を参照してください。

## エクスポートの動作 {#export-behavior}

クラウドデータストレージソリューションとエクスポートAPI、ダッシュボードレポート、またはCSVレポートを統合したユーザーは、以下の動作が適用されます。

- すべてのAPIエクスポートでは、レスポンスボディにダウンロードURLが返されないため、データストレージから取得する必要があります。
- すべてのダッシュボードレポートとCSVレポートは、ダウンロード用にユーザーのメールに送信され（ストレージの権限は不要）、データストレージにバックアップされます。

### `Unable to connect to S3, please validate that your credentials are correct` エラー {#unable-to-connect-to-s3-please-validate-that-your-credentials-are-correct-error}

CSVエクスポートのダウンロード時にこのエラーが表示された場合は、**テクノロジーパートナー**ページで [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) 連携を開き、**認証情報をテスト**を選択してください。結果にはバリデーションに失敗した内容が表示されます。たとえば、キーに `GetObject` 権限がないため、Brazeがダウンロードリンクを生成できない場合があります。

IAMポリシーを更新して、連携ユーザーまたはロールがBraze連携で設定されたS3バケットとオブジェクトパスに対して `s3:GetObject` を呼び出せるようにしてください。その他のエクスポートの問題については、[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)を参照してください。

{% alert important %}
**JSON形式の要件：** JSONエクスポートでは、BrazeはJSONL（改行区切りJSON）形式を使用します。この形式では、各行に個別のJSONオブジェクトが含まれます。この形式は、単一のJSON配列またはオブジェクトで構成される標準的なJSONとは異なります。エクスポートされたファイルの各行は有効なJSONオブジェクトですが、ファイル全体としては単一の有効なJSONドキュメントではありません。これらのファイルを処理する際は、ファイル全体を単一のJSONドキュメントとして解析しようとせず、各行を個別のJSONオブジェクトとして解析してください。

Currentsのエクスポートでは、JSONではなくApache Avro形式（`.avro`ファイル）が使用されます。このJSON形式の要件は、ダッシュボードデータのエクスポートとAPIエクスポートに適用されます。
{% endalert %}

## 複数のコネクター {#multiple-connectors}

複数のCurrentsコネクターを作成してS3バケットにデータを送信する場合、同じ認証情報を使用できますが、各コネクターに異なるフォルダーパスを指定する必要があります。これらは同じワークスペース内で作成することも、分割して複数のワークスペースにまたがって作成することもできます。また、各連携ごとに個別のポリシーを作成するか、両方の連携をカバーする1つのポリシーを作成するかを選択できます。

同じS3バケットをCurrentsとデータエクスポートの両方に使用する場合は、各連携に異なる権限が必要なため、2つの別々のポリシーを作成する必要があります。

## トラブルシューティング {#troubleshooting}

### エラー: アカウントに `PutObject` アクセスがない {#error-account-does-not-have-putobject-access}

ダッシュボードのデータエクスポート用に Amazon S3 認証情報を保存する際に以下のエラーが表示される場合、権限の誤りまたはサーバー側の暗号化設定が原因である可能性があります。

```
S3 Credentials are invalid because this account does not have 'PutObject access'. Please check the permissions and ensure that this key has access to 'PutObject' in the 'CUSTOMER-BUCKET-HERE' bucket.
```

この問題を解決するには、以下の項目を確認してください。

#### バケットポリシーの誤り {#incorrect-bucket-policy}

[Amazon S3 連携](#integration)に記載されている正しい権限でポリシーを作成したことを確認してください（認証方法に合わせて**ダッシュボードデータエクスポート**ポリシーを使用してください）。

#### サーバー側の暗号化 {#server-side-encryption}

```
User: arn:aws:sts::XXX:assumed-role/braze-iam-role/braze is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:XXX because no identity-based policy allows the kms:GenerateDataKey action
```

このエラーメッセージを [Braze サポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)または AWS ログで受け取った場合、S3 バケットが AWS Key Management Service（SSE-KMS）暗号化で設定されています。Braze は Currents やダッシュボードのデータエクスポートで SSE-KMS をサポートしていません。この問題を解決するには、S3 バケットで SSE-KMS を無効にしてください。

{% alert note %}
Braze は S3 マネージドキーによるサーバー側暗号化（SSE-S3）をサポートしています。これは Currents とダッシュボードのデータエクスポートの両方に対応しています。
{% endalert %}

#### 追加の権限を確認する {#check-additional-permissions}

`s3:GetBucketLocation` および `s3:PutObject` を含む必要な権限があることを確認してください。