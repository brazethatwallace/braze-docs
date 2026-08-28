---
nav_title: "PUT: 웹훅 템플릿 번역 업데이트"
article_title: "PUT: 웹훅 템플릿 번역 업데이트"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "이 문서에서는 웹훅 템플릿의 번역을 업데이트하는 엔드포인트에 대해 설명합니다."
---

{% api %}
# 웹훅 템플릿 번역 업데이트 {#update-translations-for-a-webhook-template}
{% apimethod put %}
/templates/webhook/translations
{% endapimethod %}

> 이 엔드포인트를 사용하여 [웹훅 템플릿]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)의 번역을 업데이트할 수 있습니다. 번역 기능에 대한 자세한 내용은 [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)를 참조하세요.

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `templates.translations.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 경로 매개변수 {#path-parameters}

이 엔드포인트에는 경로 매개변수가 없습니다.

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `template_id` | 필수 | 문자열 | 웹훅 템플릿의 ID입니다. |
| `locale_id` | 필수 | 문자열 | 업데이트할 로케일의 UUID입니다. 로케일은 웹훅 템플릿에 대해 설정되어 있어야 합니다. |
| `translation_map` | 필수 | 객체 | 업데이트된 번역을 포함하는 객체입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}

```bash
curl --location --request PUT 'https://rest.iad-03.braze.com/templates/webhook/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
  "locale_id": "a14404b3-3626-4de0-bdec-06935f3aa0ad",
  "translation_map": {
    "id_0": "¡Hola!",
    "id_1": "¿Te gustaría comprar esto?"
  }
}'
```

## 응답 {#response}

이 엔드포인트에는 `200`, `400`, `403`, `404`, `429` 다섯 가지 상태 코드 응답이 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음과 같은 빈 응답 본문을 반환합니다.

```json
{}
```

### 오류 응답 예시 {#example-error-response}

상태 코드 `400`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "Locale not found"
}
```

{% endapi %}