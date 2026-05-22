---
nav_title: 스냅샷과 이벤트 스트림 비교
article_title: 스냅샷과 이벤트 스트림 비교
page_order: 4
page_type: reference
description: "이 참조 문서에서는 스냅샷 데이터와 이벤트 스트림 데이터의 차이점, 그리고 각각을 BrazeAI Decisioning Studio에 전달하기 위해 어떻게 구조화하고 전달해야 하는지 설명합니다."
---

# 스냅샷과 이벤트 스트림 비교 {#snapshots-versus-event-streams}

> 데이터는 스냅샷(상태)과 이벤트 스트림(발생한 일)이라는 두 가지 기본 범주 중 하나에 속합니다. 이 구분을 이해하고 올바르게 적용하는 것은 Decisioning Studio 에이전트가 효과적으로 학습하도록 하기 위해 할 수 있는 가장 중요한 일 중 하나입니다.

## 스냅샷 데이터(상태) {#snapshot-data-state}

스냅샷은 특정 시점에서 고객의 상태를 나타냅니다. "이 고객이 지금 어떤 모습인가?"라는 질문에 답합니다.

스냅샷은 정적이고 집계된 데이터입니다. 해당 시점까지의 모든 변경 사항의 누적 결과를 반영합니다. 이는 고객 프로필, 계산된 피처(예: "마지막 구매 이후 경과 일수", "로열티 등급", "고객이탈 점수")에 가장 적합합니다.

### 필수 필드 {#required-fields}

| 필드 | 목적 |
|-------|---------|
| 고객 식별자 | 이 레코드가 설명하는 대상 |
| 스냅샷 날짜 | 이 스냅샷이 생성된 시점 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Required fields" }

### 스냅샷 업데이트 방법 {#how-snapshots-should-be-updated}

- **트리거:** 이벤트 기반이 아닌 시간 기반입니다. 스냅샷은 해당 날짜에 고객 활동이 있었는지 여부와 관계없이 고정된 스케줄(예: 매일)에 따라 생성해야 합니다.
- **범위:** 모든 업데이트에는 이벤트가 없었던 고객을 포함하여 모든 관련 고객이 포함되어야 합니다.
- **방법:** 이전 값을 덮어쓰는 대신 데이터셋에 새 스냅샷 레코드를 추가합니다. 이렇게 하면 모델 학습을 위한 과거 상태가 보존됩니다.

### 일일 전달을 위한 스냅샷 데이터 쿼리 {#query-snapshot-data-for-daily-delivery}

Decisioning Studio는 하루에 한 번 추천 파이프라인을 실행합니다. 스냅샷 데이터를 전달할 때 각 파이프라인 실행 시 전날의 스냅샷을 내보냅니다:

```sql
SELECT *
FROM snapshot_data
WHERE snapshot_date = {t-1} -- on pipeline run date t, export the snapshot from t-1
```

## 이벤트 스트림 데이터(흐름) {#event-stream-data-flow}

이벤트 스트림은 개별 동작이 발생할 때 기록합니다. "이 고객이 무엇을 했고, 언제 했는가?"라는 질문에 답합니다. 이벤트 스트림은 원시적이고, 불변이며, 증분적이고, 시간순인 데이터에 이상적입니다. 각 레코드는 특정 시점에 발생한 하나의 사건을 나타냅니다. 예를 들어, 활성화 레코드, 참여 로그(열기, 클릭), 전환 이벤트 또는 쿠폰 사용에 이 데이터 스트림을 사용합니다.

### 필수 필드

| 필드 | 목적 |
|-------|---------|
| 고객 식별자 | 이 이벤트의 대상 |
| 이벤트 유형 | 발생한 일(예: 활성화, 전환, 클릭) |
| 이벤트 타임스탬프 | 이벤트가 실제로 발생한 시점 |
| 생성 타임스탬프 | 이 레코드가 시스템에 생성된 시점(아래 참고 사항 참조) |
| 이벤트 등록정보 | 이벤트에 대한 추가 메타데이터; 이 정보가 풍부할수록 Decisioning Studio가 고객 여정 전반에 걸쳐 이벤트를 더 잘 연결할 수 있습니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Required fields" }

{% alert important %}
이벤트 타임스탬프와 생성 타임스탬프는 서로 다른 필드이며 둘 다 필수입니다. 이벤트 타임스탬프는 동작이 실제로 발생한 시점을 기록합니다. 생성 타임스탬프는 데이터 항목이 시스템에 기록된 시점을 기록하며, 처리 지연으로 인해 더 늦을 수 있습니다. 이 두 가지를 혼동하지 마세요.
{% endalert %}

### 이벤트 스트림 업데이트 방법 {#how-event-streams-should-be-updated}

