---
nav_title: 푸시 설정
article_title: 푸시 설정
page_order: 5
page_type: reference
description: "이 문서에서는 Braze 대시보드의 푸시 설정에 대한 개요를 설명합니다."
channel: push

---

# 푸시 설정 {#push-settings}

> **푸시 설정** 페이지에서는 푸시 알림에 대한 주요 설정(예: 푸시 유지 시간(TTL) 및 Android Campaign의 기본 FCM 우선순위 등)을 구성할 수 있습니다. 이러한 설정은 푸시 알림의 전달과 효과를 최적화하여 사용자에게 더 나은 경험을 제공하는 데 도움이 됩니다.

## 푸시 TTL이란? {#what-is-push-ttl}

푸시 유지 시간(TTL)은 Campaign이 전송될 때 오프라인 상태인 기기에 Braze가 푸시 알림을 전달하려고 시도하는 기간을 제어합니다. TTL이 만료된 후 기기가 다시 연결되면 메시지가 전달되지 않습니다. 이 설정은 사용자의 기기에 이미 수신된 알림을 제거하지 않으며, 푸시 제공업체가 알림을 전달하려고 시도하는 기간만 제어합니다.

## 기본 푸시 TTL 값 설정 {#setting-default-push-ttl-values}

기본적으로 Braze는 각 푸시 메시징 서비스의 최대값으로 푸시 TTL을 설정합니다.

| 푸시 메시징 서비스 | 최대 TTL |
| --- | --- |
| 웹(FCM 또는 웹 푸시 서비스를 통해) | 28일 |
| Firebase Cloud Messaging(FCM) | 28일 |
| Kindle(ADM) | 31일 |
| Huawei(HMS) | 15일 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Setting default Push TTL values" }

이 설정은 특정 메시지에 다른 TTL이 설정되지 않는 한 모든 푸시 Campaign에 전역적으로 적용됩니다. 메시지의 TTL을 조정하려면 [고급 Campaign 설정]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#ttl)을 참조하세요.

기본 푸시 TTL을 다르게 설정하려면:

1. **설정** > **설정 관리** > **푸시 설정**으로 이동합니다.
2. 각 Android 플랫폼에 대해 기본 유지 시간 값을 정의합니다. 더 정밀한 제어를 위해 시간이나 초 단위로 더 작은 단위를 설정할 수 있습니다.
3. **저장**을 선택하여 변경 사항을 적용합니다.

![Firebase, 웹, Kindle 및 Huawei 기기에 대한 푸시 TTL 설정.]({% image_buster /assets/img/push_ttl.png %})

## Android Campaign의 기본 FCM 우선순위 {#default-fcm-priority-for-android-campaigns}

모든 Android 푸시 Campaign에 대한 기본 Firebase Cloud Messaging(FCM) 우선순위를 설정할 수 있습니다. 이 우선순위는 푸시 알림이 사용자의 기기에 전달되는 방식을 결정합니다.

FCM 우선순위 옵션은 다음과 같습니다:

| 우선순위 | 설명 | 사용 사례 |
| --- | --- | --- |
| 보통 | 배터리 사용을 최적화하는 표준 전달 우선순위 | 즉각적인 주의가 필요하지 않은 콘텐츠 |
| 높음 | 메시지가 즉시 전송됨 | 신속한 전달이 필요한 시간에 민감한 알림 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Default FCM Priority for Android Campaigns" }

기본 FCM 우선순위를 설정하려면:

1. **설정** > **설정 관리** > **푸시 설정**으로 이동합니다.
2. FCM 우선순위 섹션에서 기본 설정으로 "보통" 또는 "높음"을 선택합니다.
3. **저장**을 선택하여 변경 사항을 적용합니다.

![Android 전달 우선순위 설정.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

이 설정은 특정 Campaign을 생성할 때 다른 우선순위를 선택하지 않는 한 모든 새 Android 푸시 Campaign에 전역적으로 적용됩니다.

{% alert note %}
FCM이 앱에서 사용자에게 표시되는 알림이나 사용자 참여로 이어지지 않는 높은 우선순위 메시지를 자주 보내는 것을 감지하면, 해당 메시지가 자동으로 보통 우선순위로 강등될 수 있습니다.
{% endalert %}

FCM 우선순위 수준 및 우선순위 강등에 대한 자세한 내용은 [고급 Campaign 설정]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#fcm-priority)을 참조하세요.