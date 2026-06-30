---
nav_title: 다크 모드 테마
article_title: 다크 모드 테마
page_order: 2
description: "이 참조 문서에서는 다크 모드 테마 설정 방법 및 호환성 고려 사항을 포함하여 Braze 인앱 메시지의 다크 모드 지원에 대해 다룹니다."
channel:
  - in-app messages

---

# 다크 모드 테마 {#dark-mode-themes}

> 이 문서는 [기존 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)에 적용됩니다. 다크 모드는 사용자에게 시스템 전체 색상 환경설정을 지정할 수 있는 기능을 제공합니다([Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) 및 [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)에서 도입). "다크" 테마는 배터리 수명을 절약하고 사용자의 눈의 피로를 줄이는 동시에 앱 개발자에게 다크 색상 테마를 구현할 수 있는 방법을 제공하기 위한 것입니다.

Braze 인앱 메시지는 사용자의 환경설정에 따라 적절한 색상 메시지를 전달하고 앱 디자인과의 일관성을 유지할 수 있도록 대체 다크 테마 추가를 지원합니다.

## 다크 모드 작동 방식 {#how-dark-mode-works}

Android 10 이상 또는 iOS 13 이상 버전을 사용하는 사용자는 기기 설정에서 다크 모드를 켜거나 끌 수 있습니다.

다크 모드가 활성화되면 기기의 기본 메뉴와 화면(푸시 알림, 기기 설정 등)이 어두운 회색으로 변경됩니다. 앱 코드에서 대체 테마를 지정하여 다크 모드를 지원하도록 선택할 수도 있습니다.

## 다크 모드 테마 설정 {#setting-a-dark-mode-theme}

[인앱 메시지를 생성]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)할 때 **디자인** 탭에 있는 다크 모드를 사용하면 기기에서 다크 모드를 사용 중인 사용자를 위한 대체 색상 테마를 추가할 수 있습니다.

![인앱 메시지를 생성할 때 스타일 탭에서 라이트 모드 스타일과 다크 모드 스타일 간에 전환하는 사용자.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

이 옵션이 활성화되면 색상 선택기를 사용하거나 기존 [색상 프로필]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#color-profile)을 선택하여 기존 다크 또는 라이트 테마를 재사용함으로써 인앱 메시지의 다크 테마 색상을 선택할 수 있습니다.

{% alert note %}
앱에서 자체 다크 테마를 제공하지 않더라도 이 기능을 사용할 수 있습니다. 그러나 다크 모드를 지원하지 않는 기기에서는 기본적으로 라이트 테마가 표시됩니다. 인앱 메시지가 표시되는 동안 Android에서 기기 테마를 변경해도 해당 인앱 메시지에 사용되는 테마는 변경되지 않습니다.
{% endalert %}

### 다크 모드를 일관되게 사용하기 {#using-dark-mode-consistently}

모든 인앱 메시지에 다크 모드를 사용하려면 먼저 다크 모드 테마에 맞는 색상 프로필을 생성합니다.

1. **콘텐츠** > **인앱 메시지**로 이동합니다.
2. **템플릿 생성**을 선택하고 드롭다운에서 [색상 프로필]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#color-profile)을 선택합니다.
3. 색상 프로필을 생성하고 저장합니다.

인앱 메시지의 다크 모드 버전을 생성할 때 해당 색상 프로필을 선택하면 인앱 메시지의 외관을 일관되게 유지할 수 있습니다.

## 호환성 {#compatibility}

- 사용자의 iOS 기기 버전이 13 이상이거나 Android 기기 버전이 10 이상이어야 합니다.
- Braze iOS SDK v3.21.0 이상, Braze Android SDK v3.8.0 이상이 필요합니다.

{% alert note %}
다크 모드 앱은 Android 10 및 iOS 13에서 도입되었습니다. 최소한 이 버전으로 휴대폰을 업그레이드하지 않은 사용자에게는 라이트 테마만 표시됩니다. <br><br>사용자의 다크 모드 설정이나 OS 버전에 관계없이, 선택한 오디언스에 적합한 모든 사용자에게 Campaign(캠페인)이 계속 제공됩니다.
{% endalert %}

## HTML 인앱 메시지 사용 {#using-html-in-app-messages}

HTML 인앱 메시지에 다크 및 라이트 테마를 생성하려면 [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS 미디어 기능을 사용하여 사용자의 환경설정을 감지할 수 있습니다.

예시:

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

