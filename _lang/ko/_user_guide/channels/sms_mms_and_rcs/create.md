---
nav_title: 메시지 만들기
article_title: SMS, MMS 또는 RCS 메시지 만들기
page_order: 1
description: "이 문서에서는 Braze에서 SMS, MMS 또는 RCS 메시지를 만들고 발송하는 방법을 설명합니다."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# SMS, MMS 또는 RCS 메시지 만들기 {#create-an-sms-mms-or-rcs-message}

> SMS, MMS, RCS Campaign(캠페인)은 고객에게 직접 도달하고 프로그래밍 방식으로 대화하는 데 매우 유용합니다. Liquid 및 기타 동적 콘텐츠를 사용하여 사용자에게 개인화된 경험을 제공하고, 브랜드와의 자연스러운 사용자 경험을 촉진하고 향상시키는 환경을 만들 수 있습니다.

## 1단계: 메시지를 작성할 위치 선택 {#step-1-choose-where-to-build-your-message}

메시지를 Campaign으로 보낼지 Canvas로 보낼지 확실하지 않으신가요? Campaign은 단일 타겟 메시징에 적합하고, Canvas는 다단계 사용자 여정에 더 적합합니다.

{% tabs %}
{% tab Campaign %}

1. **메시징** > **Campaigns**로 이동하여 **캠페인 생성**을 선택합니다.
2. **SMS/MMS/RCS**를 선택하거나, 여러 채널을 타겟팅하는 Campaign의 경우 **멀티채널**을 선택합니다.
3. Campaign에 명확하고 의미 있는 이름을 지정합니다.
4. 필요에 따라 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) 및 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/)를 추가합니다.
   * 태그를 사용하면 Campaign을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder/)를 사용할 때 특정 태그로 필터링할 수 있습니다.
5. Campaign에 필요한 만큼 배리언트를 추가하고 이름을 지정합니다. 추가된 각 배리언트에 대해 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing/)를 참조하세요.
   * Braze에서는 단일 Campaign 내에 SMS와 RCS 배리언트를 모두 포함할 수 있으므로 각각의 성과를 비교할 수 있습니다.

{% alert tip %}
Campaign의 모든 메시지가 유사하거나 동일한 콘텐츠를 가질 경우, 추가 배리언트를 추가하기 전에 먼저 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. Canvas 작성기를 사용하여 [Canvas를 만듭니다]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).
2. Canvas를 설정한 후 Canvas 빌더에서 **SMS/MMS/RCS** 메시지 단계를 추가합니다.
3. 단계에 명확하고 의미 있는 이름을 지정합니다.
4. [단계 스케줄]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay)을 선택하고 필요에 따라 지연을 지정합니다.
5. 필요에 따라 이 단계의 오디언스를 필터링합니다. Segments를 지정하고 추가 필터를 추가하여 이 단계의 수신자를 더 세밀하게 조정할 수 있습니다. 오디언스 옵션은 메시지가 발송되는 시점에 지연 후 확인됩니다.
6. [진행 동작]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/)을 선택합니다.
7. 메시지와 함께 사용할 다른 메시징 채널을 선택합니다.

{% endtab %}
{% endtabs %}

## 2단계: 구독 그룹 선택 {#step-2-select-a-subscription-group}

적절한 사용자에게 메시지를 보내려면 [구독 그룹]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/)을 선택합니다. 구독 그룹을 선택하면 Braze가 자동으로 세그먼팅 필터를 추가하여 구독한 사용자만 Campaign을 수신하도록 합니다.

선택한 구독 그룹에 따라 작성기에서 사용할 수 있는 메시지 유형이 결정됩니다:

| 구독 그룹 유형 | 사용 가능한 메시지 유형 |
| --- | --- |
| SMS 전용 | SMS |
| MMS 지원 번호가 포함된 SMS | SMS 및 MMS |
| RCS 지원(RCS 인증 발신자 포함) | SMS, MMS(활성화된 경우) 및 RCS |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Select a subscription group" }

