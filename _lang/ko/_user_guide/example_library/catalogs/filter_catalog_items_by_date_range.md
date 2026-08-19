---
nav_title: 날짜 범위로 필터링
article_title: 날짜 범위로 카탈로그 항목 필터링
page_order: 1
page_type: reference
description: "카탈로그 셀렉션과 Liquid 날짜 표현식을 사용하여 향후 7일 이내의 이벤트와 같이 롤링 시간 범위 내의 카탈로그 항목을 표시합니다."
---

# 날짜 범위로 카탈로그 항목 필터링 {#filter-catalog-items-by-date-range}

> 이 예제에서는 가상의 티켓 마켓플레이스가 카탈로그 셀렉션과 Liquid 날짜 표현식을 사용하여 발송 시점으로부터 향후 7일 이내에 예정된 이벤트만 소비자에게 이메일로 보내는 방법을 보여줍니다. 롤링 시간 필터가 적용된 셀렉션을 생성한 다음, 일치하는 카탈로그 항목을 Campaign 또는 Canvas 메시지에 렌더링합니다.

## 이 예제에 대하여 {#about-this-example}

가상의 티켓 마켓플레이스인 MovieCanon은 이 패턴을 사용하여 이메일 Campaign에 시간적으로 관련 있는 콘서트와 공연만 나열합니다.

이 패턴은 두 가지 Braze 기능을 함께 사용합니다:

- 발송 시점에 롤링 시간 범위를 계산하는 Liquid 스니펫을 값으로 사용하는 `time` 필드 필터가 포함된 [카탈로그 셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- 메시지 본문에서 일치하는 카탈로그 행을 렌더링하는 {% raw %}`{% catalog_selection_items %}`{% endraw %} Liquid 태그

## 고려 사항 {#considerations}

- 필터링할 날짜/시간 열에 대해 문자열 필드가 아닌 카탈로그 `time` 필드를 생성합니다. 값은 `2026-06-20T19:30:00Z`와 같은 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 형식으로 저장합니다. 지원되는 유형에 대해서는 [지원되는 데이터 유형]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types)을 참조하세요.
- `before` 및 `after` 연산자는 엄격한 비교를 사용합니다. 경계 타임스탬프와 정확히 같은 이벤트는 제외될 수 있습니다. 범위가 발송 시점에 시작되어야 하는 경우 전체 타임스탬프를 사용하세요. 날짜만 포함된 `YYYY-MM-DD` 값은 해당 날짜의 자정(UTC)으로 변환됩니다.
- 셀렉션 필터의 Liquid는 발송 시점에 평가됩니다. `'now'` 변수는 메시지가 렌더링되는 시점을 반영하며, 일반적으로 UTC 기준입니다. 시간대에 따라 결과 범위가 의도와 일치하는지 확인하세요.
- [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), 카탈로그 태그, `abort_message`는 카탈로그 셀렉션 필터 값에서 지원되지 않습니다. 필터에 허용되지 않는 태그가 포함되면 셀렉션은 오류를 발생시키지 않고 항목을 반환하지 않습니다.
- 셀렉션당 최대 10개의 필터를 추가하고 최대 50개의 항목을 반환할 수 있습니다. `'now'`에 추가되는 초 값을 변경하여 7일 범위를 조정합니다(`604800` = 7일 × `86400`초/일).
- 카탈로그 셀렉션 결과 배열은 0부터 시작합니다(`items[0]`이 첫 번째 항목).
- 프로덕션 오디언스에 발송하기 전에 프로덕션 워크스페이스 외부에서 필터 Liquid, 메시지 Liquid, 중단 로직을 테스트하세요.

## 설정 {#setup}

이 예제에서는 다음 필드가 포함된 `live_events`라는 카탈로그를 사용합니다:

| 필드 | 유형 | 예시 값 |
| ----- | ---- | ------------- |
| `id` | 문자열 | `show-1042` |
| `event_name` | 문자열 | `Summer Jazz Night` |
| `event_date_time` | Time | `2026-06-20T19:30:00Z` |
| `ticket_price` | Number | `45` |
| `city` | 문자열 | `Austin` |
| `venue` | 문자열 | `Riverside Amphitheater` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="카탈로그 필드" }

