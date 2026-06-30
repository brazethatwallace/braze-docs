---
nav_title: 기능
article_title: Operator로 할 수 있는 것
page_order: 1
page_type: reference
toc_headers: h2
description: "이 참조 문서에서는 BrazeAI Operator™를 통해 사용할 수 있는 AI 작업(카피라이팅, Liquid, 이미지 생성, 데이터 변환 코드, 콘텐츠 검토 등)을 다룹니다."
---

# Operator로 할 수 있는 것 {#operator-capabilities}

> 이전에 독립형 어시스턴트로 제공되던 AI 기능은 이제 [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator)를 통해 이용할 수 있습니다. Operator는 대시보드에 내장되어 있으며 워크스페이스(브랜드 가이드라인, 속성, 연결된 콘텐츠, 현재 작업 중인 페이지)를 이해하므로, 이전 어시스턴트보다 더 맥락을 인식한 결과물을 생성합니다.

각 작업마다 다른 도구를 열 필요 없이, 원하는 내용을 자연어로 설명하면 Operator가 맥락에 맞게 처리합니다. 대화를 이어가며 다른 톤, 더 짧은 버전, 번역 등을 요청할 수도 있으며 처음부터 다시 시작할 필요가 없습니다. Operator는 또한 [액션 카드]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions)를 통해 변경 사항을 제안하고 실행할 수 있으며, 적용 전에 사용자가 검토할 수 있습니다.

## 필수 조건 {#prerequisites}

Operator는 사용자와 동일한 권한을 가지므로, 특정 동작에는 해당 영역에 대한 관련 권한이 필요합니다. 예를 들어, 이미지를 생성하려면 *미디어 라이브러리 자산 편집* 권한이 필요합니다. 진입점이 보이지 않는 경우 관리자에게 권한을 확인하세요. 자세한 내용은 [권한 목록]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)을 참조하세요.

## Operator를 통해 사용할 수 있는 기능 {#whats-available-through-operator}

기존의 모든 진입점은 그대로 유지되므로 워크플로에 영향이 없습니다. 이러한 경험은 이제 Operator로 구동됩니다. 다음 표는 이전의 각 독립형 어시스턴트와 현재 위치를 매핑합니다.

| 이전 어시스턴트 | 기능 | 현재 위치 |
| --- | --- | --- |
| AI 카피라이터 | 제품 이름 또는 설명에서 마케팅 카피 생성 | SMS, 푸시, HTML 이메일, Canvas 작성기의 새로운 **Ask Operator** 아이콘 |
| AI Liquid 어시스턴트 | 개인화를 위한 Liquid 생성 | SMS, 푸시, HTML 이메일, Canvas 작성기의 새로운 **Ask Operator** 아이콘 |
| AI 이미지 생성기 | 텍스트 프롬프트에서 미디어 라이브러리용 이미지 생성 | 미디어 라이브러리의 새로운 **Generate with Operator** 버튼 |
| 데이터 변환 AI 코파일럿 | 변환 코드 생성 | 데이터 변환 페이지의 **Insert Code** 버튼 |
| 콘텐츠 검토 | 맞춤법, 문법, 톤, 부적절한 언어, 잔여 코드 확인 | **테스트** 탭의 **Review with Operator** 버튼 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Operator를 통해 사용할 수 있는 기능" }

## 브랜드 가이드라인 적용 {#apply-brand-guidelines}

Operator는 워크스페이스에 구성된 브랜드 가이드라인을 사용하여 생성된 카피, 템플릿, 이미지가 브랜드의 보이스, 톤, 스타일과 일치하도록 합니다. 브랜드 가이드라인을 설정하려면 **콘텐츠** > **브랜드 가이드라인**으로 이동하세요. 자세한 내용은 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)을 참조하세요. Operator와 함께 브랜드 가이드라인을 적용하는 방법에 대한 자세한 내용은 [브랜드 가이드라인 적용]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines)을 참조하세요.

## 카피 생성 {#generate-copy}

