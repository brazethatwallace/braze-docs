---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "이 참조 문서에서는 모바일, 웹 및 대체 데이터를 다른 서드파티 소스에 연결할 수 있는 범용 데이터 허브인 Tealium과 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/)은 옴니채널 고객 세분화 및 실시간 동작 엔진입니다. AudienceStream은 EventStream으로 유입되는 데이터를 가져와 브랜드에 대한 고객 인게이지먼트의 가장 중요한 속성을 나타내는 방문자 프로필을 생성합니다.

Braze와 Tealium 통합은 AudienceStream 방문자 프로필을 활용합니다. 공유된 행동은 이러한 프로필을 세분화하여 공통 특성을 가진 방문자 집합(오디언스)을 생성합니다. 이러한 오디언스는 커넥터를 통해 실시간으로 기술적 마케팅 스택을 지원할 수 있습니다.

{% alert important %}
Tealium AudienceStream과 EventStream은 배치 및 비배치 커넥터 동작을 모두 제공합니다. 비배치 커넥터는 실시간 요청이 사용 사례에 중요하고 Braze API 사용량 제한 사양에 도달하는 것에 대한 우려가 없을 때 사용해야 합니다. 질문이 있으시면 Braze [고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support) 또는 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 사전 요구 사항 {#prerequisites}

| 이름 | 설명 |
| ---- | ----------- |
| Tealium 계정 | 서버 측 액세스가 가능한 [Tealium 계정](https://my.tealiumiq.com/)이 필요합니다. 이 파트너십을 최대한 활용하려면 클라이언트 측 통합도 함께 사용하는 것을 권장합니다. |
| REST API 키 | `users.track`, `users.delete`, `subscription.status.set` 권한이 있는 Braze REST API 키.<br><br>이 키는 **Braze 대시보드 > 개발자 콘솔 > REST API 키 > 새 API 키 생성**에서 생성할 수 있습니다. |
| [Braze REST 엔드포인트]({{site.baseurl}}/api/basics#endpoints) | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/api/basics#endpoints)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## 통합 {#integration}

### 1단계: 속성 및 배지 설정 {#step-1-set-up-attributes-and-badges}

#### 속성 이해하기 {#understanding-attributes}

AudienceStream 사용의 첫 번째 단계는 속성을 생성하는 것입니다. 속성을 사용하면 방문자의 습관, 선호도, 행동, 브랜드 인게이지먼트를 나타내는 중요한 특성을 정의할 수 있습니다.

**방문 속성**: 방문 속성은 사용자의 현재 방문(또는 세션)과 관련됩니다. 이러한 속성에 저장된 데이터는 방문 기간 동안 유지됩니다. 방문 속성의 예시는 다음과 같습니다:
- 방문 기간 (숫자)
- 현재 브라우저 (문자열)
- 현재 기기 (문자열)
- 페이지 조회수 (숫자)

**방문자 속성**: 방문자 속성은 현재 사용자와 관련됩니다. 이러한 속성에 저장된 데이터는 사용자의 수명 기간 동안 유지됩니다. 방문자 속성의 예시는 다음과 같습니다:
- 전체 주문 금액 (숫자)
- 이름 (문자열)
- 생년월일 (날짜)
- 구매 브랜드 (집계)

사용 가능한 데이터 유형의 전체 목록은 [Tealium](https://docs.tealium.com/server-side/attributes/about/)을 참조하세요.

##### 속성 보강 {#attribute-enrichment}

원하는 속성을 식별한 후에는 [보강(enrichments)](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/)으로 속성을 구성할 수 있습니다. 보강은 속성 값을 언제, 어떻게 업데이트할지 결정하는 비즈니스 규칙입니다. 각 데이터 유형은 속성 값을 조작하기 위한 고유한 보강 옵션을 제공합니다. 이것은 "WHEN" 설정과 연관됩니다. 각 방문 및 방문자 속성에 대해 다음 옵션을 사용할 수 있습니다:

- New Visitor: 방문자가 사이트를 처음 방문할 때 발생합니다.
- New Visit: 방문자가 새로 방문할 때 발생합니다.
- Any Event: 모든 이벤트에서 발생합니다.
- Visit Ended: 방문이 종료될 때 발생합니다.

보강이 언제 발생할지를 결정하는 규칙이라는 커스텀 조건을 만들 수도 있습니다.

#### 배지 {#badges}

배지는 가치 있는 행동 패턴을 나타내는 특별한 방문자 속성입니다. 배지는 보강 로직에 따라 방문자에게 할당되거나 제거됩니다. 이 로직은 일반적으로 방문자 세그먼트를 캡처하기 위해 여러 조건을 결합하거나 특정 값에 도달할 때의 임계값을 설정합니다.

#### 속성 및 배지 예시 {#attribute-and-badge-example}

{% tabs local %}
{% tab 속성 %}

고객의 모든 완료된 주문(구매 이벤트)에 대해 누적 지출 금액(`order_total`)을 계산하는 방문자 속성 "전체 주문 금액"을 생성합니다. Tealium 계정에서 전체 주문 금액을 설정하려면 다음 지침을 따르세요:

1. **AudienceStream > Visitor/Visit Attributes**로 이동하여 **Add Attribute**를 클릭합니다.
2. 범위를 **Visitor**로 선택하고 **Continue**를 클릭합니다.
3. 데이터 유형으로 **Number**를 선택하고 **Continue**를 클릭합니다.
4. 속성 이름으로 "Lifetime Order Value"를 입력합니다.
5. **Add Enrichment**를 클릭하고 **Increment or Decrement Number**를 선택합니다.
6. 증가시킬 값이 포함된 속성(`order_total`)을 선택합니다.
7. "WHEN"을 "Any Event"로 두고 **Create a New Rule**을 클릭합니다.
8. 구매 이벤트가 발생했을 때를 식별하는 규칙을 생성합니다.
9. **Save**를 클릭한 다음 **Finish**를 클릭합니다.

이제 모든 고객에게 전체 주문 금액 속성이 연결됩니다.

{% endtab %}
{% tab 배지 %}

공유된 특정 속성에 따라 사용자를 분류하고 타겟팅하는 데 도움이 되는 배지를 만들 수 있습니다. 다음 예시에서는 "전체 주문 금액"이 $500 이상인 사용자를 위한 VIP 배지를 생성합니다.

1. **AudienceStream > Visitor/Visit Attributes**로 이동하여 **Add Attribute**를 클릭합니다.
2. 범위를 **Visitor**로 선택하고 **Continue**를 클릭합니다.
3. 데이터 유형으로 **Badge**를 선택하고 **Continue**를 클릭합니다.
4. 배지 이름으로 "VIP"를 입력합니다.
5. **Add Enrichment**를 클릭하고 **Assign Badge**를 선택합니다.
6. "WHEN"을 "Any Event"로 둡니다.
7. **Create Rule**을 선택하여 배지 할당 규칙을 생성합니다. 이 규칙에 제목을 지정하고, 이전에 생성한 속성을 사용하여 규칙을 "...has attribute "Lifetime Order Value greater than 500"으로 설정합니다.
8. **Save**를 클릭한 다음 **Finish**를 클릭합니다.

{% endtab %}
{% endtabs %}

### 2단계: 오디언스 생성 {#step-2-create-an-audience}

Tealium 홈 페이지에서 사이드바 내비게이션의 **AudienceStream** 아래에 있는 **Audiences**를 선택합니다. 여기서 공통 속성을 가진 사용자 오디언스를 생성할 수 있습니다. 이 오디언스에 대한 사용자의 진입 또는 이탈은 다음 단계에서 설정할 커넥터 액션의 트리거가 되며, 이 정보가 Braze의 고객 프로필로 전달됩니다.

먼저 오디언스의 이름을 지정한 다음, 생성하려는 오디언스 유형에 적용할 속성을 고려합니다. 예를 들어 VIP 사용자 오디언스를 만들려면 **VIP 배지**를 가진 방문자의 오디언스를 생성할 수 있습니다.

완료되면 오디언스를 **Save / Publish** 해야 합니다.

### 3단계: 이벤트 커넥터 생성 {#step-3-create-an-event-connector}

커넥터는 Tealium과 다른 벤더 간의 데이터 전송에 사용되는 통합입니다. 이러한 커넥터에는 파트너가 지원하는 API를 나타내는 액션이 포함되어 있습니다.

1. Tealium의 사이드바에서 **Server-Side** 아래의 **AudienceStream > Audience Connectors**로 이동합니다.
2. 파란색 **+ Add Connector** 버튼을 선택하여 커넥터 마켓플레이스를 탐색합니다. 표시되는 새 대화 상자에서 스포트라이트 검색을 사용하여 **Braze** 커넥터를 찾습니다.
3. 이 커넥터를 추가하려면 **Braze** 커넥터 타일을 클릭합니다. 클릭하면 연결 요약과 필수 정보, 지원되는 액션 및 구성 지침 목록을 볼 수 있습니다. 구성은 소스, 구성, 액션의 세 단계로 구성됩니다.

#### 소스 {#source}

표시되는 **Source** 대화 상자에서 이전 단계에서 생성한 오디언스와 상황에 적합하다고 판단되는 트리거를 선택합니다. 또한 빈도 제한을 토글하여 이 액션이 트리거되는 빈도를 제어할 수도 있습니다.

![오디언스 및 트리거 선택이 포함된 Tealium AudienceStream 커넥터 소스 구성.]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### 구성 {#configuration}

다음으로 **Configuration** 대화 상자가 나타납니다. 페이지 하단에서 **Add Connector**를 선택합니다. 커넥터 이름을 지정하고 Braze API 엔드포인트와 Braze REST API 키를 여기에 입력합니다.

![Braze 엔드포인트 및 REST API 키 필드가 포함된 Tealium 커넥터 구성 대화 상자.]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

이전에 커넥터를 생성한 적이 있다면 사용 가능한 커넥터 목록에서 기존 커넥터를 선택하여 사용하고, 연필 아이콘으로 수정하거나 휴지통 아이콘으로 삭제할 수 있습니다.

이 오디언스에 연결할 커넥터를 생성하거나 선택한 후 Done을 클릭하여 계속합니다.

#### 액션 {#action}

다음으로 커넥터 액션의 이름을 지정하고 구성한 매핑에 따라 데이터를 전송할 액션 유형을 선택합니다. 여기서 Braze 속성을 Tealium 속성 이름에 매핑합니다. 선택한 액션 유형에 따라 Tealium에서 요구하는 필드가 달라집니다. 다음은 이러한 필드의 예시와 설명입니다.

{% alert important %}
제공되는 모든 필드가 필수는 아닙니다.

![축소 가능한 선택 필드가 표시된 Tealium 액션 매핑 패널.]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab 사용자 추적 - 배치 및 비배치 %}

이 액션을 사용하면 사용자, 이벤트 및 구매 속성을 하나의 액션으로 추적할 수 있습니다. 사용자 추적 액션은 AudienceStream과 EventStream 모두에서 동일하지만, Tealium은 AudienceStream 액션으로 사용자 속성 매핑을 설정하고 EventStream 액션으로 이벤트 및 구매 매핑을 설정하는 것을 권장합니다.

| 파라미터 | 설명 |
| ---------- | ----------- |
| 사용자 ID | 이 필드를 사용하여 Tealium 사용자 ID 필드를 해당하는 Braze 필드에 매핑합니다. 하나 이상의 사용자 ID 속성을 매핑합니다. 여러 ID가 지정된 경우 다음 우선순위에 따라 첫 번째 비어 있지 않은 값이 선택됩니다: 외부 ID, Braze ID, 별칭 이름, 별칭 라벨.<br><br>- 푸시 토큰을 가져오는 경우 외부 ID와 Braze ID를 지정하지 마세요.<br>- 사용자 별칭을 지정하는 경우 별칭 이름과 별칭 라벨을 모두 설정해야 합니다. <br><br>자세한 내용은 Braze [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 확인하세요. |
| 사용자 속성 | 기존 Braze 고객 프로필 필드 이름을 사용하여 Braze 대시보드에서 고객 프로필 값을 업데이트하거나, 고객 프로필에 커스텀 [사용자 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object) 데이터를 추가합니다.<br><br>- 기본적으로 존재하지 않는 경우 새 사용자가 생성됩니다.<br>- **Update Existing Only**를 `true`로 설정하면 기존 사용자만 업데이트되며 새 사용자는 생성되지 않습니다.<br>- Tealium 속성이 비어 있으면 null로 변환되어 Braze 고객 프로필에서 제거됩니다. 사용자 속성을 제거하기 위해 Braze에 null 값을 전송하지 않으려면 보강을 사용해야 합니다. |
| 사용자 속성 수정 | 이 필드를 사용하여 특정 사용자 속성을 증가 또는 감소시킵니다<br><br>- 정수 속성은 양의 정수 또는 음의 정수로 증가시킬 수 있습니다.<br>- 배열 속성은 기존 배열에서 값을 추가하거나 제거하여 수정할 수 있습니다. |
| 이벤트 | 이벤트는 특정 사용자가 특정 타임스탬프에 수행한 커스텀 이벤트의 단일 발생을 나타냅니다. 이 필드를 사용하여 Braze [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object)와 같은 이벤트 속성을 추적하고 매핑합니다. <br><br>- 매핑된 모든 이벤트에 이벤트 속성 `Name`은 필수입니다.<br>- 이벤트 속성 `Time`은 명시적으로 매핑하지 않는 한 자동으로 현재 시간으로 설정됩니다. <br>- 기본적으로 존재하지 않는 경우 새 이벤트가 생성됩니다. `Update Existing Only`를 `true`로 설정하면 기존 이벤트만 업데이트되며 새 이벤트는 생성되지 않습니다.<br>- 여러 이벤트를 추가하려면 배열 유형 속성을 매핑합니다. 배열 유형 속성은 동일한 길이여야 합니다.<br>- 단일 값 속성을 사용하여 각 이벤트에 적용할 수 있습니다. |
| 이벤트 템플릿 | 본문 데이터에서 참조할 이벤트 템플릿을 제공합니다. 템플릿을 사용하여 Braze로 전송하기 전에 데이터를 변환할 수 있습니다. 자세한 내용은 Tealium의 [템플릿 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)를 참조하세요. |
| 이벤트 템플릿 변수 | 데이터 입력으로 이벤트 템플릿 변수를 제공합니다. 자세한 내용은 Tealium의 [템플릿 변수 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)를 참조하세요. |
| 구매 | 이 필드를 사용하여 Braze [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object)와 같은 사용자 구매 속성을 추적하고 매핑합니다.<br><br>- 매핑된 모든 구매에 구매 속성 `Product ID`, `Currency`, `Price`는 필수입니다.<br>- 구매 속성 `Time`은 명시적으로 매핑하지 않는 한 자동으로 현재 시간으로 설정됩니다.<br>- 기본적으로 존재하지 않는 경우 새 구매가 생성됩니다. `Update Existing Only`를 `true`로 설정하면 기존 구매만 업데이트되며 새 구매는 생성되지 않습니다.<br>- 여러 구매 항목을 추가하려면 배열 유형 속성을 매핑합니다. 배열 유형 속성은 동일한 길이여야 합니다.<br>- 단일 값 속성을 사용하여 각 항목에 적용할 수 있습니다. |
| 구매 템플릿 | 템플릿을 사용하여 Braze로 전송하기 전에 데이터를 변환할 수 있습니다.<br>- 중첩 오브젝트 지원이 필요한 경우 구매 템플릿을 정의합니다.<br>- 구매 템플릿이 정의되면 액션의 구매 섹션에서 설정한 구성은 무시됩니다.<br>- 자세한 내용은 Tealium의 [템플릿 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)를 참조하세요. |
| 구매 템플릿 변수 | 데이터 입력으로 제품 템플릿 변수를 제공합니다. 자세한 내용은 Tealium의 [템플릿 변수 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="액션" }

![매핑된 사용자 속성 및 이벤트 필드가 포함된 Tealium 사용자 추적 액션 예시.]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab 사용자 삭제 - 비배치 %}

이 액션을 사용하면 Braze 대시보드에서 사용자를 삭제할 수 있습니다.

| 파라미터 | 설명 |
| ---------- | ----------- |
| 사용자 ID | 이 필드를 사용하여 Tealium 사용자 ID 필드를 해당하는 Braze 필드에 매핑합니다.<br><br>- 하나 이상의 사용자 ID 속성을 매핑합니다. 여러 ID가 지정된 경우 다음 우선순위에 따라 첫 번째 비어 있지 않은 값이 선택됩니다: 외부 ID, Braze ID, 별칭 이름, 별칭 라벨.<br>- 사용자 별칭을 지정할 때는 별칭 이름과 별칭 라벨을 모두 설정해야 합니다.<br><br>자세한 내용은 Braze [`/users/delete` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="액션" }

![Braze 사용자 ID 매핑이 구성된 Tealium 사용자 삭제 액션.]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab 사용자 구독 그룹 상태 업데이트 - 비배치 %}
이 액션을 사용하면 Braze SMS 또는 이메일 구독 그룹에서 사용자를 추가하거나 제거할 수 있습니다.

| 파라미터 | 설명 |
| ---------- | ----------- |
| 그룹 유형 | 이 필드를 사용하여 SMS 또는 이메일 구독 그룹인지 표시합니다. |
| 업데이트 유형 | 이 액션을 탈퇴 또는 가입 이벤트에 매핑합니다. |
| 속성 | - 구독 그룹 ID (필수): 이전 필드에서 매핑된 그룹 유형과 관련된 구독 그룹의 ID입니다.<br>- 외부 ID: 사용자의 외부 ID입니다.<br><br>이메일 그룹 전용:<br>- 이메일: 사용자의 이메일 주소입니다.<br>**외부 ID가 정의되지 않은 경우 이메일이 필수입니다.**<br><br>SMS 그룹 전용:<br>- 전화번호: E.164 형식의 전화번호입니다. 예: +14155552671.<br>**외부 ID가 정의되지 않은 경우 전화번호가 필수입니다.** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="액션" }

![그룹 유형 및 업데이트 유형 매핑이 포함된 Tealium 구독 그룹 상태 업데이트 액션.]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

**Finish**를 선택합니다.

#### 요약 {#summary}

생성한 커넥터의 요약을 확인합니다. 선택한 옵션을 수정하려면 **Back**을 선택하여 편집하거나 **Finish**를 선택하여 완료합니다.

이제 커넥터가 Tealium 홈 페이지의 커넥터 목록에 표시됩니다.

완료되면 커넥터를 저장하거나 게시해야 합니다. 구성한 액션은 트리거 연결 조건이 충족되면 실행됩니다.

### 4단계: Tealium 커넥터 테스트 {#step-4-test-your-tealium-connector}

커넥터가 실행되면 올바르게 작동하는지 테스트해야 합니다. 가장 간단한 테스트 방법은 Tealium **Trace Tool**을 사용하는 것입니다. Trace 사용을 시작하려면 Tealium Tools 브라우저 확장 프로그램을 추가했는지 확인하세요.

1. 새 트레이스를 시작하려면 **Server-Side** 옵션 아래의 사이드바에서 **Trace**를 선택합니다. **Start**를 클릭하고 Trace ID를 캡처합니다.
2. 브라우저 확장 프로그램을 열고 AudienceStream Trace에 Trace ID를 입력합니다.
3. 실시간 로그를 확인합니다.
4. **Actions Triggered** 항목을 클릭하여 확장하고 유효성을 검사할 액션을 확인합니다.
5. 유효성을 검사할 액션을 찾고 로그 상태를 확인합니다.

Tealium의 Trace 도구 구현에 대한 자세한 지침은 Tealium의 [Trace 설명서](https://docs.tealium.com/server-side/connectors/trace/about/)를 참조하세요.

## 통합 데모 {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" title="Tealium AudienceStream 통합 데모" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 잠재적 데이터 포인트 초과량 {#potential-data-point-overages}

Tealium을 통해 Braze를 통합할 때 실수로 데이터 초과량이 발생할 수 있는 주요 원인은 세 가지입니다:

### 중복 데이터 전송 - Braze 속성의 변경 사항만 전송하세요 {#sending-duplicate-data-only-send-braze-deltas-of-attributes}
Tealium은 사용자 속성의 변경 사항(델타)만 Braze에 전송하지 않습니다. 예를 들어, 사용자의 이름, 이메일, 휴대전화 번호를 추적하는 EventStream 액션이 있는 경우, Tealium은 해당 액션이 트리거될 때마다 세 가지 속성을 모두 Braze에 전송합니다. Tealium은 무엇이 변경되었거나 업데이트되었는지 확인하고 해당 정보만 전송하지 않습니다.<br><br>
**해결 방법**: <br>백엔드에서 속성이 변경되었는지 여부를 확인하고, 변경된 경우 Tealium의 관련 메서드를 호출하여 고객 프로필을 업데이트할 수 있습니다. **이 방법은 Braze를 직접 통합하는 사용자가 일반적으로 사용하는 방식입니다.** <br>**또는**<br> 백엔드에 자체 사용자 프로필 버전을 저장하지 않아 속성이 변경되었는지 확인할 수 없는 경우, AudienceStream을 사용하고 [보강 생성](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/)을 통해 값이 변경되었을 때만 사용자 속성을 전송할 수 있습니다.

#### 관련 없는 데이터 전송 또는 불필요한 데이터 덮어쓰기 {#sending-irrelevant-data-or-needlessly-overwriting-data}
동일한 이벤트 피드를 대상으로 하는 여러 EventStream이 있는 경우, **해당 커넥터에 대해 활성화된 모든 액션**은 단일 액션이 트리거될 때마다 자동으로 실행되며, **이로 인해 Braze에서 데이터가 덮어쓰여질 수 있습니다.**<br><br>
**해결 방법**: <br>각 액션을 추적하기 위한 별도의 이벤트 사양 또는 피드를 설정하세요. <br>**또는**<br> Tealium 대시보드에서 토글을 사용하여 실행하고 싶지 않은 액션(또는 커넥터)을 비활성화하세요.

#### Braze를 너무 일찍 초기화 {#initializing-braze-too-early}
Braze 웹 SDK 태그를 사용하여 Tealium과 통합하는 경우, MAU가 급격히 증가할 수 있습니다. **페이지 로드 시 Braze가 초기화되면, 웹 사용자가 처음으로 웹사이트를 방문할 때마다 Braze는 익명 프로필을 생성합니다.** 여기에는 봇 트래픽도 포함되어 활성 사용자 수가 부풀려질 수 있습니다. 일부 사용자는 "로그인" 또는 "비디오 시청"과 같이 특정 행동을 완료한 사용자의 행동만 추적하여 MAU 수를 줄이고 싶을 수 있습니다. <br><br>
**해결 방법**: <br>[로드 규칙](https://docs.tealium.com/iq-tag-management/load-rules/about/)을 설정하여 사이트에서 태그가 로드되는 시점과 위치를 정확히 결정하세요. 봇 트래픽 필터링 및 조건부 SDK 초기화에 대한 보다 종합적인 안내는 [봇 트래픽 필터링]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering)을 참조하세요.