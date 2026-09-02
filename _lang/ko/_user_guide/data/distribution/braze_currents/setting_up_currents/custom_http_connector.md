---
nav_title: 커스텀 커런츠 내보내기
article_title: 커스텀 커런츠 내보내기
alias: /currents/custom_http_connector/
page_order: 3
page_type: reference
tool: Currents
description: "이 참조 문서에서는 Braze Currents 이벤트 데이터를 자체 HTTP 엔드포인트로 실시간 스트리밍하기 위해 커스텀 커런츠 내보내기를 설정하는 방법을 설명합니다."
---

# 커스텀 커런츠 내보내기 {#custom-currents-export}

> 커스텀 Currents 커넥터를 통합하여 Braze에서 실시간으로 이벤트 데이터를 수신하고, 보다 맞춤화된 분석, 보고서 및 자동화를 구현하는 방법을 알아보세요.

{% alert note %}
이 기능은 기술 설명서 및 API 참조에서 커스텀 HTTP 커넥터라고도 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

Braze에서 커스텀 Currents 커넥터를 통합하려면 엔드포인트 URL과 [선택 사항인 인증 토큰](#authentication)을 제공해야 합니다.

또한 Braze에 앱 그룹이 두 개 이상 있는 경우, 각 그룹에 대해 커스텀 Currents 커넥터를 구성해야 합니다. 그러나 모든 앱 그룹을 동일한 엔드포인트로 지정하거나, `your_app_group_key="Brand A"`와 같은 추가 `GET` 파라미터가 포함된 엔드포인트로 지정할 수 있습니다.

## 통합 {#integration}

### 1단계: 엔드포인트 설정 {#step-1-set-up-your-endpoint}

이 통합을 구성하려면 엔드포인트 URL이 필요합니다. 엔드포인트는 HTTP POST 요청을 수신하고, 이벤트 수신이 성공했음을 확인하기 위해 `2XX` 상태 코드를 반환할 수 있어야 합니다. Braze에서 보내는 요청을 인증하려면 베어러 토큰도 필요합니다.

### 2단계: Braze Currents 구성 {#step-2-configure-braze-currents}

Braze에서 **파트너 통합** > **데이터 내보내기**로 이동한 후 **새 커런트 생성**을 클릭하고 **커스텀 커런츠 내보내기**를 선택합니다.

내보내기 이름과 연락처 이메일을 입력한 다음 **커런트 세부 정보** 페이지로 이동합니다. 이 페이지에서 엔드포인트 URL과 선택 사항인 베어러 토큰을 입력합니다.

자격 증명을 구성한 후, 내보내려는 모든 메시지 인게이지먼트, 고객 행동 및 사용자 이벤트를 선택하고 **커런트 시작**을 클릭합니다.

## 지원되는 Currents 이벤트 {#supported-currents-events}

Braze는 다음 데이터를 커스텀 HTTP 커넥터로 내보내는 것을 지원합니다:

- [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events?tab=custom%20http%20connector)
- [고객 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events?tab=custom%20http%20connector)

각 이벤트의 페이로드 구조를 확인하려면 이벤트 용어집에서 **Custom HTTP Connector** 탭을 선택하세요.

## 데이터 손실 방지 {#preventing-data-loss}

### 오류 모니터링 {#error-monitoring}

데이터 손실과 서비스 중단을 방지하려면 항상 엔드포인트를 모니터링하고 오류나 중단 시간이 발생하면 신속하게 대응하는 것이 중요합니다.

대부분의 오류 유형(서버 오류 및 네트워크 연결 오류 등)에 대해 Braze는 이벤트 전송을 적극적으로 재시도합니다. 문제가 5일 이상 지속되면 통합이 자동으로 비활성화됩니다. 이후 수신되는 새 이벤트는 삭제되며 영구적으로 손실됩니다.

### 변경 복원력 {#change-resilience}

Braze 커런츠 스키마에 비파괴적 변경이 이루어지는 경우가 있습니다. 비파괴적 변경이란 새로운 nullable 열이나 이벤트 유형을 추가하는 것을 의미합니다.

일반적으로 이러한 변경에 대해 2주 전에 공지하지만, 항상 가능한 것은 아닙니다. 인식할 수 없는 필드나 이벤트 유형을 처리할 수 있도록 통합을 설계하는 것이 중요합니다. 그렇지 않으면 데이터 손실이 발생할 가능성이 높습니다.

{% alert tip %}
Currents 이벤트 스키마의 전체 목록은 [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 및 [고객 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)를 참조하세요.
{% endalert %}

## 일괄 처리 및 직렬화 {#batching-and-serialization}

대상 데이터 형식은 HTTPS를 통한 JSON입니다. 기본적으로 이벤트는 최대 100개씩 일괄 처리되어 엔드포인트로 전송됩니다.

이벤트는 다음 형식의 JSON 배열로 엔드포인트에 전송됩니다.

```json
{"events": [event1, event2, event3, etc...]}
```

최상위 JSON 오브젝트에는 `"events"` 키가 있으며, 이 키는 개별 이벤트를 나타내는 JSON 오브젝트의 배열에 매핑됩니다. 각 이벤트에는 두 개의 하위 오브젝트가 포함됩니다.

| 이름 | 설명 |
|----|-----------|
| `"user"` | `user_id`, `external_user_id`, `device_id`, `timezone` 등의 사용자 속성을 포함합니다. |
| `"properties"` | 이벤트가 적용되는 `app/campaign/canvas/platform` 등 이벤트의 속성을 포함합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

다운스트림 엔드포인트가 이벤트가 0개인 페이로드 또는 빈 요청 본문을 수신하는 경우, 이 호출로 인해 다운스트림에 어떠한 영향도 발생하지 않아야 하므로 해당 결과는 무연산(no-op)으로 간주해야 합니다. 다만, 일반 API 호출과 마찬가지로 `Authorization` 헤더를 확인하고 [유효하지 않은 자격 증명](#authentication)에 대해 `401` 또는 `403`과 같은 적절한 HTTP 응답을 반환해야 합니다. 이를 통해 Braze는 커넥터의 자격 증명이 유효한지 확인할 수 있습니다.

## 인증 {#authentication}

페이로드의 인증 토큰은 선택 사항입니다. [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1)에 명시된 대로 `Bearer` 인증 방식을 사용하여 HTTP `Authorization` 헤더를 통해 전달할 수 있습니다. 선택 사항이지만, 인증 토큰이 전달되면 Braze는 페이로드에 이벤트가 없더라도 항상 먼저 유효성을 검사합니다.

RFC 6750에 따르면, 토큰은 최소 한 문자 이상의 Base64 인코딩 값이어야 합니다. RFC 6750은 일반 Base64 문자 외에 `-`, `.`, `_`, `~` 문자도 토큰에 포함할 수 있도록 허용합니다. 이러한 문자를 토큰에 포함할지 여부는 선택할 수 있지만&#8212;반드시 Base64 형식이어야 합니다.

또한 `Authorization` 헤더가 있는 경우 다음 형식으로 구성됩니다:

```plaintext
"Authorization: Bearer " + <token>
```

예를 들어, 인증 토큰이 `0p3n5354m3==`인 경우 `Authorization` 헤더는 다음과 유사해야 합니다:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
향후 Braze는 `Authorization` 헤더를 사용하여 Braze 고유의 커스텀 키-값 쌍 인증 방식을 구현할 수 있습니다. 이는 Amazon Web Services(AWS)와 같은 일부 기업이 인증 방식을 구현하는 방법인 [RFC 7235](https://tools.ietf.org/html/rfc7235) 사양을 준수하게 됩니다.
{% endalert %}

## 버전 관리 {#versioning}

HTTP 커넥터 통합의 모든 요청은 Currents 요청의 버전을 나타내는 커스텀 헤더와 함께 전송됩니다:

```plaintext
Braze-Currents-Version: 1
```

이 버전은 항상 `1`이며, 이 번호를 자주 증가시킬 계획은 없습니다.

[데이터 웨어하우스 스토리지 스키마]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics?redirected=1)와 마찬가지로, 개별 이벤트의 모든 이벤트 필드는 [Apache Avro](https://avro.apache.org/)의 역호환성 정의에 따라 이전 이벤트 페이로드 버전과의 역호환성이 보장됩니다:

1. 특정 이벤트 필드는 시간이 지나도 항상 동일한 데이터 유형을 유지합니다.
2. 시간이 지남에 따라 페이로드에 추가되는 새로운 필드는 모든 당사자가 선택 사항으로 간주해야 합니다.
3. 필수 필드는 절대 제거되지 않습니다.

## 오류 처리 및 재시도 메커니즘 {#error-handling-and-retry-mechanism}

오류가 발생하면 Braze는 수신한 HTTP 반환 코드에 따라 요청을 대기줄에 넣고 재시도합니다. 문제가 5일 이상 지속되면 통합이 자동으로 비활성화됩니다. 새로 수신되는 이벤트는 삭제되어 영구적으로 손실되며, 이미 대기줄에 있는 이벤트는 7일간 유지된 후 영구적으로 삭제됩니다. 데이터가 24시간 이상 정체되면 당직 엔지니어에게 자동으로 알림이 전송됩니다. 각 상태 코드가 어떻게 처리되는지에 대한 전체 내역은 다음 섹션의 표를 참조하세요.

Currents 통합에서 인증 오류가 반환되면 Braze에서 자동으로 알림 이메일을 발송합니다.

다음 섹션에 나열되지 않은 HTTP 오류 코드는 HTTP `5XX` 오류로 처리됩니다.

{% alert warning %}
문제가 5일 이상 지속되면 통합이 비활성화됩니다. 새로 수신되는 이벤트는 삭제되어 영구적으로 손실되며, 이미 대기줄에 있는 이벤트는 7일간 유지된 후 영구적으로 삭제됩니다.
{% endalert %}

다음 HTTP 상태 코드는 커넥터 클라이언트에서 인식됩니다.

<table aria-label="오류 처리 및 재시도 메커니즘">
  <thead>
    <tr>
      <th>상태 코드</th>
      <th>응답</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>성공</td>
      <td>이벤트 데이터가 다시 전송되지 않습니다.</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>서버 측 오류</td>
      <td>이벤트 데이터가 지터(jitter)를 포함한 지수 백오프 패턴으로 재전송됩니다. 문제가 5일 이상 지속되면 통합이 비활성화되며, 이미 대기줄에 있는 이벤트는 7일간 유지됩니다.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>클라이언트 측 오류</td>
      <td>커넥터가 하나 이상의 잘못된 형식의 이벤트를 전송했습니다. 이벤트 데이터는 크기 1의 배치로 분할되어 재전송됩니다. 이 크기 1 배치에서 또다시 <code>400</code> 응답을 받는 이벤트는 영구적으로 삭제됩니다.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>인증 실패</td>
      <td>커넥터가 잘못된 자격 증명으로 구성되었습니다. 실패한 이벤트는 재전송되지 않습니다. 자격 증명을 수정하고 통합을 다시 활성화하여 재개하세요. 문제가 5일 이상 지속되면 통합이 비활성화되며, 이미 대기줄에 있는 이벤트는 7일간 유지됩니다.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>금지됨</td>
      <td>커넥터가 잘못된 자격 증명으로 구성되었습니다. 실패한 이벤트는 재전송되지 않습니다. 자격 증명을 수정하고 통합을 다시 활성화하여 재개하세요. 문제가 5일 이상 지속되면 통합이 비활성화되며, 이미 대기줄에 있는 이벤트는 7일간 유지됩니다.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>찾을 수 없음</td>
      <td>커넥터가 잘못된 엔드포인트 URL 또는 유효하지 않은 자격 증명으로 구성되었습니다. 엔드포인트 URL이 올바르고 접근 가능한지 확인하세요. 구성을 수정하고 통합을 다시 활성화하여 재개하세요. 문제가 5일 이상 지속되면 통합이 비활성화되며, 이미 대기줄에 있는 이벤트는 7일간 유지됩니다.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>페이로드 너무 큼</td>
      <td>이벤트 데이터가 더 작은 배치로 분할되어 재전송됩니다.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>요청이 너무 많음</td>
      <td>사용량 제한조치를 나타냅니다. 이벤트 데이터가 지터(jitter)를 포함한 지수 백오프 패턴으로 재전송됩니다. 문제가 5일 이상 지속되면 통합이 비활성화되며, 이미 대기줄에 있는 이벤트는 7일간 유지됩니다.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }