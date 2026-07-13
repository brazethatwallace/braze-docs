---
nav_title: Use case
article_title: "사용 사례: 시청 후 콘텐츠 발견 유도"
description: "이 예시는 가상의 브랜드가 Braze AI 아이템 추천을 사용하여 주요 고객 순간에 개인화된 콘텐츠 및 제품 제안을 제공하는 방법을 보여줍니다."
page_type: tutorial
---

# 사용 사례: 시청 후 콘텐츠 발견 유도 {#use-case-drive-content-discovery-after-viewing}

> 이 예시는 가상의 브랜드가 Braze AI 아이템 추천을 사용하여 주요 고객 순간에 개인화된 콘텐츠 및 제품 제안을 제공하는 방법을 보여줍니다. 추천 로직이 참여를 개선하고, 전환율을 높이며, 수동 작업을 줄이는 방법을 알아보세요.

카밀라가 큐레이션된 영화와 시리즈를 제공하는 스트리밍 플랫폼인 MovieCanon의 CRM 매니저라고 가정해 봅시다.

카밀라의 목표는 시청자가 무언가를 다 보고 난 후에도 계속 참여하도록 하는 것입니다. 역사적으로 MovieCanon의 "당신이 좋아할 만한 것" 메시지는 광범위한 장르 매칭을 기반으로 하여 임의의 시간에 전송되었습니다—종종 세션 후 몇 시간 또는 며칠 후에 전송되었습니다. 참여율이 낮았고, 그녀의 팀은 더 나은 방법이 있을 것이라는 것을 알고 있었습니다.

[AI 아이템 추천]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai)을 사용하여 카밀라는 각 시청자의 시청 기록에 따라 새로운 제목을 자동으로 추천하는 시스템을 설정합니다. 이는 사용자가 영화나 에피소드를 다 보고 난 직후에 전달됩니다. 이는 사용자가 실제로 다음에 보고 싶어할 콘텐츠를 발견하도록 돕고 플랫폼에 계속 참여하도록 하는 더 스마트하고 개인화된 방법입니다.

![인앱 메시지: "다음은 당신을 위해 준비했습니다. '태양의 유목민'을 시청했기 때문에"라는 문구와 함께 이미지, 제목, 설명 및 "지금 보기" 또는 다음 추천으로 "건너뛰기" CTA가 포함되어 있습니다.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

이 튜토리얼은 카밀라가 어떻게 다음을 구축하는지 안내합니다:

- 사용자가 무언가를 다 보고 난 후에 트리거되는 개인화된 메시지
- 시청자의 선호에 맞춘 추천—MovieCanon의 카탈로그에서 자동으로 가져와 메시지에 삽입됩니다

## 1단계: 추천 모델 생성 {#step-1-create-a-churn-prediction-model}

카밀라는 사용자가 무언가를 다 보고 난 후 관련 제목을 표시할 추천을 만드는 것으로 시작합니다. 그녀는 이를 동적으로 만들고 싶어 하며, 사용자가 최근에 본 것에 따라 다른 제안을 받도록 합니다.

1. Braze 대시보드에서 카밀라는 **AI 아이템 추천**으로 이동합니다.
2. 그녀는 새로운 추천을 만들고 이름을 "시청 후 제안"으로 지정합니다.
3. 추천 유형으로 그녀는 **AI 개인화**를 선택하여, 각 사용자가 과거 행동에 기반한 맞춤형 추천을 볼 수 있도록 합니다.
4. 그녀는 **사용자가 이전에 상호작용한 항목을 추천하지 않음**을 선택하여 사용자가 이미 본 항목에 대한 추천을 받지 않도록 합니다.
5. 그녀는 MovieCanon의 현재 콘텐츠 라이브러리를 포함하는 카탈로그를 선택합니다. 카밀라는 카탈로그 선택을 추가하지 않으며, 카탈로그의 모든 항목이 추천 대상 항목으로 적합하도록 합니다.
6. 카밀라는 완료된 조회를 추적하는 `Watched Content` 커스텀 이벤트에 추천을 연결하고, **등록정보 이름**을 콘텐츠의 제목으로 설정합니다.
7. 그녀는 추천을 생성합니다.

## 2단계: 인앱 메시지 설정 {#step-2-set-up-an-in-app-message}

추천 훈련이 완료된 후, 카밀라는 사용자가 제목을 끝낸 직후에 도달하는 메시징 흐름을 구축합니다. 메시지에는 카탈로그에서 직접 가져온 세 가지 개인화된 제안 목록이 포함됩니다.

1. 카밀라는 드래그 앤 드롭 편집기를 사용하여 인앱 메시지 Campaign을 생성합니다.
2. 그녀는 트리거를 자신의 커스텀 이벤트로 설정합니다: `Watched Content`.
3. 그녀는 제목 이미지, 이름 및 "지금 보기" CTA가 포함된 다중 페이지 인앱 메시지를 디자인합니다.

!["개인화 추가" 모달이 Braze 편집기에서 열려 있으며, "항목 추천"이 개인화 유형으로 선택되어 있습니다.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. 메시지 본문에서 카밀라는 [개인화 추가 모달]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#inserting-pre-formatted-variables)을 사용하여 추천 제목의 이름, 설명 및 썸네일과 같은 변수를 Liquid를 사용하여 추가합니다. 이는 카탈로그에서 콘텐츠를 동적으로 채웁니다. 그녀는 `Last Watched Movie`에 대한 커스텀 속성을 템플릿화하여 사용자가 이 추천이 자신의 시청 기록에 기반하고 있음을 알 수 있도록 합니다.

![인앱 메시지 편집기에서 추천의 카탈로그 항목에서 특정 필드를 템플릿화하기 위한 원시 Liquid가 표시되어 있습니다.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

{% details 이미지에 사용된 Liquid 보기 %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. 카밀라는 페이지를 복제한 후 각 변수에서 Liquid 배열 {% raw %}(`{{ items[0]}}` 에서 `{{items[1]}}`){% endraw %}을 증가시켜 추천 목록의 다음 항목을 템플릿화합니다.

## 3단계: 측정 및 최적화 {#step-3-measure-and-optimize}

Campaign이 진행 중인 동안, 카밀라는 열람률, CTR 및 후속 시청 행동을 모니터링합니다. 그녀는 이전의 정적 추천 Campaign과 성과를 비교하고 더 높은 참여도와 사용자당 더 많은 콘텐츠 세션을 확인합니다.

그녀는 A/B 테스트도 계획하고 있습니다:

- 타이밍(즉시 대 시청 후 10분)
- 콘텐츠 레이아웃(캐러셀 대 목록)
- CTA 변형("지금 보기" 대 "대기줄에 추가")

이벤트 기반 메시징과 AI 아이템 추천을 결합함으로써, 카밀라는 콘텐츠 발견을 자동화된 개인화 경험으로 전환합니다. MovieCanon은 추측 없이 사용자 참여를 유지하며, 세션 깊이를 높이고 고객이탈을 줄이기 위해 적절한 시점에 관련 콘텐츠를 제공합니다.