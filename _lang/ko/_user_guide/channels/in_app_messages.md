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

> 인앱 메시지는 푸시 알림으로 사용자의 일상을 방해하지 않으면서 콘텐츠를 전달할 수 있도록 도와줍니다. 맞춤화된 인앱 메시지는 사용자 경험을 향상시키고, 오디언스가 앱에서 최대한의 가치를 얻을 수 있도록 합니다. 다양한 레이아웃과 커스텀 도구를 선택할 수 있어, 인앱 메시지는 그 어느 때보다 효과적으로 사용자의 참여를 유도합니다.

## 필수 조건 {#prerequisites}

인앱 메시지를 보내려면 먼저 앱이나 웹사이트에 [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)를 통합해야 합니다. 추가 설정은 필요하지 않습니다.

최소 SDK 버전 및 기능별 요구 사항은 다음을 참조하세요:
- [드래그 앤 드롭 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [메시지 유형]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)

## 활용 사례 {#use-cases}

인앱 메시지가 제공하는 풍부한 콘텐츠를 활용하여 다양한 사용 사례에 이 채널을 활용할 수 있습니다:

| 활용 사례 | 설명 |
| --- | --- |
| 푸시 프라이밍 | 풍부한 인앱 메시지를 사용하여 [푸시 프라이밍]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) Campaign을 실행하여 고객에게 앱이나 사이트에서 푸시를 수신하는 이점을 보여주고, 푸시 권한을 부여하도록 프롬프트를 제시합니다.
| 세일 및 프로모션 | 모달 인앱 메시지를 사용하여 정적 프로모션 코드나 혜택이 포함된 시각적으로 매력적인 미디어로 고객을 맞이하세요. 그렇지 않았다면 하지 않았을 구매나 전환을 유도합니다. |
| 기능 채택 장려 | 고객이 앱의 다른 부분을 사용하거나 서비스를 활용하도록 장려합니다. |
| 고도로 개인화된 Campaign | 고객이 앱이나 사이트에 들어올 때 가장 먼저 보는 것으로 인앱 메시지를 배치합니다. [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)와 같은 Braze 개인화 기능을 추가하여 사용자가 행동을 취하도록 유도하고, 아웃리치를 더욱 효과적으로 만드세요.
{: .reset-td-br-1 .reset-td-br-2 aria-label="활용 사례" }

고려할 수 있는 기타 활용 사례는 다음과 같습니다:

- 새로운 앱 기능
- 앱 관리
- 리뷰
- 앱 업그레이드 또는 업데이트
- 경품 및 추첨

## 표준 메시지 유형 {#standard-message-types}

다음 탭은 사용자가 표준 인앱 메시지 유형(슬라이드업, 모달, 전체화면 인앱 메시지)을 열었을 때 어떻게 보이는지 보여줍니다.

{% tabs %}
{% tab 슬라이드업 %}

슬라이드업 메시지는 일반적으로 앱 화면의 상단과 하단에 나타납니다(메시지를 생성할 때 설정할 수 있습니다). 이 메시지는 새로운 이용 약관, 쿠키 및 기타 정보 스니펫에 대해 사용자에게 알리는 데 적합합니다.

![앱 화면 하단에서 나타나는 슬라이드업 인앱 메시지. 슬라이드업에는 아이콘 이미지와 간단한 메시지가 포함되어 있습니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 모달 %}

모달은 기기 화면 중앙에 화면 오버레이와 함께 나타나 배경의 앱과 구분되도록 합니다. 사용자에게 세일이나 경품을 활용하도록 권유하는 데 적합합니다.

![앱과 웹사이트 중앙에 대화 상자로 나타나는 모달 인앱 메시지. 모달에는 이미지, 헤더, 메시지 본문, 두 개의 버튼이 포함되어 있습니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab 전체화면 %}

전체화면 메시지는 말 그대로 기기의 전체 화면을 차지합니다! 이 메시지 유형은 필수 앱 업데이트와 같이 사용자의 주의가 정말 필요할 때 적합합니다.

![앱 화면을 차지하는 전체화면 인앱 메시지. 전체화면 메시지에는 큰 이미지, 헤더, 메시지 본문, 두 개의 버튼이 포함되어 있습니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

이러한 기본 메시지 템플릿 외에도 커스텀 HTML 인앱 메시지, CSS가 포함된 웹 모달 또는 웹 이메일 캡처 양식을 사용하여 메시징을 추가로 커스텀할 수 있습니다. 자세한 내용은 [사용자 지정]({{site.baseurl}}/user_guide/channels/in_app_messages/customize)을 참조하세요.

표시 시점의 템플릿 전달이 **중단** 로깅에 미치는 영향에 대해서는 [인앱 메시지 FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)를 참조하세요.

## 다음 단계 {#next-steps}

- [드래그 앤 드롭 편집기로 인앱 메시지 만들기]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [기존 편집기로 인앱 메시지 만들기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}