Operator를 사용하여 어디서든 카피를 브레인스토밍하거나 생성할 수 있지만, 메시지 작성기에서 직접 사용할 때 가장 좋은 경험을 얻을 수 있습니다. 작성기에서는 Operator가 작성 중인 메시지와 함께 작업할 수 있습니다. 제품이나 Campaign(캠페인)을 설명하면 Operator가 검토하고 삽입할 수 있는 카피를 반환합니다.

Operator는 독립형 카피라이터보다 몇 가지 면에서 개선되었습니다:

- [브랜드 가이드라인](#apply-brand-guidelines)이 구성되어 있으면 자동으로 적용합니다.
- [페이지 인식 컨텍스트]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context)를 사용하므로 작업 중인 채널이나 메시지를 다시 설명할 필요가 없습니다. 페이지를 인식하기 때문에 처음부터 생성하는 대신 기존 메시지를 편집하거나 다듬는 데에도 사용할 수 있습니다.
- [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)과 이벤트를 조회할 수 있으므로, 실제 Liquid를 사용한 개인화된 카피 추천을 요청할 수 있습니다.
- 대화를 이어가며 반복할 수 있습니다. 예를 들어, 다른 톤, 더 짧은 버전, 번역을 요청할 수 있습니다.

### 톤 {#generate-copy-tones}

생성된 카피의 톤은 프롬프트에 의해 결정됩니다. 원하는 스타일을 설명하세요. 예를 들어, 격식체, 캐주얼, 긴급, 눈길을 끄는 등의 스타일을 지정하면 Operator가 그에 맞게 출력을 조정합니다. 후속 프롬프트에서 톤을 다듬을 수도 있습니다. 예를 들어, 더 편안한 버전이나 더 세련된 버전을 요청할 수 있습니다. [브랜드 가이드라인](#apply-brand-guidelines)이 구성되어 있으면 Operator가 자동으로 적용하여 카피가 브랜드의 보이스와 일관되게 유지됩니다.

### 프롬프트 예시 {#generate-copy-example-prompts}

{% include copy_block.html content="Write a short, eye-catching push notification announcing our summer sale." %}

{% include copy_block.html content="Rewrite this subject line in a more casual tone." %}

{% include copy_block.html content="Translate this copy into Spanish." %}

## Liquid 생성 {#generate-liquid}

모든 메시지 작성기에서 Operator를 열어 개인화를 위한 Liquid를 생성하고 다듬을 수 있습니다. Operator는 [Liquid 구문]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), 표준 및 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 이해하며, 코드가 무엇을 하는지 설명할 수 있습니다.

### Liquid를 생성할 수 있는 위치 {#generate-liquid-supported-channels}

카피라이팅과 마찬가지로, 어디서든 Operator에게 Liquid 생성을 요청할 수 있으며 모든 채널과 메시지 작성기에서 작동합니다. 메시지 작성기 내에서 사용할 때 가장 좋은 결과를 얻을 수 있으며, 이 경우 Operator가 작성 중인 메시지의 전체 컨텍스트를 파악합니다.

### Liquid 기능 {#generate-liquid-attributes}

Operator는 Liquid에 매우 능숙합니다. 워크스페이스의 데이터를 기반으로 복잡한 Liquid 로직을 생성할 수 있으며, 여기에는 예시 값을 찾기 위한 [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs) 데이터 조회도 포함됩니다. 또한 Campaign의 기존 Liquid를 검토하고 설명할 수 있습니다.

### 모범 사례 {#generate-liquid-best-practices}

#### 자연어 사용 {#generate-liquid-use-natural-language}

Operator는 자연어를 이해하도록 훈련되었습니다. 도움을 요청할 때 동료에게 말하듯이 대화하세요. 이렇게 하면 Operator가 요구 사항을 이해하고 정확한 지원을 제공하는 데 도움이 됩니다.

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

### 프롬프트 예시 {#generate-liquid-example-prompts}

{% tabs local %}
{% tab Liquid 소개 %}

{% include copy_block.html content="What is Liquid, and how can it help me enhance the personalization of my marketing campaigns within Braze?" %}

{% include copy_block.html content="What types of data can I use in Liquid to personalize my marketing messages, such as demographic information or past purchases?" %}

