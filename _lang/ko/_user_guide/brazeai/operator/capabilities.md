---
nav_title: 기능
article_title: Operator로 할 수 있는 것
page_order: 1
page_type: reference
toc_headers: h2
description: "이 참조 문서에서는 BrazeAI Operator™가 대시보드 전반에서 수행할 수 있는 기능을 다룹니다. Campaigns, Segments, 에이전트 구축, 카피·메시지·Liquid·이미지 생성, 데이터 변환, 콘텐츠 품질 검토, 정보 조회 등이 포함됩니다."
---

# Operator로 할 수 있는 것 {#operator-capabilities}

> [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator)는 Braze 대시보드에 내장된 AI 어시스턴트입니다. 질문에 답하고, 메시지를 작성하며, 지원되는 페이지 전반에서 동작을 수행합니다. 원하는 내용을 자연어로 설명하면 Operator가 맥락에 맞게 처리합니다.

Operator는 워크스페이스(브랜드 가이드라인, 커스텀 속성, 연결된 콘텐츠, 현재 작업 중인 페이지)를 이해하므로, 독립형 어시스턴트보다 더 맥락을 인식한 결과물을 생성합니다. Operator가 Campaign, Segment 또는 기타 객체에 대한 변경을 제안하면, 저장되기 전에 사용자가 검토하고 승인할 수 있는 [액션 카드]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)로 변경 사항을 시각적 차이로 표시합니다.

후속 대화를 이어갈 수 있습니다. Operator는 채팅 기록을 지울 때까지 이전 메시지를 기억합니다.

## 사전 요구 사항 {#prerequisites}

Operator는 사용자와 동일한 권한을 가지므로, 특정 작업에는 해당 영역에 대한 관련 권한이 필요합니다. 예를 들어, 이미지를 생성하려면 *미디어 라이브러리 자산 편집* 권한이 필요합니다. 진입점이 보이지 않는 경우 관리자에게 권한을 확인하세요. 자세한 내용은 [권한 목록]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)을 참조하세요.

## Operator가 만들 수 있는 것 {#what-operator-can-create}

카피와 Liquid 생성 외에도, Operator는 대시보드 전반에서 다음을 포함한 다양한 객체를 구축하는 데 도움을 줄 수 있습니다:

