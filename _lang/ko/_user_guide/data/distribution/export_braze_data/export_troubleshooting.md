---
nav_title: 문제 해결
article_title: 내보내기 문제 해결
page_order: 6
page_type: reference
description: "증상 색인, 표준 조사 경로, 스토리지별 오류 안내를 활용하여 CSV 및 API 내보내기 실패를 진단합니다."
---

# 내보내기 문제 해결 {#export-troubleshooting}

> 이 페이지에서는 대시보드 및 Export API에서 발생하는 CSV 및 API 내보내기 문제를 진단하는 방법을 안내합니다. 내보내기 워크플로우 및 제한 사항은 [Segment 데이터를 CSV로 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) 및 [Export API]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_apis)를 참조하세요.

## 여기서 시작하세요: 증상 매칭 {#start-here-match-your-symptom}

아래 표에서 현재 겪고 있는 동작을 찾은 후 해당 섹션으로 이동하여 맞춤 점검을 진행하세요.

| 증상 | 이동 |
| --- | --- |
| CSV 다운로드 링크가 `AccessDenied`, `ExpiredToken` 또는 "file doesn't exist"를 반환하는 경우 | [기본 내보내기: CSV 오류](#defaultexport_csv-exports) 또는 [클라우드 스토리지: CSV 오류](#csv-exports-1) |
| API 내보내기 다운로드 URL이 `403 Forbidden`을 반환하는 경우 | [내보낸 Segment ZIP을 다운로드할 수 없음](#cant-download-an-exported-segment-zip-from-a-braze-url) |
| Segment 내보내기가 실패하거나 Segment가 너무 크다는 메시지가 표시되는 경우 | [Segment가 너무 큼](#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users) |
| Segment 내보내기 이메일을 받지 못한 경우 | [Segment 내보내기 이메일 미수신](#not-receiving-segment-export-emails) |
| CSV 행 수가 Campaign 분석과 일치하지 않는 경우 | [Campaign 및 Canvas 분석 불일치](#number-of-users-in-csv-export-doesnt-match-messages-sent-or-unique-recipients) |
| 내보내기 파일에서 예상 열이 누락된 경우 | [누락된 열](#expected-columns-are-missing-from-a-segment-export-file) |
| 클라우드 스토리지 내보내기에서 `AccessDenied` 또는 `ExpiredToken`이 표시되는 경우 | [클라우드 스토리지 연결: API 오류](#common-errors-1) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="내보내기 증상" }

## 표준 조사 경로 {#standard-investigation-path}

모든 내보내기 문제에 대해 이 워크플로를 사용하세요. 1단계부터 시작합니다.

1. 기본 Braze S3 버킷으로 내보내기를 하는지, 아니면 연결된 클라우드 스토리지 파트너로 내보내기를 하는지 확인하세요. 링크 만료 및 재시도 동작은 두 가지 방식 간에 다릅니다.
2. 대시보드 CSV 내보내기의 경우, 다운로드 링크를 열 때 Braze에 로그인되어 있는지 확인하세요. 기본 버킷 링크는 활성 대시보드 세션이 필요합니다.
3. 내보내기가 완료된 후 얼마나 시간이 지났는지 확인하세요. 이메일로 전송된 대시보드 다운로드 링크는 기본 Braze 버킷을 사용하든 연결된 스토리지 파트너를 사용하든 4시간 후에 만료됩니다. 스토리지 파트너가 연결된 경우 Braze는 해당 버킷에도 사본을 전달합니다. 이 사본은 보존 정책에 따르며, 이메일 링크가 만료된 후에도 계속 사용할 수 있습니다.
4. 대규모 Segment 내보내기의 경우, 오디언스가 대시보드 CSV 내보내기 제한인 500,000명 이하인지 확인하세요. Segment 빌더 추정치는 내보내기 파이프라인 평가와 다를 수 있습니다.
5. API 내보내기의 경우, 다운로드하기 전에 처리가 완료될 때까지 기다리세요. URL을 즉시 요청하는 대신 [`/users/export/segment`]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#exporting-large-segments)에서 `callback_endpoint`를 사용하거나 지수 백오프로 폴링하세요.
6. 여전히 문제가 해결되지 않는 경우, 내보내기 유형(CSV 또는 API), Segment 또는 Campaign ID, 타임스탬프(시간대 포함), 정확한 오류 메시지를 포함하여 [Braze 지원팀](#standard-investigation-path)에 문의하세요.

## 스토리지 대상 {#cloud-storage-connected}

탭을 사용하여 기본 Braze S3 버킷으로 내보내는지, 클라우드 스토리지 파트너로 내보내는지 선택하세요. 클라우드 스토리지 안내는 **클라우드 스토리지 연결** 탭을 열고 CSV 및 API 섹션을 확인하세요.

{% sdktabs %}
{% sdktab Default export %}

기본 내보내기 대상으로 지정된 스토리지 파트너가 없는 경우, Braze는 자체 Amazon S3 버킷을 사용하여 내보내기 파일을 보관합니다. 이 설정의 파일은 임시 파일이며 4시간 후에 만료됩니다.

### CSV 내보내기 {#csv-exports}

증상: 대시보드 CSV 내보내기 이메일은 도착했지만 다운로드 링크가 실패하거나, 내보내기가 완료되지 않는 경우.


대시보드에서 CSV를 내보내면, Braze는 로그인한 사용자에게 다운로드 링크를 이메일로 발송합니다. 해당 링크는 Braze의 S3 버킷에 호스팅된 ZIP 파일을 가리킵니다. ZIP 파일 내부에는 여러 개의 작은 파일들이 포함되어 있으며, 이 파일들이 합쳐져 내보내기 데이터를 구성합니다.

링크를 사용하려면 Braze 대시보드에 로그인해야 하며, 파일은 4시간 동안만 이용 가능합니다. 그 이후에는 링크가 더 이상 작동하지 않으며 데이터는 삭제됩니다. 매우 큰 규모의 내보내기(500,000명 이상의 사용자)에서 반복적인 실패가 발생하면 내보내기가 실패할 수 있습니다. 이 경우 내보내기를 더 작은 그룹이나 필드로 나누어 보거나, 스토리지 파트너를 설정하는 것을 고려해 보세요.

#### 일반적인 오류 {#common-errors}

- `AccessDenied` 오류가 표시되면 파일이 이미 만료되었거나 준비되기 전에 열려고 시도했을 수 있습니다. 큰 보고서는 생성하는 데 시간이 더 오래 걸리므로, 몇 분 기다린 후 다시 시도해 보세요.
- `ExpiredToken` 오류는 4시간의 유효 기간이 지났음을 의미합니다. 내보내기를 다시 실행하여 새로운 링크를 생성하세요.
- `Looks like the file doesn't exist anymore` 메시지는 일반적으로 이메일은 전송되었지만 파일이 S3에 아직 업로드 완료되지 않았을 때 나타납니다. 몇 분만 기다리면 보통 해결됩니다.
- 특정 필드(예: `-`, `=`, `+`, 또는 `@`)의 시작 부분에 아포스트로피가 추가되는 것은 정상적인 동작입니다. 예를 들어, `-1943`은 CSV에서 `'-1943`으로 변환됩니다. Braze는 스프레드시트 프로그램이 데이터를 잘못 해석하는 것을 방지하기 위해 이렇게 처리합니다. 이는 [`/users/export/segment` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)에서 반환되는 것과 같은 JSON 내보내기에는 적용되지 않습니다.

### API 내보내기 {#api-exports}

증상: Export API 호출은 성공했지만 다운로드 URL이 실패하거나 빈 데이터를 반환하는 경우.


클라우드 스토리지 없이 Export API를 통해 내보낼 경우, Braze는 파일을 자체 S3 버킷에 기록합니다. 이메일은 발송되지 않으며, 대신 API 응답에 임시 다운로드 URL이 포함됩니다. 내보내기 파일은 ZIP 형식으로 제공되며, 각 ZIP 파일에는 여러 JSON 파일이 포함되어 있고, 각 JSON 파일에는 한 줄에 한 명의 사용자가 기록됩니다.

CSV 내보내기와 마찬가지로 API 링크도 4시간 후에 만료됩니다. 링크를 너무 일찍 클릭하면 파일이 아직 준비되지 않아 오류가 발생할 수 있습니다. 파일이 준비되었을 때 Braze에서 알림을 받으려면 요청에 `callback_endpoint`를 제공할 수 있습니다.

대규모 API 내보내기도 시간 초과될 수 있습니다. 이 경우 더 작은 요청을 시도하거나 스토리지 파트너를 연결하여 대용량을 처리하세요.

#### 일반적인 오류

- `AccessDenied` 또는 `ExpiredToken`은 일반적으로 링크가 만료되었거나 아직 준비되지 않았음을 의미합니다. 내보내기를 다시 실행하거나 조금 더 기다려 보세요.

{% endsdktab %}

{% sdktab Cloud storage connected %}

대시보드의 **기술 파트너** 페이지에서 스토리지 파트너(예: Amazon S3, Google Cloud Storage 또는 Azure Blob)를 연결하고 이를 기본 내보내기 대상으로 설정하면, Braze가 내보내기 데이터를 해당 버킷에 직접 기록합니다. 이 설정은 일반적으로 대용량 내보내기에 더 안정적입니다.

### CSV 내보내기 {#csv-exports-1}

증상: 이메일로 전송된 CSV 링크가 실패하지만 연결된 버킷에 파일이 나타나거나 나타나지 않는 경우.


CSV 내보내기 시, Braze에서 다운로드 링크를 이메일로 발송합니다. 해당 링크는 짧은 시간(일반적으로 약 4시간) 후에 만료됩니다. 스토리지 파트너가 연결되어 있고 기본 내보내기 대상으로 설정된 경우, Braze는 내보내기 데이터의 사본을 연결된 버킷에도 전달합니다. 해당 사본은 자체 인프라에 저장되며, 만료 및 보존 기간은 스토리지 정책을 따릅니다.

클라우드 스토리지에서 CSV 내보내기 파일은 ZIP 파일로 압축됩니다. ZIP 파일 내부에는 여러 개의 작은 CSV 파일이 포함되어 있습니다. 대규모 내보내기는 종종 여러 청크(예: 각각 약 5,000명의 사용자)로 분할되며, 청크 크기는 달라질 수 있습니다. 파일 크기가 작다고 해서 데이터가 누락된 것은 아닙니다. 이메일로 전송된 링크가 실패하더라도 스토리지에 저장된 사본이 성공적으로 전달되었다면, 언제든지 버킷에서 직접 데이터를 가져올 수 있습니다.

#### 일반적인 오류

- `AccessDenied`는 Braze가 버킷에 쓰기 작업을 수행할 수 없음을 의미합니다. 자격 증명과 권한이 여전히 유효한지 다시 확인하세요.
- `ExpiredToken`은 Braze가 버킷에 대한 접근 권한을 상실한 경우 표시됩니다. Braze 대시보드에서 자격 증명을 업데이트하세요.
- 일부 파일이 예상보다 작게 보이는 것은 정상적인 동작입니다. 내보내기 프로세스는 안정성을 위해 의도적으로 파일을 분할합니다.
- 특정 필드(예: `-`, `=`, `+`, 또는 `@`)의 시작 부분에 아포스트로피가 추가되는 것은 정상적인 동작입니다. 예를 들어, `-1943`은 CSV에서 `'-1943`으로 변환됩니다. Braze는 스프레드시트 프로그램이 데이터를 잘못 해석하는 것을 방지하기 위해 이렇게 처리합니다. 이는 [`/users/export/segment` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)에서 반환되는 것과 같은 JSON 내보내기에는 적용되지 않습니다.

### API 내보내기

증상: API 내보내기가 버킷에 나타나지 않거나 파일이 불완전한 경우.


스토리지 파트너가 연결된 상태에서 API를 통해 데이터를 내보내면, 내보내기 파일은 버킷에 기록됩니다. 이메일은 발송되지 않습니다. 기본 오브젝트는 스토리지에 존재하며 보존 설정을 따르지만, Braze가 반환하는 다운로드 URL은 여전히 시간 제한이 있을 수 있습니다.

파일은 일반적으로 내보내기가 실행되는 동안 버킷에 나타나므로, 부분 결과에 접근하기 위해 전체 작업이 완료될 때까지 기다릴 필요가 없습니다. Braze는 모든 데이터를 마지막까지 보관하는 대신 완료된 배치를 점진적으로 업로드합니다. 대용량 내보내기는 여러 압축 파일(ZIP 또는 GZIP)로 분할되며, 각 파일에는 한 줄에 하나씩 JSON 오브젝트가 포함되어 있습니다. 이 방법은 대용량 내보내기에 더 안정적입니다.

#### 일반적인 오류 {#common-errors-1}

- `AccessDenied`는 Braze가 버킷에 쓰기 작업을 수행할 수 없거나 오브젝트가 이후에 삭제된 경우 발생합니다. 권한을 확인하고 외부에서 파일을 삭제하는 요소가 없는지 확인하세요.
- `ExpiredToken`은 Braze의 버킷 접근 자격 증명이 만료되었음을 의미합니다. 대시보드에서 자격 증명을 새로고침하세요.
- 파일이 누락되었거나 예상보다 작은 경우, 먼저 Braze 외부에서 오브젝트를 삭제하는 요소가 없는지 확인하세요. 파일 크기가 작은 것 자체는 정상적인 동작입니다.

{% endsdktab %}
{% endsdktabs %}

## Campaign 및 Canvas 분석 {#campaign-and-canvas-analytics}

### CSV 내보내기의 사용자 수가 *보낸 메시지* 또는 *고유 수신자*와 일치하지 않는 경우 {#number-of-users-in-csv-export-doesnt-match-messages-sent-or-unique-recipients}

증상: Campaign의 CSV 내보내기에서 분석 페이지의 *보낸 메시지* 또는 *고유 수신자*와 다른 사용자 수가 표시됩니다.


Campaign의 CSV 내보내기는 다음과 같은 이유로 *보낸 메시지* 및 *고유 수신자*와 다른 사용자 수를 표시할 수 있습니다.

#### 재자격이 켜져 있는 경우 {#re-eligibility-is-turned-on}

사용자가 Campaign을 두 번 이상 수신할 수 있는 경우(또는 한때 그런 적이 있는 경우), Campaign 분석 수치와 사용자 데이터 내보내기의 행 수가 일치하지 않습니다. *보낸 메시지*는 동일한 사용자에게 두 번 이상 메시지를 보낸 경우를 포함하여 모든 발송을 집계합니다. **CSV 사용자 데이터 내보내기** 다운로드는 고유 사용자만 나열합니다. 즉, 발송당 한 행이 아니라 Campaign을 수신한 프로필당 한 행입니다. 예를 들어, *보낸 메시지*가 12이고 CSV에 10개의 행이 있다면, 해당 12건의 발송은 10명의 고유 사용자에게 전달된 것입니다(일부 사용자에게 Campaign이 두 번 이상 발송됨).

#### Campaign 또는 Canvas 발송 이후 사용자가 삭제되거나 병합된 경우 {#users-were-deleted-or-merged-since-the-campaign-or-canvas-sent}

CSV 내보내기는 특정 Campaign 또는 Canvas를 수신한 기존 사용자의 스냅샷을 제공합니다. 사용자가 삭제되거나 병합될 수 있으므로, CSV 내보내기 수가 고유 수신자 수보다 적을 수 있습니다. 예를 들어, 1,000명의 사용자가 Campaign을 수신하면 Campaign에는 1,000명의 고유 수신자가 표시되고, 같은 날 CSV 내보내기에도 1,000명의 사용자가 표시됩니다. 한 달 후 해당 1,000명 중 50명이 삭제되면, CSV 내보내기에는 950명의 사용자가 포함되지만 누적된 고유 수신자 수는 여전히 1,000입니다.

## 대시보드 Segment 내보내기 이메일 {#dashboard-segment-export-emails}

### Segment가 너무 크거나 50만 명 미만인 것처럼 보이는데 내보내기가 실패합니다 {#segment-is-too-large-or-export-fails-when-my-segment-looks-under-500000-users}

증상: 대시보드 Segment 내보내기가 실패하거나, Segment 추정치가 적절해 보임에도 크기 오류가 표시됩니다.


대시보드 Segment **크기는 추정치입니다**. CSV 내보내기는 이 추정치를 사용하여 [50만 명 사용자 내보내기 제한]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details)을 적용하며, 내보내기 파이프라인은 Segment 빌더 UI와 다르게 크기를 평가할 수 있습니다. 해당 임계값 근처의 Segment에서 내보내기가 실패하는 경우, [무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)를 사용하거나 오디언스를 더 작은 Segment로 분할하세요. 또는 [대용량 Segment 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)에 설명된 대로 [`/users/export/segment` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)를 사용하세요.

### Segment 내보내기 이메일이 수신되지 않는 이유는 무엇인가요? {#not-receiving-segment-export-emails}

증상: Segment CSV 내보내기가 트리거되었지만 이메일이 도착하지 않습니다.


먼저 스팸 폴더에서 `no-reply@alerts.braze.com`으로부터 온 이메일이 있는지 확인하세요. 해당 이메일이 스팸 폴더에 있다면, 이후 내보내기 메시지가 필터링되지 않도록 해당 주소를 수신 허용 목록에 추가하세요.

스팸 폴더에도 이메일이 없다면, 팀의 다른 구성원이 내보내기 이메일을 수신할 수 있는지 확인하세요. 다른 구성원도 수신할 수 없다면, 내보내기 크기를 확인해 보세요. 배달 시간은 내보내기 크기에 따라 달라지지만, 1시간이 지나도 이메일이 도착하지 않으면 [지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.

## Segment 내보내기 API 다운로드 {#segment-export-api-downloads}

### Braze URL에서 내보낸 Segment ZIP을 다운로드할 수 없음 {#cant-download-an-exported-segment-zip-from-a-braze-url}

증상: `/users/export/segment` 응답 URL에서 다운로드할 때 `403 Forbidden` 오류가 발생합니다.


[`/users/export/segment` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)를 사용할 때 `403 Forbidden` 오류가 발생하면, 파일이 아직 준비되지 않았을 수 있습니다. 대용량 내보내기는 처리에 시간이 걸릴 수 있습니다. 최대 1시간 정도 기다린 후 다시 다운로드해 보세요.

자동화된 스크립트를 사용하여 파일을 가져오는 경우, URL을 너무 빨리 요청하면 `403 Forbidden` 오류가 발생할 수도 있습니다. Segment 데이터를 정기적으로 내보내는 경우, 자체 S3 버킷 통합을 연결하고 파일을 자체 ETL(추출, 변환, 로드) 파이프라인으로 전달하는 것을 고려해 보세요.

내보내기는 완료까지 시간이 걸리므로, 스크립트에서 즉시 액세스하면 실패하는 경우가 많습니다. 다음 방법을 사용할 수 있습니다:

- 지수 백오프를 적용하여 다운로드 URL을 폴링하거나,
- [`callback_endpoint` 파라미터]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#request-parameters)를 사용하여 내보내기가 준비되면 스크립트를 실행하는 서비스를 지정합니다.

## Segment 및 사용자 내보내기 API 필드 {#segment-and-user-export-api-fields}

### Segment 내보내기 파일에서 예상 열이 누락됨 {#expected-columns-are-missing-from-a-segment-export-file}

증상: API 또는 대시보드 내보내기에서 예상했던 필드가 누락되어 있습니다.


대시보드에서 Segment의 **CSV Export User Data**는 고정된 열 집합을 사용합니다([CSV로 Segment 데이터 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#data-included-in-export) 참조). 여기에는 `fields_to_export` 열이나 파라미터가 포함되지 않습니다.

API Segment 내보내기의 경우, 요청 본문에 `fields_to_export`를 전달해야 합니다. 일부 필드는 관련 데이터를 자동으로 가져옵니다. 예를 들어, `canvases_received`를 요청하면 고객 프로필에 여정 요약 데이터도 필요합니다. 유효한 필드 이름과 요구 사항은 [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) 엔드포인트 참조를 확인하세요.

API 내보내기 ZIP에서 열이 누락된 경우, 요청의 `fields_to_export` 배열에 필요한 모든 필드가 포함되어 있는지, 워크스페이스에 필수 내보내기 권한이 설정되어 있는지 확인하세요.

## 지원팀에 문의해야 하는 경우 {#when-to-contact-support}

[표준 조사 경로]({{site.baseurl}}/user_guide/administer/personal/braze_support)를 완료했지만 여전히 도움이 필요한 경우 [Braze 지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요. 내보내기 유형, Segment 또는 Campaign ID, 타임스탬프(시간대 포함), 정확한 오류 메시지 또는 HTTP 상태 코드를 포함해 주세요.