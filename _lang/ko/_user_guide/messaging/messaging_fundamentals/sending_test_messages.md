---
nav_title: 테스트 메시지 보내기
article_title: 테스트 메시지 보내기
page_order: 11.5
tool:
  - Campaigns
  - Canvas
page_type: reference
description: "이 참조 문서에서는 다양한 Braze 채널에서 테스트 메시지를 보내는 방법과 커스텀 이벤트 속성정보 또는 사용자 속성을 포함하는 방법을 다룹니다."
---

# 테스트 메시지 보내기 {#send-test-messages}

> 사용자에게 메시징 캠페인을 보내기 전에, 메시지가 올바르게 표시되고 의도한 대로 작동하는지 확인하기 위해 테스트하는 것을 권장합니다. Braze 대시보드의 도구를 사용하여 선택한 기기 또는 팀원에게 테스트 메시지를 생성하고 보낼 수 있습니다.

{% alert important %}
테스트 후에는 캠페인 초안을 저장하여 캠페인이 삭제되지 않도록 하세요. 메시지를 초안으로 저장하지 않고도 테스트 메시지를 보낼 수 있습니다.
{% endalert %}

## 1단계: 테스트 사용자 식별하기 {#step-1-identify-your-test-users}

메시징 캠페인을 테스트하기 전에 테스트 사용자를 식별하는 것이 중요합니다. 이러한 사용자는 기존 사용자 ID 또는 이메일 주소일 수도 있고, 메시징 캠페인 테스트 전용으로 사용되는 새 사용자일 수도 있습니다.

### 선택 사항: 콘텐츠 테스트 그룹 만들기 {#optional-create-a-content-test-group}

테스트 사용자를 구성하는 편리한 방법은 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)을 만드는 것입니다. 콘텐츠 테스트 그룹에는 Campaigns에서 테스트 메시지를 받을 사용자 그룹이 포함됩니다. 이 테스트 그룹을 Campaign의 **테스트 수신자** 아래에 있는 **콘텐츠 테스트 그룹 추가** 필드에 추가하면, 개별 테스트 사용자를 만들거나 추가하지 않고도 테스트를 시작할 수 있습니다.

## 2단계: 채널별 테스트 메시지 보내기 {#step-2-send-channel-specific-test-messages}

테스트 메시지 전송 방법은 아래에서 해당 채널 섹션을 참조하세요.

{% tabs local %}
{% tab 배너 %}

{% alert important %}
Braze에서 배너 메시지를 테스트하려면 먼저 Braze에서 배너 Campaign을 만들어야 합니다. 또한 테스트하려는 배치가 이미 [앱 또는 웹사이트에 배치]({{site.baseurl}}/developer_guide/banners/placements)되어 있는지 확인하세요.
{% endalert %}

배너 메시지를 만든 후 배너를 미리 보거나 테스트 메시지를 보낼 수 있습니다.

1. 배너 메시지를 작성합니다.
2. **미리보기**를 선택하여 배너를 미리 보거나 테스트 메시지를 보냅니다.
3. 테스트 메시지를 보내려면 콘텐츠 테스트 그룹 또는 한 명 이상의 개별 사용자를 **테스트 수신자**로 추가한 다음 **테스트 전송**을 선택합니다.

테스트 메시지는 최대 5분 동안 기기에서 확인할 수 있습니다.

