{% if include.alert == 'User profile external_id' %}

{% alert warning %}
사용자를 고유하게 식별할 수 있기 전에는 고객 프로필에 `external_id`를 할당하지 마세요. 사용자를 식별한 후에는 익명으로 되돌릴 수 없습니다.
<br><br>
`external_id`는 [`/users/external_ids/rename` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename)를 사용하여 업데이트할 수 있습니다. 그러나 사용자의 세션 중에 다른 `external_id`를 설정하려고 시도하면 새로운 `external_id`가 연결된 새 고객 프로필이 생성됩니다. 두 프로필 간에 데이터는 전달되지 않습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
동일한 Currents 커넥터를 두 개 이상 만들려는 경우(예: 메시지 인게이지먼트 이벤트 커넥터 두 개), 반드시 서로 다른 워크스페이스에 생성해야 합니다. Braze Segment Currents 통합은 단일 워크스페이스 내에서 서로 다른 앱의 이벤트를 분리할 수 없으므로, 이를 지키지 않으면 불필요한 데이터 중복 제거 및 데이터 손실이 발생할 수 있습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
오디언스 필터와 동일한 트리거(예: 속성 변경 또는 커스텀 이벤트 수행)로 액션 기반 Campaign 또는 Canvas를 구성하지 마세요. 사용자가 트리거 이벤트를 수행하는 시점에 오디언스에 포함되지 않아 [경합 조건]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)이 발생할 수 있으며, 이 경우 Campaign을 받지 못하거나 Canvas에 진입하지 못하게 됩니다.
{% endalert %}

{% endif %}