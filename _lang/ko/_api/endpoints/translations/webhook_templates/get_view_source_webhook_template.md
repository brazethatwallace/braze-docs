---
nav_title: "GET: 웹훅 템플릿의 소스 번역 조회"
article_title: "GET: 웹훅 템플릿의 소스 번역 조회"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 웹훅 템플릿의 소스 번역을 조회하는 엔드포인트에 대해 설명합니다."
---

{% api %}
# 웹훅 템플릿의 소스 번역 조회 {#view-source-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations/source
{% endapimethod %}

> 이 엔드포인트를 사용하여 [웹훅 템플릿]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)의 기본 소스 번역을 조회할 수 있습니다. 번역 기능에 대한 자세한 내용은 [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)를 참조하세요.

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `templates.translations.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 쿼리 매개변수 {#query-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `template_id` | 필수 | 문자열 | 웹훅 템플릿의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="쿼리 매개변수" }

## 요청 예시 {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations/source?template_id={TEMPLATE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

*`TEMPLATE_ID`*를 웹훅 템플릿의 ID로 대체하세요.

## 응답 {#response}

이 엔드포인트에는 `200`, `400`, `403`, `404`, `429`의 다섯 가지 상태 코드 응답이 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "translations": {
    "translation_map": {
      "id_0": "Hello!",
      "id_1": "Would you like to buy this?"
    }
  }
}
```

### 오류 응답 예시 {#example-error-response}

상태 코드 `400`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "This template does not have multi-language setup"
}
```

{% endapi %}