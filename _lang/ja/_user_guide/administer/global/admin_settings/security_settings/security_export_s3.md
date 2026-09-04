---
nav_title: セキュリティイベントのS3エクスポート
article_title: S3でのセキュリティ設定のエクスポート
page_order: 1
page_type: reference
description: "この参照記事では、UTCの午前0時にセキュリティイベントを毎日Amazon S3に自動的にエクスポートする方法について説明します。"
---

# Amazon S3でのセキュリティイベントのエクスポート {#security-events-export-with-amazon-s3}

> セキュリティイベントをクラウドストレージプロバイダーであるAmazon S3に自動的にエクスポートできます。このエクスポートはUTCの深夜0時に実行される日次ジョブで処理されます。設定後は、ダッシュボードからセキュリティイベントを手動でエクスポートする必要はありません。このジョブは、過去24時間のセキュリティイベントをCSV形式で、設定済みのS3ストレージにエクスポートします。CSVファイルは手動でエクスポートしたレポートと同じ列に加え、`Version`列を使用します。

{% alert important %}
Amazon S3でのセキュリティイベントのエクスポートの利用可否は、プラットフォームのエディションによって異なります。この機能がワークスペースにない場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

Brazeは、Amazon S3エクスポートを設定するための2つの異なるS3認証および許可方法をサポートしています。

- AWSシークレットアクセスキー方式
- AWSロールARN方式

{% alert note %}
S3へのセキュリティイベントのエクスポートは、ダッシュボードからの手動CSVレポートダウンロードに適用される10,000行の制限の対象外です。
{% endalert %}

## AWSシークレットアクセスキー方式 {#aws-secret-access-key-method}

この方式では、シークレットキーとアクセスキーIDを生成し、BrazeがAWSアカウント上のユーザーとして認証を行い、バケットにデータを書き込めるようにします。

### ステップ1:Identity and Access Management（IAM）ユーザーを作成する {#step-1-create-an-identity-and-access-management-iam-user}

シークレットアクセスキーとアクセスキーIDを取得するには、[AWSアカウントのセットアップ](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin)の手順に従ってIAMユーザーを作成する必要があります。

### ステップ2:認証情報を取得する {#step-2-get-credentials}

1. 新しいユーザーを作成した後、アクセスキーを生成し、アクセスキーIDとシークレットアクセスキーをダウンロードします。

![「liyu-chen-test」というロールの概要ページ。]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2. これらの認証情報をメモするか認証情報ファイルをダウンロードしてください。後ほどBrazeに入力する必要があります。

![アクセスキーとシークレットアクセスキーを含むフィールド。]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### ステップ3:ポリシーを作成する {#step-3-create-policy}

1. **IAM**（Identity and Access Management）> **Policies** > **Create Policy** に移動して、ユーザーに権限を追加します。
2. **Create Your Own Policy** を選択します。これにより、Brazeが指定されたバケットにのみアクセスできるよう権限が制限されます。
3. 任意のポリシー名を指定します。
4. **Policy Document** セクションに以下のコードスニペットを入力します。「INSERTBUCKETNAME」を実際のバケット名に置き換えてください。これらの権限がないと、連携時の認証情報チェックに失敗し、作成されません。

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

### ステップ4:ポリシーをアタッチする {#step-4-attach-policy}

1. 新しいポリシーを作成した後、**Users** に移動して対象のユーザーを選択します。
2. **Permissions** タブで **Add Permissions** を選択し、ポリシーを直接アタッチしてから、該当のポリシーを選択します。

これでAWSの認証情報をBrazeアカウントにリンクする準備が整いました。

### ステップ5:BrazeをAWSにリンクする {#step-5-link-braze-to-aws}

1. Brazeで、**設定** > **会社設定** > **管理者設定** > **セキュリティ設定** に移動し、**セキュリティイベントダウンロード**セクションまでスクロールします。
2. **クラウドストレージへのエクスポート**の下にある **Export to AWS S3** をオンに切り替え、**AWSシークレットアクセスキー**を選択してS3エクスポートを有効にします。
3. 以下を入力します:

