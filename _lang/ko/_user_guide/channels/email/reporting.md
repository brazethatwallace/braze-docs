---
nav_title: 보고서
article_title: 이메일 보고서
page_order: 21
description: "이 참조 문서에서는 이메일 보고서의 다양한 구성요소와 대시보드에서 확인할 수 있는 위치를 다룹니다."
tool:
  - Reports
channel:
  - email

---

# 이메일 보고서 {#email-reporting}

> 이 문서에서는 이메일 보고서의 다양한 구성요소와 대시보드에서 확인할 수 있는 위치를 다룹니다.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## 문제 해결 {#troubleshooting}

### 반송된 이메일 {#bounced-emails}

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** 다른 주소를 시도하거나, 다른 채널을 통해 재참여를 유도하거나, 본인의 테스트 주소에 한해서만 억제 목록에서 해당 주소를 제거하세요. 실제 사용자 억제를 제거하면 발신 평판에 악영향을 줄 수 있으므로 피하세요.
- **Mailbox full / invalid account:** 대부분 목록 품질 문제의 신호입니다. 최근에 열람하거나 클릭한 사용자(예: 최근 30~60일)를 우선시하면서 비활성 또는 잘못된 주소를 정리하세요.

#### 소프트 바운스 재시도 동작 {#soft-bounce-retry-behavior}

일시적인 문제(예: 메일함 가득 참, 서버 일시적 사용 불가 또는 기타 일시적 전달 가능성 장애)로 인해 이메일이 소프트 바운스되면, Braze는 최대 72시간 동안 자동으로 전달을 재시도합니다. 재시도 횟수는 수신 서버에 따라 다릅니다.

재시도 기간이 지나도 이메일이 성공적으로 전달되지 않으면, Braze는 해당 Campaign 발송에 대해 소프트 바운스 이벤트 하나를 기록합니다. 이러한 소프트 바운스는 Campaign 분석에 표시되지 않지만, 다음과 같은 방법으로 확인할 수 있습니다:
- [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 바운스 사유를 모니터링
- [소프트 바운스 Segment 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced)를 사용하여 향후 발송에서 해당 사용자를 제외

이 재시도 기간 때문에, 소프트 바운스된 이메일이 최종적으로 전달에 실패한 Campaign에서는 이메일 전달 측정기준(전달, 바운스, 스팸 비율)이 합산하여 100%가 되지 않을 수 있습니다.

소프트 바운스에 대한 자세한 내용은 [이메일 분석 용어집]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce)을 참조하세요.

### 유효하지 않은 도메인 {#invalid-domains}

`unable to get mx info`와 같은 오류는 많은 대상이 잘못된 도메인(예: 오타)을 사용하고 있음을 의미하는 경우가 많습니다. 해당 프로필을 Segment로 분류하고, 내보내기한 후, 수정하여 다시 가져오세요.

### 제한된 IP {#throttled-ips}

메일함 제공업체가 발송량, 평판 또는 두 가지 모두로 인해 IP에서의 전달을 일시적으로 늦추거나 차단하는 경우, [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]`라는 메시지를 확인할 수 있습니다. Braze는 지연된 메시지를 재시도하며, 이러한 지연이 집중되면 소프트 바운스가 함께 증가하는 경우가 많습니다.

이 패턴은 일반적으로 현재 평판 수준에서 메일함 제공업체가 수용하는 속도보다 빠르게 발송하고 있음을 의미합니다. 인게이지먼트 및 목록 품질을 개선하는 것 외에도, [전달 속도 사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)을 사용하여 Campaign 또는 Canvas에서 Braze를 통해 메시지가 발송되는 속도를 제한하세요. 이렇게 하면 전달 가능성 팀과 함께 장기적인 해결책을 마련하는 동안 스로틀링을 줄이는 데 도움이 됩니다.

특정 도메인에 대해 스로틀링이 지속되면, 해당 도메인으로의 발송량을 줄이고 Braze 전달 가능성 지원팀에 문의하여 안내를 받으세요.