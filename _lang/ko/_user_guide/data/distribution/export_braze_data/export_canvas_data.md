---
nav_title: 캔버스 데이터
article_title: Canvas 데이터 내보내기
page_order: 3
page_type: reference
description: "이 참조 문서에서는 Canvas 분석을 내보내는 방법에 대해 설명합니다."
tool:
  - Canvas
  - Reports

---

# Canvas 데이터 내보내기 {#export-canvas-data}

> 사용자 데이터를 CSV로 내보낼 수 있습니다. 이 페이지에서는 전체 Canvas 또는 특정 Canvas 구성요소의 데이터를 내보내는 방법을 설명합니다.

## Canvas 데이터 내보내기 {#exporting-data-for-a-canvas}

Canvas 데이터를 내보내려면 다음과 같이 하세요.

1. **메시징** > **Canvas**로 이동하여 Canvas를 선택합니다.
2. **Canvas 세부 정보** 섹션에서 **사용자 데이터** 드롭다운을 선택합니다.
3. 다음 내보내기 옵션 중 하나를 선택합니다:
  - **CSV 내보내기 사용자 데이터** 또는
  - **CSV 내보내기 이메일 주소**.

Canvas의 모든 참가자에 대한 사용자 데이터를 CSV 파일로 내보낼 수도 있습니다.

## Canvas에 진입하거나 재진입한 사용자 내보내기 {#export-users-who-entered-or-re-entered-a-canvas}

[재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)이 활성화되면 사용자는 동일한 Canvas에 두 번 이상 진입할 수 있습니다. Canvas 세부 정보 페이지의 **CSV 내보내기 사용자 데이터** 옵션은 Canvas에 진입한 사용자를 내보내지만, 각 사용자가 몇 번 진입했는지 또는 각 진입 타임스탬프는 포함하지 않습니다.

사용자가 Canvas에 진입하거나 재진입한 시점을 분석하려면 다음 옵션 중 하나를 사용하세요.

- **사용자별 가장 최근 진입:** [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) 엔드포인트를 사용하여 [`canvases_received`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) 필드가 포함된 Segment를 내보냅니다. 각 Canvas에 대해 해당 사용자의 `last_entered` 및 `last_exited` 타임스탬프가 포함됩니다. `canvases_received` 필드에는 최근 90일간의 데이터가 포함됩니다.
- **재진입을 포함한 모든 진입:** Braze 커런츠 또는 Snowflake 데이터 공유에서 [Canvas 진입 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-entry-events)를 사용합니다. 각 `users.canvas.Entry` 이벤트는 하나의 Canvas 진입을 나타내며 `time` 타임스탬프를 포함합니다. 사용자별 이벤트 수를 집계하여 진입 횟수를 확인할 수 있습니다.
- **대시보드에서 사용자 목록 작성:** **Entered Canvas Variation** 필터를 사용하여 Segment를 생성한 다음 해당 Segment를 CSV로 내보냅니다. [Canvas 문제 해결]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#user-didnt-enter-a-canvas)을 참조하세요.

{% alert note %}
Currents가 연동되어 있지 않고 모든 과거 진입 타임스탬프가 필요한 경우, Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

원본 워크플로의 특정 캔버스 단계에 대해서는 해당 단계의 세부 정보 페이지에서 **CSV 내보내기 사용자 데이터**를 사용하세요.

## 구성요소 데이터 내보내기(원본 워크플로만 해당) {#exporting-data-for-a-component-original-workflow-only}

Canvas 결과는 원본 Canvas 워크플로에서 개별 구성요소 단위로 내보낼 수 있습니다. 이렇게 하려면 특정 구성요소를 선택한 다음 **캔버스 단계 세부 정보** 페이지에서 **사용자 데이터** 드롭다운을 선택합니다.

![Canvas 세부 정보 페이지의 사용자 데이터 드롭다운.]({% image_buster /assets/img/canvas_csv_export.png %})

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting) 문서를 참조하세요.
{% endalert %}