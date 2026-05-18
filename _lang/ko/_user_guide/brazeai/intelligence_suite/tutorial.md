---
nav_title: "Tutorial: 퀵 서비스 레스토랑"
article_title: Intelligence Suite 튜토리얼
page_order: 10
search_rank: 12
description: "Braze Intelligence Suite를 처음 사용하시나요? 이 튜토리얼부터 시작하세요."
tool:
  - Dashboard
---

# Intelligence Suite 튜토리얼 {#intelligence-suite-tutorial}

> Braze Intelligence Suite를 처음 사용하시나요? 이 튜토리얼부터 시작하세요! 자세한 내용은 [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/)를 참조하세요.

## 튜토리얼: 퀵 서비스 레스토랑 {#tutorial-quick-service-restaurant}

패스트푸드 레스토랑인 SandwichEmperor에서 일한다고 가정해 봅시다. 이 레스토랑에서 새로운 한정 메뉴 아이템인 Royal Roast를 출시했습니다. Canvas에서 개인화된 프로모션을 보내기 위해 두 가지 Intelligence Suite 기능을 사용하겠습니다.

### 1단계: Intelligent Timing을 사용하여 알림 발송 시점 결정하기 {#step-1-use-intelligent-timing-for-when-to-send-notifications}

Intelligent Timing을 사용하여 앱 및 각 메시징 채널에서 사용자의 과거 상호작용을 분석한 다음, 각 사용자에게 Royal Roast를 홍보할 최적의 시간을 자동으로 선택합니다. 일부 사용자는 오후에 프로모션을 받을 수 있고, 다른 사용자는 저녁에 받을 수 있습니다.

분석할 과거 상호작용이 충분하지 않은 사용자를 위해 대체 시간을 제공합니다. 이 대체 시간은 모든 사용자 중 앱을 가장 많이 사용하는 시간대입니다.

![메시지 단계의 Intelligent Timing 전달 설정.]({% image_buster /assets/img/intelligence_suite1.png %})

### 2단계: 지능형 선택을 사용하여 프로모션 선택하기 {#step-2-use-intelligent-selection-to-select-the-promotion}

실제 프로모션 메시지의 경우, 지능형 선택을 사용하여 Royal Roast에 대한 세 가지 메시지(푸시 알림, 이메일, SMS)를 테스트합니다. 지능형 선택은 하루에 두 번 모든 프로모션 메시지의 성과를 분석한 후, 가장 성과가 좋은 메시지를 점진적으로 더 많이 보내고 나머지 메시지는 덜 보냅니다.

지능형 선택이 최고 성과 메시지를 결정하기에 충분한 데이터를 수집하면, 이후 발송의 100%에 해당 메시지를 사용합니다.

![지능형 선택이 활성화된 Canvas의 A/B 테스트 섹션.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### 3단계: Canvas 시작하기 {#step-3-launch-the-canvas}

Intelligent Timing과 지능형 선택을 모두 활용하여 Royal Roast 프로모션의 타이밍과 메시징이 최적화되도록 설정했습니다. 이제 Canvas를 시작하고 사용자 선호에 맞게 발송이 조정되는 과정을 지켜볼 수 있습니다.