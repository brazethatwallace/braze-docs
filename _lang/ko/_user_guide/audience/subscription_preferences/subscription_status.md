---
nav_title: 구독 상태
article_title: 구독 상태
page_order: 0
page_type: reference
description: "Braze가 이메일, LINE, SMS, RCS, WhatsApp에서 구독 상태를 추적하는 방법과 상태가 메시지 전달을 제어하는 방식에 대해 알아보세요."

---

# 구독 상태 {#subscription-status}

> Braze가 메시징 채널 전반에서 구독 상태를 추적하는 방법, 글로벌 및 구독 그룹 상태가 상호작용하는 방식, 그리고 채널별 규칙이 적용되는 위치에 대해 알아보세요.

구독 상태는 사용자가 특정 채널에서 메시지를 수신할 자격이 있는지 여부를 Braze에 알려줍니다. 상태는 Campaign 및 Canvas 타겟팅, Segment 필터, 그리고 Braze의 전달 시도 여부를 제어할 수 있습니다.

## Braze에서 구독 상태가 작동하는 방식 {#how-subscription-status-works-in-braze}

Braze는 두 가지 수준에서 구독 상태를 추적합니다:

| 수준 | 제어 대상 | 채널 |
| ----- | ---------------- | -------- |
| 글로벌 구독 상태 | 사용자가 해당 채널에서 메시지를 수신할 수 있는지 여부 | 이메일, 푸시 |
| 구독 그룹 상태 | 사용자가 채널 내 특정 그룹에 옵트인했는지 여부 | 이메일, SMS, MMS, RCS, WhatsApp, LINE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Braze에서 구독 상태가 작동하는 방식" }

글로벌 상태와 구독 그룹 상태는 함께 작동합니다. 이메일의 경우, 글로벌 수신 거부 상태인 사용자는 구독 그룹에 가입되어 있더라도 이메일을 수신하지 않습니다. SMS, RCS, WhatsApp, LINE의 경우, 사용자는 해당 그룹에서 메시지를 수신하려면 관련 구독 그룹에 가입되어 있어야 합니다.

**인게이지먼트** > **연락처 설정**에서 사용자 프로필의 구독 상태를 확인하고 업데이트할 수 있으며, REST API, SDK, CSV 가져오기, 환경설정 센터, 채널별 옵트인 플로우를 통해서도 가능합니다. Braze는 구독 상태 변경을 데이터 포인트에 포함하지 않습니다.

{% alert note %}
구독 그룹은 채널 내에서 세분화된 옵트인을 추가합니다(예: 프로모션 SMS와 트랜잭션 SMS). 글로벌 이메일 상태와 구독 그룹 멤버십은 도달 가능한 사용자를 결정할 때 함께 작동합니다.
{% endalert %}

## 이메일 {#email}

Braze에는 이메일에 대한 세 가지 글로벌 구독 상태가 있습니다. 이 상태는 구독 또는 옵트인 오디언스를 대상으로 하는 메시지를 사용자가 수신하는지 여부를 제어합니다. 예를 들어, `unsubscribed` 상태의 사용자는 `subscribed` 또는 `opted-in` 사용자를 대상으로 하는 메시지를 수신하지 않습니다.

| 상태 | 정의 |
| ----- | ---------- |
| 옵트인 | 사용자가 이메일 수신을 원한다고 명시적으로 확인했습니다. Braze는 이메일 발송에 대한 사용자 동의를 얻기 위해 명시적 옵트인 프로세스를 권장합니다. |
| 구독됨 | 사용자가 수신 거부하지도, 이메일 수신에 명시적으로 옵트인하지도 않은 상태입니다. 사용자 프로필이 생성될 때의 기본 구독 상태입니다. |
| 수신 거부 | 사용자가 이메일 수신을 명시적으로 거부했습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이메일 구독 상태" }

### 이메일 관련 동작 {#email-specific-behavior}

