---
nav_title: LINE 메시지 만들기
article_title: LINE 메시지 만들기
page_order: 1
description: "이 문서에서는 LINE 메시지 Campaign 또는 Canvas를 만드는 방법을 다룹니다."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# LINE 메시지 만들기 {#create-a-line-message}

> LINE Campaign을 사용하면 고객에게 직접 도달하고 프로그래밍 방식으로 대화할 수 있습니다. Liquid 및 기타 동적 콘텐츠를 사용하여 사용자와 개인화된 경험을 만들고, 브랜드와의 자연스러운 사용자 경험을 촉진하고 향상시키는 환경을 조성할 수 있습니다.

## 필수 조건 {#prerequisites}

LINE 메시지를 만들기 전에 다음을 수행하세요:

1. LINE 개요를 읽으세요.
2. 정책, 제한 사항 및 콘텐츠 규칙을 확인하세요.
3. [LINE 연결을 설정하세요]({{site.baseurl}}/user_guide/channels/line/line_setup).

Braze에서 LINE 메시지를 발송하면 계정의 메시지 또는 액션 크레딧이 차감됩니다.

## 1단계: 메시지를 작성할 위치 선택 {#step-1-choose-where-to-build-your-message}

메시지를 Campaign으로 보낼지 Canvas로 보낼지 확실하지 않으신가요? Campaign은 단일 타겟 메시징에 적합하고, Canvas는 다단계 사용자 여정에 더 적합합니다.

{% tabs %}
{% tab Campaign %}

**단계:**

1. **메시징** > **Campaigns**로 이동하여 **캠페인 생성**을 선택합니다.
2. **LINE**을 선택하거나, 여러 채널을 타겟팅하는 Campaign의 경우 **멀티채널 Campaign**을 선택합니다.
3. Campaign에 명확하고 의미 있는 이름을 지정합니다.
4. 필요에 따라 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) 및 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가합니다.
   * 태그를 사용하면 Campaign을 더 쉽게 찾고 보고서를 작성할 수 있습니다.
5. Campaign에 필요한 만큼 배리언트를 추가하고 이름을 지정합니다. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

{% alert tip %}
Campaign의 모든 메시지가 유사하거나 동일한 콘텐츠를 가질 경우, 추가 배리언트를 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**단계:**

1. Canvas 작성기를 사용하여 [Canvas를 만듭니다]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).
2. Canvas를 설정한 후 Canvas 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 지정합니다.
3. [단계 스케줄]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#schedule-delay)을 선택하고 필요에 따라 delay를 지정합니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. Segments를 지정하고 추가 필터를 추가하여 이 단계의 수신자를 더 세밀하게 조정할 수 있습니다. 오디언스 옵션은 메시지가 발송되는 시점에 지연 후 확인됩니다.
5. [진행 동작]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)을 선택합니다.
6. 메시지와 함께 사용할 다른 메시징 채널을 선택합니다.

{% endtab %}
{% endtabs %}

## 2단계: LINE 메시지 작성 {#step-2-compose-your-line-message}

필요에 따라 개인화(Liquid 또는 연결된 콘텐츠 등)를 사용하여 메시지를 작성합니다. LINE은 각 메시지에 최대 5개의 메시지 버블을 허용하며, 텍스트, 이미지, 리치 또는 카드 기반 등 사용 가능한 메시지 레이아웃 중 하나를 사용할 수 있습니다.

![미리보기에 메시지가 표시된 LINE 작성기.]({% image_buster /assets/img/line/line_composer.png %})

### 팁 {#tips}

#### Liquid 사용 {#using-liquid}

Liquid를 사용할 계획이라면 개인화에 기본값을 포함해야 합니다. 이렇게 하면 불완전한 사용자 프로필을 가진 수신자가 빈 입력 안내를 받는 것을 방지할 수 있습니다. 예를 들어, 사용자가 "안녕하세요, !"라는 메시지를 받는 대신 "안녕하세요, 새 가입자님!"이라는 메시지를 받을 수 있습니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### 오른쪽에서 왼쪽으로 쓰는 메시지 만들기 {#creating-right-to-left-messages}

