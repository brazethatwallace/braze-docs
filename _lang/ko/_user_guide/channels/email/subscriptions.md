---
nav_title: "구독"
article_title: "구독"
page_order: 5
description: "이 참조 문서에서는 다양한 사용자 구독 상태, 이메일 구독을 관리하는 방법, 그리고 구독을 기반으로 사용자를 세그먼트하는 방법을 다룹니다."
channel:
  - email

---

# 이메일 구독 {#email-subscriptions}

> 글로벌 이메일 구독 상태, 푸터 및 탈퇴 페이지, 환경설정 센터, Campaign 타겟팅에 대해 알아보세요. 모든 채널의 구독 그룹에 대해서는 [구독 그룹]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)을 참조하세요.

이 문서는 정보 제공 목적으로만 작성되었습니다. 어떠한 형태로든 법적 자문을 제공하거나 법적 자문으로 의존할 수 있는 것이 아닙니다. 마케팅 및 트랜잭션 이메일 발송은 특정 법적 요건의 적용을 받을 수 있습니다. 회사에 적용되는 모든 관련 법률, 규칙 및 규정을 준수하고 있는지 확인하려면 법률 고문 및/또는 규정 준수 팀의 자문을 구해야 합니다.

## 구독 상태 {#subscription-states}

Braze는 글로벌 구독 상태를 사용하여 이메일을 수신할 사용자를 제어합니다. `opted-in`, `subscribed`, `unsubscribed`의 정의, 글로벌 상태와 구독 그룹의 차이점, 다른 채널에서 구독 상태가 작동하는 방식에 대해서는 [구독 상태]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#email)를 참조하세요.

### 탈퇴된 이메일 주소 {#unsubscribed-email-addresses}

Braze는 [커스텀 바닥글]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer)을 통해 수동으로 탈퇴한 사용자를 자동으로 구독 취소합니다. 사용자가 이메일 주소를 업데이트하고 **발송 구성**에서 **이메일 업데이트 시 사용자 재구독**이 활성화되어 있으면 정상적인 발송이 재개됩니다.

사용자가 이메일 중 하나 이상을 스팸으로 표시하면 Braze는 해당 사용자에게 트랜잭션 이메일만 발송합니다. 트랜잭션 이메일은 **타겟 오디언스**의 **탈퇴한 사용자를 포함한 모든 사용자에게 발송** 옵션을 의미합니다.

{% alert tip %}
사용자를 효과적으로 재참여시키는 방법에 대한 안내는 [IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) 모범 사례를 참조하세요.
{% endalert %}

### 반송 및 유효하지 않은 이메일 {#bounces-and-invalid-emails}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}

이메일 주소가 하드바운스되면 Braze는 사용자의 구독 상태를 자동으로 "탈퇴됨"으로 설정하지 않습니다. 주소가 하드바운스(유효하지 않거나 존재하지 않음)되면 Braze는 해당 주소를 유효하지 않음으로 표시하고 추가 발송을 시도하지 않습니다. 사용자가 이메일 주소를 변경하면 Braze는 발송을 재개합니다. Braze는 소프트바운스를 72시간 동안 재시도합니다.

### 이메일 구독 상태 업데이트 {#updating-email-subscription-states}

사용자의 이메일 구독 상태를 업데이트하는 네 가지 방법이 있습니다:

#### SDK 통합 {#sdk-integration}

Braze SDK를 사용하여 사용자의 구독 상태를 업데이트합니다.

#### REST API

