---
nav_title: 동작 검토
article_title: BrazeAI Operator<sup>TM</sup> 동작 검토
page_order: 2
description: "BrazeAI Operator가 대시보드에서 변경 사항을 제안할 때 동작을 검토하고 승인하는 방법을 알아보세요."
---

# BrazeAI Operator 동작 검토 {#reviewing-brazeai-operator-actions}

> BrazeAI Operator<sup>TM</sup>가 대시보드에서 변경 사항을 제안할 때 동작을 검토하고 승인하는 방법을 알아보세요.

![Operator가 검토를 위해 제안된 액션 카드를 제시하는 화면.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## 액션 카드 작동 방식 {#how-action-cards-work}

Operator가 대시보드에서 변경 사항을 제안할 때(예: 양식 필드 채우기, 설정 업데이트, 이미지 생성 등), 각 변경 사항을 검토할 수 있도록 액션 카드로 표시합니다.

1. **Operator가 계획을 요약합니다:** Operator는 액션 카드를 표시하기 전에 수행할 계획을 설명합니다.
2. **개별 액션 카드가 나타납니다:** 제안된 각 변경 사항은 Operator가 대시보드에서 변경하거나 수행하려는 내용을 보여주는 별도의 카드로 표시됩니다. 기존 값에 대한 변경의 경우, 이전 값과 제안된 값이 비교를 위해 나란히 표시됩니다.
3. **검토 및 승인:** 각 카드를 검토하고 승인하거나 거부합니다.
4. **액션 실행:** 승인된 액션은 Braze에서 실행됩니다. 거부된 액션은 적용되지 않습니다.

승인 후 액션이 실패하면, Operator가 실패에 대한 세부 정보를 알려줍니다.

### 사용 가능 범위 {#availability}

Operator는 메시지 작성기, 목록 및 개요 페이지, 설정 등 지원되는 대시보드 페이지에서 액션 카드를 제안할 수 있습니다. 표현 기반 범위에 대해서는 [Operator로 할 수 있는 것]({{site.baseurl}}/user_guide/brazeai/operator/capabilities)을 참조하세요. 지원되는 메시지 채널 및 편집기에 대해서는 [메시지 생성]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages)을 참조하세요.

지원 범위는 정기적으로 확장됩니다. Operator가 현재 페이지에서 작동할 수 없는 경우, UI에서 따라야 할 단계 목록을 대신 제공합니다.

## 플랜 수정 {#modify-a-plan}

Operator의 플랜을 수정하려면 먼저 대기 중인 작업을 승인하거나 거부합니다. 그런 다음 새 채팅 메시지에서 원하는 변경 사항을 설명합니다.

승인된 작업은 Operator를 통해 되돌릴 수 없습니다. Operator에 새로운 변경 사항을 설명하거나 대시보드에서 직접 변경합니다.

## 자동 승인 작업 {#auto-approve-actions}

**자동 승인 작업** 토글은 Operator 채팅 패널에 있습니다.

- **켜기:** Operator가 제안한 작업이 수동 승인 없이 즉시 실행되며, 요청을 완료하기 위해 [다른 페이지로 이동]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard)하는 것도 포함됩니다. 이미지 생성이나 워크스페이스 수준 설정 변경 등 일부 작업은 안전을 위해 여전히 명시적 승인이 필요합니다.
- **끄기(기본값):** 제안된 모든 작업은 페이지 이동을 포함하여 위에서 설명한 수동 검토 프로세스를 따릅니다. Operator가 이동을 제안하고 사용자의 승인을 기다린 후 해당 페이지로 이동합니다.

![Operator 채팅 패널의 자동 승인 토글 및 확인 Modal.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

자동 승인은 페이지를 새로고침하거나, 새 탭을 열거나, 로그아웃 후 다시 로그인하면 초기화됩니다. 대시보드 내에서 페이지 간 이동 시에는 초기화되지 않습니다. 자동 승인은 언제든지 끌 수 있습니다.

Operator 접근 제한 및 팀 사용 감사에 대한 자세한 내용은 [데이터 프라이버시 및 보안]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security)을 참조하세요.