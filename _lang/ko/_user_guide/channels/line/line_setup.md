---
nav_title: "설정"
article_title: LINE 설정
description: "이 문서에서는 필수 조건과 권장 다음 단계를 포함하여 Braze LINE 채널을 설정하는 방법을 다룹니다."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# LINE 설정 {#line-setup}

> 이 문서에서는 사용자 설정, 사용자 ID 조정, Braze에서 LINE 테스트 사용자 생성 방법을 포함하여 Braze에서 LINE 채널을 설정하는 방법을 다룹니다.

## 사전 요구 사항 {#prerequisites}

LINE을 Braze와 통합하려면 다음이 필요합니다:

- [LINE 비즈니스 계정](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- 프리미엄 또는 인증된 계정 상태(기존 팔로워 동기화에 필요)
   - [LINE 계정 가이드라인](https://terms2.line.me/official_account_guideline_oth) 보기
- [LINE 개발자 계정](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE 메시징 API 채널](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Braze에서 LINE 메시지를 전송하면 계정의 메시지 또는 액션 크레딧이 차감됩니다.

{% alert note %}
**`native_line_id` 설정**: Braze에 사용자 업데이트를 전송하여 `native_line_id`를 설정할 수 있습니다(예: [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트, [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) 사용). 클라이언트 측 SDK에 `native_line_id` 전용 필드가 없는 경우, 이러한 메서드 중 하나를 사용하여 서버 측 사용자 업데이트로 전송하세요.
{% endalert %}

## LINE 계정 유형 {#types-of-line-accounts}

| 계정 유형 | 설명 |
| --- | --- |
| 미인증 계정 | 누구나(개인 또는 법인) 취득할 수 있는 미심사 계정입니다. 이 계정은 회색 배지로 표시되며 LINE 앱 내 검색 결과에 나타나지 않습니다. |
| 인증 계정 | LINE Yahoo 심사를 통과한 계정입니다. 이 계정은 파란색 배지로 표시되며 LINE 앱 내 검색 결과에 나타납니다.<br><br>이 계정은 일본, 대만, 태국, 인도네시아에 기반한 계정에서만 사용할 수 있습니다. |
| 프리미엄 계정 | LINE Yahoo 심사를 통과한 계정입니다. 이 계정은 녹색 배지로 표시되며 LINE 앱 내 검색 결과에 나타납니다. 이 계정 유형은 LINE의 재량에 따라 심사 과정에서 자동으로 부여됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE 계정 유형" }

### 필요한 계정 유형 {#required-account-type}

팔로워를 Braze에 동기화하려면 LINE 계정이 인증 또는 프리미엄 상태여야 합니다. 계정을 생성하면 기본 상태는 미인증입니다. 계정 인증을 요청해야 합니다.

### 인증 LINE 계정 신청 {#applying-for-a-verified-line-account}

{% alert important %}
인증 계정은 일본, 대만, 태국, 인도네시아에 기반한 계정에서만 사용할 수 있습니다.
{% endalert %}

1. LINE **Official Account** 페이지에서 **Settings**를 선택합니다.
2. **Information Disclosure Verification Status** 아래에서 **Request Account Verification**을 선택합니다.
3. 필요한 정보를 입력합니다.
4. 심사 결과가 포함된 알림을 기다립니다.

## LINE 통합 {#integrating-line}

일관된 사용자 업데이트를 설정하고, 기존 사용자의 LINE ID를 가져오며, 모든 사용자를 LINE의 구독 상태와 동기화하려면 다음 단계를 따르세요.

1. [기존에 알려진 사용자 가져오기 또는 업데이트](#step-1-import-or-update-existing-line-users)
2. [LINE 채널 통합](#step-2-integrate-line-channel)
3. [사용자 ID 조정](#step-3-reconcile-user-ids)
4. [사용자 업데이트 방법 변경](#step-4-change-your-user-update-methods)
5. [(선택 사항) 고객 프로필 병합](#step-5-merge-profiles-optional)

{% alert note %}
하나의 워크스페이스에는 하나의 LINE 계정만 사용할 수 있습니다. LINE 계정이 여러 개인 경우, 각 계정을 별도의 워크스페이스에서 사용하는 것을 권장합니다.
{% endalert %}

## 1단계: 기존 LINE 사용자 가져오기 또는 업데이트 {#step-1-import-or-update-existing-line-users}

이 단계는 기존에 식별된 LINE 사용자가 있는 경우에 필요합니다. Braze가 나중에 자동으로 해당 사용자의 구독 상태를 가져와 올바른 고객 프로필을 업데이트하기 때문입니다. 이전에 사용자와 LINE ID를 연결한 적이 없다면 이 단계를 건너뛰세요.

Braze가 지원하는 모든 방법을 사용하여 사용자를 가져오거나 업데이트할 수 있습니다. [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트, [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv), 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 활용할 수 있습니다.

어떤 방법을 사용하든 `native_line_id`를 업데이트하여 사용자의 LINE ID를 제공하세요. `native_line_id`에 대해 자세히 알아보려면 [사용자 설정](#user-setup)을 참조하세요.

{% alert note %}
구독 그룹 상태는 지정할 필요가 없으며, 지정하더라도 무시됩니다. LINE이 사용자 구독 상태의 정보 소스이며, 구독 동기화 도구 또는 이벤트 업데이트를 통해 Braze에 동기화됩니다.
{% endalert %}

## 2단계: LINE 채널 통합 {#step-2-integrate-line-channel}

통합 프로세스가 완료되면 Braze는 해당 채널의 LINE 팔로워를 자동으로 Braze에 가져옵니다. 이미 Braze 고객 프로필과 연결된 LINE ID의 경우 각 프로필이 "subscribed" 상태로 업데이트되며, 나머지 LINE ID는 익명 사용자를 생성합니다. 또한 LINE 채널의 새로운 팔로워가 채널을 팔로우하면 미식별 고객 프로필이 생성됩니다.

### 2.1단계: 웹훅 설정 편집 {#step-21-edit-webhook-settings}

1. LINE에서 **Messaging API** 탭으로 이동하여 **Webhook settings**를 편집합니다:
   - **Webhook URL**을 `https://anna.braze.com/line/events`로 설정합니다.
      - Braze는 통합 시 대시보드 클러스터에 따라 이 URL을 자동으로 다른 URL로 변경합니다.
   - **Use webhook**과 **Webhook redelivery**를 켭니다. <br><br> ![웹훅 URL을 확인하거나 편집하고, "Use webhook", "Webhook redelivery", "Error statistics aggregation"을 켜거나 끌 수 있는 웹훅 설정 페이지.]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. **Providers** 탭에서 다음 정보를 확인합니다:

| 정보 유형 | 위치 |
| --- | --- |
| Provider ID | 공급자를 선택한 다음 **Settings** > **Basic information**으로 이동합니다 |
| Channel ID | 공급자를 선택한 다음 **Channels** > 해당 채널 > **Basic settings**로 이동합니다 |
| Channel secret | 공급자를 선택한 다음 **Channels** > 해당 채널 > **Basic settings**로 이동합니다. |
| Channel access token | 공급자를 선택한 다음 **Channels** > 해당 채널 > **Messaging API**로 이동합니다. 채널 액세스 토큰이 없으면 **Issue**를 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2.1단계: 웹훅 설정 편집" }

{% alert note %}
이미 통합된 LINE 채널의 채널 시크릿과 채널 액세스 토큰을 업데이트하거나 교체하려면 **파트너 통합** > **기술 파트너** > **LINE**으로 이동하여 해당 통합을 선택합니다.
{% endalert %}

{: start="3"}
3. **Settings** 페이지 > **Response settings**로 이동하여 다음을 수행합니다:
   - **Greeting message**를 끕니다. 이 기능은 Braze에서 팔로우 시 트리거하여 처리할 수 있습니다.
   - **Auto-response messages**를 끕니다. 모든 트리거 메시징은 Braze를 통해 이루어져야 합니다. 이 설정은 LINE 콘솔에서 직접 전송하는 것을 막지 않습니다.
   - **Webhooks**를 켭니다.

![계정의 채팅 처리 방식을 토글로 설정할 수 있는 응답 설정 페이지.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### 2.2단계: Braze에서 LINE 구독 그룹 생성 {#step-22-generate-line-subscription-groups-in-braze}

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

1. Braze의 LINE 기술 파트너 페이지로 이동하여 LINE **Providers** 탭에서 확인한 정보를 입력합니다:
   - Provider ID
   - Channel ID
   - Channel secret
   - Channel access token

LINE 계정에 IP 화이트리스트를 추가하려면 [IP 허용 목록]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting)에 나열된 클러스터의 모든 IP 주소를 허용 목록에 추가합니다.

{% alert important %}
통합 시 채널 시크릿이 올바른지 반드시 확인하세요. 올바르지 않으면 구독 상태에 불일치가 발생할 수 있습니다.
{% endalert %}

![LINE 통합 섹션이 있는 LINE 메시징 통합 페이지.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. 연결이 완료되면 Braze는 워크스페이스에 성공적으로 추가된 각 LINE 통합에 대해 Braze 구독 그룹을 자동으로 생성합니다. <br><br> 팔로워 목록의 변경 사항(새 팔로워 또는 언팔로우 등)은 자동으로 Braze에 반영됩니다.

![LINE 채널에 대한 하나의 구독 그룹을 표시하는 LINE 구독 그룹 섹션.]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## 3단계: 사용자 ID 조정 {#step-3-reconcile-user-ids}

[사용자 ID 조정](#user-id-reconciliation)의 단계를 따라 사용자의 LINE ID를 기존 Braze 고객 프로필과 결합하세요.

## 4단계: 사용자 업데이트 방법 변경 {#step-4-change-your-user-update-methods}

이미 Braze에 사용자 업데이트를 제공하는 방법이 있다고 가정하면, 이후 Braze로 전송되는 사용자 업데이트에 해당 필드가 포함되도록 새 필드 `native_line_id`를 포함하도록 업데이트해야 합니다.

`native_line_id`가 있는 미식별 고객 프로필이 구독 상태 동기화 프로세스의 일부로 생성되었거나, 새 팔로워가 채널을 팔로우했을 때 Braze에 존재할 수 있습니다.

LINE 사용자가 [사용자 조정](#user-id-reconciliation) 또는 기타 수단을 통해 애플리케이션에서 식별되면, [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) 엔드포인트를 사용하여 Braze에서 잠재적인 미식별 고객 프로필을 타겟팅할 수 있습니다. `native_line_id`가 있는 모든 미식별 고객 프로필에는 식별할 고객 프로필을 타겟팅하는 데 사용할 수 있는 사용자 별칭 `line_id`도 있습니다.

다음은 사용자 별칭 `line_id`로 미식별 고객 프로필을 타겟팅하는 `/users/identify` 페이로드 예시입니다:

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

제공한 `external_id`에 대한 기존 고객 프로필이 없으면, 미식별 고객 프로필에 추가되어 식별된 상태가 됩니다. `external_id`에 대한 고객 프로필이 이미 존재하는 경우, `native_line_id` 및 사용자의 구독 상태를 포함하여 미식별 고객 프로필에만 있는 모든 속성이 알려진 고객 프로필로 복사됩니다.

[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트를 통해 외부 식별자와 `native_line_id`를 전달하여 애플리케이션에서 알려진 LINE 사용자를 업데이트할 수 있습니다. 사용자에 대한 미식별 고객 프로필이 이미 존재하고 동일한 `native_line_id`가 `/users/track`을 통해 다른 고객 프로필에 추가되면, 미식별 고객 프로필의 모든 구독 상태를 상속합니다. 그러나 동일한 `native_line_id`를 가진 중복 고객 프로필이 존재하게 됩니다. 이벤트 업데이트로 인한 이후 구독 업데이트는 모든 프로필을 그에 맞게 업데이트합니다.

{% alert note %}
LINE 구독 상태는 `external_id`가 아닌 `native_line_id`로 추적됩니다. 예를 들어, 사용자 B의 고객 프로필이 사용자 A와 동일한 `native_line_id`로 생성되었지만 동일한 `external_id`가 아닌 경우, 사용자 B는 사용자 A의 LINE 구독 상태를 상속합니다.
{% endalert %}

다음은 외부 사용자 ID로 고객 프로필을 업데이트하여 `native_line_id`를 추가하는 `/users/track` 페이로드 예시입니다:

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## 5단계: 프로필 병합(선택 사항) {#step-5-merge-profiles-optional}

이 섹션의 앞부분에서 설명한 것처럼, 동일한 `native_line_id`를 가진 여러 사용자 프로필이 존재할 가능성이 있습니다. 업데이트 방법으로 인해 중복 사용자 프로필이 생성되는 경우, `/user/merge` 엔드포인트를 사용하여 미식별 사용자 프로필을 식별된 사용자 프로필로 병합할 수 있습니다.

다음은 사용자 별칭 `line_id`로 미식별 사용자 프로필을 대상으로 하는 `/users/merge` 페이로드 예시입니다:

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Braze에서 중복 사용자를 관리하는 방법에 대해 자세히 알아보려면 [중복 사용자]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)를 참조하세요.
{% endalert %}

## 사용자 설정 {#user-setup}

LINE은 사용자 구독 상태의 신뢰할 수 있는 소스입니다. 사용자의 LINE ID(`native_line_id`)를 보유하고 있더라도, 해당 사용자가 메시지를 보내는 LINE 채널을 팔로우하지 않은 경우 LINE은 해당 사용자에게 메시지를 전달하지 않습니다.

이를 관리하기 위해 Braze는 구독 동기화와 LINE 팔로우 및 언팔로우에 대한 이벤트 업데이트를 포함하여 잘 통합된 사용자 기반을 지원하는 도구와 로직을 제공합니다.

### 구독 동기화 및 이벤트 로직 {#subscription-syncing-and-event-logic}

구독 동기화 도구와 팔로우 및 언팔로우 이벤트 업데이트가 LINE 구독 상태를 Braze와 어떻게 동기화하는지에 대한 자세한 내용은 [구독 상태]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#line)를 참조하세요.

## 다른 워크스페이스에서 LINE 채널 재통합하기 {#re-integrate-a-line-channel-in-another-workspace}

다른 Braze 워크스페이스에서 LINE 채널을 사용하려면 다음을 수행합니다:

1. 원래 워크스페이스에서 해당 채널의 구독 그룹을 보관합니다.
2. 대상 워크스페이스에서 [2단계: LINE 채널 통합](#step-2-integrate-line-channel)을 사용하여 채널을 통합합니다.

두 워크스페이스 모두에서 [구독 그룹 관리]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) 권한이 있는지 확인합니다. 두 워크스페이스 모두에 권한이 없으면 채널이 이미 연결되어 있다는 오류와 함께 통합이 실패합니다.

보관이 구독 그룹에 미치는 영향에 대해서는 [LINE 구독 그룹]({{site.baseurl}}/line/subscription_groups#archive-behavior)을 참조하세요.

## 사용 사례 {#use-cases}

설정 단계를 완료한 후 사용자가 업데이트될 수 있는 사용 사례입니다.

### 기존 Braze 고객 프로필이 이미 LINE 채널을 팔로우하고 있는 경우 {#existing-braze-user-profile-already-follows-line-channel}

1. Braze 고객 프로필이 `native_line_id` 속성으로 업데이트됩니다. 기본 구독 상태는 `unsubscribed`입니다.
2. 구독 동기화 도구가 실행되어 사용자가 LINE 채널을 팔로우하고 있음을 확인한 후, 고객 프로필의 구독 상태를 `subscribed`로 업데이트합니다.
3. 구독 상태 변경이 발생하면(예: 사용자가 채널을 차단, 친구 삭제 또는 다시 팔로우하는 경우) Braze가 LINE으로부터 업데이트를 수신하고 그에 따라 `native_line_id`가 포함된 고객 프로필을 업데이트합니다.

### 기존 고객 프로필이 LINE 채널을 차단, 친구 삭제 또는 팔로우 해제한 경우 {#existing-user-profile-has-blocked-unfriended-or-unfollowed-line-channel}

1. Braze 고객 프로필이 `native_line_id` 속성으로 업데이트됩니다. 기본 구독 상태는 `unsubscribed`입니다.
2. 구독 동기화 도구가 사용자가 LINE 채널을 팔로우하고 있지 않음을 확인하고, 사용자의 구독 상태는 `unsubscribed`로 유지됩니다.
3. 사용자가 나중에 채널을 팔로우하면 Braze가 LINE으로부터 업데이트를 수신하고 고객 프로필의 구독 상태를 `subscribed`로 업데이트합니다.

### LINE 팔로우 후 고객 프로필이 생성되는 경우 {#user-profile-creation-occurs-after-line-follow}

1. 채널에 새로운 LINE 팔로워가 생깁니다.
2. Braze가 팔로워의 LINE ID로 설정된 `native_line_id` 속성과 팔로워의 LINE ID로 설정된 `line_id` 사용자 별칭을 가진 익명 사용자 프로필을 생성합니다. 이 프로필의 구독 상태는 `subscribed`입니다.
3. [사용자 조정](#user-id-reconciliation)을 통해 해당 사용자가 LINE ID를 보유하고 있음이 확인됩니다.
  - 익명 사용자 프로필은 [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) 엔드포인트를 사용하여 식별된 프로필로 전환할 수 있습니다. 이후 이 고객 프로필에 대한 업데이트([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트, [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 통해)는 알려진 `external_id`로 사용자를 타겟팅할 수 있습니다.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - `native_line_id`를 설정하여 새 고객 프로필을 생성할 수 있습니다([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트, [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 통해). 이 새 프로필은 기존 익명 사용자 프로필의 구독 상태를 상속합니다. 이 경우 동일한 `native_line_id`를 공유하는 여러 프로필이 생성됩니다. 이러한 프로필은 [5단계](#step-5-merge-profiles-optional)에 설명된 프로세스에 따라 `/users/merge` 엔드포인트를 사용하여 언제든지 병합할 수 있습니다.

### LINE 팔로우 전에 고객 프로필이 생성되는 경우 {#user-profile-creation-occurs-before-line-follow}

1. 새로운 사용자를 확보하고 해당 정보를 Braze에 전송합니다. 새 고객 프로필이 생성됩니다(프로필 1).
2. 사용자가 LINE 계정을 팔로우합니다.
3. Braze가 팔로우 이벤트를 수신하고 익명 사용자 프로필을 생성합니다(프로필 2).
4. [사용자 조정](#user-id-reconciliation)을 통해 해당 사용자가 LINE ID를 보유하고 있음이 확인됩니다.
5. 프로필 1에 `native_line_id` 속성을 설정하여 업데이트합니다. 이 프로필은 프로필 2의 구독 상태를 상속합니다.
  - 이제 동일한 `native_line_id`를 가진 두 개의 고객 프로필이 존재합니다. 이러한 프로필은 [5단계](#step-5-merge-profiles-optional)에 설명된 프로세스에 따라 `/users/merge` 엔드포인트를 사용하여 언제든지 병합할 수 있습니다.

## 사용자 ID 조정 {#user-id-reconciliation}

LINE ID는 사용자가 채널을 팔로우하거나 일회성 "팔로워 동기화" 워크플로를 사용할 때 Braze에 자동으로 수신됩니다. LINE ID는 사용자가 팔로우하는 채널에 고유하므로, 사용자가 자신의 LINE ID를 직접 제공할 가능성은 낮습니다.

LINE ID를 기존 Braze 고객 프로필과 결합하는 방법은 두 가지가 있습니다:

- [LINE 로그인](#line-login)
- [사용자 계정 연결](#user-account-linking)

### LINE 로그인 {#line-login}

이 방법은 소셜 미디어 로그인을 사용하여 조정을 수행합니다. 사용자가 앱에 로그인하면 [LINE 로그인](https://developers.line.biz/en/docs/line-login/overview/)을 사용하여 사용자 계정을 만들거나 로그인할 수 있는 옵션이 제공됩니다.

{% alert note %}
각 사용자에 대해 올바른 LINE ID를 획득하려면, Braze와 통합된 LINE 공식 계정 또는 채널과 동일한 공급자 아래에서 LINE 로그인을 설정하세요.
{% endalert %}

1. LINE 개발자 콘솔로 이동하여 LINE 로그인을 통해 앱에 로그인하는 [사용자의 이메일 주소를 얻기 위한 권한을 요청](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)합니다.

2. LINE에서 제공하는 적절한 단계에 따라 LINE 로그인을 구현합니다:<br><br>
  - [웹 앱 안내](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [네이티브 앱 안내](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>인증 요청을 위한 [범위 설정](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)에 `email`을 포함해야 합니다.

{: start="3"}
3. [ID 토큰 확인 호출](https://developers.line.biz/en/reference/line-login/#verify-id-token)을 사용하여 사용자의 이메일을 획득합니다.

4. 사용자의 LINE ID(`native_line_id`)를 데이터베이스에서 일치하는 이메일이 있는 고객 프로필에 저장하거나, 사용자의 이메일과 LINE ID로 새 고객 프로필을 생성합니다.

5. [`/user/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track), [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 사용하여 새로운 또는 업데이트된 사용자 정보를 Braze에 전송합니다.

#### 워크플로 {#workflows}

##### 기존 팔로워가 LINE 로그인을 사용하는 경우 {#existing-follower-uses-line-login}

**시나리오:** 초기 가입자 동기화 중 또는 통합 후 "팔로우" 이벤트를 통해 익명 사용자가 생성되었습니다.

1. 사용자가 LINE 로그인을 사용하여 앱에 로그인합니다.
2. LINE이 사용자의 이메일을 제공합니다.
3. 업데이트된 사용자(LINE ID를 추가하기 위해 해당 이메일이 있는 기존 고객 프로필)를 Braze에 전송하거나, 익명 사용자를 이메일로 업데이트합니다.

##### 새 팔로워가 LINE 로그인을 사용하는 경우 {#new-follower-uses-line-login}

**시나리오:** Braze에 사용자의 LINE ID가 있는 고객 프로필이 존재하지 않습니다.

1. 사용자가 LINE 로그인을 사용하여 앱에 로그인합니다.
2. LINE이 사용자의 이메일을 제공합니다.
3. 다음 중 하나를 수행합니다:
  - 해당 이메일이 있는 기존 고객 프로필을 업데이트하여 사용자의 LINE ID도 포함시킵니다.
  - 이메일과 LINE ID로 새 고객 프로필을 생성합니다.
4. 사용자가 LINE 공식 계정을 팔로우하면, Braze가 팔로우 이벤트를 수신하고 사용자의 구독 상태를 `subscribed`로 업데이트합니다.

### 사용자 계정 연결 {#user-account-linking}

이 방법을 사용하면 사용자가 LINE 계정을 앱의 사용자 계정에 연결할 수 있습니다. 그런 다음 Braze에서 {% raw %}`{{line_id}}`{% endraw %}와 같은 Liquid를 사용하여 사용자의 LINE ID를 웹사이트 또는 앱으로 다시 전달하는 개인화된 URL을 생성할 수 있으며, 이를 알려진 사용자와 연결할 수 있습니다.

1. 구독 상태 변경을 기반으로 하는 액션 기반 Canvas를 생성하고, 사용자가 LINE 채널을 구독할 때 트리거되도록 설정합니다.<br>![사용자가 LINE 채널을 구독할 때 트리거되는 Canvas.]({% image_buster /assets/img/line/account_link_1.png %})
2. 사용자가 웹사이트 또는 앱에 로그인하도록 유도하는 메시지를 생성하고, 사용자의 LINE ID를 쿼리 파라미터로(Liquid를 통해) 전달합니다. 예시:

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. 쿠폰 코드를 전달하는 후속 메시지를 생성합니다.
4. (선택 사항) LINE 사용자가 식별되었을 때 트리거되는 액션 기반 Campaign 또는 Canvas를 생성하여 사용자에게 쿠폰 코드를 전송합니다. <br>![LINE 사용자가 식별되었을 때 트리거되는 액션 기반 Campaign.]({% image_buster /assets/img/line/account_link_2.png %})

#### 작동 방식 {#how-it-works}

사용자가 로그인한 후, 웹사이트 또는 앱에서 변경이 이루어져 사용자 ID가 URL의 일부로 전달된 LINE ID와 연결하기 위해 Braze로 다시 전송됩니다. 예시 코드는 다음과 같습니다:

```javascript
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### 워크플로

##### 기존 사용자가 LINE 채널을 팔로우하는 경우 {#existing-user-follows-your-line-channel}

**시나리오:** Braze의 기존 사용자가 LINE에서 채널을 팔로우합니다.

1. LINE이 Braze에 팔로우 이벤트를 전송합니다.
2. Braze가 LINE ID, `line_id` 사용자 별칭, 그리고 LINE 구독 그룹 상태가 `subscribed`인 익명 고객 프로필을 생성합니다.
3. 사용자가 웹사이트 및 앱 링크가 포함된 LINE 메시지를 수신하고 로그인합니다. 이제 고객 프로필이 알려진 상태가 됩니다.
4. 생성된 익명 고객 프로필이 식별되고 [/users/identify 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)를 통해 사용자의 알려진 고객 프로필에 병합됩니다. 알려진 고객 프로필에는 이제 LINE ID가 포함되며 구독 상태가 `subscribed`입니다.
5. (선택 사항) 사용자가 쿠폰 코드가 포함된 LINE 메시지를 수신하고, Braze가 해당 전송을 Braze 고객 프로필에 기록합니다.

## Braze에서 LINE 테스트 사용자 만들기 {#creating-line-test-users-in-braze}

[사용자 조정](#user-id-reconciliation)을 설정하기 전에 "Who am I" Canvas 또는 Campaign을 만들어 LINE 채널을 테스트할 수 있습니다.

1. 특정 트리거 단어에 대해 사용자의 Braze 사용자 ID를 반환하는 Canvas를 설정합니다. <br><br>트리거 예시 <br><br>![특정 구독 그룹에 인바운드 LINE을 보낸 사용자에게 Campaign을 전송하는 트리거.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>메시지 예시<br><br>![Braze 사용자 ID를 표시하는 LINE 메시지.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Braze에서 Braze ID를 사용하여 특정 사용자를 검색하고 필요에 따라 수정할 수 있습니다.

{% alert important %}
Canvas에 전역 제어 또는 대조군이 설정되어 발송을 차단하지 않는지 확인하세요.
{% endalert %}