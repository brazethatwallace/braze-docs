---
nav_title: "커스텀 HTML"
article_title: "커스텀 HTML"
page_order: 4
page_type: reference
description: "이 문서에서는 JavaScript 메서드, 버튼 추적, Braze에서 인터랙티브 HTML 미리보기 사용 등 사용자 지정 코드 인앱 메시지에 대한 개요를 제공합니다."
channel:
  - in-app messages
---

# 커스텀 HTML 인앱 메시지 {#custom-html-messages}

> 표준 인앱 메시지를 다양한 방식으로 커스터마이징할 수 있지만, HTML, CSS, JavaScript를 사용하여 디자인하고 구축한 메시지를 활용하면 Campaign의 외관과 느낌을 더욱 세밀하게 제어할 수 있습니다. 간단한 구성만으로 커스텀 기능과 브랜딩을 구현하여 모든 요구 사항에 맞출 수 있습니다.

이 메시지 유형은 [기존 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)에서 사용할 수 있습니다.

## 작동 방식 {#how-it-works}

HTML 인앱 메시지를 사용하면 다음을 포함하여 메시지의 외관과 느낌을 더욱 세밀하게 제어할 수 있습니다:

- 커스텀 글꼴 및 스타일
- 동영상
- 다중 이미지
- 클릭 시 동작
- 인터랙티브 구성요소
- 커스텀 애니메이션

커스텀 HTML 메시지는 [JavaScript 브리지](#javascript-bridge) 메서드를 사용하여 이벤트를 기록하고, 커스텀 속성을 설정하고, 메시지를 닫는 등의 작업을 수행할 수 있습니다! HTML 인앱 메시지를 사용하고 커스터마이징하는 방법에 대한 자세한 안내와 시작에 도움이 되는 HTML5 인앱 메시지 템플릿 세트가 포함된 [GitHub 리포지토리](https://github.com/braze-inc/in-app-message-templates)를 확인하세요.

{% alert note %}
웹 SDK를 통해 HTML 인앱 메시지를 활성화하려면 Braze에 `allowUserSuppliedJavascript` 초기화 옵션을 제공해야 합니다. 예: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. 이는 보안상의 이유로, HTML 인앱 메시지가 JavaScript를 실행할 수 있으므로 사이트 관리자가 이를 활성화해야 합니다.
{% endalert %}

## JavaScript 브리지 {#javascript-bridge}

{% include javascript_bridge/reference.md %}

## 링크 기반 동작 {#link-based-actions}

커스텀 JavaScript 외에도 Braze SDK는 이러한 편리한 URL 단축키를 사용하여 분석 데이터를 전송할 수 있습니다. 이러한 쿼리 매개변수와 URL 스킴은 모두 대소문자를 구분합니다.

### 버튼 클릭 추적(지원 중단) {#button-click-tracking-deprecated}

{% alert warning %}
`abButtonID` 사용은 [미리보기가 포함된 HTML]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/#html-upload-with-preview/) 메시지 유형에서 지원되지 않습니다. 자세한 내용은 [업그레이드 가이드]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/#html-upload-with-preview)를 참조하세요.
{% endalert %}

인앱 메시지 분석을 위해 버튼 클릭을 기록하려면 딥링크, 리디렉션 URL 또는 앵커 요소 `<a>`에 쿼리 매개변수로 `abButtonId`를 추가할 수 있습니다. "Button 1" 클릭을 기록하려면 `?abButtonId=0`을, "Button 2" 클릭을 기록하려면 `?abButtonId=1`을 사용하세요.

다른 URL 매개변수와 마찬가지로 첫 번째 매개변수는 물음표 `?`로 시작해야 하며, 이후 매개변수는 앰퍼샌드 `&`로 구분해야 합니다.

#### URL 예시 {#example-urls}

- `https://example.com/?abButtonId=0` - Button 1 클릭
- `https://example.com/?abButtonId=1` - Button 2 클릭
- `https://example.com/?utm_source=braze&abButtonId=0` - 기존 URL 매개변수가 포함된 Button 1 클릭
- `myApp://deep-link?page=home&abButtonId=1` - Button 2 클릭이 포함된 모바일 딥링크
- `<a href="https://example.com/?abButtonId=1">` - Button 2 클릭이 포함된 앵커 요소 `<a>`

{% alert note %}
인앱 메시지는 Button 1과 Button 2 클릭만 지원합니다. 이 두 버튼 ID 중 하나를 지정하지 않는 URL은 일반적인 "본문 클릭"으로 기록됩니다.
{% endalert %}

### 새 창에서 링크 열기(모바일 전용) {#open-link-in-new-window-mobile-only}

앱 외부의 링크를 새 창에서 열려면 `?abExternalOpen=true`를 설정하세요. 링크를 열기 전에 메시지가 닫힙니다.

딥링킹의 경우 Braze는 `abExternalOpen` 값에 관계없이 URL을 엽니다.

### 딥링크로 열기(모바일 전용) {#open-as-deeplink-mobile-only}

Braze가 HTTP 또는 HTTPS 링크를 딥링크로 처리하도록 하려면 `?abDeepLink=true`를 설정하세요.

이 쿼리 문자열 매개변수가 없거나 `false`로 설정된 경우, Braze는 호스트 앱 내부의 내장 웹 브라우저에서 웹 링크를 열려고 시도합니다.

### 인앱 메시지 닫기 {#close-in-app-message}

인앱 메시지를 닫으려면 `brazeBridge.closeMessage()` JavaScript 메서드를 사용할 수 있습니다.

예를 들어, `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>`는 인앱 메시지를 닫습니다.

## 미리보기가 포함된 HTML 업로드 {#html-upload-with-preview}

커스텀 HTML 인앱 메시지를 작성할 때 Braze에서 직접 인터랙티브 콘텐츠를 미리 볼 수 있습니다.

편집기의 메시지 미리보기 패널은 메시지에 포함된 JavaScript를 렌더링하는 사실적인 미리보기를 보여줍니다. 미리보기 패널에서 페이지 넘기기, 양식 또는 설문조사 제출, JavaScript 애니메이션 보기 등을 통해 커스텀 메시지를 미리 보고 상호작용할 수 있습니다!

![페이지를 스와이프하여 HTML 미리보기와 상호작용하는 모습.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
HTML에서 사용하는 `brazeBridge` JavaScript 메서드는 대시보드에서 미리보기하는 동안 고객 프로필을 업데이트하지 않습니다.
{% endalert %}

### SDK 요구 사항 {#supported-sdk-versions}

인앱 메시지의 HTML 미리보기를 사용하려면 다음 최소 Braze SDK 버전으로 업그레이드해야 합니다:

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
이 메시지 유형은 특정 최신 SDK 버전에서만 수신할 수 있으므로, 지원되지 않는 SDK 버전을 사용하는 사용자는 메시지를 수신하지 못합니다. 사용자 기반의 상당 부분이 도달 가능한 상태가 된 후에 이 메시지 유형을 채택하거나, 앱 버전이 요구 사항보다 최신인 사용자만 타겟팅하는 것을 고려하세요. [최신 앱 버전별 필터링]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)에 대해 자세히 알아보세요.
{% endalert %}

### Campaign 생성 {#instructions}

모바일 앱 사용자가 **사용자 지정 코드** 인앱 메시지를 수신하려면 지원되는 SDK 버전으로 업그레이드해야 합니다. 최신 Braze SDK 버전에 의존하는 Campaign을 시작하기 전에 사용자에게 [모바일 앱 업그레이드를 유도]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/)하는 것을 권장합니다.

