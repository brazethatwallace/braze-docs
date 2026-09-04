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

## 특정 날짜 범위의 Campaign 또는 Canvas 데이터를 내보낼 수 있나요? {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

정의된 날짜 범위의 Campaign 또는 Canvas 측정기준을 가져오려면 다음 방법 중 하나를 사용하세요:

- {% multi_lang_include product_feedback_cta.md context="gap" feature="date-aligned campaign or Canvas exports for dashboard-style reporting outside standard API windows" %}
- `ending_at` 및 `length` 매개변수를 사용하여 [Campaign 분석]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) 또는 [Canvas 분석]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) 엔드포인트를 호출하거나, 시계열 데이터를 위해 [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) 및 [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics)를 사용하세요.
- Amazon S3, Azure Blob Storage 또는 기타 지원되는 대상에서 지속적이고 쿼리 가능한 메시지 인게이지먼트 데이터가 필요한 경우, [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)를 사용하여 이벤트를 데이터 웨어하우스로 스트리밍하세요.

## 활성 상태인 Currents 통합을 어떻게 편집하나요? {#how-do-i-edit-a-live-currents-integration}

활성 상태인 Currents 커넥터를 변경하려면 통합을 열고 **편집**을 선택합니다. **편집**이 없으면 통합 UI는 읽기 전용 상태로 유지되며, 아이콘만으로는 커넥터 설정을 수정할 수 없습니다.

## Braze는 업로드 후 Azure Blob Storage Avro 파일을 어떻게 처리하나요? {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

Braze는 업로드가 완료된 후 [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)의 Avro 파일을 수정하지 않습니다. Azure는 업로드가 아직 진행 중인 동안 blob 삭제를 차단할 수 있습니다.

## 과거 데이터를 가져오려면 어떻게 해야 하나요? {#how-do-i-get-historical-data}

Currents는 실시간 라이브 데이터 스트림이므로 이벤트를 다시 재생할 수 없습니다. 하지만 [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) 또는 [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)와 같은 데이터 웨어하우스에 Currents 데이터를 저장할 수 있으므로, 필요에 따라 과거 이벤트에 대해 조치를 취할 수 있습니다. 데이터는 30일 동안 보존되지만, 더 오래된 과거 데이터가 필요한 경우 [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake)에서 쿼리할 수 있습니다.

## Currents가 JSON이 아닌 Avro 형식으로 데이터를 출력하는 이유는 무엇인가요? {#why-does-currents-output-data-in-the-avro-format-not-json}

스키마가 없는 JSON과 달리, Avro는 기본적으로 스키마 진화를 지원합니다. 또한 Avro는 높은 압축률을 제공하므로, 더 적은 대역폭으로 Avro 파일을 전송하고 저장 공간을 절약할 수 있습니다.

## Braze는 파일 오버헤드를 어떻게 처리하나요? {#how-does-braze-handle-file-overhead}

Braze는 ETL(Extract, Transform, Load) 프로세스를 구축하여 하나의 데이터베이스에서 대량의 데이터를 추출한 후 다른 데이터베이스에 저장할 수 있도록 합니다.

## 쿼리를 위해 이 데이터를 어디에 저장해야 하나요? {#where-should-i-store-this-data-for-querying}

Braze는 쿼리를 위해 데이터를 저장할 수 있는 여러 데이터 웨어하우스와 파트너십을 맺고 있습니다. 다음을 사용하는 것을 권장합니다:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents).

## Currents 데이터는 얼마나 신뢰할 수 있나요? {#how-reliable-is-currents-data}

Currents는 "최소 한 번" 전달을 보장하므로, 스토리지 버킷에 중복 이벤트가 간헐적으로 기록될 수 있습니다. 사용 사례에서 정확히 한 번만 전달해야 하는 경우, 모든 이벤트와 함께 전송되는 고유 식별자 필드(`id`)를 사용하여 이벤트 중복을 제거할 수 있습니다. 자세한 내용은 [이벤트 전달 의미론]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics)을 참조하세요.

## 데이터는 Currents에 얼마나 자주 동기화되나요? {#how-often-is-data-synced-to-currents}

