---
nav_title: API 캠페인
article_title: API 캠페인
page_order: 5
description: "이 참조 문서에서는 API 호출에 포함할 campaign_id를 생성하는 방법과 해당 캠페인을 구성하는 방법에 대해 설명합니다."
page_type: reference
tool: Campaigns

---
# API 캠페인 {#api-campaigns}

> 이 참조 문서에서는 API 호출에 포함할 `campaign_id`를 생성하는 방법과 해당 캠페인을 구성하는 방법에 대해 설명합니다.

API 캠페인은 일반적으로 트랜잭션 메시징에 사용됩니다. API 캠페인([API 트리거 캠페인]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)이 아닌)을 생성할 때, Braze 대시보드는 캠페인 보고를 위한 분석을 추적할 수 있는 `campaign_id`를 생성하는 데만 사용됩니다. 캠페인의 각 배리언트마다 다른 메시지 배리언트 ID를 생성할 수도 있습니다.

그런 다음 해당 정보를 개발팀에 전달하여 API 요청에 사용할 수 있도록 합니다. 전달할 정보는 다음과 같습니다.
- 캠페인 카피
- 오디언스 멤버십
- 자산

캠페인이 시작되면 대시보드에서 결과를 확인할 수 있습니다. API 캠페인은 대시보드를 통해 완전히 생성된 캠페인과 동일한 세부 보고 및 리타겟팅 옵션이 있는 Braze [메시징 API]({{site.baseurl}}/api/endpoints/messaging)를 사용합니다.

{% alert warning %}
API 캠페인은 일반적으로 트랜잭션이므로 글로벌 컨트롤 그룹에 속한 사용자를 포함하여 모든 사용자가 API 캠페인을 수신할 수 있습니다. 이러한 발송에는 [원클릭 목록 수신 거부]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings#list-unsubscribe) 헤더가 추가되지 않습니다. 모든 API 캠페인에 원클릭 목록 수신 거부 헤더를 추가하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 새 Campaign 만들기 {#create-a-new-campaign}

**메시징** > **Campaigns**로 이동하여 **Campaign 만들기**를 선택한 다음 **API Campaigns**를 선택합니다. 이제 API Campaign 구성을 진행할 수 있습니다.

[API 트리거 Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)은 API Campaign과 다릅니다.

## Campaign 구성하기 {#configure-your-campaign}

Campaign을 구성하려면 다음 단계를 수행합니다:

1. 메시지를 보낸 후 Campaigns 페이지에서 결과를 찾을 수 있도록 설명이 포함된 제목을 추가합니다.
2. **Add Message**를 선택하고 API Campaign에 포함할 메시지 유형을 추가합니다. 이렇게 하면 `campaign_id`와 메시지 배리언트 ID가 생성되며, 포함하는 각 채널마다 다른 값이 부여됩니다.
3. 선택 사항으로, 특정 액션이나 Campaign 목표에 대한 사용자 전환을 추적하기 위해 전환 이벤트를 추가할 수 있습니다.
4. **Save Campaign**을 선택하면 API Campaign을 시작할 준비가 완료됩니다!

## API 호출 {#api-calls}

API Campaign을 저장한 후 API 요청에 다음을 포함합니다:
- [메시지 전송 엔드포인트]({{site.baseurl}}/api/endpoints/messaging)에 명시된 대로 생성된 `campaign_id` 필드를 API 요청에 포함합니다.
- Campaign에 포함된 각 플랫폼에 대한 [메시지 오브젝트]({{site.baseurl}}/api/objects_filters#messaging-objects)를 포함합니다. 메시지 오브젝트에서 메시지 배리언트 ID를 제공합니다. 이렇게 하면 해당 배리언트 아래에 통계가 수집되고 표시됩니다. 지원되는 메시지 오브젝트는 Android, Content Cards, 이메일, iOS, Kindle, SMS/MMS, 웹 푸시, 웹훅입니다.

### 이메일 첨부 파일 추가 {#adding-email-attachments}

API Campaign 이메일에 첨부 파일을 추가하려면 [이메일 오브젝트]({{site.baseurl}}/api/objects_filters/messaging/email_object)에 `attachments` 배열을 포함합니다. 드래그 앤 드롭 또는 HTML 편집기에서 생성한 이메일 템플릿을 참조하려면 이메일 오브젝트에 `email_template_id`를 제공한 다음 API 호출을 통해 첨부 파일을 추가할 수 있습니다.

첨부 파일 세부 정보, 크기 제한 및 모범 사례에 대해서는 [첨부 파일이 포함된 이메일 오브젝트 예시]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment)를 참조하세요.