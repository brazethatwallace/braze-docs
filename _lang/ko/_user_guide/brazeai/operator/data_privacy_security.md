---
nav_title: 데이터 프라이버시 및 보안
article_title: BrazeAI Operator의 데이터 프라이버시 및 보안
page_order: 5
page_type: reference
description: "이 참조 문서에서는 HIPAA 준수, 데이터 보존, PII 최소화, 거버넌스를 포함하여 BrazeAI Operator가 데이터를 처리하는 방법을 다룹니다."
---

# BrazeAI Operator의 데이터 프라이버시 및 보안 {#data-privacy-and-security-for-brazeai-operator}

> BrazeAI Operator<sup>TM</sup>는 OpenAI와 통합되어 AI 기반 지원을 제공합니다. 이 문서에서는 Operator가 데이터를 처리하는 방법, OpenAI와 공유되는 정보, PII 노출을 최소화하고 접근을 제어하는 방법을 다룹니다.

## Operator가 데이터에 접근하는 방법 {#how-operator-accesses-data}

Operator의 고객 데이터 접근은 영구적이지 않으며, 엄격하게 이벤트 기반 및 호출 범위로 제한됩니다. Operator가 열려 있는 동안 각 사용자 메시지 또는 탐색 이벤트는 OpenAI에 대한 개별 HTTP 요청을 트리거합니다. 상시 연결이나 영구 데이터 피드는 없습니다.

OpenAI는 Braze 데이터 저장소나 전체 사용자 테이블에 직접 접근할 수 없습니다. LLM은 활성 요청과 관련된 특정 페이로드만 수신합니다.

### 각 요청에 포함되는 데이터 {#what-data-is-included-in-each-request}

OpenAI로 전송되는 각 요청 페이로드에는 다음이 포함될 수 있습니다:

- **시스템 메타데이터:** Braze가 작성한 시스템 프롬프트 및 도구 스키마(LLM이 호출할 수 있는 도구의 정의).
- **대시보드 사용자 메시지:** 대시보드 사용자가 입력한 텍스트.
- **도구 출력:** 이름, ID 및 관련 데이터를 포함하는 검색 결과.
- **스크래핑된 페이지 콘텐츠:** 활성 대시보드 페이지의 콘텐츠로, 약 4,000자로 잘립니다.
- **페이지 컨텍스트 문자열:** 활성 대시보드 페이지의 상황별 문자열.

## 데이터 하위 처리자 {#data-sub-processors}

### 하위 처리자 또는 서드파티 제공자로서의 모델 제공자 {#model-providers-as-sub-processors-or-third-party-providers}

Braze 서비스를 통해 Braze가 제공하는 LLM 제공자와의 통합("Braze 제공 LLM")을 사용하는 경우, 해당 Braze 제공 LLM의 제공자는 귀하와 Braze 간의 데이터 처리 부록(DPA) 조건에 따라 Braze 하위 처리자로 활동합니다. BrazeAI Operator<sup>TM</sup>는 OpenAI와 통합됩니다.

### OpenAI에서 데이터가 사용되는 방식 {#how-data-is-used-with-openai}

OpenAI를 활용하는 BrazeAI 기능을 통해 AI 출력("출력")을 생성하기 위해, Braze는 특정 정보("입력")를 OpenAI에 전송합니다. 입력은 프롬프트, 대시보드에 표시되는 콘텐츠, 쿼리와 관련된 워크스페이스 데이터로 구성됩니다. [OpenAI의 API 플랫폼 약속](https://openai.com/enterprise-privacy/)에 따라, Braze를 통해 OpenAI의 API로 전송된 데이터는 OpenAI 모델을 학습하거나 개선하는 데 사용되지 않습니다. 귀하와 Braze 간에 출력은 귀하의 지적 재산입니다. Braze는 해당 출력에 대한 저작권 소유권을 주장하지 않습니다. Braze는 출력을 포함한 AI 생성 콘텐츠에 대해 어떠한 종류의 보증도 하지 않습니다.

## HIPAA 준수 및 데이터 보존 {#hipaa-compliance-and-data-retention}

### HIPAA 준수 {#hipaa-compliance}

Braze의 US-02 클러스터를 사용하는 경우, Operator는 Braze의 비즈니스 제휴 계약(BAA)에 의해 보호되며, HIPAA 요구 사항에 따라 개인 건강 정보(PHI)를 해당 기능에 제출할 수 있습니다. 다른 Braze 클러스터에서 Operator를 사용할 때는 HIPAA 적용 대상인 PHI를 제출하지 마세요.

### PII 수정 {#pii-redaction}

Operator 요청 파이프라인에는 자동화된 PII 수정 레이어가 없습니다. 데이터는 완전히 원시 상태로 전송되며, OpenAI로 전송되기 전에 익명화되지 않습니다. 접근은 활성 대시보드 페이지 또는 대시보드 사용자의 입력으로 범위가 제한되지만, 전송 전에 콘텐츠 필터링은 적용되지 않습니다.

### OpenAI 데이터 보존 {#openai-data-retention}

Operator를 통해 전송된 데이터를 OpenAI가 보존하는 기간은 클러스터에 따라 다릅니다:

| 클러스터 | 보존 기간 |
| --- | --- |
| US-02 (HIPAA 고객) | 제로 데이터 보존(ZDR). 처리 후 OpenAI에 의해 데이터가 저장되지 않습니다. |
| 기타 모든 클러스터 | 남용 모니터링을 위해 30일. 이는 OpenAI가 적용하는 업계 표준 보존 기간입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="클러스터별 OpenAI 데이터 보존" }

