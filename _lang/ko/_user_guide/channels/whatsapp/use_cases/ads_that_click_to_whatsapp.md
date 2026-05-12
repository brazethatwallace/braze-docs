---
nav_title: "WhatsApp으로 연결되는 광고"
article_title: "WhatsApp으로 연결되는 광고"
page_order: 1
description: "이 참조 문서에서는 WhatsApp으로 연결되는 광고를 설정하고 사용하는 방법에 대한 단계별 가이드를 제공합니다."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# WhatsApp으로 연결되는 광고 {#ads-that-click-to-whatsapp}

> 이 페이지에서는 WhatsApp으로 연결되는 광고를 설정하고 사용하는 방법에 대한 단계별 가이드를 제공하여, 여러분과 팀이 WhatsApp 프로그램을 한 단계 끌어올릴 수 있도록 도와줍니다.

WhatsApp으로 연결되는 광고는 Facebook, Instagram 또는 기타 플랫폼의 Meta 광고를 통해 신규 및 기존 고객을 유입시키는 효율적인 방법입니다. 이러한 광고를 사용하여 제품과 서비스를 홍보하는 동시에 사용자에게 WhatsApp 채널의 존재를 알릴 수 있습니다.

![Calorie Rocket의 무료 배달을 홍보하는 Facebook 광고와, 사용자가 광고 버튼을 선택했을 때 발생하는 WhatsApp 대화 화면.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## WhatsApp으로 연결되는 광고 설정하기 {#setting-up-ads-that-click-to-whatsapp}

1. Meta 광고 관리자에서 [WhatsApp으로 연결되는 광고 만들기](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp) 단계별 가이드를 따라 Facebook, Instagram 또는 기타 플랫폼에 광고를 생성합니다. 자동 응답은 설정하지 **마세요**. 대신 Braze에서 응답을 설정합니다.

![참여 광고를 만들기 위한 작성기가 있는 광고 관리자 화면.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

사전 입력 메시지를 설정할 때(사용자가 WhatsApp 비즈니스 계정으로 보내는 메시지), 특정 광고에 대한 응답을 트리거하는 데 사용할 특정 단어나 문구를 포함하세요. 이 예시에서는 음식 배달 앱이 광고에서 홍보하는 내용이므로 "free delivery"를 사용하고 있습니다.

![사전 입력 메시지가 "I want free delivery"로 설정된 광고 관리자 템플릿 작성기.]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
광고 설명에 "지금 WhatsApp에서 채팅하세요"와 같은 문구를 사용하여 광고를 클릭하면 브랜드와의 대화가 시작된다는 것을 명확히 알려주세요.
{% endalert %}

{: start="2"}
2. Braze에서 액션 기반 Canvas를 설정합니다. 액션 기반 옵션은 **Send a WhatsApp inbound message**이며, 메시지 본문은 "YOUR_TRIGGER_WORD"입니다. 이 예시에서는 음식 배달 앱이 "free delivery"를 사용하고 있습니다.

![트리거 이벤트가 "Send a WhatsApp inbound message"이고 메시지 본문이 "free delivery"의 정규식과 일치하는 액션 기반 Braze Canvas의 진입 스케줄.]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3. 고객이 Canvas에 진입한 직후(예: 지연 없이) 즉시 전송되는 응답 메시지를 Canvas에 설정합니다. 광고를 클릭하는 것이 기술적으로 옵트인에 해당하지만, 응답 메시지에서 사용자에게 WhatsApp을 통해 향후 마케팅 메시지를 수신할 의향이 있는지 확인하는 것을 권장합니다.

{% alert tip %}
사용자가 옵트인 여부를 빠르게 표시할 수 있도록 빠른 답장(예: "예" 또는 "아니요")이 포함된 응답 메시지를 설정하세요.
{% endalert %}

광고에서 약속한 할인 코드, 혜택 또는 기타 정보를 제공하는 것도 잊지 마세요!

![버튼 답장이 "Yes"와 "No Thanks"인 WhatsApp 메시지 작성기.]({% image_buster /assets/img/whatsapp/quick_replies.png %})

![트리거 이벤트가 "Sent inbound WhatsApp to subscription group"이고 트리거 단어가 "YES"인 "Opting in" 그룹이 있는 캔버스 단계.]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4. 다음 업데이트 방법 중 하나를 사용하여 고객 프로필의 구독 상태를 업데이트하여 사용자를 옵트인합니다:
    - REST API를 통해 구독 상태를 업데이트하는 Braze-to-Braze 웹훅을 생성합니다.
    - 고급 JSON 편집기를 사용하여 [WhatsApp Canvas에 대한 사용자의 구독 상태 업데이트]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/#whatsapp-opt-in-and-opt-out-process) 템플릿으로 고객 프로필을 업데이트합니다.

![고급 JSON 편집기를 사용하여 고객 프로필을 업데이트하는 사용자 업데이트 캔버스 단계.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![옵트인, 옵트아웃, 다른 모든 사용자의 세 가지 행동 경로를 포함하여 WhatsApp으로 연결되는 광고를 전송하는 워크플로를 보여주는 Canvas.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## 고려 사항 {#considerations}

다음 조건이 충족되면 WhatsApp으로 연결되는 광고에서 시작된 대화는 무료입니다:

- 사용자가 WhatsApp으로 연결되는 광고와 같은 [무료 진입점](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations)을 통해 메시지를 보내면, 24시간 [고객 서비스 기간](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows)이 열리며, 이 기간 동안 해당 사용자에게 모든 유형의 메시지를 보낼 수 있습니다.
- 고객 서비스 기간 내(24시간 이내)에 응답하면, 72시간 동안 무료 진입점이 열리며, 72시간 기간 내의 모든 메시지는 무료입니다.
- 응답 메시지는 무료입니다.