---
nav_title: 콘텐츠 카드
article_title: Canvas의 콘텐츠 카드
page_order: 1
page_type: reference
description: "이 참조 문서에서는 Canvas 내에서 Content Cards를 메시징 채널로 사용할 때의 기능과 주의사항을 설명합니다."
tool: Canvas
channel: content cards

---

# Canvas의 Content Cards {#content-cards-in-canvas}

> Content Cards는 Canvas 여정의 일부로 고객에게 전송할 수 있습니다. 이 문서에서는 Canvas 내에서 Content Cards를 메시징 채널로 사용할 때의 기능과 주의사항을 설명합니다.

다른 Canvas 메시징 채널과 마찬가지로, Content Cards는 사용자가 해당 단계에 지정된 오디언스 및 타겟팅 기준을 충족할 때 사용자의 기기로 전송됩니다. Content Cards가 전송된 후에는 다음에 카드 피드가 새로고침될 때 각 대상 사용자의 피드에서 확인할 수 있습니다.

![메시지 단계의 메시징 채널로 Content Cards가 선택된 모습.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Content Cards 단계가 Canvas와 상호작용하는 방식을 변경하는 두 가지 옵션은 [만료](#content-card-expiration)와 [제거](#removal)입니다.

## Content Cards 만료 {#content-card-expiration}

새 Content Cards를 작성할 때 전송 시간을 기준으로 사용자의 피드에서 만료되는 시점을 선택할 수 있습니다. Content Cards의 만료 카운트다운은 사용자가 카드가 전송되는 Canvas의 메시지 단계에 도달할 때 시작됩니다. 카드는 이 시점부터 만료될 때까지 사용자의 피드에서 활성 상태로 유지됩니다. 카드는 사용자의 피드에 최대 30일 동안 존재할 수 있습니다.

![사용자의 피드에서 3시간 후 제거되는 메시지 단계의 Content Cards 만료 설정.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### 만료 유형 {#types-of-expiration}

카드가 사용자의 피드에서 사라지는 시점을 설정하는 방법은 상대 날짜와 절대 날짜 두 가지가 있습니다.

#### 상대 날짜 {#relative-dates}

"사용자의 피드에서 5일 후 전송된 카드 제거"와 같이 상대 날짜를 선택하면 최대 30일까지 만료 날짜를 설정할 수 있습니다.

#### 절대 날짜 {#absolute-dates}

"2023년 12월 1일 오후 4시에 전송된 카드 제거"와 같이 절대 날짜를 선택하는 경우 몇 가지 주의사항이 있습니다.

만료 기간을 30일 이상으로 지정할 수 있지만, Content Cards는 사용자의 피드에 최대 30일 동안만 존재합니다. 30일보다 긴 기간을 지정하면 메시지 단계가 트리거되기 전의 지연을 고려할 수 있지만, 사용자의 피드에서 카드의 최대 수명이 연장되지는 않습니다.

Canvas 시작일로부터 30일 이상 앞선 만료 날짜를 설정할 때는 주의하세요. 사용자가 지정된 만료 날짜보다 30일 이상 전에 메시지 단계에 도달하면 카드가 전송되지 않습니다.

#### Liquid를 사용한 개인화된 만료 {#personalized-expiry-with-liquid}

Liquid 개인화를 사용하여 만료 기간을 설정하는 경우(예: 커스텀 속성 또는 Canvas 진입 속성 사용), 절대 날짜나 상대 날짜와는 동작이 다릅니다.

- 개인화된 만료가 30일보다 긴 기간으로 확인되면, Braze가 자동으로 최대 30일로 제한합니다.
- Content Cards는 제한된 만료 기간으로 사용자에게 전송됩니다.
- 사용자는 Canvas의 다음 단계로 진행합니다.

이 제한을 통해 확인된 기간이 플랫폼 한도를 초과하더라도 개인화된 만료가 적용된 카드가 전달됩니다. 처리 원장 결과에는 "Personalized expiration capped by max TTL"이 표시되며, `reason=capped_by_max_ttl` 및 `capped=true`를 나타내는 세부 정보가 포함됩니다.

### 만료 동작 {#expiration-behavior}

Content Cards는 사용자가 Canvas 여정의 후속 단계로 진행하더라도 만료 날짜에 도달할 때까지 사용자의 피드에서 계속 사용할 수 있습니다. Canvas의 다음 단계가 전달될 때 Content Cards가 활성 상태가 아니길 원한다면, 만료 기간이 후속 단계의 지연보다 짧은지 확인하세요.

Content Cards가 만료되면 사용자가 아직 확인하지 않았더라도 다음 새로고침 시 사용자의 피드에서 자동으로 제거됩니다.

## Content Cards 제거 {#removal}

Content Cards는 사용자가 구매를 완료하거나 커스텀 이벤트를 수행할 때 제거할 수 있습니다. 제거 이벤트로 **커스텀 이벤트 수행** 및 **구매하기** 중 하나를 선택할 수 있습니다. 그런 다음 **트리거 추가**를 선택합니다.

!["사용자가 구매를 완료하거나 커스텀 이벤트를 수행할 때 카드 제거"가 선택되어 있으며, 특정 주문을 한 사용자의 카드를 제거하는 트리거가 설정된 모습.]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## 보고서 및 분석 {#reporting-and-analytics}

Canvas에서 Content Cards 단계를 시작한 후 이 단계에 대한 여러 측정기준을 분석할 수 있습니다. 이러한 측정기준에는 전송된 메시지 수, 일일 고유 노출 횟수, 전환율, 총 매출 등이 포함됩니다.

![Content Cards 메시지 성과가 표시된 메시지 단계의 분석.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

사용 가능한 측정기준과 정의에 대한 자세한 내용은 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/analytics/metrics_glossary)을 참조하세요.

## 활용 사례 {#use-cases}

### 프로모션 오퍼 {#promotional-offers}

사용자가 특정 프로모션 및 광고 대상이 될 때 카드를 사용자의 피드에 추가합니다. 예를 들어, 사용자가 특정 동작을 수행하거나 구매를 한 후 새로운 오퍼 대상이 되면, Canvas를 사용하여 다른 메시징 채널과 함께 Content Cards를 전송할 수 있으므로 다음에 앱을 열 때 해당 오퍼를 확인할 수 있습니다.

### 푸시 알림 받은편지함 {#push-notification-inbox}

사용자가 푸시 알림을 무시하거나 이메일을 삭제하는 경우가 있지만, 마음이 바뀔 경우를 대비하여 알림을 보내거나 오퍼를 홍보하고 싶을 수 있습니다.

Canvas를 사용하면 Content Cards와 푸시 알림을 모두 전송하는 구성요소를 추가하여 푸시를 통해 전송된 프로모션 메시지와 연동되는 지속적인 카드 "받은편지함"을 사용자에게 제공할 수 있습니다.

### 카테고리 기반 다중 피드 {#multiple-feeds-based-on-categories}

사용자가 탐색할 수 있는 다양한 주제, 또는 트랜잭션 및 마케팅 피드와 같은 카테고리를 기반으로 Content Cards를 여러 피드로 분리할 수 있습니다. 키-값 페어를 사용하여 다중 피드를 만드는 방법에 대한 자세한 내용은 [Content Cards 피드 커스터마이징]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds) 가이드를 참조하세요.