---
nav_title: Criteo
article_title: Criteo에 Canvas 오디언스 동기화
description: "이 참조 문서에서는 Braze Audience Sync to Criteo를 사용하여 행동 트리거, 세분화 등을 기반으로 광고를 전달하는 방법을 다룹니다."
page_order: 1
alias: /audience_sync_criteo/

tool:
  - Canvas
---

# Criteo에 오디언스 동기화 {#audience-sync-to-criteo}

Braze Audience Sync to Criteo를 사용하면 브랜드는 자체 Braze 통합에서 사용자 데이터를 Criteo 고객 목록에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달할 수 있습니다. 일반적으로 사용자 데이터를 기반으로 BRAZE 캔버스에서 메시지(푸시, 이메일, 단문 메시지 서비스, 웹훅 등)를 트리거하는 데 사용하는 모든 기준을 이제 Criteo 고객 목록에서 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다.

**오디언스 동기화의 일반적인 사용 사례는 다음과 같습니다:**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

이 기능을 통해 브랜드는 Criteo와 공유하는 특정 퍼스트파티 데이터를 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합에 대해 최대한 신중하게 고려합니다. 자세한 내용은 [개인정보 보호정책](https://www.braze.com/privacy)을 참조하세요.

{% alert important %}
**Audience Sync Pro 면책 조항**<br>
Braze Audience Sync to Criteo는 Audience Sync Pro 통합입니다. 이 통합에 대한 자세한 내용은 Braze 계정 매니저에게 문의하세요. <br>
{% endalert %}

## 사전 요구 사항 {#prerequisites}

Criteo로의 오디언스 동기화를 설정하기 전에 다음 항목이 생성 및/또는 완료되어 있는지 확인해야 합니다.

| 요구 사항 | Origin | 설명 |
| --- | --- | --- |
| Criteo 광고 계정 | [Criteo](https://marketing.criteo.com/) | 브랜드에 연결된 활성 Criteo 광고 계정이 필요합니다.<br><br>Criteo 관리자가 오디언스에 접근할 수 있는 적절한 권한을 부여했는지 확인하세요. |
| [Criteo 광고 가이드라인](https://www.criteo.com/advertising-guidelines/)<br>및<br>[Criteo 브랜드 안전 가이드라인](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | 활성 Criteo 고객으로서, Criteo Campaigns를 시작하기 전에 Criteo의 광고 및 브랜드 안전 가이드라인을 준수할 수 있는지 확인해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사전 요구 사항" }

## 통합 {#integration}

### 1단계: Criteo에 연결하기 {#step-1-connect-to-criteo}

{% alert important %}
Criteo를 Braze 계정에 연결하려면 ["관리자" 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)이 필요합니다.
{% endalert %}

Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Criteo**를 선택합니다. Criteo 오디언스 내보내기 아래에서 **Connect Criteo**를 선택합니다.

![개요 섹션과 Connect Criteo 버튼이 있는 Criteo 섹션을 포함하는 Braze의 Criteo 기술 페이지.]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

오디언스 동기화 통합과 관련된 권한에 대해 Braze를 승인하는 Criteo oAuth 페이지가 나타납니다.

확인을 선택하면 Braze로 다시 리디렉션되어 동기화할 Criteo 광고 계정을 선택할 수 있습니다.

![Criteo에 연결할 수 있는 사용 가능한 광고 계정 목록.]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

성공적으로 연결되면 파트너 페이지로 돌아가며, 연결된 계정을 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![성공적으로 연결된 광고 계정을 보여주는 업데이트된 Criteo 기술 파트너 페이지.]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Criteo 연결은 Braze 워크스페이스 수준에서 적용됩니다. Criteo 관리자가 Criteo 광고 계정에서 사용자를 제거하면 Braze가 유효하지 않은 토큰을 감지합니다. 그 결과, Criteo를 사용하는 활성 Canvases에 오류가 표시되며 Braze가 사용자를 동기화할 수 없게 됩니다.

### 2단계: Canvas 진입 기준 구성하기 {#step-2-configure-your-canvas-entry-criteria}

광고 추적을 위한 오디언스를 구축할 때, 사용자의 선호도에 따라 특정 사용자를 포함하거나 제외하고, [CCPA](https://oag.ca.gov/privacy/ccpa)에 따른 "판매 또는 공유 금지" 권리와 같은 개인정보 보호법을 준수하기 위해 관련 필터를 구현할 수 있습니다. 마케터는 Canvas 진입 기준 내에서 사용자 자격에 대한 관련 필터를 구현해야 합니다. 다음 옵션이 도움이 될 수 있습니다.

[Braze SDK를 통해 iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)를 수집한 경우, 광고 추적 활성화 필터를 사용할 수 있습니다. 값을 true로 선택하면 옵트인한 사용자만 오디언스 동기화 대상으로 전송됩니다.

![광고 추적 활성화가 true로 설정된 Canvas 진입 필터.]({% image_buster /assets/img/criteo/criteo11.png %})

`opt-ins`, `opt-outs`, `Do Not Sell Or Share` 또는 기타 관련 커스텀 속성을 수집하는 경우, Canvas 진입 기준에 필터로 포함해야 합니다.

![오디언스 자격을 위한 커스텀 옵트인 속성을 사용하는 Canvas 진입 필터.]({% image_buster /assets/img/criteo/criteo12.png %})

Braze 플랫폼 내에서 이러한 데이터 보호법을 준수하는 방법에 대해 자세히 알아보려면 [데이터 보호 기술 지원]({{site.baseurl}}/dp-technical-assistance)을 참조하세요.

### 3단계: Criteo와 함께 오디언스 동기화 단계 추가하기 {#step-3-add-an-audience-sync-step-with-criteo}

Canvas에 컴포넌트를 추가하고 **Audience Sync**를 선택합니다.

![Canvas에서 Criteo 오디언스 컴포넌트를 추가하는 이전 단계의 워크플로.]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![Canvas에서 Criteo 오디언스 컴포넌트를 추가하는 이전 단계의 워크플로.]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### 4단계: 동기화 설정 {#step-4-sync-setup}

**Custom Audience** 버튼을 클릭하여 컴포넌트 편집기를 엽니다.

원하는 오디언스 동기화 파트너로 **Criteo**를 선택합니다.

![Criteo가 파트너로 선택된 오디언스 동기화 단계 편집기.]({% image_buster /assets/img/criteo/criteo6.png %})

그런 다음 원하는 Criteo 광고 계정을 선택합니다. **Choose a New or Existing Audience** 드롭다운에서 새 오디언스 또는 기존 오디언스의 이름을 입력합니다.

{% tabs %}
{% tab 새 오디언스 만들기 %}
**새 오디언스 만들기**<br>
새 오디언스의 이름을 입력하고 **Add Users to Audience**를 선택한 다음, Criteo와 동기화할 필드를 선택합니다. 그런 다음 단계 편집기 하단의 **Create Audience** 버튼을 클릭하여 오디언스를 저장합니다.

![커스텀 오디언스 Canvas 단계의 확장된 보기. 여기에서 원하는 광고 계정이 선택되고 새 오디언스가 생성됩니다.]({% image_buster /assets/img/criteo/criteo3.png %})

오디언스가 성공적으로 생성되거나 오류가 발생하면 Braze가 단계 편집기 상단에 알림을 표시합니다. 오디언스가 초안 모드로 생성되었으므로, 사용자는 나중에 Canvas 여정에서 사용자 제거를 위해 이 오디언스를 참조할 수 있습니다.

![Canvas 컴포넌트에서 새 오디언스가 생성된 후 나타나는 알림.]({% image_buster /assets/img/criteo/criteo1.png %})

새 오디언스로 Canvas를 시작하면, Braze는 사용자가 오디언스 동기화 컴포넌트에 진입할 때 거의 실시간으로 사용자를 동기화합니다.
{% endtab %}
{% tab 기존 오디언스와 동기화 %}
**기존 오디언스와 동기화**<br>
Braze는 기존 Criteo 오디언스에 사용자를 추가하여 해당 오디언스를 최신 상태로 유지하는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에서 기존 오디언스 이름을 입력하고 **Add to the Audience**를 선택합니다. 그러면 Braze가 사용자가 오디언스 동기화 컴포넌트에 진입할 때 거의 실시간으로 사용자를 추가합니다.

![커스텀 오디언스 Canvas 단계의 확장된 보기. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### 5단계: Canvas 시작하기 {#step-5-launch-canvas}

Criteo에 대한 오디언스 동기화를 구성한 후 Canvas를 시작합니다! 새 오디언스가 생성되고, 오디언스 동기화 단계를 통과하는 사용자가 Criteo의 이 오디언스에 전달됩니다. Canvas에 후속 컴포넌트가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행합니다.

Criteo에서 오디언스를 확인하려면 광고 매니저 계정으로 이동한 다음 내비게이션의 **Audience Library**에서 Segments를 선택합니다. **Segments** 페이지에서 각 오디언스의 크기가 약 1,000에 도달한 후 확인할 수 있습니다.

![세그먼트, ID, 소스, 유형, 크기, 현재 사용 여부 및 마지막 업데이트를 보여주는 오디언스 라이브러리.]({% image_buster /assets/img/criteo/criteo.png %})

## 사용자 동기화 및 사용량 제한 고려 사항 {#user-syncing-and-rate-limit-considerations}

사용자가 Audience Sync 단계에 도달하면, Braze는 Criteo의 API 사용량 제한을 준수하면서 거의 실시간으로 사용자를 동기화합니다. Braze는 5초마다 가능한 한 많은 사용자를 일괄 처리한 후 Criteo로 전송합니다.

Criteo의 API 사용량 제한은 분당 최대 250건의 요청을 허용합니다. 고객이 이 제한에 도달하면, Braze는 최대 약 13시간 동안 동기화를 재시도합니다. 그래도 동기화가 불가능한 경우, Braze는 해당 사용자를 Users Errored 측정기준에 기록합니다.

## 분석 이해하기 {#understanding-analytics}

다음 표에는 오디언스 동기화 구성 요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| --- | --- |
| 진입 | Criteo에 동기화하기 위해 이 구성 요소에 진입한 사용자 수입니다. |
| 다음 단계로 진행 | 다음 구성 요소가 있는 경우 해당 구성 요소로 진행한 사용자 수입니다. Canvas 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| 동기화된 사용자 | Criteo에 성공적으로 동기화된 사용자 수입니다. |
| 동기화되지 않은 사용자 | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| 대기 중인 사용자 | 현재 Braze에서 Criteo로 동기화하기 위해 처리 중인 사용자 수입니다. |
| 오류 발생 사용자 | 약 13시간의 재시도 후 API 오류로 인해 Criteo에 동기화되지 않은 사용자 수입니다. 오류의 잠재적 원인으로는 유효하지 않은 Criteo 토큰이나 Criteo에서 오디언스가 삭제된 경우 등이 있습니다. |
| Canvas 종료 | Canvas를 종료한 사용자 수입니다. Canvas의 마지막 단계가 오디언스 동기화 구성 요소인 경우 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="분석 이해하기" }

{% alert important %}
동기화된 사용자 및 오류 발생 사용자 측정기준은 각각 대량 플러셔와 13시간 재시도로 인해 보고에 지연이 발생할 수 있다는 점을 기억하세요.
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 유효하지 않은 토큰 오류를 받으면 어떻게 해야 하나요? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Criteo 파트너 페이지에서 Criteo 계정의 연결을 해제한 후 다시 연결하면 됩니다. Criteo 관리자에게 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 확인하세요.

### Canvas를 시작할 수 없는 이유는 무엇인가요? {#why-is-my-canvas-not-allowed-to-launch}

Criteo 파트너 페이지에서 Criteo 광고 계정이 Braze에 성공적으로 연결되었는지 확인하세요. 그런 다음 광고 계정을 선택했는지, 새 오디언스의 이름을 입력했는지, 매칭할 필드를 선택했는지 확인하세요.

### 사용자를 Criteo에 전달한 후 사용자가 매칭되었는지 어떻게 알 수 있나요? {#how-do-i-know-if-users-have-matched-after-passing-users-to-criteo}

Criteo는 자체 데이터 프라이버시 정책에 따라 이 정보를 제공하지 않습니다.

### Criteo는 몇 개의 오디언스를 지원할 수 있나요? {#how-many-audiences-can-criteo-support}

현재 Criteo 계정 내에서 최대 1,000개의 오디언스만 보유할 수 있습니다. 이 한도를 초과하면 Braze에서 새 오디언스를 생성할 수 없다는 알림을 보냅니다. Criteo 광고 계정에서 더 이상 사용하지 않는 오디언스를 제거해야 합니다.