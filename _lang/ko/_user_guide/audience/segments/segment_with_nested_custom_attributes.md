---
nav_title: "사용 사례: 중첩 고객 속성"
article_title: "사용 사례: 중첩 고객 속성으로 Segment 만들기"
page_order: 10
page_type: tutorial
tool: Segments
description: "중첩 고객 속성을 사용하여 Segments를 구축합니다: 중첩 고객 속성 필터, 경로 및 비교 연산자, 시간 필터, 다중 기준 세분화, 스키마 생성, 중첩 오브젝트 탐색기를 다룹니다."
---

# 사용 사례: 중첩 고객 속성으로 Segment 만들기 {#use-case-segment-with-nested-custom-attributes}

> 이 사용 사례에서는 Braze에서 중첩 고객 속성을 사용하여 사용자를 세분화하는 방법을 보여주며, 자체 데이터에 맞게 조정할 수 있는 샘플 JSON 및 대시보드 워크플로를 포함합니다.

음악 스트리밍 앱의 마케팅 팀에 소속되어 있고, 잔액과 유형이 포함된 계정 오브젝트와 같은 사용자의 중첩 고객 속성을 기반으로 메시지를 보내고 싶다고 가정해 보겠습니다. 이 사용 사례에서는 팀이 Segments에서 중첩 고객 속성을 사용할 수 있는 다양한 방법을 보여주며, 다음 내용을 배울 수 있습니다:

- 중첩 고객 속성 Segment 필터를 구성하고, 경로를 검증하며, 각 등록정보의 데이터 유형에 맞는 비교 연산자를 선택하는 방법.
- 중첩 날짜 값에 **Day of Year** 연산자와 **Time** 연산자를 언제 사용해야 하는지, 그리고 **다중 기준 세분화**가 배열 내 하나 이상의 오브젝트가 나열된 모든 기준을 충족할 때 사용자를 매칭하는 방식.
- 오브젝트 또는 오브젝트 배열의 스키마를 생성하고, 대시보드에서 탐색한 후, 경로를 직접 입력하는 대신 경로 선택기를 사용하여 Segment(예: 잔액이 100 미만인 사용자)를 완성하는 방법.

## 중첩 고객 속성으로 필터링하기 {#filter-by-nested-custom-attributes}

가장 많이 재생한 곡을 300회 이상 재생한 사용자를 타겟팅하기 위해 중첩 고객 속성을 기반으로 Segment를 만들어 보겠습니다.

### 1단계: 필터 추가 {#step-1-add-the-filter}

**Nested Custom Attributes** 필터를 선택하면 특정 중첩 고객 속성을 선택할 수 있는 드롭다운이 표시됩니다. 사용자의 가장 많이 재생한 곡에 대한 데이터를 포함하는 `most_played_song`을 선택하겠습니다.

### 2단계: 등록정보 선택 {#step-2-select-the-property}

필터링할 중첩 고객 속성 내의 **등록정보**를 선택합니다. 사용자가 가장 많이 재생한 곡을 몇 번 재생했는지 추적하는 `play_analytics.count`를 선택하겠습니다.

### 3단계: 비교 연산자 및 중첩 고객 속성 값 선택 {#step-3-select-a-comparison-and-nested-custom-attribute-value}

중첩 고객 속성으로 필터링할 때, 등록정보의 데이터 유형에 따라 사용할 수 있는 비교 연산자가 결정됩니다. 예를 들어, `play_analytics.count`는 숫자이므로 **숫자** 카테고리에서 비교 연산자를 선택할 수 있습니다.

가장 많이 재생한 곡을 최소 300회 이상 재생한 사용자를 필터링하려면 **More than** 비교 연산자를 선택한 다음 값으로 "300"을 입력합니다.

![중첩 고객 속성의 데이터 유형에 따라 연산자를 선택하는 사용자]({% image_buster /assets/img_archive/nca_comparator.png %})

## 시간 데이터 유형으로 필터링하기 {#filter-for-time-data-types}

중첩 시간 커스텀 속성으로 필터링할 때, 날짜 값을 비교할 때 **Day of Year** 또는 **Time** 카테고리의 연산자를 선택하여 필터링할 수 있습니다.

**Day of Year** 카테고리의 연산자를 선택하면, 중첩 고객 속성 값의 전체 타임스탬프 대신 월과 일만 비교에 사용됩니다. **Time** 카테고리의 연산자를 선택하면 연도를 포함한 전체 타임스탬프를 비교합니다.

## 다중 기준 세분화 사용하기 {#use-multi-criteria-segmentation}

**다중 기준 세분화**를 사용하여 단일 오브젝트 내에서 여러 기준에 일치하는 Segment를 만들 수 있습니다. 배열 내 하나 이상의 오브젝트가 지정된 모든 기준에 일치하면 해당 사용자가 Segment에 포함됩니다. 예를 들어, 키가 비어 있지 않고 숫자가 0보다 큰 경우에만 사용자가 이 Segment에 매칭됩니다.

### Segment용 Liquid 복사 {#copy-liquid-for-segment}

