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

> 푸시 알림은 모바일 및 웹 기기에 시간에 민감한 행동 유도 메시지를 전송하여, 최근 앱을 열지 않은 사용자를 다시 참여시킵니다. 관련 콘텐츠로 바로 연결되어 제품의 지속적인 가치를 보여줍니다. 이 허브에서는 푸시 통합, 옵트인 전략, 메시지 유형, 모범 사례, 그리고 iOS, Android, 웹 플랫폼별 설정을 다룹니다. 시스템 권한을 요청하기 전에 [푸시 프라이머 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)를 고려해 보세요. 시작하려면 [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android), [웹]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web) 통합 가이드를 참조하세요.

[![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## 필수 조건 {#prerequisites}

시작하기 전에 다음 사항을 확인하세요:

- **앱 또는 웹사이트에 푸시가 통합되어 있어야 합니다.** 개발자와 협력하여 이를 설정하세요. 자세한 단계는 [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications?tab=android), [웹]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)용 통합 가이드를 참조하세요.
- **푸시 옵트인 전략이 필요합니다.** 사용자는 기기에서 푸시 권한을 부여해야 합니다. 프롬프트를 표시하기 전에 [푸시 프라이머 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)를 활용하여 푸시의 가치를 설명하는 것을 고려하세요.

## 사용 사례 {#use-cases}

| 사용 사례 | 설명 |
| --- | --- |
| 초기 온보딩 | 사용자가 계정 등록과 같은 앱 사용의 첫 단계를 완료하기 전까지는 그 가치가 매우 제한적입니다. 푸시 알림을 사용하여 사용자에게 이러한 단계를 완료하도록 독려하면, 앱을 본격적으로 활용할 수 있도록 도울 수 있습니다. |
| 첫 구매 | 사용자가 앱 사용에 익숙해지면, 푸시 알림을 활용하여 인앱 구매자로 전환하는 데 도움을 줄 수 있습니다. |
| 새로운 기능 | 푸시 알림은 이탈한 사용자에게 앱으로 다시 돌아오도록 유도할 수 있는 새로운 기능을 알리는 데 효과적입니다. |
| 시간 제한 혜택 | 특정 혜택에 시간 제한이 있는 경우, 만료되기 전에 사용자에게 알리는 데 푸시가 매우 유용합니다. 이러한 메시지는 일반적으로 높은 긴급성을 전달하며, 최근 이탈한 사용자에게 앱을 상기시키는 데 최적입니다. 예를 들어, 앱이 게임이고 매일 연속 플레이 시 인게임 화폐 보너스를 제공하는 경우, 사용자가 일정 일수에 도달한 후 연속 플레이 기록이 끊길 위험이 있음을 알리는 것은 효과적인 푸시가 될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 사례" }

## 푸시 메시지 규정 {#push-message-regulations}

푸시는 고객의 기기에 직접 도달하므로, 앱 및 스토어 정책에 따라 사용 방식이 제한됩니다.

{% alert important %}
푸시 메시지는 [Apple 앱 스토어 심사 지침](https://developer.apple.com/app-store/review/guidelines/) 및 [Google Play 정책](https://support.google.com/googleplay/android-developer/answer/9888379)을 준수해야 합니다. 여기에는 광고, 스팸, 프로모션 및 관련 주제에 대한 푸시 사용 규칙이 포함됩니다.
{% endalert %}

| 정책 출처 | 요약 |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | 허용되지 않는 사용 사례에는 앱 스토어와 유사한 서드파티 앱, 확장 프로그램 또는 플러그인을 표시하는 인터페이스를 만들거나 일반적인 관심사 모음으로 활용하는 것이 포함됩니다. |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | 푸시는 앱이 작동하는 데 필수 요건이어서는 안 되며, 민감한 개인 정보 또는 기밀 정보를 전달해서는 안 됩니다. 고객이 앱 UI 내 동의 문구를 통해 명시적으로 옵트인하고 앱 내에서 옵트아웃할 수 있는 경우를 제외하고, 프로모션이나 다이렉트 마케팅에 푸시를 사용하지 마세요. |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | 푸시 알림, 카메라, 자이로스코프 등 내장 기능이나 Apple Music, iCloud 등 Apple 서비스를 수익화해서는 안 됩니다. |
| Google Play — [시스템 기능의 무단 사용 또는 모방](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | 앱은 시스템 알림을 모방하거나 방해해서는 안 됩니다. 시스템 수준 알림은 앱의 핵심 기능에만 사용됩니다(예: 항공사 앱이 사용자에게 특가 정보를 알리거나, 게임이 사용자에게 인게임 프로모션을 알리는 경우). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 메시지 규정" }

## 자주 묻는 질문 {#frequently-asked-questions}

### Braze는 푸시 발송 성공을 언제 기록하나요? {#when-does-braze-record-a-successful-send-for-push}

Braze는 일반적으로 메시지가 Braze에서 Apple, Google 또는 웹 푸시 서비스로 전달된 시점에 **발송**을 기록합니다. **전달**, 열람, 반송 및 앱 삭제 감지 신호는 별도로 추적되며 나중에 도착할 수 있습니다. **발송** 수치와 후속 측정기준이 일치하지 않는 것처럼 보일 때는 단계 및 Campaign 수준 분석과 함께 [푸시 문제 해결]({{site.baseurl}}/user_guide/channels/push/troubleshooting)을 활용하세요.

## 다음 단계 {#next-steps}

- [푸시 설정]({{site.baseurl}}/user_guide/channels/push/push_setup)
- [푸시 메시지 만들기]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)