---
nav_title: 보고서 빌더
article_title: 보고서 빌더
alias: /report_builder/
page_type: reference
description: "이 참조 문서에서는 보고서 빌더 기능에 대해 설명합니다."
tool:
    - Reports
page_order: 3
---

# 보고서 빌더 {#report-builder}

> 이 페이지에서는 보고서 빌더를 사용하여 Braze 데이터로 세분화된 보고서를 생성 및 조회하는 방법과 보고서를 대시보드에 추가하는 방법을 다룹니다.

다음 동영상에서는 보고서 빌더에서 보고서를 생성하고 커스터마이즈하는 방법에 대한 개요를 제공합니다.

{% multi_lang_include video.html id="oi66kwwldv" source="wistia" %}

## 보고서 템플릿 사용하기 {#using-a-report-template}

1. **Analytics** > **보고서 빌더 (신규)**로 이동합니다.
2. **새 보고서 생성** 버튼 옆의 **더 보기** 화살표를 선택한 다음 **보고서 템플릿 사용**을 선택합니다.<br><br>![커스텀 보고서 생성 또는 템플릿 사용 옵션이 표시된 "새 보고서 생성" 버튼 드롭다운]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Braze 템플릿 라이브러리에서 보고서 템플릿 중 하나를 선택합니다.
    - **행 항목** 및 **태그** 드롭다운을 사용하여 사용 사례에 적합한 보고서를 찾으세요.<br><br>![선택할 수 있는 Braze 템플릿 목록이 표시된 "Braze 보고서 템플릿" 창]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. [보고서 생성하기](#creating-a-report)의 3단계 이후를 따라 사용 사례에 맞게 보고서를 추가로 커스터마이즈합니다.

## 보고서 생성 {#creating-a-report}

1. **Analytics** > **보고서 빌더 (신규)**로 이동합니다.
2. **새 보고서 생성**을 선택합니다.
3. **행** 드롭다운에서 보고할 항목을 선택합니다:
    - Campaigns
    - Canvases
    - Campaigns 및 Canvases
    - 채널
    - 태그

    **행** 선택에 따라 [조회할 수 있는 측정기준](#metrics-availability)이 달라집니다. 예를 들어, 다변량 측정기준은 **Canvases**를 보고하거나 **배리언트** 드릴다운이 적용된 **Campaigns**를 보고할 때만 조회할 수 있습니다. **Campaigns 및 Canvases**를 함께 보고할 때는 해당 Campaign과 Canvases에 다변량 테스트가 있더라도 이러한 측정기준을 조회할 수 없습니다.

![보고서의 행과 그룹을 선택하는 필드가 있는 "행과 열" 섹션]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4. (선택 사항) **드릴다운 추가**를 선택하여 데이터를 더 세분화된 뷰로 분류합니다:
    - 채널
    - 날짜
        - 데이터를 더 작은 시간 범위로 분할할 때 사용합니다. 예를 들어, Campaign이 일별로 어떤 성과를 보였는지 확인하려면 다음과 같이 구성합니다:
            - **행**: Campaigns
            - **그룹화:** 날짜
            - **간격:** 일
    - 배리언트
    - Campaigns 및 Canvases

{% alert tip %}
다양한 드릴다운 옵션 구성을 시도하여 [데이터를 분류할 수 있는 다양한 방법](#metrics-availability)을 탐색해 보세요.
{% endalert %}

{: start="5"}
5. **열** 섹션에서 **측정기준 사용자 지정**을 선택합니다.

![여러 측정기준을 선택할 수 있는 옵션이 있는 "측정기준 사용자 지정" 섹션]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6. 카테고리별로 측정기준을 탐색하고 해당 체크박스를 선택하여 보고서에 측정기준을 추가합니다.
    - **일반** 아래에서 **태그**를 선택하면 보고서 행의 각 Campaign 또는 Canvas에 적용된 태그가 포함됩니다.
    - 점선 아이콘을 위아래로 드래그하여 측정기준과 열을 재정렬할 수 있습니다.
7. **보고서 콘텐츠**에서 보고서에 포함할 데이터의 날짜 범위를 구성합니다.
8. 그런 다음, 3단계에서의 선택에 따라 Campaign, Canvases 또는 둘 다를 수동 또는 자동으로 보고서에 추가합니다.
    - **수동 추가:** **마지막 발송** 날짜 및 태그 또는 채널 필터를 사용하거나 Campaign 또는 Canvas 이름을 검색하여 보고서에 포함할 각 Campaign 또는 Canvas를 선택합니다.<br><br>![선택할 수 있는 Campaign 목록이 표시된 "수동으로 Campaign 및 Canvases 추가" 섹션]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **자동 추가:** 보고서에 포함할 Campaign 또는 Canvases에 대한 규칙을 설정합니다. 이 페이지에서 하나의 필드만 선택하면 됩니다.
        - 이 화면에서 설정한 조건을 충족하는 추가 Campaign 또는 Canvases가 있으면 향후 보고서 실행 시 자동으로 추가됩니다.
        - **채널** 드롭다운에 배너는 옵션으로 제공되지 않으므로, 채널 규칙을 사용하여 배너 Campaign 또는 Canvases를 자동으로 추가할 수 없습니다. 그러나 보고서 측정기준에 배너 KPI를 포함할 수는 있습니다.<br><br>![보고서에 추가할 Campaign 및 Canvases 규칙을 설정하는 필드가 있는 "자동으로 Campaign 및 Canvases 추가" 섹션]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9. **저장 및 실행**을 선택하여 보고서를 실행합니다.

{% alert note %}
구성 단계에서 선택한 날짜 범위와 Campaign 또는 Canvases 수에 따라 보고서 실행에 몇 분 정도 소요될 수 있습니다.
{% endalert %}

## 측정기준 가용성 {#metrics-availability}

**행** 선택에 따라 선택할 수 있는 측정기준이 달라집니다.

{% alert tip %}
캔버스 배리언트 또는 단계에 대해 보고하려면, 행에 **Canvases**를 선택하고 드릴다운 필드를 비워 두거나 **Date**를 선택합니다. 보고서를 실행하면 결과 페이지에 **Canvas View** 드롭다운이 나타나며, 이를 통해 Canvas 전체의 측정기준을 확인하거나 배리언트, 단계 또는 메시지별로 측정기준을 그룹화하여 볼 수 있습니다.<br><br> 보고서를 편집할 때 미리보기 테이블에는 최대 50개 행이 표시됩니다. 보고서를 실행하면 결과 페이지에서 페이지네이션(페이지당 100개 행)으로 모든 행을 확인하거나 전체 데이터셋을 CSV로 내보낼 수 있습니다.

![열린 Canvas View 드롭다운.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| 측정기준 | 설명 |
| --- | --- |
| 전환 측정기준 | Campaigns, Canvases, Campaigns 및 Canvases에서 사용할 수 있습니다. |
| 진입 | Campaigns, Canvases, Campaigns 및 Canvases, 태그에서 사용할 수 있습니다. |
| 마지막 발송 날짜 | Campaigns, Canvases, Campaigns 및 Canvases에서 사용할 수 있습니다. 스케줄된 Campaign에만 표시되며, 액션 기반 또는 API 트리거 Campaign에서는 채워지지 않습니다. |
| 태그 | Campaigns, Canvases, Campaigns 및 Canvases에서 사용할 수 있습니다. 각 Campaign 또는 Canvas에 적용된 태그를 나열합니다. 메시지에 여러 태그가 있는 경우 세미콜론으로 구분된 목록으로 표시됩니다. |
| 발송 | 관련 채널별로 사용할 수 있습니다. |
| 메시지 발송됨 | Campaigns, Canvases, Campaigns 및 Canvases, 태그에서 사용할 수 있습니다. |
| 제목란 | **배리언트** 드릴다운이 있는 이메일 Campaigns, Canvases, **배리언트** 드릴다운이 있는 Canvases에서 사용할 수 있습니다. |
| 총 매출 | Campaigns, Canvases, Campaigns 및 Canvases, 태그에서 사용할 수 있습니다. **Channels** 드릴다운에서는 사용할 수 없습니다. |
| 고유 노출 횟수 | Campaigns, Canvases, Campaigns 및 Canvases, 태그에서 사용할 수 있습니다. |
| 고유 수신자 | Campaigns, Canvases, Campaigns 및 Canvases, 태그에서 사용할 수 있습니다. **Channels** 드릴다운에서는 사용할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="측정기준 가용성" }

### 삭제된 메시지 배리언트 {#deleted-message-variants}

Campaign 또는 Canvases별로 보고서를 분류할 때는 삭제된 메시지 배리언트의 통계가 표시되지 않습니다. 그러나 채널 수준의 합계에는 배리언트 삭제 여부와 관계없이 모든 통계가 포함됩니다. 예를 들어, 이메일의 _발송_에는 모든 이메일 발송이 포함되지만, 이를 Campaign별로 분류하면 삭제된 메시지 배리언트의 발송이 필터링되어 숫자가 더 낮을 수 있습니다.

같은 보고서에서 메시지 배리언트가 발송 후 삭제된 경우 _고유 수신자_가 _고유 노출 횟수_보다 높을 수 있습니다. Campaign 수준의 _고유 수신자_에는 삭제된 배리언트를 받은 사용자가 여전히 포함될 수 있지만, _고유 노출 횟수_는 메시지 수준 집계에서 삭제된 배리언트의 통계를 제외합니다.

## 보고서 보기 {#viewing-a-report}

보고서를 실행한 후 보고서 결과 페이지에서 테이블 형식으로 결과를 확인할 수 있습니다.

![각 Campaign 측정기준에 대한 보고서 데이터 테이블.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### 보고서 차트 만들기 {#creating-a-report-chart}

페이지 하단에서 **차트 유형**을 선택하고 차트 측정기준을 구성하여 데이터 차트를 만들 수 있습니다. 기본적으로 첫 번째 측정기준이 표시됩니다.

![보고서 데이터 차트와 차트의 x축, y축, 차트 유형 등을 구성하는 옵션.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
꺾은선 차트를 만들려면 보고서를 구성할 때 드릴다운 옵션으로 **Date**를 선택하세요. 이렇게 하면 시간에 따른 추세를 표시할 수 있습니다.
{% endalert %}

#### 보고서 차트 다운로드 {#downloading-a-report-chart}

보고서 차트의 이미지를 다운로드하려면 점 아이콘을 선택한 다음 다운로드 옵션을 선택합니다.

![다양한 파일 형식에 대한 다운로드 옵션이 있는 메뉴.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## 보고서 공유 {#sharing-a-report}

**공유**를 선택한 후 다음 옵션 중 하나를 선택하여 보고서에 대한 대시보드 링크를 공유할 수 있습니다:
- **링크 공유:** 링크를 복사하여 공유합니다.
- **이메일 전송 또는 스케줄:** 1시간 후 만료되는 다운로드 링크가 포함된 이메일을 즉시 또는 지정된 시간에 전송합니다. **이메일 수신자** 드롭다운에 나열된 회사 사용자 중에서 수신자를 선택하거나, 다른 이메일 주소를 직접 입력할 수 있습니다.

{% alert note %}
**이메일 수신자** 드롭다운에는 Braze 회사 사용자만 표시되며, 이들의 이메일 주소는 보고서 스케줄 전체에 걸쳐 저장됩니다. 외부 이메일 주소는 새 보고서 스케줄을 생성할 때마다 수동으로 입력해야 합니다. 파트너 담당자 등 외부 수신자에게 보고서를 자주 전송하는 경우, 적절한 권한을 가진 회사 사용자로 추가하면 해당 주소가 드롭다운에 표시됩니다.
{% endalert %}

![보고서 형식, 수신자, 전송 시간을 선택할 수 있는 필드가 있는 이메일 스케줄 창]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **CSV 다운로드:** 보고서의 CSV를 다운로드합니다.

## 대시보드에 보고서 추가 {#adding-a-report-to-a-dashboard}

1. 보고서 테이블 상단의 점 아이콘을 선택합니다.
2. **대시보드에 추가**를 선택합니다.
3. 새 대시보드를 생성할지 기존 대시보드에 추가할지 선택합니다.<br><br>![보고서를 새 대시보드에 추가할지 기존 대시보드에 추가할지 선택하는 옵션이 있는 창]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. 대시보드 작성에 대해 자세히 알아보려면 [대시보드 빌더]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder)의 단계를 따르세요.

## 팀 권한 {#team-permissions}

보고서 빌더 보고서는 Campaign이나 Canvases와 달리 [팀 할당]({{site.baseurl}}/user_guide/administer/global/user_management/teams)을 지원하지 않습니다. 보고서를 생성할 때 저장된 보고서를 특정 팀으로 제한할 수 없습니다.

팀 수준의 ["대시보드 보고서 보기"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) 권한(워크스페이스 수준이 아닌)을 가진 사용자도 보고서 빌더를 사용할 수 있지만, 보고서 가시성이 제한됩니다:

- 이러한 사용자는 선택된 모든 Campaign과 Canvas가 자신의 팀에 할당된 보고서만 볼 수 있습니다.
- **채널**이 행으로 설정된 보고서는 숨겨집니다.
- 자동 선택을 사용하여 Campaign이나 Canvases를 추가하는 보고서는 숨겨집니다. 보고서 실행 시 추가될 수 있는 메시지에 대해 Braze가 팀 접근 권한을 확인할 수 없기 때문입니다.

[보고서 빌더 (레거시)]({{site.baseurl}}/report_builder_legacy)는 보고서에 추가할 수 있는 Campaign과 Canvases를 팀별로 범위를 지정하지만, 저장된 보고서는 보고서 빌더 (신규)에서와 같은 방식으로 목록에서 필터링되지 않습니다. 권한 설정에 대한 자세한 내용은 [사용자 권한 설정]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) 및 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams)를 참조하세요.

## 문제 해결 {#troubleshooting}

### 보고서에서 Campaign 또는 Canvas의 발송이 표시되지 않음 {#report-shows-no-sends-for-a-campaign-or-canvas}

Campaign 또는 Canvas는 **마지막 발송** 날짜가 설정한 **마지막 발송** 기간 내에 해당할 때 보고서에 표시됩니다. **발송** 및 기타 측정기준은 **데이터 표시 기간** 날짜 범위 내의 활동에 대해서만 채워집니다. 메시지가 **데이터 표시 기간** 동안 발송되지 않았다면, 해당 행에 Campaign 또는 Canvas가 발송 수 0으로 표시될 수 있습니다.

예를 들어 **마지막 발송**이 2025년 1월 1일~2025년 4월 14일로 설정되어 Campaign이 포함되었지만, **데이터 표시 기간**은 2024년 12월 1일~2025년 1월 14일인 경우를 가정해 보겠습니다. 해당 Campaign이 12월이나 1월에 발송이 없었다면, 테이블에는 여전히 표시되지만 발송 측정기준은 없습니다.

### 다운로드 링크가 만료됨 {#download-link-has-expired}

보고서 다운로드 링크는 1시간 후에 만료됩니다. 링크가 만료된 경우 새 보고서를 생성하고 1시간 이내에 다운로드하세요. 만료 시간을 연장하는 방법은 없습니다.

[Amazon S3 버킷]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)이 **파트너 통합**에 연결되어 있는 경우, S3 버킷을 직접 탐색하여 이전 보고서의 데이터를 가져올 수 있습니다.