{% alert tip %}
Braze는 RCS 발신자를 포함하는 모든 구독 그룹에 대체용 SMS 코드를 하나 이상 포함할 것을 강력히 권장합니다. 이렇게 하면 RCS 메시지가 전달되지 않는 경우(예: 기기 호환성 문제 또는 불완전한 통신사 커버리지) SMS를 통해 사용자에게 메시지가 전달됩니다.
{% endalert %}

구독 그룹을 선택한 후 작성할 메시지 유형을 선택합니다. 구독 그룹이 여러 유형을 지원하는 경우 유형 간에 선택할 수 있는 옵션이 표시됩니다.

![RCS 또는 SMS/MMS 메시지 유형 중에서 선택하는 옵션.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

## 3단계: 메시지 작성 {#step-3-compose-your-message}

선택한 메시지 유형에 따라 작성 경험이 달라집니다. 메시지 유형에 해당하는 탭을 선택하세요.

{% tabs local %}
{% tab SMS %}

언어와 개인화(Liquid, 연결된 콘텐츠, 이모지)를 필요에 따라 사용하여 메시지를 작성합니다. 초과 요금이 발생할 가능성을 줄이기 위해 메시지 문구 제한을 준수하세요.

{% alert important %}
진행하기 전에 [SMS 메시지 세그먼트 및 문구 제한]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/) 가이드라인을 읽어보세요. SMS 메시지 세그먼트는 통신사가 문자 메시지를 측정하는 데 사용하는 문자 배치입니다. 메시지는 메시지 세그먼트당 요금이 부과되므로 메시지가 어떻게 분할되는지에 대한 세부 사항을 이해하는 것이 좋습니다.
{% endalert %}

![Braze의 SMS 작성기에 "Hi first_name, we appreciate your support! Why not stop by one of our stores and show them this SMS for an exclusive discount? Reply STOP to stop receiving messages from us."라는 메시지가 표시된 모습.]({% image_buster /assets/img/sms_campaign_compose.png %})

### 연락처 카드 추가 {#adding-a-contact-card}

SMS 메시지에 연락처 카드를 추가하여 고객이 비즈니스 및 연락처 정보를 기기 연락처에 추가할 수 있도록 할 수 있습니다. 회사 이름, 전화번호, 주소, 이메일, 작은 사진 등의 등록정보를 할당할 수 있습니다. 자세한 내용은 [연락처 카드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card/)를 참조하세요.

{% endtab %}
{% tab MMS %}

MMS 메시지를 보내려면 구독 그룹에 MMS 지원 전화번호가 하나 이상 있어야 합니다. 이는 작성기에서 구독 그룹 옆에 **MMS** 태그로 표시됩니다.

메시지 본문을 입력한 다음 [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)에서 PNG, JPEG 또는 GIF 이미지를 업로드하거나 이미지 URL을 지정합니다. 메시지당 하나의 이미지만 지원됩니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

![MMS 메시지를 작성하기 위한 작성 탭.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### 이미지 사양 {#image-specifications}

| 등록정보 | 권장 사항 |
| --- | --- |
| 크기 | 최대 600&nbsp;KB |
| 파일 유형 | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image specifications" }

### 연락처 카드 {#contact-cards}

이미지 대신 [연락처 카드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card/)(vCard)를 포함할 수도 있습니다.

### 통신사 동작 {#carrier-behavior}

MMS 메시지는 텍스트 전용 SMS와 다른 요금으로 청구됩니다. 모든 통신사가 MMS를 수신할 수 있는 것은 아닙니다. 이러한 경우 MMS는 사용자가 선택할 수 있는 이미지 링크로 자동 변환됩니다.

### 인바운드 MMS 및 개인화 {#inbound-mms-and-personalization}

고객이 미디어가 포함된 인바운드 메시지를 보내면 Braze는 [Currents SMS 인바운드 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events) 및 Liquid에서 {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %}로 미디어를 노출합니다(예: 리타겟팅 또는 후속 메시지에서). Canvas에서 인바운드 SMS 등록정보를 사용하는 방법에 대한 자세한 내용은 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)를 참조하세요.

{% endtab %}
{% tab RCS %}

RCS 텍스트 또는 미디어 메시지를 만드는 방법에 대한 간단한 안내를 시청하세요.

