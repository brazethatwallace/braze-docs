---
nav_title: 푸시
article_title: 푸시
page_order: 7
page_type: landing
description: "모바일 및 웹 푸시 알림을 통해 시간에 민감한 행동 유도 메시지를 전송하여 사용자를 다시 참여시키고 행동을 유도하세요."
channel:
  - push
search_rank: 3
---

# 푸시 {#push}

> 푸시 알림은 모바일이나 웹을 통해 시간에 민감한 행동 유도 메시지를 보내고, 한동안 앱을 사용하지 않은 사용자를 다시 참여시키는 검증된 방법입니다. 사용자를 콘텐츠로 직접 안내하고 애플리케이션의 가치를 보여줍니다.

[![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## 필수 조건 {#prerequisites}

시작하기 전에 다음 사항을 확인하세요:

- **앱 또는 웹사이트에 푸시가 통합되어 있어야 합니다.** 개발자와 협력하여 설정하세요. 자세한 단계는 [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android), [웹]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) 통합 가이드를 참조하세요.
- **푸시 옵트인 전략이 필요합니다.** 사용자는 기기에서 푸시 권한을 허용해야 합니다. 프롬프트를 표시하기 전에 [푸시 프라이머 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/)를 사용하여 가치를 설명하는 것을 고려하세요.

## 활용 사례 {#use-cases}

| 활용 사례 | 설명 |
| --- | --- |
| 초기 온보딩 | 사용자가 앱 사용을 위한 초기 단계(예: 계정 등록)를 완료하기 전까지는 가치가 크게 제한됩니다. 푸시 알림을 사용하여 사용자가 이러한 단계를 완료하도록 유도하면 앱을 완전히 활용할 수 있게 됩니다. |
| 첫 구매 | 사용자가 앱 사용에 익숙해지면 푸시 알림을 사용하여 인앱 구매자로 전환하는 데 도움을 줄 수 있습니다. |
| 새로운 기능 | 푸시 알림은 이탈한 사용자에게 앱으로 다시 돌아오게 할 수 있는 새로운 기능을 알리는 데 효과적입니다. |
| 시간 제한 혜택 | 혜택에 시간 제한이 있는 경우, 푸시는 만료 전에 사용자에게 알리는 좋은 방법입니다. 이러한 메시지는 일반적으로 높은 긴급성을 전달하며, 최근 이탈한 사용자에게 앱을 상기시키는 데 최적입니다. 예를 들어, 앱이 게임이고 매일 연속 플레이 시 인게임 화폐 보너스를 제공하는 경우, 일정 일수에 도달한 후 연속 기록이 위험에 처해 있다고 알리는 것은 효과적인 푸시가 될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="활용 사례" }

## 푸시 메시지 규정 {#push-message-regulations}

푸시는 고객의 기기에 직접 도달하므로, 앱 및 스토어 정책에 따라 사용 방법이 제한됩니다.

{% alert important %}
푸시 메시지는 [Apple App Store 심사 가이드라인](https://developer.apple.com/app-store/review/guidelines/) 및 [Google Play 정책](https://support.google.com/googleplay/android-developer/answer/9888379)을 준수해야 합니다. 여기에는 광고, 스팸, 프로모션 및 관련 주제에 대한 푸시 사용 규칙이 포함됩니다.
{% endalert %}

| 정책 출처 | 요약 |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | 허용되지 않는 사용에는 App Store와 유사한 서드파티 앱, 확장 프로그램 또는 플러그인을 표시하기 위한 인터페이스를 만들거나 일반적인 관심 컬렉션으로 사용하는 것이 포함됩니다. |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | 푸시는 앱 작동에 필수적이어서는 안 되며, 민감한 개인 정보나 기밀 정보를 전달해서는 안 됩니다. 고객이 앱 UI의 동의 문구를 통해 명시적으로 옵트인하고 앱에서 옵트아웃할 수 있는 경우가 아니라면, 프로모션이나 다이렉트 마케팅에 푸시를 사용하지 마세요. |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | 푸시 알림, 카메라, 자이로스코프 등의 내장 기능이나 Apple Music, iCloud 등의 Apple 서비스를 수익화해서는 안 됩니다. |
| Google Play — [시스템 기능의 무단 사용 또는 모방](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | 앱은 시스템 알림을 모방하거나 방해해서는 안 됩니다. 시스템 수준 알림은 앱의 핵심 기능에만 사용해야 합니다(예: 항공사 앱이 사용자에게 특가 정보를 알리거나, 게임이 사용자에게 인게임 프로모션을 알리는 경우). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 메시지 규정" }

## 다음 단계 {#next-steps}

- [푸시 설정]({{site.baseurl}}/user_guide/channels/push/push_setup/)
- [푸시 메시지 만들기]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/)