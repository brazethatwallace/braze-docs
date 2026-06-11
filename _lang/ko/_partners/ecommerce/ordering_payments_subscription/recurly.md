---
nav_title: Recurly
article_title: Recurly
description: "Recurly는 구독 성장과 반복 매출 확대를 추구하는 D2C 브랜드를 위한 선도적인 구독 관리 및 청구 플랫폼입니다."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/)는 구독 관리 및 청구 플랫폼입니다. Recurly 통합 플랫폼은 새로운 요금제, 오퍼, 프로모션 테스트부터 결제 수단, 통합, 인사이트 관리까지 팀이 가입자 경험을 관리하고 최적화할 수 있도록 지원하여 대규모 구독 라이프사이클 자동화를 간소화합니다.

_이 통합은 Recurly에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Recurly와 Braze 간의 통합은 구독 데이터를 Braze와 공유하는 프로세스를 간소화하여 고객과의 타겟 커뮤니케이션을 가능하게 합니다.

- Braze에서 Recurly 구독 라이프사이클 이벤트(예: 구독 갱신, 일시 중지 또는 취소)를 활용하여 개인화된 Campaign과 커뮤니케이션을 트리거합니다.
- Recurly 구독 데이터(예: 구독 요금제, 애드온 또는 상태)를 활용하여 회사 사용자, Segments, Canvases를 생성 및 관리하고 코호트별 Campaign과 커뮤니케이션을 실행합니다.
- Recurly 데이터를 Braze로 직접 전송하여 추가 메시징 사용 사례를 지원하고 개발 오버헤드 비용을 절감합니다.

Recurly와 Braze를 함께 사용하는 방법에 대한 자세한 내용은 [Recurly 문서](https://docs.recurly.com/docs/braze-integration)에서 확인할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Recurly 계정 | 이 파트너십을 활용하려면 Braze 피처 플래그가 활성화된 Elite [Recurly](https://recurly.com/) 구독 요금제가 필요합니다. Recurly 플랫폼에서 크레딧 인보이스 활성화도 필요합니다.|
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. Recurly는 `users.track` 엔드포인트만 사용하므로 이 권한만 부여된 Recurly 전용 키를 프로비저닝하는 것을 권장합니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

시작하기 전에 Braze와 Recurly 모두에서 활성 계정이 있는지 확인하세요.

### Recurly를 Braze에 연결하기 {#connect-recurly-to-braze}

1. Recurly에서 **Integrations** > **Braze**로 이동합니다. Recurly에서 Braze 통합 구성 페이지로 처음 이동하면 인터페이스에서 두 시스템을 연결하라는 메시지가 표시됩니다.

2. 다음 자격 증명을 입력합니다:

- **Instance URL:** 프로비저닝된 인스턴스의 Braze REST 엔드포인트.
- **API Key (Identifier):** Recurly가 Braze에 요청을 보낼 때 사용할 Braze REST API 키.

Braze 인스턴스의 URL을 복사하는 것을 잊지 마세요. 예를 들어, URL은 다음과 같을 수 있습니다:

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3. 자격 증명을 입력한 후 **Connect**를 클릭합니다.

## 이 통합 사용하기 {#using-this-integration}

### 지원되는 식별자 {#supported-identifiers}

Recurly는 계정의 `account_code`를 Braze의 `external_id`로 사용합니다. 따라서 Recurly 계정의 `account_code`는 Braze 사용자의 `external_id`와 일치해야 합니다.

### 커스텀 이벤트 {#custom-events}

효과적인 고객 참여를 위해 Recurly에서 트리거되는 이벤트를 수신하려면 Braze에서 [커스텀 이벤트를 구성]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)해야 합니다. 철저한 데이터 통합을 위해 Recurly의 각 이벤트를 포함해야 합니다. 이러한 이벤트는 [Braze 분석]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics)에서도 추적할 수 있습니다. 구성이 완료되면 이러한 커스텀 이벤트를 사용하여 사용자를 세그먼트하거나 메시징을 개인화할 수 있습니다.

| Braze 커스텀 이벤트 | Recurly 이벤트 |
| ----------- | ----------- |
| Recurly New Subscription              | 구독이 생성될 때 트리거됨                            |
| Recurly Renewed Subscription          | 구독이 갱신될 때 트리거됨                                |
| Recurly Updated Subscription          | 구독 속성이 변경될 때 트리거됨(요금제 변경, 가격 변경 또는 수량 변경) |
| Recurly Canceled Subscription         | 구독이 취소될 때 트리거됨                           |
| Recurly Reactivated Subscription      | 취소된 구독이 재활성화될 때 트리거됨               |
| Recurly Paused Subscription           | 구독이 일시 중지로 설정될 때 트리거됨                   |
| Recurly Resumed Subscription          | 구독 일시 중지가 해제될 때 트리거됨                              |
| Recurly Subscription Expired          | 구독이 만료될 때 트리거됨                               |
| Recurly Invoice Created               | 인보이스가 생성될 때 트리거됨                                |
| Recurly Successful Payment            | 인보이스가 성공적으로 수금될 때 트리거됨                 |
| Recurly Refund Issued                 | 환불이 발행될 때 트리거됨                                   |
| Recurly Failed Recurring Payment      | 구독 갱신 시 인보이스가 실패할 때 트리거됨          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom events" }

### 일괄 처리 및 사용량 제한 {#batching-and-rate-limiting}

Recurly는 Braze `/users/track` 엔드포인트를 사용하므로 이 통합은 분당 50,000건의 표준 Braze 사용량 제한이 적용됩니다.

Recurly는 특정 구독 라이프사이클 이벤트를 단일 API 호출로 일괄 처리하여 Braze에 대한 요청 횟수를 줄입니다.

- Recurly는 동시에 생성된 여러 구독을 일괄 처리하여 단일 요청으로 전송합니다.
- Recurly는 한 계정에 대한 동시 갱신 여러 건을 단일 요청으로 일괄 처리합니다.
- Recurly는 동일 모델의 구독 라이프사이클 이벤트를 단일 요청으로 전송합니다. 예를 들어, 결제와 함께 새로 생성된 인보이스는 `Recurly Invoice Created`와 `Recurly Successful Payment` 커스텀 이벤트가 모두 포함된 하나의 API 요청을 생성합니다.

일괄 처리는 한 번에 최대 75개의 이벤트 그룹으로 Braze에 전송됩니다. 예를 들어, 100개의 구독이 한꺼번에 생성되면 Recurly는 Braze에 두 번의 API 요청을 보냅니다. 자세한 내용은 [User Track 요청 일괄 처리]({{site.baseurl}}/api/api_limits/#batch-user-track)를 참조하세요.