- **수신 거부 및 스팸 신고:** Braze는 [커스텀 푸터]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer)를 통해 수신 거부한 사용자를 자동으로 수신 거부 처리합니다. 사용자가 이메일을 스팸으로 신고하면, Braze는 트랜잭션 이메일(**수신 거부한 사용자를 포함한 모든 사용자에게 발송**으로 전송된 메시지)만 발송합니다.
- **하드 바운스:** 이메일 주소가 하드 바운스되면, Braze는 사용자의 구독 상태를 자동으로 `unsubscribed`로 설정하지 않습니다. Braze는 해당 주소를 유효하지 않은 것으로 표시하고 사용자가 이메일 주소를 업데이트할 때까지 발송을 중단합니다.
- **공유 이메일 주소:** 사용자의 글로벌 이메일 구독 상태가 변경되면, Braze는 동일한 이메일 주소를 공유하는 다른 프로필에 해당 상태를 전파하며, 변경당 최대 100개 프로필까지 적용됩니다.
- **이메일 주소 업데이트:** 사용자가 이메일 주소를 업데이트하면, 구독 상태가 `subscribed`로 설정됩니다. 단, 업데이트된 주소가 이미 다른 프로필에 존재하는 경우 해당 프로필의 상태를 상속받습니다.

구독 상태 업데이트, 상태 확인, 환경설정 센터, Campaign 타겟팅에 대한 자세한 내용은 [이메일 구독]({{site.baseurl}}/user_guide/channels/email/subscriptions)을 참조하세요.

## LINE {#line}

LINE 구독 상태의 정보 소스는 LINE입니다. 사용자 프로필에 `native_line_id`가 있더라도, 해당 사용자가 LINE 채널을 팔로우하지 않으면 Braze는 LINE 메시지를 전달하지 않습니다.

LINE 구독 상태는 `external_id`가 아닌 `native_line_id`로 추적됩니다. 여러 프로필이 동일한 `native_line_id`를 공유하면, 동일한 LINE 구독 상태를 상속받습니다.

| 상태 | 정의 |
| ----- | ---------- |
| 구독됨 | 사용자가 LINE 앱 내에서 LINE 채널을 팔로우했습니다. |
| 수신 거부 | 사용자가 LINE 채널을 팔로우하지 않았거나, 명시적으로 팔로우를 해제했습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE 구독 상태" }

### 구독 동기화 도구 {#subscription-sync-tool}

LINE 채널 통합이 성공적으로 완료되면, Braze는 기존 Braze 프로필을 LINE 팔로워 데이터와 정렬하기 위해 구독 동기화 도구를 배포합니다:

- 채널을 팔로우하는 `native_line_id`가 있는 프로필은 `subscribed`로 업데이트됩니다.
- 일치하는 Braze 프로필이 없는 팔로워는 `native_line_id`, `line_id` 사용자 별칭, `subscribed` 상태를 가진 익명 사용자 프로필이 생성됩니다.

통합 중에는 LINE 구독 그룹 상태를 수동으로 설정할 수 없습니다. LINE이 상태를 제어하고, Braze가 이를 동기화합니다.

### 팔로우 및 팔로우 해제 이벤트 업데이트 {#follow-and-unfollow-event-updates}

Braze가 통합된 채널에 대한 LINE 웹훅 이벤트를 수신하면:

- **팔로우:** 일치하는 `native_line_id`를 가진 모든 프로필이 `subscribed`로 설정됩니다. 프로필이 존재하지 않으면, Braze가 [익명 사용자를 생성]({{site.baseurl}}/user_guide/channels/line/message_users/user_management)합니다.
- **팔로우 해제:** 일치하는 `native_line_id`를 가진 모든 프로필이 `unsubscribed`로 설정됩니다.

설정 단계, 사용자 조정, 사용 사례에 대한 자세한 내용은 [LINE 설정]({{site.baseurl}}/user_guide/channels/line/line_setup#user-setup) 및 [LINE 구독 그룹]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups)을 참조하세요.

## SMS 및 RCS {#sms-and-rcs}

SMS와 RCS는 별도의 글로벌 채널 상태가 아닌 구독 그룹 상태를 사용합니다. 사용자는 트랜잭션 그룹에는 `subscribed`이면서 동시에 프로모션 그룹에는 `unsubscribed`일 수 있습니다.

| 상태 | 정의 |
| ----- | ---------- |
| 구독됨 | 사용자가 Braze 구독 API, 옵트인 키워드 또는 기타 지원되는 방법을 통해 특정 구독 그룹에서 SMS 및 RCS를 수신하도록 구독했습니다. [이중 옵트인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)이 활성화된 경우, 사용자는 상태가 `Subscribed`로 업데이트되기 전에 옵트인을 확인해야 합니다. |
| 수신 거부 | 사용자가 옵트아웃 키워드를 문자로 보내거나 [Braze 구독 API]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)를 통해 해당 구독 그룹에서 옵트아웃했습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS 및 RCS 구독 상태" }

