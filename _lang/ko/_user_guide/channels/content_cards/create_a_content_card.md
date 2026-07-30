---
nav_title: 콘텐츠 카드 만들기
article_title: 콘텐츠 카드 만들기
page_order: 1
description: "이 참조 문서에서는 Braze Campaign 및 Canvases를 사용하여 콘텐츠 카드를 생성, 작성, 구성 및 전송하는 방법을 다룹니다."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# 콘텐츠 카드 만들기 {#create-a-content-card}

> 이 문서에서는 Campaign 및 Canvases를 구축할 때 Braze에서 콘텐츠 카드를 만드는 방법을 다룹니다. 여기서는 메시지 유형 선택, 카드 작성, 메시지 전달 스케줄 설정 과정을 안내합니다.

## 1단계: 메시지를 작성할 위치 선택 {#step-1-choose-where-to-build-your-message}

단일하고 간단한 메시징(예: 하나의 메시지로 사용자에게 제품을 알리는 경우)에는 Campaign을 사용합니다. 다단계 사용자 여정(예: 시간 경과에 따른 사용자 행동을 기반으로 맞춤형 제품 추천을 보내는 경우)에는 Canvas를 사용합니다.

{% tabs %}
{% tab Campaign %}

1. **메시징** > **Campaigns**로 이동하여 **Campaign 만들기**를 선택합니다.
2. **Content Cards**를 선택하거나, 여러 채널을 타겟팅하는 Campaign의 경우 **멀티채널**을 선택합니다.
3. Campaign에 명확하고 의미 있는 이름을 지정합니다.
4. 필요에 따라 [팀]({{site.baseurl}}/user_guide/administer/global/user_management/teams) 및 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가합니다.
   * 태그를 사용하면 Campaign을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder)를 사용할 때 관련 태그로 필터링할 수 있습니다.
5. Campaign에 원하는 만큼 배리언트를 추가하고 이름을 지정합니다. 추가된 각 배리언트에 대해 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 배리언트에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

{% alert tip %}
Campaign의 모든 메시지가 유사하거나 동일한 콘텐츠를 포함하는 경우, 추가 배리언트를 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. Canvas 작성기를 사용하여 [Canvas를 만듭니다]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).
2. Canvas를 설정한 후 Canvas 빌더에서 메시지 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 지정합니다.
3. 메시징 채널로 **Content Cards**를 선택합니다.
4. Braze가 콘텐츠 카드에 대한 오디언스 자격 및 개인화를 계산하는 시기를 선택합니다. 이는 단계 진입 시 또는 첫 번째 노출 시(권장)로 설정할 수 있습니다. Content Cards를 포함하는 단계는 예약 또는 실행 기반으로 설정할 수 있습니다.
5. 사용자가 구매를 완료하거나 커스텀 이벤트를 수행할 때 Content Cards를 제거할지 여부를 선택합니다.
6. 콘텐츠 카드의 만료 기간(피드 내 유지 시간)을 설정합니다. 일정 기간 후 또는 특정 시간에 만료되도록 설정할 수 있습니다.
7. **전달 설정**에서 필요에 따라 이 단계의 오디언스 또는 수신자를 필터링합니다. Segment를 지정하고 추가 필터를 추가하여 오디언스를 더 세분화할 수 있습니다. 오디언스 옵션은 지연 후 메시지가 전송되는 시점에 확인됩니다.
8. 메시지와 함께 사용할 다른 메시징 채널을 선택합니다.

{% endtab %}
{% endtabs %}

## 2단계: 메시지 유형 지정 {#step-2-specify-your-message-types}

세 가지 필수 Content Cards 유형 중 하나를 선택합니다: **클래식**, **자막 이미지**, **이미지 전용**.

각 유형의 예상 동작과 외관에 대해 자세히 알아보려면 [크리에이티브 세부 정보]({{site.baseurl}}/user_guide/channels/content_cards/creative_details)를 참조하거나 다음 표의 링크를 확인하세요. 이러한 Content Cards 유형은 모바일 앱과 웹 애플리케이션 모두에서 지원됩니다.

