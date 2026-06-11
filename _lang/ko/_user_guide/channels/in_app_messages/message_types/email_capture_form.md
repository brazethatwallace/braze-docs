---
nav_title: 이메일 캡처 양식
article_title: 이메일 캡처 양식
page_order: 5
page_type: reference
description: "이 문서에서는 이메일 캡처 인앱 메시지 유형에 대한 개요를 제공합니다."
channel:
  - in-app messages
---

# 이메일 캡처 양식 {#email-capture-form}

> 이메일 캡처 메시지를 사용하면 사이트 사용자에게 이메일 주소를 제출하도록 안내할 수 있습니다. Braze는 해당 주소를 고객 프로필에 추가하여 모든 메시징 캠페인에서 활용할 수 있도록 합니다.

이 메시지 유형은 [기존 에디터]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)에서 사용할 수 있습니다.

## 작동 방식 {#how-it-works}

최종 사용자가 이 양식에 이메일 주소를 입력하면, Braze가 해당 이메일 주소를 고객 프로필에 추가합니다.

- 아직 계정이 없는 [익명 사용자]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#anonymous-user-profiles)의 경우, 이메일 주소는 사용자의 기기에 연결된 익명 사용자 프로필에 저장됩니다.
- 고객 프로필에 이메일 주소가 이미 존재하는 경우, 새로 입력된 이메일 주소가 기존 이메일 주소를 덮어씁니다.
- 알려진 사용자의 이메일 주소가 [하드바운스]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary/#hard-bounce)로 표시된 경우, Braze는 새로 입력된 이메일 주소가 Braze 프로필에 있는 주소와 다른지 확인합니다. 제공된 이메일 주소가 다르면 Braze가 이메일 주소를 업데이트하고 하드바운스 상태를 제거합니다.
- 사용자가 유효하지 않은 이메일 주소를 입력하면 "Please enter a valid email."이라는 오류 메시지가 표시됩니다.
    - 유효하지 않은 이메일 주소:
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - 유효한 이메일 주소:
        - `example@gmail.com`
        - `example@gnail.com` (오타 포함)
    - Braze에서의 이메일 유효성 검사에 대한 자세한 내용은 [이메일 기술 가이드라인 및 참고 사항]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/)을 참조하세요.

{% details 식별된 사용자와 익명 사용자에 대한 추가 정보 %}

이메일 캡처 양식은 현재 활성 상태인 Braze 고객 프로필에 이메일 주소를 설정합니다. 사용자가 식별되었는지(로그인 상태, `changeUser` 호출됨) 여부에 따라 동작이 달라집니다.

익명 사용자가 양식에 이메일을 입력하고 제출하면, Braze가 해당 프로필에 이메일 주소를 추가합니다. 이후 웹 여정에서 `changeUser`가 호출되고 새로운 `external_id`가 할당되면(예: 새 사용자가 서비스에 등록할 때), 이메일 주소를 포함한 모든 익명 사용자 프로필 데이터가 병합됩니다.

기존 `external_id`로 `changeUser`가 호출되면, 익명 사용자 프로필은 분리되고 식별된 사용자에 아직 존재하지 않는 [특정 고객 프로필 데이터 필드]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)가 병합되지만, 이미 존재하는 필드는 이메일 주소를 포함하여 손실됩니다.

자세한 내용은 [고객 프로필 수명주기]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)를 참조하세요.

{% enddetails %}

## 1단계: 인앱 메시지 Campaign 생성 {#step-1-create-an-in-app-message-campaign}

이 옵션으로 이동하려면 인앱 메시징 Campaign을 생성해야 합니다. 그런 다음 사용 사례에 따라 **Send To**를 **Web Browsers**, **Mobile Apps** 또는 **Both Mobile Apps & Web Browsers**로 설정하고, **Message Type**으로 **Email Capture Form**을 선택합니다.

{% alert note %}
**웹 사용자를 타겟팅하시나요?** <br>Web SDK를 통해 HTML 인앱 메시지를 활성화하려면 Braze에 `allowUserSuppliedJavascript` 초기화 옵션을 제공해야 합니다. 예: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. 이는 보안상의 이유로, HTML 인앱 메시지가 JavaScript를 실행할 수 있기 때문에 사이트 관리자가 이를 활성화해야 합니다.
{% endalert %}

## 2단계: 양식 커스터마이즈 {#customizable-features}

다음으로 필요에 따라 양식을 커스터마이즈합니다. 이메일 캡처 양식에서 다음 기능을 커스터마이즈할 수 있습니다:

- 헤더, 본문 및 제출 버튼 텍스트
- 선택 사항 이미지
- 선택 사항 "서비스 이용약관" 링크
- 헤더 및 본문 텍스트, 버튼, 배경의 다양한 색상
- 키-값 페어
- 헤더 및 본문 텍스트, 버튼, 버튼 테두리 색상, 배경 및 오버레이 스타일
- 제출 버튼
    - 제출 버튼은 사용자가 유효한 이메일 주소를 입력한 후에만 표시됩니다. 이를 통해 완전한 이메일 주소를 수집할 수 있습니다.

![이메일 캡처 양식 작성기.]({% image_buster /assets/img/email_capture.png %})

추가 커스터마이즈가 필요한 경우, **Message Type**으로 **Custom Code**를 선택하세요. [Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) GitHub 리포지토리에서 이 [이메일 캡처 모달 템플릿](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal)을 시작 코드로 사용할 수 있습니다.

## 3단계: 진입 오디언스 설정 {#step-3-set-your-entry-audience}

인앱 메시지를 사용하여 사용자 이메일을 캡처하는 경우, 이미 이 정보를 제공한 사용자를 제외하도록 오디언스를 제한할 수 있습니다.

- **이메일 주소가 없는 사용자를 타겟팅하려면:** `Email Available`이 `false`인 필터를 사용합니다. 이렇게 하면 이메일이 등록되지 않은 사용자에게만 양식이 표시되어, 이미 알려진 사용자에게 불필요한 안내를 방지할 수 있습니다.
- **외부 ID가 없는 익명 사용자를 타겟팅하려면:** `External User ID`가 `is blank`인 필터를 사용합니다. 이는 아직 인증되지 않았거나 등록하지 않은 사용자를 식별하려는 경우에 유용합니다.

원하는 경우 `AND` 로직을 사용하여 두 필터를 결합할 수도 있습니다. 이렇게 하면 이메일 주소와 외부 사용자 ID가 모두 없는 사용자에게만 양식이 표시되며, 새로운 리드를 확보하거나 계정 생성을 유도하는 데 이상적입니다.

## 4단계: 양식을 작성한 사용자 타겟팅 (선택 사항) {#step-4-target-users-who-filled-out-the-form-optional}

이메일 캡처 양식을 시작하고 사용자로부터 이메일 주소를 수집한 후, 양식을 작성한 사용자를 타겟팅할 수 있습니다.

1. Braze의 Segment 필터에서 `Clicked/Opened Campaign` 필터를 선택합니다.
2. 드롭다운에서 `clicked in-app message button 1`을 선택합니다.
3. 이메일 캡처 양식 Campaign을 선택합니다.