---
nav_title: Lytics
article_title: Lytics
description: "このリファレンス記事では、BrazeとLyticsの統合について説明します。Lyticsは、マーケター、アナリスト、技術者向けのエンタープライズ顧客データプラットフォームです。この統合により、ブランドはLyticsのデータをBrazeに直接同期およびマッピングできます。"
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics](https://www.lytics.com/)は、顧客中心の次世代ビジネスに最適な顧客データプラットフォーム（CDP）です。Lytics Decision Engine、Conductor、Cloud Connectの各ソリューションは、マーケターとデータチームに、プライバシーに準拠した方法で、アイデンティティ解決、オーケストレーション、キャンペーン最適化をリアルタイムで実行する機会を提供します。

_この統合はLyticsによって管理されています。_

## 統合について {#about-the-integration}

BrazeとLyticsの統合により、顧客を一元的に把握できるため、強力なパーソナライゼーションが可能になり、ネクストベストアクションのオーケストレーションと意思決定を使用して最適化されたキャンペーンを推進できます。

この統合により、ブランドは以下のことができるようになります。

- LyticsからBrazeに直接オーディエンスをエクスポートする
- BrazeのキャンペーンやキャンバスのイベントをリアルタイムでLyticsに送信し、パーソナライズされたキャンペーンやリッチなユーザープロファイルを構築する

## ユースケース {#use-cases}

BrazeをLyticsに接続して、メール、SMS、プッシュアクティビティを[インポート](#importing-data-from-braze-to-lytics)し、Lyticsのユーザープロファイルを充実させます。BrazeとLyticsを併用することで、Lyticsのクロスチャネルの行動主導型オーディエンスを[エクスポート](#integration)し、ファーストパーティデータを使用して高度にパーソナライズされたBrazeカスタマージャーニーを構築することもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Lyticsアカウント | この統合を活用するには、Lyticsアカウントが必要です。 |
| Lyticsアカウント番号 | WebhookエンドポイントURLを設定するには、Lyticsのアカウント番号が必要です。 |
| Lytics APIトークン | データマネージャー権限を持つLytics REST APIトークン。<br><br> これは、Lyticsダッシュボード内の**Account Settings Console** > **Access Tokens** > **Create New Token**から作成できます。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Brazeインスタンス | お客様の[Brazeインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)。不明な場合は、Brazeのオンボーディングマネージャーにお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

このセクションでは、LyticsのデータをBrazeにエクスポートする方法を説明します。

### ステップ1:認証を作成する {#step-1-create-an-authorization}

Lyticsで、ナビゲーションバーの**Data**コンソール内の**Authorization**ダッシュボードに移動します。**Create New Authorization**を選択し、**Braze**を検索して選択します。

表示される**Configure Authorization**プロンプトで、ラベルと説明を入力し、REST APIキーとBrazeインスタンスを入力します。完了したら**Complete**を選択します。

![ラベル、説明、REST APIキー、Brazeインスタンスのフィールドを含むBraze用のLytics認証設定プロンプト。]({% image_buster /assets/img/lytics/braze_authorization.png %}){: style="max-width:80%;"}

### ステップ2:新しいジョブを作成する {#step-2-create-a-new-job}

Lyticsで、ナビゲーションバーの**Data**コンソール内の**Jobs**ダッシュボードに移動します。**Create New Job**を選択し、**Braze**を検索して選択します。表示される**Select Job Type**プロンプトで**Export Audience**を選択します。

![Export Audienceが選択された新しいBrazeジョブのLyticsジョブタイプ選択プロンプト。]({% image_buster /assets/img/lytics/braze_jobtype.png %}){: style="max-width:80%;"}

次に、**Select Authorization**オプションの中から認証を選択します。

![エクスポートジョブに使用するBraze認証を表示するLytics認証選択ステップ。]({% image_buster /assets/img/lytics/braze_jobauth.png %}){: style="max-width:80%;"}

### ステップ3:ジョブを設定する {#step-3-configure-the-job}

**Configure Job**プロンプト内で、ラベルとオプションの説明を入力します。次に、**Braze External User ID Field**の入力欄から、Braze外部ユーザーID（`braze_id`）を含むLyticsのフィールドを選択します。次は最も重要なステップです。同じプロンプト内のオーディエンスピッカーを使用して、Brazeにエクスポートするオーディエンスを選択します。

最後に、**Existing Users**チェックボックスで適切なオプションを選択します。このボックスをオンのままにすると、選択したLyticsオーディエンスにすでに存在しているユーザーが追加されます。オフにすると、ワークフロー開始後にオーディエンスに追加された時点またはオーディエンスから外れた時点でのみ、ユーザーがBrazeにエクスポートされます。

{% alert note %}
このボックスをチェックすると、選択したオーディエンスのすべての既存ユーザーがBrazeに送信されます。Brazeの料金にデータポイントが含まれている場合は、データポイント使用量を適宜モニターしてください。
{% endalert %}

完了したら**Complete**を選択してエクスポートを開始し、保存します。

![Completeコントロールと、Brazeオーディエンスエクスポートを保存または実行するオプションを表示するLyticsエクスポートジョブの概要。]({% image_buster /assets/img/lytics/braze_backfill.png %}){: style="max-width:80%;"}

エクスポートジョブの設定が完了すると、Lyticsはネイティブ統合を介して、選択されたオーディエンスをBrazeに送信します。以下は、Brazeに送信されるオーディエンスのJSON構造を示すサンプルオーディエンスです。

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

オーディエンスのエクスポートに含まれ、Brazeにまだ存在していない`external_id`に対して、Brazeで新しいユーザーが作成されます。

## BrazeからLyticsにデータをインポートする {#importing-data-from-braze-to-lytics}

BrazeからLyticsへのオーディエンスデータのインポートは、以下の方法で行うことができます。

- [Webhookを使用する](#using-webhooks)
- [CSVファイルから](#from-a-csv-file)

### Webhookを使用する {#using-webhooks}

#### ステップ1:Lytics APIトークンを作成する {#step-1-create-a-lytics-api-token}

アカウント名を選択してLytics Account Menuに移動し、ドロップダウンメニューから**Access Tokens**を選択します。次に**Create API Token**を選択します。

![アカウントメニューからCreate API Tokenが選択されたLyticsのAccess Tokens画面。]({% image_buster /assets/img/lytics/create_token.png %}){: style="max-width:80%;"}

名前、オプションの説明、トークンの有効期限を入力します。次にAPI権限の**Data マネージャー**スコープをオンに切り替え、**Generate Token**を選択します。トークンをコピーし、安全な場所に保管してください。

![トークン生成前にData Managerスコープが有効になっているLytics APIトークン権限。]({% image_buster /assets/img/lytics/data_manager.png %}){: style="max-width:80%;"}

#### ステップ2:LyticsのWebhook URLを設定する {#step-2-configure-the-lytics-webhook-url}

Lytics Webhook URLは、BrazeからLytics APIにメッセージを送信するためにBrazeによって使用されます。このメッセージは、Lyticsでキャンペーンをパーソナライズする場合や、Lyticsの顧客プロファイルを充実させる場合に使用できます。以下の2つのパラメータは、Lytics Webhook URL内に追加する必要があります。

- Lyticsアカウント番号
- Lytics APIトークン

Webhook URLを以下のように設定します。

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

`<ACCOUNT-NUMBER>`をアカウント番号に置き換え、`<LYTICS-API-TOKEN>`をLytics APIトークンに置き換えます。

#### ステップ3:BrazeでWebhookを作成する {#step-3-create-a-webhook-on-braze}

Brazeで新しい[Webhookキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)を作成します。**Webhook URL**フィールドにLyticsのWebhook URLを追加します。

リクエストタイプ（HTTP `POST`メソッド）を定義し、残りのWebhookの詳細を設定したら、Webhookをテストおよびデプロイできます。以下は、BrazeでWebhookを設定した後のPOSTリクエスト本文のサンプルです。

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "Alex",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@example.com",
  "braze_id": "xxxxxx"
}
```

### CSVファイルから {#from-a-csv-file}

このセクションでは、BrazeのユーザーデータをセグメントからLyticsにインポートする方法を説明します。

#### ステップ1:認証を作成する

Lyticsで、ナビゲーションバーの**Data**コンソール内の**Authorization**ダッシュボードに移動します。**Create New Authorization**を選択し、**Custom Integrations**を検索して選択します。

ビジネス要件とセキュリティ要件に基づいて、使用するSFTP認証タイプを選択します。SFTP経由でLyticsにファイルをインポートする場合、以下の認証タイプがサポートされています。

- クライアントSFTPサーバー認証
- PGP秘密鍵によるクライアントSFTPサーバー認証
- LyticsマネージドSFTPサーバー認証

公開鍵SFTP認証は、SFTPエクスポート専用です。

![クライアントおよびLyticsマネージドサーバーの選択肢を含む、Custom Integrationsインポート用のLytics SFTP認証方法オプション。]({% image_buster /assets/img/lytics/authorization_method.png %}){: style="max-width:80%;"}

表示される**Configure Authorization**プロンプトで、ラベルと説明を入力し、残りの設定要件を完了します。完了したら**Complete**を選択します。

#### ステップ2:セグメントデータをCSVにエクスポートする {#step-2-export-your-segment-data-to-csv}

Brazeで**オーディエンス** > **セグメント**に移動します。エクスポートするセグメントを見つけ、<i class="fas fa-gear" aria-label="設定"></i>を選択し、次に**ユーザーデータをCSV形式でエクスポート**を選択します。1つのセグメントで最大500,000ユーザーをエクスポートできます。詳細については、「[CSVへのセグメントデータのエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)」を参照してください。

#### ステップ3:CSVインポートジョブを設定する {#step-3-configure-a-csv-import-job}

Lyticsで、ナビゲーションバーの**Data**コンソール内の**Jobs**ダッシュボードに移動します。**Create New Job**を選択し、**Custom Integrations**を検索して選択します。

次にジョブタイプを選択します。BrazeのCSVファイルをLyticsにインポートするには、ジョブタイプとして**Import CSV**を選択します。

![Import CSVがジョブタイプとして選択されたLytics Custom Integrationsジョブ設定。]({% image_buster /assets/img/lytics/configure_job.png %}){: style="max-width:80%;"}

最後に、ジョブのラベルとオプションの説明を入力し、その他の必要な詳細を設定します。**Complete**を選択して、ジョブを開始し保存します。