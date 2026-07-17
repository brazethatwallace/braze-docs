---
nav_title: 사용자 관리
article_title: LINE 사용자 관리
page_order: 0
description: "이 문서에서는 LINE 사용자 ID와 이를 설정하는 방법에 대해 설명합니다."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# LINE 사용자 관리 {#line-user-management}

> LINE 사용자 ID는 `native_line_id`라는 고객 프로필 속성에 저장되며, LINE 채널에서 사용자에게 메시지를 보내는 데 사용됩니다. 이 문서에서는 `native_line_id` 속성을 설정하고 찾는 방법을 다룹니다.

고객 사용자 데이터는 [Braze 고객 프로필]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)에 표현됩니다. 고객 프로필에는 이름, 이메일 주소 등 회사 사용자에 대한 정보와 속성이 저장됩니다.

Braze를 통해 LINE 메시지를 보낼 때, Braze는 `native_line_id` 속성을 사용하여 메시지를 보낼 사용자를 식별합니다. LINE이 Braze에 웹훅 이벤트를 보낼 때(예: 사용자가 채널을 팔로우하거나 메시지에 답장하는 경우), `native_line_id`를 사용하여 해당하는 고객 프로필을 조회합니다.

{% alert note %}
LINE 사용자 ID는 LINE 공급자별로 고유합니다. 특정 사용자는 팔로우하는 각 공급자마다 서로 다른 LINE 사용자 ID를 갖게 됩니다. 사용자는 팔로우하는 브랜드마다 ID가 변경되기 때문에 자신의 LINE ID를 알 가능성이 낮습니다(이메일이나 전화번호와는 다릅니다).
{% endalert %}

## `native_line_id` 속성 설정하기 {#setting-the-native_line_id-attribute}

고객 프로필에 `native_line_id`가 설정되는 여러 시나리오가 있으며, 아래 목록에 설명되어 있습니다.

| 시나리오 | `native_line_id`가 있는 고객 프로필 존재 여부 | 결과 |
| --- | --- | --- |
| 사용자가 LINE 채널을 팔로우함 | 아니요 | 익명 사용자 프로필이 생성됩니다(병합이 필요합니다):<br> - `native_line_id`가 사용자의 LINE ID로 설정됩니다 <br>- `line_id` 사용자 별칭이 사용자의 LINE ID로 설정됩니다<br>- 사용자가 채널의 Braze 구독 그룹에 가입됩니다 |
| 사용자가 LINE 채널을 팔로우함 | 예 | `native_line_id`가 있는 모든 고객 프로필:<br>- 채널의 Braze 구독 그룹에 가입됩니다 |
| 회사가 `native_line_id` 열이 포함된 사용자 CSV 업로드를 사용함 | 아니요 | 지정된 `external_id` 또는 사용자 별칭에 대한 고객 프로필이 없는 경우:<br>- `native_line_id`가 지정된 값으로 설정됩니다<br> - CSV에 지정된 다른 모든 속성이 고객 프로필에 설정됩니다 |
| 회사가 `native_line_id` 열이 포함된 사용자 CSV 업로드를 사용함 | 예 | 지정된 `external_id` 또는 사용자 별칭에 대한 고객 프로필이 있는 경우:<br>- `native_line_id`가 지정된 값으로 설정됩니다<br>- CSV에 지정된 다른 모든 속성이 고객 프로필에 설정됩니다<br>- 여러 프로필이 동일한 `native_line_id`를 가질 수 있습니다 |
| 회사가 `/users/track` 엔드포인트를 사용하고 `native_line_id` 속성을 지정함 | 아니요 | 지정된 사용자에 대한 고객 프로필이 없는 경우([`external_id`, `user_alias`, `braze_id` 또는 `email`로 지정]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)):<br>- `native_line_id`가 지정된 값으로 설정됩니다<br>- 요청에 지정된 다른 모든 속성이 고객 프로필에 설정됩니다 |
| 회사가 `/users/track` 엔드포인트를 사용하고 `native_line_id` 속성을 지정함 | 예 | 지정된 사용자에 대한 고객 프로필이 있는 경우([`external_id`, `user_alias`, `braze_id` 또는 `email`로 지정]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)):<br>- `native_line_id`가 지정된 값으로 설정됩니다<br>- 요청에 지정된 다른 모든 속성이 고객 프로필에 설정됩니다<br>- 여러 프로필이 동일한 `native_line_id`를 가질 수 있습니다 |
| 회사가 Braze에 구독 상태 동기화 도구 실행을 요청함 | 아니요 | LINE에서 반환된 사용자 LINE ID에 해당하는 고객 프로필이 Braze에 없는 경우, 익명 사용자 프로필이 생성됩니다:<br>- `native_line_id`가 사용자의 LINE ID로 설정됩니다<br>- `line_id` 사용자 별칭이 사용자의 LINE ID로 설정됩니다<br>- 사용자가 채널의 Braze 구독 그룹에 가입됩니다<br><br>동일한 LINE ID를 가진 사용자가 나중에 생성되면 중복 사용자가 발생하지만, 두 프로필 모두 올바른 LINE 구독 상태를 갖게 됩니다. 이러한 경우 사용자 병합을 통해 사용자 기반을 정리할 수 있습니다. |
| 회사가 Braze에 구독 상태 동기화 도구 실행을 요청함 | 예 | LINE에서 반환된 사용자 LINE ID에 해당하는 고객 프로필이 Braze에 있는 경우:<br>- 사용자가 채널의 Braze 구독 그룹에 가입됩니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="native_line_id 속성 설정하기" }

## `native_line_id` 찾기 {#finding-the-native_line_id}

Braze 대시보드에서 고객 프로필을 볼 때, **참여** 탭 > **연락처 설정** 섹션 > **LINE** 섹션으로 이동하여 `native_line_id` 속성이 설정되어 있는지 확인할 수 있습니다.

`native_line_id`가 설정된 경우 **LINE User ID** 아래에 표시됩니다. 설정되지 않은 경우에는 표시되지 않습니다.

![참여 탭의 LINE 연락처 설정.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}