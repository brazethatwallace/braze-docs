---
nav_title: 기존 에디터
article_title: 기존 에디터에서 인앱 메시지 만들기
page_order: 2
description: "이 참조 문서에서는 Campaigns 또는 Canvas를 사용하여 Braze 플랫폼에서 인앱 메시지를 만드는 방법을 다룹니다."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# 기존 에디터로 인앱 메시지 만들기 {#create-an-in-app-message-with-the-traditional-editor}

> Braze 플랫폼에서 Campaigns, Canvas 또는 API 캠페인을 사용하여 인앱 메시지 또는 인브라우저 메시지를 만들 수 있습니다. 편리한 [인앱 메시지 준비 가이드]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices)를 활용하여 메시지를 미리 계획하고 모든 자료를 사전에 준비하는 것을 적극 권장합니다.

## 1단계: 메시지를 작성할 위치 선택 {#create-new-campaign-in-app}

메시지를 Campaign으로 보낼지 Canvas로 보낼지 확실하지 않으신가요? Campaigns는 단일 타겟 메시징에 적합하고, Canvases는 다단계 사용자 여정에 더 적합합니다.

{% tabs %}
{% tab Campaign %}

1. **메시징** > **Campaigns**로 이동하여 **캠페인 생성**을 선택합니다.
2. **인앱 메시지**를 선택합니다. 인앱 메시지는 멀티채널 캠페인에서는 사용할 수 없습니다.
3. 캠페인에 명확하고 의미 있는 이름을 지정합니다.
4. 필요에 따라 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams)와 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가합니다.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder)를 사용할 때 특정 태그로 필터링할 수 있습니다.
5. 캠페인에 필요한 만큼 배리언트를 추가하고 이름을 지정합니다. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

{% alert tip %}
캠페인의 모든 메시지가 유사하거나 동일한 콘텐츠를 가질 경우, 추가 배리언트를 추가하기 전에 메시지를 먼저 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. Canvas 작성기를 사용하여 [Canvas를 만듭니다]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).
2. Canvas를 설정한 후 Canvas 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 지정합니다.
3. [단계 스케줄]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#schedule-delay)을 선택하고 필요에 따라 지연을 지정합니다. 인앱 메시지를 포함하는 단계는 액션 기반으로 설정할 수 없습니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. Segments를 지정하고 추가 필터를 추가하여 이 단계의 수신자를 더 세밀하게 조정할 수 있습니다. 오디언스 옵션은 지연 후 메시지가 전송되는 시점에 확인됩니다.
5. [진행 동작]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)을 선택합니다.
6. 메시지와 함께 사용할 다른 메시징 채널을 선택합니다.

{% alert important %}
단일 단계에 여러 인앱 메시지 배리언트를 포함할 수 없습니다.
{% endalert %}

Canvas 관련 추가 정보는 [Canvas의 인앱 메시지]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas)에서 확인할 수 있습니다.

{% endtab %}
{% endtabs %}

## 2단계: 전달 플랫폼 지정 {#step-2-specify-delivery-platforms}

먼저 메시지를 수신할 플랫폼을 선택합니다. 이 선택을 사용하여 캠페인의 전달을 특정 앱 세트로 제한할 수 있습니다. 예를 들어, 사용자에게 모바일 앱 다운로드를 권장하는 인브라우저 메시지에 대해 **Web Browsers**를 선택하여 이미 앱을 다운로드한 후에는 메시지를 받지 않도록 할 수 있습니다. 플랫폼 선택은 각 배리언트에 따라 다르므로 플랫폼별 메시지 참여를 테스트해 볼 수 있습니다.

| 플랫폼 | 메시지 전달 |
|---------------------------------|------------------------------|
| Mobile Apps | iOS, Android 및 Vega SDK |
| Web Browsers | Web SDK |
| Mobile Apps 및 Web Browsers 모두 | iOS, Android, Vega 및 Web SDK |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: 전달 플랫폼 지정" }

## 3단계: 메시지 유형 지정 {#step-3-specify-your-message-types}