#### 자산 파일 {#asset-files}

HTML 업로드로 사용자 지정 코드 인앱 메시지를 생성할 때, Campaign 자산을 [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)에 업로드하여 메시지에서 참조할 수 있습니다.

업로드에 지원되는 파일 유형은 다음과 같습니다:

| 파일 유형 | 파일 확장자 |
| :--------------- | :-------------------------------- |
| 글꼴 파일 | `.ttf`, `.woff`, `.otf`, `.woff2` |
| SVG 이미지 | `.svg` |
| JavaScript 파일 | `.js` |
| CSS 파일 | `.css` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="자산 파일" }

Braze는 두 가지 이유로 자산을 미디어 라이브러리에 업로드하는 것을 권장합니다:

1. 미디어 라이브러리를 통해 Campaign에 추가된 자산은 사용자가 오프라인이거나 인터넷 연결이 불안정한 경우에도 메시지를 표시할 수 있습니다.
2. Braze에 업로드된 자산은 여러 Campaign에서 재사용할 수 있습니다.

##### 자산 파일 추가 {#adding-asset-files}

Campaign에 새 자산 또는 기존 자산을 추가할 수 있습니다.

Campaign에 새 자산을 추가하려면 드래그 앤 드롭 섹션을 사용하여 파일을 업로드하세요. 이 섹션에서 추가된 자산은 미디어 라이브러리에도 자동으로 추가됩니다. 이미 미디어 라이브러리에 업로드한 자산을 추가하려면 **미디어 라이브러리에서 추가**를 선택하세요.

자산이 추가되면 **이 Campaign의 자산** 섹션에 표시됩니다.

자산의 파일 이름이 로컬 HTML 자산의 파일 이름과 일치하면 자동으로 교체됩니다(예: `cat.png`이 업로드되고 `<img src="cat.png" />`이 존재하는 경우).

