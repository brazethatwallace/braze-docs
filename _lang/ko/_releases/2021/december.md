---
nav_title: 12월
page_order: 0
noindex: true
page_type: update
description: "이 문서에는 2021년 12월의 릴리스 노트가 포함되어 있습니다."
alias: "/help/release_notes/2022/january/"
---
# 2021년 12월 {#december-2021}

## Segment별 사용자 내보내기 엔드포인트 업데이트 {#update-to-export-users-by-segment-endpoint}

2021년 12월부터 [Segment별 사용자 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)에 대해 다음과 같은 변경 사항이 적용됩니다.

1. 이 API 요청의 `fields_to_export` 필드는 필수입니다. 모든 필드를 기본값으로 설정하는 옵션이 제거됩니다.
2. `custom_events`, `purchases`, `campaigns_received`, `canvases_received`의 필드에는 지난 90일 동안의 데이터만 포함됩니다.

## Currents 메시지 참여 이벤트의 새로운 속성 {#new-properties-for-currents-message-engagement-events}

일부 [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)에 대한 새로운 속성이 추가되었습니다. 이 업데이트는 다음 Currents 메시지 참여 이벤트와 이를 사용하는 모든 파트너에 적용됩니다.

- `LINK_ID`, `LINK_ALIAS`를 다음에 추가:
  - 이메일 클릭(모든 대상)
- `USER_AGENT`를 다음에 추가:
  - 이메일 열람
  - 이메일 클릭
  - 이메일 스팸으로 표시
- `MACHINE_OPEN`을 다음에 추가:
  - 이메일 열람

## 새로운 Liquid 개인화 태그 {#new-liquid-personalization-tag}

이제 기기에서 포그라운드 푸시를 활성화한 사용자를 다음 Liquid 태그를 사용하여 타겟팅할 수 있습니다.

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

자세한 내용은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)를 참조하세요.

## 웹훅 소개 {#about-webhooks}

웹훅은 강력하고 유연한 도구이지만 다소 혼란스러울 수 있습니다. 웹훅이 무엇이고 Braze에서 어떻게 사용할 수 있는지 궁금하다면 [웹훅 소개]({{site.baseurl}}/about_webhooks/) 문서를 확인하세요.

## Amazon Personalize

Amazon Personalize는 하루 종일 사용할 수 있는 나만의 Amazon 머신 러닝 추천 시스템과 같습니다. 20년 이상의 추천 경험을 바탕으로 한 Amazon Personalize를 사용하면 실시간 개인화 제품 및 콘텐츠 추천과 타겟 마케팅 프로모션을 통해 고객 참여를 향상시킬 수 있습니다.

더 자세히 알아보려면 Amazon Personalize가 제공하는 사용 사례, 연동되는 데이터, 서비스 구성 방법, Braze와 통합하는 방법을 이해할 수 있는 새로운 [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/amazon_personalize/) 문서를 참조하세요.

## 새로운 Braze 파트너십 {#new-braze-partnerships}

### Yotpo – 전자상거래 {#yotpo-ecommerce}

[Yotpo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/yotpo/)와 Braze의 통합을 통해 이메일 및 Braze 내 기타 커뮤니케이션 채널에서 제품에 대한 별점, 인기 리뷰, 시각적 사용자 생성 콘텐츠를 동적으로 가져와 표시할 수 있습니다. 또한 이메일 및 기타 커뮤니케이션 방법에 고객 수준의 로열티 데이터를 포함시켜 보다 개인화된 상호 작용을 생성하여 매출과 로열티를 높일 수 있습니다.

### Zeotap – 고객 데이터 플랫폼 {#zeotap-customer-data-platform}

[Zeotap]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/zeotap/)과 Braze의 통합을 통해 Zeotap 고객 세그먼트를 동기화하여 Zeotap 사용자 데이터를 Braze 사용자 계정에 매핑함으로써 Campaign의 규모와 도달 범위를 확장할 수 있습니다. 그런 다음 이 데이터를 기반으로 조치를 취하여 사용자에게 개인화된 타겟 경험을 제공할 수 있습니다.