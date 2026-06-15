---
nav_title: Datadog
article_title: Datadog
description: "이 참조 문서에서는 SaaS 기반 데이터 분석 플랫폼을 통해 서버, 데이터베이스, 도구 및 서비스의 모니터링을 제공하는 클라우드 규모 애플리케이션용 관찰 가능성 서비스인 Braze와 Datadog의 파트너십에 대해 설명합니다."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/)은 SaaS 기반 데이터 분석 플랫폼을 통해 서버, 데이터베이스, 도구 및 서비스의 모니터링을 제공하는 클라우드 규모 애플리케이션용 관찰 가능성 서비스입니다.

Braze와 Datadog 통합을 통해 고객은 Datadog에서 Braze 데이터를 수집하고 전송되는 데이터에 대한 알림을 생성할 수 있습니다. 예를 들어, 주간 뉴스레터 Campaign이 비정상적으로 적은 양의 메시지를 발송하거나, 평소 하루에 몇 건의 메시지만 발송하던 캔버스 단계가 수천 건을 발송하기 시작하는 경우 모니터와 알림을 설정할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Datadog 계정 | 이 파트너십을 활용하려면 Datadog 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Datadog 키 생성 {#step-1-generate-datadog-key}

Datadog에서 [API 키](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys)를 생성해야 합니다. API 키를 추가하려면 **Organization Settings** > **API Keys** > **New Key**로 이동합니다.

### 2단계: Braze에 키 추가 {#step-2-add-key-to-braze}

Braze 대시보드에서 **Partner Integrations** > **Technology Partners**로 이동한 다음 **Datadog**을 검색합니다. Datadog 파트너 페이지에서 Datadog API 키를 입력합니다. 이렇게 하면 Braze가 Datadog으로 데이터를 전송할 수 있는 연결이 생성됩니다.

## Braze 이벤트 {#braze-events}

연결이 통합되면 Braze는 다음 이벤트를 Datadog으로 전송합니다:

- `braze.messaging.sent` - 발송 횟수

이러한 각 이벤트에는 다음과 같은 정보를 제공하는 Datadog 태그 형태의 메타데이터가 포함됩니다:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (사용 가능한 경우)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (사용 가능한 경우)

이러한 이벤트와 태그는 Datadog **Metrics Explorer** 페이지에서 모니터링할 수 있습니다. 이 측정기준은 DataDog에 [분포](https://docs.datadoghq.com/metrics/distributions/)로 기록됩니다. 측정기준의 특성과 DataDog의 집계 및 롤업의 부정확성을 고려하여, Braze는 전송 중 발생할 수 있는 간헐적인 네트워크 오류 또는 기타 DataDog API 오류에 대해 재시도하지 않습니다. 따라서 이러한 측정기준 수치는 Braze 대시보드 및/또는 Currents에서 확인되는 수치와 약간 다를 수 있습니다.

![]({% image_buster /assets/img/datadog.png %})