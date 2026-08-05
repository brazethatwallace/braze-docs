---
nav_title: API 트리거 전달
article_title: API 트리거 전달
page_order: 2
page_type: reference
description: "이 참조 문서에서는 API 트리거 캠페인을 스케줄하고 설정하는 방법을 설명합니다."
tool: Campaigns
platform: API

---

# API 트리거 전달 {#api-triggered-delivery}

> API 트리거 캠페인 또는 서버 트리거 캠페인은 보다 고급 트랜잭션 사용 사례에 적합합니다. Braze API 트리거 캠페인을 사용하면 마케터가 Braze 대시보드 내에서 캠페인 문구, 다변량 테스트 및 재자격 규칙을 관리하면서 자체 서버와 시스템에서 해당 콘텐츠의 전달을 트리거할 수 있습니다. 메시지를 트리거하는 API 요청에는 실시간으로 메시지에 템플릿화할 추가 데이터도 포함할 수 있습니다.

## API 트리거 Campaign 설정하기 {#setting-up-an-api-triggered-campaign}

API 트리거 Campaign을 설정하려면 몇 가지 단계가 필요합니다. 먼저 새로운 멀티채널 또는 단일 채널 Campaign을 생성합니다(다변량 테스트 포함).

{% alert note %}
API 트리거 Campaign은 [API Campaign]({{site.baseurl}}/developer_guide/rest_api/api_campaigns#api-campaigns)과 다릅니다.
{% endalert %}

다음으로, 예약된 알림과 동일한 방식으로 문구와 알림을 구성한 후 **API-Triggered Delivery**를 선택합니다. 서버에서 이러한 Campaign을 트리거하는 방법에 대한 자세한 내용은 [API 트리거 Campaign 전송]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) 문서를 참조하세요.

![예약된 알림과 동일한 방식으로 문구와 알림을 구성한 후 API-Triggered Delivery를 선택합니다. 서버에서 이러한 Campaign을 트리거하는 방법에 대한 자세한 내용은 API 트리거 Campaign 전송 문서를 참조하세요.]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## API 트리거와 발송 사이의 지연 줄이기 {#reducing-delay-between-your-api-trigger-and-send}

트리거 엔드포인트를 호출한 후 메시지 발송이 예상보다 오래 걸리는 경우, 트리거 시점에 고객 프로필이 준비되어 있는지 확인하세요.

기본적으로 [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)에서 `send_to_existing_only`는 `true`로 설정되어 있습니다. Braze는 기존 사용자에게만 발송하며, 해당 호출에서 새로운 프로필을 생성하지 않습니다. 사용자를 생성 또는 업데이트하면서 동일한 요청으로 발송하려면 `send_to_existing_only`를 `false`로 설정하고 각 수신자에 `attributes` 객체를 포함하세요.

이메일 Campaigns의 경우, `attributes` 안에 `email`(및 기타 필수 전달 필드)도 포함하세요. 발송을 트리거할 때 프로필에 이메일 주소가 없으면, Braze는 프로필 데이터가 도착할 때까지 약 2시간 동안 재시도합니다. 동일한 호출에 `email`을 포함하면 이러한 지연을 방지할 수 있습니다.

전체 요청 파라미터, 예시 및 재시도 동작에 대한 자세한 내용은 [API 트리거 Campaigns 발송]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#recipient-limits-and-profile-creation) 및 [수신자 객체]({{site.baseurl}}/api/objects_filters/recipient_object)를 참조하세요.

{% alert note %}
이 안내는 API 트리거 Campaigns(`/campaigns/trigger/send`)에 적용됩니다. [트랜잭션 이메일 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)는 다른 요청 형식(`recipient`, 단수)을 사용하며 `send_to_existing_only`를 지원하지 않습니다. 트랜잭션 발송과 함께 사용자를 인라인으로 생성하려면, `recipient` 객체에 `attributes`를 전달하세요.
{% endalert %}

## API 요청에 포함된 템플릿 콘텐츠 사용하기 {#using-the-templated-content-included-with-an-api-request}

메시지를 트리거하는 것 외에도, API 요청에 콘텐츠를 포함하여 `trigger_properties` 객체 내에서 메시지에 템플릿으로 적용할 수 있습니다. 이 콘텐츠는 메시지 본문에서 참조할 수 있습니다.

`trigger_properties` 및 메시지 본문에서 Liquid 태그당 정확히 두 개의 중괄호를 사용합니다. 예시: {% raw %}`{{api_trigger_properties.${your_property}}}`.{% endraw %} 추가 `{` 또는 `}`는 [API 트리거 개인화 실패]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze)의 일반적인 원인입니다.

추가 맥락은 아래의 소셜 알림 예시를 참조하세요.

![메시지에 포함된 트리거 속성정보가 사용자 이름을 자동으로 채운 후 "liked your photo! Click here to see what they've been up to."라는 텍스트가 이어지는 모습.]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## API 트리거 Campaigns의 재자격 설정 {#re-eligibility-with-api-triggered-campaigns}

사용자가 API 트리거 Campaign을 수신하는 횟수는 재자격 설정을 통해 제한할 수 있습니다. 이는 API 트리거가 몇 번 실행되었는지에 관계없이, 사용자가 해당 Campaign을 한 번만 또는 지정된 기간 내에 한 번만 수신한다는 것을 의미합니다.

예를 들어, 사용자가 최근 조회한 상품에 대해 API 트리거 Campaign을 사용하여 메시지를 보내는 경우를 생각해 보겠습니다. 이 경우, 각 상품에 대해 API 트리거가 실행되더라도 하루에 최대 한 건의 메시지만 발송되도록 Campaign을 제한할 수 있습니다. API 트리거 Campaign이 트랜잭션 성격인 경우, 사용자가 트랜잭션을 수행할 때마다 Campaign을 수신할 수 있도록 지연 시간을 0분으로 설정하세요.

![API 트리거 Campaigns의 재자격 설정과 관련된 스크린샷.]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})