{% multi_lang_include developer_guide/prerequisites/roku.md %} 또한 인앱 메시지는 지원되는 최소 SDK 버전을 실행하는 Roku 기기로만 전송됩니다:

{% sdk_min_versions roku:0.1.2 %}

## 메시지 유형 {#message-types}

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## 인앱 메시지 활성화 {#enabling-in-app-messages}

### 1단계: 옵저버 추가 {#step-1-add-an-observer}

인앱 메시지를 처리하려면 `BrazeTask.BrazeInAppMessage`에 옵저버를 추가할 수 있습니다:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### 2단계: 트리거된 메시지에 액세스하기 {#step-2-access-triggered-messages}

그런 다음, 핸들러 내에서 Campaign이 트리거한 최상위 인앱 메시지에 액세스할 수 있습니다:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## 메시지 필드 {#message-fields}

### 처리 {#handling}

다음은 인앱 메시지를 처리하는 데 필요한 필드 목록입니다:

| 필드 | 설명 |
| ------ | ----------- |
| `buttons` | 버튼 목록(빈 목록일 수 있음). |
| `click_action` | `"URI"` 또는 `"NONE"`. 이 필드를 사용하여 인앱 메시지를 클릭할 때 URI 링크로 열 것인지 아니면 메시지를 닫을 것인지 나타냅니다. 버튼이 없는 경우, 인앱 메시지가 표시될 때 사용자가 "확인"을 클릭하면 이 동작이 수행됩니다. |
| `dismiss_type` | `"AUTO_DISMISS"` 또는 `"SWIPE"`. 이 필드를 사용하여 인앱 메시지를 자동으로 닫을지 아니면 스와이프하여 닫을지 나타냅니다. |
| `display_delay` | 인앱 메시지를 표시할 때까지 대기하는 시간(초). |
| `duration` | `dismiss_type`이 `"AUTO_DISMISS"`로 설정된 경우 메시지가 표시되는 시간(밀리초). |
| `extras` | 키-값 페어. |
| `header` | 헤더 텍스트. |
| `id` | 노출 횟수 또는 클릭을 기록하는 데 사용되는 ID. |
| `image_url` | 인앱 메시지 이미지 URL. |
| `message` | 메시지 본문 텍스트. |
| `uri` | `click_action`에 따라 사용자가 이동하게 되는 URI입니다. 이 필드는 `click_action`이 `"URI"`일 때 반드시 포함되어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="처리" }

{% alert important %}
버튼이 포함된 인앱 메시지의 경우, 버튼 텍스트를 추가하기 전에 클릭 동작이 추가되면 메시지 `click_action`도 최종 페이로드에 포함됩니다.
{% endalert %}

### 스타일링 {#styling}

대시보드에서 사용할 수 있는 다양한 스타일 필드도 있습니다:

| 필드 | 설명 |
| ------ | ----------- |
| `bg_color` | 배경색. |
| `close_button_color` | 닫기 버튼 색상. |
| `frame_color` | 배경 화면 오버레이의 색상. |
| `header_text_color` | 헤더 텍스트 색상. |
| `message_text_color` | 메시지 텍스트 색상. |
| `text_align` | "START", "CENTER" 또는 "END". 선택한 텍스트 정렬. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="스타일링" }

또는 인앱 메시지를 구현하고 표준 팔레트를 사용하여 Roku 애플리케이션 내에서 스타일을 지정할 수 있습니다:

### 버튼 {#buttons}

| 필드 | 설명 |
| ------ | ----------- |
| `click_action` | `"URI"` 또는 `"NONE"`. 이 필드를 사용하여 인앱 메시지를 클릭할 때 URI 링크로 열 것인지 아니면 메시지를 닫을 것인지 나타냅니다. |
| `id` | 버튼 자체의 ID 값. |
| `text` | 버튼에 표시할 텍스트. |
| `uri` | `click_action`에 따라 사용자가 이동하게 되는 URI입니다. 이 필드는 `click_action`이 `"URI"`일 때 반드시 포함되어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="버튼" }