---
nav_title: "푸시 메시지 만들기"
article_title: "푸시 메시지 만들기"
page_order: 1
page_type: tutorial
description: "이 튜토리얼 페이지에서는 구성, 발송, 타겟팅 등 푸시 메시지를 만드는 데 관련된 다양한 구성요소를 다룹니다."
channel: push
tool:
  - Campaigns

---

# 푸시 메시지 만들기 {#create-a-push-message}

> 푸시 알림은 시간에 민감한 행동 유도와 한동안 앱을 사용하지 않은 사용자를 다시 참여시키는 데 매우 유용합니다. 성공적인 푸시 캠페인은 사용자를 콘텐츠로 직접 안내하고 앱의 가치를 보여줍니다. 푸시 알림 예시를 확인하려면 [Braze 고객 사례 연구](https://www.braze.com/customers)를 참조하세요.

## 1단계: 메시지를 작성할 위치 선택 {#create-new-campaign-push}

{% alert tip %}
Campaign과 Canvas 중 어떤 것을 사용할지 확실하지 않으신가요? Campaign은 단일 타겟 메시징에 적합하고, Canvas는 다단계 사용자 여정에 더 적합합니다.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. **메시징** > **Campaigns**로 이동한 다음 **캠페인 생성**을 선택합니다.
2. 여러 채널을 타겟팅하는 Campaign의 경우 **멀티채널**을 선택합니다. 그렇지 않으면 **푸시 알림**을 선택합니다.
3. Campaign에 명확하고 의미 있는 이름을 지정합니다.
4. 필요에 따라 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) 및 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/)를 추가합니다.

{% alert tip %}
태그를 사용하면 Campaign을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder/)를 사용할 때 특정 태그로 필터링할 수 있습니다.
{% endalert %}

{: start="5"}
5. Campaign에 필요한 만큼 배리언트를 추가하고 이름을 지정합니다. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing/)를 참조하세요.

{% alert tip %}
Campaign의 모든 메시지가 유사하거나 동일한 콘텐츠를 가질 경우, 추가 배리언트를 추가하기 전에 먼저 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. Canvas 작성기를 사용하여 [Canvas를 생성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)합니다.
2. Canvas를 설정한 후 Canvas 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 지정합니다.
3. [단계 스케줄]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay)을 선택하고 필요에 따라 지연을 지정합니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. Segments를 지정하고 추가 필터를 추가하여 이 단계의 수신자를 더 세밀하게 조정할 수 있습니다. 오디언스 옵션은 메시지가 발송되는 시점에 지연 후 확인됩니다.
5. [진행 동작]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/)을 선택합니다.
6. 메시지와 함께 사용할 다른 메시징 채널을 선택합니다.

{% endtab %}
{% endtabs %}

## 2단계: 푸시 플랫폼 선택 {#step-2-select-push-platforms}

다음으로, 푸시를 수신할 플랫폼과 모바일 기기 조합을 선택합니다. 이 선택을 사용하여 푸시 알림의 전달을 특정 앱 세트로 제한합니다.

이전 선택에 따라 몇 가지 다른 방법이 있습니다:

| 이전 선택 | 옵션 |
| --- | --- |
| 푸시 알림 캠페인 | 하나 이상의 플랫폼과 기기를 선택합니다. 여러 기기와 플랫폼을 타겟팅하도록 선택하면 선택한 모든 플랫폼에 대해 하나의 메시지를 작성하는 데 최적화된 편집 환경이 제공됩니다. 이 편집 환경에서 달라지는 점을 이해하려면 [다중 플랫폼 푸시]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push/)를 참조하세요. |
| 멀티채널 캠페인 | **메시징 채널 추가**를 선택하여 추가 푸시 플랫폼을 추가합니다. 플랫폼 선택은 각 배리언트에 고유하므로 플랫폼별 메시지 참여를 테스트할 수 있습니다. |
| Canvas | 메시지 단계에서 **+ 더 추가**를 선택하여 추가 푸시 플랫폼을 추가합니다. 멀티채널 캠페인과 마찬가지로 플랫폼 선택은 각 배리언트에 고유합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: 푸시 플랫폼 선택" }

## 3단계: 알림 유형 선택 (iOS 및 Android) {#step-3-select-notification-type-ios-and-android}

다중 플랫폼 푸시 캠페인을 만들고 웹 및/또는 Kindle을 선택한 경우 알림 유형은 자동으로 **표준 푸시**로 설정되며 변경할 수 없습니다.

![표준 푸시가 선택된 알림 유형 예시.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

그렇지 않은 경우 iOS 및 Android에서 알림 유형을 선택합니다:

- 표준 푸시
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories/) (Android + iOS 지원)
- 인라인 이미지 (Android 전용)

푸시 캠페인에 이미지를 포함하려면 [iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/) 또는 [Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/)용 리치 알림 만들기에 대한 다음 가이드를 참조하세요.

## 4단계: 푸시 메시지 작성 {#step-4-compose-your-push-message}

이제 푸시 메시지를 작성할 차례입니다! **작성** 탭에서 메시지의 콘텐츠와 동작의 모든 측면을 편집할 수 있습니다.

![푸시 알림 만들기의 작성 탭.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

**작성** 탭의 콘텐츠는 이전 단계에서 선택한 알림 유형에 따라 달라지며, 다음 옵션 중 하나를 포함할 수 있습니다:

### 알림 채널 또는 그룹 (iOS 및 Android) {#notification-channel-or-group-ios-and-android}

플랫폼별 알림 옵션에 대한 자세한 내용은 [iOS 알림 옵션]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/) 또는 [Android 알림 옵션]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_options/)을 참조하세요.

### 언어 {#language}

**언어 추가** 버튼을 사용하여 여러 언어로 문구를 추가합니다. 콘텐츠를 작성하기 전에 언어를 선택하여 Liquid에서 적절한 위치에 텍스트를 입력하는 것을 권장합니다. 사용 가능한 전체 언어 목록은 [지원되는 언어]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)를 참조하세요.

오른쪽에서 왼쪽으로 쓰는 언어로 문구를 추가하는 경우, 오른쪽에서 왼쪽으로 쓰는 메시지의 최종 모양은 서비스 제공업체가 렌더링하는 방식에 크게 좌우됩니다. 가능한 한 정확하게 표시되는 오른쪽에서 왼쪽으로 쓰는 메시지를 작성하는 모범 사례는 [오른쪽에서 왼쪽으로 쓰는 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/)를 참조하세요.

### 제목 및 본문 {#title-and-body}

{% tabs local %}
{% tab ios %}
메시지 상자에 입력을 시작하면 왼쪽 미리보기 상자에 미리보기가 나타납니다. 푸시 메시지는 일반 텍스트 형식이어야 합니다.

**제목** 필드를 사용하여 헤드라인을 추가합니다. 푸시를 개인화하고 타겟팅하려면 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)를 포함할 수 있습니다.
{% endtab %}

{% tab android %}
메시지 상자에 입력을 시작하면 왼쪽 미리보기 상자에 미리보기가 나타납니다. 푸시 메시지는 일반 텍스트 형식이어야 합니다.

푸시를 개인화하고 타겟팅하려면 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)를 포함할 수 있습니다.

{% alert important %}
제목 없이 Android 푸시 메시지를 보낼 수 **없습니다**&#8212;그러나 대신 공백 하나를 입력할 수 있습니다. 메시지에 공백 하나만 포함된 경우 무음 푸시 알림으로 발송된다는 점에 유의하세요. 자세한 내용은 [무음 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)을 참조하세요.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
멋진 문구를 작성하는 데 도움이 필요하신가요? [AI 카피라이팅 어시스턴트]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-copy)를 사용해 보세요. 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있는 사람이 쓴 것 같은 마케팅 문구를 생성합니다.

