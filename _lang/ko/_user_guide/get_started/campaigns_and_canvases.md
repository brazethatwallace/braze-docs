---
nav_title: Campaigns 및 Canvases
article_title: "시작하기: Campaigns 및 Canvases"
page_order: 3
page_type: reference
description: "이 문서는 Braze를 사용하여 메시지를 보낼 수 있는 다양한 방법에 대한 개요를 제공합니다."

---

# 시작하기: Campaigns 및 Canvases {#get-started-campaigns-and-canvases}

> 이 문서는 Braze를 사용하여 메시지를 보낼 수 있는 다양한 방법에 대한 개요를 제공합니다. Braze에서는 [Campaign](#campaigns) 또는 [Canvas](#canvas)를 통해 메시지를 보낼 수 있습니다.

- 단일 타겟 메시지를 사용자 그룹에 보내려면 Campaign을 선택하세요. Campaign은 다양한 메시징 채널에서 사용자와 연결하기 위한 단일 메시지 단계입니다.
- 포괄적인 고객 여정 내에서 지속적인 메시지 시리즈를 보내려면 여정 오케스트레이션 도구인 Canvas를 선택하세요. Campaigns는 간단하고 타겟팅된 메시지를 보내는 데 적합하지만, Canvases는 고객과의 관계를 한 단계 끌어올리는 곳입니다.

## Campaigns {#campaigns}

Campaigns는 채널에 따라 고유하게 구축될 수 있지만, Braze에서 알아야 할 주요 Campaign 유형은 네 가지입니다:

| Campaign 유형 | 설명 |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 정규 | 가장 일반적인 유형의 Campaign입니다. 메시징 목표에 따라 하나 이상의 채널을 타겟팅하고, Braze의 시각적 편집기를 사용하여 콘텐츠를 직접 설계, 커스텀 및 테스트할 수 있습니다. [Campaign 생성]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/) 방법을 알아보세요. |
| A/B 테스트 | 단일 채널을 타겟팅하는 Campaigns의 경우, 동일한 Campaign의 여러 버전을 보내고 어떤 버전이 가장 좋은 성과를 내는지 확인할 수 있습니다. [다변량 Campaign]({{site.baseurl}}/user_guide/messaging/ab_testing/)을 통해 최대 8개의 다른 버전으로 카피, 개인화 등을 테스트할 수 있습니다. |
| API | [API Campaigns]({{site.baseurl}}/api/api_campaigns/)를 사용하면 가능한 한 빠르게 시기적절한 메시지를 보낼 수 있습니다. 다른 Campaign 유형과 달리, Braze 대시보드에서 메시지, 수신자 또는 스케줄을 지정하지 않습니다. 대신 이러한 식별자를 API 호출에 전달합니다. 일반적으로 실시간 트랜잭션 메시징이나 속보에 사용됩니다. |
| 트랜잭션 이메일 | Braze [트랜잭션 이메일]({{site.baseurl}}/user_guide/channels/email/)은 귀하와 고객 간의 합의된 거래를 촉진하기 위해 자동화된 비프로모션 이메일 메시지를 보내도록 설계되었습니다. 속도가 가장 중요한 단일 사용자에게 비즈니스에 중요한 알림을 보냅니다. *일부 패키지에서만 사용할 수 있습니다.* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

{% alert note %}
정규 및 A/B 테스트 Campaigns는 스케줄에 따라 발송하거나(예: 다가오는 이벤트에 대해 사용자 목록에 알림) 사용자의 행동에 대한 응답으로 자동 발송할 수 있습니다(예: 누군가가 뉴스레터를 구독할 때 이메일 발송). [Campaigns 스케줄링]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/)에 대해 자세히 알아보세요.
{% endalert %}

어떤 유형의 Campaign을 생성하든, Campaigns는 사용자의 요구를 파악하고 사려 깊고 개인화된 응답을 전달할 수 있습니다. Campaign을 발송한 후에는 [내장 분석 도구]({{site.baseurl}}/user_guide/analytics/reports/)를 사용하여 성과를 확인하고 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/)를 기반으로 얼마나 많은 사용자가 전환했는지 확인하세요.

Braze에서 Campaigns에 대해 더 알아보려면 다음 추가 리소스를 확인하세요:

- Braze 학습센터: [Campaign 설정](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Campaign 생성]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/)
- [아이디어와 전략]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/)

## Canvas {#canvas}

여러 Campaigns에 걸쳐 산발적인 메시지를 보내는 대신, Canvases는 사용자와 지속적이고 유동적인 대화를 만듭니다. 사용자가 Canvas를 통해 이동하는 과정이 브랜드와의 행동(또는 비행동)에 따라 다른 경로로 나뉠 수 있기 때문에, 실시간으로 특정 흐름을 통해 사용자를 자동으로 진행시킬 수 있습니다.

![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

이러한 방식으로, Canvases는 전환 경로에서 이탈한 사용자를 포착하여 가장 효과적인 아웃리치 이니셔티브에 배치하는 데 매우 유용합니다.

Canvas를 생성할 때는 Campaign을 설정하는 것과 동일한 단계를 많이 따릅니다: 전체 오디언스, 진입 조건 및 발송 설정을 지정합니다. 누군가가 트리거 조건과 일치하면 Canvas가 시작됩니다. 그런 다음 종료 조건을 충족할 때까지 Canvas의 경로를 따라 이동합니다.

Canvas는 [메시지]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/), [지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/), [실험]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) 등 다양한 조합을 가질 수 있습니다. 지원되는 모든 메시징 채널로 발송할 수 있으며, Facebook, Google, TikTok 등 [소셜 및 광고 플랫폼과 통합]({{site.baseurl}}/partners/canvas_audience_sync/overview/)할 수도 있습니다.

Canvas에 대해 더 알아보려면 다음 추가 리소스를 확인하세요:

- Braze 학습센터: [Canvas 플로우를 활용한 여정 오케스트레이션](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Canvas 생성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)
- [Canvas 아웃라인]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines/)

## 메시징 채널 {#messaging-channels}

메시징 채널은 고객과 소통하고 타겟 메시지를 전달할 수 있는 다양한 커뮤니케이션 채널입니다.

![]({% image_buster /assets/img/getting_started/channels.png %})

다음 표는 지원되는 채널을 설명합니다.

| 채널 | 설명 |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [이메일]({{site.baseurl}}/user_guide/channels/email/) | 사용자의 받은편지함으로 개인화된 이메일을 보내세요. |
| [모바일 푸시]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/) | 사용자의 모바일 기기로 알림을 직접 전달합니다. |
| [웹 푸시]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/) | 사용자가 웹사이트에 적극적으로 접속하지 않아도 웹 브라우저에 알림을 전달합니다. |
| [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/) | 사용자가 모바일 앱을 적극적으로 사용하는 동안 앱 내에 메시지를 표시합니다. |
| [SMS, MMS, RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/)* | 사용자의 휴대폰으로 문자 메시지를 보내세요. |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)* | 인기 있는 메시징 플랫폼인 WhatsApp을 통해 메시지를 보내고 사용자와 소통하세요. |
| [배너]({{site.baseurl}}/user_guide/channels/banners/)* | 앱이나 웹사이트에 메시지를 직접 삽입합니다. |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/)* | 앱 또는 웹사이트 내에서 사용자가 메시지를 수신하고 상호작용할 수 있는 받은편지함을 제공하거나, 메시지를 캐러셀, 배너 등으로 표시합니다. |
| [커넥티드 TV]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/) | 커넥티드 TV 플랫폼에서 사용자와 소통하세요. |
| [웹훅]({{site.baseurl}}/user_guide/channels/webhooks/) | 커스텀 HTTP 콜백을 통해 외부 시스템과의 실시간 통신 및 통합을 활성화합니다. |
| [LINE]({{site.baseurl}}/user_guide/channels/line/) | 일본에서 가장 인기 있는 메시징 앱인 LINE에서 사용자와 소통하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messaging channels" }

<sup>*추가 기능으로 사용할 수 있습니다.*</sup>

{% alert tip %}
대부분의 채널(이메일, SMS, 푸시)을 통해 전달할 수 있는 짧고 긴급한 메시지의 경우, [인텔리전트 채널]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/) 필터를 활용하여 각 사용자에게 가장 적합한 채널을 통해 메시지를 자동으로 전송하세요.
{% endalert %}