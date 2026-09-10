---
nav_title: WhatsApp
article_title: WhatsApp
page_order: 10
page_type: landing
channel:
  - WhatsApp
search_rank: 3
description: "Braze를 통해 고객지원, 알림, 프로모션 Campaign을 위한 개인화된 WhatsApp 메시지로 고객에게 도달하세요."
alias: /whatsapp/
---

# WhatsApp

> WhatsApp은 전 세계적으로 사용되는 P2P 메시징 플랫폼으로, 대화 기반 비즈니스 메시징을 제공합니다. Braze의 WhatsApp 채널을 사용하면 사용자가 매일 사용하는 스레드 대화에서 고객지원 메시지, 알림, 프로모션 Campaign을 보낼 수 있습니다. 이 허브에서는 WhatsApp 설정, 메시지 유형, 템플릿, 구독 관리, 리포팅에 대해 다룹니다. [WhatsApp 설정]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)부터 시작하여 Meta Business 및 WhatsApp Business 계정을 연결한 후 첫 번째 템플릿 기반 메시지를 생성하세요. 신규 사용자에게 프로모션 메시지를 보내기 전에 [옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)을 확인하세요.

## 전제 조건 {#prerequisites}

WhatsApp 사용 가능 여부는 Braze 패키지에 따라 다릅니다. 시작하려면 계정 매니저 또는 고객 성공 매니저에게 문의하세요.

시작하기 전에 다음 사항을 준비하세요:

- Meta Business 매니저 계정 및 WhatsApp Business 계정
- [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) 요구 사항을 충족하는 WhatsApp 전화번호

전체 안내는 [WhatsApp 설정]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)을 참조하세요.

## 사용 사례 {#use-cases}

| 사용 사례 | 설명 |
| --- | --- |
| 고객 지원 | 실시간 양방향 대화를 통해 문의 사항을 처리하고, 문제를 해결하며, 개인화된 지원을 제공합니다. |
| 주문 알림 | 주문 확인, 배송 업데이트 및 배달 알림을 WhatsApp을 통해 고객에게 직접 전송합니다. |
| 예약 리마인더 | 시의적절한 예약 리마인더로 노쇼를 줄이고, 고객이 확인하거나 일정을 변경할 수 있도록 합니다. |
| 프로모션 Campaign | 리치 미디어 메시지를 통해 타겟팅된 프로모션, 제품 출시 및 개인화된 오퍼로 고객에게 도달합니다. |
| 양방향 대화 | 고객이 응답하고, 질문하고, 피드백을 제공할 수 있는 인터랙티브 메시징으로 더 깊은 관계를 구축합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 사례" }

## 자주 묻는 질문 {#frequently-asked-questions}

### WhatsApp을 Braze에 어떻게 연결하나요? {#how-do-i-connect-whatsapp-to-braze}

Meta Business 매니저 계정과 WhatsApp Business 계정을 생성한 다음, [WhatsApp 설정]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)의 단계를 완료합니다.

### WhatsApp에서 어떤 메시지 유형을 보낼 수 있나요? {#what-message-types-can-i-send-on-whatsapp}

아웃바운드 메시지에는 승인된 템플릿을 사용하고, 양방향 대화에는 지원되는 세션 메시지를 사용합니다. 지원되는 메시지 유형에 대해서는 [WhatsApp 메시지 만들기]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)를 참고하세요.

### 사용자가 WhatsApp 메시지를 수신하려면 옵트인해야 하나요? {#do-users-need-to-opt-in-to-whatsapp-messages}

네. 프로모션 또는 반복적인 WhatsApp 메시지를 보내기 전에 사용자의 옵트인을 받아야 합니다. 구독 처리에 대한 자세한 내용은 [옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)을 참고하세요.

## 다음 단계 {#next-steps}

{% article_tiles %}
- name: WhatsApp 설정
  link: /docs/user_guide/channels/whatsapp/whatsapp_setup
- name: WhatsApp 메시지 만들기
  link: /docs/user_guide/channels/whatsapp/create_a_whatsapp_message
{% endarticle_tiles %}