---
nav_title: "알림 옵션"
article_title: Android 알림 옵션
page_order: 2
page_type: reference
description: "이 참조 문서에서는 여러 Android 알림 옵션과 Braze Campaign에서 이를 효과적으로 사용하는 방법을 다룹니다."

platform: Android
channel:
  - Push

---

# 알림 옵션 {#notification-options}

> 다음은 Braze를 통해 사용할 수 있는 Android 전용 푸시 알림 옵션입니다.

## 무음 알림 {#silent-notifications}

[푸시 알림 메시지를 작성]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/?tab=android#step-4-compose-your-push-message)할 때, 제목 없이 Android 푸시 메시지를 보낼 수는 **없습니다**. 하지만 제목 대신 공백 하나를 입력할 수 있습니다. 메시지에 공백 하나만 포함된 경우 무음 푸시 알림으로 전송된다는 점에 유의하세요. 자세한 내용은 [무음 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)을 참조하세요.

## 알림 그룹 {#notification-groups}

메시지를 분류하고 사용자의 알림 트레이에서 그룹화하려면 Braze를 통해 Android의 알림 채널 기능을 활용할 수 있습니다.

먼저 Android 푸시 Campaign을 생성한 다음, **작성** 탭 상단에서 **Notification Channel** 드롭다운을 찾으세요.

![]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

드롭다운에서 알림 채널을 선택하세요. 알림 채널 설정에 문제가 발생할 경우를 대비하여 대체 채널도 선택해야 합니다.

여기에 [알림 채널]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels/)이 나열되지 않은 경우, 알림 채널 ID를 사용하여 추가할 수 있습니다. 개발자에게 연락하여 알림 채널 ID를 확인하거나 필요에 따라 새 ID를 생성하세요.

알림 채널에 알림 ID를 추가하려면 **Notification Channel** 드롭다운 메뉴에서 **Manage Notification Channel**을 클릭하고 필수 필드를 입력하세요. 알림 채널은 Braze 플랫폼에서 사용하기 전에 앱에서 먼저 정의해야 합니다.

![]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }