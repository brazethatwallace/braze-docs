---
nav_title: "고급 푸시 Campaign 설정"
article_title: "고급 푸시 Campaign 설정"
page_order: 5
page_layout: reference
description: "이 참조 문서에서는 우선순위, 커스텀 URL, 전달 옵션 등 고급 Android 푸시 Campaign 설정에 대해 설명합니다."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# 고급 푸시 Campaign 설정 {#advanced-push-campaign-settings}

> Braze 대시보드를 통해 전송되는 Android 및 Fire OS 푸시 알림에는 다양한 고급 설정이 있습니다. 이 문서에서는 이러한 기능과 성공적으로 사용하는 방법을 설명합니다.

## 알림 ID {#notification-id}

알림 ID는 사용자가 선택한 메시지 카테고리의 고유 식별자로, 메시징 서비스에 해당 ID의 가장 최근 메시지만 유지하도록 지시합니다. 알림 ID를 설정하면 오래되고 관련 없는 메시지가 쌓이는 대신 가장 최근의 관련 메시지만 전송할 수 있습니다.

알림 ID를 할당하려면 업데이트할 푸시의 작성 페이지로 이동하여 **설정** 탭을 선택한 다음 **Notification ID** 섹션에 정수를 입력합니다. 이 알림을 발행한 후 업데이트하려면 이전에 사용한 것과 동일한 ID로 다른 알림을 전송합니다.

![알림 ID 필드.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## 유지 시간(TTL) {#ttl}

**Time to Live** 필드를 사용하면 푸시 메시징 서비스에 메시지를 저장하는 커스텀 기간을 설정할 수 있습니다. 기기가 TTL을 초과하여 오프라인 상태를 유지하면 메시지가 만료되어 전달되지 않습니다.

Android 푸시의 유지 시간을 편집하려면 작성기로 이동하여 **설정** 탭을 선택합니다. **Time to Live** 필드를 찾아 일, 시간 또는 초 단위로 값을 입력합니다.

유지 시간의 기본값은 관리자가 [푸시 설정]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings) 페이지에서 정의합니다. 기본적으로 Braze는 각 푸시 메시징 서비스의 최대값으로 푸시 TTL을 설정합니다. 기본 TTL 설정은 전역적으로 적용되지만, Campaign 생성 시 메시지 수준에서 재정의할 수 있습니다. 이는 Campaign마다 긴급도나 전달 기간이 다를 때 유용합니다.

예를 들어, 앱에서 주간 퀴즈 대회를 진행한다고 가정해 보겠습니다. 대회 시작 1시간 전에 푸시 알림을 전송합니다. TTL을 1시간으로 설정하면 대회가 시작된 후 앱을 여는 사용자에게 이미 시작된 이벤트에 대한 알림이 전달되지 않습니다.

{% details 모범 사례 %}

### 짧은 TTL을 사용해야 하는 경우 {#when-to-use-shorter-ttl}

짧은 TTL은 빠르게 관련성을 잃는 이벤트나 프로모션에 대해 사용자가 적시에 알림을 받을 수 있도록 합니다. 예를 들어:

- **리테일:** 2시간 후 종료되는 플래시 세일에 대한 푸시 전송(TTL: 1~2시간)
- **음식 배달:** 주문이 근처에 도착했을 때 사용자에게 알림(TTL: 10~15분)
- **교통 앱:** 차량 도착 업데이트 공유(TTL: 몇 분)
- **이벤트 리마인더:** 웨비나가 곧 시작될 때 사용자에게 알림(TTL: 1시간 미만)

### 짧은 TTL을 피해야 하는 경우 {#when-to-avoid-shorter-ttl}

- Campaign 메시지가 며칠 또는 몇 주 동안 관련성을 유지하는 경우(예: 구독 갱신 리마인더 또는 진행 중인 프로모션).
- 긴급성보다 도달 범위를 극대화하는 것이 더 중요한 경우(예: 앱 업데이트 공지 또는 기능 프로모션).

{% enddetails %}

## Firebase 메시징 전달 우선순위 {#fcm-priority}

**Firebase Messaging Delivery Priority** 필드를 사용하면 Firebase Cloud Messaging으로 푸시를 "일반" 또는 "높음" 우선순위로 전송할지 제어할 수 있습니다. 이 설정은 메시지가 얼마나 빠르게 전달되는지와 기기 배터리 수명에 미치는 영향을 결정합니다.

| 우선순위 | 설명 | 적합한 용도 |
|---------|-------------|----------|
| 일반 | 배터리를 절약하기 위해 전달이 지연될 수 있는 배터리 최적화 전달 | 긴급하지 않은 콘텐츠, 프로모션 제안, 뉴스 업데이트 |
| 높음 | 배터리 소모가 높은 즉시 전달 | 시간에 민감한 알림, 중요 알림, 라이브 이벤트 업데이트, 계정 알림, 속보, 긴급 리마인더 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Firebase 메시징 전달 우선순위" }

### 고려 사항 {#considerations}

