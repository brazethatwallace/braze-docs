---
nav_title: "인앱 메시지"
article_title: "인앱 메시지"
page_order: 5
page_type: landing
alias: /in-app_messages/
description: "Braze의 다양한 레이아웃과 개인화 도구를 사용하여 사용자 경험을 향상시키는 맞춤형 인앱 메시지로 사용자의 참여를 유도하세요."
channel:
  - in-app messages
search_rank: 5
---

# 인앱 메시지 {#in-app-messages}

> 인앱 메시지는 푸시 알림으로 사용자를 방해하지 않으면서 앱이나 웹사이트 내에서 콘텐츠를 전달합니다. 맞춤형 인앱 메시지는 레이아웃, 개인화, 타겟팅 도구를 활용하여 사용자 경험을 향상시키고 오디언스가 제품에서 더 많은 가치를 얻을 수 있도록 도와줍니다. 이 허브에서는 메시지 유형, 드래그 앤 드롭 편집기, 사전 요구 사항, 온보딩 및 프로모션과 같은 일반적인 사용 사례를 다룹니다. 첫 번째 인앱 메시지를 만들기 전에 [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)를 통합한 다음, Campaign에 맞는 표준 또는 커스텀 레이아웃을 선택하세요.

## 사전 요구 사항 {#prerequisites}

인앱 메시지를 보내려면 먼저 앱이나 웹사이트에 [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)를 통합해야 합니다. 추가적인 설정은 필요하지 않습니다.

최소 SDK 버전 및 기능별 요구 사항에 대해서는 다음을 참조하세요:
- [드래그 앤 드롭 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [메시지 유형]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)

## 사용 사례 {#use-cases}

인앱 메시지가 제공하는 풍부한 콘텐츠를 통해 다양한 사용 사례에 이 채널을 활용할 수 있습니다:

| 사용 사례 | 설명 |
| --- | --- |
| 푸시 프라이밍 | 풍부한 인앱 메시지를 사용하여 [푸시 프라이밍]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) Campaign을 실행하여 고객에게 앱 또는 사이트에서 푸시 알림을 수신하는 이점을 보여주고, 푸시 권한을 부여하도록 안내합니다.
| 세일 및 프로모션 | Modal 인앱 메시지를 사용하여 정적 프로모션 코드 또는 혜택이 포함된 시각적으로 매력적인 미디어로 고객을 맞이합니다. 그렇지 않았다면 하지 않았을 구매 또는 전환을 유도합니다. |
| 기능 채택 촉진 | 고객이 앱의 다른 부분을 사용하거나 서비스를 이용하도록 장려합니다. |
| 고도로 개인화된 Campaigns | 고객이 앱이나 사이트에 접속할 때 가장 먼저 보이는 곳에 인앱 메시지를 배치합니다. [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)와 같은 Braze 개인화 기능을 추가하여 사용자가 행동을 취하도록 유도함으로써 아웃리치의 효과를 높입니다.
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 사례" }

고려할 수 있는 기타 사용 사례는 다음과 같습니다:

- 새로운 앱 기능
- 앱 관리
- 리뷰
- 앱 업그레이드 또는 업데이트
- 경품 및 이벤트

## 표준 메시지 유형 {#standard-message-types}

다음 탭에서는 사용자가 슬라이드업, Modal, 전체화면 인앱 메시지 등 표준 인앱 메시지 유형을 열었을 때 어떻게 보이는지 확인할 수 있습니다.

{% tabs %}
{% tab 슬라이드업 %}

슬라이드업 메시지는 일반적으로 앱 화면의 상단 또는 하단에 나타납니다(메시지 작성 시 설정할 수 있습니다). 새로운 이용약관, 쿠키 및 기타 간단한 정보를 사용자에게 알릴 때 유용합니다.

![앱 화면 하단에서 나타나는 슬라이드업 인앱 메시지. 슬라이드업에는 아이콘 이미지와 간단한 메시지가 포함되어 있습니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Modal은 기기 화면 중앙에 화면 오버레이와 함께 표시되어 백그라운드의 앱과 구분됩니다. 사용자에게 세일이나 경품 행사를 적극적으로 알리고 싶을 때 적합합니다.

![앱과 웹사이트 중앙에 대화 상자로 나타나는 Modal 인앱 메시지. Modal에는 이미지, 헤더, 메시지 본문, 두 개의 버튼이 포함되어 있습니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 전체화면 %}

전체화면 메시지는 말 그대로 기기의 전체 화면을 차지합니다! 필수 앱 업데이트와 같이 사용자의 주의를 반드시 끌어야 할 때 유용한 메시지 유형입니다.

![앱 화면 전체를 차지하는 전체화면 인앱 메시지. 전체화면 메시지에는 큰 이미지, 헤더, 메시지 본문, 두 개의 버튼이 포함되어 있습니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

이러한 기본 메시지 템플릿 외에도 커스텀 HTML 인앱 메시지, CSS가 적용된 웹 Modal, 웹 이메일 캡처 양식을 사용하여 메시징을 더욱 커스터마이징할 수 있습니다. 자세한 내용은 [사용자 지정]({{site.baseurl}}/user_guide/channels/in_app_messages/customize)을 참조하세요.

표시 시점의 템플릿 전달이 **중단** 로깅에 어떤 영향을 미치는지에 대해서는 [인앱 메시지 FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)를 참조하세요.

## 다음 단계 {#next-steps}

{% article_tiles %}
- name: 드래그 앤 드롭 편집기로 인앱 메시지 만들기
  link: /docs/user_guide/channels/in_app_messages/drag_and_drop
- name: 기존 편집기로 인앱 메시지 만들기
  link: /docs/user_guide/channels/in_app_messages/traditional
{% endarticle_tiles %}

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}