![배너 작성기의 미리보기 탭입니다.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
하드웨어 차이로 인해 미리보기가 사용자 기기에서의 최종 렌더링과 동일하지 않을 수 있다는 점을 유의하세요.
{% endalert %}

### 테스트 체크리스트 {#test-checklist}

- 배너 Campaign이 배치에 할당되어 있나요?
- 타겟 기기 유형과 화면 크기에서 이미지와 미디어가 예상대로 표시되고 작동하나요?
- 링크와 버튼이 사용자를 올바른 위치로 안내하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않을 경우를 대비해 기본 속성 값을 설정했나요?
- 문구가 명확하고 간결하며 정확한가요?

{% endtab %}
{% tab Content Cards %}

{% alert important %}
[콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) 또는 개별 사용자에게 테스트를 보내려면, 전송 전에 테스트 기기에서 푸시가 활성화되어 있어야 하며 테스트 사용자에 대해 유효한 푸시 토큰이 등록되어 있어야 합니다. iOS 사용자의 경우 테스트 Content Cards를 보려면 Braze에서 보낸 푸시 알림을 탭해야 합니다. 이 동작은 테스트 Content Cards에만 적용됩니다.
{% endalert %}

테스트 Content Cards는 푸시 알림을 통해 전달됩니다. 카드는 푸시 페이로드에 포함되며, 푸시가 수신되면 SDK가 이를 추출하여 로컬에 캐시합니다.

이 프로세스는 일반적인 카드 전달 시스템을 우회하므로 Content Cards를 테스트하더라도 푸시가 활성화되어 있어야 합니다.

테스트 Content Cards는 전송 후 약 5분이 지나면 만료됩니다.

Content Cards를 만든 후 앱으로 테스트 Content Cards를 보내 실시간으로 어떻게 보이는지 확인할 수 있습니다.

1. Content Cards를 작성합니다.
2. **테스트** 탭을 선택하고 이 테스트 메시지를 받을 콘텐츠 테스트 그룹 또는 개별 사용자를 하나 이상 선택합니다.
3. **테스트 전송**을 선택하여 앱으로 Content Cards를 전송합니다.

![Content Cards 테스트]({% image_buster /assets/img/contentcard_test.png %})

### 미리보기 {#preview}

**미리보기** 탭에서 카드를 작성하면서 미리 볼 수 있습니다. 이를 통해 사용자 관점에서 최종 메시지가 어떻게 보일지 시각화할 수 있습니다.

{% alert note %}
작성기의 **미리보기** 탭에서 메시지 표시가 사용자 기기에서의 실제 렌더링과 동일하지 않을 수 있습니다. 미디어, 문구, 개인화 및 커스텀 속성이 올바르게 생성되는지 확인하려면 항상 기기로 테스트 메시지를 보내는 것을 권장합니다.
{% endalert %}

### 테스트 체크리스트

- 테스트 사용자가 유효한 푸시 토큰으로 푸시를 수신 동의했나요?
- 이미지와 미디어가 예상대로 표시되고 작동하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않을 경우 [기본 속성 값]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values)을 설정했나요?
- 문구가 명확하고 간결하며 정확한가요?
- 링크가 사용자를 올바른 위치로 안내하나요?
- 테스트 사용자가 유효한 푸시 토큰으로 푸시를 수신 동의했나요?

### 깨진 이미지 문제 해결 {#troubleshooting-broken-images}

Content Cards 이미지가 렌더링되지 않거나 깨져 보이는 경우:

- **URL이 올바르고 URL 인코딩되어 있는지 확인합니다:** URL의 특수 문자(공백 또는 쿼리 매개변수 등)는 올바르게 인코딩되어야 합니다. 그렇지 않으면 이미지 요청이 실패합니다.
- **콘텐츠 보안 정책을 확인합니다:** 조직에 콘텐츠 보안 정책(CSP)이나 내부 IT 보안 규칙이 있는 경우 해당 정책이 이미지 도메인을 차단할 수 있습니다. 이미지 URL의 도메인이 CSP에서 허용되는지 확인하세요.
- **HTTPS를 사용합니다:** 이미지 URL은 브라우저 및 앱에서의 혼합 콘텐츠 차단을 방지하기 위해 `http://` 대신 `https://`를 사용해야 합니다.
- **브라우저에서 URL을 직접 엽니다:** 브라우저에서 이미지가 로드되지 않으면 문제는 이미지 URL 또는 호스팅에 있는 것이며, Braze의 문제가 아닙니다.

