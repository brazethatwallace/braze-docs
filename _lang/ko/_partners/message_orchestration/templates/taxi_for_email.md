---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "이 참조 문서에서는 Braze와 Taxi for Email 간의 파트너십에 대해 설명합니다. Taxi for Email은 Braze 고객이 드래그 앤 드롭 인터페이스와 간단하면서도 강력한 구문을 사용하여 지능형 이메일 템플릿을 만들 수 있는 온라인 이메일 마케팅 도구입니다."
page_type: partner
search_tag: Partner

---

# Taxi for Email

> [Taxi for Email](http://taxiforemail.com/)은 직관적인 드래그 앤 드롭 비주얼 이메일 편집기를 제공하는 온라인 이메일 마케팅 도구입니다. Taxi를 사용하면 팀이 이메일 캠페인에서 쉽게 협업할 수 있으며, 카피라이터와 편집자가 코드 없이도 이메일을 작성하는 데 필요한 액세스 권한과 리소스를 제공합니다.

_이 통합은 Taxi for Email에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Taxi의 통합은 Taxi의 간단하면서도 강력한 구문을 사용하여 지능형 이메일 템플릿을 생성하고 Braze로 내보냅니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ------------| ----------- |
| Taxi for Email 계정 | 이 파트너십을 이용하려면 Taxi for Email 계정이 필요합니다. |
| Braze REST API 키 | 전체 **템플릿** 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 엔드포인트 | [Braze 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)는 Braze 대시보드 URL에 맞춰 설정됩니다.<br><br> 예를 들어, 대시보드 URL이 `https://dashboard-03.braze.com`이면 엔드포인트는 `dashboard-03`입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Taxi 이메일 템플릿 만들기 {#step-1-create-a-taxi-email-template}

Taxi 플랫폼에서 Taxi 템플릿을 만듭니다. 템플릿이 생성되면 **Organization Settings**로 이동하여 **ESP Connectors** 탭을 선택합니다.

### 2단계: Braze 커넥터 만들기 {#step-2-create-braze-connector}

1. 표시되는 대화 상자에서 **Add New** 버튼을 선택한 다음 드롭다운에서 **Braze**를 선택합니다.
2. **Braze**를 선택하여 Braze 커넥터 설정을 편집합니다.
3. Braze 엔드포인트와 Braze API 키를 입력합니다.

올바른 권한이 있는 세부 정보가 제공되면 커넥터 필드의 색상이 변경됩니다. 필드 색상이 변경되지 않으면 입력한 필드가 나열된 요구 사항에 맞는지 확인하세요.

## 사용법 {#usage}

Braze 계정의 **템플릿 및 미디어 > 이메일 템플릿** 섹션에서 업로드한 Taxi 템플릿을 찾으세요. 이제 이 이메일 템플릿을 사용하여 고객에게 매력적인 이메일 메시지를 보낼 수 있습니다!