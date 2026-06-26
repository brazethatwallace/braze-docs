---
nav_title: 커스텀 키워드 처리
article_title: 커스텀 키워드 처리
page_order: 2
description: "이 참조 문서에서는 Braze가 양방향 SMS, MMS, RCS 메시징 및 자동 응답을 처리하는 방법을 다룹니다. 키워드 트리거 작동 방식, 커스텀 키워드 카테고리, 다중 언어 지원에 대한 설명이 포함되어 있습니다."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# 커스텀 키워드 처리 {#custom-keyword-handling}

> 이 참조 문서에서는 Braze가 양방향 SMS, MMS, RCS 메시징 및 자동 응답을 처리하는 방법을 다룹니다. 키워드 트리거 작동 방식, 커스텀 키워드 카테고리, 다중 언어 지원에 대한 설명이 포함되어 있습니다.

## 양방향 메시징(커스텀 키워드 응답) {#two-way-messaging-custom-keyword-responses}

양방향 메시징을 사용하면 메시지를 보내고 해당 메시지에 대한 응답을 처리할 수 있습니다. 최종 사용자가 Braze에 키워드를 보내면 해당 사용자에게 자동 응답이 전송됩니다. 올바르게 적용하면 양방향 메시징은 고객 마케팅을 위한 간단하고 즉각적이며 역동적인 솔루션이 되어 시간과 리소스를 절약할 수 있습니다.

## 키워드 및 자동 응답 관리 {#managing-keywords-and-auto-responses}

Braze의 SMS, MMS, RCS를 사용하면 키워드 트리거를 생성하고, 커스텀 응답을 정의하며, 여러 언어에 대한 키워드 세트를 정의하고, 커스텀 키워드 카테고리를 설정할 수 있습니다.

{% alert note %}
Braze는 정확한 옵트아웃 처리 및 [퍼지 옵트아웃]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/)을 위해 전체 옵트아웃 키워드 세트([기본 키워드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/) 및 [커스텀 키워드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/))를 사용합니다.
{% endalert %}

{% tabs %}
{% tab 키워드 트리거 추가 %}

### 키워드 트리거 추가 {#add-keyword-triggers}

기본 옵트인 및 옵트아웃 키워드 외에도 옵트인, 옵트아웃, 도움말 응답을 트리거하는 자체 키워드를 정의할 수 있습니다.

자체 키워드를 정의하려면 다음을 수행합니다:

1. Braze 대시보드에서 **오디언스** > **구독 그룹 관리**로 이동하여 **SMS/MMS/RCS** 구독 그룹을 선택합니다.
2. **글로벌 키워드**에서 키워드를 추가하려는 키워드 카테고리 옆의 연필 아이콘을 선택합니다. ![연필 아이콘이 표시된 옵트인 키워드.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. 열리는 탭에서 이 키워드 카테고리를 트리거할 키워드를 추가합니다. 키워드는 대소문자를 구분하지 않으며, `START`, `YES`, `UNSTOP`과 같은 범용 키워드는 변경할 수 없습니다. !["옵트인" 카테고리의 키워드 편집. 추가된 키워드는 "START", "UNSTOP", "YES"입니다. 응답 메시지 필드에는 "이 번호의 메시지 수신이 해제되었습니다. 도움이 필요하면 HELP를 보내세요. 수신 거부하려면 STOP을 보내세요. 메시지 및 데이터 요금이 부과될 수 있습니다."라고 표시됩니다.]({% image_buster /assets/img/sms/keyword_edit2.png %})

키워드 및 키워드 응답에는 다음 규칙이 적용됩니다:

| 키워드 | 키워드 응답 |
| -------- | ----------------- |
| - 유효한 UTF-8 인코딩 문자<br>- 카테고리당 최대 20개 키워드<br>- 최대 길이 34자<br>- 최소 길이 1자<br>- 공백 포함 불가<br>- 대소문자를 구분하지 않으며 구독 그룹 내에서 고유해야 함 | - 비워둘 수 없음<br>- 최대 길이 300자<br>- 유효한 UTF-8 문자 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="키워드 트리거 추가" }

{% alert tip %}
이러한 키워드를 Campaigns 및 Canvases에서 메시지를 리타겟팅하고 트리거하는 데 어떻게 사용할 수 있는지 알고 싶으신가요? 자세한 내용은 [사용자 리타겟팅]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/)을 참조하세요.
{% endalert %}
{% endtab %}

