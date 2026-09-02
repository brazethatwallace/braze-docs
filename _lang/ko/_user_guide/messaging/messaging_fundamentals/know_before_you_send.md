---
nav_title: 발송 전 알아두기
article_title: 발송 전 알아두기
description: "사전 출시 가이드를 확인한 후, Content Cards, 이메일, 인앱 메시지, 푸시, SMS에 대한 최종 체크리스트 또는 '주의사항'을 참조하세요."
alias: /know_before_send/
page_order: 7
tool:
    - Campaigns
    - Canvas
---

# 발송 전 알아두기: 채널 {#know-before-you-send-channels}

> Campaign과 Canvas를 자신 있게 시작하세요! Braze에서 자주 사용하는 메시징 [채널]({{site.baseurl}}/user_guide/channels)에 대한 최종 체크리스트 또는 "주의사항"을 참조하세요.

{% alert note %}
발송 전 참조할 수 있는 광범위한 리소스 목록을 제공하고 있지만, 각 채널에는 제품이 발전함에 따라 계속 늘어나는 고유한 특성이 있습니다. 아래 나열된 체크리스트는 유용한 제안이며, Campaign과 대량 발송을 실행하기 전에 철저히 테스트하는 것을 권장합니다.
{% endalert %}

## 일반사항 {#general}

### 확인해야 할 사항 {#things-to-check}
- [**API 사용량 제한**](https://braze.com/resources/articles/whats-rate-limiting): 워크스페이스의 Braze API [사용량 제한]({{site.baseurl}}/api/api_limits)을 검토하여 오류가 발생하지 않도록 하세요. 사용량 제한을 늘리고 싶은 경우(이미 요청을 일괄 처리하고 있는 경우), 고객 성공 매니저에게 문의하세요. 이 과정에는 리드 타임이 필요하므로 그에 맞게 계획을 세우세요.
- [**필요한 최대 게재빈도 설정 재정의**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): 트랜잭션 메시지와 같이, 사용자가 이미 최대 게재빈도에 도달한 경우에도 항상 메시지를 전달하고 싶은 Campaigns가 있을 수 있습니다(예: 배송 알림). 특정 Campaign이 최대 게재빈도 설정 규칙을 재정의하도록 하려면, Braze 대시보드에서 해당 Campaign의 전달을 스케줄할 때 최대 게재빈도 설정을 끄기로 전환하여 설정할 수 있습니다.

### 알아두어야 할 사항 {#things-to-know}
- [**글로벌 컨트롤 그룹**]({{site.baseurl}}/user_guide/audience/global_control_group): 글로벌 컨트롤 그룹을 사용하는 경우, 일정 비율의 사용자가 어떤 Campaigns나 Canvases도 수신하지 않게 됩니다. ([제외 설정]({{site.baseurl}}/user_guide/audience/global_control_group#step-3-assign-exclusion-settings)을 통해 예외를 만들 수 있습니다.) 이러한 사용자 목록을 확인하려면 CSV 또는 [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)를 통해 내보내세요.
- [**Canvas 사용량 제한**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Canvas에서 사용량 제한은 개별 단계가 아닌 전체 Canvas에 적용됩니다. 예를 들어, 여러 단계가 있는 Canvas에 분당 10,000건의 메시지 사용량 제한을 설정하면, 첫 번째 단계에서 이미 제한에 도달하기 때문에 여전히 10,000건의 메시지로 제한됩니다.
- **최대 게재빈도 설정**:
  - 최대 게재빈도 설정 규칙은 푸시, 이메일, SMS, 웹훅에 적용되지만, 인앱 메시지 및 Content Cards에는 적용되지 않습니다.
  - 글로벌 최대 게재빈도 설정은 사용자의 시간대를 기준으로 스케줄되며, 24시간 단위가 아닌 달력 일 기준으로 계산됩니다. 예를 들어, 하루에 Campaign을 1건만 발송하는 최대 게재빈도 설정 규칙을 설정한 경우, 사용자가 현지 시간대로 오후 11시에 메시지를 받을 수 있으며, 1시간 후에 또 다른 메시지를 수신할 자격이 생깁니다.

{% alert tip %}
Canvas 및 Campaign 문제 해결에 대한 추가 지원이 필요한 경우, 문제 발생 후 30일 이내에 Braze 지원팀에 문의해 주세요. 최근 30일간의 진단 로그만 보유하고 있습니다.
{% endalert %}

## 배너 {#banners}

### 확인할 사항
- **배너 크기:** 고정 크기 요소를 사용하여 배너를 만들고 에디터에서 테스트하세요.
- **우선순위:** 여러 배너를 동시에 실행하는 경우, 각 배너가 표시되는 우선순위를 수동으로 설정할 수 있습니다.

### 알아두어야 할 사항
- **Liquid 개인화:** Liquid 개인화는 새로고침 요청이 있을 때마다 갱신됩니다.
- **배치 및 배너 비율:** 각 배너 배치는 워크스페이스 내에서 최대 25개의 메시지에 사용할 수 있습니다.
- **클릭 및 노출 횟수:** 배너의 클릭 및 노출 횟수는 SDK를 통해 자동으로 추적됩니다.
- **제한 사항:** 현재 Canvas 통합, API 트리거 및 액션 기반 Campaigns, 연결된 콘텐츠, 프로모션 코드, [`:rerender` 태그]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid)를 사용하는 `catalog_items` 기능은 지원되지 않습니다.
- **테스트:** 테스트 배너를 표시하려면 사용 중인 기기에서 포그라운드 푸시 알림을 수신할 수 있어야 합니다.
- **커스텀 HTML:** 커스텀 HTML을 사용하여 링크, 버튼 등의 클릭 액션을 정의할 때는 [JavaScript 브리지]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge)를 활용하여 클릭을 기록하세요. 드래그 앤 드롭 에디터에서 미리 제작된 컴포넌트를 사용하는 경우에만 클릭 액션이 자동으로 기록됩니다.
- **배치 요청:** 단일 새로고침 요청에서 최대 10개의 배치를 SDK에 반환할 수 있습니다. 각 배치에는 사용자가 수신 자격이 있는 가장 높은 우선순위의 배너가 포함됩니다.

## Content Cards

### 확인할 사항
- **Content Cards 크기**: Content Cards 메시지 필드는 압축 전 크기 기준 2&nbsp;KB로 제한되며, 제목, 메시지, 이미지 URL, 링크 텍스트, 링크 URL, 키-값 페어 필드의 바이트 크기 길이를 합산하여 계산됩니다. 이 크기를 초과하는 메시지는 발송되지 않습니다. 이미지 자체의 크기가 아닌 이미지 URL의 길이가 포함된다는 점에 유의하세요.
- **발송 후 문구 업데이트**: 카드가 발송된 후에는 동일한 카드의 문구를 업데이트할 수 없습니다. 이 시나리오에 대한 접근 방법은 [발송된 카드 업데이트]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards)를 참조하세요.

### 알아두어야 할 사항
- **활성 Content Cards Campaign 제한**: 최대 500개의 활성 Content Cards Campaign을 보유할 수 있습니다. 이 수에는 [카드 생성]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card) 옵션 중 하나로 발송된 Content Cards가 포함됩니다.
- [**보고 용어**]({{site.baseurl}}/user_guide/channels/content_cards/reporting): 총 노출 횟수, 고유 노출 횟수, 고유 수신자 등의 용어를 검토하세요. 정의가 때때로 혼동을 일으킬 수 있습니다.
- **Content Cards 새로고침**: 기본적으로 Braze는 세션 시작 시 동기화할 때, 피드를 아래로 스와이프할 때(모바일), 마지막 새로고침이 1분 이상 경과한 경우 카드 뷰가 열릴 때 Content Cards 요청을 새로고침합니다.
- **Content Cards 캐싱**: Content Cards 캐싱 옵션은 [Android/FireOS]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style) 및 [웹](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards) 문서에서 확인할 수 있습니다.
- **최대 게재빈도 설정**: 최대 게재빈도 설정은 Content Cards에 적용되지 않습니다.
- **노출**: 노출은 일반적으로 카드가 표시될 때 기록됩니다. 예를 들어, Content Cards로 가득 찬 받은편지함이 있는 경우, 사용자가 특정 Content Cards까지 스크롤할 때까지 노출이 기록되지 않습니다. 웹, Android, iOS 플랫폼 간에 약간의 차이가 있습니다.
- **SDK 세션 및 카드 생성**: Segment 기준을 충족하더라도 SDK 세션이 없는 사용자에게는 Content Cards가 생성되지 않습니다. 그러나 사용자가 이미 Android 세션을 보유하고 있는 경우, iOS 전용 클릭 동작이 있는 Content Cards가 여전히 생성되며, 해당 사용자는 iOS에서 세션을 시작하면 해당 Content Cards를 볼 수 있습니다. 카드가 생성되는 시점에 대한 자세한 내용은 [카드 생성]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card)을 참조하세요.

