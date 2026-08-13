---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "Push Max는 실패한 푸시 알림을 추적하고 사용자가 수신할 가능성이 더 높은 시점에 푸시를 재전송하여 Android 푸시 알림을 강화합니다."

permalink: /user_guide/channels/push/platform_specific_resources/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Push Max에 대해 알아보고, 이 기능을 사용하여 [중국 OEM 기기]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability)에 대한 Android 푸시 알림의 전달 가능성을 잠재적으로 개선하는 방법을 알아보세요.

## Push Max란 무엇인가요? {#what-is-push-max}

Push Max는 실패한 Android 푸시 알림을 추적하고 사용자가 수신할 가능성이 더 높은 시점에 푸시를 재전송하여 Android 푸시 알림을 강화합니다.

Xiaomi, OPPO, Vivo 등 중국 OEM(Original Equipment Manufacturer)이 제조한 일부 Android 기기는 배터리 수명을 연장하기 위해 강력한 배터리 최적화 방식을 사용합니다. 이 동작은 백그라운드 앱 처리를 종료하는 의도치 않은 결과를 초래할 수 있으며, 앱이 포그라운드에 있지 않은 경우 이러한 기기에서 푸시 알림의 전달 가능성이 저하될 수 있습니다. 이 상황은 아시아 태평양(APAC) 시장에서 가장 자주 발생합니다.

## 사용 가능 여부 {#availability}

- Android 푸시 알림에서만 사용 가능합니다
- 동작 기반 또는 API 트리거 메시지에는 지원되지 않습니다
- [사용자의 마지막 사용 기기에만 전송]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#most-recently-used-device) 옵션이 선택된 경우 지원되지 않습니다

## 필수 조건 {#prerequisites}

Push Max를 사용하여 전송된 푸시 알림은 최소 다음 [최소 SDK 버전]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions)을 갖춘 기기에만 전달됩니다:

{% sdk_min_versions android:29.0.1 %}

## Push Max 사용하기 {#using-push-max}

{% tabs %}
{% tab Campaigns %}

Campaign에서 Push Max를 사용하려면:

1. 푸시 Campaign을 생성합니다.
2. 플랫폼으로 **Android Push**를 선택합니다.
3. **Schedule Delivery** 단계로 이동합니다.
4. **Send using Push Max**를 선택합니다.

!["Send using Push Max" 옵션이 표시된 Schedule Delivery 단계의 Android 푸시 전달 가능성 섹션.]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

Canvas에서 Push Max를 사용하려면:

1. Canvas에 메시지 단계를 추가합니다.
2. 플랫폼으로 **Android Push**를 선택합니다.
3. **Delivery Settings** 탭으로 이동합니다.
4. **Send using Push Max**를 선택합니다.

!["Send using Push Max" 옵션이 표시된 Android 푸시 메시지 단계의 Delivery Settings 탭.]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

다음 두 가지 기능인 Intelligent Timing과 TTL을 Push Max와 함께 사용하여 Android 푸시 알림의 전달 가능성을 잠재적으로 높일 수 있습니다.

### Intelligent Timing {#intelligent-timing}

Push Max는 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)이 켜져 있을 때 가장 효과적으로 작동합니다. Intelligent Timing은 사용자가 앱을 사용할 가능성이 가장 높고 푸시가 전달될 가능성이 가장 높은 시간을 계산하여 푸시 알림을 전송할 수 있습니다.

### TTL(Time to Live) {#time-to-live-ttl}

TTL(Time to Live)은 Firebase Cloud Messaging(FCM)에 대한 실패한 푸시 알림을 추적하고 사용자가 수신할 가능성이 있는 시점에 알림을 재시도할 수 있습니다.

기본적으로 TTL은 최대값인 28일로 설정되어 있습니다. **설정** > **워크스페이스 설정** > **푸시 설정**에서 모든 새 Android 푸시 메시지의 기본 TTL을 줄이거나, Android 푸시 알림을 작성할 때 **설정** 탭에서 메시지별로 일수를 구성할 수 있습니다.

![TTL 필드가 28일로 설정되어 있습니다.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## 알아두어야 할 사항 {#things-to-know}

### 프로모션 코드 {#promotion-codes}

Push Max가 켜져 있는 메시지에서는 Braze [프로모션 코드]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)를 사용하지 않는 것을 권장합니다.

프로모션 코드는 고유하기 때문입니다. 프로모션 코드가 포함된 푸시 알림이 전달에 실패하면, Push Max로 인해 해당 알림이 재전송될 때 새로운 프로모션 코드가 전송됩니다. 이로 인해 예상보다 빠르게 프로모션 코드가 소진될 수 있습니다.

### Canvas 이벤트 속성정보 및 항목 속성정보 {#canvas-event-properties-and-entry-properties}

메시지에 [Canvas 항목 속성정보 또는 이벤트 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)에 대한 Liquid 참조를 포함하면 Push Max가 예상대로 작동하지 않을 수 있습니다. Push Max가 메시지를 재전송하려고 할 때 항목 및 이벤트 속성정보를 사용할 수 없기 때문입니다.