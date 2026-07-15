---
nav_title: "POST: 스팸 목록에서 이메일 주소 제거"
article_title: "POST: 스팸 목록에서 이메일 주소 제거"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "이 문서에서는 스팸 목록에서 이메일 주소 제거 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 스팸 목록에서 이메일 주소 제거 {#remove-email-addresses-from-spam-list}
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> 이 엔드포인트를 사용하여 Braze 스팸 목록 및 이메일 제공업체가 관리하는 스팸 목록에서 이메일 주소를 제거할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `email.spam.remove` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문 {#request-body}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@example.com"
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| ----------|-----------| --------|------- |
| `email` | 필수 | 문자열 또는 배열 | 수정할 이메일 주소 문자열 또는 수정할 이메일 주소를 최대 50개까지 포함하는 배열입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@example.com"
}'
```
{% endapi %}