- Campaigns
- Content Blocks
- 커스텀 에이전트
- 이미지
- 메시지 및 메시지 템플릿([메시지 생성](#generate-messages) 및 [메시지 템플릿 만들기](#create-message-templates) 참조)
- Segments
- 세그먼트 확장

{% alert note %}
Operator의 대시보드 전반 기능은 정기적으로 확장됩니다. 최신 기능에 대해서는 **Operator에게 직접 물어보세요**.
{% endalert %}

## Campaigns 및 오디언스 {#campaigns-and-audiences}

Operator는 아이디어에서 Campaign 또는 오디언스 초안까지 진행하고, 이미 존재하는 것을 다듬는 데 도움을 줄 수 있습니다. Operator가 Campaign이나 Segment에 제안하는 모든 변경 사항은 저장되기 전에 검토할 수 있는 액션 카드로 표시됩니다.

시작하려면 Campaign이나 Segment를 만들 때 **Create with Operator** 옵션을 찾으세요.

![Campaign 만들기 및 Segment 만들기 메뉴에 각각 Create with Operator 옵션이 표시됩니다.]({% image_buster /assets/img/operator/operator_create_with_operator.png %}){:style="max-width:90%"}

- **Campaigns 만들기 및 편집:** Campaign을 시작할 때, Operator는 하나의 자연어 브리프에서 포괄적인 초안을 작성하는 데 도움을 줄 수 있습니다. 여기에는 오디언스, 콘텐츠, 전달 설정이 포함됩니다. 기존 Campaign을 편집하는 데에도 Operator에게 도움을 요청할 수 있습니다. 예를 들어, 타겟팅을 조정하거나 메시지 콘텐츠를 새로 고칠 수 있습니다.
- **브리프에서 Campaign으로:** 전체 Campaign 브리프를 설명하면, Operator가 카피, 이미지, 개인화, 타겟팅, 발송 시간 추천을 포함한 초안을 작성하는 데 도움을 줍니다. Campaign 작성기에서 초안을 검토하고 후속 프롬프트로 다듬은 후 발송하세요.
- **Segments 만들기 및 편집:** Segment를 시작할 때, 원하는 오디언스를 설명하면 Operator가 속성 조건, 이벤트 기록, 카탈로그 조회를 포함한 필터 로직을 구축하는 데 도움을 줍니다. 타겟팅 전략을 변경해야 할 때 기존 Segment의 필터를 편집하는 데에도 Operator가 도움을 줄 수 있습니다.
- **세그먼트 확장 만들기:** Operator는 SQL로 정의된 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension)을 구축하는 데 도움을 줄 수 있습니다. 원하는 오디언스 로직을 설명하면 Operator가 저장하기 전에 검토할 수 있는 쿼리를 작성합니다. Operator와 SQL에 대한 자세한 내용은 [SQL 쿼리 작성](#write-sql-queries)을 참조하세요.

## 에이전트 {#agents}

![커스텀 에이전트 옵션과 Operator로 구축된 에이전트 템플릿을 보여주는 에이전트 만들기 메뉴.]({% image_buster /assets/img/operator/operator_create_agent.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

Operator는 [에이전트 콘솔]({{site.baseurl}}/user_guide/brazeai/agents)에서 에이전트를 구축하고 다듬는 데 도움을 줄 수 있습니다. Operator가 에이전트에 제안하는 모든 변경 사항은 저장되기 전에 검토할 수 있는 액션 카드로 표시됩니다.

- **처음부터 에이전트 만들기:** Operator는 에이전트 콘솔의 모든 필드에 접근할 수 있으므로, 원하는 에이전트를 설명하면 Operator가 구성하는 데 도움을 줍니다. 여기에는 지침, 출력 설정, 기타 에이전트 필드가 포함됩니다.
- **템플릿에서 시작:** 에이전트 콘솔은 카피라이팅, 감성 분석, 여정 라우팅, 카탈로그 보강 등 일반적인 사용 사례에 대해 미리 작성된 프롬프트를 로드하는 **Create agent with Operator** 옵션을 제공합니다. 카테고리를 선택하면 Operator가 다듬을 수 있는 에이전트 초안을 작성하는 데 도움을 줍니다. 전체 템플릿 목록은 [Operator로 구축된 에이전트 템플릿]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)을 참조하세요.
- **기존 에이전트 다듬기:** 에이전트를 편집할 때, 에이전트의 지침 필드 근처에서 **Generate with Operator** 또는 **Refine with Operator**를 선택하여 에이전트의 프롬프트와 출력 설정을 작성하거나 수정하는 데 Operator의 도움을 받으세요.

## 콘텐츠 및 크리에이티브 {#content-and-creative}

Operator는 카피, 메시지 HTML, Liquid, 이미지를 포함하여 메시지의 콘텐츠를 생성하고 검토할 수 있으며, 브랜드 가이드라인이 구성된 곳에서는 자동으로 적용합니다.

### 브랜드 가이드라인 적용 {#apply-brand-guidelines}

Operator는 워크스페이스에 구성된 브랜드 가이드라인을 사용하여 생성된 카피, 템플릿, 이미지가 브랜드의 보이스, 톤, 스타일과 일치하도록 합니다. 브랜드 가이드라인을 설정하려면 **콘텐츠** > **브랜드 가이드라인**으로 이동하세요. 자세한 내용은 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) 및 Operator 사용 가이드의 [브랜드 가이드라인 적용]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines)을 참조하세요.

### 카피 생성 {#generate-copy}

Operator를 사용하여 어디서든 카피를 브레인스토밍하거나 생성할 수 있지만, 메시지 작성기에서 직접 사용할 때 가장 좋은 경험을 얻을 수 있습니다. 작성기에서는 Operator가 작성 중인 메시지와 함께 작업할 수 있습니다. 제품이나 Campaign을 설명하면 Operator가 검토하고 삽입할 수 있는 카피를 반환합니다.

Operator는 독립형 카피라이터보다 몇 가지 면에서 개선되었습니다:

- [브랜드 가이드라인](#apply-brand-guidelines)이 구성되어 있으면 자동으로 적용합니다.
- [페이지 인식 컨텍스트]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context)를 사용하므로 작업 중인 채널이나 메시지를 다시 설명할 필요가 없습니다. 페이지를 인식하기 때문에 처음부터 생성하는 대신 기존 메시지를 편집하거나 다듬는 데에도 사용할 수 있습니다.
- [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)과 이벤트를 조회할 수 있으므로, 실제 Liquid를 사용한 개인화된 카피 추천을 요청할 수 있습니다.
- 대화를 이어가며 반복할 수 있습니다. 예를 들어, 다른 톤, 더 짧은 버전, 번역을 요청할 수 있습니다.

#### 톤 {#generate-copy-tones}

생성된 카피의 톤은 프롬프트에 의해 결정됩니다. 원하는 스타일을 설명하면 Operator가 그에 맞게 출력을 조정합니다. 예를 들어, 격식체, 캐주얼, 긴급, 눈길을 끄는 등의 스타일을 요청할 수 있습니다. 후속 프롬프트에서 톤을 다듬을 수도 있습니다. 예를 들어, 더 편안한 버전이나 더 세련된 버전을 요청할 수 있습니다. 브랜드 가이드라인이 구성되어 있으면 Operator가 자동으로 적용하여 카피가 브랜드의 보이스와 일관되게 유지됩니다.

### 메시지 생성 {#generate-messages}

Operator는 HTML 모드가 있는 모든 채널 또는 편집기에서 전체 메시지 디자인을 생성할 수 있습니다. 지원되는 채널에는 다음이 포함되지만 이에 국한되지 않습니다:

- 이메일
- SMS/MMS/RCS
- 인앱 메시지
- 콘텐츠 카드
- 배너
- 푸시
- 웹훅

드래그 앤 드롭 편집기는 직접적인 디자인 생성을 지원하지 않지만, Operator는 수동으로 추가하는 카피나 기타 콘텐츠에 대해 여전히 도움을 줄 수 있습니다. 원하는 메시지를 자연어로 설명하고, 출력을 검토한 후 작성기에 삽입하세요. 대화를 이어가며 결과를 다듬을 수 있습니다. 예를 들어, 다른 레이아웃, 더 짧은 카피, 업데이트된 버튼 스타일링을 요청한 후 HTML을 편집기에 삽입할 수 있습니다.

작성 중인 작성기에서 Operator를 사용할 때 가장 좋은 결과를 얻을 수 있으며, 이 경우 채널과 메시지 유형에 대한 [페이지 인식 컨텍스트]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context)를 활용합니다. 브랜드 가이드라인이 구성되어 있으면 Operator가 자동으로 적용합니다.

