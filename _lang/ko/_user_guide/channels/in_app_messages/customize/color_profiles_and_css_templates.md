---
nav_title: 색상 프로필 및 CSS 템플릿
article_title: 색상 프로필 및 CSS 템플릿
page_order: 3
page_type: reference
description: "이 문서에서는 인앱 메시지 색상 프로필 및 CSS 템플릿에 대한 개요를 제공합니다."
channel:
  - in-app messages
---

# 색상 프로필 및 CSS 템플릿 {#reusable-color-profiles}

> 대시보드에서 인앱 메시지 및 인브라우저 메시지 템플릿을 저장하여 자신만의 스타일로 새로운 Campaign과 메시지를 빠르게 구축할 수 있습니다. 이 문서는 [기존 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)에 적용됩니다. 드래그 앤 드롭 편집기를 사용하는 경우 [스타일 설정]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/)을 참조하세요.

**템플릿** > **인앱 메시지 템플릿**으로 이동합니다.

이 페이지에서 기존 템플릿을 편집하거나 **+ 생성**을 클릭한 후 **색상 프로필** 또는 **CSS 템플릿**을 선택하여 인앱 메시지에 사용할 새 템플릿을 만들 수 있습니다.

## 색상 프로필 {#color-profile}

HEX 색상 코드를 입력하거나 색상 상자를 클릭하고 색상 선택기에서 색상을 선택하여 메시지 템플릿의 색상 구성을 커스텀할 수 있습니다.

완료되면 **Save Color Profile**을 클릭합니다.

### 색상 프로필 관리 {#managing-color-profiles}

템플릿을 [복제]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)하거나 [아카이브]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)할 수도 있습니다! 템플릿 및 크리에이티브 콘텐츠를 만들고 관리하는 방법에 대해 자세히 알아보려면 [템플릿 및 미디어]({{site.baseurl}}/user_guide/messaging/templates/)를 참조하세요.

## CSS 템플릿 {#in-app-message-templates}

[웹 모달 인앱 메시지](#web-modal-css)에 대한 완전한 CSS 템플릿을 커스텀할 수 있습니다.

CSS 템플릿의 이름을 지정하고 태그를 추가한 다음, 기본 템플릿으로 설정할지 여부를 선택합니다. 제공된 공간에 직접 CSS를 작성할 수 있습니다. 이 공간에는 메시지 미리보기에 표시된 CSS가 이미 채워져 있으며, 필요에 맞게 자유롭게 조정할 수 있습니다.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

보시다시피 배경색부터 글꼴 크기 및 두께 등 다양한 요소를 편집할 수 있습니다.

### CSS 템플릿 관리 {#managing-css-templates}

템플릿을 [복제]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)하거나 [아카이브]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)할 수도 있습니다! 템플릿 및 크리에이티브 콘텐츠를 만들고 관리하는 방법에 대해 자세히 알아보려면 [템플릿 및 미디어]({{site.baseurl}}/user_guide/messaging/templates/)를 참조하세요.

## CSS가 포함된 모달 (웹 전용) {#web-modal-css}

웹 전용 CSS 포함 웹 모달 메시지를 사용하도록 선택한 경우, 자체 템플릿을 적용하거나 제공된 공간에 직접 CSS를 작성할 수 있습니다. 이 공간에는 메시지 미리보기에 표시된 CSS가 이미 채워져 있지만, 필요에 맞게 자유롭게 조정할 수 있습니다.

자체 템플릿을 적용하려면 **Apply Template**을 클릭하고 인앱 메시지 템플릿 갤러리에서 선택합니다. 옵션이 없는 경우 CSS 템플릿 빌더를 사용하여 [CSS 템플릿]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/color_profiles_and_css_templates/#in-app-message-templates)을 업로드할 수 있습니다.