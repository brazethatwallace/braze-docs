# 자주 묻는 질문 {#frequently-asked-questions}

> Braze의 배너에 대해 자주 묻는 질문과 답변입니다. 더 일반적인 정보는 [배너 소개]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %})를 참조하세요.

## 배너 업데이트는 사용자에게 언제 표시되나요? {#when-do-banner-updates-appear-for-users}

배너는 새로고침 메서드를 호출할 때마다 최신 데이터로 갱신됩니다&#8212;배너 Campaign을 다시 보내거나 업데이트할 필요가 없습니다.

## 한 세션에서 몇 개의 배치를 요청할 수 있나요? {#how-many-placements-can-i-request-in-a-session}

단일 새로고침 요청에서 최대 10개의 배치를 요청할 수 있습니다. 요청하는 각 배치에 대해 Braze는 사용자가 수신 자격이 있는 가장 높은 우선순위의 배너를 반환합니다. 추가 요청은 오류를 반환합니다.

자세한 내용은 [배치 요청]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %})을 참조하세요.

## 동시에 활성화할 수 있는 배너 Campaign은 최대 몇 개인가요? {#how-many-banner-campaigns-can-be-active-simultaneously}

각 워크스페이스는 최대 200개의 활성 배너 Campaign을 지원할 수 있습니다. 이 한도에 도달하면 새 Campaign을 만들기 전에 기존 Campaign을 [보관 또는 비활성화]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses#changing-the-status)해야 합니다.

## 동일한 위치를 공유하는 Campaign에서 어떤 배너가 먼저 표시되나요? {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

사용자가 동일한 위치를 공유하는 여러 배너 Campaign에 자격이 있는 경우, 가장 높은 우선순위를 가진 배너가 표시됩니다. 자세한 내용은 [배너 우선순위]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %})를 참조하세요.

## 기존 Content Cards 피드에서 배너를 사용할 수 있나요? {#can-i-use-banners-in-my-existing-content-card-feed}

배너는 Content Cards와 다르므로, 배너와 Content Cards를 동일한 피드에서 사용할 수 없습니다. 기존 Content Cards 피드를 배너로 교체하려면, [앱 또는 웹사이트에서 배치를 생성]({{site.baseurl}}/developer_guide/banners/placements)해야 합니다.

## 배너와 인앱 메시지는 어떻게 다른가요? {#how-are-banners-different-from-in-app-messages}

배너와 [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages)는 모두 앱이나 웹사이트 내에서 사용자에게 도달하지만, 서로 다른 전달 모델을 사용합니다. 배너를 기존 인앱 메시지 설정과 비교하는 경우, 트리거, 새로고침 타이밍, 테스트 방식에서 차이가 있으며, 단순히 일대일로 대체되는 것은 아닙니다.

| 주제 | 배너 | 인앱 메시지 |
| --- | --- | --- |
| 메시지가 표시되는 위치 | 앱이나 사이트에서 정의한 [배치]({{site.baseurl}}/developer_guide/banners/placements)에 인라인으로 표시 | SDK가 관리하는 전체화면, Modal 또는 슬라이드업 오버레이 |
| 콘텐츠가 업데이트되는 시점 | 앱이나 사이트에서 배너 새로고침을 호출할 때(예: 세션 시작 또는 세션 중간) | 템플릿 메시지는 인앱 메시지가 트리거될 때(예: 커스텀 이벤트 또는 세션 시작 시) 기기에 페이로드가 캐시된 후 Liquid를 평가합니다 |
| 실행 기반 트리거 | [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) 없음; 대신 Segments, 우선순위, 새로고침 타이밍을 사용합니다 | 실행 기반 및 API 트리거 전달을 지원합니다 |
| 테스트 | 사용자를 미리보기한 다음, 앱이나 사이트에서 배치 새로고침이 예상 배너를 표시하는지 확인합니다 | **Test Send** 또는 인앱 미리보기 플로우를 사용하여 트리거 기반 표시를 확인합니다 |
| 리포팅 | 배너 조회수와 클릭은 배너 분석을 따릅니다 | 인앱 노출 횟수와 클릭은 인앱 메시지 분석을 따릅니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="배너와 인앱 메시지는 어떻게 다른가요?" }

## 배너에 비디오를 포함할 수 있나요? {#can-banners-include-video}

표준 배너 빌더는 이미지, 텍스트, 버튼을 지원합니다. 배너에 비디오를 포함하려면 빌더에서 **커스텀 코드** 블록을 사용하거나, HTML 편집기로 전체 배너를 빌드하고 HTML에 비디오 플레이어를 직접 삽입할 수 있습니다.

## 사용자 행동을 기반으로 배너를 트리거할 수 있나요? {#can-i-trigger-a-banner-based-on-user-actions}

배너는 [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)을 지원하지 않지만, 세분화 및 우선순위를 사용하여 과거 행동을 기반으로 사용자를 타겟팅할 수 있습니다.

예를 들어, `purchase` 이벤트를 완료한 사용자에게만 특별한 배너를 표시하려면 다음과 같이 합니다:
1. **타겟팅:** Campaign에서 커스텀 이벤트 `purchase`를 최소 1회 이상 수행한 사용자 Segment를 타겟팅합니다.
2. **우선순위:** 모든 사용자를 대상으로 하는 일반 배너와 구매자를 대상으로 하는 특정 배너가 동일한 위치를 타겟팅하는 경우, 특정 배너의 우선순위를 **높음**으로, 일반 배너의 우선순위를 **중간** 또는 **낮음**으로 설정합니다.