데이터는 지속적으로 스트리밍됩니다. Braze는 전송할 전체 배치가 준비되거나 5분이 경과할 때 중 먼저 도래하는 시점에 이벤트 배치를 전송합니다. 대용량 커넥터의 경우 데이터가 거의 실시간으로 도착합니다. 소용량 커넥터의 경우 데이터가 5~30분 이내에 도착할 수 있습니다. 자세한 내용은 [Avro 쓰기 임계값]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics#avro-write-threshold)을 참조하세요.

{% alert note %}
기기가 인터넷에 연결되어 있지 않으면 이벤트 생성이 지연될 수 있습니다. 인앱 메시지는 오프라인에서도 트리거될 수 있으므로, 인앱 메시지 이벤트에서 이러한 지연이 가장 흔하게 발생합니다.
{% endalert %}

## Currents에서 사용할 수 있는 이벤트는 어떻게 찾나요? {#how-do-i-find-which-events-are-available-for-currents}

Currents가 기록하는 이벤트의 전체 목록은 [고객 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) 및 [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 용어집을 참조하세요. 이벤트 유형(예: 발송, 전달, 열람)별로 이 용어집을 필터링할 수 있습니다.

## Currents 이벤트 수가 대시보드 또는 참여 보고서 측정기준과 일치하지 않는 이유는 무엇인가요? {#why-do-my-currents-event-counts-not-match-my-dashboard-or-engagement-report-metrics}

Currents와 Braze 대시보드는 특정 측정기준을 다르게 계산하므로, Currents 이벤트와 대시보드 측정기준이 정확히 일치하지 않을 수 있습니다.

**고유 클릭:** 이메일의 경우, 대시보드는 7일 기간 동안의 고유 클릭을 추적하며 `dispatch_id`를 기준으로 측정합니다. Currents는 각 원시 클릭 이벤트를 기록합니다. Currents 기반의 고유 클릭 수를 대시보드 측정기준과 맞추려면 `is_unique`가 `true`인 이벤트만 필터링하세요.

**구독 취소:** 대시보드의 *구독 취소* 측정기준은 Braze의 표준 구독 취소 링크 클릭을 반영합니다. 커스텀 구독 취소 페이지는 API를 통해 사용자를 업데이트하지 않는 한 이 측정기준에 반영되지 않습니다. Currents의 `users.messages.email.Unsubscribe` 이벤트는 사용자가 이메일 본문이나 푸터에 있는 구독 취소 링크를 클릭하거나 list-unsubscribe 헤더를 통해 구독 취소할 때 발생하는 특수 클릭 이벤트입니다. 이 이벤트가 모든 이메일 구독 상태 변경을 나타내는 것은 아닙니다.

**타임스탬프 및 시간대:** 모든 Currents 타임스탬프는 UTC 기준입니다. 대시보드 측정기준은 회사의 시간대를 따릅니다. Currents 데이터를 회사의 시간대로 변환하지 않고 달력 날짜 기준으로 집계하면, 대시보드에 표시되는 것과 다른 날짜 버킷에 수치가 집계될 수 있습니다.

**중복 이벤트:** Currents는 최소 1회 전달(at-least-once delivery)을 제공하므로, 간혹 중복 이벤트가 기록될 수 있습니다. 대시보드 측정기준과 총계를 비교하기 전에 각 이벤트의 고유 `id` 필드를 기준으로 중복을 제거하세요.

## Currents 이메일 열람 또는 클릭 이벤트의 `external_user_id`(Braze 스키마: `external_id`)가 Braze 대시보드의 사용자 프로필과 다른 이유는 무엇인가요? {#why-does-the-external_user_id-braze-schema-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **Braze 대시보드에서:** 이메일 주소와 연결된 사용자가 이메일을 열람하거나 클릭하면, 해당 이메일 주소를 공유하는 모든 사용자 프로필이 해당 이메일을 열람하거나 클릭한 것으로 표시됩니다. 자세한 내용은 [이메일이 발송될 때 여러 프로필이 동일한 이메일 주소를 가지고 있으면 어떻게 되나요?]({{site.baseurl}}/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)를 참조하세요.
- **Currents에서:** 동일한 열람 또는 클릭이 하나의 프로필에 저장됩니다. Braze는 해당 프로필이 여전히 해당 이메일 주소를 공유하고 있는 경우, 원래 발송 대상으로 지정된 프로필에 귀속시킵니다. 그렇지 않은 경우, Braze는 해당 이메일 주소를 공유하는 프로필 중 무작위로 선택한 하나의 프로필에 귀속시킵니다.

이러한 이유로, Currents 이메일 열람 또는 클릭 이벤트의 `external_user_id` 값(Braze 스키마 매핑 테이블에서 `external_id`로 명명됨)은 Currents를 Braze 대시보드와 비교할 때 예상하는 사용자 프로필과 일치하지 않을 수 있습니다.

## 모든 발송 이벤트가 Currents에 기록되나요? {#are-all-send-events-logged-to-currents}

모든 이벤트는 Currents에 기록됩니다. 이벤트가 Currents 스트림에서 의도적으로 누락되는 시나리오는 없습니다.

## Currents에서 데이터가 손상될 수 있나요? {#can-data-be-corrupted-in-currents}

정상적인 상황에서 Currents 데이터는 손상되지 않습니다. 드문 문제가 발생할 가능성은 항상 있지만, 데이터가 체계적으로 손상되는 알려진 조건은 없습니다.

## Currents 통합이 설정되기 전 날짜의 커스텀 이벤트 데이터가 표시되는 이유는 무엇인가요? {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

Braze는 Currents에 이벤트를 소급하여 채우지 않습니다. 그러나 커스텀 이벤트는 과거 타임스탬프로 기록될 수 있습니다(예: 이벤트가 발생했을 때 기기가 오프라인 상태였다가 나중에 동기화된 경우). 이러한 경우 이벤트 타임스탬프는 이벤트가 원래 발생한 시점을 반영하므로, Currents 통합이 구성되기 전일 수 있습니다.

## Currents 이벤트에는 어떤 사용자 식별자가 포함되나요? {#what-user-identifiers-are-included-in-currents-events}

메시지 인게이지먼트 이벤트(발송, 열람, 클릭 등)에는 Braze 사용자 ID(`user_id`)와 프로필에 존재하는 경우 외부 식별자(이벤트 페이로드에서는 `external_user_id`, Braze 스키마 매핑 테이블에서는 `external_id`로 표시)가 포함됩니다. 일부 이메일 메시지 인게이지먼트 이벤트에는 `email_address`도 포함됩니다. 커스텀 속성은 포함되지 않습니다.

Currents 데이터를 데이터 웨어하우스 또는 CRM으로 라우팅하고 프로필 데이터와 조인해야 하는 경우, 다운스트림 시스템에서 `user_id` 또는 `external_user_id`를 사용하여 조인을 수행하세요.

## Currents 발송 이벤트에 커스텀 속성을 포함할 수 있나요? {#can-i-include-custom-attributes-in-currents-send-events}

아니요. Currents는 발송 이벤트에 커스텀 속성을 포함하지 않습니다. Currents는 커스텀 이벤트와 메시지 인게이지먼트 이벤트를 기록합니다. 사용 가능한 필드의 전체 목록은 [이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary)을 참조하세요.

## Currents에 Campaign 또는 Canvas 태그나 키-값 페어가 포함되나요? {#does-currents-include-campaign-or-canvas-tags-or-key-value-pairs}

아니요. Currents에는 Campaign 또는 Canvas 태그나 메시지 수준의 키-값 페어가 포함되지 않습니다. 태그 데이터를 가져오려면 [REST API 내보내기]({{site.baseurl}}/api/endpoints/export)를 사용하세요. 다른 대안으로, Campaign에서 웹훅 채널을 사용하여 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)로 값을 템플릿화한 뒤, 태그 또는 키-값 페어 데이터를 자체 엔드포인트로 전송할 수 있습니다.

