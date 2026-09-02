---
nav_title: 채널 필터
article_title: 인텔리전트 채널 필터
page_order: 1.5
description: "이 문서는 인텔리전트 채널 필터에 대해 다루고 있으며, 선택된 메시징 채널이 가장 적합한 채널인 오디언스의 일부를 선택하는 필터입니다. 이 경우, 최적이란 사용자의 기록을 고려할 때 참여 가능성이 가장 높은 것을 의미합니다."
search_rank: 11
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}인텔리전트 채널 필터 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommost-engaged-channel-stylefloatrightwidth120pxborder0-classnoimgborderintelligent-channel-filter}

> `Intelligent Channel` 필터(이전 명칭 `Most Engaged`)는 선택된 메시징 채널이 "최적" 채널인 오디언스의 일부를 선택합니다.

## 필터 소개 {#about-the-filter}

![선택할 수 있는 다양한 채널에 대한 드롭다운이 있는 인텔리전트 채널 필터.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

이 경우, 최적이란 사용자의 기록을 고려할 때 참여 가능성이 가장 높은 채널을 의미합니다. 이메일, 단문 메시지 서비스, WhatsApp, 웹 푸시 또는 모바일 푸시(사용 가능한 모든 모바일 OS 또는 기기 포함)를 채널로 선택할 수 있습니다.

인텔리전트 채널은 지원되는 각 채널에 대해 각 사용자의 참여율을 계산하고, 해당 채널의 순위를 매긴 다음, 가장 높은 순위의 채널을 해당 사용자의 최적 채널로 처리합니다.

인텔리전트 채널 필터를 활성화하려면 Campaign 또는 Canvas를 생성할 때 **타겟 오디언스** 페이지에서 **Intelligent Channel** 필터를 선택합니다.

## 채널별 참여율 계산 방법 {#how-engagement-is-calculated-by-channel}

인텔리전트 채널은 참여율을 사용하여 채널을 비교합니다. 참여율은 메시지 상호작용 수를 수신한 메시지 수로 나눈 값입니다. Braze는 지난 6개월 이내에 채널당 수신한 최근 100개의 메시지까지 평가합니다.

사용자에게 메시지가 전송되거나 사용자가 메시지와 상호작용할 때마다 참여율이 몇 초 내에 다시 계산됩니다. 사용자는 메시지와 상호작용한 것으로 한 번만 계산됩니다(예를 들어, 동일한 이메일에서 열람 및 클릭이 발생해도 해당 메시지는 두 번이 아닌 한 번만 상호작용한 것으로 표시됩니다).

### 채널별 상호작용 데이터 {#interaction-data-by-channel}

Braze는 참여율을 계산할 때 다음 이벤트를 추적합니다:

- **이메일:** 열람([머신 열람]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) 제외). 이메일 클릭은 포함되지 않습니다.
- **모바일 푸시:** 직접 열람. 각 모바일 플랫폼(iOS, Android, Kindle 등)은 별도로 점수가 매겨집니다. 푸시 영향 열람은 포함되지 않습니다.
- **웹 푸시:** 열람
- **단문 메시지 서비스:** 단축 링크 클릭
- **WhatsApp:** 메시지 읽음 또는 추적 링크 클릭

푸시 영향 열람, 이메일 클릭 및 세션 활동은 인텔리전트 채널에 사용되지 않습니다. 세션 활동은 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#about-intelligent-timing)에서 사용됩니다.

인텔리전트 채널은 웹훅, LINE, Kakao Talk, 인앱 메시지 또는 Content Cards를 지원하지 않습니다.

{% alert important %}
단문 메시지 서비스 채널의 참여율을 계산하려면 고급 추적 및 클릭 추적과 함께 [단문 메시지 서비스 링크 단축]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)을 켜세요. 이 추적이 없으면 [동점 해결 동작]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#tie-breaking)으로 인해 단문 메시지 서비스가 0% 참여율로 인텔리전트 채널로 선택될 수 있습니다.
{% endalert %}

## 데이터가 충분하지 않음 {#not-enough-data}

Braze가 어떤 채널이 "최적"인지 결정하려면 충분한 데이터가 필요합니다. 이는 사용자가 채널당 최소 세 개 이상의 메시지를 수신해야 해당 채널의 순위를 매길 수 있으며, 최소 두 개 이상의 지원 채널에서 충분한 데이터가 있어야 함을 의미합니다.

사용자가 채널을 통해 충분한 메시지를 받지 못한 경우, 해당 사용자는 이 필터의 "데이터 부족" 옵션에 속하게 됩니다. 이를 통해 지원되는 메시징 채널을 사용하여 이러한 사용자를 타겟팅할 수 있습니다.

