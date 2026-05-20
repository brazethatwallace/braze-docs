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

> 대상으로 보내기 단계를 사용하면 한 Canvas에서 다른 Canvas로 사용자를 보낼 수 있습니다. 예를 들어, 프로모션 오퍼에 대한 메시징을 공유하는 두 개의 Canvases가 있는 경우, 대상으로 보내기를 사용하여 이러한 Canvases를 연결할 수 있습니다.

## 작동 방식 {#how-it-works}

![새 Canvas로 사용자를 보내는 대상으로 보내기 단계.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

대상으로 보내기 단계가 포함된 현재 Canvas가 소스입니다. 이 단계에서 대상 Canvas를 선택할 수 있습니다. 소스 Canvas에서 유입되는 사용자는 대상 Canvas의 진입 규칙을 따라야 합니다. 두 개의 Canvases가 있다고 가정해 보겠습니다:

- **소스:** Canvas 1, 사용자를 Canvas 2로 보내는 대상으로 보내기 단계를 포함
- **대상:** Canvas 2, 아이템을 주문한 사용자를 진입시키는 진입 기준 포함

이 단계를 통해 Canvas 1의 사용자를 Canvas 2로 보낼 수 있습니다. Canvas 1의 사용자가 대상으로 보내기 단계에 진입하면, Canvas 2의 진입 규칙에 따라 해당 Canvas에 진입할 자격이 있는지 평가됩니다. 이 경우, 아이템을 주문한 사용자는 Canvas 2에 진입할 수 있으며 동시에 Canvas 1에서의 여정도 계속 진행합니다. 아이템을 주문하지 않은 사용자는 Canvas 1에서만 여정을 계속 진행합니다.

## 대상으로 보내기 단계 생성 {#create-a-send-to-destination-step}

### 1단계: 단계 추가 {#step-1-add-a-step}

사이드바에서 **대상으로 보내기** 구성요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택한 후 **대상으로 보내기**를 선택합니다.

### 2단계: 대상 선택 {#step-2-choose-your-destination}

드롭다운을 선택하거나 **Destination** 필드에 Canvas 이름을 입력합니다. 그런 다음 **Done**을 선택합니다.

![사용자를 "Feature Adoption"이라는 Canvas에서 "New Canvas"로 보내도록 설정된 대상으로 보내기 단계.]({% image_buster /assets/img/send_to_destination2.png %})

### 3단계: 대상 미리보기 {#step-3-preview-your-destination}

**Preview destination**을 선택하여 대상 Canvas의 진입 기준을 충족하는 사용자의 여정을 확인할 수 있습니다.

이 캔버스 단계를 설정한 후 [사용자 경로 미리보기]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths/)를 통해 사용자가 현재 Canvas의 다음 단계로 진행하는지, 그리고 대상 Canvas로도 진행하는지 확인할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 대상을 초안 Canvas로 설정할 수 있나요? {#can-i-set-the-destination-to-a-draft-canvas}

네. 대상 Canvas는 초안 또는 유휴 상태일 수 있습니다.

### 컨텍스트 변수가 유지되나요? {#are-context-variables-preserved}

네. 소스 Canvas의 [컨텍스트]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)는 항상 대상 Canvas로 전달됩니다.