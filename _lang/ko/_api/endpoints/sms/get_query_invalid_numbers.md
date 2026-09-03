---
nav_title: "GET: 유효하지 않은 전화번호 조회"
article_title: "GET: 유효하지 않은 전화번호 조회"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 유효하지 않은 전화번호를 조회하는 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."
---
{% api %}
# 유효하지 않은 전화번호 조회 {#query-invalid-phone-numbers}
{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

> 이 엔드포인트를 사용하여 특정 기간 내에 "유효하지 않음"으로 표시된 전화번호 목록을 가져올 수 있습니다. 자세한 내용은 [유효하지 않은 전화번호 처리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers) 설명서를 참조하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `sms.invalid_phone_numbers` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| ----------|-----------| ----------|----- |
| `start_date` | 선택 사항 <br>(참고 참조) | YYYY-MM-DD 형식의 문자열 | 유효하지 않은 전화번호를 검색할 범위의 시작 날짜로, `end_date`보다 이전이어야 합니다. API에서 UTC 시간 기준 자정으로 처리됩니다. |
| `end_date` | 선택 사항 <br>(참고 참조) | YYYY-MM-DD 형식의 문자열 | 유효하지 않은 전화번호를 검색할 범위의 종료 날짜입니다. API에서 UTC 시간 기준 자정으로 처리됩니다. |
| `limit` | 선택 사항 | 정수 | 반환되는 결과 수를 제한하는 선택적 필드입니다. 기본값은 100이며, 최대값은 500입니다. |
| `offset` | 선택 사항 | 정수 | 검색을 시작할 목록의 시작점입니다(선택 사항). |
| `phone_numbers` | 선택 사항 <br>(참고 참조) | e.164 형식의 문자열 배열 | 제공된 경우, 해당 전화번호가 유효하지 않은 것으로 확인되면 반환합니다. |
| `reason` | 선택 사항 <br>(참고 참조) | 문자열 | 사용 가능한 값은 "provider_error"(공급자 오류로 인해 해당 전화기에서 SMS를 수신할 수 없음) 또는 "deactivated"(전화번호가 비활성화됨)입니다. 생략하면 모든 사유가 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

{% alert note %}
`start_date`와 `end_date` 또는 `phone_numbers` 중 하나를 제공해야 합니다. 세 가지를 모두 제공하면 지정된 전화번호를 우선시하고 날짜 범위는 무시합니다.
{% endalert %}

날짜 범위에 유효하지 않은 전화번호가 `limit` 개수보다 많은 경우, 매번 `offset`을 늘려가며 `limit`보다 적거나 결과가 0이 될 때까지 여러 번 API를 호출해야 합니다.

## 요청 예시 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 응답 {#response}
항목은 내림차순으로 나열됩니다.

```json
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "deactivated"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    }
  ],
  "message": "success"
}
```
{% endapi %}