---
nav_title: 통합
article_title: 온보딩 통합 개요
page_order: 8
page_type: reference
description: "이 참조 문서에서는 엔지니어 또는 개발자에게 필요한 통합 단계에 대해 간략하게 설명합니다."
---

# 통합 {#integration}

> Braze와의 통합은 가치 있는 과정입니다. 하지만 현명한 선택을 내리셨습니다. **여기**에 오셨으니까요. 이미 그 가치를 알고 계실 겁니다. 하지만 아마도 여러분과 개발자가 기술적 전문성, 전략적 계획, 그리고 둘 사이의 조율에 도움이 되는 일관된 커뮤니케이션이 필요한 여정을 함께 시작하려 한다는 사실은 모르실 수 있습니다.

{% alert note %}
이 문서의 내용은 이메일에는 적용되지 않습니다. 이메일에 대해서는 [이메일 설정]({{site.baseurl}}/user_guide/channels/email/email_setup) 섹션을 확인하세요.
{% endalert %}

## 통합 프로세스의 기술적 측면 {#the-technical-side-of-the-integration-process}

"우리 개발자들은 마법사예요! 뭐든 할 수 있으니까, 보통 그냥 맡겨두죠!"라고 생각하실 수도 있습니다. 아마 실제로 그렇겠죠! 하지만 개발자들이 뒤에서 무엇을 하고 있는지 알아둘 이유가 충분히 있습니다. 사실, 언제 정보를 제공해야 하는지, 그리고 개발자가 "API 키와 API 엔드포인트를 보내주시겠어요?"라고 할 때 무엇을 찾아야 하는지 알고 있다면 전체 프로세스에 큰 도움이 됩니다.

그렇다면 개발자들이 Braze를 여러분의 앱이나 사이트에 통합할 때 실제로 무엇을 하고 있을까요? 좋은 질문입니다!

### 1단계: Braze SDK 구현 {#step-1-they-implement-the-braze-sdk}

Braze SDK(소프트웨어 개발 키트)는 앱이나 사이트에서 정보를 주고받는 방법입니다. 개발자는 본질적으로 양쪽 앱을 서로 연결하는 작업을 하게 됩니다. 이를 위해 몇 가지 핵심 정보가 필요합니다:

* [API 키]({{site.baseurl}}/api/basics)
* [SDK 엔드포인트]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)
  * Braze는 더 이상 커스텀 엔드포인트를 제공하지 않으므로, 사전 정의된 SDK 엔드포인트를 사용하세요. 기존에 커스텀 엔드포인트를 받은 경우, [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift), [웹]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#initializing-the-sdk) 통합에 필요한 설정 단계를 확인할 수 있습니다.

이 정보를 개발자에게 직접 전달하거나, 계정을 만들어 Braze에 접근할 수 있도록 할 수 있습니다.

{% alert warning %}
본인과 개발자가 Braze에서 회사의 자격 증명을 무의식적으로 또는 의도치 않게 변경하지 않도록 주의하세요. 이로 인해 구현 과정에서 문제가 발생하거나, 한 명 이상이 계정에서 잠길 수 있습니다.
{% endalert %}

### 2단계: 원하는 메시징 채널 구현 {#step-2-they-implement-your-desired-messaging-channels}

Braze에는 사용자에게 연락할 수 있는 다양한 옵션이 있으며, 각 옵션은 원하는 방식으로 작동하기 위해 자체 설정이나 조정이 필요합니다. 이 부분에서 개발자와의 커뮤니케이션이 매우 중요합니다.

어떤 채널을 사용하고 싶은지 개발자에게 미리 알려주어 구현이 효율적으로 올바른 순서로 이루어지도록 하세요.

| 채널 | 세부 사항 |
|---|---|
| 인앱 메시지 | SDK 구현 외에도 채널별 설정 단계가 필요합니다. |
| 푸시 | 메시징 자격 증명 및 푸시 토큰을 적절히 처리하기 위해 SDK 구현이 필요합니다. |
| 이메일 | 이메일은 완전히 다른 프로세스입니다. 통합에 대한 자세한 내용은 [이메일 설정]({{site.baseurl}}/user_guide/channels/email/email_setup) 섹션을 참고하세요. |
| Content Cards | [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)를 시작하려면 Braze 고객 성공 매니저에게 문의하세요. |
| SMS 및 MMS | 통합에 대한 자세한 내용은 [SMS 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending) 섹션을 참고하세요. |
| 웹훅 | SDK 구현 외에도 채널별 설정 단계가 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: 원하는 메시징 채널 구현" }

