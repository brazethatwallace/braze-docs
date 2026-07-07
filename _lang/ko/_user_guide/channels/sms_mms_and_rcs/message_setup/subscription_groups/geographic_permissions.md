---
nav_title: "지리적 권한"
article_title: "지리적 권한"
description: "이 문서에서는 지리적 권한의 국가 허용 목록에 대해 다룹니다. 이를 통해 SMS, MMS, RCS를 전달할 수 있는 국가를 선택할 수 있습니다."
page_order: 0
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# 지리적 권한 {#geographic-permissions}

> 지리적 권한은 메시지를 보낼 수 있는 국가에 대한 제어를 적용하여 보안을 강화하고 사기성 SMS, MMS, RCS 트래픽으로부터 보호합니다. 국가 허용 목록을 지정하여 SMS, MMS, RCS 메시지가 승인된 지역으로만 전송되도록 할 수 있습니다. 메시지는 해당 국가의 다이얼링 코드가 포함된 전화번호로만 전송됩니다.<br><br> 관리자만 국가 허용 목록을 변경할 수 있습니다. 관리자가 아닌 사용자는 구독 그룹이 전송할 수 있는 국가를 나타내는 읽기 전용 버전의 허용 목록에 접근할 수 있습니다.

관리자인 경우 허용 목록에 포함할 국가를 구성할 수 있습니다. 국가 허용 목록은 [구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups) 수준에서 구성됩니다. **오디언스** > **구독 그룹 관리**로 이동한 후 SMS, MMS 또는 RCS 구독 그룹을 선택하여 접근할 수 있습니다. 허용 목록은 **Geographic Permissions** 아래에 있습니다.

![관리자용 편집 가능한 지리적 권한 섹션으로, "Country allowlist"에 여러 국가가 선택되어 있습니다.]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

## 국가 선택 {#selecting-countries}

드롭다운을 사용하여 허용 목록에 국가를 추가합니다. 가장 일반적인 SMS, MMS, RCS 국가가 상단에 표시되며, 나머지는 아래에 표시됩니다. 텍스트 필드에 입력하여 국가를 검색할 수도 있습니다.

