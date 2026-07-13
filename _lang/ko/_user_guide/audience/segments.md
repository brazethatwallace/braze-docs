---
nav_title: Segments
article_title: Segments
page_order: 3
layout: dev_guide
guide_top_header: "Segments"
guide_top_text: "오디언스 세분화는 전략적 마케팅의 핵심입니다. 과도한 타겟팅, 불필요한 메시지 전송, 또는 고객과의 잠재적 연결 기회를 놓치는 것을 방지할 수 있습니다. 다음 문서를 통해 오디언스를 세분화하고 필터링하여 여러분과 고객 모두에게 최대한의 이점을 제공하는 방법을 알아보세요."
descriptions: "오디언스 세분화는 전략적 마케팅의 핵심입니다. 과도한 타겟팅, 불필요한 메시지 전송, 또는 고객과의 잠재적 연결 기회를 놓치는 것을 방지할 수 있습니다. 이 랜딩 페이지에서 오디언스를 세분화하고 필터링하여 여러분과 고객 모두에게 최대한의 이점을 제공하는 방법을 알아보세요."
search_rank: 4
tool: Segments
page_type: landing
description: "이 랜딩 페이지에서는 대시보드 Campaigns 내 세분화에 대한 문서를 다룹니다. 여기에서 Segment 설정, 필터, 퍼널, 인사이트, 확장 등에 대한 정보를 확인할 수 있습니다."

guide_featured_title: "섹션 문서"
guide_featured_list:
  - name: Segment 생성
    link: /docs/user_guide/audience/segments/creating_a_segment
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Segment 관리
    link: /docs/user_guide/audience/segments/managing_segments
    image: /assets/img/braze_icons/edit-05.svg
  - name: 세분화 필터
    link: /docs/user_guide/audience/segments/segmentation_filters
    image: /assets/img/braze_icons/flag-02.svg
  - name: Segment 데이터
    link: /docs/user_guide/audience/segments/segment_data
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: 세그먼트 확장
    link: /docs/user_guide/audience/segments/segment_extension
    image: /assets/img/braze_icons/users-01.svg
  - name: 세그먼트 인사이트
    link: /docs/user_guide/audience/segments/segment_insights
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "추가 문서"
guide_menu_list:
  - name: 위치 타겟팅
    link: /docs/user_guide/audience/segments/location_targeting
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: 정규표현식
    link: /docs/user_guide/audience/segments/regex
    image: /assets/img/braze_icons/search-sm.svg
  - name: Segment 크기 측정
    link: /docs/user_guide/audience/segments/measuring_segment_size
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: "사용 사례: 중첩 커스텀 속성으로 세분화"
    link: /docs/user_guide/audience/segments/segment_with_nested_custom_attributes
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: 문제 해결
    link: /docs/user_guide/audience/segments/troubleshooting
    image: /assets/img/braze_icons/annotation-question.svg

---

## Braze Segment 소개 {#about-braze-segments}

Braze에서 Segment는 사용자 속성, 사용자 행동, 커스텀 이벤트 등 여러분이 정의한 특정 기준에 맞는 동적 사용자 그룹입니다. Segment를 다른 Segment 안에 중첩하고 추가 기능을 적용하여 기준을 세밀하게 조정할 수 있으며, 오디언스 범위를 좁혀 적합한 사용자에게 고도로 개인화된 매력적인 콘텐츠를 전송할 수 있습니다.

사용자를 타겟팅하기 위해 원하는 만큼 Segment를 생성할 수 있습니다. Segment 기능과 세분화 필터의 다양한 조합을 탐색하여 사용자 데이터를 활용하는 창의적인 방법을 발견하고, 사용자에게 관련성 높은 메시지를 전송하여 인게이지먼트를 높이는 새로운 방법을 찾아보세요.

아래 사용 사례를 통해 Braze Segment가 사용자 타겟팅에 어떻게 도움이 되는지 간략히 살펴보세요.

### 사용 사례 {#use-cases}

- **환영 메시지:** 신규 사용자를 세분화하여 앱을 소개하는 온보딩 이메일이나 인앱 메시지를 전송할 수 있습니다.
- **로열티 리워드:** 구매 빈도, 가입 기념일 또는 기타 마일스톤을 기준으로 사용자를 세분화하고, 가장 충성도 높은 사용자에게 독점 혜택이나 리워드를 전송할 수 있습니다.
- **행동 트리거:** 장바구니에 상품을 담고 결제를 포기하는 등의 사용자 행동을 기준으로 세분화하여 인앱 메시지나 푸시 알림을 트리거할 수 있습니다.
- **상품 추천:** 특정 제품을 구매한 사용자를 세분화하고 보완 제품이나 상위 등급 제품에 대한 추천을 전송할 수 있습니다.
- **A/B 테스트:** 다양한 메시지, 제목란 또는 콘텐츠에 대한 A/B 테스트를 위해 사용자를 세분화하여 특정 연령, 성별 및 기타 속성의 사용자에게 가장 효과적인 것이 무엇인지 파악할 수 있습니다.

#### 세그먼트 확장 사용 사례 {#segment-extension-use-cases}

[세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension)을 사용하면 고객 프로필의 전체 기간 동안 저장된 커스텀 이벤트 또는 구매 행동을 기반으로 Segment를 더욱 세밀하게 조정할 수 있습니다.

- **과거 구매 이력:** 지난 2년간 특정 제품의 특정 색상을 최소 2회 이상 구매한 사용자를 세분화할 수 있습니다.
- **이벤트 및 메시지 상호작용:** 지난 30일 이내에 구매를 완료하고 특정 인앱 메시지와 상호작용한 사용자를 세분화할 수 있습니다.
- **데이터 쿼리:**
  - **Snowflake 쿼리:** [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)을 사용하여 Snowflake를 쿼리함으로써 Braze와 CRM 또는 데이터 웨어하우스 같은 외부 소스의 데이터를 결합하여 사용자를 세분화할 수 있습니다.
  - **데이터 웨어하우스에서 동기화:** [CDI 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)을 사용하여 데이터 웨어하우스 또는 파일 스토리지 시스템에서 Braze로 직접 동기화된 데이터로 사용자를 세분화할 수 있습니다.