| 메시지 유형 | 예시 | 설명 |
|---|---|---|
| [클래식]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![운동 수업 예약을 권장하는 작은 아이콘과 텍스트가 있는 클래식 콘텐츠 카드.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) | 클래식 카드는 굵은 제목, 메시지 텍스트, 그리고 제목과 텍스트 시작 부분에 위치하는 선택적 이미지로 구성된 간결한 레이아웃입니다. 클래식 카드에는 정사각형 이미지나 아이콘을 사용하는 것이 가장 좋습니다. |
| [자막 이미지]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![역도 선수 이미지와 운동 수업 예약을 권장하는 텍스트가 있는 자막 콘텐츠 카드.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | 자막 이미지 카드는 카피와 시선을 사로잡는 이미지로 콘텐츠를 보여줍니다. |
| [이미지 전용]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types) | ![텍스트만 있는 이미지 전용 콘텐츠 카드.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | 이미지 전용 카드는 이미지, GIF 및 기타 텍스트가 아닌 크리에이티브 콘텐츠를 위한 공간으로 시선을 사로잡습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2단계: 메시지 유형 지정" }

## 3단계: 콘텐츠 카드 작성 {#step-3-compose-a-content-card}

메시지 편집기의 **Compose** 탭에서 메시지의 콘텐츠와 동작의 모든 측면을 편집할 수 있습니다.

![메시지 편집기의 Compose 탭에 있는 샘플 콘텐츠 카드 세부 정보.]({% image_buster /assets/img/content_card_compose.png %})

여기에 표시되는 콘텐츠는 이전 단계에서 선택한 **카드 유형**에 따라 달라지지만, 다음 옵션 중 하나를 포함할 수 있습니다:

### 언어 {#language}

**Add Languages**를 선택하여 제공된 목록에서 원하는 언어를 추가합니다. 이렇게 하면 메시지에 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic)가 삽입됩니다. Liquid에서 적절한 위치에 텍스트를 입력할 수 있도록 콘텐츠를 작성하기 전에 언어를 선택하는 것이 좋습니다. 사용할 수 있는 전체 언어 목록은 [지원되는 언어]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported)를 참조하세요.

![영어, 스페인어, 프랑스어가 언어로 선택되어 있고, 제목, 설명, 링크 텍스트가 국제화할 필드로 선택된 창.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### 오른쪽에서 왼쪽으로 쓰는 메시지 만들기 {#create-right-to-left-messages}

오른쪽에서 왼쪽으로 쓰는 메시지의 최종 모양은 서비스 제공업체가 렌더링하는 방식에 크게 좌우됩니다. 가능한 한 정확하게 표시되는 오른쪽에서 왼쪽으로 쓰는 메시지를 작성하기 위한 모범 사례는 [오른쪽에서 왼쪽으로 쓰는 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)를 참조하세요.

#### 제목 및 메시지 {#title-and-message}

원하는 내용을 자유롭게 작성할 수 있습니다. 제한은 없지만, 메시지를 빠르게 전달하고 고객이 클릭하도록 유도할수록 좋습니다! 명확하고 간결한 제목과 메시지 콘텐츠를 권장합니다. 이미지 전용 카드에는 이러한 필드가 제공되지 않습니다.

#### 이미지 {#image}

콘텐츠 카드에 이미지를 추가하려면 **Add Image**를 선택하거나 이미지 URL을 입력할 수 있습니다. **Add Image**를 선택하면 **미디어 라이브러리**가 열리며, 이전에 업로드한 이미지를 선택하거나 새 이미지를 추가할 수 있습니다.

각 메시지 유형과 플랫폼에는 고유한 권장 비율과 요구 사항이 있을 수 있으므로, 이미지를 의뢰하거나 처음부터 만들기 전에 반드시 확인하세요. 콘텐츠 카드 메시지 필드는 총 크기가 2&nbsp;KB로 제한됩니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### 상단에 고정 {#pin-to-top}

Braze는 고정된 카드를 사용자 피드의 상단에 표시하며, 사용자는 이를 닫을 수 없습니다. 사용자의 피드에 여러 개의 고정된 카드가 있는 경우, Braze는 시간순으로 정렬합니다. Braze가 콘텐츠 카드를 전달할 때 카드는 고정되거나 고정 해제된 상태이며, 해당 상태는 카드의 수명 동안 변경되지 않습니다. Campaign의 고정 설정을 변경하면 수정 후 전송된 카드에만 업데이트가 적용됩니다. 이미 사용자 피드에 있는 카드의 고정 상태는 변경되지 않습니다.

![모바일 및 웹용 Braze의 콘텐츠 카드 미리보기를 나란히 표시한 화면으로, '피드 상단에 이 카드 고정' 옵션이 선택되어 있습니다.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### 클릭 시 동작 {#on-click-behavior}

고객이 카드에 표시된 링크를 클릭하면 앱 내부로 더 깊이 이동하거나 다른 사이트로 이동할 수 있습니다. 콘텐츠 카드의 클릭 시 동작을 선택하는 경우 **Link Text**도 적절히 업데이트해야 합니다.

콘텐츠 카드 링크에 사용할 수 있는 동작은 다음과 같습니다:

| 동작 | 설명 |
|---|---|
| 웹 URL로 리디렉션 | 네이티브가 아닌 웹 페이지를 엽니다. |
| [앱으로 딥링크]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | 앱의 기존 화면으로 딥링크합니다. |
| 커스텀 이벤트 기록 | 트리거할 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events)를 선택합니다. 다른 콘텐츠 카드를 표시하거나 추가 메시징을 트리거하는 데 사용할 수 있습니다. |
| 커스텀 속성 기록 | 현재 사용자에 대해 설정할 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)을 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="클릭 시 동작" }