[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 사용하여 사용자의 [`email_subscribe` 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)을 업데이트합니다. 예를 들어, 사용자가 커스텀 탈퇴 링크를 사용할 때 이메일 구독 상태를 탈퇴됨으로 설정하려면 요청의 사용자 속성에 `email_subscribe: "unsubscribed"`를 포함합니다.

#### 고객 프로필 {#user-profile}

1. **사용자 검색**을 통해 사용자를 찾습니다.
2. **참여** 아래에서 **탈퇴됨**, **가입됨** 또는 **옵트인**을 선택하여 사용자의 구독 상태를 변경합니다.

고객 프로필에는 사용자의 구독이 마지막으로 변경된 타임스탬프도 표시됩니다. 타임스탬프는 상태가 **옵트인** 또는 **탈퇴됨**일 때 기록되지만, **가입됨** 상태일 때는 기록되지 않습니다. 예를 들어, 명시적으로 옵트인하거나 옵트아웃한 적이 없는 새로 생성된 프로필에는 구독 타임스탬프가 없습니다.

#### 환경설정 센터 {#preference-center}

이메일 하단에 [환경설정 센터](#email-preference-center) Liquid를 포함하여 사용자가 옵트인 또는 옵트아웃할 수 있도록 합니다. Braze는 환경설정 센터에서의 구독 상태 업데이트를 관리합니다.

### 이메일 구독 상태 확인 {#checking-email-subscription-state}

![John Doe의 고객 프로필에서 이메일 구독 상태가 가입됨으로 설정되어 있습니다.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

다음과 같은 방법으로 사용자의 이메일 구독 상태를 확인할 수 있습니다:

1. **REST API 내보내기:** [Segment별 사용자 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) 또는 [식별자별 사용자 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) 엔드포인트를 사용하여 개별 고객 프로필을 JSON 형식으로 내보냅니다.
2. **고객 프로필:** [사용자 검색]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) 페이지에서 사용자의 프로필을 찾은 다음 **참여** 탭을 선택하여 사용자의 구독 상태를 확인하고 수동으로 업데이트합니다.

사용자가 이메일 주소를 업데이트하면 구독 상태가 가입됨으로 설정됩니다. 업데이트된 이메일 주소가 Braze 워크스페이스의 다른 곳에 이미 존재하는 경우 해당 사용자는 기존 사용자의 구독 상태를 상속받습니다. 단, **발송 구성**에서 **이메일 업데이트 시 사용자 재구독** 설정이 활성화되어 있는 경우는 예외입니다.

구독 상태 변경 문제를 해결하려면 고객 프로필 로그에서 **이메일 구독 상태 변경**을 검토하여 변경 이력과 소스를 확인하세요. 다음 소스가 이메일 구독 상태 변경을 트리거할 수 있습니다:

| 소스 | 설명 |
| ------ | ----------- |
| SDK | Braze SDK를 통해 전송된 사용자 속성 업데이트 |
| REST API | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트를 통해 전송된 사용자 속성 업데이트 |
| 대시보드 | 고객 프로필 페이지에서 수동으로 변경된 구독 상태 |
| CSV 가져오기 | 사용자 CSV 가져오기 중 설정된 구독 상태 |
| 환경설정 센터 | Braze에서 호스팅하는 환경설정 센터에서 사용자가 환경설정을 업데이트함 |
| 구독 페이지 | 사용자가 이메일의 탈퇴 링크를 선택하고 Braze 구독 페이지에 도달함 |
| List-Unsubscribe | 사용자가 이메일 클라이언트의 기본 list-unsubscribe 헤더를 통해 탈퇴함 |
| Canvas 사용자 업데이트 단계 | Canvas의 [사용자 업데이트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update)에 의해 업데이트된 구독 상태 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이메일 구독 상태 업데이트 소스" }

사용자의 글로벌 이메일 구독 상태가 변경되면 Braze는 동일한 이메일 주소를 공유하는 다른 프로필에 해당 상태를 전파하며, 변경당 최대 100개의 프로필까지 처리합니다. 100개 이상의 프로필이 동일한 이메일 주소를 공유하는 경우 Braze는 전파를 보장하지 않습니다. 동일한 이메일을 공유하는 사용자가 서로 다른 구독 상태를 보이는 경우 Braze 고객지원에 문의하세요.

## 구독 그룹 {#subscription-groups}

이메일 구독 그룹을 사용하면 사용자가 글로벌 이메일 구독 상태를 변경하지 않고도 특정 이메일 카테고리(예: 뉴스레터 또는 프로모션)에 옵트인하거나 옵트아웃할 수 있습니다. 생성한 그룹은 [환경설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)에 추가할 수 있습니다.

그룹 생성, 세그먼팅, 보관 및 채널별 동작에 대한 자세한 내용은 [구독 그룹]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups)을 참조하세요.

## 이메일 수신 설정 센터 {#email-preference-center}

이메일 수신 설정 센터를 사용하면 구독 그룹 뉴스레터를 수신하는 사용자를 관리할 수 있습니다. 대시보드에서 **구독 그룹** 아래에서 확인할 수 있습니다. 생성한 각 구독 그룹은 수신 설정 센터 목록에 추가됩니다.

수신 설정 센터를 추가하거나 커스터마이즈하는 방법에 대해 자세히 알아보려면 [수신 설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)를 참조하세요.

## 이메일 구독 변경 {#changing-email-subscriptions}

대부분의 경우 사용자는 수신한 이메일에 포함된 링크를 통해 이메일 구독을 관리합니다. 모든 이메일 하단에 탈퇴 링크가 포함된 법적 요건을 준수하는 바닥글을 삽입하세요. 사용자가 탈퇴 URL을 선택하면 Braze가 해당 사용자를 탈퇴 처리하고 변경을 확인하는 랜딩 페이지를 표시합니다. 다음 Liquid 태그를 포함하세요: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

{% alert note %}
{%raw%}`${set_user_to_unsubscribed_url}`{%endraw%} Liquid 태그는 이메일 Campaign과 Canvases에서만 사용할 수 있습니다. 다른 메시징 채널에서는 이 태그를 사용할 수 없습니다.
{% endalert %}

사용자가 환경설정 센터에서 "나열된 모든 유형의 이메일 수신 거부"를 선택하면 Braze는 해당 사용자의 글로벌 이메일 구독 상태를 `unsubscribed`로 설정하고 모든 그룹에서 탈퇴 처리합니다.

수신자 측 이메일 탈퇴(탈퇴 링크, list-unsubscribe, 환경설정 센터 제출, ESP가 보고한 탈퇴)는 Snowflake의 `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` 테이블에 표시됩니다. REST API를 통해 수행된 탈퇴는 해당 테이블에 포함되지 않으며, 대신 [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) 또는 [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events) 이벤트가 발생합니다. 테이블 스키마에 대해서는 [USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED)를 참조하세요.

### 커스텀 바닥글 생성 {#custom-footer}

기본 바닥글을 사용하지 않으려면 워크스페이스 전체에 적용되는 커스텀 이메일 바닥글을 생성하고 {% raw %}`{{${email_footer}}}`{% endraw %}를 사용하여 모든 이메일에 템플릿으로 적용합니다.

이렇게 하면 모든 이메일 템플릿이나 이메일 Campaign에 대해 새 바닥글을 생성할 필요가 없습니다. 단계별 안내는 [커스텀 이메일 바닥글]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer)을 참조하세요.

