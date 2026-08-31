---
nav_title: LINE 클릭 추적
article_title: LINE 클릭 추적
page_order: 2
description: "이 페이지에서는 LINE 메시지에서 클릭 추적을 활성화하는 방법, 단축 링크를 테스트하는 방법, 추적 링크에 커스텀 도메인을 사용하는 방법 등을 다룹니다."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# LINE 클릭 추적 {#line-click-tracking}

> 이 페이지에서는 LINE 메시지에서 클릭 추적을 활성화하는 방법, 단축 링크를 테스트하는 방법, 추적 링크에 커스텀 도메인을 사용하는 방법 등을 다룹니다.


LINE 클릭 추적이 활성화되면 Braze가 자동으로 URL을 단축하고, 추적 메커니즘을 추가하며, 실시간으로 클릭을 기록합니다. LINE은 집계된 클릭 데이터를 제공하지만, Braze는 시의적절하고 실행 가능한 세분화된 사용자 정보를 제공합니다. 이 데이터를 활용하면 클릭 동작을 기반으로 사용자를 세분화하거나 특정 클릭에 대한 응답으로 메시지를 트리거하는 등 보다 타겟팅된 세분화 및 리타겟팅 전략을 수립할 수 있습니다.

LINE 클릭 추적은 텍스트, 리치, 카드 기반 메시지에 사용할 수 있습니다. 버튼 및 URL을 클릭 동작으로 설정한 이미지 맵 영역 내의 링크를 지원합니다. Liquid 및 커스텀 도메인을 사용하여 URL을 개인화할 수도 있습니다.

## 작동 방식 {#how-it-works}

메시지를 작성하는 동안 **설정** 탭에서 LINE 클릭 추적 기술 설정을 관리할 수 있습니다. 이 기능을 켜면 URL이 기본 Braze 도메인(`https://brz.ai`) 또는 구독 그룹에 지정된 커스텀 도메인을 사용하여 단축되고, 사용자에 맞게 개인화됩니다.

`http://` 또는 `https://`로 시작하는 모든 URL이 단축됩니다. 하나의 메시지에 최대 25개의 URL을 포함할 수 있습니다. Liquid 개인화(사용자 수준 추적 또는 UTM 매개변수 등)가 포함된 단축 URL은 2개월 동안 유효합니다.

## 클릭 추적 설정 {#setting-up-click-tracking}

### 텍스트 메시지 {#text-messages}

텍스트 메시지의 클릭 추적을 설정하려면:

1. **Text** 메시지를 작성기로 드래그하고 텍스트 필드에 URL을 추가합니다.

![단축 전의 긴 URL이 포함된 텍스트 메시지가 있는 LINE 메시지 작성기.]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2. **Settings** 탭으로 이동하여 **Click Tracking**이 켜져 있는지 확인합니다. 클릭 추적은 모든 새 메시지에 대해 기본적으로 켜져 있습니다.

{% alert note %}
**Settings** 또는 **Preview & Test** 탭에서 단축된 링크의 미리보기를 확인할 수 있습니다. 메시지를 작성하는 동안에는 작성기에서 전체 링크가 표시됩니다.
{% endalert %}

