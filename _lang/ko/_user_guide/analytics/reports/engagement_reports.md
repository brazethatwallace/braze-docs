---
nav_title: 참여 보고서
article_title: 참여 보고서
page_order: 5
local_redirect:
  report-glossary: '/docs/user_guide/analytics/metrics_glossary'
page_type: tutorial
description: "이 사용 방법 문서에서는 Campaigns 및 Canvases에 대한 참여 보고서를 생성, 맞춤 설정 및 예약하는 방법을 안내합니다."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# 참여 보고서 {#engagement-reports}

> 참여 보고서를 사용하면 Campaigns 및 Canvases의 특정 메시지에 대한 참여 통계를 가져와 원하는 시간에 이메일로 받을 수 있습니다.

{% alert note %}
참여 보고서를 실행하려면 "사용자 데이터 내보내기" 권한이 필요합니다.
{% endalert %}

참여 보고서를 사용하면 이메일 보고서에 포함할 Campaigns 및 Canvases를 수동으로 선택하거나, 규칙을 지정하여 관련 Campaigns 및 Canvases를 자동으로 선택할 수 있습니다.

선택한 Campaigns 또는 Canvases의 수에 관계없이 최대 두 개의 CSV 파일이 생성됩니다. 하나는 모든 캠페인 데이터용이고 다른 하나는 모든 Canvas 데이터용입니다. 보고서 이메일에 포함된 링크에서 이 CSV 파일에 액세스할 수 있습니다. 참여 보고서는 Braze 대시보드에 저장되지 않습니다.

일부 데이터는 개별 캠페인 배리언트 또는 캔버스 단계 수준이 아닌 캠페인 또는 Canvas 수준에서 집계됩니다. [시작 후 캔버스 단계를 삭제]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#canvas-details)하면 참여 보고서에서도 해당 데이터가 제거됩니다.

{% alert tip %}
보고서를 다시 실행하여 업데이트된 통계를 생성할 수 있습니다.
{% endalert %}

## 새 보고서 생성 {#creating-a-new-report}

### 1단계: 보고서 생성 {#step-1-create-a-report}

대시보드 계정에서 **Analytics** > **참여 보고서**로 이동합니다. **+ 새 보고서 생성**을 선택합니다.

### 2단계: 메시지 추가 {#step-2-add-messages}

보고서에 포함할 Campaigns 및 Canvas 메시지를 추가합니다. 두 가지 방법으로 메시지를 선택할 수 있습니다:

- Campaigns 및 Canvases를 수동으로 선택
- 특정 규칙에 따라 Campaigns 및 Canvases를 자동으로 선택

![engagement_reports_message_selection]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Campaigns 또는 Canvases를 수동으로 선택 {#manually-select-campaigns-or-canvases}

이 옵션을 사용하면 이 보고서에 포함할 Campaigns 또는 Canvases를 자유롭게 선택할 수 있습니다.

#### Campaigns 또는 Canvases를 자동으로 선택 {#automatically-select-campaigns-or-canvases}

이 옵션을 사용하면 특정 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)가 포함된 모든 메시지를 자동으로 포함할 수 있습니다. 나열된 태그 중 하나 또는 모든 태그가 있는 메시지를 타겟팅할 수 있습니다. 이 옵션은 반복 보고서를 설정하고 참여 메시지에 정기적으로 태그를 지정하는 경우에 유용합니다.

{% alert important %}
보고서가 생성되려면 태그가 하나 이상의 캠페인 또는 Canvas와 일치해야 합니다. **특정 규칙에 따라 Campaigns 및 Canvases를 자동으로 선택**을 사용하고 오류가 표시되면, 하나 이상의 캠페인 또는 Canvas가 태그 및 기타 필터와 일치하는지 확인하세요(예: 나열된 모든 태그를 요구하는 경우, 일치하는 모든 메시지에 모든 태그가 있어야 합니다).
{% endalert %}

### 3단계: 통계 추가 {#add-statistics-to-your-reports}

