---
nav_title: 메시지 활동 로그
article_title: 메시지 활동 로그
page_order: 3
page_type: reference
description: "이 참조 문서에서는 Campaign 및 전송과 관련된 메시지를 보여주는 메시지 활동 로그에 대해 설명합니다. 여기에서 로그 메시지를 이해하는 방법에 대한 정보도 확인할 수 있습니다."

---

# 메시지 활동 로그 {#dev-console-troubleshooting}

> **메시지 활동 로그**를 통해 Campaign 및 전송과 관련된 모든 메시지(특히 오류 메시지)를 확인할 수 있습니다.

API Campaign 트랜잭션을 확인하고, 실패한 메시지에 대한 세부 정보를 문제 해결하며, 알림 전달을 개선하거나 기존 기술 문제를 해결하는 방법에 대한 인사이트를 얻을 수 있습니다.

로그에 접근하려면 **설정** > **설정 및 테스트** > **메시지 활동 로그**로 이동합니다.

![메시지 활동 로그]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
이 문서 외에도 메시지 활동 로그를 사용하여 직접 문제 해결 및 디버깅을 수행하는 방법을 다루는 [품질 보증 및 디버깅 툴](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze 학습 과정도 확인하는 것을 권장합니다.
{% endalert %}

**메시지 활동 로그**에 기록된 다음 콘텐츠를 기준으로 필터링할 수 있습니다:

- 푸시 알림 오류
- 중단된 템플릿 인앱 메시지 오류
- 웹훅 오류
- 메일 오류
- API 메시지 기록
- 연결된 콘텐츠 오류
- REST API 연결된 오디언스 오류
- 사용자 별칭 지정 오류
- A/B 테스트 오류
- SMS/MMS 오류
- WhatsApp 오류
- 라이브 활동 오류
- 잘못된 사용자 트리거 오류
- Braze Agents [일일 호출 한도]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#monitor-your-agent) 오류
- Braze Agents 사용 불가 [모델]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) 오류

이러한 메시지는 Braze 자체 시스템, 사용자의 앱 또는 플랫폼, 또는 서드파티 파트너로부터 올 수 있습니다. 따라서 이 로그에 표시될 수 있는 메시지의 수는 무한합니다.

## 로그 메시지 이해하기 {#understanding-log-messages}

메시지의 의미를 파악하려면 각 메시지의 문구와 해당 메시지에 대응하는 열에 주의를 기울이세요. 이를 통해 맥락 단서를 활용한 문제 해결에 도움이 됩니다.

예를 들어, **Aborted Message Error** 항목은 [Liquid 중단 메시지]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)뿐만 아니라 다양한 이유로 발생할 수 있습니다. 구체적인 이유를 확인하려면 **Message** 열을 읽어보세요:

- Liquid `abort_message` 태그에 의해 발송이 중단된 경우, **Message** 열에 호출된 정확한 Liquid 스니펫이 표시됩니다. 예: {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %}.
- 다른 중단 사유의 경우, **Message** 열에 발송이 중단된 이유가 설명됩니다.

### API Campaign 페이로드 {#api-campaign-payloads}

메시지 활동 로그는 API Campaign 유형에 따라 다른 정보를 기록합니다. [`/messages/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)는 API 메시지 레코드에 메시지 본문(messages)을 기록하는 반면, [`/campaigns/trigger/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)는 요청 페이로드나 `api_trigger_properties`를 메시지 활동 로그에 기록하지 않습니다.

### 일반적인 메시지 {#common-messages}

자주 볼 수 있는 몇 가지 일반적인 메시지 유형이 있으며, 일부는 문제를 진단하고 해결하는 데 도움이 되는 문제 해결 링크를 제공하기도 합니다.

다음에 나열된 메시지는 예시 목적이며, 로그의 **Message** 열에 표시되는 내용과 정확히 일치하지 않을 수 있습니다.

| 메시지 유형 | 잠재적 메시지 | 설명 |
|---|---|---|
| 소프트 바운스 | The email address same@example.com soft bounced. | 이메일 주소가 유효하고 이메일 메시지가 수신자의 메일 서버에 도달했지만, "일시적인" 문제로 거부되었습니다. <br><br>일반적인 소프트 바운스 원인은 다음과 같습니다: {::nomarkdown} <ul> <li> 메일함이 가득 찬 경우 (사용자가 할당량을 초과) </li> <li> 서버가 다운된 경우 </li> <li> 메시지가 수신자의 받은편지함에 비해 너무 큰 경우 </li>  </ul> {:/} 이메일이 소프트 바운스를 받은 경우, 일반적으로 72시간 이내에 재시도하지만, 재시도 횟수는 수신자에 따라 다릅니다. |
| 하드 바운스 | The email account that you tried to reach does not exist. Try double-checking the recipient's email address for typos or unnecessary spaces. | 메시지가 이 사람의 받은편지함에 도달하지 못했습니다. 도달할 받은편지함이 존재하지 않기 때문입니다. 더 자세히 알아보려면, 이러한 메시지에는 **View Details** 열에 의도한 수신자의 프로필을 볼 수 있는 링크가 포함되어 있을 수 있습니다.|
| 차단 | Spam message is rejected because of anti-spam policy. | 메시지가 스팸으로 분류되었습니다. 이 메일 오류는 ESP로부터 이메일이 삭제되었다는 이벤트를 수신한 경우 사용자에 대해 기록됩니다. 해당 수신자에게만 해당될 수 있지만, 이 메시지가 자주 표시된다면 발송 습관이나 메시지 내용을 재검토해야 할 수 있습니다. 또한, [IP 워밍업]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)을 수행했는지 되돌아보세요. 수행하지 않았다면 Braze에 연락하여 이를 시작하는 방법에 대한 조언을 받으세요.|
| 중단된 메시지 오류 | {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %} | Liquid `abort_message` 태그에 의해 발송이 중단된 경우, **Message** 열에 호출된 정확한 Liquid 스니펫이 표시됩니다. 다른 **Aborted Message Error** 항목에는 중단 사유를 설명하는 다른 메시지가 포함될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="일반적인 메시지" }