![푸시 작성기의 본문 필드에 있는 AI 카피라이터 시작 버튼.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

### 이미지 {#image}

지원되는 경우 앱 아이콘이 푸시 알림의 이미지로 자동 추가됩니다. 또한 리치 알림을 보내는 옵션도 있으며, 이를 통해 문구 외에 추가 콘텐츠를 추가하여 푸시 알림을 더욱 커스터마이징할 수 있습니다.

푸시 알림에서 이미지를 사용하는 방법에 대한 추가 안내는 다음 문서를 참조하세요:

- [iOS용 리치 알림 만들기]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/)
- [Android용 리치 알림 만들기]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### 클릭 시 동작 {#on-click-behavior}

**On-Click Behavior**로 사용자가 푸시 알림의 본문을 선택할 때 어떤 일이 발생하는지 지정합니다. 예를 들어, 고객에게 애플리케이션을 열도록 유도하거나, 지정된 웹 URL로 리디렉션하거나, [딥링크]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/)를 사용하여 애플리케이션의 특정 페이지를 열 수도 있습니다.

여기에서 푸시 알림 내에 버튼 프롬프트를 설정할 수도 있습니다. 예를 들면:

- Accept/Decline
- Yes/No
- Confirm/Cancel
- More

### 발송 옵션 {#sending-options}

사용자가 여러 기기에 앱을 설치한 경우, 기본적으로 푸시 메시지는 유효한 푸시 토큰이 할당된 모든 기기로 발송됩니다. 원하는 경우 **가장 최근에 사용한 기기**를 선택할 수 있습니다.

![사용자의 가장 최근에 사용한 기기에만 이 푸시를 보내는 기기 옵션 체크박스.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

이 설정에는 몇 가지 세부 사항이 있습니다. 이 옵션을 선택하면 Braze는 iOS와 Android 모두를 타겟팅하는 것처럼 Campaign이 여러 플랫폼을 타겟팅하는 경우를 제외하고 다중 발송을 제한합니다. 사용자가 iOS와 Android 기기 모두에 앱을 가지고 있는 경우 두 플랫폼 모두에 대해 푸시를 받게 됩니다. 사용자의 가장 최근에 사용한 기기가 [푸시 활성화]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled) 상태가 아닌 경우 메시지가 발송되지 않습니다.

기본적으로 Braze는 유효한 푸시 토큰이 있는 사용자가 소유한 모든 기기로 메시지를 보냅니다. iOS의 경우 iPad 기기에만 알림을 보내거나 iPhone 및 iPod 기기에만 알림을 보내도록 도달 범위를 더 세밀하게 조정할 수 있습니다.

원하는 경우 푸시 대상을 **가장 최근에 사용한 기기**로 설정할 수 있습니다.

#### 가장 최근에 사용한 기기 {#most-recently-used-device}

"가장 최근에 사용한"은 행동적 상태가 아닌 기술적 상태입니다. Braze는 기본적으로 모든 기기로 발송하므로, 이 설정으로 전환하면 도달 범위가 크게 줄어들고 가장 최신 토큰을 가진 단일 기기의 상태에 전적으로 의존하게 됩니다.

가장 최근에 사용한 기기는 가장 최근 세션이 있었던 기기가 아니라, 가장 최근에 업데이트된 푸시 토큰을 가진 기기에 의해 결정됩니다.
* API를 통해 새 기기의 푸시 토큰이 사용자 프로필에 추가되면, 사용자가 아직 해당 기기에서 세션을 시작하지 않았더라도 해당 기기가 즉시 가장 최근에 사용한 기기로 간주됩니다.
* 사용자의 가장 최근에 사용한 기기가 [푸시 활성화]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled) 상태가 아닌 경우 메시지가 전혀 발송되지 않습니다.

