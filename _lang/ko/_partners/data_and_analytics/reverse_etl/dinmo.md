---
nav_title: DinMo
article_title: DinMo
description: "이 참조 문서에서는 리버스 ETL을 사용하여 데이터 웨어하우스 데이터를 Braze로 동기화하는 구성 가능한 고객 데이터 플랫폼인 DinMo와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/dinmo/
page_type: partner
search_tag: Partner

---

# DinMo

> [DinMo](https://www.dinmo.com/)는 리버스 ETL(Extract, Transform, Load)을 통해 클라우드 데이터 웨어하우스를 Braze에 연결하는 구성 가능한 고객 데이터 플랫폼(CDP)입니다. 마케팅 팀은 데이터 웨어하우스 데이터에서 오디언스 세그먼트를 구축하고, 사용자 속성 및 이벤트를 Braze로 동기화하며, CSV 업로드나 엔지니어링 지원 없이 구독 상태를 최신으로 유지할 수 있습니다.

_이 통합은 DinMo에서 관리합니다._

Braze와 DinMo 통합은 Braze REST API를 통해 데이터 웨어하우스의 세그먼트 및 데이터 모델을 Braze로 푸시합니다. DinMo에서 Braze 대상을 연결하면, 활성화를 통해 모델 또는 세그먼트의 데이터가 Braze로 전송됩니다.

## 사전 요구 사항 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| DinMo 계정 | 이 파트너십을 활용하려면 대상을 생성할 수 있는 권한이 있는 [DinMo 계정](https://www.dinmo.com/)이 필요합니다. |
| Braze REST API 키 | 사용하려는 대상 서비스에 필요한 [권한](#api-key-permissions)이 있는 Braze REST API 키. Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 Braze 인스턴스의 [API 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)에 따라 달라집니다. |
| Braze 대시보드 URL | 인스턴스에 대한 Braze 대시보드 URL(예: `https://dashboard.iad-01.braze.com`). 자세한 내용은 [사용 가능한 SDK 엔드포인트]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)를 참조하세요. |
| 데이터 웨어하우스 및 데이터 모델 | 통합을 시작하기 전에 DinMo에서 데이터 웨어하우스를 연결하고 Braze에 동기화할 데이터에 대한 모델 또는 Segment를 정의하세요. 자세한 내용은 [DinMo Braze 통합 가이드](https://docs.dinmo.io/integrations/destination-platforms/braze)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## 사용 사례 {#use-cases}

이 통합을 통해 다음을 수행할 수 있습니다:

* 데이터 웨어하우스의 사용자 속성을 Braze로 동기화하여 Campaigns와 Canvases를 개인화할 수 있습니다.
* 데이터 웨어하우스 데이터에서 커스텀 이벤트 및 구매 이벤트를 Braze로 전송하여 행동 기반 타겟팅에 활용할 수 있습니다.
* DinMo에서 정의한 오디언스 Segments에 맞춰 Braze 구독 그룹 멤버십을 동기화할 수 있습니다.
* DinMo Segments를 Braze 사용자 속성으로 내보내고, 해당 속성을 기반으로 Braze Segments를 구축할 수 있습니다.

## API 키 권한 {#api-key-permissions}

사용하는 대상 서비스에 따라 Braze REST API 키에 다음 권한을 부여하세요:

| 권한 | 필요한 경우 |
| --- | --- |
| `users.track` | 사용자 속성 동기화, 추적 이벤트 전송 및 대상 연결 유효성 검사 |
| `users.export.ids` | 대량 작업을 위한 사용자 ID 내보내기 |
| `users.alias.update` | 사용자 별칭 업데이트 |
| `subscription.status.set` | 구독 상태 동기화 |
| `users.delete` | 미러 동기화 모드 전용(다른 대상 서비스에서는 선택 사항) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API 키 권한" }

## 통합 {#integration}

### 1단계: DinMo에서 Braze 대상 구성하기 {#step-1-configure-the-braze-destination-in-dinmo}

1. DinMo에서 사이드 내비게이션의 **Destinations**로 이동합니다.
2. **Add a new destination** > **Connect a new platform** > **Braze**를 선택합니다.
3. 연결 양식에 다음 세부 정보를 입력합니다:
   * **Platform Name**: 예를 들어, `Braze – Your Company`
   * **REST API URL**: 인스턴스 REST 엔드포인트(예: `https://rest.eu-01.braze.com`)
   * **Dashboard URL**: 인스턴스 대시보드 URL(예: `https://dashboard.eu-01.braze.com`)
   * **API Key**: Braze에서 복사한 키
4. **Connect**를 선택하여 자격 증명을 검증합니다.

{% alert note %}
REST API URL과 대시보드 URL을 모두 지정해야 합니다. REST API URL 끝에 슬래시를 포함하지 마세요.
{% endalert %}

### 2단계: 연결 확인하기 {#step-2-verify-the-connection}

대상을 저장하면 DinMo가 테스트 호출(예: `users.track`)을 수행하여 API 키와 엔드포인트가 정상적으로 작동하는지 확인합니다.

검증에 실패하면 다음 사항을 확인하세요:

* REST API URL이 올바르고 끝에 슬래시가 없는지 확인합니다.
* API 키가 유효하고 필요한 권한이 있는지 확인합니다.
* Braze 워크스페이스에서 IP 허용 목록을 사용하는 경우, DinMo의 IP 주소가 포함되어 있는지 확인합니다.

## 지원되는 대상 서비스 {#supported-destination-services}

DinMo의 각 대상 서비스는 동일한 일반 워크플로를 따릅니다: Braze 대상을 생성하고, DinMo 모델 또는 Segment를 구축한 다음, 활성화를 생성하여 Braze로 데이터를 전송합니다. 단계별 활성화 안내는 [DinMo Braze 대상 서비스](https://docs.dinmo.io/integrations/destination-platforms/braze)를 참조하세요.

다음 대상 서비스를 사용할 수 있습니다:

| 대상 서비스 | 설명 |
| --- | --- |
| [사용자 속성 동기화](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-users-attributes) | Braze에서 고객 프로필 속성을 업데이트하고 선택적으로 새 사용자를 삽입합니다. |
| [트랙 이벤트 전송](https://docs.dinmo.io/integrations/destination-platforms/braze/send-track-events) | Braze로 커스텀 이벤트 및 구매 이벤트를 전송합니다. |
| [구독 상태 동기화](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-subscription-statuses) | DinMo Segment 멤버십을 기반으로 Braze 구독 그룹에서 사용자를 구독 또는 탈퇴 처리합니다. |
| [사용자 목록 내보내기](https://docs.dinmo.io/integrations/destination-platforms/braze/export-user-lists) | Segment 멤버십을 Braze 사용자 속성에 동기화하여 Braze 세분화에 활용합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="지원되는 대상 서비스" }

### 사용자 속성 동기화 {#synchronize-user-attributes}

이 대상 서비스를 사용하여 기존 Braze 고객 프로필의 속성을 업데이트하고, 선택적으로 새 사용자를 삽입할 수 있습니다.

활성화를 실행하면:

* 삽입 모드를 활성화한 경우, 모델의 새 사용자가 Braze에 생성됩니다(UPSERT 동작).
* 마지막 활성화 이후 변경된 속성 값이 Braze에서 업데이트됩니다.

삽입 모드를 활성화하지 않으면, DinMo는 Braze에 이미 존재하며 일치하는 외부 ID가 있는 사용자만 업데이트합니다.

활성화 설정 중에 DinMo 모델에서 사용자의 [외부 ID]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids) 또는 Braze ID에 해당하는 필드를 매핑합니다. 각 DinMo 필드를 Braze의 정확한 속성 이름에 매핑하세요. Braze에 해당 속성이 존재하지 않으면 DinMo가 자동으로 생성합니다.

사용자 속성 활성화에 사용할 수 있는 동기화 모드는 다음과 같습니다:

| 동기화 모드 | 설명 |
| --- | --- |
| UPDATE | Braze에 이미 존재하는 사용자의 변경된 레코드를 업데이트합니다. 레코드를 삽입하거나 삭제하지 않습니다. |
| UPSERT | 새 레코드를 삽입하고 변경된 레코드를 업데이트합니다. 레코드를 삭제하지 않습니다. |
| MIRROR | 소스를 미러링하기 위해 Braze에서 레코드를 삽입, 업데이트 및 삭제합니다. 삭제 작업을 위한 커넥터 지원이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 속성 동기화 모드" }

{% alert warning %}
미러 동기화 모드는 DinMo 소스에 더 이상 존재하지 않는 레코드를 Braze에서 영구적으로 삭제합니다. 데이터 웨어하우스가 단일 정보 소스이고 삭제가 의도적인 경우에만 미러 모드를 사용하세요. 프로덕션에서 미러 동기화를 실행하기 전에 삭제 규칙을 검증하세요.
{% endalert %}

### 트랙 이벤트 전송 {#send-track-events}

이 대상 서비스를 사용하여 DinMo 이벤트 모델 또는 Segment에서 Braze로 커스텀 이벤트 또는 구매 이벤트를 전송합니다. Braze는 각 유형에 대해 서로 다른 API를 사용하므로, DinMo는 커스텀 이벤트와 구매를 별도의 대상 서비스로 처리합니다.

모델의 각 레코드는 단일 이벤트 유형(예: `Purchase`)을 나타냅니다. DinMo는 각 활성화 실행 시 새 이벤트만 전송하며, 이전에 전송된 이벤트를 업데이트하지 않습니다.

활성화 설정 중:

1. Braze에 표시될 이벤트 이름을 정확히 지정합니다. 해당 이벤트가 존재하지 않으면 DinMo가 자동으로 생성합니다.
2. 필수 필드를 매핑합니다:
   * **이벤트 시간**: 이벤트가 발생한 타임스탬프
   * **외부 ID**: 이벤트와 연결된 사용자의 외부 ID
3. 선택적 이벤트 속성정보를 Braze 속성 이름에 매핑합니다.
4. 새 이벤트가 Braze로 전송되는 빈도에 대한 스케줄을 설정합니다.

### 구독 상태 동기화 {#synchronize-subscription-statuses}

이 대상 서비스를 사용하여 Braze 구독 그룹을 DinMo Segment 또는 모델과 정렬된 상태로 유지합니다.

이 서비스를 활성화하기 전에:

1. Braze에서 대상 구독 그룹(SMS 또는 이메일)을 생성합니다.
2. 해당 구독 그룹에 속해야 하는 사용자를 포함하는 DinMo 모델 또는 Segment를 구축합니다.

활성화 설정 중에 Braze의 정확한 구독 그룹 ID를 입력합니다. 여러 구독 그룹을 동기화하려면 그룹당 하나의 활성화를 생성하세요.

활성화가 실행되면:

* 사용자가 이미 Braze에 존재하는 경우, DinMo Segment에 진입한 사용자는 대상 구독 그룹에 구독 상태로 표시됩니다.
* DinMo Segment를 떠난 사용자는 구독 그룹에서 탈퇴 상태로 표시됩니다.

DinMo는 Segment에 한 번도 포함되지 않은 사용자를 수정하지 않으며, 이 대상 서비스에서 새 Braze 사용자를 생성하지 않습니다.

### 사용자 목록 내보내기 {#export-user-lists}

이 대상 서비스를 사용하여 DinMo Segment를 Braze 사용자 속성으로 나타냅니다. Braze 제한으로 인해 DinMo는 Braze 목록을 직접 생성하지 않습니다. 대신, Segment에 포함된 사용자의 사용자 속성을 `true`로 설정하고, Segment를 떠난 사용자의 속성을 `false`로 설정합니다.

활성화 설정 중에 오디언스 이름을 지정합니다. DinMo는 이 이름을 Braze 속성으로 사용합니다(공백은 밑줄로 대체됩니다). 동일한 이름의 속성이 Braze에 이미 존재하지 않는지 확인하세요. 사용자의 외부 ID에 해당하는 DinMo 필드를 매핑합니다.

활성화가 실행된 후, 동기화된 속성이 `true`인 사용자를 필터링하는 Braze Segment를 생성합니다.

기존 Braze 사용자와 일치하는 외부 ID가 있는 사용자만 업데이트됩니다. 이 대상 서비스는 새 사용자를 생성하지 않습니다.