{% include copy_block.html content="Can you give me some examples of how Liquid is used in marketing campaigns to increase engagement and conversion rates?" %}

{% include copy_block.html content="What are some common use cases for Liquid in text messages for summer sales, such as abandoned cart reminders or personalized promotions?" %}

{% endtab %}
{% tab 개인화 %}

{% include copy_block.html content="Add a countdown to this message that shows the time until the user's flight." %}

{% include copy_block.html content="Personalize this message with the user's first name, with a fallback if it's missing." %}

{% include copy_block.html content="Improve this Liquid so it's easier to read." %}

{% include copy_block.html content="Create a message that shows different content based on my customer's loyalty status. If we don't know about their loyalty status, send a fallback message." %}

{% include copy_block.html content="Write a dynamic message that includes a user's favorite product and their last purchase date. If there's no last purchase, abort the message." %}

{% include copy_block.html content="Write me Liquid to encourage someone to click my message that includes a countdown with how much time is left. If the offer has expired, abort the message." %}

{% include copy_block.html content="Help me write a message to encourage users to come back and check out if they have items remaining in their cart." %}

{% include copy_block.html content="Write Liquid to personalize a message based on a customer's country. I want to fill in the message with the country's name. If we don't have either of them, suggest they click on a link to update their profile." %}

{% include copy_block.html content="How can I personalize a welcome message with a user's first name and write different copy based on the user's gender?" %}

{% include copy_block.html content="Write Liquid to display different messages based on a custom attribute, \"CUSTOM_ATTRIBUTE_NAME\" and its value. There are six different options I could send. If there's no value for the custom attribute, I want to send a placeholder message." %}

{% endtab %}
{% endtabs %}

## 이미지 생성 {#generate-images}

Operator는 OpenAI의 AI 시스템이자 Braze 서드파티 제공업체인 [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)을 사용하여 이미지를 생성합니다. 이를 통해 자연어 설명에서 사실적인 이미지와 아트를 만들 수 있습니다.

[미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)에서 **자산 업로드** 패널의 **Generate with Operator**를 선택하세요. 원하는 이미지를 설명하면 Operator가 이미지를 생성하고 미디어 라이브러리에 직접 저장합니다.

### 프롬프트 팁 {#generate-images-prompt-tips}

- 주제, 스타일, 분위기, 색상을 구체적으로 설명하세요. 세부 정보를 많이 포함할수록 더 좋은 결과를 얻을 수 있습니다.
- 텍스트 입력만 가능하며, 참조 이미지 업로드는 지원되지 않습니다.
- Operator 프롬프트에서 [브랜드 가이드라인](#apply-brand-guidelines)을 컨텍스트로 적용하면, Operator가 생성된 이미지에 직접 적용하여 결과물이 브랜드의 시각적 스타일을 반영합니다.
- 이미지 생성은 일일 Operator 사용 한도에 포함됩니다. 자세한 내용은 [제한 사항]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting#limitations)을 참조하세요.

### 프롬프트 예시 {#generate-images-example-prompts}

{% include copy_block.html content="Generate a bright, summery banner image of a beach scene for an email header." %}

{% include copy_block.html content="Create a minimalist product background in our brand colors." %}

## 데이터 변환 코드 생성 {#generate-data-transformation-code}

[데이터 변환]({{site.baseurl}}/user_guide/data/unification/data_transformation) 편집기에서 **Insert Code**를 선택하여 수신 웹훅 페이로드를 유효한 Braze API 요청으로 변환하는 변환 코드를 생성합니다.

변환을 만드는 단계별 지침은 [변환 만들기]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation)를 참조하세요.

### 프롬프트 예시 {#generate-data-transformation-example-prompts}

{% include copy_block.html content="Write transformation code that maps this survey webhook to a custom event on the user's profile." %}

{% include copy_block.html content="Update this transformation to identify users by email address instead of external ID." %}

## 콘텐츠 품질 검토 {#review-content-quality}

