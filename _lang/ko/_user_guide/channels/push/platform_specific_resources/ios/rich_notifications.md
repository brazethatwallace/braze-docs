---
nav_title: 리치 알림 생성
article_title: "iOS용 리치 푸시 알림 생성"
page_order: 3
page_type: tutorial
description: "이 튜토리얼에서는 Braze Campaigns에 대한 iOS 리치 알림을 생성하기 위한 요구 사항과 단계를 다룹니다."

platform: iOS
channel:
  - push
tool:
  - Campaigns
---

# iOS용 리치 푸시 알림 생성 {#create-rich-push-notifications-for-ios}

> 리치 알림을 사용하면 텍스트 이외의 추가 콘텐츠를 포함하여 푸시 알림을 더욱 다양하게 커스텀할 수 있습니다. Android 알림에는 이미 오래전부터 푸시 알림에 이미지가 포함되어 있으며, '확장 알림 이미지'로 메시지가 전달됩니다. iOS 10부터는 고객이 GIF, 이미지, 비디오 또는 오디오가 포함된 iOS 푸시 알림을 받을 수 있습니다.

## 필수 조건 {#prerequisites}

iOS용 리치 푸시 알림을 생성하기 전에 다음 세부 사항을 확인하세요:

- 앱에서 리치 알림을 보낼 수 있도록 하려면 [iOS 푸시 통합]({{site.baseurl}}/developer_guide/push_notifications/rich?sdktab=swift) 안내를 참고하세요. 개발자가 앱에 서비스 확장을 추가해야 합니다.
- 현재 대시보드에서 직접 업로드할 수 있는 파일 형식은 JPEG, PNG, GIF입니다. 이러한 파일은 템플릿 가능한 URL 필드에 입력할 수도 있으며, AIF, M4A, MP3, MP4, WAV 등의 추가 파일 형식도 지원됩니다.
- 미디어 제한 사항 및 사양은 [Apple 설명서](https://developer.apple.com/reference/usernotifications/unnotificationattachment)를 참고하세요.
- iOS는 화면에 맞게 이미지를 조정하며, 활성 또는 잠금 화면 보기에 맞게 리치 이미지를 스케일링합니다.

{% alert note %}
2020년 1월부터 iOS 리치 푸시 알림은 10&nbsp;MB 미만의 1038x1038 이미지를 처리할 수 있지만, 가능한 한 작은 파일 크기를 사용하는 것을 권장합니다. 실제로 대용량 파일을 전송하면 불필요한 네트워크 부하가 발생하고 다운로드 시간 초과가 더 자주 발생할 수 있습니다.
{% endalert %}

{% alert important %}
이미지 파일 크기가 너무 크거나, 종횡비가 올바르지 않거나, 텍스트가 최대 메시지 길이를 초과하거나, 제목 텍스트가 최대 제목 길이를 초과하는 경우 푸시 알림 이미지가 예상대로 표시되지 않을 수 있습니다.
{% endalert %}

### 글자 수 {#character-count}

푸시에 포함할 정확한 글자 수에 대한 엄격한 규칙을 제공하기는 어렵지만, iOS 메시지를 디자인할 때 고려할 [몇 가지 가이드라인]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)을 제공합니다. 이미지 유무, 사용자 기기의 알림 상태 및 디스플레이 설정, 기기 크기에 따라 차이가 있을 수 있습니다. 확실하지 않은 경우, 짧고 간결하게 작성하세요.

모범 사례로서, Braze는 모바일 푸시 알림에서 선택적 제목과 메시지 본문 모두 각 줄에 약 30~40자를 유지할 것을 권장합니다.

#### 알림 상태 {#notification-states}

사용자는 다양한 상황에서 푸시 알림을 볼 수 있으며, 다음과 같이 서로 다른 길이의 텍스트를 확인할 수 있습니다.

<table aria-label="알림 상태">
  <caption>알림 상태</caption>
<thead>
  <tr>
    <th>잠금 화면 또는 알림 센터</th>
    <th>확장됨</th>
    <th>기기 활성 상태</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">가장 일반적인 시나리오입니다.<br><br><b>제목:</b> 텍스트 1줄<br><b>본문:</b> 텍스트 4줄<br><b>이미지:</b> 정사각형 썸네일</td>
    <td width="33%">사용자가 메시지를 길게 누를 때 표시됩니다.<br><br><b>제목:</b> 텍스트 1줄<br><b>본문:</b> 텍스트 7줄<br><b>이미지:</b> 2:1 종횡비(권장, 아래 참고 사항 참조)</td>
    <td width="33%">사용자가 기기의 잠금이 해제되어 활성 상태일 때 푸시를 수신하는 경우입니다.<br><br><b>제목:</b> 텍스트 1줄<br><b>본문:</b> 텍스트 2줄</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="알림 상태" }

