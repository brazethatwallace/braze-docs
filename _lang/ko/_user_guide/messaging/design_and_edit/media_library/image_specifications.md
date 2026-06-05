---
nav_title: 이미지 사양
article_title: 이미지 사양
page_order: 1
page_type: reference
description: "이 참조 문서에서는 각 채널 유형에 대한 권장 이미지 크기 및 사양을 설명합니다."
tool:
  - Templates
  - Media

---

# 이미지 사양 {#image-specifications}

> 일반적으로 작고 고품질인 이미지가 더 빠르게 로드되므로, 원하는 결과를 달성할 수 있는 가장 작은 자산을 사용하는 것을 권장합니다. 특정 채널에서 이미지 활용을 극대화하려면 이 문서의 세부 정보를 참조하세요.

항상 다양한 기기에서 [메시지를 미리보기하고 테스트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/)하여 이미지와 메시지의 가장 중요한 영역이 예상대로 표시되는지 확인해야 합니다.

## 이미지 동작 {#image-behavior}

{% multi_lang_include image_specs.md variable_name='image behavior' %}

## 동영상 {#video}

미디어 라이브러리에 업로드된 동영상은 WhatsApp 메시지에서만 사용할 수 있습니다. 자세한 내용은 [WhatsApp 메시지 만들기]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#outbound-messages)를 참조하세요.

## GIF {#gifs}

GIF는 iOS 푸시, 인앱 메시지, 이메일, Content Cards, MMS 또는 RCS 메시지에서 지원됩니다. 매우 길쭉한 형태(예: 3000 x 2 픽셀)이거나 300프레임 이상인 GIF는 전체 파일 크기가 작더라도 업로드에 실패할 수 있습니다.

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

## 채널 가이드 {#channel-guidance}

### Content Cards

{% multi_lang_include image_specs.md variable_name='content cards' %}

### 이메일 {#email}

{% multi_lang_include image_specs.md variable_name='email' %}

### 인앱 메시지 {#in-app-messages}

{% multi_lang_include image_specs.md variable_name='in-app messages' %}

{% alert tip %} 자신 있게 자산을 만들어 보세요! 인앱 메시지 이미지 템플릿과 세이프 존 오버레이는 모든 크기의 기기에서 잘 작동하도록 설계되었습니다. [디자인 템플릿 ZIP 다운로드]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

자세한 내용은 [인앱 메시지 크리에이티브 세부 정보]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/)를 참조하세요.

#### Font Awesome

Braze는 모달 인앱 메시지 아이콘에 [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) 사용을 지원합니다.

### 푸시 알림 {#push-notifications}

{% multi_lang_include image_specs.md variable_name='payload size' %}

{% multi_lang_include image_specs.md variable_name='push notifications' %}

#### 권장 메시지 길이 {#recommended-message-lengths}

최상의 결과를 위해 푸시 메시지를 작성할 때 다음 메시지 길이 가이드라인을 참조하세요. 이미지 유무, 알림 상태(iOS), 사용자 기기의 표시 설정, 기기 크기에 따라 다소 차이가 있을 수 있습니다.

| 메시지 유형 | 권장 길이 (텍스트만) | 권장 길이 (리치) |
| --- | --- | --- |
| iOS 잠금 화면 | 160자 | 130자 |
| iOS 알림 센터 | 160자 | 130자 |
| iOS 배너 알림 | 80자 | 65자 |
| Android 잠금 화면 | 49자 | N/A |
| Android 알림 서랍 | 597자 | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="권장 메시지 길이" }

iOS 글자 수에 대한 자세한 내용은 [iOS 글자 수 가이드라인]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/#character-count)을 참조하세요.

#### 웹 푸시 {#web-push}

{% tabs %}
{% tab 이미지 %}

| 브라우저 | 권장 아이콘 크기 |
| --- | --- |
| Chrome | 192 x 192 px 이상 |
| Firefox | 192 x 192 px 이상 |
| Safari | 192 x 192 px 이상 (macOS 13+ Safari 16에서 캠페인별 설정 가능) |
| Opera | 192 x 192 px 이상 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="웹 푸시" }

| 브라우저 | 플랫폼 | 큰 이미지 크기 |
| --- | --- | --- |
| Chrome | Android | 2:1 종횡비 |
| Firefox | Android | N/A |
| Chrome | Windows | 2:1 종횡비 |
| Edge | Windows | 2:1 종횡비 |
| Firefox | Windows | N/A |
| Opera | Windows | 2:1 종횡비 |
| Chrome | macOS | N/A |
| Safari | macOS | N/A |
| Firefox | macOS | N/A |
| Opera | macOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="웹 푸시" }

{% endtab %}
{% tab 텍스트 %}

| 브라우저 | 플랫폼 | 최대 제목 길이 | 최대 본문 길이 |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="웹 푸시" }

{% endtab %}
{% endtabs %}

#### 푸시 알림 예시 {#push-notification-examples}

{% tabs %}
{% tab iOS %}

![텍스트에 "Hi! This is an iOS Push with an image"라고 표시되고 이모지가 포함된 iOS 푸시 알림. 텍스트 옆에 작은 이미지가 있습니다.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![하드 푸시 상태의 iOS 푸시 알림으로, 이전 메시지와 동일한 텍스트가 표시되며 텍스트 앞에 확장된 이미지가 있습니다.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![메시지 텍스트 아래에 큰 이미지가 있는 Android 푸시 알림.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
큰 이미지 알림은 최소 600 x 300 픽셀 이상의 이미지를 사용할 때 가장 잘 표시됩니다.
{% endalert %}

{% endtab %}
{% endtabs %}

추가 리소스는 [푸시 이미지 및 텍스트 사양]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)을 참조하세요.