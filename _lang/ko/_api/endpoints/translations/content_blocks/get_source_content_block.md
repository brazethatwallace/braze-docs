---
nav_title: "GET: 콘텐츠 블록 번역 태그의 기본 소스 값 보기"
article_title: "GET: 콘텐츠 블록 번역 태그의 기본 소스 값 보기"
search_tag: Endpoint
page_order: 0

layout: api_page
page_type: reference
description: "이 문서에서는 콘텐츠 블록 번역 소스 엔드포인트에 대한 세부 정보를 설명합니다."
---

{% api %}
# 콘텐츠 블록의 번역 태그에 대한 기본 소스 값 보기 {#view-default-source-values-for-a-content-blocks-translation-tags}
{% apimethod get %}
/content_blocks/translations/source
{% endapimethod %}

> 이 엔드포인트를 사용하여 콘텐츠 블록의 번역 태그에 대한 모든 기본 번역 소스를 확인할 수 있습니다. 이 값은 {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %} 내의 값입니다. 번역 기능에 대한 자세한 내용은 [메시지의 로케일]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)을 참조하세요.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `content_blocks.translations.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 쿼리 매개변수 {#query-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | 필수 | 문자열 | 콘텐츠 블록의 ID입니다. |
| `locale_id` | 선택 사항 | 문자열 | 응답을 필터링할 로케일 UUID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Query parameters" }

{% alert note %}
모든 번역 ID는 범용 고유 식별자(UUID)로 간주되며, GET 엔드포인트의 응답에서 확인할 수 있습니다.
{% endalert %}

## 요청 예시 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations/source?content_block_id={content_block_id}&locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답 {#response}

이 엔드포인트에는 `200`, `400`, `404`, `429`의 네 가지 상태 코드 응답이 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음과 같은 응답 헤더와 본문을 반환할 수 있습니다.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Welcome!",
           "id_1": "Thank you for joining our program"
       }
   },
   "message": "success"
}
```

### 오류 응답 예시 {#example-error-response}

상태 코드 `400`은 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결](#troubleshooting)을 참조하세요.

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}