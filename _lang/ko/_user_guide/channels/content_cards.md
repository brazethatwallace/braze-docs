---
nav_title: 콘텐츠 카드
article_title: 콘텐츠 카드
page_order: 2
page_type: landing
description: "콘텐츠 카드를 사용하여 앱이나 웹사이트에 직접 삽입된 풍부한 콘텐츠의 동적 스트림을 사용자에게 전달하세요."
channel:
  - content cards
search_rank: 5
---

# 콘텐츠 카드 {#content-cards}

> Content Cards를 사용하면 사용자가 즐겨 사용하는 앱 내에서 경험을 방해하지 않으면서 고도로 타겟팅된 풍부한 콘텐츠의 동적 스트림을 고객에게 전달할 수 있습니다. Content Cards는 앱이나 웹사이트에 직접 삽입되어 메시지 받은편지함과 커스텀 인터페이스를 만들 수 있으며, 이메일이나 푸시 알림 같은 다른 채널의 도달 범위를 확장합니다.

## 전제 조건 {#prerequisites}

Content Cards 사용 가능 여부는 Braze 패키지에 따라 다릅니다. 시작하려면 계정 매니저 또는 고객 성공 매니저에게 문의하세요.

Content Cards를 사용하려면 먼저 앱이나 웹사이트에 [Braze SDK]({{site.baseurl}}/developer_guide/content_cards)를 연동해야 합니다. 추가 설정은 필요하지 않습니다. 자체 UI를 구축하려면 [Content Cards 커스터마이징 가이드]({{site.baseurl}}/developer_guide/content_cards/customizing_cards)를 참조하세요.

## Content Cards 사용의 이점 {#benefits-of-using-content-cards}

Content Cards를 사용하면 개발자가 앱에 직접 콘텐츠를 구축하는 것에 비해 다음과 같은 이점이 있습니다:

- **더 쉬운 세분화 및 개인화:** 사용자 데이터가 Braze에 저장되므로 오디언스를 정의하고 Content Cards로 메시지를 개인화하기가 쉽습니다.
- **중앙 집중식 보고:** Content Cards 분석이 Braze에서 추적되므로 모든 Campaigns에 대한 인사이트를 한 곳에서 확인할 수 있습니다.
- **통합된 고객 여정:** Braze의 다른 채널과 Content Cards를 결합하여 일관된 고객 경험을 만들 수 있습니다. 대표적인 사용 사례로, 푸시 알림을 보낸 후 푸시에 반응하지 않은 사용자를 위해 해당 알림을 앱의 콘텐츠 카드로 저장하는 방법이 있습니다. 콘텐츠가 개발자에 의해 앱에 직접 구축된 경우, 나머지 메시징과 분리됩니다.
- **옵트인 불필요:** 인앱 메시지와 마찬가지로 Content Cards는 사용자의 옵트인이나 권한이 필요하지 않습니다. 그러나 인앱 메시지는 권한이 필요 없지만 일시적인 반면, Content Cards는 권한이 필요 없으면서도 영구적입니다. 따라서 인앱 메시지와 Content Cards를 함께 사용하는 메시징 전략은 훌륭한 균형을 이룹니다.
- **메시징 경험에 대한 더 많은 제어:** Content Cards의 초기 설정에는 개발자의 도움이 필요하지만, 그 이후에는 메시지, 수신자, 타이밍 등을 Braze 대시보드에서 직접 제어할 수 있습니다.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## 숫자로 보는 Content Cards {#content-cards-by-the-numbers}

Braze에서 Content Cards를 구축하면 앱이나 웹사이트를 전면 개편하지 않고도 메시징을 업데이트하고 효과를 측정할 수 있습니다. Braze 리서치의 주요 결과는 다음과 같습니다:

- Content Cards는 72시간 동안 매출을 높이는 데 이메일보다 **38배** 더 효과적입니다.[^1]
- 로열티 등록 Campaigns에 Content Cards를 활용하면 전환율이 **5배** 향상됩니다.[^1]
- 푸시 알림, In-App Messages, Content Cards를 통한 아웃리치는 푸시만 사용하는 것보다 세션 수가 **6.9배** 더 많습니다.[^2]
- 이메일, In-App Messages, Content Cards를 통한 아웃리치는 이메일만 사용하는 것보다 평균 사용자 수명이 **3.6배** 더 깁니다.[^2]

## 사용 사례 {#use-cases}

이 섹션에서는 Content Cards의 일반적인 사용 사례를 소개합니다.

{% alert tip %}
더 많은 아이디어가 필요하면 추천 프로그램, 신제품 출시, 구독 갱신 등 20개 이상의 커스터마이징 가능한 캠페인이 포함된 [Content Cards 인스피레이션 가이드](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide)를 참조하세요.
{% endalert %}

{% tabs %}
{% tab 온보딩 및 다음 단계 %}

신규 사용자가 앱과 웹사이트를 탐색할 때, 전략적으로 배치된 Content Cards를 통해 제공하는 가치와 혜택을 안내하세요. 홈페이지의 콘텐츠 카드를 활용하여 다른 커뮤니케이션 채널에 옵트인하도록 유도하고, Content Cards로 구동되는 전용 온보딩 탭에 미완료 온보딩 과제를 저장하세요. 사용자가 원하는 작업을 완료하면 해당 카드를 반드시 제거하세요!

![Content Cards 온보딩 사용 사례 예시]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab 이벤트 참석 %}

사용자 홈페이지 상단에 Content Cards를 표시하여 이벤트 참석을 유도하고, 위치 타겟팅을 활용하여 잠재 사용자가 있는 곳에서 도달하세요. 사용자를 관련 오프라인 이벤트에 초대하면 특별한 느낌을 줄 수 있으며, 특히 브랜드와의 이전 활동을 활용한 개인화된 메시징으로 더욱 효과적입니다.

![Content Cards 이벤트 참석 사용 사례 예시]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab 추천 %}

사용자 행동 및 선호도 데이터를 활용하여 홈페이지 또는 받은편지함 Content Cards에서 관련 콘텐츠를 실시간으로 표시하고, 사용자를 제품 오퍼링으로 다시 유도하세요.

![Content Cards 추천 사용 사례 예시]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab 세일 및 프로모션 %}

Content Cards를 활용하여 프로모션 메시지와 미수령 혜택을 홈페이지 또는 전용 프로모션 받은편지함에 직접 표시하세요. 각 고객의 이전 구매 내역을 기반으로 관련 콘텐츠를 불러와 시선을 사로잡는 개인화된 프로모션을 제공하세요.

![Content Cards 세일 및 프로모션 사용 사례 예시]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### 기타 사용 사례 {#other-use-cases}

이러한 주요 사용 사례 외에도 고객은 다양한 방식으로 Content Cards를 활용하고 있습니다. Content Cards의 강점은 유연성에 있습니다. 원하는 사용 사례가 여기에 없는 경우, [키-값 페어]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)를 설정하고 앱이나 웹사이트로 페이로드를 전송할 수 있습니다.

앱이나 웹사이트에서 콘텐츠 카드 배치를 구현하는 방법에 대한 개요는 [커스텀 Content Cards 만들기]({{site.baseurl}}/developer_guide/content_cards/creating_cards)를 참조하세요.

## 다음 단계 {#next-steps}

{% article_tiles %}
- name: 콘텐츠 카드 만들기
  link: /docs/user_guide/channels/content_cards/create_a_content_card
- name: 크리에이티브 세부 정보
  link: /docs/user_guide/channels/content_cards/creative_details
{% endarticle_tiles %}

[^1]: [고객 유지 캠페인을 최대한 활용하기 위한 8가지 팁](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [보고서: 크로스채널 마케팅의 차이](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)