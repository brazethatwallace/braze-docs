---
nav_title: アカウントオブジェクト
article_title: アカウントオブジェクト
page_type: reference
permalink: /account_object/
hidden: true
description: "アカウントオブジェクトを使用して、ユーザーが所属するアカウントに基づいてセグメントを構築し、Liquidタグを使用してパーソナライズされたメッセージを送信する方法を説明します。"
---

# アカウントオブジェクト {#account-objects}

> アカウントオブジェクトを使用して、ユーザーが所属するアカウントに基づいてセグメントを構築し、Liquidタグを使用してパーソナライズされたメッセージを送信する方法を説明します。

アカウントデータをインポートするには、[CSVファイル](#using-a-csv-file)またはBraze APIを使用します。Braze APIを使用すると、[複数のアカウントを作成](#create-multiple-accounts)、[1つのアカウントを作成](#create-one-account)、[複数のアカウントを削除](#delete-multiple-accounts)、[1つのアカウントを削除](#delete-one-account)できます。

| オーディエンス | この記事の活用方法 |
|----------|----------------------------|
| マーケター | CSVを使用してユーザーデータとアカウントデータをインポートし、アカウント属性に基づいてセグメントを構築し、Brazeでアカウント情報を使ってメッセージをパーソナライズします。 |
| 開発者 | Braze REST APIを使用して、アカウントレコードをプログラムで作成、更新、削除し、Brazeをデータと同期させます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
アカウントオブジェクトは現在ベータ版です。このベータへの参加に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 仕組み {#how-it-works}

アカウントオブジェクトは、ユーザーの会社を表すカスタムデータ構造です。ユーザープロファイルに接続されるため、B2Bスタイルのセグメントを構築し、メッセージをパーソナライズできます。会社名、業種、役割、商談ステータスなどのアカウントフィールドを、Brazeカタログ、セグメンテーションフィルター、Liquidタグと組み合わせて使用します。

たとえば、ヘルスケア業界で働くユーザーをターゲットにし、医師や病院管理者にパーソナライズされたメッセージを送信して、メッセージの関連性をさらに高めることができます。

アカウントオブジェクトを使用するには、3種類のデータをBrazeにインポートします。

- **ユーザーデータ:** Brazeで各個人を識別するための個別のユーザープロファイル（たとえば、`external_id`、メール、電話、またはユーザーエイリアスを使用）。ユーザーデータはCSVでインポートします。
- **ユーザーとアカウントの関連データ:** ユーザーとアカウントの関係。ユーザーがどの会社に所属し、そのアカウントでどのような役割を持っているかを含みます。この関連データはCSVでインポートします。
- **アカウントデータ:** 会社名、業種、年間収益、その他の企業属性などの会社レコード自体。これらはセグメントやメッセージでターゲティングやパーソナライズに使用するレコードです。アカウントデータはCSVまたはBraze REST APIでインポートします。

アカウントオブジェクトが機能するには、3種類のデータすべてをインポートする必要があります。ユーザーデータはBrazeで人を識別し、ユーザーとアカウントの関連データはそれらのユーザーを特定のアカウントと役割に接続し、アカウントデータはセグメンテーションとパーソナライゼーションに使用される会社レベルの属性を提供します。

## 前提条件 {#prerequisites}

この機能を使用するには、Brazeにすでにユーザーが存在している必要があります。

## Brazeへのデータインポート {#import-data-to-braze}

メッセージ内でアカウントオブジェクトを使用するには、ユーザーデータがすでにBrazeに存在している必要があります。そこから、2つのインポートを完了します。まず、ユーザーとアカウントの関連データをインポートして、アカウントの関連付けと役割を確立します（現在はCSVのみ）。次に、セグメンテーションとパーソナライゼーションに使用される会社レベルの詳細を含むアカウントデータをインポートします（CSVまたはBraze REST API経由）。

### ステップ 1: ユーザーとアカウントの関連データをインポートする {#step-1-import-user-account-relationship-data}

まず、以下のフィールドを含むCSVファイルとして、ユーザーとアカウントの関連データをBrazeにインポートします。これにより、Brazeは既存のユーザーを正しいアカウントと役割に関連付けることができます。

<style>
table td {
    word-break: break-word;
}
</style>

| フィールド名 | フィールドタイプ | 必須 | 説明 |
|------------------|------------|----------|-------------------------------------------------------------------------------------------------------|
| `account_id`       | 文字列     | はい      | ユーザーが所属するアカウント。これはアカウントオブジェクトの`id`フィールド（CRM ID）と同じです。 |
| `external_id`      | 文字列     | はい      | Brazeにおけるユーザーの[external ID](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles)。 |
| `user_alias_name`  | 文字列     | いいえ*      | Brazeにおけるユーザーの[エイリアス名](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases)。 |
| `user_alias_label` | 文字列     | いいえ*      | Brazeにおけるユーザーの[エイリアスラベル](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users)。 |
| `email`            | 文字列     | いいえ*     | ユーザーのメールアドレス。 |
| `phone`            | 文字列     | いいえ*      | ユーザーの電話番号。 |
| `user_role`             | 文字列     | いいえ       | ユーザーがアカウントで持つ役割（「ディレクター」や「従業員」など）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
<sup>ユーザーを識別するには、`external_id`、`email`、`phone`、または`user_alias`のいずれかが必要です。</sup>

#### CSVファイルを使用する {#using-a-csv-file}

ユーザーとアカウントの関連付けを含むCSVをBrazeにアップロードします。

1. **データ設定** > **アカウント**に移動します。
2. **データを更新**を選択します。
3. **CSVアップロード**で**ユーザー**を選択し、ファイルをBrazeにアップロードします。

![Brazeの「アカウント」ページにある「データをアップロード」ドロップダウン。]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### ステップ 2: アカウントデータをインポートする {#step-2-import-account-data}

アカウントは、ユーザーが所属する会社です。以下のフィールドを含むCSVファイルとして、アカウントデータをBrazeにインポートします。各アカウントにはIDと名前を割り当てる必要があることに注意してください。

<style>
table td {
    word-break: break-word;
}
</style>

| フィールド名 | フィールドタイプ | 必須 | 説明 |
|-----------------------------|------------|----------|------------------------------------------------------------------------------------|
| `id`                          | 文字列     | はい      | CRM（顧客関係管理）プラットフォームにおけるアカウントのID。 |
| `name`                        | 文字列     | はい      | アカウントの名前。 |
| `type`                        | 文字列     | いいえ       | アカウントのタイプ（顧客、パートナー、リセラーなど）。 |
| `annual_revenue`              | 文字列     | いいえ       | アカウントの年間収益。 |
| `industry`                    | 文字列     | いいえ       | アカウントが事業を行っている業種。 |
| `number_of_employees`         | 文字列     | いいえ       | 従業員数。範囲指定をサポートしています。 |
| `address`                     | 文字列     | いいえ       | アカウントの住所。 |
| `city`                        | 文字列     | いいえ       | アカウントが所在する市区町村。 |
| `state`                       | 文字列     | いいえ       | アカウントが所在する州。 |
| `postal_code`                 | 文字列     | いいえ       | アカウントの住所の郵便番号。 |
| `country`                     | 文字列     | いいえ       | アカウントが所在する国。 |
| `notes`                       | 文字列     | いいえ       | アカウントに関する追加メモ。 |
| `website`                     | 文字列     | いいえ       | アカウントのWebサイトURL。 |
| `main_phone`                  | 文字列     | いいえ       | アカウントの代表電話番号。 |
| `created_date`                | 時間       | いいえ       | アカウントが作成された日付。 |
| `account_owner_email_address` | 文字列     | いいえ       | 社内のアカウントオーナー（「A社営業のTomがB社を担当」など）。 |
| `parent_account_id`           | 文字列     | いいえ       | 親アカウントのID（該当する場合。親会社のIDへのリンクなど）。 |
| `sic_code`                    | 文字列     | いいえ       | 標準産業分類コード。 |
| カスタムフィールド                 | N/A        | いいえ       | ユーザーが定義・管理するカスタムフィールド。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
{% alert note %}
一部のフィールドはオプションですが、予約済みのフィールド名であり、データの整理に役立つため、可能な限り含めてください。
{% endalert %}

次に、CSVファイルをアップロードするか、Braze REST APIを使用して、アカウントデータをBrazeにインポートします。このデータは**データ設定**で確認できます。ブラウザ内エディターではこのデータを編集できません。

#### CSVファイルを使用する

CSVでデータをインポートするには：

1. **データ設定** > **アカウント**に移動します。
2. **データを更新**を選択します。
3. **CSVアップロード**で**アカウントデータ**を選択し、ファイルをBrazeにアップロードします。

![Brazeの「アカウント」ページにある「データをアップロード」ドロップダウン。]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

## Braze APIを使用する {#using-the-braze-api}

API（アプリケーションプログラミングインターフェイス）は、異なるソフトウェアシステムがプログラムで通信できるようにします。Braze APIとやり取りする際は、特定のエンドポイントにHTTPリクエストを送信します。エンドポイントは、指示を受け取り応答を返す構造化されたURLです。HTTPメソッドは、Brazeに実行するアクションを伝え、リクエストボディにはデータが含まれます。

アカウント管理では、Braze APIは以下のHTTPメソッドを使用します。

| メソッド | 目的 | 動作 |
|--------|---------|----------|
| `PUT` | リソースの作成または更新 | アカウントレコードが存在しない場合は新規追加します。存在する場合は既存のレコードを更新します。`PUT`はべき等になるよう設計されているため、重複を作成することなく同じデータを複数回同期できます。 |
| `DELETE` | リソースの削除 | 指定されたアカウントレコードとその関連付けをBrazeから完全に削除します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze APIを使用すると、アカウントデータを大規模にプログラムで制御できます。アカウント管理ワークフローを自動化し、データソースからアカウント情報を直接同期し、手動のアップロードや編集なしにBrazeを信頼できるソースと整合させることができます。これにより、運用オーバーヘッドが削減され、セグメンテーションとパーソナライゼーションのための正確でタイムリーなアカウントデータを維持できます。

HTTPメソッドとREST APIの仕組みの詳細については、以下のリソースを参照してください。
- MDN Web Docsの[HTTPリクエストメソッド](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
- [REST APIチュートリアル](https://restapitutorial.com/)
- [Braze APIの概要]({{site.baseurl}}/api/basics/)

{% alert note %}
`/business/accounts`エンドポイントへのリクエストを認証するには、カタログ権限を持つAPIキーを使用してください。
{% endalert %}

このセクションでは、Braze APIを使用して以下を行う方法を説明します。
- [複数のアカウントを作成する](#create-multiple-accounts)
- [1つのアカウントを作成する](#create-one-account)
- [複数のアカウントを削除する](#delete-multiple-accounts)
- [1つのアカウントを削除する](#delete-one-account)

### 複数のアカウントを作成する {#create-multiple-accounts}

`PUT`はべき等であるため、同じリクエストを複数回送信しても、Brazeは重複を作成するのではなく既存のレコードを更新します。これにより、Brazeのアカウントレコードを最新の状態に保つための信頼性の高い方法となります。

以下のコードスニペットは、`/business/accounts`エンドポイントに`PUT`リクエストを送信します。`accounts`配列には複数の会社オブジェクトが含まれ、それぞれが[ステップ 2: アカウントデータをインポートする](#step-2-import-account-data)で定義されたアカウントフィールドにマッピングされています。Brazeは各オブジェクトを処理し、**アカウント**ページで対応するレコードを作成または更新します。この操作は非同期です。Brazeはリクエストをキューに入れ、バックグラウンドで処理するため、即時の確認が不要な一括インポートに適しています。

複数のアカウントを作成するには、`/business/accounts`に`PUT`リクエストを送信します。アカウントが存在しない場合、Brazeは**アカウント**ページに新しいアイテムを追加します。各リクエストは最大50アカウントをサポートします。この操作は非同期であることに注意してください。

リクエストは以下のようになります。

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
          "accounts": [
              {
                  "id": "ACC001",
                  "name": "Acme Corporation",
                  "type": "Customer",
                  "annual_revenue": "$5,000,000",
                  "industry": "Manufacturing",
                  "number_of_employees": "150",
                  "address": "123 Industrial Way",
                  "city": "Metropolis",
                  "state": "NY",
                  "postal_code": "10001",
                  "country": "USA",
                  "notes": "Key client in the manufacturing sector",
                  "website": "http://www.acme.com",
                  "main_phone": "+1-212-555-1234",
                  "created_date": "2023-01-15T09:30:00Z",
                  "account_owner_email_address": "owner@acme.com",
                  "parent_account_id": "",
                  "sic_code": "2011"
              },
              {
                  "id": "ACC002",
                  "name": "Global Solutions",
                  "type": "Partner",
                  "annual_revenue": "$10,000,000",
                  "industry": "Technology",
                  "number_of_employees": "500",
                  "address": "456 Tech Park",
                  "city": "Silicon Valley",
                  "state": "CA",
                  "postal_code": "94043",
                  "country": "USA",
                  "notes": "Important partner for software solutions",
                  "website": "http://www.globalsolutions.com",
                  "main_phone": "+1-650-555-5678",
                  "created_date": "2023-02-20T14:45:00Z",
                  "account_owner_email_address": "partner@globalsolutions.com",
                  "parent_account_id": "ACC001",
                  "sic_code": "7372"
              },
              {
                  "id": "ACC003",
                  "name": "Oceanic Ventures",
                  "type": "Customer",
                  "annual_revenue": "$3,200,000",
                  "industry": "Retail",
                  "number_of_employees": "75",
                  "address": "789 Ocean Blvd",
                  "city": "Miami",
                  "state": "FL",
                  "postal_code": "33101",
                  "country": "USA",
                  "notes": "Expanding presence in retail markets",
                  "website": "http://www.oceanicventures.com",
                  "main_phone": "+1-305-555-6789",
                  "created_date": "2023-03-05T08:15:00Z",
                  "account_owner_email_address": "contact@oceanicventures.com",
                  "parent_account_id": "",
                  "sic_code": "5941"
              }
          ]
      }'
```

### 1つのアカウントを作成する {#create-one-account}

複数のアカウントの作成と同様に、この操作は`PUT`メソッドを使用します。違いは、アカウントIDがリクエストボディではなくエンドポイントURLに直接含まれることです。これにより、単一のレコードを正確に制御できます。

以下のコードスニペットは、`/business/accounts/ACC001`に`PUT`リクエストを送信します。`ACC001`はアカウントの一意の識別子です。この操作は同期的です。Brazeはリクエストを即座に処理し、完了次第応答を返します。これはリアルタイム統合に適しています。たとえば、システムでアカウント情報が変更された場合、ターゲティングやパーソナライゼーションのためにその更新をBrazeにすぐに反映できます。

1つのアカウントを作成するには、`/business/accounts/:account_id`に`PUT`リクエストを送信します。アカウントが存在しない場合、Brazeは新しいアカウントレコードを作成します。この操作は同期的です。

リクエストは以下のようになります。

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "accounts": [
            {
                "name": "Braze",
                "type": "Customer",
                "annual_revenue": "$5,000,000",
                "industry": "Manufacturing",
                "number_of_employees": "150",
                "address": "123 Industrial Way",
                "city": "Metropolis",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA",
                "notes": "Key client in the manufacturing sector",
                "website": "http://www.acme.com",
                "main_phone": "+1-212-555-1234",
                "created_date": "2023-01-15T09:30:00Z",
                "account_owner_email_address": "owner@acme.com",
                "parent_account_id": "",
                "sic_code": "2011"
            }
        ]
      }'
```

### 複数のアカウントを削除する {#delete-multiple-accounts}

`DELETE`メソッドは、Brazeからアカウントレコードを削除します。`PUT`とは異なり、`DELETE`リクエストは元に戻せません。アカウントが削除されると、ユーザーとそのアカウントの関連付けも削除されます。

以下のコードスニペットは、リクエストボディにアカウントIDのリストを含む`DELETE`リクエストを`/business/accounts`に送信します。Brazeは各IDを処理し、対応するアカウントレコードを削除します。この操作は非同期です。Brazeは削除をキューに入れ、バックグラウンドで処理します。アカウントのグループが解約された、統合された、またはBrazeでのセグメンテーションに不要になった場合など、一括クリーンアップタスクに使用します。

複数のアカウントを削除するには、アカウントIDのリストを含むボディとともに`/business/accounts`に`DELETE`リクエストを送信します。この操作は非同期であることに注意してください。

リクエストは以下のようになります。

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "accounts": [
      { "id": "ACC001" },
      { "id": "ACC002" },
      { "id": "ACC003" }
    ]
  }'
```

### 1つのアカウントを削除する {#delete-one-account}

1つのアカウントの作成と同様に、この操作はエンドポイントURLにIDを直接含めることで特定のアカウントをターゲットにします。これにより、他のレコードに影響を与えることなく、単一のレコードを正確に制御できます。

以下のコードスニペットは、`/business/accounts/ACC001`に`DELETE`リクエストを送信します。この操作は同期的です。Brazeはリクエストを即座に処理し、完了次第応答を返します。個別のアカウントがクローズされた、統合された、またはコンプライアンスやデータ衛生の目的でBrazeから削除する必要がある場合に使用します。

単一のアカウントを削除するには、`/business/accounts/:account_id`に`DELETE`リクエストを送信します。この操作は同期的であることに注意してください。

リクエストは以下のようになります。

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY"
```

## メッセージでオブジェクトを使用する {#using-objects-in-messages}

[Brazeにデータをインポート](#importing-data-to-braze)した後、アカウントオブジェクトを使用してセグメントを構築し、Liquidを使用してユーザーにパーソナライズされたメッセージを送信できます。

### ステップ 1: セグメントを構築する {#step-1-build-a-segment}

次に、ユーザーデータとアカウントデータを組み合わせたセグメントを構築します。この例では、ヘルスプロモーション会社の新しいウェビナーへの登録を増やすために、ヘルスケア企業のディレクターをターゲットにします。

1. **オーディエンス** > **Segments**に移動し、**セグメントを作成**を選択します。
2. セグメントに名前を付けます。
3. **セグメントビルダー**で**ビジネス**フィルターを選択し、以下のセグメンテーションフィルターを設定します。完了したら、**保存**を選択します。

| フィルター | 説明 |
|---------------------------------|--------------------------------------------------|
| `Role is exactly director`      | 役割がディレクターであるユーザーをターゲットにします |
| `Accounts industry matches regex healthcare` | ヘルスケア関連の業種のアカウントに属するユーザーにマッチします |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
現在、複数のアカウントフィルターを使用するには、**OR/AND**ドロップダウンではなく**条件を追加**を選択してください。
{% endalert %}

![ヘルスケア企業のディレクターであるユーザーのセグメントを作成するために設定されたセグメンテーションフィルター。]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/build_segment.png %})

{% alert note %}
セグメンテーションは、条件に一致する最初の1,000件のアカウントレコードに対してのみ機能します。セグメントごとに最大1つのビジネスフィルターを使用でき、すべての条件は1つのフィルター内に含める必要があります。
{% endalert %}

### ステップ 2: Liquidを使用してパーソナライズする {#step-2-use-liquid-to-personalize}

これで、メッセージをパーソナライズして、ユーザーにオポチュニティに関する情報を送信できます。この例では、ディレクター向けのメッセージを作成し、ウェビナーへのリンクを含めます。また、Brazeカタログを使用して、パーソナライゼーション用の業種固有の画像を取得することもできます。

#### ステップ 2.1: アカウント情報でパーソナライズする {#step-21-personalize-with-account-information}

パーソナライゼーションタイプとして**ビジネス**を選択し、次に**名前**を選択して、ユーザーの会社名でメッセージをパーソナライズします。

以下がクリップボードにコピーされます。

{% raw %}
```javascript
{% business %}
{{ business_accounts[0].name }}
```
{% endraw %}

Brazeは{% raw %}`{% business %}`{% endraw %}タグを生成します。これにより、関連するアカウントのアカウント情報を含む`business_accounts`という名前の配列が設定されます。

自動生成された出力を調整してメッセージを作成します。

以下の例では、{% raw %}`{% business %}`{% endraw %}タグの呼び出しをメッセージの先頭に移動し、ユーザーの名でパーソナライズします。アカウント名を使用してメッセージをパーソナライズします。Liquidの出力は同じですが、メッセージの異なる部分に配置します。

{% raw %}
```javascript
{% business %}

Hi {{${first_name}}},

We would love to invite you and your peers at {{ business_accounts[0].name }} to join our latest webinar named "Creating Optimal Health Outcomes for Patients".  Click the link below to register.
```
{% endraw %}

出力は以下のようになります。

{% raw %}
```javascript
Hi John,

We would love to invite you and your peers at Sunshine Health to join our latest webinar named "Creating Optimal Health Outcomes for Patients". Click the link below to register.
```
{% endraw %}

#### ステップ 2.2: カタログと接続する {#step-22-connect-with-catalogs}

次に、Brazeカタログを使用して、ヘルスケア企業に対応する画像を追加・保存することで、メッセージをさらにパーソナライズします。

この例では、以下があることを前提としています。

- `industry_assets`というカタログが設定されている
- 各カタログエントリのIDが、アカウントの業種に対応する業種名である
- プライマリ画像とセカンダリ画像の画像URLリンク

以下は、このパーソナライゼーションに使用されるLiquidの例です。
{% raw %}
```javascript
//Make a call to the business tag.  This sets the accounts array and prepares us to pull account data out.
{% business %}

//Assign the user's accounts industry to a variable called industry.  This step isn't required but it makes everything easier to read.
{% assign industry = {{business_accounts[0].industry}} %}

//Make a catalog_items call to the industry_assets catalog and ask for the industry item (in this case, it will ask for "healthcare")
{% catalog_items industry_assets industry %}

// Get the hero image for the "healthcare" industry
{{items[0].hero_image}}
```
{% endraw %}

## よくある質問（FAQ） {#faq}

### カスタムフィールドを追加できますか？ {#can-i-add-custom-fields}

はい。アカウントにカスタムフィールドを追加できます。独自のリードスコアリング方法がある場合は、アカウントオブジェクトのカスタムフィールドを使用してこれを追跡することもできます。

### ユーザーは複数のアカウントに関連付けることができますか？ {#can-a-user-be-associated-with-more-than-one-account}

いいえ。現在、各ユーザーは1つのアカウントの関連付けのみ持つことができます。

### 1つのユーザープロファイルに複数のメールを含めることはできますか？ {#can-one-user-profile-contain-multiple-emails}

いいえ。ユーザープロファイルには、個人用メールと仕事用メールなど、複数のメールを含めることはできません。