**통계 추가** 단계에서는 선택한 Campaigns 또는 Canvases 유형에 대한 통계를 보여줍니다. 예를 들어, 이메일 메시지를 선택한 경우 관련 이메일 통계만 볼 수 있습니다. 이메일과 푸시의 조합을 선택한 경우 두 채널의 통계를 볼 수 있습니다.

![engagement_report_add_stats]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

참여 보고서는 캠페인 또는 Canvas별로 데이터를 집계하며, 워크스페이스 수준에서 집계하지 않습니다. 모든 활성 Campaigns 및 Canvases에 걸친 총 발송 수 또는 노출 횟수(예: 전체 워크스페이스의 채널별 발송 수 및 노출 횟수)를 모니터링하려면 [보고서 빌더]({{site.baseurl}}/report_builder)를 사용하세요.

{% alert note %}
*통신사 전송 수*는 더 이상 사용되지 않지만, 이미 사용 중인 사용자에게는 계속 지원됩니다.
{% endalert %}

| 채널 | 사용 가능한 통계 |
| ------| --------------|
| 이메일 | 발송 수, 열람 수, 고유 열람 수, 클릭 수, 고유 클릭 수, 클릭 대비 열람률, 탈퇴 수, 반송 수, 전달 수, 스팸 신고 수 |
| 푸시  | 발송 수, 열람 수, 영향받은 열람 수, 반송 수, 본문 클릭 수 |
| 웹 푸시 | 발송 수, 열람 수, 반송 수, 본문 클릭 수 |
| 인앱 메시지 | 노출 횟수, 클릭 수, 첫 번째 버튼 클릭 수, 두 번째 버튼 클릭 수 |
| 웹훅  |  발송 수, 오류 수 |
| SMS | 발송 수, 통신사 전송 수, 전달 확인 수, 전달 실패 수, 거부 수 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3단계: 통계 추가 #add-statistics-to-your-reports" }

### 4단계: 보고서 설정 완료 {#step-4-complete-report-setup}

보고서에 이름을 지정하고, 보고서 형식을 선택하고, 수신자를 선택합니다. 기본적으로 참여 보고서는 데이터가 쉼표로 구분된(각 데이터가 쉼표로 구분되는) ZIP 파일로 전송됩니다.

다음 압축 및 구분 기호 옵션 중에서 선택할 수 있습니다:

- **압축:** ZIP, 비압축 또는 gzip
- **구분 기호:** 쉼표(`,`), 콜론(`:`), 세미콜론(`;`) 또는 파이프(`|`)

{% alert note %}
통계는 보고서에서 지정한 날짜 범위에 대해서만 수집됩니다. 정확한 열람률 및 클릭률 통계를 받으려면 Campaigns 및 Canvases에 대한 발송 이벤트가 수행된 시점을 포함하는 날짜 범위를 선택하세요.
{% endalert %}

#### 기간 선택 {#select-time-frame}

기본적으로 표시되는 데이터 범위는 회사의 시간대를 기준으로 하며, 선택한 가장 이른 메시지부터 현재 날짜까지입니다. 날짜 드롭다운을 선택하고 커스텀 범위 선택을 사용하거나, 다음 라디오 버튼을 선택하고 사용 가능한 드롭다운 옵션으로 날짜 범위를 정의하여 이를 맞춤 설정할 수 있습니다.

#### 데이터 표시 선택 {#select-data-display}

기본적으로 참여 보고서에 표시되는 데이터는 일별(1일)입니다. 다른 간격으로 이 데이터를 보려면 보고서의 데이터를 집계할 명시적인 일수 또는 주수를 선택합니다. 따라서 일별 측정기준을 보는 대신 주별, 월별, 분기별 또는 유사한 기간별로 참여를 볼 수 있습니다. 시간 중심 집계가 충분하지 않은 경우 캠페인 또는 Canvas 수준에서 데이터를 내보내도록 선택할 수도 있습니다.

![engagement_reports_data_coverage]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

