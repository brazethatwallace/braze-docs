---
nav_title: A/B 테스트 투영
article_title: A/B 테스트 투영
page_order: 20
hidden: true
page_type: reference
description: "이 문서에서는 A/B 테스트 예측의 작동 방식, 예측을 실행하는 방법, Braze가 데이터를 사용하는 방법에 대해 설명합니다."
---

# A/B 테스트 투영 {#ab-test-projection}

> A/B 테스트 투영은 신경망을 사용하여 어떤 제목란이 가장 좋은 성과를 내는지 예측합니다. 이 모델은 Braze에서 수행된 성공적인 A/B 테스트에서 언어적 특성을 추출하고, 이러한 통계적 언어 패턴을 활용하여 AI에게 더 나은 제목란을 구성하는 요소를 학습시킵니다.

{% alert important %}
이 기능은 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 Braze 고객 성공 또는 계정 매니저에게 문의하세요.
{% endalert %}

## 프로젝션 실행 {#running-a-projection}

캠페인 작성 시, 메시지 배리언트와 제목란을 편집기에 입력합니다. 준비가 되면 캠페인 생성 플로우의 **타겟 오디언스** 단계로 이동합니다. **A/B 테스트** 패널에서 **투영 실행**을 선택합니다.

<img width="518" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

이미 생성한 메시지 배리언트의 제목란이 표시된 모달이 열립니다. 선택 사항으로, 추가 제목란(최대 10개)을 직접 입력란에 입력하여 투영을 실행할 수 있습니다. **프로젝션 실행**을 선택합니다.

<img width="722" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

AI가 가장 우수하다고 예측한 제목란에는 **예상 위너** 레이블이 표시됩니다.

{% alert note %}
[빠른 푸시 캠페인]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/quick_push_messages/)의 경우, 여러 플랫폼을 선택할 때 A/B 테스트가 지원됩니다.
{% endalert %}

### 예측은 얼마나 정확한가요? {#how-accurate-are-the-projections}

테스트 결과, 실제 A/B 테스트에서 메시지 쌍 중 하나를 선택할 때 예측 정확도가 약 70%인 것으로 나타났습니다. 모델이 승리할 것으로 예측하는 메시지를 해석할 때 이 점을 참고하세요.

### 데이터는 어떻게 사용하나요? {#how-do-we-use-your-data}

이 기능은 Braze에서 수행된 과거 A/B 테스트를 통해 학습합니다. 회원님 또는 다른 Braze 고객의 실제 메시지 내용은 모델에 제공되지 않습니다. 먼저 A/B 테스트에서 승리하는 메시지를 예측하는 상위 수준의 언어 패턴을 추출합니다. 그런 다음, 이러한 패턴을 AI에 제공하여 어떤 언어적 특성이 우수한 제목란을 구성하는지 판별하도록 학습시킵니다.