SMS, Android 푸시, iOS 푸시, 전통적인 인앱 메시지의 **테스트** 탭에서 **Review with Operator**를 선택하여 발송 전에 콘텐츠를 검토할 수 있습니다. 기본적으로 Operator는 Campaign의 맞춤법 및 문법 오류, 브랜드에 맞지 않거나 부적절한 톤, 공격적인 언어, 잔여 코드, 테스트 콘텐츠 또는 렌더링되지 않은 Liquid를 검토하고 발견된 문제의 수정 방법을 추천합니다. 프롬프트에서 Operator가 콘텐츠를 검토하는 방식을 직접 맞춤 설정하도록 요청할 수도 있습니다.

### Operator에게 확인을 요청할 수 있는 항목 {#review-content-quality-supported-features}

기본 검토 외에도 Operator가 특정 검사에 집중하도록 지시할 수 있습니다. 다음 항목을 확인하도록 프롬프트하는 것을 고려하세요:

| 검사 항목 | 요청 방법 |
| --- | --- |
| 맞춤법 및 문법 | Operator에게 맞춤법 및 문법 오류를 교정하고 콘텐츠의 정확성을 높이는 수정 사항을 제안하도록 요청하세요. |
| 톤 | Operator에게 톤이 의도한 커뮤니케이션 스타일과 일치하는지 평가하고 오해의 소지가 있는 부분을 표시하도록 요청하세요. |
| 공격적인 언어 | Operator에게 잠재적으로 공격적이거나 부적절한 언어를 스캔하여 수정하고 메시징을 존중하는 방식으로 유지하도록 요청하세요. |
| 의도하지 않은 콘텐츠 | Operator에게 의도치 않게 추가된 잔여 코드, 마크업 또는 테스트 메시지(테스트 사용자에게 렌더링되지 않은 Liquid 포함)를 찾도록 요청하세요. |
| 다른 언어 | Operator에게 다른 언어로 작성된 콘텐츠를 검토하도록 요청하세요. 영어 이외의 콘텐츠에 대한 지원은 다를 수 있으므로 결과를 신중하게 검토하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Operator에게 확인을 요청할 수 있는 항목" }

### 모범 사례 {#review-content-quality-best-practices}

콘텐츠 검토를 최대한 활용하려면 다음을 고려하세요:

- **메시지를 교정하세요:** 콘텐츠 검토가 오류를 식별하는 데 도움이 될 수 있지만, 콘텐츠를 수동으로 교정하는 것은 여전히 필수적입니다. AI가 생성한 제안을 유용한 가이드로 활용하되, 정확성을 보장하기 위해 본인의 판단을 사용하세요.
- **톤 분석을 이해하세요:** 톤 분석 결과는 주관적이며 AI 모델의 이해에 기반합니다. 유용한 인사이트를 제공할 수 있지만, 의도한 톤과 대화 맥락을 고려하여 적절한 조정을 하세요.
- **표시된 공격적인 언어를 다시 확인하세요:** 공격적인 언어 감지는 강력하게 설계되었지만, 간혹 오탐지가 발생할 수 있습니다. 표시된 섹션을 신중하게 검토하고 필요에 따라 적절한 변경을 하세요.

### 프롬프트 예시 {#review-content-quality-example-prompts}

{% include copy_block.html content="Review this push notification for spelling, grammar, and tone, and flag any unrendered Liquid or leftover test content before I send it." %}

{% multi_lang_include brazeai/generative_ai/policy.md %}

## 데이터 프라이버시 및 보안 {#data-privacy-and-security}

Operator는 OpenAI와 통합하여 출력을 생성합니다. Braze가 OpenAI에 보내는 정보, 해당 데이터의 사용 방식, 지적 재산권에 대한 자세한 내용은 [OpenAI와의 데이터 사용 방식]({{site.baseurl}}/user_guide/brazeai/operator#how-data-is-used-with-openai)을 참조하세요.

## 다음 단계 {#next-steps}

- [Operator 시작하기]({{site.baseurl}}/user_guide/brazeai/operator): Operator에 접근하고 사용하기
- [액션 검토]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Operator가 제안한 변경 사항을 검토하고 승인하기
- [문제 해결]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): 일반적인 문제와 해결 방법 참조