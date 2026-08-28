---
nav_title: SMS 발송
article_title: SMS 발송
page_order: 4
alias: /sms_message_sending/
description: "Braze에서 SMS 메시지를 발송할 때 적용되는 구독 그룹, 메시지 과금, 키워드 기본 사항을 확인하세요."
page_type: reference
channel:
  - SMS

---

# SMS 메시지 발송 {#sms-message-sending}

> Braze에서 SMS 메시지를 발송할 때 적용되는 구독, 과금, 키워드 처리 기본 사항을 확인하세요.

## SMS 발송 기본 사항 {#sms-sending-basics}

### 구독 그룹 선택 {#select-your-subscription-group}

[구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups)에서 SMS 메시지를 보내세요. 구독 그룹에는 짧은 코드, 긴 코드, 영숫자 발신자 ID 등 특정 메시징 목적을 위한 발신 전화번호가 포함됩니다. 트랜잭션 메시징과 프로모션 메시징 같은 사용 사례에는 별도의 구독 그룹을 사용하세요.

### 메시지 작성 {#compose-the-message}

메시지 필드, 글자 수 제한, 개인화, 미디어 및 링크 단축에 대한 자세한 내용은 [SMS, MMS 또는 RCS 메시지 만들기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create#sms-and-mms-fields-and-settings)를 참조하세요.

### 메시지 세그먼트 및 글자 수 제한 이해 {#understand-message-segments-and-character-limits}

SMS 메시지는 GSM-7 또는 UCS-2 인코딩을 사용하며, 메시지 세그먼트당 요금이 부과됩니다. 인코딩 규칙, 세그먼트 크기 및 세그먼트 계산기에 대한 자세한 내용은 [SMS 및 RCS 요금 계산기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)를 참조하세요.

### 키워드 커스터마이징 (선택 사항) {#keyword-customization-optional}

규정에 따라 옵트인, 옵트아웃, 도움말 또는 정보 키워드에 대한 응답이 필요합니다. [키워드 처리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing)를 통해 키워드, 응답, 언어별 키워드 세트를 정의하세요.

발송 모범 사례(다국가 발송 및 대량 발송 가이드 포함)에 대한 자세한 내용은 [SMS, MMS 및 RCS 모범 사례]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices)를 참조하세요.