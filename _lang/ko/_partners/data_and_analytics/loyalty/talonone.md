---
nav_title: Talon.One
article_title: Talon.One
alias: /partners/talonone/
description: "이 참조 문서에서는 상황별 1:1 쿠폰, 추천, 할인 및 로열티 캠페인을 빠르고 효율적으로 시작할 수 있는 프로모션 엔진인 Talon.One과 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Talon.One

> [Talon.One](https://talon.one/)은 모바일 마케팅 CRM을 위한 개인화된 인센티브를 제공하며, 상황별 1:1 쿠폰, 추천, 할인 및 로열티 캠페인을 빠르고 효율적으로 시작할 수 있도록 합니다.

_이 통합은 Talon.One에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Talon.One 통합은 Talon.One에서 생성된 코드를 Braze 연결된 콘텐츠를 통해 오디언스에게 전송하여 로열티 또는 쿠폰 프로그램을 한 단계 더 발전시킬 수 있도록 도와줍니다.


## 필수 조건 {#prerequisites}

| 필수 조건 | 설명 |
| ----------- | ----------- |
| Talon.One 계정 | 이 파트너십을 활용하려면 Talon.One 계정이 필요합니다. |
| Talon.One API 키 | Talon.One에서 **Settings** > **Developer Settings**로 이동하여 통합을 위한 Braze 서드파티 API 키를 생성합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% alert warning %}
Talon.One은 분당 최대 2,500건의 메시지 사용량 제한을 **_필수로 요구합니다_**. 이 사용량 제한은 Braze 대시보드에서 [수정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting)할 수 있습니다.
{% endalert %}

## 통합 {#integration}

1. 통합 설정 방법, Talon.One API 쿠폰 엔드포인트 사용 방법, Braze 메시지에 필요한 연결된 콘텐츠 템플릿을 찾는 방법에 대한 안내는 [Talon.One 설명서](https://docs.talon.one/docs/dev/technology-partners/braze)를 참조하세요.
2. Talon.One이 제공하는 로열티 포인트 및 추천 등의 기타 기능을 활용하려면 다음 문서를 참조하세요:
  - [Braze에서 로열티 포인트 추가](https://docs.talon.one/docs/dev/technology-partners/braze/adding-loyalty-points-braze)
  - [Braze에서 로열티 원장 가져오기](https://docs.talon.one/docs/dev/technology-partners/braze/receiving-loyalty-ledger-braze)
  - [Braze를 통해 쿠폰 생성](https://docs.talon.one/docs/dev/technology-partners/braze/creating-coupons-braze)
  - [Braze를 통해 추천 생성](https://docs.talon.one/docs/dev/technology-partners/braze/creating-referrals-braze)
  - [Braze를 통해 생일 프로모션 생성](https://docs.talon.one/docs/dev/technology-partners/braze/bday-promotion-braze)