!["Country allowlist" 드롭다운으로, 가장 일반적인 국가가 상단에 표시됩니다.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

이전에 선택한 국가를 제거하려면 해당 국가 옆의 체크박스를 해제합니다.

### 변경 사항 저장 {#saving-your-changes}

저장하면 변경 사항이 적용됩니다. 허용 목록에서 국가를 제거하면 해당 국가의 다이얼링 코드가 포함된 전화번호로의 모든 SMS, MMS, RCS 메시지 전송이 차단됩니다.

![허용 목록에서 삭제될 국가를 확인하는 경고 모달.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## 높은 사기 위험 국가 {#high-fraud-risk-countries}

특정 국가는 SMS, MMS, RCS 트래픽 펌핑 위험이 더 높습니다. 이러한 국가는 국가 드롭다운에서 **High Fraud Risk** 태그로 표시됩니다.

![아제르바이잔에 "High Fraud Risk" 태그가 있는 국가 드롭다운.]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

이러한 국가에서의 전송을 허용하려면 먼저 해당 위험을 인지해야 하며, 그 후에 국가가 허용 목록에 추가됩니다.

{% alert note %}
허용 목록의 국가를 비즈니스 요구 사항을 지원하는 데 필요한 국가로만 제한하세요. 이렇게 하면 사기성 트래픽의 가능성을 최소화할 수 있습니다. SMS, MMS, RCS 트래픽 펌핑 방지에 대한 자세한 안내는 [SMS 트래픽 펌핑 사기 FAQ]({{site.baseurl}}/sms_traffic_pumping_fraud)를 참조하세요.
{% endalert %}

## 허용 목록 외 전송의 가시성 {#visibility-of-sends-outside-the-allowlist}

국가 허용 목록에 없는 국가로의 전송 시도는 중단됩니다. 중단된 메시지는 [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) 및 [SMS 중단 메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)에 기록됩니다.

허용 목록에 없는 국가의 수신자에 대해 중단된 메시지는 **Aborted Message Errors**로 표시되며 "The recipient's phone number is in a blocked country"라는 메시지가 포함됩니다.

![전화번호의 국가가 국가 허용 목록에 없어 중단된 여러 SMS, MMS, RCS 전송을 보여주는 중단 로그.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

## 높은 사기 위험 국가 및 트래픽 펌핑 사기에 대한 중요 안내 {#important-notice-for-high-fraud-risk-countries-and-traffic-pumping-fraud}

### SMS, MMS, RCS 트래픽 펌핑이란? {#what-is-sms-mms-and-rcs-traffic-pumping}

SMS, MMS, RCS 트래픽 펌핑(인위적으로 부풀린 트래픽이라고도 함)은 고객에게 상당한 재정적 노출을 초래할 수 있는 증가하는 사기 수법입니다. 사기범은 보호되지 않은 공개 웹 양식, 인증 흐름 또는 API 엔드포인트를 악용하여 자신이 통제하거나 영향력을 행사하는 전화번호로 대량의 SMS, MMS, RCS 전송(옵트인 확인, 일회용 비밀번호 또는 알림 등)을 트리거할 수 있습니다. 그런 다음 공격자는 해당 인위적 트래픽을 생성한 대가로 공모하거나 인지하지 못하는 모바일 네트워크로부터 수익 분배를 받습니다. 이로 인한 후속 영향은 상당한 재정적 노출을 초래합니다.

### 높은 사기 위험 국가란? {#what-are-high-fraud-risk-countries}

국가 또는 지역이 높은 사기 위험으로 지정되는 경우는 비정상적으로 높은 밀도의 소규모 프리미엄 요금 로컬 로밍 통신사가 있거나 엄격한 규제 감독이 부족한 경우입니다. 악의적 행위자는 메시지당 수익 분배 지급을 극대화하기 위해 이러한 고요금 통신사 네트워크를 체계적으로 타겟팅합니다.

또한 시스템 라우팅 제한은 수신자의 실제 물리적 위치가 아닌 대상 국가 코드를 기반으로 적용됩니다. 즉, 자주 여행하는 고객이 있는 경우 여행 위치를 국가 허용 목록에 추가할 필요가 없습니다. 메시징은 현재 물리적 위치가 아닌 원래 대상 국가 코드를 기반으로 라우팅되기 때문입니다. 예를 들어, 저위험 지역과 국가 코드를 공유하는 지역(예: 영국과 +44 국가 코드를 공유하는 저지 또는 건지)은 여전히 높은 통신사 요금 노출을 가지며 동일한 높은 사기 위험 프레임워크 조건에서 관리됩니다.

### 고객 책임 및 재정적 의무 {#customer-responsibility-and-financial-liability}

고객은 SMS, MMS, RCS 트래픽 펌핑으로 인한 메시지를 포함하여 서비스를 통해 자신을 대신하여 전송된 모든 모바일 메시지에 대해 책임을 지며 청구됩니다. 국가 허용 목록과 같은 플랫폼 보호 장치는 신뢰할 수 있는 지역으로의 전달을 제한하는 데 도움이 됩니다. 그러나 궁극적으로 외부 대면 엔드포인트를 보호하고 심각한 재정적 피해를 방지하는 것은 전적으로 고객의 책임입니다.

### 트래픽 펌핑 방지 방법 {#how-to-prevent-traffic-pumping}

실제 고객이 거주하는 지리적 지역으로 메시지 배포를 엄격히 제한하지 않으면 사기 및 심각한 재정적 피해에 즉각적으로 취약해집니다. 회사를 보호하려면 국가 허용 목록을 사용하여 전달 지역을 사전에 제한해야 합니다. 또한 가장 중요한 것은 [SMS, MMS, RCS 트래픽 펌핑 사기 이해 및 방지]({{site.baseurl}}/sms_traffic_pumping_fraud)에 설명된 업계 모범 사례에 따라 SMS, MMS, RCS 전송을 트리거하는 온라인 전화번호 요청 양식 또는 API 엔드포인트를 보호해야 합니다.