{% multi_lang_include video.html id="3y0iiqqygw" source="wistia" %}

**텍스트** 또는 **미디어** 메시지 유형 중에서 선택합니다.

![텍스트 또는 미디어 메시지 유형 중에서 선택하는 옵션.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% subtabs %}
{% subtab 텍스트 %}

RCS 텍스트 메시지는 텍스트를 매체로 사용합니다. 메시지가 리치 요소 없이 160자 이하인 경우 기본 RCS 메시지로 청구됩니다. 160자를 초과하거나 리치 요소를 사용하면 문자 제한이 3,072자인 리치(단일) RCS 메시지로 청구됩니다.

**기능:**

- 모든 SMS 기능이 포함되며, URL 클릭 추적을 위한 고급 추적이 가능합니다.
- **추천 답장**: 사용자가 선택하여 텍스트 입력에 미리 채울 수 있는 추천 응답이 포함된 버튼입니다.
- **추천 동작**: 사용자의 기기에서 동작을 시작하는 버튼입니다. Braze는 현재 사용자를 웹페이지 또는 기타 URL로 리디렉션하는 OpenURL 추천 동작을 지원합니다.

![트렌디한 패션 스타일을 홍보하는 RCS 메시지의 세 가지 추천 동작.]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

**고려 사항:**

- Android와 iOS는 다르게 잘릴 수 있습니다: Android는 전체 리치 메시지 텍스트를 표시하지만, iOS는 세 번째 줄 이후에 잘립니다.
- 메시지당 최대 5개의 버튼을 추가할 수 있습니다. 추천 동작 또는 추천 답장 중 하나일 수 있습니다.
- 긴 텍스트 블록과 많은 버튼은 수신자를 압도할 수 있으므로 가능하면 간결하게 유지하세요.
- 경우에 따라 긴 텍스트 전용 메시지를 SMS보다 RCS로 보내는 것이 더 비용 효율적일 수 있습니다. 긴 SMS 메시지는 여러 개의 청구 가능한 세그먼트로 분할되는 반면, RCS 메시지는 메시지당 청구되기 때문입니다.

{% endsubtab %}
{% subtab 미디어 %}

RCS 미디어 메시지를 사용하면 이미지, 동영상, 문서 파일 등 SMS로는 불가능한 매력적인 미디어 형식을 사용할 수 있습니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

**기능:**

- 텍스트, 추천 답장, 추천 동작을 포함하여 텍스트 메시지 유형에서 사용 가능한 모든 기능을 지원합니다.
- [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)에서 업로드한 이미지 파일(JPEG, PNG).
- 메시지 작성기에서 URL로 추가한 동영상 파일(MP4, MPEG, MV4).
- 메시지 작성기에서 URL로 추가한 문서 파일(PDF).