## 이메일 {#email}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### 확인할 사항
- **고객 동의**: 초기 이메일을 발송하기 전에 먼저 고객으로부터 허가를 받는 것이 중요합니다. 자세한 내용은 [동의 및 주소 수집]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection)과 [Braze 이용 약관](https://www.braze.com/company/legal/aup)을 참조하세요.
- **예상 볼륨**: 단일 IP의 경우 하루 200만 건의 이메일이 일반적으로 권장되며, 해당 볼륨이 [적절하게 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)된 경우에 한합니다.
  - 이보다 지속적으로 높은 볼륨을 발송할 계획이라면, 공급자가 이메일 수신을 제한하여 소프트 바운스가 다량 발생하고 전달 가능성이 낮아지며 IP 평판이 떨어지는 것을 방지하기 위해 IP 풀로 묶인 여러 IP 주소를 사용하는 것을 고려하세요.
  - 짧은 시간 내에 발송하려는 경우, 다양한 공급자가 메일을 수락하는 속도를 확인하여 발송에 적합한 IP 수를 판단하는 것이 좋습니다.

### 알아두기
- **발송 볼륨 요인**: IP의 발송 가능 볼륨을 결정하는 요인에는 다음이 포함됩니다:
  - 메일박스: 대형 이메일 공급자는 단일 IP에서 하루 수백만 건을 처리할 수 있지만, 소규모 지역 메일박스 공급자나 인프라가 작은 공급자는 그 정도의 양을 처리하지 못할 수 있습니다.
  - 발송자 평판: 발신자가 해당 볼륨까지 점진적으로 늘렸고 발송 대상인 각 메일박스 또는 도메인에서 발송자 평판이 충분히 높다면, 단일 IP에서 더 많은 양을 하루에 발송할 수 있습니다.
- **모범 사례**: Braze [이메일 모범 사례]({{site.baseurl}}/user_guide/channels/email/best_practices)를 검토하고, 전달 가능성 서비스에 대해 자세히 알고 싶으시면 Braze 계정 팀에 문의하세요.

## 인앱 메시지 {#in-app-messages}

### 알아두어야 할 사항
- **인앱 메시지 트리거링**: 세션 시작 시, SDK는 적격한 모든 인앱 메시지를 트리거와 함께 기기로 전송하도록 요청합니다. 이를 통해 사용자가 세션 중에 해당 이벤트를 수행하면 인앱 메시지를 빠르고 안정적으로 받을 수 있습니다.
- **발송 대 노출 횟수**: 인앱 메시지의 경우, "발송"의 개념이 다른 사용 가능한 채널과 다릅니다. 인앱 메시지를 보려면 사용자가 세션을 시작하고, 적격한 오디언스에 속하며, 트리거를 수행해야 합니다. 이 때문에 보다 명확한 "노출 횟수"를 추적합니다.
- **트리거링**: 기본적으로 인앱 메시지는 SDK가 기록한 이벤트에 의해 트리거됩니다. 서버에서 전송된 이벤트로 인앱 메시지를 트리거하려면 [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=swift) 및 [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android) 가이드를 통해서도 이를 수행할 수 있습니다.
- [Canvas 인앱 메시지]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#advancement-behavior): 이 메시지는 Canvas 컴포넌트에서 예약된 메시지가 사용자에게 전송된 후, 사용자가 앱을 처음 열 때(세션 시작에 의해 트리거됨) 표시됩니다.
- **연결된 콘텐츠 호출**: 연결된 콘텐츠를 사용하면 메시지에 동적 콘텐츠를 전송할 수 있습니다. 인앱 메시지와 같은 채널을 통해 메시지를 전송할 때, 사용자 기기에 더 많은 동시 연결이 발생할 수 있습니다(메시지가 일괄이 아닌 하나씩 전송됨). 이를 관리하기 위해 메시지에 [사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)을 설정하는 것을 권장합니다.

## 푸시 {#push}

### 확인해야 할 사항
- [**옵트인/구독 및 푸시 활성화**]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states): 사용자가 Braze에서 푸시 메시지를 수신하려면 구독 상태가 옵트인(iOS) 또는 구독(Android)이어야 하며, `Push Enabled = True`여야 합니다. Android 13에서는 푸시 알림을 전송하는 앱을 사용자가 관리하는 방식에 주요 변경 사항이 도입되었습니다. Braze [Android 13 SDK 업그레이드 가이드]({{site.baseurl}}/developer_guide/platforms/android/android_13)는 새로운 Android 13 베타 버전이 출시됨에 따라 계속 업데이트됩니다.

