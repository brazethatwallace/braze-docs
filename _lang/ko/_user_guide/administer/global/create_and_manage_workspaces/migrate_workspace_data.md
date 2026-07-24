---
nav_title: 워크스페이스 간 데이터 마이그레이션
article_title: 워크스페이스 및 인스턴스 간 데이터 마이그레이션
page_order: 1
page_type: reference
description: "워크스페이스 데이터가 어떻게 격리되는지, Braze가 워크스페이스 간에 복사하거나 가져올 수 있는 항목, 스테이징, 프로덕션 또는 별도의 대시보드 환경 간 이동을 계획하는 방법을 알아보세요."
---

# 워크스페이스 및 인스턴스 간 데이터 마이그레이션 {#migrate-data-between-workspaces-and-instances}

> 워크스페이스는 Braze 데이터를 분리합니다. 이 페이지에서는 이러한 격리가 마이그레이션에 미치는 영향, 제품 기능과 API를 통해 이동할 수 있는 항목, 그리고 Braze 외부에서 다시 구축하거나 처리해야 하는 항목을 설명합니다. 마이그레이션은 일반적으로 회사 관리자만의 작업이 아닌 여러 부서가 함께하는 작업입니다. 관리자는 워크스페이스 설정과 채널 구성을 담당하고, 개발자는 SDK 및 API 변경을 처리하며, 마케터는 Segments를 다시 구축하고 메시징 콘텐츠를 복사합니다. 각 단계에는 소스 및 대상 워크스페이스에서 관련 [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 필요합니다.

Braze에 저장하는 모든 것(고객 프로필, Segments, 메시징 콘텐츠, 인게이지먼트 기록)은 워크스페이스 내에 존재합니다. Segment, Campaign 또는 Canvas는 다른 워크스페이스의 데이터를 읽거나 타겟팅할 수 없습니다. 대시보드 사용자는 스테이징과 프로덕션, 다른 브랜드 또는 지역 분할을 위해 동일한 회사 대시보드에서 여러 워크스페이스를 사용하는 경우가 많습니다. 이러한 설정은 격리를 제공하지만, 대시보드에서 모든 워크스페이스 데이터를 다른 워크스페이스나 다른 Braze 인스턴스로 이동하는 단일 작업은 없다는 것을 의미합니다.

계획 관련 맥락은 [시작하기: 워크스페이스]({{site.baseurl}}/user_guide/get_started/workspaces) 및 [워크스페이스 생성 및 관리]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces)를 참조하세요.

## Braze가 워크스페이스 간에 자동으로 마이그레이션하지 않는 항목 {#what-braze-does-not-automatically-migrate-between-workspaces}

SDK 또는 API를 새 워크스페이스(또는 자체 워크스페이스가 있는 새 Braze 대시보드 환경)로 연결할 때 다음 항목은 일괄 마이그레이션되지 않습니다.

