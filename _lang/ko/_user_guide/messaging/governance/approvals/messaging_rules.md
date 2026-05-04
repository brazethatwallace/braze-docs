---
nav_title: 메시징 규칙
article_title: 메시징 규칙
page_order: 1
page_type: reference
description: "이 페이지에서는 대량 발송 볼륨이 있는 Campaigns 및 Canvases의 승인 워크플로우에서 메시징 규칙을 사용하는 방법을 다룹니다."
---

# 메시징 규칙 {#messaging-rules}

> 승인 워크플로우에서 메시징 규칙을 사용하여 추가 승인이 필요하기 전에 도달 가능 사용자 수를 제한하세요. 이렇게 하면 더 큰 오디언스를 타겟팅하기 전에 Campaigns 및 Canvases를 검토할 수 있습니다.

## 필수 조건 {#prerequisites}

Braze 관리자만 메시징 규칙을 설정할 수 있지만, 모든 Braze 사용자가 메시징 규칙 승인자가 될 수 있습니다(일반 승인 권한이 없는 사용자 포함).

## 작동 방식 {#how-it-works}

메시징 규칙은 워크스페이스에 적용되며, 메시지 유형과 최대 도달 가능 사용자 수로 구성됩니다.

- **메시지 유형:** 규칙이 적용되는 메시지 유형을 정의합니다: Campaign, Canvas, 또는 Canvas와 Campaigns 모두.
- **최대 도달 가능 사용자:** 추가 승인이 필요한 오디언스 규모를 결정합니다.

### 별도의 승인자 {#separate-approvers}

두 규칙이 동일한 사용자 최대값을 공유할 수 있으므로 승인자별로 규칙을 구성하고 분리할 수 있습니다. 예를 들어, 다음 두 가지 규칙을 생성합니다:

- 법무팀 승인자가 있는 최대 100,000명 사용자의 Canvas용 규칙 A
- 마케팅팀 승인자가 있는 최대 100,000명 사용자의 Canvas용 규칙 B

### 도달 가능 사용자 중복 불가 {#no-overlapping-reachable-users}

혼란을 방지하기 위해, 동일한 메시지 유형과 승인자에 대해 사용자 수가 중복되는 동일한 규칙을 설정할 수 없습니다. 예를 들어, 다음 메시징 규칙은 설정할 수 **없습니다**:

- 최대 10,000명 사용자의 Canvas용 규칙 C
- 최대 1,000,000명 사용자의 Canvas용 규칙 D

## 메시징 규칙 생성 {#creating-a-messaging-rule}

### 1단계: 규칙 추가 {#step-1-add-a-rule}

{% alert note %}
최대 5개의 메시징 규칙을 생성할 수 있습니다.
{% endalert %}

1. **설정** > **승인 워크플로우** > **메시징 규칙**으로 이동합니다.
2. **규칙 생성**을 선택합니다.
3. 이 규칙에 이름을 지정합니다(예: "모든 사용자 구독").
4. **메시지 유형**에서 **Campaign**, **Canvas**, 또는 **Both Canvas and Campaigns**를 선택하여 승인 규칙을 적용합니다.
5. **Maximum reachable users**에 숫자를 입력합니다. 자세한 내용은 [오디언스 통계]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/#audience-statistics)를 참조하세요.
6. **저장**을 선택합니다.

![최대 100,000명 사용자의 Campaigns용 메시징 규칙 예시 "규칙 1". Canvas와 Campaign 시작을 승인할 수 있는 사용자가 한 명 있습니다.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### 2단계: 승인을 통한 시작 결정(선택 사항) {#step-2-determine-launching-with-approval-optional}

**Allow launching with approval**을 선택합니다. 그런 다음 **With Approval From**에서 최대값이 충족될 경우 Canvas 또는 Campaign을 승인할 권한이 있는 승인자를 선택합니다.

승인을 통한 메시지 시작에 대한 다음 세부 사항을 참고하세요:

- 최대값이 충족되고 승인자가 선택된 경우, 승인 권한이 있는 Braze 사용자가 **Target Audience** 승인 드롭다운에서 **Approved**를 선택할 수 있습니다.
- 최대값이 충족되고 승인자가 선택되지 않은 경우, Canvas 또는 Campaign의 시작이 차단됩니다.

![시작하려면 승인이 필요하다는 것을 보여주는 Canvas 워크플로우의 "요약" 단계.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## 자주 묻는 질문 {#frequently-asked-questions}

### 메시징 규칙을 사용하려면 권한을 다시 구성해야 하나요? {#do-i-have-to-reconfigure-my-permissions-to-use-messaging-rules}

아니요. 현재 권한에 관계없이 모든 사용자가 대상 집단 승인자로 선택될 수 있습니다.

### 메시징 규칙은 타겟 오디언스 단계와 어떤 관련이 있나요? {#how-do-messaging-rules-relate-to-the-target-audience-step}

메시징 규칙은 트리거 이벤트와 같은 세부 사항을 고려하지 않습니다. 예를 들어, Campaign이 모든 사용자를 타겟팅할 수 있습니다. 그러나 해당 Campaign이 이벤트 트리거 방식이므로 실제로 수신하는 사용자 수는 더 적습니다.

### 메시징 규칙이 켜지면 자동으로 변경되는 사항이 있나요? {#will-anything-automatically-change-when-messaging-rules-are-turned-on}

아니요. 이 기능이 켜진 후에는 기능을 사용하려면 최대 사용자 수를 수동으로 입력하고 승인자를 선택해야 합니다.