### 디버그 {#debug}

Content Cards가 전송된 후 개발자 콘솔의 [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)에서 문제를 분석하거나 디버그할 수 있습니다.

일반적인 사용 사례는 사용자가 특정 Content Cards를 볼 수 없는 이유를 디버그하는 것입니다. 이를 위해 **이벤트 사용자 로그**에서 세션 시작 시 SDK에 전달된 Content Cards를 확인하고, 노출 전에 특정 Campaign으로 추적할 수 있습니다:

1. **설정** > **이벤트 사용자 로그**로 이동합니다.
2. 테스트 사용자의 SDK 요청을 찾아 펼칩니다.
3. **원시 데이터**를 클릭합니다.
4. 세션의 `id`를 찾습니다. 다음은 예시입니다:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

{: start="5"}
5. [Base64 Decode and Encode](https://www.base64decode.org/)와 같은 디코딩 도구를 사용하여 Base64 형식의 `id`를 디코딩하고 연관된 `campaign_id`를 찾습니다. 이 예시에서는 다음과 같은 결과가 나옵니다:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    여기서 `4861692e-6fce-4215-bd05-3254fb9e9057`이 `campaign_id`입니다.<br><br>

6. **Campaigns** 페이지로 이동하여 `campaign_id`를 검색합니다.

![Campaigns 페이지에서 campaign_id 검색]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

여기서 메시지 설정과 콘텐츠를 검토하여 사용자가 특정 Content Cards를 볼 수 없는 이유를 파악할 수 있습니다.

{% endtab %}
{% tab 이메일 %}

1. 이메일 메시지를 작성합니다.
2. **미리보기 및 테스트**를 선택합니다.
3. **테스트 전송** 탭을 선택하고 **개별 사용자 추가** 필드에 이메일 주소 또는 사용자 ID를 추가합니다.
4. **테스트 전송**을 선택하여 작성한 이메일을 받은편지함으로 보냅니다.

![이메일 테스트]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

이메일에 [기본 설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) 링크가 포함된 경우, 테스트 전송으로는 작동하는 링크가 생성되지 않으며 기본 설정을 저장할 수도 없습니다. 기본 설정 센터를 테스트하려면 테스트 사용자 또는 소규모 내부 Segment에 메시지를 실행하세요. 자세한 내용은 [기본 설정 센터 테스트]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers)를 참조하세요.

이메일 Campaign에 큰 이미지가 포함되어 있고 Outlook에서 예상대로 표시되지 않는 경우, CSS 또는 HTML로만 크기를 조정하는 대신 이미지 편집 또는 리사이징 도구를 사용하여 이미지의 실제 파일 크기를 줄이는 것을 고려하세요.

{% endtab %}
{% tab 인앱 메시지 %}

{% alert warning %}
[콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) 또는 개별 사용자에게 테스트를 보내려면 전송 전에 테스트 기기에서 푸시가 활성화되어 있어야 합니다. 예를 들어, 테스트 메시지가 표시되기 전에 알림을 탭하려면 iOS 기기에서 푸시가 활성화되어 있어야 합니다. {% endalert %}

앱 및 테스트 기기에서 푸시 알림이 설정되어 있다면 앱으로 테스트 인앱 메시지를 보내 실시간으로 어떻게 보이는지 확인할 수 있습니다.

1. 인앱 메시지를 작성합니다.
2. **테스트** 탭을 선택하고 **개별 사용자 추가** 필드에 이메일 주소 또는 사용자 ID를 추가합니다.
3. **테스트 전송**을 선택하여 기기로 푸시 메시지를 전송합니다.

테스트 푸시 메시지가 기기 화면 상단에 표시됩니다.

![인앱 메시지 테스트]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
테스트 전송 시 각 수신자에게 인앱 메시지가 두 개 이상 전송될 수 있습니다.
{% endalert %}

