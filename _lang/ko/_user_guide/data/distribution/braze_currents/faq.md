---
nav_title: FAQ
article_title: 커런츠 FAQ
page_order: 4
page_type: reference
description: "이 문서에서는 Braze 커런츠를 설정할 때 가장 자주 발생하는 질문에 대해 다룹니다."
tool: Currents
---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 페이지에서는 Currents에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

### 특정 날짜 범위의 Campaign 또는 Canvas 데이터를 내보낼 수 있나요? {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

Campaign 또는 Canvas 측정기준을 특정 날짜 범위로 가져오려면 다음 방법 중 하나를 사용하세요:

- 표준 API 기간 외에 대시보드 스타일의 보고가 필요한 경우 날짜 기반 내보내기를 위한 [제품 요청](https://portal.braze.com/)을 제출하세요.
- `ending_at` 및 `length` 파라미터를 사용하여 [Campaign 분석]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) 또는 [Canvas 분석]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) 엔드포인트를 호출하거나, 시계열 데이터를 위해 [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) 및 [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)를 사용하세요.
- Amazon S3, Azure Blob Storage 또는 기타 지원되는 대상에서 지속적으로 쿼리 가능한 메시지 참여 데이터가 필요한 경우 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)를 사용하여 이벤트를 데이터 웨어하우스로 스트리밍하세요.

### 활성 상태의 커런츠 통합을 어떻게 편집하나요? {#how-do-i-edit-a-live-currents-integration}

활성 상태의 Currents 커넥터를 변경하려면 통합을 열고 페이지 왼쪽 하단의 **편집**을 클릭하세요. **편집**이 없으면 통합 UI는 읽기 전용 상태로 유지되며, 아이콘만으로는 커넥터 설정을 수정할 수 없습니다.

### Braze는 업로드 후 Azure Blob Storage Avro 파일을 어떻게 처리하나요? {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

Braze는 업로드가 완료된 후 [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)의 Avro 파일을 수정하지 않습니다. Azure는 업로드가 아직 진행 중인 동안 blob 삭제를 차단할 수 있습니다.

### 과거 데이터는 어떻게 얻나요? {#how-do-i-get-historical-data}

Currents는 실시간 라이브 데이터 스트림이므로 이벤트를 다시 재생할 수 없습니다. 하지만 [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) 또는 [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)와 같은 데이터 웨어하우스에 Currents 데이터를 저장할 수 있으므로 과거 이벤트에 대해 적절하게 조치를 취할 수 있습니다. 데이터는 30일 동안 보관되지만, 더 많은 과거 데이터가 필요하면 [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake/)를 쿼리할 수 있습니다.

### Currents가 JSON이 아닌 Avro 형식으로 데이터를 출력하는 이유는 무엇인가요? {#why-does-currents-output-data-in-the-avro-format-not-json}

Avro는 스키마가 없는 JSON과 달리 스키마 진화를 기본적으로 지원합니다. 또한 Avro는 압축률이 높기 때문에 대역폭을 줄이고 저장 공간을 절약하면서 Avro 파일을 전송할 수 있는 이점을 누릴 수 있습니다.

### Braze는 파일 오버헤드를 어떻게 처리하나요? {#how-does-braze-handle-file-overhead}

한 데이터베이스에서 대량의 데이터를 가져와 다른 데이터베이스에 저장할 수 있는 추출, 변환, 로드(ETL) 프로세스를 구축합니다.

### 쿼리를 위해 이 데이터를 어디에 저장해야 하나요? {#where-should-i-store-this-data-for-querying}

Braze는 쿼리를 위해 데이터를 저장할 수 있는 여러 데이터 웨어하우스와 제휴하고 있습니다. 다음을 사용하는 것을 권장합니다:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

### Currents 데이터는 얼마나 신뢰할 수 있나요? {#how-reliable-is-currents-data}

Currents는 "최소 1회" 전달을 보장하므로, 중복 이벤트가 간혹 스토리지 버킷에 기록될 수 있습니다. 사용 사례에서 정확히 1회 전달이 필요한 경우, 모든 이벤트와 함께 전송되는 고유 식별자 필드(`id`)를 사용하여 이벤트를 중복 제거할 수 있습니다. 자세한 내용은 [이벤트 전달 시맨틱]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/)을 참조하세요.

### 데이터는 얼마나 자주 Currents에 동기화되나요? {#how-often-is-data-synced-to-currents}

데이터는 지속적으로 스트리밍됩니다. Braze는 전송할 전체 배치가 준비되거나 5분이 경과할 때마다(둘 중 먼저 도래하는 시점에) 이벤트 배치를 전송합니다. 대용량 커넥터의 경우 데이터가 거의 실시간으로 도착합니다. 소량 커넥터의 경우 데이터가 5~30분 내에 도착할 것으로 예상됩니다. 자세한 내용은 [Avro 쓰기 임계값]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/#avro-write-threshold)을 참조하세요.

