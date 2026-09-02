---
nav_title: 커스텀 폼 블록 만들기
article_title: 랜딩 페이지에서 커스텀 폼 블록 만들기
page_order: 6
page_type: reference
description: "Braze 랜딩 페이지에서 커스텀 인터랙티브 폼 입력을 구축하여 표준 폼 블록과 함께 값을 검증하고 제출하는 방법을 알아봅니다."
---

# 랜딩 페이지에서 커스텀 폼 블록 만들기 {#create-custom-form-blocks-on-landing-pages}

> Braze 랜딩 페이지 [폼 블록]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)은 텍스트 필드, 체크박스, 드롭다운과 같은 표준 입력을 캡처합니다. 커스텀 폼 블록은 별점 평가, 이모지 감정 선택기, 스크래치 카드 등 자체 인터랙티브 요소를 구축할 수 있도록 하여 가능성을 확장합니다.

방문자가 커스텀 폼을 제출하면 선택한 값이 검증되어 표준 필드와 함께 저장된 후 커스텀 사용자 속성으로 Braze에 전송됩니다. 이를 통해 랜딩 페이지 에디터를 벗어나지 않고도 더 풍부하고 매력적인 입력을 수집할 수 있습니다.

커스텀 폼 블록은 단일 JavaScript 헬퍼인 `window.brazeHelpers.forms.registerFormInput`을 사용하여 구축하며, 랜딩 페이지의 **커스텀 코드** 블록에서 호출합니다.

{% alert note %}
설문조사와 인앱 메시지에는 자체 폼 블록이 있지만, `registerFormInput`(커스텀 코딩된 UI를 폼 블록에 연결하는 JavaScript API)은 랜딩 페이지에서만 사용할 수 있습니다.
{% endalert %}

## 작동 방식 {#how-it-works}

커스텀 폼 입력은 랜딩 페이지에서 값을 캡처하고 폼과 함께 제출하려는 모든 요소입니다. 해당 요소를 등록하여 Braze 폼 시스템에 연결합니다. 등록은 Braze에 어떤 요소를 감시할지, 현재 값을 어떻게 읽을지, 폼이 제출될 때 해당 값으로 무엇을 할지 알려줍니다.

