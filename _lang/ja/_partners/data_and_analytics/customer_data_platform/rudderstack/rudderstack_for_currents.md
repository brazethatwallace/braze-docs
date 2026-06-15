---
nav_title: RudderStack と Currents
article_title: RudderStack と Currents
description: "この記事では、Braze Currentsと RudderStack のパートナーシップについて説明します。RudderStack は、Android、iOS、およびWebアプリケーション向けのシームレスなBraze統合を提供するオープンソースの顧客データインフラです。"
page_type: partner
tool: Currents
search_tag: Partner

---

# RudderStack と Currents {#rudderstack-for-currents}

> [RudderStack](https://www.rudderstack.com/) では、スタック全体で顧客データを収集、変換、アクティブ化し、クラウドデータウェアハウスを一元的な信頼できる情報源として活用できます。この記事では、Braze CurrentsとRudderStack間の接続を設定する方法の概要を説明します。

BrazeとRudderStackの統合により、Braze Currentsを利用してBrazeイベントをRudderStackにエクスポートし、より深い分析を促進できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| RudderStackアカウント | このパートナーシップを活用するには、[RudderStackアカウント](https://app.rudderstack.com/login)が必要です。 |
| Brazeの送信先 | RudderStackで[Brazeを送信先として設定する]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration)ことをお勧めします。 |
| Currents | RudderStackにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ 1: RudderStack内でBrazeのデータソースを作成する {#step-1-create-a-data-source-for-braze-within-rudderstack}

まず、RudderStack WebアプリでBrazeソースを作成する必要があります。データソースの作成手順は、[RudderStack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/)サイトで確認できます。

作業が完了すると、RudderStackから書き込みキーを含むWebhook URLが提供されます。このURLは次のステップで使用します。Webhook URLは、Brazeソースの**設定**タブで確認できます。

### ステップ 2: Currentを作成する {#step-2-create-current}

Brazeで**Currents > + Create Current > RudderStack Export**に移動します。統合名、連絡先メール、RudderStack Webhook URL（キーフィールドに入力します）、およびRudderStackリージョンを指定します。

### ステップ 3: イベントをエクスポートする {#step-3-export-events}

次に、エクスポートするイベントを選択します。最後に、**Launch Current**をクリックします。

RudderStackに送信されるすべてのイベントには、ユーザーの`external_user_id`が含まれます。現時点では、Brazeは`external_user_id`が設定されていないユーザーのイベントデータをRudderStackに送信しません。

## 統合の詳細 {#integration-details}

Brazeは、[Currentsイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)に記載されているすべてのデータをRudderStackにエクスポートできます。

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクターのペイロード構造と同じです。これは、[カスタムHTTPコネクターのサンプルリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。