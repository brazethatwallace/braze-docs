---
nav_title: 예측 이벤트
article_title: 예측 이벤트
description: "이 문서에서는 Braze Predictive Suite의 도구인 예측 이벤트(이전 명칭: 예측 구매)를 다룹니다. 이 도구를 통해 마케터는 사용자가 특정 이벤트를 수행할 가능성에 기반하여 사용자를 식별하고 메시지를 전달할 수 있습니다."
page_order: 9
alias: /predictive_purchases/
search_rank: 1
---

# 예측 이벤트 {#predictive-events}

> 예측 이벤트는 Braze Predictive Suite에서 사용자의 이벤트 수행 가능성에 기반하여 사용자를 식별하고 메시징하는 강력한 도구입니다. 이벤트 예측을 생성하면 Braze는 [그레디언트 부스티드 결정 트리](https://en.wikipedia.org/wiki/Gradient_boosting)를 사용하여 이전 활동을 학습하고 미래 활동을 예측하는 머신 러닝 모델을 훈련시킵니다.

## 예측 이벤트 정보 {#about-predictive-events}

예측이 생성된 후, 사용자에게는 선택한 이벤트를 수행할 가능성을 나타내는 0에서 100 사이의 [가능성 점수]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#purchase_score)가 할당됩니다. 점수가 높을수록 사용자가 해당 이벤트를 수행할 가능성이 높습니다. 사용자는 낮음, 중간, 높음 가능성 카테고리로도 분류됩니다.

예측 이벤트의 진정한 가치는 예측 결과를 사용하여 **Segment** 또는 **Campaign**을 만드는 데 있습니다. 마케터는 **예측** 페이지에서 직접 타겟팅된 **Campaign**을 구축하여 즉각적인 매출 증대 결과를 얻거나, 향후 **Campaign** 또는 **Canvas**를 위해 **Segment**를 저장할 수 있습니다. 누구를 먼저 타겟팅해야 할지 모르겠나요? 가능성 점수에 기반한 사용자 메시징에 대한 [전략적 고려 사항]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy)을 읽어보세요.

![예측 이벤트의 작동 방식을 보여주는 그래픽으로, 사용자 데이터가 머신 러닝 모델에 유입되는 과정을 표시합니다. 라벨에는 "과거 데이터를 사용하여 특정 기간 동안 이벤트를 수행한 사용자와 수행하지 않은 사용자의 동작을 비교하여 학습합니다."라고 적혀 있습니다. 또한 머신 러닝 결과로 사용자가 이벤트를 수행할 가능성이 가장 낮은 순서부터 가장 높은 순서까지 순위가 매겨진 모습도 보여줍니다. 라벨에는 "미래 이벤트의 가능성을 예측하고, 정확하고 편리한 타겟팅을 위해 사용자에게 가능성 점수를 할당합니다."라고 적혀 있습니다.]({% image_buster /assets/img/how_predictive_events_works.png %})

## Predictive Events에 접근하기 {#accessing-predictive-events}

{% multi_lang_include brazeai/predictions_page_access.md %}

이 기능을 구매하기 전에 미리보기 모드에서 사용할 수 있습니다. 미리보기 모드에서는 합성 데이터를 사용한 데모 예측을 확인할 수 있으며, 한 번에 하나의 미리보기 예측 모델을 생성할 수 있습니다. 이 예측은 실제 사용자 데이터를 기반으로 생성되지만, 가능성 점수에 따라 사용자를 메시징 대상으로 타겟팅할 수는 없습니다. 또한 생성 후에는 정기적으로 업데이트되지 않습니다.

미리보기를 사용하면 이 예측을 편집하고 다시 구축하거나 아카이브하고 다른 예측을 생성하여 [다양한 오디언스]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience)의 예상 [예측 품질]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#prediction_quality)을 테스트하고 분석에 익숙해질 수 있습니다.