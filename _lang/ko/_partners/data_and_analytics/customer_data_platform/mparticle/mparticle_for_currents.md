---
nav_title: mParticle for Currents
article_title: mParticle for Currents
alias: /partners/mparticle_for_currents/
description: "이 참조 문서에서는 Braze 커런츠와 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 mParticle 간의 파트너십에 대해 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle for Currents

> [mParticle](https://www.mparticle.com)은 여러 소스에서 정보를 수집하여 마케팅 스택의 다양한 위치로 라우팅하는 고객 데이터 플랫폼입니다.

Braze와 mParticle 통합을 통해 두 시스템 간의 정보 흐름을 원활하게 제어할 수 있습니다. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)를 사용하면 데이터를 mParticle에 연결하여 전체 성장 스택에서 활용할 수도 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Currents | 데이터를 mParticle로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. |
| mParticle 계정 | 이 파트너십을 활용하려면 [mParticle 계정](https://app.mparticle.com/login)이 필요합니다. |
| mParticle 서버 간 키 및 시크릿 | mParticle 대시보드로 이동하여 mParticle이 iOS, Android 및 웹 플랫폼에 대한 Braze 상호작용 데이터를 수신할 수 있도록 [필요한 피드](#step-1-create-feeds)를 생성하면 얻을 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## mParticle 자격 증명 정보 {#about-mparticle-credentials}

mParticle에는 이벤트 전송 방식에 영향을 미치는 앱 수준 및 워크스페이스 수준 자격 증명이 있습니다.

- **앱 수준:** mParticle은 각 개별 앱별로 이벤트를 분리합니다. 즉, iOS 앱에 제공한 앱 수준 자격 증명은 iOS 전용 이벤트를 전송하는 데만 사용할 수 있습니다.
- **워크스페이스 수준:** mParticle은 앱별이 **아닌** 모든 이벤트를 함께 그룹화합니다. 즉, 앱 그룹에 제공한 워크스페이스 수준 자격 증명은 앱별이 아닌 모든 이벤트를 전송하는 데 사용됩니다.

mParticle이 각 개별 앱을 기반으로 "피드"를 수집한다고 생각하면 됩니다. 예를 들어, iOS용 앱 하나, Android용 앱 하나, 웹용 앱 하나가 있는 경우 이벤트가 분리됩니다. 즉, 각 앱에 동일한 자격 증명을 제공하면 하나의 mParticle 피드가 모든 앱의 모든 데이터를 중복 없이 수신하는 데 사용됩니다.

## 통합 {#integration}

### 1단계: 피드 생성 {#step-1-create-feeds}

mParticle 관리자 계정에서 **Setup > Inputs**로 이동합니다. mParticle **Directory**에서 **Braze**를 찾아 피드 통합을 추가합니다.

Braze 피드 통합은 iOS, Android, 웹, 언바운드의 네 가지 별도 피드를 지원합니다. 언바운드 피드는 플랫폼에 연결되지 않은 이메일과 같은 이벤트에 사용할 수 있습니다. 각 주요 플랫폼 피드에 대한 입력을 생성해야 합니다. **Setup > Inputs**의 **Feed Configurations** 탭에서 추가 입력을 생성할 수 있습니다.

![]({% image_buster /assets/img/braze-feed-inputs.png %})

각 피드에 대해 **Act as Platform**에서 목록에서 일치하는 플랫폼을 선택합니다. **act-as** 피드를 선택하는 옵션이 표시되지 않으면 데이터는 언바운드로 처리되지만 데이터 웨어하우스 출력으로 전달할 수 있습니다.

![구성 이름을 입력하고, 피드 상태를 결정하고, 작동할 플랫폼을 선택하라는 첫 번째 통합 대화 상자.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![서버 간 키와 서버 간 시크릿을 보여주는 두 번째 통합 대화 상자.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

각 입력을 생성하면 mParticle에서 키와 시크릿을 제공합니다. 이 자격 증명을 복사하고 각 자격 증명 쌍이 어떤 피드용인지 기록해 두세요.

### 2단계: Current 생성 {#step-2-create-current}

Braze에서 **Currents > + Create Current > Create mParticle Export**로 이동합니다. 통합 이름, 연락처 이메일, 각 플랫폼의 mParticle API 키와 mParticle 시크릿 키를 입력합니다. 그런 다음 추적할 이벤트를 선택합니다. 사용 가능한 이벤트 목록이 제공됩니다. 마지막으로 **Launch Current**을 클릭합니다.

![Braze의 mParticle Currents 페이지. 여기에서 통합 이름, 연락처 이메일, API 키 및 시크릿 키 필드를 찾을 수 있습니다.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
mParticle API 키와 mParticle 시크릿 키를 최신 상태로 유지하는 것이 중요합니다. 커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중지합니다. 이 상태가 **5일** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

mParticle로 전송되는 모든 이벤트에는 사용자의 `external_user_id`가 `customerid`로 포함됩니다. 현재 Braze는 `external_user_id`가 설정되지 않은 사용자에 대한 이벤트 데이터를 전송하지 않습니다. `external_user_id`를 mParticle에서 기본 `customerid`가 아닌 다른 ID에 매핑하려면 Braze 고객 성공 매니저에게 문의하세요.

## 지원되는 Currents 이벤트 {#supported-currents-events}

Braze는 Currents [사용자 행동]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) 및 [메시지 참여]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) 이벤트 용어집에 나열된 다음 데이터를 mParticle로 내보내는 것을 지원합니다.

### 동작 {#behaviors}
- 제거: `users.behaviors.Uninstall`
- 구독(글로벌 상태 변경): `users.behaviors.subscription.GlobalStateChange`
- 구독 그룹(상태 변경): `users.behaviors.subscriptiongroup.StateChange`

### Campaigns
- 중단: `users_campaigns_abort`
- 전환: `users.campaigns.Conversion`
- 컨트롤 등록: `users.campaigns.EnrollInControl`

### Canvas
- 중단: `users_canvas_abort`
- 전환: `users.canvas.Conversion`
- 진입: `users.canvas.Entry`
- 종료(일치하는 오디언스, 수행된 이벤트)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- 실험 단계(전환, 분할 진입)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### 메시지 {#messages}
- 콘텐츠 카드(중단, 클릭, 닫기, 노출, 전송)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- 이메일(중단, 반송, 클릭, 전달, 스팸 신고, 열기, 전송, 소프트 반송, 구독 취소)
- 인앱 메시지(중단, 클릭, 노출)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- 푸시 알림(중단, 반송, 열기, 전송)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS(중단, 통신사 전송, 전달, 전달 실패, 인바운드 수신, 거부, 전송, 단축 링크 클릭)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- 웹훅(중단, 전송)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp(중단, 전달, 실패, 인바운드 수신, 읽음, 전송)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`


mParticle 통합에 대해 자세히 알아보려면 [여기](http://docs.mparticle.com/integrations/braze/feed)에서 해당 설명서를 참조하세요.