- **기본 설정**: [푸시 설정]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings)에서 모든 Android Campaign에 대한 기본 FCM 우선순위를 설정할 수 있습니다. 이 Campaign 수준 설정은 필요한 경우 기본값을 재정의합니다.
- **우선순위 하향 조정**: FCM이 앱에서 사용자에게 표시되는 알림이나 사용자 참여로 이어지지 않는 높은 우선순위 메시지를 자주 전송하는 것을 감지하면, 해당 메시지가 자동으로 일반 우선순위로 하향 조정될 수 있습니다.
- **배터리 영향**: 높은 우선순위 메시지는 절전 모드의 기기를 더 적극적으로 깨우고 더 많은 배터리를 소모합니다. 이 우선순위는 신중하게 사용하세요.

메시지 처리 및 우선순위 하향 조정에 대한 자세한 내용은 [FCM 문서](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) 및 [Android에서의 메시지 처리 및 우선순위 하향 조정](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize)을 참조하세요.

## 요약 텍스트 {#summary-text}

요약 텍스트를 사용하면 확장된 알림 보기에서 추가 텍스트를 설정할 수 있습니다. 또한 이미지가 포함된 알림의 캡션 역할도 합니다.

![제목이 "This is the title for the notification."이고 요약 텍스트가 "This is the summary text for the notification."인 Android 메시지]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

요약 텍스트는 확장된 보기에서 메시지 본문 아래에 표시됩니다.

![제목이 "This is the title for the notification."이고 요약 텍스트가 "This is the summary text for the notification."인 Android 메시지]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

이미지가 포함된 푸시 알림의 경우, 축소된 보기에서는 메시지 텍스트가 표시되고, 알림이 확장되면 요약 텍스트가 이미지 캡션으로 표시됩니다.

## 커스텀 URI {#custom-uris}

**Custom URI** 기능을 사용하면 알림을 클릭했을 때 이동할 웹 URL 또는 Android 리소스를 지정할 수 있습니다. 커스텀 URI를 지정하지 않으면 알림을 클릭했을 때 사용자가 앱으로 이동합니다. 커스텀 URI를 사용하여 앱 내부로 딥링크하거나 앱 외부에 있는 리소스로 사용자를 안내할 수도 있습니다. 이는 [메시징 API]({{site.baseurl}}/api/endpoints/messaging) 또는 푸시 작성기의 **작성** 탭에서 지정할 수 있습니다.