### 내 메시지가 여기에 나열되지 않는 이유는 무엇인가요? {#why-isnt-my-message-listed-here}

메시지 활동 로그의 메시지는 Braze, 앱 또는 플랫폼, 서드파티 파트너 등 다양한 소스에서 올 수 있습니다. 이는 이 로그에 표시될 수 있는 메시지의 수가 무한하다는 것을 의미합니다. 상상할 수 있듯이, 모든 메시지를 나열할 수는 없습니다!

예를 들어, 앞의 표에 나열된 것 외에도 잠재적인 "차단" 메시지에는 다음과 같은 것들이 있을 수 있습니다:

- Unfortunately, messages from [_IP_ADDRESS_] weren't sent. Please contact your Internet Service provider since part of their network is on our block list.
- Message rejected due to local policy.
- The message was blocked by the receiver as spam.
- Service unavailable, Client host [_IP_ADDRESS_] blocked using Spamhaus.

## 저장 보존 기간 {#storage-retention-period}

최근 60시간 이내의 오류는 메시지 활동 로그에서 확인할 수 있습니다. 60시간이 지난 로그는 정리되어 더 이상 접근할 수 없습니다.

### 저장되는 오류 로그 수 {#number-of-error-logs-stored}

저장되는 로그 수는 여러 조건에 따라 달라집니다. 예를 들어, 예약된 Campaign이 수천 명의 사용자에게 발송된 경우, 메시지 활동 로그에서 모든 오류가 아닌 오류의 샘플만 표시될 수 있습니다. 다음은 저장되는 로그 수에 영향을 미치는 조건에 대한 개요입니다:
- 다음 오류 유형의 경우, 동일한 Campaign 또는 캔버스 단계에서 1시간(고정 시계 기준) 이내에 동일한 오류 유형의 오류 로그가 최대 20개까지 저장됩니다:
    - 연결된 콘텐츠 오류
    - 메시지 중단 오류
    - 웹훅 오류
    - SMS 거부 오류
    - SMS 전송 실패 오류
    - WhatsApp 실패 오류
    - A/B 테스트 오류
- 다음 오류 유형의 경우, 동일한 Campaign 또는 캔버스 단계와 앱 조합에서 동일한 오류 유형의 푸시 알림 오류 로그가 최대 20개까지 저장됩니다:
    - 유효하지 않은 푸시 자격 증명
    - 유효하지 않은 푸시 토큰
    - 푸시 자격 증명 없음
    - 토큰 오류
    - 할당량 초과
    - 재시도 시간 초과
    - 유효하지 않은 페이로드
    - 예기치 않은 오류
- 다음 오류 유형의 경우, 동일한 앱에서 1시간(고정 시계 기준) 이내에 동일한 오류 유형의 오류 로그가 최대 100개까지 저장됩니다:
    - 라이브 활동 오류 (푸시 자격 증명 없음)
    - 라이브 활동 오류 (유효하지 않은 푸시 자격 증명)
    - 기타 라이브 활동 오류
    - APN 피드백 제거된 토큰 오류
- 다음 오류 유형의 경우, 동일한 Campaign 또는 캔버스 단계에서 1시간(고정 시계 기준) 이내에 동일한 오류 유형의 오류 로그가 최대 100개까지 저장됩니다:
    - 이메일 소프트 바운스 오류
    - 이메일 하드 바운스 오류
    - 이메일 차단 오류
- 동일한 워크스페이스에서 1시간(고정 시계 기준) 이내에 사용자 별칭 지정 오류 로그가 최대 100개까지 저장됩니다.

## 테스트 전송 {#test-sends}

**메시지 활동 로그**는 다음 메시징 채널에 대한 테스트 로그를 표시합니다:

- SMS
- WhatsApp
- LINE
- KakaoTalk
- 웹훅

이메일, Content Cards, 인앱 메시지, 푸시 채널에서는 테스트 전송 로그를 사용할 수 없습니다.

테스트 전송 로그에는 "[TEST SEND]" 접두사가 붙지만, 모든 테스트 전송 로그에 이 접두사가 포함되는 것은 아닙니다(예: 연결된 콘텐츠 오류에는 접두사가 포함되지 않습니다).