### Content Blocks 만들기 {#create-content-blocks}

Operator는 메시지 전반에 삽입하는 재사용 가능한 콘텐츠 조각인 [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)를 만드는 데 도움을 줄 수 있습니다. 원하는 블록을 설명하면 Operator가 저장하기 전에 검토할 수 있는 콘텐츠를 작성합니다. Content Blocks는 공유되므로, 하나를 업데이트하면 이를 참조하는 모든 메시지가 업데이트됩니다.

Operator는 대시보드에서 Content Blocks를 한 번에 하나씩 만듭니다. Content Blocks를 대량으로 만들려면 `content_blocks.create` 권한이 있는 API 키를 사용하여 [Content Block 만들기]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) 엔드포인트를 사용하세요.

### 메시지 템플릿 만들기 {#create-message-templates}

Operator는 Campaigns 전반에 적용할 수 있는 재사용 가능한 [메시지 템플릿]({{site.baseurl}}/user_guide/messaging/templates)을 만드는 데 도움을 줄 수 있습니다. 원하는 템플릿을 설명하면 Operator가 저장하기 전에 검토할 수 있는 초안을 작성합니다. 템플릿 생성은 메시지 생성과 유사하게 작동하므로, 지원되는 채널과 편집기에 대해서는 [메시지 생성](#generate-messages)을 참조하세요.

### Liquid 생성 {#generate-liquid}

Operator는 [Liquid 구문]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)에 매우 능숙합니다. 워크스페이스의 데이터를 기반으로 복잡한 Liquid 로직을 생성할 수 있으며, 여기에는 예시 값을 찾기 위한 속성, 이벤트, [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs) 데이터 조회가 포함됩니다. 또한 Campaigns의 기존 Liquid를 검토하고 설명할 수 있습니다.

카피라이팅과 마찬가지로, 어디서든 Operator에게 Liquid 생성을 요청할 수 있으며 모든 채널과 메시지 작성기에서 작동합니다. 메시지 작성기 내에서 사용할 때 가장 좋은 결과를 얻을 수 있으며, 이 경우 Operator가 작성 중인 메시지의 전체 컨텍스트를 파악합니다.

{% details Liquid 프롬프트 모범 사례 %}

#### 컨텍스트 제공 {#generate-liquid-give-context}

컨텍스트를 제공하면 Operator가 프로젝트를 둘러싼 전체적인 그림을 이해하는 데 도움이 됩니다. 다음과 같은 컨텍스트를 포함하면 유용합니다:

