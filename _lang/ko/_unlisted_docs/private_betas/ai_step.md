---
nav_title: AI 단계
article_title: AI 단계
permalink: /ai_step/
description: "이 참조 문서에서는 Canvas AI 단계에 대해 다룹니다."
tool:
  - Canvas
hidden: true
---

# AI 단계 {#ai-step}

> Canvas 내의 AI 단계는 ChatGPT를 활용하여 사용자 생성 입력(예: 설문조사 피드백)을 해석하고, 적절한 응답을 결정하며, 메시지를 트리거하는 등 개인화된 마케팅을 자동화합니다. 이 모든 과정이 Braze 내에서 이루어집니다. ChatGPT는 서드파티인 OpenAI에 의해 구동됩니다.

{% alert note %}
AI 단계는 현재 베타 기능으로 제공됩니다. 이 베타 체험에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## AI 단계 생성하기 {#create-ai-step}

1. Canvas에 새 단계를 추가하고 **AI Step**을 선택합니다. <br><br>![Canvas 빌더의 AI 단계][1]{: style="max-width: 30%;"}<br><br>
2. AI가 다양한 사용자 동작에 어떻게 응답할지 알려주는 프롬프트를 작성합니다. 응답에는 커스텀 속성 업데이트 또는 메시지 발송이 포함될 수 있습니다. 이 프롬프트는 Liquid를 사용하여 다양한 사용자 속성이나 입력에 따라 서로 다른 응답 출력을 할당할 수 있습니다. <br><br>동일한 Canvas 내에서 향후 메시지를 개인화하는 데 사용할 수 있는 출력을 할당하려면, 특정 이름(예: "message" 및 "sentiment score")으로 변수를 저장하는 프롬프트를 작성합니다. <br><br> ![생성된 감정 점수를 기반으로 개인화된 메시지를 보내기 위해 AI 단계 설정에서 사용된 샘플 AI 프롬프트. 이 예시는 '고객 감정 응답' 섹션에 설명되어 있습니다.][2] <br><br>
3. **미리보기** 탭을 사용하여 특정 사용자에 대해 AI가 어떤 출력을 생성할 수 있는지 테스트합니다.<br><br> ![이름이 Cameron, 제품명이 shoes, 텍스트가 'decent but my shoe lace already broke'인 세 가지 매개변수에 대해 AI가 생성한 개인화된 메시지를 보여주는 AI 단계 설정의 미리보기 탭][3]

## Liquid를 사용하여 AI 출력 참조하기 {#referencing-ai-output-using-liquid}

이후 단계에서 AI 출력을 참조하려면 Liquid 로직 `{% raw %}{{ai_step_output.${key_name}}}{% endraw %}`를 삽입합니다. AI 단계의 프롬프트 내에서 `key_name`을 설정할 수 있습니다.

예를 들어, "message"와 "sentiment score" 변수를 사용하는 경우, `{% raw %}{{ai_step_output.${message}}}{% endraw %}`를 사용하여 동일한 Canvas 내의 후속 메시지를 개인화할 수 있습니다.

또한 사용자 업데이트 캔버스 단계를 사용하여 AI 단계의 출력을 커스텀 속성으로 기록할 수 있으며, 여기서 AI 단계 출력(예: `{% raw %}{{ai_step_output.${sentiment_score}}}{% endraw %}`)을 읽습니다. 출력이 커스텀 속성으로 저장되지 않으면, 동일한 Canvas의 후속 단계 외에는 다른 곳에서 사용할 수 없습니다.

### 컨텍스트 단계 사용하기 {#using-context-steps}

[Canvas 컨텍스트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works)를 활용하여 Canvas 후반부에서 출력을 쉽게 참조할 수 있습니다.

다음은 AI 단계 이후에 설정할 수 있는 컨텍스트 단계의 예시입니다. 이 예시에서 이전 AI 단계에는 감정 점수와 메시지에 대한 AI 단계 출력이 포함되어 있으며, 이 컨텍스트 단계는 후속 단계에서 사용할 수 있는 `sentiment_score` 및 `message` 변수를 생성합니다.

![두 개의 변수 'sentiment_score'와 'message'가 있는 컨텍스트 단계][6]

