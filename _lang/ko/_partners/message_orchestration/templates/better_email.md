---
nav_title: Better Email
article_title: Better Email
alias: /partners/better_email/
description: "이 참조 문서에서는 Braze와 Better Email 간의 파트너십에 대해 설명합니다. Better Email은 이메일 디자인 시스템을 기반으로 구축된 협업 이메일 제작 플랫폼으로, 프로덕션 준비가 완료된 템플릿을 Braze로 내보낼 수 있습니다."
page_type: partner
search_tag: Partner
---

# Better Email

> [Better Email](https://better.email)은 이메일 디자인 시스템을 기반으로 구축된 협업 이메일 제작 플랫폼입니다. 팀은 공유 블록 및 스타일 시스템에서 프로덕션 준비가 완료된 이메일을 디자인, 관리 및 내보내기할 수 있으며, 개발자나 에이전시에 의존하지 않고도 대규모로 브랜드 일관성을 유지할 수 있습니다.

_이 통합은 Better Email에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Better Email 통합을 사용하면 Better Email의 협업 편집기에서 이메일 템플릿을 생성 및 관리하고, 바로 사용할 수 있는 이메일 템플릿으로 Braze에 직접 내보낼 수 있습니다.

이메일을 다시 내보내면 중복을 생성하는 대신 기존 Braze 템플릿이 업데이트되므로 템플릿 라이브러리가 깔끔하게 유지됩니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Better Email 계정 | 통합을 생성할 수 있는 관리자 액세스 권한이 있는 Better Email 계정 |
| Braze REST API 키 | 전체 **템플릿** 권한이 있는 Braze REST API 키.<br><br>이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 대시보드 URL이 아닌 REST 호스트를 사용하세요. 예: `rest.fra-01.braze.eu`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 활용 사례 {#use-cases}

Better Email은 디자인 시스템을 통해 이메일을 관리하고 수동 HTML 작업 없이 Braze로 내보내려는 마케팅 팀을 위해 만들어졌습니다. 다음과 같은 경우 Better Email을 고려해 보세요:

- 대규모 이메일 템플릿 라이브러리를 유지 관리하면서 모든 템플릿의 일관성을 유지해야 하는 경우
- 공유 이메일 디자인 시스템을 통해 브랜드 가이드라인을 적용하려는 경우
- 디자이너, 마케터, 개발자 등 여러 팀이 이메일 제작에 협업하는 경우
- Campaign 실행에 Braze를 사용하면서 디자인과 배포 간의 핸드오프 병목 현상을 제거하려는 경우

## Better Email과 Braze 통합하기 {#integrate-better-email-with-braze}

### 1단계: Braze 값 확인하기 {#step-1-find-your-braze-values}

Braze 대시보드에서 다음 정보를 수집하세요:

- **인스턴스 URL** — 대시보드 URL이 아닌 REST 호스트를 사용하세요(예: `rest.fra-01.braze.eu`).
- **API 키** — **설정** > **API 키**에서 생성한 전체 **템플릿** 권한이 있는 REST API 키.

### 2단계: Better Email에서 통합 설정하기 {#step-2-set-up-the-integration-in-better-email}

1. **Integrations**로 이동합니다.
2. 새 통합을 생성합니다.
3. 통합 이름을 입력합니다(예: `Braze`).
4. 유형으로 **Braze**를 선택합니다.
5. 선택 사항으로, **Access**에서 특정 사용자 또는 그룹으로 통합을 제한할 수 있습니다.
6. **Save**를 선택합니다.
7. **Instance URL**과 **API Key**를 입력합니다.
8. 통합을 활성화합니다.
9. **Save**를 다시 선택합니다.

### 3단계: Braze로 내보내기 {#step-3-export-to-braze}

통합이 활성화되면 Better Email에서 이메일을 열고 **Export** > **Braze**를 선택합니다.

Better Email이 해당 Braze 이메일 템플릿을 생성하거나 업데이트합니다. 첫 번째 내보내기 후 Better Email은 Braze 템플릿 ID를 저장하므로, 동일한 이메일을 다시 내보내면 중복을 생성하는 대신 해당 템플릿이 업데이트됩니다.

### Braze에서 수신자 필드 동기화하기(선택 사항) {#sync-recipient-fields-from-braze-optional}

Better Email은 Braze 커스텀 속성을 동기화하여 병합 태그 및 세분화 필드로 사용할 수 있습니다.

1. Better Email에서 Braze 통합을 엽니다.
2. **Sync recipient fields**를 활성화합니다.
3. **Save**를 선택합니다.
4. **Recipient Fields**로 이동합니다.
5. 통합 옆의 **Sync from**을 선택합니다.

Better Email이 사용 가능한 Braze 커스텀 속성을 읽고 수신자 필드에 매핑합니다.

## 문제 해결 {#troubleshooting}

내보내기 또는 동기화가 실패하면 다음 사항을 확인하세요:

- **인스턴스 URL**이 대시보드 URL이 아닌 REST URL인지 확인합니다.
- API 키가 여전히 활성 상태이며 필요한 **템플릿** 권한이 있는지 확인합니다.
- Better Email에서 통합이 활성화되어 있는지 확인합니다.
- 통합이 필요한 사용자 또는 그룹이 **Access**에서 액세스 권한을 가지고 있는지 확인합니다.

추가 지원이 필요하면 [Better Email 고객지원에 문의](mailto:support@better.email)하세요.

## 통합 사용하기 {#use-the-integration}

내보낸 Better Email 템플릿은 Braze의 **템플릿 및 미디어** > **이메일 템플릿**에서 확인할 수 있습니다. 모든 Braze Campaign 또는 Canvas에서 사용하세요.