{% alert tip %}
Braze를 사용하여 각 채널에서 접근성 있는 메시징 캠페인을 만들 수 있습니다. 개발자와 협력하여 구현 시 접근성 표준을 충족하도록 하세요.
{% endalert %}

### 3단계: 데이터 설정 {#step-3-they-set-up-your-data}

Braze는 단순한 도구가 아닙니다. 이메일만 보내거나 푸시만 보내는 것이 아닙니다. 모든 사용자와 고객에게 고유한 개인화된 고객 여정을 만드는 것입니다. 고객 여정은 앱이나 사이트 내에서의 행동을 기반으로 하며, 그 행동을 여러분이 직접 정의할 수 있습니다! 개발자의 다음 과제는 앱이나 사이트에서 취해지는 행동이 Braze에서 수집될 수 있도록 하는 것입니다.

그렇다면 이 정보를 개발자에게 전달하기 위해 무엇을 해야 할까요?

1. 마케팅 팀과 협력하여 추적해야 할 캠페인, 목표, 속성, 이벤트를 정의하세요. 사용 사례를 정의하고 팀과 공유하세요.
2. 커스텀 데이터 요구 사항([커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events) 등)을 정의하세요.
3. 거기에서 해당 데이터가 어떻게 추적되어야 하는지(SDK를 통해 트리거 등) 논의하세요.
4. 필요한 [워크스페이스]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces) 수를 결정하세요. 개발자는 이러한 워크스페이스를 [테스트하고 구성]({{site.baseurl}}/user_guide/get_started/workspaces)하는 방법을 알아야 합니다.

이 모든 정보를 파악한 후 개발자에게 공유하세요. 개발자는 해당 정보를 바탕으로 [커스텀 데이터]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data)를 구현합니다. [일부 사용자를 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)해야 할 수도 있습니다. 또한 [이벤트 네이밍 규칙]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions)에 대해서도 알아두는 것이 좋습니다.

### 4단계: 원하는 사항에 맞게 커스터마이즈 {#step-4-they-customize-based-on-what-you-want}

API 트리거 실행이나 연결된 콘텐츠 같은 기능을 원한다면, Braze 담당자 및 개발자와 함께 논의하여 앱과 Braze 외부에 있는 데이터를 메시지에 가져올 수 있도록 하세요.

### 5단계: 구현에 대한 QA 수행 {#step-5-you-both-perform-qa-on-your-implementation}

개발자와 함께 모든 것이 제대로 작동하는지 확인하세요. [테스트 메시지]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)를 보내고, [Android 테스트 앱]({{site.baseurl}}/developer_guide/references?tab=android)과 [iOS 테스트 앱]({{site.baseurl}}/developer_guide/references?tab=swift)을 사용하여 발송을 시작하기 전에 모든 항목을 점검하세요!

[Android 또는 FireOS 통합 테스트]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android) 및 [iOS 푸시 테스트]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing)에 대한 구체적인 지침도 제공하고 있습니다.

## 구현 이후 {#after-implementation}

구현이 완료되었다고 해서 바로 수백만 건의 메시지를 한꺼번에 보내도 된다는 뜻은 아닙니다. 모든 고객이 동시에 같은 링크를 클릭하면 수백만 건의 푸시를 한꺼번에 보내는 것만으로도 앱이 다운될 수 있습니다. **Send** 버튼을 클릭하기 전에 Braze에서 발생하는 요청을 내부 인프라가 어느 정도까지 처리할 수 있는지 먼저 확인하는 것을 권장합니다. 그런 다음, 이를 기반으로 [사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting)을 설정할 수 있습니다.

![Braze Firebrands 커뮤니티 로고]({% image_buster /assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Braze 사용에 익숙해지면 Braze Firebrand가 되는 것도 고려해 보세요! Braze Firebrands는 고객 참여 커뮤니티로, Braze를 활용하여 고객 경험과 마케팅을 혁신하는 선도자들의 커뮤니티를 만들어 가고 있습니다. 더 자세히 알아보고 싶으신가요? [지금 참여하세요](https://brazefirebrands.splashthat.com/).