---
nav_title: DataGrail
article_title: DataGrail
description: "이 참조 문서에서는 Braze와 개인정보 관리 플랫폼인 DataGrail 간의 파트너십을 설명합니다. 이 통합을 통해 Braze 내에서 수집 및 저장된 소비자 데이터를 감지하여 DSR을 신속하게 처리할 수 있습니다."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> [DataGrail](https://www.datagrail.io/)은 개인정보 관리 플랫폼으로, 소비자 신뢰를 구축하고 위험한 비즈니스 관행을 제거하는 데 도움을 줍니다. 지속적인 시스템 감지와 자동화된 데이터 주체 요청(DSR) 처리를 통해 DataGrail은 개인정보 보호 프로그램을 지원하며, GDPR, CCPA, CPRA와 같이 진화하는 개인정보 보호 법률 및 규정 준수를 돕습니다.

_이 통합은 DataGrail에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 DataGrail 통합을 사용하면 Braze 내에서 수집 및 저장된 소비자 데이터를 감지하여 DSR(액세스, 삭제 및 판매 거부 요청)을 신속하게 처리할 수 있습니다. Braze는 자동화된 데이터 매핑을 통해 조직 내 소비자 데이터가 존재하는 위치에 대한 정확한 블루프린트에 추가됩니다. 개인정보 보호 프레임워크를 유지하거나 처리 활동 기록(RoPA)을 생성하기 위해 더 이상 설문조사나 스프레드시트가 필요하지 않습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| DataGrail 계정 | 이 파트너십을 활용하려면 DataGrail 계정이 필요합니다.<br>통합에 관한 문제나 질문이 있으면 관리자에게 문의하거나 support@datagrail.io로 이메일을 보내주세요. |
| Braze API 키 | `events.list`, `users.export.ids`, `users.delete`, `users.track` 권한이 있는 Braze REST API 키가 필요합니다.<br><br>이 키는 Braze 대시보드의 **Settings** > **API Keys**에서 생성할 수 있습니다. |
| Braze 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저에게 문의하거나 [API 개요 페이지]({{site.baseurl}}/api/basics/#endpoints)에서 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

DataGrail 포털에 로그인하고 Braze 통합 페이지에서 **Connect**를 선택합니다. 그런 다음 인스턴스와 Braze API 키를 입력하고 **Connect Braze**를 선택합니다.

추가 Braze 계정을 통합해야 하는 경우:
1. Braze 통합 페이지에서 **Edit Connection**을 선택합니다.
2. 드롭다운에서 **+Add New Connection**을 선택합니다.
3. **Connection Name** 아래에 이 별도 계정을 식별할 새 이름을 입력합니다(예: Braze Training Account).
4. 이 새 계정에 대한 별도의 Braze 인스턴스와 API 키를 입력합니다.
5. **Connect**를 선택합니다.

통합에 관한 문제나 질문이 있으면 support@datagrail.io로 DataGrail에 이메일을 보내주세요.