---
nav_title: "구독"
article_title: "구독"
page_order: 5
description: "이 참조 문서에서는 다양한 사용자 구독 상태, 구독 그룹을 생성하고 관리하는 방법, 그리고 구독을 기반으로 사용자를 세그먼트하는 방법을 다룹니다."
channel:
  - email

---

# 이메일 구독 {#email-subscriptions}

> 사용자 구독 상태, 구독 그룹을 생성하고 관리하는 방법, 그리고 구독을 기반으로 사용자를 세그먼트하는 방법에 대해 알아보세요.

이 문서는 정보 제공 목적으로만 작성되었습니다. 어떠한 형태로든 법적 자문을 제공하거나 법적 자문으로 의존할 수 있는 것이 아닙니다. 마케팅 및 트랜잭션 이메일 발송은 특정 법적 요건의 적용을 받을 수 있습니다. 회사에 적용되는 모든 관련 법률, 규칙 및 규정을 준수하고 있는지 확인하려면 법률 고문 및/또는 규정 준수 팀의 자문을 구해야 합니다.

## 구독 상태 {#subscription-states}

Braze에는 이메일 사용자를 위한 세 가지 글로벌 구독 상태가 있습니다. 이러한 상태는 사용자에게 보내는 메시지를 제어합니다. 예를 들어, `unsubscribed` 상태의 사용자는 `subscribed` 또는 `opted-in`을 대상으로 하는 메시지를 수신하지 않습니다.

| 상태 | 정의 |
| ----- | ---------- |
| 옵트인 | 사용자가 이메일 수신을 명시적으로 확인했습니다. 이메일 발송에 대한 사용자 동의를 얻기 위해 명시적 옵트인 프로세스를 권장합니다. |
| 가입됨 | 사용자가 탈퇴하지도 않았고 이메일 수신에 명시적으로 옵트인하지도 않았습니다. 이것은 고객 프로필이 생성될 때의 기본 구독 상태입니다. |
| 탈퇴됨 | 사용자가 이메일 수신을 명시적으로 탈퇴했습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="구독 상태" }

{% alert note %}
Braze는 글로벌 및 구독 그룹 관련 구독 상태 변경을 데이터 포인트에 포함하지 않습니다.
{% endalert %}

### 탈퇴된 이메일 주소 {#unsubscribed-email-addresses}

Braze는 [사용자 지정 바닥글]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/)을 통해 수동으로 탈퇴한 사용자를 자동으로 구독 취소합니다. 사용자가 이메일 주소를 업데이트하고 **발송 구성**에서 **이메일 업데이트 시 사용자 재구독**이 활성화되어 있으면 정상적인 발송이 재개됩니다.

사용자가 이메일 중 하나 이상을 스팸으로 표시하면 Braze는 해당 사용자에게 트랜잭션 이메일만 발송합니다. 트랜잭션 이메일은 **타겟 오디언스**의 **탈퇴한 사용자를 포함한 모든 사용자에게 발송** 옵션을 의미합니다.

{% alert tip %}
사용자를 효과적으로 재참여시키는 방법에 대한 안내는 [IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/) 모범 사례를 참조하세요.
{% endalert %}

### 반송 및 유효하지 않은 이메일 {#bounces-and-invalid-emails}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}

이메일 주소가 하드바운스되면 Braze는 사용자의 구독 상태를 자동으로 "탈퇴됨"으로 설정하지 않습니다. 주소가 하드바운스(유효하지 않거나 존재하지 않음)되면 Braze는 해당 주소를 유효하지 않음으로 표시하고 추가 발송을 시도하지 않습니다. 사용자가 이메일 주소를 변경하면 Braze는 발송을 재개합니다. Braze는 소프트바운스를 72시간 동안 재시도합니다.

### 이메일 구독 상태 업데이트 {#updating-email-subscription-states}

사용자의 이메일 구독 상태를 업데이트하는 네 가지 방법이 있습니다:

