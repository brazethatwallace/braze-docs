---
nav_title: Roku SDK
article_title: Roku SDK 리포지토리 가이드
page_order: 8
description: "GitHub에서 미러링된 Braze Roku SDK README 참조입니다."
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze Roku SDK 소개 {#about-the-braze-roku-sdk}

Braze Roku SDK는 Braze 메시징, 분석 및 사용자 참여 기능을 애플리케이션에 통합하는 데 도움을 줍니다.

시작하려면 다음 리소스를 참조하세요:

- [Braze 사용자 가이드](https://www.braze.com/docs/user_guide/introduction/)
- [Braze 개발자 가이드](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=roku)

## 초기 SDK 통합 {#initial-sdk-integration}

Braze Roku SDK는 분석, 세분화 및 참여에 사용할 정보를 보고하기 위한 API를 제공합니다.

## 1단계: 파일 추가 {#step-1-add-files}

1. `source` 디렉토리의 앱에 `BrazeSDK.brs`를 추가합니다.
2. `components` 디렉토리의 앱에 `BrazeTask.brs` 및 `BrazeTask.xml`을 추가합니다.

## 2단계: 참조 추가 {#step-2-add-references}

다음 `script` 요소를 사용하여 기본 장면에서 `BrazeSDK.brs`에 대한 참조를 추가합니다:

``` text
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## 3단계: 구성 {#step-3-configure}

`main.brs`에서 글로벌 노드에 Braze 구성을 설정합니다:

``` text
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = "YOUR_API_KEY_HERE"
config[config_fields.ENDPOINT] = "YOUR_ENDPOINT_HERE (e.g. https://sdk.iad-01.braze.com/)"
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

## 4단계: Braze 초기화 {#step-4-initialize-braze}

Braze 인스턴스를 초기화합니다:

``` text
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## 인앱 메시지 설정 {#in-app-message-setup}

인앱 메시지를 처리하려면 `BrazeTask.BrazeInAppMessage`에 옵저버를 추가할 수 있습니다:

``` text
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

그런 다음, 핸들러 내에서 Campaign이 트리거한 최상위 인앱 메시지에 액세스할 수 있습니다:

``` text
in_app_message = m.BrazeTask.BrazeInAppMessage
```

이후 인앱 메시지로 수행할 작업을 결정할 수 있습니다. 사용 가능한 필드 중 일부는 다음과 같습니다:

- `in_app_message.message` - 인앱 메시지의 본문 텍스트
- `in_app_message.buttons` - 버튼 목록(빈 목록일 수 있음).
- `in_app_message.id` - 노출 횟수 또는 클릭을 기록할 때 사용하는 ID
- `in_app_message.extras` - 키/값 쌍
- `in_app_message.image_url` - 이미지 URL
- `in_app_message.click_action` - 버튼이 없는 경우, IAM이 표시될 때 사용자가 "확인"을 클릭하면 수행되는 동작입니다. `"URI"` 또는 `"NONE"`일 수 있습니다.
- `in_app_message.dismiss_type` - `"AUTO_DISMISS"` 또는 `"SWIPE"`일 수 있습니다.
- `in_app_message.display_delay` - 인앱 메시지를 표시할 때까지 대기하는 시간(초)
- `in_app_message.duration` - `dismiss_type`이 `"AUTO_DISMISS"`인 경우 메시지가 표시되는 시간(밀리초)
- `in_app_message.header` - 인앱 메시지의 헤더 텍스트
- `in_app_message.uri` - `click_action`이 `"URI"`인 경우 표시되어야 하는 URI

대시보드에서 사용할 수 있는 다양한 스타일링 필드도 있습니다. 또는 표준 팔레트를 사용하여 Roku 애플리케이션 내에서 인앱 메시지를 구현하고 스타일을 지정할 수 있습니다.
- `in_app_message.bg_color` - 배경 색상
- `in_app_message.close_button_color` - 닫기 버튼 색상
- `in_app_message.frame_color` - 배경 화면 오버레이 색상
- `in_app_message.header_text_color` - 헤더 텍스트 색상
- `in_app_message.message_text_color` - 메시지 텍스트 색상
- `in_app_message.text_align` - `"START"`, `"CENTER"` 또는 `"END"`일 수 있습니다.

버튼 필드는 다음과 같습니다:
- `buttons[0].click_action` - `uri` 필드를 열도록 `"URI"`로 설정할 수 있습니다. 인앱 메시지를 닫도록 `"NONE"`으로 설정할 수 있습니다.
- `buttons[0].id` - 버튼 자체의 ID 값
- `buttons[0].text` - 버튼에 표시할 텍스트
- `buttons[0].uri` - `click_action`이 `"URI"`인 경우 표시되어야 하는 URI
- `buttons[0].bg_color` - 버튼 배경 색상
- `buttons[0].border_color` - 버튼 테두리 색상
- `buttons[0].text_color` - 버튼 텍스트 색상

메시지가 표시되거나 확인되면 노출 횟수를 기록합니다:

``` text
LogInAppMessageImpression(in_app_message.id, brazetask)
```

사용자가 메시지를 클릭하면 클릭을 기록합니다:
``` text
LogInAppMessageClick(in_app_message.id, brazetask)
```
그런 다음 `in_app_message.click_action`을 처리합니다.

사용자가 버튼을 클릭하면 버튼 클릭을 기록합니다:

``` text
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```
그런 다음 `inappmessage.buttons[selected].click_action`을 처리합니다.

인앱 메시지를 처리한 후에는 해당 필드를 지워야 합니다:

``` text
m.BrazeTask.BrazeInAppMessage = invalid
```

## 기본 SDK 통합 완료 {#basic-sdk-integration-complete}

이제 Braze가 애플리케이션에서 데이터를 수집합니다. SDK에 속성, 이벤트 및 구매를 기록하는 방법에 대해서는 공개 설명서를 참조하세요. 샘플 앱의 장면 `MainScene.brs`에도 API 사용 예제가 포함되어 있습니다.

`BrazeInAppMessage.brs` 및 `CustomSideBySideInAppMessage.brs`는 인앱 메시지 처리 예제를 보여줍니다. `MainScene.brs`의 `onInAppMessageTriggered()`는 여러 레이아웃을 지원하는 방법을 보여줍니다.

## 추가 참조 {#additional-reference}

`torchietv` 디렉토리에는 Braze SDK가 통합된 샘플 앱이 포함되어 있습니다.
<!-- END GENERATED README CONTENT -->

리포지토리 세부 정보 및 샘플 프로젝트는 [https://github.com/braze-inc/braze-roku-sdk](https://github.com/braze-inc/braze-roku-sdk)를 참조하세요.