![미디어 파일을 업로드하는 옵션이 있는 RCS 작성기.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

**파일 사양:**

| 파일 유형 | 사양 |
| --- | --- |
| 전체 | 파일 크기는 100MB로 제한됩니다. 파일 URL은 최대 2,048자까지 가능합니다. |
| 이미지 | 지원 형식: JPG, JPEG, GIF |
| 동영상 | 지원 형식: H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| 문서 | 지원 형식: PDF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Inbound MMS and personalization" }

**고려 사항:**

RCS 메시지 수신 시 사용자 경험은 통신사 커버리지, 모바일 기기 하드웨어 및 운영체제에 따라 달라질 수 있습니다. RCS는 Android 기기와 더 자연스럽게 통합되며, 기기에 따라 경험이 다른 속도와 품질로 렌더링될 수 있습니다.

{% endsubtab %}
{% endsubtabs %}

언어와 개인화([Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/), [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), 이모지)를 필요에 따라 사용하여 메시지를 작성합니다. 초과 요금이 발생할 가능성을 줄이기 위해 메시지 문구 제한을 준수하세요.

{% alert important %}
진행하기 전에 위의 [RCS 메시지 유형 가이드라인](#step-3-compose-your-message)을 읽어보세요. RCS 메시지는 [메시지당 요금이 부과]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/)되므로 각 유형에 포함할 수 있는 내용을 이해하는 것이 좋습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 팁 {#tips}

#### Liquid 사용 {#using-liquid}

{% raw %}
Liquid를 사용할 계획이라면 선택한 개인화에 기본값을 포함하여 사용자의 프로필이 불완전한 경우 이름 대신 빈 자리 표시자 `Hi, !`나 일관성 없는 문장을 받지 않도록 하세요.
{% endraw %}

#### AI 문구 생성 {#generating-ai-copy}

[AI 카피라이팅 어시스턴트]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/)를 사용해 보세요. 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있는 사람이 작성한 것 같은 마케팅 문구를 생성합니다.

![SMS 작성기의 메시지 필드에 있는 AI 카피라이터 시작 버튼.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### 오른쪽에서 왼쪽으로 쓰는 메시지 만들기 {#creating-right-to-left-messages}

오른쪽에서 왼쪽으로 쓰는 메시지의 최종 모양은 서비스 제공업체가 렌더링하는 방식에 크게 좌우됩니다. 가능한 한 정확하게 표시되는 오른쪽에서 왼쪽으로 쓰는 메시지를 작성하는 모범 사례는 [오른쪽에서 왼쪽으로 쓰는 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/)를 참조하세요.

#### 대화형 메시지 워크플로 만들기(RCS) {#create-conversational-message-workflows-rcs}

대화형 메시지 워크플로를 사용하면 사용자에게 동적으로 응답하여 양방향 메시징 경험을 만들 수 있습니다. 워크플로를 구축하려면 Canvas를 만든 다음 추천 답장과 [행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/)를 결합하여 사용자가 선택한 답장에 따라 워크플로를 안내합니다.

1. Canvas 빌더에서 여러 추천 답장이 포함된 RCS 메시지 단계를 만듭니다.

![추천 답장이 포함된 RCS 메시지 작성기.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. 해당 메시지를 각 추천 답장에 대한 동작 그룹이 있는 행동 경로에 연결합니다.
3. 각 동작 그룹에 대해:
   - 트리거로 **SMS 인바운드 메시지 보내기**를 선택합니다.
   - 메시지 본문을 해당 추천 답장과 동일하게 설정합니다.

![세 개의 동작 그룹으로 구성된 행동 경로 단계, 각 추천 답장에 하나씩.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. 각 동작 그룹을 RCS 메시지 단계에 연결한 다음 관련 추천 답장에 기반한 콘텐츠를 추가합니다.
5. 후속 메시지에 추천 답장을 추가하여 대화형 워크플로를 계속합니다.
6. 워크플로가 완료될 때까지 2~4단계를 반복합니다.

![두 개의 행동 경로가 있는 대화형 워크플로를 보여주는 Canvas.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

## 4단계: 메시지 미리보기 및 테스트 {#step-4-preview-and-test-your-message}

Braze는 항상 메시지를 보내기 전에 미리보기하고 테스트할 것을 권장합니다. **테스트** 탭으로 전환하여 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#content-test-groups) 또는 개별 사용자에게 테스트 SMS, MMS 또는 RCS 메시지를 보내거나, Braze에서 직접 사용자로서 메시지를 미리볼 수 있습니다.

{% alert tip %}
SMS가 몇 개의 세그먼트로 분할될 수 있는지 테스트하려면 [SMS 세그먼트 계산기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator)로 문구 길이를 테스트하세요.
{% endalert %}

![작성기의 테스트 탭에서 SMS 문구를 미리보는 모습. 프로필 섹션에서 이름 필드가 "James"로 설정되어 있습니다. 미리보기 섹션에서 SMS에 "Hi James, we appreciate your support!"라고 표시됩니다.]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert note %}
MMS의 경우 자산(이미지 및 메시지 본문)의 순서를 사용자 지정할 수 없습니다. 순서는 메시지를 수신하는 전화기에 따라 달라집니다.
{% endalert %}

{% alert note %}
RCS 렌더링은 사용자의 운영체제, 기기 제조사, 통신사 및 메시징 앱(예: Google Messages vs. Apple Messages)에 의해 제어되므로 메시지 모양이 달라질 수 있습니다. Braze에 표시되는 미리보기는 최종 사용자가 수신하는 것과 정확히 일치하지 않을 수 있습니다. 가능하면 실제 기기에서 최종 렌더링을 확인하세요. iOS 기기에서의 RCS 렌더링에 대한 자세한 내용은 [iOS 기기에서 RCS 메시지가 정확하게 렌더링되지 않는 이유는 무엇인가요?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs/#why-doesnt-my-rcs-message-render-accurately-on-ios-devices)를 참조하세요.
{% endalert %}

자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=sms%2Fmms%20and%20rcs)를 참조하세요.

## 5단계: 나머지 Campaign 또는 Canvas 구축 {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

다음으로 나머지 Campaign을 구축합니다. 메시지를 작성하기 위한 도구를 가장 잘 활용하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

#### 전달 스케줄 또는 트리거 선택 {#choose-delivery-schedule-or-trigger}

메시지는 스케줄된 시간, 동작 또는 API 트리거를 기반으로 전달할 수 있습니다. 자세한 내용은 [Campaign 스케줄링]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/)을 참조하세요.

실행 기반 전달의 경우 Campaign의 기간과 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/)도 설정할 수 있습니다.

이 단계에서는 사용자가 Campaign을 [다시 수신할 수 있도록]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns) 허용하거나 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping) 규칙을 활성화하는 등의 전달 제어를 지정할 수도 있습니다.