전송 플랫폼을 선택한 후 관련 메시지 유형, 레이아웃 및 기타 옵션을 살펴보세요. [메시지 유형]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types) 페이지에서 각 메시지의 예상 동작과 모양에 대해 자세히 알아보거나, 다음 표에서 링크된 메시지 유형을 클릭하세요.

어떤 메시지 유형을 사용할지 결정할 때 메시지가 차지하는 공간과 사용자 경험에 얼마나 방해가 될 수 있는지를 고려하세요.

- **슬라이드업** 메시지는 가장 방해가 적으며, 콘텐츠를 차단하지 않고 은은하게 나타납니다.
- **모달** 메시지는 중간 수준으로, 화면을 완전히 차지하지 않으면서도 주의를 끌기에 충분히 눈에 띕니다.
- **전체화면** 메시지는 가장 주목도가 높으며 중요한 공지사항이나 프로모션에 가장 적합합니다.

콘텐츠가 복잡할수록 더 많은 공간이 필요하며, 사용자의 흐름을 방해할 가능성이 높아집니다.

### 메시지 유형 {#message-types}

이 인앱 메시지는 모바일 앱과 웹 애플리케이션 모두에서 사용할 수 있습니다.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table aria-label="메시지 유형" class="tg">
  <caption>메시지 유형</caption>
<thead>
  <tr>
    <th>메시지 유형</th>
    <th>유형 설명</th>
    <th>사용 가능한 레이아웃</th>
    <th>기타 옵션</th>
    <th>권장 사용</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/fullscreen'>전체화면</a></td>
    <td>메시지 블록으로 전체 화면을 덮는 메시지입니다.</td>
    <td>
      <ul>
      <li>이미지 및 텍스트</li>
      <li>이미지만</li>
      </ul>
    </td>
    <td>기기 방향 강제 적용(세로 또는 가로)</td>
    <td>크고 대담하게! 가장 중요한 캠페인, 중요한 알림 또는 대규모 프로모션과 같이 사용자가 콘텐츠를 반드시 보도록 하고 싶을 때 사용하세요.<br><br>모바일 기기에서는 기기의 방향이 메시지의 방향과 일치하지 않으면 세로 및 가로 메시지가 표시되지 않습니다.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/modal'>모달</a></td>
    <td>화면 오버레이와 메시지 블록으로 전체 화면을 덮는 메시지입니다.</td>
    <td>
      <ul>
      <li>텍스트(선택적 이미지 포함)</li>
      <li>이미지만</li>
      </ul>
    </td>
    <td>해당 없음</td>
    <td>좋은 중간 지점입니다. 새로운 기능을 사용해 보도록 권장하거나 프로모션을 활용하도록 유도하는 등 사용자의 주의를 확실히 끌어야 할 때 사용하세요.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/slideup'>슬라이드업</a></td>
    <td>화면의 나머지 부분을 차단하지 않고 지정된 위치에 슬라이드되어 나타나는 메시지입니다.</td>
    <td>해당 없음</td>
    <td>해당 없음</td>
    <td>방해가 되지 않으며 화면 공간을 가장 적게 차지합니다. 새로운 기능, 공지사항, 쿠키 사용 등 작은 정보를 사용자에게 알릴 때 사용하세요.<br></td>
  </tr>
</tbody>
</table>

### 고급 메시지 유형 {#advanced-message-types}

이 인앱 메시지는 필요에 맞게 커스터마이징할 수 있습니다.

<table aria-label="고급 메시지 유형" class="tg">
  <caption>고급 메시지 유형</caption>