### SMS 및 RCS 관련 동작 {#sms-and-rcs-specific-behavior}

- **전화번호 상속:** 프로필에 전화번호가 추가되거나 업데이트되면, 해당 번호는 프로필 또는 이미 해당 번호를 사용하는 기존 프로필의 구독 그룹 상태를 상속받습니다.
- **키워드 처리:** 사용자는 기본 또는 커스텀 [키워드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout)를 문자로 보내 옵트인 또는 옵트아웃할 수 있습니다. Braze는 구독 상태를 자동으로 업데이트합니다.
- **규정 준수:** Braze는 선택한 구독 그룹에 구독되지 않은 사용자에게 SMS 또는 RCS를 발송하지 않습니다.

설정, 발송, 구독 그룹 관리에 대한 자세한 내용은 [SMS, MMS, RCS 구독 그룹]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups)을 참조하세요.

## WhatsApp {#whatsapp}

WhatsApp도 구독 그룹 상태를 사용합니다. Meta는 마케팅 메시지를 발송하기 전에 명시적인 [옵트인 동의](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)를 요구합니다.

| 상태 | 정의 |
| ----- | ---------- |
| 구독됨 | 사용자가 옵트인 플로우 또는 Braze 구독 API를 통해 비즈니스의 WhatsApp 메시지 수신을 명시적으로 확인했습니다. |
| 수신 거부 | 사용자가 옵트인하지 않았거나, 옵트인이 제거되었습니다. 수신 거부 사용자는 해당 구독 그룹의 전화번호에서 메시지를 수신하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsApp 구독 상태" }

### 옵트인 요구 사항 {#opt-in-requirements}

WhatsApp에서 사용자에게 메시지를 보내려면, 각 사용자에 대해 `external_id`, [전화번호]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers), 업데이트된 구독 상태를 Braze에 제공해야 합니다. 웹사이트, 앱, SMS, 인앱 메시지, 인바운드 WhatsApp 스레드를 통해 옵트인을 수집하거나, 이미 다른 곳에서 옵트인한 사용자의 CSV 가져오기를 통해 수집할 수 있습니다.

### 옵트아웃 방법 {#opt-out-methods}

사용자는 다음을 통해 옵트아웃할 수 있습니다:

- **인바운드 키워드 워크플로우:** 옵트아웃 키워드(예: "STOP")에 의해 트리거되는 Canvases 또는 Campaigns로, 구독 상태를 업데이트하는 후속 단계가 포함됩니다.
- **마케팅 옵트아웃 빠른 응답:** Meta의 마케팅 옵트아웃 버튼이 포함된 메시지 템플릿으로, Canvas에서 구독 그룹 업데이트 단계와 연결됩니다.
- **차단 및 신고:** 사용자가 비즈니스를 차단하면, 이후 메시지는 전달되지 않고 요금도 청구되지 않지만, Braze 구독 상태는 업데이트되지 않습니다. 사용자 신고도 구독 상태를 변경하지 않습니다.

### WhatsApp "혜택 및 공지" 토글 {#whatsapp-offers-and-announcements-toggle}

WhatsApp의 기본 **혜택 및 공지** 토글은 Braze 구독 그룹과 별개입니다. 사용자가 WhatsApp에서 이를 끄면, Braze에서 `subscribed`로 표시되더라도 Meta가 마케팅 전달을 차단합니다. 두 레이어는 자동으로 동기화되지 않습니다.

단계별 옵트인 및 옵트아웃 워크플로우에 대한 자세한 내용은 [WhatsApp 옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) 및 [WhatsApp 구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)을 참조하세요.

## 구독 상태별 세분화 및 타겟팅 {#segment-and-target-by-subscription-status}

Segment 빌더에서 구독 상태 필터를 사용하여 채널별로 오디언스를 타겟팅하거나 제외할 수 있습니다. 예를 들어, **Email Subscription Status**, **Push Subscription Status**, **Subscription Group** 필터를 사용할 수 있습니다.

Campaigns 및 Canvases를 구성할 때, **발송 설정** 및 **타겟 오디언스** 옵션을 통해 특정 구독 상태(예: 구독됨 및 옵트인)의 사용자에게만 발송할 수 있습니다. 이메일 및 푸시 필터 정의에 대한 자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 참조하세요.