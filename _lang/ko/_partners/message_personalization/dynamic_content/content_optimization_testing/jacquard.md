---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "이 참조 문서에서는 웹훅을 통해 가입자의 클릭 추적 정보를 수집하기 위해 Braze 커런츠와 연결된 콘텐츠를 사용하는 Braze와 Jacquard Dynamic Optimisation의 파트너십에 대해 설명합니다. 그런 다음 Jacquard는 해당 이벤트를 언어 배리언트에 연결하여 실시간 언어 최적화를 수행합니다."
page_type: partner
search_tag: Partner
---

# Jacquard Dynamic Optimisation

> [Jacquard](https://www.jacquard.com/)는 인공지능, 전산 언어학, 고객 중심 정신을 결합하여 브랜드 보이스에 맞게 커스텀된 채널 전반에 걸쳐 브랜드 언어를 대규모로 배포할 수 있도록 지원합니다.

Jacquard X에서 제공하는 Dynamic Optimisation은 Braze 커런츠와 연결된 콘텐츠를 사용하여 웹훅을 통해 가입자로부터 클릭 추적 정보를 수집합니다. 그런 다음 Jacquard는 해당 이벤트를 언어 배리언트에 연결하여 실시간 언어 최적화를 수행합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Jacquard 계정 | 이 파트너십을 활용하려면 [Jacquard 계정](https://www.jacquard.com/)이 필요합니다. |
| Jacquard 연결 서버 토큰 | Braze Campaign의 비밀번호 역할을 하여 Jacquard 언어에 접근할 수 있게 해주는 긴 문자열입니다.<br><br>아직 제공받지 못한 경우 Jacquard 고객 성공 매니저에게 요청할 수 있습니다. |
| Currents | 데이터를 Currents로 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Jacquard Amazon S3 자격 증명 요청 {#step-1-request-jacquard-amazon-s3-credentials}

Braze에서 클릭 추적 이벤트를 수신하기 위해 Jacquard에서 전용 Amazon S3 버킷을 설정해야 합니다. 이 프로세스를 시작하려면 Jacquard 고객 성공 매니저에게 문의하세요. 버킷이 생성되면 Currents를 만들기 위한 고유 자격 증명이 제공됩니다.

### 2단계: Currents 생성 {#step-2-create-current}

1. Braze에서 **Currents > Create New Current > Amazon S3 Data Export**를 선택합니다.
2. 다음으로, Currents의 이름을 지정하고 연락처 이메일을 입력합니다.
3. 자격 증명 상자에 Jacquard AWS 액세스 키 ID와 시크릿 액세스 키를 추가합니다. 그런 다음 AWS S3 버킷 이름으로 "phrasee-braze-currents-exports"를 추가합니다.
4. 마지막으로, Jacquard 고객 성공 매니저로부터 받은 AWS S3 버킷 폴더를 추가합니다. 일반적으로 회사 이름일 것입니다.
5. **General Settings**에서 "Include events from anonymous users" 상자를 체크하고, **Manage Engagement Events**에서 "Email Click"을 체크합니다.
6. 완료되면 **Launch Current**를 선택합니다.

### 3단계: 개인 식별 정보(PII) 제거 요청 {#step-3-request-to-remove-personally-identifiable-information-pii}

다음으로, Braze 계정 팀에 연락하여 개인 식별 정보가 Jacquard에 전송되지 않도록 하세요.

기본적으로 Currents에는 이메일 및 주소와 같은 특정 PII 속성이 포함됩니다. Jacquard는 PII를 수신할 수 없으며 수신하지 않으므로, Jacquard로 전달되는 모든 이벤트 데이터에 대해 이 기능을 비활성화하도록 Braze 계정 팀에 요청하는 것이 중요합니다.

### 4단계: Jacquard X 코드 스니펫 {#step-4-jacquard-x-code-snippets}

필요한 코드 스니펫은 Jacquard 계정 팀에 문의하세요.

이러한 스니펫은 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)를 사용하며, 이메일에 배치된 후에는 언어와 추적 픽셀을 동적으로 가져와서 Jacquard X를 사용하여 실시간으로 언어를 최적화할 수 있습니다.