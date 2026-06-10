---
nav_title: "메시지 및 이미지 형식"
article_title: "메시지 및 이미지 형식"
page_order: 1
page_type: reference
description: "이 문서에서는 푸시 알림의 메시지 및 이미지 형식에 대해 설명합니다."
channel: push

---

# 푸시 메시지 및 이미지 형식 {#push-message-and-image-formats}

> 이 참조 문서에서는 푸시 알림의 메시지 및 이미지 형식에 대해 설명합니다.

최상의 결과를 얻으려면 푸시 메시지를 작성할 때 다음 이미지 크기 및 메시지 길이 가이드라인을 참조하세요. 이미지 유무, 알림 상태(iOS), 사용자 기기의 표시 설정, 기기 크기에 따라 다소 차이가 있을 수 있습니다. 확실하지 않은 경우 문구를 짧고 간결하게 유지하세요.

## iOS 및 Android 푸시 {#ios-and-android-push}

{% tabs local %}
{% tab 이미지 %}

**이미지 유형** | **권장 이미지 크기** | **최대 이미지 크기** | **파일 유형**
--- | --- | --- | ---
(iOS) 2:1 *권장* | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG, GIF
(Android) 푸시 아이콘 | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG
(Android) 확장 알림 | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="iOS and Android push" }

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

{% endtab %}
{% tab 텍스트 %}

| 메시지 유형 | 권장 메시지 길이 (텍스트만) | 권장 메시지 길이 (리치)
--- | ---
(iOS) 잠금 화면 | 160자 | 130자
(iOS) 알림 센터 | 160자 | 130자
(iOS) 배너 알림 | 80자 | 65자
(Android) 잠금 화면 | 49자 | N/A
(Android) 알림 서랍 | 597자 | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS and Android push" }

iOS 푸시 알림에서 잘리지 않고 사용할 수 있는 글자 수가 궁금하신가요? [iOS 글자 수 가이드라인]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/#character-count)을 확인하세요.

{% endtab %}
{% tab 페이로드 크기 %}

**플랫폼** | **크기**
--- | ---
iOS 8 이전 | 0.256 KB
iOS 8 이후 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 aria-label="iOS and Android push" }

{% endtab %}
{% tab 이미지 예시 %}
{% subtabs %}
{% subtab iOS %}

![텍스트에 "Hi! This is an iOS Push with an image"라고 표시되고 이모지가 포함된 iOS 푸시 알림. 텍스트 옆에 작은 이미지가 있습니다.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![이전 메시지와 동일한 텍스트가 포함된 하드 푸시 iOS 푸시 알림으로, 텍스트 앞에 확장된 이미지가 표시됩니다.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![메시지 텍스트 아래에 큰 이미지가 있는 Android 푸시 알림.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
큰 이미지 알림은 최소 600x300 픽셀 이상의 이미지를 사용할 때 가장 잘 표시됩니다.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 텍스트 예시 %}
{% subtabs %}
{% subtab iOS %}

![텍스트에 "Hi! This is an iOS Push"라고 표시된 iOS 푸시 알림.]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
![홈 화면에 표시된 Android 푸시 알림.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 웹 푸시 {#web-push}

{% tabs local %}
{% tab 이미지 %}

| **브라우저** | **권장 아이콘 크기**
| --- | ---
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web push" }
Chrome | 192 x 192 이상
Firefox | 192 x 192 이상
Safari | 192 x 192 이상 (macOS 13 이상의 Safari 16 이상에서 Campaign별로 아이콘 구성 가능)
Opera | 192x192 이상
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web push" }

| **브라우저** | **플랫폼** | **큰 이미지 크기**
| --- | --- | ---
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web push" }
Chrome | Android | 2:1 종횡비
Firefox | Android | N/A
Chrome | Windows | 2:1 종횡비
Edge | Windows | 2:1 종횡비
Firefox | Windows | N/A
Firefox | Windows | 2:1 종횡비
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web push" }

{% endtab %}
{% tab 텍스트 %}

| **브라우저** | **플랫폼** | **최대 제목 길이**  | **최대 메시지 본문 길이**
| --- | --- | --- | ---
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Web push" }
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Web push" }

{% endtab %}
{% endtabs %}