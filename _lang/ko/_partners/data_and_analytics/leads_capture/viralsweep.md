---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "이 참조 문서에서는 브랜드가 경품 행사, 콘테스트, 즉석 당첨, 대기자 명단, 추천 프로모션 등 디지털 마케팅 프로모션을 구축, 실행 및 관리할 수 있는 소프트웨어 서비스인 ViralSweep과 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com)은 브랜드가 경품 행사, 콘테스트, 즉석 당첨, 대기자 명단, 추천 프로모션 등 디지털 마케팅 프로모션을 구축, 실행 및 관리할 수 있는 소프트웨어 서비스입니다.

_이 통합은 ViralSweep에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 ViralSweep 통합을 사용하면 ViralSweep 플랫폼에서 경품 행사와 콘테스트를 진행하여 이메일 및 SMS 목록을 확장하고, 경품 행사 또는 콘테스트 참가 정보를 Braze로 전송하여 Campaigns 또는 Canvases에서 활용할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| ViralSweep 계정 | 이 파트너십을 활용하려면 비즈니스 플랜을 사용하는 ViralSweep 계정이 필요합니다. |
| Braze REST API 키 | 모든 사용자 데이터 및 이메일 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스]({{site.baseurl}}/api/basics/#endpoints)의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: ViralSweep에서 Braze에 연결하기 {#step-1-connect-to-braze-within-viralsweep}

ViralSweep에서 **Integrations > Email & SMS > Add Service**로 이동하여 **Braze**를 선택합니다.

![]({% image_buster /assets/img/viralsweep/connect.gif %})

### 2단계: Braze 자격 증명 추가하기 {#step-2-add-braze-credentials}

통합 구성 창에서 Braze REST API 키와 REST 엔드포인트를 입력합니다. 제공하는 엔드포인트에 `https://`가 포함되지 않도록 해야 합니다. 예를 들어 `dashboard-03.braze.com`과 같이 입력합니다.

![사용자에게 Braze API 키와 Braze 대시보드 URL을 입력하라는 메시지가 표시되는 ViralSweep 서비스 통합 페이지.]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

**Connect**를 클릭합니다.

### 3단계: Braze 자격 증명 추가하기 {#step-3-add-braze-credentials}
연결이 완료되었습니다! 이제 프로모션이 Braze에 연결되었으며, ViralSweep에서 수집한 모든 참가 정보가 자동으로 Braze로 전송됩니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### ViralSweep은 어떤 필드를 Braze로 전달하나요? {#what-fields-does-viralsweep-pass-to-braze}
- First name
- Last name
- Email address
- Address
- Address 2
- City
- State
- Zip
- Country
- Birthdate
- Phone
- Promotion ID
- Referral link
- Tracking campaign name

### ViralSweep은 가입자 정보를 업데이트하나요? {#does-viralsweep-update-subscribers}
네. 프로모션을 실행하여 ViralSweep이 누군가를 Braze로 전달한 후, 나중에 다른 프로모션을 실행했을 때 같은 사람이 참가하면 해당 사용자의 정보가 Braze에서 자동으로 업데이트됩니다(새로운 정보가 제공된 경우). 주로 추천 URL이 참가한 각 프로모션의 최신 URL로 업데이트되며, 프로모션 ID 필드에는 참가한 모든 프로모션의 ID가 포함됩니다.

## 문제 해결 {#troubleshooting}

Braze에 연결했는데 데이터가 계정에 추가되지 않는 경우, 다음과 같은 이유일 수 있습니다:

- **이메일이 이미 Braze에 존재하는 경우**<br>
프로모션에 입력한 이메일 주소가 이미 Braze 계정에 존재할 수 있으며, 이 경우 다시 추가되지 않습니다. 해당 연락처에 대해 새로운 정보가 제공된 경우에만 업데이트됩니다.<br><br>
- **이메일이 이미 ViralSweep에 입력된 경우**<br>
프로모션에 입력한 이메일 주소가 이전에 이미 입력된 적이 있어 Braze로 다시 전달되지 않습니다. 이는 프로모션에 이미 참가한 후에 Braze 통합을 설정한 경우에 발생할 수 있습니다.