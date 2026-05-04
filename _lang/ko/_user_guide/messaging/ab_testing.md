---
nav_title: A/B Testing
article_title: "A/B 테스트"
page_order: 6
layout: dev_guide
guide_top_header: "A/B 테스트"
guide_top_text: "실험을 통해 메시징을 최적화하세요. A/B 테스트는 동일한 Campaign(캠페인)의 여러 버전에 대한 사용자 응답을 비교하며, 다변량 테스트는 이를 두 개 이상의 변수로 확장합니다. Braze에서는 설정 과정이 동일하기 때문에 두 용어를 같은 의미로 사용합니다. A/B 테스트와 <a href='/docs/user_guide/brazeai/intelligence_suite/intelligent_selection'>지능형 선택</a>을 함께 사용하여 결과를 자동으로 최적화하세요."

page_type: landing
description: "Braze에서 A/B 테스트 및 다변량 실험을 설정하고 분석하세요."

guide_featured_title: "섹션 문서"
guide_featured_list:
  - name: 개념
    link: /docs/user_guide/messaging/ab_testing/concepts
    image: /assets/img/braze_icons/lightbulb-02.svg
  - name: 테스트 생성
    link: /docs/user_guide/messaging/ab_testing/create_tests
    image: /assets/img/braze_icons/plus-circle.svg
  - name: 최적화
    link: /docs/user_guide/messaging/ab_testing/optimizations
    image: /assets/img/braze_icons/settings-01.svg
  - name: 분석
    link: /docs/user_guide/messaging/ab_testing/analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: FAQ
    link: /docs/user_guide/messaging/ab_testing/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## A/B 테스트를 사용해야 하는 경우 {#when-to-use-ab-tests}

- **새로운 메시징 유형을 시도할 때:** 실험을 통해 사용자에게 어떤 메시지가 공감을 얻는지 알아보세요.
- **온보딩 Campaigns(캠페인) 또는 반복 발송:** 트래픽이 높은 Campaigns(캠페인)가 최대한 효과적인지 확인하세요.
- **여러 메시지 아이디어가 있을 때:** 테스트를 실행하고 데이터 중심의 의사결정을 내리세요.
- **기존 가정에 도전할 때:** 기존의 마케팅 전략이 실제로 특정 오디언스에게 효과가 있는지 테스트하세요.

## 효과적인 테스트를 위한 팁 {#tips-for-running-effective-tests}

- **큰 표본을 사용하세요.** 결과가 평균적인 사용자를 반영하고 이상값에 의해 왜곡되지 않도록 합니다.
- **테스트 그룹을 무작위로 배정하세요.** 응답률 차이가 표본 차이가 아닌 메시지 차이를 반영하도록 합니다.
- **무엇을 테스트하는지 명확히 하세요.** 단일 변경 사항을 분리하면 어떤 요소가 가장 큰 영향을 미쳤는지 파악할 수 있고, 여러 차이점을 동시에 테스트하면 더 넓은 접근 방식을 비교할 수 있습니다.
- **테스트 기간을 사전에 설정하세요.** 초기 결과가 유망해 보이더라도 테스트를 조기에 종료하지 마세요.
- **시작 전에 테스트를 추가하세요.** 실행 중인 Campaign에 테스트를 추가하면 부정확한 결과가 나옵니다. Campaign을 복제하고, 원본을 중지한 다음, 복제본에 테스트를 추가하세요.
- **[대조군]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/#including-a-control-group)을 포함하세요.** 메시지를 전혀 보내지 않는 경우와 비교하여 효과를 측정할 수 있습니다.