| 영역 | 동작 |
| --- | --- |
| **고객 프로필** | 프로필은 패키지 단위로 전송되지 않습니다. 대상 워크스페이스에서 사용자를 다시 생성하거나 가져오세요([고객 프로필 데이터](#user-profile-data) 참조). |
| **Segments 및 필터** | Segment 정의는 소스 워크스페이스에 유지됩니다. 가능한 경우 동일한 로직을 사용하여 대상 워크스페이스에서 Segments를 다시 구축하세요. |
| **메시징 기록** | 프로필의 Campaign 및 Canvas 수신 기록은 소스 워크스페이스에 연결되어 있습니다. [Braze 온보딩 FAQ]({{site.baseurl}}/onboarding_faq)에 설명된 대로 직접 모델링하지 않는 한(예: 커스텀 속성을 통해) 다른 워크스페이스의 새 프로필에는 표시되지 않습니다. |
| **채널별 구성** | 발송 도메인, SMS 구독, WhatsApp 번호 및 유사한 설정은 워크스페이스 범위입니다. 해당하는 경우 대상 워크스페이스에서 다시 구성하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze가 워크스페이스 간에 자동으로 마이그레이션하지 않는 항목" }

{% alert important %}
스테이징과 프로덕션에 별도의 워크스페이스를 사용하는 경우, [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 커넥터는 워크스페이스 간에 공유되지 않는다는 점을 기억하세요. 어떤 워크스페이스가 프로덕션 내보내기를 소유할지 계획하세요. 자세한 내용은 [시작하기: 워크스페이스]({{site.baseurl}}/user_guide/get_started/workspaces#currents-connectors)를 참조하세요.
{% endalert %}

## 이동하거나 다시 생성할 수 있는 항목 {#what-you-can-move-or-recreate}

### Campaign, Canvas 및 랜딩 페이지 콘텐츠 {#campaign-canvas-and-landing-page-content}

많은 Campaign, Canvas 및 랜딩 페이지 정의를 다른 워크스페이스에 초안으로 복사할 수 있습니다. 지원되는 채널, 생략된 필드 및 Liquid 관련 주의사항은 [워크스페이스 간 Campaigns, Canvases 및 랜딩 페이지 복사]({{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces)에 문서화되어 있습니다. 복사 후 시작하거나 게시하기 전에 Segments, 트리거 및 워크스페이스별 참조를 업데이트하세요.

### 고객 프로필 데이터 {#user-profile-data}

일반적인 접근 방식:

- **REST API:** [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)을 사용하여 필요한 식별자와 속성으로 대상 워크스페이스에서 사용자를 생성하거나 업데이트합니다. 이는 과거 데이터를 Braze로 가져올 때 설명된 [레거시 사용자 데이터 마이그레이션]({{site.baseurl}}/developer_guide/getting_started/integration_overview#migrating-legacy-user-data)과 동일한 패턴입니다.
- **CSV 가져오기:** 마케터 주도의 가져오기는 [사용자 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) 및 [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)를 참조하세요.
- **클라우드 데이터 수집:** 웨어하우스에서 대상 워크스페이스로 속성을 동기화하려면 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 참조하세요.
- **소스 워크스페이스에서 내보내기:** [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) 또는 [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)를 사용하여 이동이 허용된 데이터를 추출한 다음, 대상에 맞게 `users/track` 또는 CSV로 매핑합니다. 데이터를 내보내고 다시 로드할 때 데이터 보존, 개인정보 보호 및 계약상 의무를 준수하세요.

{% alert note %}
[사용자 병합]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) 엔드포인트 또는 대시보드의 [중복 사용자]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)를 사용한 중복 프로필 병합은 단일 워크스페이스 내에서 적용되며, 두 워크스페이스 간에는 적용되지 않습니다.
{% endalert %}

### 표준 프로필 API에 매핑되지 않는 사용자 내보내기 필드 {#user-export-fields-that-dont-map-to-standard-profile-apis}

[사용자 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)에서 대상 워크스페이스의 사용자를 다시 구축할 때, 일부 내보내기 필드는 REST API 또는 CSV를 통해 Braze 표준 프로필 필드에 다시 기록할 수 없습니다(SDK와 서버가 채우는 방식). 대신 커스텀 속성으로 값을 유지할 수 있는 경우가 많습니다. 다음 제한 사항에 유의하세요.

#### 기기 정보(`devices`) {#device-information-devices}

내보내기의 기기 레코드는 SDK에 의해 채워집니다. REST API를 통해 해당 데이터를 Braze의 표준 기기 필드로 마이그레이션할 수 없습니다.

사용자가 대상 워크스페이스를 타겟팅하는 앱에서 세션을 시작하기 전에 해당 정보가 필요한 경우, 사용자를 가져올 때 커스텀 속성으로 전송하세요. 내장 기기 데이터에 의존하는 표준 세분화 필터 및 Liquid 참조는 사용자가 새 워크스페이스에 연결된 앱 인스턴스에서 세션을 열 때까지(SDK가 표준 기기 필드를 새로고침할 때) 내보낸 기기 페이로드를 사용하지 않습니다.

{% alert note %}
이것은 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)의 `push_tokens` 필드를 사용하는 [푸시 토큰 마이그레이션](#push-tokens)과는 별개입니다.
{% endalert %}

#### 총 세션 수 및 앱별 세션 데이터(`apps` 및 중첩된 `sessions`) {#total-sessions-and-per-app-session-data-apps-and-nested-sessions}

내보내기의 `apps` 오브젝트에서 가져온 세션 합계 및 중첩된 세션 데이터는 동일한 내장 필드로 다시 가져올 수 없습니다. 레거시 카운트(예: 소스 워크스페이스의 총 세션 수)를 보존하려면 커스텀 속성에 저장하고 대상 워크스페이스에서 해당 필드를 기준으로 세분화하세요.

[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 또는 CSV 가져오기를 통해 `date_of_first_session` 및 `date_of_last_session`을 설정할 수 있습니다. 허용되는 형식은 [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) 및 [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)를 참조하세요.

#### 무작위 버킷(`random_bucket`) {#random-bucket-random_bucket}

각 사용자에게는 워크스페이스에서 [무작위 버킷 번호]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-update-events)가 할당됩니다. 이 값은 다시 가져올 수 없으며, 사용자는 대상 워크스페이스에서 새로운 무작위 버킷을 받게 됩니다.

홀드아웃이나 샘플링을 위해 이전 번호에 의존하는 경우(예: `random_bucket`이 임계값 미만인 사용자 제외), 내보낸 값을 커스텀 속성으로 저장하고 내장 무작위 버킷 필드 대신 해당 속성을 기준으로 Segments 또는 필터를 구축하세요.

#### 파트너 기여도 필드(`attributed_*`) {#partner-attribution-fields-attributed_}

파트너 통합의 기여도 필드(내보내기의 `attributed_*` 필드)는 REST API를 통해 Braze 표준 기여도 필드에 설정할 수 없습니다. 세분화 또는 메시징을 위해 유지해야 하는 경우 대상 워크스페이스에서 커스텀 속성에 매핑하세요.

### 푸시 토큰 {#push-tokens}

사용자가 이전 공급자 또는 앱 버전의 푸시 토큰을 이미 가지고 있는 경우, API를 통해 모바일 앱의 토큰을 가져오거나 통합 후 SDK에 의존할 수 있습니다. 웹 푸시 토큰에는 API 제한이 있습니다. 전체 세부 정보 및 예시는 [푸시 토큰 마이그레이션]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)을 참조하세요.

### WhatsApp

전화번호와 구독 그룹은 특정 전송 흐름을 통해 워크스페이스 간에 이동할 수 있습니다. [워크스페이스 간 WhatsApp 전화번호 및 구독 그룹 전송]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/transfer_between_workspaces)을 참조하세요.

### Braze 외부의 인게이지먼트 및 분석 데이터 {#engagement-and-analytics-data-outside-braze}

환경을 통합할 때 발송, 열람 또는 클릭의 과거 기록이 필요한 경우, [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 및 기타 내보내기가 해당 데이터를 웨어하우스나 도구에 저장하는 지원되는 방법입니다. 해당 데이터는 다른 워크스페이스의 기본 사용자별 메시지 기록으로 Braze에 다시 수집되지 않습니다.

## SDK 또는 API 키를 변경하기 전에 {#before-you-change-sdk-or-api-keys}

앱이나 사이트를 새 워크스페이스로 연결한 경우:

- 앱이나 사이트를 여는 사용자는 새 워크스페이스에 새 프로필을 생성할 수 있습니다. 이전 워크스페이스별 기록은 자동으로 이전되지 않습니다.
- 동일한 사람이 두 워크스페이스에 모두 존재할 수 있는 경우, [중복과 유사한 시나리오]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces#should-i-create-a-new-workspace-when-im-releasing-an-updated-app)가 발생할 수 있습니다(예: 푸시 도달 범위 중복). 프로덕션과 스테이징 키를 의도치 않게 공유하는 것보다 신중한 데이터 및 타겟팅 계획을 수립하세요.

{% alert tip %}
워크스페이스 또는 앱 인스턴스 삭제 제한, 특수 계정 이동 또는 대규모 마이그레이션 계획에 대해서는 대시보드 링크와 소스 및 대상 워크스페이스 요약을 포함하여 [Braze 고객지원에 문의]({{site.baseurl}}/user_guide/administer/personal/braze_support)하세요.
{% endalert %}