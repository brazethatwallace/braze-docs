---
nav_title: "옵트인 및 옵트아웃"
article_title: "옵트인 및 옵트아웃"
description: "이 참조 문서에서는 다양한 WhatsApp 옵트인 및 옵트아웃 방법을 다룹니다."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
---

# 옵트인 및 옵트아웃 {#opt-in-and-opt-out}

> WhatsApp 옵트인 및 옵트아웃을 처리하는 것은 매우 중요합니다. WhatsApp은 [전화번호 품질 등급](https://www.facebook.com/business/help/896873687365001)을 모니터링하며, 등급이 낮으면 메시지 한도가 줄어들 수 있습니다. <br><br>높은 품질 등급을 유지하는 한 가지 방법은 사용자가 비즈니스를 차단하거나 신고하지 않도록 하는 것입니다. 이를 위해 [고품질 메시징](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits)(사용자에게 가치를 제공하는 것 등)을 제공하고, 메시지 빈도를 조절하며, 고객이 향후 커뮤니케이션 수신을 옵트아웃할 수 있도록 해야 합니다. <br><br>이 페이지에서는 옵트인 및 옵트아웃 설정 방법과 "정규식" 및 "is" 수정자 간의 차이점을 설명합니다.

옵트인은 외부 소스 또는 SMS, 인앱 및 인브라우저 메시지와 같은 Braze 방법을 통해 수집할 수 있습니다. 옵트아웃은 Braze에서 설정한 키워드와 WhatsApp 마케팅 버튼을 사용하여 처리할 수 있습니다. 옵트인 및 옵트아웃 설정에 대한 안내는 다음 방법을 참조하세요.

## 옵트인 방법 {#opt-in-methods}
- [Braze 외부 옵트인 방법](#external-to-braze-opt-in-methods)
  - [외부에서 구축한 옵트인 목록](#externally-built-opt-in-list)
  - [고객 지원 WhatsApp 채널의 아웃바운드 메시지](#outbound-message-in-customer-support-whatsapp-channel)
  - [인바운드 WhatsApp 메시지](#inbound-whatsapp-message)
- [Braze 기반 옵트인 방법](#braze-powered-opt-in-methods)

### 옵트아웃 방법 {#opt-out-methods}
- [일반 옵트아웃 키워드](#general-opt-out-keywords)
- [마케팅 옵트아웃 선택](#marketing-opt-out-selection)

## Braze WhatsApp 채널의 옵트인 설정 {#set-up-opt-ins-for-your-braze-whatsapp-channel}

WhatsApp 옵트인의 경우 [WhatsApp의 요구 사항](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)을 준수해야 합니다. 또한 Braze에 다음 정보를 제공해야 합니다:
- 모든 사용자에 대한 `external_id`, [전화번호]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) 및 업데이트된 구독 상태. 이는 [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)를 사용하거나 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 통해 전화번호와 구독 상태를 업데이트하여 수행할 수 있습니다.

{% alert note %}
Braze는 구독 상태 업데이트를 허용하는 `/users/track` 엔드포인트의 개선 사항을 출시했으며, 이에 대한 자세한 내용은 [구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)에서 확인할 수 있습니다. 그러나 이미 [`/v2/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2)를 사용하여 옵트인 프로토콜을 생성한 경우 해당 엔드포인트를 계속 사용할 수 있습니다.
{% endalert %}

### Braze 외부 옵트인 방법 {#external-to-braze-opt-in-methods}

앱 또는 웹사이트(계정 등록, 결제 페이지, 계정 설정, 신용카드 단말기)에서 Braze로 전달합니다.

이메일이나 문자에 대한 마케팅 동의를 이미 받고 있는 곳에 WhatsApp을 위한 추가 섹션을 포함하세요. 사용자가 옵트인한 후에는 `external_id`, [전화번호]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) 및 업데이트된 구독 상태가 필요합니다. 이를 위해 Braze 설치 방식에 따라 [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)를 활용하거나 [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)를 사용하세요.

#### 외부에서 구축한 옵트인 목록 {#externally-built-opt-in-list}

이전에 WhatsApp을 사용한 적이 있다면 WhatsApp 요구 사항에 따라 옵트인이 포함된 사용자 목록을 이미 구축했을 수 있습니다. 이 경우 CSV를 업로드하거나 [다음 정보]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv)와 함께 API를 사용하여 Braze에 가져오세요.

#### 고객 지원 WhatsApp 채널의 아웃바운드 메시지 {#outbound-message-in-customer-support-whatsapp-channel}

고객 지원 채널에서 해결된 문제에 대한 후속 조치로 마케팅 메시징 옵트인 여부를 묻는 자동 메시지를 보내세요. 이 기능은 사용 중인 고객 지원 도구의 기능 가용성과 사용자 정보를 보관하는 위치에 따라 달라집니다.

1. WhatsApp Business 전화번호에서 [메시지 링크](https://business.facebook.com/business/help/890732351439459?ref=search_new_0)를 제공합니다.
2. 고객이 옵트인을 나타내기 위해 "예"라고 응답하는 [빠른 답장 동작]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies)을 제공합니다.
3. 커스텀 키워드 트리거를 설정합니다.
4. 위의 방법 중 하나를 사용하는 경우 다음과 같은 경로로 완료해야 할 수 있습니다:
	- [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 호출하여 사용자를 업데이트하거나 생성합니다.
	- [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)를 활용하거나 [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)를 사용합니다.

#### 인바운드 WhatsApp 메시지 {#inbound-whatsapp-message}

고객이 WhatsApp 번호로 인바운드 메시지를 보내도록 합니다.

이는 사용자가 새 채널에서 확인 메시지를 받기를 원하는지 여부에 따라 Canvas 또는 Campaign으로 설정할 수 있습니다.

1. 인바운드 메시지의 실행 기반 전달 트리거가 있는 Campaign을 생성합니다.
2. 웹훅 Campaign을 생성합니다. 웹훅 예시는 [구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#update-subscription-status)을 참조하세요.

{% alert tip %}
[WhatsApp 매니저](https://business.facebook.com/wa/manage/phone-numbers/)의 **Phone Number** > **Message Links**에서 WhatsApp 채널에 참여할 수 있는 URL 또는 QR 코드를 만들 수 있습니다.<br>![WhatsApp QR 코드 작성기.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Braze 기반 옵트인 방법 {#braze-powered-opt-in-methods}

#### SMS 메시지 {#sms-message}

Canvas에서 다음 방법 중 하나를 사용하여 고객에게 WhatsApp 메시지 수신 옵트인 여부를 묻는 Campaign을 설정합니다:
- 고객 Segment: 미국 외 지역의 구독된 마케팅 그룹
- 커스텀 키워드 트리거 설정

고객 프로필의 구독 상태 업데이트에 대해서는 [구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)을 참조하세요.

#### 인앱 또는 인브라우저 메시지 {#in-app-or-in-browser-message}

고객에게 WhatsApp 사용 옵트인을 요청하는 인앱 메시지 또는 인브라우저 팝업을 생성합니다.

Braze SDK와 인터페이스하기 위해 [JavaScript "브릿지"]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge)와 함께 [HTML 인앱 메시지](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)를 사용하세요. WhatsApp 구독 그룹 ID를 사용해야 합니다.

#### 전화번호 수집 양식 {#phone-number-capture-form}

인앱 메시지용 드래그 앤 드롭 편집기에서 [전화번호 수집 양식]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture) 템플릿을 사용하여 사용자 전화번호를 수집하고 WhatsApp 구독 그룹을 확장하세요.

## Braze WhatsApp 채널의 옵트아웃 설정 {#set-up-opt-outs-for-your-braze-whatsapp-channel}

### WhatsApp "혜택 및 공지" 토글 {#whatsapp-offers-and-announcements-toggle}

WhatsApp은 앱 설정에서 사용자가 마케팅 메시지를 옵트아웃할 수 있는 "혜택 및 공지" 토글을 제공합니다. 이 토글은 Braze 구독 그룹과 독립적으로 작동합니다:

- **Braze 구독 그룹**은 Braze 통합(API, 환경설정 센터 또는 SDK)을 통해 관리되며, 메시징 대상으로 지정할 사용자를 제어합니다.
- **WhatsApp의 네이티브 토글**은 Meta에 의해 제어되며 Braze 외부의 플랫폼 수준에서 적용됩니다.

이 두 레이어는 설계상 자동으로 동기화되지 않습니다. 사용자가 WhatsApp에서 "혜택 및 공지" 토글을 끄면, 사용자의 Braze 구독 상태가 "가입됨"으로 표시되더라도 Meta가 플랫폼 수준에서 마케팅 메시지 전달을 차단합니다. 사용자의 환경설정은 전달 시점에서 존중됩니다.

{% alert note %}
Braze는 발송 시도가 이루어지고 Meta가 오류를 반환할 때까지 옵트아웃 신호를 수신하지 않으므로, Braze의 구독 수는 메시지가 시도될 때까지 WhatsApp 토글을 통해 옵트아웃한 사용자를 반영하지 않을 수 있습니다. 이는 해당 피드백 루프가 발생할 때까지 도달 범위 추정치가 약간 과대 평가될 수 있음을 의미합니다.
{% endalert %}

### 일반 옵트아웃 키워드 {#general-opt-out-keywords}

특정 단어를 메시지로 보내는 사용자가 향후 메시징을 옵트아웃할 수 있도록 Campaign 또는 Canvas를 설정할 수 있습니다. Canvas는 성공적인 옵트아웃을 확인하는 후속 메시지를 포함할 수 있으므로 특히 유용합니다.

#### 1단계: "인바운드 WhatsApp 메시지" 트리거로 Canvas 생성 {#step-1-create-a-canvas-with-a-trigger-of-inbound-whatsapp-message}

![WhatsApp 인바운드 메시지를 보내는 사용자가 진입하는 실행 기반 Canvas 진입 단계.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

키워드 트리거를 선택할 때 "Stop" 또는 "No Message"와 같은 단어를 포함하세요. 이 방법을 선택하는 경우 고객이 옵트아웃 단어를 알 수 있도록 해야 합니다. 예를 들어, 초기 옵트인을 받은 후 "이 메시지를 옵트아웃하려면 언제든지 'Stop'이라고 메시지를 보내세요."와 같은 후속 응답을 포함하세요.

![메시지 본문이 'STOP' 또는 'NO MESSAGE'인 WhatsApp 인바운드 메시지를 보내는 메시지 단계.]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### 2단계: 사용자 프로필 업데이트 {#step-2-update-the-users-profile}

[구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)에 설명된 방법 중 하나를 사용하여 사용자 프로필을 업데이트합니다.

### 마케팅 옵트아웃 선택 {#marketing-opt-out-selection}

WhatsApp 메시지 템플릿 생성기에서 "마케팅 옵트아웃" 옵션을 포함할 수 있습니다. 이 옵션을 포함할 때마다 구독 그룹 변경을 위한 후속 단계가 있는 Canvas에서 해당 템플릿을 사용해야 합니다.

1. "마케팅 옵트아웃" 빠른 답장이 포함된 메시지 템플릿을 생성합니다.<br>![푸터 옵션이 '마케팅 옵트아웃'인 메시지 템플릿.]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![마케팅 옵트아웃 버튼을 구성하는 섹션.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. 이 메시지 템플릿을 사용하는 Canvas를 생성합니다.<br><br>
3. 앞의 예시와 동일한 단계를 따르되 트리거 텍스트를 "STOP PROMOTIONS"로 설정합니다.<br><br>
4. [구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)에 설명된 방법 중 하나를 사용하여 사용자의 구독 상태를 업데이트합니다.

## 옵트인 및 옵트아웃 워크플로 설정 {#set-up-opt-in-and-opt-out-workflows}

다음 두 가지 방법으로 WhatsApp의 "START" 및 "STOP" 키워드 응답 워크플로를 구성할 수 있습니다:

- [사용자 업데이트 단계](#user-update-step)
- [두 번째 WhatsApp Campaign을 트리거하는 웹훅 Campaign](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### 사용자 업데이트 단계 {#user-update-step}

[사용자 업데이트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)는 사용자가 구독 그룹의 전화번호로 키워드를 보낼 때 사용자의 전화번호를 WhatsApp 구독 그룹에 추가할 수 있습니다.

사용자 업데이트 단계는 사용자의 전화번호가 구독 그룹에 추가되기 전에 Canvas의 다음 단계로 진행하지 않으므로 경합 조건을 방지합니다. 또한 다른 방법보다 설정 단계가 적으므로 Braze는 일반적으로 이 방법을 권장합니다.

1. 실행 기반 단계 **Send a WhatsApp Inbound Message**로 Canvas를 생성합니다. **Where the message body**를 선택하고 **Is**에 "START"를 입력합니다.

{% alert important %}
"STOP" 메시지의 경우 옵트아웃을 확인하는 메시지 단계와 사용자 업데이트 단계의 순서를 반대로 하세요. 그렇지 않으면 사용자가 먼저 구독 그룹에서 옵트아웃되어 확인 메시지를 받을 수 없게 됩니다.
{% endalert %}

![메시지 본문이 'START'인 WhatsApp 메시지 단계.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. Canvas에서 **Set Up User Update** 단계를 생성하고 **Action**에서 **Advanced JSON Editor**를 선택합니다. <br><br>![동작이 'Advanced JSON Editor'인 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3. 다음 JSON 페이로드로 **User Update object**를 채우고, `XXXXXXXXXXX`를 구독 그룹 ID로 교체합니다:

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4. 후속 WhatsApp 메시지 단계를 추가합니다. <br><br>![Canvas의 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### 고려 사항 {#considerations}

Braze가 [사용자 업데이트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) 요청을 일괄 처리하기 때문에 업데이트가 다양한 속도로 완료될 수 있습니다.

### 두 번째 WhatsApp Campaign을 트리거하는 웹훅 Campaign {#webhook-campaign-to-trigger-a-second-whatsapp-campaign}

웹훅 Campaign은 사용자가 구독 그룹의 전화번호로 키워드를 보낼 때 사용자의 전화번호를 WhatsApp 구독 그룹에 추가한 후 두 번째 Campaign으로의 진입을 트리거할 수 있습니다.

{% alert important %}
STOP 메시지에는 이 방법을 사용할 필요가 없습니다. 확인 메시지는 사용자가 구독 그룹에서 제거되기 전에 전송되므로 다른 두 단계 중 하나를 사용할 수 있습니다.
{% endalert %}

1. 실행 기반 단계 **Send a WhatsApp Inbound Message**로 Campaign 또는 Canvas를 생성합니다. **Where the message body**를 선택하고 **Is**에 "START"를 입력합니다.

![메시지 본문이 'START'인 WhatsApp 메시지 단계.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2. Campaign 또는 Canvas에서 웹훅 메시지 단계를 생성하고 **Request Body**를 **Raw Text**로 변경합니다.

![웹훅의 메시지 단계.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3. **Webhook URL**에 고객의 [엔드포인트 URL]({{site.baseurl}}/api/basics)을 입력하고 그 뒤에 엔드포인트 링크 `campaigns/trigger/send`를 추가합니다. 예를 들어, `https://dashboard-02.braze.eu/campaigns/trigger/send`입니다.

!['Compose Webhook' 섹션 아래의 Webhook URL 필드.]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4. 원시 텍스트에 다음 JSON 페이로드를 입력하고 `XXXXXXXXXXX`를 구독 그룹 ID로 교체합니다. 두 번째 Campaign을 생성한 후 `campaign_id`를 교체해야 합니다.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5. WhatsApp Campaign(두 번째 Campaign)을 생성하고 트리거를 API로 설정합니다. 이 `campaign_id`를 첫 번째 Campaign의 JSON 페이로드에 복사해야 합니다.

#### 고려 사항

- Canvas API 트리거 JSON 페이로드 내의 속성 업데이트는 아직 지원되지 않으므로 WhatsApp 응답 메시지에 대해서만 WhatsApp Campaign을 트리거할 수 있습니다(2단계 참조).
- WhatsApp 템플릿은 응답 메시지로 보내려면 승인을 받아야 합니다. 빠른 응답은 인바운드 메시지 트리거가 동일한 Campaign 또는 Canvas 내에 있어야 하기 때문입니다. [사용자 업데이트 단계](#user-update-step)를 사용하면 Meta 승인 없이 빠른 응답 메시지를 보낼 수 있습니다.

## "정규식"과 "is" 수정자의 차이점 이해 {#understanding-the-difference-between-regex-and-is-modifiers}

이 표에서는 수정자의 작동 방식을 보여주기 위해 `STOP`을 예시 트리거 단어로 사용합니다.

| 수정자 | 트리거 단어 | 동작 |
| --- | --- | --- |
| `Is` | `STOP` | 대소문자에 관계없이 "stop"이라는 전체 단어 사용을 포착합니다. 예를 들어, "stop"은 포착하지만 "please stop"은 포착하지 않습니다. |
| `Matches regex` | `STOP` | 정확한 대소문자의 "STOP" 사용을 포착합니다. 예를 들어, "STOP"과 "PLEASE STOP"은 포착하지만 "stop"은 포착하지 않습니다. |
| `Matches regex` | `(?i)STOP(?-i)` | 대소문자에 관계없이 "STOP"의 모든 사용을 포착합니다. 예를 들어, "stop", "please stop", "never stop sending me messages"를 포착합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="정규식과 is 수정자의 차이점 이해" }