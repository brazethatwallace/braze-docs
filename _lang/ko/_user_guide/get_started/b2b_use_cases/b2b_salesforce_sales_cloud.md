---
nav_title: Salesforce Sales Cloud
article_title: Salesforce Sales Cloud로 리드 관리하기
page_order: 3
page_type: reference
description: "Braze 웹훅을 사용하여 Salesforce sobjects/Lead 엔드포인트를 통해 Salesforce Sales Cloud에서 리드를 생성하고 업데이트하는 방법을 알아보세요."
---

# Salesforce Sales Cloud로 리드 관리하기 {#manage-leads-with-salesforce-sales-cloud}

> [Salesforce](https://www.salesforce.com/)는 리드 생성, 기회 추적, 계정 관리 등 전체 영업 프로세스를 관리할 수 있도록 설계된 세계 최고의 클라우드 기반 고객 관계 관리(CRM) 플랫폼 중 하나입니다.<br><br>이 페이지에서는 커뮤니티에서 제출한 통합을 통해 Braze 웹훅을 사용하여 Salesforce Sales Cloud에서 리드를 생성하고 업데이트하는 방법을 보여줍니다.

{% alert important %}
이 기능은 커뮤니티에서 제출한 통합이며 Braze에서 직접 지원하지 않습니다. Braze에서 제공하는 공식 웹훅 템플릿만 Braze에서 지원합니다.
{% endalert %}

## 작동 방식 {#how-it-works}

Braze와 Salesforce Sales Cloud 통합은 Braze 웹훅을 사용하여 Salesforce [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html) 엔드포인트를 통해 Salesforce Sales Cloud에서 리드를 생성하고 업데이트합니다.

Braze는 현재 다음 사용 사례를 위해 Salesforce Sales Cloud에 두 가지 통합을 제공합니다:
1. [Salesforce Sales Cloud에서 리드 생성하기](#creating-lead)
2. [Salesforce Sales Cloud에서 리드 업데이트하기](#updating-lead)

{% alert note %}
이 통합은 리드 확보 및 육성 노력의 일환으로 Braze에서 Salesforce를 업데이트하기 위한 것입니다. Salesforce에서 Braze로 데이터를 다시 동기화하려면 [B2B 데이터 모델]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models/)을 확인하거나 [기술 파트너]({{site.baseurl}}/partners/home/) 중 한 곳에 문의하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

이 통합을 진행하기 전에 Salesforce 고객지원에서 연결된 앱을 만들 수 있는 권한을 부여받아야 합니다. [Salesforce 고객지원 요청](https://help.salesforce.com/s/articleView?id=005167035&type=1)을 제출하여 요청할 수 있습니다.

Salesforce 고객지원에서 Salesforce Sales Cloud에서 연결된 앱을 만들 수 있는 권한을 부여한 후, Salesforce 설명서의 단계를 따르세요: [OAuth 2.0 클라이언트 자격 증명 흐름에 대해 연결된 앱 구성하기](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

연결된 앱에 필요한 OAuth 설정을 구성할 때 다음을 제외한 모든 OAuth 설정은 기본값과 선택 항목을 그대로 유지합니다:
1. **Enable for device** 흐름을 선택합니다. **Callback URL**은 기본적으로 입력 안내로 설정되므로 비워 둘 수 있습니다.
2. 선택한 **OAuth Scopes**에 **Manage user data via APIs (api)**를 추가합니다.
3. **Enable Client Credentials Flow**를 선택합니다.

## Salesforce Sales Cloud에서 리드 생성하기 {#creating-lead}

고객 참여 플랫폼인 Braze는 랜딩 페이지에서 양식을 작성하는 등의 사용자 흐름을 기반으로 새로운 리드를 생성할 수 있습니다. 이 경우 Braze Salesforce Sales Cloud 웹훅을 사용하여 Salesforce에서 해당 리드를 생성할 수 있습니다.

### 1단계: `client_id` 및 `client_secret` 수집하기 {#step-1-collect-your-client_id-and-client_secret}

1. Salesforce에서 **Platform Tools** > **Apps** > **App Manager**로 이동합니다.
2. 새로 생성한 Braze 앱을 찾아 **View**를 선택합니다.
3. **Consumer Key and Secret** 아래에서 **Manage Consumer Details**를 선택합니다.
4. 결과 페이지에서 **Consumer Key**와 **Consumer Secret**을 기록합니다. **Consumer Key**는 `client_id`이고, **Consumer Secret**은 `client_secret`입니다.

### 2단계: 웹훅 템플릿 설정하기 {#step-2-set-up-your-webhook-template}

템플릿을 사용하면 Braze 플랫폼 전반에서 이 웹훅을 빠르게 재사용할 수 있습니다.

1. Braze에서 **템플릿**으로 이동하여 **웹훅 템플릿**을 선택한 다음 **+ 웹훅 템플릿 만들기**를 선택합니다.
2. 템플릿의 이름을 입력합니다(예: "Salesforce Sales Cloud > Create Lead").
3. **작성** 탭에서 다음 세부 정보를 입력합니다:

#### 웹훅 작성 {#compose-webhook}

| 필드 | 세부 정보 |
| --- | --- |
| 웹훅 URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| HTTP 메서드 | `POST` |
| 요청 본문 | JSON 키/값 쌍 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="웹훅 작성" }

#### 본문 등록정보 키 값 {#body-property-key-values}

Braze에서 Salesforce로 매핑하려는 각 키/값 쌍에 대해 **+ Add New Body Property**를 선택합니다. 원하는 모든 필드를 매핑할 수 있으므로 다음 표는 하나의 예시일 뿐입니다.

| 키 | 값 |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| lastName | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| company | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="본문 등록정보 키 값" }

#### 요청 헤더 {#request-headers}

다음 요청 헤더 각각에 대해 **+ Add New Header**를 선택합니다.

| 키 | 값 |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요청 헤더" }

{: start="4" }
4. **템플릿 저장**을 선택합니다.

![리드를 생성하기 위해 작성된 웹훅 템플릿.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}

## Salesforce Sales Cloud에서 리드 업데이트하기 {#updating-lead}

Salesforce에서 리드를 업데이트하는 Braze Salesforce Sales Cloud 웹훅을 설정하려면 Salesforce Sales Cloud와 Braze 간의 공통 식별자가 필요합니다. 아래 예시에서는 Salesforce `lead_id`를 Braze `external_id`로 사용하지만, `user_alias`를 사용하여 이 작업을 수행할 수도 있습니다. 자세한 내용은 [B2B 데이터]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models/)를 참조하세요.

이 예시에서는 리드가 특정 리드 임계값을 넘은 후 리드의 리드 단계를 "MQL"(마케팅 적격 리드)로 업데이트하는 방법을 구체적으로 보여줍니다. 이는 [B2B 리드 스코어링 워크플로]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring/) 사용 사례의 핵심 부분입니다.

