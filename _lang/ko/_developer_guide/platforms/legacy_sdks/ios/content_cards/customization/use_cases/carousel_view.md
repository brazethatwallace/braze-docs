---
nav_title: 캐러셀 뷰
article_title: iOS용 콘텐츠 카드 캐러셀 뷰
platform: iOS
page_order: 5
description: "이 문서에서는 iOS 애플리케이션에서 콘텐츠 카드 캐러셀 뷰 사용 사례를 구현하는 방법을 다룹니다."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 사용 사례: 캐러셀 뷰 {#use-case-carousel-view}

![샘플 뉴스 앱에서 기사 내 Content Cards 캐러셀을 보여주는 화면]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

이 섹션에서는 사용자가 수평으로 스와이프하여 추가 추천 카드를 볼 수 있는 다중 카드 캐러셀 피드를 구현하는 방법을 다룹니다. 캐러셀 뷰를 통합하려면 완전히 커스텀된 Content Cards 구현을 사용해야 합니다. 이는 [크롤, 워크, 런 접근 방식]({{site.baseurl}}/developer_guide/getting_started/customization_overview)의 "런" 단계에 해당합니다.

이 접근 방식을 사용하면 Braze 뷰와 기본 로직을 사용하지 않고, Braze 모델의 데이터로 채워진 자체 뷰를 사용하여 Content Cards를 완전히 커스텀 방식으로 표시하게 됩니다.

개발 노력 수준 측면에서 기본 구현과 캐러셀 구현 간의 주요 차이점은 다음과 같습니다.

- 자체 뷰 구축
- Content Cards 분석 기록
- 추가 클라이언트 측 로직을 도입하여 캐러셀에 표시할 카드 수와 종류 결정

## 구현 {#implementation}

### 1단계: 커스텀 뷰 컨트롤러 만들기 {#step-1-create-a-custom-view-controller}

Content Cards 캐러셀을 만들려면 직접 커스텀 뷰 컨트롤러(예: `UICollectionViewController`)를 만들고 [데이터 업데이트를 구독]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#getting-the-data)하세요. 기본 `ABKContentCardTableViewController`는 기본 Content Card 유형만 처리할 수 있으므로, 이를 확장하거나 서브클래스로 만들 수 없다는 점에 유의하세요.

### 2단계: 분석 구현하기 {#step-2-implement-analytics}

완전히 커스텀 뷰 컨트롤러를 만들 경우, Content Card 노출 횟수, 클릭 및 해제는 자동으로 기록되지 않습니다. 노출 횟수, 해제 이벤트 및 클릭이 Braze 대시보드 분석에 올바르게 기록되도록 해당 분석 메서드를 구현해야 합니다.

분석 메서드에 대한 자세한 내용은 [카드 메서드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#card-methods)를 참조하세요.

{% alert note %}
같은 페이지에서 일반 Content Card 모델 클래스에서 상속되는 다양한 속성정보도 설명하고 있으며, 이는 뷰 구현 시 유용할 수 있습니다.
{% endalert %}

### 3단계: Content Card 옵저버 만들기 {#step-3-create-a-content-card-observer}

Content Cards의 도착을 처리하는 [Content Card 옵저버]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener)를 만들고, 캐러셀에 한 번에 표시할 카드 수를 지정하는 조건 로직을 구현하세요. 기본적으로 Content Cards는 생성 날짜순(최신순)으로 정렬되며, 사용자는 자신이 수신 대상인 모든 카드를 볼 수 있습니다.

다양한 방법으로 정렬하고 추가 표시 로직을 적용할 수 있습니다. 예를 들어, 배열에서 처음 5개의 Content Card 객체를 선택하거나 키-값 페어(데이터 모델의 `extras` 속성정보)를 도입하여 조건 로직을 구성할 수 있습니다.

캐러셀을 보조 Content Cards 피드로 구현하는 경우, 키-값 페어를 기반으로 카드가 올바른 피드로 정렬되도록 [여러 Content Card 피드 사용하기]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds)를 참조하세요.

{% alert important %}
마케팅 팀과 개발자 팀이 사용할 키-값 페어(예: `feed_type = brand_homepage`)에 대해 사전에 조율하는 것이 중요합니다. 마케터가 Braze 대시보드에 입력하는 키-값 페어는 개발자가 앱 로직에 구축하는 키-값 페어와 정확히 일치해야 합니다.
{% endalert %}

Content Cards 클래스, 메서드 및 속성에 대한 iOS 전용 개발자 설명서는 iOS [`ABKContentCard` 클래스 레퍼런스](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)를 참조하세요.

## 고려 사항 {#considerations}

- 완전히 커스텀 뷰를 사용하면 `ABKContentCardsController`에서 사용하는 메서드를 확장하거나 서브클래싱할 수 없습니다. 대신 데이터 모델 메서드와 속성정보를 직접 통합해야 합니다.
- 캐러셀 뷰의 로직과 구현은 Braze에서 기본값으로 제공하는 Content Cards 유형이 아니므로, 이 사용 사례를 구현하기 위한 로직은 개발팀에서 직접 제공하고 지원해야 합니다.
- 캐러셀에 한 번에 표시할 카드 수를 지정하기 위한 클라이언트 측 로직을 구현해야 합니다.