1. 랜딩 페이지의 **커스텀 코드** 블록 내에 커스텀 UI를 구축하고 `id`와 같은 안정적인 CSS 선택자를 지정합니다.
2. 구성 객체와 함께 `window.brazeHelpers.forms.registerFormInput`을 호출하여 요소를 등록합니다.
3. Braze는 필요할 때 `getValue` 함수를 호출하여 현재 값을 읽습니다.
4. 필드가 필수이거나 `onValidate` 함수를 제공한 경우, Braze는 값이 통과할 때까지 제출을 차단하고 스타일을 지정할 수 있는 CSS 클래스로 유효하지 않은 요소를 표시합니다. [검증 및 필수 필드](#validation-and-required-fields)를 참조하세요.
5. 폼이 제출되고 검증이 통과하면, Braze는 `onSubmit` 함수를 호출하며, 여기서 Braze SDK를 호출하여 커스텀 사용자 속성과 같은 정보를 기록할 수 있습니다.

값을 읽고, 검증하고, 제출하는 함수를 직접 제공하므로, 이 접근 방식은 거의 모든 커스텀 폼 요소에서 작동하며 에디터의 표준 필드 유형에 제한되지 않습니다.

## 기본 프레임워크 {#basic-framework}

가장 간단한 등록은 하나의 요소를 대상으로 하고, 필수로 처리하며, 데이터 속성에서 값을 읽고, 폼이 제출될 때 해당 값을 커스텀 사용자 속성에 기록합니다. 이 페이지의 예제처럼 `DOMContentLoaded` 리스너로 호출을 감싸서 `registerFormInput`이 실행되기 전에 요소가 존재하도록 합니다:

```js
document.addEventListener("DOMContentLoaded", () => {
  window.brazeHelpers.forms.registerFormInput({
    selector: "#my-custom-input",
    isRequired: true,
    getValue: (element) => element.dataset.value ?? null,
    onSubmit: (value) => {
      window.brazeBridge.getUser().setCustomUserAttribute("my_attribute", value);
    },
  });
});
```

페이지의 각 커스텀 입력에 대해 `registerFormInput`을 한 번씩 호출합니다. 랜딩 페이지 에디터를 통해 배치된 표준 폼 필드는 등록할 필요가 없습니다. 등록은 **커스텀 코드** 블록에서 구축한 커스텀 입력에만 필요합니다.

## 구성 참조 {#configuration-reference}

`registerFormInput`은 단일 구성 객체를 받습니다. 함수 시그니처로 표현하면 전체 형태는 다음과 같습니다:

```js
window.brazeHelpers.forms.registerFormInput({
  // Provide exactly one of `selector` or `element` to identify the input.
  selector?: string,
  element?: HTMLElement,
  isRequired?: boolean | Promise<boolean>,
  getValue: (element: HTMLElement) => value,
  onValidate?: (value, element: HTMLElement) => boolean | Promise<boolean>,
  onSubmit?: (value, element: HTMLElement) => void | Promise<void>,
});
```

최소한 요소를 찾는 방법(`selector` 또는 `element`)과 `getValue` 함수를 제공해야 합니다. 나머지는 모두 선택 사항입니다.

| 속성 | 유형 | 필수 | 설명 |
| --- | --- | --- | --- |
| `selector` | `string` | 예 (또는 `element`) | 커스텀 요소와 일치하는 CSS 선택자입니다(예: `"#scratch-card"`). Braze는 검증 및 제출 시점에 `querySelector`로 지연 해석하므로, `registerFormInput` 실행 후 DOM에 추가된 요소와도 일치할 수 있습니다. |
| `element` | `HTMLElement` | 예 (또는 `selector`) | `selector` 대신 사용되는 요소에 대한 직접 참조입니다. 요소가 페이지에 연결되어 있는 동안에만 사용되며, 둘 다 제공된 경우 `selector`보다 우선합니다. |
| `isRequired` | `boolean \| Promise<boolean>` | 아니요 | `true`인 경우, 입력에 비어 있지 않은 값이 있을 때까지 폼을 제출할 수 없습니다. `null`, `undefined`, 빈 문자열(공백만 있는 문자열 포함), 빈 배열은 모두 비어 있는 것으로 간주됩니다. 불리언으로 해석되는 프로미스일 수도 있으며, Braze는 입력이 검증될 때마다 재평가하므로 런타임에 필수 상태를 결정할 수 있습니다. 기본값은 `false`입니다. 전체 검증 순서는 [검증 및 필수 필드](#validation-and-required-fields)를 참조하세요. |
| `getValue` | `function` | 예 | 입력의 현재 값을 반환합니다. Braze는 일치하는 요소를 인수로 전달하므로 DOM에서 값을 읽을 수 있습니다(예: `element.dataset.sentiment`). 또는 자체 코드의 변수에서 읽을 수도 있습니다. 아직 값이 없을 때는 `null`을 반환합니다. |
| `onValidate` | `function` | 아니요 | 현재 값과 일치하는 요소를 받으며, `boolean \| Promise<boolean>`(`isRequired`와 동일한 반환 유형)을 반환해야 합니다. `true`는 값이 유효함을, `false`는 유효하지 않음을 의미합니다. 값이 허용된 집합에 포함되는지 등 값의 존재 여부를 넘어서는 규칙을 적용하는 데 사용합니다. 생략하면 `isRequired`와 네이티브 제약 조건 검증만 적용됩니다. |
| `onSubmit` | `function` | 아니요 | 폼이 제출되고 검증이 통과할 때 실행됩니다. 현재 값과 일치하는 요소를 받습니다. 여기서 일반적으로 `setCustomUserAttribute`를 사용하여 Braze에 값을 기록합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="구성 참조" }

### onSubmit에서 값 처리 {#act-on-the-value-in-onsubmit}

`onSubmit`은 일반 JavaScript 콜백이므로 통합에 필요한 방식으로 캡처된 값을 처리할 수 있습니다. `onSubmit`은 폼 제출의 일부로 실행되므로, 그 안에서 수행하는 `brazeBridge` 호출은 랜딩 페이지를 익명으로 연 방문자에게도 예상대로 작동합니다. 브릿지 호출이 작동하는 다른 상황은 [브릿지 가용성]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#bridge-availability)을 참조하세요.

가장 일반적인 패턴은 랜딩 페이지에서 사용할 수 있는 [Braze JavaScript 브릿지]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge)를 사용하여 캡처된 값을 고객 프로필에 기록하는 것입니다:

```js
window.brazeBridge.getUser().setCustomUserAttribute("attribute_name", value);
```

워크스페이스에 이미 존재하거나 생성하려는 커스텀 속성 이름을 사용합니다. 전달하는 값은 사용자 프로필에 저장되며, 이후 세분화, 개인화, 후속 메시지 트리거에 사용할 수 있습니다.

커스텀 속성에만 제한되지 않습니다. 동일한 콜백에서 모든 [`brazeBridge.getUser()` 메서드]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge#supported-methods)를 호출할 수 있습니다. 예를 들어, 사용자를 구독 그룹에 추가하거나, 표준 속성을 설정하거나, 커스텀 이벤트를 기록하거나, 자체 API 엔드포인트로 값을 전송할 수 있습니다.

{% alert note %}
`onSubmit` 내에서 `requestImmediateDataFlush`를 호출할 필요가 없습니다. 폼 제출 프로세스는 `onSubmit` 콜백이 완료된 후 자동으로 모든 데이터를 Braze로 플러시합니다.
{% endalert %}

## 예제 {#examples}

다음 예제는 완전하고 독립적입니다. 각 예제는 마크업, `<script>` 태그, `<style>` 태그를 포함하는 단일 블록으로, 랜딩 페이지의 하나의 **커스텀 코드**(HTML) 블록에 붙여넣습니다. 각 스크립트 끝부분의 `registerFormInput` 호출이 커스텀 입력을 Braze 폼에 연결합니다. 코드 샘플 위에 마우스를 올리고 복사 아이콘을 선택하여 복사할 수 있습니다.

{% alert important %}
이 예제는 전적으로 방문자의 브라우저에서 실행됩니다. 스크래치 카드 예제의 경우, "상품"은 방문자의 브라우저에서 JavaScript로 선택되므로 기술적으로 능숙한 방문자가 코드를 수정하여 원하는 결과를 얻을 수 있습니다. 리워드, 할인 또는 방문자별 엄격한 적용이 필요한 기타 결과에 이 패턴을 의존하지 마세요. 보안이나 매출에 민감한 사항은 자체 서버에서 검증하세요.
{% endalert %}

<div class="scrollable-code-examples" markdown="1">

{% tabs local %}
{% tab 감정 선택기 %}

**목표:** 방문자가 행복한 얼굴 또는 불행한 얼굴을 선택하면, 선택한 내용이 `feedback_sentiment`라는 문자열 커스텀 속성에 기록됩니다.

다음을 하나의 **커스텀 코드**(HTML) 블록에 붙여넣습니다:

```html
<div id="sentiment-picker" class="sentiment-picker">
  <button type="button" data-sentiment="positive" aria-label="Happy">🙂</button>
  <button type="button" data-sentiment="negative" aria-label="Unhappy">🙁</button>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const picker = document.getElementById("sentiment-picker");

    picker.querySelectorAll("button").forEach((button) => {
      button.addEventListener("click", () => {
        picker.dataset.sentiment = button.dataset.sentiment;
        picker.querySelectorAll("button").forEach((b) => b.classList.remove("selected"));
        button.classList.add("selected");
      });
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#sentiment-picker",
      isRequired: true,
      getValue: (element) => element.dataset.sentiment ?? null,
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("feedback_sentiment", value);
      },
    });
  });
</script>

<style>
  .sentiment-picker {
    display: flex;
    gap: 16px;
    justify-content: center;
    font-size: 40px;
  }

  .sentiment-picker button {
    background: none;
    border: 2px solid transparent;
    border-radius: 12px;
    cursor: pointer;
    line-height: 1;
    padding: 8px;
  }

  .sentiment-picker button.selected {
    border-color: #1f2933;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .sentiment-picker.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**작동 방식:** 버튼을 선택하면 해당 `data-sentiment` 값이 컨테이너 요소에 저장됩니다. `getValue`는 Braze가 전달하는 컨테이너 요소에서 해당 값을 다시 읽습니다. `isRequired`가 `true`이므로 방문자가 얼굴을 선택할 때까지 폼이 제출되지 않으며, 비어 있는 동안 컨테이너에 `bz-validation-error` 클래스가 표시됩니다. 제출 시 선택한 값(`"positive"` 또는 `"negative"`)이 `feedback_sentiment`에 기록됩니다.

{% endtab %}
{% tab 스크래치 카드 %}

**목표:** 방문자가 카드를 긁어 세 가지 할인(10% Off, 20% Off, 25% Off) 중 하나를 확인하면, 해당 할인이 `scratch_off_reward`라는 문자열 커스텀 속성에 기록됩니다.

이 예제는 HTML Canvas에 스크래치 카드를 그립니다. 페이지가 로드될 때 리워드가 무작위로 선택되고 방문자가 긁어내는 불투명 레이어 아래에 숨겨집니다. Canvas 접근 방식을 원하는 스크래치 위젯으로 교체할 수 있습니다. `registerFormInput` 호출만이 이를 Braze에 연결합니다. 다음을 하나의 **커스텀 코드**(HTML) 블록에 붙여넣습니다:

```html
<div id="scratch-card" class="scratch-card" data-reward="">
  <span class="scratch-card__reward"></span>
  <canvas class="scratch-card__surface" width="300" height="150"></canvas>
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const rewards = ["10% Off", "20% Off", "25% Off"];

    const card = document.getElementById("scratch-card");
    const label = card.querySelector(".scratch-card__reward");
    const canvas = card.querySelector(".scratch-card__surface");
    const ctx = canvas.getContext("2d");

    // Randomly assign which reward this visitor will reveal.
    const reward = rewards[Math.floor(Math.random() * rewards.length)];
    label.textContent = reward;

    // Paint the opaque scratch layer over the reward.
    ctx.fillStyle = "#b3b3b3";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.globalCompositeOperation = "destination-out";

    let isScratching = false;

    function scratchAt(event) {
      const rect = canvas.getBoundingClientRect();
      ctx.beginPath();
      ctx.arc(event.clientX - rect.left, event.clientY - rect.top, 18, 0, Math.PI * 2);
      ctx.fill();
    }

    canvas.addEventListener("pointerdown", () => { isScratching = true; });
    canvas.addEventListener("pointermove", (event) => {
      if (isScratching) scratchAt(event);
    });
    canvas.addEventListener("pointerup", () => {
      isScratching = false;
      // The visitor has scratched the card, so record the revealed reward.
      card.dataset.reward = reward;
    });

    window.brazeHelpers.forms.registerFormInput({
      selector: "#scratch-card",
      isRequired: true,
      getValue: (element) => element.dataset.reward || null,
      onValidate: (value) => rewards.includes(value),
      onSubmit: (value) => {
        window.brazeBridge.getUser().setCustomUserAttribute("scratch_off_reward", value);
      },
    });
  });
</script>

<style>
  .scratch-card {
    position: relative;
    width: 300px;
    height: 150px;
    margin: 0 auto;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }

  /* The reward sits underneath and is revealed as the canvas is scratched away. */
  .scratch-card__reward {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    font-weight: 700;
    color: #1f2933;
  }

  .scratch-card__surface {
    position: absolute;
    inset: 0;
    border-radius: 12px;
    cursor: pointer;
    touch-action: none;
  }

  /* Braze adds this class to the registered element when validation fails. */
  .scratch-card.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 4px;
    border-radius: 12px;
  }
