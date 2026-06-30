---
nav_title: 특별 혜택이 포함된 이메일 가입
article_title: 특별 혜택이 포함된 이메일 가입
alias: "/email_offer/"
page_order: 6
description: "이 페이지에서는 인앱 메시지 드래그 앤 드롭 편집기를 사용하여 가입 시 특별 할인을 제공함으로써 이메일 목록을 구축하는 방법을 다룹니다."
---

# 특별 혜택이 포함된 이메일 가입 {#email-sign-up-with-special-offer}

> 인앱 메시지 드래그 앤 드롭 편집기를 사용하여 가입 시 특별 할인을 제공함으로써 이메일 목록을 구축하세요.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 특별 혜택이 포함된 이메일 가입 양식 만들기 {#creating-an-email-sign-up-form-with-a-special-offer}

### 1단계: 템플릿 선택 {#step-1-choose-your-template}

드래그 앤 드롭 인앱 메시지를 만들 때 템플릿으로 **Email sign-up with special offer**를 선택한 다음 **Build message**를 선택합니다. 이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.

![특별 혜택이 포함된 이메일 가입 양식 템플릿이 표시된 인앱 메시지 편집기.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_offer.png %})

### 2단계: 메시지 스타일 설정 {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### 3단계: 이메일 가입 구성요소 커스터마이즈 {#step-3-customize-your-email-sign-up-component}

이메일 가입 양식을 만들려면 **Email sign-up** 페이지를 선택한 다음 편집기에서 이메일 캡처 요소를 선택합니다. 기본적으로 수집된 이메일 주소는 글로벌 구독 그룹에서 **가입됨** 상태가 됩니다. 사용자를 특정 구독 그룹에 옵트인시키려면 [이메일 구독 상태 업데이트]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states)를 참조하세요.

이메일 캡처 요소의 입력 안내 텍스트와 레이블 텍스트를 커스터마이즈할 수 있습니다.

![이메일 캡처 요소를 커스터마이즈하기 위한 사이드 메뉴가 표시된 인앱 메시지 편집기.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_offer.png %})

#### 이메일 유효성 검사 {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### 4단계: 면책 조항 문구 추가(선택 사항) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### 5단계: 메시지 스타일 지정 {#step-5-style-your-message}

드래그 앤 드롭 [인앱 메시지 구성요소]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components)를 사용하여 특별 혜택의 디자인과 느낌을 커스터마이즈하세요.

## 결과 분석 {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## 모범 사례 {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}