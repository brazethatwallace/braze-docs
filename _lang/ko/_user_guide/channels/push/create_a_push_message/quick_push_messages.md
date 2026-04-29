---
nav_title: "빠른 푸시 메시지"
article_title: "빠른 푸시 메시지"
alias: "/quick_push/"
description: "이 문서에서는 빠른 푸시 편집 환경을 사용하여 푸시 Campaign 또는 Canvas를 생성할 때 알아야 할 사항을 설명합니다."
page_order: 4
---

# 빠른 푸시 메시지 {#quick-push-messages}

> 이 문서에서는 빠른 푸시 편집 환경을 사용하여 하나의 작성기에서 여러 플랫폼과 기기를 타겟팅하는 푸시 Campaign 또는 Canvas를 생성할 때 알아야 할 사항을 설명합니다.

Braze에서 푸시 Campaign 또는 Canvas를 생성할 때 여러 플랫폼과 기기를 선택하여 빠른 푸시라는 단일 편집 환경에서 모든 플랫폼을 위한 하나의 메시지를 작성할 수 있습니다.

## 활용 사례 {#use-cases}

이 편집 환경은 다음과 같은 사용 사례에 가장 적합합니다:

- 여러 기기 유형(예: iOS와 Android 모두)으로 발송해야 하는 모바일 푸시 Campaign 및 Canvas 메시지 단계.
- 여러 플랫폼을 빠르고 정확하게 타겟팅해야 하며 플랫폼 간 콘텐츠가 동일한 시간에 민감한 푸시 알림(예: 속보 또는 실시간 경기 업데이트).

## 빠른 푸시 Campaign 또는 Canvas 생성하기 {#creating-a-quick-push-campaign-or-canvas}

여러 플랫폼과 기기를 타겟팅하는 Campaign을 생성하려면:

1. Campaign을 생성하거나 Canvas에 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)를 추가합니다.
2. **푸시 알림**을 선택합니다.
3. 원하는 플랫폼(모바일, 웹, Kindle)과 모바일 기기(iOS, Android)를 선택합니다. 여러 기기를 선택하면 Campaign에서 다변량 테스트를 사용할 수 없습니다.

### Campaign의 플랫폼 선택하기 {#selecting-platforms-for-a-campaign}
![모바일, 웹, Kindle 등 여러 플랫폼과 iOS, Android 등 여러 기기를 선택할 수 있는 푸시 Campaign 옵션.]({% image_buster /assets/img_archive/quick_push_1.png %})

### Canvas 단계의 플랫폼 선택하기 {#selecting-platforms-for-a-canvas-step}
![모바일, 웹, Kindle 등 여러 플랫폼과 iOS, Android 등 여러 기기를 선택할 수 있는 푸시 메시지 단계 옵션.]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4. **확인**을 선택합니다. **확인**을 선택한 후에는 선택한 플랫폼이나 기기를 변경할 수 없습니다.
5. Campaign 또는 Canvas 설정을 계속 진행합니다.

작성기가 평소와 약간 다르게 보일 수 있습니다. 어떤 점이 다른지 계속 읽어보세요.

### 달라진 점 {#whats-different}

**작성** 탭에서 선택한 모든 플랫폼과 기기에 대해 하나의 제목, 메시지, 클릭 시 동작을 지정할 수 있습니다.

미리보기 창에는 각 플랫폼에서 메시지가 어떻게 보이는지 대략적으로 표시됩니다. 글자 수 제한에 도달할 수 있는 위치를 파악하는 데 좋은 지표가 될 수 있지만, Campaign을 발송하기 전에 항상 실제 기기에서 메시지를 테스트하는 것을 잊지 마세요.

![iOS, Android, 웹 세 가지 푸시 유형에 대해 하나의 제목, 메시지, 클릭 시 동작 필드가 있는 단일 편집 보기.]({% image_buster /assets/img_archive/quick_push_2.png %})

**자산** 섹션에서 각 플랫폼에 표시할 이미지를 선택하거나 업로드합니다. 기기마다 이미지와 글자 수에 대한 사양이 다르다는 점을 유의하세요. 도움이 필요하면 [푸시 메시지 및 이미지 형식]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)을 참조하세요.

![푸시 아이콘 이미지, iOS 알림 이미지, Android 알림 이미지, 웹 알림 이미지 필드가 있는 단일 편집 보기의 자산 섹션.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

그런 다음 평소처럼 푸시 Campaign 설정을 완료합니다. 자세한 내용은 [푸시 Campaign 생성하기]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/)를 참조하세요.

## 알아두어야 할 사항 {#things-to-know}

### 알림 유형 {#notification-type}

알림 유형은 기본적으로 "표준 푸시"로 설정되며 변경할 수 없습니다. Push Stories 또는 인라인 이미지(Android)와 같은 다른 푸시를 생성하려면 각 기기 유형별로 별도의 Campaign을 생성하세요.

### 다변량 테스트 {#multivariate-testing}

iOS와 Android 모두와 같이 모바일 플랫폼에서 여러 기기를 선택하면 Campaign에서 다변량 테스트를 사용할 수 없습니다. 다변량 테스트를 수행하려면 각 기기 유형별로 별도의 Campaign을 생성하세요.

### 기기별 설정 {#device-specific-settings}

편집기에서 플랫폼별 설정을 편집할 수 있습니다. 여기에는 [푸시 실행 버튼]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/), 알림 채널 및 그룹, TTL, 표시 우선순위, 사운드 등의 설정이 포함됩니다.

빠른 푸시 Campaign을 사용하여 iOS와 Android를 동시에 타겟팅할 때는 푸시 실행 버튼이 지원되지 않습니다. 기기별 설정에 대한 자세한 내용은 다음 문서 모음을 참조하세요:

- [iOS 옵션]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/)
- [Android 옵션]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/)