### 알아두면 좋은 사항
- **웹 푸시**: Braze [웹 SDK 설정]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web)을 완료했다면 웹 푸시를 활용하여 사용자를 참여시키는 것을 고려해 보세요. 웹 푸시는 휴대폰의 앱 푸시 알림과 동일한 방식으로 작동합니다. 웹 푸시 작성에 대한 자세한 내용은 [푸시 알림 만들기]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)를 확인하세요.
- **단일 앱 타겟팅**: 단일 앱과 해당 사용자를 타겟팅하기 위한 [세분화 차이점]({{site.baseurl}}/user_guide/get_started/workspaces)을 검토하세요.

## SMS

### 확인할 사항
- **할당량 및 처리량**: 현재 계정에 연결된 SMS 할당량(짧은 코드, 긴 코드 등)과 [제공되는 처리량]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)을 파악하여 원하는 시간 내에 발송할 수 있는 충분한 처리량이 있는지 확인하세요.
- **SMS 문구에서 세그먼트 추정**: [SMS 세그먼트 계산기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)에서 SMS 문구를 테스트하세요. SMS 세그먼트 수는 처리량 능력과 함께 고려해야 합니다. (오디언스 × SMS 세그먼트 = 필요한 처리량). SMS FAQ에서 [초과 요금 방지]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs)를 참조하세요.
- **SMS 법률 및 규정**: [SMS 법률, 규정 및 남용 방지]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)를 검토하여 모든 관련 법률을 준수하면서 SMS 서비스를 사용하고 있는지 확인하세요. 발송 전에 법률 자문을 구하는 것을 권장합니다.

### 알아두어야 할 사항
- **SMS 메시지 기본 설정**: SMS 메시지는 일반적으로 발신자 풀의 짧은 코드에서 발송되도록 기본 설정됩니다.
- **영숫자 발신자 ID**: 영숫자 발신자 ID를 사용하면 양방향 메시징이 더 이상 작동하지 않습니다. 이제 단방향 전용입니다.
- **미국 내 업데이트된 처리량**: 미국 [A2P 10DLC 등록](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US)으로 인해 미국 내 처리량이 변경되었습니다. 트래픽 혼잡 및 통신사 문제 등 실제 전달률에 영향을 미칠 수 있는 여러 요인으로 인해 발송 속도 SLA를 계약상 보장하지 않는다는 점에 유의하세요.
- **구독 그룹**: Braze를 통해 SMS Campaign을 시작하려면 구독 그룹을 선택해야 합니다. 또한 국제 [통신 규정 및 가이드라인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)을 준수하기 위해, Braze는 [선택한 구독 그룹에 가입]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#check-a-users-group)하지 않은 사용자에게는 절대 SMS를 발송하지 않습니다.

## WhatsApp

### 알아두어야 할 사항

- [**모범 사례**]({{site.baseurl}}/user_guide/channels/whatsapp/best_practices): 권장하는 WhatsApp 모범 사례를 검토하세요.