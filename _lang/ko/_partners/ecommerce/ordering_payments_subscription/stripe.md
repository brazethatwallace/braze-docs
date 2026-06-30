---
nav_title: Stripe
article_title: Stripe
description: "이 문서에서는 Braze와 Stripe 간의 파트너십에 대해 설명합니다."
alias: /partners/stripe/
page_type: partner
search_tag: Partner
---

# Stripe

> [Stripe](https://www.stripe.com/)는 통합 API 및 서비스 제품군을 통해 기업이 결제를 수락하고, 매출 운영을 관리하며, 글로벌 커머스를 촉진할 수 있도록 지원하는 종합 금융 인프라 플랫폼입니다.

Braze와 Stripe를 통합하면 다음을 수행할 수 있습니다.

- Stripe의 실시간 결제 및 청구 데이터로 Braze의 고객 프로필을 업데이트합니다.
- 체험판 시작, 구독 활성화, 구독 취소 등 Stripe 이벤트를 기반으로 Braze에서 메시징을 트리거합니다.
- Stripe 웹훅을 통해 수신한 사용자의 결제 내역 또는 청구 상태를 기반으로 Braze 메시징을 개인화합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Stripe 계정 | 이 파트너십을 활용하려면 웹훅에 접근할 수 있는 Stripe 계정이 필요합니다. |
| Braze 데이터 변환 | Stripe에서 데이터를 수신하려면 [데이터 변환 URL]({{site.baseurl}}/data_transformation)이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Stripe 웹훅을 수신하기 위한 Braze 데이터 변환 설정 {#step-1}

{% multi_lang_include data_activation/create_transformation.md %}

### 2단계: Stripe 웹훅 설정 {#step-2-set-up-stripe-webhooks}

[Stripe 웹훅 설명서](https://docs.stripe.com/development/dashboard/webhooks)의 단계를 따라 웹훅을 설정합니다.

데이터 변환 웹훅 URL을 **Destination URL**로 추가하고 Braze로 전송할 이벤트 유형을 선택합니다. 전체 이벤트 유형 목록은 [Stripe 설명서](https://docs.stripe.com/api/events/types)를 참조하세요.

![Stripe 웹훅 구성 예시.]({% image_buster /assets/img/stripe/stripe_webhook_configuration.png %}){: style="max-width:80%;"}

그런 다음 데이터 변환으로 테스트 이벤트를 전송합니다.

### 3단계: 선택한 Stripe 이벤트를 수신하기 위한 변환 코드 작성 {#step-3-write-transformation-code-to-accept-your-chosen-stripe-events}

다음으로, Stripe에서 전송되는 웹훅 페이로드를 JavaScript 오브젝트 반환 값으로 변환합니다.

1. 데이터 변환을 새로고침하고 **Webhook details** 섹션에서 Stripe 테스트 페이로드를 확인할 수 있는지 확인합니다.
2. 선택한 Stripe 이벤트를 지원하도록 데이터 변환 코드를 업데이트합니다.
3. **Validate**를 선택하여 코드 출력의 미리보기를 반환하고 유효한 `/users/track` 요청인지 확인합니다.
4. 데이터 변환을 저장하고 활성화합니다.

![웹훅 세부 정보 및 변환 코드의 예시.]({% image_buster /assets/img/stripe/stripe_data_transformation.png %})

#### 요청 본문 형식 {#request-body-format}

이 반환 값은 `/users/track` 엔드포인트 요청 본문 형식을 준수해야 합니다.

- 변환 코드는 JavaScript 프로그래밍 언어로 작성됩니다. if/else 로직과 같은 모든 표준 JavaScript 제어 흐름이 지원됩니다.
- 변환 코드는 payload 변수를 사용하여 웹훅 요청 본문에 접근합니다. 이 변수는 요청 본문 JSON을 파싱하여 채워진 오브젝트입니다.
- `/users/track` 엔드포인트에서 지원하는 모든 기능이 지원되며, 다음을 포함합니다.
    - 사용자 속성 오브젝트, 이벤트 오브젝트 및 구매 오브젝트
    - 중첩 속성 및 중첩 커스텀 이벤트 등록정보
    - 구독 그룹 업데이트
    - 식별자로서의 이메일 주소

### 4단계: Stripe 웹훅 게시 {#step-4-publish-your-stripe-webhook}

데이터 변환을 작성한 후 **Validate**를 선택하여 데이터 변환 코드가 올바르게 포맷되었는지, 예상대로 작동하는지 확인합니다. 그런 다음 데이터 변환을 저장하고 활성화합니다. 활성화 후 사용자가 이벤트를 완료하면 커스텀 이벤트 데이터가 해당 사용자의 프로필에 기록됩니다.

![Braze 고객 프로필에 표시된 Stripe 커스텀 이벤트 "Charge Succeeded".]({% image_buster /assets/img/stripe/stripe_braze_profile_event.png %}){: style="max-width:80%;"}

## Stripe 웹훅 페이로드 예시 {#example}

```json
{
 "headers": {
   "Version": "HTTP/1.1",
   "X-Datadog-Trace-Id": "9124157397962821303",
   "X-Datadog-Parent-Id": "9124157397962821303",
   "X-Datadog-Sampling-Priority": "2",
   "Host": "xxx",
   "X-Request-Id": "xxx",
   "X-Real-Ip": "165.159.72.690",
   "X-Forwarded-For": "161.123.56.890",
   "X-Forwarded-Host": "xxx",
   "X-Forwarded-Port": "443",
   "X-Forwarded-Proto": "https",
   "X-Forwarded-Scheme": "https",
   "X-Scheme": "https",
   "X-Original-Forwarded-For": "12.345.678.123",
   "Cf-Ray": "9470a06172f8816e-IAD",
   "Cache-Control": "no-cache",
   "User-Agent": "Stripe/1.0 (+https://stripe.com/docs/webhooks)",
   "Accept-Encoding": "gzip",
   "Cf-Connecting-Ip": "12.123.456.789",
   "Cf-Visitor": "{\"scheme\":\"https\"}",
   "X-Worker-Executions": "1",
   "Cf-Worker": "xxx",
   "X-Fastly-Geoloc-Countrycode": "US",
   "Stripe-Signature": "t=xxx,v1=xxxx,v0=xxxx",
   "Cf-Ew-Via": "15",
   "Cdn-Loop": "cloudflare; loops=1; subreqs=1",
   "Accept": "*/*; q=0.5, application/xml"
 },
 "payload": {
   "id": "evt_3RTqw0RMEOaIvYpU1k2TFajH",
   "object": "event",
   "api_version": "2025-04-30.basil",
   "created": 1748465448,
   "data": {
     "object": {
       "id": "ch_3RTqw0RMEOaIvYpU1M9ZYtjP",
       "object": "charge",
       "amount": 100,
       "amount_captured": 100,
       "amount_refunded": 0,
       "application": null,
       "application_fee": null,
       "application_fee_amount": null,
       "balance_transaction": null,
       "billing_details": {
         "address": {
           "city": null,
           "country": null,
           "line1": null,
           "line2": null,
           "postal_code": null,
           "state": null
         },
         "email": null,
         "name": null,
         "phone": null,
         "tax_id": null
       },
       "calculated_statement_descriptor": "Stripe",
       "captured": true,
       "created": 1748465448,
       "currency": "usd",
       "customer": "cus_SOeDf39aosGb97",
       "description": "(created by Stripe CLI)",
       "destination": null,
       "dispute": null,
       "disputed": false,
       "failure_balance_transaction": null,
       "failure_code": null,
       "failure_message": null,
       "fraud_details": {},
       "livemode": false,
       "metadata": {},
       "on_behalf_of": null,
       "order": null,
       "outcome": {
         "advice_code": null,
         "network_advice_code": null,
         "network_decline_code": null,
         "network_status": "approved_by_network",
         "reason": null,
         "risk_level": "normal",
         "risk_score": 9,
         "seller_message": "Payment complete.",
         "type": "authorized"
       },
       "paid": true,
       "payment_intent": "pi_3RTqw0RMEOaIvYpU1pQl3Lmp",
       "payment_method": "pm_1RTqw0RMEOaIvYpU5VE8HFlp",
       "payment_method_details": {
         "card": {
           "amount_authorized": 100,
           "authorization_code": null,
           "brand": "visa",
           "checks": {
             "address_line1_check": null,
             "address_postal_code_check": null,
             "cvc_check": "pass"
           },
           "country": "US",
           "exp_month": 5,
           "exp_year": 2026,
           "extended_authorization": {
             "status": "disabled"
           },
           "fingerprint": "HAKdyqJ9xh2YhbzT",
           "funding": "credit",
           "incremental_authorization": {
             "status": "unavailable"
           },
           "installments": null,
           "last4": "4242",
           "mandate": null,
           "multicapture": {
             "status": "unavailable"
           },
           "network": "visa",
           "network_token": {
             "used": false
           },
           "network_transaction_id": "726575100121113",
           "overcapture": {
             "maximum_amount_capturable": 100,
             "status": "unavailable"
           },
           "regulated_status": "unregulated",
           "three_d_secure": null,
           "wallet": null
         },
         "type": "card"
       },
       "radar_options": {},
       "receipt_email": null,
       "receipt_number": null,
       "receipt_url": "https://pay.stripe.com/receipts/payment/xxx",
       "refunded": false,
       "review": null,
       "shipping": null,
       "source": null,
       "source_transfer": null,
       "statement_descriptor": null,
       "statement_descriptor_suffix": null,
       "status": "succeeded",
       "transfer_data": null,
       "transfer_group": null
     }
   },
   "livemode": false,
   "pending_webhooks": 3,
   "request": {
     "id": "req_jqtL1Q6CPaNx8x",
     "idempotency_key": "f0f9aee4-a889-4fcc-bc2e-fa41fa426f05"
   },
   "type": "charge.succeeded"
 }
}
```

## 데이터 변환 활용 사례 {#data-transformation-use-cases}

다음은 [Stripe 웹훅 페이로드 예시](#example)를 사용하여 구축한 예시 템플릿입니다. 이 템플릿을 시작점으로 사용할 수 있습니다. 처음부터 시작하거나 필요에 따라 특정 구성요소를 삭제할 수 있습니다.

이 예시 템플릿에서는 Braze 프로필에 커스텀 이벤트를 기록합니다. 이벤트 유형은 커스텀 이벤트 이름으로 전송되고, 데이터 오브젝트는 이벤트 등록정보로 전달됩니다.

### 활용 사례: customer를 식별자로 사용 {#use-case-customer-as-an-identifier}

이 예시 템플릿에서는 customer 필드를 식별자로 사용합니다.

{% tabs local %}
{% tab 입력 %}

```javascript

/* This template is based on the source platform's documentation here: https://stripe.com/docs/webhooks


/* Braze's /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Stripe's charge succeeded event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.data.object.created;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();


/* defines a variable 'brazecall' that will hold the request payload for the /users/track request
let brazecall;


/* if the type is charge.succeeded and customer field is not null, build the /users/track request to log an event to the user profile
if (payload.type == "charge.succeeded" && payload.data.object.customer) {
 brazecall = {
   "events": [
     {
       "external_id": payload.data.object.customer,
       "name": "Charge Succeeded",
       "time": isoString,
       "properties": {
         "amount": payload.data.object.amount,
         "paid": payload.data.object.paid,
         "status": payload.data.object.status
       }
     }
   ]
 };
}
/* After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab 출력 %}

```json
{
  "events": [
    {
      "external_id": "an_account@example.com",
      "name": "Charge Succeeded",
      "time": "2025-05-28T18:21:39.527Z",
      "properties": {
        "amount": 100,
    "paid":true,
    "Status":"succeeded"
    }
   }
  ]
}
```

{% endtab %}
{% endtabs %}

## 모니터링 및 문제 해결 {#monitoring-and-troubleshooting}

변환 모니터링 및 문제 해결에 대한 자세한 내용은 [변환 모니터링]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-5-monitor-your-transformation)을 참조하세요.