---
nav_title: Narvar
article_title: Narvar
description: "Narvar와 Braze를 통합하는 방법을 알아보세요."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar는 주문 추적, 배송 업데이트, 반품 관리를 통해 고객 로열티를 강화하는 구매 후 플랫폼입니다. Braze와 Narvar 통합을 통해 브랜드는 Narvar의 알림 이벤트를 활용하여 Braze에서 직접 메시지를 트리거하고, 고객에게 적시에 업데이트를 제공할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Narvar 계정 | 이 파트너십을 활용하려면 Narvar 계정이 필요합니다. |
| Braze REST API 키 | `messages.send` 권한이 있는 Braze REST API 키. Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Braze 인스턴스의 URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 지원 기능 {#supported-features}

| 유형 | 지원 기능 |
|-------|----------|
| 알림 | - 배송 예상<br>- 운송사 지연<br>- 표준 배송 완료 |
| 채널 | 푸시 알림 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported features" }

{% alert note %}
추가 알림 유형이나 채널에 관심이 있으시면 Braze 및 Narvar 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 통합 세부 정보 {#integration-details}

각 알림 이벤트에 대해 Narvar는 Braze [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging/) 엔드포인트에 요청을 보내 옵트인한 각 소비자에게 푸시 메시지를 전달합니다.

Narvar는 각 메시지에 대한 푸시 알림 페이로드 구성을 담당합니다. 현재 Narvar에는 푸시 알림을 위한 내장 디자인 인터페이스가 없으므로, Narvar 팀이 귀사 팀과 협력하여 페이로드 요구 사항을 결정하고 정의합니다. 이러한 페이로드는 주문 데이터 및 소비자 세부 정보와 같은 변수 콘텐츠 플레이스홀더를 포함하여, 자체 시스템을 통해 전송하는 것과 동일한 수준으로 커스터마이즈할 수 있습니다.

## Braze-Narvar 통합 시작하기 {#getting-started-with-the-braze-narvar-integration}

1. **Narvar 고객 성공 매니저에게 연락**하여 통합에 대한 관심을 표명하세요.
2. 스테이징 및 프로덕션용 **Braze 환경을 지정**하세요.
3. Narvar가 사용할 **API 키를 Braze에서 생성**하세요.
4. 필요에 따라 Braze에서 **Campaign 키를 생성**하세요.
5. 안전한 일회성 링크를 통해 Narvar에 **API 및 Campaign 키를 제공**하세요.
6. 설정을 완료하기 위해 **푸시 알림 페이로드 세부 정보를 공유**하세요.