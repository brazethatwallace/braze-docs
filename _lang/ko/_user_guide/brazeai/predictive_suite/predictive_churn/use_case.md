---
nav_title: Use case
article_title: "사용 사례: 적시 콘텐츠로 고객이탈 줄이기"
description: "이 예시는 가상의 브랜드가 Predictive Churn을 사용하여 사용자 이탈을 사전에 줄이는 방법을 보여줍니다."
page_type: tutorial
---

# Use case: 적시 콘텐츠 재참여로 고객이탈 줄이기 {#use-case-reduce-churn-with-timely-content-re-engagement}

> 이 예시는 가상의 브랜드가 Predictive Churn을 사용하여 사용자 이탈을 사전에 줄이는 방법을 보여줍니다. 고객이탈이 발생할 때까지 기다리는 대신, 위험에 처한 사용자를 예측하고 그들이 여전히 활동 중일 때 맞춤형 메시지를 전달합니다.

Camila는 독립 영화, 다큐멘터리 및 해외 시리즈를 위한 스트리밍 플랫폼인 MovieCanon의 CRM 매니저라고 가정해 보겠습니다.

Camila의 팀은 걱정스러운 추세를 발견했습니다: 사용자가 가입하고 영화를 한두 편 스트리밍한 후 사라집니다. 역사적으로 그들은 일주일 후에 일반적인 "보고 싶어요" 이메일을 보내려고 했지만, 전환율이 3%에 불과하여 너무 적고 너무 늦었습니다. 대부분의 사용자는 재참여하지 않으며, 고객이탈은 불가피해집니다.

Camila는 이를 바꾸고 싶어합니다. 고객이탈이 발생한 후에 반응하는 대신, 그녀는 Predictive Churn을 사용하여 다음 14일 이내에 비활성화될 가능성이 있는 사용자를 식별합니다—이는 그녀의 팀이 여전히 활동 중인 사람들을 재참여시킬 기회를 제공합니다.

이 튜토리얼은 Camila가 어떻게 하는지를 안내합니다:

- 사용자 행동을 기반으로 한 고객이탈 예측 모델 생성
- 위험 수준에 따라 사용자 세분화
- 가장 위험에 처한 사용자에게 맞춤형 재참여 Campaign 구축
- Campaign 분석을 사용하여 영향 평가

## 1단계: 고객이탈 예측 모델 생성 {#step-1-create-a-churn-prediction-model}

Camila는 피하고 싶은 결과, 즉 사용자가 비활성화되는 것을 모델링하는 것으로 시작합니다. MovieCanon에서 고객이탈은 14일 이내에 스트리밍을 시작하지 않는 것을 의미하므로, 그녀가 예측하고자 하는 행동입니다.

1. Braze 대시보드에서 Camila는 **Analytics** > **Predictive Churn**으로 이동합니다.
2. 그녀는 새로운 고객이탈 예측을 생성하고 이름을 "2주 내 고객이탈 위험"으로 지정합니다.
3. 고객이탈을 정의하기 위해 그녀는 `do not`과 커스텀 이벤트 `stream_started`를 선택하여 활성 참여를 나타냅니다.
4. 그녀는 예측 기간을 14일로 설정합니다—즉, 모델은 새로운 스트림을 시작하지 않고 14일 동안 갈 가능성이 있는 사용자를 식별합니다.

![고객이탈 정의: 지난 14일 동안 커스텀 이벤트 "stream_started"를 수행하지 않은 사용자를 고객이탈로 정의합니다.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5. 그녀는 지난 30일 동안 관련 이벤트를 트리거한 모든 사용자를 포함하는 예측 오디언스를 선택하여 모델이 학습할 수 있는 충분한 최근 행동을 제공합니다.
6. 그녀는 예측 업데이트 일정을 주간으로 설정하여 점수가 최신 상태를 유지하도록 합니다.
7. 그녀는 **예측 생성**을 선택합니다.

그런 다음 모델은 최근 세션, 시청 빈도 및 콘텐츠 상호작용과 같은 행동을 분석하여 이탈을 예측하는 패턴을 발견하기 위해 훈련을 시작합니다. Camila는 한 시간 후에 예측 훈련이 완료되었다는 이메일을 받고, Braze에서 열어 [예측 품질]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#prediction_quality) 점수를 확인합니다. "좋음"으로 표시되어 있으며, 이는 모델의 예측이 정확하고 신뢰할 가능성이 높다는 것을 의미합니다. 모델의 성능에 자신감을 가진 그녀는 다음 단계로 나아갑니다.

## 2단계: 고객이탈 위험에 따라 사용자 세분화 {#step-2-segment-users-by-churn-risk}

모델 훈련이 완료된 후, Braze는 각 적격 사용자에게 0-100 사이의 [고객이탈 위험 점수]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/#churn_score)를 할당합니다.

타겟팅을 위한 시작 임계값을 결정하기 위해 Camila는 예측 오디언스 슬라이더를 사용하여 각 점수 범위에 얼마나 많은 사용자가 포함되는지와 해당 수준에서 예측의 정확성을 미리 봅니다. 그녀는 예상되는 참양성에 따라 범위와 정밀도를 조정합니다. 이를 바탕으로 그녀는 70 이상의 위험 점수를 타겟팅하기로 결정합니다.

1. Camila는 Braze에서 Segments로 이동합니다.
2. 그녀는 [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/)를 생성하고 [고객이탈 위험 점수 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#churn-risk-score)를 사용하여 그녀가 생성한 고객이탈 예측을 선택합니다:
   - **이탈 가능성:** 70 이상 점수

![70 이상의 고객이탈 위험 점수를 가진 사용자를 필터링하는 Segment.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## 3단계: 위험에 처한 사용자를 반복적인 재참여 콘텐츠로 타겟팅 {#step-3-target-at-risk-users-with-recurring-re-engagement-content}

예측과 Segment가 준비된 Camila는 매주 위험에 처한 사용자에게 자동으로 도달하는 반복 Campaign을 설정합니다.

1. Camila는 반복 Campaign을 생성하고 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/)을 활성화하여 각 메시지가 각 개별 사용자가 참여할 가능성이 가장 높은 시점에 전달되도록 합니다. 고정된 날짜와 시간에 의존하지 않습니다.
2. 그녀는 방금 생성한 "이탈 가능성 높은" Segment를 타겟팅합니다.
3. 그녀는 Campaign 전환 이벤트를 커스텀 이벤트 `stream_started`로 설정하여 실제로 콘텐츠를 보러 돌아오는 사용자의 수를 추적합니다.
4. Camila는 이메일을 주요 채널로 선택합니다—이는 시각적으로 풍부한 형식으로 여러 개인화된 콘텐츠 선택을 강조할 수 있는 공간을 제공하면서 부담을 주지 않습니다. 이메일에는 다음이 포함됩니다:
   - [AI 아이템 추천]({{site.baseurl}}/user_guide/brazeai/item_recommendations/)에 의해 제공되는 개인화된 시청 목록, MovieCanon의 카탈로그에서 동적으로 선택됩니다
   - 사용자를 앱으로 직접 유도하는 행동 촉구

이것은 매주 MovieCanon이 필요한 사용자에게만 도달하도록 보장합니다—과도한 메시지 전송이나 추측이 없습니다.

### 예시 이메일 {#example-email}

- **제목란:** 이 제목들을 놓치지 마세요
- **헤더:** 당신의 다음 훌륭한 시청이 기다리고 있습니다
- **본문:** 한동안 재생 버튼을 누르지 않으셨나요? 걱정하지 마세요—당신을 위해 몇 가지 선택을 준비했습니다. 느리게 진행되는 스릴러부터 수상 경력이 있는 다큐멘터리까지, 여기 당신의 이름이 붙은 무언가가 있습니다.
- **CTA:** 더 많은 선택 보기

## 4단계: 성과 측정 {#step-4-measure-performance}

몇 주 후, Camila는 [Campaign 분석]({{site.baseurl}}/user_guide/channels/email/reporting/)을 확인하여 전략이 얼마나 잘 수행되고 있는지 평가합니다.

그녀는 다음과 같은 결과를 봅니다:

- *열람률:* 31%
- *클릭률:* 15%
- *전환율* (48시간 이내에 스트림 시작): 11%

기존 "보고 싶어요" Campaign(전환율이 약 3%였던)과 비교할 때, 이 새로운 흐름은 타겟 그룹의 고객이탈을 28% 줄입니다. 그녀는 사용자가 이탈하는 지점을 파악하기 위해 [퍼널 보고서]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/)를 자세히 살펴봅니다. 열람률과 클릭률이 강한 반면, 클릭과 전환 사이에 약간의 마찰이 있음을 발견하여 CTA 문구를 테스트하거나 레이아웃을 실험해 볼 것을 고려합니다.

장기적인 영향을 이해하기 위해, Camila는 또한 "이탈 가능성" Segment에 들어가는 사용자 수를 주마다 추적합니다. 이것은 그녀가 라이프사이클의 전반적인 건강 상태를 평가하고 더 넓은 수준에서 유지 전략을 수립하는 데 도움이 됩니다. 마지막으로, 그녀는 고객이탈 예측의 [예측 분석]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/) 페이지를 다시 방문하여 예측된 이탈자와 실제 이탈자를 비교합니다—이는 모델이 예상대로 작동하는지 확인하는 유용한 점검입니다.

이러한 인사이트를 바탕으로 Camila는 제목란 A/B 테스트, 다양한 타이밍 기간 테스트, 인앱 메시지에서 캐러셀 스타일 추천과 같은 콘텐츠 형식 실험을 계획합니다.

Predictive Churn, Intelligent Timing, AI 기반 개인화를 통해 Camila의 팀은 단순히 고객이탈에 반응하는 것이 아니라—고객이탈을 앞서 나가고 있습니다. 그리고 그녀의 Campaign은 백그라운드에서 조용히 실행되며, 적절한 시간에 적절한 사람들에게 그들이 실제로 관심을 가질 콘텐츠를 전달합니다.