### 1단계: `client_id` 및 `client_secret` 수집하기

1. Salesforce에서 **Platform Tools** > **Apps** > **App Manager**로 이동합니다.
2. 새로 생성한 Braze 앱을 찾아 **View**를 선택합니다.
3. **Consumer Key and Secret** 아래에서 **Manage Consumer Details**를 선택합니다.
4. 결과 페이지에서 **Consumer Key**와 **Consumer Secret**을 기록합니다.
    - **Consumer Key**는 `client_id`이고, **Consumer Secret**은 `client_secret`입니다.

### 2단계: 웹훅 템플릿 설정하기

1. Braze에서 **템플릿**으로 이동하여 **웹훅 템플릿**을 선택한 다음 **+ 웹훅 템플릿 만들기**를 선택합니다.
2. 템플릿의 이름을 입력합니다(예: "Salesforce Sales Cloud > Update Lead to MQL").
3. **작성** 탭에서 다음 세부 정보를 입력합니다:

#### 웹훅 작성

| 필드 | 세부 정보 |
| --- | --- |
| 웹훅 URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| HTTP 메서드 | `PATCH` |
| 요청 본문 | JSON 키/값 쌍 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="웹훅 작성" }

#### 본문 등록정보 키 값

다음 키/값 쌍에 대해 **+ Add New Body Property**를 선택합니다. `Lead_Stage__c`는 예시 이름입니다. Salesforce에서 MQL을 추적하는 데 사용하는 커스텀 필드의 이름이 다를 수 있으므로 이름이 일치하는지 확인하세요.

| 키 | 값 |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="본문 등록정보 키 값" }

#### 요청 헤더

다음 요청 헤더 각각에 대해 **+ Add New Header**를 선택합니다.

| 키 | 값 |
| --- | --- |
| Authorization | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Content-Type | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요청 헤더" }

{: start="4"}
4. **템플릿 저장**을 선택합니다.

![리드를 업데이트하기 위해 작성된 웹훅 템플릿.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## 운영 워크플로에서 이러한 웹훅 사용하기 {#using-these-webhooks-in-an-operational-workflow}

다음과 같이 Braze의 운영 워크플로에 템플릿을 빠르게 추가할 수 있습니다:

1. Salesforce에서 리드를 생성하는 [신규 리드 Campaign](#new-lead)의 일부
2. MQL 임계값을 넘은 사용자를 "MQL"로 업데이트하고 동일한 정보로 Salesforce Sales Cloud를 업데이트하는 [리드 스코어링 Canvas](#lead-scoring)의 일부

### 새로운 리드 Campaign {#new-lead}

사용자가 이메일 주소를 제공할 때 Salesforce에서 리드를 생성하려면 "Update Lead" 웹훅 템플릿을 사용하고 사용자가 이메일 주소를 추가할 때(예: 웹 양식 작성) 트리거되는 Campaign을 만들 수 있습니다.

![액션 기반이며 트리거 동작이 "Add an Email Address"인 Campaign 생성 2단계.]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### MQL(마케팅 적격 리드) 임계값 초과를 위한 리드 스코어링 Canvas {#lead-scoring}

이 웹훅은 [리드 스코어링]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring/#lead-handoff) 사용 사례에서 다루고 있지만, 별도의 웹훅 Campaign을 만드는 대신 리드 스코어링 Canvas 내에서 직접 MQL을 확인하고 Salesforce를 업데이트할 수도 있습니다:

사용자 업데이트에 후속 단계를 추가하여 사용자가 정의한 MQL 임계값을 넘었는지 확인하세요. 임계값을 넘었다면 사용자의 상태를 "MQL"로 업데이트한 다음, 이 웹훅 템플릿을 사용하여 동일한 "MQL" 상태로 Salesforce를 업데이트합니다. Salesforce는 정의된 리드 라우팅 규칙에 따라 이 리드를 적절한 영업 팀으로 라우팅하여 나머지 작업을 처리합니다.

#### MQL 임계값을 통과한 사용자를 확인하는 캔버스 단계 추가하기 {#adding-canvas-step-to-check-for-users-who-passed-the-mql-threshold}

1. 두 그룹으로 **오디언스 경로** 단계를 추가합니다: "MQL Threshold"와 "다른 모든 사용자".
2. "MQL Threshold" 그룹에서 현재 "MQL" 상태가 아니지만(예: `lead_stage`가 "Lead"와 같음) 리드 점수가 정의한 임계값을 초과하는(예: `lead_score`가 50보다 큰) 사용자를 찾습니다. 해당되면 다음 단계로 이동하고, 그렇지 않으면 종료합니다.

![`lead_stage`가 "Lead"와 같고 `lead_score`가 "50"보다 큰 필터가 있는 "MQL Threshold" 오디언스 경로 그룹.]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3. 사용자의 `lead_stage` 속성 값을 "MQL"로 업데이트하는 **사용자 업데이트** 단계를 추가합니다.

![`lead_stage` 속성을 "MQL" 값으로 업데이트하는 "Update to MQL" 사용자 업데이트 단계.]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4. 새 MQL 단계로 Salesforce를 업데이트하는 웹훅 단계를 추가합니다.

![완료된 세부 정보가 포함된 "Update Salesforce" 웹훅 단계.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

이제 Canvas 흐름이 MQL 임계값을 넘은 사용자를 업데이트합니다!

![사용자가 MQL 임계값을 통과하는지 확인하고, 통과할 경우 Salesforce를 업데이트하는 Canvas 사용자 업데이트 단계.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## 문제 해결 {#troubleshooting}

이러한 워크플로는 Salesforce 내에서 디버깅 기능이 제한되어 있으므로 Braze [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/#message-activity-log)를 참조하여 웹훅이 실패한 이유와 오류 발생 여부를 확인하는 것이 좋습니다.

예를 들어, OAuth 토큰 검색에 사용된 잘못된 URL로 인한 오류는 `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL`로 표시됩니다.

![URL이 유효한 URL이 아님을 나타내는 오류 응답 본문.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})