---
nav_title: LinkedIn
article_title: LinkedIn으로 Canvas 오디언스 동기화
alias: /linkedin_audience_sync/
description: "이 참조 문서에서는 Braze Audience Sync to LinkedIn을 사용하여 행동 트리거, 세분화 등을 기반으로 광고를 전달하는 방법을 다룹니다."
tool:
  - Canvas
page_order: 4

---

# LinkedIn으로 오디언스 동기화 {#audience-sync-to-linkedin}

Braze Audience Sync to LinkedIn을 사용하면 브랜드는 Braze 통합에서 LinkedIn 고객 목록에 사용자 데이터를 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달할 수 있습니다. 사용자 데이터를 기반으로 Braze Canvas에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 일반적으로 사용하는 모든 기준을 이제 LinkedIn 고객 목록에서 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다.

**오디언스 동기화의 일반적인 사용 사례는 다음과 같습니다**:

- 여러 채널을 통해 고가치 사용자를 타겟팅하여 구매 또는 참여를 유도
- 다른 마케팅 채널에 반응이 적은 사용자를 리타겟팅
- 이미 브랜드의 충성 고객인 사용자가 광고를 받지 않도록 억제 오디언스 생성

이 기능을 통해 브랜드는 LinkedIn과 공유되는 특정 퍼스트파티 데이터를 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합에 대해 최대한 신중하게 고려합니다. 자세한 내용은 [개인정보 보호정책](https://www.braze.com/privacy)을 참조하세요.

{% multi_lang_include early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## 필수 조건 {#prerequisites}

Canvas에서 LinkedIn 오디언스 동기화 단계를 설정하기 전에 다음 항목이 생성, 완료 또는 수락되었는지 확인해야 합니다.

| 요구 사항 | 출처 | 설명 |
| --- | --- | --- |
| LinkedIn 광고 계정 | [LinkedIn](https://www.linkedin.com/campaignmanager) | 브랜드에 연결된 활성 LinkedIn 광고 계정.<br><br>해당 계정에 액세스하고 사용하기 위한 관련 LinkedIn 이용약관에 동의했는지, 그리고 LinkedIn 관리자가 오디언스를 관리할 수 있는 적절한 권한을 부여했는지 확인하세요. |
| LinkedIn 약관 및 정책 | LinkedIn | LinkedIn Audience Sync 사용과 관련된 LinkedIn의 필수 약관, 정책, 가이드라인 및 문서(여기에 참조로 포함된 약관, 정책, 가이드라인 및 문서 포함)를 준수하는 데 동의합니다. 여기에는 LinkedIn의 서비스 약관, 광고 계약, 데이터 처리 계약 및 전문 커뮤니티 가이드라인이 포함될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: LinkedIn에 연결 {#step-1-connect-to-linkedin}

{% alert important %}
LinkedIn을 Braze 계정에 연결하려면 ["관리자" 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)이 있어야 합니다.
{% endalert %}

Braze 대시보드에서 **기술 파트너**로 이동하여 **LinkedIn**을 선택합니다. **LinkedIn Audience Sync** 섹션에서 **Connect LinkedIn**을 선택합니다.

![Braze의 LinkedIn 기술 페이지에는 개요 섹션과 Connect LinkedIn 버튼이 있는 LinkedIn Audience Sync 섹션이 있습니다.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

그러면 오디언스 동기화 통합과 관련된 권한을 Braze에 부여하기 위해 LinkedIn OAuth 페이지로 리디렉션됩니다. **Confirm**을 선택하면 Braze로 다시 리디렉션되어 동기화할 LinkedIn 광고 계정을 선택할 수 있습니다.

![연결할 광고 계정으로 "Braze Self Service"가 선택되어 있습니다.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

성공적으로 연결되면 파트너 페이지로 돌아가며, 연결된 계정을 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![성공적으로 연결된 LinkedIn 계정.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

LinkedIn 연결은 Braze 워크스페이스 수준에서 적용됩니다. LinkedIn 관리자가 LinkedIn 광고 계정에서 사용자를 제거하면 Braze는 유효하지 않은 토큰을 감지합니다. 그 결과 LinkedIn을 사용하는 활성 Canvases에 오류가 표시되며, Braze는 사용자를 동기화할 수 없게 됩니다.

### 2단계: Canvas 진입 기준 구성 {#step-2-configure-your-canvas-entry-criteria}

광고 추적을 위한 오디언스를 구축할 때 사용자의 선호도에 따라 특정 사용자를 포함하거나 제외하고, [CCPA](https://oag.ca.gov/privacy/ccpa)의 "판매 또는 공유 금지" 권리와 같은 개인정보 보호법을 준수할 수 있습니다. 마케터는 Canvas 진입 기준 내에서 사용자 자격에 대한 관련 필터를 구현해야 합니다. 아래에 몇 가지 옵션을 나열합니다.

[Braze SDK를 통해 iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection)를 수집한 경우 **Ads Tracking Enabled** 필터를 사용할 수 있습니다. 값을 `true`로 선택하면 옵트인한 사용자만 오디언스 동기화 대상으로 보냅니다.

!["Ads Tracking Enabled is true" 필터가 적용된 진입 오디언스.]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

`opt-ins`, `opt-outs`, `Do Not Sell Or Share` 또는 기타 관련 커스텀 속성을 수집하는 경우 Canvas 진입 기준에 필터로 포함해야 합니다:

![진입 오디언스가 "opted_in_marketing"이 "true"인 Canvas.]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Braze 플랫폼 내에서 이러한 데이터 보호법을 준수하는 방법에 대해 자세히 알아보려면 [데이터 보호 기술 지원]({{site.baseurl}}/dp-technical-assistance/)을 참조하세요.

### 3단계: LinkedIn으로 오디언스 동기화 단계 추가 {#step-3-add-an-audience-sync-step-with-linkedin}

Canvas에 구성요소를 추가하고 Audience Sync를 선택합니다. **Custom Audience** 버튼을 클릭하여 구성요소 편집기를 엽니다.

![사용 가능한 구성요소 목록이 있는 Canvas 편집기.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![선택된 Audience Sync 구성요소.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### 4단계: 동기화 설정 {#step-4-sync-setup}

원하는 Audience Sync 파트너로 **LinkedIn**을 선택합니다.

![여러 파트너를 선택할 수 있는 "오디언스 동기화 설정" 세부 정보.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

그런 다음 원하는 LinkedIn 광고 계정을 선택합니다. **Choose a New or Existing Audience** 드롭다운에서 새 오디언스 또는 기존 오디언스의 이름을 입력합니다.

![광고 계정으로 Braze가 선택된 LinkedIn 오디언스 동기화.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab 새 오디언스 생성 %}

**새 오디언스 생성**<br>
새 오디언스의 이름을 입력하고 **Add Users to Audience**를 선택한 다음 LinkedIn과 동기화할 필드를 선택합니다. 이 통합에서는 현재 다음을 지원합니다:
- 이메일
- 이름 및 성
- Android GAID

그런 다음 단계 편집기 하단의 **Create Audience** 버튼을 클릭하여 오디언스를 저장합니다.

![선택한 Braze 광고 계정이 있는 "leads" 오디언스 예시로, 오디언스에 사용자를 추가하는 동작과 일치시킬 필드로 이메일, Android GAID, 이름 및 성이 표시됩니다.]({% image_buster /assets/img/linkedin/linkedin10.png %})

오디언스가 성공적으로 생성되거나 오류가 발생하면 Braze가 단계 편집기 상단에 알림을 표시합니다. 오디언스가 초안 모드로 생성되었으므로 사용자는 나중에 Canvas 여정에서 사용자 제거를 위해 이 오디언스를 참조할 수 있습니다.

!["leads" 오디언스가 생성되었음을 확인합니다.]({% image_buster /assets/img/linkedin/linkedin9.png %})

새 오디언스로 Canvas를 시작하면 Braze는 사용자가 Audience Sync 구성요소에 진입할 때 거의 실시간으로 동기화합니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}

**기존 오디언스와 동기화**<br>
Braze는 기존 LinkedIn 오디언스에 사용자를 추가하여 해당 오디언스가 최신 상태인지 확인하는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에서 기존 오디언스 이름을 입력하고 **Add to the Audience**를 선택합니다. 그러면 Braze가 사용자가 Audience Sync 구성요소에 진입할 때 거의 실시간으로 사용자를 추가합니다.

![Custom Audience Canvas 단계의 확장된 보기. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### 5단계: Canvas 시작 {#step-5-launch-canvas}

LinkedIn으로의 오디언스 동기화를 구성한 후 Canvas를 시작하면 됩니다! 새 오디언스가 생성되고, Audience Sync 단계를 통과하는 사용자가 LinkedIn의 이 오디언스에 전달됩니다. Canvas에 후속 구성요소가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행합니다.

광고 계정으로 이동하여 내비게이션의 **Assets** 섹션에서 **Audiences**를 선택하면 LinkedIn에서 오디언스를 볼 수 있습니다. **Audiences** 페이지에서 300명 이상의 회원에 도달한 후 각 오디언스의 규모를 확인할 수 있습니다.

![주어진 오디언스에 대한 다음 측정기준을 나열하는 LinkedIn 페이지.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## 사용자 동기화 및 사용량 제한 고려 사항 {#user-syncing-and-rate-limit-considerations}

사용자가 Audience Sync 단계에 도달하면 Braze는 LinkedIn의 API 사용량 제한을 준수하면서 거의 실시간으로 동기화합니다. Braze는 5초마다 가능한 한 많은 사용자를 배치하고 처리한 후 LinkedIn으로 보냅니다.

LinkedIn의 API 사용량 제한은 초당 쿼리 10건, 요청당 사용자 수 100,000명을 넘지 못하도록 설정되어 있습니다. 고객이 이 제한에 도달하면 Braze는 최대 약 13시간 동안 동기화를 재시도합니다. 그래도 동기화가 되지 않으면 Braze는 이러한 사용자를 Users Errored 측정기준 아래에 나열합니다.

## 분석 이해하기 {#understanding-analytics}

다음 표에는 Audience Sync 구성요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| ------ | ----------- |
| Entered | LinkedIn에 동기화하기 위해 이 구성요소에 진입한 사용자 수. |
| Proceeded to Next Step | 다음 구성요소가 있는 경우 다음 구성요소로 진행한 사용자 수. Canvas 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행합니다. |
| Users Synced | LinkedIn에 성공적으로 동기화된 사용자 수. |
| Users Not Synced | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수. |
| Users Pending | 현재 Braze에서 LinkedIn으로 동기화하기 위해 처리 중인 사용자 수. |
| Users Errored | 약 13시간의 재시도 후 API 오류로 인해 LinkedIn에 동기화되지 않은 사용자 수. 오류의 잠재적 원인에는 유효하지 않은 LinkedIn 토큰 또는 LinkedIn에서 오디언스가 삭제된 경우가 포함될 수 있습니다. |
| Exited Canvas | Canvas를 종료한 사용자 수. Canvas의 마지막 단계가 Audience Sync 구성요소인 경우 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="분석 이해하기" }

{% alert important %}
대량 플러셔와 13시간 재시도로 인해 동기화된 사용자 및 오류 발생 사용자 측정기준의 보고에 지연이 있을 수 있습니다.
{% endalert %}

{% alert important %}
LinkedIn은 플랫폼 내에서 매칭률에 대한 추가 측정기준을 제공합니다. 특정 오디언스 동기화의 매칭을 검토하려면 Audience Sync 단계 측정기준을 선택하여 **Canvas Step Details** 페이지로 이동합니다.
<br><br>
파트너로 **LinkedIn**, 광고 계정, 오디언스를 선택하면 LinkedIn의 오디언스 규모와 매칭률을 확인할 수 있습니다.

![입력된 사용자가 10,000명인 Audience Sync 단계 측정기준의 예.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

### LinkedIn에서 오디언스 규모가 채워지는 데 얼마나 걸리나요? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

LinkedIn 계정 내에서 오디언스를 확인하는 데 최대 48시간이 지연될 수 있습니다.

### 광고 계정 내에서 LinkedIn이 채우는 최소 오디언스 규모는 얼마인가요? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

LinkedIn 계정 내에서 오디언스 규모를 채우려면 오디언스에 최소 300명의 회원이 포함되어야 합니다.

### 유효하지 않은 토큰 오류를 받으면 어떻게 해야 하나요? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

LinkedIn 파트너 페이지에서 LinkedIn 계정의 연결을 해제하고 다시 연결할 수 있습니다. 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 LinkedIn 관리자에게 확인하세요.

### Canvas가 시작되지 않는 이유는 무엇인가요? {#why-is-my-canvas-not-allowed-to-launch}

LinkedIn 파트너 페이지에서 LinkedIn 광고 계정이 Braze에 성공적으로 연결되었는지 확인하세요. 그런 다음 광고 계정을 선택하고, 새 오디언스의 이름을 입력하고, 일치시킬 필드를 선택했는지 확인하세요.

### 사용자를 LinkedIn에 전달한 후 사용자가 매칭되었는지 어떻게 알 수 있나요? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn은 대시보드에서 매칭률에 대한 정보를 제공합니다. LinkedIn의 **Audiences** 섹션에서 확인할 수 있습니다. Audience Sync 단계의 Canvas 단계 세부 정보에서 LinkedIn 오디언스의 매칭률을 검토할 수 있습니다.

### LinkedIn은 몇 개의 오디언스를 지원할 수 있나요? {#how-many-audiences-can-linkedin-support}

현재 LinkedIn 광고 계정의 오디언스 수에는 제한이 없습니다.

### Segment가 BUILDING 상태에서 멈추고 업데이트되지 않는 이유는 무엇인가요? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Segment는 초안 또는 활성 Campaign에서 30일 동안 지속적으로 사용되지 않으면 미사용으로 간주되어 ARCHIVED로 설정됩니다. 이로 인해 ARCHIVED된 Segment에 업데이트가 스트리밍되면 BUILDING 상태로 전환되어 Segment가 "멈춘" 것처럼 보일 수 있으며, 다시 아카이브되기 직전에 미사용 Segment에 새 업데이트가 스트리밍됩니다.