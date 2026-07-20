# 자주 묻는 질문 {#frequently-asked-questions}

> Braze의 배너에 대해 자주 묻는 질문과 답변입니다. 더 일반적인 정보는 [배너 소개]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %})를 참조하세요.

## 배너 업데이트는 사용자에게 언제 나타나나요? {#when-do-banner-updates-appear-for-users}

배너는 새로고침 메서드를 호출할 때마다 최신 데이터로 새로고침됩니다&#8212;배너 Campaign을 다시 전송하거나 업데이트할 필요가 없습니다.

## 세션에서 요청할 수 있는 배치 수는 몇 개인가요? {#how-many-placements-can-i-request-in-a-session}

단일 새로고침 요청에서 최대 10개의 배치를 요청할 수 있습니다. 요청하는 각 배치에 대해 Braze는 사용자가 자격이 있는 가장 높은 우선순위의 배너를 반환합니다. 추가 요청은 오류를 반환합니다.

자세한 내용은 [배치 요청]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %})을 참조하세요.

## 동시에 활성화할 수 있는 배너 Campaign은 몇 개인가요? {#how-many-banner-campaigns-can-be-active-simultaneously}

각 워크스페이스는 최대 200개의 활성 배너 Campaign을 지원할 수 있습니다. 이 한도에 도달하면 새 Campaign을 만들기 전에 기존 Campaign을 [아카이브하거나 비활성화]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses#changing-the-status)해야 합니다.

## 배치를 공유하는 Campaign에서 어떤 배너가 먼저 표시되나요? {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

사용자가 동일한 배치를 공유하는 여러 배너 Campaign에 자격이 있는 경우, 가장 높은 우선순위의 배너가 표시됩니다. 자세한 내용은 [배너 우선순위]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %})를 참조하세요.

## 기존 Content Cards 피드에서 배너를 사용할 수 있나요? {#can-i-use-banners-in-my-existing-content-card-feed}

배너는 Content Cards와 다르므로, 같은 피드에서 배너와 Content Cards를 함께 사용할 수 없습니다. 기존 Content Cards 피드를 배너로 교체하려면 [앱이나 웹사이트에 배치를 생성]({{site.baseurl}}/developer_guide/banners/placements)해야 합니다.

## 배너는 인앱 메시지와 어떻게 다른가요? {#how-are-banners-different-from-in-app-messages}

배너와 [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages)는 모두 앱이나 웹사이트 내에서 사용자에게 도달하지만, 서로 다른 전달 모델을 사용합니다. 배너를 기존 인앱 메시지 설정과 비교하는 경우, 트리거, 새로고침 타이밍, 테스트에서 차이가 있으며 일대일 대체가 아닙니다.

| 주제 | 배너 | 인앱 메시지 |
| --- | --- | --- |
| 메시지가 표시되는 위치 | 앱이나 사이트에서 정의한 [배치]({{site.baseurl}}/developer_guide/banners/placements)에 인라인으로 표시 | SDK가 관리하는 전체화면, Modal 또는 슬라이드업 오버레이 |
| 콘텐츠가 업데이트되는 시점 | 앱이나 사이트에서 배너 새로고침을 호출할 때(예: 세션 시작 시 또는 세션 중) | 템플릿화된 메시지는 인앱 메시지가 트리거될 때(예: 커스텀 이벤트 또는 세션 시작 시) 기기에 페이로드가 캐시된 후 Liquid를 평가합니다 |
| 실행 기반 트리거 | [실행 기반 전달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery) 없음; 대신 Segments, 우선순위, 새로고침 타이밍을 사용합니다 | 실행 기반 및 API 트리거 전달을 지원합니다 |
| 테스트 | 사용자를 미리보기한 다음, 앱이나 사이트에서 배치 새로고침이 예상 배너를 표시하는지 확인합니다 | **Test Send** 또는 인앱 미리보기 플로우를 사용하여 트리거 기반 표시를 확인합니다 |
| 리포팅 | 배너 조회 및 클릭은 배너 분석을 따릅니다 | 인앱 노출 횟수 및 클릭은 인앱 메시지 분석을 따릅니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="배너는 인앱 메시지와 어떻게 다른가요?" }


## 배너에 비디오를 포함할 수 있나요? {#can-banners-include-video}

표준 배너 작성기는 이미지, 텍스트, 버튼을 지원합니다. 배너에 비디오를 포함하려면 작성기에서 **커스텀 코드** 블록을 사용하거나, HTML 편집기로 전체 배너를 작성하여 HTML에 비디오 플레이어를 직접 임베드할 수 있습니다.

## 사용자 동작에 따라 배너를 트리거할 수 있나요? {#can-i-trigger-a-banner-based-on-user-actions}

배너는 [실행 기반 전달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery)을 지원하지 않지만, 세분화 및 우선순위를 사용하여 과거 동작에 따라 사용자를 타겟팅할 수 있습니다.