![커스텀 URI 필드.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## 알림 표시 우선순위 {#notification-display-priority}

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

푸시 알림의 우선순위 수준은 알림 트레이에서 다른 알림 대비 알림이 표시되는 방식에 영향을 줍니다. 또한 전달 속도와 방식에도 영향을 줄 수 있는데, 일반 및 낮은 우선순위 메시지는 배터리 수명을 보존하기 위해 약간 높은 지연 시간으로 전송되거나 일괄 처리될 수 있지만, 높은 우선순위 메시지는 항상 즉시 전송됩니다.

이 기능은 메시지의 중요도나 시간 민감도에 따라 메시지를 구분하는 데 유용합니다. 예를 들어, 위험한 도로 상황에 대한 알림은 높은 우선순위를 받기에 적합하고, 진행 중인 세일에 대한 알림은 낮은 우선순위를 받아야 합니다. 전송하는 알림에 방해가 되는 우선순위가 실제로 필요한지 고려해야 합니다. 사용자의 받은편지함에서 항상 최상위를 차지하거나 다른 활동을 방해하면 부정적인 영향을 줄 수 있습니다.

Android O에서는 알림 우선순위가 알림 채널의 속성이 되었습니다. 개발자와 협력하여 채널 구성 시 우선순위를 정의한 다음, 알림을 전송할 때 대시보드에서 적절한 채널을 선택해야 합니다. Android O 이전 버전을 실행하는 기기의 경우, Braze 대시보드 및 메시징 API를 통해 Android 및 Fire OS 알림의 우선순위 수준을 지정할 수 있습니다.

전체 사용자 기반에 특정 우선순위로 메시지를 보내려면 [알림 채널 구성](https://developer.android.com/training/notify-user/channels#importance)(O+ 기기 대상)을 통해 간접적으로 우선순위를 지정하고, 대시보드에서 개별 우선순위를 전송(&#60;O 기기 대상)하는 것을 권장합니다.

Android 또는 Fire OS 푸시 알림에 설정할 수 있는 우선순위 수준은 다음 표를 참조하세요:

| 우선순위 | 설명 | `priority` 값(API 메시지용) |
|------|-----------|----------------------------|
| 최대 | 긴급하거나 시간에 민감한 메시지. | `2` |
| 높음 | 친구의 새 메시지와 같은 중요한 커뮤니케이션. | `1` |
| 기본값 | 대부분의 알림. 메시지가 다른 우선순위 유형에 명시적으로 해당하지 않는 경우 사용합니다. | `0` |
| 낮음 | 사용자가 알아야 하지만 즉각적인 조치가 필요하지 않은 정보. | `-1`|
| 최소 | 상황별 또는 배경 정보. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="알림 표시 우선순위" }

자세한 내용은 Google의 [Android 알림](http://developer.android.com/design/patterns/notifications.html) 문서를 참조하세요.

## 푸시 카테고리 {#push-category}

Android 푸시 알림은 알림이 미리 정의된 카테고리에 해당하는지 지정하는 옵션을 제공합니다. Android 시스템 UI는 이 카테고리를 사용하여 사용자의 알림 트레이에서 알림을 배치할 위치에 대한 순위 또는 필터링 결정을 내릴 수 있습니다.

![카테고리가 기본 설정인 없음으로 설정된 설정 탭.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| 카테고리 | 설명 |
|---|-------|
| 없음 | 기본 옵션. |
| 알람 | 알람 또는 타이머. |
| 통화 | 수신 전화(음성 또는 영상) 또는 유사한 동기식 통신 요청. |
| 이메일 | 비동기 대량 메시지(이메일). |
| 오류 | 백그라운드 작업 또는 인증 상태의 오류. |
| 이벤트 | 캘린더 이벤트. |
| 메시지 | 수신 다이렉트 메시지(단문 메시지 서비스, 인스턴트 메시지 등). |
| 진행 상황 | 장시간 실행되는 백그라운드 작업의 진행 상황. |
| 프로모션 | 프로모션 또는 광고. |
| 추천 | 단일 항목에 대한 구체적이고 시의적절한 추천. |
| 리마인더 | 사용자가 예약한 리마인더. |
| 서비스 | 실행 중인 백그라운드 서비스 표시. |
| 소셜 | 소셜 네트워크 또는 공유 업데이트. |
| 상태 | 기기 또는 상황별 상태에 대한 지속적인 정보. |
| 시스템 | 시스템 또는 기기 상태 업데이트. 시스템 사용을 위해 예약됨. |
| 전송 | 재생을 위한 미디어 전송 제어. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 카테고리" }

## 푸시 가시성 {#push-visibility}

Android 푸시 알림은 사용자의 잠금 화면에 알림이 표시되는 방식을 결정하는 선택적 필드를 제공합니다. 가시성 옵션과 설명은 다음 표를 참조하세요.

| 가시성 | 설명 |
|---|-----|
| 공개 | 잠금 화면에 알림이 표시됩니다 |
| 비공개 | "콘텐츠 숨김"이라는 메시지와 함께 알림이 표시됩니다 |
| 비밀 | 잠금 화면에 알림이 표시되지 않습니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 가시성" }

또한 Android 사용자는 기기의 알림 개인정보 설정을 변경하여 잠금 화면에 푸시 알림이 표시되는 방식을 재정의할 수 있습니다. 이 설정은 푸시 알림의 가시성을 재정의합니다.

![가시성 설정이 활성화되어 비공개로 설정된 대시보드 푸시 우선순위 위치.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

기기의 알림 개인정보 설정이 **모든 콘텐츠 표시**(기본 설정)인 경우, 가시성에 관계없이 모든 알림이 사용자의 잠금 화면에 표시됩니다. 마찬가지로 알림 개인정보가 **알림 표시 안 함**으로 설정된 경우 잠금 화면에 알림이 표시되지 않습니다. 가시성은 알림 개인정보가 **민감한 콘텐츠 숨기기**로 설정된 경우에만 효과가 있습니다.

가시성은 Android Lollipop 5.0.0 이전 기기에서는 효과가 없으며, 이러한 기기에서는 모든 알림이 표시됩니다.

자세한 내용은 [Android 문서](https://developer.android.com/guide/topics/ui/notifiers/notifications)를 참조하세요.

## 알림 사운드 {#notification-sounds}

Android O에서는 알림 사운드가 알림 채널의 속성이 되었습니다. 개발자와 협력하여 채널 구성 시 사운드를 정의한 다음, 알림을 전송할 때 대시보드에서 적절한 채널을 선택해야 합니다.

Android O 이전 버전을 실행하는 기기의 경우, Braze를 사용하면 대시보드 작성기를 통해 개별 푸시 메시지의 사운드를 설정할 수 있습니다. 기기의 로컬 사운드 리소스를 지정하여 이를 수행할 수 있습니다(예: `android.resource://com.mycompany.myapp/raw/mysound`).

이 필드에서 **Default**를 선택하면 기기의 기본 알림 사운드가 재생됩니다. 이는 [메시징 API]({{site.baseurl}}/api/endpoints/messaging) 또는 푸시 작성기의 **설정**에서 지정할 수 있습니다.

![사운드 필드.]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

다음으로, 대시보드 프롬프트에 전체 사운드 리소스 URI(예: `android.resource://com.mycompany.myapp/raw/mysound`)를 입력합니다.

전체 사용자 기반에 특정 사운드로 메시지를 보내려면 [알림 채널 구성](https://developer.android.com/training/notify-user/channels)(O+ 기기 대상)을 통해 간접적으로 사운드를 지정하고, 대시보드에서 개별 사운드를 전송(&#60;O 기기 대상)하는 것을 권장합니다.