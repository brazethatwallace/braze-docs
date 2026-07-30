---
nav_title: Snapchat
article_title: Snapchat에 Canvas 오디언스 동기화
description: "이 참조 문서에서는 Braze Audience Sync to Snapchat을 사용하여 행동 트리거, 세분화 등을 기반으로 광고를 전달하는 방법을 다룹니다."
page_order: 6
alias: "/audience_sync_snapchat/"

tool:
  - Canvas

---

# Snapchat에 오디언스 동기화 {#audience-sync-to-snapchat}

Braze Audience Sync to Snapchat을 사용하면 브랜드는 Braze 통합의 사용자 데이터를 Snapchat 고객 목록에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달할 수 있습니다. 일반적으로 사용자 데이터를 기반으로 Braze Canvas에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 사용하는 모든 기준을 이제 Snapchat 고객 목록에서 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다.

**오디언스 동기화의 일반적인 사용 사례는 다음과 같습니다.**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

이 기능을 통해 사용자는 Snapchat과 공유되는 특정 퍼스트파티 데이터를 제어할 수 있습니다. Braze에서는 퍼스트파티 데이터를 공유할 수 있는 통합과 공유할 수 없는 통합에 대해 최대한 신중하게 고려합니다. 자세한 내용은 [개인정보 보호정책](https://www.braze.com/privacy)을 참조하세요.

{% alert important %}
**Audience Sync Pro 면책 조항**<br>
Braze Audience Sync to Snapchat은 Audience Sync Pro 통합입니다. 이 통합에 대한 자세한 내용은 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 사전 요구 사항 {#prerequisites}

Canvas에서 Snapchat 오디언스 단계를 설정하기 전에 다음 항목이 생성, 완료 및/또는 승인되었는지 확인해야 합니다.

| 요구 사항 | Origin | 설명 |
| --- | --- | --- |
| Snapchat Business Manager | Snapchat | 브랜드의 Snapchat 자산(예: 광고 계정, 페이지, 앱)을 관리하기 위한 중앙 집중식 도구입니다. |
| Snapchat 광고 계정 | Snapchat | 브랜드의 Snapchat Business Manager에 연결된 활성 Snapchat 광고 계정입니다.<br><br>Snapchat Business Manager 관리자가 Braze와 함께 사용할 Snapchat 광고 계정에 대한 관리자 권한을 부여했는지 확인하세요. |
| Snapchat 약관 및 정책 | [Snapchat](https://www.snap.com/en-US/policies) | Snapchat 오디언스 동기화 사용과 관련하여 Snapchat에서 요구하는 약관, 정책, 가이드라인 및 설명서(여기에 참조로 포함된 약관, 정책, 가이드라인 및 설명서 포함)를 준수하는 데 동의해야 합니다. 여기에는 서비스 약관, 비즈니스 서비스 약관, 개발자 약관, Audience Match, 광고 정책, 상업 콘텐츠 정책, 커뮤니티 가이드라인 및 공급업체 책임이 포함될 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사전 요구 사항" }

## 통합 {#integration}

### 1단계: Snapchat에 연결하기 {#step-1-connect-to-snapchat}

{% alert important %}
Snapchat을 Braze 계정에 연결하려면 ["관리자" 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)이 있어야 합니다.
{% endalert %}

Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Snapchat**을 선택합니다. Snapchat 오디언스 동기화 아래에서 **Snapchat 연결**을 선택합니다.

![개요 섹션과 Snapchat 연결 버튼이 있는 Snapchat 오디언스 동기화 섹션이 포함된 Braze의 Snapchat 기술 페이지.]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

그러면 Snapchat OAuth 페이지로 리디렉션되어 오디언스 동기화 통합과 관련된 권한에 대해 Braze를 승인하게 됩니다.

확인을 선택하면 Braze로 다시 리디렉션되어 동기화할 Snapchat 광고 계정을 선택할 수 있습니다.

![Snapchat에 연결할 수 있는 사용 가능한 광고 계정 목록.]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

성공적으로 연결되면 파트너 페이지로 돌아가며, 연결된 계정을 확인하고 기존 계정의 연결을 해제할 수 있습니다.

![성공적으로 연결된 광고 계정을 보여주는 업데이트된 Snapchat 기술 파트너 페이지.]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Snapchat 연결은 Braze 워크스페이스 수준에서 적용됩니다. Snapchat 관리자가 Snapchat Business Manager에서 사용자를 제거하거나 연결된 Snapchat 광고 계정에 대한 액세스를 제거하면, Braze는 유효하지 않은 토큰을 감지합니다. 그 결과, Snapchat을 사용하는 활성 Canvases에 오류가 표시되며, Braze는 사용자를 동기화할 수 없게 됩니다.

### 2단계: Snapchat으로 오디언스 동기화 단계 추가하기 {#step-2-add-an-audience-sync-step-with-snapchat}

Canvas에 컴포넌트를 추가하고 **오디언스 동기화**를 선택합니다.

![오디언스 동기화 컴포넌트 옵션이 있는 캔버스 단계 선택기.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Canvas 경로에 추가된 오디언스 동기화 컴포넌트 카드.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### 3단계: 동기화 설정 {#step-3-sync-setup}

**커스텀 오디언스** 버튼을 클릭하여 컴포넌트 편집기를 엽니다.

원하는 오디언스 동기화 파트너로 **Snapchat**을 선택합니다.

![Snapchat이 동기화 파트너로 선택된 오디언스 동기화 컴포넌트 편집기.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

그런 다음 원하는 Snapchat 광고 계정을 선택합니다. **새 오디언스 또는 기존 오디언스 선택** 드롭다운에서 새 오디언스 또는 기존 오디언스의 이름을 입력합니다.

{% tabs %}
{% tab 새 오디언스 만들기 %}

**새 오디언스 만들기**<br>
새 오디언스의 이름을 입력하고, **오디언스에 사용자 추가**를 선택한 다음, Snapchat과 동기화할 필드를 선택합니다. 그런 다음 단계 편집기 하단의 **오디언스 만들기** 버튼을 클릭하여 오디언스를 저장합니다.

![커스텀 오디언스 캔버스 단계의 확장된 보기. 여기에서 원하는 광고 계정이 선택되고 새 오디언스가 생성됩니다.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

오디언스가 성공적으로 생성되거나 오류가 발생하면 Braze는 단계 편집기 상단에 알림을 표시합니다. 오디언스가 초안 모드로 생성되었으므로, 사용자는 나중에 Canvas 여정에서 사용자 제거를 위해 이 오디언스를 참조할 수 있습니다.

![Canvas 컴포넌트에서 새 오디언스가 생성된 후 나타나는 알림.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

새 오디언스로 Canvas를 시작하면, Braze는 사용자가 오디언스 동기화 컴포넌트에 진입할 때 거의 실시간으로 사용자를 동기화합니다.

{% endtab %}
{% tab 기존 오디언스와 동기화 %}
**기존 오디언스와 동기화**<br>
Braze는 기존 Snapchat 오디언스에 사용자를 추가하여 해당 오디언스를 최신 상태로 유지하는 기능도 제공합니다. 기존 오디언스와 동기화하려면 드롭다운에서 기존 오디언스 이름을 입력하고 **오디언스에 추가**합니다. 그러면 Braze는 사용자가 오디언스 동기화 컴포넌트에 진입할 때 거의 실시간으로 사용자를 추가합니다.

![커스텀 오디언스 캔버스 단계의 확장된 보기. 여기에서 원하는 광고 계정과 기존 오디언스가 선택됩니다.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### 4단계: Canvas 시작하기 {#step-4-launch-canvas}

Snapchat으로의 오디언스 동기화를 구성한 후 Canvas를 시작합니다! 새 오디언스가 생성되고, 오디언스 동기화 단계를 통과하는 사용자는 Snapchat의 해당 오디언스로 전달됩니다. Canvas에 후속 컴포넌트가 포함되어 있으면, 사용자는 사용자 여정의 다음 단계로 진행합니다.

광고 매니저 계정에 접속하고 내비게이션의 에셋 섹션에서 **Audiences**를 선택하여 Snapchat에서 오디언스를 확인할 수 있습니다. **Audiences** 페이지에서 각 오디언스의 크기가 약 1,000명에 도달한 후 확인할 수 있습니다.

![오디언스 이름, 오디언스 유형, 오디언스 크기, 오디언스 유지 일수를 포함하는 특정 Snapchat 오디언스의 세부 정보.]({% image_buster /assets/img/snapchat/snapchat7.png %})

## 사용자 동기화 및 사용량 제한 고려 사항 {#user-syncing-and-rate-limit-considerations}

사용자가 오디언스 동기화 단계에 도달하면, Braze는 Snapchat의 API 사용량 제한을 준수하면서 거의 실시간으로 사용자를 동기화합니다. Braze는 5초마다 가능한 한 많은 사용자를 일괄 처리한 후 Snapchat으로 전송합니다.

Snapchat의 API 사용량 제한은 초당 최대 10개의 쿼리와 요청당 100,000명의 사용자를 허용합니다. 고객이 이 제한에 도달하면, Braze는 최대 약 13시간 동안 동기화를 재시도합니다. 그래도 동기화가 불가능한 경우, Braze는 해당 사용자를 Users Errored 측정기준에 표시합니다.

### 분석 이해하기 {#understanding-analytics}

다음 표에는 오디언스 동기화 구성 요소의 분석을 더 잘 이해하는 데 도움이 되는 측정기준과 설명이 포함되어 있습니다.

| 측정기준 | 설명 |
| --- | --- |
| Entered | Snapchat에 동기화하기 위해 이 구성 요소에 진입한 사용자 수입니다. |
| Proceeded to Next Step | 다음 구성 요소가 있는 경우 다음 구성 요소로 진행한 사용자 수입니다. Canvas 브랜치의 마지막 단계인 경우 모든 사용자가 자동으로 진행됩니다. |
| Users Synced | Snapchat에 성공적으로 동기화된 사용자 수입니다. |
| Users Not Synced | 매칭할 필드가 누락되어 동기화되지 않은 사용자 수입니다. |
| Users Pending | 현재 Braze에서 Snapchat으로 동기화하기 위해 처리 중인 사용자 수입니다. |
| Users Errored | 약 13시간의 재시도 후 API 오류로 인해 Snapchat에 동기화되지 않은 사용자 수입니다. 오류의 잠재적 원인으로는 유효하지 않은 Snapchat 토큰이나 Snapchat에서 오디언스가 삭제된 경우 등이 있습니다. |
| Exited Canvas | Canvas를 종료한 사용자 수입니다. Canvas의 마지막 단계가 오디언스 동기화 구성 요소인 경우 발생합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="분석 이해하기" }

{% alert important %}
동기화된 사용자 및 오류 측정기준의 보고에는 대량 플러셔와 13시간 재시도로 인해 각각 지연이 발생할 수 있다는 점을 유의하세요.
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

### Snapchat에서 지원할 수 있는 오디언스 수는 얼마인가요? {#how-many-audiences-can-snapchat-support}

현재 Snapchat 계정 내에서 최대 1,000개의 오디언스만 보유할 수 있습니다.

이 한도를 초과하면 Braze에서 새 오디언스를 생성할 수 없다는 알림을 보냅니다. Snapchat 광고 계정에서 더 이상 사용하지 않는 오디언스를 제거해야 합니다.

### 사용자를 Snapchat에 전달한 후 매칭 여부를 어떻게 확인할 수 있나요? {#how-do-i-know-if-users-have-matched-after-passing-users-to-snapchat}

Snapchat은 데이터 프라이버시 정책에 따라 이 정보를 제공하지 않습니다.

### 유효하지 않은 토큰 오류가 발생하면 어떻게 해야 하나요? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Snapchat 파트너 페이지에서 Snapchat 계정의 연결을 해제한 후 다시 연결할 수 있습니다. Snapchat Business Manager 관리자에게 동기화하려는 광고 계정에 대한 적절한 권한이 있는지 확인하세요.

### Canvas를 시작할 수 없는 이유는 무엇인가요? {#why-is-my-canvas-not-allowed-to-launch}

Snapchat 파트너 페이지에서 Snapchat 광고 계정이 Braze에 성공적으로 연결되어 있는지 확인하세요. 광고 계정을 선택했는지, 새 오디언스의 이름을 입력했는지, 매칭할 필드를 선택했는지 확인하세요.