{% alert note %}
기기가 인터넷에 연결되어 있지 않으면 이벤트 생성이 지연될 수 있습니다. 인앱 메시지는 오프라인에서도 트리거될 수 있으므로, 인앱 메시지 이벤트에서 이러한 현상이 가장 흔하게 발생합니다.
{% endalert %}

### Currents에서 사용 가능한 이벤트를 어떻게 확인하나요? {#how-do-i-find-which-events-are-available-for-currents}

Currents가 기록하는 이벤트의 전체 목록은 [고객 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) 및 [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) 용어집을 참조하세요. 이벤트 유형(예: 발송, 전달, 열기)별로 이 용어집을 필터링할 수 있습니다.

### Currents 이메일 열기 또는 클릭 이벤트의 `external_id`가 Braze 대시보드의 고객 프로필과 다른 이유는 무엇인가요? {#why-does-the-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **Braze 대시보드에서:** 이메일 주소와 연결된 사용자가 이메일을 열거나 클릭하면, 해당 이메일 주소를 공유하는 모든 고객 프로필이 이메일을 열었거나 클릭한 것으로 표시됩니다. 자세한 내용은 [이메일이 발송될 때 여러 프로필이 동일한 이메일 주소를 가지고 있으면 어떻게 되나요?]({{site.baseurl}}/user_guide/channels/email/faq/#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)를 참조하세요.
- **Currents에서:** 동일한 열기 또는 클릭은 하나의 프로필에 저장됩니다. Braze는 해당 프로필이 여전히 이메일 주소를 공유하고 있는 경우 원래 발송 대상이었던 프로필에 귀속시킵니다. 그렇지 않으면 이메일 주소를 공유하는 프로필 중 무작위로 선택된 하나의 프로필에 귀속시킵니다.

이러한 이유로, Currents 이메일 열기 또는 클릭 이벤트의 `external_id`는 Currents와 Braze 대시보드를 비교할 때 예상하는 고객 프로필과 일치하지 않을 수 있습니다.

### 모든 발송 이벤트가 Currents에 기록되나요? {#are-all-send-events-logged-to-currents}

모든 이벤트가 Currents에 기록됩니다. 이벤트가 Currents 스트림에서 의도적으로 제외되는 시나리오는 없습니다.

### Currents에서 데이터가 손상될 수 있나요? {#can-data-be-corrupted-in-currents}

정상적인 상황에서 Currents 데이터는 손상되지 않습니다. 드문 문제가 발생할 가능성은 항상 있지만, 데이터가 체계적으로 손상되는 알려진 조건은 없습니다.

### 커런츠 통합을 설정하기 전 날짜의 커스텀 이벤트 데이터가 보이는 이유는 무엇인가요? {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

Braze는 Currents에 이벤트를 소급 적용하지 않습니다. 하지만 커스텀 이벤트는 과거 타임스탬프로 기록될 수 있습니다(예: 이벤트 발생 시 기기가 오프라인이었고 나중에 동기화된 경우). 이러한 경우 이벤트 타임스탬프는 이벤트가 원래 발생한 시점을 반영하며, 이는 커런츠 통합이 구성되기 전일 수 있습니다.

### Currents 발송 이벤트에 커스텀 속성을 포함할 수 있나요? {#can-i-include-custom-attributes-in-currents-send-events}

아니요. Currents는 발송 이벤트에 커스텀 속성을 포함하지 않습니다. Currents는 커스텀 이벤트와 메시지 참여 이벤트를 기록합니다. 사용 가능한 필드의 전체 목록은 [이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/)을 참조하세요.

### Currents에 Campaign 태그나 키-값 페어가 포함되나요? {#does-currents-include-campaign-tags-or-key-value-pairs}

아니요. Currents에는 Campaign 태그나 메시지 수준의 키-값 페어가 포함되지 않습니다. 대안으로, Campaign에서 웹훅 채널을 사용하여 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)로 태그 및 키-값 페어 데이터를 템플릿화하여 자체 엔드포인트로 이 정보를 전송할 수 있습니다.

### Braze는 Currents 변경 사항을 고객에게 어떻게 알리나요? {#how-does-braze-notify-customers-of-changes-to-currents}

Currents 변경 사항(예: 새 이벤트 필드 또는 이벤트 유형)이 발생하면, Braze는 활성 커런츠 통합을 보유하고 있으며 지난 30일 이내에 대시보드를 사용한 모든 고객에게 이메일을 발송합니다. 최신 변경 사항은 [커런츠 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/)에서도 확인할 수 있습니다.

### Currents 데이터에 얼마나 많은 스토리지가 필요한가요? {#how-much-storage-do-i-need-for-currents-data}

