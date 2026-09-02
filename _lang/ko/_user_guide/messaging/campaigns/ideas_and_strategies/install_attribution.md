---
nav_title: 사용자 설치 이해하기
article_title: 사용자 설치 이해하기
page_order: 7
page_type: reference
description: "이 참조 문서에서는 사용자 설치(설치 경로 추적)와 이 정보를 캠페인에 적용하는 다양한 방법을 설명합니다."
tool:
  - Campaigns
  - Segments
---

# 사용자 설치 이해하기 {#understanding-user-installs}

> 설치 경로 추적은 사용자와의 초기 관계를 개선하는 훌륭한 방법입니다. 사용자가 앱을 어떻게, 어디서, 그리고 더 중요하게는 왜 설치했는지 알면 사용자가 누구인지, 그리고 앱을 어떻게 소개해야 하는지 더 잘 이해할 수 있습니다.

Braze는 설치 경로 추적을 직접 제공하지는 않지만, Branch 및 AppsFlyer와 같은 [서비스]({{site.baseurl}}/partners/message_orchestration)와 통합하여 설치 데이터를 원활하게 제공할 수 있습니다.

## 사용자 세분화 {#segment-your-users}

사용자가 앱을 설치하면 다음 [설치 경로 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#install-attribution)를 기반으로 사용자를 세분화할 수 있습니다. 예를 들어, 여행 앱은 해변 휴가 특가 관련 광고를 통해 유입된 사용자를 "Beach Lovers" Segment에 추가할 수 있습니다. 마찬가지로, 음악 앱은 설치로 이어진 광고에 표시된 음악 장르를 기반으로 사용자를 세분화할 수 있습니다.

## 모범 사례 {#best-practices}

### 개인화된 온보딩 {#personalized-onboarding}

이제 사용자에 대한 정보가 더 많아졌으므로, 온보딩 과정을 개인화할 수 있습니다. 메시지의 이미지를 사용자의 선호도에 맞게 변경하는 간단한 방법부터, 설치로 이어질 수 있는 각 광고에 대해 고유한 사용자 온보딩을 만드는 복잡한 방법까지 다양합니다. 사용자 행동을 고려할 수 있는 포괄적인 메시지 시퀀스를 확장하려면, [Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)에 대한 설명서를 참조하세요.

### 광고 데이터 참조 {#reference-data-from-the-ad}

사용자는 프로모션 혜택이나 경품 이벤트를 통해 앱에 유입될 수 있습니다. 설치 경로 데이터를 활용하면, 이러한 프로모션으로 인해 설치한 사용자에게만 할인 코드나 혜택이 포함된 Campaigns를 보낼 수 있습니다. 마찬가지로, 광고에 특정 제품에 대한 정보(예: 비디오 앱의 특정 영화나 이커머스 앱의 할인 행사)가 포함되어 있는 경우, 사용자를 앱의 올바른 페이지로 안내하는 Campaigns를 보낼 수 있습니다.

## 광고 효과 평가 {#evaluate-advertising-efforts}

설치 경로 데이터는 다양한 마케팅 Campaign의 효과를 평가하는 데 유용할 수 있습니다. 어떤 광고와 Campaign이 가장 많은 설치를 유도하고 어떤 것이 뒤처지고 있는지 확인하면, 가장 효과적인 광고에 리소스를 집중하는 데 활용할 수 있습니다.