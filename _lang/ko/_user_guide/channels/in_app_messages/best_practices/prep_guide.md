---
nav_title: 준비 가이드
article_title: 인앱 메시지 준비 가이드
page_order: 0.5

page_type: reference
description: "이 문서에서는 인앱 메시지를 작성하기 전에 고려해야 할 질문과 모범 사례를 다루며, 타겟팅, 스케줄링, 콘텐츠, 성능, 전환 등을 포함합니다."
channel: in-app messages
toc_headers: h2
---

# 인앱 메시지 준비 가이드 {#in-app-message-prep-guide}

> 인앱 메시지를 작성하기 전에 다음 주제들을 고려하면 프로세스를 더 효율적으로 진행할 수 있습니다.

## 일반적인 고려 사항 {#general-considerations}

- Campaign을 구축하는 경우, 이 메시지의 배리언트를 몇 개나 표시하고 싶으신가요? 배리언트 테스트 아이디어에 대해서는 [다양한 채널을 위한 팁]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels)을 확인하세요.
- Canvas를 구축하는 경우, 이 메시지가 해당 단계에서 다른 메시징 채널과 함께 사용될 예정인가요?
- [메시지가 만료]({{site.baseurl}}/canvas_in-app_messages)되는 시점을 언제로 설정하시겠습니까?

## 타겟팅 고려 사항 {#targeting-considerations}

- 인앱 메시지는 앱을 정기적으로 방문하는 사용자에게 가장 적합합니다. 이 오디언스를 포함하고 있나요?
- 사용자가 어디에서 메시지를 볼 수 있도록 하고 싶으신가요? 웹 앱에서? 모바일 앱에서?
- 어떤 이벤트가 이 메시지를 트리거해야 하나요?
- 사용자 중에 이전 버전의 앱을 사용하는 사람이 있나요? 그렇다면 메시지의 일부 요소를 볼 수 없을 수 있습니다.
- 어떤 유형의 기기를 위해 이 메시지를 만들고 있나요? **미리보기** 상자 또는 **테스트** 탭을 사용하여 메시지를 미리 볼 수 있다는 점을 기억하세요. 자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)를 참조하세요.

## 스케줄, 지연 및 세션 시작 {#scheduling-delays-and-session-starts}

인앱 메시지 Campaign에 세션 시작 트리거와 함께 **스케줄 지연**이 설정된 경우, 세션을 시작한 후 인앱 메시지가 표시되기 전에 앱을 닫은 사용자는 지연이 만료된 후 다음 세션 시작 시 해당 메시지를 받을 수 있습니다.

인앱 메시지 Campaign은 트리거 후 최대 2시간까지 전달을 지연할 수 있습니다. 더 긴 대기가 필요한 경우, Canvas에서 인앱 메시지 단계 앞에 [지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) 단계를 추가하세요. 지연 설정에 대해서는 [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-2-select-delay-length)을 참조하세요.

이 타이밍은 특히 Campaign에서 **표시 전 Campaign 자격 재평가**가 선택되지 않은 경우 예상치 못한 표시 동작을 유발할 수 있습니다.

예를 들어, 사용자가 Campaign이 시작된 지 한 달 후에 8초 지연이 설정된 인앱 메시지를 받을 수 있습니다. 이는 사용자가 세션을 시작하고 즉시 세션을 종료한 뒤, 한 달 후에 다시 세션을 시작하고 8초 후에 인앱 메시지를 수신하는 경우에 발생할 수 있습니다. 앱을 닫지 않고 다른 화면으로 이동한 경우, 앱으로 돌아올 때 인앱 메시지가 표시됩니다.

## 콘텐츠 고려 사항 {#content-considerations}

- 이 메시지에 어떤 언어를 사용할 예정인가요?
- 제목과 본문 카피는 어떤가요? 눈길을 끌고 사용자와 관련이 있나요?
- 인앱 메시지는 정해진 시간 동안만 표시됩니다. 카피가 간결하고 기억에 남나요?
- 커스텀 카피를 추가하기 위해 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)를 사용할 예정인가요?
- 사용자가 메시지 텍스트(예: 할인 또는 바우처 코드)를 복사해야 하나요? iOS 및 Android에서 사용자는 텍스트나 텍스트 입력 필드를 길게 눌러 콘텐츠를 복사할 수 있습니다. 이미지에서는 길게 누르기가 작동하지 않으므로, 사용자가 복사해야 할 코드나 기타 카피가 포함된 이미지 대신 텍스트 또는 텍스트 입력 필드를 사용하세요.
- 전체 화면 인앱 메시지의 경우, 이미지 또는 기타 미디어가 [안전 영역]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone) 내에 있나요?
- 설문조사 인앱 메시지의 경우, 속성이나 제출을 기록하고 싶으신가요? 확인 페이지를 설정하셨나요?
- 커스텀 HTML 인앱 메시지의 경우, HTML에 특수 문자를 올바르게 표시하기 위한 UTF-8 인코딩이 포함되어 있나요? 자세한 내용은 [커스텀 HTML 인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding)를 참조하세요.
- 인앱 메시지에 비디오를 포함하는 경우: Braze는 기기에서의 로컬 재생을 위한 비디오 파일 크기에 기술적 제한을 적용하지 않지만, 사용자가 느린 연결, 비용이 많이 드는 데이터 요금제 또는 제한된 저장 공간을 가지고 있을 수 있다는 점을 유의하세요. 품질과 파일 크기의 균형을 맞추도록 비디오 파일을 최적화하세요.

