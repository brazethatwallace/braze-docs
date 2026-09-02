---
nav_title: Facebook
article_title: Facebook으로 Canvas 오디언스 동기화
description: "이 참조 문서에서는 Braze 오디언스 동기화를 Facebook에 사용하여 행동 트리거, 세분화 등을 기반으로 광고를 전달하는 방법을 다룹니다."
page_order: 2
alias: /audience_sync_facebook/

tool:
  - Canvas

---

# Facebook으로 오디언스 동기화 {#audience-sync-to-facebook}

> Braze 오디언스 동기화를 Facebook에 사용하면 Braze 통합에서 자체 사용자 데이터를 Facebook 커스텀 오디언스에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달할 수 있습니다.

사용자 데이터를 기반으로 BRAZE 캔버스에서 메시지(푸시, 이메일, 단문 메시지 서비스 또는 웹훅)를 트리거하는 데 일반적으로 사용하는 모든 기준을 이제 커스텀 오디언스를 사용하여 Facebook에서 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다. 예를 들어 오디언스 동기화를 Facebook에 구성하면 이메일, 전화, 이름, 성 등 다양한 퍼스트파티 필드를 사용할 수 있습니다.

**커스텀 오디언스 동기화의 일반적인 사용 사례는 다음과 같습니다**:

- 여러 채널을 통해 고가치 사용자를 타겟팅하여 구매 또는 참여를 유도합니다.
- 다른 마케팅 채널에 반응이 적은 사용자를 리타겟팅합니다.
- 이미 브랜드의 충성 고객인 사용자가 광고를 받지 않도록 억제 오디언스를 생성합니다.
- 유사 오디언스를 생성하여 신규 사용자를 더 효율적으로 확보합니다.

