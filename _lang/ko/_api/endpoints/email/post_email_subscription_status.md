---
nav_title: "POST: 이메일 구독 상태 변경"
article_title: "POST: 이메일 구독 상태 변경"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "이 문서에서는 사용자의 이메일 구독 상태 변경 Braze 엔드포인트에 대한 세부 정보를 설명합니다."

---
{% api %}
# 이메일 구독 상태 변경 {#change-email-subscription-status}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/status
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용자의 이메일 구독 상태를 설정할 수 있습니다.

사용자는 `opted_in`, `unsubscribed` 또는 `subscribed`(명시적으로 옵트인 또는 옵트아웃하지 않은 상태)일 수 있습니다.

Braze 내에서 아직 사용자와 연결되지 않은 이메일 주소의 이메일 구독 상태를 설정할 수 있습니다. 나중에 해당 이메일 주소가 사용자와 연결되면 업로드한 이메일 구독 상태가 자동으로 설정됩니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `email.status` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `email` | 필수 | 문자열 또는 배열 | 수정할 이메일 주소를 문자열로 입력하거나, 수정할 이메일 주소를 최대 50개까지 배열로 입력할 수 있습니다. |
| `subscription_state` | 필수 | 문자열 | "subscribed", "unsubscribed" 또는 "opted_in" 중 하나입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## SendGrid 이메일 차단 문제 해결 {#troubleshooting-sendgrid-email-blocks}

SendGrid가 수신자를 차단하는 경우, 이 엔드포인트를 사용하여 구독 상태를 업데이트하고 세그먼트 필터로 참여를 검토하세요. 전달 가능성 모니터링을 위해 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) 소프트 반송 이벤트를 활용하고, 재발송 전에 구독 상태를 확인하세요.

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}