예를 들어 푸시 메시지를 선호하는 사용자에게는 푸시를, 데이터가 충분하지 않은 사용자에게는 동일한 푸시 메시지를 보내려고 한다고 가정해 보겠습니다. 이 경우 인텔리전트 채널 필터를 **모바일 푸시**로 설정하고 **OR**을 사용하여 **데이터 부족**으로 설정된 두 번째 인텔리전트 채널 필터를 추가할 수 있습니다. 이메일을 선호하는 사용자를 대상으로 하는 별도의 Campaign에서는 인텔리전트 채널 필터를 이메일로 설정할 수 있습니다.

![모바일 푸시 또는 데이터 부족에 대한 인텔리전트 채널 필터.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
[최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules)을 무시하는 Campaigns 및 캔버스 단계는 인텔리전트 채널에 의해 고려되지 않으며 데이터 요구 사항에 기여할 수 없습니다.
{% endalert %}

## 모바일 푸시 {#mobile-push}

모바일 푸시는 Android, iOS, Kindle 및 Braze에서 사용할 수 있는 기타 모바일 기기 채널을 포함합니다. Braze는 참여율을 계산할 때 각 모바일 플랫폼을 별도로 점수 매깁니다.

인텔리전트 채널 필터를 **모바일 푸시**로 설정하면, iOS 푸시 또는 Android 푸시가 가장 높은 순위의 채널인 경우 사용자가 일치합니다. 이것이 사용자가 특정 기기에서만 푸시 알림을 받도록 강제하지는 않습니다. 이 순위는 이메일, 웹 푸시, 단문 메시지 서비스, WhatsApp과 비교하여 모바일 푸시가 해당 사용자의 최적 채널인지 결정하는 데만 사용됩니다.

## 개별 채널에 대한 메시지 열람 가능성 필터 {#individual-channels}

Braze가 사용자에게 가장 적합한 단일 채널을 선택하도록 하는 대신, ["메시지 열람 가능성" 세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood)를 사용하여 선택한 특정 채널에서 메시지를 열 가능성이 있는지 여부에 따라 사용자를 필터링할 수 있습니다. 이 필터는 채널당 전송된 마지막 100개의 메시지에 대한 상호작용 비율로 계산됩니다.

메시지 열람 가능성은 인텔리전트 채널과 동일한 기본 참여 데이터를 사용하지만, 사용자의 최적 채널을 선택하는 대신 단일 채널에 대한 임계값을 설정할 수 있습니다. 이메일, 모바일 푸시, 단문 메시지 서비스, 웹 푸시에서 사용할 수 있습니다.

특정 채널에 대한 가능성 점수를 받으려면 사용자가 해당 채널에서 최소 세 개의 메시지를 수신해야 합니다. 채널의 가능성을 측정할 충분한 데이터가 없는 사용자는 "비어 있음"을 사용하여 선택할 수 있습니다.

## 모범 사례 및 효과적인 사용 전략 {#best-practices-and-effective-use-strategy}

### 동점 해결 {#tie-breaking}

일부 사용자는 수신한 메시지 수가 적기 때문에 특정 사용자에 대해 사용 가능한 채널 간 참여율이 동점인 경우가 드물지 않습니다(예: 단일 사용자가 이메일 및 모바일 푸시 모두에 대해 20% 참여율을 가짐). 이러한 경우에는 가장 최근에 상호작용 이벤트가 있는 채널에 우선 순위를 부여하여(더 높은 순위를 매겨) 동점을 해결합니다.

동점인 채널 모두 0% 참여율인 경우, Braze는 가장 최근에 메시지를 수신한 채널을 사용하여 동점을 해결합니다.

### 도달할 수 없는 채널 {#unreachable-channels}

사용자가 Braze에서 채널 순위를 결정할 수 있는 충분한 데이터를 가지고 있지만, 가장 높은 순위의 채널에서 도달할 수 없게 될 수 있습니다. 예를 들어, 과거 최적 채널이 이메일인 사용자가 최근 이메일 구독을 취소했을 수 있습니다. 해당 채널로 메시지를 보내면 해당 사용자에게 전달되지 않습니다. 특정 채널에서 도달할 수 없는 사용자는 별도로 타겟팅하거나 라우팅해야 합니다.

### 오디언스 사이징 {#audience-sizing}

인텔리전트 채널을 사용하면 나머지 오디언스보다 메시지에 참여할 가능성이 훨씬 높은 사용자 그룹을 미리 선택적으로 타겟팅할 수 있습니다. 이 그룹은 일반적인 오디언스에서 대다수를 차지하지 않을 가능성이 큽니다. 오히려, 이 필터는 특정 채널에서 참여한 기록이 있는 일반 오디언스의 5~20%를 찾아낼 것으로 기대할 수 있습니다.