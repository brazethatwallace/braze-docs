---
nav_title: 준비 가이드
article_title: 인앱 메시지 준비 가이드
page_order: 0.5

page_type: reference
description: "이 문서에서는 인앱 메시지를 작성하기 전에 고려해야 할 질문과 모범 사례를 다루며, 타겟팅, 스케줄링, 콘텐츠, 전환 등을 포함합니다."
channel: in-app messages
toc_headers: h2
---

# 인앱 메시지 준비 가이드 {#in-app-message-prep-guide}

> 인앱 메시지를 작성하기 전에 다음 주제들을 고려하면 메시지를 빠르고 쉽게 만들 수 있습니다.

## 일반 고려 사항 {#general-considerations}

- Campaign을 작성하는 경우, 이 메시지의 배리언트를 몇 개나 표시하고 싶으신가요? 배리언트 테스트 아이디어는 [다양한 채널을 위한 팁]({{site.baseurl}}/user_guide/messaging/ab_testing/#tips-different-channels)을 확인하세요.
- Canvas를 작성하는 경우, 이 메시지가 해당 단계에서 다른 메시징 채널과 함께 사용되나요?
- [메시지가 만료]({{site.baseurl}}/canvas_in-app_messages/)되는 시점은 언제로 설정하고 싶으신가요?

## 타겟팅 고려 사항 {#targeting-considerations}

- 인앱 메시지는 앱을 정기적으로 방문하는 사용자에게 가장 적합합니다. 이 오디언스를 포함하고 있나요?
- 사용자가 메시지를 어디에서 보기를 원하시나요? 웹 앱에서? 모바일 앱에서?
- 어떤 이벤트가 이 메시지를 트리거해야 하나요?
- 사용자 중 이전 버전의 앱을 사용하는 사람이 있나요? 그렇다면 메시지의 일부 요소를 볼 수 없을 수 있습니다.
- 이 메시지를 어떤 유형의 기기에 맞춰 작성하고 있나요? **Preview** 상자 또는 **Test** 탭을 사용하여 메시지를 미리 볼 수 있다는 점을 기억하세요. 자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=in-app%20message)를 참조하세요.

## 스케줄링, 지연 및 세션 시작 {#scheduling-delays-and-session-starts}

인앱 메시지 Campaign에 세션 시작 트리거와 함께 **스케줄 지연**이 설정된 경우, 세션을 시작한 후 인앱 메시지가 표시되기 전에 앱을 닫은 사용자도 지연이 만료된 후 다음 세션 시작 시 해당 메시지를 받을 수 있습니다.

이 타이밍은 특히 Campaign에서 **Re-evaluate campaign eligibility before displaying**가 선택되지 않은 경우 예상치 못한 표시 동작을 유발할 수 있습니다.

예를 들어, 사용자가 Campaign 시작 한 달 후에 8초 지연이 설정된 인앱 메시지를 받을 수 있습니다. 이는 사용자가 세션을 시작하고 즉시 세션을 종료한 후, 한 달 뒤에 세션을 다시 시작하고 8초 후에 인앱 메시지를 받는 경우에 발생할 수 있습니다. 앱을 닫지 않고 다른 곳으로 이동한 경우, 앱으로 돌아올 때 인앱 메시지가 표시됩니다.

## 콘텐츠 고려 사항 {#content-considerations}

- 이 메시지에 어떤 언어를 사용할 예정인가요?
- 헤더와 본문 카피는 무엇인가요? 눈길을 끌고 사용자에게 관련성이 있나요?
- 인앱 메시지는 정해진 시간 동안만 표시됩니다. 카피가 간결하고 기억에 남나요?
- [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/)을 사용하여 커스텀 카피를 추가할 예정인가요?
- 전체화면 인앱 메시지의 경우, 이미지 또는 기타 미디어가 [안전 영역]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen/#image-safe-zone) 내에 있나요?
- 설문조사 인앱 메시지의 경우, 속성이나 제출을 기록하고 싶으신가요? 확인 페이지를 설정하셨나요?

## 전환 고려 사항 {#conversion-considerations}

- 이 메시지의 목표는 무엇인가요? 메시지에서 이를 어떻게 표현할 수 있나요?
- 버튼이 사용자에게 적합한 옵션을 제공하나요? [기본 행동 유도]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/#buttons)는 무엇인가요?
- [다른 인앱 콘텐츠로 딥링킹]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#deep-link-to-in-app-content)하고 있나요? 이 인앱 메시지를 사용하여 [권한 또는 푸시 프라이밍 요청]({{site.baseurl}}/user_guide/channels/push/best_practices/)을 보내고 수락하나요?
- 메시지 종료 옵션이 있나요? 없다면 이 스니펫을 복사하여 붙여넣기하면 빠르게 버튼을 만들 수 있습니다:
    ```html
    <a href="appboy://close">X</a>
    ```

## 드래그 앤 드롭 에디터 고려 사항 {#drag-and-drop-editor-considerations}

### 다양한 기기에 대한 딥링크 추가 {#adding-deep-links-for-different-devices}

드래그 앤 드롭 에디터는 기존 에디터와 달리 다양한 기기에 대해 서로 다른 딥링크를 추가하는 것을 지원하지 않습니다.

### 배경 이미지 불투명도 조정 {#adjusting-background-image-opacity}

불투명도 설정은 기존 IAM 에디터와 달리 배경 이미지의 완전한 투명도를 허용하지 않습니다. 불투명도 설정을 사용하여 메시지 배경색을 완전히 투명하게 만들 수 있습니다.

### 최대 너비 설정 {#setting-the-maximum-width}

드래그 앤 드롭 에디터의 최대 너비는 325px로 제한되며, 이는 주로 대시보드 미리보기를 위한 것입니다. 메시지는 더 작은 화면의 기기에서도 올바르게 표시될 수 있습니다.

### 다양한 플랫폼에 대한 서로 다른 배경 선택 {#selecting-different-backgrounds-for-different-platforms}

동일한 메시지에 대해 다양한 플랫폼(예: 웹 및 모바일)에서 서로 다른 배경을 표시하는 것은 불가능합니다.

### 메시지 스타일 적용 {#applying-message-styles}

배경 이미지는 전체 메시지에 적용되며 페이지별로 커스터마이즈할 수 없습니다. 메시지 스타일은 개별 페이지가 아닌 전체 메시지에 적용됩니다.

### 스페이서 블록 높이 측정 {#measuring-spacer-blocks-height}

스페이서 블록의 측정 단위는 픽셀(px)이며 변경할 수 없습니다.

### 지원되는 형식 {#supported-formats}

현재 드래그 앤 드롭 에디터에서는 모달 및 전체화면 인앱 메시지만 지원됩니다.

### 크기 및 종횡비 조정 {#adjusting-to-size-and-aspect-ratio}

모달이 배경 이미지의 크기와 종횡비에 맞게 조정되므로 배경 이미지가 인앱 메시지를 늘립니다. 필요에 따라 비율을 조정할 수 있습니다.

### 배경 이미지 및 클릭 시 동작 {#background-images-and-on-click-behavior}

이러한 설정은 페이지 간에 유지됩니다. 각 페이지에 서로 다른 전체 이미지가 있는 다중 페이지 인앱 메시지의 경우, 사용자가 다음 페이지로 클릭할 수 있도록 버튼을 추가하세요.