<thead>
  <tr>
    <th>메시지 유형</th>
    <th>유형 설명</th>
    <th>사용 가능한 레이아웃</th>
    <th>요구 사항</th>
    <th>권장 사용</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#custom-html-messages'>커스텀 HTML 메시지</a></td>
    <td>커스텀 코드(HTML, CSS 및/또는 JavaScript)에서 정의한 대로 작동하는 커스텀 메시지입니다.</td>
    <td>해당 없음</td>
    <td>인앱 메시지가 작동하려면 <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> 초기화 옵션을 <code>true</code>로 설정해야 합니다.</td>
    <td>인앱 메시지의 모든 장점을 원하면서도 추가 기능이 필요하거나 브랜드에 맞는 외관을 유지하고 싶을 때 좋은 옵션입니다. 메시지의 모든 세부 사항(글꼴, 색상, 모양, 크기, 버튼 등)을 변경할 수 있습니다. <br><br>사용 사례 예시로는 사용자에게 앱 피드백 요청, 이메일 수집 양식 또는 페이지 형식 메시지가 있습니다.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#email-capture-form'>이메일 수집 양식</a></td>
    <td>일반적으로 뷰어의 이메일을 수집하는 데 사용됩니다.</td>
    <td>해당 없음</td>
    <td>인앱 메시지가 작동하려면 <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> 초기화 옵션을 <code>true</code>로 설정해야 합니다.</td>
    <td>사용자에게 이메일 주소를 제출하도록 요청할 때 사용합니다.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#web-modal-css'>CSS가 포함된 웹 모달</a></td>
    <td>커스터마이징 가능한 CSS가 포함된 웹용 모달 메시지입니다.</td>
    <td>
      <ul>
      <li>텍스트(선택적 이미지 포함)</li>
      <li>이미지만</li>
      </ul>
    </td>
    <td>CSS가 포함된 웹 모달은 Web SDK에서만 사용할 수 있으며 <b>Web Browsers</b>를 선택한 후에만 사용할 수 있습니다.</td>
    <td>커스텀 CSS를 업로드하거나 작성하여 아름답고 완전히 커스텀 스타일의 메시지를 만들고 싶을 때 사용합니다.</td>
  </tr>
</tbody>
</table>

{% alert important %}
Braze가 코드에 닫기 또는 해제 버튼이 포함되어 있지 않음을 감지하면 추가하도록 요청합니다. 편의를 위해 코드에 복사하여 붙여넣을 수 있는 스니펫을 제공합니다: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## 4단계: 인앱 메시지 작성 {#step-4-compose-your-in-app-message}

**작성** 탭에서 메시지의 콘텐츠와 동작의 모든 측면을 편집할 수 있습니다.

![신규 고객을 환영하고 사용자 프로필 설정을 안내하는 브랜드 인앱 메시지 예시.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

**작성** 탭의 콘텐츠는 이전 단계에서 선택한 메시지 옵션에 따라 달라지지만, 다음 옵션 중 하나를 포함할 수 있습니다:

### 언어 {#language}

**Add Languages**를 선택하고 제공된 목록에서 원하는 언어를 선택합니다. 이렇게 하면 메시지에 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic)가 삽입됩니다. 콘텐츠를 작성하기 전에 언어를 선택하여 Liquid에서 적절한 위치에 텍스트를 입력할 수 있도록 하는 것을 권장합니다. [사용 가능한 언어의 전체 목록]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported)을 참조하세요.

### 이미지 {#image}

메시지 유형에 따라 **Upload Image**, **Pick a Badge** 또는 **Font Awesome**을 사용할 수 있습니다. 이미지를 업로드하려면 **이미지 추가**를 선택하거나 이미지 URL을 제공합니다. **이미지 추가**를 선택하면 **미디어 라이브러리**가 열리며, 이전에 업로드한 이미지를 선택하거나 새 이미지를 추가할 수 있습니다. 각 메시지 유형과 플랫폼에는 고유한 권장 비율과 요구 사항이 있을 수 있으므로, 이미지를 의뢰하거나 처음부터 만들기 전에 반드시 확인하세요.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### 헤더 및 본문 {#header-and-body}

원하는 내용을 작성하세요! 완전히 커스텀한 문구(종종 커스텀 HTML 기능 포함)와 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) 및 기타 유형의 개인화를 포함할 수 있습니다. 메시지를 빠르게 전달하고 고객이 클릭하도록 유도할수록 좋습니다! 명확하고 간결한 헤더와 메시지 콘텐츠를 권장합니다.

일부 메시지 유형은 헤더가 필요하지 않으므로 요청하지 않습니다.

#### 팁 {#tips}

##### AI 문구 생성 {#generating-ai-copy}