- AWSアクセスキーID
- AWSバケット名
- AWSシークレットアクセスキー
    - このキーを入力する際、まず**認証情報をテスト**を選択して認証情報が正しく機能することを確認してください。

![BrazeアカウントとBraze external IDが入力された「セキュリティイベントダウンロード」ページ。]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4. **変更を保存**を選択します。

AWS S3がBrazeアカウントに統合されました。

## AWS ロール ARN 方式 {#aws-role-arn-method}

AWS ロール ARN 方式では、ロール Amazon リソースネーム（ARN）を生成し、Braze の Amazon アカウントがそのロールのメンバーとして認証できるようにします。

### ステップ1:ポリシーを作成する {#step-1-create-policy}

1. AWS マネジメントコンソールにアカウント管理者としてサインインします。
2. AWS コンソールで、**IAM**（Identity and Access Management）セクション > **Policies** に移動し、**Create Policy** を選択します。

![ポリシーの一覧と「Create policy」ボタンが表示されたページ。]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3. **JSON** タブを開き、**Policy Document** セクションに以下のコードスニペットを入力します。`INSERTBUCKETNAME` はお使いのバケット名に置き換えてください。

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
4. ポリシーを確認したら、**Next** を選択します。

![ポリシーを確認し、オプションで権限を追加できるページ。]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5. ポリシーに名前と説明を入力し、**Create Policy** を選択します。

![ポリシーを確認して作成するページ。]({% image_buster /assets/img/security_export/review_and_create.png %})

### ステップ2:ロールを作成する {#step-2-create-role}

1. Braze で、**設定** > **会社設定** > **管理者設定** > **セキュリティ設定** に移動し、**セキュリティイベントダウンロード** セクションまでスクロールします。
2. **AWS Role ARN** を選択します。
3. ロールの作成に必要な識別子（Braze アカウント ID と Braze external ID）を控えておきます。

![Braze アカウント ID と Braze external ID が表示された「セキュリティイベントダウンロード」ページ。]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. AWS コンソールで、**IAM**（Identity and Access Management）セクション > **Roles** > **Create Role** に移動します。
5. 信頼されるエンティティの選択タイプとして **Another AWS Account** を選択します。
6. Braze アカウント ID を入力し、**Require external ID** チェックボックスにチェックを入れて、Braze external ID を入力します。
7. 完了したら **Next** を選択します。

![信頼されるエンティティタイプを選択し、AWS アカウントの情報を入力するオプションがあるページ。]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### ステップ3:ポリシーをアタッチする {#step-3-attach-policy}

1. 検索バーで先ほど作成したポリシーを検索し、ポリシーの横にチェックマークを付けてアタッチします。
2. **Next** を選択します。

![タイプと説明の列があるポリシーの一覧。]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3. ロールに名前と説明を入力し、**Create Role** を選択します。

![名前、説明、信頼ポリシー、権限、タグなどのロール詳細を入力するフィールド。]({% image_buster /assets/img/security_export/name_review_create.png %})

新しく作成されたロールが一覧に表示されます。

### ステップ4:Braze AWS にリンクする {#step-4-link-to-braze-aws}

1. AWS コンソールで、一覧から新しく作成したロールを見つけます。名前を選択してそのロールの詳細を開き、**ARN** を控えておきます。

![「security-event-export-olaf」というロールのサマリーページ。]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2. Braze で、**設定** > **会社設定** > **管理者設定** > **セキュリティ設定** に移動し、**セキュリティイベントダウンロード** セクションまでスクロールします。

![「AWS S3 にエクスポート」のトグルがオンになった「セキュリティイベントダウンロード」セクション。]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3. **AWS role ARN** が選択されていることを確認し、指定のフィールドにロール ARN と AWS S3 バケット名を入力します。
4. **Test Credentials** を選択して、認証情報が正しく機能することを確認します。
5. **Save Changes** を選択します。

AWS S3 と Braze アカウントの統合が完了しました。