</style>
```

**작동 방식:** 페이지가 로드되면 스크립트가 세 가지 리워드 중 하나를 무작위로 선택하고 Canvas에 불투명 레이어를 그립니다. 방문자가 Canvas를 드래그하면 `"destination-out"` 합성 모드가 해당 레이어를 지우고 아래의 리워드를 드러냅니다. `pointerup` 시 드러난 리워드가 카드의 `data-reward` 속성에 기록됩니다. `getValue`는 거기서 값을 다시 읽고, `onValidate`는 정의된 세 가지 리워드 중 하나인지 확인하며, `isRequired`는 카드가 긁힐 때까지 제출을 방지합니다. 제출 시 드러난 할인(예: `"20% Off"`)이 `scratch_off_reward`에 기록됩니다.

{% endtab %}
{% tab Campaign 기여도 %}

**목표:** 방문자를 랜딩 페이지로 유도한 Campaign을 캡처하고 다운스트림 보고 및 기여도 분석을 위한 커스텀 이벤트 속성정보로 기록합니다.

이 예제는 랜딩 페이지 폼 제출을 특정 Campaign에 기여도를 부여하는 방법을 보여줍니다. 이메일, SMS 또는 WhatsApp 메시지의 랜딩 페이지 URL에 {% raw %}`{{campaign.${api_id}}}`{% endraw %}와 같은 Liquid 변수를 추가하면 Campaign 식별자를 랜딩 페이지에 전달할 수 있습니다. 그러면 커스텀 폼 블록이 URL에서 이 매개변수를 읽고 Campaign API ID를 이벤트 속성정보로 포함하는 커스텀 이벤트로 기록하여, 어떤 Campaign이 폼 제출을 유도하는지 더 쉽게 추적할 수 있습니다.

다음을 하나의 **커스텀 코드**(HTML) 블록에 붙여넣습니다:

```html
<input type="hidden" id="campaign-attribution" value="" />

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const hiddenInput = document.getElementById("campaign-attribution");
    const campaignApiId = new URLSearchParams(window.location.search).get("campaign_api_id");

    if (campaignApiId) {
      hiddenInput.value = campaignApiId;
    }

    window.brazeHelpers.forms.registerFormInput({
      selector: "#campaign-attribution",
      isRequired: false,
      getValue: (element) => element.value || null,
      onSubmit: async (value) => {
        if (!value) {
          return;
        }

        await window.brazeBridge.logCustomEvent("landing_page_form_submitted", {
          campaign_api_id: value,
        });
      },
    });
  });
</script>
```

**작동 방식:** 랜딩 페이지로 연결되는 이메일, SMS 또는 WhatsApp 메시지를 만들 때 Liquid 템플릿을 사용하여 URL에 Campaign 식별자를 추가합니다: {% raw %}`https://your-landing-page.com?campaign_api_id={{campaign.${api_id}}}`{% endraw %}. 방문자가 해당 메시지에서 랜딩 페이지에 도착하면 스크립트가 URL에서 `campaign_api_id` 매개변수를 읽고 숨겨진 입력 필드에 저장합니다. 폼 제출 시 Campaign ID가 있으면 `onSubmit` 콜백이 Campaign API ID를 이벤트 속성정보로 포함하는 `landing_page_form_submitted`라는 커스텀 이벤트를 기록합니다. 이 이벤트는 Currents에 표시되며 보고, 세분화, 기여도 분석에 사용할 수 있습니다.

{% alert tip %}
이 패턴을 확장하여 메시지 배리언트, 캔버스 단계 또는 기여도 목적으로 랜딩 페이지에 전달하려는 기타 Liquid 변수와 같은 추가 URL 매개변수를 캡처할 수 있습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

</div>

## 검증 및 필수 필드 {#validation-and-required-fields}

입력은 폼을 제출하기 전에 적용되는 다음 모든 레이어를 통과해야 합니다:

1. **`isRequired`**는 비어 있지 않은 값의 존재 여부에 따라 제출을 제어합니다. 입력에 아직 값이 없을 때 `getValue`에서 `null`을 반환하여 Braze가 비어 있음을 알 수 있도록 합니다. 빈 문자열(공백만 있는 문자열 포함)과 빈 배열도 비어 있는 것으로 처리되며, `0`과 `false`는 존재하는 값으로 간주됩니다. `isRequired`는 불리언 또는 불리언으로 해석되는 프로미스일 수 있으며, 입력이 검증될 때마다 재평가됩니다.
2. **네이티브 제약 조건 검증.** 일치하는 요소가 표준 HTML `checkValidity()` API를 지원하는 경우(예: `required`, `pattern`, `min` 또는 `max`가 있는 네이티브 `<input>`), Braze가 이를 실행하고 실패 시 제출을 차단합니다. 완전히 커스텀인 비네이티브 요소(`div`, `canvas` 등)의 경우 이 검사는 항상 통과하므로 자체 로직을 방해하지 않습니다.
3. **`onValidate`**는 자체 규칙에 따라 제출을 제어합니다. 현재 값과 일치하는 요소를 받으며, `boolean \| Promise<boolean>`(`isRequired`와 동일한 반환 유형)을 반환해야 합니다. `true`는 값이 유효함을, `false`는 유효하지 않음을 의미합니다. 허용 값 검사, 형식 검사, 범위 또는 JavaScript로 표현할 수 있는 모든 로직에 사용합니다.