멋진 문구를 만드는 데 도움이 필요하신가요? [AI 카피라이팅 어시스턴트]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)를 사용해 보세요. 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있는 사람이 작성한 것 같은 마케팅 문구를 생성합니다.

![인앱 메시지 작성기의 메시지 필드에 있는 AI 카피라이터 시작 버튼.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### 오른쪽에서 왼쪽으로 쓰는 메시지 만들기 {#creating-right-to-left-messages}

아랍어나 히브리어와 같은 오른쪽에서 왼쪽으로 쓰는 메시지를 작성하는 데 도움이 필요하신가요? 모범 사례는 [오른쪽에서 왼쪽으로 쓰는 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)를 참조하세요.

### 버튼 텍스트 {#buttons}

메시지 유형에 따라 본문 텍스트 아래에 최대 두 개의 버튼을 표시할 수 있습니다. 커스텀 버튼 텍스트와 색상을 만들고 편집할 수 있습니다. 이메일 수집 양식 내에 서비스 약관 링크를 추가할 수도 있습니다.

버튼을 하나만 사용하도록 선택하면, 추가 버튼을 위한 공간을 남기지 않고 메시지 하단의 사용 가능한 공간을 자동으로 차지하도록 조정됩니다.

#### 기본 버튼 선택 {#choosing-a-primary-button}

이 버튼들을 자체 색상으로 포맷하기로 결정한 경우, 더 선호하는 결과에 Button 2를 사용하는 것을 권장합니다.

즉, 사용자가 한 버튼을 다른 버튼보다 더 많이 클릭하기를 원한다면 오른쪽에 배치하세요. 오른쪽 버튼은 종종 더 높은 클릭 가능성을 보여주며, 특히 메시지의 나머지 부분과 다소 대비되거나 눈에 띄는 색상을 가진 경우 더욱 그렇습니다. 이는 왼쪽 버튼이 메시지와 시각적으로 더 잘 어울릴 때 더욱 강조됩니다.

![인앱 메시지의 기본 및 보조 버튼]({% image_buster /assets/img/primary-secondary-buttons.png %})

### 클릭 시 동작 {#button-actions}

고객이 인앱 메시지의 버튼을 클릭하면 다음 동작을 사용할 수 있습니다.

| 동작 | 설명 |
|---|---|
| 웹 URL로 리디렉션 | 네이티브가 아닌 웹 페이지를 엽니다. |
| [앱으로 딥링크]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | 앱의 기존 화면으로 딥링크합니다. |
| 메시지 닫기 | 현재 활성 메시지를 닫습니다. |
| 커스텀 이벤트 기록 | 트리거할 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events)를 선택합니다. 다른 인앱 메시지를 표시하거나 추가 메시징을 트리거하는 데 사용할 수 있습니다. |
| 커스텀 속성 기록 | 현재 사용자에 대해 설정할 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)을 선택합니다. |
| 푸시 권한 요청 | 네이티브 푸시 권한을 표시합니다. [푸시 프라이밍]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)과 사용자에게 푸시를 안내하기 위한 [모범 사례]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#best-practices)에 대해 자세히 알아보세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="클릭 시 동작" }

참고: __푸시 권한 요청__, __커스텀 이벤트 기록__ 및 __커스텀 속성 기록__ 옵션에는 다음 최소 SDK 버전이 필요합니다:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### iOS 기기 옵션 {#ios-device-options}

원하는 경우 인앱 메시지를 iOS 기기에만 전송하도록 제한할 수 있습니다. 이렇게 하려면 **Change**를 클릭하고 **Only send to iOS devices**를 선택합니다.

### 메시지 닫기 {#message-close}

다음 옵션 중에서 선택합니다:

- **Dismiss Automatically:** 메시지가 화면에 표시될 시간(초)을 선택합니다.
- **Wait for User Swipe or Touch:** 해제 또는 닫기 옵션이 필요합니다.

### 슬라이드업 위치 {#slide-up-position}

이 설정은 슬라이드업 메시지 유형에만 적용됩니다. 슬라이드업이 **From Bottom of App Screen** 또는 **From Top of App Screen**에서 나타나도록 선택합니다.

