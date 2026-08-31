---
nav_title: 워크스페이스
article_title: "시작하기: 워크스페이스"
page_order: 3
page_type: reference
description: "Braze 플랫폼에서 하는 모든 작업은 워크스페이스 내에서 이루어집니다. 이 문서에서는 워크스페이스의 작동 방식과 유의해야 할 중요한 사항에 대해 설명합니다."
---

# 시작하기: 워크스페이스 {#get-started-workspaces}

> Braze 플랫폼에서 하는 모든 작업은 워크스페이스 내에서 이루어집니다. 워크스페이스는 별도의 데이터 사일로 역할을 하며, 서로 다른 브랜드나 활동을 분리하여 관리할 수 있습니다. 웹사이트 또는 모바일 앱의 여러 버전에서 동일한 워크스페이스로 데이터를 전송할 수 있습니다. 워크스페이스 내에서 수집되는 다양한 사이트와 앱을 "앱 인스턴스"라고 합니다.

## 워크스페이스 이해하기 {#understanding-workspaces}

워크스페이스는 두 가지 핵심 목적을 제공합니다:

- **사용자 데이터 통합:** 하나의 워크스페이스에 여러 앱 인스턴스가 있으면 iOS, Android, 웹 등 다양한 버전의 앱에서 사용자 데이터를 원활하게 수집하고 타겟팅할 수 있습니다. 이를 통해 사용자가 어떤 플랫폼을 사용하든 항상 최신 정보를 확보할 수 있습니다.
- **별도의 활동 분리:** 워크스페이스는 서로 다른 브랜드나 활동을 분리하는 수단도 제공합니다. 예를 들어, 서로 다른 사용자 기반을 가진 여러 하위 브랜드가 있는 경우 각각에 대해 별도의 워크스페이스를 만드는 것이 좋습니다.

{% alert tip %}
이 접근 방식은 각 게임별로 개별 워크스페이스를 관리할 수 있는 모바일 게임 회사나 운영하는 각 지역별로 별도의 워크스페이스를 원하는 이커머스 사이트와 같은 기업에 특히 유용합니다.
{% endalert %}

## 워크스페이스 계획하기 {#planning-workspaces}

각 플랫폼에서 앱의 각 버전에 대해 별도의 앱 인스턴스를 생성해야 합니다. 워크스페이스에 포함할 앱 인스턴스를 결정할 때, 타겟팅하려는 사용자를 고려하고 그에 따라 그룹화하세요.

하나의 워크스페이스에 여러 앱 인스턴스를 두면 전체 앱 포트폴리오에 걸쳐 메시징 사용량 제한을 적용할 수 있기 때문에 매력적으로 보일 수 있습니다. 그러나 모범 사례로서, 동일한(또는 매우 유사한) 앱의 서로 다른 버전만 하나의 워크스페이스에 함께 두는 것을 권장합니다.

### 공유 워크스페이스 {#shared-workspaces}

동일한 워크스페이스에 여러 앱 인스턴스를 두는 일반적인 예시는 다음과 같습니다:

- 서로 다른 플랫폼에 거의 동일한 앱이 여러 개 있는 경우
- 앱의 주요 버전이 다르지만, 사용자가 업그레이드할 때 동일한 사용자에게 계속 참여시키고 싶은 경우
- 동일한 사용자가 이동할 수 있는 서로 다른 버전의 앱이 있는 경우(예: 무료에서 프리미엄으로)

#### 세분화 필터에 미치는 영향 {#impact-on-segmentation-filters}

하나의 워크스페이스에 포함하기로 선택한 앱들의 데이터는 집계됩니다. 이는 Braze의 다음 세분화 필터에 주목할 만한 영향을 미칩니다(전체 목록이 아닙니다):

- 마지막 사용 앱
- 최초 사용 앱
- 세션 수
- 인앱 결제 금액
- 푸시 구독 (이는 전부 아니면 전무의 상황이 됩니다. 사용자가 하나의 앱에서 구독을 취소하면 워크스페이스 내 모든 앱에서 구독이 취소됩니다.)
- 이메일 구독 (이는 전부 아니면 전무의 상황이 되며, 규정 준수 문제에 노출될 수 있습니다.)

{% alert note %}
이러한 필터에서 앱 인스턴스 간 데이터가 집계되기 때문에, 상당히 다른 앱을 동일한 워크스페이스에 두는 것을 권장하지 않습니다. 타겟팅이 까다로워질 수 있습니다!
{% endalert %}

### 별도의 워크스페이스 {#separate-workspaces}

때로는 여러 개의 별도 워크스페이스를 사용하고 싶을 수 있습니다. 일반적인 예시는 다음과 같습니다:

