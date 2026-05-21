---
nav_title: 결정 분할
article_title: 결정 분할
alias: /decision_split/
page_order: 7
page_type: reference
description: "이 참조 문서에서는 Canvas에서 결정 분할을 생성하고 사용하는 방법을 다룹니다."
tool: Canvas

---

# 결정 분할 {#decision-split}

> Canvas의 결정 분할 구성요소를 사용하면 사용자에게 개인화된 실시간 경험을 제공할 수 있습니다.

![푸시가 활성화되지 않은 사용자와 푸시가 활성화된 사용자를 위한 "푸시 활성화됨?"이라는 이름의 결정 분할 단계.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

이 구성요소를 사용하면 사용자가 쿼리와 일치하는지 여부에 따라 Canvas 분기를 생성할 수 있습니다.

## 결정 분할 생성 {#create-a-decision-split}

워크플로에서 결정 분할을 생성하려면 Canvas에 단계를 추가합니다. 그런 다음 사이드바에서 구성요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택한 후 **결정 분할**을 선택합니다.

### 분할 정의 {#define-your-split}

사용자를 어떻게 분할하시겠습니까? [Segments]({{site.baseurl}}/user_guide/audience/segments/)와 필터를 사용하여 기준을 설정할 수 있습니다. 기본적으로 사용자를 평가한 후 한 단계 또는 다른 단계로 보내는 `true` 또는 `false` 쿼리를 만드는 것입니다. 최소 하나의 Segment 또는 하나의 필터를 사용해야 합니다. Segment와 필터를 모두 사용할 필요는 없습니다.

!["포그라운드 푸시 활성화됨이 true" 필터가 선택된 결정 분할 단계.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
기본적으로 결정 분할 단계의 Segments와 필터는 지연을 추가하지 않는 한 이전 단계를 수신한 직후에 확인됩니다.
{% endalert %}

## 분할 사용 {#use-your-split}

결정 분할을 사용하면 사용자의 Segment나 속성, 심지어 특정 메시징 채널을 사용하여 메시지를 수신하는지 여부에 따라 사용자의 경로를 구분할 수 있습니다!

온보딩 플로우를 만든다고 가정해 보겠습니다. 가입 시 환영 이메일로 시작할 수 있습니다. 그런 다음 이틀 후에 푸시 메시지를 보내되, 푸시가 활성화된 사용자에게만 보내려고 합니다. 그 후 모든 사용자는 가입 3일 후에 또 다른 이메일을 받습니다. 또한 결정 분할을 사용하여 푸시가 활성화되지 않은 사용자에게 인앱 메시지를 보내 푸시 활성화를 권장할 수도 있습니다.

경로 중 하나 뒤에 단계가 없으면 해당 경로로 진행한 사용자는 Canvas를 종료합니다.

![푸시가 활성화되지 않은 사용자와 활성화된 사용자를 위한 "푸시 활성화됨?"이라는 이름의 결정 분할 단계. 푸시가 활성화되지 않은 사용자는 3일 지연 후 이메일 메시지를 받습니다. 푸시가 활성화된 사용자는 1일 지연 후 푸시 알림을 받고, 2일 지연 후 푸시가 활성화되지 않은 사용자와 동일한 이메일 메시지를 받습니다.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## 분석 {#analytics}

이 단계의 분석에 대한 설명은 다음 표를 참조하세요.

| 측정기준 | 설명 |
|---|---|
| _진입_ | 해당 단계에 진입한 총 횟수입니다. Canvas에 재자격이 있고 사용자가 결정 분할 단계에 두 번 진입하면 두 번의 진입이 기록됩니다. |
| _예_ | 지정된 기준을 충족하고 "예" 경로로 진행한 진입 수입니다. |
| _아니요_ | 지정된 기준을 충족하지 않고 "아니요" 경로로 진행한 진입 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics" }