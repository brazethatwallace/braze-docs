---
nav_title: 지식 소스
article_title: 지식 소스
permalink: "/knowledge_sources/"
description: "이 참조 문서에서는 BrazeAI 에이전트를 위한 지식 소스를 생성하고 관리하는 방법을 다룹니다."
page_type: reference
---

# 지식 소스 {#knowledge-sources}

> 지식 소스는 AI 에이전트가 카탈로그 데이터를 해석하고 목표를 달성하기 위해 적절한 정보를 검색하는 데 도움을 줍니다.

{% alert important %}
에이전트 콘솔의 지식 소스는 현재 얼리 액세스 단계입니다. 이 얼리 액세스에 참여하고 싶으시면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 작동 방식 {#how-it-works}

지식 소스는 에이전트 컨텍스트의 한 유형입니다. AI 에이전트는 카탈로그를 에이전트의 지침에서 직접 참조하는 것보다 지식 소스를 참조하여 카탈로그에서 더 정확하게 데이터를 검색할 수 있습니다.

예를 들어, 커스텀 속성인 사용자의 좋아하는 요리를 기반으로 뉴욕시의 레스토랑을 추천하는 에이전트를 구축한다고 가정해 보겠습니다. 이 에이전트는 "nyc_restaurants" 카탈로그의 지식 소스를 참조합니다. 해당 지식 소스를 생성할 때, 레스토랑 이름, 위치, 요리 종류 등 에이전트에 필요한 필드만 포함하고 추천에 도움이 되지 않는 다른 카탈로그 열은 제외합니다.

에이전트의 지침은 역할과 제약 조건을 명확하게 설명합니다:

{% raw %}
```
You are a restaurant recommendation agent. Use your knowledge to help find restaurants for the user. Only include filters in your knowledge source query. Don't ask any followup questions. The user's favorite cuisine is {{custom_attribute.${favorite_cuisine}}}
```
{% endraw %}

사용자가 좋아하는 요리가 피자인 경우, 에이전트는 지식 소스를 기반으로 다음과 같은 응답을 반환할 수 있습니다:

```
Here are some pizza recommendations for you:
- Dale's Pizza (Greenwich Village, Manhattan): Dale's Pizza invites you to savor the taste of authentic New York. Nestled in the heart of Manhattan, this iconic pizzeria offers a warm and inviting atmosphere perfect for any occasion.
- Pizza Palace (Carroll Gardens, Brooklyn): Pizza Palace is a highly-rated culinary gem renowned for its exquisite pizza. This inviting spot offers a warm and modern dining experience.
```

## 지식 소스 생성 {#create-a-knowledge-source}

지식 소스를 생성하려면:

1. **에이전트 콘솔** > **지식 소스**로 이동합니다.
2. **지식 소스 추가**를 선택합니다. 드롭다운에서 **카탈로그**를 선택합니다.
3. 드롭다운에서 카탈로그를 선택합니다.
4. 카탈로그 필드를 검토하고 에이전트의 사용 사례에 해당하지 않는 필드는 선택 해제합니다. 검색이나 생성에 유용하지 않은 카탈로그 필드는 제외하고, 에이전트에 필요한 필드만 지식 소스에 포함하는 것을 권장합니다.
5. (선택 사항) 지식 소스에 포함된 내용을 설명하는 설명을 추가합니다.
6. **지식 소스 추가**를 선택합니다.

모든 카탈로그 필드를 포함하면 불필요한 컨텍스트가 추가되어 출력 품질이 저하될 수 있습니다. 사용 사례와 관련 없는 필드를 선택 해제하면 에이전트가 중요한 데이터에 집중할 수 있습니다.

![카탈로그 'nyc_restaurants'를 참조하는 지식 소스 'nyc_restaurants'.]({% image_buster /assets/unlisted_docs/img/knowledge_sources/knowledge_source_example.png %}){: style="max-width:80%;"}

에이전트를 구축하면서 지식 소스를 생성할 수도 있습니다. 에이전트의 **지침** 섹션으로 이동한 다음, **지식 추가** > **지식 소스 생성**을 선택합니다.

## AI 에이전트에서 지식 소스 사용 {#use-a-knowledge-source-in-your-ai-agent}

**지식 소스** 섹션에서 지식 소스를 관리할 수 있습니다. 여기에서 어떤 지식 소스가 활성 상태인지, 마지막으로 동기화된 시점 등의 세부 정보를 확인할 수 있습니다. 지식 소스의 이름은 소스로 사용된 카탈로그의 이름과 일치합니다.

AI 에이전트에서 지식 소스를 사용하려면:

1. 에이전트의 **지침** 섹션으로 이동합니다.
2. **+ 에이전트 컨텍스트** > **지식 추가**를 선택합니다.
3. 드롭다운에서 지식 소스를 선택합니다.

이제 에이전트가 지식 소스를 참조하여 관련 카탈로그 데이터를 검색할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 지식 소스는 어떻게 작동하나요? {#how-do-knowledge-sources-work}

카탈로그를 지식 소스로 변환하면 Braze 에이전트가 카탈로그의 단어와 구문 뒤에 있는 실제 의미를 이해할 수 있으므로, 에이전트가 더 나은 출력을 위해 의미 있는 데이터를 더 효과적으로 찾을 수 있습니다.

### 지식 소스는 언제 생성해야 하나요? {#when-should-i-create-a-knowledge-source}

카탈로그를 컨텍스트로 사용할 수 있는 커스텀 에이전트(Canvas 에이전트 또는 카탈로그 에이전트)를 설정하려는 경우 지식 소스를 생성합니다. 지식 소스를 사용하는 것이 기존 방법에 비해 카탈로그를 컨텍스트로 연결하는 더 나은 방법입니다.

### 에이전트에 지식 소스가 컨텍스트로 제공된 경우, 원본 카탈로그도 컨텍스트로 할당해야 하나요? {#if-an-agent-has-been-given-a-knowledge-source-as-context-do-i-also-need-to-assign-the-original-catalog-as-context}

아니요. 지식 소스가 에이전트 컨텍스트로서 카탈로그를 대체하므로 둘 다 연결할 필요가 없습니다. 지식 소스를 생성할 때 에이전트에 필요한 카탈로그 필드만 포함하세요.

### 지식 소스의 효과를 어떻게 평가해야 하나요? {#how-should-i-evaluate-the-efficacy-of-knowledge-source}

일반 카탈로그를 참조하는 기존 에이전트를 복제하고, 동등한 지식 소스를 참조하도록 전환합니다. 에이전트 콘솔에서 몇 가지 테스트 호출을 실행하여 정확성을 확인한 다음, 배포된 위치에서 기존 에이전트를 교체하거나, 이전 에이전트와 새 에이전트를 A/B 테스트(실험 경로 단계 사용)하여 성과 영향을 파악하는 것을 고려하세요.