#### 타겟 사용자 선택 {#choose-users-to-target}

다음으로 Segments 또는 필터를 선택하여 오디언스를 좁혀 [사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/)합니다. 이미 구독 그룹을 선택했으므로 사용자가 원하는 커뮤니케이션 수준이나 카테고리에 따라 사용자가 좁혀집니다.

{% multi_lang_include target_audiences.md %}

Segments에서 더 큰 오디언스를 선택하고 선택적 필터로 해당 Segment를 더 좁힙니다. 대략적인 Segment 인구가 어떻게 보이는지 자동으로 미리보기가 제공됩니다. 정확한 Segment 멤버십은 항상 메시지가 발송되기 전에 계산된다는 점을 유의하세요.

{% alert tip %}
리타겟팅에 관심이 있으신가요? 자세한 내용은 [사용자 리타겟팅]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/)을 참조하세요.
{% endalert %}

#### 전환 이벤트 선택 {#choose-conversion-events}

Braze를 사용하면 Campaign을 수신한 후 사용자가 특정 동작인 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/)를 수행하는 빈도를 추적할 수 있습니다. 사용자가 지정된 동작을 수행하면 전환이 집계되는 최대 30일의 기간을 허용할 수 있습니다.

전환 이벤트는 Campaign의 성공을 측정하는 데 도움이 됩니다. 예를 들어:

- 지오타겟팅을 사용하여 사용자의 구매를 최종 목표로 하는 메시지를 트리거하는 경우 전환 이벤트를 `Purchase`로 설정합니다.
- 사용자를 앱으로 유도하려는 경우 전환 이벤트를 `Starts Session`으로 설정합니다.

특정 사용 사례에 따라 커스텀 전환 이벤트를 설정할 수도 있습니다.

{% endtab %}
{% tab Canvas %}

아직 완료하지 않았다면 Canvas 구성요소의 나머지 섹션을 완료합니다. Canvas의 나머지 부분을 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대한 자세한 내용은 Canvas 설명서의 [Canvas 구축]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.

{% endtab %}
{% endtabs %}

## 6단계: 검토 및 배포 {#step-6-review-and-deploy}

Campaign 또는 Canvas의 마지막 부분을 완성한 후 세부 정보를 검토하고 테스트한 다음 발송합니다!

다음으로 [SMS, MMS 및 RCS 보고]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting/)를 확인하여 Campaign의 결과에 액세스하는 방법을 알아보세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### RCS로 미리 녹음된 음성 메시지를 보낼 수 있나요? {#can-i-send-pre-recorded-voicemails-with-rcs}

네, 미디어 메시지를 사용하여 오디오 파일을 지원할 수 있습니다.