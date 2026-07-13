---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "この参考記事では、Braze Currentsとコネクテッドコンテンツを使用し、Webhookを通じてサブスクライバーからクリック追跡情報を収集する、BrazeとJacquard Dynamic Optimisationのパートナーシップについて概説しています。Jacquardは、これらのイベントを言語バリアントに関連付けて、リアルタイムで言語を最適化します。"
page_type: partner
search_tag: Partner
---

# Jacquard Dynamic Optimisation

> [Jacquard](https://www.jacquard.com/) は、人工知能、計算言語学、そして顧客中心の精神を融合し、ブランドボイスに合わせてカスタマイズされたチャネルにわたり、ブランドのメッセージを大規模に展開できるようにします。

Jacquard Xを活用したDynamic Optimisationは、Braze Currentsとコネクテッドコンテンツを使用し、Webhookを通じてサブスクライバーからクリック追跡情報を収集します。Jacquardは、これらのイベントを言語バリアントに関連付けて、リアルタイムで言語を最適化します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Jacquardアカウント | このパートナーシップを活用するには、[Jacquardアカウント](https://www.jacquard.com/)が必要です。 |
| Jacquard接続サーバートークン | Jacquardの言語にアクセスするための、Braze キャンペーンのパスワードとして機能する長い文字列です。<br><br>このトークンがまだ提供されていない場合は、Jacquardカスタマーサクセスマネージャーにリクエストできます。 |
| Currents | Currentsにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1: Jacquard Amazon S3の認証情報をリクエストする {#step-1-request-jacquard-amazon-s3-credentials}

クリック追跡イベントをBrazeから受け取るには、Jacquardが専用のAmazon S3バケットをセットアップする必要があります。このプロセスを開始するには、Jacquardカスタマーサクセスマネージャーに連絡してください。バケットが作成されると、Currentを作成するための一意の認証情報が提供されます。

### ステップ2: Currentを作成する {#step-2-create-current}

1. Brazeで、**Currents > Create New Current > Amazon S3 Data Export**を選択します。
2. 次にCurrentに名前を付け、連絡先メールアドレスを入力します。
3. 認証情報ボックスに、Jacquard AWSアクセスキーIDとシークレットアクセスキーを追加します。次に、AWS S3バケット名として「phrasee-braze-currents-exports」を追加します。
4. 最後に、Jacquardカスタマーサクセスマネージャーから受け取ったAWS S3バケットフォルダーを追加します。これはお客様の会社名である可能性があります。
5. **General Settings**で「Include events from anonymous users」ボックスをオンにし、**Manage Engagement Events**で「Email Click」をオンにします。
6. 完了したら、**Launch Current**を選択します。

### ステップ3: 個人を特定できる情報（PII）の削除をリクエストする {#step-3-request-to-remove-personally-identifiable-information-pii}

次に、Brazeアカウントチームに連絡し、個人を特定できる情報がJacquardに送信されないようにします。

デフォルトでは、Currentにはメールや住所などの特定のPII属性が含まれます。JacquardはPIIを受け取ることができず、また受け取ることもないため、Jacquardに渡されるすべてのイベントデータについてこれをオフにするよう、Brazeアカウントチームにリクエストすることが重要です。

### ステップ4: Jacquard Xコードスニペット {#step-4-jacquard-x-code-snippets}

必要なコードスニペットについては、Jacquardアカウントチームにお問い合わせください。

これらのスニペットは[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)を使用し、メールに配置された後、動的に言語とトラッキングピクセルを取り込み、Jacquard Xを使用してリアルタイムで言語を最適化できるようにします。