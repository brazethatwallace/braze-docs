---
nav_title: "지리적 권한"
article_title: "지리적 권한"
description: "이 문서에서는 지리적 권한의 국가 허용 목록에 대해 다룹니다. 이를 통해 SMS, MMS, RCS를 전달할 수 있는 국가를 선택할 수 있습니다."
page_order: 4
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# 지리적 권한 {#geographic-permissions}

> 지리적 권한은 메시지를 보낼 수 있는 국가에 대한 제어를 적용하여 보안을 강화하고 사기성 SMS, MMS, RCS 트래픽으로부터 보호합니다. 국가 허용 목록을 지정하여 SMS, MMS, RCS 메시지가 승인된 지역으로만 전송되도록 할 수 있습니다. 관리자만 국가 허용 목록을 변경할 수 있습니다. 관리자가 아닌 사용자는 구독 그룹이 전송할 수 있는 국가를 나타내는 읽기 전용 버전의 허용 목록에 접근할 수 있습니다.

관리자인 경우 허용 목록에 포함할 국가를 구성할 수 있습니다. 국가 허용 목록은 [구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups/) 수준에서 구성됩니다. **오디언스** > **구독**으로 이동한 후 SMS, MMS 또는 RCS 구독 그룹을 선택하여 접근할 수 있습니다. 허용 목록은 **Geographic Permissions** 아래에 있습니다.

![관리자용 편집 가능한 SMS 지리적 권한 섹션으로, "Country allowlist"에 여러 국가가 선택되어 있습니다.]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### 국가 선택 {#selecting-countries}

드롭다운을 사용하여 허용 목록에 국가를 추가합니다. 가장 일반적인 SMS 및 RCS 국가가 상단에 표시되며, 나머지는 아래에 표시됩니다. 텍스트 필드에 입력하여 국가를 검색할 수도 있습니다.

!["Country allowlist" 드롭다운으로, 가장 일반적인 국가가 상단에 표시됩니다.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

이전에 선택한 국가를 제거하려면 해당 국가 옆의 체크박스를 해제합니다.

### 변경 사항 저장 {#saving-your-changes}

**Save**를 선택하면 변경 사항이 적용됩니다. 허용 목록에서 국가를 제거하면 해당 국가의 번호로 모든 SMS, MMS, RCS 메시지 전송이 차단됩니다.

![허용 목록에서 삭제될 국가를 확인하는 경고 모달.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## 높은 위험도 국가 {#high-risk-countries}

특정 국가는 SMS 및 RCS 트래픽 펌핑 위험이 더 높습니다. 이러한 국가는 국가 드롭다운에서 **High Risk** 태그로 표시됩니다.

![아제르바이잔에 "High Risk" 태그가 있는 국가 드롭다운.]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

이러한 국가로의 전송을 허용하는 경우, 해당 국가가 허용 목록에 추가되기 전에 먼저 위험을 인지해야 합니다.

{% alert note %}
허용 목록의 국가를 비즈니스 요구 사항을 지원하는 데 필요한 국가로만 제한하세요. 이렇게 하면 사기성 트래픽의 가능성을 최소화할 수 있습니다. SMS 트래픽 펌핑 방지에 대한 자세한 안내는 [SMS 트래픽 펌핑 사기 FAQ]({{site.baseurl}}/sms_traffic_pumping_fraud/)를 참조하세요.
{% endalert %}

## 차단된 전송의 가시성 {#visibility-of-blocked-sends}

허용 목록에 없는 국가로의 전송 시도는 중단됩니다. 중단된 메시지는 [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) 및 [SMS 중단 메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)에 기록됩니다.

차단된 전송으로 인해 중단된 메시지는 **Aborted Message Errors**로 표시되며 "The recipient's phone number is in a blocked country"라는 메시지가 포함됩니다.

![전화번호가 차단된 국가에 있어 차단된 여러 SMS 전송을 보여주는 중단 로그.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}