사용자가 행동을 수행한 후 새 세션을 시작하거나 배너를 새로고침하면, Braze는 사용자의 자격을 평가합니다. "Purchase" Segment에 일치하는 경우 높은 우선순위의 배너가 표시됩니다.

## 사용자가 배너를 닫을 수 있나요? {#can-users-dismiss-a-banner}

네, 사용자가 배너를 수동으로 닫을 수 있도록 허용할 수 있습니다. 빌더와 HTML 편집기에서 닫기 동작을 구성하는 방법에 대한 자세한 내용은 [닫기 동작 구성]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior)을 참조하세요.

사용자는 닫기 동작이 활성화된 경우에만 배너를 수동으로 닫을 수 있습니다. 닫기가 활성화되지 않은 경우, 사용자 Segment 자격을 관리하여 배너 가시성을 제어할 수 있습니다. 사용자가 더 이상 배너 Campaign의 타겟팅 기준을 충족하지 않으면, 다음 세션에서 해당 배너가 표시되지 않습니다.

사용자가 배너를 닫으면, 기본적으로 해당 Campaign에 대한 수신 자격이 사라집니다. 닫은 사용자가 배너를 다시 볼 수 있도록 하려면, Campaign의 **전달 제어** 단계에서 [재자격 구성]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility)을 설정하세요. Canvas 배너 단계는 재자격을 제어하기 위해 Canvas 재진입 설정을 대신 사용합니다.

예를 들어, 사용자가 구매할 때까지 프로모션 배너를 표시하는 경우, `purchase_completed`와 같은 이벤트를 기록하면 해당 사용자를 타겟 Segment에서 제거하여 이후 세션에서 배너를 효과적으로 숨길 수 있습니다.

## Banners Campaign 분석을 Braze API를 사용하여 내보낼 수 있나요? {#can-i-export-banners-campaign-analytics-using-the-braze-api}

네. [`/campaigns/data_series` 엔드포인트]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)를 사용하여 배너 Campaign이 조회, 클릭 또는 전환된 횟수에 대한 데이터를 가져올 수 있습니다.

## 사용자는 언제 세분화되나요? {#when-are-users-segmented}

사용자는 세션이 시작될 때 세분화됩니다. Campaign의 타겟 Segments가 커스텀 속성, 커스텀 이벤트 또는 기타 타겟팅 속성에 의존하는 경우, 해당 속성들은 세션 시작 시점에 사용자에게 존재해야 합니다.

## 배너를 구성할 때 지연 시간을 최소화하려면 어떻게 해야 하나요? {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

배너의 메시지가 단순할수록 렌더링 속도가 빨라집니다. 예상되는 지연 시간에 맞춰 배너 Campaign을 테스트하는 것이 좋습니다. 예를 들어, `catalog_items`와 같은 Liquid 속성을 반드시 테스트하세요.

[연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)(얼리 액세스)를 사용하는 경우, 각 호출은 단일 새로고침 시 모든 배치에 걸쳐 약 2초의 공유 렌더링 예산에 포함된다는 점에 유의하세요. 예산이 초과되거나 호출이 시간 초과되면 연결된 콘텐츠 결과는 null로 처리되며, 배너는 재시도하지 않습니다. 지연 시간을 최소화하려면 다음을 따르세요.

- 엔드포인트를 빠르게 유지하고, 가능한 한 [응답을 캐시]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)하세요.
- 함께 렌더링되는 배치 전체에서 고유한 연결된 콘텐츠 URL 수를 제한하세요.
- 하나의 연결된 콘텐츠 응답이 다음 호출의 URL을 결정하는 체이닝 호출은 피하세요.
- Liquid 가드 구문이나 [`default` 필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values)를 사용하여 null 결과를 처리하고 빈 배너가 표시되지 않도록 하세요.

## 모든 Liquid 태그가 지원되나요? {#are-all-liquid-tags-supported}

아니요. 그러나 [`:rerender` 태그]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid)를 사용하여 다시 렌더링되는 `catalog_items`를 제외하고, 대부분의 Liquid 태그는 배너 메시지에서 지원됩니다.

## 클릭 이벤트를 캡처할 수 있나요? {#can-i-capture-click-events}

네. 클릭 이벤트가 캡처되는 방식은 배너가 렌더링되는 방식에 따라 다릅니다.

- **빌더 — 표준 컴포넌트:** 배너가 표준 편집기 컴포넌트(이미지, 버튼, 텍스트)를 사용하는 경우, SDK의 삽입 메서드를 사용하면 클릭이 자동으로 추적됩니다.
- **빌더 — 커스텀 코드 블록:** 커스텀 코드 편집기 블록 내의 요소에 대해 클릭을 추적하려면, 커스텀 HTML 내에서 `brazeBridge.logClick()`을 호출해야 합니다. 이는 SDK 메서드를 사용하여 배너를 삽입하고 렌더링하는 경우에도 적용됩니다.
- **HTML 편집기:** 클릭 추적은 자동으로 이루어지지 않습니다. 추적하려는 모든 클릭 가능한 요소에 대해 `brazeBridge.logClick()`을 호출해야 합니다. 전체 레퍼런스는 [배너용 커스텀 코드 및 JavaScript 브리지]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge)를 참조하세요.
- **커스텀 UI (헤드리스):** 배너 HTML을 렌더링하는 대신 배너의 커스텀 속성을 사용하여 완전히 커스텀 UI를 구축하는 경우, 애플리케이션 코드에서 배너 객체의 `logClick()`을 호출하세요.

자세한 내용은 [클릭 로깅]({{site.baseurl}}/developer_guide/banners/placements#logging-clicks)을 참조하세요.