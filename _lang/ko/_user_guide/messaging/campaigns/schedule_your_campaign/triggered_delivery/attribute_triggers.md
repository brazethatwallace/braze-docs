---
nav_title: 속성 트리거
article_title: 속성 트리거
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "이 참조 문서에서는 속성 트리거의 개요와 이를 사용하여 사용자에게 실행 기반 메시지를 보내는 방법을 설명합니다."
tool:
  - Campaigns

---

# 속성 트리거 {#attribute-triggers}

> 속성 트리거를 사용하면 사용자의 구독 상태 또는 커스텀 속성 값이 변경될 때 실행 기반 메시지를 보낼 수 있습니다.

속성 트리거는 다음 시나리오에서 사용할 수 있습니다:

- 구독 상태 업데이트.
- 부울, 정수, 문자열 또는 시간 유형 커스텀 속성 값이 임의의 값으로 변경.
- 부울, 정수 또는 문자열 커스텀 속성 값이 특정 값으로 변경.

{% alert note %}
대시보드에서 커스텀 속성 유형은 정수의 경우 `Number`, 날짜의 경우 `Time`으로 표시되며, `String` 또는 `Date`로 표시되지 않습니다.
{% endalert %}

속성 트리거를 사용하려면 Campaign 또는 Canvas 구성요소를 생성하고 전달 방법으로 **실행 기반 전달**을 선택합니다. 그런 다음 사용하려는 속성 트리거를 선택합니다.

![트리거를 선택하는 드롭다운이 있는 실행 기반 전달 섹션.]({% image_buster /assets/img_archive/trigger_attribute.png %})

## 구독 상태 업데이트 {#update-subscription-status}

`Update Subscription Status` 트리거를 사용하여 구독 상태가 업데이트된 사용자를 타겟팅합니다.

예를 들어, 이메일 또는 푸시 구독 상태가 수신 동의로 변경된 사용자를 타겟팅하여 수신 동의에 감사를 표할 수 있습니다. 또한 사용자가 이메일 구독을 탈퇴할 때마다 시스템에 웹훅을 보내 내부 시스템이 최신 구독 상태 정보를 유지하도록 할 수 있습니다.

{% alert important %}
이 트리거는 새 사용자가 기본 이메일 글로벌 상태인 `subscribed`로 생성되고 이후 상태를 `subscribed`로 업데이트하는 요청이 있는 경우에는 적용되지 않습니다. 구독 상태가 변경되지 않았기 때문입니다.
{% endalert %}

## 구독 그룹 상태 업데이트 {#update-subscription-group-status}

`Update Subscription Group Status` 트리거를 사용하여 이메일, SMS 또는 WhatsApp의 구독 그룹 상태가 업데이트된 사용자를 타겟팅합니다.

예를 들어, 프로그램에 수신 동의한 사용자에게 환영 SMS 메시지를 보낼 수 있습니다. 또한 업데이트 소스를 지정하여 메시지가 발송되는 시점을 더 세밀하게 제어할 수 있습니다.

사용 가능한 업데이트 소스는 채널에 따라 다릅니다:
- Canvas 사용자 업데이트 단계
- CSV 가져오기
- 수신 거부 목록
- 환경설정 센터
- REST API
- SDK
- Shopify (이메일, SMS)
- 인바운드 메시지 (SMS)

예를 들어, Braze가 특정 인바운드 SMS에 이미 자동으로 응답하므로 인바운드 메시지가 아닌 REST API에서 업데이트가 올 때만 환영 SMS를 보내고 싶을 수 있습니다.

## 커스텀 속성 값 변경 {#change-custom-attribute-value}

속성 변경의 경우, 트리거가 먼저 평가된 후 오디언스 기준이 평가됩니다. 이는 오디언스 기준이 먼저 평가된 후 트리거가 평가되는 기본 동작과 다릅니다. 경합 조건을 방지하려면 트리거로 사용되는 속성이 오디언스를 한정하는 데 사용되는 속성과 동일하지 않도록 해야 합니다.

### 임의의 새 값 옵션 {#any-new-value-option}

`Change Custom Attribute Value` 트리거와 `any new value` 옵션을 사용하여 부울, 정수, 문자열 또는 시간 유형 값이 임의의 새 값으로 변경될 때 사용자를 타겟팅합니다.

예를 들어, 리워드 포인트 수가 변경될 때 사용자를 타겟팅하여 현재 보유한 포인트를 알려줄 수 있습니다. 이 예시에서 사용자가 85 리워드 포인트를 보유하고 있고, 리워드 포인트 속성이 임의의 새 값으로 변경될 때 트리거되도록 Campaign을 설정했다고 가정합니다. 이 사용자의 리워드 포인트 속성 값이 임의의 새 값(예: 83, 84, 86 등)으로 변경되면 Campaign이 트리거됩니다.

다음 사용 사례인 등급 업데이트 알림을 살펴보겠습니다. 리워드 등급이 변경되면 사용자에게 알리고 싶을 수 있습니다. 이 사용 사례를 구현하려면 `Change Custom Attribute Value`로 트리거되는 Campaign을 설정하고, 커스텀 속성 리워드 등급이 임의의 새 값으로 변경될 때 트리거되도록 설정합니다.

{% alert important %}
속성 트리거는 현재 배열 속성에는 사용할 수 없습니다.
{% endalert %}

!["AA_current_rewards_tier"가 임의의 값으로 변경되는 커스텀 속성 값 변경 트리거.]({% image_buster /assets/img_archive/any_value.png %})

Liquid를 사용하여 고객의 새 리워드 등급으로 메시지 본문을 개인화하고 변경 사항에 대한 추가 정보를 제공할 수도 있습니다.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

### 특정 값 {#specific-value}

`Change Custom Attribute Value` 트리거와 `specific value` 옵션을 사용하여 부울, 정수 또는 문자열 커스텀 속성이 특정 값으로 변경될 때 사용자를 타겟팅합니다.

예를 들어, 리워드 등급이 최고 등급으로 변경될 때 사용자를 타겟팅합니다. 이 예시에서 최고 리워드 등급이 Super VIP라고 가정합니다. 사용자의 리워드 등급 커스텀 속성이 `Super VIP`로 변경될 때 트리거되도록 Campaign을 설정하여 Super VIP가 된 것을 축하할 수 있습니다.

!["AA_current_rewards_tier"가 특정 값 "super vip"로 변경되는 커스텀 속성 값 변경 트리거.]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- 특정 커스텀 속성 값에 대한 속성 트리거는 배열 및 시간 유형 커스텀 속성에는 사용할 수 없습니다.
- 커스텀 속성 값 변경 트리거는 커스텀 속성 값이 null로 업데이트될 때는 트리거되지 않습니다.
- 커스텀 속성 값 변경 트리거는 커스텀 속성 값이 실제로 변경될 때만 트리거됩니다. 커스텀 속성의 현재 값이 Braze에 다시 전송되는 경우(예: 좋아하는 색상 속성의 값이 빨간색인데 빨간색 값을 다시 Braze에 전송하는 경우), 커스텀 속성 값 변경 트리거는 발생하지 않습니다.
- 커스텀 속성 값 변경 트리거는 새로 생성된 사용자에게도 적용됩니다.
{% endalert %}