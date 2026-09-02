---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 3
description: "이 참조 문서에서는 WhatsApp Flows 메시지를 구축하고 생성하는 데 관련된 단계를 다룹니다."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flows는 기존 WhatsApp 채널의 향상된 기능으로, 인터랙티브하고 동적인 메시징 경험을 만들 수 있게 해줍니다. 이 페이지에서는 WhatsApp Flows 사용에 대한 단계별 안내를 제공합니다.

## WhatsApp Flows 설정하기 {#setting-up-whatsapp-flows}

1. Meta 계정에 로그인합니다.
2. 두 가지 주요 위치 중 하나에서 Flows를 생성합니다:
    - **계정 도구:** **Flows** 탭으로 이동하여 Flow ID를 확인하고 새 Flow를 생성합니다.
    - **템플릿 관리:** Flows를 생성할 때 권장되는 방법입니다. 여기에서 템플릿을 생성하고 템플릿 생성 과정에서 Flow 옵션을 선택할 수 있습니다.

![Flows 템플릿을 생성하는 페이지가 표시된 WhatsApp Manager.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{% alert tip %}
[WhatsApp 템플릿 빌더]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder)를 사용하여 Braze에서 마케팅 또는 유틸리티 Flow 템플릿을 생성할 수도 있습니다. Meta의 WhatsApp Manager에서 Flow 자체를 생성하고 관리한 다음, Braze에서 템플릿을 빌드할 때 해당 Flow를 선택합니다.
{% endalert %}

{: start="3"}
3. 기존 Flow를 선택하거나 새로 생성합니다. Flow를 생성하는 경우, 두 가지 옵션 중 하나를 선택합니다:
  - **커스텀 폼:** 특정 요구 사항에 적합
  - **사전 디자인된 요소:** 더 빠른 설정에 적합

## WhatsApp Flow 메시지 및 응답 구성하기 {#configuring-whatsapp-flow-messages-and-responses}

{% tabs local %}
{% tab 템플릿 메시지 %}

1. Braze Canvas에서 해당 Flow가 포함된 템플릿 메시지를 사용하는 WhatsApp 메시지 단계를 생성합니다.
2. 템플릿 생성을 계속합니다. 필요한 경우 미디어, 변수 콘텐츠 또는 둘 다를 메시지에 추가합니다. Flow 선택은 템플릿 생성 시 이루어지므로 Flow 경험에 대한 추가 정보는 필요하지 않습니다.

![WhatsApp Flow 템플릿을 사용하는 WhatsApp 메시지 작성기.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab 응답 메시지 %}

1. Braze Canvas에서 응답 메시지와 Flow 메시지를 사용하는 WhatsApp 메시지 단계를 생성합니다.

