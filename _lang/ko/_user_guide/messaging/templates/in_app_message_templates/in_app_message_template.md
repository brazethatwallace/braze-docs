---
nav_title: 인앱 메시지 템플릿 만들기
article_title: 인앱 메시지 템플릿 만들기
page_order: 0
description: "이 참조 문서에서는 Braze 대시보드의 템플릿 섹션에서 인앱 메시지 템플릿을 생성, 저장 및 관리하는 방법을 다루며, 기존 편집기를 위한 색상 프로필 및 CSS 템플릿도 포함합니다."
tool:
  - Templates
channel:
  - in-app messages
search_rank: 1
---

# 인앱 메시지 템플릿 만들기 {#create-an-in-app-message-template}

> **콘텐츠** > **인앱 메시지**를 사용하여 인앱 및 인브라우저 메시지 레이아웃의 재사용 가능한 라이브러리를 구축할 수 있습니다. 드래그 앤 드롭 편집기에서 디자인을 저장하거나, [기존 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)를 위한 **색상 프로필** 및 **CSS 템플릿** 자산을 생성할 수 있습니다.

## 1단계: 인앱 메시지 템플릿 열기 {#step-1-open-in-app-message-templates}

Braze 대시보드에서 **콘텐츠** > **인앱 메시지**로 이동합니다.

## 2단계: 템플릿 생성 방법 선택 {#step-2-choose-how-to-create-a-template}

템플릿을 추가하는 방법은 목표에 따라 다릅니다.

| 목표 | 수행 방법 |
|------|------------|
| 드래그 앤 드롭 레이아웃을 재사용하기 위해 저장 | [드래그 앤 드롭 인앱 메시지 작성기]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)에서 편집기를 종료한 후 **템플릿으로 저장**을 선택합니다(먼저 Campaign을 시작하거나 초안으로 저장해야 합니다). 템플릿은 다음 메시지를 위해 **템플릿** > **인앱 메시지 템플릿**에 표시됩니다. |
| 색상 프로필 또는 CSS 템플릿 생성(기존 편집기) | **인앱 메시지 템플릿** 페이지에서 **+ 생성**을 선택한 다음 **색상 프로필** 또는 **CSS 템플릿**을 선택합니다. 자세한 내용은 [색상 프로필 및 CSS 템플릿](#reusable-color-profiles)을 참조하세요. |
| Braze 템플릿 커스터마이즈 | 드래그 앤 드롭 편집기에서 [인앱 메시지를 생성]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)하고, Braze 템플릿을 선택한 후 커스터마이즈한 다음 **템플릿으로 저장**을 선택합니다. 각 Braze 템플릿에 대한 설명은 [인앱 메시지 템플릿]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: 템플릿 생성 방법 선택" }

{% alert note %}
색상 프로필과 CSS 템플릿은 기존 편집기에 적용됩니다. 드래그 앤 드롭 편집기를 사용하는 경우 메시지 수준 스타일링을 위해 [스타일 설정]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings)을 사용하세요.
{% endalert %}

## 3단계: 템플릿 관리 {#step-3-manage-your-templates}

**콘텐츠** > **인앱 메시지**에서 필터, 검색하거나 템플릿을 열어 편집할 수 있습니다. 다른 템플릿 유형과 마찬가지로 템플릿을 [복제]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicate-templates)하거나 [아카이브]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archive-templates)할 수 있습니다. 템플릿 및 미디어 워크플로에 대한 개요는 [템플릿]({{site.baseurl}}/user_guide/messaging/templates)을 참조하세요.

인앱 메시지 템플릿에 접근하려면 인앱 메시지 템플릿을 보거나 편집할 수 있는 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 필요합니다.

### 색상 프로필 및 CSS 템플릿 생성 {#reusable-color-profiles}

{% alert note %}
다음 옵션은 [기존 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)에 적용됩니다. 드래그 앤 드롭 편집기를 사용하는 경우 대신 [스타일 설정]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings)을 사용하세요.
{% endalert %}

기존 템플릿을 편집하거나 **+ 생성**을 선택하고 **색상 프로필** 또는 **CSS 템플릿**을 선택하여 인앱 메시지를 위한 새 템플릿을 만들 수 있습니다.

#### 색상 프로필 {#color-profile}

HEX 색상 코드를 입력하거나 색상 상자를 선택하고 색상 선택기에서 색상을 선택하여 메시지 템플릿의 색상 구성을 커스터마이즈할 수 있습니다. 기존 편집기에서 새 인앱 메시지를 만들 때 이 프로필을 기본값으로 적용하려면 **기본 프로필로 사용**을 선택합니다.

완료되면 **색상 프로필 저장**을 선택합니다.

![인앱 메시지 색상 프로필 템플릿 편집기.]({% image_buster /assets/img/drag_and_drop/templates/color_profile_template.png %})

#### CSS 템플릿 {#in-app-message-templates}

[웹 모달 인앱 메시지](#web-modal-css)를 위한 완전한 CSS 템플릿을 커스터마이즈할 수 있습니다.

CSS 템플릿의 이름을 지정하고 태그를 추가한 다음, 기본 템플릿으로 사용할지 여부를 선택합니다. 제공된 공간에 직접 CSS를 작성할 수 있습니다. 이 공간에는 메시지 미리보기에 표시된 CSS가 이미 채워져 있으며, 필요에 맞게 조정할 수 있습니다.

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

배경색부터 글꼴 크기 및 두께 등 모든 것을 편집할 수 있습니다.

#### CSS가 포함된 모달(웹 전용) {#web-modal-css}

웹 전용 CSS 포함 웹 모달 메시지를 사용하도록 선택한 경우, 자체 템플릿을 적용하거나 제공된 공간에 직접 CSS를 작성할 수 있습니다. 이 공간에는 메시지 미리보기에 표시된 CSS가 이미 채워져 있지만, 필요에 맞게 조정할 수 있습니다.

자체 템플릿을 적용하려면 **템플릿 적용**을 선택하고 인앱 메시지 템플릿 갤러리에서 선택합니다. 옵션이 없는 경우 **템플릿** > **인앱 메시지 템플릿**의 CSS 템플릿 빌더를 사용하여 [CSS 템플릿](#in-app-message-templates)을 추가할 수 있습니다.