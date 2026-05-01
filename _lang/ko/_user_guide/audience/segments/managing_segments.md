---
nav_title: Segment 관리
article_title: Segment 관리
page_order: 2
page_type: tutorial
tool: Segments
description: "이 문서에서는 Segment 목록 필터링, Segment 생성, Segment 편집 등 Segment를 관리하기 위해 수행할 수 있는 작업에 대해 설명합니다."

---

# Segment 관리 {#manage-segments}

> Segments 섹션에서는 기존 Segment의 전체 목록을 확인하고, 새 Segment를 생성하며, 기존 Segment를 편집할 수 있습니다. 다양한 필터와 열을 선택하여 Segment 목록을 세분화하면 가장 관련성 높은 정보만 표시할 수 있습니다.

![활성 Segment 목록을 표시하는 Segments 섹션.]({% image_buster /assets/img/segment/segments_page.png %})

## 보기 커스터마이징 {#customizing-your-view}

필터를 사용하고 표시할 열을 변경하여 Segment 목록 보기를 맞춤 설정할 수 있습니다. **Segments** 섹션을 떠났다가 다시 돌아오면 목록이 기본 보기로 되돌아가며, 이전에 선택한 필터가 모두 초기화됩니다.

### 상태 필터 {#status-filter}

활성 또는 아카이브된 Segment만 표시하도록 목록 범위를 좁힐 수 있습니다. 아카이브되지 않은 모든 Segment는 활성 상태로 간주됩니다.

### 필터 {#filters}

다음 필터를 조정하여 목록에서 Segment를 정렬할 수 있습니다:
- **마지막 수정자:** Segment를 마지막으로 편집한 사용자
- **마지막 수정일:** Segment가 마지막으로 편집된 시간 범위
- **예상 크기:** Segment에 포함된 사용자 수의 대략적인 범위
- **태그:** Segment에 연결된 태그
- **Teams:** Segment에 연결된 Teams
- **고급 추적 Segment만:** [분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/#segment-analytics-tracking)이 활성화된 Segment만 표시합니다.

### 열 {#columns}

Segment 목록에 표시할 수 있는 정보 열은 다음과 같습니다:
- **필터:** Segment의 필터 수
- **마지막 수정일:** Segment가 마지막으로 편집된 날짜
- **마지막 수정자:** Segment를 마지막으로 편집한 사용자
- **태그:** Segment에 연결된 태그
- **Teams:** Segment에 연결된 Teams
- **예상 크기:** Segment의 예상 사용자 수
- **Canvases:** Segment를 사용하는 Canvases 수
- **Campaigns:** Segment를 사용하는 Campaigns 수

### 즐겨찾기만 표시 {#show-starred-only}

**Show Starred Only**를 선택하면 사용자가 즐겨찾기로 표시한 Segment만 보기에 표시됩니다.

## Segment의 메시징 사용 현황 보기 {#messaging-use}

Segment의 **Messaging Use** 섹션으로 이동하면 해당 Segment가 다른 Segment, Campaigns, Canvases 등에서 어디에 사용되고 있는지 개요를 확인할 수 있습니다.

{% alert note %}
Segment가 서로 참조하는 루프를 방지하기 위해, **Segment Membership** 필터를 사용하는 Segment는 다른 Segment에서 참조할 수 없습니다. 자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)를 참조하세요.
{% endalert %}

## 특정 Segment 관리 {#managing-specific-segments}

![편집, 복제, 아카이브, 즐겨찾기에 추가 옵션을 보여주는 Segment 편집 메뉴.]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

특정 Segment를 관리하려면 해당 Segment 위에 마우스를 올리고 행 끝에 있는 메뉴 아이콘을 선택하여 다음 옵션을 확인하세요:
- **Edit:** Segment의 필터를 편집합니다.
- **Duplicate:** Segment의 사본을 만듭니다.
- **Archive:** Segment를 아카이브합니다. 해당 Segment를 사용하는 모든 Campaigns 또는 Canvases도 함께 아카이브됩니다.
- **Add to starred:** Segment를 즐겨찾기로 표시하면 Segments 섹션에서 즐겨찾기만 표시 체크박스를 선택하여 빠르게 접근할 수 있습니다.

여러 Segment 이름 옆의 체크박스를 선택하여 일괄 아카이브 및 일괄 태그 지정 등의 일괄 작업을 수행할 수도 있습니다.

{% alert tip %}
워크스페이스에 있는 기존 Segment의 머신 판독 가능한 내보내기가 필요한 경우(현재 테이블 보기뿐만 아니라), [Segment 목록 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)를 사용하고 결과를 페이지네이션하세요. 아카이브된 Segment를 감사하려면 상태 필터를 사용하여 **Segments** 대시보드에서 별도로 검토하세요.
{% endalert %}

![여러 Segment가 선택되어 있고 태그 지정 드롭다운 필드에서 CRM이 선택된 모습.]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### 마지막 조회 이후 변경 사항 {#changes-since-last-viewed}

팀원들이 Segment에 대해 수행한 업데이트 수는 Segment 개요 페이지의 *마지막 조회 이후 변경 사항* 측정기준으로 추적됩니다. **마지막 조회 이후 변경 사항**을 선택하면 Segment의 이름, 설명, 타겟 오디언스에 대한 업데이트 체인지로그를 확인할 수 있습니다. 각 업데이트에 대해 누가 언제 수행했는지 확인할 수 있습니다. 이 체인지로그를 사용하여 Segment의 변경 사항을 감사할 수 있습니다.

## Segment 검색 {#searching-for-segments}

검색 필드에 용어를 입력하여 Segment 이름을 검색할 수 있습니다.

이 필드에 입력한 모든 용어와 문자열이 검색됩니다. 예를 들어 "test segment 1"을 검색하면 이름에 "test", "segment" 또는 "1"이 포함된 Segment가 반환됩니다. 정확한 문자열을 검색하려면 검색어를 따옴표로 감싸세요. ["test segment 1"]을 검색하면 이름에 정확히 "test segment 1"이라는 문구가 포함된 모든 Segment가 반환됩니다.

![검색 필드에 "all users"를 입력한 검색 결과로 "All Users (Test)", "All Users", "All Users 15"가 표시됩니다.]({% image_buster /assets/img/segment/segments_search.png %})

### Canvases의 Segment {#segments-in-canvases}

다른 Segment, Campaigns 또는 Canvases에 포함된 모든 Segment 참조를 검색하려면 Segment의 [메시징 사용 현황](#messaging-use) 섹션으로 이동하세요. **Canvas** 페이지의 **Target segment** 필터는 Canvas 오디언스 Segment만 검색합니다.

![Canvas 페이지의 Target segment 필터.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}