## 인앱 메시지 성능 최적화 {#optimize-in-app-message-performance}

Braze는 세션 시작 시 사용자에게 적격한 인앱 메시지 트리거를 전달합니다. Liquid를 사용하는 메시지가 많으면 세션 시작이 지연되어 앱 성능에 영향을 줄 수 있습니다.

이 작업이 몇 초 이상 걸리면 Braze는 나머지 Liquid 렌더링을 지연시킬 수 있습니다. 이 경우 각 메시지는 트리거될 때 렌더링되고 온디맨드로 가져옵니다. 이 [템플릿 전달]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages) 방식은 응답 지연 시간 증가로 인한 앱 성능 저하로부터 사용자를 보호합니다.

메시지 전달 속도를 높이려면 다음 모범 사례를 활용하세요:

- Campaign의 트리거를 수행할 수 있는 사용자만 타겟팅하세요. 지나치게 넓은 타겟팅은 사용자가 활성화할 수 없는 인앱 메시지 트리거를 수신하게 만들 수 있습니다. 예를 들어, 특정 푸시 Campaign에 의해 트리거되는 인앱 메시지는 동일한 타겟 오디언스를 사용하도록 범위를 좁힐 수 있습니다. 이 방법은 다른 Campaign 유형, Canvases, 특정 사용자만 트리거할 수 있는 커스텀 이벤트 등에도 유사하게 적용할 수 있습니다.
- 시간에 민감한 Campaign에는 종료 날짜를 설정하세요. 더 이상 노출 횟수가 발생하지 않을 것으로 예상되면 Campaign을 중지하세요.
- 메시지나 콘텐츠 블록에 큰 정적 스타일시트, 스크립트 또는 base64 인코딩 미디어 자산을 직접 삽입하지 마세요. 대신 [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)를 사용하여 메시지 렌더링 시간을 줄이세요.
- 복잡한 분기 또는 반복 Liquid 로직을 줄이세요.
- 사용자가 메시지를 여러 번 수신해야 하는 경우에만 재적격성을 활성화하세요. 재적격성이 비활성화된 경우 Braze는 사용자가 메시지를 본 후 인앱 메시지 트리거 전달을 중지합니다. 자세한 내용은 [재적격성]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 참조하세요.
- 중요한 Campaign에 더 높은 우선순위를 부여하세요. Braze는 우선순위가 높은 적격 메시지를 먼저 렌더링하므로, 사용자가 여러 Campaign에 해당하는 경우 템플릿 전달이 발생할 가능성이 줄어듭니다. 자세한 내용은 [우선순위 선택]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority)을 참조하세요.

### 정적 코드와 자산 분리 {#separate-static-code-and-assets}

개인화된 값과 조건부 규칙은 메시지에 유지하세요. 재사용 가능한 CSS, JavaScript, 미디어 자산은 [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)에 호스팅한 후 링크하세요.

모든 스크립트와 스타일에 대해 이 작업을 수행할 필요는 없습니다. 이 방법은 주로 공유 브랜드 스타일이나 인터랙티브 위젯 같은 복잡한 스크립트 등 대용량 자산의 비대화를 줄이는 데 유용합니다.

미디어 라이브러리의 스타일시트와 스크립트는 Liquid를 평가하지 않으므로 사용자의 기기에서 캐시할 수 있습니다. 다음 예시는 동적 값을 인라인으로 유지하고 재사용 가능한 코드를 정적 파일에서 로드합니다:

{% raw %}

```liquid
<head>
  <style>
    /* Select a hero image URL based on the user's subscription tier. */
    {% capture hero_image_url %}
      {% if custom_attribute.${subscription_tier} == 'premium' %}
        https://braze-images.com/path/to/premium/hero.jpg
      {% else %}
        https://braze-images.com/path/to/standard/hero.jpg
      {% endif %}
    {% endcapture %}
    /* Assigning to a CSS variable so it can be used inside our stylesheet. */
    :root {
      --hero-image: url("{{ hero_image_url | url_escape }}");
    }
  </style>
  <script>
    // Assigning to the global window object so the value can be referenced in our script.
    window.brandConfig = {
      subscriptionTier: "{{custom_attribute.${subscription_tier} | json_escape }}"
    };
  </script>
  <!-- Linking to a stylesheet from the Braze media library. -->
  <link rel="stylesheet" href="https://braze-images.com/path/to/media/library/asset.css">
  <!-- Linking to a script from the Braze media library. -->
  <script src="https://braze-images.com/path/to/other/media/library/asset.js" defer></script>
</head>

<body>
  <div class="hero"></div>
  <div class="user-styles" data-subscription-tier="{{custom_attribute.${subscription_tier} | escape}}">
    ...
  </div>
</body>
```