예를 들어, `purchase` 이벤트를 완료한 사용자에게만 특별한 배너를 표시하려면:
1. **타겟팅:** Campaign에서 커스텀 이벤트 `purchase`를 최소 한 번 수행한 사용자 Segment를 타겟팅하세요.
2. **우선순위:** 모든 사용자를 위한 일반 배너와 구매자를 위한 특정 배너가 동일한 배치를 타겟팅하는 경우, 특정 배너의 우선순위를 **High**로 설정하고 일반 배너는 **Medium** 또는 **Low**로 설정하세요.

사용자가 새 세션을 시작하거나 동작을 수행한 후 배너를 새로고침하면, Braze가 자격 여부를 평가합니다. "Purchase" Segment에 해당하면 높은 우선순위의 배너가 표시됩니다.


## 사용자가 배너를 닫을 수 있나요? {#can-users-dismiss-a-banner}

네. 사용자가 배너를 수동으로 닫을 수 있도록 허용할 수 있습니다. 작성기와 HTML 편집기에서 닫기 동작을 구성하는 방법에 대한 자세한 내용은 [닫기 동작 구성]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior)을 참조하세요.

사용자는 닫기 동작이 활성화된 경우에만 배너를 수동으로 닫을 수 있습니다. 닫기 기능이 활성화되지 않은 경우, 사용자 Segment 자격을 관리하여 배너 표시 여부를 제어할 수 있습니다. 사용자가 배너 Campaign의 타겟팅 기준을 더 이상 충족하지 않으면, 다음 세션에서 해당 배너를 다시 보지 않게 됩니다.

사용자가 배너를 닫으면 기본적으로 해당 Campaign에 대한 자격이 없어집니다. 닫은 사용자가 배너를 다시 볼 수 있도록 하려면 Campaign의 **전달 제어** 단계에서 [재자격 구성]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility)을 설정하세요. Canvas 배너 단계는 재자격을 제어하기 위해 Canvas 재진입 설정을 대신 사용합니다.

예를 들어, 사용자가 구매할 때까지 프로모션 배너를 표시하는 경우, `purchase_completed`와 같은 이벤트를 기록하면 해당 사용자가 타겟팅된 Segment에서 제거되어 이후 세션에서 배너가 효과적으로 숨겨집니다.

## Braze API를 사용하여 배너 Campaign 분석을 내보낼 수 있나요? {#can-i-export-banners-campaign-analytics-using-the-braze-api}

네. [`/campaigns/data_series` 엔드포인트]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)를 사용하여 배너 Campaign의 조회 수, 클릭 수, 전환 수에 대한 데이터를 가져올 수 있습니다.

## 사용자는 언제 세그먼트화되나요? {#when-are-users-segmented}

사용자는 세션 시작 시 세그먼트화됩니다. Campaign의 타겟팅 Segments가 커스텀 속성, 커스텀 이벤트 또는 기타 타겟팅 속성에 의존하는 경우, 세션 시작 시 사용자에게 해당 속성이 존재해야 합니다.

## 최소 지연 시간을 보장하려면 배너를 어떻게 작성해야 하나요? {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

배너의 메시지가 간단할수록 더 빠르게 렌더링됩니다. 사용 사례에 대한 예상 지연 시간을 기준으로 배너 Campaign을 테스트하는 것이 가장 좋습니다. 예를 들어, `catalog_items`와 같은 Liquid 속성을 반드시 테스트하세요.

## 모든 Liquid 태그가 지원되나요? {#are-all-liquid-tags-supported}

아니요. 하지만 대부분의 Liquid 태그는 배너 메시지에서 지원됩니다. 단, [`:rerender` 태그]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid)를 사용하여 다시 렌더링되는 `catalog_items`는 예외입니다.

## 클릭 이벤트를 캡처할 수 있나요? {#can-i-capture-click-events}

네. 클릭 이벤트가 캡처되는 방식은 배너가 렌더링되는 방법에 따라 다릅니다:

- **작성기 — 표준 구성요소:** 배너가 표준 편집기 구성요소(이미지, 버튼, 텍스트)를 사용하는 경우, SDK의 삽입 메서드를 사용할 때 클릭이 자동으로 추적됩니다.
- **작성기 — 커스텀 코드 블록:** 커스텀 코드 편집기 블록 내의 요소에 대한 클릭을 추적하려면, 커스텀 HTML 내에서 `brazeBridge.logClick()`을 호출해야 합니다. 이는 SDK 메서드를 사용하여 배너를 삽입하고 렌더링하는 경우에도 적용됩니다.
- **HTML 편집기:** 클릭 추적은 자동으로 이루어지지 않습니다. 추적하려는 모든 클릭 가능한 요소에 대해 `brazeBridge.logClick()`을 호출해야 합니다. 전체 참조는 [배너를 위한 커스텀 코드 및 JavaScript 브리지]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge)를 참조하세요.
- **커스텀 UI(헤드리스):** 배너 HTML을 렌더링하는 대신 배너의 커스텀 속성을 사용하여 완전히 커스텀 UI를 구축하는 경우, 애플리케이션 코드에서 배너 오브젝트의 `logClick()`을 호출하세요.

자세한 내용은 [클릭 로깅]({{site.baseurl}}/developer_guide/banners/placements#logging-clicks)을 참조하세요.