---
nav_title: セキュリティイベントのS3エクスポート
article_title: S3 でのセキュリティ設定のエクスポート
page_order: 1
page_type: reference
description: "この参照記事では、UTC の午前0時にセキュリティイベントを毎日 Amazon S3 に自動的にエクスポートする方法について説明します。"
---

# Amazon S3 でのセキュリティイベントのエクスポート

> セキュリティイベントをクラウドストレージプロバイダーである Amazon S3 に自動的にエクスポートできます。このエクスポートは UTC の深夜0時に実行される日次ジョブで処理されます。設定後は、ダッシュボードからセキュリティイベントを手動でエクスポートする必要はありません。このジョブは、過去24時間のセキュリティイベントを CSV 形式で、設定済みの S3 ストレージにエクスポートします。CSV ファイルは手動でエクスポートしたレポートと同じ構造を持っています。

{% alert note %}
10,000行の制限は、ダッシュボードからの手動 CSV レポートダウンロードにのみ適用されます。セキュリティイベントの S3 へのエクスポートは、この行数制限の対象外です。
{% endalert %}

Braze は、Amazon S3 エクスポートを設定するための 2 つの異なる S3 認証および許可方法をサポートしています。

- AWS シークレットアクセスキー方式
- AWS ロール ARN メソッド

## AWS シークレットアクセスキー方式

この方法では、シークレットキーとアクセスキー ID を生成します。これにより、Braze は AWS アカウントでユーザーとして認証し、バケットにデータを書き込むことができます。

### ステップ 1: アイデンティティとアクセス管理（IAM）ユーザーを作成する

シークレットアクセスキーとアクセスキー ID を取得するには、[AWS アカウントの設定](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin)手順に従って IAM ユーザーを作成する必要があります。

### ステップ 2: 認証情報を取得する

1. 新しいユーザーを作成した後、アクセスキーを生成し、アクセスキー ID とシークレットアクセスキーをダウンロードします。

![「liyu-chen-test」というロールの概要ページ。]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2. これらの認証情報は、後で Braze に入力する必要があるため、どこかにメモしておくか、認証情報ファイルをダウンロードしてください。

![アクセスキーとシークレットアクセスキーを含むフィールド。]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### ステップ 3: ポリシーの作成

1. **IAM**（Identity and Access Management）> **ポリシー** > **ポリシーの作成**に進み、ユーザーへの権限を追加します。
2. **Create Your Own Policy** を選択します。これにより、Braze は指定されたバケットにのみアクセスできるように制限された権限が与えられます。
3. 任意のポリシー名を指定します。
4. **ポリシードキュメント**セクションに以下のコードスニペットを入力します。「INSERTBUCKETNAME」を実際のバケット名に置き換えてください。これらの権限がないと、インテグレーションは認証情報チェックに失敗し、作成されません。

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

### ステップ 4: ポリシーのアタッチ

1. 新しいポリシーを作成した後、**Users** に移動し、対象のユーザーを選択します。
2. **Permissions** タブで **Add Permissions** を選択し、ポリシーを直接アタッチしてから、そのポリシーを選択します。

これで、AWS 認証情報を Braze アカウントにリンクする準備が整いました。

### ステップ 5: Braze を AWS にリンクする

1. Braze で、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動し、**セキュリティイベントのダウンロード**セクションまでスクロールします。
2. **クラウドストレージへのエクスポート**の下にある **Export to AWS S3** をオンに切り替え、**AWS secret access key** を選択して S3 エクスポートを有効にします。
3. 以下を入力します:
- AWS アクセスキー ID
- AWS シークレットアクセスキー
    - このキーを入力する際は、まず **Test Credentials** を選択して認証情報が正しく機能することを確認してください。
- AWS バケット名

![Braze アカウントと Braze external ID が入力された「セキュリティイベントのダウンロード」ページ。]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4. **変更内容を保存**を選択します。

![「変更内容を保存」ボタン。]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

AWS S3 が Braze アカウントに統合されました。

## AWS ロール ARN メソッド

AWS ロール ARN メソッドは、ロール Amazon リソースネーム（ARN）を生成し、Braze の Amazon アカウントがそのロールのメンバーとして認証できるようにします。

### ステップ 1: ポリシーの作成

1. アカウント管理者として AWS マネジメントコンソールにサインインします。
2. AWS コンソールで、**IAM**（Identity and Access Management）セクション > **ポリシー**に移動し、**ポリシーの作成**を選択します。

![ポリシーの一覧と「ポリシーの作成」ボタンがあるページ。]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3. **JSON** タブを開き、**ポリシードキュメント**セクションに以下のコードスニペットを入力します。`INSERTBUCKETNAME` を実際のバケット名に置き換えてください。

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
4. ポリシーを確認した後、**Next** を選択します。

![ポリシーを確認し、オプションで権限を追加できるページ。]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5. ポリシーに名前と説明を入力し、**Create Policy** を選択します。

![ポリシーを確認して作成するページ。]({% image_buster /assets/img/security_export/review_and_create.png %})

### ステップ 2: ロールの作成

1. Braze で、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動し、**セキュリティイベントのダウンロード**セクションまでスクロールします。
2. **AWS Role ARN** を選択します。
3. ロールの作成に必要な識別子、Braze アカウント ID、および Braze external ID をメモしておきます。

![Braze アカウントと Braze external ID が入力された「セキュリティイベントのダウンロード」ページ。]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. AWS コンソールで、**IAM**（Identity and Access Management）セクション > **ロール** > **ロールの作成**に移動します。
5. 信頼されたエンティティのセレクタータイプとして **Another AWS Account** を選択します。
6. Braze アカウント ID を入力し、**Require external ID** チェックボックスをオンにして、Braze external ID を入力します。
7. 完了したら **Next** を選択します。

![信頼されたエンティティタイプを選択し、AWS アカウントの情報を入力するオプションがあるページ。]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### ステップ 3: ポリシーのアタッチ

1. 検索バーで先ほど作成したポリシーを検索し、ポリシーの横にチェックマークを付けてアタッチします。
2. **Next** を選択します。

![タイプと説明の列を持つポリシーの一覧。]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3. ロールに名前と説明を入力し、**Create Role** を選択します。

![名前、説明、信頼ポリシー、権限、タグなどのロール詳細を入力するフィールド。]({% image_buster /assets/img/security_export/name_review_create.png %})

新しく作成されたロールが一覧に表示されます。

### ステップ 4: Braze AWS にリンクする

1. AWS コンソールで、一覧から新しく作成したロールを見つけます。名前を選択してロールの詳細を開き、**ARN** をメモしておきます。

![「security-event-export-olaf」というロールの概要ページ。]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2. Braze で、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動し、**セキュリティイベントのダウンロード**セクションまでスクロールします。

![「Export to AWS S3」のトグルがオンになっている「セキュリティイベントのダウンロード」セクション。]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3. **AWS role ARN** が選択されていることを確認し、指定されたフィールドにロール ARN と AWS S3 バケット名を入力します。
4. **Test Credentials** を選択して、認証情報が正しく機能することを確認します。
5. **変更内容を保存**を選択します。

![「変更内容を保存」ボタン。]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

AWS S3 が Braze アカウントに統合されました。