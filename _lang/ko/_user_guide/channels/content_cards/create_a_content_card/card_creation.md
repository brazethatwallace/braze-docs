---
nav_title: 카드 생성
article_title: 카드 생성
alias: /card_creation/
description: "이 문서에서는 캠페인 시작 또는 캔버스 단계 진입 시 콘텐츠 카드를 생성하는 것과 첫 번째 노출 시 생성하는 것의 차이점을 설명합니다."
page_order: 0
tool: Campaigns
channel:
  - content cards
---

# 카드 생성

> 카드가 생성되는 시점을 지정하여 Braze가 새 콘텐츠 카드 캠페인 및 캔버스 단계에 대한 오디언스 자격 및 개인화를 평가하는 시점을 선택할 수 있습니다.

## 필수 조건

이 기능을 활용하려면 다음 최소 SDK 버전으로 업그레이드해야 합니다:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

SDK를 업그레이드한 후 모바일 사용자가 앱을 업데이트해야 합니다. 캠페인 또는 캔버스 오디언스를 필터링하여 [이 최소 앱 버전의 사용자만 타겟팅]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions)할 수 있습니다.

## 개요

{% tabs %}
{% tab 캠페인 %}

예약 전달로 새 [콘텐츠 카드 캠페인]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/)을 생성할 때 **전달** 단계에서 Braze가 카드를 생성하는 시점을 선택할 수 있습니다.

![예약된 콘텐츠 카드의 전달을 편집할 때 콘텐츠 카드 제어 섹션.]({% image_buster /assets/img_archive/card_creation.png %})

다음 옵션을 사용할 수 있습니다:

- **캠페인 시작 시:** 콘텐츠 카드의 이전 기본 동작입니다. Braze는 캠페인이 시작될 때 오디언스 자격과 개인화를 계산한 다음 카드를 생성하고 사용자가 앱을 열 때까지 저장합니다.
- **첫 번째 노출 시(권장):** 사용자가 다음에 앱을 열면(새 [세션](https://www.braze.com/resources/articles/whats-an-app-session-anyway) 시작), Braze는 사용자가 자격이 있는 콘텐츠 카드를 결정하고, Liquid 또는 연결된 콘텐츠와 같은 개인화를 템플릿으로 처리한 다음 카드를 생성합니다. 이 옵션은 일반적으로 더 나은 성과를 제공합니다.

선택한 옵션에 관계없이 콘텐츠 카드 만료일 카운트다운은 캠페인이 시작될 때 시작됩니다.

{% endtab %}
{% tab 캔버스 %}

콘텐츠 카드 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)의 **메시징 채널** 탭에서 Braze가 카드를 생성하는 시점을 선택할 수 있습니다.

![예약된 콘텐츠 카드의 전달을 편집할 때 콘텐츠 카드 제어 섹션.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

다음 옵션을 사용할 수 있습니다:

- **단계 진입 시:** 콘텐츠 카드의 이전 기본 동작입니다. Braze는 사용자가 캔버스 단계에 진입할 때 오디언스 자격을 계산한 다음 카드를 생성하고 사용자가 앱을 열 때까지 저장합니다.
- **첫 번째 노출 시(권장):** Braze는 사용자가 캔버스 단계에 진입할 때 오디언스 자격을 계산합니다. 사용자가 다음에 앱을 열면(새 [세션](https://www.braze.com/resources/articles/whats-an-app-session-anyway) 시작), Braze는 Liquid 또는 연결된 콘텐츠와 같은 개인화를 템플릿으로 처리한 다음 카드를 생성합니다. 이 옵션은 카드 전달에서 더 나은 성과와 더 최신의 개인화를 제공합니다.

선택한 옵션에 관계없이 콘텐츠 카드 만료일 카운트다운은 사용자가 캔버스 단계에 진입할 때 시작됩니다.

{% alert tip %}
익명 사용자가 첫 번째 세션에서 콘텐츠 카드를 볼 수 있도록 하려면 캔버스 대신 캠페인을 사용하세요. 익명 사용자가 캔버스에 진입할 때 세션이 이미 시작되었기 때문에 새 세션을 시작할 때까지 콘텐츠 카드를 받지 못합니다.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
두 옵션 모두 카드가 생성된 후에는 Braze가 오디언스 자격이나 개인화를 다시 계산하지 않습니다.
{% endalert %}

### 시작 또는 진입 시 카드 생성과 첫 번째 노출 시 카드 생성의 차이점 {#differences}

이 섹션에서는 캠페인 시작 또는 단계 진입 시 카드 생성과 첫 번째 노출 시 카드 생성의 주요 차이점을 설명합니다.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">캠페인 시작 시 / 캔버스 단계 진입 시</th>
    <th class="tg-0pky">첫 번째 노출 시</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">사용 시기</td>
    <td class="tg-0pky">특정 시점(시작 시점)에 콘텐츠의 스냅샷이 필요한 경우.</td>
    <td class="tg-0pky"><ul><li>시작 후 세그먼트에 진입할 수 있는 신규 또는 익명 사용자에게 카드를 표시해야 하는 경우(<a href="#campaign_note">캠페인에만 해당*</a>).</li><li>개인화를 사용하고 카드에 최신 콘텐츠를 표시하려는 경우.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">오디언스</td>
    <td class="tg-0pky">Braze는 캠페인이 발송될 때 오디언스 멤버십을 평가합니다.<br><br>캠페인 발송 후 카드를 보려는 신규 또는 익명 사용자는 자격 평가를 받지 않습니다. 반복 캠페인의 경우 다음 반복 간격에 평가됩니다.</td>
    <td class="tg-0pky">Braze는 사용자가 다음에 앱을 열 때(세션 시작, <a href="#campaign_note">캠페인에만 해당*</a>) 멤버십을 평가합니다.<br><br>이 설정은 신규 또는 익명 사용자가 카드를 보려고 할 때 항상 자격 평가를 받으므로 더 넓은 오디언스 도달 범위를 갖습니다.<br><br>또한 첫 번째 노출 시로 설정하면 사용량 제한(카드를 받을 사용자 수 제한)이 적용되지 않습니다.</td>
  </tr>
  <tr>
    <td class="leftHeader">개인화</td>
    <td class="tg-0pky">Braze는 캠페인이 시작되거나 사용자가 캔버스 단계에 진입할 때 Liquid, 연결된 콘텐츠, 콘텐츠 블록을 평가합니다. 반복 캠페인의 경우 다음 반복 간격에 평가됩니다.</td>
    <td class="tg-0pky">Braze는 첫 번째 노출 시 또는 다음 반복 간격 이후에 Liquid, 연결된 콘텐츠, 콘텐츠 블록을 평가합니다.</td>
  </tr>
  <tr>
    <td class="leftHeader">분석</td>
  <td class="tg-0pky"><em>발송된 메시지</em>는 Braze가 생성하여 사용 가능하게 만든 카드 수를 나타냅니다. 사용자가 카드를 조회했는지 여부는 포함되지 않습니다.</td>
  <td class="tg-0pky"><em>발송된 메시지</em>는 세션 시작 후 Braze가 사용자에게 보내는 카드 수를 나타냅니다. 캔버스에서 사용자가 세션을 시작하지 않고 단계에 진입하면 Braze는 카드를 보내지 않으므로 이 측정기준이 단계에 진입하는 사용자 수와 일치하지 않을 수 있습니다.<br><br>도달 가능 사용자와 노출 횟수는 변하지 않지만, 첫 번째 노출 시 카드를 생성하면 캠페인 시작 또는 캔버스 단계 진입 시보다 발송량(<em>발송된 메시지</em>)이 낮아질 수 있습니다.</td>
  </tr>
  <tr>
    <td class="leftHeader">처리 시간</td>
  <td class="tg-0pky">Braze는 시작 시점에 세그먼트의 모든 자격 있는 사용자에 대해 카드를 생성합니다. 대규모 오디언스의 경우 <b>첫 번째 노출 시</b>를 선택하면 시작 후 카드를 더 빠르게 사용할 수 있습니다.</td>
  <td class="tg-0pky">Braze는 사용자가 처음 카드를 보려고 할 때 카드를 생성하므로 첫 번째 노출 시 표시되기까지 1~2초가 걸릴 수 있습니다.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* 이 시나리오는 캠페인에만 적용됩니다. 캔버스 오디언스는 단계 수준이 아닌 캔버스 진입 시 평가되기 때문입니다.</sup></p>

## 고려 사항

### 캔버스 컨텍스트 등록정보 사용

콘텐츠 카드를 [캔버스 컨텍스트 등록정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)로 개인화할 때는 `${...}` 구문을 사용하세요(예: {%raw%}`{{context.${property_name}}}`{%endraw%}). 이 구문 없이 점 표기법을 사용하면(예: {%raw%}`{{context.property_name}}`{%endraw%}) 푸시나 이메일 같은 다른 채널에서는 작동하더라도 콘텐츠 카드에서는 올바르게 처리되지 않을 수 있습니다.

### 시작 후 카드 생성 방식 변경

Braze는 캠페인이 시작된 후에는 카드 생성 방식을 변경하지 않는 것을 권장합니다. 두 가지 카드 생성 유형 간에 발송된 메시지 계산 방식이 다르기 때문에, 캠페인 시작 후 카드 생성 방식을 변경하면 발송량의 정확성에 영향을 줄 수 있습니다.

### 잠재적 처리 시간

대규모 오디언스의 경우 첫 번째 노출 시 카드를 생성하는 옵션을 선택하면 시작 후 카드를 빠르게 사용할 수 있습니다. 세션 시작 시 트리거되는 캠페인도 성과 향상을 위해 첫 번째 노출 시 생성으로 전환하면(예약 전달을 통해 사용 가능) 도움이 될 수 있습니다.

첫 번째 노출 시 카드를 생성하면 카드 처리에 1~2초가 걸릴 수 있습니다. 이 처리 시간은 카드 크기와 메시지 템플릿 옵션의 복잡성 등 다양한 요인에 따라 달라집니다. 예를 들어, 연결된 콘텐츠를 사용하는 카드의 처리 시간은 최소한 연결된 콘텐츠 응답 시간만큼 걸립니다.

### 이전 SDK 버전

사용자의 앱이 이전 SDK 버전을 실행하는 경우에도 발송한 콘텐츠 카드를 받을 수 있습니다. 다만 카드가 표시되기까지 시간이 더 걸리며 다음 콘텐츠 카드 동기화까지 표시되지 않을 수 있습니다.