{% tab 응답 관리 %}

### 응답 관리 {#manage-responses}

사용자가 특정 키워드 카테고리에 키워드를 문자로 보낸 후 전송되는 자체 응답을 관리할 수 있습니다.

1. Braze 대시보드에서 **오디언스** > **구독 그룹 관리**로 이동하여 **SMS/MMS/RCS** 구독 그룹을 선택합니다. <br><br>
2. **글로벌 키워드**에서 연필 아이콘을 선택하여 응답을 편집할 키워드 카테고리를 선택합니다. ![연필 아이콘이 표시된 옵트인 키워드.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. 열리는 탭에서 응답을 편집합니다. 응답을 작성할 때 [규정 준수를 위한 6가지 규칙]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/#the-six-rules-to-get-compliance-right)을 유의하고, 키워드 및 키워드 응답에 적용되는 다음 규칙을 읽어보세요.<br><br>
4. 응답에서 정적 URL을 자동으로 단축하려면 **링크 단축** 토글을 선택합니다. 문자 카운터가 업데이트되어 단축된 URL의 예상 길이를 표시합니다. !["링크 단축" 토글이 켜져 있을 때 문자 카운터가 업데이트되는 GIF.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:60%;"}

#### 고려 사항 {#considerations}

| 키워드 | 키워드 응답 |
| -------- | ----------------- |
| - 유효한 UTF-8 인코딩 문자<br>- 카테고리당 최대 20개 키워드<br>- 최대 길이 34자<br>- 최소 길이 1자<br>- 공백 포함 불가<br>- 대소문자를 구분하지 않으며 구독 그룹 내에서 고유해야 함 | - 비워둘 수 없음<br>- 최대 길이 300자<br>- 유효한 UTF-8 문자 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="고려 사항" }

{% endtab %}
{% endtabs %}

{% alert tip %}
실행 기반 Canvas가 인바운드 SMS, MMS 또는 RCS 메시지에 의해 트리거되는 경우, Canvas의 첫 번째 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)에서 SMS, MMS 또는 RCS 등록정보를 참조할 수 있습니다.
{% endalert %}

## 다중 언어 지원 {#multi-language-support}

특정 국가로 발송할 때 발신자는 현지 언어로 인바운드 키워드와 아웃바운드 응답을 지원해야 할 수 있습니다. 이를 지원하기 위해 Braze에서는 언어별 키워드 설정을 생성할 수 있습니다. 생성된 언어별 키워드 설정은 구독 그룹 내의 모든 발신 번호에 적용됩니다.
![키워드 설정으로 추가할 언어를 표시하는 드롭다운.]({% image_buster /assets/img/sms/multi-language.png %}){: style="float:right;max-width:50%;margin-left:10px;"}

### 언어별 키워드 생성 {#creating-language-specific-keywords}

**언어 추가**를 선택하고 대상 언어를 선택하거나 드롭다운에서 언어를 검색합니다.

{% alert important %}
영어 이외의 언어에는 사전 설정된 키워드와 응답이 제공되지 않으므로, 발신자는 마케팅 및 법무 팀과 협력하여 이 세트에 필요한 키워드를 추가해야 합니다. 그렇지 않으면 Braze가 해당 언어의 현지화된 수신 메시지를 처리하지 않습니다.
{% endalert %}

언어를 삭제해야 하는 경우 오른쪽 하단의 **언어 삭제** 버튼을 선택합니다.

!["이탈리아어" 탭이 선택된 글로벌 키워드 페이지. 추가된 각 언어에 대한 추가 탭이 있습니다.]({% image_buster /assets/img/sms/multi-language2.png %})

## 커스텀 키워드 카테고리 {#custom-keyword-categories}

세 가지 기본 키워드 카테고리(옵트인, 옵트아웃, 도움말) 외에도 최대 25개의 자체 키워드 카테고리를 생성할 수 있습니다. 이를 통해 임의의 키워드를 식별하고 비즈니스에 맞는 응답을 설정할 수 있습니다. 예를 들어 "PROMO" 또는 "DISCOUNT" 카테고리를 만들어 이번 달 진행 중인 프로모션에 대한 응답을 보낼 수 있습니다.

