---
nav_title: 메시지 만들기
article_title: SMS, MMS 또는 RCS 메시지 만들기
page_order: 1
description: "SMS, MMS 또는 RCS 메시지를 만들고 채널별 메시지 유형, 필드, 링크 단축, 전달 설정 및 동작을 구성합니다."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
  - Canvas
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# SMS, MMS 또는 RCS 메시지 만들기 {#create-an-sms-mms-or-rcs-message}

> Campaigns 또는 Canvas에서 개인화된 SMS, MMS, 리치 커뮤니케이션 서비스(RCS) 메시지를 만들 수 있습니다. 선택한 구독 그룹에 따라 사용할 수 있는 메시지 유형과 발신자가 결정됩니다.

## 사전 준비 사항 {#prerequisites}

시작하기 전에 다음 사항을 확인하세요:

| 요구 사항 | 설명 |
| --- | --- |
| 발신자 설정 | [발신자 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)을 완료하세요. MMS를 보내려면 구독 그룹에 MMS가 활성화된 전화번호가 필요합니다. RCS를 보내려면 [RCS 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)을 완료하고 인증된 RCS 발신자를 추가하세요. |
| 구독 그룹 | 이 메시지의 발신자를 포함하는 [구독 그룹]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups)을 생성하세요. |
| 사용자 전화번호 및 동의 | 사용자의 전화번호를 가져오고 적절한 [SMS, MMS 및 RCS 옵트인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)을 수집하세요. |
| Campaign 또는 Canvas | 단일 타겟 메시지에는 Campaign을 사용하고, 다단계 사용자 여정에는 Canvas를 사용하세요. |
| 메시지 또는 액션 크레딧 | 계정에 사용 가능한 크레딧이 있는지 확인하세요. Braze에서 SMS, MMS, RCS 메시지를 발송하면 이 크레딧이 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS, MMS 및 RCS 메시지 사전 준비 사항" }

## 메시지 만들기 {#create-a-message}

### 1단계: 메시지를 작성할 위치 선택 {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. **메시징** > **Campaigns**로 이동하여 **Campaign 만들기**를 선택합니다.
2. **SMS/MMS/RCS**를 선택하거나, 여러 채널을 타겟팅하는 Campaign의 경우 **멀티채널 Campaign**을 선택합니다.
3. Campaign 이름을 명확하고 의미 있게 지정합니다.
4. 필요에 따라 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams)와 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가합니다.
  - 태그를 사용하면 Campaign을 더 쉽게 찾고 보고서에서 활용할 수 있습니다.
5. Campaign의 배리언트를 추가하고 이름을 지정합니다. 동일한 Campaign에 SMS/MMS 및 RCS 배리언트를 포함할 수 있습니다. 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

{% alert tip %}
Campaign 배리언트의 콘텐츠가 유사한 경우, 먼저 첫 번째 메시지를 작성한 후 배리언트를 추가하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### 2단계: 구독 그룹 및 메시지 유형 선택 {#step-2-select-a-subscription-group-and-message-type}

이 메시지의 발신자를 포함하는 **구독 그룹**을 선택합니다. Braze는 선택한 그룹을 사용하여 도달 가능한 오디언스를 계산하고 발송 시간 적격성을 결정합니다.

선택한 구독 그룹에 따라 작성기에서 사용할 수 있는 메시지 유형이 결정됩니다:

| 구독 그룹 유형 | 사용 가능한 메시지 유형 |
| --- | --- |
| SMS 전용 | SMS |
| MMS 지원 번호가 포함된 SMS | SMS 및 MMS |
| 인증된 RCS 발신자가 있는 RCS 지원 | RCS 및 그룹에 SMS 발신자가 포함된 경우 SMS. 해당 발신자가 MMS를 지원하는 경우 MMS도 사용 가능합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="구독 그룹별 사용 가능한 메시지 유형" }

{% alert tip %}
RCS 전달이 실패할 때 SMS 대체 메시지를 보낼 수 있도록 RCS 구독 그룹에 SMS 발신자를 하나 이상 추가하세요.
{% endalert %}

구독 그룹이 두 프로토콜을 모두 지원하는 경우 **SMS/MMS** 또는 **RCS**를 선택합니다. RCS의 경우 **텍스트**, **미디어** 또는 **카드**를 선택합니다.

### 3단계: 메시지 작성 {#step-3-compose-your-message}

작성기의 필드와 제한은 선택한 메시지 유형에 따라 다릅니다.

{% tabs local %}
{% tab SMS 및 MMS %}

#### SMS 및 MMS 필드와 설정 {#sms-and-mms-fields-and-settings}

| 필드 또는 설정 | 설명 |
| --- | --- |
| **언어** | 메시지에 언어별 콘텐츠를 삽입합니다. |
| **메시지** | Liquid, 연결된 콘텐츠, 이모지를 포함하여 최대 1,600자까지 입력할 수 있습니다. 작성기는 인코딩, 문자 수 및 과금 대상 SMS 메시지 세그먼트 수를 추정합니다. MMS 메시지에는 메시지 본문 없이 미디어만 포함할 수 있습니다. |
| **미디어** | MMS 지원 구독 그룹의 경우 미디어 라이브러리 또는 URL에서 PNG, JPEG 또는 GIF 이미지를 하나 추가합니다. 이미지 대신 vCard를 추가할 수도 있습니다. |
| **링크 단축** | HTTP 및 HTTPS URL을 단축하고 인게이지먼트를 추적합니다. 레거시 링크 단축의 경우 기본 또는 고급 추적을 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS 및 MMS 필드와 설정" }

SMS 메시지는 GSM-7 또는 UCS-2 인코딩을 사용하며 메시지 세그먼트당 과금됩니다. 단일 문자가 인코딩을 변경하여 과금 대상 세그먼트 수를 늘릴 수 있습니다. 인코딩 규칙, 세그먼트 크기 및 세그먼트 계산기에 대한 자세한 내용은 [SMS 및 RCS 과금 계산기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)를 참조하세요.

![메시지 카피와 예상 문자 수 및 세그먼트 수를 보여주는 SMS 작성기.]({% image_buster /assets/img/sms_campaign_compose.png %})

#### MMS 미디어 사양 {#mms-media-specifications}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

사용자가 기기 연락처에 저장할 수 있는 비즈니스 정보를 보내려면 [연락처 카드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card)를 참조하세요. 연락처 카드 발송은 MMS로 과금됩니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

MMS의 사용 가능 여부와 렌더링은 수신 통신사에 따라 다릅니다. 통신사가 MMS를 수신할 수 없는 경우 미디어는 제공업체를 통해 SMS 본문의 링크로 변환됩니다. Google Voice 번호로 MMS를 보내는 것은 피하세요. 제한된 MMS 지원으로 인해 안정적인 전달이 어려울 수 있습니다.

사용자가 인바운드 미디어를 보내면 Braze는 [Currents SMS 인바운드 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)에서 해당 URL을 노출하고, Liquid에서 {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %}를 통해 접근할 수 있습니다.

{% endtab %}
{% tab RCS %}

#### RCS 메시지 유형 {#rcs-message-types}

| 메시지 유형 | 필드 및 설정 | 제한 및 동작 |
| --- | --- | --- |
| **텍스트** | 필수 메시지 본문, 선택 사항인 추천 답장 또는 URL 열기 액션, 선택 사항인 SMS 대체, 링크 단축 | 메시지 본문은 SMS 서비스 제공업체에 따라 최대 1,600자 또는 3,072자를 포함할 수 있습니다. 최대 5개의 추천을 추가할 수 있습니다. |
| **미디어** | 필수 이미지, 비디오, 문서 또는 오디오; 선택 사항인 메시지 본문; 선택 사항인 추천, SMS 대체, 링크 단축 | 메시지 본문은 제공업체에 따라 최대 1,600자 또는 3,072자를 포함할 수 있으며 추가 RCS 메시지로 과금됩니다. 최대 5개의 추천을 추가할 수 있습니다. |
| **카드** | 미디어 카드 또는 텍스트 전용 카드, 제목, 설명, 버튼, 선택 사항인 추천 및 SMS 대체 | 제목은 최대 200자를 포함할 수 있습니다. 설명은 제공업체에 따라 최대 1,600자 또는 2,000자를 포함할 수 있습니다. 1~4개의 버튼을 추가할 수 있습니다. 텍스트 전용 카드 및 카드 외부의 추천 지원 여부는 제공업체에 따라 다릅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RCS 메시지 유형, 필드 및 제한" }

추천은 사용자의 텍스트 입력을 미리 채우는 추천 답장이거나 URL 열기 액션일 수 있습니다. 각 추천에 최대 25자의 텍스트를, 각 URL 열기 액션에 최대 2,048자의 URL을 추가할 수 있습니다.

모든 RCS 메시지 유형에서 **RCS 실패 시 SMS 전송**을 켜면 최대 1,600자의 대체 메시지를 추가할 수 있습니다. 선택한 구독 그룹에는 SMS 발신자가 포함되어 있어야 합니다. **카드** 메시지의 경우 설명에 포함된 링크는 클릭할 수 없으므로 URL 열기 버튼을 대신 사용하세요.

일부 SMS 서비스 제공업체는 독립형 **미디어** 메시지나 텍스트 전용 카드를 지원하지 않습니다. 작성기에는 지원되는 RCS 메시지 유형만 표시됩니다. **카드** 메시지의 경우 링크 단축은 SMS 대체의 링크에만 적용됩니다.

RCS 메시지 과금은 메시지 유형 및 콘텐츠에 따라 다릅니다. 기본, 리치 및 리치 카드 과금 규칙에 대한 자세한 내용은 [RCS 메시지 과금]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing)을 참조하세요.

#### RCS 미디어 사양 {#rcs-media-specifications}

작성기는 최대 1,000자의 미디어 URL을 허용합니다. 사용 가능한 형식과 최대 파일 크기는 SMS 서비스 제공업체에 따라 다릅니다.

| 파일 유형 | 사양 |
| --- | --- |
| 전체 | 최대 파일 크기는 제공업체에 따라 16&nbsp;MB 또는 100&nbsp;MB입니다. |
| 이미지 | JPEG, JPG, GIF, PNG |
| 비디오 | H263, M4V, MP4, MPEG, MPEG-4, WEBM |
| 문서 | PDF. **미디어** 메시지에서 사용 가능하지만 미디어 카드에서는 사용할 수 없습니다. |
| 오디오 | AAC, MP3, MPEG, MP4, 3GPP, OGG. 제공업체 지원은 다를 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RCS 미디어 사양" }

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% endtabs %}

#### 개인화 {#personalization}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), 이모지, 언어별 콘텐츠를 사용하여 메시지를 개인화하세요. 데이터가 불완전한 프로필이 빈 콘텐츠를 수신하지 않도록 Liquid 개인화에 기본값을 포함하세요.

프롬프트에서 메시지 카피를 생성하려면 Operator의 [카피 생성]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)을 사용하세요.

오른쪽에서 왼쪽으로 쓰는 언어에 대한 자세한 내용은 [오른쪽에서 왼쪽으로 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)를 참조하세요.

#### 대화형 메시지 워크플로 만들기 (RCS) {#create-conversational-message-workflows-rcs}

대화형 메시지 워크플로를 사용하면 사용자에게 동적으로 응답하여 양방향 메시징 경험을 만들 수 있습니다. 워크플로를 구축하려면 Canvas를 만든 다음 추천 답장과 [작업 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)를 결합하여 사용자가 선택한 답장에 따라 워크플로를 분기시키세요.

1. Canvas 빌더에서 여러 추천 답장이 포함된 RCS 메시지 단계를 만듭니다.

![추천 답장이 포함된 RCS 메시지 작성기.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. 해당 메시지를 각 추천 답장에 대한 액션 그룹이 있는 작업 경로에 연결합니다.
3. 각 액션 그룹에 대해:
   - 트리거로 **인바운드 SMS 메시지 전송**을 선택합니다.
   - 메시지 본문을 해당 추천 답장과 동일하게 설정합니다.

![세 개의 추천 답장에 대해 각각 하나의 액션 그룹으로 구성된 작업 경로 단계.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. 각 액션 그룹을 RCS 메시지 단계에 연결한 다음 관련 추천 답장에 기반한 콘텐츠를 추가합니다.
5. 후속 메시지에 추천 답장을 추가하여 대화형 워크플로를 계속 이어갑니다.
6. 워크플로가 완료될 때까지 2~4단계를 반복합니다.

![두 개의 작업 경로가 포함된 대화형 워크플로를 보여주는 Canvas.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

### 4단계: 링크 단축 설정 {#step-4-configure-link-shortening}

**링크 단축**을 켜서 HTTP 및 HTTPS URL을 단축하고 SMS, MMS 및 지원되는 RCS 링크의 클릭을 추적합니다. 워크스페이스에서 사용 가능한 버전에 따라 기본 또는 고급 추적을 선택하거나 통합 링크 단축을 사용하세요.

고급 추적은 세분화 및 리타겟팅을 위한 사용자 수준 클릭 데이터를 추가합니다. 통합 링크 단축은 SMS와 RCS 단축 링크를 하나의 개인화된 형식으로 결합합니다. 지원되는 URL, Liquid 동작, 테스트 요구 사항, 커스텀 도메인 및 리타겟팅에 대한 자세한 내용은 [링크 단축]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)을 참조하세요.

Braze는 메시지에서 최대 25개의 링크를 단축합니다. 4,000자를 초과하는 URL은 단축할 수 없으며 발송 시 메시지 실패를 유발합니다.

### 5단계: 메시지 미리보기 및 테스트 {#step-5-preview-and-test-your-message}

**테스트** 탭으로 이동하여 사용자로서 메시지를 미리 보거나 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) 또는 개별 사용자에게 테스트 SMS, MMS 또는 RCS 메시지를 보냅니다.

{% alert tip %}
[SMS 세그먼트 계산기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)를 사용하여 메시지에 포함된 세그먼트 수를 추정하세요.
{% endalert %}

![작성기의 테스트 탭에서 SMS 카피 미리보기. 프로필 섹션에서 이름 필드가 'James'로 설정되어 있습니다. 미리보기 섹션에서 SMS에 'Hi James, we appreciate your support!'라고 표시됩니다.]({% image_buster /assets/img/sms_campaign_test.png %})

MMS의 경우 미디어가 메시지 본문 앞에 표시될지 뒤에 표시될지는 수신 기기에 따라 결정됩니다.

{% alert note %}
RCS 렌더링은 사용자의 운영 체제, 기기 제조사, 통신사 및 메시징 앱(예: Google Messages와 Apple Messages)에 의해 제어되므로 메시지 외관이 달라질 수 있습니다. Braze에 표시되는 미리보기는 최종사용자가 수신하는 것과 정확히 일치하지 않을 수 있습니다. 가능한 한 실제 기기에서 최종 렌더링을 확인하세요. iOS 기기에서 RCS 렌더링에 대한 자세한 내용은 [iOS 기기에서 RCS 메시지가 정확하게 렌더링되지 않는 이유는 무엇인가요?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices)를 참조하세요. 리치 카드의 GIF에 대한 자세한 내용은 [iOS에서 RCS 리치 카드의 GIF가 정지 상태로 표시되는 이유는 무엇인가요?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios)를 참조하세요.
{% endalert %}

자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs)를 참조하세요.

