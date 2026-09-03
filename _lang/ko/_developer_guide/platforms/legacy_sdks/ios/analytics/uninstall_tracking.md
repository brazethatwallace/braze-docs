---
nav_title: 제거 추적
article_title: iOS용 제거 추적
platform: iOS
page_order: 7
description: "이 문서에서는 iOS 애플리케이션에 대한 제거 추적을 구성하는 방법을 다룹니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS용 제거 추적 {#uninstall-tracking-for-ios}

> 이 문서에서는 iOS 애플리케이션에 대한 제거 추적을 구성하는 방법과 앱이 Braze 제거 추적 푸시를 수신할 때 원치 않는 자동 동작을 취하지 않도록 테스트하는 방법을 다룹니다.

제거 추적은 페이로드에 Braze 플래그가 포함된 백그라운드 푸시 알림을 활용합니다. 자세한 내용은 사용자 안내서의 [제거 추적]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)을 참조하세요.

## 1단계: 백그라운드 푸시 활성화 {#step-1-enabling-background-push}

Xcode 프로젝트의 **Capabilities** 탭에 있는 **Background Modes** 섹션에서 **Remote notifications** 옵션이 활성화되어 있는지 확인하세요. 자세한 내용은 [무음 푸시 알림]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications) 설명서를 참조하세요.

## 2단계: Braze 백그라운드 푸시 확인 {#step-2-checking-for-braze-background-push}

Braze는 백그라운드 푸시 알림을 사용하여 제거 추적 분석 데이터를 수집합니다. 애플리케이션이 제거 추적 알림을 수신할 때 [원치 않는 동작을 수행하지 않도록]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push) 해야 합니다.

## 3단계: 대시보드에서 테스트하기 {#step-3-test-from-the-dashboard}

다음으로, 대시보드에서 테스트 푸시를 직접 보내보세요. 이 테스트 푸시는 고객 프로필을 업데이트하지 않습니다.

1. **Campaigns** 페이지에서 푸시 알림 Campaign을 생성하고 플랫폼으로 **iOS push**를 선택합니다.<br><br>
2. **Settings** 페이지에서 키 `appboy_uninstall_tracking`에 해당 값 `true`를 추가하고 **Add Content-Available Flag**를 선택합니다.<br><br>
3. **Preview** 페이지에서 제거 추적 테스트 푸시를 직접 보내봅니다.<br><br>
4. 앱이 푸시를 수신할 때 원치 않는 자동 동작을 수행하지 않는지 확인합니다.

{% alert important %}
이 테스트 단계는 Braze에서 제거 추적 푸시를 전송하는 것을 대리하는 과정입니다. 배지 카운트가 활성화되어 있는 경우 테스트 푸시와 함께 배지 번호가 전송되지만, Braze 제거 추적 푸시는 애플리케이션에 배지 번호를 설정하지 않습니다.
{% endalert %}

## 4단계: 제거 추적 활성화 {#step-4-enable-uninstall-tracking}

[제거 추적 활성화]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking) 지침을 따르세요.