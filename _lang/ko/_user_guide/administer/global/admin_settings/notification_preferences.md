---
nav_title: 알림 환경설정
article_title: 알림 환경설정
page_order: 1
page_type: reference
description: "이 참조 문서에서는 회사 계정의 메시징 및 활동을 모니터링하는 데 사용할 수 있는 옵션에 대해 설명합니다."

---

# 알림 환경설정 {#notification-preferences}

> 회사 계정의 메시징 및 활동을 모니터링하려면 특정 알림을 설정하고 알림이 전송되는 위치를 선택할 수 있습니다.

**알림 환경설정** 페이지에서는 회사에 대한 알림을 받을 사람(있는 경우)을 구성할 수 있습니다. Campaign 전달 또는 기술적 오류에 대한 알림을 수신할 대상을 구성할 수 있습니다. 주간 분석 보고서의 수신자를 지정할 수도 있습니다. 대부분의 알림에 대해 Braze는 이메일과 웹훅 채널을 지원합니다.

![Braze 대시보드의 알림 환경설정 페이지]({% image_buster /assets/img_archive/notification_preferences.png %})

이 페이지에 액세스하려면 **설정** > **관리자 설정** > **알림 환경설정**으로 이동합니다.

{% alert tip %}
Slack과 통합하여 알림을 받을 수도 있습니다. 단계는 [수신 웹훅을 사용하여 메시지 보내기](https://api.slack.com/incoming-webhooks)를 참조하세요.
{% endalert %}

## 사용 가능한 알림 {#available-notifications}

다음 표에서는 사용 가능한 알림과 알림을 전달하는 데 사용되는 채널에 대해 설명합니다.

{% alert note %}
알림 유형에 따라 **All Dashboard Users** 및 **All Admins**가 수신자 드롭다운에 표시되지 않을 수 있습니다. 수동으로 입력할 수 있으며, 수신자 값은 대소문자를 구분하므로 정확히 일치해야 합니다. 영어 이외의 언어로 현지화된 대시보드의 경우, 해당 알림에 대해 제안이 표시될 때 Braze가 보여주는 정확한 수신자 태그를 사용하세요. 직접 번역하지 마세요.
{% endalert %}

| 알림 | 설명 | 사용 가능한 알림 채널 |
|---|---|---|
| API 사용량 알림 | 이 항목을 선택하면 **API 사용량 대시보드**로 이동하며, 여기서 [**API 사용량 알림**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts/) 탭으로 이동하여 주요 API 요청 볼륨을 추적하는 알림을 설정할 수 있습니다. | 이메일, 웹훅 |
| AWS 자격 증명 오류 | Braze가 데이터 내보내기를 위해 Amazon Web Services 자격 증명을 사용하는 중에 오류가 발생할 때 수신자에게 알립니다. 여기에는 Google Cloud Storage 및 Azure(Microsoft Cloud Services)에 대한 자격 증명 오류 알림도 포함됩니다. | 이메일, 웹훅 |
| Campaign 자동 중단 | Braze가 Campaign을 중단했을 때 수신자에게 알립니다. | 이메일 |
| Canvas 자동 중단 | Braze가 Canvas를 중단했을 때 수신자에게 알립니다. | 이메일 |
| Campaign 상호작용 만료 | Campaign 상호작용 데이터 만료가 예정된 Campaign과, 리타겟팅 필터에서 해당 Campaign을 참조하며 지난 30일 이내에 메시지 발송에 사용된 Segments, Campaigns 또는 Canvases에 대한 정보를 수신자에게 알립니다. | 이메일 |
| Campaign/Canvas 업데이트됨 | 활성 Campaign 또는 Canvas가 업데이트되거나 비활성화될 때, 비활성 Campaign 또는 Canvas가 다시 활성화되거나 초안이 시작될 때 수신자에게 알립니다. | 이메일 |
| Campaign/Canvas 볼륨 한도 도달 | Campaign 또는 Canvas가 볼륨 한도에 도달했을 때 수신자에게 알립니다. | 이메일 |
| Canvas 상호작용 만료 | Canvas 상호작용 데이터 만료가 예정된 Canvas와, 리타겟팅 필터에서 해당 Canvas를 참조하며 지난 30일 이내에 메시지 발송에 사용된 Segments, Campaigns 또는 Canvases에 대한 정보를 수신자에게 알립니다. | 이메일 |
| Canvas 내 댓글 | Canvas에 새 댓글이 있을 때 수신자에게 알립니다. | 이메일 |
| 연결된 콘텐츠 오류 | 연결된 콘텐츠 엔드포인트에 오류가 발생할 때 수신자에게 알립니다. | 이메일 |
| 푸시 오류 | 푸시 엔드포인트에 오류가 발생할 때 수신자에게 알립니다. | 이메일, 웹훅 |
| 스케줄된 Campaign 한도 도달 | 반복 스케줄된 Campaign의 한도에 도달했을 때 수신자에게 알립니다. | 이메일, 웹훅 |
| 스케줄된 Campaign 발송 완료 | 스케줄된 Campaign의 발송이 완료되었을 때 수신자에게 알립니다. | 이메일, 웹훅 |
| 웹훅 오류 | 웹훅 엔드포인트에 오류가 발생할 때 수신자에게 알립니다. | 이메일 |
| 주간 분석 보고서 | 매주 월요일에 수신자에게 지난 한 주간의 워크스페이스 활동 요약을 보냅니다. 수신자는 자신이 속한 각 워크스페이스에 대한 요약을 받습니다. | 이메일 |
| 일일 Canvas/Campaign 진입 볼륨 한도 | 발송 한도에 도달할 때마다 알림을 보냅니다. | 이메일 |
| 에이전트 콘솔 오류 | [에이전트 콘솔 에이전트]({{site.baseurl}}/user_guide/brazeai/agents/)가 호출 한도에 도달했거나, 사용할 수 없게 된 모델을 사용하거나, LLM 제공업체와의 결제 오류가 발생했을 때(자체 API 키 사용 시에만) 수신자에게 알립니다. | 이메일 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용 가능한 알림" }

{% alert note %}
[일시 중지된 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/#suspending-company-users)도 Braze로부터 알림을 계속 받을 수 있습니다.
{% endalert %}

## 주간 분석 보고 {#weekly-analytics-reporting}

Braze는 선택적으로 매주 월요일 오전 5시(EST)에 회사 내 지정된 개인에게 이메일로 주간 보고서를 보냅니다. **데이터 설정** > **커스텀 이벤트**에서 주간 보고서에 포함할 커스텀 이벤트를 선택할 수 있습니다.

주간 보고서에 포함할 이벤트를 최대 5개까지 선택할 수 있습니다.

![분석 보고서에 포함할 이벤트 선택]({% image_buster /assets/img_archive/company_analytics_report_new.png %})