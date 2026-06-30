---
nav_title: SMS 발송
article_title: SMS 발송
page_order: 4
alias: /sms_message_sending/
description: "이 참조 문서에서는 SMS 발송의 기본 사항과 모범 사례를 다룹니다."
page_type: reference
channel:
  - SMS

---

# SMS 메시지 발송 {#sms-message-sending}

> 메시징은 복잡할 수 있지만, 반드시 그럴 필요는 없습니다. 다음 섹션에서는 구독 그룹의 중요성, SMS 메시지 세그먼트 및 메시지 본문 요구 사항, 그리고 사용 가능한 고급 커스텀 옵션을 포함하여 Braze에서의 SMS 메시지 발송 기본 사항을 설명합니다.

## SMS 발송 기본 사항 {#sms-sending-basics}

### 구독 그룹 선택 {#select-your-subscription-group}

SMS 메시지는 [구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups)에서 발송해야 합니다. 구독 그룹은 특정 유형의 메시징 목적에 사용되는 발송 전화번호(짧은 코드, 긴 코드 및/또는 영숫자 발신자 ID 등)의 모음입니다. 가입된 사용자만 타겟팅되도록 구독 그룹을 지정해야 합니다. 일부 클라이언트는 트랜잭션 SMS 메시징 및 프로모션 SMS 메시징과 같은 다양한 사용 사례에 대해 여러 구독 그룹을 보유할 수 있습니다.<br><br>

### 메시지 본문 입력 {#input-message-body}

SMS 메시지 본문은 이모지, Liquid, 연결된 콘텐츠를 포함하여 최대 1,600자까지 허용됩니다. 단일 Campaign 발송으로 여러 메시지 세그먼트가 발송될 수 있습니다. Braze SMS 메시지 본문은 [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) 또는 [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) 인코딩 표준으로 구성할 수 있습니다. UCS-2 문자(예: 이모지)가 사용되는 경우, 메시지 본문은 해당 인코딩 표준에 맞게 자동으로 포맷됩니다.<br><br>

### 메시지 세그먼트 및 글자 수 제한 이해 {#understand-message-segments-and-character-limits}

SMS 메시지 세그먼트는 SMS 업계에서 메시지를 계산하는 방식입니다. 메시지 세그먼트는 단일 SMS 발송으로 전송되는 정의된 글자 수(GSM-7 인코딩의 경우 160자, UCS-2 인코딩의 경우 67자)까지의 그룹입니다. GSM-7 인코딩을 사용하여 161자의 SMS를 발송하면 두(2)개의 메시지 세그먼트가 전송된 것을 확인할 수 있습니다. 여러 메시지 세그먼트를 발송하면 추가 요금이 발생할 수 있습니다.<br><br>

### 키워드 커스텀 설정(선택 사항) {#keyword-customization-optional}

규정에 따라 모든 옵트인, 옵트아웃 및 도움말/정보 SMS 키워드 응답에 대한 회신이 필요합니다. Braze를 사용하면 옵트인, 옵트아웃 및 도움말 응답을 트리거하는 자체 키워드를 정의하고, 사용자에게 전송되는 자체 응답을 관리하며, 다양한 언어에 대한 키워드 세트를 정의할 수 있습니다. 자세한 내용은 [키워드 처리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing) 모음을 참조하세요.

{% alert tip %}
SMS Campaign을 만드는 방법을 알고 싶으신가요? [SMS, MMS 또는 RCS 메시지 생성]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)에 대한 단계별 가이드를 확인하세요.
{% endalert %}

다국가 및 대량 발송 가이드를 포함한 발송 모범 사례는 [SMS, MMS 및 RCS 모범 사례]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices)를 참조하세요.