---
nav_title: 클릭 추적
article_title: 클릭 추적
page_order: 2
description: "이 참조 문서에서는 WhatsApp 메시지에서 클릭 추적을 활성화하는 방법, 단축 링크를 테스트하는 방법, 추적 링크에 커스텀 도메인을 사용하는 방법 등을 다룹니다."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# 클릭 추적 {#click-tracking}

> 이 페이지에서는 WhatsApp 메시지에서 클릭 추적을 활성화하는 방법, 단축 링크를 테스트하는 방법, 추적 링크에 커스텀 도메인을 사용하는 방법 등을 다룹니다.

클릭 추적을 사용하면 누군가가 WhatsApp 메시지의 링크를 탭했을 때 이를 측정할 수 있어, 어떤 콘텐츠가 참여를 유도하는지 명확하게 파악할 수 있습니다. Braze는 URL을 단축하고, 백그라운드에서 추적을 추가하며, 클릭 이벤트가 발생하면 이를 기록합니다.

응답 메시지와 템플릿 메시지 모두에서 클릭 추적을 활성화할 수 있습니다. 버튼과 본문 텍스트의 링크에서 작동하며, 개인화된 URL과 커스텀 도메인을 지원합니다. 활성화한 후에는 WhatsApp 성과 보고서에서 클릭 데이터를 확인하고, 누가 무엇을 클릭했는지에 따라 사용자를 세그먼트할 수 있습니다.

{% alert note %}
클릭 추적은 딥링크에서는 작동하지 않습니다. Branch or 브랜치나 Appsflyer와 같은 제공업체의 유니버설 링크를 단축할 수는 있지만, 이 과정에서 발생할 수 있는 문제(예: 기여도 분석이 깨지거나 리디렉션이 발생하는 경우)에 대해 Braze는 문제 해결을 지원할 수 없습니다.
{% endalert %}

## 작동 방식 {#how-it-works}

### 응답 메시지 {#response-messages}

응답 메시지에 대한 클릭 추적을 설정하려면:
1. 웹사이트 URL이 포함된 행동 유도(CTA) 버튼이 있는 응답 메시지를 생성합니다.
2. 인터페이스에서 지정된 버튼을 클릭하여 클릭 추적을 활성화합니다.

링크는 Braze 도메인 또는 구독 그룹에 지정된 커스텀 도메인으로 단축되며, 사용자별로 개인화됩니다.

`http://` 또는 `https://`로 시작하는 모든 정적 URL이 단축됩니다. Liquid 개인화(예: 사용자 수준 추적 타겟팅)가 포함된 단축 URL은 2개월 동안 유효합니다.

