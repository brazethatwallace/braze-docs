---
nav_title: Olo
article_title: Olo
description: "この記事では、あらゆるタッチポイントでホスピタリティを実現するレストラン向けの大手オープンSaaSプラットフォームであるOloとBrazeのパートナーシップについて説明します。"
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> [Olo](https://www.olo.com/)は、あらゆるタッチポイントでのホスピタリティを実現するレストラン向けの大手オープンSaaSプラットフォームです。

OloとBrazeを統合することで、以下のことが可能になります。

- BrazeのユーザープロファイルをOloのユーザープロファイルと一致するように更新する
- Oloのイベントに基づいて、Brazeから最適な次のメッセージを送信する

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Oloアカウント | このパートナーシップを利用するには、webhookにアクセスできるOloアカウントが必要です。Oloダッシュボード内の[セルフサービスwebhookツール](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks)を使用してwebhook購読を設定してください。 |
| Brazeデータ変換 | Oloからデータを受信するには、[データ変換URL]({{site.baseurl}}/data_transformation)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

webhookは、Oloがユーザーとそのアクションに関するイベント駆動型の情報をBrazeに送信する方法です。送信されるイベントには、注文完了、ゲストのオプトイン、注文のピックアップなどが含まれます。Olo webhookは、アクションが実行されてから通常数秒以内にイベントをBrazeに配信します。

## 免責事項 {#disclaimer}

Oloでは、承認された各ブランドの環境ごとにWebhookは1つに制限されており、すべて同じ**Destination URL**に送信されます。異なるブランドには異なるURLを設定できますが、同じブランドのイベントは1つのURLを共有する必要があります。Brazeでは、これはOloとの連携に使用できるトランスフォーメーションが1つだけであることを意味します。

この単一のトランスフォーメーション内で複数のOloイベントを処理するには、各webhookの `X-Olo-Event-Type` ヘッダーを確認してください。このヘッダーにより、異なるOloイベントを条件付きで処理できます。

## 連携 {#integration}

### ステップ1: Oloのテストイベントを受け入れるためのBrazeデータ変換を設定する {#step-1}

{% multi_lang_include data_activation/create_transformation.md location="default" %}

### ステップ2: Olo webhookを設定する {#step-2-set-up-olo-webhooks}

Oloダッシュボード内の[セルフサービスWebhookツール](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks)を使用して、データ変換に送信するwebhookを設定します。

1. Brazeに送信するイベントを選択します
2. **送信先URL**を設定します。これは[ステップ1](#step-1)で作成したデータ変換URLです。

{% alert note %}
`OAuth`および`X-Olo-Signature`ヘッダーの共有シークレットは、変換には必要ありません。
{% endalert %}

{:start="3"}
3. [テストイベント](https://developer.olo.com/docs/load/webhooks#operation/test)をデータ変換に送信して、webhookが正しく設定されていることを確認します。テストイベントを送信できるのは、[開発者ツール権限](https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions)を持つOloダッシュボードユーザーのみです。

Oloでは、Olo webhookの設定プロセスを完了する前に、テストイベントwebhookからの成功レスポンスが必要です。

### ステップ3: 選択したOloイベントを受け入れるための変換コードを記述する {#step-3-write-transformation-code-to-accept-your-chosen-olo-events}

このステップでは、ソースプラットフォームから送信されるwebhookペイロードをJavaScriptオブジェクトの戻り値に変換します。

1. サポートするOloイベントのサンプルイベントペイロードを使用して、データ変換URLにリクエストを送信します。リクエストのフォーマットについては、[リクエストボディのフォーマット](#request-body-format)を参照してください。
2. データ変換を更新し、**Webhookの詳細**でサンプルイベントペイロードが表示されることを確認します。
3. 選択したOloイベントをサポートするようにデータ変換コードを更新します。
4. **検証**をクリックして、コード出力のプレビューを返し、それが受け入れ可能な`/users/track`リクエストであるかどうかを確認します。
5. データ変換を保存して有効化します。

#### リクエストボディのフォーマット {#request-body-format}

この戻り値は、Brazeの`/users/track`リクエストボディのフォーマットに準拠している必要があります。

{% multi_lang_include data_transformation/transformation_code_requirements.md %}

## Olo webhookのデータ変換テンプレートの例 {#example-data-transformations-for-olo-webhooks}

このセクションでは、出発点として使用できるテンプレートの例を紹介します。ゼロから作成することも、必要に応じて特定のコンポーネントを削除することもできます。

各テンプレートでは、`/users/track`リクエストを構築するための変数`brazecall`をコードで定義しています。

`/users/track`リクエストを`brazecall`に割り当てた後、明示的に`brazecall`を返してアウトプットを作成します。

### 単一イベントの変換 {#single-event-transformation}

単一のOloイベントのみをサポートする場合、`X-Olo-Event-Type`ヘッダーを使用して`/users/track`リクエストペイロードを条件付きで作成する必要はありません。たとえば、Olo Order Placed webhookがBrazeに送信されたときに、購入イベントまたはカスタムイベントをユーザープロファイルに記録する場合です。

### 各製品を購入として記録する {#logging-each-product-as-a-purchase}

```javascript
// iterate through the items included within the order

const purchases = payload.items.map((item) => {
 return {
   external_id: payload.customer.customerId.toString(),
   product_id: item.productId.toString(),
   currency: 'USD',
   price: item.sellingPrice,
   time: new Date().toISOString(),
   quantity: item.quantity,
   properties: {
     customValues: item.customValues
   }
 };
});

// log a purchase per item in the order

let brazecall = {
 "purchases": purchases
};

return brazecall;
```

### カスタムイベントを記録する {#logging-a-custom-event}

```javascript
// log an event “Order Placed” to the profile that includes all items in the order as event properties.

let brazecall = {
"events": [
   {
     "external_id": payload.customer.customerId.toString(),
     "_update_existing_only": false,
     "name": "Order Placed",
     "time": new Date().toISOString(),
     "properties": {
       "Delivery Method": payload.deliveryMethod,
       "Items": payload.items,
       "Total": payload.totals.total,
       "Location": payload.location.name
     }
   }
 ]
};

return brazecall;
```

## マルチイベントトランスフォーメーション {#multi-event-transformation}

Oloは各webhookの`X-Olo-Event-Type`ヘッダー内にイベントタイプを送信します。単一のトランスフォーメーション内で複数のOlo webhookイベントをサポートするには、このヘッダータイプの値に基づいてwebhookペイロードを変換する条件ロジックを使用します。

以下のトランスフォーメーションの例では、JavaScriptが`UserSignedUp`と`OrderPlaced`のイベントに対して特定のペイロードを作成します。さらに、`else`条件は、X-Olo-Event-Typeヘッダーが`UserSignedUp`および`OrderPlaced`以外のOloイベントがBrazeに送信された場合のペイロードを処理します。

```javascript
// captures the value within the X-Olo-Event-Type header for use in the conditional logic

let event_type = headers["X-Olo-Event-Type"];

// defines a variable 'brazecall' that will hold the request payload for the /users/track request

let brazecall;

// if the X-Olo-Event-Type header is 'UserSignedUp', define a variable for the different subscription statuses that could be included within the Olo event payload

if (event_type == "UserSignedUp") {
	let emailSubscribe;
	let emailSubscriptionGroup;
	let smsSubscriptionGroup;


// determine if the user has opted into marketing emails


	if (payload.allowEmail) {
		emailSubscribe = "opted_in";
		emailSubscriptionGroup = "subscribed";
	} else {
		emailSubscribe = "unsubscribed";
		emailSubscriptionGroup = "unsubscribed";
	}


	// determine if the user has opted into SMS


	if (payload.allowMarketingSms) {
		smsSubscriptionGroup = "subscribed";
	} else {
		smsSubscriptionGroup = "unsubscribed";
	}

	// build the /users/track request and pass in the appropriate subscription statuses


	brazecall = {
		"attributes": [{
			"external_id": payload.id.toString(),
			"_update_existing_only": false,
			"email": payload.emailAddress,
			"first_name": payload.firstName,
			"last_name": payload.lastName,
			"email_subscribe": emailSubscribe,
			"phone": payload.contactNumber,
			"subscription_groups": [{
					"subscription_group_id": "57e5307f-9084-490d-9d6d-8244dc919a48",
					"subscription_state": emailSubscriptionGroup
				},
				{
					"subscription_group_id": "6440ba26-86ea-47db-a935-6647941dc78b",
					"subscription_state": smsSubscriptionGroup
				}
			]
		}]
	}; // if the X-Olo-Event-Type header is 'OrderPlaced', build the /users/track request to log an event to the user profile
} else if (event_type == "OrderPlaced") {
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": false,
			"name": "Order Placed",
			"time": new Date().toISOString(),
			"properties": {
				"Delivery Method": payload.deliveryMethod,
				"Items": payload.items,
				"Total": payload.totals.total,
				"Location": payload.location.name
			}
		}]
	};
} else { // if the X-Olo-Event-Type header is anything else, build the /users/track request to log an event to the user profile
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": true,
			"name": "Another Event",
			"time": new Date().toISOString()
		}]

	};
}

// return `brazecall` to create an output.

return brazecall;
```

### ステップ4:Olo webhookを公開する {#step-4-publish-your-olo-webhook}

Brazeでデータトランスフォーメーションを有効にしたら、Oloダッシュボード内の[セルフサービスwebhookツール](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks)を使用してwebhookを公開します。webhookが公開されると、データトランスフォーメーションがOlo webhookイベントメッセージの受信を開始します。

## 知っておくべきこと {#things-to-know}

### リトライ {#retries}

OloはHTTPレスポンスステータスコード`429 - Too Many Requests`または`5xx`範囲（ゲートウェイタイムアウトやサーバーエラーなど）のwebhook呼び出しを、リクエストを破棄するまでの24時間以内に最大50回リトライします。

### 最低1回の配信 {#at-least-once-delivery}

webhook呼び出しがHTTPレスポンスステータスコード`429 - Too Many Requests`または`5xx`範囲（ゲートウェイタイムアウトやサーバーエラーなど）になった場合、Oloはメッセージの送信を諦めるまでの24時間以内に最大50回リトライします。

そのため、サブスクライバーがwebhookを複数回受信する可能性があります。`X-Olo-Message-Id`ヘッダーを確認して重複を無視するのは、サブスクライバー側の責任です。