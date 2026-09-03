---
nav_title: "다중 플랫폼 푸시 메시지"
article_title: "다중 플랫폼 메시지"
alias: "/multiple_platform_push/"
description: "이 문서에서는 여러 플랫폼이 선택된 푸시 Campaign 또는 Canvas를 생성할 때 알아야 할 사항을 설명합니다."
page_order: 4
---

# 다중 플랫폼 푸시 메시지 {#multiple-platform-push-messages}

> 이 문서에서는 하나의 작성기에서 여러 플랫폼과 기기를 타겟팅하는 푸시 Campaign 또는 Canvas를 생성할 때 알아야 할 사항을 설명합니다.

Braze에서 푸시 Campaign 또는 Canvas를 생성할 때 여러 플랫폼과 기기를 선택하여 단일 편집 환경에서 모든 플랫폼에 대한 하나의 메시지를 작성할 수 있습니다.

## 사용 사례 {#use-cases}

이 편집 환경은 다음과 같은 사용 사례에 가장 적합합니다:

- 여러 기기 유형(예: iOS와 Android 모두)에 발송해야 하는 모바일 푸시 Campaign 및 Canvas 메시지 단계.
- 여러 플랫폼을 빠르고 정확하게 타겟팅해야 하며, 플랫폼 간 콘텐츠가 동일한 시간에 민감한 푸시 알림(예: 속보 또는 실시간 경기 업데이트).

## 다중 플랫폼 푸시 Campaign 또는 Canvas 만들기 {#creating-a-multiple-platform-push-campaign-or-canvas}

여러 플랫폼과 기기를 타겟팅하는 Campaign을 만들려면 다음을 수행하세요.

1. Campaign을 만들거나 Canvas에 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)를 추가합니다.
2. **푸시 알림**을 선택합니다.
3. 원하는 플랫폼(모바일, 웹, Kindle)과 모바일 기기(iOS, Android)를 선택합니다. 여러 기기를 선택하면 Campaign에서 다변량 테스트를 사용할 수 없습니다.

### Campaign에서 플랫폼 선택하기 {#selecting-platforms-for-a-campaign}
![모바일, 웹, Kindle 등 푸시 Campaign의 여러 플랫폼과 iOS, Android 등 여러 기기를 선택하는 옵션입니다.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### 캔버스 단계에서 플랫폼 선택하기 {#selecting-platforms-for-a-canvas-step}
![모바일, 웹, Kindle 등 푸시 메시지 단계의 여러 플랫폼과 iOS, Android 등 여러 기기를 선택하는 옵션입니다.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. **확인**을 선택합니다. **확인**을 선택한 후에는 선택한 플랫폼이나 기기를 변경할 수 없습니다.
5. Campaign 또는 Canvas 설정을 계속 진행합니다.

## 멀티 플랫폼 다변량 테스트 실행 {#running-a-multi-platform-multivariate-test}

다변량 테스트는 멀티 플랫폼 Campaign에서 지원됩니다. 단일 플랫폼 Campaign과 마찬가지로 배리언트 이름 옆의 더하기 아이콘을 선택합니다. 설정 단계는 [다변량 및 A/B 테스트 만들기]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests)를 참조하세요.

배리언트를 자동으로 최적화하려면 [BrazeAI<sup>TM</sup>를 활용한 A/B 테스트 최적화]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)를 참조하세요.

![간편한 멀티 플랫폼 다변량 테스트]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## 알아두어야 할 사항 {#things-to-know}

### 통합 메시징 {#unified-messaging}
**작성** 탭에서 선택한 모든 플랫폼과 기기에 대해 하나의 제목, 메시지, 클릭 시 동작을 지정할 수 있습니다.

미리보기 창에서는 각 플랫폼에서 메시지가 어떻게 보이는지 대략적으로 확인할 수 있습니다. 글자 수 제한에 도달할 수 있는 위치를 파악하는 데 유용한 지표가 될 수 있지만, Campaign을 전송하기 전에 항상 실제 기기에서 메시지를 테스트하는 것을 잊지 마세요.

![iOS, Android, 웹의 세 가지 푸시 유형에 대해 하나의 제목, 메시지, 클릭 시 동작 필드가 있는 단일 편집 보기.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### 개별 에셋 {#separate-assets}
**에셋** 섹션에서 각 플랫폼에 표시할 이미지를 선택하거나 업로드합니다. 기기마다 이미지 및 글자 수에 대한 사양이 다르다는 점을 유의하세요. 도움이 필요하면 [푸시 메시지 및 이미지 형식]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)을 참조하세요.

![푸시 아이콘 이미지, iOS 알림 이미지, Android 알림 이미지, 웹 알림 이미지 필드가 있는 단일 편집 보기의 에셋 섹션.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### 알림 유형 {#notification-type}

알림 유형은 기본적으로 "표준 푸시"로 설정되어 있으며 변경할 수 없습니다. Push Stories나 인라인 이미지(Android) 등 다른 푸시를 만들려면 각 기기 유형에 대해 별도의 Campaign을 생성하세요.

### 기기별 설정 {#device-specific-settings}

편집기에서 플랫폼별 설정을 편집할 수 있습니다. [푸시 실행 버튼]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), 알림 채널 및 그룹, TTL, 표시 우선순위, 사운드 등의 설정이 포함됩니다.

기기별 설정에 대한 자세한 내용은 다음 문서를 참조하세요:

- [iOS 옵션]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios)
- [Android 옵션]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android)

### Push Stories

Push Stories는 Android와 iOS에서만 멀티 플랫폼으로 사용할 수 있으며, 전송 플랫폼으로 웹이나 Kindle을 선택하면 이 옵션을 사용할 수 없습니다.