또한 컨텍스트 변수의 값에 따라 사용자를 다른 경로로 보내는 오디언스 경로 단계를 만들 수도 있습니다. 이 예시에서는 감정 점수에 따라 사용자를 다르게 타겟팅할 수 있습니다. 또한 Liquid를 사용하여 {% raw %}`{{context.${message}}}`{% endraw %}를 삽입함으로써 이메일 본문에 메시지 변수를 포함할 수 있습니다.

![감정 점수가 80 이상인 필터가 적용된 'Group 1'이라는 오디언스 그룹이 있는 오디언스 경로 단계][7]

## AI 단계 측정기준 {#ai-step-metrics}

AI 단계에는 다음과 같은 단계 수준 측정기준이 있습니다.

| 측정기준 | 설명 |
| _다음 단계로 진행_ | Canvas의 다음 단계로 진행한 사용자 수 |
| _Canvas 종료_ | AI 단계가 마지막 단계인 경우 Canvas를 종료한 사용자 수 |
| _출력 성공_ | AI 단계가 성공적으로 출력을 생성한 사용자 수 |
| _출력 실패_ | AI 단계가 출력을 생성하지 못한 사용자 수. 이 경우 사용자는 여전히 후속 단계로 진행합니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### AI 단계 출력 이해하기 {#understanding-your-ai-step-outputs}

Braze가 AI 단계의 출력을 폐기하고 고객을 다음 단계로 보내는 몇 가지 시나리오가 있습니다.

