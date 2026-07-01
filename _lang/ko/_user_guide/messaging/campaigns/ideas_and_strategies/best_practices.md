---
nav_title: 모범 사례
article_title: 캠페인 모범 사례
page_order: 0
description: "이 문서에서는 캠페인을 생성하고 커스터마이징하기 위한 모범 사례를 제공합니다."
tool: Campaign

---

# 캠페인 모범 사례 {#campaign-best-practices}

> 이 문서에서는 캠페인을 생성하고 커스터마이징하기 위한 모범 사례를 제공합니다.

## Braze의 4T 원칙 {#four-ts-of-braze}

Braze는 Braze 플랫폼에서 활용할 의도가 있는 고객 데이터만 전송할 것을 권장합니다. "Braze의 4T 원칙"을 고려하여 실제로 사용할 데이터만 전송하세요:

- **타겟(Target)**: [오디언스 Segments]({{site.baseurl}}/user_guide/audience/segments)를 구축하여 오디언스를 타겟팅합니다.
- **트리거(Trigger)**: [액션 기반]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#action-based-delivery) 또는 [API 트리거]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) 전달로 메시지를 트리거합니다.
- **템플릿(Template)**: [Liquid 조건 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)으로 메시지를 템플릿화하고 개인화합니다.
- **추적(Track)**: [전환 추적]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)으로 캠페인의 효과를 추적합니다.

이를 통해 Braze로 전송하는 데이터를 최적화하고, 팀이 장기적으로 유용하지 않다고 판단할 수 있는 데이터 포인트 추적을 방지하면서 사용자에게 메시지를 보내는 능력을 간소화할 수 있습니다.

## 사용자 타겟팅 {#user-targeting}

시간이 지남에 따라 캠페인을 구축하다 보면 오디언스에서 이탈이 발생할 수 있습니다. 이 중요한 시점에서 세분화를 활용한 전문 캠페인으로 [이탈 중인 사용자]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users)를 타겟팅할 수 있습니다.

### 오디언스 파악하기 {#identify-your-audience}

Segments와 필터를 활용하여 오디언스를 정의하세요. 캠페인과 메시지가 누구를 타겟팅하는지 고려하세요. 이 핵심 정보를 바탕으로 오디언스의 알림 환경설정에 맞춰 다양한 채널에서 메시지를 구성할 수 있는 유연성을 제공하는 [멀티채널 캠페인]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-campaigns)을 생성할 수 있습니다.

또한 꾸준히 이용하는 사용자에게 감사를 표하기 위해 [활성 사용자]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/active_user_campaigns)를 이해하는 것도 중요합니다.

## 멀티채널 캠페인 {#multichannel-campaigns}

### 기능 인지도 {#feature-awareness}

사용자를 새로운 기능이나 앱 버전으로 유도하는 것이 목표라면, 인앱 채널에 중점을 둔 멀티채널 전략을 사용하세요. [인앱 메시지]({{site.baseurl}}/in-app_messages)와 [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)는 사용자가 즉시 업데이트하고 싶지 않을 때 일반적으로 덜 방해가 됩니다.

적절한 앱 스토어로의 [딥링크]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls)를 반드시 포함하세요.

사용자에게 앱을 업데이트하거나 앱 사용 방식을 변경하도록 설득하는 것은 어려울 수 있으므로, 새 버전이나 기능의 모든 이점과 앱 경험이 어떻게 개선되는지 알려주세요.

### 발송 타이밍 {#send-timing}

타이밍이 핵심입니다! 사용자에게 앱 업데이트를 설득하는 것이 목표라면, 앱 내에서 긍정적인 경험을 한 후에 요청하세요. 오디언스의 참여를 유지하려면 방해가 될 수 있는 반복적인 메시징을 피하세요.