![콘텐츠 본문과 버튼이 있는 WhatsApp 메시지 작성기.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### 템플릿 메시지 {#template-messages}

템플릿 메시지의 클릭 추적은 Braze의 **WhatsApp 템플릿 빌더**를 통해 활성화하는 것을 권장합니다. 이 방법을 사용하면 URL 형식 요구 사항이 자동으로 처리되므로 WhatsApp Business 매니저에서 수동으로 구성할 필요가 없습니다.

WhatsApp Business 매니저에서 직접 템플릿을 생성하는 경우, [WhatsApp Business 매니저에서 클릭 추적 구성](#configuring-click-tracking-from-whatsapp-business-manager)을 참조하세요.

#### 템플릿 빌더 사용 {#use-the-template-builder}

템플릿 빌더에서 템플릿을 생성할 때, 클릭 추적은 **설정** 탭에서 구성합니다.

##### 1단계: 클릭 추적 활성화 {#step-1-enable-click-tracking}

템플릿 빌더에서 **설정** 탭으로 이동합니다. **링크 옵션**에서 **클릭 추적** 체크박스를 선택합니다. 활성화하면 템플릿의 모든 링크(메시지 본문과 CTA 웹사이트 버튼 모두)가 단축되고 추적됩니다.

![템플릿 빌더의 설정 탭에서 클릭 추적 체크박스가 활성화된 링크 옵션 섹션과 커스텀 도메인 드롭다운을 보여줍니다.]({% image_buster /assets/img/whatsapp/click_tracking/template_builder_settings.png %})

##### 2단계: 커스텀 도메인 선택(선택 사항) {#step-2-select-a-custom-domain-optional}

**커스텀 도메인**에서 단축 링크에 사용할 도메인을 선택합니다. 드롭다운에는 워크스페이스에 구성된 모든 커스텀 추적 도메인이 표시됩니다. 선택하지 않으면 Braze는 기본 `brz.ai` 도메인을 사용합니다.

도메인을 추가하거나 변경하려면 **구독 그룹 관리**를 선택합니다.

{% alert important %}
템플릿이 Meta에 승인을 위해 제출된 후에는 추적 도메인을 변경할 수 없습니다. 제출하기 전에 올바른 도메인을 선택했는지 확인하세요.
{% endalert %}

##### 3단계: 대상 URL 추가 {#step-3-add-your-destination-urls}

**작성** 탭으로 돌아가서 메시지 콘텐츠를 추가합니다.

- **CTA 웹사이트 버튼의 경우:** **클릭 추적 URL** 필드에 대상 URL을 입력합니다. Braze는 대상 URL을 저장하고 추적 도메인과 변수 입력 안내{% raw %}(예: `https://brz.ai/{{1}}`){% endraw %}를 사용하여 버튼의 웹사이트 URL을 자동으로 형식화합니다. 이 입력 안내가 Meta에 제출되는 내용입니다. 발송 시 Braze는 각 사용자에 대해 전체 추적 URL을 생성하고 변수를 채웁니다.
- **본문 텍스트 링크의 경우:** 본문에 직접 URL을 입력합니다.

각 버튼의 추적 URL 형식은 **웹사이트 URL** 필드에서 직접 미리볼 수 있습니다(예: `https://brz.ai/XXXXXXXX`).

![웹사이트 URL이 추적 형식으로 미리 채워진 웹사이트 방문 버튼과 대상을 위한 클릭 추적 URL 필드를 보여주는 행동 유도 버튼 섹션.]({% image_buster /assets/img/whatsapp/click_tracking/template_builder_compose.png %}){: style="max-width:70%;"}

##### 제출 후 대상 URL 업데이트 {#update-destination-urls-after-submission}

템플릿이 Meta에 제출된 후 추적 도메인은 잠기지만, 대상 URL은 언제든지 편집할 수 있습니다. 링크가 가리키는 위치를 업데이트하려면 해당 버튼의 **클릭 추적 URL** 필드를 편집합니다. 추적 URL 형식은 동일하게 유지되며, Braze는 발송 시 사용자를 새 대상으로 리디렉션합니다.

#### WhatsApp Business 매니저에서 클릭 추적 구성 {#configure-click-tracking-from-whatsapp-business-manager}

템플릿 빌더 대신 WhatsApp Business 매니저에서 템플릿을 생성하는 경우, Braze에서 템플릿을 사용할 때 클릭 추적이 올바르게 작동하도록 다음 단계를 따르세요.

##### 1단계: WhatsApp Business 매니저에서 클릭 추적을 지원하는 템플릿 구축 {#step-1-build-a-click-tracking-supported-template-in-whatsapp-business-manager}

1. WhatsApp Business 매니저에서 커스텀 도메인 또는 `brz.ai`인 기본 URL을 생성합니다.
2. 템플릿에 포함된 링크가 클릭 추적과 호환되는지 확인합니다.
3. Braze에서 Campaign으로 설정한 후에는 템플릿 변수를 변경하지 마세요. 다운스트림 변경 사항은 반영할 수 없습니다.
4. CTA 버튼 링크의 경우 **Dynamic**을 선택한 다음 기본 URL(`brz.ai` 또는 커스텀 도메인)을 제공합니다.

![행동 유도를 생성하는 섹션.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %}){: style="max-width:70%;"}

{: start="5"}
5. 본문 텍스트의 링크의 경우, WhatsApp Business 매니저에서 템플릿을 작성할 때 추적하려는 본문 내 링크에 삽입된 공백을 제거합니다.

![행동 유도의 콘텐츠 본문을 입력하는 텍스트 상자.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %}){: style="max-width:70%;"}

##### 2단계: Braze에서 템플릿 완성 {#step-2-complete-your-template-in-braze}

작성 시 Braze는 본문 텍스트와 CTA 버튼 모두에서 지원 가능한 URL 도메인이 있는 템플릿을 자동으로 감지합니다. 상태는 템플릿 하단에 표시됩니다.