- 회사 이름과 업종
- 작업 중인 Campaign(예: 블랙 프라이데이 또는 연말 세일)
- 목표(예: 클릭률 향상)
- 메시지에 포함하려는 특정 커스텀 속성

프롬프트에 컨텍스트를 포함하면 Operator가 요구 사항에 더 잘 맞는 응답을 제공하는 데 도움이 됩니다. Campaign, 메시지 브리프 또는 브레인스토밍 문서의 세부 정보를 포함하여 Operator에게 배경 정보를 제공할 수도 있습니다.

#### 구체적으로 작성 {#generate-liquid-be-specific}

Operator는 후속 질문을 할 수 있지만, 세부 정보를 미리 제공하면 더 정확한 결과를 더 빨리 얻을 수 있습니다. 다음과 같은 세부 정보를 포함하는 것을 고려하세요:

- 메시지에 대한 알려진 선호 사항이나 요구 사항
- 메시지 수신자의 응답이 없는 경우나 대체 메시지 옵션 등의 상황 처리 방법에 대한 지침
- 사용하려는 커스텀 속성의 정확한 값 또는 유사한 값(Operator가 더 정확한 로직을 생성하고 테스트하는 데 도움이 됩니다)
- 연결된 콘텐츠를 사용하는 Liquid를 요청할 때, API 엔드포인트에 대한 설명서, 샘플 API 응답 또는 둘 다

#### 창의적으로 시도 {#generate-liquid-get-creative}

다양한 프롬프트를 시도하여 Operator가 메시징을 어떻게 향상시킬 수 있는지 확인하세요. 다양한 프롬프트와 아이디어를 실험해 보세요. 창의성이 더 매력적인 결과로 이어질 수 있습니다.

{% enddetails %}

### 이미지 생성 {#generate-images}

Operator는 OpenAI의 인공지능 시스템이자 Braze 서드파티 제공업체인 [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)을 사용하여 이미지를 생성합니다. 이를 통해 자연어 설명에서 사실적인 이미지와 아트를 만들 수 있습니다.

[미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)에서 **자산 업로드** 패널의 **Generate with Operator**를 선택하세요. 원하는 이미지를 설명하면 Operator가 이미지를 생성하고 미디어 라이브러리에 직접 저장합니다.

#### 프롬프트 팁 {#generate-images-prompt-tips}