푸시 메시지를 직접 클릭하여 열면 앱으로 이동하여 인앱 메시지 테스트를 확인할 수 있습니다. 이 인앱 메시지 테스트 기능은 사용자가 테스트 푸시 알림을 클릭하여 인앱 메시지를 트리거하는 방식에 의존합니다. 따라서 테스트 푸시 알림이 성공적으로 전달되려면 사용자가 해당 앱에서 푸시 알림을 받을 수 있는 자격이 있어야 합니다.

### 미리보기

**미리보기** 탭에서 인앱 메시지를 작성하면서 미리 볼 수 있습니다. 이를 통해 사용자 관점에서 최종 메시지가 어떻게 보일지 시각화할 수 있습니다. 무작위 사용자, 특정 사용자 또는 커스텀 사용자로 미리 볼 수 있습니다. 또한 모바일 기기 또는 태블릿에서 메시지를 미리 볼 수도 있습니다.

![인앱 메시지 작성 시 메시지 미리보기를 보여주는 작성 탭입니다. 사용자가 선택되지 않아 본문에 추가된 Liquid가 그대로 표시됩니다.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze에는 세 세대의 인앱 메시지가 있습니다. 지원하는 세대에 따라 메시지를 전송할 기기를 세밀하게 조정할 수 있습니다.

![인앱 메시지 미리보기 시 세대 간 전환하기]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
**미리보기**에서 메시지 표시가 사용자 기기에서의 실제 렌더링과 동일하지 않을 수 있습니다. 미디어, 문구, 개인화 및 커스텀 속성이 올바르게 생성되는지 확인하려면 항상 기기로 테스트 메시지를 보내는 것을 권장합니다.
{% endalert %}

### 테스트 체크리스트

- 이미지와 미디어가 예상대로 표시되고 작동하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않을 경우 [기본 속성 값]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values)을 설정했나요?
- 문구가 명확하고 간결하며 정확한가요?
- 버튼이 사용자를 올바른 위치로 안내하나요?

### 접근성 스캐너 {#accessibility-scanner}

접근성 모범 사례를 지원하기 위해 Braze는 기존 HTML 편집기를 사용하여 작성된 인앱 메시지의 콘텐츠를 접근성 표준에 따라 자동으로 검사합니다. 이 스캐너는 웹 콘텐츠 접근성 지침([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) 표준을 충족하지 못할 수 있는 콘텐츠를 식별하는 데 도움이 됩니다. WCAG는 장애가 있는 사용자가 웹 콘텐츠에 더 쉽게 접근할 수 있도록 월드 와이드 웹 컨소시엄(W3C)이 개발한 국제적으로 인정된 기술 표준입니다.

![접근성 검사 결과]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
인앱 메시지 접근성 스캐너는 커스텀 HTML로 작성된 메시지에서만 실행됩니다.
{% endalert %}

#### 작동 방식 {#how-it-works}

스캐너는 커스텀 HTML 메시지에서 자동으로 실행되며 전체 HTML 메시지를 [WCAG 2.1 AA 규칙 세트](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) 전체에 대해 평가합니다. 플래그가 지정된 각 문제에 대해 다음 정보를 표시합니다:

- 관련된 특정 HTML 요소
- 접근성 문제에 대한 설명
- 추가 컨텍스트 또는 해결 지침 링크

#### 자동화된 접근성 테스트 이해 {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. LINE 메시지를 작성합니다.
2. **테스트** 탭을 선택하고 이 테스트 메시지를 받을 콘텐츠 테스트 그룹 또는 개별 사용자를 하나 이상 선택합니다.
3. **테스트 전송**을 선택하여 메시지를 전송합니다.

![LINE 메시지 테스트]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab 푸시 %}

#### 모바일 푸시 {#mobile-push}

1. 모바일 푸시를 작성합니다.
2. **테스트** 탭을 선택하고 **개별 사용자 추가** 필드에 이메일 주소 또는 사용자 ID를 추가합니다.
3. **테스트 전송**을 선택하여 작성한 메시지를 기기로 전송합니다.

