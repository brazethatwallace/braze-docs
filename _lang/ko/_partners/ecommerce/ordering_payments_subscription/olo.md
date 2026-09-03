---
nav_title: Olo
article_title: Olo
description: "이 문서에서는 모든 터치포인트에서 호스피탈리티를 실현하는 레스토랑 업계 선도적인 오픈 SaaS 플랫폼인 Olo와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> [Olo](https://www.olo.com/)는 모든 터치포인트에서 호스피탈리티를 실현하는 레스토랑 업계 선도적인 오픈 SaaS 플랫폼입니다.

Olo와 Braze를 통합하면 다음을 수행할 수 있습니다.

- Braze의 고객 프로필을 Olo 고객 프로필과 일관되게 업데이트
- Olo 이벤트를 기반으로 Braze에서 최적의 다음 메시지 발송

## 사전 요구 사항 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Olo 계정 | 이 파트너십을 활용하려면 웹훅 접근 권한이 있는 Olo 계정이 필요합니다. Olo 대시보드 내 [셀프서비스 웹훅 도구](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks)를 통해 웹훅 구독을 설정하세요. |
| Braze 데이터 변환 | Olo에서 데이터를 수신하려면 [데이터 변환 URL]({{site.baseurl}}/data_transformation)이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

웹훅은 Olo가 사용자와 사용자 행동에 대한 이벤트 기반 정보를 Braze로 전송하는 방법으로, 주문 완료, 고객 수신 동의, 주문 픽업 등의 이벤트를 포함합니다. Olo 웹훅은 일반적으로 해당 행동이 수행된 후 몇 초 이내에 Braze로 이벤트를 전달합니다.

## 면책 조항 {#disclaimer}

Olo에서는 승인된 브랜드당 환경별로 하나의 웹훅만 사용할 수 있으며, 모두 동일한 **Destination URL**로 전송됩니다. 브랜드마다 다른 URL을 설정할 수 있지만, 동일한 브랜드의 이벤트는 하나의 URL을 공유해야 합니다. Braze에서는 Olo와 함께 사용할 수 있는 변환을 하나만 만들 수 있습니다.

이 단일 변환 내에서 여러 Olo 이벤트를 처리하려면 각 웹훅의 `X-Olo-Event-Type` 헤더를 확인하세요. 이 헤더를 사용하면 다양한 Olo 이벤트를 조건부로 처리할 수 있습니다.

## 통합 {#integration}

### 1단계: Olo 테스트 이벤트를 수신할 Braze 데이터 변환 설정 {#step-1}

{% multi_lang_include data_activation/create_transformation.md location="default" %}

### 2단계: Olo 웹훅 설정 {#step-2-set-up-olo-webhooks}

Olo 대시보드 내 [셀프서비스 웹훅 도구](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks)를 사용하여 데이터 변환으로 전송할 웹훅을 설정합니다.