- 주제, 스타일, 분위기, 색상을 구체적으로 설명하세요. 세부 정보를 많이 포함할수록 더 좋은 결과를 얻을 수 있습니다. 참조 이미지 업로드는 지원되지 않습니다.
- Operator 프롬프트에서 [브랜드 가이드라인](#apply-brand-guidelines)을 컨텍스트로 적용하면, Operator가 생성된 이미지에 직접 적용하여 결과물이 브랜드의 시각적 스타일을 반영합니다.
- 이미지 생성은 일일 Operator 사용 한도에 포함됩니다. 자세한 내용은 [제한 사항](#limitations)을 참조하세요.

### 콘텐츠 품질 검토 {#review-content-quality}

SMS, Android 푸시, iOS 푸시, 전통적인 인앱 메시지의 **테스트** 탭에서 **Review with Operator**를 선택하여 발송 전에 콘텐츠를 검토할 수 있습니다. 기본적으로 Operator는 Campaign의 맞춤법 및 문법 오류, 브랜드에 맞지 않거나 부적절한 톤, 공격적인 언어, 잔여 코드, 테스트 콘텐츠 또는 렌더링되지 않은 Liquid를 검토하고 발견된 문제의 수정 방법을 추천합니다. 프롬프트에서 Operator가 콘텐츠를 검토하는 방식을 직접 맞춤 설정하도록 요청할 수도 있습니다.

기본 검토 외에도 Operator가 특정 검사에 집중하도록 지시할 수 있습니다. 다음 항목을 확인하도록 프롬프트하는 것을 고려하세요:

- **맞춤법 및 문법:** 맞춤법 및 문법 오류를 교정하고 콘텐츠의 정확성을 높이는 수정 사항을 제안합니다.
- **톤:** 톤이 의도한 커뮤니케이션 스타일과 일치하는지 평가하고 오해의 소지가 있는 부분을 표시합니다.
- **공격적인 언어:** 잠재적으로 공격적이거나 부적절한 언어를 스캔하여 수정하고 메시징을 존중하는 방식으로 유지합니다.
- **의도하지 않은 콘텐츠:** 의도치 않게 추가된 잔여 코드, 마크업 또는 테스트 메시지(테스트 사용자에게 렌더링되지 않은 Liquid 포함)를 찾습니다.
- **다른 언어:** 다른 언어로 작성된 콘텐츠를 검토합니다. 영어 이외의 콘텐츠에 대한 지원은 다를 수 있으므로 결과를 신중하게 검토하세요.

#### 모범 사례 {#review-content-quality-best-practices}

콘텐츠 검토를 최대한 활용하려면 다음을 고려하세요:

- **메시지를 교정하세요:** 콘텐츠 검토가 오류를 식별하는 데 도움이 될 수 있지만, 콘텐츠를 수동으로 교정하는 것은 여전히 필수적입니다. 인공지능이 생성한 제안을 유용한 가이드로 활용하되, 정확성을 보장하기 위해 본인의 판단을 사용하세요.
- **톤 분석을 이해하세요:** 톤 분석 결과는 주관적이며 인공지능 모델의 이해에 기반합니다. 유용한 인사이트를 제공할 수 있지만, 의도한 톤과 대화 맥락을 고려하여 적절한 조정을 하세요.
- **표시된 공격적인 언어를 다시 확인하세요:** 공격적인 언어 감지는 강력하게 설계되었지만, 간혹 오탐지가 발생할 수 있습니다. 표시된 섹션을 신중하게 검토하고 필요에 따라 적절한 변경을 하세요.

## 데이터 자동화 및 조회 {#data-automation-and-lookup}

Operator는 워크스페이스 데이터와 Braze 설명서에 대한 참조 역할을 하고, 데이터를 직접 쿼리해야 할 때 SQL을 작성하며, 웹훅 페이로드와 같은 수신 데이터를 Braze가 사용할 수 있는 형식으로 변환하는 코드를 생성할 수 있습니다.

### Operator가 조회할 수 있는 것 {#what-operator-can-look-up}

Operator는 질문에 답하거나 생성하는 콘텐츠의 근거로 다음을 참조할 수 있으며, 이에 국한되지 않습니다:

- Braze 설명서
- [Segments]({{site.baseurl}}/user_guide/audience/segments)
- [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) 및 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs) 데이터
- 기존 [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) 및 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) 구성(타겟팅 및 전달 설정 등)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [프로모션 코드]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)
- [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) 응답
- [에이전트]({{site.baseurl}}/user_guide/brazeai/agents)

특정 정보를 조회할 수 있는지 확실하지 않은 경우 Operator에게 직접 물어보세요.

### 성능 데이터 분석 {#analyze-performance-data}

Campaign 및 Canvas 성능에 대해 Operator에게 자연어로 질문하면, 워크스페이스 데이터에서 차트, 비교, 간단한 인사이트를 가져와 제공합니다. 현재 페이지의 컨텍스트가 필요한 Operator의 페이지 인식 기능과 달리, 분석 기능은 대시보드 어디에서든 응답할 수 있습니다. 자세한 내용은 [Operator 분석]({{site.baseurl}}/user_guide/brazeai/operator/analyze)을 참조하세요.

### SQL 쿼리 작성 {#write-sql-queries}

Operator는 [세그먼트 확장](#campaigns-and-audiences) 및 쿼리 빌더 [쿼리 템플릿]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)을 위한 SQL을 작성하는 데 도움을 줄 수 있습니다. 원하는 쿼리를 자연어로 설명하면 Operator가 실행하기 전에 검토할 수 있는 SQL을 생성합니다.

### 데이터 변환 코드 생성 {#generate-data-transformation-code}

[데이터 변환]({{site.baseurl}}/user_guide/data/unification/data_transformation) 편집기에서 **Insert Code**를 선택하여 수신 웹훅 페이로드를 유효한 Braze API 요청으로 변환하는 변환 코드를 생성합니다. 변환을 만드는 단계별 지침은 [변환 만들기]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation)를 참조하세요.

## 워크스페이스 설정 {#workspace-settings}

Operator는 여러 워크스페이스 구성 페이지에서 설정을 검토하고 업데이트할 수 있습니다. 원하는 변경 사항을 설명하면, Operator가 저장하기 전에 검토할 수 있는 액션 카드로 제안합니다. 지원되는 설정 페이지에는 다음이 포함되지만 이에 국한되지 않습니다:

- [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- [푸시 설정]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings)
- [메시징 사용량 제한]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits)
- [승인 워크플로]({{site.baseurl}}/user_guide/messaging/governance/approvals), [메시징 규칙]({{site.baseurl}}/user_guide/messaging/governance/approvals/messaging_rules) 및 상시 승인 포함
- [API 및 식별자]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers), [기타 식별자]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers#other-identifiers) 및 API 제한 포함
- [관리자 설정 연락처 정보]({{site.baseurl}}/user_guide/administer/global/admin_settings/contact_information)

{% alert note %}
Operator의 설정 페이지 지원 범위는 정기적으로 확장됩니다. 현재 구성할 수 있는 항목에 대한 최신 답변을 얻으려면 **Operator에 직접 문의하세요**.
{% endalert %}

## 제한 사항 {#limitations}

{% alert note %}
Operator의 지원 범위는 자주 변경됩니다. 특정 화면이나 워크플로가 지원되는지 확실하지 않은 경우 Operator에게 직접 물어보세요.
{% endalert %}

Operator의 대시보드 지원 범위는 넓지만 한계가 있습니다.

- **Canvases:** Operator는 [Canvases]({{site.baseurl}}/user_guide/messaging/canvas)를 만들거나 편집할 수 없지만, 기존 Canvas의 구성(타겟팅 및 전달 설정 등)을 참조하여 질문에 답하고 출력의 근거로 사용할 수 있습니다.
- **Campaign 복제:** Operator는 Campaigns 목록 보기에서 기존 Campaign을 복제할 수 없습니다. 유사한 Campaign을 만들려면 Operator에게 처음부터 새로 만들도록 요청하거나, 목록 보기의 **More Actions** 메뉴에서 수동으로 Campaign을 복제하세요.
- **드래그 앤 드롭 편집기:** Operator는 [이메일]({{site.baseurl}}/user_guide/channels/email/drag_and_drop), [배너]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner), [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)용 드래그 앤 드롭 편집기에서 메시지 디자인을 직접 생성하거나 삽입할 수 없습니다. 해당 HTML 편집기로 전환하여 Operator를 사용하거나, Operator에게 카피 등의 콘텐츠를 생성하도록 요청한 후 수동으로 붙여넣으세요. 지원되는 채널과 편집기에 대해서는 [메시지 생성](#generate-messages)을 참조하세요.
- **화면 가시성:** Operator는 페이지 인식 컨텍스트를 사용하여 사용자가 보고 있는 내용을 이해하며, 지원되는 미리보기와 편집기 내의 콘텐츠도 포함됩니다. 페이지의 일부가 Operator가 읽을 수 있는 범위 밖에 있으면, 추측하는 대신 알려주므로 해당 콘텐츠를 직접 설명할 수 있습니다.
- **사용 한도:** Operator에는 24시간마다 초기화되는 회사 전체 일일 사용 한도가 있습니다. 이미지 생성도 이 한도에 포함됩니다. 한도에 도달하면 "일일 사용 한도 초과" 메시지가 표시되며 초기화될 때까지 추가 요청을 할 수 없습니다. 문제 해결 단계는 [문제 해결]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting)을 참조하세요.

## 레거시 어시스턴트 {#legacy-assistants}

Operator 이전에는 AI 카피라이터, AI Liquid 어시스턴트, AI 이미지 생성기, AI SQL 생성기, 데이터 변환 AI 코파일럿, 콘텐츠 검토 등 여러 AI 기능이 별도의 어시스턴트로 독립적으로 제공되었습니다. 모든 진입점은 그대로 유지되며 Operator로 연결되므로 기존 워크플로에 영향이 없습니다. 현재 이러한 기능이 수행하는 작업에 대해서는 [콘텐츠 및 크리에이티브](#content-and-creative)와 [데이터 자동화 및 조회](#data-automation-and-lookup)를 참조하세요.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## 데이터 프라이버시 및 보안 {#data-privacy-and-security}

Operator는 OpenAI와 통합하여 출력을 생성합니다. Braze가 OpenAI에 보내는 정보, 해당 데이터의 사용 방식, 지적 재산권에 대한 자세한 내용은 [OpenAI와의 데이터 사용 방식]({{site.baseurl}}/user_guide/brazeai/operator#data-privacy-and-security)을 참조하세요.

## 다음 단계 {#next-steps}

- [Operator 시작하기]({{site.baseurl}}/user_guide/brazeai/operator): Operator에 접근하고 사용하기
- [프롬프트 라이브러리]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): 바로 사용할 수 있는 예시 프롬프트 둘러보기
- [액션 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Operator가 제안한 변경 사항을 검토하고 승인하기
- [문제 해결]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): 일반적인 문제와 해결 방법 참조