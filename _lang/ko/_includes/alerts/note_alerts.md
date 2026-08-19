{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
Content Cards에는 최대 게재빈도 설정이 적용되지 않습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
"12-1-2021" 또는 "12/1/2021"과 같은 날짜 문자열은 날짜/시간 오브젝트로 변환되어 [시간 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#time)으로 처리됩니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
모든 고객 프로필 데이터(커스텀 이벤트, 커스텀 속성, 커스텀 데이터)는 해당 프로필이 활성 상태인 동안 저장됩니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze는 사용자가 앱을 처음 사용할 때까지 프로필을 생성하지 않으므로, 아직 앱을 열지 않은 사용자를 타겟팅할 수 없습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify attributes REST API' %}

{% alert note %}
모든 속성의 소스는 Braze REST API입니다.
{% endalert %}

{% endif %}

{% if include.alert == 'subscription group limit' %}

{% alert note %}
워크스페이스당 최대 450개의 구독 그룹을 추가할 수 있습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'GIF platform support' %}

{% alert note %}
Android 푸시 알림에서는 GIF가 지원되지 않습니다. 이는 Braze의 제한이 아니라 Android 플랫폼의 제한입니다.
<br><br>
- Android에서 인앱 메시지 및 Content Cards의 경우, [Glide](https://bumptech.github.io/glide/) 또는 [Fresco](https://frescolib.org/)와 같은 서드파티 이미지 라이브러리를 통합하여 GIF를 지원할 수 있습니다.
<br>
- iOS에서는 푸시 알림이 GIF를 지원합니다. 인앱 메시지 및 Content Cards의 경우 커스텀 GIF 이미지 프로바이더가 필요합니다.
{% endalert %}

{% endif %}