Campaign이 iOS와 Android 등 서로 다른 플랫폼을 타겟팅하는 경우 다중 발송이 여전히 발생할 수 있습니다. 사용자가 두 플랫폼 모두에 앱을 가지고 있는 경우 두 플랫폼 모두에 대해 푸시를 받을 수 있습니다.

iOS의 경우 iPad 기기에만 푸시 알림을 보내거나 iPhone 및 iPod 기기에만 보내도록 메시징을 추가로 제한할 수 있습니다.

## 5단계: 메시지 미리보기 및 테스트 (선택 사항) {#step-5-preview-and-test-your-message-optional}

테스트는 가장 중요한 단계 중 하나입니다. 완벽한 푸시 메시지를 작성한 후 발송하기 전에 테스트하세요. **테스트** 탭을 선택하여 푸시 메시지를 테스트하는 방법에 대한 옵션을 선택합니다. **테스트 수신자**에서 콘텐츠 테스트 그룹 또는 개별 사용자를 선택할 수 있습니다. 또한 **사용자로 메시지 미리보기**를 사용하여 임의의 사용자, 기존 사용자, 커스텀 사용자 또는 다국어 사용자에 대해 모바일에서 메시지가 어떻게 보이는지 확인할 수 있습니다.

자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=push)를 참조하세요.

## 6단계: 나머지 Campaign 또는 Canvas 구축 {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

나머지 Campaign을 구축합니다. 푸시 알림을 구축하기 위한 도구 활용 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

### 전달 스케줄 또는 트리거 선택 {#choose-delivery-schedule-or-trigger}

푸시 메시지는 예약된 시간, 실행 또는 API 트리거를 기반으로 전달할 수 있습니다. 자세한 내용은 [Campaign 스케줄링]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/)을 참조하세요.

실행 기반 전달의 경우 Campaign의 기간과 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/)도 설정할 수 있습니다.

이 단계에서는 사용자가 Campaign을 다시 받을 수 있도록 [재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns)을 허용하거나 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping) 규칙을 활성화하는 등의 전달 제어를 지정할 수도 있습니다.

### 타겟 사용자 선택 {#choose-users-to-target}

다음으로, Segments 또는 필터를 선택하여 오디언스를 좁혀 [사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/)해야 합니다. 해당 대략적인 Segment 인구가 어떻게 보이는지 자동으로 미리보기가 제공됩니다. Campaign이 타겟팅하는 채널에 대한 상세한 오디언스 통계는 하단에서 확인할 수 있습니다. 사용자 기반의 몇 퍼센트가 타겟팅되고 있는지와 이 Segment의 생애주기 가치를 확인하려면 **추가 통계 표시**를 선택하세요.

{% multi_lang_include target_audiences.md %}

{% details 총 도달 가능 사용자 측정기준이 모든 채널의 합계와 일치하지 않는 이유는 무엇인가요? %}