![LINE 메시지 작성기의 "Settings" 탭에서 "Click Tracking"이 켜져 있고 단축된 URL(https://olaf.brz.ai/p/9rcfdqdD)이 포함된 미리보기 텍스트 메시지가 표시된 화면.]({% image_buster /assets/img/line/click_tracking_settings.png %})

### 리치 메시지 {#rich-messages}

리치 메시지의 클릭 추적을 설정하려면:

1. **Rich message**를 작성기로 드래그하고 템플릿을 선택합니다.
2. 해당 탭 가능한 영역에 대해 **On-click behavior**를 **URI**로 선택합니다.
3. **Open URL** 필드에 URL을 입력합니다.

![각각 URL이 있는 두 개의 탭 가능한 영역이 포함된 리치 메시지가 있는 LINE 메시지 작성기.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4. **Settings** 탭으로 이동하여 **Click Tracking**이 켜져 있는지 확인합니다. 클릭 추적은 모든 새 메시지에 대해 기본적으로 켜져 있습니다.

### 카드 기반 메시지 {#card-based-messages}

카드 기반 메시지의 클릭 추적을 설정하려면:

1. **Card-based message**를 작성기로 드래그합니다.
2. 해당 카드 또는 버튼 영역에 대해 **On-click behavior**를 **URI**로 선택합니다.

![각각 URL이 있는 두 개의 버튼이 포함된 카드 기반 메시지가 있는 LINE 메시지 작성기.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3. **Settings** 탭으로 이동하여 **Click Tracking**이 켜져 있는지 확인합니다. 클릭 추적은 모든 새 메시지에 대해 기본적으로 켜져 있습니다.

{% alert note %}
**Title** 또는 **Description** 필드의 URL은 LINE 내에서 클릭할 수 없는 필드이므로 단축되지 않습니다.
{% endalert %}

## 커스텀 도메인 {#custom-domains}

LINE 클릭 추적을 사용하면 자체 도메인을 사용하여 단축 URL의 룩앤필을 개인화할 수 있으며, 일관된 브랜드 이미지를 전달하는 데 도움이 됩니다. 자세한 내용은 [커스텀 도메인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains)을 참조하세요.

## URL에서의 Liquid 개인화 {#liquid-personalization-in-urls}

Braze 작성기 내에서 URL을 동적으로 구성할 수 있으므로, URL에 동적 UTM 파라미터를 추가하거나 사용자에게 고유한 링크를 보낼 수 있습니다(예: 사용자를 유기한 장바구니로 안내하거나 재입고된 특정 제품으로 연결).
지원되는 모든 Liquid 개인화 태그를 사용하여 URL을 동적으로 생성할 수 있습니다.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

다음 예시와 같이 커스텀 정의된 Liquid 변수를 단축할 수도 있습니다:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Liquid 변수로 렌더링된 URL 단축 {#shorten-urls-rendered-by-liquid-variables}

Braze는 API 트리거 속성에 포함된 URL을 포함하여 Liquid로 렌더링된 URL을 단축합니다. 예를 들어, {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}가 유효한 URL을 나타내는 경우, LINE 메시지를 보내기 전에 해당 URL을 단축하고 추적합니다.

## 테스트 {#testing}

캠페인이나 Canvas를 시작하기 전에, 먼저 메시지를 미리 보고 테스트하는 것이 좋습니다. 이를 위해 **테스트** 탭으로 이동하여 콘텐츠 테스트 그룹이나 개별 사용자에게 LINE 메시지를 미리 보고 전송하세요.

이 미리보기는 관련 개인화 및 단축 URL로 업데이트됩니다.

{% alert important %}
활성 Canvas 내에서 초안이 생성된 경우 단축 URL이 생성되지 않습니다. 실제 단축 URL은 Canvas 초안이 활성화될 때 생성됩니다.
{% endalert %}

## 리포팅 {#reporting}

LINE 성능 테이블에는 배리언트별 클릭 이벤트 수와 관련 클릭률을 보여주는 **총 클릭 수** 열이 포함되어 있습니다. LINE 측정기준에 대한 자세한 내용은 [LINE 메시지 성능]({{site.baseurl}}/user_guide/channels/line/reporting)을 참조하세요.

![LINE Canvas 단계의 성능.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

클릭 데이터는 분석 대시보드에 자동으로 보고됩니다.

![LINE 성능 분석 대시보드.]({% image_buster /assets/img/line/line_performance.png %})

## 사용자 리타겟팅 {#retargeting-users}

다음 세분화 필터와 트리거를 사용하여 LINE 메시지에서 URL을 클릭한 사용자를 리타겟할 수 있습니다:

- 실행 기반 트리거
    - Campaign과 상호작용
    - 단계와 상호작용

![LINE 실행 기반 전달 트리거.]({% image_buster /assets/img/line/line_action_based.png %})

- 세분화 필터
    - Campaign 클릭/열람
    - 태그가 있는 Campaign 또는 Canvas 클릭/열람
    - 단계 클릭/열람

![세 가지 세분화 필터를 모두 표시하는 필터 그룹: "Campaign 클릭/열람", "태그가 있는 Campaign 또는 Canvas 클릭/열람", "단계 클릭/열람".]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## 자주 묻는 질문 {#frequently-asked-questions}

### 테스트 발송 시 받는 링크가 실제 URL인가요? {#are-the-links-i-receive-when-test-sending-real-urls}

네, 테스트 발송 시 실제 URL이 생성됩니다. 다만, 실제로 시작된 Campaign에서 발송되는 정확한 URL은 테스트 발송에서 보내진 것과 다를 수 있습니다.

### URL이 단축되기 전에 UTM 파라미터를 추가할 수 있나요? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

네, 정적 및 동적 파라미터를 모두 추가할 수 있습니다.

### 단축 URL은 얼마나 오래 유효한가요? {#how-long-do-shortened-urls-remain-valid}

개인화된 URL은 URL 등록 시점으로부터 2개월 동안 유효합니다.

### URL을 단축하려면 Braze SDK를 설치해야 하나요? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

아니요, 클릭 추적은 SDK 통합 없이도 작동합니다.

### 어떤 개별 사용자가 URL을 클릭했는지 알 수 있나요? {#do-i-know-which-individual-users-are-clicking-on-a-url}

네. 클릭 추적이 활성화되면 [LINE 리타겟팅 필터](#retargeting-users)를 사용하여 URL을 클릭한 사용자를 리타겟할 수 있습니다.

### 클릭 추적은 딥링크 또는 유니버설 링크에서도 작동하나요? {#does-click-tracking-work-with-deep-links-or-universal-links}

클릭 추적은 딥링크에서는 작동하지 않습니다. Branch나 Appsflyer와 같은 제공업체의 유니버설 링크를 단축할 수는 있지만, 이 과정에서 발생할 수 있는 문제(기여도 추적이 중단되거나 리디렉션에 실패하는 경우 등)에 대해 Braze는 문제 해결을 지원하지 못합니다.

### LINE 앱의 미리보기가 클릭으로 집계되나요? {#do-previews-on-the-line-app-count-as-clicks}

아니요, LINE 메시지의 클릭률에 포함되지 않습니다.