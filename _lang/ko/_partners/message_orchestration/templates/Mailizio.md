---
nav_title: Mailizio
article_title: Mailizio
alias: /partners/mailizio
description: "이 참고 문서에서는 재사용 가능하고 브랜드에 안전한 콘텐츠를 디자인하여 Braze로 내보낼 수 있는 이메일 제작 및 관리 플랫폼인 Mailizio와 Braze의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Mailizio

> [Mailizio](https://mailizio.com/)는 직관적인 시각적 편집기를 사용하여 재사용 가능하고 브랜드에 안전한 콘텐츠를 쉽게 디자인할 수 있는 이메일 제작 및 관리 플랫폼입니다. Mailizio를 Braze에 통합하면 콘텐츠 블록과 이메일 템플릿을 내보낸 다음 동일한 자산에서 인앱 메시지를 자동으로 생성하여 빠르고 완벽하게 제어되는 Campaign 배포가 가능합니다.

_이 통합은 Mailizio에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Mailizio와 Braze의 통합을 통해 Mailizio의 편집기를 사용하여 동적 이메일 템플릿을 디자인하고, Braze 구성에 사용된 Liquid 변수를 활용하고, 이를 Braze로 푸시하여 Campaign 실행을 간소화할 수 있습니다.

## 활용 사례 {#use-cases}

- Campaigns 및 트랜잭션 메시지를 위해 바로 보낼 수 있는 이메일 템플릿을 Braze에 직접 푸시하세요.
- 재사용 가능한 콘텐츠 모듈(헤더, 푸터, 프로모션 등)을 구축하여 여러 Campaigns와 채널에서 제작을 간소화하세요.
- 이메일에서 인앱 메시지를 생성하세요: Mailizio는 이메일의 관련 섹션을 식별하고 인앱 Campaigns에 사용할 수 있도록 HTML을 내보낼 수 있습니다.
- 이메일과 인앱 메시지 모두에서 Braze 호환 Liquid 변수를 사용하여 대규모로 개인화할 수 있습니다.
- Mailizio에서 크리에이티브 자산을 관리하고 한 번의 내보내기로 Braze에서 업데이트하여 브랜딩의 일관성을 유지하세요.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Mailizio 계정 | 이 파트너십을 이용하려면 Mailizio 계정이 필요합니다. |
| Braze REST API 키 | 전체 **Templates** 권한이 있는 Braze REST API 키.<br><br>Braze 대시보드의 **Settings** > **API Keys**에서 Braze REST API 키를 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

Mailizio 고객 성공 매니저에게 Braze REST API 키와 클러스터 인스턴스를 제공하세요. 그런 다음 Mailizio 팀이 초기 통합을 설정합니다.

{% alert important %}
이 설정은 일회성이며, 향후 모든 내보내기는 이 API 키를 자동으로 사용합니다.
{% endalert %}

### 1단계: Mailizio에서 이메일 만들기 {#step-1-create-an-email-in-mailizio}

Mailizio에서 드래그 앤 드롭 편집기를 사용하여 브랜드 아이덴티티를 반영한 이메일을 구축한 다음 **Save**를 클릭하여 작업을 저장하세요.

![드래그 앤 드롭 편집기 스크린샷]({% image_buster /assets/img/mailizio/screenshot_1.png %})

### 2단계: 이메일 템플릿을 Braze로 내보내기 {#step-2-export-your-email-template-to-braze}

준비가 되면 **Export Newsletter**를 클릭합니다. 팝업에서 **Braze-email**을 선택하고 내보내기를 확인합니다.

나중에 콘텐츠를 업데이트하는 경우 Mailizio에서 다시 내보내기를 수행하여 Braze에서 새로고침하세요.

![내보내기 모달 스크린샷]({% image_buster /assets/img/mailizio/screenshot_2.png %})

{% alert important %}
Mailizio의 **Module** 편집기를 사용하여 동일한 방식으로 콘텐츠 블록을 생성하고 내보낼 수 있습니다.
{% endalert %}

## 사용법 {#usage}

Braze 계정의 **Templates & Media > Email Templates** 섹션에서 업로드한 Mailizio 템플릿을 찾으세요. 이제 이 이메일 템플릿을 사용하여 고객에게 매력적인 이메일 메시지를 보낼 수 있습니다!