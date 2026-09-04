---
nav_title: FAQ
article_title: Snowflake 데이터 공유 FAQ
page_order: 50
page_type: FAQ
description: "이 문서에서는 Snowflake 데이터 공유에 대해 자주 묻는 질문에 대한 답변을 제공합니다."

---

# 자주 묻는 질문 {#frequently-asked-questions}

## Snowflake 데이터 공유를 통해 PII 데이터를 난독화할 수 있나요? {#is-it-possible-to-obfuscate-pii-data-via-snowflake-data-sharing}

아니요, 현재로서는 지원되지 않습니다.

## 동일 리전 데이터 공유와 크로스 리전 데이터 공유 중 어떤 것이 필요한가요? {#do-i-need-data-share-for-the-same-region-or-cross-region}
다음 시나리오에서는 동일 리전 데이터 공유를 사용하세요:
- Snowflake 계정이 US-EAST-1(AWS)에 있고 Braze 대시보드 리전이 미국인 경우.
- Snowflake 리전이 EU-CENTRAL-1(AWS)에 있고 Braze 대시보드 리전이 EU인 경우.
- Snowflake 리전이 AP-Northeast-1(AWS)에 있고 Braze 대시보드 리전이 일본인 경우.
- Snowflake 리전이 AP-Southeast-2(AWS)에 있고 Braze 대시보드 리전이 호주인 경우.
- Snowflake 리전이 AP-Southeast-3(AWS)에 있고 Braze 대시보드 리전이 인도네시아인 경우.

그 외의 경우에는 크로스 리전 데이터 공유를 사용하세요.

## 새 Snowflake 계정으로 전환할 때 데이터 공유는 어떻게 해야 하나요? {#what-should-i-do-with-my-data-share-when-i-switch-to-a-new-snowflake-account}
이전 Snowflake 계정에 연결된 기존 데이터 공유를 삭제한 다음 새 계정에 대한 새 공유를 생성할 수 있습니다. 모든 과거 데이터는 새 공유에서 사용할 수 있습니다.

## 데이터 공유를 새로운 Braze 워크스페이스로 전환하면 어떻게 되나요? {#what-happens-if-i-switch-my-data-share-to-a-new-braze-workspace}

기존 데이터 공유 통합을 다른 Braze 워크스페이스를 사용하도록 재구성하면, Snowflake에서 테이블을 쿼리할 때 다음과 같은 오류가 표시될 수 있습니다:

> Shared database is no longer available for use. It will need to be re-created if and when the publisher makes it available again.

이 문제를 해결하려면 Snowflake 내에서 공유를 삭제하고 다시 생성해야 합니다:

1. 이전 공유로 생성된 데이터베이스를 삭제합니다.
2. [통합 지침]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake#step-2-create-the-database-in-snowflake)에 따라 데이터베이스를 다시 생성합니다.
3. 새 데이터베이스에 필요한 접근 권한을 다시 부여합니다.
4. 이전 데이터베이스를 참조하던 뷰가 있는 경우 다시 생성합니다.

{% alert note %}
새로운 Snowflake 인터페이스에서는 **Data Products** > **Private Sharing** > **Shared with you**에서 Braze 공유를 찾을 수 있습니다.
{% endalert %}

## 데이터 공유에서 데이터가 표시되지 않는 이유는 무엇인가요? {#why-dont-i-see-data-in-my-data-share}
데이터 공유를 생성할 때 잘못된 Snowflake 계정 ID를 사용했을 수 있습니다. 데이터 공유 대시보드의 계정 ID는 Snowflake 계정에서 `CURRENT_ACCOUNT()`의 출력과 일치해야 합니다.

공유가 리전 간(cross region)인 경우 데이터가 즉시 사용 가능하지 않을 수 있습니다. 데이터 볼륨에 따라 해당 리전으로 데이터가 동기화되는 데 몇 시간이 걸릴 수 있습니다.

## 데이터 공유를 생성할 때 HIPAA(미국의료정보보호법) 준수 오류가 발생하는 이유는 무엇인가요? {#why-am-i-receiving-a-hipaa-compliance-error-when-creating-a-data-share}

