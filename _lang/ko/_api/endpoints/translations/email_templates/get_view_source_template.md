---
nav_title: "GET: 이메일 템플릿에 대한 소스 번역 보기"
article_title: "GET: 이메일 템플릿에 대한 소스 번역 보기"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 이메일 템플릿 엔드포인트에 대한 소스 번역 보기의 세부 정보를 설명합니다."
---

{% api %}
# 이메일 템플릿에 대한 소스 번역 보기 {#view-the-source-translations-for-an-email-template}
{% apimethod get %}
/templates/email/translations/source
{% endapimethod %}

> 이 엔드포인트를 사용하여 [이메일 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/)에 대한 소스 번역을 볼 수 있습니다. 번역 기능에 대한 자세한 정보는 [메시지 내 로케일]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)을 참조하세요.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `templates.email.info` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 쿼리 매개변수 {#query-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---------------|----------|-----------|---------------------------------|
| `template_id` | 필수 | 문자열 | 이메일 템플릿의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Query parameters" }

## 예시 요청 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source?template_id={template_id}'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"
```

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429`의 네 가지가 있습니다.

### 성공 응답 예시 {#example-success-response}

`200` 상태 코드는 다음과 같은 응답 헤더와 본문을 반환할 수 있습니다.

```json
{
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
        }
    },
    "message": "success"
}
```

### 오류 응답 예시 {#example-error-response}

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결](#troubleshooting)을 참조하세요.

```json
{
    "errors": [
        {
            "message": "The provided locale code does not exist."
        }
    ]
}
```

{% endapi %}