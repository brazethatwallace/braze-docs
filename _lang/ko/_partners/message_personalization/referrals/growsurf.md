---
date_published: "2026-09-08"
nav_title: GrowSurf
article_title: GrowSurf
description: "이 참조 문서에서는 추천 및 제휴 프로그램 플랫폼인 GrowSurf와 Braze 간의 파트너십에 대해 설명합니다. GrowSurf는 참가자 데이터를 Braze에 동기화하여 세분화 및 Liquid 개인화에 활용할 수 있도록 합니다."
alias: /partners/growsurf/
page_type: partner
search_tag: Partner
---

# GrowSurf

> [GrowSurf](https://www.growsurf.com/)는 추천 프로그램 및 제휴 프로그램 참가자 데이터를 Braze 고객 프로필로 전송합니다. 이 통합은 추천 링크, 참가자 세부 정보, 추천 횟수, 초대 횟수, 노출 횟수, 마일스톤 진행 상황을 커스텀 속성으로 추가하여 Braze 세분화 및 Liquid 개인화에 활용할 수 있습니다.

_이 통합은 GrowSurf에서 관리합니다._

## 통합 소개 {#about-the-integration}

GrowSurf는 추천 및 제휴 프로그램 소프트웨어입니다. 이 단방향 통합은 GrowSurf 참가자 추천 데이터를 Braze에서 사용할 수 있도록 유지하여, 참가자를 세분화하고, 추천 링크 및 진행 상황으로 메시지를 개인화하며, Braze에서 시의적절한 프로그램 커뮤니케이션을 발송할 수 있게 합니다.

## 사용 사례 {#use-cases}

- 각 참가자의 추천 링크를 Braze 메시지에 추가합니다.
- 추천 상태, 추천 횟수, 마일스톤 진행 상황을 기반으로 Segment를 구축합니다.
- 참가자 및 추천인 속성으로 Campaigns와 Canvases를 개인화합니다.

## 전제 조건 {#prerequisites}

시작하기 전에 다음 항목이 필요합니다.

| 전제 조건 | 설명 |
| --- | --- |
| GrowSurf 계정 | 이 통합에는 GrowSurf 유료 플랜이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. Braze 대시보드에서 **설정** > **API 및 식별자** > **API 키**로 이동하여 이 키를 생성합니다. 자세한 내용은 [REST API 키 생성]({{site.baseurl}}/api/basics#creating-rest-api-keys)을 참조하세요. |
| Braze REST 엔드포인트 | Braze REST 엔드포인트 URL(예: `https://rest.iad-01.braze.com`). 자세한 내용은 [REST API 엔드포인트]({{site.baseurl}}/api/basics#endpoints)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

다음 단계에 따라 GrowSurf 프로그램을 Braze에 연결합니다. 단계별 지침은 [GrowSurf Braze 통합 설명서](https://docs.growsurf.com/integrations/braze)를 참조하세요.

### 1단계: Braze REST API 키 생성 {#step-1-create-a-braze-rest-api-key}

1. Braze에서 **설정** > **API 및 식별자** > **API 키**로 이동합니다.
2. `users.track` 권한이 있는 REST API 키를 생성합니다.
3. API 키를 복사하고 동일한 Braze 워크스페이스에 해당하는 REST 엔드포인트를 메모합니다.

### 2단계: GrowSurf에서 Braze 연결 {#step-2-connect-braze-in-growsurf}

1. GrowSurf에서 **Program Editor** > **4. Options** > **Integrations** > **Braze**로 이동합니다.
2. 일치하는 Braze REST 엔드포인트를 선택합니다.
3. REST API 키를 입력하고 **Submit**을 선택합니다.

### 3단계: 첫 번째 참가자 동기화 확인 {#step-3-verify-the-first-participant-sync}

1. GrowSurf에서 테스트 참가자를 추가하거나 업데이트합니다.
2. Braze에서 **오디언스** > **사용자 검색**으로 이동하여 이메일로 검색해 일치하는 고객 프로필을 엽니다.
3. `grsf_` 커스텀 속성이 프로필에 표시되는지 확인합니다.

## Braze의 GrowSurf 속성 {#growsurf-attributes-in-braze}

GrowSurf는 15개의 추천 속성을 Braze에서 사용할 수 있도록 합니다. 첫 번째 동기화에서 전체 세트가 전송됩니다. 이후에는 참가자 데이터가 변경될 때 GrowSurf가 업데이트를 전송합니다. GrowSurf에서 값이 제거되면 해당 Braze 속성도 함께 삭제됩니다. 횟수 값은 숫자로 전송됩니다.

### 문자열 속성 {#string-attributes}

| 커스텀 속성 | 설명 |
| --- | --- |
| `grsf_share_url` | 참가자의 추천 공유 URL입니다. |
| `grsf_participant_id` | 참가자의 GrowSurf ID입니다. |
| `grsf_referral_status` | 참가자의 추천 상태입니다. |
| `grsf_participant_first_name` | 참가자의 이름입니다. |
| `grsf_participant_last_name` | 참가자의 성입니다. |
| `grsf_referrer_first_name` | 추천인의 이름입니다. |
| `grsf_referrer_last_name` | 추천인의 성입니다. |
| `grsf_referrer_email` | 추천인의 이메일 주소입니다. |
| `grsf_next_milestone` | 참가자가 달성하려는 다음 마일스톤입니다. |
| `grsf_next_monthly_milestone` | 참가자가 달성하려는 다음 월간 마일스톤입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="문자열 속성" }

### 숫자 속성 {#number-attributes}

| 커스텀 속성 | 설명 |
| --- | --- |
| `grsf_total_referral_count` | 참가자의 총 추천 횟수입니다. |
| `grsf_monthly_referral_count` | 참가자의 이번 달 추천 횟수입니다. |
| `grsf_prev_monthly_referral_count` | 참가자의 지난달 추천 횟수입니다. |
| `grsf_total_invite_count` | 참가자의 총 초대 횟수입니다. |
| `grsf_total_impression_count` | 참가자의 총 추천 링크 노출 횟수입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="숫자 속성" }

## Braze에서 GrowSurf 활용 {#use-growsurf-with-braze}

GrowSurf 추천 속성을 Braze 세분화 및 Liquid 개인화에 활용합니다. GrowSurf는 참가자가 추가되거나 추천 데이터가 변경될 때 이러한 속성을 업데이트합니다. 이미 프로그램에 있는 참가자도 동기화할 수 있습니다.

### 1단계: Segment 구축 {#step-1-build-segments}

1. Braze에서 관련 `grsf_` 커스텀 속성으로 Segment를 생성합니다.
2. 추천 상태, 추천 횟수 또는 마일스톤 진행 상황을 기준으로 참가자를 타겟팅하거나 제외합니다.

### 2단계: 메시지 개인화 {#step-2-personalize-messages}

1. `grsf_share_url` 커스텀 속성을 Liquid를 사용하여 Braze 메시지에 추가합니다: {% raw %}`{{custom_attribute.${grsf_share_url}}}`{% endraw %}.

{: start="2"}
2. 기타 `grsf_` 속성을 사용하여 추천 상태, 횟수 및 마일스톤 진행 상황을 개인화합니다.

## 고려 사항 {#considerations}

- GrowSurf는 커스텀 속성만 전송합니다. 커스텀 이벤트, 구매 또는 가입 변경 사항은 전송하지 않습니다.
- GrowSurf는 참가자 이메일을 기준으로 Braze 프로필을 식별합니다. 일치하는 프로필이 없으면 Braze가 이메일 전용 프로필을 생성합니다.
- 동일한 이메일이 둘 이상의 연결된 GrowSurf 프로그램에 속한 경우, 가장 최근에 동기화된 프로그램 데이터가 해당 Braze 프로필에 표시됩니다.
- 참가자를 가져오기 전에 Braze를 연결하세요. 기존 참가자를 동기화하려면 GrowSurf의 기존 참가자 동기화 옵션을 사용하세요.

## 문제 해결 {#troubleshooting}

- Braze REST API 키에 `users.track` 권한이 있고, 선택한 REST 엔드포인트가 동일한 Braze 워크스페이스에 속하는지 확인합니다.
- 참가자 한 명이 동기화에 실패하면 해당 참가자에게 유효한 이메일 주소가 있는지 확인합니다.
- 참가자의 GrowSurf 활동 로그에서 동기화 결과를 확인합니다.
- GrowSurf는 일시적인 Braze 오류를 자동으로 재시도합니다. GrowSurf가 업데이트를 확인할 수 없는 경우, 해당 Braze 프로필이 다음에 동기화될 때 모든 추천 속성을 전송합니다. API 키 또는 REST 엔드포인트가 유효하지 않으면 설정을 수정하고 통합을 다시 연결합니다.

자세한 문제 해결 방법은 [GrowSurf Braze 통합 설명서](https://docs.growsurf.com/integrations/braze#troubleshooting)를 참조하세요.