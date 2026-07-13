---
nav_title: "트랜잭션 이메일 생성"
article_title: "트랜잭션 이메일 생성"
page_order: 1

description: "이 참조 문서에서는 새로운 Braze 트랜잭션 이메일 캠페인을 생성하고 구성하는 방법을 다룹니다."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# 트랜잭션 이메일 생성 {#create-a-transactional-email}

> Braze 트랜잭션 이메일은 발신자와 수신자 간에 합의된 트랜잭션을 처리하기 위해 발송됩니다. 이 참조 문서에서는 Braze 대시보드에서 트랜잭션 이메일 캠페인을 생성하고, API 호출에 포함할 `campaign_id`를 생성하는 방법을 다룹니다. 자세한 내용은 [`/transactional/v1/campaigns/{campaign_id}/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)를 참조하세요.

{% alert important %}
Braze 트랜잭션 이메일은 특정 Braze 패키지의 일부로만 제공됩니다. 자세한 내용은 Braze 고객 성공 매니저에게 문의하거나 [고객지원 티켓]({{site.baseurl}}/braze_support)을 열어 주세요.
{% endalert %}

트랜잭션 이메일 캠페인 유형은 귀하와 고객 간에 합의된 트랜잭션을 처리하기 위해 자동화된 비프로모션 이메일 메시지를 발송하도록 특별히 설계되었습니다. 여기에는 다음과 같은 정보가 포함됩니다:

- 주문 확인
- 비밀번호 재설정
- 결제 알림
- 배송 알림

간단히 말해, 트랜잭션 이메일은 속도가 가장 중요한 경우 서비스에서 발생하는 비즈니스 크리티컬 알림을 단일 사용자에게 발송하는 데 사용할 수 있습니다.

{% alert important %}
트랜잭션 이메일은 추가 비용 없이 사용자를 타겟팅하는 데 사용할 수 있는 트랜잭션 Campaign(캠페인)과 다릅니다. 예를 들어, 트랜잭션 Campaign에는 사용자가 장바구니에 항목을 추가한 후 발송되는 메시지가 포함될 수 있습니다. 자세한 내용은 [오디언스 타겟팅 옵션]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)을 확인하세요.
{% endalert %}

{% alert note %}
트랜잭션 이메일 API 발송은 메시지 아카이브를 지원합니다. 워크스페이스에서 이메일에 대한 메시지 아카이브가 활성화된 경우, Braze는 각 트랜잭션 이메일 발송의 렌더링된 사본을 저장합니다. 자세한 내용은 [메시지 아카이브]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving)를 참조하세요.
{% endalert %}

## 1단계: 새 캠페인 생성 {#step-1-create-a-new-campaign}

새 트랜잭션 이메일 캠페인을 생성하려면 캠페인을 생성하고 메시징 채널로 **트랜잭션 이메일**을 선택합니다.

![트랜잭션 이메일 옵션이 강조 표시된 캠페인 생성 드롭다운.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

이제 트랜잭션 이메일 캠페인 구성을 진행할 수 있습니다.

## 2단계: 캠페인 구성 {#step-2-configure-your-campaign}

트랜잭션 이메일 캠페인의 생성 흐름은 [표준 이메일 캠페인]({{site.baseurl}}/user_guide/channels/email/html_editor)에 비해 간소화되어 비즈니스 크리티컬 트랜잭션 이메일이 모든 사용자에게 도달할 수 있도록 합니다.

따라서 다른 Braze 캠페인 유형에서 익숙할 수 있는 여러 설정이 이 캠페인 유형을 설정할 때 필요하지 않습니다:

- **전달** 단계에서 예약 옵션이 제거되어 간소화되었습니다. 트랜잭션 이메일은 항상 **전달** 페이지에 표시된 캠페인 ID를 사용하여 Braze REST API를 통해 트리거됩니다. 재자격 제어 및 최대 게재빈도 설정과 같은 추가 설정도 제거되어, 서비스가 발송 요청을 트리거할 때 모든 사용자가 이러한 중요한 트랜잭션 알림을 받을 수 있도록 합니다.
- **타겟 오디언스** 단계가 제거되었습니다. 트랜잭션 이메일은 전체 사용자 기반(탈퇴한 사용자 포함)을 대상으로 등록하므로 필터나 Segments를 지정할 필요가 없습니다. 따라서 이 메시지를 받을 대상에 적용할 로직이 있는 경우, 특정 사용자에게 메시지를 트리거하기 위해 Braze에 API 요청을 보내기 전에 해당 로직을 적용하는 것을 권장합니다.
- **전환** 단계가 제거되었습니다. 트랜잭션 이메일은 현재 전환 이벤트 추적을 지원하지 않습니다.

![트랜잭션 이메일 캠페인을 생성하기 위한 작성, 전달, 확인 워크플로.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

트랜잭션 이메일 캠페인을 구성하려면 다음 단계를 따르세요:

1. 메시지를 발송한 후 **Campaigns** 페이지에서 결과를 찾을 수 있도록 설명적인 이름을 추가합니다.
2. 이메일을 작성하거나 템플릿에서 선택합니다.
3. `campaign_id`를 기록해 둡니다. API 캠페인을 저장한 후, 생성된 `campaign_id` 필드를 [트랜잭션 이메일 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) 문서에 명시된 대로 API 요청에 포함해야 합니다.
4. **캠페인 저장**을 클릭하면 API 캠페인을 시작할 준비가 완료됩니다!

{% alert note %}
트랜잭션 이메일 캠페인의 원클릭 목록 탈퇴 설정은 다른 이메일 캠페인과 마찬가지로 **워크스페이스 기본값 사용**으로 기본 설정됩니다. 이것은 트랜잭션 메시징을 위한 것이므로 Braze는 원클릭 탈퇴를 추가하지 않습니다. 이 캠페인 유형에 원클릭 탈퇴를 추가하려면 **발송 정보**에서 [이 설정을 편집]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#message-level-one-click-list-unsubscribe)하세요.
{% endalert %}

### 트랜잭션 이메일에서 허용되지 않는 태그 {#disallowed-tags-in-transactional-emails}

`Connected Content` 및 `Promotion Code` Liquid 태그는 트랜잭션 이메일 캠페인 내에서 사용할 수 없습니다.

`Connected Content` 태그를 사용하면 발송 프로세스 중에 Braze가 외부 API 요청을 수행해야 하며, 요청하는 외부 서비스에 지연이 발생하면 메시지 발송 프로세스가 느려질 수 있습니다. 마찬가지로 `Promotion Code` 태그는 발송 전에 프로모션의 가용성을 평가하기 위해 Braze가 추가 처리를 수행해야 하며, 프로모션을 사용할 수 없는 경우 발송 프로세스가 느려질 수 있습니다.

따라서 트랜잭션 이메일 캠페인의 어떤 필드에도 `Connected Content` 또는 `Promotion Code` 태그를 포함하는 것을 지원하지 않습니다.