- 동일한 앱의 개발 환경과 프로덕션 환경을 위한 별도의 워크스페이스
- 서로 다른 하위 브랜드, 예를 들어 여러 게임을 제공하는 모바일 게임 회사
- 서로 다른 국가에서 운영되거나 다른 언어를 타겟팅하는 동일한 앱 또는 웹사이트의 서로 다른 현지화 버전

### 주요 고려사항 {#important-considerations}

워크스페이스는 별도의 데이터 사일로로 작동한다는 점을 기억하세요. 사용자 데이터든 마케팅 자산이든 모든 데이터는 워크스페이스 내에 저장됩니다. 이 데이터는 해당 워크스페이스 외부에서 쉽게 공유할 수 없습니다.

다음은 워크스페이스 내에서 구성되는 모든 핵심 요소입니다:

- [앱 인스턴스](#app-instances)
- [Teams](#teams)
- [회사 사용자 권한](#company-user-permissions)(회사 사용자 자체는 제외)
- [Currents 커넥터](#currents-connectors)
- [고객 프로필](#user-profiles) 및 관련 사용자 데이터
- [Segments, Campaigns, Canvases](#segments-campaigns-and-canvases)

#### 앱 인스턴스 {#app-instances}

각 플랫폼에서 앱의 각 버전에 대해 별도의 앱 인스턴스를 생성해야 합니다. 예를 들어, iOS와 Android 모두에서 무료 버전과 프로 버전의 앱이 있다면 워크스페이스 내에 네 개의 앱 인스턴스를 생성합니다(무료 iOS 앱, 무료 Android 앱, 프로 iOS 앱, 프로 Android 앱). 이렇게 하면 각 앱 인스턴스에 하나씩, 네 개의 API 키를 사용할 수 있습니다.

#### Teams {#teams}

[Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams)는 고객 기반 위치, 언어 및 커스텀 속성에 따라 설정할 수 있으므로, 팀 구성원과 비팀 구성원이 메시징 기능과 고객 데이터에 서로 다른 접근 권한을 갖게 됩니다.

#### 회사 사용자 권한 {#company-user-permissions}

워크스페이스는 독립적인 접근 권한과 사용자 권한 정의를 갖습니다. [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)을 통해 개별 대시보드 사용자 또는 팀이 단일 워크스페이스 내에서 접근할 수 있는 항목에 대한 세분화된 제어를 만들 수 있습니다.

#### Currents 커넥터 {#currents-connectors}

[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 도구는 인게이지먼트 이벤트의 실시간 데이터 스트림으로, Braze 플랫폼에서 가장 강력하면서도 세분화된 내보내기입니다. Currents 커넥터는 특정 Braze 패키지에 포함되어 있으며, 단일 워크스페이스를 가정한 상태에서 처음에 하나를 받았을 수 있습니다.

별도의 워크스페이스와 통합 워크스페이스 중 결정할 때, 보유한 Currents 커넥터의 수를 고려하는 것이 중요합니다. Currents 커넥터는 워크스페이스 간에 공유되지 않기 때문입니다.

예를 들어, 동일한 앱의 개발 환경과 프로덕션 환경에 대해 별도의 워크스페이스가 있다면, 프로덕션 워크스페이스에서 Currents 커넥터를 활성화하세요. 두 워크스페이스 모두에서 Currents를 활성화하려면 추가 Currents 커넥터를 구매해야 합니다.

#### 고객 프로필 {#user-profiles}

사용자와 관련된 모든 영구 데이터는 [고객 프로필]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)에 저장됩니다. 그러나 고객 프로필은 사용자의 인게이지먼트 기록, Segment 멤버십, 기기 및 운영 체제에 대한 정보에 쉽게 접근할 수 있으므로 문제 해결 및 테스트에도 훌륭한 리소스입니다.

#### Segments, Campaigns, Canvases {#segments-campaigns-and-canvases}

Segment, Campaign 또는 Canvas는 다른 워크스페이스에 저장된 데이터를 참조하거나 접근할 수 없습니다. 반대로, 여러 앱이 동일한 워크스페이스에 있을 때 모든 앱의 데이터가 집계됩니다. 이는 [Braze 필터에 미치는 영향](#impact-on-segmentation-filters)이 있습니다.

### 각 접근 방식의 개요 {#overview-of-each-approach}

다음 표는 워크스페이스 계획에 대한 두 가지 접근 방식의 장단점을 설명합니다:

- **별도의 워크스페이스 및 고객 프로필:** 하나의 워크스페이스에 하나의 앱 인스턴스가 있고, 한 사람이 해당 앱 인스턴스에 대해 하나의 고객 프로필을 갖습니다.
- **공유 워크스페이스 및 고객 프로필:** 하나의 워크스페이스에 여러 앱 인스턴스가 있고, 한 사람이 해당 모든 앱 인스턴스에 대해 하나의 고객 프로필을 갖습니다.

<style type="text/css">
  table {
    width: 100%;
  }
  th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid black;
    word-break: break-word !important;
  }
  th {
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
  th[colspan="2"] {
    background-color: #fffae6;
  }
  th:last-child[colspan="2"] {
    background-color: #deebff;
  }
  td:nth-child(2), td:nth-child(3) {
    background-color: #fffae6;
  }
  td:nth-child(4), td:nth-child(5) {
    background-color: #deebff;
  }
  th:nth-child(2), th:nth-child(3) {
    background-color: #fffae6;
  }
  th:nth-child(4), th:nth-child(5) {
    background-color: #deebff;
  }
  th:first-child, td:first-child {
    min-width: 150px;
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
</style>

<table aria-label="각 접근 방식의 개요">
  <caption>각 접근 방식의 개요</caption>
    <thead>
    <tr>
        <th></th>
        <th colspan="2" scope="colgroup">별도의 워크스페이스</th>
        <th colspan="2" scope="colgroup">공유 워크스페이스</th>
    </tr>
    <tr>
        <th></th>
        <th scope="col">장점</th>
        <th scope="col">단점</th>
        <th scope="col">장점</th>
        <th scope="col">단점</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <th scope="row">타겟팅</th>
        <td>커뮤니케이션을 분리하는 가장 안전한 방법입니다. Campaigns가 특정 고객 프로필만 타겟팅하도록 보장됩니다.</td>
        <td>사용자가 다른 워크스페이스에 다른 고객 프로필을 가지고 있다는 것을 알더라도 교차 프로모션 메시징을 보낼 수 없습니다.</td>
        <td>사용자가 워크스페이스 내에 여러 앱을 가지고 있다는 것을 알면 교차 프로모션 메시징을 보낼 수 있습니다.<br><br>앱 간의 사용자 데이터를 참조할 수 있습니다. 예를 들어, John이 앱 1과 관련된 X 속성과 앱 2와 관련된 Y 속성을 가지고 있을 때, 두 가지를 하나의 Campaign에서 참조할 수 있습니다.</td>
        <td>사람의 실수 여지가 더 많습니다. 실수로 여러 앱 인스턴스에 걸쳐 사용자를 타겟팅할 수 있습니다.<br><br>인앱 메시지를 보내려면 앱별 커스텀 이벤트가 있어야 합니다. 그래야 하나의 Campaign이 실수로 다른 앱에 표시되지 않습니다. 예를 들어, <code>app_1_action</code> 대 <code>app_2_action</code>입니다.</td>
    </tr>
    <tr>
        <th scope="row">커스텀 이벤트 및 속성</th>
        <td>커스텀 속성과 이벤트가 특정 앱 인스턴스에만 해당되도록 보장됩니다.</td>
        <td>워크스페이스 간에 사용자 행동을 추적할 수 없습니다.<br><br><b>팁:</b> 여러 Currents 커넥터를 활용하여 이를 달성할 수 있습니다.</td>
        <td>워크스페이스 내 모든 앱 인스턴스에 걸쳐 사용자 행동을 추적할 수 있습니다.</td>
        <td>커스텀 속성과 이벤트가 모든 앱 인스턴스에 적용되므로, 고객 프로필에서 어떤 데이터가 어떤 앱 인스턴스와 관련 있는지 구별하기 어려울 수 있습니다. 예를 들어, "date_of_parking"이 앱 1과 관련이 있는지 앱 2와 관련이 있는지 알기 어렵습니다. 이를 해결하려면 잘 구조화된 명명 규칙을 사용하세요.</td>
    </tr>
    <tr>
        <th scope="row">최대 게재빈도 설정</th>
        <td>최대 게재빈도 설정을 각 앱 인스턴스(워크스페이스 기반)에 대해 별도로 정의할 수 있습니다.</td>
        <td>해당 없음</td>
        <td>해당 없음</td>
        <td>최대 게재빈도 설정은 앱별이 아닌 모든 Campaigns에 적용되므로, 고객에게 과도한 메시지를 보내는 것을 방지하기가 더 어렵습니다.</td>
    </tr>
    <tr>
        <th scope="row">고객 프로필의 구독 상태</th>
        <td>각 고객 프로필의 구독 상태는 각 앱 인스턴스에 고유합니다.</td>
        <td>해당 없음</td>
        <td>해당 없음</td>
        <td>고객 프로필의 구독 상태는 앱 인스턴스 간에 결합됩니다.<br><br><b>팁:</b> <a href='/docs/user_guide/data/activation/attributes/custom_attributes'>커스텀 속성</a> 을 사용하여 사용자의 구독을 관리할 수 있습니다.</td>
    </tr>
    <tr>
        <th scope="row">회사 사용자 권한</th>
        <td>해당 없음</td>
        <td>대시보드 사용자의 <a href='/docs/user_guide/administer/global/user_management/permissions'>사용자 권한</a> 업데이트는 사용자가 접근해야 하는 각 워크스페이스에 대해 별도로 수행해야 합니다.</td>
        <td>대시보드 사용자에 대해 <a href='/docs/user_guide/administer/global/user_management/permissions'>사용자 권한</a> 을 한 번 설정하면, 워크스페이스 내 모든 앱 인스턴스에 대해 동일한 권한을 갖게 됩니다.</td>
        <td>해당 없음</td>
    </tr>
    <tr>
        <th scope="row">콘텐츠 복제</th>
        <td>해당 없음</td>
        <td>Segments 및 콘텐츠 카드 캠페인과 같은 일부 콘텐츠는 워크스페이스 간에 복사할 수 없습니다.</td>
        <td><a href='{{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces'>워크스페이스 간에 Campaigns, Canvases 및 랜딩 페이지를 복사</a> 할 수 있습니다. 지원되는 콘텐츠에는 적격한 채널의 Campaigns 및 Canvases뿐만 아니라 랜딩 페이지, 이메일 템플릿, 기능 플래그 및 Content Blocks가 포함됩니다.<br><br>Segments, Campaigns, Canvases 및 랜딩 페이지를 복제하여 한 앱 인스턴스의 콘텐츠를 다른 앱 인스턴스에서 재사용할 수 있습니다.</td>
        <td>해당 없음</td>
    </tr>
    <tr>
        <th scope="row">분석</th>
        <td>홈 페이지에서 전체 통계가 정확합니다.</td>
        <td>해당 없음</td>
        <td>해당 없음</td>
        <td>홈 페이지에서 전체 통계가 워크스페이스 내 모든 앱 인스턴스에 대해 집계됩니다.</td>
    </tr>
    </tbody>
</table>

{% alert note %}
모든 앱을 볼 때와 단일 앱을 볼 때 MAU가 어떻게 다른지에 대해서는 [월간 활성 사용자]({{site.baseurl}}/user_guide/analytics/dashboards/home#monthly-active-users)를 참조하세요.
{% endalert %}

## 모범 사례 {#best-practices}

### 테스트 워크스페이스 설정 {#set-up-a-testing-workspace}

모범 사례로, 프로덕션 워크스페이스(실제 사용자에게 메시지를 전송하는 워크스페이스)를 설정할 때마다 테스트 워크스페이스도 함께 설정해야 합니다. 테스트 워크스페이스는 실제 사용자 데이터가 없는 프로덕션 워크스페이스의 복제본입니다.

이것이 모범 사례로 간주되는 이유는 다음과 같습니다:

- **변경 사항 격리:** 라이브 프로덕션 환경에 영향을 주지 않고 격리된 환경에서 새로운 기능, 구성 또는 업데이트를 테스트할 수 있습니다. 이렇게 하면 테스트 중에 문제가 발생하더라도 프로덕션 환경은 영향을 받지 않습니다.
- **정확한 테스트:** 테스트 환경의 데이터를 실제 데이터에 대한 걱정 없이 제어하고 조작할 수 있으므로 보다 정확한 테스트가 가능합니다.
- **디버깅:** 프로덕션 환경에 미치는 영향을 걱정하지 않고 자유롭게 환경을 조작할 수 있으므로 테스트 환경에서 문제를 디버깅하기가 더 쉽습니다.
- **교육:** 새로운 팀원이 실수해도 실제 결과에 영향을 미치지 않는 안전한 환경에서 워크스페이스에 익숙해질 수 있습니다.

{% alert tip %}
테스트 워크스페이스와 프로덕션 워크스페이스를 설정하는 순서는 특정 필요와 상황에 따라 달라질 수 있습니다. 그러나 일반적으로 테스트 워크스페이스를 먼저 설정하는 것이 좋습니다. 이를 통해 프로덕션 워크스페이스에 적용하기 전에 기능, 구성 및 업데이트를 테스트할 수 있습니다. 테스트와 결과에 만족한 후에 프로덕션 워크스페이스를 설정하면 됩니다.
{% endalert %}

### 관리자 추가 {#add-administrators}

하나의 워크스페이스에 관리자 권한을 가진 Braze 사용자가 두 명 이상 있어야 합니다. 이렇게 하면 조직 내에서 다른 사용자의 권한을 관리할 수 있는 충분한 인원을 확보할 수 있습니다.

## 다음 단계 {#next-steps}

워크스페이스 플랜을 결정한 후에는 워크스페이스를 생성하고 앱 인스턴스를 추가할 차례입니다. 단계별 안내는 [워크스페이스 생성 및 관리]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces)를 확인하세요.