- **트리거:** 이벤트 기반입니다. 새 이벤트가 발생하면 새 레코드가 추가됩니다.
- **범위:** 이벤트가 있었던 고객만 새 레코드를 받습니다.
- **방법:** 기존 레코드는 불변입니다. 업데이트는 항상 새 레코드의 삽입입니다.

### 일일 전달을 위한 이벤트 데이터 쿼리 {#query-event-data-for-daily-delivery}

일일 내보내기를 분할할 때 `event_timestamp`가 아닌 `create_timestamp`를 사용하세요. 이벤트는 발생 후에 시스템에 기록되는 경우가 있습니다(지연 도착). `event_timestamp`로 분할하면 지연 도착한 레코드가 영구적으로 누락됩니다.

```sql
-- Correct: use create_timestamp to ensure late-arriving events are captured
SELECT *
FROM events_data
WHERE DATE(create_timestamp) = {t-1} -- on run date t, export all records created yesterday
```

```sql
-- Incorrect: slicing on event_timestamp will permanently lose late-arriving events
SELECT *
FROM events_data
WHERE DATE(event_timestamp) = {t-1}
```

예를 들어, 이벤트가 1월 1일에 발생했지만 1월 2일까지 시스템에 기록되지 않은 경우, 1월 2일에 `event_timestamp`로 분할하면 해당 이벤트가 완전히 누락됩니다. `create_timestamp`로 분할하면 올바르게 캡처됩니다.

## 네이티브 Braze 통합의 경우 {#for-native-braze-integrations}

Braze는 이 두 가지 데이터 유형에 직접 매핑되는 두 가지 기본 제공 메커니즘을 제공합니다.

### 커스텀 속성: 스냅샷 데이터 {#custom-attributes-snapshot-data}

커스텀 속성은 특정 시점의 사용자 수준 상태를 저장합니다. 고객 프로필 및 계산된 피처(예: `churn_score`, `total_purchases_last_30d`)에 적합한 수단입니다. 커스텀 속성은 축적이 아닌 덮어쓰기 방식이므로 원시 이벤트 데이터에는 **적합하지 않습니다**.

### Braze 커런츠: 이벤트 스트림 데이터 {#braze-currents-event-stream-data}

Braze 커런츠는 원시적이고 불변인 이벤트 흐름 데이터를 제공합니다. `USER_BEHAVIOR_CUSTOM_EVENTS` 테이블은 커스텀 이벤트가 발생할 때마다 모든 인스턴스를 캡처하므로, 활성화, 참여 및 전환 이벤트의 올바른 소스입니다.

{% alert tip %}
커스텀 속성은 고객 상태의 소스로, Braze 커런츠는 고객 행동 이벤트의 소스로 취급하세요. 원시 이벤트 데이터를 Decisioning Studio에 전달하기 위해 커스텀 속성을 사용하지 마세요.
{% endalert %}

## 일반적인 문제 {#common-issues}

### 이벤트 데이터를 스냅샷으로 전달 {#pass-event-data-as-a-snapshot}

이벤트 데이터를 Decisioning Studio에 보내기 전에 스냅샷 필드로 집계하면 여러 문제가 발생합니다:

- **세분성 손실:** 데이터가 일별 고객 수준 요약으로 집계되면 개별 이벤트 레코드가 사라집니다. Decisioning Studio는 이를 재구성할 수 없습니다.
- **부정확한 타임스탬프:** "last_email_sent"와 같은 필드는 가장 최근 발생 시점을 알려주지만 전체 이벤트 이력을 잃게 되어 정확한 기여도 분석이 불가능해집니다.
- **팬텀 업데이트:** 이벤트가 발생하지 않은 날에도 스냅샷 레코드가 업데이트되어 중복 제거가 어려운 중복 항목이 생성됩니다.

Braze를 사용하는 경우, 원시 이벤트 데이터를 Decisioning Studio에 전달하려면 커스텀 속성이 아닌 Currents 내보내기를 사용하세요.

### 이벤트 트리거로 스냅샷 데이터 업데이트 {#update-snapshot-data-on-an-event-trigger}

일부 구현에서는 이벤트가 발생할 때만 스냅샷 데이터를 업데이트합니다. 예를 들어, 고객이 구매할 때만 피처를 재계산하는 경우입니다. 이렇게 하면 시간 경과에 의존하는 피처가 최근 이벤트가 없는 고객에 대해 오래된 값으로 남게 됩니다.

예를 들어, `days_since_last_purchase`와 같은 피처는 매일 다른 올바른 값을 가집니다. 구매가 발생할 때만 재계산되면 최근에 구매하지 않은 모든 고객에 대해 잘못된 값으로 고정됩니다. 항상 모든 고객을 대상으로 매일 시간 기반 스케줄에 따라 스냅샷 데이터를 업데이트하세요.