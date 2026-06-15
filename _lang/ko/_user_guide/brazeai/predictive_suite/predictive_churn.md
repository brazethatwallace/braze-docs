---
nav_title: Predictive Churn
article_title: Predictive Churn
description: "이 랜딩 페이지는 Braze Predictive Suite의 도구인 Predictive Churn을 소개합니다. 이 도구를 통해 비즈니스에서 고객이탈이 의미하는 바를 정의하고, 고객이탈을 방지하고자 하는 사용자를 지정할 수 있습니다."
page_order: 8
alias: /predictive_churn/
search_rank: 2
---

# Predictive Churn {#predictive-churn}

> Braze Predictive Suite의 도구인 Predictive Churn을 통해 비즈니스에서 고객이탈이 무엇을 의미하는지 정의하고 유지하고자 하는 사용자를 식별할 수 있습니다. 예측을 생성하면 Braze는 [그래디언트 부스팅 의사 결정 트리](https://en.wikipedia.org/wiki/Gradient_boosting)를 사용하여 머신 러닝 모델을 학습시켜, 이탈한 사용자와 그렇지 않은 사용자 모두의 과거 행동 패턴을 분석하여 위험에 처한 사용자를 인식합니다.

{% alert tip %}
자세한 내용은 [고객이탈 정의]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) 및 [예측 오디언스]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)를 참조하세요.
{% endalert %}

## 이탈 예측 정보 {#about-predictive-churn}

예측 모델이 구축되면 예측 오디언스에 속한 사용자에게는 정의에 따라 이탈 가능성을 나타내는 0~100 사이의 [고객이탈 위험 점수]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/#churn_score)가 할당됩니다. 점수가 높을수록 사용자가 고객이탈할 가능성이 높습니다.

예측 오디언스의 위험 점수 업데이트는 [선택한 빈도]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-prediction)로 수행할 수 있습니다. 이렇게 하면 고객이탈 위험이 있는 사용자에게 실제 고객이탈이 발생하기 전에 먼저 연락하여 이를 사전에 방지할 수 있습니다. 최대 세 개의 활성 예측을 사용하여 Predictive Churn을 활용하면 가장 가치 있다고 생각되는 특정 사용자 세그먼트 내에서 고객이탈을 방지하기 위해 개별 모델을 맞춤화할 수 있습니다.

![과거 예측 오디언스를 포함한 고객이탈 개요로, 과거 데이터로 학습합니다. 이는 오늘의 예측 오디언스를 고객이탈 위험 점수로 측정하여 미래의 고객이탈 위험을 예측하는 데 기여합니다.]({% image_buster /assets/img/churn/churn_overview.png %})

## Predictive Churn에 액세스하기 {#accessing-predictive-churn}

{% multi_lang_include brazeai/predictions_page_access.md %}

이 기능을 구매하기 전에 미리보기 모드에서 사용할 수 있습니다. 미리보기를 통해 합성 데이터로 데모 고객이탈 예측을 확인하고, 한 번에 하나의 사용자 데이터 기반 고객이탈 예측 모델을 만들 수 있습니다. 이 미리보기에서는 고객이탈 위험에 따라 메시징 대상으로 사용자를 타겟팅할 수 없으며, 생성 후 정기적으로 업데이트되지 않습니다.

미리보기를 통해 하나의 예측을 편집하고 다시 구축하거나 아카이브한 후 다른 [정의]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)의 예상 [예측 품질]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/)을 테스트하기 위해 새로운 예측을 만들 수도 있습니다.