##### 전체 Campaign 또는 Canvas별 데이터 표시 {#show-data-by-entire-campaign-or-canvas}

**전체 Campaign 또는 Canvas별 데이터 표시**를 선택하면 Braze가 보고서의 기간 범위에 걸쳐 1,825일(5년) 단위로 측정기준을 집계합니다.

기간 범위가 하나 이상의 단위를 포함하는 경우, 동일한 캠페인 또는 Canvas에 대해 날짜 열에 서로 다른 날짜가 있는 여러 행이 표시될 수 있습니다. 일부 행에는 범위 후반에 기록된 측정기준만 포함될 수 있습니다(예: 탈퇴). 또한 워크스페이스에서 발송을 시작하기 수년 전의 날짜가 표시될 수 있는데, 이는 첫 번째 발송 시점만이 아니라 내보내기의 단위 경계를 반영하기 때문입니다.

날짜 열을 선택한 Campaigns 및 Canvases가 실제로 발송된 시점과 맞추려면 보고서의 [**기간 선택**에서 시작 날짜](#select-time-frame)를 파일에 포함하려는 가장 이른 날짜(일반적으로 해당 메시지가 발송되기 시작한 시점)로 설정하세요. 가장 오래된 선택 메시지까지 거슬러 올라가는 기본 범위를 그대로 두지 마세요.

#### 보고서 예약 {#schedule-your-report}

보고서를 예약할 때 두 가지 옵션이 있습니다:

- **즉시 발송:** 보고서가 시작된 후 Braze가 이 보고서를 즉시 발송합니다.
- **지정된 시간에 발송:** 이 옵션을 사용하면 이 보고서를 받는 빈도를 유연하게 선택할 수 있습니다. 설정된 일수, 주수 또는 월수마다 이 보고서를 발송하도록 선택할 수 있습니다. 보고서 발송을 중지할 시점도 정의할 수 있습니다.

![engagement_reports_schedule_report]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### 5단계: 검토 및 시작 {#step-5-review-and-launch}

보고서 설정의 마지막 단계에서는 구성된 옵션의 읽기 전용 개요를 보여줍니다. 보고서를 검토하고 만족스러우면 **보고서 시작**을 선택합니다.

### 6단계: 이메일 확인 {#step-6-check-your-email}

선택한 시간 또는 스케줄에 따라 보고서 링크가 포함된 이메일을 받게 됩니다. **이 링크는 보고서가 발송된 후 1시간이 지나면 만료됩니다.** 제공된 링크를 선택하면 CSV 파일이 포함된 ZIP 파일이 자동으로 다운로드됩니다. 하나는 모든 캠페인용입니다.

보고서에는 설정 과정의 [통계 추가](#add-statistics-to-your-reports) 섹션에서 선택한 모든 통계가 포함됩니다.

## 문제 해결 {#troubleshooting}

### 참여 보고서 측정기준이 이메일 성능 대시보드와 다른 경우 {#engagement-report-metrics-differ-from-the-email-performance-dashboard}

참여 보고서와 [이메일 성능 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance)는 동일한 이메일 측정기준 정의를 사용합니다. 둘 다 열람과 클릭을 각 이벤트가 **발생한** 날짜에 귀속시키며, *고유 열람*과 *고유 클릭*을 일별 7일 고유 수로 계산하여 선택한 날짜 범위에 걸쳐 합산합니다. 정의에 대해서는 [이메일 측정기준]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary) 및 채널 성능 대시보드 페이지의 [측정기준 계산 방법]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#how-metrics-are-calculated)을 참조하세요.

동일한 Campaigns 및 기간에 대해 합계가 여전히 다른 경우 다음을 확인하세요:

| 확인 사항 | 중요한 이유 |
| --- | --- |
| 날짜 범위 및 시간대 | 두 화면 모두 동일한 시간대에서 동일한 캘린더 일수를 포함해야 합니다. |
| Campaign 또는 Canvas 선택 | 이메일 성능 대시보드는 워크스페이스 전체의 이메일 활동을 집계합니다. 참여 보고서에는 선택한 Campaigns 또는 Canvases만 포함됩니다. |
| 일별 행 대 보고서 합계 | **데이터 표시**가 내보내기를 일별 행으로 분할하는 경우, 해당 행을 합산하여 동일한 범위의 대시보드 합계와 비교하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="참여 보고서 이메일 측정기준이 이메일 성능 대시보드와 다를 때 확인 사항" }

