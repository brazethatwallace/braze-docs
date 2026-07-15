---
nav_title: 리드 스코어링
article_title: 리드 스코어링 워크플로 생성
page_order: 1
page_type: reference
description: "Braze를 사용하여 간단한 리드 스코어링, 외부 리드 스코어링 및 리드 핸드오프를 수행하는 방법을 알아보세요."
---

# 리드 스코어링 워크플로 생성 {#create-a-lead-scoring-workflow}

> 이 사용 사례는 Braze를 사용하여 실시간으로 사용자 리드 점수를 업데이트하고 자동으로 리드를 영업 팀에 전달하는 방법을 보여줍니다.

Braze에서 리드 스코어링 워크플로를 만드는 두 가지 주요 단계가 있습니다.

1. Braze에서 리드 스코어링 Canvas를 만들거나 외부 리드 스코어링 도구를 통합합니다.
- [간단한 리드 스코어링](#simple-lead-scoring)
- [외부 리드 스코어링](#external-lead-scoring)

2. 웹훅 Campaign을 만들어 자격을 갖춘 리드를 영업 팀에 전달합니다.
- [리드 핸드오프: 마케팅 적격 리드(MQL)에서 영업으로](#lead-handoff)

## 간단한 리드 스코어링 {#simple-lead-scoring}

### 1단계: Canvas 만들기 {#step-1-create-a-canvas}

1. **메시징** > **Canvas**로 이동하여 **Canvas 만들기**를 선택한 다음 Canvas 기본 사항을 입력합니다.

2. Canvas에 "Lead Scoring Canvas"와 같은 관련 이름을 지정하고, 검색 편의를 위해 "Lead Management"와 같은 태그를 지정하세요.<br><br>![Canvas 이름을 "Lead Scoring Canvas"로 하고 태그를 "Lead Management"로 하여 Canvas를 만드는 1단계.]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### 2단계: 진입 기준 설정 {#step-2-set-up-your-entry-criteria}

1. **진입 스케줄** 단계로 이동하여 **행동 기반** 진입 스케줄을 선택합니다. 사용자가 특정 동작을 수행하면 Canvas에 진입하게 됩니다.

2. **행동 기반 옵션**에서 다음 두 가지 동작을 추가합니다.
    - 리드 스코어링 속성 이름(예: `lead score`)으로 **커스텀 속성 값 변경**. 아직 리드 스코어링 속성을 만들지 않았다면 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)의 단계를 따르세요. 이렇게 하면 리드 점수가 변경될 때마다 사용자가 Canvas에 진입합니다.
    - **이메일 주소 추가**

!["행동 기반" 진입 스케줄과 커스텀 속성 "lead score" 변경 및 이메일 주소 추가의 행동 기반 옵션으로 Canvas를 만드는 2단계.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### 3단계: 타겟 오디언스 식별 {#step-3-identify-your-target-audience}

#### 3a단계: Segments 선택 {#step-3a-select-segments}

모든 사용자가 리드 스코어링 대상이므로, 타겟팅할 사용자 [Segments]({{site.baseurl}}/user_guide/audience/segments)를 선택하고 추가 [필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 적용하여 회사별 규칙을 추가할 수 있습니다. 예를 들어, 직원, 이미 고객인 사용자 등을 제외할 수 있습니다.

![Segments와 필터를 선택하여 진입 오디언스를 좁히는 옵션이 있는 Canvas 생성 3단계.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### 3b단계: Canvas 재진입 자격 설정 {#step-3b-set-canvas-re-eligibility}

사용자는 라이프사이클 동안 이 Canvas를 여러 번 거치게 되므로, 이전에 나간 것만큼 빠르게 다시 진입할 수 있도록 해야 합니다. 이는 재진입 자격 설정을 통해 달성할 수 있습니다.

**진입 제어**에서 다음을 수행합니다.
- **사용자가 이 Canvas에 다시 진입할 수 있도록 허용**을 선택합니다.
- **지정된 기간**을 선택합니다.
- 재진입 자격을 "0" **초**로 설정합니다.

!["진입 제어" 섹션에서 "지정된 기간" 0초 동안 "사용자가 이 Canvas에 다시 진입할 수 있도록 허용"이 선택되어 있습니다.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### 3c단계: 발송 설정 업데이트 {#step-3c-update-send-settings}

이 Canvas의 운영 특성과 사용자에게 메시지가 발송되지 않는다는 점을 감안하면, 구독 상태를 준수할 필요가 없습니다.

**구독 설정**에서 **이 사용자에게 보내기:** **구독 취소한 사용자를 포함한 모든 사용자**를 선택합니다.

![메시지 발송 옵션을 설정하는 Canvas 생성 4단계.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### 4단계: Canvas 구축 {#step-4-build-your-canvas}

#### 4a단계: 행동 경로 추가 {#step-4a-add-an-action-path}

배리언트 아래에서 <i class="fas fa-plus" aria-label="추가"></i> **추가**를 선택한 다음 **행동 경로**를 선택합니다.

![더하기 아이콘으로 열린 메뉴에 "행동 경로"가 표시된 Canvas.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### 4b단계: 행동 그룹 만들기 {#step-4b-create-action-groups}

각 행동 그룹은 동일한 포인트 증가 또는 감소로 이어지는 모든 동작을 나타냅니다. 최대 8개의 행동 그룹을 설정할 수 있습니다. 이 시나리오에서는 네 개의 그룹을 설정합니다.

다음 그룹을 행동 경로에 추가합니다.

- **그룹 1:** 1점 증가에 해당하는 모든 이벤트.
- **그룹 2:** 5점 증가에 해당하는 모든 이벤트.
- **그룹 3:** 1점 감소에 해당하는 모든 이벤트.
- **다른 모든 사용자:** 행동 경로를 사용하면 사용자가 동작을 수행하는지 확인하기 위해 기다리는 기간을 정의한 후, "다른 모든 사용자" 그룹으로 분류할 수 있습니다. 리드 스코어링의 경우, 이는 "비활동"에 대해 점수를 감소시킬 수 있는 기회입니다.

![1점, 5점, 10점 추가, 1점과 10점 차감, "다른 모든 사용자"에 대한 행동 그룹을 포함하는 행동 경로.]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### 4c단계: 각 그룹에 관련 이벤트를 포함하도록 구성 {#step-4c-configure-each-group-to-include-the-relevant-events}

각 행동 그룹에서 **트리거 선택**을 선택하고 해당 행동 그룹에 대한 포인트 수를 추가할 이벤트를 선택합니다. 리드 점수를 1점씩 증가시키는 모든 이벤트를 포함하도록 트리거를 추가하세요. 예를 들어, 사용자가 앱에서 세션을 시작하거나 커스텀 이벤트(예: 등록 또는 웨비나 참여)를 수행할 때 점수를 1점 올릴 수 있습니다.

!["모든 앱에서 세션 시작" 및 "커스텀 이벤트 수행" 트리거가 있는 포인트 추가용 행동 그룹.]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### 4d단계: 사용자 업데이트 단계 추가 {#step-4d-add-user-update-steps}

행동 경로에서 생성된 각 Canvas 경로에 사용자 업데이트 단계를 추가합니다.

![각 행동 그룹에 대한 분기된 사용자 업데이트 경로가 있는 행동 경로를 표시하는 Canvas.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start="2"}
각 사용자 업데이트 단계의 **작성** 탭에서 해당 필드에 대해 다음을 수행합니다.

| 필드 | 동작 |
| --- | --- |
| **Attribute Name** | 2단계에서 선택한 리드 점수 속성(`lead score`)을 선택합니다. |
| **Action** | 경로가 점수를 증가시키면 **Increment By**로, 경로가 점수를 감소시키면 **Decrement By**로 변경합니다. |
| **Increment By** 또는 **Decrement By** | 리드 점수에서 증가하거나 감소할 포인트 수를 입력합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="4d단계: 사용자 업데이트 단계 추가" }

### 5단계: Canvas 시작 {#step-5-launch-your-canvas}

이것으로 끝입니다! 리드 스코어링 Canvas를 시작할 준비가 되었습니다.

## 외부 리드 스코어링 {#external-lead-scoring}

[기술 파트너]({{site.baseurl}}/partners/home), 자체 내부 리드 스코어링 모델, 머신 러닝 또는 다른 리드 스코어링 도구를 사용하든, 여러 가지 옵션이 있습니다.

### 외부 파트너 {#external-partners}

[기술 파트너]({{site.baseurl}}/partners/home)를 확인하여 리드 스코어링 기능을 제공하는 B2B 파트너에 대해 알아보세요. 원하는 도구가 보이지 않나요? [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users) API 엔드포인트를 호출하여 통합할 수 있습니다.

### 내부 리드 스코어링 데이터 모델 {#internal-lead-scoring-data-models}

Braze를 리드 스코어링 모델을 포함한 내부 데이터 모델과 다양한 방식으로 통합할 수 있습니다. 아래에서 고객들이 Braze와 통합한 일반적인 예시를 확인하세요.

#### 통합 클라우드 데이터 웨어하우스 {#integrated-cloud-data-warehouse}

{% tabs %}
{% tab 데이터 소스로서의 Braze %}

마케팅 도구로서 Braze는 팀의 내부 리드 스코어 모델을 보완할 수 있는 매우 관련성 높은 데이터를 포함하고 있습니다.

예를 들어, 메시징 인게이지먼트 데이터(예: 이메일 열람 및 클릭, 랜딩 페이지 참여 등)는 리드의 참여 수준을 결정할 수 있습니다. Braze 스트리밍 내보내기 데이터 솔루션을 사용하여 이 데이터를 클라우드 데이터 웨어하우스로 다시 전달하고 리드 스코어링 모델의 입력으로 사용할 수 있습니다.

- [Braze 커런츠]({{site.baseurl}}/user_guide/data/distribution/braze_currents)
- [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

{% endtab %}
{% tab 대상으로서의 Braze %}

내부 팀이 리드 스코어링 모델을 생성하고 실행한 후, 해당 데이터를 Braze로 다시 가져와서 관련 메시징을 위해 리드를 더 잘 세분화하고 타겟팅할 수 있습니다. [Braze 클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 사용하면 됩니다.

클라우드 데이터 수집을 통해 내부 팀은 사용자 식별자, 최신 리드 점수 및 점수가 업데이트된 타임스탬프가 포함된 새 테이블 또는 뷰를 생성합니다. Braze가 테이블 또는 뷰를 가져와서 리드 점수를 고객 프로필에 추가합니다.

{% endtab %}
{% endtabs %}

## 리드 핸드오프: 마케팅 적격 리드(MQL)에서 영업으로 {#lead-handoff}

리드 핸드오프에 대한 권장 접근 방식은 Braze의 각 사용자에게 해당 리드 또는 연락처를 연결하는 것입니다. 이 리드는 리드 상태가 MQL 단계로 변경되면 영업 팀의 대기줄에 들어가며, 이 시점에서 Salesforce가 리드 라우팅 또는 할당 워크플로를 시작합니다.

Braze의 리드 상태로 Salesforce의 리드 레코드를 업데이트하려면 트리거된 웹훅 템플릿을 사용하는 것을 권장합니다.

### 1단계: 웹훅 Campaign 생성 {#step-1-create-a-webhook-campaign}

### 2단계: 웹훅 구성 {#step-2-configure-your-webhook}

#### 2a단계: 웹훅 작성 {#step-2a-compose-webhook}

1. 웹훅 Campaign에 "Salesforce > MQL로 리드 업데이트"와 같은 이름을 지정합니다.

2. {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} 형식으로 웹훅 URL을 입력합니다. {% raw %}`{{${user_id}}}`{% endraw %}의 Braze 사용자 ID는 Salesforce 연락처 ID와 일치해야 합니다. 일치하지 않으면 {% raw %}`{{${user_id}}}`{% endraw %} 대신 별칭을 사용하세요.

3. **HTTP Method**를 **PATCH**로 업데이트합니다.

4. 리드의 리드 점수가 미리 정의된 임계값을 초과하는 경우에만 Salesforce에서 리드 레코드를 업데이트하도록 페이로드를 구성합니다. 리드 점수가 100보다 큰 경우의 예시 요청 본문을 아래에서 확인하세요.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5. 다음 헤더를 포함합니다.

| 헤더 | 콘텐츠 |
| --- | --- |
| Authorization | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>토큰을 가져오려면 OAuth 2.0 클라이언트 자격 증명 흐름에 대해 [연결된 앱을 구성](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5)한 다음 연결된 콘텐츠를 사용하여 Salesforce에서 베어러를 가져옵니다. <br><br>{% raw %}<code>{% connected_content https://[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content-Type | application/json |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2a단계: 웹훅 작성" }

![Salesforce 웹훅 URL, PATCH HTTP 메서드, 원시 텍스트 요청 본문 및 요청 헤더로 구성되는 웹훅.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### 2b단계: 웹훅 발송 예약 {#step-2b-schedule-webhook-sends}

이 Campaign은 사용자의 리드 점수가 변경될 때마다 트리거되어야 합니다. 이 Campaign은 점수가 변경된 모든 사용자에 대해 트리거되지만, 현재 MQL이 아니고 이전 단계에서 설정한 임계값을 초과한 사용자에게만 영향을 미칩니다.

**배달 예약** 단계에서 다음을 선택합니다.
- **행동 기반** 전달 유형
- 리드 스코어링 속성 이름과 **새로운 값** 동작으로 **커스텀 속성 값 변경** 트리거 동작

#### 2c단계: 타겟 오디언스 식별 {#step-2c-identify-target-audience}

**타겟 오디언스** 단계에서 리드 상태가 이미 MQL 이상인 사용자를 제외하는 필터를 포함합니다. 예를 들어 "`lead_status` `is none of` `MQL`"과 같습니다.

!["lead_status"가 "MQL"이 아닌 필터가 적용된 웹훅 타겟팅 옵션.]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### 3단계: Campaign 시작 {#step-3-launch-campaign}

**시작**을 선택하고 고객이 MQL 리드 점수 임계값을 초과할 때 Salesforce에서 리드 상태가 변경되는 것을 확인하세요.