**커스텀 이벤트 기록** 및 **커스텀 속성 기록** 옵션에는 다음 SDK 버전 호환성이 필요합니다:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## 4단계: 추가 설정 구성(선택 사항) {#step-4-configure-additional-settings-optional}

[키-값 페어]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)를 사용하여 카드의 카테고리를 만들고, [여러 Content Cards 피드]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds)를 만들고, 카드 정렬 방식을 커스터마이즈할 수 있습니다.

메시지에 키-값 페어를 추가하려면 **Settings** 탭으로 이동하여 **Add New Pair**를 선택합니다.

## 5단계: Campaign 또는 Canvas의 나머지 부분 구성 {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Campaign의 나머지 부분을 구성합니다. Content Cards를 구성하기 위한 도구 활용 방법에 대한 자세한 내용은 다음 섹션을 계속 참조하세요.

### 전달 스케줄 또는 트리거 선택 {#choose-a-delivery-schedule-or-trigger}

Content Cards는 예약된 시간, 실행 또는 API 트리거를 기반으로 전달할 수 있습니다. 자세한 내용은 [Campaign 스케줄링]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)을 참조하세요.

Campaign의 기간과 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)을 설정하고 콘텐츠 카드의 만료를 결정할 수도 있습니다. 특정 만료 날짜 또는 카드가 만료될 때까지의 일수를 최대 30일까지 설정할 수 있습니다. 모든 배리언트의 만료 날짜는 동일합니다.

만료 카운트다운은 카드의 전송 시간부터 시작됩니다:

- **예약된 Campaigns:** 카운트다운은 예약된 시작 시간에 시작됩니다.
- **실행 기반 Campaigns:** 카운트다운은 사용자가 트리거 실행을 수행할 때 시작됩니다.

예를 들어, 실행 기반 콘텐츠 카드가 오늘 오후 2시에 전송되고 만료 기간이 1일인 경우, 다음 날 오후 2시에 만료됩니다.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

실행 기반 전달의 경우, 콘텐츠 카드가 표시되기 전에 짧은 지연이 예상됩니다. 이러한 지연이 발생하는 이유와 이를 최소화하는 방법에 대한 자세한 내용은 [트리거 이벤트 후 Content Cards가 즉시 표시되지 않는 이유는 무엇인가요?]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#why-dont-content-cards-appear-immediately-after-a-trigger-event)를 참조하세요.

#### 예약 전달 {#scheduled-delivery}

