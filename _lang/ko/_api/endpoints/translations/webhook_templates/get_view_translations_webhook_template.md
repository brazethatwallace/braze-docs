---
nav_title: "GET: 웹훅 템플릿의 번역 보기"
article_title: "GET: 웹훅 템플릿의 번역 보기"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "이 문서에서는 웹훅 템플릿의 번역을 보기 위한 엔드포인트에 대해 설명합니다."
---

{% api %}
# 웹훅 템플릿의 번역 보기 {#view-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations
{% endapimethod %}

> 이 엔드포인트를 사용하여 [웹훅 템플릿]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)의 번역을 볼 수 있습니다. 구성된 모든 로케일을 반환하거나 로케일별로 응답을 필터링할 수 있습니다. 번역 기능에 대한 자세한 내용은 [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)를 참조하세요.

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `templates.translations.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 쿼리 매개변수 {#query-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `template_id` | 필수 | 문자열 | 웹훅 템플릿의 ID입니다. |
| `locale_id` | 선택 사항 | 문자열 | 반환할 로케일 UUID입니다. 생략하면 웹훅 템플릿에 구성된 모든 로케일이 응답에 포함됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="쿼리 매개변수" }

## 요청 예시 {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations?template_id={TEMPLATE_ID}&locale_id={LOCALE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

*`TEMPLATE_ID`*를 웹훅 템플릿의 ID로, *`LOCALE_ID`*를 반환하려는 로케일의 UUID로 바꾸세요. 구성된 모든 로케일을 반환하려면 `locale_id`를 생략하세요.

## 응답 {#response}

이 엔드포인트에는 `200`, `400`, `403`, `404`, `429`의 다섯 가지 상태 코드 응답이 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "translations": [
    {
      "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "¿Te gustaría comprar esto?"
      },
      "locale": {
        "uuid": "c7c12345-de35-1234-5678-abcdefa99a3f",
        "name": "es-MX",
        "country": "MX",
        "language": "es",
        "locale_key": "es-mx"
      }
    },
    {
      "translation_map": {
        "id_0": "你好！",
        "id_1": "你想買這個嗎？"
      },
      "locale": {
        "uuid": "a1b12345-cd35-1234-5678-abcdefa99a3f",
        "name": "zh-HK",
        "country": "HK",
        "language": "zh",
        "locale_key": "zh-hk"
      }
    }
  ]
}
```

### 오류 응답 예시 {#example-error-response}

상태 코드 `400`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "Invalid locale ID"
}
```

{% endapi %}