#### 중국 IP 주소에 대한 구독 상태 관리 {#managing-subscription-states-for-chinese-ip-addresses}

중국 IP 주소가 예상되는 경우 `unsubscribed` 목록을 유지하기 위해 탈퇴 링크에만 의존하지 마세요. 고객지원 티켓이나 담당자 이메일과 같은 대체 탈퇴 경로를 제공하세요.

### 커스텀 구독취소 페이지 생성 {#creating-a-custom-unsubscribe-page}

사용자가 이메일에서 탈퇴 URL을 선택하면 구독 변경을 확인하는 기본 랜딩 페이지가 열립니다.

커스텀 랜딩 페이지를 대신 사용하려면:

1. **이메일 환경설정** > **구독 페이지 및 바닥글**로 이동합니다.
2. 커스텀 페이지의 HTML을 추가합니다.

사용자가 실수로 탈퇴한 경우 되돌릴 수 있도록 재구독 링크(예: {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %})를 포함하세요. {% raw %}`${set_user_to_unsubscribed_url}`{% endraw %}와 마찬가지로 이 태그는 이메일 Campaign과 Canvases에서만 사용할 수 있습니다.

또한 사용자를 사이트로 보내고 Braze REST API로 상태를 업데이트할 수도 있습니다(예: {% raw %}`?user_id={{${user_id}}}`{% endraw %}가 포함된 링크를 사용한 다음 [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)를 호출).

