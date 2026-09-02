---
nav_title: 단문 메시지 서비스, RCS, WhatsApp 가입 양식
article_title: 단문 메시지 서비스, RCS, WhatsApp 가입 양식
alias: "/phone_number_capture/"
page_order: 2
description: "이 페이지에서는 인앱 메시지 드래그 앤 드롭 에디터를 사용하여 단문 메시지 서비스, RCS, WhatsApp 가입 양식을 만드는 방법을 다룹니다."
---

# 단문 메시지 서비스, RCS, WhatsApp 가입 양식 {#sms-rcs-and-whatsapp-sign-up-form}

> 단문 메시지 서비스, RCS, WhatsApp 가입 양식은 인앱 메시지용 드래그 앤 드롭 에디터에서 사용할 수 있는 템플릿입니다. 이 템플릿을 사용하여 사용자의 전화번호를 수집하고 단문 메시지 서비스, MMS, RCS, WhatsApp 구독 그룹을 확장하세요.

![전화번호 가입 양식 템플릿을 사용하여 만든 인앱 메시지의 세 가지 예시.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 전화번호 가입 양식 만들기 {#creating-a-phone-number-sign-up-form}

### 1단계: 템플릿 선택 {#step-1-choose-your-template}

드래그 앤 드롭 인앱 메시지를 만들 때 템플릿으로 **단문 메시지 서비스 sign-up**(RCS 가입도 지원) 또는 **WhatsApp sign-up**을 선택한 다음 **Build message**를 선택합니다. 이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.

![인앱 메시지를 만들 때 단문 메시지 서비스 sign-up 또는 WhatsApp sign-up을 템플릿으로 선택하는 Modal.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### 2단계: 메시지 스타일 설정 {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![커스텀 폰트를 업로드하고 선택하는 워크플로.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### 3단계: 전화번호 입력 구성요소 커스터마이즈 {#step-3-customize-your-phone-number-input-component}

가입 양식 작성을 시작하려면 에디터에서 전화번호 입력 구성요소를 선택합니다.

![전화번호 입력 구성요소가 선택된 가입 양식 작성 시 미리보기 영역.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

사이드 메뉴에서 이 템플릿이 전화번호를 수집할 구독 그룹을 지정합니다. 컴플라이언스 모범 사례를 준수하기 위해 전화번호 가입 양식당 하나의 구독 그룹에 대한 동의만 수집할 수 있습니다. 그러나 원하는 경우 여러 양식을 사용하여 다른 구독 그룹에 대한 동의를 수집할 수 있습니다.

![구독 그룹이 선택된 구독 그룹 드롭다운.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

기본적으로 전 세계의 번호를 수집하지만, 번호를 수집할 국가를 제한할 수 있습니다. 이는 특정 국가의 전화번호를 가진 사용자에게만 메시지를 보내려는 경우에 유용하며, 목록 정리에도 도움이 됩니다. 이렇게 하려면 **Collect numbers from all countries**를 끄고 드롭다운을 사용하여 특정 국가를 선택합니다. 사용자는 명시적으로 추가한 국가만 선택할 수 있습니다.

![번호를 수집할 국가를 선택하는 국가 드롭다운.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### 유효하지 않은 전화번호 {#invalid-phone-numbers}

사용자가 허용되지 않는 특수 문자가 포함된 전화번호를 입력하면 커스터마이즈할 수 없는 일반 오류 표시가 나타나며 양식을 제출할 수 없습니다. **Preview & Test** 탭과 테스트 기기에서 오류 동작을 확인할 수 있습니다. [Braze가 전화번호를 포맷하는 방법]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#import-phone-numbers)에 대해 알아보려면 이 문서를 참조하세요.

### 4단계: 면책 조항 문구 추가(단문 메시지 서비스 및 RCS 가입 양식용) {#step-4-add-disclaimer-language-for-sms-and-rcs-sign-up-forms}

단문 메시지 서비스 및 RCS 가입 양식의 경우, 발송할 단문 메시지 서비스 또는 RCS의 유형을 명확하게 전달하는 것이 중요합니다. 양식에 다음 정보를 포함하여 목록 성장이 컴플라이언스를 준수하도록 하세요:

- 고객이 받을 수 있는 단문 메시지 서비스 및 RCS 메시지 유형에 대한 설명(장바구니 알림, 프로모션 및 할인, 예약 알림 등). 모든 사용 사례를 나열할 필요는 없지만, 브랜드가 발송할 메시지 유형에 대한 설명을 제공해야 합니다.
- 동의가 구매의 조건이 아니라는 안내(해당되는 경우).
- 메시지 빈도 및 메시지와 데이터 요금이 적용된다는 안내. 정확한 메시지 빈도를 모르는 경우 빈도가 달라질 수 있다고 안내할 수 있습니다.
- 이용약관 및 단문 메시지 서비스, RCS 개인정보 보호정책 링크.
- 도움말 및 수신 거부 키워드 안내(도움말은 HELP, 취소는 STOP).

템플릿에 예시용으로만 플레이스홀더 면책 조항을 제공했으며, 이는 법적 조언을 구성하지 않으며 컴플라이언스 목적으로 의존해서는 안 됩니다. 법무팀과 협력하여 특정 브랜드에 맞는 문구를 개발하는 것이 중요합니다.

{% alert note %}
이 설명서는 법적 조언을 제공하기 위한 것이 아니며, 법적 조언으로 전적으로 의존해서는 안 됩니다.
{% endalert %}

단문 메시지 서비스 및 RCS 컴플라이언스에 대한 자세한 내용은 [단문 메시지 서비스, MMS, RCS에 대한 법률 및 규정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)을 참조하세요.

### 5단계: 메시지 스타일 지정 {#step-5-style-your-message}

드래그 앤 드롭 [인앱 메시지 구성요소]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components)를 사용하여 메시지의 모양과 느낌을 커스터마이즈하세요.

## 결과 분석 {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

![인앱 메시지의 각 링크에 대한 클릭 수를 보여주는 인앱 메시지 성능 패널.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})