---
nav_title: 리치 알림 생성
article_title: "Android용 리치 푸시 알림 생성"
page_order: 3
page_layout: tutorial
description: "이 튜토리얼에서는 Braze Campaigns에 대한 Android 리치 알림을 설정하는 방법을 다룹니다."
platform: Android
channel:
  - Push
tool:
  - Campaigns

---

# Android용 리치 푸시 알림 생성 {#create-rich-push-notifications-for-android}

> 리치 알림을 사용하면 단순한 텍스트 외에 추가 콘텐츠를 포함하여 푸시 알림을 더욱 다양하게 커스텀할 수 있습니다. Android 알림에는 이미 오래전부터 푸시 알림에 이미지를 포함하는 기능이 있었으며, 이를 "확장 알림 이미지"라고 합니다.

## 필수 조건 {#prerequisites}

Android용 리치 푸시 알림을 생성하기 전에 다음 세부 사항을 확인하세요:

- Android 확장 알림 이미지는 종횡비가 2:1이어야 하지만 크기 제한은 없습니다.
- Android에서는 표준 알림 보기에 별도의 이미지를 설정할 수도 있습니다. 권장 이미지 크기는 다음과 같습니다:
  - **소형:** 512x256
  - **중형:** 1024x512
  - **대형:** 2048x1024
- 현재 Android 리치 알림은 JPEG 및 PNG 이미지 형식을 포함한 정적 이미지만 지원합니다. GIF 및 기타 이미지 형식은 아직 지원되지 않습니다.
- 푸시 알림에 실행 버튼을 추가하면 표시 가능한 이미지 영역에 영향을 줄 수 있습니다. 대시보드 미리보기와 실제 기기에서 테스트하여 결과가 예상대로인지 확인하세요.
- 이미지를 렌더링하려면 Braze Android SDK가 활성화되어 있어야 합니다.

{% alert note %}
Braze에서 리치 푸시 설정 방법에 대한 안내를 제공하지만, 리치 푸시 알림의 실제 렌더링은 기기 종횡비, Android 버전, OEM별 제약 조건 등 외부 요인에 따라 달라질 수 있습니다. 리치 푸시 알림이 의도한 대로 표시되는지 확인하기 위해 여러 Android 기기에서 테스트 발송을 수행하는 것을 권장합니다.
{% endalert %}

## Android 리치 알림 설정하기 {#setting-up-your-android-rich-notification}

### 1단계: 푸시 Campaign 생성 {#step-1-create-a-push-campaign}

[Campaign 생성]({{site.baseurl}}/user_guide/channels/push/create_a_push_message) 단계를 따라 Android용 푸시 알림을 작성합니다. 리치 콘텐츠가 포함되지 않은 푸시 알림을 설정할 때와 동일한 작성기를 사용합니다.

### 2단계: 캡션 추가 {#step-2-add-captioning}

알림에서 이미지 앞에 표시할 **Summary Text**를 추가합니다.

![Dog이라는 반려동물 사료 앱에서 보낸 리치 푸시 알림으로, 요약 텍스트와 함께 Spot의 사료를 추가 주문할 시간임을 알려줍니다.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### 3단계: 미디어 추가 {#step-3-add-media}

메시지 작성기의 **Android Notification Image** 필드에 이미지를 추가합니다. 이미지는 대시보드를 통해 직접 업로드하거나 외부에서 호스팅되는 콘텐츠 URL을 지정하여 추가할 수 있습니다.

지원되는 이미지에 대한 자세한 내용은 [이미지 사양]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#image-specifications)을 확인하세요.

![이미지를 추가하거나 이미지 URL을 입력할 수 있는 Android 알림 이미지 섹션.]({% image_buster /assets/img_archive/android_rich_image.png %})

### 4단계: Campaign 생성 계속하기 {#step-4-continue-creating-your-campaign}

리치 알림 콘텐츠가 대시보드에 업로드되면 [Campaign 스케줄 설정]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)을 계속 진행할 수 있습니다.