### 6단계: Campaign 또는 Canvas의 나머지 구성 {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### 전달 스케줄 또는 트리거 선택 {#choose-a-delivery-schedule-or-trigger}

예약된 시간, 액션 또는 API 트리거에 대한 응답으로 메시지를 전달합니다. 스케줄 및 트리거 옵션에 대한 자세한 내용은 [Campaign 스케줄 설정]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)을 참조하세요.

[재적격성]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) 및 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)과 같은 전달 제어를 구성합니다. 실행 기반 전달의 경우 Campaign 기간 및 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)을 설정합니다.

#### 타겟 사용자 선택 {#choose-users-to-target}

Segments와 필터를 선택하여 [사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)합니다. Braze는 메시지를 보내기 전에 정확한 Segment 멤버십을 계산합니다.

선택한 구독 그룹은 구독 중인 사용자를 필터링합니다. SMS 및 MMS 수신자는 유효한 전화번호도 필요합니다. RCS 수신자는 RCS 지원 기기와 통신사 연결이 필요합니다. RCS 전달이 실패할 때 적격한 사용자에게 도달하려면 SMS 대체를 사용하세요.

{% multi_lang_include audience/target_audiences.md %}

클릭 및 상호작용 타겟팅에 대한 자세한 내용은 [사용자 리타겟팅]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting)을 참조하세요.

#### 전환 이벤트 선택 {#choose-conversion-events}

사용자가 Campaign을 수신한 후의 행동을 측정하려면 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 사용합니다. 최대 30일의 전환 기간을 설정하세요.

{% endtab %}
{% tab Canvas %}

Canvas의 나머지 섹션을 완료합니다. 항목 스케줄, 오디언스 설정 및 발송 제어에 대한 자세한 내용은 [Canvas 만들기]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)를 참조하세요.

{% endtab %}
{% endtabs %}

### 7단계: 검토 및 배포 {#step-7-review-and-deploy}

Campaign 또는 Canvas 구축을 마친 후 세부 정보를 검토하고 발송 전에 메시지를 테스트하세요.

출시 후 [SMS, MMS 및 RCS 보고서]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)를 사용하여 메시지 성능을 확인하세요.

## 알아두어야 할 사항 {#things-to-know}

- SMS는 메시지 세그먼트당, MMS는 자체 요금으로, RCS는 메시지 유형별로 요금이 부과됩니다. 발송 전에 [SMS 및 RCS 요금 계산기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)를 확인하세요.
- MMS는 하나의 이미지 또는 vCard를 지원합니다. 수신자가 미디어를 받을지 이미지 링크를 받을지는 통신사 지원 여부에 따라 결정됩니다.
- RCS 기능 및 제한 사항은 SMS 서비스 공급자에 따라 다릅니다. 메시지 작성기에는 선택한 구독 그룹에서 사용 가능한 옵션만 표시됩니다.
- RCS **미디어** 메시지에서 사전 녹음된 음성 메일을 오디오로 발송할 수 있습니다.
- 렌더링 및 인터랙션 동작은 기기, 통신사, 운영 체제, 메시징 앱에 따라 다릅니다.