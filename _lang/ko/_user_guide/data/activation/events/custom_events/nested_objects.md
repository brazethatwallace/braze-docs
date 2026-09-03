---
nav_title: 중첩된 오브젝트
article_title: 커스텀 이벤트의 중첩된 오브젝트
page_order: 1
page_type: reference
description: "이 문서에서는 중첩된 JSON 데이터를 커스텀 이벤트 및 구매의 등록정보로 전송하는 방법과 메시징에서 이러한 중첩된 오브젝트를 사용하는 방법에 대해 설명합니다."
---

# 커스텀 이벤트의 중첩된 오브젝트 {#nested-objects-in-custom-events}

> 이 페이지에서는 중첩된 JSON 데이터를 커스텀 이벤트 및 구매의 등록정보로 전송하는 방법과 메시징에서 이러한 중첩된 오브젝트를 사용하는 방법에 대해 설명합니다.

중첩 오브젝트(다른 오브젝트 안에 있는 오브젝트)를 사용하여 중첩된 JSON 데이터를 커스텀 이벤트 및 구매의 등록정보로 전송할 수 있습니다. 이 중첩된 데이터는 메시지에서 개인화된 정보를 템플릿화하고, 메시지 전송을 트리거하고, 사용자를 세분화하는 데 사용할 수 있습니다.

## 고려 사항 {#considerations}

- 중첩된 데이터는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events) 및 [구매 이벤트]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) 모두에 지원되지만 다른 이벤트 유형은 지원되지 않습니다.
- 배열 또는 오브젝트 값을 포함하는 이벤트 등록정보 오브젝트는 최대 100KB의 이벤트 등록정보 페이로드를 가질 수 있습니다.
- 구매 이벤트에 대해서는 이벤트 등록정보 스키마를 생성할 수 없습니다.
- 이벤트 등록정보 스키마는 지난 24시간 동안의 커스텀 이벤트를 샘플링하여 생성됩니다.

### 최소 SDK 버전 {#minimum-sdk-versions}

다음 SDK 버전은 중첩된 오브젝트를 지원합니다:

{% sdk_min_versions swift:5.0.0 android:20.0.0 web:3.3.0 %}

## 1단계: 스키마 생성 {#step-1-generate-a-schema}

중첩된 이벤트 등록정보가 있는 각 이벤트에 대한 스키마를 생성하여 커스텀 이벤트의 중첩된 데이터에 액세스할 수 있습니다. 스키마를 생성하려면:

1. **데이터 설정** > **커스텀 이벤트**로 이동합니다.
2. 중첩된 등록정보가 있는 이벤트의 **등록정보 관리**를 선택합니다.
3. <i class="fas fa-arrows-rotate"></i> 버튼을 선택하여 스키마를 생성합니다. 스키마를 보려면 <i class="fas fa-plus"></i> 더하기 버튼을 선택합니다.

![버튼을 선택하여 스키마를 생성합니다. 스키마를 보려면 더하기 버튼을 선택합니다.]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

향후 새로운 등록정보가 전송되면 스키마가 재생성될 때까지 스키마에 포함되지 않습니다. 스키마는 24시간마다 재생성할 수 있습니다.

## 2단계: 중첩된 오브젝트 사용 {#step-2-use-the-nested-object}

세분화 및 개인화 중에 중첩된 데이터를 참조할 수 있습니다. 스키마는 필요하지 않습니다. 사용 예는 다음 섹션을 참조하세요:

- [API 요청 본문](#api-request-body)
- [Liquid 템플릿](#liquid-templating)
- [메시지 트리거](#message-triggering)
- [세분화](#segmentation)
- [개인화](#personalization)

### API 요청 본문 {#api-request-body}

{% tabs %}
{% tab Music Example %}

다음은 "Created Playlist" 커스텀 이벤트가 포함된 `/users/track` 예시입니다. 재생 목록이 생성된 후 다음을 전송하여 재생 목록의 등록정보를 캡처합니다:
- "songs"를 등록정보로 나열하는 API 요청
- 노래의 중첩 등록정보 배열

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

다음은 "Ordered" 커스텀 이벤트가 포함된 `/users/track` 예시입니다. 주문이 완료된 후 다음을 전송하여 해당 주문의 등록정보를 캡처합니다:
- `r_details`를 등록정보로 나열하는 API 요청
- 해당 주문의 중첩 등록정보

```
...
"properties": {
  "r_details": {
    "name": "SandwichEmperor",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
중첩 커스텀 이벤트 등록정보의 경우, 연도가 0 미만이거나 3000을 초과하면 Braze는 해당 값을 사용자에게 저장하지 않습니다.
{% endalert %}

### Liquid 템플릿 {#liquid-templating}

다음은 [이전 API 요청](#api-request-body)에서 요청한 중첩 등록정보를 참조하는 Liquid 템플릿을 만드는 방법을 보여줍니다.

{% tabs %}
{% tab Music Example %}
"Created Playlist" 이벤트에 의해 트리거된 메시지에서 Liquid 템플릿 사용:

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind"<br>
`{{event_properties.${songs}[1].title}}`: "While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
"Ordered" 이벤트에 의해 트리거된 메시지에서 Liquid 템플릿 사용:

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### 메시지 트리거 {#message-triggering}

이러한 등록정보를 사용하여 Campaign을 트리거하려면 커스텀 이벤트 또는 구매를 선택한 다음 **중첩 등록정보** 필터를 추가합니다. 인앱 메시지에서는 메시지 트리거가 아직 지원되지 않지만, 메시지 내 Liquid 개인화의 중첩 등록정보는 여전히 표시됩니다.

{% tabs %}
{% tab Music Example %}

"Created Playlist" 이벤트의 중첩 등록정보로 Campaign 트리거:

![커스텀 이벤트의 등록정보 필터에 대해 중첩 등록정보를 선택하는 사용자.]({% image_buster /assets/img/nested_object2.png %})

트리거 조건 `songs[].album.yearReleased` "is" "1968"은 노래 중 하나라도 1968년에 발매된 앨범이 있는 이벤트와 일치합니다. 배열을 순회하기 위해 대괄호 표기법 `[]`을 사용하며, 순회된 배열의 **어떤** 항목이든 이벤트 등록정보와 일치하면 매칭됩니다.

{% alert important %}
**같지 않음** 필터는 배열의 등록정보 중 어느 것도 제공된 값과 같지 않을 때만 일치합니다. <br><br>예를 들어, Canvas A에 동작 기반 커스텀 이벤트 중첩 등록정보 필터 **같음** "smartwatch"가 있고, Canvas B에 동작 기반 커스텀 이벤트 중첩 등록정보 필터 **같지 않음** "simphone"이 있다고 가정합니다. 등록정보에 "smartwatch"와 "simphone"이 모두 있으면 두 Canvases 모두 트리거됩니다. 하지만 어떤 등록정보에든 "simphone" 또는 "sim only"가 있으면 어느 Canvas도 트리거되지 않습니다.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

"Ordered" 이벤트의 중첩 등록정보로 Campaign 트리거:

![커스텀 이벤트에 대해 등록정보 필터 r_details.name is SandwichEmperor를 추가하는 사용자.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "SandwichEmperor"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
이벤트 등록정보에 `[]` 또는 `.` 문자가 포함된 경우, 해당 부분을 큰따옴표로 감싸서 이스케이프합니다. 예를 들어, `"songs[].album".yearReleased`는 리터럴 등록정보 `"songs[].album"`이 있는 이벤트와 일치합니다.
{% endalert %}

### 세분화 {#segmentation}

중첩 이벤트 등록정보를 기반으로 사용자를 세분화하려면 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension)을 사용해야 합니다. 스키마를 생성한 후 세분화 섹션에 중첩된 오브젝트 탐색기가 표시됩니다.

![세분화와 관련된 스크린샷.]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

세분화는 트리거와 동일한 표기법을 사용합니다([메시지 트리거](#message-triggering) 참조).

세그먼트 확장을 편집하거나 생성하려면 "세그먼트 편집" 권한이 필요합니다.

### 개인화 {#personalization}

**개인화 추가** 모달을 사용하여 개인화 유형으로 **고급 이벤트 등록정보**를 선택합니다. 이렇게 하면 스키마가 생성된 후 중첩 이벤트 등록정보를 추가할 수 있는 옵션이 제공됩니다.

![개인화 추가 모달을 사용하여 개인화 유형으로 고급 이벤트 등록정보를 선택합니다. 이렇게 하면 스키마가 생성된 후 중첩 이벤트 등록정보를 추가할 수 있는 옵션이 제공됩니다.]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## 메시지에서 중첩된 오브젝트 테스트 {#testing-nested-objects-in-messages}

대시보드의 **미리보기 및 테스트** 도구는 중첩된 오브젝트 또는 중첩 커스텀 속성에 대한 모의 데이터 추가를 지원하지 않습니다. Liquid를 통해 중첩 데이터를 참조하는 메시지를 테스트하려면, 해당 중첩 속성이 있는 기존 사용자로 메시지를 미리 보거나, 테스트 사용자에게 라이브 Campaign을 실행하여 커스텀 이벤트 등록정보가 포함된 메시지를 미리 볼 수 있습니다.

### 중첩 커스텀 속성 {#nested-custom-attributes}

1. API를 통해 테스트 사용자 프로필에 중첩 속성을 가져옵니다.
2. Campaign 또는 Canvas에서 **미리보기 및 테스트**로 이동합니다.
3. **사용자로 미리보기**를 선택하고 테스트 사용자를 검색합니다. Liquid는 해당 사용자 프로필의 실제 중첩 속성을 사용하여 렌더링됩니다.

### 중첩 이벤트 등록정보 {#nested-event-properties}

중첩 이벤트 등록정보는 라이브 이벤트 트리거가 필요하므로 대시보드에서 미리 볼 수 없습니다. 테스트하려면:

1. 테스트 사용자만을 타겟으로 하고 중첩 등록정보가 있는 커스텀 이벤트에 의해 트리거되는(또는 참조하는) Campaign 또는 캔버스 단계를 생성합니다.
2. 테스트 오디언스에게 Campaign을 시작합니다.
3. 테스트 사용자의 프로필에 중첩된 오브젝트 페이로드가 포함된 커스텀 이벤트를 기록합니다(API 또는 SDK 사용).
4. 메시지가 중첩 등록정보 값으로 올바르게 렌더링되는지 확인합니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 중첩된 오브젝트를 사용하면 추가 데이터 포인트가 기록되나요? {#does-using-nested-objects-log-additional-data-points}

이 기능을 추가함으로써 데이터 포인트를 기록하는 방식에는 변경이 없습니다. 중첩된 오브젝트를 기반으로 한 세분화는 세그먼트 확장을 사용하며, 추가 데이터 포인트를 사용하지 않습니다.

### 얼마나 많은 중첩 데이터를 전송할 수 있나요? {#how-much-nested-data-can-be-sent}

이벤트의 등록정보 중 하나 이상이 중첩 데이터를 포함하는 경우, 이벤트의 모든 결합된 등록정보에 대한 최대 페이로드는 100KB입니다. 해당 크기 제한을 초과하는 요청은 거부됩니다.