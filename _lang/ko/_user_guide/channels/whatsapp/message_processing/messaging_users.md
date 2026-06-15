---
nav_title: "사용자 메시지"
article_title: "WhatsApp 사용자 메시지"
description: "이 참조 문서에서는 Braze가 사용자 메시지를 처리하는 방법에 대해 설명합니다."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# 사용자 메시지 {#user-messages}

> WhatsApp은 양방향 소통 채널입니다. 브랜드가 사용자에게 메시지를 보낼 수 있을 뿐만 아니라, 사용자도 템플릿 기반 Campaigns와 Canvases를 사용하여 대화에 참여할 수 있습니다. WhatsApp 빠른 답장, 목록 메시지, 트리거 단어 등 다양한 방법이 있습니다. 빠른 답장과 목록 메시지의 행동 유도(CTA)는 WhatsApp 메시징에 대한 사용자 참여를 유도하는 좋은 방법입니다.

## 행동 기반 트리거 {#action-based-triggers}

Campaigns와 Canvases 모두 트리거 단어와 같은 인바운드 WhatsApp 메시지(사용자가 WhatsApp으로 보내는 메시지)를 통해 시작, 분기, 여정 중간 변경이 가능합니다.

트리거 단어가 사용자에게 기대하는 내용과 일치하는지 확인하세요.

**알아두어야 할 사항:**
- 트리거 단어의 각 글자는 설정 시 대문자로 입력해야 합니다. Braze는 사용자가 보내는 인바운드 트리거 단어가 대문자일 것을 요구하지 않습니다. 예를 들어, "jOin2023"이라고 메시지를 보내도 Canvas 또는 Campaign이 트리거됩니다.
- 진입 스케줄 행동 기반 트리거에 트리거 단어가 지정되지 않은 경우, Campaign 또는 Canvas는 모든 인바운드 WhatsApp 메시지에 대해 실행됩니다. 여기에는 활성 Campaigns 및 Canvases에서 일치하는 문구가 있는 메시지도 포함되며, 이 경우 사용자는 두 개의 WhatsApp 메시지를 받게 됩니다.

{% tabs %}
{% tab Campaign %}

![행동 기반 Campaign 스케줄링 옵션.]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

![행동 기반 Canvas 스케줄링 옵션.]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## 인식되지 않는 응답 {#unrecognized-responses}

인터랙티브 Canvases에 인식되지 않는 응답에 대한 옵션을 포함하는 것을 권장합니다. 이를 통해 사용자가 사용 가능한 프롬프트를 이해하고 채널에 대한 기대치를 설정할 수 있습니다. 기대치 관리는 라이브 상담원 채팅이 있는 WhatsApp 채널이 있는 경우 특히 유용할 수 있습니다.
- 동작 단계에서 커스텀 필터 문구에 대한 동작 그룹을 생성한 후, "WhatsApp 메시지 보내기"에 대한 추가 동작 그룹을 추가하되 **메시지 본문이 다음인 경우**를 체크하지 마세요. 이렇게 하면 "else" 절과 유사하게 인식되지 않는 모든 사용자 응답을 포착합니다.
- 이 채널에 담당자가 없음을 사용자에게 알리고 필요한 경우 고객지원 채널로 안내하는 WhatsApp 메시지로 후속 조치를 취하는 것을 권장합니다.

## 빠른 답장 {#quick-replies}

