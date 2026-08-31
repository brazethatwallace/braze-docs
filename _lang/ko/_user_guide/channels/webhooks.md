---
nav_title: 웹훅
article_title: 웹훅
page_order: 9
page_type: landing
alias: /about_webhooks/
description: "커스텀 이벤트로 트리거되는 Braze의 웹훅을 사용하여 시스템을 연결하고, 외부 엔드포인트로 데이터와 프로그래밍 방식의 메시지를 전송하세요."
channel:
  - webhooks
search_rank: 3
---

# 웹훅 {#webhooks}

> 웹훅은 특정 조건이 충족되면 한 시스템에서 다른 시스템으로 전송되는 자동화된 메시지입니다. Braze에서 이 조건은 보통 커스텀 이벤트의 트리거입니다. 웹훅은 데이터와 프로그래밍 기능에 대한 동적이고 유연한 접근을 제공하며, 프로세스를 간소화하는 고객 여정을 설정할 수 있도록 지원합니다.

## 전제 조건 {#prerequisites}

웹훅 사용 가능 여부는 Braze 패키지에 따라 다릅니다. 시작하려면 계정 매니저 또는 고객 성공 매니저에게 문의하세요.

## 사용 사례 {#use-cases}

웹훅은 시스템을 연결하는 훌륭한 방법입니다. 결국 웹훅은 앱이 서로 통신하는 방식이기 때문입니다. 다음은 웹훅이 특히 유용할 수 있는 일반적인 시나리오입니다:

- Braze와 데이터를 주고받기
- Braze에서 직접 지원하지 않는 채널을 통해 고객에게 메시지 보내기
- Braze API에 게시하기

더 구체적인 사용 사례는 다음과 같습니다:

- 웹훅과 Canvas를 사용하여 리드를 검증하고 라우팅하는 [리드 스코어링 워크플로]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring)를 만들 수 있습니다.
- 사용자가 이메일을 탈퇴하면 웹훅으로 분석 데이터베이스나 CRM에 동일한 정보를 업데이트하여 해당 사용자의 행동에 대한 전체적인 뷰를 확보할 수 있습니다.
- Facebook 메신저나 Line을 통해 사용자에게 [트랜잭션 메시지]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)를 보낼 수 있습니다.
- 웹훅을 사용하여 [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob)과 같은 서드파티 서비스와 통신함으로써, 고객의 인앱 및 웹 활동에 대한 응답으로 다이렉트 메일을 보낼 수 있습니다.
- 게이머가 특정 레벨에 도달하거나 특정 포인트를 적립하면, 웹훅과 기존 API 설정을 사용하여 캐릭터 업그레이드나 코인을 해당 계정에 직접 보낼 수 있습니다. 멀티 채널 메시징 캠페인의 일부로 웹훅을 보내면 푸시 또는 기타 메시지를 보내 게이머에게 보상을 동시에 알릴 수 있습니다.
- 항공사라면 웹훅과 기존 API 설정을 사용하여 고객이 특정 횟수의 항공편을 예약한 후 할인 혜택을 고객 계정에 적립할 수 있습니다.
- 무한한 "If This Then That"([IFTTT](https://ifttt.com/about)) 레시피가 가능합니다. 예를 들어, 고객이 이메일을 통해 앱에 로그인하면 해당 주소가 자동으로 Salesforce에 설정될 수 있습니다.

## 웹훅 오류 처리 및 사용량 제한 {#webhook-error-handling-and-rate-limiting}

Braze는 특정 HTTP 응답(예: `408`, `429`, `5XX`)에 대해서만 웹훅 전송을 재시도합니다. `401 Unauthorized` 및 기타 `4XX` 오류를 포함한 대부분의 다른 응답은 재시도되지 않습니다. `Retry-After` 및 `X-Rate-Limit-*`와 같은 응답 헤더는 **응답이 이미 재시도 대상인 경우에** 백오프 타이밍에 영향을 줄 수 있지만, 재시도 가능한 범위에 해당하지 않는 오류를 Braze가 재시도하도록 만들지는 않습니다.

전체 응답 코드 테이블, 재시도 제한 및 타임아웃 동작에 대한 자세한 내용은 [응답 코드 및 재시도 로직]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#response-codes-and-retry-logic)을 참조하세요.

특정 호스트에 대한 대부분의 웹훅 요청이 실패하는 경우, Braze는 해당 호스트에 대한 모든 전송 시도를 일시적으로 보류합니다. 정의된 쿨다운 기간이 지나면 전송이 재개되어 시스템이 복구할 수 있도록 합니다.

## Braze 파트너와 웹훅 사용하기 {#utilizing-webhooks}

웹훅을 사용하는 방법은 다양하며, 기술 파트너(Alloys)를 통해 웹훅을 활용하여 고객 및 사용자와의 커뮤니케이션을 한 단계 높일 수 있습니다.

확인해 보세요:
* [메신저]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger)
* [Remerge]({{site.baseurl}}/partners/remerge)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob)
* 그리고 더 많은 [기술 파트너]({{site.baseurl}}/partners/home)를 확인하세요!

## 다음 단계 {#next-steps}

- [웹훅 생성]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)
- [Braze-to-Braze 웹훅 생성]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook)