---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "이 참조 문서에서는 비즈니스 분석 플랫폼인 Mixpanel과 Braze 간의 파트너십을 설명합니다. Mixpanel 코호트를 Braze로 가져와 향후 Braze Campaign 또는 Canvases에서 사용자를 타겟팅하는 데 사용할 수 있는 Braze Segments를 생성할 수 있습니다."
page_type: partner
search_tag: Partner
tool: Currents

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommixpanel-integration-with-braze339085scorm2u7y2e6qrldh2-stylefloatrightwidth120pxborder0-classnoimgbordermixpanel}

> [Mixpanel](https://mixpanel.com/)은 Mixpanel에서 다른 플랫폼으로 이벤트를 내보내 더 심층적인 분석을 수행할 수 있는 비즈니스 분석 플랫폼입니다. 수집된 데이터는 커스텀 보고서를 작성하고 사용자 참여 및 리텐션을 측정하는 데 사용할 수 있습니다.

Braze와 Mixpanel 통합을 통해 [Mixpanel 코호트를 Braze로 가져와]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/) 향후 Braze Campaign 또는 Canvases에서 사용자를 타겟팅할 수 있는 Braze Segments를 생성할 수 있습니다. 코호트 동기화는 Braze에서 코호트 멤버십을 업데이트하며, Mixpanel 이벤트나 사용자 속성정보를 가져오지는 않습니다. 자세한 내용은 [Mixpanel 코호트 가져오기]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/#data-import-integration)를 참조하세요.

또한 Braze 커런츠를 사용하여 [Braze 이벤트를 Mixpanel로 내보내](#data-export-integration) 전환, 리텐션 및 제품 사용에 대한 더 심층적인 분석을 수행할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Mixpanel 계정 | 이 파트너십을 활용하려면 [Mixpanel 계정](https://mixpanel.com/)이 필요합니다. |
| Currents | 데이터를 Mixpanel로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 데이터 내보내기 통합 {#data-export-integration}

Braze에서 Mixpanel로 내보낼 수 있는 이벤트의 전체 목록은 아래에서 확인할 수 있습니다. Mixpanel로 전송되는 모든 이벤트에는 사용자의 `external_user_id`가 Mixpanel Distinct ID로 포함됩니다. 현재 Braze는 `external_user_id`가 설정되지 않은 사용자에 대해서는 이벤트 데이터를 전송하지 않습니다.

Mixpanel로 두 가지 유형의 이벤트를 내보낼 수 있습니다: 메시지 발송과 직접 관련된 Braze 이벤트로 구성된 [메시지 참여 이벤트](#supported-currents-events)와 세션, 커스텀 이벤트, 플랫폼을 통해 추적된 구매 등 기타 앱 또는 웹사이트 활동을 포함하는 [고객 행동 이벤트](#supported-currents-events)입니다. 모든 커스텀 이벤트에는 `[Braze Custom Event]` 접두사가 붙습니다. 커스텀 이벤트 속성정보와 구매 이벤트 속성정보에는 각각 `[Custom event property]`와 `[Purchase property]` 접두사가 붙습니다.

추가 이벤트 권한에 대한 액세스가 필요한 경우 계정 매니저에게 문의하거나 [고객지원 티켓]({{site.baseurl}}/braze_support/)을 열어주세요.

### 1단계: Mixpanel 자격 증명 가져오기 {#step-1-get-mixpanel-credentials}

Mixpanel 대시보드에서 새 프로젝트 또는 기존 프로젝트의 **Project Settings**를 클릭합니다. 여기에서 Mixpanel API 시크릿과 Mixpanel 토큰을 확인할 수 있습니다. 이 자격 증명은 다음 단계에서 Currents 연결을 생성하는 데 사용됩니다.

### 2단계: Braze Current 생성 {#step-2-create-braze-current}

1. Braze에서 **Currents** > **+ Create Current** > **Create Mixpanel Export**로 이동합니다.
2. 나열된 필드에 통합 이름, 연락처 이메일, Mixpanel API 시크릿 및 Mixpanel 토큰을 입력합니다.
3. 추적하려는 이벤트를 선택합니다. 사용 가능한 이벤트 목록이 제공됩니다.
4. **Launch Current**을 선택합니다.

![Braze Mixpanel Currents 페이지. 이 페이지에는 통합 이름, 연락처 이메일, API 시크릿 및 Mixpanel 내보내기 토큰 필드가 포함되어 있습니다. Currents 페이지 하단에는 보낼 수 있는 Currents 이벤트가 나열되어 있습니다.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
자세한 내용은 Mixpanel의 [통합 문서](https://help.mixpanel.com/hc/en-us/articles/360001243663)를 확인하세요.
{% endtab %}

## 지원되는 Currents 이벤트 {#supported-currents-events}

Braze는 Currents [사용자 행동]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) 및 [메시지 참여]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) 이벤트 용어집에 나열된 다음 데이터를 Mixpanel로 내보내는 것을 지원합니다:

### 동작 {#behaviors}
- 커스텀 이벤트: `users.behaviors.CustomEvent`
- 설치 경로: `users.behaviors.InstallAttribution`
- 위치: `users.behaviors.Location`
- 구매: `users.behaviors.Purchase`
- 제거: `users.behaviors.Uninstall`
- 앱 (첫 세션, 세션 종료, 세션 시작)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- 구독 (글로벌 상태 변경): `users.behaviors.subscription.GlobalStateChange`
- 구독 그룹 (상태 변경): `users.behaviors.subscriptiongroup.StateChange`

### Campaigns
- 중단: `users_campaigns_abort`
- 전환: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`

### Canvas
- 중단: `users_canvas_abort`
- 전환: `users.canvas.Conversion`
- 진입: `users.canvas.Entry`
- 종료 (일치하는 오디언스, 수행된 이벤트)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- 실험 단계 (전환, 분할 진입)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### 메시지 {#messages}
- 콘텐츠 카드 (중단, 클릭, 닫기, 노출, 발송)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- 이메일 (중단, 반송, 클릭, 전달, 스팸 신고, 열기, 발송, 소프트 반송, 수신 거부)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- 인앱 메시지 (중단, 클릭, 노출)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- 푸시 알림 (중단, 반송, iOS 포그라운드, 열기, 발송)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (중단, 통신사 발송, 전달, 전달 실패, 인바운드 수신, 거부, 발송, 단축 링크 클릭)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- 웹훅 (중단, 발송)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (중단, 전달, 실패, 인바운드 수신, 읽음, 발송)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`

## 문제 해결 {#troubleshooting}

### Mixpanel API 키 및 Braze 외부 ID 확인 {#verify-mixpanel-api-key-and-braze-external-id}

Mixpanel API 키와 `braze_external_id` 값이 Braze와 Mixpanel 양쪽에서 예상한 것과 일치하는지 확인합니다. 코호트 동기화 API는 제품 간에 사용자 그룹을 공유하며, Braze의 `external_id`와 Mixpanel이 전송하는 식별자가 일치하지 않으면 동기화가 올바르게 작동하지 않습니다. Mixpanel의 코호트 동기화는 Mixpanel의 스케줄에 따라 실행됩니다(예: 1회 또는 약 2시간마다). 따라서 확인 사이에 시간을 두세요.

### 구현 상태 확인 {#check-implementation-status}

Mixpanel에서 `braze_external_id`가 구현되어 있는지 확인합니다.

### 사용자 속성정보 직접 설정 {#set-the-user-property-directly}

모호함을 줄이려면 Mixpanel에서 `braze_external_id`를 직접 설정합니다.

### 자동 속성정보 설정 (SDK) {#automatic-property-setting-sdks}

Mixpanel SDK는 동일한 애플리케이션에 Braze SDK가 통합되어 있을 때 `braze_external_id`를 자동으로 설정할 수 있습니다. Mixpanel과 Braze를 함께 구현하는 경우 일반적으로 두 SDK를 모두 설치하는 것 외에 추가 연결 작업이 필요하지 않습니다.

{% alert note %}
`braze_external_id`는 Braze에서 `changeUser()`가 호출될 때 설정되는 것이 아니라, Mixpanel이 초기화되거나 세션을 시작할 때("init" 또는 "start session" 시점)에 설정됩니다.
{% endalert %}