---
nav_title: 제거 추적
article_title: 제거 추적
page_order: 1
page_type: reference
description: "이 참조 문서에서는 Campaign 수준 및 앱 수준 통계에 대한 제거 추적 구현에 대해 설명합니다."
tool: Reports

---

# 제거 추적 {#uninstall-tracking}

> 이 문서에서는 시간 경과에 따른 집계된 앱 제거를 확인하여 추세와 이상 징후를 파악하고, Campaign 수준의 제거를 추적하여 특정 Campaign이 앱 설치를 유도하는지 또는 방해하는지 확인하는 방법을 설명합니다.

Braze의 제거 추적은 다음과 같은 세부 정보를 제공합니다:

1. **홈** 페이지의 시계열 그래프에서 일일 앱 수준 제거 통계를 확인할 수 있습니다.
2. 특정 Campaign의 **Campaign Details** 페이지에서 Campaign 수준 제거 통계를 시계열 그래프로 확인할 수 있습니다. 이 통계는 매일 앱을 제거하는 Campaign 수신자 수를 나타냅니다.

{% alert note %}
Braze 대시보드에서 제거 추적을 활성화해야 합니다. 이 기능은 iOS, Android 및 Fire OS의 앱에서 사용할 수 있습니다.
{% endalert %}

## 작동 방식 {#how-it-works}

Braze는 일반 푸시 Campaign에서 기본 수준의 제거 정보를 자동으로 수집합니다. 그러나 사용자마다 푸시 Campaign을 수신하는 빈도가 다를 수 있으므로, 사용자들의 제거 활동에 대한 보다 정확한 스냅샷을 제공하기 위해 제거 추적 기능을 제공합니다.

Braze가 제거를 감지하면 해당 사용자에게 제거됨 태그가 지정됩니다. Campaign에서 **제거하지 않음** 필터를 사용하면 이러한 태그가 지정된 사용자는 제외됩니다. 사용자가 앱을 다시 설치했지만 열지 않은 경우, 제거 태그는 프로필에 그대로 남아 있습니다. 이 태그는 사용자가 다시 설치한 앱에서 새 세션을 시작해야만 제거됩니다. 즉, 앱을 다시 설치했지만 한 번도 열지 않은 사용자는 계속 제거된 상태로 표시됩니다.

제거 추적 사용에 대한 자세한 내용은 블로그 게시물 [제거 추적: 장점과 한계에 대한 업계 시각](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/)을 참조하세요.

## 제거 추적 활성화 {#turning-on-uninstall-tracking}

**Settings**의 **App Settings** 페이지에서 추적하려는 각 앱에 대해 제거 추적을 활성화할 수 있습니다.

앱에 대해 제거 추적을 활성화하면, Braze는 24시간 이내에 세션을 기록하지 않았거나 푸시를 수신하지 않은 사용자에게 매일 밤 백그라운드 푸시 메시지를 전송합니다.

### 구성 {#configuration}

iOS 애플리케이션의 제거 추적을 구성하려면 [유틸리티 메서드]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls?sdktab=swift)를 사용하세요. Android 애플리케이션의 경우 [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html)를 사용하세요. Braze가 제거 추적 또는 일반 푸시 Campaign 전달을 통해 제거를 감지하면, 제거가 발생한 최적의 추정 시간을 사용자 프로필에 기록합니다. 이 시간은 고객 프로필에 표준 속성으로 저장되며, 윈백 Campaign을 위한 사용자 Segment를 정의하는 데 사용할 수 있습니다.

## 제거를 기준으로 Segments 필터링 {#filtering-segments-by-uninstalls}

**제거됨** 필터는 특정 기간 내에 앱을 제거한 사용자를 선택합니다. 제거가 발생한 정확한 시점을 파악하기 어렵기 때문에, 제거 필터에는 더 넓은 기간 범위를 설정하여 제거한 모든 사용자가 어느 시점에서든 Segment에 포함되도록 하는 것이 좋습니다.

제거에 대한 일별 통계는 **홈** 페이지에서 확인할 수 있습니다.

![제거 Segment.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

이 그래프는 Braze에서 제공하는 다른 통계와 마찬가지로 앱별 및 Segment별로 분류할 수 있습니다. **성능 개요** 섹션에서 날짜 범위를 선택하고, 필요한 경우 앱을 선택합니다. 그런 다음 **시간대별 성능** 그래프로 스크롤하여 다음을 수행합니다:

1. **통계 대상** 드롭다운에서 **제거**를 선택합니다.
2. **분류** 드롭다운에서 **Segment별**을 선택합니다.
3. **분류 값** 드롭다운에서 그래프에 포함할 Segments를 선택합니다.

{% alert note %}
제거 추적이 활성화되지 않은 앱은 전체 사용자 중 일부(푸시 알림 대상으로 지정된 사용자)만의 제거 데이터를 보고하므로, 실제 일별 제거 합계는 표시되는 수치보다 높을 수 있습니다.
{% endalert %}

## Campaigns의 제거 추적 {#uninstall-tracking-for-campaigns}

Campaign 제거 추적은 특정 Campaign을 수신한 후 선택한 기간 내에 앱을 제거한 사용자 수를 보여줍니다. 이 도구는 Campaign이 의도치 않은 부정적인 사용자 행동을 유발하고 있는지에 대한 인사이트를 제공하고, 전반적인 Campaign 효과를 측정하는 데 도움이 됩니다.

Campaigns의 제거 추적 통계는 특정 Campaign의 **Campaign Analytics** 페이지에서 확인할 수 있습니다. 멀티채널 및 다변량 Campaigns의 경우, 제거 수를 각각 채널별 및 배리언트별로 분류할 수 있습니다.

![Campaign 수준의 제거 추적.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### 작동 방식

Braze는 사용자의 기기로 전송된 푸시 메시지가 Firebase Cloud Messaging(FCM) 또는 Apple Push Notification Service(APNs)로부터 앱이 더 이상 설치되어 있지 않다는 신호를 반환할 때 제거를 추적합니다. 앱에 대해 글로벌 제거 추적을 활성화하면, Braze는 사용자가 앱을 제거했는지 감지하기 위해 매일 무음 푸시 메시지를 전송합니다. Braze는 이 "무음" 푸시를 모든 사용자에게 전송하며(사용자가 앱 설정에서 무음 푸시를 비활성화하지 않은 경우), 이 푸시는 사용자에게 표시되지 않습니다. Braze가 사용자의 앱 제거를 감지하면 다음과 같이 처리합니다:

* 앱의 총 제거 수를 1 증가시킵니다.
* 해당 사용자가 지난 24시간 동안 성공적으로 수신한 모든 Campaign의 제거 수를 1 증가시킵니다.
* 사용자가 24시간 내에 세 개의 Campaign을 수신한 후 앱을 제거하면, 세 Campaign 모두의 "제거" 수를 증가시킵니다.

FCM과 APNs는 제거 추적에 제한을 두고 있습니다. Braze는 FCM 또는 APNs가 사용자의 앱 제거를 알려줄 때만 제거 수를 증가시키지만, 이러한 서드파티 시스템은 언제든지 제거를 통지할 수 있습니다. 정확한 통계보다는 방향적 추세를 감지하기 위해 제거 추적을 사용하세요.

Braze는 FCM이 `DEVICE_UNREGISTERED` 또는 `NotRegistered`와 같이 등록 토큰이 더 이상 유효하지 않다고 보고할 때 FCM 응답을 토큰 제거(제거) 응답으로 처리합니다. Braze는 다른 푸시 오류를 토큰을 제거하지 않고 반송으로 기록합니다.

제거 추적 사용에 대한 자세한 내용은 블로그 게시물 [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/)을 참조하세요.

## 문제 해결 {#troubleshooting}

### 사용자 프로필이 제거됨으로 표시되는 시점은 언제인가요? 제거 태그는 언제 해제되나요? {#when-is-a-users-profile-flagged-as-uninstalled-when-is-the-uninstall-tag-cleared}

Braze는 기기에 앱이 더 이상 설치되어 있지 않음을 감지하면 해당 사용자를 제거된 것으로 표시합니다(일반 푸시 및 선택적 제거 추적을 통한 감지 방법은 [작동 방식](#how-it-works)을 참조하세요). 사용자가 앱을 재설치한 후에도 **앱을 열고 새 세션을 시작**할 때까지 제거 태그가 프로필에 남아 있을 수 있습니다. 단순히 재설치하는 것만으로는 태그가 해제되지 않습니다. 해당 세션이 시작되기 전까지, 제거 상태를 사용하는 Segments 및 필터(예: **Has Not Uninstalled**)는 해당 사용자를 여전히 제거된 것으로 처리합니다.

### 갑자기 제거 수가 급증하는 이유는 무엇인가요? {#why-am-i-suddenly-seeing-a-spike-in-uninstalls}

앱 제거 수가 급증하는 경우, Firebase Cloud Messaging(FCM) 및 Apple Push Notification Service(APNS)가 오래된 토큰을 다른 빈도로 취소하기 때문일 수 있습니다.

{% alert note %}
개인정보 보호를 위해 Braze의 푸시 공급자가 불규칙한 간격으로 토큰을 취소할 수 있으며, 이로 인해 특정 기간에 제거 수가 급증할 수 있습니다.<br><br>이러한 변화를 검증하려면 제거 추적과 함께 직접 푸시 열람율과 같은 사용자 행동 측정기준을 모니터링하세요. 제거 수는 급격히 증가하지만 직접 푸시 열람이 안정적으로 유지된다면, 이 급증은 실제 사용자 행동이 아니라 파트너가 오래된 토큰을 취소한 것일 가능성이 높습니다.
{% endalert %}

### 특정 Campaign이 제거를 유발했는지 어떻게 확인하나요? {#how-do-i-determine-if-a-specific-campaign-caused-uninstalls}

제거 급증이 발생한 시점과 같은 시간대에 메시지를 발송한 Campaigns의 분석을 확인하세요. 특정 메시지가 제거 증가와 상관관계가 있다면, 해당 메시지가 사용자의 제거에 영향을 미치고 있을 수 있습니다.

Segment별 제거를 확인하려면 다음과 같이 하세요:
1. 대시보드의 **홈** 페이지로 이동합니다.
2. **시간별 성능** 섹션에서 **통계 항목**으로 **제거**를, **분류 기준**으로 **Segment별**을 선택합니다.

[분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)이 활성화된 상태에서 휴면 사용자를 추적하는 Segment가 있다면, 해당 Segment의 제거 추세를 전체 앱 추세와 비교해 보세요.

### 제거가 실제인지 어떻게 확인하나요? {#how-do-i-confirm-uninstalls-are-genuine}

APNs의 경우, 고객 프로필에서 `BadDeviceToken` 푸시 오류를 확인하세요. 제거 급증과 같은 시간대에 이 오류가 대량으로 나타나면, 해당 제거는 실제일 가능성이 높습니다. `BadDeviceToken`은 기기의 푸시 토큰이 더 이상 유효하지 않음을 나타내며, 이는 일반적으로 앱이 제거되었을 때 발생합니다.

### 앱 제거 수가 APNs의 수치와 다른 이유는 무엇인가요? {#why-are-the-number-of-app-uninstalls-different-from-whats-in-apns}

이 차이는 예상된 것입니다.

Apple은 푸시 토큰이 무효화되었을 때 보고를 지연하기 위해 무작위 스케줄을 사용합니다. 이는 사용자가 앱을 제거한 후에도 APNs가 일정 기간 동안 푸시 알림에 대해 성공 응답을 계속 반환할 수 있음을 의미합니다. 이 지연은 의도적이며 사용자 개인정보를 보호하기 위해 설계되었습니다. APNs가 무효 토큰에 대해 `410` 상태를 반환할 때까지 바운스나 실패가 보고되지 않습니다.

### 제거 추적은 무음 또는 백그라운드 푸시와 어떤 관련이 있나요? {#how-does-uninstall-tracking-relate-to-silent-or-background-push}

제거 감지에는 사용자에게 표시되는 알림으로 나타나지 않는 낮은 우선순위의 백그라운드 푸시를 사용할 수 있습니다. 이러한 푸시는 표준 메시징 분석에서 Campaign [**발송**]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics)과는 별도입니다. 제거 추세를 분석할 때는 제거 추적 푸시를 마케팅 발송 총계와 직접 비교하기보다, 제거 차트를 푸시 인게이지먼트 측정기준과 함께 검토하세요.