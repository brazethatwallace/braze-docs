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

## 활용 사례 {#use-cases}

이 편집 환경은 다음과 같은 사용 사례에 가장 적합합니다.

- 여러 기기 유형(예: iOS와 Android 모두)으로 발송해야 하는 모바일 푸시 Campaign 및 Canvas 메시지 단계.
- 콘텐츠가 플랫폼 간에 동일한 경우(예: 속보 또는 실시간 경기 업데이트) 여러 플랫폼을 빠르고 정확하게 타겟팅해야 하는 시간에 민감한 푸시 알림.

## 다중 플랫폼 푸시 Campaign 또는 Canvas 생성하기 {#creating-a-multiple-platform-push-campaign-or-canvas}

여러 플랫폼과 기기를 타겟팅하는 Campaign을 생성하려면:

1. Campaign을 생성하거나 Canvas에 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)를 추가합니다.
2. **푸시 알림**을 선택합니다.
3. 원하는 플랫폼(모바일, 웹, Kindle)과 모바일 기기(iOS, Android)를 선택합니다. 여러 기기를 선택하면 Campaign에서 다변량 테스트를 사용할 수 없습니다.

### Campaign에서 플랫폼 선택하기 {#selecting-platforms-for-a-campaign}
![모바일, 웹, Kindle 등 푸시 Campaign에 대해 여러 플랫폼을 선택하는 옵션과 iOS, Android 등 여러 기기를 선택하는 옵션.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### Canvas 단계에서 플랫폼 선택하기 {#selecting-platforms-for-a-canvas-step}
![모바일, 웹, Kindle 등 푸시 메시지 단계에 대해 여러 플랫폼을 선택하는 옵션과 iOS, Android 등 여러 기기를 선택하는 옵션.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. **확인**을 선택합니다. **확인**을 선택한 후에는 선택한 플랫폼이나 기기를 변경할 수 없습니다.
5. Campaign 또는 Canvas 설정을 계속 진행합니다.

## 다중 플랫폼 다변량 테스트 실행하기 {#running-a-multi-platform-multivariate-test}

다변량 테스트는 다중 플랫폼 Campaign에서 지원됩니다. 단일 플랫폼 Campaign에서와 마찬가지로 배리언트 이름 옆의 더하기 아이콘을 선택하면 됩니다. 다변량 테스트 생성에 대한 [가이드를 읽어보시고]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) [BrazeAI<sup>TM</sup> 배리언트 선택]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection/)을 활용하여 참여를 자동화하고 극대화하는 것을 권장합니다.

![간편한 다중 플랫폼 다변량 테스트]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## 알아야 할 사항 {#things-to-know}

### 통합 메시징 {#unified-messaging}
**작성** 탭에서 선택한 모든 플랫폼과 기기에 대해 하나의 제목, 메시지, 클릭 시 동작을 지정할 수 있습니다.

미리보기 창에는 각 플랫폼에서 메시지가 어떻게 보이는지 대략적으로 표시됩니다. 글자 수 제한에 도달할 수 있는 위치를 잘 파악할 수 있지만, Campaign을 발송하기 전에 항상 실제 기기에서 메시지를 테스트하는 것을 잊지 마세요.

![iOS, Android, 웹 세 가지 푸시 유형에 대해 하나의 제목, 메시지, 클릭 시 동작 필드가 있는 단일 편집 화면.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### 개별 자산 {#separate-assets}
**자산** 섹션에서 각 플랫폼에 표시할 이미지를 선택하거나 업로드합니다. 기기마다 이미지 및 글자 수에 대한 사양이 다르다는 점에 유의하세요. 도움이 필요하면 [푸시 메시지 및 이미지 형식]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)을 참조하세요.

![푸시 아이콘 이미지, iOS 알림 이미지, Android 알림 이미지, 웹 알림 이미지 필드가 있는 단일 편집 화면의 자산 섹션.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### 알림 유형 {#notification-type}

알림 유형은 기본적으로 "표준 푸시"로 설정되어 있으며 변경할 수 없습니다. Push Stories 또는 인라인 이미지(Android)와 같은 다른 푸시를 생성하려면 각 기기 유형에 대해 별도의 Campaign을 생성하세요.

### 기기별 설정 {#device-specific-settings}

편집기에서 플랫폼별 설정을 편집할 수 있습니다. 여기에는 [푸시 실행 버튼]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/), 알림 채널 및 그룹, TTL, 표시 우선순위, 사운드 등의 설정이 포함됩니다.

기기별 설정에 대한 자세한 내용은 다음 문서 모음을 참조하세요.

- [iOS 옵션]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/)
- [Android 옵션]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/)

### Push Stories

Push Stories는 Android와 iOS에서만 다중 플랫폼으로 사용할 수 있으며, 웹 또는 Kindle을 발송 플랫폼으로 선택하면 이 옵션을 사용할 수 없습니다.