![푸시 테스트]({% image_buster /assets/img_archive/testpush.png %})

선택한 사용자 중 일치하는 푸시 토큰이 없다는 오류가 표시되면, 테스트 사용자에게 선택한 플랫폼에 대한 유효한 푸시 토큰이 없는 것입니다. 사용자가 앱에서 세션을 시작하고 해당 기기에서 푸시를 활성화해야 합니다. 자세한 내용은 [푸시 활성화 및 푸시 구독]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states)을 참조하세요.

#### 웹 푸시 {#web-push}

1. 웹 푸시를 작성합니다.
2. **테스트** 탭을 선택합니다.
3. **나에게 테스트 전송**을 선택합니다.
4. **테스트 전송**을 선택하여 웹 브라우저로 웹 푸시를 전송합니다.

![웹 푸시 테스트]({% image_buster /assets/img_archive/testwebpush.png %})

Braze 대시보드에서 푸시 메시지를 이미 수락한 경우 화면 모서리에 메시지가 표시됩니다. 그렇지 않은 경우 프롬프트가 표시되면 **허용**을 선택하면 메시지가 표시됩니다.

선택한 사용자 중 웹 푸시에 대해 일치하는 푸시 토큰이 없다는 오류가 표시되면, 테스트 사용자에게 선택한 플랫폼에 대한 유효한 푸시 토큰이 등록되어 있는지 확인하세요. 푸시 토큰을 받으려면 사용자가 자신의 기기에서 해당 앱에 대한 푸시 알림을 받도록 구성되어 있어야 합니다. 자세한 내용은 [푸시 활성화 및 푸시 구독]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states)을 참조하세요.

{% endtab %}
{% tab SMS/MMS 및 RCS %}

SMS, MMS 또는 RCS 메시지를 만든 후 휴대폰으로 테스트 메시지를 보내 실시간으로 어떻게 보이는지 확인할 수 있습니다. 수신자는 테스트 전송 시 선택한 SMS 구독 그룹에 속해 있어야 하며, 유효한 전화번호가 있어야 하고, **지역 권한** 아래에 최소 하나의 국가가 선택되어 있어야 합니다. 자세한 내용은 [SMS FAQ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages)를 참조하세요.

1. SMS, MMS 또는 RCS 메시지를 작성합니다.
2. **테스트** 탭을 선택하고 이 테스트 메시지를 받을 콘텐츠 테스트 그룹 또는 개별 사용자를 하나 이상 선택합니다.
3. **테스트 전송**을 선택하여 테스트 메시지를 전송합니다.

![SMS/MMS 테스트]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab 웹훅 %}

웹훅을 만든 후 테스트 전송을 수행하여 웹훅 응답을 확인할 수 있습니다. **테스트** 탭을 선택하고 **테스트 전송**을 선택하여 지정된 웹훅 URL로 테스트 전송을 보냅니다. 또한 개별 사용자를 선택하여 특정 사용자로서 응답을 미리 볼 수도 있습니다.

{% endtab %}
{% tab WhatsApp %}

1. WhatsApp 메시지를 작성합니다.
2. **테스트** 탭을 선택하고 이 테스트 메시지를 받을 콘텐츠 테스트 그룹 또는 개별 사용자를 하나 이상 선택합니다.
3. 이 메시지에 사용하는 구독 그룹에 연결된 전화번호로 WhatsApp 메시지를 보내 대화 창을 시작합니다. 연결된 전화번호는 **테스트** 탭의 알림에 표시됩니다.
4. **테스트 전송**을 선택하여 메시지를 전송합니다.

![WhatsApp 메시지 테스트]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## 개인화된 캠페인 테스트 {#test-personalized-campaigns}

사용자 데이터를 채우거나 커스텀 이벤트 속성정보를 사용하는 캠페인을 테스트하는 경우, 추가적이거나 다른 단계를 수행해야 합니다.

