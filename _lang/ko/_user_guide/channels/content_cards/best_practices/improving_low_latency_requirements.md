---
nav_title: 낮은 지연 시간 개선
article_title: 배너로 사용하는 콘텐츠 카드의 낮은 지연 시간 개선
page_order: 10
description: "이 문서에서는 콘텐츠 카드의 낮은 지연 시간 요구 사항을 충족하기 위한 전략을 다룹니다."
channel:
  - content cards
---

# 배너로 사용하는 콘텐츠 카드의 지연 시간 개선 {#improve-latency-for-content-cards-as-banners}

> 홈페이지 배너와 같은 중요한 사용 사례에서 콘텐츠 카드 구현 시 지연 시간이 발생하는 경우, 이 페이지에서 렌더링 속도를 높이고 문제를 해결하기 위한 전략과 팁을 확인하세요.

{% alert tip %}
앱이나 웹사이트에 눈에 띄는 커스텀 배너를 표시하고 싶으신가요? 낮은 지연 시간의 배너 사용 사례를 지원하도록 설계된 [배너]({{site.baseurl}}/user_guide/channels/banners)를 사용해 보세요.
{% endalert %}

## 액션 기반 진입 대신 예약된 진입 사용하기 {#use-scheduled-entry-instead-of-action-based-entry}

Campaigns와 Canvases 모두에서 액션 기반 카드는 백그라운드 처리가 필요합니다. Braze는 사용자에게 카드를 생성하기 전에 먼저 트리거 액션(예: 구매 발생 또는 세션 시작)에 대한 알림을 수신해야 합니다. 따라서 이러한 카드를 사용할 수 있게 되기까지 지연이 발생합니다.

액션 기반 카드는 앱에 복잡성을 추가하여, 카드가 사용 가능해질 때까지 지속적으로 폴링하고 새로고침해야 하는 상황이 발생할 수 있습니다. 대신 카드를 `Scheduled Entry`로 구성하면, 타겟 오디언스에게 항상 카드가 제공되는 가용 기간으로 작동합니다.

카드를 미리 스케줄하면, 사용자가 앱을 열고 카드를 요청할 때 이미 준비된 상태로 대기하고 있습니다.

## "첫 노출 시" 전송 로직 사용 {#use-at-first-impression-send-logic}

스케줄된 전송과 함께 `At First Impression` 옵션을 사용하면 카드가 Braze에서 생성되고 저장되는 속도 덕분에 지연 시간을 방지할 수 있습니다. `At Campaign Launch` 옵션은 Segment에 포함된 모든 사용자의 카드를 미리 생성하므로 완료까지 시간이 걸릴 수 있습니다. `At First Impression` 옵션은 사용자가 앱을 처음 열 때와 같이, 카드가 처음 요청되는 시점에 해당 사용자의 카드를 생성합니다.

따라서 스케줄된 진입과 함께 사용하면 세션 시작 시점이든 시간 기반 자격 조건 기간이든, 카드가 필요한 즉시 사용할 수 있습니다.

## Canvas 항목은 카드를 수신하기 위한 전제 조건입니다 {#remember-that-canvas-entry-is-a-prerequisite-for-receiving-cards}

Canvas를 사용할 때, 사용자는 먼저 설정된 항목 기준에 따라 Canvas에 진입한 *다음*, Content Cards 메시지 단계를 거쳐야 합니다. 그래야만 앱이나 웹사이트에서 카드를 사용할 수 있습니다. 사용자가 단계를 통과한 후 카드가 생성되기까지 기본적인 지연 시간이 있으며, 이로 인해 카드를 사용할 수 있는 시점이 늦어질 수 있다는 점을 기억하세요.

## 카드를 과도하게 새로고침하지 마세요 {#dont-refresh-cards-excessively}

Content Cards는 새로운 세션이 시작될 때마다 SDK에 의해 자동으로 새로고침됩니다. 활성 세션 중에 언제든지 수동으로 Content Cards 새로고침을 요청할 수도 있습니다. 지원되는 SDK 버전에서 Braze는 [실시간 전달]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#real-time-delivery)을 통해 세션 동안 전송 및 제거를 기기에 푸시하므로, 수동으로 새로고침해야 하는 빈도가 줄어듭니다.

`requestContentCardsRefresh` 메서드를 호출하고 너무 자주 새로고침하면 사용량 제한조치가 적용될 수 있습니다. 앱에 일시적으로 사용량 제한조치가 적용되면, 필요할 때나 사용자가 앱에 참여하는 중요한 시점에 카드를 새로고침하지 못할 수 있습니다.

이를 방지하려면, 사용자가 구매를 완료한 후나 가입 등급을 업그레이드한 후와 같이 사용자 라이프사이클에서 중요한 시점에만 이 새로고침 메서드를 호출하세요.

## 연결된 콘텐츠 포함 지양 {#avoid-including-connected-content}

연결된 콘텐츠는 자사 또는 서드파티 API 데이터로 Content Cards를 풍부하게 만들어 줍니다. 그러나 Content Cards 메시지에 포함하면 연결된 콘텐츠 네트워크 요청이 완료될 때까지 카드의 가용성이 차단됩니다. 경우에 따라 SDK가 몇 초 후에 재시도하게 되는데, 이는 앱의 렌더링 로직이 SDK의 새로고침 작업 완료를 기다릴 수 있기 때문에 지연을 방지하기 위한 것입니다.

연결된 콘텐츠를 반드시 사용해야 하는 경우, 이러한 카드를 사전에 스케줄하고 `At Campaign Launch` 옵션을 사용하여 사용자의 다음 세션 이전에 카드가 미리 생성되도록 하세요. 이 카드들은 Braze가 모든 적격 사용자에 대해 카드를 작성하기 때문에 즉시 사용할 수 없다는 점에 유의하세요.