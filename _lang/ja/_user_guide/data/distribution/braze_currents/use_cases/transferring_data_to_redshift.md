---
nav_title: データをRedshiftに転送する
article_title: Redshift へのデータ転送
page_order: 8
page_type: tutorial
description: "このハウツー記事では、ETL（Extract, Transform, Load）プロセスを通じてAmazon S3からRedshiftにデータを転送する方法を説明します。"
tool: Currents

---

# データをRedshiftに転送する

> [Amazon Redshift](https://aws.amazon.com/redshift/) は、Amazon S3 と並んでAmazon Web Services 上で動作する、評判の良いデータウェアハウスです。Currents の Braze データは、Redshift への直接転送用に構造化されています。

以下では、ETL（Extract, Transform, Load）プロセスを通じて Amazon S3 から Redshift へデータを転送する方法を説明します。完全なソースコードについては、Currents のサンプル [GitHub リポジトリ](https://github.com/Appboy/currents-examples)を参照してください。

{% alert important %}
これは、最も有利な場所にデータを転送するという観点で、選択できる多くのオプションのうちの1つに過ぎません。
{% endalert %}

## S3 から Redshift へのローダーの概要

[`s3loader.py`](https://github.com/Appboy/currents-examples/tree/master/redshift-s3-loader) スクリプトは、同じ Redshift データベース内の別のマニフェストテーブルを使用して、既にコピーされたファイルのトラッキングを行います。全体的な構造は以下の通りです：

1. S3 内の全ファイルをリストアップし、前回 `s3loader.py` を実行した時点から追加された新規ファイルを、リストとマニフェストテーブルの内容を比較して識別します。
2. 新しいファイルを含む[マニフェスト](http://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html)ファイルを作成します。
3. マニフェストファイルを使用して、S3 から Redshift へ新しいファイルをコピーする `COPY` クエリを実行します。
4. コピーされたファイルの名前を Redshift の別のマニフェストテーブルに挿入します。
5. コミットします。

## 依存関係

ローダーを実行するには、AWS Python SDK と Psycopg をインストールする必要があります。

```bash
pip install boto3
pip install psycopg2
```

## 権限

### S3 への読み取りアクセス権を持つ Redshift ロール

まだ行っていない場合は、[AWS のドキュメント](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html)に従って、S3 上のファイルに対して `COPY` コマンドを実行できるロールを作成してください。

### Redshift VPC の受信ルール

Redshift クラスターが VPC 内にある場合、S3 ローダーを実行しているサーバーからの接続を許可するように VPC を設定する必要があります。Redshift クラスターに移動し、ローダーが接続する VPC セキュリティグループのエントリを選択します。次に、新しい受信ルールを追加します：**Type** = Redshift、**Protocol** = TCP、**Port** = クラスターのポート、**Source** = ローダーを実行しているサーバーの IP（テスト用には「Anywhere」）。

### S3 フルアクセス権を持つ Identity and Access Management（IAM）ユーザー

S3 ローダーには、Currents データを含むファイルへの読み取りアクセスと、Redshift の `COPY` コマンド用に生成するマニフェストファイルの保存場所へのフルアクセスが必要です。[IAM コンソール](https://console.aws.amazon.com/iam/home#/users)から `AmazonS3FullAccess` 権限を持つ新しい Identity and Access Management（IAM）ユーザーを作成してください。認証情報はローダーに渡す必要があるため、保存しておいてください。

アクセス認証情報は、環境変数、共有認証情報ファイル（`~/.aws/credentials`）、または [AWS 設定ファイル](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials)を通じてローダーに渡すことができます。あるいは、`S3LoadJob` オブジェクト内の `aws_access_key_id` および `aws_secret_access_key` フィールドに直接割り当てることでローダーに含めることもできますが、ソースコード内に認証情報をハードコーディングすることは推奨しません。

## 使用方法

### 使用例

以下のサンプルプログラムは、`users.messages.contentcard.Impression` イベントのデータを S3 から Redshift の `content_card_impression` テーブルに読み込みます。

```
if __name__ == '__main__':
    host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
    port = 5439
    database = '{YOUR_DATABASE}'
    user = '{YOUR_USER}'
    password = '{YOUR_PASSWORD}'
    role = '{YOUR_REDSHIFT_ROLE_ARN}'

    # Do not hard code these credentials.
    aws_access_key_id = None
    aws_secret_access_key = None

    # Content Card Impression Avro fields:
    #   id            - string
    #   user_id       - string
    #   external_user_id - string (nullable)
    #   app_id        - string
    #   content_card_id  - string
    #   campaign_id   - string (nullable)
    #   send_id       - string (nullable)
    #   time          - int
    #   platform      - string (nullable)
    #   device_model  - string (nullable)

    print('Loading Content Card Impression...')
    cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
    cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
    cc_impression_redshift_table = 'content_card_impression'
    cc_impression_redshift_column_def = [
        ('id', 'text'),
        ('user_id', 'text'),
        ('external_user_id', 'text'),
        ('app_id', 'text'),
        ('content_card_id', 'text'),
        ('campaign_id', 'text'),
        ('send_id', 'text'),
        ('time', 'integer'),
        ('platform', 'text'),
        ('device_model', 'text')
    ]

    cc_impression_redshift = RedshiftEndpoint(host, port, database, user, password,
        cc_impression_redshift_table, cc_impression_redshift_column_def)
    cc_impression_s3 = S3Endpoint(cc_impression_s3_bucket, cc_impression_s3_prefix)

    cc_impression_job = S3LoadJob(cc_impression_redshift, cc_impression_s3, role,
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    cc_impression_job.perform()
```

### 認証情報

ローダーを実行するには、まず Redshift クラスターの `host`、`port`、`database`、および `COPY` クエリを実行できる Redshift ユーザーの `user` と `password` を指定する必要があります。さらに、前のセクションで作成した S3 読み取りアクセス権を持つ Redshift ロールの ARN を指定する必要があります。

```
host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
port = 5439
database = '{YOUR_DATABASE}'
user = '{YOUR_USER}'
password = '{YOUR_PASSWORD}'
role = '{YOUR_REDSHIFT_ROLE_ARN}'
```

### ジョブの設定

イベントファイルの S3 バケットとプレフィックス、および `COPY` 先の Redshift テーブル名を指定する必要があります。

また、ローダーが必要とする「auto」オプションで Avro ファイルを `COPY` するには、Redshift テーブルのカラム定義が、サンプルプログラムに示されているように Avro スキーマのフィールド名と一致し、適切な型マッピング（例：`string` → `text`、`int` → `integer`）が行われている必要があります。

すべてのファイルを一度にコピーするのに時間がかかりすぎる場合は、ローダーに `batch_size` オプションを渡すこともできます。`batch_size` を渡すと、ローダーはすべてを同時にコピーする必要なく、一度に1バッチずつインクリメンタルにコピーしてコミットできます。1バッチの読み込みにかかる時間は、`batch_size`、ファイルのサイズ、および Redshift クラスターのサイズによって異なります。

```
# Content Card Impression Avro fields:
#   id            - string
#   user_id       - string
#   external_user_id - string (nullable)
#   app_id        - string
#   content_card_id  - string
#   campaign_id   - string (nullable)
#   send_id       - string (nullable)
#   time          - int
#   platform      - string (nullable)
#   device_model  - string (nullable)
cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
cc_impression_redshift_table = 'content_card_impression'
cc_impression_redshift_column_def = [
    ('id', 'text'),
    ('user_id', 'text'),
    ('external_user_id', 'text'),
    ('app_id', 'text'),
    ('content_card_id', 'text'),
    ('campaign_id', 'text'),
    ('send_id', 'text'),
    ('time', 'integer'),
    ('platform', 'text'),
    ('device_model', 'text')
]
cc_impression_batch_size = 1000
```
