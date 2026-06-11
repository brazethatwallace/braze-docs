---
nav_title: Kognitiv Inspire
article_title: Kognitiv Inspire
description: "Kognitiv Inspire는 혁신적인 기능과 맞춤형 회원 커뮤니케이션을 제공하여 로열티 전략을 구현하고 평가할 수 있게 해주는 로열티 기술 시스템입니다."
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> [Kognitiv Inspire](http://kognitiv.com)는 고객 참여를 증폭시키고, 지출을 늘리며, 충성 행동을 기념하는 성과 중심의 로열티 프로그램을 통해 비할 데 없는 고객 경험을 실현할 수 있도록 돕는 로열티 기술 시스템입니다.

_이 통합은 Kognitiv Inspire에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Kognitiv 통합을 통해 로열티 전략을 구현하고 평가할 수 있으며, 혁신적인 기능과 맞춤형 회원 커뮤니케이션을 제공하여 프로그램 효과를 높일 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Kognitiv 계정 | 이 파트너십을 활용하려면 [Kognitiv](http://kognitiv.com) 계정이 필요합니다. |
| Kognitiv API 키 | Kognitiv REST API 키입니다. **API Security Tokens** 페이지에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL입니다. 엔드포인트는 [인스턴스]({{site.baseurl}}/api/basics/#endpoints)의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

- **개인화된 로열티 프로그램 등록**: 원활한 프로그램 등록과 선호 채널을 통해 전달되는 맞춤형 환영 알림으로 회원의 로열티 여정을 시작하세요.
- **리워드 발급 및 참여 알림**: 각 회원의 마일스톤을 축하하는 리워드와 알림을 발급하여 로열티의 불꽃을 유지하세요.
- **전략적 회원 등급 분류 및 세분화**: 지출, 참여도, 브랜드의 특정 요구에 맞춘 단순하거나 복잡한 비즈니스 규칙을 기반으로 회원을 등급 분류하고 세분화하여 더욱 개인화된 참여를 가능하게 합니다.
- **실시간 프로모션 자격 알림**: 독점 프로모션 자격에 대한 즉각적인 알림으로 각 회원이 특별함을 느끼게 하세요.

## 통합 {#integration}

로열티 이벤트가 발생할 때 Kognitiv 웹훅을 사용하여 Braze에 요청을 보냅니다. 다음 예시는 Kognitiv과 Braze를 사용하여 리워드를 발급하고, Kognitiv 사용자를 Braze에 등록하고, 환영 이메일을 보내는 방법을 보여줍니다.

{% raw %}
### Braze 리워드 발급 {#braze-issue-reward}

다음 Kognitiv 예시는 회원 리워드를 발급합니다. Kognitiv Inspire는 웹훅을 통해 해당 리워드 발급 이벤트를 커스텀 이벤트로 Braze에 전달합니다. 리워드를 알리는 후속 이메일을 보내려면 해당 커스텀 이벤트를 트리거로 하는 Campaign 또는 Canvas를 생성하세요.

**웹훅 URL**: `<braze-api-rest-endpoint>`
**요청 본문**: `Raw Text`

- **HTTP 메서드**: POST
- **요청 헤더**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### 요청 본문 {#request-body}

```json
{
  "events" : [
    {
    "external_id" : "{{memberId}}",
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38",
    "name" : "rewards_issued",
    "time" : "{{issuedDate}}",
    "issued_date" : "{{issuedDate}}",
    "issued_location_name" : "{{issuedLocationName}}",
    "reward_type" : "{{rewardType}}"
    }
  ]
}
```

### 사용자 생성 및 환영 이메일 발송 {#create-a-user-and-send-a-welcome-email}

다음 Kognitiv 예시는 KLS에 등록할 때 Braze에 새 사용자를 생성합니다. 이 사용자에게 환영 이메일을 예약하려면 특정 커스텀 속성을 기반으로 트리거되는 Campaign 또는 Canvas를 Braze에서 생성하세요.

**웹훅 URL**: `<braze-api-rest-endpoint>` <br>
**요청 본문**: `Raw Text`

- **HTTP 메서드**: POST
- **요청 헤더**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### 요청 본문

```json
{
  "attributes": [
    {
      "app_id": "93ec5a59-3752-4a45-855b6109ba38",
      "bio": "Software Architect",
      "country": "{{memberAddressCO}}",
      "email": "{{memberEmail}}",
      "email_subscribe": "opted_in",
      "external_id": "{{memberId}}",
      "first_name": "{{memberFirstName}}",
      "home_city": "{{memberAddressCity}}",
      "time_zone": "America/Chicago",
      "total_points_balance": "{{memberPointsAvailable}}",
      "CreatedKLS": "{{issuedTimestamp}}",
      "email_contact_allowed" : "{{memberEmailContactAllowed}}",
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}",
      "date_joined": "{{issuedDate}}"
    }
  ]
}
```
{% endraw %}

## Kognitiv Inspire 설명서 및 통합 기능 {#kognitiv-inspire-documentation-and-integration-features}

Braze와 Kognitiv Inspire를 통합하면 Kognitiv의 광범위한 API 포트폴리오, 최첨단 웹훅 기능, 원활한 대량 전송을 위한 강력한 데이터 가져오기 및 내보내기 기능에 접근할 수 있습니다. Kognitiv Inspire 기능 및 통합 역량에 대한 자세한 내용은 Kognitiv [리소스 가이드](https://info.kognitivloyalty.com)를 확인하거나 가이드 데모를 요청하세요.

### 엔드포인트 {#endpoints}

**REST API 승인**
- US 리전: `https://app.kognitivloyalty.com/Auth/connect/token`
- CA/EMEA 리전: `https://ca.kognitivloyalty.com/Auth/connect/token`
- APAC 리전: `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API (기본 URL)**
- US 리전: `https://app.kognitivloyalty.com/api`
- CA/EMEA 리전: `https://ca.kognitivloyalty.com/api`
- APAC 리전: `https://aus.kognitivloyalty.com/api`

**웹 서비스 엔드포인트 (기본 URL)**
- US 리전: `https://app.kognitivloyalty.com/WS`
- CA/EMEA 리전: `https://ca.kognitivloyalty.com/WS`
- APAC 리전: `https://aus.kognitivloyalty.com/WS`

액세스 토큰 및 SFTP 엔드포인트 구성에 대한 자세한 내용은 Kognitiv에 데모를 요청하세요.