### 모델 학습 {#model-training}

Braze를 통해 OpenAI의 API로 전송된 데이터는 OpenAI 모델을 학습하거나 개선하는 데 사용되지 않습니다. 이는 Braze와 OpenAI 간의 계약 및 OpenAI의 API 플랫폼 약속에 의해 규율됩니다. OpenAI는 Braze 하위 처리자로 활동하며, 모든 개인 데이터는 Braze와 클라이언트 간의 DPA에 따릅니다.

### EU 데이터 라우팅 {#eu-data-routing}

현재 Operator에 대한 EU 데이터 라우팅은 구현되어 있지 않으며, 이를 구현할 현재 계획도 없습니다.

## PII 노출 최소화 {#minimize-pii-exposure}

Operator를 사용할 때 PII 노출을 제한하기 위해 취할 수 있는 몇 가지 단계가 있습니다:

- Operator를 사용하는 모든 사용자에 대해 **PII 보기 설정을 비활성화**하세요. 사용자가 PII를 볼 수 없으면 Operator도 접근할 수 없습니다.
- **고객 프로필 페이지에서 Operator를 열지 마세요.** 페이지 콘텐츠가 스크래핑되어 OpenAI로 전송되는 각 요청에 포함됩니다.
- **테스트할 때는 기존 프로필을 선택하는 대신 커스텀 고객 프로필을 사용하세요.** 이것이 Operator의 기본 동작입니다.
- Operator 프롬프트에 **PII를 직접 입력하거나 붙여넣지 마세요.**
- Operator가 접근하고 실행할 수 있는 항목을 제어하기 위해 **동작 자동 승인을 비활성화**하세요.
- Segment를 구축하거나 Liquid를 작성할 때 **Operator에게 속성의 미리보기 값을 표시하도록 요청하지 마세요.**

## 거버넌스 및 접근 제어 {#governance-and-access-control}

### Operator에 대한 접근 제한 {#restrict-access-to-operator}

Operator에 대한 접근은 [세분화된 사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)을 통해 워크스페이스 수준에서 관리됩니다. 관리자는 개별 사용자에 대해 **BrazeAI Operator 사용** 권한을 부여하거나 취소하여 승인된 인원만 도구와 상호작용할 수 있도록 할 수 있습니다. 이러한 특정 권한이 없으면 Operator 인터페이스가 완전히 숨겨지고 백엔드 엔드포인트도 보안이 유지됩니다.

### 휴먼 인 더 루프 모델 {#human-in-the-loop-model}

기본적으로 Operator는 변경 사항을 커밋하기 전에 명시적 승인을 요구합니다. 제안된 수정 사항은 검토를 위해 [동작 카드]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/)로 표시됩니다. 사용자가 제안을 거부하면 변경 사항이 발생하지 않습니다. 사용자가 제안을 수락하면 대시보드가 업데이트되지만, 변경 사항은 보류 상태로 유지되며 영구적으로 적용되려면 수동으로 저장하거나 시작해야 합니다.

사용자는 Operator 채팅 패널에서 **동작 자동 승인**을 활성화할 수 있으며, 이 경우 제안된 동작이 수동 검토 없이 즉시 실행됩니다. 자동 승인이 활성화된 경우에도 이미지 생성 및 워크스페이스 수준 설정 수정을 포함하여 일부 동작은 안전을 위해 항상 명시적 승인이 필요합니다.

### 사용자 권한 상속 {#user-permission-inheritance}

Operator는 로그인한 사용자의 권한 프로필을 완전히 상속합니다. 사용자가 독립적으로 수행할 권한이 없는 데이터 보기 또는 Campaign 수정과 같은 동작은 실행이 제한됩니다.

### 팀 사용 감사 {#audit-team-usage}

팀 사용을 모니터링하려면 Braze의 [보안 이벤트 보고서]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report)를 다운로드하세요. "Requested BrazeAI Operator Response" 이벤트는 포괄적인 감사 추적을 제공하여 Operator에 제공된 정확한 입력을 검토할 수 있게 합니다.