1. Braze로 전송할 이벤트를 선택합니다.
2. **Destination URL**을 설정합니다. 이 URL은 [1단계](#step-1)에서 생성한 데이터 변환 URL입니다.

{% alert note %}
`OAuth` 및 `X-Olo-Signature` 헤더 공유 비밀키는 변환에 필요하지 않습니다.
{% endalert %}

{:start="3"}
3. [테스트 이벤트](https://developer.olo.com/docs/load/webhooks#operation/test)를 데이터 변환으로 전송하여 웹훅이 올바르게 설정되었는지 확인합니다. [개발자 도구 권한](https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions)이 있는 Olo 대시보드 사용자만 테스트 이벤트를 전송할 수 있습니다.

Olo 웹훅 설정 프로세스를 완료하려면 먼저 테스트 이벤트 웹훅에서 성공 응답을 받아야 합니다.

### 3단계: 선택한 Olo 이벤트를 수신하는 변환 코드 작성 {#step-3-write-transformation-code-to-accept-your-chosen-olo-events}

이 단계에서는 소스 플랫폼에서 전송되는 웹훅 페이로드를 JavaScript 객체 반환 값으로 변환합니다.

1. 지원하려는 Olo 이벤트의 샘플 이벤트 페이로드와 함께 데이터 변환 URL로 요청을 전송합니다. 요청 형식에 대한 도움말은 [요청 본문 형식](#request-body-format)을 참조하세요.
2. 데이터 변환을 새로고침하고 **Webhook Details**에서 샘플 이벤트 페이로드를 확인할 수 있는지 확인합니다.
3. 선택한 Olo 이벤트를 지원하도록 데이터 변환 코드를 업데이트합니다.
4. **Validate**를 클릭하여 코드 출력의 미리 보기를 반환하고 이것이 유효한 `/users/track` 요청인지 확인합니다.
5. 데이터 변환을 저장하고 활성화합니다.

#### 요청 본문 형식 {#request-body-format}

이 반환 값은 Braze의 `/users/track` 요청 본문 형식을 준수해야 합니다:

{% multi_lang_include data_transformation/transformation_code_requirements.md %}

## Olo 웹훅을 위한 데이터 변환 예시 {#example-data-transformations-for-olo-webhooks}

이 섹션에는 시작 지점으로 사용할 수 있는 예시 템플릿이 포함되어 있습니다. 처음부터 시작하거나 필요에 따라 특정 구성 요소를 삭제할 수 있습니다.

각 템플릿에서 코드는 `/users/track` 요청을 구성하기 위해 `brazecall` 변수를 정의합니다.

`/users/track` 요청이 `brazecall`에 할당된 후, 출력을 생성하기 위해 `brazecall`을 명시적으로 반환합니다.

### 단일 이벤트 변환 {#single-event-transformation}

단일 Olo 이벤트만 지원하려는 경우 `X-Olo-Event-Type` 헤더를 사용하여 `/users/track` 요청 페이로드를 조건부로 생성할 필요가 없습니다. 예를 들어, Olo Order Placed 웹훅이 Braze로 전송될 때 사용자 프로필에 구매 이벤트 또는 커스텀 이벤트를 기록할 수 있습니다.

### 각 제품을 구매로 기록하기 {#logging-each-product-as-a-purchase}

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

### 커스텀 이벤트 기록하기 {#logging-a-custom-event}

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

## 다중 이벤트 변환 {#multi-event-transformation}

Olo는 각 웹훅의 `X-Olo-Event-Type` 헤더 내에 이벤트 유형을 전송합니다. 단일 변환 내에서 여러 Olo 웹훅 이벤트를 지원하려면, 이 헤더 유형의 값에 따라 웹훅 페이로드를 변환하는 조건 로직을 사용하세요.

다음 변환 예시에서 JavaScript는 `UserSignedUp` 및 `OrderPlaced` 이벤트에 대한 특정 페이로드를 생성합니다. 또한 `else` 조건은 `UserSignedUp` 및 `OrderPlaced`의 X-Olo-Event-Type 헤더 없이 Braze로 전송되는 모든 Olo 이벤트에 대한 페이로드를 처리합니다.

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

### 4단계: Olo 웹훅 게시하기 {#step-4-publish-your-olo-webhook}

Braze에서 데이터 변환을 활성화한 후, Olo 대시보드 내의 [셀프 서비스 웹훅 도구](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks)를 사용하여 웹훅을 게시합니다. 웹훅이 게시되면 데이터 변환이 Olo 웹훅 이벤트 메시지를 수신하기 시작합니다.

## 알아두어야 할 사항 {#things-to-know}

### 재시도 {#retries}

Olo는 HTTP 응답 상태 코드가 `429 - Too Many Requests`이거나 `5xx` 범위(예: 게이트웨이 타임아웃 또는 서버 오류)인 웹훅 호출을 요청을 삭제하기 전까지 24시간 동안 최대 50회 재시도합니다.

### 최소 1회 전달 {#at-least-once-delivery}

웹훅 호출의 HTTP 응답 상태 코드가 `429 - Too Many Requests`이거나 `5xx` 범위(예: 게이트웨이 타임아웃 또는 서버 오류)인 경우, Olo는 포기하기 전까지 24시간 동안 최대 50회 메시지를 재시도합니다.

따라서 가입자가 웹훅을 여러 번 수신할 수 있습니다. `X-Olo-Message-Id` 헤더를 확인하여 중복 항목을 무시하는 것은 가입자의 책임입니다.