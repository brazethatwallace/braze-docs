---
nav_title: 이메일 가입 양식
article_title: 이메일 가입 양식
alias: "/email_capture/"
page_order: 3
description: "이 페이지에서는 인앱 메시지 드래그 앤 드롭 편집기를 사용하여 이메일 가입 양식을 만드는 방법을 다룹니다."
---

# 이메일 가입 양식 {#email-sign-up-form}

> 드래그 앤 드롭 이메일 가입 인앱 메시지 템플릿을 사용하여 사용자의 이메일 주소를 수집하고 구독 그룹을 확장하세요.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 이메일 가입 양식 만들기 {#creating-an-email-sign-up-form}

### 1단계: 템플릿 선택 {#step-1-choose-your-template}

드래그 앤 드롭 인앱 메시지를 만들 때 템플릿으로 **Email sign-up**을 선택한 다음 **Build message**를 선택합니다. 이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.

![이메일 캡처 양식 템플릿이 있는 인앱 메시지 편집기.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### 2단계: 메시지 스타일 설정 {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### 3단계: 이메일 가입 구성요소 커스터마이즈 {#step-3-customize-your-email-sign-up-component}

이메일 가입 양식을 만들려면 편집기에서 이메일 캡처 요소를 선택합니다. 기본적으로 수집된 이메일 주소는 글로벌 구독 그룹 **가입됨** 상태가 됩니다. 특정 구독 그룹에 사용자를 옵트인하려면 [이메일 구독 상태 업데이트]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states)를 참조하세요.

이메일 캡처 요소의 입력 안내 텍스트와 레이블 텍스트를 커스터마이즈할 수 있습니다.

![이메일 캡처 요소를 커스터마이즈하기 위한 사이드 메뉴가 있는 인앱 메시지 편집기.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### 이메일 유효성 검사 {#email-validation}

사용자가 허용되지 않는 특수 문자가 포함된 이메일 주소를 입력하면 일반 오류 표시기가 나타나며 양식을 제출할 수 없습니다. 이 오류 메시지는 커스터마이즈할 수 없습니다. **미리보기 및 테스트** 탭과 테스트 기기에서 오류 동작을 확인할 수 있습니다. Braze가 이메일 주소 형식을 처리하는 방법에 대해 자세히 알아보려면 [이메일 유효성 검사]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation)를 참조하세요.

### 4단계: 면책 조항 문구 추가(선택 사항) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### 5단계: 메시지 스타일 지정 {#step-5-style-your-message}

드래그 앤 드롭 [인앱 메시지 구성요소]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components)를 사용하여 가입 양식의 디자인과 느낌을 커스터마이즈하세요.

## 결과 분석 {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## 모범 사례 {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}