---
nav_title: 모의 JSON으로 메시지 테스트
article_title: 미리보기에서 모의 JSON으로 메시지 테스트
page_order: 1
page_type: reference
description: "Liquid capture와 json_parse를 사용하여 Campaign을 시작하거나 테스트 메시지를 보내지 않고도 메시지 작성기 미리보기에서 연결된 콘텐츠 또는 항목 스타일 JSON을 모의 테스트할 수 있습니다."
---

# 미리보기에서 모의 JSON으로 메시지 테스트 {#test-messages-with-mock-json-in-preview}

> `capture`와 `json_parse`를 사용하여 메시지 내에서 API 또는 항목 스타일 JSON을 모의 구성하면, Campaign을 시작하거나 Canvas를 트리거하거나 실시간으로 연결된 콘텐츠를 호출하기 전에 작성기 미리보기에서 Liquid와 레이아웃을 검증할 수 있습니다.

## 이 예제 소개 {#about-this-example}

의류 소매 브랜드인 Flash & Thread는 연결된 콘텐츠 응답, Canvas 컨텍스트 변수 또는 프로필의 객체 배열 데이터에 의존하는 메시지를 작성합니다. 매번 반복할 때마다 실제 API 호출을 트리거하거나 Campaign을 시작하면 개발 속도가 느려집니다.

이 패턴은 메시지 본문에 모의 JSON 페이로드를 삽입하고, `capture`로 저장한 다음 `json_parse`로 파싱하여 **미리보기** 섹션에서 Liquid가 구조화된 필드를 참조할 수 있도록 합니다. 실시간 연결된 콘텐츠 호출, API 트리거 Canvas 진입 또는 테스트 전송이 필요하지 않습니다.

이 방법은 메시지 개발 중에 사용합니다. 실제 트리거, 테스트 전송 또는 Canvas의 [사용자 경로 미리보기]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)를 통한 포괄적인 테스트를 대체하지는 않습니다.

## 고려 사항 {#considerations}

- 이 접근 방식은 개발 중 작성기 미리보기를 지원합니다. 고객에게 발송하기 전에 테스트 전송과 실시간 경로 확인을 실행하세요.
- `capture` 블록만으로는 JSON이 문자열로 저장됩니다. **`json_parse`**를 적용한 후에만 필드를 참조하세요. 그렇지 않으면 미리보기 출력이 비어 있을 수 있습니다.
- 모의 JSON은 유효해야 합니다. 유효하지 않은 JSON은 `json_parse`가 실패하거나 예상치 못한 구조를 반환하게 합니다.
- 발송 전에 모의 블록을 교체하거나 제거하세요. 또는 프로덕션 Liquid를 보호하여 모의 데이터가 미리보기에서만 사용되도록 하세요(예: 출시 전에 삭제하는 주석 플래그 사용).
- 이 문서의 Liquid 스니펫은 예시입니다. 실제 채널과 실제 페이로드 형태로 테스트하세요.
- 프로덕션에서 연결된 콘텐츠를 사용할 때는 모의 블록을 제거하고 실시간 URL 태그를 사용하세요. [API 호출하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)를 참조하세요.

## 설정 {#setup}

이 예제는 `listings`를 반복하는 이메일에 대해 연결된 콘텐츠 스타일의 제품 목록 응답을 모의 구성합니다.

### 1단계: 메시지에서 모의 JSON 캡처 {#step-1-capture-mock-json-in-the-message}

`capture`를 사용하여 JSON 문자열을 저장합니다. 블록 내에서 유효한 JSON 구문(키와 문자열 값에 큰따옴표)을 사용하세요.

{% raw %}
```liquid
{% capture mock_response %}
{
  "success": true,
  "listings": [
    {
      "id": 45731,
      "name": "Summit Trail Jacket",
      "image_url": "https://example.com/images/trail-jacket.png",
      "price": {
        "actual": "89.00",
        "currency": "USD"
      },
      "link": "https://example.com/products/trail-jacket",
      "product_category": "Outerwear",
      "properties": {
        "size": "L",
        "colour": "Navy",
        "limited_edition": false
      },
      "out_of_stock": false
    }
  ]
}
{% endcapture %}
```
{% endraw %}

### 2단계: json_parse로 JSON 파싱 {#step-2-parse-json-with-json_parse}

파싱된 구조를 메시지의 나머지 부분에서 참조할 변수에 할당합니다.

{% raw %}
```liquid
{% assign response_json = mock_response | json_parse %}
```
{% endraw %}

`json_parse` 없이 캡처된 문자열에 점 표기법을 사용하면(예: {% raw %}`{{ mock_response.listings }}`{% endraw %}) 미리보기에서 일반적으로 빈 값이 렌더링됩니다.

### 3단계: Liquid에서 파싱된 필드 참조 {#step-3-reference-parsed-fields-in-liquid}

파싱된 배열을 반복하고 실시간 API 응답에서와 동일하게 필드를 렌더링합니다.

{% raw %}
```liquid
{% for listing in response_json.listings %}
{{ listing.name }} — {{ listing.price.actual }} {{ listing.price.currency }}
{% endfor %}
```
{% endraw %}

메시지 작성기의 **미리보기** 섹션으로 이동하여 필드가 렌더링되는지 확인합니다.

### 4단계: 다른 JSON 형태에 동일한 패턴 적용 {#step-4-apply-the-same-pattern-to-other-json-shapes}

동일한 `capture` + `json_parse` 흐름을 사용하여 다음을 모의 구성합니다.

| 테스트하려는 데이터 | 모의 JSON 형태 |
| --- | --- |
| Canvas 컨텍스트 변수 | 메시지에서 예상하는 속성정보 키가 포함된 객체 |
| 프로필의 객체 배열 | 커스텀 속성과 동일한 키를 가진 객체의 JSON 배열 |
| 연결된 콘텐츠 응답 | 이전에 성공한 호출에서 저장한 샘플 API JSON |
{: .reset-td-br-1 .reset-td-br-2 aria-label="테스트하려는 데이터와 JSON 형태" }

발송 전에 모의 변수를 프로덕션 Liquid(Canvas 컨텍스트 변수, 커스텀 속성 또는 연결된 콘텐츠 태그)로 교체하세요.

## 관련 문서 {#related-articles}

- [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)
- [Canvas에서 사용자 경로 미리보기]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)
- [고급 Liquid 필터(`json_parse`)]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)
- [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [객체 배열]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)
- [컨텍스트 변수]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)