![잠금 화면, 확장 시, 기기 활성 상태에서 표시되는 푸시 알림의 예시.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
확장된 푸시 알림에는 2:1 종횡비를 권장하지만, 거의 모든 종횡비가 지원됩니다. 이미지는 항상 알림의 전체 너비에 걸쳐 표시되며, 높이는 이에 맞게 조정됩니다.
{% endalert %}

#### 텍스트 잘림에 영향을 주는 변수 {#variables-in-text-truncation}

콘텐츠를 작성할 때, 표시되는 텍스트 양에 영향을 줄 수 있는 다음 시나리오를 고려하세요.

{% tabs %}
{% tab 타이밍 %}

사용자가 푸시 알림에 참여하는 시점에 따라 타임스탬프가 제목 텍스트를 줄일 수 있습니다.

![타임스탬프가 '지금'이고 제목 글자 수가 35인 푸시 알림 예시.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>제목 글자 수: **35**

![타임스탬프가 '3시간 전'이고 제목 글자 수가 33인 푸시 알림 예시.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>제목 글자 수: **33**

![타임스탬프가 '어제, 오전 8:37'이고 제목 글자 수가 22인 푸시 알림 예시.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>제목 글자 수: **22**

{% endtab %}
{% tab 이미지 %}

이미지가 있는 경우 본문 텍스트는 줄당 약 10자 정도 줄어듭니다.

![이미지가 없고 본문 글자 수가 179인 푸시 알림 예시.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>본문 글자 수: **179**

![이미지가 있고 본문 글자 수가 154인 푸시 알림 예시.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>본문 글자 수: **154**

{% endtab %}
{% tab 인터럽션 수준 %}

iOS 15에서는 시간 민감(Time Sensitive) 및 긴급(Critical) 표시가 제목을 타임스탬프 없이 새 줄로 밀어내어 약간 더 많은 공간을 제공합니다.

![시간 민감 또는 긴급 표시가 없고 제목 글자 수가 35인 푸시 알림 예시.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>제목 글자 수: **35**

![시간 민감 표시가 있고 제목 글자 수가 39인 푸시 알림 예시.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>제목 글자 수: **39**

{% endtab %}
{% tab 기타 %}

다음 세부 사항도 텍스트 잘림에 영향을 줄 수 있습니다:

- **휴대폰 디스플레이 설정:** 사용자가 접근성을 이유로 휴대폰의 전체 UI 글꼴 크기를 늘리거나 줄일 수 있습니다.
- **기기 너비:** 메시지가 작은 휴대폰이나 넓은 iPad에 표시될 수 있습니다.
- **콘텐츠 유형:** 이모지와 "m", "w" 같은 넓은 문자는 "i"나 "t"보다 더 많은 공간을 차지하며, "engagement"와 같은 긴 단어는 짧은 단어보다 더 갑작스럽게 줄바꿈될 수 있습니다.

{% endtab %}
{% endtabs %}

## iOS 리치 알림 설정하기 {#setting-up-your-ios-rich-notification}

### 1단계: 푸시 Campaign 생성 {#step-1-create-a-push-campaign}

[Campaign 생성]({{site.baseurl}}/user_guide/channels/push/create_a_push_message) 단계를 따라 iOS용 푸시 알림을 작성합니다. 리치 콘텐츠가 포함되지 않은 푸시 알림을 설정할 때와 동일한 작성기를 사용합니다.

### 2단계: 미디어 추가 {#step-2-add-media}

메시지 작성기의 **iOS Notification Image** 필드에 이미지, GIF, 오디오 또는 비디오 파일을 추가합니다. 콘텐츠 파일 추가 방법은 [요구 사항](#requirements)을 참조하세요.

![푸시 알림의 요약 텍스트 예시.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

이 메시지를 iOS 10 이상이 실행되는 기기를 가진 사용자에게만 전송하도록 제한할 수도 있습니다. iOS 10으로 업그레이드하지 않은 사용자의 경우, **Only send to devices with Rich Notification support** 옵션을 선택하지 않으면 리치 콘텐츠 없이 텍스트 전용 알림으로 표시됩니다.

![이미지를 추가하거나 이미지 URL을 입력할 수 있는 확장 알림 이미지 섹션.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### 3단계: Campaign 생성 계속하기 {#step-3-continue-creating-your-campaign}

리치 알림 콘텐츠가 대시보드에 업로드되면, [Campaign 스케줄 설정]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#choose-delivery-schedule-or-trigger)을 계속 진행할 수 있습니다.

사용자가 푸시 알림을 받으면 푸시 메시지를 세게 눌러 이미지를 확장할 수 있습니다.

![사용자가 푸시 알림을 받고 메시지를 세게 눌러 "Hello!"라고 표시된 확장 이미지를 보여주는 화면.]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }