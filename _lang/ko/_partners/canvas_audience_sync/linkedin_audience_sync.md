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

Braze Audience Sync to LinkedIn을 사용하면 브랜드는 Braze 통합에서 LinkedIn 고객 목록에 사용자 데이터를 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달할 수 있습니다. 사용자 데이터를 기반으로 BRAZE 캔버스에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 일반적으로 사용하는 모든 기준을 이제 LinkedIn 고객 목록에서 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다.

**오디언스 동기화의 일반적인 사용 사례는 다음과 같습니다**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

이 기능을 통해 브랜드는 LinkedIn과 공유되는 특정 퍼스트파티 데이터를 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합에 대해 최대한 신중하게 고려합니다. 자세한 내용은 [개인정보 보호정책](https://www.braze.com/privacy)을 참조하세요.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## 전제 조건 {#prerequisites}

Canvas에서 LinkedIn 오디언스 동기화 단계를 설정하기 전에 다음 항목이 생성, 완료 또는 수락되었는지 확인해야 합니다.

| 요구 사항 | Origin | 설명 |
| --- | --- | --- |
| LinkedIn 광고 계정 | [LinkedIn](https://www.linkedin.com/campaignmanager) | 브랜드에 연결된 활성 LinkedIn 광고 계정이 필요합니다.<br><br>해당 계정에 액세스하고 사용하기 위해 관련 LinkedIn 이용약관에 동의했는지, 그리고 LinkedIn 관리자가 오디언스를 관리할 수 있는 적절한 권한을 부여했는지 확인하세요. |
| LinkedIn 약관 및 정책 | LinkedIn | LinkedIn 오디언스 동기화 사용과 관련하여 LinkedIn에서 요구하는 모든 약관, 정책, 가이드라인 및 설명서(여기에 참조로 포함된 약관, 정책, 가이드라인 및 설명서 포함)를 준수하는 데 동의해야 합니다. 여기에는 LinkedIn의 서비스 약관, 광고 계약, 데이터 처리 계약 및 전문가 커뮤니티 가이드라인이 포함될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: LinkedIn에 연결하기 {#step-1-connect-to-linkedin}

{% alert important %}
LinkedIn을 Braze 계정에 연결하려면 ["관리자" 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)이 있어야 합니다.
{% endalert %}

Braze 대시보드에서 **기술 파트너**로 이동하여 **LinkedIn**을 선택합니다. **LinkedIn 오디언스 동기화** 섹션에서 **LinkedIn 연결**을 선택합니다.

![Braze의 LinkedIn 기술 파트너 페이지에는 개요 섹션과 LinkedIn 연결 버튼이 있는 LinkedIn 오디언스 동기화 섹션이 포함되어 있습니다.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

그러면 LinkedIn OAuth 페이지로 리디렉션되어 오디언스 동기화 통합과 관련된 권한에 대해 Braze를 승인하게 됩니다. **확인**을 선택하면 Braze로 다시 리디렉션되어 동기화할 LinkedIn 광고 계정을 선택할 수 있습니다.

![연결할 광고 계정으로 'Braze Self Service'가 선택되어 있습니다.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

성공적으로 연결되면 파트너 페이지로 돌아가며, 연결된 계정을 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![성공적으로 연결된 LinkedIn 계정.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

LinkedIn 연결은 Braze 워크스페이스 수준에서 적용됩니다. LinkedIn 관리자가 LinkedIn 광고 계정에서 사용자를 제거하면 Braze가 유효하지 않은 토큰을 감지합니다. 그 결과, LinkedIn을 사용하는 활성 Canvases에 오류가 표시되며 Braze가 사용자를 동기화할 수 없게 됩니다.

### 2단계: Canvas 진입 기준 구성하기 {#step-2-configure-your-canvas-entry-criteria}

광고 추적을 위한 오디언스를 구축할 때, 사용자의 선호도에 따라 특정 사용자를 포함하거나 제외하고, [CCPA](https://oag.ca.gov/privacy/ccpa)에 따른 "판매 또는 공유 거부" 권리와 같은 개인정보 보호법을 준수하고자 할 수 있습니다. 마케터는 Canvas 진입 기준 내에서 사용자 자격에 대한 관련 필터를 구현해야 합니다. 다음 옵션이 도움이 될 수 있습니다.

[Braze SDK를 통해 iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)를 수집한 경우, **광고 추적 활성화** 필터를 사용할 수 있습니다. 값을 `true`로 선택하면 옵트인한 사용자만 오디언스 동기화 대상으로 보낼 수 있습니다.

![필터 '광고 추적 활성화가 true'인 진입 오디언스.]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

`opt-ins`, `opt-outs`, `Do Not Sell Or Share` 또는 기타 관련 커스텀 속성을 수집하는 경우, Canvas 진입 기준에 필터로 포함해야 합니다.

![진입 오디언스가 'opted_in_marketing'이 'true'인 Canvas.]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Braze 플랫폼 내에서 이러한 데이터 보호법을 준수하는 방법에 대해 자세히 알아보려면 [데이터 보호 기술 지원]({{site.baseurl}}/dp-technical-assistance)을 참조하세요.

### 3단계: LinkedIn과 오디언스 동기화 단계 추가하기 {#step-3-add-an-audience-sync-step-with-linkedin}

Canvas에 컴포넌트를 추가하고 오디언스 동기화를 선택합니다. **커스텀 오디언스** 버튼을 클릭하여 컴포넌트 편집기를 엽니다.

![사용 가능한 컴포넌트 목록이 있는 Canvas 편집기.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![선택된 오디언스 동기화 컴포넌트.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### 4단계: 동기화 설정 {#step-4-sync-setup}

원하는 오디언스 동기화 파트너로 **LinkedIn**을 선택합니다.

![여러 파트너를 선택할 수 있는 오디언스 동기화 설정 세부 정보.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

그런 다음 원하는 LinkedIn 광고 계정을 선택합니다. **새 오디언스 또는 기존 오디언스 선택** 드롭다운에서 새 오디언스 또는 기존 오디언스의 이름을 입력합니다.

![Braze가 광고 계정으로 선택된 LinkedIn 오디언스 동기화.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab 새 오디언스 만들기 %}

**새 오디언스 만들기**<br>
새 오디언스의 이름을 입력하고, **오디언스에 사용자 추가**를 선택한 다음, LinkedIn과 동기화할 필드를 선택합니다. 이 통합에서는 현재 다음을 지원합니다:
- 이메일
- 이름 및 성
- Android GAID

다음으로, 단계 편집기 하단의 **오디언스 만들기** 버튼을 클릭하여 오디언스를 저장합니다.

![선택된 Braze 광고 계정, 'leads' 오디언스, 오디언스에 사용자를 추가하는 작업, 그리고 이메일, Android GAID, 이름 및 성을 매칭 필드로 사용하는 예시 'leads' 오디언스.]({% image_buster /assets/img/linkedin/linkedin10.png %})

오디언스가 성공적으로 생성되거나 오류가 발생하면 Braze가 단계 편집기 상단에 알림을 표시합니다. 오디언스가 초안 모드로 생성되었으므로, 사용자는 나중에 Canvas 여정에서 사용자 제거를 위해 이 오디언스를 참조할 수 있습니다.

!['leads' 오디언스가 생성되었다는 확인 메시지.]({% image_buster /assets/img/linkedin/linkedin9.png %})

새 오디언스로 Canvas를 시작하면, Braze는 사용자가 오디언스 동기화 컴포넌트에 진입할 때 거의 실시간으로 사용자를 동기화합니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}

**기존 오디언스와 동기화**<br>
Braze는 기존 LinkedIn 오디언스에 사용자를 추가하여 해당 오디언스가 최신 상태인지 확인하는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에서 기존 오디언스 이름을 입력하고 **오디언스에 추가**합니다. 그러면 Braze가 사용자가 오디언스 동기화 컴포넌트에 진입할 때 거의 실시간으로 사용자를 추가합니다.

![커스텀 오디언스 Canvas 단계의 확장된 보기. 여기에서 원하는 광고 계정과 기존 오디언스가 선택되어 있습니다.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### 5단계: Canvas 시작하기 {#step-5-launch-canvas}

LinkedIn에 대한 오디언스 동기화를 구성한 후 Canvas를 시작합니다! 새 오디언스가 생성되고, 오디언스 동기화 단계를 통과하는 사용자가 LinkedIn의 이 오디언스에 전달됩니다. Canvas에 후속 컴포넌트가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행합니다.

광고 계정으로 이동하여 내비게이션의 **에셋** 섹션에서 **오디언스**를 선택하면 LinkedIn에서 오디언스를 확인할 수 있습니다. **오디언스** 페이지에서 300명 이상의 멤버에 도달한 후 각 오디언스의 규모를 확인할 수 있습니다.

![지정된 오디언스에 대한 다음 측정기준을 나열하는 LinkedIn 페이지.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## 사용자 동기화 및 사용량 제한 고려 사항 {#user-syncing-and-rate-limit-considerations}

사용자가 오디언스 동기화 단계에 도달하면, Braze는 LinkedIn의 API 사용량 제한을 준수하면서 거의 실시간으로 사용자를 동기화합니다. Braze는 LinkedIn으로 전송하기 전에 5초마다 가능한 한 많은 사용자를 일괄 처리합니다.

LinkedIn의 API 사용량 제한은 초당 최대 10개의 쿼리와 요청당 100,000명의 사용자를 허용합니다. 고객이 이 제한에 도달하면, Braze는 약 13시간 동안 동기화를 재시도합니다. 그래도 동기화가 불가능한 경우, Braze는 해당 사용자를 오류 발생 사용자 측정기준에 표시합니다.

## 분석 이해하기 {#understanding-analytics}

다음 표에는 오디언스 동기화 구성 요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| ------ | ----------- |
| 진입 | LinkedIn에 동기화하기 위해 이 구성 요소에 진입한 사용자 수입니다. |
| 다음 단계로 진행 | 다음 구성 요소가 있는 경우 다음 구성 요소로 진행한 사용자 수입니다. Canvas 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| 동기화된 사용자 | LinkedIn에 성공적으로 동기화된 사용자 수입니다. |
| 동기화되지 않은 사용자 | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| 대기 중인 사용자 | 현재 Braze에서 LinkedIn으로 동기화하기 위해 처리 중인 사용자 수입니다. |
| 오류 발생 사용자 | 약 13시간의 재시도 후 API 오류로 인해 LinkedIn에 동기화되지 않은 사용자 수입니다. 오류의 잠재적 원인으로는 유효하지 않은 LinkedIn 토큰 또는 LinkedIn에서 오디언스가 삭제된 경우 등이 있습니다. |
| Canvas 종료 | Canvas를 종료한 사용자 수입니다. Canvas의 마지막 단계가 오디언스 동기화 구성 요소인 경우 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="분석 이해하기" }

{% alert important %}
동기화된 사용자 및 오류 발생 사용자 측정기준은 각각 대량 플러셔 및 13시간 재시도로 인해 보고에 지연이 발생할 수 있다는 점을 기억하세요.
{% endalert %}

{% alert important %}
LinkedIn은 자체 플랫폼 내에서 매치율에 대한 추가 측정기준을 제공합니다. 특정 오디언스 동기화의 매치를 검토하려면 오디언스 동기화 단계 측정기준을 선택하여 **Canvas 단계 세부 정보** 페이지로 이동하세요.
<br><br>
파트너로 **LinkedIn**, 광고 계정, 오디언스를 선택하면 LinkedIn의 오디언스 규모와 매치율을 확인할 수 있습니다.

![진입한 사용자 10,000명이 표시된 오디언스 동기화 단계 측정기준 예시.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

### LinkedIn에서 오디언스 크기가 채워지는 데 얼마나 걸리나요? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

LinkedIn 계정에서 오디언스를 확인하기까지 최대 48시간이 소요될 수 있습니다.

### LinkedIn 광고 계정에서 오디언스 크기가 표시되려면 최소 오디언스 규모는 얼마인가요? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

LinkedIn 계정에서 오디언스 크기가 표시되려면 최소 300명의 멤버가 포함되어야 합니다.

### 유효하지 않은 토큰 오류가 발생하면 어떻게 해야 하나요? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

LinkedIn 파트너 페이지에서 LinkedIn 계정을 연결 해제한 후 다시 연결할 수 있습니다. LinkedIn 관리자에게 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 확인하세요.

### Canvas가 실행되지 않는 이유는 무엇인가요? {#why-is-my-canvas-not-allowed-to-launch}

LinkedIn 파트너 페이지에서 LinkedIn 광고 계정이 Braze에 성공적으로 연결되었는지 확인하세요. 그런 다음 광고 계정을 선택하고, 새 오디언스의 이름을 입력하고, 매칭할 필드를 선택했는지 확인하세요.

### 사용자를 LinkedIn에 전달한 후 매칭 여부를 어떻게 확인할 수 있나요? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn은 대시보드에서 매칭률 관련 정보를 제공합니다. LinkedIn의 **오디언스** 섹션에서 확인할 수 있습니다. 또한 Audience Sync 단계의 캔버스 단계 세부 정보에서 LinkedIn 오디언스의 매칭률을 확인할 수 있습니다.

### LinkedIn에서 지원할 수 있는 오디언스 수는 몇 개인가요? {#how-many-audiences-can-linkedin-support}

현재 LinkedIn 광고 계정의 오디언스 수에는 제한이 없습니다.

### Segment가 BUILDING 상태에서 멈추고 업데이트되지 않는 이유는 무엇인가요? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Segment는 초안 또는 활성 캠페인에서 30일 동안 지속적으로 사용되지 않으면 미사용으로 간주되어 ARCHIVED로 설정됩니다. 이로 인해 ARCHIVED 상태의 Segment에 업데이트가 스트리밍되면 BUILDING 상태로 전환되고, 다시 아카이브되기 직전에 미사용 Segment에 새로운 업데이트가 스트리밍되면서 Segment가 BUILDING 상태에서 "멈춘" 것처럼 보일 수 있습니다.