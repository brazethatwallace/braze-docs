---
nav_title: "GET: 캔버스에 대한 번역 보기"
article_title: "GET: 캔버스에 대한 번역 보기"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 캔버스에 대한 번역 보기 엔드포인트에 대해 자세히 설명합니다."
---

{% api %}
# 캔버스에 대한 번역 보기 {#view-translation-for-a-canvas}
{% apimethod get %}
/canvas/translations
{% endapimethod %}

> 이 엔드포인트를 사용하여 Canvas의 번역된 메시지를 미리 볼 수 있습니다. 번역 기능에 대한 자세한 내용은 [메시지의 로케일]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)을 참조하세요.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `canvas.translations.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 쿼리 매개변수 {#query-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id` | 필수 | 문자열 | Canvas의 ID입니다. |
| `step_id` | 필수 | 문자열 | 캔버스 단계의 ID입니다. |
| `message_variation_id` | 필수 | 문자열 | 메시지 변형의 ID입니다. |
| `locale_id` | 선택 사항 | 문자열 | 로케일의 ID(UUID)입니다. |
| `post_launch_draft_version` | 선택 사항 | 부울 | `true`인 경우 최신 라이브 게시 버전 대신 최신 초안 버전을 반환합니다. 기본값은 `false`이며 최신 라이브 버전을 반환합니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Query parameters" }

{% alert note %}
모든 번역 ID는 범용 고유 식별자(UUID)로 간주되며, GET 엔드포인트의 응답에서 확인할 수 있습니다.
{% endalert %}

## 요청 예시 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429`의 네 가지가 있습니다.

### 성공 응답 예시 {#example-success-response}

`200` 상태 코드는 다음과 같은 응답 헤더와 본문을 반환할 수 있습니다.

```json
{
    "translations": [
        {
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
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