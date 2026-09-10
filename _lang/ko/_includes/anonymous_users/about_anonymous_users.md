[Braze SDK를 통합한]({{site.baseurl}}/developer_guide/sdk_integration) 후 앱을 처음 실행하는 사용자는 `changeUser` 메서드를 호출하여 `external_id`를 할당할 때까지 "익명" 사용자로 간주됩니다. 일단 할당되면 다시 익명으로 설정할 수 없습니다. 그러나 앱을 삭제했다가 다시 설치하면 `changeUser`를 호출할 때까지 다시 익명으로 전환됩니다.

이전에 식별된 사용자가 새 기기에서 세션을 시작하는 경우, 해당 기기에서 `external_id`를 사용하여 `changeUser`를 호출하면 Braze는 식별된 프로필에 아직 존재하지 않는 특정 필드를 익명 프로필에서 병합합니다. 모든 데이터가 전달되는 것은 아니며, 식별된 프로필에 아직 채워지지 않은 필드만 병합됩니다. 전달되는 필드의 전체 목록은 [병합 동작]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)을 참조하세요.

{% if include.section == "user_guide" %}
{% alert tip %}
전체 안내는 [사용자 ID 설정하기]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)를 참조하세요.
{% endalert %}
{% endif %}