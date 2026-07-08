---
nav_title: 문제 해결
article_title: 푸시 문제 해결
page_order: 5
page_type: reference
description: "푸시 메시징 채널과 관련된 문제에 대한 문제 해결 단계입니다."
channel: push
---

# 푸시 문제 해결 {#troubleshoot-push}

> 이 페이지를 사용하여 푸시 메시징 채널의 문제를 해결하세요.

## 푸시 알림 누락 {#missing-push-notifications}

푸시 알림이 예상대로 도착하지 않는 경우, 다음 항목을 순서대로 확인하세요:

- [푸시 구독 상태](#push-subscription-status)
- [Segment](#segment)
- [푸시 알림 한도](#push-notification-caps)
- [사용량 제한](#rate-limits)
- [대조군 상태](#control-group-status)
- [유효한 푸시 토큰](#valid-push-token)
- [푸시 알림 유형](#push-notification-type)
- [현재 앱](#current-app)

### 푸시 구독 상태 {#push-subscription-status}

푸시는 가입됨 또는 옵트인한 사용자에게만 발송할 수 있습니다. **고객 프로필**에서 [참여]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) 탭을 열고 테스트 중인 워크스페이스에 대해 푸시에 활성 등록되어 있는지 확인하세요. 여러 앱에 등록되어 있는 경우 **Push Registered For**에 목록이 표시됩니다:

![푸시 등록 대상]({% image_buster /assets/img_archive/trouble1.png %})

Braze 내보내기 엔드포인트를 사용하여 고객 프로필을 내보낼 수도 있습니다:

- [식별자별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Segment별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

두 엔드포인트 모두 기기별 푸시 활성화 정보를 포함하는 푸시 토큰 오브젝트를 반환합니다.

### Segment {#segment}

타겟팅하는 Segment에 포함되어 있는지 확인하세요(라이브 Campaign이고 테스트가 아닌 경우). **고객 프로필**에서 사용자가 현재 포함된 Segment 목록을 확인할 수 있습니다. Segment 멤버십은 실시간으로 업데이트됩니다.

![Segment 목록]({% image_buster /assets/img_archive/trouble2.png %})

Segment를 생성할 때 **User Lookup**을 사용하여 사용자가 해당 Segment에 포함되어 있는지 확인할 수도 있습니다. **User Lookup**은 `external_id` 또는 `braze_id`만 허용하며, 이메일 주소나 전화번호는 사용할 수 없습니다. 이메일, 전화번호, 푸시 토큰 또는 사용자 별칭으로 검색하려면 [**사용자 검색**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)을 참조하세요.

![검색 필드가 있는 User Lookup 섹션.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

### 푸시 알림 한도 {#push-notification-caps}

워크스페이스에 글로벌 최대 게재빈도 설정이 적용되어 있는 경우, 해당 기간 동안 한도에 이미 도달하여 푸시를 받지 못했을 수 있습니다. 대시보드에서 [글로벌 최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#freq-cap-feat-over)과 한도를 확인하세요. Campaign이 최대 게재빈도 설정 규칙을 따르는 경우, Campaign 세부 정보에 영향을 받은 사용자 수가 표시됩니다.

![Campaign 세부 정보]({% image_buster /assets/img_archive/trouble3.png %})

### 사용량 제한 {#rate-limits}

Campaign 또는 Canvas에 사용량 제한이 설정되어 있는 경우, 해당 한도를 초과하면 메시지를 받지 못할 수 있습니다. 자세한 내용은 [사용량 제한조치]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#rate-limiting)를 참조하세요.

### 대조군 상태 {#control-group-status}

단일 채널 Campaign이거나 대조군이 있는 Canvas인 경우, 대조군에 포함되었을 수 있습니다.

  1. [배리언트 분배]({{site.baseurl}}/user_guide/messaging/ab_testing#step-5-distribute-users-among-your-variants)를 확인하여 대조군이 있는지 확인하세요.
  2. 대조군이 있는 경우, [Campaign 대조군 포함]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#in-campaign-control-group-filter) 필터로 Segment를 생성한 다음 [Segment를 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#exporting-to-csv)하여 사용자 ID가 목록에 있는지 확인하세요.

### 유효한 푸시 토큰 {#valid-push-token}

푸시 토큰은 발신자가 푸시 알림으로 특정 기기를 타겟팅하는 데 사용하는 식별자입니다. 유효한 푸시 토큰이 없으면 Braze는 해당 기기에 푸시를 보낼 수 없습니다.

Braze는 고객 프로필당 최대 20개의 기기를 저장합니다. 21번째 기기가 등록되면 가장 오래된 기기가 제거됩니다(선입선출, FIFO). SDK에서 [`changeUser()`]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)를 호출하면 현재 기기가 프로필에 다시 등록됩니다.

### 푸시 알림 유형 {#push-notification-type}

타겟팅하는 기기 또는 플랫폼에 맞는 푸시 유형을 사용하세요. 예를 들어, Fire TV를 타겟팅하려면 Android 푸시 Campaign이 아닌 Kindle 푸시 알림을 사용해야 합니다. Android 기기의 경우 iOS 푸시 Campaign이 아닌 Android 푸시 알림을 사용하세요.

플랫폼별 문제 해결 워크플로는 다음을 참조하세요:

- [Apple 푸시 알림 문제 해결]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging 문제 해결]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

### 현재 앱 {#current-app}

내부 사용자를 대상으로 푸시를 테스트할 때, 푸시 알림을 받을 사용자가 올바른 앱에 로그인되어 있는지 확인하세요. 그렇지 않으면 푸시를 받지 못하거나 세분화에 따라 예상하지 못한 푸시를 받을 수 있습니다.

{% alert note %}
Android에서 이미지가 포함된 푸시 메시지를 보내는 경우, FCM이 이미지를 삭제하고 푸시 메시지에 텍스트만 표시하는 경우가 있습니다. 이 문제는 일반적으로 서버 연결 문제로 인해 발생합니다.
{% endalert %}

## 오류: MismatchSenderID {#error-mismatchsenderid}

MismatchSenderID는 Firebase Cloud Messaging(FCM)의 인증 실패를 나타냅니다. Firebase 발신자 ID와 FCM API 키가 올바른지 확인하세요.

올바른 Firebase 서버 키를 찾아 교체하려면:

1. 앱의 Firebase 콘솔로 이동하세요.
2. **Project Overview**에서 **Project Settings**를 선택하세요.
3. **Cloud Messaging** 탭에서 API 키 아래의 발신자 ID가 Braze의 것과 일치하는지 확인하세요(**설정** > **앱 설정** > **Cloud Messaging API Key**).

{% alert warning %}
Braze 대시보드에서 발신자 ID를 변경하지 마세요. 변경하면 기존 푸시 등록이 무효화됩니다. 발신자 ID가 일치하지 않는 경우, 일치하는 발신자 ID가 있는 Firebase 프로젝트를 찾아야 합니다.
{% endalert %}

{:start="4"}
4. **Project credentials** 아래의 **Server Key**를 복사하세요.
5. Braze에서 **설정** > **앱 설정**으로 이동하여 앱을 선택한 다음, **Cloud Messaging API Key** 필드에 서버 키를 붙여넣으세요(기존 키를 교체).
6. **저장**을 선택하세요.
7. 확인을 위해, API 키를 변경하기 전과 후에 앱을 열지 않은 상태에서 기기로 테스트 푸시를 보내세요. 이렇게 하면 새로운 푸시 등록 ID(푸시 토큰)를 생성하지 않아도 사용자가 계속 푸시 알림을 받을 수 있는지 확인할 수 있습니다.

## 문제 해결 시나리오 {#troubleshooting-scenarios}

### 푸시 알림 지연 {#delayed-push-notifications}

다음과 같은 이유로 푸시 알림이 지연될 수 있습니다:

- 기기의 데이터 연결이 약한 경우
- 앱의 커스텀 코드가 Braze 푸시 알림을 억제할 수 있는 경우
- 기기 설정에서 푸시 알림에 대한 사용자 환경설정
- Campaign 또는 Canvas에서 생성 시 푸시의 메시지 우선순위
- 푸시 서비스 제공업체(FCM 및 APNs)의 트래픽 지연 또는 문제

### 푸시 알림이 예상보다 느리게 발송됨 {#push-notifications-are-sending-slower-than-expected}

푸시 알림 설정이 다음 모범 사례를 따르고 있는지 확인하세요:

- 푸시 활성화 상태를 고려하지 않고 대규모 오디언스에 발송하는 경우, 발송 속도가 느려질 수 있습니다. 대신 푸시 활성화된 사용자에게만 발송하여 오디언스 규모를 줄이는 것을 고려하세요.
- 가능하면 Campaign을 즉시 발송하는 대신 미리 스케줄하세요.
- Canvas에서 더 많은 수의 사용자에게 푸시 알림을 타겟팅하는 경우, Canvas의 후속 메시지 단계가 사용자에게 즉시 발송하는 Campaign과 다른 처리 시간이 필요할 수 있습니다. 이 경우 Campaign이 일반적으로 Canvas보다 먼저 발송을 완료합니다. Canvas의 첫 번째 "단계"는 사용자가 특정 사용자 여정에 적합한지 확인하는 것이기 때문입니다.

## 푸시 알림을 클릭해도 앱이 열리지 않음 {#clicking-a-push-notification-doesnt-open-the-app}

푸시 알림을 클릭해도 앱이 열리지 않는 경우, 플랫폼에 따라 다음 사항을 확인하세요.

### Android

1. **클릭 시 동작 확인:** Campaign이 클릭 시 앱을 열도록 구성되어 있는지 확인하세요.
2. **딥링크 처리 확인:** `braze.xml` 파일에서 `com_braze_handle_push_deep_links_automatically`가 `true`로 설정되어 있는지 `false`로 설정되어 있는지 확인하세요.
   - `true`로 설정된 경우, Braze SDK가 딥링크를 직접 처리하며 앱이 정상적으로 열려야 합니다.
   - `false`로 설정된 경우, 앱에서 푸시 수신 및 열기 의도를 수신하고 처리할 방송 수신기가 필요합니다. 이 수신기가 올바르게 구현되어 있는지 확인하세요.
3. **상세 로그 수집:** [상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)하고, 문제를 재현한 다음, `braze.xml` 및 `AndroidManifest.xml`과 함께 로그를 Braze 고객지원에 제공하세요.

### iOS

1. **클릭 시 동작 확인:** Campaign이 클릭 시 앱을 열도록 구성되어 있는지 확인하세요.
2. **푸시 통합 확인:** 푸시에서 앱으로의 딥링킹은 Braze [표준 푸시 통합]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)에 의해 자동으로 처리됩니다. 커스텀 델리게이트 처리를 포함하여 통합이 올바르게 구현되어 있는지 확인하세요.
3. **상세 로그 수집:** [상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)하고, 문제를 재현한 다음, 로그를 Braze 고객지원에 제공하세요.

## 푸시 클릭 시 예기치 않게 앱에서 열림 {#push-clicks-unexpectedly-open-in-app}

푸시 알림의 링크가 웹 브라우저 대신 앱에서 예기치 않게 열리는 문제가 발생하는 경우, Campaign 구성 또는 SDK 구현에 문제가 있을 수 있습니다. 다음 단계를 참조하세요.

### 클릭 시 동작 확인 {#verify-on-click-behavior}

Campaign 또는 캔버스 단계에서 **Open web URL inside mobile app**이 선택되어 있지 않은지 다시 확인하세요. 선택되어 있다면 선택을 해제하고 다시 시작하세요.

![푸시 구성의 "클릭 시 동작" 필드가 "Open web URL"로 설정되어 있고 "Open web URL inside mobile app"이 선택 해제된 상태.]({% image_buster /assets/img/push_on_click.png %})

클릭 시 동작 "Open web URL"의 기본 상호작용은 SDK 버전에 따라 다릅니다. SDK 버전 iOS 2.29.0 및 Android 2.0.0 이상에서는 이 옵션이 기본적으로 선택되어 있으며 웹 URL이 앱 내 웹뷰에서 열립니다. 이전 버전에서는 이 옵션이 기본적으로 해제되어 있으며 웹 URL이 기기의 기본 웹 브라우저에서 열립니다.

이것이 문제가 아닌 경우, 푸시 구현에 문제가 있을 수 있습니다.

### 푸시 통합 재확인 {#double-check-push-integration}

푸시 알림의 링크가 예기치 않게 앱에서 열리는 경우, 푸시 알림 통합 또는 커스터마이징 설정에 문제가 있을 수 있습니다. 다음 단계에 따라 문제를 해결하세요:

1. **푸시 델리게이트 구현 검토:** Braze 푸시 델리게이트가 올바르게 구현되어 있는지 확인하세요. 자세한 지침은 해당 [플랫폼]({{site.baseurl}}/developer_guide/home)의 푸시 알림 통합 가이드를 참조하세요.
2. **커스텀 링크 처리 검사:** 앱에 모든 `https://` 링크에 대한 커스텀 처리가 포함되어 있는지 확인하세요. 커스텀 구성이 기본 동작을 재정의할 수 있습니다. 개발팀과 협력하여 필요한 경우 이러한 설정을 검토하고 조정하세요.
3. **iOS 푸시 등록 확인:** iOS의 경우, [APNs에 푸시 알림 등록]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns)에 대한 푸시 통합 가이드의 1단계를 다시 확인하세요. 앱이 실행을 완료하기 전에 델리게이트 오브젝트가 동기적으로 할당되어야 합니다. 이 단계는 `application:didFinishLaunchingWithOptions:` 메서드에서 완료해야 합니다.
4. **통합 테스트:** 조정을 완료한 후, iOS 및 Android 기기 모두에서 푸시 알림 동작을 테스트하여 문제가 해결되었는지 확인하세요.

### 앱이 백그라운드에서 실행 중일 때 딥링크가 작동하지 않는 경우(iOS) {#deep-links-with-app-still-running-in-the-background-ios}

앱이 실행 중이 아니거나 링크를 직접 사용할 때는 딥링크가 작동하지만, 앱이 이미 백그라운드에서 실행 중일 때는 작동하지 않는 경우, 앱이 링크를 처리하는 방식에 문제가 있을 수 있습니다. 메서드 스위즐링을 사용하는 서드파티 라이브러리를 사용하고 있는지 확인하세요. 스위즐링은 딥링크 구현에 문제를 일으킬 수 있으므로 끄는 것을 권장합니다.

## .p8 인증 키로 마이그레이션 {#migrate-to-a-p8-authentication-key}

Apple `.p8` 인증 키는 Braze에서 APNs 푸시에 필요한 방식입니다. 레거시 인증서 파일 유형과 달리 `.p8` 키는 만료되지 않으며 단일 키로 모든 앱을 지원하므로, 연간 인증서 갱신이 필요 없고 푸시 전달 실패 위험이 줄어듭니다.

현재 `.p12` 또는 `.pem` 인증서를 사용 중이라면 가능한 한 빨리 `.p8` 키로 마이그레이션하세요. `.p8` 키 생성 및 업로드 방법은 [APNs 푸시 인증서 업로드]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)를 참조하세요. 개발자 계정에서 `.p8` 키를 생성하는 방법에 대한 Apple의 안내는 [인증 토큰을 사용하여 APNs와 통신](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/)을 참조하세요.

### .p8 키와 .p12 인증서 비교 {#p8-keys-versus-p12-certificates}

다음 표를 사용하여 자격 증명 유형, 만료 및 대시보드에서의 표시 방식을 비교하세요.

| 자격 증명 | 만료 | 대시보드 상태 표시기 |
| --- | --- | --- |
| `.p8` 인증 키 | 만료되지 않음 | 녹색 상태 표시기 없음(정상) |
| `.p12` 푸시 인증서 | 매년 만료 | 인증서가 유효할 때 녹색 표시기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label=".p8 키와 .p12 인증서 비교" }

`.p12` 인증서를 `.p8` 키로 교체하거나 새 자격 증명을 업로드하면, Braze가 변경 사항을 처리하는 동안 푸시 전달이 잠시 중단될 수 있습니다. 가능하면 유지보수 기간 동안 업데이트를 계획하세요.

**설정** > **앱 설정** > **푸시 알림 설정**에서 **App Bundle ID**, **Team ID**, **Key ID**(`.p8` 키의 경우)가 Apple Developer 계정의 값과 일치하는지 확인하세요. iOS 앱 **번들 ID**가 동일한 경우 여러 Braze 워크스페이스에서 동일한 Apple 푸시 자격 증명을 사용할 수 있습니다. 자격 증명 환경(개발 대 프로덕션)은 앱이 빌드된 방식과 일치해야 합니다.

[Braze Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.0.0) 이상의 앱은 [동적 APNs 게이트웨이 관리]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#dynamic-apns-gateway-management)를 사용하여 토큰을 올바른 APNs 환경으로 자동 라우팅할 수 있습니다.

## 웹 푸시 알림이 예상대로 작동하지 않음 {#web-push-notifications-arent-behaving-as-expected}

브라우저에서 푸시 알림에 문제가 있는 경우, 사이트의 알림 권한을 재설정하고 사이트의 저장소를 지워야 할 수 있습니다. 다음 단계를 참조하세요.

{% tabs %}
{% tab Chrome %}

### 데스크탑에서 Chrome 재설정 {#reset-chrome-on-desktop}

1. Chrome 브라우저에서 URL 옆의 **사이트 정보 보기** 슬라이더 아이콘을 선택하세요.
2. **알림**에서 **권한 재설정**을 선택하세요.
3. Chrome DevTools를 여세요. 운영 체제별 관련 단축키는 다음과 같습니다.

<style>
table {
    max-width: 50%;
}
</style>

| 운영 체제 | 키보드 단축키 |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="데스크탑에서 Chrome 재설정" }

{:start="4"}
4. DevTools에서 **Application** 탭으로 이동하세요.
5. 사이드바에서 **Storage**를 선택하세요.
6. **Clear site data**를 선택하세요.
7. Chrome에서 업데이트된 설정을 적용하기 위해 페이지를 새로고침하라는 메시지가 표시됩니다. **Reload**를 선택하세요.

푸시 권한이 재설정되었습니다. 사이트에 새 탭을 열고 테스트해 보세요.

### Android에서 Chrome 재설정 {#reset-chrome-on-android}

Android 알림 서랍에 사이트의 알림이 표시되는 경우:

1. 푸시 알림에서 <i class="fas fa-cog" title="설정"></i> **설정**을 탭하고 **사이트 설정**을 선택하세요.
2. **사이트 설정**에서 **지우기 및 재설정**을 탭하세요.

사이트의 알림이 열려 있지 않은 경우:

1. Android에서 Chrome을 여세요.
2. <i class="fas fa-ellipsis-vertical"></i> 메뉴를 탭하세요.
3. **설정** > **사이트 설정** > **알림**으로 이동하세요.
4. 알림이 **보내기 전에 확인(권장)**으로 설정되어 있는지 확인하세요.
5. 목록에서 사이트를 찾으세요.
6. 항목을 선택하고 **지우기 및 재설정**을 탭하세요.

푸시 권한이 재설정되었습니다. 사이트에 새 탭을 열고 테스트해 보세요.

{% endtab %}
{% tab Firefox %}

### 데스크탑에서 Firefox 재설정 {#reset-firefox-on-desktop}

1. 사이트 URL 옆의 <i class="fa-solid fa-circle-info" alt="정보 아이콘"></i> 또는 <i class="fas fa-lock" alt="잠금 아이콘"></i>을 선택하세요.
2. **권한**에서 **알림 수신** 옆의 <i class="fa-solid fa-circle-xmark" title="이 권한을 지우고 다시 요청"></i> **권한 지우기**를 선택하여 알림 권한을 지우세요.
3. 같은 메뉴에서 **쿠키 및 사이트 데이터 지우기**를 선택하세요.
4. 선택을 확인하는 대화 상자에서 **확인**을 선택하세요.

푸시 권한이 재설정되었습니다. 사이트에 새 탭을 열고 테스트해 보세요.

### Android에서 Firefox 재설정 {#reset-firefox-on-android}

Android에서 푸시 권한을 재설정하려면 Mozilla 지원의 [검색 기록 및 기타 개인 데이터 지우기](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser)를 참조하세요.

{% endtab %}
{% tab Safari %}

### macOS에서 Safari 재설정 {#reset-safari-on-macos}

{% alert note %}
이 단계는 macOS 전용입니다. Apple은 Windows의 Safari에서 웹 푸시를 지원하지 않습니다.
{% endalert %}

1. Safari를 여세요.
2. [Mac 메뉴 막대](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac)에서 **Safari** > **설정** > **웹사이트** > **알림**으로 이동하세요.
3. 목록에서 사이트를 선택하세요.
4. **제거**를 선택하여 해당 사이트의 알림 권한을 삭제하세요.
5. 그런 다음 **개인 정보 보호** > **웹사이트 데이터 관리**로 이동하세요.
6. 목록에서 사이트를 선택하세요.
7. **제거**를 선택하거나, 모든 사이트 데이터를 제거하려면 **모두 제거**를 선택하세요.
8. **완료**를 선택하세요.

푸시 권한이 재설정되었습니다. 사이트에 새 탭을 열고 테스트해 보세요.

{% endtab %}
{% endtabs %}

## 푸시 열람 측정기준 {#push-open-metrics}

Braze는 사용자가 알림을 탭하고 앱이 세션을 시작할 때 직접 열람을 기록합니다. 앱을 열지 않고 리치 푸시 알림을 확장하는 것은 직접 열람으로 기록되지 않습니다.

사용자가 알림을 탭하지 않고 푸시를 받은 후 앱을 열면, Braze는 대신 영향받은 열람을 기록할 수 있습니다. 정의 및 보고에 대한 자세한 내용은 [영향받은 열람]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens)을 참조하세요.

## 푸시 오류 메시지 {#push-error-messages}

일반적인 푸시 오류 코드(`DEVICE_UNREGISTERED`, `NotRegistered`, `Unregistered` 등)에 대한 정의는 [일반적인 푸시 오류 메시지]({{site.baseurl}}/user_guide/channels/push/push_error_codes)를 참조하세요.

FCM이 `DEVICE_UNREGISTERED` 또는 `NotRegistered`와 같은 오류를 반환하면, Braze는 일반적으로 고객 프로필에서 해당 푸시 토큰을 제거합니다. 이 제거는 보통 앱이 제거되었거나 토큰이 더 이상 유효하지 않음을 나타냅니다. 제거 추적 Campaign은 동일한 토큰 제거 로직을 대규모로 사용합니다.

추가 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support)을 열어주세요.