## Braze는 Currents 변경 사항을 고객에게 어떻게 알리나요? {#how-does-braze-notify-customers-of-changes-to-currents}

드물지만 호환성을 깨는 변경이 발생하는 경우, Braze는 활성 통합의 담당자와 최근 30일 이내에 대시보드를 사용한 활성 Currents 통합을 보유한 모든 관리자에게 사전 이메일을 보냅니다. 새로운 이벤트나 기존 이벤트에 새 필드가 추가되는 것과 같은 비호환성 변경의 경우, Braze는 별도의 알림을 보내지 않습니다. 최신 변경 사항은 [Currents 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)를 참조하세요.

## Currents 데이터에 얼마나 많은 저장 공간이 필요한가요? {#how-much-storage-do-i-need-for-currents-data}

저장 공간 요구 사항은 이벤트 볼륨과 내보내는 이벤트 유형에 따라 다릅니다. Braze는 사용 사례에 맞는 파일 크기를 추정하는 데 사용할 수 있는 [Avro 형식의 샘플 이벤트](https://github.com/appboy/currents-examples/tree/master/sample-data)를 제공합니다.

## Currents 데이터에서 Campaign 이름이나 Canvas 단계 이름이 `NULL`인 이유는 무엇인가요? {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

새 Campaign 또는 Canvas를 생성하면 이름이 모든 Braze 시스템에 전파되기까지 다소 시간이 걸릴 수 있습니다. 이 시간 동안 Currents를 통해 전송된 이벤트의 이름 필드(예: `campaign_name` 또는 `canvas_step_name`)에 `NULL`이 표시될 수 있습니다. 이벤트가 기록되기 직전에 이름을 수정한 경우에도 이 현상이 발생할 수 있습니다. 이를 방지하려면 Campaign 또는 캔버스 단계를 생성하거나 이름을 변경한 후 발송하기 전에 잠시 시간을 두세요.

## Currents에서 세션 종료 이벤트가 지연되거나 누락되는 이유는 무엇인가요? {#why-are-session-end-events-delayed-or-missing-in-currents}

세션 종료 이벤트는 SDK의 일반적인 업로드 일정에 따릅니다. Braze SDK는 세션 데이터를 로컬에 캐시하고 네트워크 품질에 따라 주기적으로 플러시합니다. 예를 들어, 연결 상태가 좋을 때는 약 10초마다 플러시합니다. SDK가 이벤트를 업로드할 때까지 Currents에 표시되지 않습니다.

사용자가 다음 플러시 전에 앱을 강제 종료하거나 오프라인 상태가 되면, 세션 종료 이벤트가 늦게 도착하거나 아예 도착하지 않을 수 있습니다. iOS에서는 SDK가 앱이 백그라운드에 있는 동안 데이터를 전송할 수 없기 때문에, 앱이 다시 열릴 때까지 세션 종료 이벤트가 플러시되지 않는 경우가 많습니다.

Currents에서 보다 적시에 세션 경계를 확인해야 하는 경우, 앱이 백그라운드로 전환되거나 포그라운드로 복귀하는 등의 라이프사이클 시점에서 `requestImmediateDataFlush()`를 호출하세요. 자세한 내용은 [데이터 업로드 및 다운로드]({{site.baseurl}}/developer_guide/getting_started/sdk_overview#data-upload-and-download) 및 [세션 종료와 세션 시작의 타임스탬프가 유사한 경우(iOS)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log#session-end-and-session-start-have-similar-timestamps-ios)를 참조하세요.

## 커런츠가 데이터를 쓰려고 할 때 스토리지 버킷을 사용할 수 없으면 어떻게 되나요? {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

데이터 전송 시점에 스토리지 버킷을 사용할 수 없는 경우 해당 데이터는 손실됩니다. Braze는 성공적으로 전달되지 않은 이벤트를 다시 채울 수 없습니다. 데이터 손실을 방지하려면 스토리지 버킷이 항상 사용 가능하고 올바르게 구성되어 있는지 확인하세요.

## 커런츠 통합을 생성하거나 편집할 때 자격 제한 메시지가 표시되는 이유는 무엇인가요? {#why-do-i-see-entitlement-limit-messages-when-creating-or-editing-a-currents-integration}

Currents는 다양한 커넥터 기능에 대해 별도의 자격 풀을 사용합니다.

- **Engagement Events**: 표준 Currents 커넥터를 생성하거나 업그레이드하는 데 필요합니다.
- **Customer Behavior Events**: **Track Customer Behavior and User Events**를 활성화하는 데 필요합니다.
- **User Profiles and Attributes**: **Track user profiles and attributes**를 활성화하는 데 필요합니다.

풀이 소진되면 Braze에서 자격 경고를 표시하고 해당 작업을 차단합니다. 추가 자격을 요청하거나 구성 조정에 대한 도움이 필요하면 Braze 계정 매니저에게 문의하세요.

## 스토리지 경로의 Currents 버전은 얼마나 자주 변경되나요? {#how-often-does-the-currents-version-in-the-storage-path-change}

스토리지 경로의 `version=<currents_version>` 세그먼트는 월별 주기로 Currents 릴리스마다 증가합니다(예: `version=6`에서 `version=7`으로). 특정 버전 세그먼트를 하드코딩하는 대신 루트 경로에서 파일을 재귀적으로 읽는 것을 권장합니다. 이렇게 하면 버전 변경 후에도 파이프라인이 자동으로 데이터를 가져옵니다. 경로 형식에 대한 자세한 내용은 [이벤트 전달 의미론]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics)을 참조하세요. 버전별 변경 이력은 [Currents 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)를 참조하세요.

## `campaign_id` 또는 `canvas_id`가 메시지 인게이지먼트 이벤트에서 누락되는 이유는 무엇인가요? {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

이벤트 유형과 컨텍스트에 따라 메시지 인게이지먼트 이벤트가 특정 Campaign이나 캔버스 단계에 연결되지 않을 수 있습니다. 이러한 경우 `campaign_id`, `canvas_id` 및 관련 이름 필드가 이벤트 페이로드에서 생략될 수 있습니다. 특정 이벤트에서 해당 필드가 보이지 않는 경우, 해당 이벤트 유형과 컨텍스트에서 Campaign 또는 Canvas 식별자가 일반적으로 포함되는지 확인하세요.

## Currents 타임스탬프가 초 단위 정밀도로 제한되는 이유는 무엇인가요? {#why-are-currents-timestamps-limited-to-second-precision}

Currents 이벤트의 `time` 필드는 32비트 정수로 저장되므로 초 단위 정밀도로 제한됩니다. 일부 이벤트에는 별도의 64비트 밀리초 정밀도 타임스탬프 필드가 포함되어 있습니다. 각 이벤트 유형에서 사용 가능한 필드는 [이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary)을 확인하세요.

## Currents의 `users.canvas.Conversion` 이벤트 시간이 Canvas와 다른 이유는 무엇인가요? {#why-does-the-userscanvasconversion-event-from-currents-have-a-different-time-than-the-canvas}

Currents의 `users.canvas.Conversion` 이벤트 시간은 Canvas 진입 시점부터 측정되는 총 전환 기간, 즉 Canvas 기간과 전환 마감 기한을 합산한 시간을 반영합니다.

## S3로 참여 보고서가 전송되면 어떻게 되나요? {#what-happens-when-engagement-reports-are-sent-to-s3}

데이터 내보내기를 위해 S3 인증정보가 구성되어 있지만 Currents에는 구성되어 있지 않은 경우, Braze는 참여 보고서를 지정된 S3 버킷에 업로드합니다. **Send Report To** 필드에 나열된 사용자는 S3에 있는 보고서 링크가 포함된 이메일을 수신합니다.

## 익명 사용자 데이터를 Braze Currents를 통해 Amplitude로 전송할 수 있나요? {#can-anonymous-user-data-be-sent-to-amplitude-through-braze-currents}

`device_id`로 식별되는 익명 사용자 데이터는 Currents를 통해 Amplitude로 전송할 수 있습니다. 이 기능을 사용하려면 Braze 계정 팀의 기능 활성화가 필요합니다.

## Content Cards 및 인앱 메시지의 대조군 노출 횟수는 Currents에서 어떻게 기록되나요? {#how-are-control-group-impressions-for-content-cards-and-in-app-messages-logged-in-currents}

사용자가 Content Cards 또는 인앱 메시지 Campaign의 대조군에 배정되면, Currents는 노출 이벤트 대신 `users.campaigns.EnrollInControl` 이벤트를 발생시킵니다.

## API를 통해 존재하지 않는 사용자를 타겟팅하면 어떻게 되나요? {#what-happens-when-you-target-a-non-existent-user-through-the-api}

존재하지 않는 사용자를 타겟팅하면 API는 `200` 응답을 반환하지만, 발송은 "Unknown external ID"라는 결과와 함께 취소됩니다. 해당 발송에 대해 Currents 이벤트는 생성되지 않습니다. `send_to_existing_only` 파라미터의 기본값은 `true`이므로, 명시적으로 `false`로 설정하지 않는 한 알 수 없는 사용자에 대한 발송은 자동으로 건너뛰게 됩니다.