이러한 커스텀 키워드는 "항상 활성" 상태로 작동하므로, 메시지 서비스에 가입한 모든 사용자가 언제든지 키워드를 문자로 보내고 응답을 받을 수 있습니다. 이 동작 외에도 사용자 라이프사이클의 [특정 시점](#lifecycle-specific-keywords)에서만 전송할 수 있는 특정 키워드를 정의하는 옵션도 있습니다.

!["Promo" 카테고리의 키워드. 사용자가 "YO"를 문자로 보내면 프로모션 코드가 포함된 메시지를 받습니다.]({% image_buster /assets/img/sms/sms_custom_keyword.png %})

### 커스텀 카테고리 생성 {#creating-a-custom-category}

커스텀 키워드 카테고리를 생성하려면 다음을 수행합니다:

1. 해당 구독 그룹을 편집합니다.
2. **커스텀 키워드 추가**를 선택합니다. ![새 키워드를 추가하는 필드.]({% image_buster /assets/img/sms/sms_custom_step.png %}){: style="max-width:90%;"}
3. 키워드 카테고리 이름을 입력하고 사용자가 응답 메시지를 받기 위해 문자로 보낼 수 있는 키워드를 정의합니다.

이 키워드 카테고리가 생성되면 Campaigns 및 Canvases에서 [필터링 및 트리거]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/)에 사용할 수 있습니다.

커스텀 키워드 카테고리에서 생성된 키워드는 새 키워드 생성에 대한 모든 규칙과 유효성 검사를 따릅니다.

### 라이프사이클별 키워드 {#lifecycle-specific-keywords}

고객이 라이프사이클 중 특정 시점(예: 초기 온보딩 중)에만 특정 키워드를 보내 응답을 받을 수 있도록 제한하려는 사용 사례가 있는 경우, Campaign 또는 Canvas에서 **구독 그룹 내 키워드 카테고리 OTHER로 인바운드 SMS 전송** 트리거를 사용하고 사용자가 특정 시점에 보낼 수 있는 키워드를 정의할 수 있습니다.

이 트리거는 메시지의 일치 또는 불일치 비교와 정규표현식 일치 또는 불일치 규칙을 사용하여 특정 인바운드 메시지에 대한 필터링을 지원하여 사용자의 입력을 검증합니다.

#### Canvas

![구독 그룹 "Messaging Service" 내 키워드 카테고리 "Other"에 인바운드 SMS 전송 트리거가 있는 실행 기반 캔버스 단계. 메시지 본문이 정규표현식 "caret symbol skip"과 일치합니다.]({% image_buster /assets/img/sms/canvas_trigger.png %}){: style="max-width:90%;"}

#### Campaign

![구독 그룹 "Marketing Message Service A" 내 키워드 카테고리 "Other"에 인바운드 SMS 전송 트리거가 있는 실행 기반 Campaign. 메시지 본문이 "Keyword1"이거나 "Keyword2"이거나 "Keyword A"가 아닙니다.]({% image_buster /assets/img/sms/campaign_trigger.png %}){: style="max-width:90%;"}

### 알 수 없는 키워드 처리 {#dealing-with-unknown-keywords}

가입한 사용자가 정의된 키워드와 일치하지 않는 내용을 문자로 보낼 때 자동 응답을 설정하는 것을 강력히 권장합니다(**OTHER** 키워드 카테고리에서 처리됨).

기본 응답(예: "죄송합니다! 해당 키워드를 인식하지 못했습니다.")을 보내려면 다음을 수행합니다:

1. [SMS Campaign]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/)을 생성합니다.
2. **타겟 오디언스**에서 **모든 사용자**를 선택합니다(트리거가 메시지를 받는 대상을 제한합니다).
3. **스케줄**에서 **실행 기반 전달**을 선택합니다.
4. 트리거를 적절한 구독 그룹에 대한 **인바운드 SMS 전송**, **키워드 카테고리 OTHER 내**로 설정합니다.
5. **메시징** 단계에서 사용자에게 전송할 응답 본문을 입력합니다.

Braze가 **알 수 없는** 전화번호(프로필이 존재하기 전)에서 수신된 메시지를 처리하는 방법에 대해서는 [알 수 없는 전화번호 처리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/unknown_phone_numbers/)를 참조하세요.

{% alert tip %}
이러한 키워드와 키워드 카테고리를 Campaigns 및 Canvases에서 메시지를 리타겟팅하고 트리거하는 데 어떻게 사용할 수 있는지 알고 싶으신가요? 자세한 내용은 [사용자 리타겟팅]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/)을 참조하세요.
{% endalert %}