#### SDK 통합 {#sdk-integration}

Braze SDK를 사용하여 사용자의 구독 상태를 업데이트합니다.

#### REST API

[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 사용하여 사용자의 [`email_subscribe` 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens)을 업데이트합니다. 예를 들어, 사용자가 커스텀 탈퇴 링크를 사용할 때 이메일 구독 상태를 탈퇴됨으로 설정하려면 요청의 사용자 속성에 `email_subscribe: "unsubscribed"`를 포함합니다.

#### 고객 프로필 {#user-profile}

1. **사용자 검색**을 통해 사용자를 찾습니다.
2. **참여** 아래에서 **탈퇴됨**, **가입됨** 또는 **옵트인**을 선택하여 사용자의 구독 상태를 변경합니다.

가능한 경우 고객 프로필에는 사용자의 구독이 마지막으로 변경된 타임스탬프도 표시됩니다.

#### 환경설정 센터 {#preference-center}

이메일 하단에 [환경설정 센터](#email-preference-center) Liquid를 포함하여 사용자가 옵트인 또는 옵트아웃할 수 있도록 합니다. Braze는 환경설정 센터에서의 구독 상태 업데이트를 관리합니다.

### 이메일 구독 상태 확인 {#checking-email-subscription-state}

![John Doe의 고객 프로필에서 이메일 구독 상태가 가입됨으로 설정되어 있습니다.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

다음과 같은 방법으로 사용자의 이메일 구독 상태를 확인할 수 있습니다:

1. **REST API 내보내기:** [Segment별 사용자 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) 또는 [식별자별 사용자 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) 엔드포인트를 사용하여 개별 고객 프로필을 JSON 형식으로 내보냅니다.
2. **고객 프로필:** [사용자 검색]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/) 페이지에서 사용자의 프로필을 찾은 다음 **참여** 탭을 선택하여 사용자의 구독 상태를 확인하고 수동으로 업데이트합니다.

사용자가 이메일 주소를 업데이트하면 구독 상태가 가입됨으로 설정됩니다. 업데이트된 이메일 주소가 Braze 워크스페이스의 다른 곳에 이미 존재하는 경우 해당 사용자는 기존 사용자의 구독 상태를 상속받습니다. 단, **발송 구성**에서 **이메일 업데이트 시 사용자 재구독** 설정이 활성화되어 있는 경우는 예외입니다.

구독 상태 변경 문제를 해결하려면 고객 프로필 로그에서 **이메일 구독 상태 변경**을 검토하여 변경 이력과 소스(API 또는 SDK)를 확인하세요.

사용자의 글로벌 이메일 구독 상태가 변경되면 Braze는 동일한 이메일 주소를 공유하는 다른 프로필에 해당 상태를 전파하며, 변경당 최대 100개의 프로필까지 처리합니다. 100개 이상의 프로필이 동일한 이메일 주소를 공유하는 경우 Braze는 전파를 보장하지 않습니다. 동일한 이메일을 공유하는 사용자가 서로 다른 구독 상태를 보이는 경우 Braze 고객지원에 문의하세요.

## 구독 그룹 {#subscription-groups}

구독 그룹은 [글로벌 구독 상태](#subscription-states)에서 오디언스를 더 세분화할 수 있는 Segment 필터입니다. 이 그룹을 통해 최종 사용자에게 더 세분화된 구독 옵션을 제공할 수 있습니다.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

예를 들어, 여러 카테고리의 이메일 Campaign(프로모션, 뉴스레터 또는 제품 업데이트)을 발송한다고 가정해 보겠습니다. 이 경우 구독 그룹을 사용하여 고객이 [이메일 환경설정 센터](#email-preference-center)를 통해 단일 페이지에서 구독하거나 탈퇴할 이메일 카테고리를 선택할 수 있도록 할 수 있습니다. 또는 구독 그룹을 사용하여 일간, 주간 또는 월간 이메일에 대한 구독 그룹을 생성하여 고객이 이메일 수신 빈도를 선택할 수 있도록 할 수도 있습니다.

[구독 그룹 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/)를 사용하여 Braze 대시보드의 **구독 그룹** 페이지에 저장된 구독 그룹을 프로그래밍 방식으로 관리합니다.

### 구독 그룹 생성 {#creating-a-subscription-group}

1. **오디언스** > **구독 그룹 관리**로 이동합니다.
2. **이메일 구독 그룹 생성**을 선택합니다.
3. 구독 그룹에 이름과 설명을 입력합니다.
4. **저장**을 선택합니다.

모든 구독 그룹은 환경설정 센터에 자동으로 추가됩니다.

![구독 그룹을 생성하기 위한 필드.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### 구독 그룹으로 세그먼트하기 {#segmenting-with-a-subscription-group}

Segment를 생성할 때 구독 그룹 이름을 필터로 설정합니다. 이렇게 하면 그룹에 옵트인한 사용자가 이메일을 수신하게 됩니다. 이는 월간 뉴스레터, 쿠폰, 멤버십 등급 등에 유용합니다.

!["이탈 사용자" Segment에서 "주간 이메일" 구독 그룹의 사용자를 필터로 타겟팅하는 예시.]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### 구독 그룹 아카이브 {#archiving-subscription-groups}

아카이브된 구독 그룹은 편집할 수 없으며 Segment 필터나 환경설정 센터에 더 이상 표시되지 않습니다. 이메일, Campaign 또는 Canvas에서 Segment 필터로 사용 중인 그룹을 아카이브하려고 하면 해당 그룹의 모든 사용을 제거할 때까지 아카이브를 방지하는 오류 메시지가 표시됩니다.

**구독 그룹** 페이지에서 그룹을 아카이브하려면 다음을 수행합니다:

1. 구독 그룹 목록에서 그룹을 찾습니다.
2. <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;드롭다운 메뉴에서 **아카이브**를 선택합니다.

Braze는 아카이브된 그룹의 사용자에 대한 상태 변경을 처리하지 않습니다. 예를 들어, Alex가 구독 그룹 1에 가입된 상태에서 해당 그룹을 아카이브하면 Alex가 탈퇴 링크를 클릭하더라도 "가입됨" 상태로 유지됩니다. 구독 그룹 1이 아카이브되어 해당 그룹을 사용하여 메시지를 보낼 수 없으므로 이는 문제가 되지 않습니다.

#### 구독 그룹 크기 확인 {#viewing-subscription-group-sizes}

**구독 그룹** 페이지의 **구독 그룹 시계열** 그래프를 참조하여 일정 기간 동안의 사용자 수를 기반으로 구독 그룹 크기를 확인할 수 있습니다. 이러한 구독 그룹 크기는 Segment 크기 계산 등 Braze의 다른 영역과도 일관됩니다.

![12월 2일부터 11일까지의 "구독 그룹 시계열" 그래프 예시. 그래프는 6일에서 7일 사이에 사용자 수가 약 1,000만 명 증가한 것을 보여줍니다.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

시계열 수치가 **이메일 구독 상태가 탈퇴됨**을 사용하는 Segment와 크게 다른 경우, 그래프는 해당 **구독 그룹**의 멤버십을 집계하는 반면 해당 필터는 **글로벌** 이메일 구독 상태를 반영한다는 점을 기억하세요. 예를 들어, 사용자가 글로벌로는 가입됨 상태이지만 특정 그룹에서는 탈퇴한 상태일 수 있습니다.

#### Campaign 분석에서 구독 그룹 확인 {#viewing-subscription-groups-in-campaign-analytics}

특정 이메일 Campaign에서 구독 상태를 변경(가입 또는 탈퇴)한 사용자 수를 해당 Campaign의 분석 페이지에서 확인할 수 있습니다.

1. Campaign의 **Campaign 분석** 페이지에서 **이메일 메시지 성과** 섹션으로 스크롤합니다.
2. **구독 그룹** 아래의 화살표를 선택하여 고객이 제출한 상태 변경의 총 수를 확인합니다.

![고객이 제출한 상태 변경의 총 수를 표시하는 "이메일 메시지 성과" 페이지.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### 사용자의 이메일 구독 그룹 확인 {#checking-a-users-email-subscription-group}

- **고객 프로필:** Braze 대시보드의 [사용자 검색]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#access-profiles) 페이지에서 개별 고객 프로필에 접근할 수 있습니다. 여기에서 이메일 주소, 전화번호 또는 외부 사용자 ID로 고객 프로필을 조회할 수 있습니다. **참여** 탭에서 사용자의 이메일 구독 그룹도 확인할 수 있습니다.
- **Braze REST API:** [사용자의 구독 그룹 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) 또는 [사용자의 구독 그룹 상태 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)를 사용하여 개별 고객 프로필의 구독 그룹을 확인합니다.

## 이메일 환경설정 센터 {#email-preference-center}

이메일 환경설정 센터를 통해 어떤 사용자가 구독 그룹 뉴스레터를 수신할지 관리할 수 있습니다. 대시보드의 **구독 그룹** 아래에서 찾을 수 있습니다. 생성한 각 구독 그룹은 환경설정 센터 목록에 추가됩니다.

환경설정 센터를 추가하거나 커스터마이즈하는 방법에 대해 자세히 알아보려면 [환경설정 센터]({{site.baseurl}}/user_guide/channels/email/subscriptions/)를 참조하세요.

## 이메일 구독 변경 {#changing-email-subscriptions}

대부분의 경우 사용자는 수신한 이메일에 포함된 링크를 통해 이메일 구독을 관리합니다. 모든 이메일 하단에 탈퇴 링크가 포함된 법적 요건을 준수하는 바닥글을 삽입하세요. 사용자가 탈퇴 URL을 선택하면 Braze가 해당 사용자를 탈퇴 처리하고 변경을 확인하는 랜딩 페이지를 표시합니다. 다음 Liquid 태그를 포함하세요: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

사용자가 환경설정 센터에서 "위의 모든 유형의 이메일 수신 거부"를 선택하면 Braze는 해당 사용자의 글로벌 이메일 구독 상태를 `unsubscribed`로 설정하고 모든 그룹에서 탈퇴 처리합니다.

### 사용자 지정 바닥글 생성 {#custom-footer}

기본 바닥글을 사용하지 않으려면 워크스페이스 전체에 적용되는 사용자 지정 이메일 바닥글을 생성하고 {% raw %}`{{${email_footer}}}`{% endraw %}를 사용하여 모든 이메일에 템플릿으로 적용합니다.

이렇게 하면 모든 이메일 템플릿이나 이메일 Campaign에 대해 새 바닥글을 생성할 필요가 없습니다. 단계별 안내는 [사용자 지정 이메일 바닥글]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/)을 참조하세요.

#### 중국 IP 주소에 대한 구독 상태 관리 {#managing-subscription-states-for-chinese-ip-addresses}

중국 IP 주소가 예상되는 경우 `unsubscribed` 목록을 유지하기 위해 탈퇴 링크에만 의존하지 마세요. 고객지원 티켓이나 담당자 이메일과 같은 대체 탈퇴 경로를 제공하세요.

### 사용자 지정 구독취소 페이지 생성 {#creating-a-custom-unsubscribe-page}

사용자가 이메일에서 탈퇴 URL을 선택하면 구독 변경을 확인하는 기본 랜딩 페이지가 열립니다.

사용자 지정 랜딩 페이지를 대신 사용하려면:

1. **이메일 환경설정** > **가입 페이지 및 바닥글**로 이동합니다.
2. 사용자 지정 페이지의 HTML을 추가합니다.

사용자가 실수로 탈퇴한 경우 되돌릴 수 있도록 재구독 링크(예: {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %})를 포함하세요.

또한 사용자를 사이트로 보내고 Braze REST API로 상태를 업데이트할 수도 있습니다(예: {% raw %}`?user_id={{${user_id}}}`{% endraw %}가 포함된 링크를 사용한 다음 [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)를 호출).

{% alert note %}
HTML 콘텐츠 블록만이 아닌 대시보드 바닥글을 사용하는 경우 템플릿에 여전히 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}가 포함되어야 저장할 수 있습니다. 다른 탈퇴 URL을 일시적으로 사용하려면 기본 태그를 주석 처리할 수 있습니다. 예시: {% raw %}`<!-- {{${set_user_to_unsubscribed_url}}} -->`{% endraw %}.
{% endalert %}

![미리보기에 "떠나시다니 아쉽습니다!"가 표시된 사용자 지정 구독취소 페이지.]({% image_buster /assets/img/custom_unsubscribe.png %})

### 사용자 지정 옵트인 페이지 생성 {#creating-a-custom-opt-in-page}

사용자 지정 옵트인 페이지를 사용하여 사용자가 구독 전에 알림 환경설정을 확인하고 제어할 수 있도록 합니다. 이 추가 커뮤니케이션은 이메일 Campaign이 스팸 폴더에 들어가지 않도록 하는 데 도움이 됩니다.

1. **설정** > **이메일 환경설정**으로 이동합니다.
2. **가입 페이지 및 바닥글**을 선택합니다.
3. **사용자 지정 옵트인 페이지** 섹션에서 스타일을 커스터마이즈하여 사용자에게 구독되었음을 어떻게 표시할지 확인합니다.

사용자는 {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} 태그를 통해 이 페이지에 도달합니다.

{% alert tip %}
더블 옵트인 프로세스를 사용하여 도달률을 개선하세요. Braze가 추가 확인 이메일을 보내면 사용자가 링크를 통해 알림 환경설정을 확인합니다. 확인 후 사용자는 옵트인됩니다.
{% endalert %}

!["아직 소식을 받고 싶으시다니 기쁩니다"라는 메시지가 포함된 사용자 지정 옵트인 이메일.]({% image_buster /assets/img/custom_optin.png %})

## 구독 및 Campaign 타겟팅 {#subscriptions-and-campaign-targeting}

기본적으로 Braze는 푸시 또는 이메일 메시지가 포함된 Campaign을 가입됨 또는 옵트인 상태의 사용자를 대상으로 합니다. **타겟 오디언스**에서 **다음 사용자에게 발송:** 옆의 드롭다운을 선택하여 이를 변경합니다.

Braze는 세 가지 타겟팅 상태를 지원합니다:

- 가입됨 또는 옵트인 상태의 사용자(기본값).
- 옵트인 상태의 사용자만.
- 탈퇴한 사용자를 포함한 모든 사용자.

{% alert important %}
이러한 타겟팅 설정을 사용할 때 해당되는 [스팸 관련 법률]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations)을 준수하는 것은 사용자의 책임입니다.
{% endalert %}

## 사용자 구독별 세그먼트 {#segmenting-by-user-subscriptions}

"이메일 구독 상태" 및 "푸시 구독 상태" 필터를 사용하여 구독 상태별로 사용자를 세그먼트합니다.

이를 사용하여 옵트인도 옵트아웃도 하지 않은 사용자를 타겟팅하고 명시적 옵트인을 유도합니다. "이메일/푸시 구독 상태가 가입됨" 필터로 Segment를 생성하고 가입됨 상태이지만 옵트인하지 않은 사용자에게 Campaign을 발송합니다.

![Segment 필터로 사용된 이메일 구독 상태.]({% image_buster /assets/img_archive/not_optin.png %})