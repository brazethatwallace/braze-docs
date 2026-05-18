---
nav_title: Transcend
article_title: Transcend
description: "이 참조 문서에서는 데이터 프라이버시 인프라 플랫폼인 Transcend와 Braze 간의 파트너십을 설명하며, Braze 사용자가 데이터 주체 요청 이행을 자동화하는 데 도움을 줍니다."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend는 데이터 프라이버시 인프라 회사로, 기업이 모든 데이터 시스템과 벤더에 걸쳐 데이터 주체 요청을 자동으로 이행하여 사용자에게 자신의 데이터에 대한 제어권을 쉽게 부여할 수 있도록 합니다.

_이 통합은 Transcend에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Transcend 파트너십은 수십 개의 데이터 시스템에 걸쳐 데이터를 오케스트레이션하여 프라이버시 요청을 자동화하고, 팀이 GDPR 및 CCPA와 같은 규정을 준수할 수 있도록 지원합니다. Transcend는 최종 사용자에게 `privacy.\<company\>.com`에서 호스팅되는 제어판 또는 프라이버시 센터를 제공하여 사용자가 프라이버시 기본 설정을 관리하고, 데이터를 내보내거나 삭제할 수 있도록 합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Transcend 계정 | 이 파트너십을 활용하려면 관리자 권한이 있는 [Transcend](https://app.transcend.io/) 계정이 필요합니다. |
| Braze API 키 | `users.delete, users.alias.new, users.export.ids, email.unsubscribe,` 및 `email.blacklist` 권한이 있는 Braze REST API 키.<br><br>이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

Transcend를 사용하면 데이터 프라이버시 규정에 따라 Braze 플랫폼에서 프로그래밍 방식으로 사용자 데이터에 액세스하고, 삭제하고, 커뮤니케이션 수신을 거부할 수 있습니다.

### 1단계: Braze 통합 설정 {#step-1-set-up-the-braze-integration}
시작하려면 [Transcend](https://app.transcend.io/login)에 로그인합니다.
1. **Data Map > Add Data Silo > Braze**로 이동하여 **Connect** 버튼을 선택합니다.<br><br>
2. 계정이 프로비저닝되면 다음 URL 중 하나로 로그인하게 됩니다: `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`.<br> 다음 [표]({{site.baseurl}}/api/basics/#endpoints)를 사용하여 대시보드 URL을 기반으로 포함해야 할 하위 도메인을 확인합니다.<br><br>
3. 연결되면 Transcend **Privacy Center** 탭으로 이동합니다. 여기에서 Braze의 데이터를 데이터 관행에 매핑해야 합니다. 이를 위해 적절한 명명 규칙으로 새 카테고리와 새 데이터 컬렉션을 생성합니다(예: "Mailing Lists or User Profile"). 완료되면 **Publish**를 선택합니다.<br><br>
4. 데이터 맵으로 다시 이동하여 Braze 데이터 사일로를 선택합니다. **Manage Datapoints**를 확장하고 드롭다운에서 이전 단계에서 생성한 컬렉션 레이블(카테고리)을 선택합니다. 어떤 데이터 포인트에 대해 어떤 데이터 동작(예: 액세스 또는 삭제)을 활성화할지 선택할 수도 있습니다.<br><br>
5. 다음으로, Braze 데이터 사일로에서 **Manage Identifiers**를 확장합니다. 활성화하려는 식별자에 대해 해당 체크박스를 선택합니다. 예를 들어, Transcend가 이메일 주소로 사용자를 검색하도록 하려면 이메일 주소 식별자를 활성화하는 체크박스를 선택합니다.

{% alert note %}
식별자가 올바르게 활성화되지 않으면 Transcend가 특정 사용자에 대한 요청을 처리하지 못할 수 있습니다.
{% endalert %}

### 2단계: 요청 테스트 {#step-2-test-requests}
Transcend는 최종 사용자의 요청을 처리하기 전에 데이터 맵 전체에서 요청을 테스트할 것을 권장합니다.
1. Transcend의 **Privacy Center**로 이동하여 **View your Privacy Center**를 선택합니다.<br><br>
2. **Privacy Center**에서 **Take Control**을 선택한 다음 **Download my data**를 선택합니다. 요청을 제출하기 전에 이메일을 입력하거나 로그인하여 본인 인증을 합니다.<br><br>
3. 이메일에서 Transcend의 메시지를 확인합니다. 요청을 확인하기 위해 인증 링크를 클릭하라는 안내를 받게 됩니다.<br><br>
4. 다음으로, **Admin** 대시보드로 돌아가서 **Incoming Requests** 탭으로 이동하여 요청을 선택합니다. 여기에서 요청이 보이지 않으면 [support@transcend.io](mailto:support@transcend.io)로 Transcend에 문의합니다.<br><br>
5. 요청을 클릭한 후 **Data Silos** 탭으로 이동하여 **Braze**를 선택합니다. 반환된 데이터를 검사하고 확인합니다.<br><br>
6. 마지막으로 **Report** 탭으로 이동하여 **Approve and Send**를 클릭합니다. 요청 시 제출한 이메일 주소로 보고서를 받게 됩니다.

## Braze 통합 제거 {#remove-the-braze-integration}
Transcend 데이터 맵에서 Braze 데이터 사일로를 제거하려면:
1. **Data Map**으로 이동하여 **Braze**를 클릭합니다.<br><br>
2. 화면 하단에서 **Remove Braze**를 확장하고 **Remove Silo**를 클릭합니다. 사일로를 제거할 것인지 확인하라는 메시지가 표시됩니다. **Ok**를 클릭합니다.<br><br>
3. 데이터 맵으로 다시 이동하여 사일로가 제거되었는지 확인합니다.