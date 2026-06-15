---
nav_title: actionable.me
article_title: actionable.me
description: "이 참조 문서에서는 Braze와 actionable.me 간의 파트너십을 설명합니다. actionable.me는 독자적인 소프트웨어와 프로세스를 통해 Braze 투자를 즉시 최대한 활용할 수 있도록 지원합니다."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me)는 데이터 및 CRM 에이전시인 Massive Rocket 팀이 구축한 솔루션으로, CRM 프로그램 운영을 위한 표준화되고 자동화된 접근 방식을 제공합니다. Braze 고객이 빠르고 일관되며 예측 가능하게 가치를 실현할 수 있도록 설계된 도구와 프로세스를 제공합니다.

_이 통합은 actionable.me에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 actionable.me 통합을 통해 Braze 활용 진행 상황을 모니터링하는 서비스를 배포할 수 있습니다. 도구와 프로세스의 조합을 통해 CRM 성과를 신속하게 벤치마킹하고, 새로운 기회를 발견하며, 더 나은 성과를 위한 추천 사항을 제공합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| actionable.me 계정 | 이 파트너십을 활용하려면 actionable.me 계정이 필요합니다. |
| Braze REST API 키 | 다음 섹션에 나열된 권한이 포함된 Braze REST API 키.<br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

Braze와 actionable.me를 통합하려면 actionable.me 플랫폼을 구성하고, Braze에서 Braze API 키를 생성한 후 actionable.me 대시보드에서 구성해야 합니다.

### 1단계: Braze API 키 생성 {#step-1-create-your-braze-api-key}

Braze에서 **설정** > **API 키**로 이동합니다. **Create New API Key**를 선택하고 다음 권한이 추가되었는지 확인합니다:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### 2단계: actionable.me 팀에 정보 제공 {#step-2-provide-information-to-the-actionableme-team}

통합을 완료하려면 REST API 키와 [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)을 actionable.me 운영팀에 제공해야 합니다. 그러면 actionable.me에서 연결을 설정하고 설정이 완료된 후 연락하여 인사이트 공유를 시작할 수 있도록 안내합니다.

![actionable.me 운영팀에서 구성할 actionable.me "add platform" 페이지입니다.]({% image_buster /assets/img/actionableme/image2.png %})

## 문제 해결 {#troubleshooting}

추가 지원이 필요하면 actionable.me 또는 Massive Rocket 팀에 문의하세요: [info@massiverocket.com](mailto:info@massiverocket.com)