필터링된 오디언스의 총 도달 가능 사용자를 볼 때, 개별 열의 합계가 총 도달 가능 사용자보다 작을 수 있습니다. 이 차이는 일반적으로 Campaign의 Segment 또는 필터에 해당하지만 푸시를 통해 도달할 수 없는 사용자(예: 유효하거나 활성 상태인 [푸시 토큰]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle/#push-tokens)이 없는 경우)가 있기 때문입니다.

{% enddetails %}

![도달 가능 사용자에 대한 상세 오디언스 통계 테이블.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

정확한 Segment 멤버십은 항상 메시지가 발송되기 전에 계산된다는 점을 유의하세요.

또한 가입됨 및 푸시 옵트인 상태인 사용자와 같이 특정 [구독 상태]({{site.baseurl}}/user_guide/channels/email/subscriptions/)를 가진 사용자에게만 Campaign을 보내도록 선택할 수도 있습니다.

선택적으로 Segment 내 지정된 수의 사용자에게만 전달을 제한하거나, Campaign이 반복될 때 사용자가 동일한 메시지를 두 번 받을 수 있도록 허용할 수도 있습니다.

#### 이메일과 푸시를 포함한 멀티채널 캠페인 {#multichannel-campaigns-with-email-and-push}

이메일과 푸시 채널 모두를 타겟팅하는 멀티채널 캠페인의 경우, 명시적으로 옵트인한 사용자만 메시지를 받도록 Campaign을 제한할 수 있습니다(가입됨 또는 가입 취소된 사용자 제외). 예를 들어, 서로 다른 옵트인 상태를 가진 세 명의 사용자가 있다고 가정합니다:

- **사용자 A**는 이메일에 가입되어 있고 푸시가 활성화되어 있습니다. 이 사용자는 이메일을 받지 않지만 푸시를 받습니다.
- **사용자 B**는 이메일에 옵트인되어 있지만 푸시가 활성화되어 있지 않습니다. 이 사용자는 이메일을 받지만 푸시를 받지 않습니다.
- **사용자 C**는 이메일에 옵트인되어 있고 푸시가 활성화되어 있습니다. 이 사용자는 이메일과 푸시를 모두 받습니다.

이렇게 하려면 **오디언스 요약**에서 이 Campaign을 "옵트인한 사용자에게만" 보내도록 선택합니다. 이 옵션은 옵트인한 사용자만 이메일을 받도록 보장하며, Braze는 기본적으로 푸시가 활성화된 사용자에게만 푸시를 보냅니다.

{% alert important %}
이 구성에서는 **타겟 오디언스** 단계에서 오디언스를 단일 채널로 제한하는 필터(예: `Foreground Push Enabled = True` 또는 `Email Subscription = Opted-In`)를 포함하지 마세요.
{% endalert %}

### 전환 이벤트 선택 {#choose-conversion-events}

Braze를 사용하면 사용자가 Campaign을 받은 후 특정 행동인 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 행동을 취하면 전환이 집계되는 최대 30일의 기간을 허용하는 옵션이 있습니다.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면 Canvas 구성요소의 나머지 섹션을 완료하세요. Canvas의 나머지 부분을 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대한 자세한 내용은 Canvas 설명서의 [Canvas 구축]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.

{% endtab %}
{% endtabs %}

## 7단계: 검토 및 배포 {#review-and-deploy-push}

Campaign 또는 Canvas의 마지막 부분을 완성한 후 세부 정보를 검토합니다. Campaign의 경우 마지막 페이지에서 설계한 Campaign의 요약을 제공합니다. 모든 관련 세부 정보를 확인하고, 메시지를 테스트한 다음 발송하고 데이터가 들어오는 것을 확인하세요!

다음으로, 푸시 캠페인의 결과에 액세스하는 방법을 알아보려면 [푸시 보고]({{site.baseurl}}/user_guide/channels/push/reporting/)를 확인하세요. 푸시 알림의 경우 발송, 전달, 반송, 열람 및 직접 열람된 메시지 수에 대한 통계를 확인할 수 있습니다.

### 문제 해결 {#troubleshooting}

#### 클릭 시 동작

SDK 버전의 기본 클릭 시 동작을 사용하고 있으며 웹 URL이 포함된 푸시 알림을 선택했을 때 웹 브라우저가 아닌 앱 내에서 열리는 경우, 다음 통합 가이드를 확인하여 푸시 알림 처리를 확인하세요:

- [Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities)
- [Android]({{site.baseurl}}/developer_guide/push_notifications/#android_step-1-register-braze-firebase-messaging-service)

{% alert important %}
앱이 실행을 완료하기 전에, 가급적 `application:didFinishLaunchingWithOptions:`에서 `center.delegate = self`를 사용하여 델리게이트 오브젝트를 동기적으로 할당해야 합니다. 그렇지 않으면 앱이 수신되는 푸시 알림을 놓칠 수 있습니다. 자세한 내용은 Apple의 [`UNUserNotificationCenterDelegate` 설명서](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate)를 참조하세요.
{% endalert %}