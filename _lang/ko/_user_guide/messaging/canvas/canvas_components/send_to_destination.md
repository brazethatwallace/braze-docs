---
nav_title: 대상으로 보내기
article_title: 대상으로 보내기
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "이 참조 문서에서는 대상으로 보내기 구성요소와 Canvases에서 이를 사용하는 방법을 다룹니다."
tool: Canvas
---

# 대상으로 보내기 단계 {#send-to-destination-step}

> 대상으로 보내기 단계를 사용하면 한 Canvas에서 다른 Canvas로 사용자를 보낼 수 있습니다. 예를 들어, 프로모션 오퍼에 대한 메시징을 공유하는 Canvases를 연결할 수 있습니다.

## 작동 방식 {#how-it-works}

![사용자를 새 Canvas로 보내는 목적지로 보내기 단계.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

목적지로 보내기 단계가 포함된 현재 Canvas가 소스입니다. 이 단계 내에서 목적지 Canvas를 선택할 수 있습니다. 소스 Canvas의 사용자는 목적지 Canvas의 오디언스 기준을 충족해야 합니다. 두 개의 Canvases가 있다고 가정해 보겠습니다:

- **소스:** Canvas 1, 사용자를 Canvas 2로 보내는 목적지로 보내기 단계를 포함
- **목적지:** Canvas 2, 아이템을 주문한 사용자를 진입시키는 오디언스 기준 포함

이 단계를 통해 Canvas 1의 사용자를 Canvas 2로 보낼 수 있습니다. Canvas 1의 사용자가 목적지로 보내기 단계에 진입하면, Canvas 2의 오디언스 기준에 따라 해당 Canvas에 진입할 자격이 있는지 평가됩니다. 이 경우, 아이템을 주문한 사용자는 Canvas 2에 진입할 수 있으며 Canvas 1에서의 여정도 계속됩니다. 아이템을 주문하지 않은 사용자는 Canvas 1에서만 여정을 계속합니다.

### 진입 동작 {#entry-behavior}

목적지로 보내기 단계는 사용자가 이 단계에 도달하는 즉시 목적지 Canvas에 진입시킵니다. 이 단계는 목적지 Canvas로의 일회성 진입 지점 역할을 합니다. 목적지 Canvas의 오디언스 기준을 충족하는 사용자는 해당 Canvas 여정을 시작합니다. 해당 시점에 기준을 충족하지 않는 사용자는 목적지 Canvas에 진입하지 않고 소스 Canvas에서 계속 진행합니다.

목적지로 보내기는 **진입 제어** 아래의 목적지 Canvas [재진입 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)도 준수합니다. 사용자가 목적지 Canvas에 재진입할 자격이 없는 경우, 해당 Canvas로 보내지지 않고 소스 Canvas에서 계속 진행합니다.

목적지 Canvas가 예약된 진입 스케줄을 사용하는 경우, 목적지로 보내기 단계는 해당 진입 스케줄을 우회합니다. 또한 목적지 Canvas의 **진입 제어** 아래 [**진입 볼륨 제한**]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls)이 **Canvas가 스케줄될 때마다**로 설정된 경우에도 이를 우회합니다. 이 단계에서 보내진 사용자는 다음 예약된 평가 기간을 기다리지 않으며, 목적지로 보내기 단계에 도달하는 즉시 목적지 Canvas의 오디언스 기준에 따라 평가되고 바로 진입합니다.

목적지 Canvas가 액션 기반 진입을 사용하는 경우, 목적지로 보내기 단계는 사용자가 해당 Canvas에 진입하기 위해 구성된 진입 액션을 수행해야 하는 요구 사항을 우회합니다.

## 목적지로 보내기 단계 만들기 {#create-a-send-to-destination-step}

### 1단계: 단계 추가하기 {#step-1-add-a-step}

사이드바에서 **목적지로 보내기** 구성 요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택한 다음 **목적지로 보내기**를 선택합니다.

### 2단계: 목적지 선택하기 {#step-2-choose-your-destination}

드롭다운을 선택하거나 **목적지** 필드에 Canvas 이름을 입력합니다. 그런 다음 **완료**를 선택합니다.

![사용자를 "Feature Adoption"이라는 Canvas에서 "New Canvas"로 보내도록 설정된 목적지로 보내기 단계.]({% image_buster /assets/img/send_to_destination2.png %})

### 3단계: 목적지 미리보기 {#step-3-preview-your-destination}

**목적지 미리보기**를 선택하여 사용자를 보내려는 Canvas를 확인할 수 있습니다.

이 캔버스 단계를 설정한 후 [사용자 경로 미리보기]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)를 통해 사용자가 현재 Canvas의 다음 단계로 진행하는지, 그리고 목적지 Canvas로도 진행하는지 확인할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 대상을 초안 Canvas로 설정할 수 있나요? {#can-i-set-the-destination-to-a-draft-canvas}

네. 대상 Canvas는 초안 또는 유휴 상태일 수 있습니다.

### 컨텍스트 변수가 유지되나요? {#are-context-variables-preserved}

네. 소스 Canvas의 [컨텍스트]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)가 대상 Canvas로 전달됩니다. 단, 컨텍스트 변수는 대상 Canvas로 전달되려면 소스 Canvas 내에서 호출되어야 합니다.

### API나 사용자 업데이트 우회 방법 대신 대상으로 전송 단계를 사용하여 Canvases를 연결할 수 있나요? {#can-i-use-the-send-to-destination-step-to-connect-canvases-instead-of-using-api-or-user-update-workarounds}

네. 사용자가 다른 Canvas 여정으로 직접 이동해야 할 때 대상으로 전송 단계를 사용하여 Canvases를 연결할 수 있습니다.

사용자가 전송 시점에 대상 Canvas의 오디언스 기준을 충족하는 한, Canvases 간에 사용자를 이동시키기 위해 별도의 사용자 업데이트 단계, API 트리거 또는 웹훅을 사용할 필요가 없습니다.

### 사용자가 대상 Canvas의 처음부터 진입하나요? {#do-users-enter-at-the-start-of-the-destination-canvas}

자격을 갖춘 사용자는 대상 Canvas의 첫 번째 단계에 즉시 진입합니다. 대상 Canvas의 이후 예약된 진입 시간을 기다리지 않습니다. 대상 Canvas 내의 특정 캔버스 단계로 직접 연결할 수는 없습니다.

### 대상으로 전송 단계는 예약된 대상 Canvas의 진입 스케줄을 따르나요? {#does-the-send-to-destination-step-respect-a-scheduled-destination-canvas-entry-schedule}

아니요. 대상 Canvas가 예약된 진입 유형을 사용하는 경우, 대상으로 전송 단계에서 전송된 사용자는 다음 예약된 평가 기간을 기다리지 않습니다. 사용자가 대상으로 전송 단계에 도달하면 오디언스 기준에 대해 즉시 평가되어 진입합니다.

### 대상으로 전송 단계의 진행 동작은 어떻게 작동하나요? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

대상으로 전송 단계에 진입한 사용자는 소스 Canvas에 추가 단계가 있는 경우 사용자 여정을 계속합니다. 사용자가 대상 Canvas의 오디언스 기준도 충족하면 해당 Canvas에 진입하여 해당 여정을 시작할 수 있습니다.