유사한 카탈로그가 아직 없다면 [카탈로그를 생성]({{site.baseurl}}/user_guide/data/activation/catalogs/create)하고 이벤트 데이터를 업로드하거나 동기화하세요.

### 1단계: 카탈로그 셀렉션 생성 {#step-1-create-the-catalog-selection}

1. **데이터 설정** > **카탈로그**로 이동하여 `live_events` 카탈로그를 선택합니다.
2. **셀렉션** 탭을 열고 **셀렉션 생성**을 선택합니다.
3. 셀렉션 이름을 `seven_day_window`로 지정하고 "향후 7일 이내에 발생하는 이벤트"와 같은 선택적 설명을 추가합니다.
4. 반환할 최대 이벤트 수에 대한 **결과 제한**을 설정합니다(최대 50개).
5. 아직 저장하지 마세요. 다음 단계에서 날짜 필터를 추가합니다.

### 2단계: 상한 필터 추가 {#step-2-add-the-upper-bound-filter}

`event_date_time` 필드에 필터를 추가합니다:

| 설정 | 값 |
| ------- | ----- |
| **필터 필드** | `event_date_time` |
| **연산자** | `before` |
| **값** | Liquid 스니펫 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="상한 필터 설정" }

필터 값 필드에 이 Liquid 스니펫을 입력합니다. 발송 시점으로부터 7일 후의 타임스탬프를 계산합니다:

{% raw %}
```liquid
{% assign seven_days = 'now' | date: '%s' | plus: 604800 %}{{ seven_days | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

이렇게 하면 해당 타임스탬프 이전의 이벤트만 포함되도록 범위의 상한이 설정됩니다.

### 3단계: 하한 필터 추가 {#step-3-add-the-lower-bound-filter}

동일한 필드에 두 번째 필터를 추가합니다:

| 설정 | 값 |
| ------- | ----- |
| **필터 필드** | `event_date_time` |
| **연산자** | `after` |
| **값** | Liquid 스니펫 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="하한 필터 설정" }

하한에 대해 이 Liquid 스니펫을 입력합니다. 현재 발송 시점을 사용하여 이미 시작된 이벤트를 제외합니다:

{% raw %}
```liquid
{{ 'now' | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

두 필터를 함께 사용하면 `event_date_time`이 현재 발송 시점 이후이고 발송 시점으로부터 7일 이전인 카탈로그 항목이 반환됩니다. **셀렉션 생성**을 선택하여 저장합니다.

### 4단계: 메시지에서 셀렉션 참조 {#step-4-reference-the-selection-in-a-message}

Campaign 또는 Canvas 메시지에서 셀렉션의 항목을 가져오는 Liquid를 삽입합니다. **개인화 추가**(**카탈로그 항목** > **셀렉션 사용**)를 사용하거나 태그를 수동으로 붙여넣을 수 있습니다:

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
Here are some upcoming events:

{{ items[0].event_name }} — ${{ items[0].ticket_price }}
{{ items[0].city }} · {{ items[0].venue }}

{{ items[1].event_name }} — ${{ items[1].ticket_price }}
{{ items[1].city }} · {{ items[1].venue }}
```
{% endraw %}

가변적인 수의 결과를 렌더링해야 하는 경우 하드코딩된 배열 인덱스를 루프로 대체하세요.

### 5단계: 빈 결과 처리 {#step-5-handle-empty-results}

셀렉션과 일치하는 카탈로그 항목이 없으면 `items` 배열이 비어 있고 태그 블록은 아무것도 렌더링하지 않습니다. 발송을 건너뛰거나 대체 문구를 표시하려면 태그를 조건문으로 감싸세요:

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
{% if items.size == 0 %}
{% abort_message('Catalog selection returned 0 items') %}
{% endif %}

Here are some upcoming events:
{{ items[0].event_name }}
```
{% endraw %}

자세한 내용은 [메시지 중단]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)을 참조하세요.

## 관련 문서 {#related-articles}

- [카탈로그 생성]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Campaign에서 카탈로그 사용]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Liquid `date` 필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#date-filter)
- [Liquid 사용 사례 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)