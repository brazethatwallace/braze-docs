---
nav_title: "커스텀 HTML의 동영상"
article_title: "커스텀 HTML의 동영상"
page_order: 4
page_type: reference
description: "이 문서에서는 HTML 인앱 메시지에 동영상을 삽입하는 방법을 설명합니다."
channel:
  - in-app messages
---

# 커스텀 HTML 인앱 메시지의 동영상 {#video}

> 이 문서는 [기존 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)의 [커스텀 HTML 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html)에 적용됩니다.

## 동영상 삽입 {#embed-videos}

HTML 인앱 메시지에서 동영상을 재생하려면 HTML에 다음 `<video>` 요소를 포함하고, 동영상 이름을 파일 이름(또는 원격 자산의 URL)으로 바꾸세요. 사용 가능한 다른 `<video>` 옵션은 [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)에서 확인할 수 있습니다.

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

로컬 동영상 자산을 사용하려면 Campaign에 자산을 업로드할 때 이 파일을 포함해야 합니다.

{% alert note %}
동영상 콘텐츠는 기기에서 로컬로 제공되는 동영상이 아닌 한, 기기의 네트워크 속도가 적절한 경우에만 사용할 수 있습니다.
{% endalert %}

## Android 고려 사항 {#android-considerations}

Android에서 HTML 인앱 메시지에 동영상 및 기타 HTML5 콘텐츠를 삽입하려면 인앱 메시지가 표시되는 Activity에서 하드웨어 가속이 활성화되어 있어야 합니다. 자세한 내용은 [Android 개발자 가이드]({{site.baseurl}}/developer_guide/in_app_messages/html_messages#android_embedding-youtube-content)를 참조하세요.

**자동 재생**: 하드웨어 가속이 활성화되어 있더라도 Android WebView에서는 미디어 재생을 시작하기 위해 사용자 제스처가 필요할 수 있습니다. 자동 재생이 필요한 경우, HTML 인앱 메시지를 렌더링하는 데 사용되는 WebView에서 [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean))를 설정하여 사용자 제스처 요구 사항을 비활성화하도록 구성하세요. 이를 위해서는 HTML 인앱 메시지 표시 방식에 대한 SDK 수준의 커스터마이징이 필요합니다. 설정 안내는 [Braze SDK의 인앱 메시지 커스터마이징]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android)을 참조하세요.

## iOS 고려 사항 {#ios-considerations}

iOS 기기를 지원하려면:

- 전체 화면 재생이 지원되지 않으므로 `playsinline` 속성을 포함해야 합니다.
- **iOS에서는 자동 재생이 보장되지 않습니다**. iOS 재생 동작은 `WKWebView` 및 OS 수준의 미디어 정책에 따라 달라지며, `autoplay`와 `muted`가 설정되어 있어도 사용자 제스처가 필요할 수 있습니다. 대상 iOS 버전 및 기기에서 HTML 인앱 메시지를 테스트하세요.

자동 재생이 필요한데 테스트 결과 기본적으로 작동하지 않는 경우, HTML 인앱 메시지에서 사용하는 `WKWebViewConfiguration`을 커스터마이징하여 미디어 재생 사용자 동작 요구 사항을 조정할 수 있습니다. 예를 들어 `mediaTypesRequiringUserActionForPlayback` 속성을 설정할 수 있습니다. 이를 위해서는 SDK 수준의 커스터마이징이 필요합니다. Swift 리소스는 [Braze SDK의 인앱 메시지 커스터마이징]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=swift) 및 [Swift용 WebView에 Braze JavaScript 인터페이스 추가]({{site.baseurl}}/developer_guide/in_app_messages/html_messages?sdktab=swift)를 참조하세요.

## 웹 고려 사항 {#web-considerations}

대부분의 최신 브라우저는 특정 조건(일반적으로 동영상이 음소거된 경우)에서만 자동 재생을 허용합니다. 웹 인앱 메시지에서 `autoplay`를 사용하는 경우 `muted`를 포함하고, 지원하는 브라우저 및 기기에서 테스트하세요. 브라우저 정책은 다양하며 일부 경우에는 여전히 사용자 제스처가 필요할 수 있습니다.

웹 인앱 메시지에서 YouTube 동영상을 자동 재생하려면 URL 파라미터 `&autoplay=1`을 추가하세요. 예를 들어, 다음 동영상은 자동 재생되고, 음소거되며(`&mute=1`), 컨트롤이 표시되지 않습니다(`&controls=0`):

```html
<iframe class="video" src="https://www.youtube.com/embed/VPIPAc4oQqw?autoplay=1&mute=1&controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## YouTube 동영상 표시 방식 {#how-youtube-videos-display}

- YouTube가 삽입된 인앱 메시지는 플랫폼에 따라 앱 내에서 직접 표시되거나 앱 내 별도의 탭에서 표시될 수 있습니다.
- YouTube 삽입이 표시될 때 인앱 메시지 텍스트가 표시되지 않을 수 있습니다.

## 문제 해결 {#troubleshooting}

인앱 메시지에 동영상이 표시되지 않는 경우:

- URL이 유효한지 확인하세요.
- `type="video/mp4"` 선언이 누락되지 않았는지 확인하세요(YouTube가 아닌 동영상의 경우).
- 누락된 닫는 태그를 추가하고 오타를 수정하세요.