예약 전달이 포함된 콘텐츠 카드 캠페인의 경우, 카드가 생성되는 시기를 지정하여 Braze가 새 콘텐츠 카드 캠페인에 대한 오디언스 자격과 개인화를 평가하는 시기를 선택할 수 있습니다. 자세한 내용은 [카드 생성]({{site.baseurl}}/card_creation)을 참조하세요.

#### 타겟 사용자 선택 {#choose-users-to-target}

다음으로, Segments 또는 필터를 선택하여 오디언스를 좁혀 [사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)합니다. 해당 대략적인 Segment 모집단이 어떻게 보이는지 자동으로 미리보기가 제공됩니다. 정확한 Segment 멤버십은 항상 메시지가 전송되기 전에 계산된다는 점을 유의하세요.

{% multi_lang_include audience/target_audiences.md %}

#### 전환 이벤트 선택 {#choose-conversion-events}

Braze를 사용하면 Campaign을 수신한 후 사용자가 특정 실행인 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 수행하는 빈도를 추적할 수 있습니다. 사용자가 지정된 실행을 수행하면 전환이 집계되는 최대 30일의 기간을 허용하는 옵션이 있습니다.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면 Canvas 구성 요소의 나머지 섹션을 완료하세요. Canvas의 나머지 부분을 구성하고, [다변량 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing) 및 [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection)을 구현하는 방법 등에 대한 자세한 내용은 Canvas 설명서의 [Canvas 구성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) 단계를 참조하세요.

{% endtab %}
{% endtabs %}

## 6단계: 검토 및 배포 {#step-6-review-and-deploy}

Campaign 또는 Canvas 빌드를 완료한 후 세부 사항을 검토하고, [테스트한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) 다음 전송합니다. 자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card)를 참조하세요.

{% alert warning %}
콘텐츠 카드가 시작된 후에는 편집할 수 없습니다. 새 사용자에게 전송을 중지하거나 사용자의 피드에서 제거하는 것만 가능합니다. 이 시나리오에 대한 접근 방법을 이해하려면 [전송된 카드 업데이트]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards)를 참조하세요.
{% endalert %}

다음으로, [콘텐츠 카드 보고]({{site.baseurl}}/user_guide/channels/content_cards/reporting)를 확인하여 콘텐츠 카드 캠페인의 결과에 액세스하는 방법을 알아보세요.

## 알아두어야 할 사항 {#things-to-know}

### 페이로드 및 피드 제한 {#payload-and-feed-limitations}

성능을 지원하기 위해 Content Cards에는 두 가지 주요 제약 조건이 있습니다: 각 카드의 페이로드 크기 제한과 피드에 표시할 수 있는 최대 카드 수입니다.

#### Content Cards 크기 제한 {#size-limitations-for-content-cards}

단일 콘텐츠 카드의 전체 데이터 페이로드는 Liquid 개인화가 렌더링된 **이후** 2KB를 초과할 수 없습니다. 여기에는 다음이 포함됩니다:

* 제목
* 메시지
* 이미지 URL(이미지 파일 크기가 아닌 URL 문자열 자체의 길이)
* 링크 텍스트
* 지정된 모든 플랫폼의 링크 URL(iOS, Android, 웹의 개별 URL이 모두 총합에 포함됨)
* 키-값 페어(키 이름과 값 모두)

Liquid를 사용하여 긴 텍스트 문자열(예: 커스텀 속성에서)을 가져오면 제한을 초과할 수 있습니다.

Campaign 작성기는 정적 콘텐츠가 제한을 초과하면 경고를 표시합니다. Liquid를 사용하는 동적 콘텐츠의 크기는 예측하지 않습니다. 메시지 크기가 2KB를 초과하면 전송 시 중단됩니다. 이러한 중단은 메시지 활동 로그에서 `Content card maximum size exceeded` 사유로 확인할 수 있습니다.

{% alert important %}
테스트 전송 시에는 2KB를 초과하는 Content Cards도 정상적으로 전달 및 표시될 수 있습니다.
{% endalert %}

다음은 Content Cards 페이로드 크기를 관리하기 위한 모범 사례입니다:

* 긴 링크에는 URL 단축기를 사용하세요. URL, 특히 광범위한 추적 파라미터가 포함된 URL은 크기 제한 문제가 발생할 수 있습니다. URL 단축 서비스를 사용하면 문자 수를 크게 줄이고 페이로드 공간을 확보할 수 있습니다.
* Liquid로 동적 콘텐츠를 잘라내세요. 사용자 속성이나 API 호출의 동적 텍스트로 카드를 개인화할 때 콘텐츠 길이가 예측 불가능할 수 있습니다. `truncate`와 같은 Liquid 필터를 사전에 사용하여 동적 텍스트의 길이를 제한하세요.
* 멀티 플랫폼 URL을 효율적으로 사용하세요. 2KB 제한에는 정의한 모든 플랫폼의 URL이 포함됩니다. 각 플랫폼에 길고 고유한 URL을 사용하면 페이로드 크기가 배로 늘어날 수 있습니다. 가능하면 모든 플랫폼에서 작동하는 단일 링크를 사용하거나 필요에 따라 URL 단축기를 사용하세요.
* 더 풍부한 콘텐츠에는 배너를 고려하세요. 지속적으로 대량의 콘텐츠가 필요한 사용 사례의 경우 Content Cards가 적합한 채널이 아닐 수 있습니다. 배너에는 동일한 2KB 페이로드 제한이 없으며 앱이나 웹사이트 경험에 더 풍부한 콘텐츠를 직접 삽입하는 데 더 적합합니다.

#### 피드의 카드 수 {#number-of-cards-in-feed}

각 사용자는 주어진 시점에 피드에 최대 250개의 만료되지 않은 Content Cards를 보유할 수 있습니다. 이 제한을 초과하면 Braze는 읽지 않은 카드라도 가장 오래된 카드부터 반환을 중지합니다. 해제된 카드도 이 제한에 포함되므로 해제된 카드가 많으면 오래된 카드에 사용할 수 있는 공간이 줄어듭니다.

카드 제한 관련 문제를 방지하기 위해 다음 모범 사례를 권장합니다:

- **더 짧은 만료일을 사용하세요:** 시간에 민감한 Campaign(예: 주말 세일)의 경우 특정 만료일을 설정하세요. 이렇게 하면 카드가 더 이상 관련이 없어진 후 피드에서 자동으로 제거되고 제한에 포함되지 않습니다.
- **실행 기반 제거를 활용하세요:** 트랜잭션 또는 목표 기반 카드에 대한 제거 이벤트를 설정하세요. 예를 들어, 사용자에게 프로필 완성을 요청하는 카드는 `profile_completed` 이벤트가 기록되는 즉시 제거되어야 합니다.
- **장기 실행 Campaign을 감사하세요:** 반복 또는 진행 중인 Campaign을 검토하여 시간이 지남에 따라 너무 많은 카드로 피드를 채워 사용자에게 좋지 않은 경험을 만들고 있지 않은지 확인하세요.

### Content Cards의 재자격 이해 {#understanding-re-eligibility-for-content-cards}

재자격은 사용자가 동일한 Campaign에서 메시지를 두 번 이상 받을 수 있는지 여부와 시기를 결정합니다. Content Cards의 경우 이 작동 방식을 이해하는 것은 반복 Campaign을 관리하고 사용자가 중복되거나 오래된 메시지를 받지 않도록 하는 데 매우 중요합니다.

{% alert tip %}
콘텐츠가 30일 이상 지속되기를 원하시나요? [배너]({{site.baseurl}}/user_guide/channels/banners)를 사용해 보세요.
{% endalert %}

#### 재자격 계산 방법 {#how-re-eligibility-is-calculated}

재자격을 켜면 사용자가 Campaign에 "재진입"할 수 있는 시점의 카운트다운은 메시지가 전송된 후 시작됩니다. 이 카운트다운이 시작되는 구체적인 시점은 카드 생성 설정에 따라 다릅니다:

- [첫 번째 노출 시]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences)를 사용하는 Content Cards는 노출 시간을 기준으로 재자격을 계산합니다.
- Campaign 시작 시, 멀티채널 Campaign에서, 또는 캔버스 단계 진입 시 생성된 Content Cards는 전송 시간 또는 노출 시간 중 더 늦은 시간을 사용합니다.

