---
nav_title: 내보내기 로그
article_title: 내보내기 로그
page_order: 2
page_type: reference
description: "이 페이지에서는 내보내기 작업의 상태를 확인하고 진행 중인 내보내기를 취소할 수 있는 내보내기 로그에 대해 설명합니다."
---

# 내보내기 로그 {#exports-log}

> **내보내기 로그** 페이지를 사용하여 내보내기 작업의 상태를 확인하고 진행 중인 내보내기를 Braze 플랫폼에서 바로 취소할 수 있습니다. 내보내기 로그는 대시보드 또는 [사용자 내보내기 API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)에서 시작된 Segment 및 [억제 목록]({{site.baseurl}}/user_guide/audience/suppression_lists) 내보내기를 지원합니다.

내보내기 로그는 **설정** > **설정 및 테스트** > **내보내기 로그**로 이동하여 찾을 수 있습니다.

## 내보내기 로그에 표시되는 내용 {#what-the-exports-log-shows}

내보내기 로그에는 현재 워크스페이스의 내보내기 작업 목록이 표시됩니다. 각 행은 하나의 내보내기 시도를 나타내며, Segment 또는 수신 거부 목록 이름, 내보내기 소스, 상태, 타임스탬프를 포함합니다.

| 열 | 설명 |
|--------|-------------|
| 내보내기 ID | 내보내기 작업의 고유 식별자입니다. 이 ID를 선택하면 내보내기 세부 정보를 열거나 로그를 공유할 수 있습니다. |
| Segment 이름 | 내보낸 Segment 또는 수신 거부 목록의 이름입니다. |
| Segment 유형 | 내보내기 대상이 **Segment**인지 **수신 거부 목록**인지를 나타냅니다. |
| 소스 | 내보내기가 트리거된 위치입니다. **대시보드**(UI에서의 CSV 내보내기) 또는 **API**(사용자 내보내기 API)가 표시됩니다. |
| 상태 | 내보내기 작업의 현재 상태입니다. [내보내기 상태](#export-statuses)를 참조하세요. |
| 시작 시간 | 내보내기 작업이 시작된 시간입니다. |
| 완료 시간 | 내보내기 작업이 완료되거나, 실패하거나, 취소된 시간입니다. 작업이 진행 중인 경우 비어 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="내보내기 로그 열" }

## 내보내기 상태 {#export-statuses}

| 상태 | 설명 |
|--------|-------------|
| In Progress | 내보내기 작업이 실행 중입니다. |
| Complete | 내보내기가 성공적으로 완료되었습니다. |
| Failed | 내보내기가 완료되지 않았습니다. |
| Cancelled | 내보내기가 완료 전에 취소되었습니다. |
| Cancelling | 취소 요청이 진행 중입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="내보내기 상태" }

**In Progress** 상태의 내보내기만 취소할 수 있습니다. 내보내기가 더 이상 실행 중이 아닌 경우 취소 작업을 사용할 수 없습니다.

## 내보내기 상세 정보 {#export-details}

**Export ID**를 선택하면 해당 작업의 추가 상세 정보를 확인할 수 있습니다. 여기에는 다음이 포함됩니다:

| 필드 | 설명 |
|-------|-------------|
| Destination | 내보낸 파일이 전달되는 위치입니다(예: 해당되는 경우 클라우드 스토리지 경로). |
| Fields Exported | 내보내기에 포함된 사용자 프로필 필드입니다. |
| Self Hosted | 내보내기가 고객 호스팅 전달을 사용하는지 여부입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="내보내기 상세 정보 필드" }

내보내기 상세 정보 페이지에서 진행 중인 내보내기를 취소하거나 로그 항목에 대한 링크를 공유할 수 있습니다.

## 관련 내보내기 워크플로 {#related-export-workflows}

| 내보내기 유형 | 시작 방법 | 설명서 |
|-------------|--------------|---------------|
| Segment CSV 내보내기 | **오디언스** > **Segments** > Segment 선택 > **사용자 데이터** > **CSV 내보내기** | [Segment 데이터를 CSV로 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) |
| 수신 거부 목록 내보내기 | **오디언스** > **수신 거부 목록** | [수신 거부 목록]({{site.baseurl}}/user_guide/audience/suppression_lists) |
| API Segment 내보내기 | `POST /users/export/segment` | [POST: Segment별 사용자 프로필 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="관련 내보내기 워크플로" }

## 대기 중인 내보내기 취소 {#cancelling-a-pending-export}

**내보내기 로그** 페이지에서 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택한 다음 **Cancel Export**를 선택하거나, **Export ID**를 선택한 후 내보내기 페이지에서 **Cancel Export**를 선택하면 대기 중인 내보내기를 직접 취소할 수 있습니다.

## 특정 내보내기 로그 공유 {#sharing-a-specific-export-log}

**Export ID**를 선택한 다음 **Share Log**를 선택하여 내보내기 로그를 공유합니다.