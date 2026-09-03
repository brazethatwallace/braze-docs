{% if include.alert == 'Web push private browsing' %}

{% alert important %}
개인 브라우징 창은 웹 푸시를 지원하지 않습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
Campaign 또는 Canvas에 BCC 주소를 추가하면 Braze가 사용자에게 하나, BCC 주소에 하나의 메시지를 보내기 때문에 해당 Campaign 또는 Canvas 구성요소의 청구 가능한 이메일이 두 배로 늘어납니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
알림 표시 우선순위 설정은 Android O 이상을 실행하는 기기에서 더 이상 사용되지 않습니다. 이러한 기기에서는 [알림 채널 구성](https://developer.android.com/training/notify-user/channels#importance)을 통해 우선순위를 설정하세요.
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
법적으로 요구되는 트랜잭션 이메일은 전달되지 않을 가능성이 높으므로 SMS 게이트웨이로 보내지 마세요.
<br><br>
전화번호와 제공업체의 게이트웨이 도메인(MM3라고 함)을 사용하여 보내는 이메일은 SMS(문자) 메시지로 수신될 수 있지만, 일부 이메일 제공업체는 이 동작을 지원하지 않습니다. 예를 들어, T-Mobile 전화번호(예: "9999999999@tmomail.net")로 이메일을 보내면 T-Mobile 네트워크에서 해당 전화번호를 소유한 사람에게 SMS 메시지가 전송됩니다.
<br><br>
이러한 이메일이 SMS 게이트웨이로 전달되지 않더라도 이메일 요금 청구에 포함된다는 점에 유의하세요. 지원되지 않는 게이트웨이로 이메일을 보내지 않으려면 [지원되지 않는 게이트웨이 도메인 이름 목록](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads)을 검토하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
보안을 강화하려면 사용자 가장을 방지하기 위해 [SDK 인증]({{site.baseurl}}/developer_guide/authentication) 기능을 추가하는 것을 권장합니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
네이버 Android 및 iOS 앱과 같은 특정 브라우저는 Braze 환경설정 센터를 지원하지 않습니다. 일부 사용자가 이러한 브라우저를 사용할 것으로 예상되는 경우 이메일 환경설정을 관리할 수 있는 대체 방법을 제공하는 것이 좋습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
레거시 구매 이벤트는 유지보수 모드로 전환됩니다. 기존 Braze 고객은 레거시 구매 이벤트를 계속 사용할 수 있습니다. 기존 구매 이벤트는 계속 정상적으로 작동하지만, 향후 새로운 기능은 이커머스 추천 이벤트를 기반으로 구축됩니다. Braze는 서비스 종료일이 설정되기 전에 충분한 사전 공지를 제공합니다. 신규 Braze 고객은 레거시 구매 이벤트를 사용할 수 없으므로 [이커머스 추천 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events)를 사용해야 합니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
레거시 구매 이벤트는 지원 중단 상태(유지보수 모드)로 전환됩니다. 구매 이벤트는 계속 정상적으로 작동하지만, [이커머스 추천 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events)를 우선하여 구매 이벤트 위에 순수하게 새로운 기능이 추가되지 않습니다. 이 변경이 적용되면 Segment 필터가 더 이상 구매 동작 아래에 표시되지 않습니다.<br><br> 현재 구매 이벤트를 사용 중인 경우 단계적 중단 계획에 대한 사전 공지를 받게 됩니다. 지금은 공식 지원 중단일까지 구매 이벤트를 계속 사용할 수 있습니다. 자세한 내용은 [추천 이벤트 개요]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events)를 참조하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
S3 버킷에 저장된 내보내기 파일은 다운로드 링크가 만료된 후 자동으로 삭제됩니다(별도로 명시되지 않는 한, 내보내기 이메일이 전송된 시점으로부터 4시간 후).
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
Shopify 통합은 데이터 구성 설정에 있는 Shopify 고객 생성 및 고객 업데이트 웹훅을 지원합니다. Shopify에서 고객 프로필이 생성되거나 업데이트되면 Braze에서도 해당 고객 프로필이 생성되거나 업데이트됩니다. <br><br>이러한 동작은 Braze에서 커스텀 이벤트를 트리거하지 않으며, [Shopify 사용자 데이터를 Braze와 동기화]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#how-the-integration-works)하는 용도로만 사용됩니다. 동기화되는 데이터에는 [커스텀 속성]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#supported-shopify-custom-attributes), [표준 속성]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#supported-shopify-standard-attributes), 그리고 구성에서 활성화된 경우 [구독 그룹 상태]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins)가 포함됩니다.
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Canvas 진입 속성은 Canvas 컨텍스트 변수의 일부입니다. 이는 `canvas_entry_properties`가 `context`로 참조됨을 의미합니다. 각 `context` 변수에는 이름, 데이터 유형, Liquid를 포함할 수 있는 값이 포함됩니다. 현재 `canvas_entry_properties`는 이전 버전과 호환됩니다. 자세한 내용은 [컨텍스트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#how-it-works) 및 [Canvas 컨텍스트 오브젝트]({{site.baseurl}}/api/objects_filters/context_object)를 참조하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
이 파트너는 [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents)가 활성화된 경우에만 **기술 파트너** 페이지에 표시됩니다. 시작하는 데 도움이 필요하면 고객 성공 매니저에게 문의하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**"연중일"과 "시간" 필터 유형 중에서 선택하기**: 날짜가 포함된 컨텍스트 변수를 필터링할 때, 날짜가 매년 반복되는지에 따라 올바른 비교 유형을 선택하세요. 컨텍스트 변수가 생성하는 값에 연도가 포함되지 않는 경우에만 "연중일"을 사용하세요.

- **"연중일" 사용**: 날짜가 매년 반복될 때(예: 생일, 기념일 또는 크리스마스와 같은 휴일). 이 비교 유형은 연도 구성요소를 무시하고 연중일(1-365/366)을 기준으로 계산합니다.
- **"시간" 사용**: 날짜가 반복되지 않는 절대 날짜일 때(예: 계약 종료일, 약속 날짜 또는 구독 갱신 날짜). 이 비교 유형은 연도를 포함한 전체 타임스탬프를 기준으로 계산합니다.

절대 날짜에 "연중일"을 사용하면 연도 구성요소를 무시하므로 잘못되거나 예상치 못한 결과가 발생할 수 있습니다. 예를 들어, 4월의 미래 계약 종료일이 63일 이내인지 비교할 때, "연중일"을 사용하면 날짜 번호(119 vs 359)만 비교하기 때문에 실제로 4월까지는 188일이 남아 있음에도 잘못 일치할 수 있습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
세분화된 권한은 얼리 액세스 중입니다. 귀사의 마이그레이션이 계획되면, Braze 관리자에게 [세분화된 권한 마이그레이션]({{site.baseurl}}/granular_permissions_migration)에 대한 이메일과 대시보드 내 배너가 전송됩니다.
{% endalert %}

{% endif %}

{% if include.alert == 'WhatsApp audio and documents' %}

{% alert note %}
[Braze 미디어 라이브러리]({{site.baseurl}}/media_library)는 이미지와 동영상만 지원합니다. 오디오 파일과 문서는 호스팅된 URL을 통해 참조해야 합니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Meta MP4 video issue' %}

{% alert important %}
Meta에는 특정 인코딩 또는 컨테이너 설정으로 인해 일부 MP4 동영상이 Android 기기에서 재생되지 않을 수 있는 알려진 문제가 있습니다. 영구적인 수정이 제공될 때까지, MP4 파일을 다시 포맷하면 대부분의 발송자에게 문제가 해결됩니다. 올바른 전달 가능성을 확인하려면 모든 동영상을 Android 기기에서 테스트하세요. <br><br>[CloudConvert](https://cloudconvert.com/mp4-converter)와 같은 웹 도구를 사용하여 MP4 파일을 다시 포맷할 수 있습니다. MP4 파일을 도구에 업로드하고 다시 MP4로 변환한 다음 변환된 파일을 다운로드하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify cart token alias' %}

{% alert important %}
이 통합에서 사용자 별칭은 Braze가 웹훅을 올바른 고객 프로필에 매칭할 수 있도록 다음 형식을 사용해야 합니다:<br><br>
- `alias_label`: `shopify_cart_${cartToken}`
- `alias_name`: `shopify_cart_token`
{% endalert %}

{% endif %}

{% if include.alert == 'network dependency' %}

{% alert important %}
Content Cards, 인앱 메시지, 배너 및 기능 플래그는 Braze 서버와 동기화하기 위해 기기 연결에 의존합니다. 네트워크 상태가 다양할 수 있으므로 콘텐츠나 업데이트가 즉시 동기화, 표시 또는 삭제되지 않을 수 있습니다(예: 사용자가 오프라인인 경우). 중요하고 시간에 민감한 업데이트에는 이러한 채널을 사용하지 않는 것을 권장합니다.
{% endalert %}

{% endif %}

{% if include.alert == 'dynamic image URL' %}

{% alert important %}
[연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) 또는 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)로 이미지를 가져오는 경우, 이미지 URL이 `https://`로 시작하는지 확인하세요. `http://`를 사용하면 앱이 충돌할 수 있습니다.
{% endalert %}

{% endif %}