### HTML 및 자산 {#html-and-assets}

이 설정은 커스텀 코드 메시지 유형에만 적용됩니다. 사용 가능한 공간에 HTML을 복사하여 붙여넣고 ZIP 파일을 사용하여 자산을 업로드합니다.

### 이메일 수집 입력 입력 안내 {#email-capture-input-placeholder}

이 설정은 이메일 수집 양식 메시지 유형에만 적용됩니다. 이메일 입력 필드의 입력 안내 텍스트로 표시될 커스텀 문구를 입력합니다. 기본값은 "Enter your email address"입니다.

## 5단계: 인앱 메시지 스타일 지정 {#step-5-style-your-in-app-message}

**스타일** 탭에서 메시지의 모든 시각적 측면을 조정할 수 있습니다. 이미지나 배지를 업로드하거나 미리 디자인된 배지 아이콘을 선택합니다. 팔레트에서 선택하거나 16진수, RGB 또는 HSB 코드를 입력하여 헤더 및 본문 텍스트, 버튼, 배경의 색상을 변경합니다.

**스타일** 탭의 콘텐츠는 이전 단계에서 선택한 메시지 옵션에 따라 달라지지만, 다음 옵션 중 하나를 포함할 수 있습니다:

| 서식 | 입력 | 설명 |
|---|---|---|
| [색상 프로필]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#reusable-color-profiles) | 인앱 메시지 템플릿 갤러리에서 적용합니다. | **Apply Template**을 선택하고 갤러리에서 선택합니다. 그런 다음 **Save**를 선택합니다. |
| 텍스트 정렬 | 왼쪽, 가운데 또는 오른쪽. | 최신 Braze SDK 버전에서만 사용할 수 있습니다. |
| 헤더 | 16진수 색상 코드. | 원하는 16진수 색상이 표시됩니다. 색상의 불투명도도 선택할 수 있습니다. |
| 텍스트 | 16진수 색상 코드. | 원하는 16진수 색상이 표시됩니다. 색상의 불투명도도 선택할 수 있습니다. |
| 버튼 | 16진수 색상 코드. | 원하는 16진수 색상이 표시됩니다. 색상의 불투명도도 선택할 수 있습니다. 메시지의 Close Button Background와 각 버튼의 Background, Text 및 Border 색상을 선택할 수 있습니다. |
| 버튼 테두리 | 16진수 색상 코드. | 새로운 기능! 기본 및 보조 버튼을 서로 구분할 수 있습니다. 대비되는 색상으로 버튼 윤곽을 지정하는 것을 권장합니다. |
| 배경색 | 16진수 색상 코드. | 원하는 16진수 색상이 표시됩니다. 색상의 불투명도도 선택할 수 있습니다. 이것은 전체 메시지의 배경이며 텍스트 본문 뒤에 명확하게 표시됩니다. |
| 화면 오버레이 | 16진수 색상 코드. | 원하는 16진수 색상이 표시됩니다. 색상의 불투명도도 선택할 수 있습니다. 최신 Braze SDK 버전에서만 사용할 수 있습니다. 이것은 전체 메시지 주위의 프레임입니다. |
| 셰브론 또는 기타 메시지 닫기 옵션 | 16진수 색상 코드. | 원하는 16진수 색상이 표시됩니다. 색상의 불투명도도 선택할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="5단계: 인앱 메시지 스타일 지정" }

전송하기 전에 항상 메시지를 [미리보기 및 테스트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)하세요.

{% alert important %}
일부 인앱 메시지 유형은 커스텀 HTML(또는 CSS 또는 JavaScript) 및 ZIP 파일을 사용한 자산 업로드 외에는 스타일 지정 옵션이 없습니다. [CSS가 포함된 웹 모달]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#web-modal-css)을 사용하면 커스텀 CSS를 업로드하거나 작성하여 아름답고 완전히 커스텀 스타일의 메시지를 만들 수 있습니다.
{% endalert %}

## 6단계: 추가 설정 구성(선택 사항) {#step-6-configure-additional-settings-optional}