### 사용자 속성으로 개인화된 캠페인 테스트 {#testing-campaigns-personalized-with-user-attributes}

메시지에서 [개인화]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/overview)를 사용하는 경우, 캠페인을 올바르게 미리 보고 사용자 데이터가 콘텐츠에 제대로 채워지는지 확인하려면 추가 단계를 수행해야 합니다.

테스트 메시지를 보낼 때 **Select Existing User**를 선택하거나 **Custom User**로 미리 보기 옵션을 선택하세요.

![개인화된 메시지 테스트]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### 기존 사용자 선택 {#selecting-an-existing-user}

기존 사용자를 선택하는 경우, 검색 필드에 특정 사용자 ID 또는 이메일을 입력합니다. 그런 다음 대시보드 미리 보기를 사용하여 해당 사용자에게 메시지가 어떻게 표시되는지 확인하고, 해당 사용자가 보게 될 내용이 반영된 테스트 메시지를 기기로 전송합니다.

![사용자 선택]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### 커스텀 사용자 선택 {#selecting-a-custom-user}

커스텀 사용자로 미리 보는 경우, 사용자의 이름 및 커스텀 속성 등 개인화에 사용할 수 있는 다양한 필드에 텍스트를 입력합니다. 마찬가지로 자신의 이메일 주소를 입력하여 기기로 테스트를 보낼 수 있습니다.

![커스텀 사용자]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### 기존 사용자 사용자 지정 {#customizing-an-existing-user}

메시지 내 동적 콘텐츠를 테스트하기 위해 무작위 또는 기존 사용자의 개별 필드를 편집할 수 있습니다. **Edit**를 선택하면 선택한 사용자가 수정 가능한 커스텀 사용자로 전환됩니다.

![편집 버튼이 있는 사용자로 미리 보기 탭]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### 커스텀 이벤트 속성정보로 개인화된 캠페인 테스트 {#testing-campaigns-personalized-with-custom-event-properties}

[커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)로 개인화된 캠페인 테스트는 위에서 설명한 다른 유형의 캠페인 테스트와 약간 다릅니다.

{% tabs local %}
{% tab 수동 트리거 %}

#### 방법 1: 수동으로 캠페인 트리거 {#method-1-triggering-campaign-manually}

커스텀 이벤트 속성정보를 사용하여 개인화된 캠페인을 테스트하는 확실한 방법으로 직접 캠페인을 트리거할 수 있습니다.

1. 이벤트 속성정보를 포함한 카피를 작성합니다.

![속성정보가 포함된 테스트 메시지 작성]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)을 사용하여 이벤트가 발생할 때 캠페인을 전달합니다.

{% alert note %}
iOS 푸시 캠페인을 테스트하는 경우, iOS는 현재 열려 있는 앱에 대해 푸시 알림을 전달하지 않으므로 앱을 종료할 시간을 확보하기 위해 지연 시간을 1분으로 설정해야 합니다. 다른 유형의 캠페인은 즉시 전달하도록 설정할 수 있습니다.
{% endalert %}

![테스트 메시지 전달]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. 테스트 필터를 사용하거나 자신의 이메일 주소를 타겟팅하여 테스트할 사용자를 대상으로 지정하고, 캠페인 생성을 완료합니다.

![테스트 메시지 타겟팅]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. 앱에 접속하여 커스텀 이벤트를 완료합니다.

캠페인이 트리거되고 이벤트 속성정보로 맞춤화된 메시지가 표시됩니다.

![테스트 메시지 예시]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab 테스트 메시지 %}

#### 방법 2: 자신에게 테스트 메시지 보내기 {#method-2-sending-yourself-a-test-message}

또는 커스텀 사용자 ID를 저장하고 있는 경우, 맞춤화된 테스트 메시지를 자신에게 보내 캠페인을 테스트할 수도 있습니다.