#### 30일 만료와 재자격 {#the-30-day-expiration-and-re-eligibility}

혼란의 일반적인 원인은 Campaign 재자격과 모든 Content Cards의 자동 30일 만료 간의 상호 작용입니다.

모든 Content Cards는 전송되거나 제거된 후 30일이 지나면 Braze 시스템에서 자동으로 삭제됩니다. 재자격이 **꺼진** 상태에서 장기 실행 반복 Campaign이 있는 경우, 사용자는 30일 후에도 동일한 카드를 다시 받을 수 있습니다. 원래 카드가 삭제되면 시스템은 해당 사용자가 Campaign을 받은 기록을 더 이상 볼 수 없으므로 다음 세션에서 다시 자격이 부여됩니다.

사용자가 특정 Campaign에서 메시지를 한 번만 받도록 하려면 이 Campaign에서 메시지를 받지 않은 사용자에 대한 오디언스 필터를 Campaign 또는 캔버스 단계에 추가하세요. 이 필터는 장기 실행 Campaign에서 중복 전송을 방지하는 가장 안정적인 방법입니다.

### 실시간 Content Cards 관리 {#managing-live-content-cards}

Content Cards가 전송된 후에는 사용자에게 전달될 준비가 된 "받은편지함"에 대기합니다(이메일과 유사). 콘텐츠가 콘텐츠 카드에 가져와지면(표시 시점에) 수명 동안 변경할 수 없습니다. 이는 연결된 콘텐츠를 통해 API를 호출하고 엔드포인트의 데이터가 변경되더라도 마찬가지입니다. 이 데이터는 업데이트되지 않습니다. 새 사용자에게 전송을 중지하고 사용자의 피드에서 제거하는 것만 가능합니다. Campaign을 수정하면 수정 후 전송된 카드만 업데이트가 포함됩니다.

#### 시작된 카드 업데이트 {#updating-launched-cards}

이미 카드를 받은 사용자의 카드를 변경하려면 다음 방법 중 하나를 사용해야 합니다:

##### 옵션 1: Campaign 복제(즉각적인 변경에 권장) {#option-1-duplicate-the-campaign-recommended-for-immediate-changes}

{% alert tip %}
카드에 최신 콘텐츠를 표시하거나, 변경 사항을 즉시 표시해야 하거나, 재자격이 꺼져 있는 메시지에 이 옵션을 권장합니다.
{% endalert %}

첫 번째 방법은 Campaign을 보관하고 새로 복제된 Campaign을 시작하는 것입니다:

1. 원래 Campaign을 중지하고 메시지가 표시되면 `Remove card after the next sync`를 선택합니다.
2. Campaign을 복제하고 편집한 후 새 버전을 시작합니다.

Campaign을 복제할 때 새 버전의 오디언스를 정의해야 합니다. 세분화 필터를 사용하여 업데이트된 카드를 받을 사용자를 제어하세요:
* 사용자가 콘텐츠 카드에 대해 재자격이 없어야 하는 경우, `Received Message from Campaign` 필터를 `Has Not` 조건으로 설정하여 이전 버전의 콘텐츠 카드를 받지 않은 사용자를 필터링할 수 있습니다.
* 이전 카드를 받은 사용자가 X일 후에 재자격이 되어야 하는 경우, `Last Received Message from specific campaign` 필터를 X일 이전으로 설정하거나 **또는** `Received Message from Campaign`을 `Has Not` 조건으로 설정할 수 있습니다.

###### 영향 {#impact}

- **기존 수신자:** 자격이 있는 경우 신규 및 기존 수신자 모두 다음 피드 새로고침 시 업데이트된 카드를 볼 수 있습니다.
- **보고:** 각 버전의 카드에는 별도의 분석이 있습니다.

세션 시작으로 트리거되도록 Campaign을 설정하고 재자격을 30일로 설정했다고 가정해 보겠습니다. 사용자가 2일 전에 Campaign을 받았고 문구를 변경하려고 합니다. 먼저 Campaign을 보관하고 피드에서 카드를 제거합니다. 그런 다음 Campaign을 복제하고 새 문구로 다시 시작합니다. 사용자가 다른 세션을 시작하면 즉시 새 카드를 받습니다.