### 키-값 페어 {#key-value-pairs}

[키-값 페어]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)를 추가하여 사용자 기기에 추가 커스텀 필드를 전송할 수 있습니다.

## 7단계: 캠페인 또는 Canvas의 나머지 부분 구축 {#step-7-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

캠페인의 나머지 부분을 구축합니다. 인앱 메시지를 구축하기 위한 도구 활용 방법에 대한 자세한 안내는 다음 섹션을 참조하세요.

### 트리거 선택 {#choose-a-trigger}

메시지를 트리거할 동작과 캠페인 또는 Canvas의 시작 및 종료 시간을 선택합니다.

{% alert important %}
커스텀 이벤트를 기반으로 인앱 메시지를 트리거하려는 경우, 해당 커스텀 이벤트는 SDK를 사용하여 전송해야 합니다.
{% endalert %}

![트리거 동작이 "Start Session"으로 설정된 액션 기반 캠페인.]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

인앱 메시지 전달은 전적으로 다음 동작 트리거를 기반으로 합니다:

- 구매하기
- 앱/웹페이지 열기
- 커스텀 이벤트 수행(SDK를 사용하여 전송된 이벤트에만 작동)
- 특정 푸시 메시지 열기
- 각 사용자의 현지 시간에 맞춰 특정 시간에 전송되도록 캠페인을 자동으로 스케줄합니다.
- 메시지는 매일, 매주(선택적으로 특정 요일) 또는 매월 반복되도록 구성할 수도 있습니다.

시작 날짜와 시간은 반드시 선택해야 하지만, 종료 날짜는 선택 사항입니다. 종료 날짜를 설정하면 지정된 날짜/시간 이후에 해당 인앱 메시지가 기기에 표시되지 않습니다.

[서버 측 이벤트 트리거]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web) 및 [로컬 인앱 메시지 전달]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery#local-in-app-messages)에 대한 개발자 설명서를 참조하세요.

#### 온라인 대 오프라인 트리거 {#online-versus-offline-triggering}

인앱 메시지는 메시지와 트리거를 사용자의 기기로 전송하는 방식으로 작동합니다. 인앱 메시지가 기기에 있으면 트리거 조건이 충족될 때까지 표시를 대기합니다. 인앱 메시지가 이미 사용자의 기기에 캐시되어 있으면 Braze에 연결되지 않은 오프라인 상태(예: 비행기 모드)에서도 인앱 메시지를 트리거할 수 있습니다.

{% alert important %}
인앱 메시지가 중지된 후에도 메시지가 중지되기 전에 세션을 시작하고 이후에 트리거 이벤트를 수행한 일부 사용자에게는 메시지가 계속 표시될 수 있습니다. 이러한 사용자는 캠페인이 중지된 후에도 고유 노출 횟수로 집계됩니다.
{% endalert %}

### 우선순위 선택 {#choose-a-priority}

마지막으로, 인앱 메시지가 트리거될 동작을 선택한 후 우선순위도 설정해야 합니다. 동일한 동작에서 두 개의 메시지가 트리거되면 높은 우선순위의 메시지가 낮은 우선순위의 메시지보다 먼저 사용자의 기기에 표시되도록 스케줄됩니다.

다음 메시지 우선순위 중에서 선택할 수 있습니다:

- 높은 우선순위(다른 메시지보다 먼저 표시)
- 중간 우선순위(기본값)
- 낮은 우선순위(다른 메시지 이후에 표시)

높음, 중간, 낮음 옵션은 트리거된 메시지 우선순위의 버킷이므로 여러 메시지가 동일한 선택된 우선순위를 가질 수 있습니다. 여러 메시지가 동일한 우선순위를 공유하는 경우, 가장 최근에 생성되거나 할당된 메시지가 우선하여 먼저 표시됩니다:

- **기본 우선순위 버킷:** 두 캠페인이 동일한 트리거를 공유하고 기본(중간) 우선순위를 사용하는 경우, 마지막에 생성된 캠페인이 트리거를 받습니다.
- **특정 우선순위 버킷:** 여러 캠페인이 동일한 트리거를 공유하고 특정 우선순위 버킷에 할당된 경우, 해당 버킷에 가장 최근에 할당된 캠페인이 트리거를 받습니다.

