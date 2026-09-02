---
nav_title: "GET: 사용자 구독 그룹 나열하기"
article_title: "GET: 사용자의 구독 그룹 나열"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 사용자의 구독 그룹 나열 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자의 구독 그룹 나열 {#list-users-subscription-groups}
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> 이 엔드포인트를 사용하여 특정 사용자의 기록이 있는 구독 그룹을 나열하고 가져올 수 있습니다.

**이메일 구독 그룹**에 대한 이 엔드포인트의 예제를 보거나 테스트하려면 다음을 참조하세요:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

**SMS 구독 그룹**에 대한 이 엔드포인트의 예제를 보거나 테스트하려면 다음을 참조하세요:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

**WhatsApp 그룹**에 대한 이 엔드포인트의 예제를 보거나 테스트하려면 다음을 참조하세요:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `subscription.groups.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `external_id` | 필수 | 문자열 | 사용자의 `external_id`입니다(최소 1개, 최대 50개의 `external_ids`를 포함해야 합니다). |
| `email` | 필수* | 문자열 | 사용자의 이메일 주소이며, 문자열 배열로 전달할 수 있습니다. 이메일 주소를 하나 이상(최대 50개) 포함해야 합니다. |
| `phone` | 필수* | [E.164](https://en.wikipedia.org/wiki/E.164) 형식의 문자열 | 사용자의 전화번호입니다. 전화번호를 하나 이상(최대 50개) 포함해야 합니다. |
| `limit` | 선택 사항 | 정수 | 반환되는 최대 결과 수에 대한 제한입니다. 기본값(및 최대값) `limit`은 100입니다. |
| `offset` | 선택 사항 | 정수 | 검색 기준에 맞는 나머지 템플릿을 반환하기 전에 건너뛸 템플릿의 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

{% alert tip %}
동일한 이메일 주소를 공유하는 사용자(여러 `external_ids`)가 여러 명인 경우, 모든 사용자가 별도의 사용자로 반환됩니다(동일한 이메일 주소 또는 구독 그룹을 가지고 있더라도).
{% endalert %}

## 요청 예시 {#example-request}

{% tabs %}
{% tab 다중 사용자 %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS 및 WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab 이메일 %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@example.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 응답 예시 {#example-response}

사용자 기록에서 구독 상태 업데이트가 있었던 구독 그룹만 성공적인 응답에 포함됩니다. 즉, 새로 생성된 구독 그룹은 나열되지 않습니다.

```json
{
    "users": [
        {
            "email": "test@example.com",
            "phone": "+11112223333",
            "external_id": "external_identifier",
            "subscription_groups": [
                {
                  "id": "ec2fcc919fca",
                  "name": "ActivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "7d7af9dd5556",
                  "name": "ReactivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "a5e84fd16220",
                  "name": "MarketingGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "64d8cad9176c",
                  "name": "TransactionalGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "b2134cd63942",
                  "name": "BankerMarketingGroup",
                  "channel": "sms",
                  "status": "Subscribed"
                }
            ]
        }
    ],
    "total_count": 1,
    "message": "success"
}
```

{% endapi %}