---
nav_title: 문제 해결
article_title: 푸시 문제 해결
page_order: 5
page_type: reference
description: "이 페이지에서는 푸시 메시징 채널과 관련된 다양한 문제에 대한 문제 해결 단계를 안내합니다."
channel: push
---

# 푸시 문제 해결 {#troubleshoot-push}

> 이 페이지를 사용하여 푸시 메시징 채널의 문제를 해결하세요.

## 푸시 알림 누락 {#missing-push-notifications}

푸시 알림 전달에 문제가 있으신가요? 다음 항목을 확인하여 이 문제를 해결할 수 있습니다:

- [푸시 구독 상태](#push-subscription-status)
- [Segment](#segment)
- [푸시 알림 한도](#push-notification-caps)
- [사용량 제한](#rate-limits)
- [대조군 상태](#control-group-status)
- [유효한 푸시 토큰](#valid-push-token)
- [푸시 알림 유형](#push-notification-type)
- [현재 앱](#current-app)

#### 푸시 구독 상태 {#push-subscription-status}

푸시는 가입됨 또는 옵트인한 사용자에게만 발송할 수 있습니다. **고객 프로필** 섹션의 [참여]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) 탭에서 고객 프로필을 확인하여 테스트 중인 워크스페이스에 대해 푸시에 활성 등록되어 있는지 확인하세요. 여러 앱에 등록되어 있는 경우 **푸시 등록 대상** 필드에 목록이 표시됩니다:

![푸시 등록 대상]({% image_buster /assets/img_archive/trouble1.png %})

Braze 내보내기 엔드포인트를 사용하여 고객 프로필을 내보낼 수도 있습니다:
- [식별자별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
- [Segment별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)

두 엔드포인트 모두 기기별 푸시 활성화 정보를 포함하는 푸시 토큰 오브젝트를 반환합니다.

#### Segment {#segment}

타겟팅하는 Segment에 포함되어 있는지 확인하세요(라이브 Campaign이고 테스트가 아닌 경우). **고객 프로필**에서 사용자가 현재 포함된 Segment 목록을 확인할 수 있습니다. 세분화는 실시간으로 업데이트되므로 이 값은 항상 변할 수 있다는 점을 기억하세요.

![Segment 목록]({% image_buster /assets/img_archive/trouble2.png %})

Segment를 생성할 때 **사용자 조회**를 사용하여 사용자가 해당 Segment에 포함되어 있는지 확인할 수도 있습니다.

![검색 필드가 있는 사용자 조회 섹션.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### 푸시 알림 한도 {#push-notification-caps}

글로벌 최대 게재빈도 설정을 확인하세요. 워크스페이스에 글로벌 최대 게재빈도 설정이 적용되어 있고 지정된 기간 동안 푸시 알림 한도에 이미 도달했기 때문에 푸시 알림을 받지 못했을 수 있습니다.

대시보드에서 [글로벌 최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#freq-cap-feat-over)을 확인하여 이를 수행할 수 있습니다. Campaign이 최대 게재빈도 설정 규칙을 따르도록 설정된 경우, 이 설정의 영향을 받는 사용자 수가 표시됩니다.

![Campaign 세부 정보]({% image_buster /assets/img_archive/trouble3.png %})

#### 사용량 제한 {#rate-limits}

Campaign 또는 Canvas에 사용량 제한이 설정되어 있는 경우, 이 한도를 초과하여 메시지를 받지 못할 수 있습니다. 자세한 내용은 [사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#rate-limiting)을 참조하세요.

#### 대조군 상태 {#control-group-status}

단일 채널 Campaign이거나 대조군이 있는 Canvas인 경우, 대조군에 포함되었을 수 있습니다.

  1. [배리언트 분배]({{site.baseurl}}/user_guide/messaging/ab_testing/#step-5-distribute-users-among-your-variants)를 확인하여 대조군이 있는지 확인하세요.
  2. 대조군이 있는 경우, [Campaign 대조군 포함]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter) 필터로 Segment를 생성한 다음 [Segment를 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/#exporting-to-csv)하여 사용자 ID가 이 목록에 있는지 확인하세요.

#### 유효한 푸시 토큰 {#valid-push-token}
푸시 토큰은 발신자가 푸시 알림으로 특정 기기를 타겟팅하는 데 사용하는 식별자입니다. 따라서 기기에 유효한 푸시 토큰이 없으면 푸시 알림을 보낼 방법이 없습니다.

#### 푸시 알림 유형 {#push-notification-type}

올바른 유형의 푸시 알림을 사용하고 있는지 확인하세요. 예를 들어, FireTV를 타겟팅하려면 Android 푸시 Campaign이 아닌 Kindle 푸시 알림을 사용해야 합니다. 마찬가지로 Android를 타겟팅하려면 iOS 푸시 Campaign이 아닌 Android 푸시 알림을 사용하세요. 다음 문서에서 Braze 워크플로우에 대한 자세한 내용을 확인하세요:
- [Apple 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### 현재 앱 {#current-app}

내부 사용자를 대상으로 푸시 발송을 테스트할 때, 푸시 알림을 받을 사용자가 현재 해당 앱에 로그인되어 있는지 확인하세요. 그렇지 않으면 사용자가 푸시를 받지 못하거나 Segment에 포함되지 않았다고 생각되는 푸시를 받을 수 있습니다.

## 푸시 알림을 클릭해도 앱이 열리지 않음 {#clicking-a-push-notification-doesnt-open-the-app}

푸시 알림을 클릭해도 앱이 열리지 않는 경우, 플랫폼에 따라 다음 사항을 확인하세요.

### Android

1. **클릭 시 동작 확인:** Campaign이 클릭 시 앱을 열도록 구성되어 있는지 확인하세요.
2. **딥링크 처리 확인:** `braze.xml` 파일에서 `com_braze_handle_push_deep_links_automatically`가 `true`로 설정되어 있는지 `false`로 설정되어 있는지 확인하세요.
   - `true`로 설정된 경우, Braze SDK가 딥링크를 직접 처리하며 앱이 정상적으로 열려야 합니다.
   - `false`로 설정된 경우, 앱에서 푸시 수신 및 열기 의도를 수신하고 처리할 방송 수신기가 필요합니다. 이 수신기가 올바르게 구현되어 있는지 확인하세요.
3. **상세 로그 수집:** [상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/)하고, 문제를 재현한 다음, `braze.xml` 및 `AndroidManifest.xml`과 함께 로그를 Braze 고객지원에 제공하세요.

### iOS

1. **클릭 시 동작 확인:** Campaign이 클릭 시 앱을 열도록 구성되어 있는지 확인하세요.
2. **푸시 통합 확인:** 푸시에서 앱으로의 딥링킹은 Braze [표준 푸시 통합]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)에 의해 자동으로 처리됩니다. 커스텀 델리게이트 처리를 포함하여 통합이 올바르게 구현되어 있는지 확인하세요.
3. **상세 로그 수집:** [상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/)하고, 문제를 재현한 다음, 로그를 Braze 고객지원에 제공하세요.

## 푸시 클릭 시 예기치 않게 앱에서 열림 {#push-clicks-unexpectedly-open-in-app}

푸시 알림의 링크가 웹 브라우저 대신 앱에서 예기치 않게 열리는 문제가 발생하는 경우, Campaign 구성 또는 SDK 구현에 문제가 있을 수 있습니다. 다음 단계를 참조하세요.

### 클릭 시 동작 확인 {#verify-on-click-behavior}

Campaign 또는 캔버스 단계에서 **모바일 앱 내에서 웹 URL 열기**가 선택되어 있지 않은지 다시 확인하세요. 선택되어 있다면 선택을 해제하고 다시 시작하세요.

![푸시 구성의 '클릭 시 동작' 필드가 '웹 URL 열기'로 설정되어 있고 '모바일 앱 내에서 웹 URL 열기'가 선택 해제된 상태.]({% image_buster /assets/img/push_on_click.png %})

클릭 시 동작 "웹 URL 열기"의 기본 상호작용은 SDK 버전에 따라 다릅니다. SDK 버전 iOS 2.29.0 및 Android 2.0.0 이상에서는 이 옵션이 기본적으로 선택되어 있으며 웹 URL이 앱 내 웹뷰에서 열립니다. 이전 버전에서는 이 옵션이 기본적으로 해제되어 있으며 웹 URL이 기기의 기본 웹 브라우저에서 열립니다.

이것이 문제가 아닌 경우, 푸시 구현에 문제가 있을 수 있습니다.

### 푸시 통합 재확인 {#double-check-push-integration}

푸시 알림의 링크가 예기치 않게 앱에서 열리는 경우, 푸시 알림 통합 또는 커스터마이징 설정에 문제가 있을 수 있습니다. 다음 단계에 따라 문제를 해결하세요:

1. **푸시 델리게이트 구현 검토:** Braze 푸시 델리게이트가 올바르게 구현되어 있는지 확인하세요. 자세한 지침은 해당 [플랫폼]({{site.baseurl}}/developer_guide/home/)의 푸시 알림 통합 가이드를 참조하세요.
2. **커스텀 링크 처리 검사:** 앱에 모든 `https://` 링크에 대한 커스텀 처리가 포함되어 있는지 확인하세요. 커스텀 구성이 기본 동작을 재정의할 수 있습니다. 개발팀과 협력하여 필요한 경우 이러한 설정을 검토하고 조정하세요.
3. **iOS 푸시 등록 확인:** iOS의 경우, [APNs에 푸시 알림 등록]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns)에 대한 푸시 통합 가이드의 1단계를 다시 확인하세요. 앱이 실행을 완료하기 전에 델리게이트 오브젝트가 동기적으로 할당되어야 합니다. 이 단계는 `application:didFinishLaunchingWithOptions:` 메서드에서 완료해야 합니다.
4. **통합 테스트:** 조정을 완료한 후, iOS 및 Android 기기 모두에서 푸시 알림 동작을 테스트하여 문제가 해결되었는지 확인하세요.

## .p8 인증 키로 마이그레이션 {#migrate-to-a-p8-authentication-key}

Apple `.p8` 인증 키는 Braze에서 APNs 푸시에 필요한 방식입니다. 레거시 인증서 파일 유형과 달리 `.p8` 키는 만료되지 않으며 단일 키로 모든 앱을 지원하므로, 연간 인증서 갱신이 필요 없고 푸시 전달 실패 위험이 줄어듭니다.

현재 `.p12` 또는 `.pem` 인증서를 사용 중이라면 가능한 한 빨리 `.p8` 키로 마이그레이션하세요. `.p8` 키 생성 및 업로드 방법은 [APNs 푸시 인증서 업로드]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)를 참조하세요. 개발자 계정에서 `.p8` 키를 생성하는 방법에 대한 Apple의 안내는 [인증 토큰을 사용하여 APNs와 통신](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/)을 참조하세요.

## 웹 푸시 알림이 예상대로 작동하지 않음 {#web-push-notifications-arent-behaving-as-expected}

브라우저에서 푸시 알림에 문제가 있는 경우, 사이트의 알림 권한을 재설정하고 사이트의 저장소를 지워야 할 수 있습니다. 다음 단계를 참조하세요.

{% tabs %}
{% tab Chrome %}

### 데스크탑에서 Chrome 재설정 {#reset-chrome-on-desktop}

1. Chrome 브라우저에서 URL 옆의 **사이트 정보 보기** 슬라이더 아이콘을 선택하세요.
2. **알림**에서 **권한 재설정**을 선택하세요.
3. Chrome DevTools를 여세요. 운영체제별 관련 단축키는 다음과 같습니다.

<style>
table {
    max-width: 50%;
}
</style>

| 운영체제 | 키보드 단축키 |
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

1. 푸시 알림에서 <i class="fas fa-cog" title="설정"></i>을 탭하고 **사이트 설정**을 선택하세요.
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
2. **권한**에서 **알림 수신** 옆의 <i class="fa-solid fa-circle-xmark" title="이 권한을 지우고 다시 묻기"></i>를 선택하여 알림 권한을 지우세요.
3. 같은 메뉴에서 **쿠키 및 사이트 데이터 지우기**를 선택하세요.
4. 선택을 확인하는 대화 상자에서 **확인**을 선택하세요.

푸시 권한이 재설정되었습니다. 사이트에 새 탭을 열고 테스트해 보세요.

### Android에서 Firefox 재설정 {#reset-firefox-on-android}

Android에서 푸시 권한을 재설정하려면 이 [Mozilla 지원 문서](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser)를 참조하세요.

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

## 푸시 오류 메시지 {#push-error-messages}

일반적인 푸시 오류 메시지(`DEVICE_UNREGISTERED`, `Unregistered`, `NotRegistered` 등)에 대한 자세한 내용은 [일반적인 푸시 오류 메시지]({{site.baseurl}}/user_guide/channels/push/push_error_codes/)를 참조하세요.

추가 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 열어주세요.