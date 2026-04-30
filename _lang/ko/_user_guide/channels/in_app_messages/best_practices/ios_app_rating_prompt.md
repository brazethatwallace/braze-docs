---
nav_title: iOS 인앱 평가 프롬프트
article_title: iOS 인앱 평가 프롬프트
page_order: 6
description: "이 문서에서는 Braze를 사용하여 사용자에게 앱 리뷰를 요청하는 접근 방식과 그에 따른 영향을 설명합니다."
channel:
  - in-app messages

---

# iOS 인앱 평가 프롬프트 {#in-app-rating-prompt-for-ios}

> 이 문서에서는 Braze를 사용하여 사용자에게 앱 리뷰를 요청하는 접근 방식과 그에 따른 영향을 설명합니다. 효과적인 앱 평가 Campaign(캠페인)을 만드는 팁은 [고객 앱 평가의 해야 할 것과 하지 말아야 할 것](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings)을 확인하세요.

Apple은 iOS 10.3에서 도입된 네이티브 프롬프트를 제공하며, 이를 통해 사용자가 앱 내에서 직접 앱을 평가할 수 있습니다. iOS에서 인앱 메시지를 사용하여 사용자에게 앱 평가를 요청하려면 네이티브 프롬프트를 사용해야 합니다. Apple은 커스텀 리뷰 프롬프트를 허용하지 않기 때문입니다([App Store 심사 지침](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), 섹션 5.6.1 참조).

Apple 지침에 따르면 앱 리뷰 프롬프트는 사용자에게 연간 최대 3회까지 표시할 수 있으므로, 앱 리뷰 Campaign은 [사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/)을 활용해야 합니다. 사용자는 앱 설정에서 앱 리뷰 프롬프트 표시를 완전히 끌 수도 있습니다. App Store 평가에 대한 자세한 내용은 Apple의 [평가, 리뷰 및 응답](https://developer.apple.com/app-store/ratings-and-reviews/) 문서를 참조하세요.

## Braze를 사용하여 사용자에게 앱 리뷰 요청하기 {#using-braze-to-ask-users-for-app-reviews}

Apple은 네이티브 프롬프트를 사용하도록 요구하지만, Braze Campaign을 활용하여 적절한 시점에 사용자에게 앱 평가 및 리뷰를 요청할 수 있습니다. 두 가지 주요 접근 방식이 있습니다.

### 접근 방식 1: App Store로 딥링킹 {#approach-1-deep-linking-to-the-app-store}

이 접근 방식에서는 사용자가 App Store를 방문하여 리뷰를 남기도록 유도합니다. 이를 위해 App Store로 [딥링크]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/)하는 인앱 메시지 Campaign을 생성합니다.

![두 개의 모바일 화면이 나란히 표시됩니다. 첫 번째는 사용자에게 App Store에서 앱을 평가해 달라고 요청하는 인앱 메시지입니다. 두 번째는 해당 앱의 iOS App Store 페이지입니다.]({% image_buster /assets/img_archive/app_store_app_review.png %})

### 접근 방식 2: 소프트 프라이밍 {#approach-2-soft-priming}

사용자가 앱을 떠나지 않기를 원한다면, 먼저 별도의 인앱 메시지로 사용자를 프라이밍할 수 있습니다. 프라이밍은 네이티브 App Store 리뷰 프롬프트를 보내기 전에 사용자에게 허락을 구하는 방법입니다. 이를 위해 인앱 메시지 Campaign을 생성하고, 클릭 시 `requestReview` 메서드를 호출하는 커스텀 딥링크를 추가합니다.

자세한 단계는 [커스텀 App Store 리뷰 프롬프트]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_customizing-the-app-store-review-prompt)를 참조하세요.

![두 개의 인앱 메시지가 나란히 표시됩니다. 첫 번째는 앱을 평가할 시간이 있는지 물어보며 사용자를 프라이밍합니다. 두 번째는 네이티브 iOS App Store 리뷰 메시지로, 사용자가 앱을 평가할 수 있는 별 5개 척도가 표시됩니다.]({% image_buster /assets/img_archive/prime_app_review.png %})

사용자는 네이티브 App Store 리뷰 프롬프트를 통해 평가를 제출하며, 앱을 떠나지 않고도 리뷰를 작성하고 제출할 수 있습니다.

### 고려 사항 {#considerations}

소프트 프라이밍의 대안으로, Braze 소프트 프라이머 메시지를 먼저 표시하지 않고 iOS 앱 평가 프롬프트를 직접 표시할 수도 있습니다. 이 방법의 장점은 사용자가 앱 리뷰 프롬프트 수신을 거부한 경우, 앱을 평가하려고 했지만 프롬프트가 나타나지 않는 좋지 않은 사용자 경험을 방지할 수 있다는 것입니다.

{% alert important %}
네이티브 iOS 앱 평가 프롬프트를 모방하는 커스텀 HTML 인앱 메시지를 만들지 마세요. 이는 Apple 지침을 위반합니다.
{% endalert %}