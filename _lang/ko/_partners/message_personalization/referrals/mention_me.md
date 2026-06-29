---
nav_title: Mention Me
article_title: Braze와 Mention Me 통합하기
description: Mention Me 통합 설정 가이드
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mention Me

> [Mention Me](https://www.mention-me.com/)와 Braze를 함께 사용하면 프리미엄 고객을 유치하고 흔들리지 않는 브랜드 로열티를 구축할 수 있습니다. 퍼스트파티 추천 데이터를 Braze에 원활하게 통합하여 브랜드 팬을 타겟으로 한 고도로 개인화된 옴니채널 경험을 제공할 수 있습니다.

_이 통합은 Mention Me에서 유지 관리합니다._

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항          | 설명                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Mention Me 계정   | 이 파트너십을 활용하려면 [Mention Me](https://mention-me.com/login) 계정이 필요합니다.                                                                     |
| Braze REST API 키  | `users.track` 및 `templates.email.create` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 활용 사례 {#use-cases}

* Mention Me 추천 고객의 연락처 데이터와 옵트인 정보를 실시간으로 Braze에 전송
* 추천 데이터를 사용하여 쿠폰 이메일 리마인더 생성
* 추천 데이터를 활용하여 고가치 고객을 세그먼트하고 타겟팅함으로써 다른 마케팅 채널의 성과 향상

## Mention Me에서 Braze로 어떤 데이터가 전송되나요? {#what-data-is-sent-from-mention-me-to-braze}

이 통합을 설정하면 Mention Me가 고객 속성과 이벤트를 자동으로 생성하므로 사전에 별도로 설정할 필요가 없습니다.

Braze에 있는 고객의 이메일 주소를 사용하여 관련 이벤트와 커스텀 속성을 연결합니다. Mention Me는 옵트인 상태와 관계없이 Mention Me를 통해 이 이벤트를 트리거하는 모든 잠재 고객 또는 기존 고객의 이벤트 및 연락처 프로필 속성을 전송합니다.

자세한 내용은 [연락처 프로필 속성 및 이벤트](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze)를 참조하세요.

## Mention Me 통합하기 {#integrating-mention-me}

{% alert tip %}
전체 단계별 안내는 [Mention Me의 Braze 설정 설명서](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me)를 참조하세요.
{% endalert %}

Mention Me를 Braze와 통합하려면:

1. Mention Me에서 [Braze 통합](https://mention-me.com/merchant/~/integrations/braze) 페이지로 이동한 다음 **Connect**를 선택합니다.
2. **Create New Authorization**을 선택한 다음 [이전에 생성한 API 키](#prerequisites)를 추가하고 Braze 인스턴스를 선택합니다.
3. 동기화할 국가를 하나 이상 선택합니다.
4. 완료되면 **Connect**를 선택합니다.