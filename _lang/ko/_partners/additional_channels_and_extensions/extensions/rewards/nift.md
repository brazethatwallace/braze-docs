---
nav_title: Nift
article_title: Nift
description: "이 참조 문서에서는 기업이 고객을 확보하고, 참여시키고, 유지할 수 있도록 돕는 양면 플랫폼인 Nift와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/)는 기업이 고객을 확보하고, 참여시키고, 유지할 수 있도록 돕습니다. 이 양면 플랫폼은 파트너가 Nift 기프트 카드를 통해 고객에게 감사를 표할 수 있도록 지원합니다. 고객에게 감사를 표하면 LTV or 생애주기 가치가 높아지고 추가 매출이 발생합니다.

_이 통합은 Nift에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Nift 통합을 사용하면 고객 생애주기의 주요 순간에 Nift 선물이 포함된 "감사 인사"를 자동으로 트리거하고, 어떤 고객이 선물을 사용했는지 확인할 수 있습니다. Nift 기프트 카드는 Nift의 매칭 기술을 활용하여 대규모로 비용 효율적으로 신규 고객을 확보하는 브랜드가 제공하는 제품 및 서비스에 사용할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Nift 계정 | 이 파트너십을 활용하려면 Nift 계정이 필요합니다. |
| Braze REST API 키 | 모든 사용자 데이터 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스]({{site.baseurl}}/api/basics/#endpoints)의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Nift에서 Braze에 연결 {#step-1-connect-to-braze-in-nift}

[Nift 대시보드](https://www.gonift.com/users/sign_in)를 방문하여 **Accounts** > **Integrations** > **Braze**로 이동한 다음 **Connect**를 클릭합니다.

### 2단계: Braze 자격 증명 추가 {#step-2-add-braze-credentials}

**Link your Braze Account** 페이지에서 Braze REST API 키를 입력하고 Braze 엔드포인트를 선택합니다. 엔드포인트는 [인스턴스]({{site.baseurl}}/api/basics/#endpoints)의 Braze URL에 따라 달라집니다.

고객에게 전송되는 추천 링크에서 고객 ID 매개변수 이름을 변경할 수 있습니다. Nift는 고객이 브랜드 중 하나에서 선물을 선택하면 이를 사용하여 Braze에서 해당 고객을 처리 완료로 표시합니다.

**Link Account**를 클릭합니다.

!["Nift 서비스 통합 페이지에서 사용자에게 Braze API 키와 Braze 대시보드 URL을 입력하라는 프롬프트를 표시합니다.]({% image_buster /assets/img/nift/link_your_braze_account.png %})

## 통합 사용 {#using-the-integration}

통합을 사용하려면 메시징에서 추천 링크를 배포합니다. 고객이 추천 링크를 사용하여 브랜드 중 하나에서 선물을 선택하면 Nift가 Braze에서 해당 고객을 처리 완료로 표시합니다.

Braze와 통합한 후 Nift는 기존 고객의 Braze 레코드에 다음 데이터가 포함된 이벤트를 자동으로 푸시합니다.

- 이벤트 이름: `nift_processed`
- 시간: 고객이 선물을 선택/사용한 시간