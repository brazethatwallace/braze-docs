---
nav_title: セキュリティイベントのS3エクスポート
article_title: S3でのセキュリティ設定のエクスポート
page_order: 1
page_type: reference
description: "この参照記事では、UTCの午前0時にセキュリティイベントを毎日Amazon S3に自動的にエクスポートする方法について説明します。"
---

# Amazon S3でのセキュリティイベントのエクスポート {#security-events-export-with-amazon-s3}

> セキュリティイベントをクラウドストレージプロバイダーであるAmazon S3に自動的にエクスポートできます。このエクスポートはUTCの深夜0時に実行される日次ジョブで処理されます。設定後は、ダッシュボードからセキュリティイベントを手動でエクスポートする必要はありません。このジョブは、過去24時間のセキュリティイベントをCSV形式で、設定済みのS3ストレージにエクスポートします。CSVファイルは手動でエクスポートしたレポートと同じ列に加え、`Version`列を使用します。

{% alert note %}
10,000行の制限は、ダッシュボードからの手動CSVレポートダウンロードにのみ適用されます。セキュリティイベントのS3へのエクスポートは、この行数制限の対象外です。
{% endalert %}

Brazeは、Amazon S3エクスポートを設定するための2つの異なるS3認証および許可方法をサポートしています。

- AWSシークレットアクセスキー方式
- AWSロールARN方式

## AWSシークレットアクセスキー方式 {#aws-secret-access-key-method}

この方式では、シークレットキーとアクセスキーIDを生成します。これにより、BrazeはAWSアカウントでユーザーとして認証し、バケットにデータを書き込むことができます。

### ステップ1:アイデンティティとアクセス管理（IAM）ユーザーを作成する {#step-1-create-an-identity-and-access-management-iam-user}

シークレットアクセスキーとアクセスキーIDを取得するには、[AWSアカウントの設定](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin)の手順に従ってIAMユーザーを作成する必要があります。

### ステップ2:認証情報を取得する {#step-2-get-credentials}

1. 新しいユーザーを作成した後、アクセスキーを生成し、アクセスキーIDとシークレットアクセスキーをダウンロードします。

![「liyu-chen-test」というロールの概要ページ。]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2. これらの認証情報は、後でBrazeに入力する必要があるため、どこかにメモしておくか、認証情報ファイルをダウンロードしてください。

![アクセスキーとシークレットアクセスキーを含むフィールド。]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### ステップ3:ポリシーの作成 {#step-3-create-policy}

1. **IAM**（Identity and Access Management）> **Policies** > **Create Policy**に進み、ユーザーへの権限を追加します。
2. **Create Your Own Policy**を選択します。これにより、Brazeは指定されたバケットにのみアクセスできるように制限された権限が与えられます。
3. 任意のポリシー名を指定します。
4. **Policy Document**セクションに以下のコードスニペットを入力します。「INSERTBUCKETNAME」を実際のバケット名に置き換えてください。これらの権限がないと、インテグレーションは認証情報チェックに失敗し、作成されません。

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

### ステップ4:ポリシーのアタッチ {#step-4-attach-policy}

1. 新しいポリシーを作成した後、**Users**に移動し、対象のユーザーを選択します。
2. **Permissions**タブで**Add Permissions**を選択し、ポリシーを直接アタッチしてから、そのポリシーを選択します。

これで、AWS認証情報をBrazeアカウントにリンクする準備が整いました。

### ステップ5:BrazeをAWSにリンクする {#step-5-link-braze-to-aws}

1. Brazeで、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動し、**セキュリティイベントのダウンロード**セクションまでスクロールします。
2. **クラウドストレージへのエクスポート**の下にある**Export to AWS S3**をオンに切り替え、**AWS secret access key**を選択してS3エクスポートを有効にします。
3. 以下を入力します:

- AWSアクセスキーID
- AWSバケット名
- AWSシークレットアクセスキー
    - このキーを入力する際は、まず**Test Credentials**を選択して認証情報が正しく機能することを確認してください。

![BrazeアカウントとBraze external IDが入力された「セキュリティイベントのダウンロード」ページ。]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4. **変更内容を保存**を選択します。

AWS S3がBrazeアカウントに統合されました。

## AWSロールARN方式 {#aws-role-arn-method}

AWSロールARN方式は、ロールAmazonリソースネーム（ARN）を生成し、BrazeのAmazonアカウントがそのロールのメンバーとして認証できるようにします。

### ステップ1:ポリシーの作成 {#step-1-create-policy}

1. アカウント管理者としてAWSマネジメントコンソールにサインインします。
2. AWSコンソールで、**IAM**（Identity and Access Management）セクション > **Policies**に移動し、**Create Policy**を選択します。

![ポリシーの一覧と「Create policy」ボタンがあるページ。]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3. **JSON**タブを開き、**Policy Document**セクションに以下のコードスニペットを入力します。`INSERTBUCKETNAME`を実際のバケット名に置き換えてください。

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

{: start="4"}
4. ポリシーを確認した後、**Next**を選択します。

![ポリシーを確認し、オプションで権限を追加できるページ。]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5. ポリシーに名前と説明を入力し、**Create Policy**を選択します。

![ポリシーを確認して作成するページ。]({% image_buster /assets/img/security_export/review_and_create.png %})

### ステップ2:ロールの作成 {#step-2-create-role}

1. Brazeで、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動し、**セキュリティイベントのダウンロード**セクションまでスクロールします。
2. **AWS Role ARN**を選択します。
3. ロールの作成に必要な識別子、BrazeアカウントID、およびBraze external IDをメモしておきます。

![BrazeアカウントとBraze external IDが入力された「セキュリティイベントのダウンロード」ページ。]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. AWSコンソールで、**IAM**（Identity and Access Management）セクション > **Roles** > **Create Role**に移動します。
5. 信頼されたエンティティのセレクタータイプとして**Another AWS Account**を選択します。
6. BrazeアカウントIDを入力し、**Require external ID**チェックボックスをオンにして、Braze external IDを入力します。
7. 完了したら**Next**を選択します。

![信頼されたエンティティタイプを選択し、AWSアカウントの情報を入力するオプションがあるページ。]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### ステップ3:ポリシーのアタッチ {#step-3-attach-policy}

1. 検索バーで先ほど作成したポリシーを検索し、ポリシーの横にチェックマークを付けてアタッチします。
2. **Next**を選択します。

![タイプと説明の列を持つポリシーの一覧。]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3. ロールに名前と説明を入力し、**Create Role**を選択します。

![名前、説明、信頼ポリシー、権限、タグなどのロール詳細を入力するフィールド。]({% image_buster /assets/img/security_export/name_review_create.png %})

新しく作成されたロールが一覧に表示されます。

### ステップ4:Braze AWSにリンクする {#step-4-link-to-braze-aws}

1. AWSコンソールで、一覧から新しく作成したロールを見つけます。名前を選択してロールの詳細を開き、**ARN**をメモしておきます。

![「security-event-export-olaf」というロールの概要ページ。]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2. Brazeで、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動し、**セキュリティイベントのダウンロード**セクションまでスクロールします。

![「Export to AWS S3」のトグルがオンになっている「セキュリティイベントのダウンロード」セクション。]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3. **AWS role ARN**が選択されていることを確認し、指定されたフィールドにロールARNとAWS S3バケット名を入力します。
4. **Test Credentials**を選択して、認証情報が正しく機能することを確認します。
5. **変更内容を保存**を選択します。

AWS S3がBrazeアカウントに統合されました。