### 오류 스타일링 {#error-styling}

입력이 검증에 실패할 때마다 Braze는 `selector` 또는 `element`로 일치하는 요소에 CSS 클래스 `bz-validation-error`를 추가하고, 입력이 다시 유효해지면 클래스를 제거합니다. 예를 들어 문제가 있는 입력에 주의를 끄는 윤곽선이나 테두리 등 원하는 방식으로 유효하지 않은 상태의 스타일을 지정할 수 있습니다. 요소와 `bz-validation-error` 클래스를 결합하여 대상으로 하는 규칙을 추가합니다:

```css
#my-custom-input.bz-validation-error {
  outline: 3px solid #f94144;
  outline-offset: 4px;
}
```

오류 상태 스타일링은 선택 사항이지만 권장됩니다. 방문자가 어떤 커스텀 입력이 제출을 차단하고 있는지 확인할 수 있습니다. 이 페이지의 각 [예제](#examples)에는 `bz-validation-error` 규칙이 포함되어 있습니다.

## 모범 사례 {#best-practices}

- 안정적이고 고유한 선택자를 사용합니다. `id`가 가장 안전한 선택입니다. 둘 이상의 요소와 일치할 수 있는 선택자는 피합니다.
- 값이 없을 때는 빈 문자열이나 `undefined`가 아닌 `null`을 반환하여 필수 검사가 예측 가능하게 동작하도록 합니다. 빈 문자열과 빈 배열도 비어 있는 것으로 처리되지만, `null`이 "값 없음"의 가장 명확한 신호입니다.
- `getValue`를 가볍고 동기적으로 유지합니다. Braze가 여러 번 호출할 수 있으므로 무거운 작업을 수행하지 말고 현재 값을 읽고 반환해야 합니다.
- `bz-validation-error` 상태에 스타일을 지정하여 방문자가 어떤 커스텀 입력이 제출을 차단하고 있는지 확인할 수 있도록 합니다.
- 커스텀 속성 이름을 미리 정의하고 일관되게 유지하여 나중에 데이터를 기반으로 안정적으로 세분화할 수 있도록 합니다.
- 전체 제출을 테스트합니다. 제출 후 고객 프로필에 속성이 나타나는지, 필수 및 검증 규칙이 예상대로 제출을 차단하는지 확인합니다.

## 문제 해결 {#troubleshooting}

### 아무것도 선택하지 않았는데 폼이 제출됩니다 {#the-form-submits-even-though-nothing-was-selected}
`isRequired`가 `true`로 설정되어 있는지 확인합니다. Braze는 `null`, `undefined`, 빈 문자열(공백만 있는 문자열 포함), 빈 배열을 값 없음으로 처리합니다. 아무것도 선택하지 않았을 때 `getValue`가 다른 값(예: 비어 있지 않은 기본값이나 입력 안내)을 반환하면 필수 검사가 이를 감지하지 못합니다.

### 프로필에 값이 나타나지 않습니다 {#the-value-doesnt-appear-on-the-profile}
`onSubmit`이 올바른 속성 이름으로 `window.brazeBridge.getUser().setCustomUserAttribute`를 호출하는지, **커스텀 코드** 블록이 폼과 동일한 랜딩 페이지에 있는지 확인합니다.

### 등록이 아무 효과가 없는 것 같습니다 {#registration-seems-to-do-nothing}
`registerFormInput`이 실행될 때 선택자가 DOM에 존재하는 요소와 일치하는지, 해당 요소가 렌더링된 후에 스크립트가 실행되는지 확인합니다. 그런 다음 브라우저의 개발자 콘솔을 엽니다. `registerFormInput`은 구성을 검증하며, 문제가 있을 때(예: `getValue` 누락, 유효한 CSS 선택자가 아닌 선택자, 잘못된 유형의 속성) 등록을 무시하고 `[brazeHelpers.forms.registerFormInput]` 접두사가 붙은 경고를 기록하여 무엇이 유효하지 않은지 설명합니다.

## 관련 콘텐츠 {#related-content}

- [랜딩 페이지용 JavaScript 브릿지]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge)에서 `onSubmit`에서 사용되는 전체 `brazeBridge` 참조를 다룹니다.
- [랜딩 페이지 만들기]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)