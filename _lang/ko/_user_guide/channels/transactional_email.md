---
nav_title: 트랜잭션 이메일
article_title: 트랜잭션 이메일
page_order: 4
page_type: landing
channel:
  - email
search_rank: 3
description: "Braze에서 API 호출로 트리거되는 중요한 시간 민감 알림을 트랜잭션 이메일로 발송하세요."
---

# 트랜잭션 이메일 {#transactional-email}

> 트랜잭션 이메일은 고객과의 합의된 트랜잭션을 처리하기 위해 자동화된 비프로모션 메시지를 발송하도록 설계되었습니다. Braze에서 트랜잭션 이메일 Campaign을 사용하여 주문 확인, 비밀번호 재설정, 배송 업데이트 등 API 호출로 트리거되는 중요한 시간 민감 알림을 발송하세요.

## 필수 조건 {#prerequisites}

트랜잭션 이메일은 특정 Braze 패키지의 일부로만 제공됩니다. 자세한 내용은 Braze 고객 성공 매니저에게 문의하거나 [고객지원 티켓]({{site.baseurl}}/braze_support/)을 열어 주세요.

시작하기 전에 다음 사항을 준비해 주세요:

- IP 및 도메인 구성, 인증, IP 워밍을 포함한 [이메일 설정]({{site.baseurl}}/user_guide/channels/email/email_setup/) 완료
- `transactional.send` 권한이 있는 **Braze REST API 키**

## 활용 사례 {#use-cases}

트랜잭션 이메일은 비프로모션, 서비스 트리거 메시지를 발송하기 위해 설계되었습니다. 일반적인 활용 사례는 다음과 같습니다.

| 활용 사례 | 설명 |
| --- | --- |
| 주문 확인 | 고객의 구매가 접수되어 처리 중임을 확인합니다. |
| 비밀번호 재설정 | 고객이 계정 자격 증명을 재설정할 수 있도록 안전하고 시간 민감한 링크를 전달합니다. |
| 배송 알림 | 추적 정보 및 예상 배송 날짜를 포함하여 주문이 발송되었음을 고객에게 알립니다. |
| 계정 알림 | 결제 실패, 구독 변경, 보안 알림 등 중요한 계정 관련 알림을 발송합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Use cases" }

## 트랜잭션 이메일과 마케팅 이메일의 차이점 {#how-transactional-email-differs-from-marketing-email}

트랜잭션 이메일은 속도와 안정성에 최적화된 전용 Braze [트랜잭션 HTTP API]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/)를 통해 발송됩니다. 마케팅 이메일과 달리 트랜잭션 이메일은 다음과 같은 특징이 있습니다.

- 사용자가 마케팅 커뮤니케이션에 옵트인할 필요가 없습니다.
- 스케줄 또는 액션 기반 트리거가 아닌 API 호출로 트리거됩니다.
- 시간 민감 콘텐츠를 위한 거의 실시간 전달을 지원합니다.

## 다음 단계 {#next-steps}

- [트랜잭션 이메일 생성]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/)
- [추적]({{site.baseurl}}/user_guide/channels/transactional_email/tracking/)