지정된 계정이 HIPAA(미국의료정보보호법)를 준수하지 않거나 [Snowflake 에디션](https://docs.snowflake.com/en/user-guide/intro-editions)이 Business Critical보다 낮은 경우에 발생합니다. 데이터 공유에서 HIPAA(미국의료정보보호법)를 준수하려면 Snowflake 계정을 Business Critical Edition으로 업그레이드해야 합니다. 계정 업그레이드에 대한 추가 지원은 Snowflake 고객지원에 문의하세요.

## 데이터 공유를 삭제한 후 다시 생성할 수 없는 이유는 무엇인가요? {#why-cant-i-recreate-a-data-share-after-deleting-one}

시스템이 이전 데이터 공유의 삭제를 아직 처리 중일 수 있습니다. 프로비저닝 해제 프로세스가 완료될 때까지 몇 분 정도 기다린 후 새 데이터 공유를 다시 생성해 보세요.

## 여러 워크스페이스가 동일한 Snowflake 계정으로 데이터를 공유할 때 `CREATE DATABASE`를 몇 번 실행해야 하나요? {#how-many-times-do-i-need-to-run-create-database-when-i-have-multiple-workspaces-sharing-data-to-the-same-snowflake-account}

`CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>`는 한 번만 실행하면 됩니다. 서로 다른 Braze 워크스페이스의 여러 데이터 공유가 동일한 Snowflake 계정으로 공유되면, 자동으로 동일한 공유에 결합됩니다. 초기 데이터베이스를 생성한 후에는 추가 워크스페이스의 데이터가 별도의 공유 요청이나 데이터베이스 생성 단계 없이 기존 데이터베이스에 자동으로 추가됩니다.

예를 들어, 워크스페이스 A에서 Snowflake 계정 123으로 데이터 공유를 생성하면 공유 요청을 수락하고 데이터베이스를 생성합니다. 이후 워크스페이스 B에서 동일한 Snowflake 계정 123으로 데이터 공유를 생성하면 새로운 공유 요청이 전송되지 않으며, 데이터가 기존 공유에 즉시 추가되어 이전에 생성한 데이터베이스에서 사용할 수 있게 됩니다.

## 여러 워크스페이스가 있는 경우, 하나의 데이터베이스에 모든 워크스페이스의 데이터가 포함되나요? {#if-i-have-multiple-workspaces-does-a-single-database-contain-data-from-all-of-them}

네. 여러 Braze 워크스페이스의 데이터를 동일한 Snowflake 계정에 공유하면, 모든 데이터가 하나의 공유에 결합되어 동일한 데이터베이스에서 사용할 수 있습니다. `app_group_id`로 데이터를 필터링하여 워크스페이스를 구분할 수 있습니다.

모범 사례로, 향후를 대비하여 쿼리에서 항상 `app_group_id`로 필터링하는 것을 권장합니다. 이렇게 하면 나중에 워크스페이스를 추가하더라도 대시보드와 보고서가 정확하게 유지됩니다. 이 필터가 없으면 새로 추가된 워크스페이스의 데이터가 측정기준에 예기치 않게 포함될 수 있습니다.

## 여러 워크스페이스의 데이터를 Snowflake에서 관리하는 데 권장되는 접근 방식은 무엇인가요? {#what-is-the-recommended-approach-for-managing-data-from-multiple-workspaces-in-snowflake}

모든 Braze 데이터를 동일한 데이터베이스로 전송하고 `app_group_id`로 필터링하여 워크스페이스를 구분하세요. 이 접근 방식은 데이터 관리를 간소화하고 조직 전체에서 일관된 리포팅을 보장합니다.

## 여러 워크스페이스에 Snowflake 데이터 공유 커넥터가 몇 개 필요한가요? {#how-many-snowflake-data-share-connectors-do-i-need-for-multiple-workspaces}

필요한 커넥터 수는 특정 구성 및 자격에 따라 다릅니다. 사용 사례에 적합한 자격에 대해 자세히 알아보려면 Braze 계정 팀에 문의하세요.

## 동일한 Snowflake 계정 내에서 서로 다른 워크스페이스의 데이터를 격리하는 방법에는 어떤 것이 있나요? {#what-options-exist-for-isolating-data-from-different-workspaces-within-the-same-snowflake-account}

각 데이터 행이 어떤 워크스페이스에 속하는지를 식별하는 `app_group_id` 열을 사용하여 논리적으로 격리할 수 있습니다. 가장 일반적인 접근 방식은 다음과 같습니다:

- **뷰(권장):** `app_group_id`로 필터링된 각 워크스페이스에 대한 뷰를 생성합니다. 이렇게 하면 데이터를 복제하지 않으면서도 각 팀이나 사용 사례에 해당 워크스페이스 데이터에 대한 깔끔하고 범위가 지정된 뷰를 제공할 수 있습니다.
- **로컬 테이블 복사:** `app_group_id`로 필터링된 데이터를 별도의 테이블에 복사합니다. 이 방법은 데이터가 복제되므로 일반적으로 뷰 접근 방식이 선호됩니다.
- **행 액세스 정책 및 역할:** Snowflake 네이티브 행 액세스 정책과 역할을 결합하여 각 역할이 쿼리할 수 있는 행을 제한합니다. 이렇게 하면 데이터를 단일 테이블에 유지하면서 쿼리 시점에 액세스를 적용할 수 있습니다.

이러한 설정은 Snowflake 계정 내에서 구성합니다.

## 서로 다른 워크스페이스의 데이터를 격리하기 위해 다른 Snowflake 계정을 사용할 수 있나요? {#can-i-use-a-different-snowflake-account-to-isolate-data-from-different-workspaces}

네. 워크스페이스 A가 계정 X에 공유하고 워크스페이스 B가 계정 Y에 공유하면, 각 계정은 별도의 데이터가 포함된 독립적인 공유를 수신합니다. 그러나 대부분의 조직은 모든 비즈니스 데이터에 단일 Snowflake 계정을 사용합니다. 따라서 이 접근 방식은 운영 오버헤드를 증가시킬 수 있습니다. 이전 섹션에서 설명한 논리적 격리 접근 방식 대신 이 방법을 선택하기 전에 이러한 트레이드오프를 고려하세요.

## 워크스페이스 데이터 격리는 Snowflake 데이터 공유에서 지원되는 사용 사례인가요? {#is-workspace-data-isolation-a-supported-use-case-for-snowflake-data-sharing}

네, 이전 섹션에서 설명한 논리적 격리 방식을 통해 가능합니다. Braze는 각 워크스페이스에 대해 별도의 공유를 생성하지 않으므로, Snowflake 수준에서 뷰, 행 액세스 정책 또는 별도의 계정을 사용하여 격리를 관리합니다.