##### 옵션 2: 동일한 Campaign 중지 및 재시작 {#option-2-stop-and-relaunch-the-same-campaign}

{% alert tip %}
알림 센터 또는 메시지 받은편지함의 고유 메시지(예: 프로모션), 분석을 통합하는 것이 중요한 경우, 또는 메시지의 적시성이 중요하지 않은 경우(예: 기존 수신자가 업데이트된 카드를 보기 전에 자격 기간을 기다릴 수 있는 경우)에 이 옵션을 사용하는 것을 권장합니다.
{% endalert %}

이 방법은 모든 분석을 단일 Campaign에 통합합니다. 새로 자격이 부여된 사용자는 새 카드를 받지만 기존 수신자에 대한 업데이트는 재자격이 될 때까지 지연됩니다:

1. Campaign을 중지하고 메시지가 표시되면 **Remove card after the next sync**를 선택합니다.
2. 필요에 따라 Campaign을 편집합니다.
3. Campaign을 다시 시작합니다.

###### 영향

* **기존 수신자:** 이미 카드를 받은 사용자는 재자격이 될 때까지 업데이트된 카드를 받지 않습니다. 재자격이 꺼져 있으면 새 카드를 받지 못합니다.
* **보고:** 하나의 Campaign에 시작된 카드 버전에 대한 모든 보고 분석이 포함됩니다. Braze는 시작된 버전을 구분하지 않습니다.

세션 시작으로 트리거되고 재자격이 30일로 설정된 Campaign이 있다고 가정해 보겠습니다. 사용자가 2일 전에 Campaign을 받았고 문구를 변경하려고 합니다. 먼저 Campaign을 중지하고 피드에서 카드를 제거합니다. 그런 다음 새 문구로 Campaign을 다시 게시합니다. 사용자가 다른 세션을 시작하면 28일 후에 새 카드를 받습니다.

{% alert note %}
Campaign을 중지하고 제거 이벤트 설정을 편집한 후 피드에서 카드를 제거하지 않고 Campaign을 다시 시작하면 사용자 피드에 있는 기존 카드는 업데이트된 제거 이벤트 설정을 사용합니다. 카드는 처음 전송되었을 때의 원래 제거 이벤트 구성을 유지하지 않습니다.
{% endalert %}

#### 카드 제거 및 만료 {#removing-and-expiring-cards}

##### 수동 카드 제거 {#manual-card-removal}

Campaign을 중지하여 언제든지 모든 사용자의 피드에서 카드를 수동으로 제거할 수 있습니다.

1. 콘텐츠 카드 캠페인을 열고 Campaign 중지를 선택합니다.
2. 메시지가 표시되면 **Remove card after the next sync**를 선택합니다. 다음 피드 새로고침 시 카드가 제거됩니다.

##### 자동 카드 제거 {#action-based-card-removal}

구매 완료 또는 기능 활성화와 같이 사용자가 특정 작업을 수행할 때 카드를 자동으로 제거할 수 있습니다.

Campaign 또는 캔버스 단계에서 제거 이벤트를 지정하세요. 사용자가 해당 이벤트를 수행하면 Braze가 이벤트를 처리한 후 후속 새로고침 시 피드에서 카드가 제거됩니다.

{% alert note %}
이 제거는 즉각적이지 않습니다. 처리 지연이 있으므로 카드가 사라지기까지 몇 분이 걸리고 피드 새로고침이 한 번 이상 필요할 수 있습니다.
{% endalert %}

{% alert tip %}
사용자의 피드에서 카드를 제거해야 하는 여러 커스텀 이벤트와 구매를 지정할 수 있습니다. 사용자가 이러한 작업 중 하나를 수행하면 Campaign의 카드에서 전송된 기존 카드가 제거됩니다. 자격이 있는 카드는 메시지 스케줄에 따라 계속 전송됩니다.
{% endalert %}