![WhatsApp 응답 메시지 유형과 Flow 메시지 레이아웃을 위한 메시지 단계.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. 해당 Flow를 선택한 다음 메시지 생성을 계속합니다.

![Flow 선택을 위한 드롭다운이 확장된 Flow 메시지 응답 작성기.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Flow 미리보기 {#preview-flow}

Flow가 포함된 Canvas를 시작하기 전에 **Preview Flow**를 선택하여 Braze에서 직접 Flow를 미리보기하고 예상대로 작동하는지 확인할 수 있습니다. 미리보기에서 Flow와 상호작용하여 사용자가 Flow를 탐색하는 방식을 직접 경험하고, 실시간으로 조정할 수도 있습니다. Flow에 여러 페이지가 포함되어 있는 경우 각 페이지와 상호작용할 수 있습니다.

![사용자가 가입을 완료하기 위한 양식을 표시하는 미리보기 창.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## 전체 Flow 응답 저장하기 {#full-flow}

WhatsApp Flow 메시지를 Braze Canvas 또는 Campaign에 통합할 때, 사용자가 Flow를 통해 제출하는 특정 정보를 캡처하고 활용하고 싶을 수 있습니다. Braze는 사용자 응답의 구조, 특히 JSON 응답의 예상 형태에 대한 추가 정보를 받아야 필요한 중첩 고객 속성(NCA) 스키마를 생성할 수 있습니다.

### 1단계: Flow 커스텀 속성 생성하기 {#step-1-generate-the-flow-custom-attribute}

{% tabs local %}
{% tab 권장 방법 %}

Braze에 응답 구조에 대한 정보를 제공하는 가장 간단한 방법은 Flow 응답을 커스텀 속성으로 저장하고 테스트 전송을 완료하는 것입니다.

#### Braze에서 사용된 적 없는 Flow 사용하기 {#using-a-flow-that-hasnt-been-used-in-braze}

Braze 내에서 이전에 사용된 적 없는 Flow를 사용하는 경우, **메시지 작성**에서 **Flow 커스텀 속성** 섹션을 볼 때 정보가 표시되지 않을 수 있습니다. 이는 스키마가 아직 생성되지 않았음을 의미합니다.

![Flow 커스텀 속성을 볼 수 있는 옵션이 있는 Meta Flow 섹션.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

이를 해결하려면 다음을 수행합니다:

1. WhatsApp 메시지 단계 설정을 완료합니다.
2. **Flow 응답을 커스텀 속성으로 저장**이 체크되어 있는지 확인합니다.
3. 자신에게 테스트 메시지를 보내고 사용자로서 Flow를 완료합니다.

이제 Braze가 Flow 응답 JSON의 형태를 파악하여 커스텀 속성을 생성할 수 있습니다.

{% endtab %}
{% tab 대체 방법 %}

고급 JSON 편집기를 사용하여 Flow 응답의 속성을 커스텀 속성에 저장하거나, 다단계 Canvas를 사용하여 응답을 중첩 고객 속성에 저장합니다.

{% subtabs %}
{% subtab 고급 JSON 편집기 %}

고급 JSON 편집기에서 {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}를 입력합니다. 여기서 "flow_1"은 Flow를 저장하려는 커스텀 속성입니다.

![고급 JSON 편집기가 있는 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI 편집기 %}

1. 워크스페이스 데이터 설정 내에서 오브젝트 데이터 유형의 커스텀 속성(이 예시에서는 "flow_1")을 이미 생성했는지 확인합니다.
2. UI 편집기에서 Liquid {% raw %}`{{whats_app.${inbound_flow_response}}}`를 사용하여 커스텀 속성을 채우고 사용자의 전체 Flow 응답을 저장합니다. 생성한 커스텀 속성을 선택하기 전에 키 값을 `{{whats_app.${inbound_flow_response}}}`{% endraw %}로 채워야 합니다.

![UI 편집기를 사용하는 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Braze가 Flow 응답을 수신하면 지정된 이름으로 중첩 고객 속성을 고객 프로필에 저장합니다. 해당 커스텀 속성은 Canvases를 구축할 때 가져올 수 있습니다.

!["flow_1" 커스텀 속성의 내용을 표시하는 창.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 2단계: 저장된 Flow 응답 확인하기 {#step-2-view-the-saved-flow-response}

Flow가 완료되면 Braze는 Flow ID를 기반으로 이름이 지정된 Flow 커스텀 속성을 자동으로 생성합니다. 그런 다음 고객 프로필로 이동하여 **커스텀 속성** 섹션에서 중첩 오브젝트로 저장된 Flow 응답을 확인할 수 있습니다.

스키마가 생성된 후 Flow **커스텀 속성** 섹션에는 각 응답에 대한 예상 데이터 유형(예: "String" 또는 "String Array")을 포함한 예상 구조가 표시됩니다.

![스키마 드롭다운이 있는 Flow 커스텀 속성 세부 정보 창.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### 고려 사항 {#considerations}

- **기존 속성:** 특정 Flow에 대한 커스텀 속성이 이미 생성된 경우, Flow는 사용 가능한 속성 정보와 함께 로드됩니다. 이 경우 Braze가 이미 예상 응답 메시지를 인식하고 있으므로 스키마를 생성하기 위해 테스트 메시지를 보낼 필요가 없습니다.
- **Flow 변경:** 스키마가 생성된 후 Flow를 변경하는 경우, Braze가 Flow 응답의 형태가 변경되었음을 이해하고 속성 구조를 적절히 조정할 수 있도록 추가 테스트 메시지를 보내야 합니다. 이 작업은 24시간에 한 번으로 제한됩니다.
- **일관성:** 생성된 Flow 커스텀 속성은 일관적이며, 사용되는 Canvas에 관계없이 이 특정 Flow에 대해 동일한 속성이 됩니다.
- **수동 옵션:** **Flow 응답을 커스텀 속성으로 저장** 체크박스를 반드시 선택할 필요는 없습니다. [Flow 응답의 특정 필드를 특정 커스텀 속성에 저장](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute)하여 커스텀 속성을 수동으로 생성할 수 있으며, 이를 통해 사용자 단계의 중복을 방지할 수 있습니다.

## Flow 응답에서 특정 필드를 특정 커스텀 속성에 저장하기 {#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute}

### 1단계: 행동 경로 만들기 {#step-1-create-an-action-path}

[행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) 캔버스 단계 또는 액션 기반 Campaign을 만드세요. **WhatsApp 인바운드 메시지 전송** 트리거와 **Flow에 응답함** 조건을 선택한 다음, 관련 Flow 또는 **모든 Flow**를 선택합니다.

![인바운드 WhatsApp 메시지를 보내고 모든 Flow에 응답한 사용자에 대한 트리거.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### 2단계: Flow 응답에서 필드 추출하기 {#step-2-extract-fields-from-flow-responses}

중첩 커스텀 속성 또는 `json_parse` Liquid 태그를 사용하여 Flow 응답에서 특정 필드를 추출할 수 있습니다.

{% tabs %}
{% tab 중첩 커스텀 속성 %}

사용자의 Flow 응답 중 특정 부분을 저장하려면 [전체 Flow 응답 저장하기](#full-flow)의 모든 단계를 완료하세요. **Canvas 실행도 포함해야 합니다**. 참조할 중첩 커스텀 속성을 생성하려면 Canvas를 실행해야 합니다. Canvas를 실행하고 Flow를 완료한 후 다음 단계를 수행하세요:

1. UI 에디터를 사용하는 후속 사용자 업데이트 단계를 만드세요.
2. **개인화 추가**를 선택한 다음, **중첩 커스텀 속성**과 Flow가 저장된 해당 최상위 속성을 선택합니다.

![중첩 커스텀 속성 개인화가 포함된 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3. 저장하려는 키 속성을 선택하고 Liquid를 **키 값** 필드에 삽입합니다.

![선택 가능한 속성이 표시된 "flow_1" 창.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4. 저장할 속성을 선택합니다.
5. 테스트 메시지를 보내 Flow를 테스트합니다.

{% endtab %}
{% tab Parse 함수 %}

`json_parse` Liquid 태그를 사용하여 Flow에서 특정 응답을 추출합니다. 예를 들어, Flow 토큰과 선택된 옵션을 가져와 후속 메시지를 커스터마이즈할 수 있습니다.

UI 에디터에서 다음을 선택하세요:

- **속성 이름:** YOUR_CUSTOM_ATTRIBUTE (이 예시에서는 "First_name")
- **작업:** 업데이트
- **키 값:** {% raw %} `{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}`{% endraw %}

![커스텀 속성 `inbound_flow_response`로 WhatsApp 속성 개인화를 삽입하는 "개인화 추가" 컴포넌트가 있는 WhatsApp 메시지 작성기.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

준비가 되면 테스트 메시지를 보내 Flow를 테스트하세요. 그런 다음 Canvas를 실행하세요!

{% endtab %}
{% endtabs %}

{% alert note %}
새로운 WhatsApp 메시지는 Canvas의 Liquid Flow 응답 사용(및 재사용) 기능을 "초기화"하므로, 후속 메시지는 Liquid Flow 응답을 사용하는 모든 사용자 업데이트 단계, 웹훅 또는 기타 단계 이후에 배치해야 합니다.
{% endalert %}

## Flow 개인화 태그 추가하기 {#adding-a-flow-personalization-tag}

Liquid를 사용하여 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)와 함께 Flow 응답을 활용하려면 다음 단계를 완료하세요:

1. WhatsApp 메시지를 작성할 때, <i class="fas fa-plus-circle" aria-label="개인화 추가"></i> **개인화 추가**를 선택하여 **개인화 추가** 창을 엽니다.
2. 개인화 유형으로 **WhatsApp Properties**를 선택하고, 커스텀 속성으로 **inbound_flow_response**를 선택합니다. 이 속성은 고객 프로필에 정보를 저장하거나 메시지에 포함하거나 웹훅과 같은 다른 서비스로 전달하는 데 사용할 수 있습니다.

![커스텀 속성 inbound_flow_response로 WhatsApp 속성 개인화를 삽입하는 '개인화 추가' 컴포넌트가 있는 WhatsApp 메시지 작성기.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

질문이 있거나 추가 지원이 필요한 경우 [지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.