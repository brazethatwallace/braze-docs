---
nav_title: LINE 메시지 만들기
article_title: LINE 메시지 만들기
page_order: 1
description: "LINE 메시지를 만들고 채널별 메시지 유형, 필드, 클릭 추적, 전달 설정 및 동작을 구성합니다."
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - LINE
alias: /line/create/
---

# LINE 메시지 만들기 {#create-a-line-message}

> Campaign 또는 Canvas에서 개인화된 LINE 메시지를 만들 수 있습니다. 텍스트, 이미지, 리치, 카드 기반 메시지 중에서 선택하고, 한 번의 전송에 최대 5개의 메시지를 결합할 수 있습니다.

## 사전 요구 사항 {#prerequisites}

시작하기 전에 다음 사항을 확인하세요:

| 요구 사항 | 설명 |
| --- | --- |
| LINE 연결 | [LINE 설정]({{site.baseurl}}/user_guide/channels/line/line_setup)을 완료하고 채널의 정책, 제한 사항 및 콘텐츠 규칙을 검토하세요. |
| Campaign 또는 Canvas | 단일 타겟팅 메시지에는 Campaign을, 다단계 사용자 여정에는 Canvas를 사용하세요. |
| 메시지 계획 | 콘텐츠, 이미지, 링크 및 구독 그룹을 준비하세요. |
| 메시지 또는 액션 크레딧 | 계정에 사용 가능한 크레딧이 있는지 확인하세요. Braze에서 LINE 메시지를 전송하면 이 크레딧이 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE 메시지 사전 요구 사항" }

## 메시지 만들기 {#create-a-message}

### 1단계: 메시지를 작성할 위치 선택하기 {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. **메시징** > **Campaigns**로 이동하여 **Campaign 만들기**를 선택합니다.
2. **LINE**을 선택하거나, 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널 Campaign**을 선택합니다.
3. 캠페인에 명확하고 의미 있는 이름을 지정합니다.
4. 필요에 따라 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) 및 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가합니다.
   * 태그를 사용하면 리포트에서 캠페인을 더 쉽게 찾고 활용할 수 있습니다.
5. 캠페인의 배리언트를 추가하고 이름을 지정합니다. 각 배리언트에서 서로 다른 메시지 유형과 레이아웃을 사용할 수 있습니다. 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

{% alert tip %}
캠페인 배리언트의 콘텐츠가 유사한 경우, 배리언트를 추가하기 전에 먼저 첫 번째 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### 2단계: 구독 그룹 선택하기 {#step-2-select-a-subscription-group}

메시지를 전송하는 LINE 채널과 연결된 **구독 그룹**을 선택합니다. 에디터를 실행하기 전에 구독 그룹이 필수로 지정되어야 합니다.

LINE 캠페인의 모든 배리언트는 동일한 구독 그룹을 사용해야 합니다. LINE 구독 상태에 대한 자세한 내용은 [LINE 구독 그룹]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups)을 참조하세요.

### 3단계: LINE 메시지 작성하기 {#step-3-compose-your-line-message}

**에디터 실행**을 선택한 다음 메시지 유형을 에디터로 드래그합니다. 하나의 전송에 최대 5개의 메시지를 조합할 수 있으며, 사용자가 수신하는 순서대로 정렬할 수 있습니다.

![미리보기에 메시지가 표시된 LINE 작성기.]({% image_buster /assets/img/line/line_composer.png %})

#### 메시지 유형 {#message-types}

| 메시지 유형 | 필드 및 설정 | 제한 및 동작 |
| --- | --- | --- |
| **텍스트** | 이모지, Liquid, URL이 포함된 메시지 본문 | 최대 5,000자. |
| **이미지** | 미디어 라이브러리 또는 URL(동적 URL 포함)의 이미지 | 이미지 URL은 최대 2,000자를 포함할 수 있습니다. 독립형 이미지 메시지는 클릭 동작을 지원하지 않습니다. |
| **리치 메시지** | 이미지, 대체 텍스트, 템플릿, URI 동작이 포함된 탭 가능 영역 | 대체 텍스트는 최대 400자를 포함할 수 있습니다. 1~50개의 탭 가능 영역을 추가할 수 있습니다. 동작 레이블은 최대 100자, 각 URI는 최대 1,000자를 포함할 수 있습니다. |
| **카드 기반 메시지** | 선택적 이미지와 헤더, 필수 본문, URI 동작이 포함된 최대 10개의 카드 | 대체 텍스트는 최대 400자를 포함할 수 있습니다. 헤더는 최대 40자를 포함할 수 있습니다. 본문은 이미지 또는 헤더가 있는 경우 최대 60자, 둘 다 없는 경우 최대 120자를 포함할 수 있습니다. 각 카드에는 최대 20자의 레이블이 포함된 1~3개의 동작이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="LINE 메시지 유형, 필드 및 제한" }

글자 수 제한에는 Liquid 구문이 포함되지 않습니다.

이미지 사양, 리치 메시지 템플릿, 캐러셀 이미지 설정 및 예시에 대한 자세한 내용은 [LINE 메시지 유형]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/message_types)을 참조하세요.

{% alert note %}
카드 기반 메시지는 모든 카드에 동일한 선택적 필드와 동작 수를 적용합니다. 예를 들어, 하나의 카드에 이미지와 두 개의 동작이 포함되어 있으면 모든 카드에 이미지와 두 개의 동작이 포함되어야 합니다.
{% endalert %}

#### 클릭 시 동작 {#on-click-behavior}

리치 메시지와 카드의 탭 가능 영역에서 **클릭 시 동작**으로 **URI**를 선택한 다음 **URL 열기**에 도착지를 입력합니다. URL을 LINE 내에서 열지 여부를 선택합니다.

#### 개인화 {#personalization}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 사용하여 텍스트, 이미지, URL을 개인화할 수 있습니다. 불완전한 데이터가 있는 프로필이 빈 콘텐츠를 받지 않도록 Liquid 개인화에 기본값을 포함하세요.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

오른쪽에서 왼쪽으로 쓰는 언어의 경우 [오른쪽에서 왼쪽 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)를 참조하세요.

### 4단계: 클릭 추적 구성하기 {#step-4-configure-click-tracking}

**설정** 탭에서 **클릭 추적**을 사용하여 전송 시 링크를 단축하고 추적할 수 있습니다. 클릭 추적은 새 메시지에 대해 기본적으로 활성화되어 있으며, 텍스트, 리치, 카드 기반 메시지의 HTTP 및 HTTPS URL에 적용됩니다.

Braze는 `https://brz.ai` 또는 구독 그룹에 구성된 커스텀 도메인을 사용합니다. Liquid를 사용하여 추적 URL을 개인화할 수 있습니다. 메시지 유형별 설정, 테스트 동작, 커스텀 도메인 및 리타겟팅에 대한 자세한 내용은 [LINE 클릭 추적]({{site.baseurl}}/user_guide/channels/line/create_a_line_message/line_click_tracking)을 참조하세요.

### 5단계: 메시지 미리보기 및 테스트하기 {#step-5-preview-and-test-your-message}

**미리보기 및 테스트** 탭으로 이동하여 사용자로서 메시지를 미리보거나 콘텐츠 테스트 그룹 또는 개별 사용자에게 테스트 LINE 메시지를 보낼 수 있습니다.

![테스트 메시지의 미리보기가 표시된 미리보기 및 테스트 탭.]({% image_buster /assets/img/line/test_preview.png %})

테스트 요구 사항 및 단계에 대한 자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line)를 참조하세요.

### 6단계: 나머지 캠페인 또는 Canvas 구성하기 {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### 전달 스케줄 또는 트리거 선택하기 {#choose-a-delivery-schedule-or-trigger}

LINE 메시지를 예약된 시간에 전달하거나 실행 또는 API 트리거에 대한 응답으로 전달합니다. 스케줄 및 트리거 옵션에 대한 자세한 내용은 [캠페인 예약하기]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)를 참조하세요.

[재자격 부여]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) 및 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)과 같은 전달 제어를 구성합니다. 실행 기반 전달의 경우 캠페인 기간과 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)을 설정합니다.

#### 타겟 사용자 선택하기 {#choose-users-to-target}

Segments 및 필터를 선택하여 [사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)합니다. Braze는 메시지를 전송하기 전에 정확한 Segment 멤버십을 계산합니다.

LINE은 각 사용자의 구독 상태를 관리합니다. 사용자가 메시지를 수신하려면 `native_line_id`가 있어야 하며, 선택한 구독 그룹과 연결된 LINE 채널을 팔로우해야 합니다. 자세한 내용은 [LINE 구독 상태]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#line)를 참조하세요.

#### 전환 이벤트 선택하기 {#choose-conversion-events}

[전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 사용하여 사용자가 캠페인을 수신한 후의 행동을 측정합니다. 최대 30일의 전환 기간을 설정합니다.

{% endtab %}
{% tab Canvas %}

Canvas의 나머지 섹션을 완성합니다. 진입 스케줄, 오디언스 설정 및 전송 제어에 대한 자세한 내용은 [Canvas 만들기]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)를 참조하세요.

인바운드 LINE 메시지를 사용하여 트리거 단어를 기반으로 Canvas를 시작하거나 분기할 수 있습니다. 동작 및 대소문자 요구 사항에 대한 자세한 내용은 [LINE 사용자에게 메시지 보내기]({{site.baseurl}}/user_guide/channels/line/message_users)를 참조하세요.

{% endtab %}
{% endtabs %}

### 7단계: 검토 및 배포하기 {#step-7-review-and-deploy}

캠페인 또는 Canvas 구성을 완료한 후 세부 정보를 검토하고 전송하기 전에 메시지를 테스트합니다.

출시 후 [LINE 리포팅]({{site.baseurl}}/user_guide/channels/line/reporting)을 사용하여 메시지 성능을 확인합니다.

## 알아두어야 할 사항 {#things-to-know}

- LINE 메시지는 1개에서 5개 사이의 메시지 말풍선을 포함할 수 있습니다.
- 구독 그룹은 하나의 LINE 채널에 매핑되며, Campaign의 모든 배리언트는 동일한 구독 그룹을 사용해야 합니다.
- LINE은 구독 상태에 대한 단일 진실 공급원입니다. 선택한 LINE 채널을 팔로우하지 않는 사용자는 메시지를 수신하지 않습니다.
- LINE은 특정 날짜에 20명 이상의 사용자가 해당 이벤트를 수행한 경우에만 열람 및 클릭 관련 통계를 계산합니다.