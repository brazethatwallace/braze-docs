---
page_order: 22
nav_title: 모범 사례
article_title: 푸시 모범 사례
description: "이 페이지에서는 푸시 메시지가 불쾌감이 아닌 참여를 유도할 수 있도록 푸시 모범 사례와 사용 사례를 안내합니다."
channel: push
---

# 푸시 모범 사례 {#push-best-practices}

> 이 페이지에서는 푸시 메시지가 불쾌감이 아닌 참여를 유도할 수 있도록 푸시 모범 사례와 사용 사례를 안내합니다.

푸시 알림은 앱 사용자와 소통하기 위한 강력한 도구이지만, 적시에 관련성 있는 메시지를 전달하기 위해 신중하게 사용해야 합니다. 푸시 메시지를 발송하기 전에 다음 모범 사례를 참고하여 알아두고 확인해야 할 사항을 점검하세요.

{% alert important %}
푸시 메시지는 Apple App Store 및 Google Play Store 정책의 가이드라인을 준수해야 하며, 특히 푸시 메시지를 광고, 스팸, 프로모션 등으로 사용하는 것에 관한 규정을 따라야 합니다. 이 페이지의 [푸시 메시지 규정](#push-message-regulations)을 참조하세요.
{% endalert %}

## 푸시 메시지 작성 {#compose-your-push-message}

모범 사례로서, Braze는 모바일 푸시 알림에서 선택적 제목과 메시지 본문 모두 각 줄의 텍스트를 약 30~40자로 유지할 것을 권장합니다. 작성기의 글자 수 카운터는 Liquid 문자를 고려하지 않습니다. 즉, 메시지의 최종 글자 수는 각 사용자에 대해 Liquid가 렌더링되는 방식에 따라 달라집니다. 확실하지 않을 때는 짧고 간결하게 작성하세요.

## 푸시 알림 페이로드 크기 줄이기 {#reduce-push-notification-payload-size}

최대 페이로드 크기는 플랫폼에 따라 다릅니다.

| 플랫폼 | 최대 페이로드 크기 |
| --- | --- |
| 웹 | 3,807바이트 |
| Android | 3,930바이트 |
| iOS | 3,960바이트 |
| Kindle | 5,985바이트 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 알림 페이로드 크기 줄이기" }

푸시가 최대 페이로드 크기를 초과하면 메시지가 발송되지 않을 수 있습니다. 모범 사례로서, 페이로드를 수백 바이트 이내로 유지하세요.

### 푸시 페이로드란? {#what-is-a-push-payload}

푸시 서비스 제공업체는 전체 푸시 페이로드의 바이트 크기를 확인하여 사용자에게 푸시 알림을 표시할 수 있는지 판단합니다. 페이로드는 다음을 포함한 대부분의 푸시 서비스에서 **4KB(4,096바이트)**로 제한됩니다:

- Apple Push Notification service(APNs)
- Android의 Firebase Cloud Messaging(FCM)
- 웹 푸시
- Huawei 푸시

이러한 푸시 서비스는 이 제한을 초과하는 알림을 거부합니다.

Braze는 통합 및 분석 목적으로 푸시 페이로드의 일부를 예약합니다. 이를 고려하여 최대 페이로드 크기는 **3,807바이트**입니다. 푸시가 이 크기를 초과하면 메시지가 발송되지 않을 수 있습니다. 모범 사례로서, 페이로드를 수백 바이트 이내로 유지하세요.

푸시에서 다음 요소들이 푸시 페이로드를 구성합니다:

- 제목 및 메시지 본문과 같은 텍스트
- Liquid 개인화의 최종 렌더링
- 이미지 URL(이미지 자체의 크기는 아님)
- 클릭 대상 URL
- 버튼 이름
- 키-값 페어

### 페이로드 크기를 줄이기 위한 팁 {#tips-to-reduce-payload-size}

페이로드 크기를 줄이려면:

- 메시지를 간결하게 유지하세요. 일반적인 가이드라인으로 40자 이내에서 실행 가능하고 유용한 내용을 담으세요.
- 텍스트에서 불필요한 공백과 줄바꿈을 제거하세요.
- 발송 시 Liquid가 어떻게 렌더링될지 고려하세요. Liquid 개인화의 최종 렌더링은 사용자마다 다르기 때문에, Liquid가 포함된 경우 Braze는 푸시 페이로드가 크기 제한을 초과할지 여부를 판단할 수 없습니다. Liquid가 짧은 메시지를 렌더링하면 문제가 없을 수 있습니다. 그러나 Liquid가 긴 메시지를 생성하면 푸시가 페이로드 크기 제한을 초과할 수 있습니다. 사용자에게 발송하기 전에 항상 실제 기기에서 푸시 메시지를 테스트하세요.
- URL 단축기를 사용하여 URL을 줄이는 것을 고려하세요.

## 타겟팅 최적화 {#optimize-targeting}

### 관련 사용자 데이터 수집 {#collect-relevant-user-data}

푸시 알림은 적시에 관련성 있는 알림으로 사용자를 타겟팅하기 위해 신중하게 다뤄야 합니다. Braze는 관련 세그먼트를 타겟팅하는 데 사용할 수 있는 유용한 기기 및 사용 정보를 수집합니다. 이 정보는 앱에 특화된 커스텀 이벤트 및 속성으로 보완되어야 합니다. 이 데이터를 활용하면 메시지를 신중하게 타겟팅하여 열람률을 높이고 사용자가 푸시를 비활성화하는 경우를 줄일 수 있습니다.

### 알림 설정 페이지 만들기 {#create-a-notification-settings-page}

앱에 설정 페이지를 만들어 사용자가 수신하고 싶은 알림을 직접 선택할 수 있도록 할 수 있습니다. 일반적인 접근 방식은 앱 설정 상태에 해당하는 부울 커스텀 속성을 Braze에 생성하는 것입니다. 예를 들어, 뉴스 앱은 속보, 스포츠 뉴스 또는 정치에 대한 구독 설정을 가질 수 있습니다.

뉴스 앱이 정치에 관심 있는 사용자만 타겟팅하는 Campaign을 만들고 싶을 때, Segment에 `Subscribes to Politics` 속성 필터를 추가합니다. true로 설정하면 알림을 구독한 사용자만 알림을 수신합니다.

커스텀 속성 설정에 대한 자세한 내용은 [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes#setting-custom-attributes) 또는 [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data#user-attributes-object-specification) 문서를 참조하세요.

## 옵트인 및 관련성 높이기 {#increase-opt-ins-and-relevance}

### 사용자 권한 획득 {#obtain-user-permission}

푸시 활성화에 대한 일반 통계는 사용자가 운영체제에서 알림을 승인했는지 여부와 관련됩니다. iOS에서 사용자가 알림을 끄면 Apple이 푸시 토큰 전송을 허용하지 않으므로 시스템에서 자동으로 제거됩니다.

Android 13 이상에서는 푸시 알림을 표시하기 전에 권한을 획득해야 합니다. 이전 버전의 Android에서는 기본적으로 사용자가 알림에 구독됩니다.

### 푸시를 위한 사전 안내 {#prime-users-for-push}

사용자에게 푸시 권한을 요청할 기회는 한 번뿐이며, 거부한 후에는 기기 설정에서 푸시를 다시 활성화하도록 설득하기가 매우 어렵습니다. 이러한 이유로 시스템 프롬프트를 표시하기 전에 인앱 메시지를 사용하여 사용자에게 푸시에 대해 사전 안내해야 합니다. 옵트인을 높이는 방법에 대해 자세히 알아보려면 [푸시 프라이머 인앱 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)를 참조하세요.

### 푸시 구독 제어 추가 {#add-push-subscription-controls}

사용자가 기기 수준에서 알림을 끄면 포그라운드 푸시 토큰이 완전히 제거되므로, 이를 방지하기 위해 사용자가 앱 내에서 직접 푸시 구독을 제어할 수 있도록 하세요. 자세한 내용은 [푸시 구독 상태 업데이트]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#update-push-subscription-state)를 참조하세요.

### 고급 스케줄링 사용 또는 지연 추가 {#use-advanced-scheduling-or-add-delays}

오디언스 규모와 푸시 메시지가 얼마나 미리 스케줄되었는지에 따라 푸시 전달에 지연이 발생할 수 있습니다. 푸시 발송에 걸리는 시간은 할당된 처리 능력에 따라 달라집니다. 예를 들어, 푸시 메시지가 여러 연결된 콘텐츠 호출을 사용하는 경우 푸시 메시지 템플릿 작성의 복잡성이 증가하여 서드파티 API가 데이터를 반환하는 속도에 의해 속도가 제한될 수 있습니다.

더 작은 푸시 페이로드와 더 높은 알림 우선순위는 지연을 줄이고 메시지를 확장하는 데 도움이 됩니다. 오디언스 필터에 `Push Enabled = true`를 추가하여 오디언스 규모를 줄이면 푸시가 활성화된 사용자만 Campaign 발송에 대해 처리됩니다.

또한 필요한 데이터를 최적화하여 API 호출 수를 최소화하는 것을 권장합니다. 가능하다면 여러 번 호출하는 대신 한 번의 API 호출로 필요한 모든 데이터를 가져오세요.

### 푸시 구독 상태 이해 {#understand-push-subscription-states}

푸시 구독 상태는 푸시가 전달된다는 것을 보장하지 않습니다. 사용자가 알림을 수신하려면 푸시가 활성화되어 있어야 합니다. 이는 사용자 프로필에 서로 다른 포그라운드 푸시 권한을 가진 여러 기기가 있을 수 있지만 푸시 구독 상태는 하나뿐이기 때문입니다.

사용자가 앱에 대한 유효한 포그라운드 푸시 토큰이 없는 경우(즉, 설정에서 기기 수준으로 푸시 토큰을 끄고 알림 수신을 거부한 경우), 해당 구독 상태는 여전히 푸시에 대해 `subscribed`로 간주될 수 있습니다. 그러나 포그라운드 푸시 토큰이 유효하지 않으므로 이 사용자는 Braze에서 `Foreground Push Enabled for App`이 아닙니다.

또한 사용자 프로필에 다른 앱에 대한 유효하거나 등록된 푸시 토큰이 없는 경우, 세분화에서 `Foreground Push Enabled` 필터도 false가 됩니다.

## 무반응 사용자에 대한 일몰 정책 구현 {#implement-a-sunset-policy-for-unresponsive-users}

관련성 있고 적시에 푸시 알림을 보내더라도 일부 사용자는 여전히 무반응이거나 스팸으로 느낄 수 있습니다. 사용자가 푸시 알림을 반복적으로 무시하는 이력을 보인다면, 앱의 커뮤니케이션에 짜증을 내거나 앱을 완전히 삭제하기 전에 푸시 발송을 중단하는 것이 좋습니다.

이를 위해 오랫동안 직접 열람 또는 영향받은 열람이 없는 사용자에게 결국 푸시 알림 발송을 중단하는 [일몰 정책]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies)을 만드세요.

1. 직접 열람 또는 영향받은 열람을 기준으로 무반응 사용자를 식별합니다.
2. 해당 사용자에게 점진적으로 푸시 알림 발송을 중단합니다.
3. 푸시 알림을 완전히 제거하기 전에, 더 이상 푸시를 수신하지 않는 이유를 설명하는 마지막 알림을 전달합니다. 이를 통해 사용자가 해당 알림을 열어 지속적인 푸시 수신에 대한 관심을 표현할 기회를 제공합니다.
4. 일몰 정책이 적용된 후, [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages)를 사용하여 이러한 사용자에게 더 이상 푸시를 수신하지 않지만 인앱 메시징 채널을 통해 흥미롭고 유용한 정보를 계속 전달받을 수 있음을 알려주세요.

원래 옵트인한 사용자에게 푸시 발송을 중단하는 것이 꺼려질 수 있지만, 다른 메시징 채널이 이러한 사용자에게 더 효과적으로 도달할 수 있다는 점을 기억하세요. 특히 이전에 푸시를 무시한 경우에는 더욱 그렇습니다. 사용자가 이메일을 열어본다면 이메일 Campaign이 앱 외부에서 도달하는 좋은 방법입니다. 그렇지 않다면 인앱 메시지가 사용자의 앱 삭제 위험 없이 콘텐츠를 전달하는 가장 좋은 방법입니다.

## 앱 열기에 대한 전환 이벤트 설정 {#set-conversion-events-for-app-opens}

푸시 Campaign에 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 할당할 때, Campaign 수신 후 일정 기간 동안의 앱 열기를 추적할 수 있습니다. 앱 열기에 대한 전환 이벤트를 설정하면 푸시 Campaign 후 일반적으로 받는 결과 통계와는 다른 인사이트를 제공합니다.

모든 푸시 Campaign 결과는 메시지의 직접 열람과 열람(직접 열람 및 [영향받은 열람]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens) 모두 포함)을 분류하지만, 전환 추적은 직접이든 영향받은 것이든 모든 유형의 열람을 추적합니다.