이러한 버킷 내에서 우선순위를 설정하려면 **상세 우선순위 지정**을 클릭하고 캠페인을 드래그 앤 드롭하여 올바른 우선순위로 정렬할 수 있습니다.

![인앱 메시지 캠페인 및 Canvas에 대한 우선순위 설정 방법 예시.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

### 타겟 사용자 선택 {#choose-users-to-target}

다음으로, Segments 또는 필터를 선택하여 오디언스를 좁혀 [사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)해야 합니다. 해당 대략적인 Segment 인구의 스냅샷이 자동으로 표시됩니다. 정확한 Segment 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 점을 유의하세요.

{% alert note %}
인앱 메시지 단계에 지연이 있는 경우, Segment 멤버십은 지연 후에 평가됩니다. 사용자가 자격이 있으면 인앱 메시지는 다음 사용 가능한 세션에서 동기화됩니다.
{% endalert %}

#### 캠페인 자격 및 Liquid 재평가 {#re-evaluate-campaign-eligibility-and-liquid}

일부 시나리오에서는 인앱 메시지가 표시되도록 트리거될 때 사용자의 자격을 재평가하고 싶을 수 있습니다. 예를 들어 자주 변경되는 커스텀 속성을 타겟팅하는 캠페인이나 마지막 순간의 프로필 변경을 반영해야 하는 메시지가 있습니다.

![표시 전 캠페인 자격 재평가 체크박스가 선택된 상태.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

**Re-evaluate campaign eligibility before displaying**을 선택하면 메시지를 전송하기 전에 사용자가 여전히 이 메시지에 대한 자격이 있는지 확인하기 위해 Braze에 추가 요청이 이루어집니다. 또한 메시지가 표시되기 전에 모든 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) 변수 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)가 해당 시점에 템플릿화됩니다.

이렇게 하면 만료되거나 아카이브된 캠페인 내의 사용자에게 인앱 메시지가 전송되는 것을 방지할 수 있습니다. 사용자의 자격을 재평가하지 않으면 메시지가 SDK에 있고 사용자가 트리거하기를 기다리고 있기 때문에 캠페인이 만료되거나 아카이브된 후에도 사용자가 인앱 메시지를 받게 됩니다.

{% alert note %}
이 옵션을 활성화하면 추가 자격 및 템플릿화 요청으로 인해 사용자가 인앱 메시지를 트리거하는 시점과 메시지가 표시되는 시점 사이에 약간의 지연(100ms 미만)이 발생합니다.
<br><br>
사용자가 오프라인 상태에서 트리거될 수 있는 메시지나 자격 및 Liquid 재평가가 필요하지 않은 메시지에는 이 옵션을 사용하지 마세요.
{% endalert %}

#### 메시지에서 REST API로 추가된 데이터 사용 {#use-data-added-by-rest-api-in-a-message}

[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)가 동일한 세션에서 추가한 사용자 데이터는 때때로 해당 사용자의 인앱 메시지에서 사용할 수 있습니다. 예를 들어, 사용자가 트리거를 기다리는 인앱 메시지의 오디언스에 있고, 세션을 시작한 후 동일한 세션에서 REST API가 프로필을 업데이트하면 **Re-evaluate campaign eligibility before displaying**이 선택된 경우 해당 새 데이터가 인앱 메시지에 나타날 수 있습니다. Braze는 렌더링할 시간이 될 때까지 인앱 메시지를 템플릿화하지 않습니다.

하나의 트리거가 Braze에 데이터를 전송하고 인앱 메시지를 실행하는 경우, 스케줄된 지연이 있더라도 메시지는 새로 업데이트된 프로필 데이터를 사용할 수 없습니다. 대신 두 개의 별도 트리거를 사용하세요: 하나는 데이터를 전송하고, 다른 하나는 인앱 메시지를 트리거합니다.

### 전환 이벤트 선택 {#choose-conversion-events}

Braze를 사용하면 캠페인을 수신한 후 사용자가 특정 동작인 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 동작을 수행하면 전환이 집계되는 최대 30일의 기간을 허용하는 옵션이 있습니다.

{% endtab %}
{% tab Canvas %}

아직 완료하지 않았다면 Canvas 구성요소의 나머지 섹션을 완료하세요. Canvas의 나머지 부분을 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대한 자세한 내용은 Canvas 설명서의 [Canvas 구축]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-3-build-your-canvas) 단계를 참조하세요.

Canvas 관련 인앱 메시징 옵션에 대한 정보는 [Canvas의 인앱 메시지]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas)를 참조하세요.

{% endtab %}
{% endtabs %}

## 8단계: 검토 및 배포 {#step-8-review-and-deploy}

캠페인 또는 Canvas의 마지막 부분을 완성한 후 세부 사항을 검토하고, [테스트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)한 다음 전송하세요!

다음으로, [인앱 메시지 보고]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting)를 확인하여 메시징 캠페인의 결과에 액세스하는 방법을 알아보세요.

## 알아두어야 할 사항 {#things-to-know}

### 활성 인앱 메시지 캠페인 제한 {#active-in-app-message-campaign-limits}

Braze는 안정성과 속도를 중요하게 생각합니다. Braze에 필요한 데이터만 전송하고 더 이상 브랜드에 가치를 더하지 않는 캠페인은 비활성화하는 것을 권장합니다.

여전히 활성 상태이지만 더 이상 메시지를 전송하지 않거나 더 이상 필요하지 않은 액션 기반 인앱 메시지 캠페인을 처리하면 귀하와 다른 고객을 위한 Braze 서비스의 전반적인 성능이 저하됩니다. 이러한 대량의 유휴 캠페인을 처리하는 데 필요한 추가 시간은 인앱 메시지가 최종 사용자의 기기에 표시되는 데 더 오래 걸리게 하여 최종 사용자의 경험에 영향을 미칩니다.

{% alert important %}
메시지 전달 속도를 최적화하고 시간 초과를 방지하기 위해 워크스페이스당 최대 200개의 활성 액션 기반 인앱 메시지 캠페인을 가질 수 있습니다. 이는 Canvases에는 적용되지 않습니다.
{% endalert %}

200개 카운트에는 아직 종료 시간에 도달하지 않은 활성 인앱 메시지 캠페인과 종료 시간이 없는 캠페인이 포함됩니다. 종료 시간이 지난 활성 인앱 메시지 캠페인은 집계되지 않습니다. 평균적인 Braze 고객은 한 번에 총 26개의 캠페인이 활성 상태이므로 이 제한이 영향을 미칠 가능성은 낮습니다.

### 현지 시간 전달 평가 {#local-time-delivery-evaluation}

인앱 메시지 캠페인이 사용자의 현지 시간대를 사용하여 스케줄된 경우, 캠페인의 시작 및 종료 시간 평가는 기기 자체에서 처리됩니다.

인앱 메시지 캠페인은 일반적으로 앱 세션이 시작되거나 새로고침될 때 사용자의 기기로 푸시됩니다. 그 시점에서:

1. SDK가 사용자가 트리거 기반 인앱 메시지에 대한 자격이 있는지 평가합니다.
2. 기기가 사용자의 트리거 이벤트가 캠페인의 시작 및 종료 시간(사용자의 현지 시간대 기준) 내에 발생했는지 확인합니다.
3. 두 조건이 모두 충족되면 인앱 메시지가 표시 대상이 됩니다.

#### 고려 사항 {#considerations}

- 사용자가 인앱 메시지가 전달된 직후에 이벤트(예: 버튼 탭)를 트리거하면, 모든 자격 기준이 여전히 충족된다는 가정 하에 다음 세션 새로고침까지 메시지가 나타나지 않을 수 있습니다.
- 다른 채널 유형과 마찬가지로, 인앱 메시지 캠페인은 이상적으로 24~48시간 전에 시작해야 합니다. 이 버퍼는 사용자가 자격을 충족하고 메시지가 평가되어 표시될 수 있도록 세션을 시작할 충분한 시간을 제공합니다.