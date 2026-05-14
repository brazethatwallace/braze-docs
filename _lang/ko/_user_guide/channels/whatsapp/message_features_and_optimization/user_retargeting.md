---
nav_title: 사용자 리타겟팅
article_title: 사용자 리타겟팅
page_order: 5
description: "이 참조 문서에서는 사용자가 WhatsApp 상호작용을 통해 메시지를 리타겟팅하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# 사용자 리타겟팅 {#user-retargeting}

> Braze는 사용자의 구독 상태를 변경하는 것 외에도 고객 프로필에 상호작용을 기록하여 메시지 필터링 및 트리거에 활용합니다.<br><br>이러한 필터와 트리거를 사용하면 WhatsApp 메시지를 수신했거나 특정 WhatsApp Campaign 또는 캔버스 단계에서 WhatsApp 메시지를 수신한 사용자를 필터링할 수 있습니다.

## 리타겟팅 옵션 {#retargeting-options}

{% alert note %}
사용자 리타겟팅으로 오디언스를 구축할 때, 사용자의 선호도에 따라 특정 사용자를 포함하거나 제외하고, CCPA의 "판매 또는 공유 거부" 권리와 같은 개인정보 보호법을 준수하기 위해 관련 필터를 구현해야 할 수 있습니다. 마케터는 Canvas 및/또는 Campaign 진입 기준 내에서 사용자 자격에 대한 관련 필터를 구현해야 합니다.
{% endalert %}

### WhatsApp으로 사용자 필터링 {#filter-users-by-whatsapp}

사용자는 마지막으로 WhatsApp을 수신한 시점 또는 특정 WhatsApp Campaign에서 WhatsApp을 수신했는지 여부로 필터링할 수 있습니다. 필터는 캠페인 빌더의 타겟 사용자 단계에서 설정할 수 있습니다.

#### 마지막 WhatsApp 수신으로 필터링 {#filter-by-last-received-whatsapp}

![2025년 4월 22일에 WhatsApp 메시지를 마지막으로 수신한 필터.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

#### WhatsApp Campaign에서 수신한 메시지로 필터링 {#filter-by-received-messages-from-whatsapp-campaign}

특정 WhatsApp Campaign에서 메시지를 수신한 사용자를 필터링합니다. 이 필터를 사용하면 WhatsApp Campaign에서 메시지를 수신하지 않은 사용자를 필터링하는 옵션도 있습니다.

{% alert note %}
WhatsApp 메시지가 전달, 열람 또는 클릭되면, Braze는 상호작용을 기록한 프로필과 동일한 전화번호를 공유하는 모든 프로필의 데이터를 업데이트합니다. 따라서 메시지를 수신, 열람 또는 클릭한 사람과 해당 번호를 공유하는 사용자는 직접 발송되지 않았더라도 "수신" 필터에 일치할 수 있습니다.
{% endalert %}

![WhatsApp Campaign 수신 필터.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### 참여로 필터링 {#filter-by-engagement}

WhatsApp Campaign 또는 캔버스 단계를 읽었거나 읽지 않은 사용자를 리타겟팅합니다.

#### 특정 WhatsApp Campaign을 열람/읽은 사용자 리타겟팅 {#retarget-users-who-have-openedread-a-specific-whatsapp-campaign}

1. **Clicked/Opened Campaign** 필터를 사용하여 Segment를 생성합니다.
2. **read WhatsApp message**를 선택합니다.
3. 원하는 캠페인을 선택합니다.

![WhatsApp 메시지를 읽은 필터.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

#### 특정 캔버스 단계를 열람/읽은 사용자 리타겟팅 {#retarget-users-who-have-openedread-a-specific-canvas-step}

1. **Clicked/Opened Step** 필터를 사용하여 Segment를 생성합니다.
2. **read WhatsApp message**를 선택합니다.
3. 원하는 Canvas 및 캔버스 단계를 선택합니다.

![WhatsApp 단계를 읽은 필터.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

#### Campaign 또는 Canvas 기여도로 필터링 {#filter-by-campaign-or-canvas-attribution}

특정 WhatsApp Campaign 또는 Canvas 구성요소 또는 태그를 열람/읽은 사용자를 필터링합니다.

![특정 WhatsApp 메시지를 열람한 필터.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}