참여 보고서 수치를 이메일 성능 대시보드 대신 **Campaign** 또는 **Canvas** 분석과 비교할 때 차이가 더 자주 발생합니다. Campaign 및 Canvas 페이지에서는 발송 날짜 측정기준(예: 발송 날짜에 귀속된 발송 수 또는 전환)과 이벤트 날짜 열람 및 클릭이 함께 표시될 수 있습니다. [참여 보고서가 Canvas 또는 캠페인의 측정기준과 일치하지 않음](#engagement-report-doesnt-match-metrics-from-the-canvas-or-campaign)을 참조하세요.

### 참여 보고서가 Canvas 또는 캠페인의 측정기준과 일치하지 않음 {#engagement-report-doesnt-match-metrics-from-the-canvas-or-campaign}

#### 기간 불일치 {#mismatched-time-range}

참여 보고서의 날짜가 Canvas 또는 캠페인 분석의 날짜와 일치하는지 확인하세요(예: 둘 다 12월 1일~15일을 포함). Canvas가 한 번만 발송된 경우에도 마찬가지입니다. 참여 보고서 설정에서 **데이터 표시**를 확인하여 올바른 Canvas 또는 캠페인을 보고 있는지 확인합니다. **데이터 표시**가 *X*일마다 데이터를 표시하도록 설정된 경우, 각 단계에 대해 측정기준이 기록된 날짜별로 한 행씩 표시됩니다.

스프레드시트에서 합계가 잘못된 것처럼 보이면 내보내기에서 추가 필터를 지우세요. 일별 행을 합산하여 동일한 기간의 Canvas 또는 캠페인 합계와 대조할 수 있습니다.

{% alert note %}
일별, 주별 또는 기타 반복 버킷 대신 전체 캠페인 또는 Canvas별로 행을 집계하려면 **데이터 표시**를 **전체 Campaign 또는 Canvas별 데이터 표시**로 설정하세요. CSV에서 행 수나 날짜가 잘못된 것처럼 보이면 [전체 Campaign 또는 Canvas별 데이터 표시](#show-data-by-entire-campaign-or-canvas)를 참조하세요.
{% endalert %}

#### HTML 인앱 메시지의 중복 버튼 클릭 {#duplicate-button-clicks-in-html-in-app-messages}

HTML 인앱 메시지를 사용하고 참여 보고서에서 **본문 클릭 수**가 높게 나타나는 경우, 클릭 로깅이 두 번 실행되고 있을 수 있습니다. 예를 들어 일반 본문 클릭에 대해 `brazeBridge.logClick()`을 호출하고 동일한 인터랙션에서 `brazeBridge.logClick('body click')`(또는 다른 ID)도 호출하는 경우입니다. 마크업에서 `brazeBridge.logClick(`을 검색하고 컨트롤당 하나의 패턴으로 맞추세요. 권장 사용법은 [버튼 추적]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#button-tracking-improvements)을 참조하세요.

#### 이메일로 발송된 참여 보고서의 링크가 작동하지 않음 {#broken-links-in-emailed-engagement-reports}

예약된 참여 보고서 이메일의 링크가 메일 클라이언트에서 올바르게 열리지 않는 경우 다음 단계를 시도해 보세요:

1. 보고서를 Gmail 받은편지함으로 전달하고 Google Chrome에서 링크를 엽니다.
2. 참여 보고서 설정에서 **보고서 스케줄**이 예상대로 발송되도록 구성되어 있는지 확인합니다(예: 지연된 스케줄이 아닌 보고서가 생성된 직후 즉시 발송).