{% alert note %}
HTML 콘텐츠 블록만이 아닌 대시보드 바닥글을 사용하는 경우 템플릿에 여전히 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}가 포함되어야 저장할 수 있습니다. 다른 탈퇴 URL을 일시적으로 사용하려면 기본 태그를 주석 처리할 수 있습니다. 예시: {% raw %}`<!-- {{${set_user_to_unsubscribed_url}}} -->`{% endraw %}.
{% endalert %}

![미리보기에 "떠나시다니 아쉽습니다!"가 표시된 커스텀 구독취소 페이지.]({% image_buster /assets/img/custom_unsubscribe.png %})

### 커스텀 옵트인 페이지 생성 {#creating-a-custom-opt-in-page}

커스텀 옵트인 페이지를 사용하여 사용자가 구독 전에 알림 환경설정을 확인하고 제어할 수 있도록 합니다. 이 추가 커뮤니케이션은 이메일 Campaign이 스팸 폴더에 들어가지 않도록 하는 데 도움이 됩니다.

1. **설정** > **이메일 환경설정**으로 이동합니다.
2. **구독 페이지 및 바닥글**을 선택합니다.
3. **커스텀 옵트인 페이지** 섹션에서 스타일을 커스터마이즈하여 사용자에게 구독되었음을 어떻게 표시할지 확인합니다.

사용자는 {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} 태그를 통해 이 페이지에 도달합니다. 다른 이메일 구독 Liquid 태그와 마찬가지로 이 태그는 이메일 Campaign과 Canvases에서만 사용할 수 있습니다.

{% alert tip %}
더블 옵트인 프로세스를 사용하여 도달률을 개선하세요. Braze가 추가 확인 이메일을 보내면 사용자가 링크를 통해 알림 환경설정을 확인합니다. 확인 후 사용자는 옵트인됩니다.
{% endalert %}

!["아직 소식을 받고 싶으시다니 기쁩니다"라는 메시지가 포함된 커스텀 옵트인 이메일.]({% image_buster /assets/img/custom_optin.png %})

## 구독 및 Campaign 타겟팅 {#subscriptions-and-campaign-targeting}

기본적으로 Braze는 푸시 또는 이메일 메시지가 포함된 Campaign을 가입됨 또는 옵트인 상태의 사용자를 대상으로 합니다. **타겟 오디언스**에서 **다음 사용자에게 발송:** 옆의 드롭다운을 선택하여 이를 변경합니다.

Braze는 세 가지 타겟팅 상태를 지원합니다:

- 가입됨 또는 옵트인 상태의 사용자(기본값).
- 옵트인 상태의 사용자만.
- 탈퇴한 사용자를 포함한 모든 사용자.

{% alert important %}
이러한 타겟팅 설정을 사용할 때 해당되는 [스팸 관련 법률]({{site.baseurl}}/help/best_practices/spam_regulations#spam-regulations)을 준수하는 것은 사용자의 책임입니다.
{% endalert %}

## 사용자 구독별 세분화 {#segmenting-by-user-subscriptions}

"이메일 구독 상태" 및 "푸시 구독 상태" 필터를 사용하여 구독 상태별로 사용자를 세분화합니다.

이를 사용하여 옵트인도 옵트아웃도 하지 않은 사용자를 타겟팅하고 명시적 옵트인을 유도합니다. "이메일/푸시 구독 상태가 가입됨" 필터로 Segment를 생성하고 가입됨 상태이지만 옵트인하지 않은 사용자에게 Campaign을 발송합니다.

![Segment 필터로 사용된 이메일 구독 상태.]({% image_buster /assets/img_archive/not_optin.png %})