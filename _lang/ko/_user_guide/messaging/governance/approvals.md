---
nav_title: 승인
article_title: 승인
page_order: 1
page_type: reference
description: "이 참조 문서에서는 Campaign과 Canvas가 가질 수 있는 다양한 상태와 그 의미에 대한 개요를 제공합니다."
tool:
    - Campaigns
    - Canvas
---

# Campaigns 및 Canvases 승인 {#approvals-for-campaigns-and-canvases}

> 승인을 사용하여 Campaigns 및 Canvases를 시작하기 전에 최종 검토 단계를 추가하세요. 이 워크플로우를 통해 메시지의 모든 필수 섹션에서 콘텐츠를 확인하고 승인할 수 있습니다.

## 작동 방식 {#how-it-works}

편집의 마지막 단계에서 Campaign 또는 Canvas의 세부 정보를 검토할 수 있습니다.

Canvases와 Campaigns 모두 승인하기 전에 모든 변경 사항을 저장해야 하며, 본인이 직접 변경한 사항이라도 마찬가지입니다. 적절한 권한을 가진 사용자가 메시지를 시작하기 전에 요약의 각 섹션을 승인해야 합니다. 각 섹션의 기본 상태는 **Pending Approval**입니다.

{% tabs %}
{% tab campaign %}
Campaign을 시작하려면 다음 구성요소를 승인해야 합니다:

- **Messages:** Campaign 메시지입니다.
- **Delivery:** 전달 유형이며, 사용자가 Campaign을 수신하는 시기를 결정합니다.
- **Target Audience:** Campaign을 수신할 대상을 결정합니다.
- **Conversion Events:** 참여 및 보고 목적으로 추적하는 측정기준입니다.
{% endtab %}

{% tab canvas %}
Canvas를 시작하려면 다음 주요 구성요소를 승인해야 합니다:

- **Conversion Events:** 참여 및 보고 목적으로 추적하는 측정기준입니다.
- **Entry Schedule:** 진입 스케줄 유형과 사용자가 Canvas에 진입하는 시기를 포함합니다.
- **Target Audience:** Canvas에 진입할 대상을 결정합니다.
- **Send Settings:** Canvas의 모든 단계에 대한 발송 옵션입니다.
- **Build Canvas:** Canvas 사용자 여정입니다.
{% endtab %}
{% endtabs %}

## 승인 워크플로우 켜기 {#turning-on-the-approval-workflow}

기본적으로 승인 워크플로우 설정은 Campaigns와 Canvases에 대해 꺼져 있습니다. 이 기능을 켜려면 **설정** > **승인 워크플로우**로 이동하여 해당 토글을 선택합니다:

- **[워크스페이스]의 모든 Campaigns에 승인 워크플로우 사용**
- **[워크스페이스]의 모든 Canvases에 승인 워크플로우 사용**

{% alert important %}
Campaign 승인은 [API 캠페인]({{site.baseurl}}/api/api_campaigns/) 및 [트랜잭션 이메일 캠페인]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/)에는 지원되지 않습니다.
{% endalert %}

## 사용자 권한 설정 {#setting-user-permissions}

승인 워크플로우를 켠 후, 회사 사용자가 Campaigns와 Canvases를 승인하거나 거부할 수 있도록 사용자 권한을 설정해야 합니다. 두 권한 모두 워크스페이스 또는 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/)에 적용하거나 [권한 세트]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#permission-sets)에 추가할 수 있습니다.

{% tabs %}
{% tab campaign %}
["Approve and Deny Campaigns" 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#managing-limited-and-team-role-permissions)이 있어야 합니다. 이 권한은 Campaign의 승인 상태를 업데이트할 수 있는 사용자를 제어합니다. 이 권한이 있으면 다음을 수행할 수 있습니다:

- Campaign을 직접 승인
- Campaign을 승인하고 시작
- Campaign을 승인하되 시작하지 않음("Send Campaigns, Canvases" 권한을 가진 다른 사용자가 Campaign을 시작할 수 있음)
- Campaign을 승인하지도 시작하지도 않음

**Summary** 단계에서 승인 상태가 설정된 후, Campaign에 대한 후속 변경 사항은 저장 시 모든 승인 상태를 초기화합니다. 이는 초안 Campaign이든 시작 후 Campaign이든 관계없이 적용됩니다. 예를 들어, 타겟 오디언스만 변경하더라도 **Summary** 단계에서 모든 섹션의 승인 상태가 기본 상태인 **Pending Approval**로 되돌아갑니다.

{% endtab %}

{% tab canvas %}
["Approve and Deny Canvases" 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#managing-limited-and-team-role-permissions)이 있어야 합니다. 이 권한은 Canvas의 승인 상태를 업데이트할 수 있는 사용자를 제어합니다. 이 권한이 있으면 다음을 수행할 수 있습니다:

- Canvas를 직접 승인
- Canvas를 승인하고 시작
- Canvas를 승인하되 시작하지 않음("Send Campaigns, Canvases" 권한을 가진 다른 사용자가 Canvas를 시작할 수 있음)
- Canvas를 승인하지도 시작하지도 않음

**Summary** 단계에서 승인 상태가 설정된 후, Canvas에 대한 후속 변경 사항은 저장 시 모든 승인 상태를 초기화합니다. 이는 초안 Canvas이든 시작 후 Canvas이든 관계없이 적용됩니다. 예를 들어, 타겟 오디언스만 변경하더라도 **Summary** 단계에서 모든 섹션의 승인 상태가 기본 상태인 **Pending Approval**로 되돌아갑니다.

{% alert note %}
**승인 상태와 저장**

- **Summary** 단계에서 섹션에 대해 **Approve**를 클릭하면 해당 승인이 즉시 저장됩니다.
- **Save** 버튼은 Canvas 콘텐츠와 설정의 변경 사항을 저장하며, 승인 상태는 저장하지 않습니다.

승인이 손실되지 않도록 하려면:

1. 필요한 Canvas 편집을 수행한 다음 **Save**를 클릭합니다.
2. Canvas 저장이 완료된 후, **Summary** 단계에서 관련 섹션을 승인합니다.
3. 승인 후 추가적인 Canvas 변경 사항이 있는 경우에만 **Save**를 다시 클릭합니다. Canvas를 변경하고 저장하면 모든 승인 상태가 **Pending Approval**로 초기화됩니다.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
라이브 Campaign을 편집하려면 "Approve and Deny Campaigns" 권한이 필요합니다. Campaigns의 초안 버전은 아직 사용할 수 없으므로 사용자가 자신의 변경 사항을 직접 승인해야 합니다. Canvases의 경우에는 사용자가 변경 사항을 적용하고 초안으로 저장한 후, 다른 사용자가 승인하고 Canvas를 시작할 수 있으므로 이에 해당하지 않습니다.
{% endalert %}