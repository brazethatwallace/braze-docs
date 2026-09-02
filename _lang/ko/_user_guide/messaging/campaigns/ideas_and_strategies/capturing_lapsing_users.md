---
nav_title: 이탈 위험 사용자 확보
article_title: 이탈 위험 사용자 확보
page_order: 1
page_type: tutorial
description: "이 사용 가이드에서는 이탈 위험 사용자 문제를 다루고, Braze Campaign을 효과적으로 활용하여 해당 사용자를 재참여시키는 방법을 설명합니다."
tool:
  - Segments
  - Campaigns

---

# 이탈 위험 사용자 확보 {#capture-lapsing-users}

> 오디언스가 줄어들고 있다면, 다시 불러오는 것이 매우 중요합니다. Braze를 사용하면 자동화된 반복 재참여 Campaign을 설정하여 이탈 위험 사용자를 확보할 수 있습니다. 앱에 가장 적합한 재참여 기간과 반복 주기를 선택할 수 있지만, 여기서는 14일 재참여 플랜을 예시로 시작하겠습니다.

사용자 타겟팅에 대한 자세한 내용은 Campaign 설정에 관한 [Braze 학습 과정](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)을 확인하세요!

## 1단계: 사용자 Segment 생성 {#step-1-segment-users}

먼저 지난 2주 동안 앱을 사용하지 않은 사용자를 타겟팅할 Segment를 만들겠습니다. 다음 필터를 사용합니다:

- **최근 앱 사용일**이 2주 이상 전
- **최근 앱 사용일**이 3주 미만 전

![1단계: 사용자 Segment 생성 관련 스크린샷.]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Segment에 "휴면 사용자 – 2주"처럼 기억하기 쉬운 이름을 지정하세요. Campaign이 매주 반복되도록 설정할 것이므로, Segment에 최소 1주일 분량의 사용자가 포함되도록 해야 합니다. 그래서 2주에서 3주 사이에 마지막으로 앱을 사용한 사용자를 선택했습니다.

## 2단계: Campaign 만들기 {#step-2-create-a-campaign}

다음으로 **Create Campaign**을 클릭하고 이 Segment에 보낼 Campaign 유형을 선택합니다. 이 예제에서는 새로운 [푸시 Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)을 만들겠습니다.

![다음으로 Create Campaign을 클릭하고 이 Segment에 보낼 Campaign 유형을 선택합니다. 이 예제에서는 새로운 푸시 Campaign을 만들겠습니다.]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Campaign 이름을 "Message to Lapsed Users - 2 Weeks"로 지정한 다음 메시지 내용을 작성합니다. 이 예제에서는 iOS 사용자만 타겟팅하지만, Braze를 사용하면 Android와 iOS 푸시 알림을 모두 보낼 수 있습니다.

사용자가 마지막으로 앱을 사용한 시점에 가까울수록 시의적절하고 관련성 있는 콘텐츠가 더욱 중요합니다. 2주간 앱을 사용하지 않은 사용자에게 메시지를 보낼 때는 관련성 높은 콘텐츠를 노출하고 앱 사용의 이점을 강조하는 것이 중요합니다.

![2단계 관련 스크린샷: Campaign 만들기.]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

다음으로, **Time-Based Scheduling Options**에서 [현지 시간대 전달]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer)을 사용하여 매주 목요일 오후 5:45에 주간 메시지를 보내는 반복 스케줄을 만들겠습니다. 세션 그래프를 확인하여 사용량이 높은 시간대 직전에 사용자를 타겟팅하는 것을 권장합니다. 이렇게 하면 사용자가 앱을 사용할 가능성이 가장 높은 시점에 재참여를 유도할 수 있습니다. 나중에 이 설정을 변경하고 초기 가설을 테스트할 수 있습니다.

![Time-Based Scheduling Options에서 현지 시간대 전달을 사용하여 매주 목요일 오후 5:45에 주간 메시지를 보내는 반복 스케줄을 만듭니다. 세션 그래프를 확인하여 사용량이 높은 시간대 직전에 사용자를 타겟팅하는 것을 권장합니다. 이렇게 하면 사용자가 앱을 사용할 가능성이 가장 높은 시점에 재참여를 유도할 수 있습니다. 나중에 이 설정을 변경하고 초기 가설을 테스트할 수 있습니다.]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## 3단계: Campaign 시작하기 {#step-3-launch-the-campaign}

이제 Campaign을 보낼 준비가 되었습니다. 작성기의 마지막 페이지에서 설정을 확인하고 **Launch Campaign**을 클릭하세요!