{% endraw %}

미디어 라이브러리 스타일시트에서 CSS 변수를 참조하고 다른 재사용 가능한 스타일을 정의할 수 있습니다:

```css
.hero {
  background-image: var(--hero-image);
}

.user-styles {
  /* styles for all users */
}

.user-styles[data-subscription-tier="premium"] {
  /* premium subscription tier user styles, color scheme, etc */
}

.user-styles[data-subscription-tier="standard"] {
  /* standard subscription tier user styles, color scheme, etc */
}
```

미디어 라이브러리 스크립트에서 인라인 JavaScript 변수를 사용하여 재사용 가능한 동작을 추가할 수 있습니다:

```javascript
const config = window.brandConfig || {};

if (config.subscriptionTier === "standard") {
  // add some sort of logic to show a "subscribe to premium" button
} else if (config.subscriptionTier === "premium") {
  // thank the user for being a premium user
}
```

## 전환 고려 사항 {#conversion-considerations}

- 이 메시지의 목표는 무엇인가요? 메시지에서 이를 어떻게 표현할 수 있나요?
- 버튼이 사용자에게 적합한 옵션을 제공하고 있나요? [주요 행동 유도 문안]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)은 무엇인가요?
- 다른 인앱 콘텐츠로 [딥링킹]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)하고 있나요? 이 인앱 메시지를 사용하여 [권한 또는 푸시 사전 요청]({{site.baseurl}}/user_guide/channels/push/best_practices)을 보내고 수락하고 있나요?
- 메시지 종료 옵션이 있나요? 없다면 이 스니펫을 복사하여 붙여넣기하면 빠르게 버튼을 만들 수 있습니다:
  ```html
  <a href="appboy://close">X</a>
  ```

## 드래그 앤 드롭 편집기 고려 사항 {#drag-and-drop-editor-considerations}

### 기기별 딥링크 추가 {#adding-deep-links-for-different-devices}

드래그 앤 드롭 편집기에서는 기기별로 서로 다른 딥링크를 추가하는 기능을 지원하지 않습니다(기존 편집기와 다름).

### 배경 이미지 불투명도 조정 {#adjusting-background-image-opacity}

불투명도 설정에서는 배경 이미지를 완전히 투명하게 만들 수 없습니다(기존 IAM 편집기와 다름). 불투명도 설정을 사용하여 메시지 배경 색상을 완전히 투명하게 만들 수 있습니다.

### 최대 너비 설정 {#setting-the-maximum-width}

드래그 앤 드롭 편집기의 최대 너비는 325px로 제한되어 있으며, 이는 주로 대시보드 미리보기에 맞추기 위한 것입니다. 메시지는 더 작은 화면의 기기에서도 올바르게 표시될 수 있습니다.

### 플랫폼별 서로 다른 배경 선택 {#selecting-different-backgrounds-for-different-platforms}

동일한 메시지에 대해 서로 다른 플랫폼(예: 웹과 모바일)에서 두 가지 다른 배경을 표시하는 것은 불가능합니다.

### 메시지 스타일 적용 {#applying-message-styles}

배경 이미지는 전체 메시지에 적용되며 페이지별로 커스터마이즈할 수 없습니다. 메시지 스타일은 개별 페이지가 아닌 전체 메시지에 적용됩니다.

### 스페이서 블록 높이 측정 {#measuring-spacer-blocks-height}

스페이서 블록의 측정 단위는 픽셀(px)이며 변경할 수 없습니다.

### 지원되는 형식 {#supported-formats}

현재 드래그 앤 드롭 편집기에서는 Modal 및 전체 화면 인앱 메시지만 지원됩니다.

### 크기 및 종횡비 조정 {#adjusting-to-size-and-aspect-ratio}

배경 이미지는 인앱 메시지를 늘리게 되는데, 이는 Modal이 배경 이미지의 크기와 종횡비에 맞게 조정되기 때문입니다. 필요에 따라 비율을 조정할 수 있습니다.

### 배경 이미지 및 클릭 시 동작 {#background-images-and-on-click-behavior}

이러한 설정은 페이지 간에 유지됩니다. 각 페이지에 서로 다른 전체 이미지가 있는 멀티 페이지 인앱 메시지의 경우, 사용자가 다음 페이지로 이동할 수 있도록 버튼을 추가하세요.