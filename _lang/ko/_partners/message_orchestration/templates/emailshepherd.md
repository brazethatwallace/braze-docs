---
nav_title: EmailShepherd
article_title: EmailShepherd
alias: /partners/emailshepherd/
description: "이 참조 문서에서는 Braze와 EmailShepherd 간의 파트너십을 설명합니다. EmailShepherd는 이메일 디자인 시스템을 기반으로 구축된 에이전트 기반 이메일 제작 플랫폼으로, 승인된 이메일을 Braze 워크스페이스에 게시합니다."
page_type: partner
search_tag: Partner
---

# EmailShepherd

> [EmailShepherd](https://emailshepherd.com/)는 이메일 디자인 시스템을 기반으로 구축된 에이전트 기반 이메일 제작 플랫폼으로, 마케팅 팀 전체와 AI 에이전트가 병목 현상 없이 브랜드에 맞는 프로덕션 준비 이메일을 제작할 수 있도록 합니다. Braze 통합을 통해 승인된 이메일을 Braze 워크스페이스에 직접 게시할 수 있으므로, 마케터는 브랜드 일관성을 유지하면서 Braze에서 이메일 제작을 확장할 수 있습니다.

_이 통합은 EmailShepherd에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 EmailShepherd 통합을 사용하면 EmailShepherd에서 이메일 디자인 시스템을 기반으로 이메일을 구축하고 이메일 템플릿으로 Braze에 내보낼 수 있습니다. 팀이 EmailShepherd에서 이메일을 생성하고 승인한 다음, 수동 HTML 전달 없이 프로덕션 준비 템플릿을 Braze에 게시합니다.

## 필수 조건 {#prerequisites}

이 통합을 사용하려면 다음이 필요합니다.

| 요구 사항 | 설명 |
| ----------- | ----------- |
| EmailShepherd 계정 | 이 통합을 사용하려면 EmailShepherd 계정이 필요합니다. |
| Braze REST API 키 | 전체 "Templates" 권한이 있는 Braze REST API 키. <br><br>Braze 대시보드에서 **설정** > **API 키**로 이동하여 생성할 수 있습니다. |
| Braze 인스턴스 | Braze [클러스터 인스턴스]({{site.baseurl}}/api/basics/#endpoints)는 Braze 대시보드 및 REST 엔드포인트와 일치합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 활용 사례 {#use-cases}

EmailShepherd는 모든 발송에서 브랜드를 유지하면서 이메일 제작을 확장하려는 팀을 위해 구축되었습니다. 다음과 같은 경우에 적합합니다.

- **대규모 브랜드 일관성 유지:** 이메일 디자인 시스템이 승인된 구성요소, 색상 및 레이아웃을 정의합니다. Braze에 게시되는 모든 이메일은 설계 단계부터 브랜드에 맞게 제작됩니다.
- **팀 전체에 이메일 제작 개방:** 이메일 디자인 시스템을 기반으로 한 드래그 앤 드롭 빌더를 통해 누구나 프로덕션 준비 이메일을 구축할 수 있습니다.
- **에이전트 기반 Campaign(캠페인) 생성 활용:** AI 에이전트가 이메일 디자인 시스템의 가드레일 내에서 구축하므로, 생성된 Campaign이 브랜드에 맞고 발송 준비가 완료됩니다.

## 통합 {#integration}

### 1단계: EmailShepherd 커넥터 생성 {#step-1-create-your-emailshepherd-connector}

{% alert note %}
이 설정은 한 번만 수행하면 됩니다. 커넥터를 생성하면 EmailShepherd가 이후 모든 Braze 내보내기에 이 자격 증명을 사용합니다.
{% endalert %}

1. EmailShepherd에서 **Connectors** > **Add connector**로 이동합니다.
2. **Braze**를 선택하고 커넥터 이름을 입력합니다.
3. API 키를 입력하고 Braze 인스턴스를 선택합니다.
4. **Create Connector**를 선택하여 연결을 저장합니다.

![Braze 인스턴스 및 API 키 필드가 있는 EmailShepherd 커넥터 양식]({% image_buster /assets/img_archive/emailshepherd_step1.png %}){: style="max-width:60%;"}

### 2단계: EmailShepherd에서 이메일 내보내기 {#step-2-export-an-email-from-emailshepherd}

EmailShepherd에서 Braze로 내보내려는 이메일을 찾습니다. 게시된 상태인지 확인한 다음 **Export**를 선택합니다.

![내보내기 동작이 있는 EmailShepherd 이메일 편집기]({% image_buster /assets/img_archive/emailshepherd_step2.png %}){: style="max-width:60%;"}

### 3단계: Braze에 구성 및 게시 {#step-3-configure-and-publish-to-braze}

1. 내보내기 페이지에서 **Connectors** 아래에 있는 Braze 커넥터를 선택합니다(예: **Braze Prod**).
2. EmailShepherd 이미지 라이브러리의 이미지에 대한 **Image hosting** 옵션을 선택합니다. URL로 입력된 이미지는 내보내기 중에 변경되지 않습니다.
3. **Locale**을 확인하고 Braze에서 사용할 이메일의 **Template name**을 입력합니다.
4. **Start export**를 선택합니다.

![Braze 커넥터, 이미지 호스팅 및 템플릿 이름 필드가 있는 EmailShepherd 내보내기 페이지]({% image_buster /assets/img_archive/emailshepherd_step3.png %}){: style="max-width:60%;"}

## 통합 사용 {#use-the-integration}

Braze에서 **콘텐츠** > **이메일**로 이동하면 내보낸 이메일을 찾을 수 있습니다. 이 템플릿을 Braze Campaigns 및 Canvases에서 사용할 수 있습니다.

## 고객지원 {#support}

EmailShepherd 통합에 대한 자세한 내용은 [EmailShepherd 설명서](https://emailshepherd.com/docs/)를 참조하세요.