스토리지 요구 사항은 이벤트 볼륨과 내보내는 이벤트 유형에 따라 달라집니다. Braze는 사용 사례에 맞는 파일 크기를 추정하는 데 사용할 수 있는 [Avro 형식의 샘플 이벤트](https://github.com/appboy/currents-examples/tree/master/sample-data)를 제공합니다.

### Currents 데이터에서 Campaign 이름이나 캔버스 단계 이름이 `NULL`인 이유는 무엇인가요? {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

새 Campaign이나 Canvas를 생성하면 이름이 모든 Braze 시스템에 전파되는 데 시간이 걸릴 수 있습니다. 이 기간 동안 Currents를 통해 전송된 이벤트의 이름 필드(예: `campaign_name` 또는 `canvas_step_name`)에 `NULL`이 표시될 수 있습니다. 이벤트가 기록되기 직전에 이름이 수정된 경우에도 이러한 현상이 예상됩니다. 이를 방지하려면 Campaign이나 캔버스 단계를 생성하거나 이름을 변경한 후 발송하기 전에 어느 정도 시간을 두세요.

### Currents에서 세션 종료 이벤트가 지연되거나 누락되는 이유는 무엇인가요? {#why-are-session-end-events-delayed-or-missing-in-currents}

세션 종료 이벤트는 SDK의 일반적인 업로드 스케줄을 따릅니다. Braze SDK는 세션 데이터를 로컬에 캐시하고 네트워크 품질에 따라 주기적으로 플러시합니다. 예를 들어, 양호한 연결에서는 약 10초마다 플러시합니다. SDK가 이벤트를 업로드하기 전까지는 Currents에 표시되지 않습니다.

사용자가 앱을 강제 종료하거나 다음 플러시 전에 오프라인 상태가 되면, 세션 종료 이벤트가 늦게 도착하거나 전혀 도착하지 않을 수 있습니다. iOS에서는 SDK가 앱이 백그라운드에 있는 동안 데이터를 전송할 수 없기 때문에 세션 종료 이벤트가 앱이 다시 열릴 때까지 플러시되지 않는 경우가 많습니다.

Currents에서 더 적시에 세션 경계가 필요한 경우, 앱이 백그라운드로 이동하거나 포그라운드로 돌아올 때와 같은 라이프사이클 시점에서 `requestImmediateDataFlush()`를 호출하세요. 자세한 내용은 [데이터 업로드 및 다운로드]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/#data-upload-and-download) 및 [세션 종료와 세션 시작의 타임스탬프가 유사한 경우(iOS)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log/#session-end-and-session-start-have-similar-timestamps-ios)를 참조하세요.

### Currents가 데이터를 쓰려고 할 때 스토리지 버킷을 사용할 수 없으면 어떻게 되나요? {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

데이터 전송 시점에 스토리지 버킷을 사용할 수 없으면 해당 데이터는 손실됩니다. Braze는 성공적으로 전달되지 않은 이벤트를 소급 적용할 수 없습니다. 데이터 손실을 방지하려면 스토리지 버킷이 항상 사용 가능하고 올바르게 구성되어 있는지 확인하세요.

### Currents 통합을 편집할 때 "고객 행동 이벤트 자격이 남아 있지 않습니다"라는 메시지가 표시되는 이유는 무엇인가요? {#why-do-i-see-you-do-not-have-any-remaining-customer-behavior-events-entitlements-when-editing-my-currents-integration}

이 메시지는 기존 커런츠 통합을 업데이트할 때 워크스페이스가 고객 행동 이벤트에 대한 자격 한도에 도달한 경우 나타날 수 있습니다. 자격을 요청하거나 구성을 조정하려면 Braze 계정 매니저에게 문의하세요.

### 스토리지 경로의 Currents 버전은 얼마나 자주 변경되나요? {#how-often-does-the-currents-version-in-the-storage-path-change}

스토리지 경로의 `version=<currents_version>` 세그먼트는 월별 주기로 각 Currents 릴리스마다 증가합니다(예: `version=6`에서 `version=7`으로). 버전 변경 후에도 파이프라인이 자동으로 데이터를 가져올 수 있도록, 특정 버전 세그먼트를 하드코딩하는 대신 루트 경로에서 파일을 재귀적으로 읽는 것을 권장합니다. 경로 형식에 대한 자세한 내용은 [이벤트 전달 시맨틱]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/)을 참조하세요. 버전별 변경 이력은 [커런츠 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/)를 참조하세요.

### 메시지 참여 이벤트에서 `campaign_id` 또는 `canvas_id`가 누락되는 이유는 무엇인가요? {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

이벤트 유형과 컨텍스트에 따라 메시지 참여 이벤트가 특정 Campaign이나 캔버스 단계에 연결되지 않을 수 있습니다. 이러한 경우 `campaign_id`, `canvas_id` 및 관련 이름 필드가 이벤트 페이로드에서 생략될 수 있습니다. 해당 필드가 특정 이벤트에 표시되지 않는 경우, 해당 이벤트 유형과 컨텍스트에서 일반적으로 Campaign 또는 Canvas 식별자가 포함되는지 확인하세요.