**Segment용 Liquid 복사** 기능을 사용하여 이 Segment에 대한 Liquid 코드를 생성하고 메시지에서 활용할 수도 있습니다. 예를 들어, 계정 오브젝트 배열이 있고 활성 과세 계정을 가진 고객을 타겟팅하는 Segment가 있다고 가정해 보겠습니다. 고객이 활성 과세 계정 중 하나와 연결된 계정 목표에 기여하도록 유도하려면, 이를 독려하는 메시지를 만들어야 합니다.

![다중 기준 세분화 체크박스가 선택된 예시 Segment.]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

**Segment용 Liquid 복사**를 선택하면, Braze가 활성이면서 과세 대상인 계정만 포함하는 오브젝트 배열을 반환하는 Liquid 코드를 자동으로 생성합니다.

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

여기서 `segmented_nested_objects`를 사용하여 메시지를 개인화할 수 있습니다. 이 예시에서는 첫 번째 활성 과세 계정의 목표를 가져와 개인화합니다:

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

이렇게 하면 고객에게 다음과 같은 메시지가 전달됩니다: "Get to your retirement goal faster, make a deposit using our new fast deposit feature!"

## 중첩 오브젝트 탐색기를 사용하여 스키마 생성하기 {#generate-schema}

중첩 오브젝트 경로를 외울 필요 없이 Segment 필터를 구축하기 위해 오브젝트의 스키마를 생성할 수 있습니다.

### 1단계: 스키마 생성 {#step-1-generate-a-schema}

예를 들어, Braze에 방금 전송한 `accounts` 오브젝트 배열이 있다고 가정해 보겠습니다:

```json
{"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true}
]}
```

Braze 대시보드에서 **데이터 설정** > **커스텀 속성**으로 이동합니다.

오브젝트 또는 오브젝트 배열을 검색합니다. **Attribute Name** 열에서 **Generate Schema**를 선택합니다.

![커스텀 속성 목록에서 accounts 속성의 스키마를 생성하는 옵션.]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
전송한 데이터 양에 따라 스키마 생성에 몇 분이 걸릴 수 있습니다.
{% endalert %}

스키마가 생성되면 **Generate Schema** 버튼 자리에 새로운 <i class="fas fa-plus"></i> 플러스 버튼이 나타납니다. 이를 클릭하면 Braze가 이 중첩 고객 속성에 대해 파악한 내용을 확인할 수 있습니다.

스키마 생성 중에 Braze는 이전에 전송된 데이터를 분석하여 해당 속성에 대한 데이터의 이상적인 표현을 구축합니다. 또한 Braze는 중첩 값의 데이터 유형을 분석하고 추가합니다. 이는 해당 중첩 속성에 대해 Braze에 이전에 전송된 데이터를 샘플링하여 수행됩니다.

`accounts` 오브젝트 배열의 경우, 오브젝트 배열 내에 다음을 포함하는 오브젝트가 있음을 확인할 수 있습니다:

- `active` 키를 가진 부울 유형 (계정이 활성인지 여부와 관계없이)
- `balance` 키를 가진 숫자 유형 (계정의 잔액)
- `type` 키를 가진 문자열 유형 (비과세 또는 과세 계정)

![active, balance, type 세 가지 중첩 값이 있는 accounts 오브젝트 배열의 스키마.]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:70%" }

이제 데이터를 분석하고 표현을 구축했으니, Segment를 만들어 보겠습니다.

### 2단계: Segment 만들기 {#step-2-build-a-segment}

잔액이 100 미만인 고객을 타겟팅하여 입금을 유도하는 메시지를 보내겠습니다.

Segment를 생성하고 `Nested Custom Attribute` 필터를 추가한 다음, 오브젝트 또는 오브젝트 배열을 검색하여 선택합니다. 여기서는 `accounts` 오브젝트 배열을 추가했습니다.

![accounts 오브젝트 배열에 대한 중첩 고객 속성 필터링.]({% image_buster /assets/img_archive/nca_segment_schema.png %})

경로 필드에서 <i class="fas fa-plus"></i> 플러스 버튼을 선택합니다. 그러면 오브젝트 또는 오브젝트 배열의 표현이 열립니다. 나열된 항목 중 하나를 선택하면 Braze가 경로 필드에 자동으로 삽입합니다. 이 예시에서는 잔액을 가져와야 합니다. 잔액을 경로로 선택하면 (이 경우 `[].balance`) 경로 필드에 자동으로 채워집니다.

![검색 가능한 경로 목록이 있는 accounts 스키마.]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

비교 연산자로 **less than**을 선택한 다음 잔액 값으로 "100"을 입력합니다.

![계정 잔액이 100 미만인 사용자를 위한 필터.]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

완료되었습니다! 데이터가 어떻게 구조화되어 있는지 알 필요 없이 중첩 고객 속성을 사용하여 Segment를 만들었습니다. Braze의 중첩 오브젝트 탐색기가 데이터의 시각적 표현을 생성하여 Segment를 만드는 데 필요한 항목을 탐색하고 정확히 선택할 수 있게 해주었습니다.