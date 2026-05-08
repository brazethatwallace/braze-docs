---
nav_title: 사용자 프로필 데이터 가져오기
article_title: 연결된 콘텐츠 호출에서 사용자 프로필 데이터 가져오기
page_order: 3
description: "이 문서에서는 사용자 프로필을 커넥티드 콘텐츠 호출로 가져오는 방법과 Liquid 템플릿과 관련된 모범 사례에 대해 설명합니다."
toc_headers: h2
---

# 연결된 콘텐츠 호출에서 사용자 프로필 데이터 가져오기 {#pull-user-profile-data-in-connected-content-calls}

> 이 페이지에서는 사용자 프로필을 커넥티드 콘텐츠 호출로 가져오는 방법과 Liquid 템플릿과 관련된 모범 사례를 다룹니다.

## 필수 조건 {#prerequisites}

연결된 콘텐츠 응답에 사용자 프로필 필드(Liquid 개인화 태그 내)가 포함된 경우, Liquid 패스백이 올바르게 렌더링되려면 해당 값이 메시지 내에서 연결된 콘텐츠 호출보다 먼저 Liquid로 정의되어야 합니다. 마찬가지로 요청에 `:rerender` 플래그가 포함되어야 합니다. `:rerender` 플래그는 한 단계 깊이까지만 적용되므로, 중첩된 연결된 콘텐츠 태그에는 적용되지 않습니다.

## 커넥티드 콘텐츠 호출의 Liquid 템플릿 {#liquid-templating-in-connected-content-calls}

개인화를 위해 Braze는 사용자 프로필 필드를 가져온 다음 해당 필드를 Liquid에 전달하므로, 커넥티드 콘텐츠의 응답에 사용자 프로필 필드가 포함된 경우 미리 정의해야 합니다.

예를 들어, 연결된 콘텐츠 호출이 다음과 같다면:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

연결된 콘텐츠 응답이 {% raw %}`Your language is ${language}`{% endraw %}인 경우, 이 예시에서 표시되는 콘텐츠는 `Hi Jon, your language is`입니다.

언어 자체는 템플릿으로 처리되지 않습니다. 이는 Braze가 연결된 콘텐츠 호출을 수행하기 전에 사용자로부터 어떤 필드를 가져올지 알아야 하기 때문입니다.

Liquid 패스백을 올바르게 렌더링하려면 다음 코드 스니펫에 표시된 것처럼 요청의 아무 곳에나 {% raw %}`${language}`{% endraw %} 태그를 포함해야 합니다. Liquid 전처리기가 사용자로부터 "language" 속성을 가져와 응답 템플릿에 사용할 수 있도록 준비합니다.

{%raw%}
```liquid
Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
`:rerender` 플래그 옵션은 한 단계 깊이까지만 적용된다는 점을 기억하세요. 연결된 콘텐츠 응답 자체에 추가 연결된 콘텐츠 태그나 카탈로그 태그가 포함된 경우, Braze는 해당 추가 태그를 다시 렌더링하지 않습니다.
{% endalert %}

## 모범 사례 {#best-practices}

### JSON 형식을 깨뜨릴 수 있는 Liquid 태그에 `json_escape` 사용하기 {#use-jsonescape-with-liquid-tags-that-could-break-the-json-format}

`:rerender`를 사용할 때는 JSON 형식을 깨뜨릴 수 있는 Liquid 태그에 `json_escape` 필터를 추가하세요. Liquid 태그에 JSON 형식을 깨뜨리는 문자가 포함된 경우, 전체 연결된 콘텐츠 응답이 텍스트로 해석되어 메시지에 템플릿으로 삽입되며, 어떤 변수도 저장되지 않습니다.

예를 들어, 아래 예시에서 `message` 이벤트 속성정보에 JSON 형식을 깨뜨릴 수 있는 문자가 포함된 경우, 다음 예시처럼 `json_escape` 필터를 추가하세요:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}