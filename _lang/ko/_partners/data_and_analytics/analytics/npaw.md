---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "이 참조 문서에서는 선도적인 온라인 미디어 전문가에게 유용한 인사이트를 제공하는 지능형 데이터 분석 플랫폼인 NPAW와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/)는 _Nice People at Work_으로도 알려져 있으며, 선도적인 온라인 미디어 전문가에게 유용한 인사이트를 제공하는 지능형 데이터 분석 플랫폼입니다. NPAW의 YOUBORA 도구 모음을 통해 Braze 고객은 예측적이고 강력한 AI를 활용하여 고객 행동을 더 잘 이해하고 플랫폼 전반에서 참여를 유도할 수 있습니다.

# 필수 조건 {#prerequisites}

| 요구 사항 | 출처 | 설명 |
| --------------|------|-------------|
| YOUBORA API 키 | [YOUBORA 설정](https://youbora.nicepeopleatwork.com/users/login) | 사용자 가입 시 생성되는 API 키로, **설정**에서 확인할 수 있습니다. |
| ID | [Braze 설정](https://dashboard.braze.com/sign_in) | YOUBORA에서는 ***Braze ID***, ***외부 사용자 ID*** 또는 ***사용자 ID***를 통해 소프트웨어를 Braze에 연결할 수 있는 옵션을 제공합니다. |
| 엔드포인트 | [Braze 설정](https://dashboard.braze.com/sign_in) | Braze 대시보드를 통해 구성할 수 있는 완전히 커스텀 가능한 URL 엔드포인트입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prerequisites" }

# 분석 통합 {#analytics-integration}

## 통합 페이지 접근하기 {#accessing-the-integrations-page}

YOUBORA 도구 모음 계정에 로그인한 후, 드롭다운 계정 메뉴에서 **Integrations** 옵션을 선택하여 통합 페이지로 이동합니다.

![NPAW 드롭다운]({% image_buster /assets/img/npaw_dropdown.png %})

## 통합 구성하기 {#configuring-your-integration}

통합 페이지에 접근한 후, **Braze** 통합 옵션이 보일 때까지 아래로 스크롤합니다. 이를 클릭하면 확장되어 입력해야 할 필수 파라미터가 표시됩니다.

![NPAW 통합]({% image_buster /assets/img/npaw_integration.png %})

필수 조건 섹션에서 수집한 적절한 정보로 세부 사항을 입력합니다.
* **Connector Name**은 향후 이 통합을 참조하는 데 사용되는 **영숫자** 문자열입니다. 이 값은 **오직** 문자와 숫자만 포함하는 한 원하는 대로 설정할 수 있습니다.
* **User ID**는 YOUBORA 소프트웨어를 Braze 계정에 연결하기 위해 이전에 선택한 ID입니다. 예를 들어, **Braze ID**를 통해 연결하려면 드롭다운에서 **Braze ID**를 선택하여 적절한 필드에 값을 할당합니다.
* **API Key**는 이전에 **설정**의 **API** 섹션에서 확인한 YOUBORA 도구 모음 API 키입니다.
* **Endpoint**는 이전에 Braze 대시보드에서 설정한 커스텀 가능한 URL 엔드포인트입니다.

모든 필드를 입력한 후, **Connect** 버튼을 클릭하여 연결을 설정하고 변경 사항을 저장합니다.

## NPAW 통합 사용하기 {#using-your-npaw-integration}

Braze와의 통합 구성을 완료한 후, **Users** 제품으로 이동하여 **Sections Manager** 내에서 **Sample Manager**를 선택합니다.

**Sample Manager**에서 샘플을 생성한 후, 오른쪽에 있는 점 세 개 아이콘을 클릭하여 샘플 내의 모든 사용자를 Braze로 전송할 수 있습니다.

![NPAW 샘플 매니저]({% image_buster /assets/img/npaw_sample_manager.png %})

이제 사용자를 Braze로 전송한 후, 사용자 Segment에 대해 Campaigns를 집중하여 비활성 사용자를 다시 참여시키거나, 가장 충성도 높은 사용자에게 연락하거나, 모든 사용자 Segment에 대해 원하는 조치를 취할 수 있습니다!