![콘텐츠 카드 제거 이벤트 옵션이 있는 콘텐츠 카드 제거 조건 패널.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### 카드 만료 {#card-expiration}

Content Cards는 전송된 후 최대 30일 동안 사용할 수 있습니다. 30일이 지나면 Braze가 사용자 피드에서 제거하고 Braze 시스템에서 삭제합니다.

#### 카드를 30일 이상 유지하기 {#making-cards-last-longer-than-30-days}

{% alert tip %}
30일 Content Cards 제한보다 더 오래 메시지를 유지해야 하는 사용 사례의 경우 배너 사용을 고려하세요. 배너는 지속성을 위해 설계되었으며 필수 만료일이 없어 필요한 만큼 계속 표시할 수 있습니다.
{% endalert %}

카드가 항상 사용 가능한 것처럼 보이게 하려면 30일마다 카드를 효과적으로 교체하는 반복 Campaign을 만들 수 있습니다:

1. Content Cards의 기간을 30일로 설정합니다.
2. Campaign 재자격을 30일로 설정합니다.
3. Campaign을 "세션 시작" 시 트리거되도록 설정합니다.

### Content Cards 동기화 및 새로고침 {#content-card-sync-and-refresh}

Content Cards는 스케줄에 따라 그리고 앱이 피드를 새로고침할 때 동기화됩니다. 동기화 동작은 전체 동기화와 부분 동기화 간에 다르며, SDK 통합은 세션 시작 시 카드가 새로고침되는 시기에 영향을 줍니다. 구현 세부 사항은 [콘텐츠 카드 피드 커스터마이징]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) 및 [Content Cards 생성]({{site.baseurl}}/developer_guide/content_cards/creating_cards)을 참조하세요.

### Content Cards Campaign 중지의 영향 {#impact-of-stopping-content-cards-campaigns}

Campaign을 중지하고 **Remove card after the next sync**를 선택하면 Braze는 다음 새로고침 시 사용자 피드에서 카드를 제거합니다. 사용자가 카드를 보기 전에 제거된 카드에 대해서는 노출이 기록되지 않으므로 노출 횟수가 전송 수보다 낮을 수 있습니다.

## 문제 해결 {#troubleshooting}

### 트리거 이벤트 후 Content Cards가 즉시 표시되지 않는 이유는 무엇인가요? {#why-dont-content-cards-appear-immediately-after-a-trigger-event}

실행 기반 전달 Campaign(예: 세션 시작)의 경우, 트리거 이벤트와 카드가 사용 가능해지는 시점 사이에 예상되는 짧은 지연이 있습니다. 이 지연은 다음과 같은 이유로 발생합니다:

- 트리거 이벤트가 Braze 서버로 전송됩니다
- Campaign이 트리거되고 사용자의 자격이 기록됩니다
- 해당 사용자를 위한 콘텐츠 카드가 데이터베이스에 생성됩니다
- SDK가 동기화되어 사용 가능한 모든 카드를 기기로 가져옵니다

SDK 동기화가 사용자의 자격이 기록되기 전에 발생하면, 사용자는 카드를 수신하지 못합니다.

첫 번째 세션에 있는 신규 사용자의 경우 이 지연은 불가피합니다. 즉시 사용 가능해야 하는 기존 사용자의 경우, 예약 전달 사용을 고려하세요.

신규 사용자와 기존 사용자 모두의 지연을 최소화해야 하는 경우, 두 개의 Campaign을 만들 수 있습니다:

- **세션 수가 0보다 큰 기존 사용자:** 예약 전달 Campaign을 사용합니다. 카드가 미리 생성되어 즉시 사용할 수 있습니다.
- **세션 수가 0인 신규 사용자:** 실행 기반 트리거 Campaign을 사용합니다. 첫 번째 세션 트리거 후 카드가 생성됩니다.

이 접근 방식은 기존 사용자가 카드를 즉시 볼 수 있도록 하면서, 신규 사용자에게는 첫 번째 세션에서 짧은 지연 후에도 도달할 수 있도록 합니다. 지연 시간을 개선하기 위한 추가 전략은 [Content Cards의 낮은 지연 시간 개선]({{site.baseurl}}/user_guide/channels/content_cards/best_practices/improving_low_latency_requirements)을 참조하세요.