오른쪽에서 왼쪽으로 쓰는 메시지의 최종 모양은 서비스 제공업체가 렌더링하는 방식에 크게 좌우됩니다. 가능한 한 정확하게 표시되는 오른쪽에서 왼쪽으로 쓰는 메시지를 작성하는 모범 사례는 [오른쪽에서 왼쪽으로 쓰는 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)를 참조하세요.

## 3단계: 메시지 미리보기 및 테스트 {#step-3-preview-and-test-your-message}

**테스트** 탭으로 전환하여 콘텐츠 테스트 그룹 또는 개별 사용자에게 테스트 LINE 메시지를 보내거나, Braze에서 직접 사용자로서 메시지를 미리 볼 수 있습니다.

![테스트 메시지 미리보기가 표시된 "테스트" 탭.]({% image_buster /assets/img/line/test_preview.png %})

자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line)를 참조하세요.

## 4단계: Campaign 또는 Canvas의 나머지 부분 구축 {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Campaign의 나머지 부분을 구축합니다. LINE 메시지를 작성하기 위한 도구를 가장 잘 활용하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

### 전달 스케줄 또는 트리거 선택 {#choose-delivery-schedule-or-trigger}

LINE 메시지는 스케줄된 시간, 동작 또는 API 트리거를 기반으로 전달할 수 있습니다. 스케줄 및 트리거 옵션에 대한 자세한 내용은 [Campaign 스케줄 설정]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)을 참조하세요.

사용자가 Campaign을 다시 받을 수 있도록 [재적격성]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#campaigns)을 허용하거나 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#frequency-capping) 규칙을 활성화하는 등 전달 제어를 지정할 수 있습니다. 실행 기반 전달의 경우 Campaign의 기간과 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)도 설정할 수 있습니다.

### 타겟 사용자 선택 {#choose-users-to-target}

Segments 또는 필터를 선택하여 오디언스를 좁혀 [사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)합니다. 이미 구독 그룹을 선택했어야 하며, 이는 사용자가 원하는 커뮤니케이션 수준이나 카테고리에 따라 사용자를 좁힙니다.

Segments에서 더 넓은 오디언스를 선택하고, 선택적으로 [필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 사용하여 해당 Segment를 더 좁힐 수 있습니다. 대략적인 Segment 인구의 스냅샷이 자동으로 표시됩니다. 정확한 Segment 멤버십은 항상 메시지가 발송되기 전에 계산된다는 점을 유의하세요.

### 전환 이벤트 선택 {#choose-conversion-events}

Braze를 사용하면 Campaign을 수신한 후 사용자가 특정 행동인 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 행동을 취하면 전환으로 집계되는 최대 30일의 기간을 허용하는 옵션이 있습니다.

전환 이벤트는 Campaign의 성공을 측정하는 데 도움이 됩니다. 예를 들어:

- 지오타겟팅을 사용하여 사용자의 구매를 최종 목표로 하는 LINE 메시지를 트리거하는 경우, 전환 이벤트를 `Purchase`로 설정합니다.
- 사용자를 앱으로 유도하려는 경우, 전환 이벤트를 `Starts Session`으로 설정합니다.

특정 사용 사례에 따라 커스텀 전환 이벤트를 설정할 수도 있습니다. 창의적으로 생각하고 이 Campaign의 성공을 어떻게 측정할지 고민해 보세요.

{% endtab %}
{% tab Canvas %}

아직 완료하지 않았다면 Canvas의 나머지 섹션을 완료하세요. Canvas의 나머지 부분을 구축하고, 다변량 테스트 및 지능형 선택을 사용하는 방법 등에 대한 자세한 내용은 [Canvas 만들기]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)를 참조하세요.

{% endtab %}
{% endtabs %}

## 5단계: 검토 및 배포 {#step-5-review-and-deploy}

Campaign 또는 Canvas의 마지막 부분을 완성한 후 세부 사항을 검토하고 테스트한 다음 발송하세요!

다음으로, [LINE 보고]({{site.baseurl}}/line/reporting)를 확인하여 LINE Campaign의 결과에 액세스하는 방법을 알아보세요.