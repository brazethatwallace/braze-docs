---
nav_title: "PUT: 이메일 템플릿에 대한 번역 업데이트"
article_title: "PUT: 이메일 템플릿에 대한 번역 업데이트"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "이 문서에서는 이메일 템플릿에 대한 번역 업데이트 엔드포인트에 대한 세부 정보를 설명합니다."
---

{% api %}
# 이메일 템플릿에 대한 번역 업데이트 {#update-translations-for-an-email-template}
{% apimethod put %}
/templates/email/translations/
{% endapimethod %}

> 이 엔드포인트를 사용하여 [이메일 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates)에 대한 번역을 업데이트합니다. 번역 기능에 대한 자세한 내용은 [메시지의 로케일]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)을 참조하세요.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `templates.translations.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 경로 매개변수 {#path-parameters}

이 엔드포인트에는 경로 매개변수가 없습니다.

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `template_id` | 필수 | 문자열 | 이메일 템플릿의 ID입니다. |
| `locale_id` | 필수 | 문자열 | 로케일의 ID입니다. |
| `translations_map` | 필수 | 문자열 | 이메일 템플릿에 대한 번역 맵입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

{% alert note %}
모든 번역 ID는 범용 고유 식별자(UUID)로 간주되며, GET 엔드포인트의 응답에서 확인할 수 있습니다.
{% endalert %}

## 요청 예시 {#example-request}

```json
{
    "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "Me llamo Jacky",
        "id_2": "¿Dónde está la biblioteca?"
    }
}
```

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429`의 네 가지가 있습니다.

### 성공 응답 예시 {#example-success-response}

```json
{
    "message": "success"
}
```

### 오류 응답 예시 {#example-error-response}

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결](#troubleshooting)을 참조하세요.

```json
{
	"errors": [
		{
			"id": "1234567-abc-123-012345678",
			"message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
		}
	]
}
```

{% endapi %}