- 출력이 1,024자를 초과하는 경우
- 출력이 JSON 형식이 아닌 경우
- 프롬프트가 OpenAI의 [모더레이션](https://platform.openai.com/docs/guides/moderation/overview) 요구 사항을 충족하지 못하는 경우(부적절한 사용자 생성 콘텐츠를 감지)

## AI 단계 활용 사례 {#ai-step-use-cases}

### 고객 감정 응답 {#customer-sentiment-responses}

[AI 단계 생성하기](#create-ai-step)의 예시에서 보여준 것처럼, 고객 피드백에서 생성된 감정 점수를 기반으로 후속 메시지를 보내도록 AI에 요청할 수 있습니다.

- **긍정적인 감정 점수:** 사용자에게 리뷰를 남기도록 요청하는 푸시 알림을 트리거합니다
- **중간 감정 점수:** 사용자에게 추가 도움이 필요한지 묻는 이메일을 트리거합니다
- **낮은 감정 점수:** 고객지원 담당자가 세심한 후속 조치를 작성할 수 있도록 사용자 헬프 데스크에 알리는 웹훅을 트리거합니다

#### AI 프롬프트 예시 {#example-ai-prompt}

이 예시는 [AI 단계 생성하기](#create-ai-step)에서 사용되었습니다.

고객이 "`{% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}`"를 구매했으며, 다음과 같은 제품 피드백을 남겼습니다: "`{% raw %}{{canvas_entry_properties.${text}}}{% endraw %}`". 0에서 100 사이의 정수로 감정 점수를 생성합니다. 그런 다음 개인화된 메시지를 작성합니다. 이 프롬프트는 "message"와 "sentiment score" 두 가지 변수를 반환해야 합니다.

### 설문조사 후속 조치 {#survey-follow-ups}

자유 응답 섹션이 포함된 인앱 또는 인브라우저 설문조사를 실행하는 경우, AI 단계를 사용하여 자유 응답을 분석하고 적절하게 후속 조치를 취할 수 있습니다.

예를 들어, 화장품 소매업체가 "올해의 뷰티 어워드에 어떤 제품을 추천하고 싶으신가요?"라는 설문조사를 진행하는 경우, 사용자가 선호하는 제품 유형과 브랜드에 대한 속성을 식별하고 할당하는 프롬프트를 사용한 다음, 이 데이터를 기반으로 향후 콘텐츠를 개인화할 수 있습니다.

#### AI 프롬프트 예시

사용자의 응답을 사용하여 선호하는 브랜드를 식별합니다. 그런 다음 설문조사를 작성해 주셔서 감사하다는 메시지를 작성하고, 뷰티 전문가들도 해당 브랜드를 좋아한다는 내용을 포함합니다. 이 프롬프트는 "message"와 "favorite brand" 두 가지 변수를 반환해야 합니다.

![설문조사 응답 매개변수 'I love Beauty Brand face creams'에 대해 AI가 생성한 개인화된 메시지를 보여주는 AI 단계 설정의 미리보기 탭. 사용자에게 설문조사 작성에 감사하고 페이스 크림을 추천합니다.][4]

### 동작 기반 추천 {#behavior-driven-recommendations}

고객은 AI에 사용자 동작을 분석하고 추천 메시지를 보내도록 요청할 수 있습니다.

예를 들어, 사용자의 최근 50건의 구매를 분석하고 가장 많이 구매한 카테고리를 새로운 커스텀 속성으로 설정하는 프롬프트를 만들 수 있습니다. 그런 다음 각 사용자가 선호하는 카테고리에 대한 개인화된 이메일 추천을 보낼 수 있습니다.

#### AI 프롬프트 예시

고객이 다음 제품을 구매했습니다: "`{% raw %}{{custom_attribute.${Products Purchased}}}{% endraw %}`". 사용자가 가장 많이 구매한 제품 카테고리를 식별합니다. 이 프롬프트는 "most purchased category"에 대한 새 변수를 반환해야 합니다.

![가장 많이 구매한 카테고리 매개변수에 대해 AI가 생성한 'book' 변수를 보여주는 AI 단계 설정의 미리보기 탭][5]

## 사용량 제한 {#rate-limits}

회사당 분당 10건의 요청(RPM) 제한이 있습니다. 이는 모든 AI 단계에서 주어진 1분 동안 최대 10명의 사용자가 해당 단계를 받을 수 있으며, 10명을 초과하는 사용자는 자동으로 다음 단계로 진행된다는 의미입니다. 다음 1분이 시작되면 사용자가 다시 AI 단계를 받을 수 있지만, 사용량 제한에 도달한 이전 사용자는 재시도되지 않습니다.

## AI 단계 제한 사항 {#ai-step-limitations}

- 이 기능은 GPT-3.5를 활용합니다.
- 이 기능은 Braze OpenAI API 키를 사용합니다. 자체 OpenAI API 키는 사용할 수 없습니다.
- 워크스페이스당 분당 5건의 요청(RPM), 회사당 분당 10건의 요청(RPM) 제한이 있습니다.
- 이 기능은 HIPAA(미국의료정보보호법)를 준수하지 않으며, 고객은 개인 식별 정보(PII) 또는 보호 대상 건강 정보(PHI)를 전송해서는 안 됩니다.

## 내 데이터는 어떻게 사용되고 OpenAI로 전송되나요? {#how-is-my-data-used-and-sent-to-openai}

Braze가 OpenAI를 활용하는 것으로 식별한 Braze AI 기능을 통해 AI 출력("출력")을 생성하기 위해, Braze는 메시지 콘텐츠, 최종 사용자 감정, 브랜드 가이드라인, 과거 Campaign 데이터 또는 기타 해당 입력("입력")과 같은 프롬프트를 [OpenAI](https://openai.com/)로 전송합니다. AI 단계와 함께 Braze의 ChatGPT 통합을 사용할 때 개인 데이터가 OpenAI로 전송되는 경우, OpenAI는 귀하와 Braze 간의 DPA에 명시된 대로 Braze의 하위 처리자로서 역할을 합니다. AI 단계와 자체 대규모 언어 모델(LLM)을 통합하는 경우, 해당 LLM의 제공자는 서드파티 제공자로 간주되며, 개인 데이터의 처리는 귀하와 해당 서드파티 제공자 간의 약관에 따릅니다. [OpenAI의 API 플랫폼 약속](https://openai.com/enterprise-privacy/)에 따라, Braze를 통해 OpenAI의 API로 전송된 데이터는 OpenAI 모델을 학습하거나 개선하는 데 사용되지 않으며, OpenAI 시스템에서 30일 후에 삭제됩니다. 귀하와 Braze 사이에서 출력은 귀하의 지적 재산입니다. Braze는 해당 출력에 대한 저작권 소유권을 주장하지 않습니다. Braze는 출력을 포함한 AI 생성 콘텐츠 전반에 대해 어떠한 종류의 보증도 하지 않습니다.

[1]: {% image_buster /assets/unlisted_docs/img/ai_step1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/ai_step2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/ai_step3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/ai_step4.png %}
[5]: {% image_buster /assets/unlisted_docs/img/ai_step5.png %}
[6]: {% image_buster /assets/unlisted_docs/img/ai_step6.png %}
[7]: {% image_buster /assets/unlisted_docs/img/ai_step7.png %}