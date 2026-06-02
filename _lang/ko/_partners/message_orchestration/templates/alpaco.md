---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "Braze와 Alpaco 통합을 사용하면 브랜드에 맞는 Liquid 호환 이메일 템플릿과 콘텐츠 블록을 Braze로 내보내어 이메일 및 인앱 메시징에 바로 사용할 수 있습니다."
page_type: partner
search_tag: Partner
---

# Alpaco

> [Alpaco](https://alpaco.email/)는 드래그 앤 드롭 편집기를 제공하는 온라인 크리에이티브 관리 툴로, Braze에서 사용할 수 있는 재사용 가능하고 브랜드에 안전한 콘텐츠를 구축할 수 있습니다. Alpaco와 Braze 통합을 통해 Content Blocks, 이메일 템플릿, 인앱 메시지 템플릿을 내보낼 수 있습니다.

_이 통합은 Alpaco에서 유지 관리합니다._

{% alert note %}
Alpaco는 [전체 Liquid](https://shopify.github.io/liquid/) 변수를 지원하며, Braze 구성에서 사용되는 모든 Liquid 변수도 완벽하게 지원합니다.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ------------| ----------- |
| Alpaco 계정 | 이 파트너십을 활용하려면 Alpaco 계정이 필요합니다. |
| Braze REST API 키 | 전체 **템플릿** 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 클러스터 인스턴스 | Braze [클러스터 인스턴스]({{site.baseurl}}/api/basics/#endpoints)는 Braze 대시보드 및 REST 엔드포인트와 일치합니다. <br><br> 예를 들어, 대시보드 URL이 `https://dashboard-03.braze.com`이면 엔드포인트는 `dashboard-03`입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

- Braze Campaigns 및 트랜잭션 메시징에서 사용할 수 있도록 완전히 디자인된 **이메일 템플릿**을 내보냅니다.
- 여러 채널에서 재사용할 수 있는 **모듈형 콘텐츠 블록**(예: 헤더, 푸터, 프로모션)을 생성하고 관리합니다.
- 이메일과 동일한 크리에이티브 유연성으로 매력적인 **인앱 메시지**를 디자인하여 채널 전반에 걸쳐 일관되고 브랜드에 맞는 경험을 쉽게 제공합니다.
- `{{first_name}}` 또는 `{{custom_attribute}}`와 같은 Braze 지원 Liquid 태그를 포함하여 **개인화**를 활성화합니다.
- Alpaco에서 크리에이티브 디자인을 중앙 집중화하고 한 번의 내보내기로 Braze에 업데이트를 푸시하여 **브랜드 일관성**을 유지합니다.

## 통합 {#integration}

Braze REST API 키와 클러스터 인스턴스를 Alpaco 고객 성공 팀에 제공하세요. 팀에서 초기 통합을 설정해 드립니다.

{% alert note %}
이 설정은 일회성이며, 이후의 모든 내보내기에서 이 API 키가 자동으로 사용됩니다.
{% endalert %}

## Alpaco 메시지를 Braze로 내보내기 {#exporting-alpaco-messages-to-braze}

### 1단계: Alpaco에서 템플릿 생성 {#step-1-create-a-template-in-alpaco}

Alpaco에서 브랜드 아이덴티티를 표현하는 템플릿을 생성합니다. 준비가 되면 **Save**를 선택합니다.

![Alpaco 템플릿 만들기]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### 2단계: 템플릿을 사용하여 메시지 작성 {#step-2-draft-a-message-using-the-template}

다음으로, Alpaco 로비로 이동하여 템플릿을 사용해 이메일, 인앱 메시지 또는 콘텐츠 블록을 생성합니다. 내보내기 전에 메시지를 다시 확인하려면 **Review**를 선택합니다.

![Alpaco 이메일 만들기]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### 3단계: Braze로 메시지 내보내기 {#step-3-export-your-message-to-braze}

**Export**를 선택한 다음 Braze 통합을 선택하고 이메일 템플릿을 내보낼지 콘텐츠 블록을 내보낼지 지정합니다.

내보내기 후 변경 사항이 있으면 Alpaco에서 콘텐츠를 다시 내보내어 Braze에서 업데이트할 수 있습니다.

![Alpaco 이메일 내보내기]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Braze에서 Alpaco 템플릿 및 블록 사용 {#using-alpaco-templates-and-blocks-in-braze}

내보내는 콘텐츠 유형에 따라 템플릿이 다음 섹션 중 하나에 표시됩니다.

- **템플릿 및 미디어 > 이메일 템플릿**
- **템플릿 및 미디어 > Content Blocks**

Alpaco 템플릿은 브랜드 일관성을 중앙에서 관리하려는 조직에 이상적입니다. 또한 쉬운 분류 및 콘텐츠 관리를 위해 Braze의 기본 제공 태그를 지원합니다.