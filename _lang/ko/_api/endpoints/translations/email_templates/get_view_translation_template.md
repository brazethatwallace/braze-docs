---
nav_title: "GET: 이메일 템플릿에 대한 모든 번역 및 로케일 보기"
article_title: "GET: 이메일 템플릿에 대한 모든 번역 및 로케일 보기"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "이 문서에서는 이메일 템플릿에 대한 모든 번역 및 로케일 보기 엔드포인트의 세부 정보를 설명합니다."
---

{% api %}
# 이메일 템플릿에 대한 모든 번역 및 로케일 보기 {#view-all-translations-and-locales-for-an-email-template}
{% apimethod get %}
/templates/email/translations/
{% endapimethod %}

> 이 엔드포인트를 사용하여 [이메일 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates)에 대한 모든 번역 및 로케일을 볼 수 있습니다. 번역 기능에 대한 자세한 내용은 [메시지 내 로케일]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)을 참조하세요.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `templates.translations.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 쿼리 매개변수 {#query-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---------------|----------|-----------|---------------------------------|
| `template_id` | 필수 | 문자열 | 이메일 템플릿의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="쿼리 매개변수" }

{% alert note %}
모든 번역 ID는 범용 고유 식별자(UUID)로 간주되며, GET 엔드포인트의 응답에서 확인할 수 있습니다.
{% endalert %}

## 요청 예시 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
--- template_id: "6ad1507f-ca10-44c4-95bf-6e4gay901kc5"
```

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429`의 네 가지가 있습니다.

### 성공 응답 예시 {#example-success-response}

`200` 상태 코드는 다음과 같은 응답 헤더와 본문을 반환할 수 있습니다.

```json
{
    "translations": [
        {
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            },
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            }
        },
        {
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            },
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            }
        }
    ]
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