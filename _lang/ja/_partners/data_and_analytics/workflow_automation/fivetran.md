---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "このリファレンス記事では、BrazeとFivetranのパートナーシップについて説明しています。Fivetranは、クラウドウェアハウスにクエリ可能なデータを提供することで、データに基づいた意思決定を支援するワークフローオートメーションツールです。"
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/) は世界的に認知されたブランドであり、アナリストに焦点を当てた製品と完全に管理されたパイプラインにより、クエリ可能なデータをクラウドウェアハウスに配信してデータに基づく意思決定を可能にします。

BrazeとFivetranの統合により、ユーザーはメンテナンス不要のパイプラインを作成できます。このパイプラインにより、すべてのアプリケーションとデータベースを中央のウェアハウスに接続することで、Brazeデータを収集・分析できます。中央ウェアハウスにデータが収集されると、データチームは好みのビジネスインテリジェンスツールを使って、Brazeのデータを効率的に調査できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Fivetranアカウント | このパートナーシップを利用するには、[Fivetran](https://fivetran.com/login?next=%2Fdashboard)アカウントが必要です。 |
| Braze REST APIキー | 以下の権限を持つBraze REST APIキー：<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> これは、Brazeダッシュボードの**設定** > **APIキー**で作成できます。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは、[BrazeインスタンスのURL]({{site.baseurl}}/api/basics/#api-definitions)によって異なります。 |
| Braze Currents | [Braze Currents](https://www.braze.com/product/data-agility-management/currents/)はAmazon S3またはGoogle Cloud Storageのいずれかに接続する必要があります。 |
| Amazon S3またはGoogle Cloud Storage | この統合では、1つのAmazon S3またはGoogle Cloud Storageにアクセスできる必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

次のCurrents統合は、[Amazon S3](#setting-up-braze-currents-for-s3)および[Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage)の両方でサポートされています。

### S3向けのBraze Currentsの設定 {#setting-up-braze-currents-for-s3}

#### ステップ1：external IDを確認する {#step-one}

[Fivetranダッシュボード](https://fivetran.com/dashboard)で、**+ Connector**を選択し、次に**Braze**コネクターを選択して設定フォームを起動します。次に、**Amazon S3**を選択します。ここに表示されるexternal IDをメモしてください。FivetranがS3バケットにアクセスできるようにするために必要です。

![Fivetranの Braze コネクター設定フォーム。このステップに必要なexternal IDフィールドは、ページ中央の薄いグレーのボックスにあります。]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### ステップ2：指定されたS3バケットへのアクセス権をFivetranに付与する {#step-2-give-fivetran-access-to-a-specified-s3-bucket}

##### IAMポリシーの作成 {#creating-an-iam-policy}

[Amazon IAMコンソール](https://console.aws.amazon.com/iam/home#home)を開き、**Policies > Create Policy**に移動します。

![ポリシーの一覧が表示されたAmazon IAMコンソール。]({% image_buster /assets/img/fivetran_as3_iam.png %})

次に、**JSON**タブを開き、以下のポリシーを貼り付けます。`{your-bucket-name}` をS3バケットの名前に置き換えてください。

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

最後に、**Review Policy**を選択し、ポリシーに一意の名前と説明を入力します。**Create Policy**を選択して、ポリシーを作成します。

![ポリシーの名前と説明を入力するフィールド。]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### IAMロールを作成する {#step-two}

AWSで、**Roles**に移動し、**Create New Role**を選択します。

![新しいロールを作成するボタンがある「Roles」ページ。]({% image_buster /assets/img/fivetran_iam_new_role.png %})

**Another AWS Account**を選択し、FivetranアカウントID `834469178297` を入力します。必ず**Require external ID**チェックボックスをオンにしてください。ここでは、ステップ1で確認したexternal IDを入力します。

![「Account ID」を入力するフィールド、external IDを要求するチェックボックス、「External ID」を入力する空白のテキストボックス。]({% image_buster /assets/img/fivetran_another_aws_account.png %})

次に、**Next: Permissions**を選択して、先ほど作成したポリシーを選択します。

![ポリシーのリスト。]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

**Next: Review**を選択し、新しいロールに名前（Fivetranなど）を付け、**Create Role**を選択します。ロールが作成されたら、それを選択し、表示されているRole ARNをメモしておきます。

![ロールに記載されているAmazon S3のARN。]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Fivetranに指定するRole ARNの権限を指定できます。このロールに選択的な権限を付与すると、Fivetranは参照する権限を持つもののみを同期できます。
{% endalert %}

#### ステップ3：Fivetranコネクターの設定を完了する {#step-3-complete-the-fivetran-connector}

Fivetranで、**+ Connector**を選択し、次に**Braze**コネクターを選択して設定フォームを起動します。フォーム内で、指定されたフィールドに適切な値を入力してください：
- `Destination schema`：一意のスキーマ名。
- `API URL`：Braze REST APIエンドポイント。
- `API Key`：Braze REST APIキー。
- `External ID`：Currentsセットアップ手順の[ステップ2](#step-two)で設定されたexternal ID。このIDは固定値です。
- `Bucket`：Brazeアカウントで、**パートナー連携** > **データのエクスポート** > 利用しているCurrent名の順に移動して確認します。
- `Role ARN`：Currentセットアップ手順の[ステップ1](#step-one)でRole ARNを確認できます。

{% alert important %}
**Amazon S3**が**Cloud Storage**の選択肢として選ばれていることを確認してください。
{% endalert %}

最後に、**Save & Test**を選択すると、FivetranがBrazeアカウントのデータと同期して残りの作業を行います。

### Google Cloud Storage向けのBraze Currentsの設定 {#setting-up-braze-currents-for-google-cloud-storage}

#### ステップ1：Google Cloud StorageからFivetranメールアドレスを取得する {#step-one2}

[Fivetranダッシュボード](https://fivetran.com/dashboard)で、**+ Connector**を選択し、次に**Braze**コネクターを選択して設定フォームを起動します。次に、**Google Cloud Storage**を選択します。表示されるメールアドレスをメモしてください。

![Fivetranの Braze コネクター設定フォーム。このステップに必要なメールフィールドは、ページ中央の薄いグレーのボックスにあります。]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### ステップ2：バケットアクセスを許可する {#step-2-grant-bucket-access}

[Google Storage Console](https://console.cloud.google.com/storage/browser)に移動し、Braze Currentsを設定したバケットを選択して、**Edit bucket permissions**を選択します。

![Google Storage Consoleで利用可能なバケット。バケットを見つけ、縦に並んだ3つの点のアイコンを選択すると、バケットの権限を編集するためのドロップダウンが開きます。]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

次に、[ステップ1](#step-one2)のメールアドレスに `Storage Object Viewer` アクセス権を付与するため、メールアドレスをメンバーとして追加します。バケット名をメモしておいてください。次のステップでFivetranを設定するときに必要となります。

![権限付きバケット。]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### ステップ3：Fivetranコネクターの設定を完了する

Fivetranで、**+ Connector**を選択し、次に**Braze**コネクターを選択して設定フォームを起動します。フォーム内で、指定されたフィールドに適切な値を入力してください：
- `Destination schema`：一意のスキーマ名。
- `API URL`：Braze REST APIエンドポイント。
- `API Key`：Braze REST APIキー。
- `Bucket Name`：Brazeアカウントで、**パートナー連携** > **データのエクスポート** > 利用しているCurrent名の順に移動して確認します。
- `Folder`：Brazeアカウントで、**パートナー連携** > **データのエクスポート** > 利用しているCurrent名の順に移動して確認します。

{% alert important %}
**Google Cloud Storage**が**Cloud Storage**の選択肢として選択されていることを確認してください。
{% endalert %}

最後に、**Save & Test**を選択すると、FivetranがBrazeアカウントのデータと同期して残りの作業を行います。