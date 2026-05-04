---
nav_title: "다중 비즈니스 계정"
article_title: "다중 비즈니스 계정"
page_order: 5
description: "이 참조 문서에서는 WhatsApp 비즈니스 계정과 전화번호를 추가하는 단계를 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# 다중 WhatsApp 비즈니스 계정 및 전화번호 {#multiple-whatsapp-business-accounts-and-phone-numbers}

> 각 워크스페이스에 여러 WhatsApp 비즈니스 계정과 구독 그룹(및 전화번호)을 추가할 수 있습니다. <br><br>각 구독 그룹은 하나의 고유 전화번호에 연결되므로, 동일한 전화번호를 여러 구독 그룹에 연결하거나 여러 전화번호를 하나의 구독 그룹에 연결할 수 없습니다.

## 다중 WhatsApp 비즈니스 계정 {#multiple-whatsapp-business-accounts}

다중 WhatsApp 비즈니스 계정은 여러 브랜드를 보유한 Braze 워크스페이스의 사용자에게 WhatsApp 메시지를 보내려는 경우에 유용합니다. 각 비즈니스 계정은 WhatsApp 내에서 독립적으로 운영되며, 자체 전화번호, 메시지 템플릿, 품질 등급을 갖습니다.

동일한 Meta Business Manager 내에 중첩된 비즈니스 계정은 사용자 액세스 권한 관리 및 카탈로그(아직 Braze에서 지원되지 않음)도 공유합니다.

![Braze와 WhatsApp 에코시스템 다이어그램으로, 워크스페이스와 WhatsApp 비즈니스 계정이 서로 어떻게 연결되는지 보여줍니다: 하나의 구독 그룹을 하나의 전화번호에, 여러 WhatsApp 비즈니스 계정을 하나의 워크스페이스에, 하나의 워크스페이스를 여러 Meta Business Portfolio에 연결할 수 있습니다.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})

### WhatsApp 비즈니스 계정 추가 {#adding-a-whatsapp-business-account}

워크스페이스당 최대 10개의 WhatsApp 비즈니스 계정을 추가할 수 있습니다. 비즈니스 계정은 서로 다른 Meta Business Manager에 중첩될 수 있습니다. 계정을 추가하려면:

1. **Technology Partners** > **WhatsApp**으로 이동하여 **Add WhatsApp Business Account**를 선택합니다.

![비즈니스 계정 추가 또는 구독 그룹 및 번호 추가 옵션이 있는 WhatsApp 메시징 통합 섹션.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. 가입 워크플로를 진행합니다. 자세한 단계별 안내는 [WhatsApp 임베디드 가입]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup/)을 참조하세요.

{% alert important %}
전화번호는 다른 WhatsApp 계정에 등록되어 있지 않아야 하는 등 WhatsApp 전화번호의 모든 요구 사항을 충족해야 합니다.
{% endalert %}

## 다중 구독 그룹 및 전화번호 {#multiple-subscription-groups-and-phone-numbers}

메시지 템플릿은 동일한 WhatsApp 비즈니스 계정 내의 모든 전화번호 간에 공유됩니다. WhatsApp 구독 그룹에 대한 자세한 내용은 [구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/)을 참조하세요.

각 WhatsApp 전화번호는 사용자에게 별도의 WhatsApp 채팅으로 표시됩니다. WhatsApp 비즈니스 계정 내의 각 전화번호는 서로 독립적으로 운영되므로, 다음 항목에 대해 동일하거나 다른 값을 가질 수 있습니다:
- 표시 이름
- 상태
- 품질 등급
- 메시징 한도

### 구독 그룹 및 전화번호 추가 {#adding-a-subscription-group-and-phone-number}

WhatsApp 비즈니스 계정당 최대 20개의 구독 그룹(및 발송 전화번호)을 추가할 수 있습니다. 구독 그룹과 전화번호를 추가하려면:

1. **Technology Partners** > **WhatsApp**으로 이동하여 **Add Subscription Group and Number**를 선택합니다.

![비즈니스 계정 추가 또는 구독 그룹 및 번호 추가 옵션이 있는 WhatsApp 메시징 통합 섹션.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2. 가입 워크플로를 진행합니다. <br><br> **Select your WhatsApp Business Account** 단계에서 기존 WhatsApp 비즈니스 계정을 선택하고 새 전화번호를 추가합니다. 이 번호는 다른 WhatsApp 계정에 등록되어 있지 않아야 하는 등 WhatsApp 전화번호의 모든 요구 사항을 충족해야 합니다.

### 구독 그룹 및 전화번호 제거 {#removing-a-subscription-group-and-phone-number}

1. **Audience** > **Subscriptions**로 이동하여 구독 그룹을 아카이브합니다.
2. Meta Business Manager로 이동하여 전화번호를 삭제합니다.