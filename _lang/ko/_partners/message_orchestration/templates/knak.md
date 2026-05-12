---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "이 참조 문서에서는 Braze와 Knak의 파트너십에 대해 설명합니다. Knak은 완전 반응형 이메일을 며칠이나 몇 주가 아닌 몇 분 또는 몇 시간 만에 만들고, 바로 사용할 수 있는 Braze 템플릿으로 내보낼 수 있는 캠페인 제작 플랫폼입니다."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak](https://knak.com/)은 엔터프라이즈 마케팅 팀이 사내에서 사용할 수 있도록 구축된 최초의 캠페인 제작 플랫폼입니다. 드래그 앤 드롭 플랫폼을 통해 누구나 코딩이나 외부 도움 없이 몇 분 만에 아름답고 브랜드에 맞는 이메일과 랜딩 페이지를 만들 수 있습니다.

_이 통합은 Knak에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Knak 통합을 사용하면 완전 반응형 이메일을 며칠이나 몇 주가 아닌 몇 분 또는 몇 시간 만에 만들고, 바로 사용할 수 있는 Braze 템플릿으로 내보낼 수 있습니다. Knak은 외부 에이전시나 직접 코딩 없이 Braze에서 관리하는 Campaign(캠페인)의 이메일 제작 수준을 높이고자 하는 마케터를 위해 구축되었습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Knak 계정 | 이 파트너십을 활용하려면 Knak 계정이 필요합니다. |
| Braze REST API 키 | 전체 **Templates** 권한이 있는 Braze REST API 키. <br><br>이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

Knak은 코딩이나 외부 도움 없이 이메일 제작 수준을 높이고자 하는 마케터를 위해 구축되었습니다. 다음과 같은 분들에게 적합합니다:
- 현재 이메일에 간단한 템플릿을 사용하고 있으며 수준을 높이고 싶은 분
- Braze용 이메일 제작을 외부 에이전시나 개발자에게 의존하고 있는 분
- 자산 제작에 대한 크리에이티브 제어권을 되찾고 훨씬 빠르게 시장에 출시하고 싶은 분

## 통합 {#integration}

### 1단계: 통합 구성 {#step-1-configure-your-integration}

Knak에서 **Integrations > Platforms > + Add New Integration**으로 이동합니다.

![통합 추가 버튼]({% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %})

그런 다음, **Braze** 플랫폼을 선택하고 Braze API 키와 REST 엔드포인트를 입력합니다. **Create New Integration**을 클릭하여 통합을 완료합니다.

![새 통합 만들기]({% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %})

### 2단계: Knak 템플릿 동기화 {#step-2-sync-your-knak-templates}

Knak에서 Braze에 동기화하려는 이메일을 찾아 **Publish**를 선택한 다음 **Sync**를 선택합니다.

![Knak 통합 1]({% image_buster /assets/img/knak/integration-post-step-1-sync.png %})

그런 다음 이메일 이름을 확인하고 **Sync**를 클릭합니다.

![Knak 통합 2]({% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %})

## 통합 사용 {#using-the-integration}

업로드한 Knak 이메일은 Braze의 **Engagement > Templates & Media**에서 찾을 수 있습니다. 아름답고 브랜드에 맞으며 완전 반응형으로 제작됩니다. 유일한 한계는 여러분의 창의력뿐입니다!