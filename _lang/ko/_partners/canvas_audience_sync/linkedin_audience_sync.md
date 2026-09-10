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

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

이 기능을 통해 브랜드는 LinkedIn과 공유되는 특정 퍼스트파티 데이터를 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합에 대해 최대한 신중하게 고려합니다. 자세한 내용은 [개인정보 보호정책](https://www.braze.com/privacy)을 참조하세요.

## 사전 요구 사항 {#prerequisites}

Canvas에서 LinkedIn 오디언스 동기화 단계를 설정하기 전에 다음 항목이 생성, 완료 또는 수락되었는지 확인해야 합니다.

| 요구 사항 | Origin | 설명 |
| --- | --- | --- |
| 오디언스 동기화 Pro | Braze | LinkedIn은 [오디언스 동기화 Pro]({{site.baseurl}}/partners/canvas_audience_sync/overview#audience-sync-pro) 파트너입니다. 광고 계정을 연결하기 전에 **기술 파트너** 페이지에서 오디언스 동기화 Pro 할당량에 LinkedIn을 선택하세요. 구매에 대한 자세한 내용은 Braze 계정 매니저에게 문의하세요. |
| LinkedIn 광고 계정 | [LinkedIn](https://www.linkedin.com/campaignmanager) | 브랜드에 연결된 활성 LinkedIn 광고 계정이 필요합니다.<br><br>해당 계정에 액세스하고 사용하기 위해 관련 LinkedIn 이용 약관에 동의했는지 확인하세요. LinkedIn 관리자가 다음 광고 계정 역할 중 하나를 부여해야 합니다: Account Billing Admin, Account Manager, Campaign Manager 또는 Creative Manager. |
| LinkedIn 약관 및 정책 | LinkedIn | LinkedIn 오디언스 동기화 사용과 관련하여 LinkedIn이 요구하는 약관, 정책, 가이드라인, 문서(여기에 참조로 포함된 모든 약관, 정책, 가이드라인, 문서를 포함)를 준수하는 데 동의해야 합니다. 여기에는 LinkedIn의 서비스 약관, 광고 계약, 데이터 처리 계약, 전문가 커뮤니티 가이드라인이 포함될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사전 요구 사항" }

## 통합 {#integration}

### 1단계: LinkedIn 연결 {#step-1-connect-to-linkedin}

{% alert important %}
LinkedIn을 Braze 계정에 연결하려면 ["관리자" 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)이 있어야 합니다.
{% endalert %}

Braze 대시보드에서 **기술 파트너**로 이동하여 **LinkedIn**을 선택합니다. **LinkedIn 오디언스 동기화** 섹션에서 **LinkedIn 연결**을 선택합니다.

그러면 LinkedIn OAuth 페이지로 리디렉션되어 오디언스 동기화 통합과 관련된 권한에 대해 Braze를 승인할 수 있습니다. **확인**을 선택하면 Braze로 다시 리디렉션되어 동기화할 LinkedIn 광고 계정을 선택할 수 있습니다.

![연결할 광고 계정으로 'Braze Self Service'가 선택된 화면.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

성공적으로 연결되면 파트너 페이지로 돌아가며, 연결된 계정을 확인하고 기존 계정을 연결 해제할 수 있습니다.

![성공적으로 연결된 LinkedIn 계정.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

LinkedIn 연결은 Braze 워크스페이스 수준에서 적용됩니다. LinkedIn 관리자가 LinkedIn 광고 계정에서 사용자를 제거하면 Braze가 유효하지 않은 토큰을 감지합니다. 그 결과 LinkedIn을 사용하는 활성 Canvases에 오류가 표시되며 Braze가 사용자를 동기화할 수 없게 됩니다.

### 2단계: Canvas 진입 기준 구성 {#step-2-configure-your-canvas-entry-criteria}

광고 추적 기술을 위한 오디언스를 구축할 때 사용자의 선호도에 따라 특정 사용자를 포함하거나 제외하고, [CCPA](https://oag.ca.gov/privacy/ccpa)의 "판매 또는 공유 거부" 권리와 같은 개인정보 보호법을 준수할 수 있습니다. 마케터는 Canvas 진입 기준 내에서 사용자 적격성에 대한 관련 필터를 구현해야 합니다. 다음 옵션이 도움이 될 수 있습니다.

[Braze SDK를 통해 iOS IDFA를 수집]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)한 경우 **광고 추적 기술 활성화됨** 필터를 사용할 수 있습니다. 값을 `true`로 선택하면 옵트인한 사용자만 오디언스 동기화 대상으로 전송합니다. iOS 광고 ID는 LinkedIn 오디언스 동기화의 매치 필드로 지원되지 않습니다.

!['광고 추적 기술 활성화됨이 true'인 필터가 포함된 진입 오디언스.]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

`opt-ins`, `opt-outs`, `Do Not Sell Or Share` 또는 기타 관련 커스텀 속성을 수집하는 경우 Canvas 진입 기준에 필터로 포함해야 합니다:

!['opted_in_marketing'이 'true'인 진입 오디언스가 있는 Canvas.]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Braze 플랫폼 내에서 이러한 데이터 보호법을 준수하는 방법에 대해 자세히 알아보려면 [데이터 보호 기술 지원]({{site.baseurl}}/dp-technical-assistance)을 참조하세요.

### 3단계: LinkedIn으로 오디언스 동기화 단계 추가 {#step-3-add-an-audience-sync-step-with-linkedin}

Canvas에 컴포넌트를 추가하고 오디언스 동기화를 선택합니다. **커스텀 오디언스** 버튼을 클릭하여 컴포넌트 편집기를 엽니다.

### 4단계: 동기화 설정 {#step-4-sync-setup}

1. 원하는 오디언스 동기화 파트너로 **LinkedIn**을 선택합니다.
2. 원하는 LinkedIn 광고 계정을 선택합니다.
3. **신규 또는 기존 오디언스 선택** 드롭다운에서 신규 또는 기존 오디언스의 이름을 입력합니다.

{% tabs %}
{% tab 신규 오디언스 생성 %}

#### 신규 오디언스 생성 {#create-a-new-audience}

새 오디언스의 이름을 입력하고 **오디언스에 사용자 추가**를 선택한 다음 LinkedIn과 동기화할 필드를 선택합니다. 이 통합을 위해 Braze는 현재 다음을 지원합니다:
- 이메일
- 이름 및 성(이름 매칭을 사용하는 경우 둘 다 필수)
- Android GAID

iOS 광고 ID는 LinkedIn의 매치 필드로 지원되지 않습니다.

다음으로, 단계 편집기 하단의 **오디언스 생성** 버튼을 클릭하여 오디언스를 저장합니다.

![선택한 Braze 광고 계정, 'leads' 오디언스, 오디언스에 사용자를 추가하는 액션, 그리고 매치할 필드로 이메일, Android GAID, 이름 및 성이 설정된 예시 'leads' 오디언스.]({% image_buster /assets/img/linkedin/linkedin10.png %})

오디언스가 성공적으로 생성되거나 오류가 발생하면 Braze가 단계 편집기 상단에 알림을 표시합니다. 단계 편집기에서 오디언스를 저장한 후 나중에 Canvas 여정에서 사용자 제거를 위해 이 오디언스를 참조할 수 있습니다.

!['leads' 오디언스가 생성되었음을 확인하는 알림.]({% image_buster /assets/img/linkedin/linkedin9.png %})

새 오디언스로 Canvas를 시작하면 사용자가 오디언스 동기화 단계에 진입할 때 Braze가 [일괄 처리 및 지연 시간]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency)에 따라 사용자를 동기화합니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}

#### 기존 오디언스와 동기화 {#sync-with-an-existing-audience}

Braze는 기존 LinkedIn 오디언스에 사용자를 추가하거나 제거하여 해당 오디언스를 최신 상태로 유지하는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에 기존 오디언스 이름을 입력한 다음 **오디언스에 추가** 또는 **오디언스에서 제거**를 선택합니다. Braze는 사용자가 오디언스 동기화 단계에 진입할 때 [일괄 처리 및 지연 시간]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency)에 따라 사용자를 동기화합니다.

![커스텀 오디언스 Canvas 단계의 확장 보기. 여기서 원하는 광고 계정과 기존 오디언스가 선택되어 있습니다.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### 5단계: Canvas 시작 {#step-5-launch-canvas}

LinkedIn으로의 오디언스 동기화를 구성한 후 Canvas를 시작합니다! 새 오디언스가 생성되고 오디언스 동기화 단계를 통해 흐르는 사용자가 LinkedIn의 이 오디언스에 전달됩니다. Canvas에 후속 컴포넌트가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행합니다.

광고 계정으로 이동하여 탐색의 **에셋** 섹션에서 **오디언스**를 선택하면 LinkedIn에서 오디언스를 볼 수 있습니다. **오디언스** 페이지에서 300명 이상의 멤버에 도달한 후 각 오디언스의 크기를 확인할 수 있습니다.

![해당 오디언스에 대한 다음 측정기준을 나열하는 LinkedIn 페이지.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## 사용자 동기화 및 사용량 제한 고려 사항 {#user-syncing-and-rate-limit-considerations}

사용자가 오디언스 동기화 단계에 도달하면, Braze는 LinkedIn으로 전송하기 전에 배치 처리를 위해 대기줄에 추가합니다. Braze가 배치를 처리하는 방식에 대한 자세한 내용은 [배치 처리 및 지연 시간]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency)을 참조하세요.

Braze는 LinkedIn에 요청당 최대 2,000명의 사용자를 전송합니다. LinkedIn의 API 사용량 제한이 계정에 적용되면 Braze는 약 13시간 동안 동기화를 재시도합니다. 그래도 동기화가 불가능한 경우, Braze는 해당 사용자를 Users Errored 측정기준에 표시합니다.

## 분석 이해하기 {#understanding-analytics}

다음 표에는 오디언스 싱크 구성 요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| ------ | ----------- |
| 진입함 | LinkedIn에 동기화하기 위해 이 구성 요소에 진입한 사용자 수입니다. |
| 다음 단계로 진행 | 다음 구성 요소가 있는 경우 해당 구성 요소로 진행한 사용자 수입니다. Canvas 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행합니다. |
| 동기화된 사용자 | LinkedIn에 성공적으로 동기화된 사용자 수입니다. |
| 동기화되지 않은 사용자 | 일치시킬 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| 대기 중인 사용자 | 현재 Braze에서 LinkedIn으로 동기화하기 위해 처리 중인 사용자 수입니다. |
| 오류 발생 사용자 | 약 13시간의 재시도 후 API 오류로 인해 LinkedIn에 동기화되지 않은 사용자 수입니다. 오류의 잠재적 원인에는 유효하지 않은 LinkedIn 토큰이거나 LinkedIn에서 오디언스가 삭제된 경우가 포함될 수 있습니다. |
| Canvas 퇴장 | Canvas를 퇴장한 사용자 수입니다. Canvas의 마지막 단계가 오디언스 싱크 구성 요소인 경우 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="분석 이해하기" }

{% alert important %}
동기화된 사용자 및 오류 발생 사용자 측정기준은 각각 배치 처리와 13시간 재시도로 인해 보고가 지연될 수 있습니다.
{% endalert %}

{% alert important %}
LinkedIn은 플랫폼 내에서 매치율에 대한 추가 측정기준을 제공합니다. 특정 오디언스 싱크의 매치를 검토하려면 오디언스 싱크 단계 측정기준을 선택하여 **캔버스 단계 세부 정보** 페이지로 이동합니다.
<br><br>
파트너로 **LinkedIn**을 선택하고 광고 계정과 오디언스를 선택하면 LinkedIn에서 제공하는 오디언스 크기와 매치율을 확인할 수 있습니다.

![10,000명의 진입 사용자가 있는 오디언스 싱크 단계 측정기준의 예시.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

### LinkedIn에서 오디언스 크기가 채워지는 데 얼마나 걸리나요? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

LinkedIn 계정 내에서 오디언스를 확인하기까지 최대 48시간이 소요될 수 있습니다.

### LinkedIn 광고 계정에서 오디언스 크기가 채워지기 위한 최소 오디언스 크기는 얼마인가요? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

LinkedIn 계정에서 오디언스 크기가 채워지려면 오디언스에 최소 300명의 멤버가 포함되어야 합니다.

### 유효하지 않은 토큰 오류를 받으면 어떻게 해야 하나요? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

LinkedIn 파트너 페이지에서 LinkedIn 계정을 연결 해제한 후 다시 연결할 수 있습니다. LinkedIn 관리자에게 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 확인하세요.

### Canvas를 시작할 수 없는 이유는 무엇인가요? {#why-is-my-canvas-not-allowed-to-launch}

LinkedIn 파트너 페이지에서 LinkedIn 광고 계정이 Braze에 성공적으로 연결되었는지 확인하세요. 그런 다음 광고 계정을 선택하고, 새 오디언스의 이름을 입력하고, 매칭할 필드를 선택했는지 확인하세요.

### 사용자를 LinkedIn에 전달한 후 사용자가 매칭되었는지 어떻게 알 수 있나요? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn은 대시보드에서 매칭률에 대한 정보를 제공합니다. LinkedIn의 **오디언스** 섹션에서 확인할 수 있습니다. Audience Sync 단계의 Canvas 단계 세부 정보에서 LinkedIn 오디언스의 매칭률을 확인할 수 있습니다.

### LinkedIn에서 지원하는 오디언스 수는 몇 개인가요? {#how-many-audiences-can-linkedin-support}

현재 LinkedIn 광고 계정의 오디언스 수에는 제한이 없습니다.

### Segment가 BUILDING 상태에서 멈춰 있고 업데이트되지 않는 이유는 무엇인가요? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Segment는 초안 또는 활성 Campaign에서 30일 동안 지속적으로 사용되지 않으면 사용되지 않는 것으로 간주되어 ARCHIVED로 설정됩니다. 이로 인해, ARCHIVED 상태의 Segment에 업데이트가 스트리밍되면 BUILDING 상태로 전환되고, 다시 보관 처리되기 직전에 사용되지 않는 Segment에 새로운 업데이트가 스트리밍되므로 Segment가 BUILDING 상태에서 "멈춘" 것처럼 보일 수 있습니다.