시간이 지나면 사용자가 특정 기능을 잊거나 새로운 기능을 인지하지 못할 수 있습니다. 새로운 기능이 추가되면 [인앱 메시지]({{site.baseurl}}/in-app_messages)로 사용자에게 알려주세요. 사용자가 앱 내 주요 기능에 참여하지 않는 경우, 앱을 사용하고 있을 때 그리고 새 기능이 유용할 때 알려주는 것이 가장 좋습니다. [데이터 옵트인]({{site.baseurl}}/user_guide/channels/content_cards)에 대한 문서에서 요청이 사용자의 워크플로 기대에 부합하도록 하는 방법에 대한 자세한 정보를 확인할 수 있습니다.

## 높은 평점 {#high-ratings}

앱 스토어에서 별 5개 평점을 받는 것은 모든 모바일 마케터의 소원입니다. 하지만 긍정적인 리뷰를 얻는 것은 사용자의 추가적인 노력이 필요하기 때문에 쉬운 일이 아닙니다. Braze의 기능을 현명하게 활용하면 고객 참여를 높이는 데 도움이 됩니다.

### 파워 유저 타겟팅 {#targeting-power-users}

파워 유저는 앱의 옹호자가 될 수 있습니다. 이들은 앱을 꾸준히 사용하며 앱 개선을 위한 피드백을 제공할 수 있습니다. 앱마다 다르지만, 파워 유저는 일반적으로 다음과 같은 특성을 가지고 있습니다:

- 많은 세션을 기록함
- 최근에 앱을 사용함
- 돈을 지출하고 구매를 함

더 높은 평점을 확보하려면 파워 유저에게 앱 스토어에서 리뷰를 남겨달라고 요청하세요. 이들은 좋은 평가를 남길 가능성이 높습니다. 예를 들어, 다음 필터를 사용하여 "파워 유저"라는 Segment를 생성할 수 있습니다:
- 지난 14일 동안 이 앱을 10회 이상 사용함
- 50달러 이상 지출함

![앱의 파워 유저를 타겟팅하는 Segment 예시.]({% image_buster /assets/img_archive/ratings_power_users.png %})

앱 스토어를 방문하는 것은 사용자의 시간이 소요됩니다. 추가적인 노력을 기울일 가능성을 극대화하려면, 앱에서 긍정적인 경험을 한 직후에 평점이나 리뷰를 요청하세요. 예를 들어, 게임 레벨을 클리어하거나 할인 코드를 사용하여 구매한 후에 요청하세요. [데이터 옵트인]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)에 대한 문서에서 요청이 사용자의 워크플로 기대에 부합하도록 하는 방법에 대한 자세한 정보를 확인할 수 있습니다.

## 캠페인 스케줄링 {#scheduling-your-campaigns}

캠페인 스케줄이나 오디언스를 편집할 때 다음 모범 사례를 참고하세요:

- **일회성 스케줄 캠페인:** 예약된 발송 시간까지 캠페인을 편집할 수 있습니다.
- **반복 스케줄 캠페인:** 예약된 발송 시간까지 캠페인을 편집할 수 있습니다.
- **현지 발송 시간 캠페인:** 예약된 발송 시간 24시간 전에는 편집하지 마세요.
- **최적 발송 시간 캠페인:** 캠페인이 발송 예정인 날의 자정 24시간 전에는 편집하지 마세요.

Canvas 스케줄링의 세부 사항(초안, 중지, 발송 시간 전후 평가)은 [Canvas 모범 사례]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/best_practices#scheduling-your-canvases)를 참조하세요.

{% alert note %}
라이브 캠페인을 편집하여 전달 방식을 **현지 발송 시간**으로 변경하면 새로운 메시지 배치가 대기줄에 추가되어, 메시지가 두 번 대기줄에 들어가므로 사용자가 메시지를 두 번 받게 됩니다. 이를 방지하려면 먼저 원래 캠페인을 중지한 다음, 스케줄을 업데이트한 후 복제본을 시작하세요.
{% endalert %}