또한 "앱 열기" 전환 이벤트를 사용하면 해당 전환 기한(예: 3일) 이전에 발생하는 앱 열기를 추적합니다. 이는 영향받은 열람과 다릅니다. 영향받은 열람을 등록하기 위한 시간은 각 사용자의 과거 참여 행동에 따라 사람마다 다를 수 있기 때문입니다.

## 푸시 메시지 규정 {#push-message-regulations}

푸시 메시지는 고객의 휴대폰이나 브라우저로 직접 전달되는 침투적인 유형의 메시징이므로, 앱과 사이트를 통해 푸시 메시지를 발송하기 위한 가이드라인이 있습니다.

### 앱에 대한 모바일 푸시 규정 {#mobile-push-regulations-for-apps}

| Apple App Store 정책 |
| --- |
| [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) 허용되지 않음: (i) App Store와 유사하거나 일반적인 관심 컬렉션으로 서드파티 앱, 확장 프로그램 또는 플러그인을 표시하기 위한 인터페이스를 만드는 것. |
| [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) 푸시 알림은 앱 기능에 필수적이어서는 안 되며, 민감한 개인 정보나 기밀 정보를 전송하는 데 사용해서는 안 됩니다. 앱의 UI에 표시된 동의 문구를 통해 고객이 명시적으로 수신에 옵트인하고, 앱에서 이러한 메시지 수신을 거부할 수 있는 방법을 제공하지 않는 한, 푸시 알림은 프로모션이나 직접 마케팅 목적으로 사용해서는 안 됩니다. |
| [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) 푸시 알림, 카메라 또는 자이로스코프와 같은 하드웨어 또는 운영체제에서 제공하는 내장 기능이나, Apple Music 접근, iCloud 저장소 또는 Screen Time API와 같은 Apple 서비스 및 기술을 수익화해서는 안 됩니다. |
{: .reset-td-br-1 aria-label="앱에 대한 모바일 푸시 규정" }

| Google Play Store 정책 |
| --- |
| [시스템 기능의 무단 사용 또는 모방](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) 알림이나 경고와 같은 시스템 기능을 모방하거나 방해하는 앱이나 광고는 허용되지 않습니다. 시스템 수준 알림은 항공사 앱이 특별 할인을 알리거나 게임이 인게임 프로모션을 알리는 것과 같이 앱의 핵심 기능에만 사용할 수 있습니다. |
{: .reset-td-br-1 aria-label="앱에 대한 모바일 푸시 규정" }

## 관련 문서 {#related-articles}

찾고 있는 내용을 찾지 못하셨나요? 다음 추가 모범 사례 문서를 확인하세요:

- [푸시 메시지 및 이미지 형식]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [푸시 프라이머 인앱 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)
- [중국 Android 기기의 전달 가능성]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability)
- [발송 전 알아두기: 채널]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)