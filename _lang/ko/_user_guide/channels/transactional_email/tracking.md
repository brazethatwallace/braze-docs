---
nav_title: "추적 설정"
article_title: "추적"
page_order: 2
description: "이 참조 문서에서는 트랜잭션 이메일 Campaign에 대한 실시간 추적을 설정하는 방법을 설명합니다."
page_type: reference
tool:
  - Campaigns
channel: email

---

# 트랜잭션 이메일 추적 {#track-transactional-emails}

> 이 페이지에서는 [트랜잭션 이메일 Campaign]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/)에 대한 실시간 추적을 설정하는 방법을 설명합니다. 엔드포인트 자체에 대한 자세한 내용은 [API 트리거 전달을 사용하여 트랜잭션 이메일 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/)를 참조하세요.

주문 확인이나 비밀번호 재설정과 같은 트랜잭션 이메일을 보낼 때, 해당 이메일이 고객에게 도달하는지 아는 것이 중요합니다. Braze 트랜잭션 HTTP 이벤트 포스트백을 사용하면 모든 트랜잭션 이메일의 상태에 대한 실시간 인사이트를 얻을 수 있으므로, 문제가 발생했을 때 신속하게 대응할 수 있습니다.

이 기능을 사용하면 다음과 같은 작업이 가능합니다:

- **이메일을 실시간으로 모니터링:** 메시지가 전송, 처리, 전달되었는지 또는 문제가 발생했는지 즉시 확인할 수 있습니다.
- **사전 대응:** 메시지를 재시도하거나, SMS와 같은 다른 채널로 전환하거나, 대체 시스템을 사용하여 커뮤니케이션이 전달되도록 할 수 있습니다.

## 트랜잭션 이메일 추적하기 {#tracking-your-transactional-emails}

{% multi_lang_include http_event_postback.md %}