![클릭 추적의 활성 상태를 보여주는 링크 상태 섹션.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **지원되는 링크:** 일치하는 기본 URL로 제출된 링크에는 클릭 추적이 활성화됩니다.
- **부분적으로 지원되는 링크:** 템플릿의 일부 링크가 전체 URL로 제출된 경우, 해당 링크에는 클릭 추적이 **적용되지 않습니다**.
- **지원되지 않는 링크:** 승인된 기본 URL이 없는 링크에는 클릭 추적 기능이 **제공되지 않습니다**.

`brz.ai` 또는 커스텀 도메인과 일치하는 기본 URL이 있는 모든 링크에 대해 대상 URL을 제공해야 합니다.

![버튼 이름, 웹사이트 URL, 클릭 추적 URL 필드가 있는 버튼 섹션.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% alert important %}
**API를 통한 템플릿 메시지 발송**: WhatsApp 클릭 추적(`brz.ai` 또는 커스텀 추적 도메인 및 메시지 작성기의 **클릭 추적 URL** 필드 사용)은 [`/messages/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)를 통해 WhatsApp 템플릿 메시지를 발송할 때 지원되지 않습니다.

API를 통해 템플릿 메시지를 발송하는 경우 CTA URL 변수(`button_variables` 사용)를 채울 수 있지만, Braze는 API 요청 흐름에서 클릭 추적 URL이나 리디렉션 링크를 생성하지 않습니다. 클릭 추적을 사용하려면 Braze 대시보드에서 또는 Braze Campaign 트리거를 통해 템플릿을 발송하세요.
{% endalert %}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## URL의 Liquid 개인화 {#liquid-personalization-in-urls}

Braze 작성기 내에서 직접 URL을 동적으로 구성할 수 있어, URL에 동적 UTM 매개변수를 추가하거나 사용자에게 고유한 링크를 보낼 수 있습니다(예: 유기한 장바구니로 이동하거나 재입고된 특정 제품으로 이동).
지원되는 모든 Liquid 개인화 태그를 사용하여 URL을 동적으로 생성할 수 있습니다.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

다음 예시와 같이 커스텀 정의된 Liquid 변수의 단축도 지원합니다:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Liquid 변수로 렌더링된 URL 단축 {#shorten-urls-rendered-by-liquid-variables}

Braze는 API 트리거 속성에 포함된 URL을 포함하여 Liquid로 렌더링된 URL을 단축합니다. 예를 들어, {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}가 유효한 URL을 나타내는 경우, WhatsApp 메시지를 발송하기 전에 해당 URL을 단축하고 추적합니다.

## 테스트 {#testing}

Campaign 또는 Canvas를 시작하기 전에 먼저 메시지를 미리보기하고 테스트하는 것이 좋습니다. 이를 위해 **테스트** 탭으로 이동하여 콘텐츠 테스트 그룹 또는 개별 사용자에게 WhatsApp을 미리보기하고 발송합니다.

이 미리보기는 관련 개인화 및 단축 URL로 업데이트됩니다.

{% alert important %}
활성 Canvas 내에서 초안이 생성된 경우 단축 URL이 생성되지 않습니다. 실제 단축 URL은 Canvas 초안이 활성화될 때 생성됩니다.
{% endalert %}

## 보고 {#reporting}

클릭 추적이 활성화되었거나 지원되는 템플릿과 함께 사용되는 경우, WhatsApp 성과 테이블에는 배리언트별 클릭 이벤트 수와 관련 클릭률을 보여주는 **총 클릭 수** 열이 포함됩니다. WhatsApp 측정기준에 대한 자세한 내용은 [WhatsApp 메시지 성과]({{site.baseurl}}/user_guide/channels/whatsapp/reporting)를 참조하세요.

![WhatsApp 메시지 캔버스 단계.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

클릭 데이터는 분석 대시보드에 자동으로 보고됩니다.

![WhatsApp 메시지 성과 테이블.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## 사용자 리타겟팅 {#retargeting-users}

`Clicked/Opened Step` 필터와 `clicked tracked WhatsApp link` 상호작용을 사용하여 링크와의 상호작용을 기반으로 사용자를 세그먼트할 수 있습니다.

![추적된 WhatsApp 링크 클릭 필터가 있는 필터 그룹.]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### 어떤 개별 사용자가 URL을 클릭하는지 알 수 있나요? {#do-i-know-which-individual-users-are-clicking-on-a-url}

예. 클릭 추적이 활성화된 경우(또는 템플릿 구성에 따라 활성화된 경우), WhatsApp 리타겟팅 필터 또는 Currents에서 전송하는 WhatsApp 클릭 이벤트(`users.messages.whatsapp.Click`)를 활용하여 URL을 클릭한 사용자를 리타겟할 수 있습니다.

### WhatsApp 기기에서의 미리보기가 클릭으로 집계되나요? {#do-previews-on-the-whatsapp-device-count-as-clicks}

아니요, WhatsApp 메시지의 클릭률에 기여하지 않습니다.