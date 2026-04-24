---
nav_title: 대상으로 보내기
article_title: 대상으로 보내기
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "이 참조 문서에서는 대상으로 보내기 구성요소와 캔버스에서 이를 사용하는 방법을 다룹니다."
tool: Canvas
---

# 대상으로 보내기 단계

> 대상으로 보내기 단계를 사용하면 한 캔버스에서 다른 캔버스로 사용자를 보낼 수 있습니다. 예를 들어, 프로모션 오퍼에 대한 메시징을 공유하는 두 개의 캔버스가 있는 경우, 대상으로 보내기를 사용하여 이러한 캔버스를 연결할 수 있습니다.

## 작동 방식

![새 캔버스로 사용자를 보내는 대상으로 보내기 단계.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

대상으로 보내기 단계가 포함된 현재 캔버스가 소스입니다. 이 단계 내에서 대상 캔버스를 선택할 수 있습니다. 여기서 사용자는 대상 캔버스로 전송됩니다. 사용자가 대상 캔버스의 진입 기준을 충족하면 해당 캔버스를 따라 진행하며, 동시에 소스 캔버스도 계속 진행합니다.

## 대상으로 보내기 단계 생성

### 1단계: 단계 추가

사이드바에서 **대상으로 보내기** 구성요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택한 후 **대상으로 보내기**를 선택합니다.

### 2단계: 대상 선택

드롭다운을 선택하거나 **대상** 필드에 캔버스 이름을 입력합니다. 그런 다음 **완료**를 선택합니다.

![사용자를 "Feature Adoption"이라는 캔버스에서 "New Canvas"로 보내도록 설정된 대상으로 보내기 단계.]({% image_buster /assets/img/send_to_destination2.png %})

### 3단계: 대상 미리보기

**대상 미리보기**를 선택하여 대상 캔버스의 진입 기준을 충족하는 사용자의 여정을 확인할 수 있습니다.

이 캔버스 단계를 설정한 후 [사용자 경로 미리보기]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)를 통해 사용자가 현재 캔버스의 다음 단계로 진행하는지, 그리고 대상 캔버스로도 진행하는지 확인할 수 있습니다.

## 자주 묻는 질문

### 대상을 초안 캔버스로 설정할 수 있나요?

네. 대상 캔버스는 초안 또는 유휴 상태일 수 있습니다.

### 컨텍스트 변수가 유지되나요?

네. 소스 캔버스의 [컨텍스트]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)는 항상 대상 캔버스로 전달됩니다.