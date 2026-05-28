---
nav_title: "푸시 실행 버튼"
article_title: "푸시 실행 버튼"
page_order: 1
page_type: reference
description: "이 참조 문서에서는 푸시 실행 버튼이 무엇인지, 그리고 iOS와 Android 플랫폼 간의 차이점을 다룹니다."
channel:
  - Push

---

# 푸시 실행 버튼 {#push-action-buttons}

> 푸시 실행 버튼을 사용하면 Braze iOS 및 Android 푸시 알림을 사용할 때 버튼의 콘텐츠와 동작을 설정할 수 있습니다. 실행 버튼을 사용하면 사용자가 앱 경험으로 직접 들어가지 않고도 알림에서 바로 앱과 상호작용할 수 있습니다.

![수락과 거절 두 개의 푸시 실행 버튼이 있는 iOS 푸시 알림.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

## 실행 버튼 생성 {#creating-action-buttons}

각 인터랙티브 버튼은 웹 페이지, 딥링크로 연결하거나 앱을 열 수 있습니다.

- 표준 푸시 Campaign의 경우, 대시보드의 푸시 메시지 작성기에서 **On-Click Behavior** 섹션에서 푸시 실행 버튼을 지정할 수 있습니다.
- [빠른 푸시 Campaign]({{site.baseurl}}/quick_push/)의 경우, **설정** 탭에서 각 플랫폼별로 실행 버튼을 별도로 구성할 수 있습니다.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

iOS 푸시 메시지에서 실행 버튼을 사용하려면 다음을 수행하세요:

1. 표준 Campaign의 경우 **작성** 탭에서, 빠른 푸시의 경우 **설정** 탭에서 실행 버튼을 켭니다.
2. 다음 사용 가능한 버튼 조합에서 **iOS Notification Category**를 선택합니다:
 - Accept / Decline
 - Yes / No
 - Confirm / Cancel
 - More
 - 사전 등록된 커스텀 iOS 카테고리

![iOS 알림 카테고리 드롭다운 메뉴.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
iOS의 버튼 처리 방식으로 인해, 푸시 실행 버튼을 설정할 때 추가 통합 단계를 수행해야 합니다. 이 단계는 [개발자 설명서]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories)에 설명되어 있습니다. 특히 iOS 카테고리를 구성하거나 특정 기본 버튼 옵션 중에서 선택해야 합니다. Android 통합의 경우 이러한 버튼은 자동으로 작동합니다.
{% endalert %}

**Yes** / **No**와 같은 사전 설정 쌍은 두 번째 버튼을 기본적으로 닫기(**CLOSE**) 동작에 매핑하므로, 첫 번째 버튼과 같은 방식으로 앱을 열지 않습니다. **_직접 열람 수_**에는 이러한 유형의 탭이 포함되지 않지만, Currents 또는 Snowflake의 **Push Notification Open** 데이터에서는 `button_action_type` 및 `button_string`과 함께 기록될 수 있습니다. 자세한 내용은 [푸시 실행 버튼과 리포팅]({{site.baseurl}}/user_guide/channels/push/reporting/#push-action-buttons-and-reporting)을 참조하세요.
{% endtab %}
{% tab Android %}
### Android {#android}

Android 푸시 메시지에서 실행 버튼을 사용하려면 다음을 수행하세요:

1. 표준 Campaign의 경우 **작성** 탭에서, 빠른 푸시의 경우 **설정** 탭에서 실행 버튼을 켭니다.
2. <i class="fas fa-plus-circle"></i> **Add Button**을 선택하고 버튼 텍스트와 **On-Click Behavior**를 지정합니다. 다음 사용 가능한 동작 중에서 선택할 수 있습니다:
  - Open App
  - Redirect to Web URL
  - 앱으로 [딥링크]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/)

![알림 버튼의 클릭 시 동작으로 "Open App"을 선택하는 화면.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

푸시에 최대 세 개의 버튼을 추가할 수 있습니다.

#### Android 글자 수 제한 {#android-character-limits}

쌓여서 표시되는 iOS 버튼과 달리, Android 버튼은 한 줄에 나란히 표시됩니다. 즉, 버튼을 더 많이 추가할수록(최대 세 개) 버튼 텍스트에 사용할 수 있는 공간이 줄어듭니다.

![텍스트가 잘린 Android 푸시 실행 버튼.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

다음 표는 버튼 수에 따라 버튼 텍스트가 잘리기 전에 추가할 수 있는 최대 글자 수를 보여줍니다:

| 버튼 수 | 버튼당 최대 글자 수 |
| --- | --- |
| 1 | 46자 |
| 2 | 20자 |
| 3 | 11자 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}