그렇지 않으면 목록에서 자산 위에 마우스를 올리고 <i class="fas fa-copy"></i> **복사**를 선택하여 파일의 URL을 클립보드에 복사하세요. 그런 다음 원격 자산을 참조할 때와 마찬가지로 복사한 자산 URL을 HTML에 붙여넣으세요.

### HTML 편집기 {#html-editor}

HTML에서 변경한 내용은 입력하는 대로 미리보기 패널에 자동으로 렌더링됩니다. HTML에서 사용하는 [`brazeBridge` JavaScript](#bridge) 메서드는 대시보드에서 미리보기하는 동안 고객 프로필을 업데이트하지 않습니다.

{% alert tip %}
HTML 편집기 내에서 <i class="fa-solid fa-magnifying-glass"></i> **검색**을 선택하여 코드 내에서 검색할 수 있습니다!
{% endalert %}

### 버튼 추적 {#button-tracking-improvements}

[`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/) JavaScript 메서드를 사용하여 사용자 지정 코드 인앱 메시지 내에서 성과를 추적할 수 있습니다. 이를 통해 `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` 또는 `brazeBridge.logClick()`을 사용하여 각각 "Button 1", "Button 2", "본문 클릭"을 프로그래밍 방식으로 추적할 수 있습니다.

| 클릭 | 메서드 |
| ---------- | ---------------------------- |
| Button 1   | `brazeBridge.logClick('0')` |
| Button 2   | `brazeBridge.logClick('1')` |
| 본문 클릭 | `brazeBridge.logClick()`    |
| 커스텀 버튼 추적 | `brazeBridge.logClick('your custom name here')` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="버튼 추적" }

{% alert note %}
이 버튼 추적 방법은 이전의 자동 클릭 추적 방법(예: `?abButtonId=0`)을 대체하며, 해당 방법은 제거되었습니다.
{% endalert %}

미리보기가 포함된 HTML 메시지에서 두 개 이상의 추적 버튼이 필요한 경우 [`brazeBridge.logClick(button_id)`](#button-tracking-improvements)를 사용하세요. Button 1과 Button 2는 `'0'`과 `'1'`에 매핑되며, 추가 버튼은 커스텀 ID를 사용합니다(Campaign당 최대 100개의 고유 ID). 버튼 ID의 문자 제한에 대해서는 [버튼 추적](#button-tracking-improvements)을 참조하세요.

### 커스텀 HTML 링크 및 닫기 동작 문제 해결 {#troubleshoot-custom-html-links-and-close-behavior}

#### 버튼 클릭 시 링크가 열리지 않음 {#button-clicks-do-not-open-the-link}

커스텀 HTML 인앱 메시지의 버튼이 클릭 시 로드되지 않는 경우, 링크가 유효한 URL 또는 지원되는 딥링크 스킴을 사용하는지 확인하세요. 잘못된 형식의 URL이나 지원되지 않는 커스텀 스킴은 클릭 동작이 완료되지 않을 수 있습니다.

#### 메시지 닫기 시 본문 클릭 {#body-clicks-when-closing-the-message}

`brazeBridge.closeMessage()`를 호출하면 메시지가 닫히지만 자체적으로 분석을 기록하지는 않습니다. 사용자가 메시지를 닫을 때 본문 클릭을 기록하려면 `brazeBridge.closeMessage()` 전에 `brazeBridge.logClick()`을 호출하여 플랫폼 간 클릭 로깅이 일관되게 유지되도록 하세요.

### 하위 호환되지 않는 변경 사항 {#backward-incompatible-changes}

1. 이 새로운 메시지 유형에서 가장 주목할 만한 호환되지 않는 변경 사항은 SDK 요구 사항입니다. 앱 SDK가 최소 [SDK 버전 요구 사항](#supported-sdk-versions)을 충족하지 않는 사용자에게는 메시지가 표시되지 않습니다.
2. 이전에 모바일 앱에서 지원되던 `braze://close` 딥링크는 JavaScript `brazeBridge.closeMessage()`로 대체되어 제거되었습니다. 이를 통해 웹이 딥링크를 지원하지 않으므로 크로스 플랫폼 HTML 메시지가 가능해집니다.
3. 버튼 ID에 `?abButtonId=0`을 사용하던 자동 클릭 추적과 닫기 버튼의 "본문 클릭" 추적이 제거되었습니다. 다음 코드 예시는 새로운 클릭 추적 JavaScript 메서드를 사용하도록 HTML을 변경하는 방법을 보여줍니다:

   | 이전 | 이후 |
   |:-------- |:------------|
   |<code>&lt;a href="braze://close"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="braze://close?abButtonId=0"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="app://deeplink" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "braze://close?abButtonId=1"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|
{: .reset-td-br-1 .reset-td-br-2 aria-label="하위 호환되지 않는 변경 사항" }