![행동 유도 버튼을 클릭하면 버튼 텍스트가 답장으로 전송되는 것을 보여주는 휴대폰 화면.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

빠른 답장은 대화 내에서 클릭 가능한 버튼 옵션으로 표시되지만, 사용자가 텍스트로 답장한 것처럼 작동합니다. Braze는 이를 인바운드 메시지로 처리하고, 클릭한 버튼에 따라 설정된 응답을 보낼 수 있습니다. 사용자의 응답을 생성하고 필터링할 때 "인바운드 WhatsApp 메시지 동작" 단계를 사용하세요.

![텍스트와 세 개의 행동 유도 버튼이 있는 WhatsApp 메시지.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Canvas에서 빠른 답장 경험 구성하기 {#configure-the-quick-reply-experience-in-canvas}

#### 1단계: CTA 구축 {#step-1-build-out-ctas}

먼저 메시지 템플릿 내의 [WhatsApp 메시지 템플릿 매니저](https://business.facebook.com/wa/manage/message-templates/)에서 빠른 답장 CTA를 구축하세요.

![CTA 버튼 생성 방법을 보여주는 WhatsApp 메시지 템플릿 매니저 UI로, 버튼 유형(커스텀)과 버튼 텍스트를 제공합니다.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

템플릿이 제출되고 WhatsApp의 승인을 받으면 Braze 내에서 Canvas를 구축하는 데 사용할 수 있습니다.

{% alert tip %}
메시지 템플릿 승인을 받기 전에 Canvas를 구축할 수 있습니다.
{% endalert %}

#### 2단계: Canvas 구축 {#step-2-build-your-canvas}

다음으로, 생성한 템플릿이 포함된 메시지 단계가 있는 Canvas를 구축하세요.

![빠른 답장 템플릿이 채워진 WhatsApp 단계 메시지 작성기.]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

메시지 단계 뒤에 동작 단계를 생성하세요. 이 동작 단계에서 빠른 답장 옵션별로 하나의 그룹을 생성하세요.

![평가 동작이 'WhatsApp 인바운드 메시지 보내기'인 Canvas.]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

각 빠른 답장 옵션 그룹에 대해 매칭하려는 버튼과 정확히 동일한 텍스트를 지정하세요. 키워드는 대문자여야 합니다.

![특정 메시지 본문이 수신될 때 전송되도록 설정된 'WhatsApp 인바운드 메시지 보내기' 동작이 있는 캔버스 단계.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

빠른 답장 대신 텍스트로 메시지에 응답하는 사용자를 위한 기본 응답을 원하는 경우, 일치하는 메시지 본문이 없는 추가 그룹을 생성하세요.

이 시점부터 평소와 같이 Canvas를 계속 구축하세요.

### 응답 {#responses}

각 응답에 대한 답장 메시지를 원할 가능성이 높습니다. 빠른 답장 범위 밖의 응답(예: 미리 정해진 프롬프트가 아닌 일반 메시지로 응답하는 고객)에 대한 포괄적인 옵션을 포함하는 것을 권장합니다. 예를 들어, "죄송합니다, 응답을 인식하지 못했습니다. 고객지원 문의는 <고객지원 채널>로 메시지를 보내주세요."

![각 행동 유도 버튼에 대한 응답을 보여주는 구축된 Canvas.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

응답 메시지, 고객 프로필 업데이트, Braze 간 웹훅 등 Braze Canvas가 제공하는 모든 후속 동작을 사용할 수 있습니다.

## 목록 메시지 {#list-messages}

목록 메시지는 클릭 가능한 옵션 목록이 포함된 본문 메시지로 표시됩니다. 각 목록에는 여러 섹션이 있을 수 있으며, 각 목록에는 최대 10개의 행이 포함될 수 있습니다.

![다양한 패션 스타일에 대한 행이 있는 WhatsApp 목록 메시지 예시.]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Canvas에서 목록 메시지 경험 구성하기 {#configure-the-list-message-experience-in-canvas}

#### 1단계: 행동 기반 Canvases 생성 또는 편집 {#step-1-create-or-edit-an-existing-action-based-canvases}

WhatsApp 목록 메시지는 사용자 메시지에 대한 응답이어야 하므로 행동 기반 Canvases에만 추가할 수 있습니다.

#### 2단계: WhatsApp 메시지 단계 생성 {#step-2-create-a-whatsapp-message-step}

WhatsApp [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)를 추가한 다음 **목록 메시지** 응답 메시지 레이아웃을 선택하세요.

![생성할 수 있는 다양한 유형의 WhatsApp 응답 메시지 중 '목록 메시지'를 포함한 선택 가능한 컬렉션.]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

사용자가 목록을 표시하기 위해 선택할 **목록 버튼** 이름을 추가하세요. 그런 다음 **목록 콘텐츠**의 필드를 사용하여 목록을 생성하세요:

- **섹션:** 목록 항목을 그룹화하고 정리하기 위해 최대 10개의 섹션을 추가하세요. 예를 들어, 의류 소매업체는 섹션을 사용하여 시즌별 스타일(봄, 여름, 가을, 겨울 등) 또는 의류 항목(상의, 하의, 신발 등)별로 정리할 수 있습니다.
- **행:** 모든 섹션에 걸쳐 최대 10개의 행 또는 목록 항목을 추가하세요.
- **행 설명(선택 사항):** 모든 행(목록 항목)에 선택적 설명을 추가하세요.

![두 개의 섹션과 여러 행 및 행 설명이 채워진 '목록 콘텐츠' 섹션.]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

이름 옆의 아이콘을 선택하고 드래그하여 섹션과 행의 순서를 변경하세요.

![목록 섹션을 새 위치로 드래그하는 모습.]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

Canvas 작성기로 돌아가서 메시지 단계 뒤에 각 목록 응답에 대한 그룹이 있는 [행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/)를 추가하세요. 각 그룹에서:

1. **인바운드 WhatsApp 구독 그룹 전송**에 대한 트리거를 추가하고 해당 WhatsApp 구독 그룹을 선택하세요.
2. **메시지 본문이 다음인 경우** 체크박스를 선택하세요.
3. 하나의 행(또는 목록 항목)에 대한 콘텐츠를 지정하세요.

![다양한 의류 스타일에 대한 그룹이 있는 행동 경로 작성기.]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

Canvas를 계속 구축하세요.

### 긴 설명에 대한 행동 경로 생성 {#creating-actions-paths-for-long-descriptions}

행 설명이 있는 경우 행을 지정하기 위해 **정규식 일치**를 사용해야 합니다. 예를 들어, "좋아하는 앵클 부츠 위에 신을 수 있는 새로운 스타일"이라는 설명이 있는 행을 지정하려면 "앵클 부츠"로 [정규식]({{site.baseurl}}/user_guide/audience/segments/regex/)을 사용할 수 있습니다.

!['정규식 일치' 필터를 사용하여 '앵클 부츠'가 포함된 응답 메시지를 캡처하는 WhatsApp 트리거.]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## 고려 사항 {#considerations}

### 응답 메시지의 타이밍 요구 사항 {#timing-requirements-for-response-messages}

응답 메시지는 사용자의 메시지를 수신한 후 24시간 이내에 전송되어야 합니다. 성공적인 경험을 구축하기 위해 Braze는 메시지 로직을 확인하여 응답 메시지를 차단 해제하는 업스트림 인바운드 사용자 메시지가 있는지 확인합니다.

다음 이벤트가 응답 메시지를 차단 해제합니다:

- 인바운드 메시지
  - **WhatsApp 인바운드 메시지 보내기** 트리거가 있는 [행동 경로]({{site.baseurl}}/action_paths/) 또는 [행동 기반 진입]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/).

![트리거가 'WhatsApp 인바운드 메시지 보내기'인 행동 기반 진입 단계.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [API 트리거 진입]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/)
- 인바운드 제품 메시지
  - [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events?tab=ecommerce.cart_updated) 이벤트

![수행된 커스텀 이벤트 `ecommerce.cart_updated` 트리거가 있는 행동 경로.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

### 커스텀 시간 속성으로 필터링 {#filtering-by-a-custom-time-attribute}

행동 기반 WhatsApp Campaign 또는 Canvas 오디언스가 상대적 기간 내(예: 현재부터 향후 24시간 사이)에 해당하는 커스텀 시간 속성에 의존하는 경우, [시간]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#time)에 설명된 대로 두 개의 필터를 결합하세요.