1. 캠페인의 카피를 작성합니다.
2. **Test** 탭을 선택하고 **Customized User**를 선택합니다.
3. 페이지 하단에 커스텀 이벤트 속성정보를 추가하고, 상단 박스에 사용자 ID 또는 이메일 주소를 추가합니다.
4. **Send Test**를 선택하면 해당 속성정보로 개인화된 메시지를 수신할 수 있습니다.

![커스텀 사용자를 활용한 테스트]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### 방법 3: Liquid 사용 {#method-3-using-liquid}

Liquid를 사용하여 값을 수동으로 입력함으로써 커스텀 이벤트 속성정보를 테스트할 수 있습니다.

1. 메시지 편집기에서 커스텀 이벤트 속성정보에 대한 값을 입력합니다.
2. **Preview as a User** 탭을 선택하여 올바른 메시지가 표시되는지 확인합니다.

{% endtab %}
{% endtabs %}

## 제한 사항 {#limitations}

테스트 메시지가 실제 사용자에게 전송되는 Campaign이나 Canvases와 동일하게 동작하지 않는 몇 가지 상황이 있습니다. 이러한 경우, Campaign이나 Canvas를 제한된 테스트 사용자 집합에 발송하여 이 동작을 검증하는 것을 고려하세요.

- 테스트 메시지에서 Braze [환경설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)를 보면 **환경설정 저장** 버튼이 비활성화됩니다. 환경설정 센터 Liquid 태그도 유효한 링크로 확인되지 않을 수 있습니다. 이는 예상된 동작입니다. 포괄적인 테스트를 하려면 [환경설정 센터 테스트]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers)를 참조하세요.
- 인앱 메시지와 Content Cards를 테스트하려면 대상 사용자가 대상 기기에 대한 푸시 토큰을 보유하고 있어야 합니다.
- 이메일의 수신 거부 링크를 테스트하려면 테스트 사용자의 이메일 주소가 해당 워크스페이스에 등록되어 있는지 확인하세요.
- `List-Unsubscribe` 헤더는 테스트 메시지 기능으로 전송된 이메일에 포함되지 않습니다.
- 시드 그룹 사용자에게 전송된 이메일은 고객 프로필의 Campaign 수신 목록을 업데이트하지 않으며, 대시보드 분석에서 전송 수를 증가시키지 않습니다.

## 문제 해결 {#troubleshooting}

### 인앱 메시지 {#in-app-messages}

인앱 메시지 Campaign이 푸시 Campaign에 의해 트리거되지 않는 경우, 사용자가 푸시 메시지를 수신하기 **전에** 타겟 오디언스에 해당하는지 인앱 Campaign 세분화를 확인하세요.

Android 및 iOS에서 테스트 전송 시, **푸시 권한 요청** 클릭 동작을 사용하는 인앱 메시지가 일부 기기에서 표시되지 않을 수 있습니다. 해결 방법은 다음과 같습니다:
- **Android:** 기기가 Android 13 이상이어야 하며 Android SDK 버전 21.0.0 이상이어야 합니다. 또 다른 원인은 인앱 메시지가 표시되는 기기에 이미 시스템 수준 프롬프트가 있는 경우입니다. **다시 묻지 않기**를 선택한 적이 있다면, 다시 테스트하기 전에 앱을 재설치하여 알림 권한을 초기화해야 할 수 있습니다.
- **iOS:** 개발자 팀에서 앱의 푸시 알림 구현을 검토하고 푸시 권한을 요청하는 코드를 수동으로 제거하는 것을 권장합니다. 자세한 내용은 [푸시 프라이머 인앱 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices)를 참조하세요.

실행 기반 인앱 메시지 Campaign이 전달되려면 REST API가 아닌 Braze SDK를 통해 커스텀 이벤트를 기록해야 사용자가 기기에서 직접 적격한 인앱 메시지를 수신할 수 있습니다. 사용자가 세션 중에 해당 이벤트를 수행하면 인앱 메시지를 수신합니다.