이 기능을 통해 브랜드는 Facebook과 공유되는 특정 퍼스트파티 데이터를 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합에 대해 최대한 신중하게 고려합니다. 자세한 내용은 [개인정보 보호정책](https://www.braze.com/privacy)을 참조하세요.

## 사용자 동기화 및 사용량 제한 고려 사항 {#user-syncing-and-rate-limit-considerations}

사용자가 오디언스 동기화 단계에 도달하면, Braze는 Facebook의 마케팅 API 사용량 제한을 준수하면서 거의 실시간으로 동기화합니다. Braze는 Facebook으로 전송하기 전에 5초마다 가능한 한 많은 사용자를 일괄 처리합니다.

Facebook의 마케팅 API 사용량 제한은 광고 계정당 1시간 동안 &#126;190,000건 이하의 API 요청만 허용합니다. 고객이 이 제한에 도달하면, Braze는 최대 &#126;13시간 동안 동기화를 재시도합니다. 그래도 동기화가 불가능한 경우, Braze는 해당 사용자를 Users Errored 측정기준에 표시합니다.

## 사전 요구 사항 {#prerequisites}

Canvas에서 Facebook 오디언스 단계를 설정하기 전에 다음 항목이 생성 및 완료되었는지 확인해야 합니다.

| 요구 사항 | Origin | 설명 |
| ----------- | ------ | ----------- |
| Facebook 비즈니스 매니저 | [Facebook](https://www.facebook.com/business/help/113163272211510) | 브랜드의 Facebook 자산(예: 광고 계정, 페이지, 앱)을 관리하는 중앙 집중식 도구입니다. |
| Facebook 광고 계정 | [Facebook](https://www.facebook.com/business/help/910137316041095) | 브랜드의 비즈니스 매니저에 연결된 활성 Facebook 광고 계정입니다.<br><br>Facebook 비즈니스 매니저 관리자가 Braze에서 사용할 Facebook 광고 계정에 대해 "Manage Campaigns" 또는 "Manage ad accounts" 권한을 부여했는지 확인하세요. 또한 광고 계정 이용약관에 동의했는지 확인하세요. |
| Facebook 커스텀 오디언스 약관 | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Braze에서 사용할 Facebook 광고 계정에 대해 Facebook의 커스텀 오디언스 약관에 동의하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사전 요구 사항" }

## 통합 {#integration}

### 1단계: Facebook에 연결하기 {#step-1-connect-to-facebook}

{% alert important %}
Facebook을 Braze 계정에 연결하려면 ["관리자" 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)이 있어야 합니다.
{% endalert %}

Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Facebook**을 선택합니다. Facebook 오디언스 내보내기에서 **Facebook 연결**을 선택합니다.

![개요 섹션과 Facebook 연결 버튼이 있는 Facebook 오디언스 내보내기 섹션이 포함된 Braze의 Facebook 기술 페이지.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Facebook oAuth 대화 상자가 나타나 Braze가 Facebook 광고 계정에 커스텀 오디언스를 생성할 수 있도록 권한을 부여합니다.

![Facebook 사용자 이름으로 연결하라는 첫 번째 Facebook 대화 상자.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![광고 계정의 광고 관리 권한을 요청하는 두 번째 Facebook 대화 상자.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Braze를 Facebook 계정에 연결한 후, Braze 워크스페이스 내에서 동기화할 광고 계정을 선택합니다. 연결이 완료되면 파트너 페이지로 돌아가 연결된 계정을 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![광고 계정이 성공적으로 연결된 것을 보여주는 업데이트된 Facebook 기술 파트너 페이지.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Facebook 연결은 Braze 워크스페이스 수준에서 적용됩니다. Facebook 관리자가 Facebook 비즈니스 매니저에서 사용자를 제거하거나 연결된 Facebook 계정에 대한 액세스를 취소하면, Braze는 유효하지 않은 토큰을 감지합니다. 그 결과, Facebook 오디언스 컴포넌트를 사용하는 활성 Canvases에 오류가 표시되며, Braze는 사용자를 동기화할 수 없게 됩니다.

{% alert important %}
이전에 [광고 관리](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) 및 [광고 관리 표준 액세스](https://developers.facebook.com/docs/marketing-api/access#standard)에 대한 Facebook 앱 검토 프로세스를 거친 고객의 경우, 시스템 사용자 토큰은 Facebook 오디언스 컴포넌트에 대해 여전히 유효합니다. Facebook 파트너 페이지를 통해 Facebook 시스템 사용자 토큰을 편집하거나 취소할 수 없습니다. 대신, Facebook 계정을 연결하여 Braze 워크스페이스 내에서 Facebook 시스템 사용자 토큰을 교체할 수 있습니다.

<br><br>Facebook oAuth 구성은 [Segments를 사용한 Facebook 내보내기]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites)에도 적용됩니다.
{% endalert %}

### 2단계: 커스텀 오디언스 서비스 약관 동의하기 {#step-2-accept-custom-audiences-terms-of-service}

Canvas를 구성하기 전에 다음 링크에서 Facebook 서비스 약관에 동의해야 합니다:

- **개인 계정의 고객 목록 커스텀 오디언스 약관:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **비즈니스 계정의 Facebook 비즈니스 도구 약관:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![고객 목록 커스텀 오디언스에 대해 동의해야 하는 약관 예시.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Facebook 비즈니스 도구에 대해 동의해야 하는 약관 예시.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

통합 시 Facebook 계정 감사에 대한 자세한 내용은 [FAQ 섹션](#terms)을 참조하세요.

### 3단계: Canvas에 Facebook 오디언스 컴포넌트 추가하기 {#step-3-add-a-facebook-audience-component-in-canvas}

Canvas에 컴포넌트를 추가하고 **Facebook 오디언스**를 선택합니다.

![Canvas에 추가할 컴포넌트 목록.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![오디언스 동기화 컴포넌트.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### 4단계: 동기화 설정 {#step-4-sync-setup}

**커스텀 오디언스** 버튼을 선택하여 컴포넌트 편집기를 엽니다. 그런 다음 오디언스 동기화 파트너로 **Facebook**을 선택합니다.

![파트너를 선택하는 옵션이 있는 오디언스 동기화 설정 화면.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

원하는 Facebook 광고 계정을 선택합니다. **새 오디언스 또는 기존 오디언스 선택** 드롭다운에서 새 오디언스 또는 기존 오디언스의 이름을 입력합니다.

{% tabs %}
{% tab 새 오디언스 만들기 %}

1. 새 커스텀 오디언스의 이름을 입력합니다.
2. **오디언스에 사용자 추가**를 선택하고 Facebook과 동기화할 필드를 선택합니다.
3. 그런 다음 **오디언스 만들기**를 선택하여 오디언스를 저장합니다.

![이메일, 전화번호, 이름, 성 정보를 매칭하는 오디언스 동기화 설정.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

오디언스가 성공적으로 생성되었거나 이 과정에서 오류가 발생한 경우 단계 편집기 상단에 알림이 표시됩니다. 오디언스가 초안 모드로 생성되었으므로 나중에 Canvas 여정에서 사용자 제거를 위해 이 오디언스를 참조할 수도 있습니다.

새 오디언스로 Canvas를 시작하면, Braze는 Canvas 시작 시 새 커스텀 오디언스를 생성하고 이후 사용자가 오디언스 동기화 단계에 진입하면 거의 실시간으로 동기화합니다.

각 오디언스 동기화 단계는 해당 단계에 구성된 Facebook 오디언스에 매핑됩니다. Canvas가 다시 실행되면(예: 반복 스케줄에 따라), Braze는 적격 사용자를 동일한 오디언스에 동기화하며, Canvas 실행마다 새 Facebook 오디언스를 생성하지 않습니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}

Braze는 기존 Facebook 커스텀 오디언스에 사용자를 추가하거나 제거하여 해당 오디언스를 최신 상태로 유지할 수 있는 기능을 제공합니다. 기존 오디언스와 동기화하려면 다음을 수행합니다:

1. 드롭다운에서 기존 오디언스 이름을 입력합니다.
2. **오디언스에 추가** 또는 **오디언스에서 제거** 중 원하는 옵션을 선택합니다.
3. Braze는 사용자가 Facebook 오디언스 단계에 진입하면 거의 실시간으로 사용자를 추가하거나 제거합니다.

![이메일, 전화번호, 이름, 성 정보를 제거하는 오디언스 동기화 설정.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook은 오디언스 크기가 너무 작은 커스텀 오디언스(일반적으로 1,000명 미만)에서 사용자를 제거하는 것을 금지합니다. 따라서 오디언스가 적절한 크기에 도달할 때까지 Braze는 오디언스 동기화 단계에서 사용자 제거를 동기화할 수 없습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 5단계: Canvas 시작하기 {#step-5-launch-canvas}

Facebook 오디언스 컴포넌트를 구성한 후 Canvas를 시작할 차례입니다! 새 커스텀 오디언스가 생성되고, Facebook 오디언스 단계를 통과하는 사용자는 Facebook의 이 커스텀 오디언스에 전달됩니다. Canvas에 후속 단계가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행합니다.

Facebook 오디언스 매니저에서 커스텀 오디언스의 **기록** 탭에는 Braze에서 오디언스로 전송된 사용자 수가 반영됩니다. 사용자가 해당 단계에 다시 진입하면 Facebook으로 다시 전송됩니다.

![활동, 활동 세부 정보, 변경된 항목, 날짜 및 시간 열이 있는 오디언스 기록 테이블을 포함하는 특정 Facebook 오디언스의 오디언스 세부 정보 및 기록 탭.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## 분석 이해하기 {#understanding-analytics}

다음 표에는 오디언스 동기화 구성 요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| --- | --- |
| 진입 | Facebook에 동기화하기 위해 이 구성 요소에 진입한 사용자 수입니다. |
| 다음 단계로 진행 | 다음 구성 요소가 있는 경우 다음 구성 요소로 진행한 사용자 수입니다. Canvas 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| 동기화된 사용자 | Facebook에 성공적으로 동기화된 사용자 수입니다. |
| 동기화되지 않은 사용자 | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수입니다. 필드는 "OR" 연산자를 사용하여 일치시키므로, 사용자가 Facebook의 필드 중 하나라도 가지고 있으면 다른 모든 필드에서 일치하지 않더라도 Facebook이 해당 사용자를 일치시킵니다. |
| 대기 중인 사용자 | 현재 Braze에서 Facebook으로 동기화하기 위해 처리 중인 사용자 수입니다. |
| 오류 발생 사용자 | 약 13시간의 재시도 후 API 오류로 인해 Facebook에 동기화되지 않은 사용자 수입니다. 오류의 잠재적 원인으로는 유효하지 않은 Facebook 토큰이나 Facebook에서 커스텀 오디언스가 삭제된 경우 등이 있습니다. |
| Canvas 종료 | Canvas를 종료한 사용자 수입니다. Canvas의 마지막 단계가 Facebook 단계인 경우 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="분석 이해하기" }

{% alert important %}
내부 처리로 인해 동기화된 사용자 및 오류 발생 사용자 측정기준의 보고에 지연이 있을 수 있습니다.
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 오디언스 동기화 파트너 대시보드에 오디언스가 채워지는 데 얼마나 걸리나요? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

오디언스가 채워지는 데 걸리는 시간은 특정 파트너에 따라 다릅니다. 모든 네트워크는 Braze의 요청을 처리하고 사용자를 매칭하려고 시도합니다. 커스텀 오디언스가 업데이트되기까지 최대 24시간이 걸릴 수 있습니다.

### 유효하지 않은 토큰 오류가 발생하면 어떻게 해야 하나요? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Facebook 파트너 페이지에서 Facebook 계정을 연결 해제한 후 다시 연결하면 됩니다. Facebook 비즈니스 매니저 관리자에게 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 확인하세요.

### Canvas를 시작할 수 없는 이유는 무엇인가요? {#why-is-my-canvas-not-allowed-to-launch}

- 시스템 사용자 토큰이 인증되었고 Facebook 비즈니스 매니저에서 원하는 광고 계정에 대한 액세스 권한이 있는지 확인하세요.
- 광고 계정을 선택하고, 새 커스텀 오디언스의 이름을 입력하고, 매칭할 필드를 선택했는지 확인하세요.
- Facebook에서 500개의 커스텀 오디언스 제한에 도달했을 수 있습니다. Facebook 오디언스 매니저로 이동하여 Canvas를 사용하여 새 커스텀 오디언스를 만들기 전에 불필요한 오디언스를 삭제하세요.

### 사용자를 Facebook에 전달한 후 사용자가 매칭되었는지 어떻게 알 수 있나요? {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

Facebook은 개인정보 보호를 위해 이 정보를 제공하지 않습니다.

### Braze는 가치 기반 커스텀 오디언스를 지원하나요? {#does-braze-support-value-based-custom-audiences}

현재 가치 기반 커스텀 오디언스는 Braze에서 지원되지 않습니다. {% multi_lang_include product_feedback_cta.md context="gap" feature="value-based custom audience sync" %}

### Braze는 오디언스 동기화 파트너에게 데이터를 보내기 전에 해싱하나요? {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

이메일 데이터가 정규화되면 Braze는 SHA256으로 해싱합니다.

**IDFA/AAID/전화번호:** Braze는 SHA256으로 해싱합니다. 동기화하는 오디언스 유형은 항상 다음 중 하나입니다:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256.

빈도 측면에서, Braze는 동기화 준비를 위해 사용자가 사용자 여정의 오디언스 동기화 단계에 진입할 때만 사용자 개인 식별 정보(PII)를 해싱합니다.

### 가치 기반 유사 커스텀 오디언스 동기화 문제를 어떻게 해결하나요? {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

현재 가치 기반 유사 커스텀 오디언스는 Braze에서 지원되지 않습니다. 이 오디언스에 동기화를 시도하면 오디언스 동기화 단계에서 오류가 발생할 수 있습니다. 이 문제를 해결하려면 다음 단계를 따르세요:

1. Facebook 광고 매니저 대시보드로 이동하여 **오디언스**를 선택합니다.
2. **오디언스 만들기** > **커스텀 오디언스**를 선택합니다.
3. **고객 목록**을 선택합니다.
4. **Value** 열 없이 CSV 또는 목록을 업로드합니다. **No, continue with a customer list that doesn't include customer value**를 선택합니다.
5. 커스텀 오디언스 만들기를 완료합니다.
6. Braze에서 생성한 커스텀 오디언스로 Facebook 오디언스 동기화 단계를 업데이트합니다.

### Facebook 커스텀 오디언스 서비스 약관과 관련된 이메일을 받았습니다. 이 문제를 해결하려면 어떻게 해야 하나요? {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

Facebook에 오디언스 동기화를 사용하려면 이 서비스 약관에 동의해야 합니다.

- 광고 계정이 개인 Facebook 계정에 직접 연결되어 있는 경우, 여기에서 개인 계정에서 서비스 약관에 동의할 수 있습니다: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- 광고 계정이 회사의 비즈니스 매니저 계정에 연결되어 있는 경우, 여기에서 Facebook 비즈니스 매니저 계정에서 서비스 약관에 동의해야 합니다: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Facebook 커스텀 오디언스 서비스 약관에 동의한 후 다음을 수행하세요:

1. Facebook 계정을 연결 해제한 후 다시 연결하여 Braze에서 Facebook 액세스 토큰을 새로고침합니다.
2. Canvas를 편집하고 업데이트하여 Facebook 오디언스 동기화 단계를 다시 활성화합니다.

그러면 Braze는 사용자가 Facebook 오디언스 동기화 단계에 도달하는 즉시 사용자를 동기화할 수 있습니다.

### **Connected Facebook** 및 **Number of Facebook Friends Using App** 필터는 어떻게 되었나요? {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

**Number of Facebook Friends Using App** 및 **Connected Facebook** Braze 세분화 필터는 더 이상 사용되지 않습니다. Facebook과 Braze SDK는 더 이상 해당 필터가 의존하던 기본 데이터를 수집하지 않습니다.

더 이상 사용되지 않는 필터를 커스텀 속성, 커스텀 이벤트 또는 인게이지먼트 기반 Segments로 대체하세요. 예를 들어, **Connected Facebook** 대신 Facebook 로그인 또는 소셜 연결을, **Number of Facebook Friends Using App** 대신 추천, 초대 및 공유를 사용할 수 있습니다.

Canvas 리타겟팅의 경우, [4단계: 동기화 설정](#step-4-sync-setup)에서 설명한 대로 이메일, 전화번호, 이름, 성으로 사용자를 매칭하세요. 도달 범위를 확장하려면 고가치 Segment를 Facebook에 동기화하고 Meta 광고 매니저에서 유사 오디언스를 만드세요.

## 문제 해결 {#troubleshooting}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table aria-label="문제 해결">
  <thead>
    <tr>
      <th>오류</th>
      <th>설명</th>
      <th>해결 단계</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>유효하지 않은 토큰</b></td>
      <td>통합을 연결한 사용자가 비밀번호를 변경하거나, 자격 증명이 만료되는 등의 경우에 일반적으로 발생합니다.</td>
      <td><b>파트너 통합</b> > <b>Facebook</b>으로 이동하여 계정을 연결 해제한 후 다시 연결합니다. Facebook 계정을 감사하기 위한 추가 단계는 <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>이 문제 해결 섹션</a> 을 참조하세요.</td>
    </tr>
    <tr>
      <td><b>오디언스 크기가 너무 작음</b></td>
      <td>이 오류는 오디언스에서 사용자를 제거하는 오디언스 동기화 단계를 생성한 경우 발생할 수 있습니다. 오디언스 크기가 0에 가까워지면 네트워크에서 오디언스 크기가 너무 작아 제공할 수 없다고 표시할 수 있습니다.</td>
      <td>오디언스 크기를 완전히 소진하지 않도록 정기적으로 사용자를 추가하고 제거하는 오디언스 동기화 전략을 사용하세요.</td>
    </tr>
    <tr>
      <td><b>오디언스가 존재하지 않음</b></td>
      <td>오디언스 동기화 단계에서 존재하지 않거나 삭제된 오디언스를 사용하고 있습니다. 오디언스에 접근하는 데 필요한 권한이 더 이상 없는 경우에도 이 오류가 트리거될 수 있습니다.</td>
      <td>관리자에게 파트너 플랫폼에서 오디언스가 여전히 존재하는지 확인하도록 요청하세요. <br><br>존재하는 경우, 통합을 연결한 사용자가 해당 오디언스에 대한 권한이 있는지 확인하세요. 권한이 없는 경우 해당 사용자에게 오디언스에 대한 접근 권한을 부여해야 합니다. <br><br>오디언스가 의도적으로 제거된 경우, 활성 오디언스를 추가하고 해당 단계에서 새 오디언스를 생성하세요.</td>
    </tr>
    <tr>
      <td><b>광고 계정 접근 시도</b></td>
      <td>선택한 광고 계정 또는 오디언스에 대한 권한이 없습니다.</td>
      <td>광고 계정 관리자와 협력하여 적절한 접근 권한과 권한을 확보하세요.</td>
    </tr>
    <tr>
      <td><b>서비스 약관 미동의</b></td>
      <td>Facebook과 같은 일부 오디언스 동기화 대상의 경우, 오디언스 동기화 기능을 사용하려면 광고 네트워크에서 특정 서비스 약관에 동의해야 합니다. 적절한 약관에 동의하지 않은 경우 이 오류가 트리거됩니다. 그 결과 Braze에서 "Facebook에 대한 인증 자격 증명이 유효하지 않습니다."라는 제목의 이메일을 받았을 수도 있습니다.</td>
      <td>Facebook의 필수 약관에 동의했는지 확인하세요.</td>
    </tr>
    <tr>
      <td><b>모든 사용자에게 오류 발생</b></td>
      <td>해당 단계에서 선택한 필드에 대한 값이 있는 사용자임을 확인했음에도 모든 사용자에게 오류가 발생하는 경우, Facebook 계정에 문제가 있을 수 있습니다.</td>
      <td><a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>이 문제 해결 섹션</a> 의 단계를 따라 계정에 문제가 있는지 확인하세요.
      </td>
    </tr>
    <tr>
      <td><b>오디언스 생성 실패</b></td>
      <td>Facebook 기술 파트너 페이지에서 "연결됨"으로 표시되지만, 오디언스를 동기화할 때 Facebook 오디언스 동기화 단계에서 "오디언스 '오디언스 이름' 생성에 실패했습니다"라는 오류가 발생합니다. Facebook 계정 인증에 실패했습니다. 기술 파트너 페이지를 방문하여 계정을 다시 연결하세요.</td>
      <td><a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>이 문제 해결 섹션</a> 의 단계를 따라 계정에 문제가 있는지 확인하세요.
      </td>
    </tr>
    <tr>
      <td><b>드롭다운에 광고 계정이 표시되지 않음</b></td>
      <td>Facebook 오디언스 단계를 구성할 때, 예상하는 광고 계정이 광고 계정 선택기에 나열되지 않습니다.</td>
      <td>Facebook 앱이 Marketing API 사용을 위해 Facebook에서 요구하는 접근 수준으로 <code>ads_management</code>에 대한 <a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">앱 검토</a> 를 완료했는지 확인하세요. <a href="https://business.facebook.com/">Facebook 비즈니스 관리자</a> 에서 시스템 사용자 토큰이 올바른 권한을 가지고 있고 Braze에서 사용하는 광고 계정과 연결되어 있으며, 광고 계정 약관에 동의했는지 확인하세요. <br><br>드롭다운이 새 Canvas에서는 작동하지만 이미 편집한 Canvas에서는 작동하지 않는 경우, 브라우저를 강제 새로고침(또는 캐시 삭제)하고 해당 광고 계정에 접근 권한이 있는 사용자로 로그인되어 있는지 확인하세요.</td>
    </tr>
    <tr>
      <td><b>접근 토큰 유효성 검사 오류</b></td>
      <td>Braze를 Facebook에 연결하거나 오디언스를 동기화할 때 Facebook 접근 토큰 유효성 검사에 대한 오류가 표시됩니다.</td>
      <td>브라우저에서 Facebook에서 로그아웃하세요. Braze에서 <b>파트너 통합</b> &gt; <b>Facebook</b>으로 이동하여 저장된 Facebook 자격 증명을 제거한 다음 Facebook을 다시 연결하세요. Braze용 Facebook 기술 파트너 페이지에서 옵션이 있는 경우 통합을 연결 해제한 후 다시 연결하세요. <br><br>문제가 계속되면 <a href="#audit-your-facebook-account">Facebook 계정 감사</a> 를 따르세요.</td>
    </tr>
    <tr>
      <td><b>오디언스 내보내기 또는 동기화 권한 오류</b></td>
      <td>Facebook 오디언스 내보내기 또는 동기화가 인증, 관리자 또는 광고 계정 오류로 실패합니다.</td>
      <td><a href="https://developers.facebook.com/">Meta for Developers</a> 에서 앱을 열고 <b>앱 역할</b>에서 사용자에게 <b>관리자</b> 역할이 있는지 확인하세요. <b>앱 설정</b> &gt; <b>고급</b>에서 <b>광고 계정</b>에 Braze에서 사용하는 계정이 포함되어 있는지 확인하세요. <a href="https://business.facebook.com/latest/settings">비즈니스 설정</a> 에서 연결하는 사용자 또는 시스템 사용자가 올바른 광고 계정에 접근할 수 있는지 확인하세요.</td>
    </tr>
  </tbody>
</table>

### Facebook 계정 감사 {#audit-your-facebook-account}

통합과 관련하여 추가 문제가 발생하는 경우, 다음 섹션과 단계를 참조하여 Facebook 계정을 감사하세요.

#### 계정 권한 검토 {#review-account-permissions}

1. 플랫폼에서 이러한 권한을 관리하는 방법에 대한 [Facebook 설명서](https://www.facebook.com/business/help/186007118118684?id=829106167281625)를 검토하세요. Facebook 비즈니스 관리자의 경우, 필요한 광고 계정에 접근할 수 있는 **관리자** 또는 **직원** 비즈니스 관리자 역할이 최소한 필요합니다.
2. **직원**인 경우, 관리자가 오디언스를 생성하거나 오디언스에 사용자를 동기화하기 위해 각 광고 계정에 대한 전체 **광고 계정 관리** 권한을 부여했는지 확인하세요.
3. 권한이 부여된 후 계정을 연결 해제한 다음 다시 연결해야 합니다.

#### 서비스 약관 동의 {#terms}

Facebook에서 보류 중인 서비스 약관(TOS)에 동의하세요. Facebook은 주기적으로 사용자와 비즈니스 관리자에게 서비스 약관을 다시 승인하도록 요구합니다.

1. 연결된 사용자는 각 광고 계정에 대한 모든 서비스 약관에 동의해야 합니다:
- 개인 Facebook 계정에 대한 커스텀 오디언스 TOS:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![광고 계정을 관리할 수 있는 전체 제어 권한이 있는 계정.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

계정 및 비즈니스 ID를 찾으려면 다음 단계를 따르세요:

1. [Facebook 광고 관리자 계정](https://adsmanager.facebook.com/)으로 이동하세요.
2. 드롭다운 메뉴에서 올바른 광고 계정을 사용하고 있는지 확인하세요.
3. URL에서 `act=` 뒤의 계정 ID와 `business_id=` 뒤의 비즈니스 ID를 찾으세요.

![계정 ID와 비즈니스 ID가 강조 표시된 URL.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. 커스텀 오디언스 약관을 읽고 **동의**를 선택하세요. 약관 상단의 드롭다운을 사용하여 어떤 계정에 대해 서비스 약관에 서명하는지 확인하는 것을 권장합니다.

![서비스 약관에 서명하는 계정을 보여주는 드롭다운.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. 서비스 약관에 대해 **동의**를 선택해야 합니다. 이후 "Braze를 대신하여 이 서비스 약관에 동의했습니다."라는 메시지가 표시됩니다.
6. Facebook 계정을 연결 해제한 후 다시 연결하여 Braze에서 Facebook 접근 토큰을 새로고침하세요.
7. Canvas를 편집하고 업데이트하여 Facebook 오디언스 동기화 단계를 다시 활성화하세요. 그러면 Braze가 사용자가 Facebook 오디언스 단계에 도달하는 즉시 사용자를 동기화할 수 있습니다.
8. 문제가 지속되면 관리자 권한이 있는 별도의 사용자를 사용하여 광고 관리자를 통해 수동으로 약관에 동의해 보세요.

#### 보류 중인 작업 완료 {#complete-any-pending-tasks}

Facebook 광고 서비스 사용을 차단할 수 있는 Facebook의 보류 중인 작업이 있는지 확인하세요:

1. [Facebook 광고 관리자에 로그인](https://adsmanager.facebook.com/)하세요.
2. 문제가 있는 광고 계정을 선택하세요.
3. 내비게이션에서 **계정 개요**를 선택하세요. <br> ![계정 개요가 선택된 내비게이션.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. 해결해야 할 알림이 있는지 확인하세요. <br> ![만료된 신용카드가 있는 계정.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. 완료해야 할 설정 작업이 있는지 확인하세요. <br> ![계정 설정이 부분적으로 완료된 계정.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### 다른 사용자로 연결 {#connect-with-a-different-user}

추가 문제 해결 단계로, 다른 관리자 사용자가 다음을 수행하여 계정을 연결해 보는 것을 권장합니다:

1. 현재 통합을 연결 해제합니다.
2. 관리자 권한이 있는 별도의 사용자가 자신의 Facebook 사용자 계정을 연결합니다.