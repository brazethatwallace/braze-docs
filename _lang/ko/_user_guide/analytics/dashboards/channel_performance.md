---
nav_title: 채널 성과
article_title: 채널 성과 대시보드
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Campaign과 Canvas 전반에 걸쳐 전체 채널의 성과 측정기준을 확인할 수 있는 채널 성과 대시보드에 대해 설명합니다."
tool:
  - Reports
toc_headers: h2
---

# 채널 성과 대시보드 {#channel-performance-dashboards}

> 채널 성과 대시보드는 Campaign과 Canvas 전반에 걸쳐 전체 채널의 집계 성과 측정기준을 보여줍니다. 이 대시보드는 현재 이메일, 푸시, 단문 메시지 서비스에서 사용할 수 있습니다.

## 대시보드 {#dashboards}

사용 가능한 채널 성과 대시보드의 세부 정보를 보려면 탭을 선택하세요.

{% tabs %}
{% tab 이메일 성과 %}

### 이메일 성과 대시보드 {#email-performance-dashboard}

이메일 성과 대시보드를 보려면 **Analytics** > **Email Performance**로 이동한 후 데이터를 확인하려는 기간의 날짜 범위를 선택하세요. 날짜 범위는 최대 1년 전까지 설정할 수 있습니다.

{% alert note %}
**Email Performance** 대시보드를 보려면 "View Usage Data" 또는 "View Dashboard Reports" 권한이 필요합니다.
{% endalert %}

![지난 30일간의 이메일 채널 인게이지먼트를 표시하는 이메일 성과 대시보드.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![335,630건의 발송과 일 평균 11,187.667건의 발송을 보여주는 이메일 Campaign 예시.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### 측정기준 계산 방식 {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 발송 | 건수 | 날짜 범위 내 각 날의 총 발송 수 |
| 전달율 | 비율 | (날짜 범위 내 각 날의 총 전달 수) / (날짜 범위 내 각 날의 총 발송 수) |
| 반송률 | 비율 | (날짜 범위 내 각 날의 총 반송 수) / (날짜 범위 내 각 날의 총 발송 수) |
| 탈퇴율 | 비율 | (날짜 범위 내 각 날의 고유 탈퇴 수) / (날짜 범위 내 총 전달 수)<br><br>이는 Campaign Analytics, Overview 및 보고서 빌더에서도 사용되는 고유 탈퇴를 사용합니다. 이러한 탈퇴는 모든 소스(예: REST API, CSV 가져오기, 이메일, 목록 탈퇴)에서 기록됩니다. Campaign 및 Canvas 분석의 탈퇴율은 Braze가 전달한 이메일의 탈퇴 클릭으로 인해 발생하는 탈퇴입니다. |
| 고유 열람율 | 비율 | (날짜 범위 내 각 날의 총 고유 열람 수) / (날짜 범위 내 총 전달 수) |
| 기타 열람율 | 비율 | (날짜 범위 내 각 날의 총 기타 열람 수) / (날짜 범위 내 총 전달 수)<br><br>기타 열람에는 사용자가 이메일을 열었을 때처럼 기계 열람으로 식별되지 않은 이메일이 포함됩니다. 이 측정기준은 고유하지 않으며 총 열람의 하위 측정기준입니다. |
| 고유 클릭률 | 비율 | (날짜 범위 내 각 날의 총 고유 클릭 수) / (날짜 범위 내 총 전달 수) |
| 고유 클릭 대비 열람율 | 비율 | (날짜 범위 내 각 날의 총 고유 클릭 수) / (날짜 범위 내 각 날의 총 고유 열람 수) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="측정기준 계산 방식" }

{% endtab %}
{% tab 이메일 인사이트 %}

### 이메일 인사이트 대시보드 {#email-insights-dashboard}

이메일 인사이트 대시보드는 고객이 이메일과 상호 작용하는 위치와 시점을 추적합니다. 이러한 보고서는 더 높은 인게이지먼트를 이끌어내기 위해 이메일을 최적화하는 방법에 대한 풍부하고 세분화된 데이터를 제공할 수 있습니다. 이메일 인사이트 대시보드에는 최대 6개월간의 데이터가 포함됩니다. 대시보드에 접근하려면 **Analytics** > **Email Performance** > **Email Insights**로 이동하세요.

#### 기기별 인게이지먼트 {#engagement-by-device}

**기기별 인게이지먼트** 보고서는 사용자가 이메일과 상호 작용하는 데 사용하는 기기의 분류를 제공합니다. 이 데이터는 모바일, 데스크톱, 태블릿 및 기타 기기 유형별 이메일 인게이지먼트를 추적합니다. 이 데이터는 사용자 기기에서 전달되는 사용자 에이전트 문자열을 기반으로 합니다.

{% alert note %}
CDN으로 CloudFront를 사용하는 경우, 사용자의 사용자 에이전트가 ESP로 전달되는지 확인하세요. 그렇지 않으면 모든 사용자 에이전트가 "Amazon Cloudfront"로 표시됩니다.
{% endalert %}

"기타" 카테고리에는 데스크톱, 모바일 또는 태블릿으로 식별할 수 없는 사용자 문자열이 포함됩니다. 예를 들어 텔레비전, 자동차, 비디오 게임 콘솔, OTT(오버더탑 또는 스트리밍) 등이 포함됩니다. 또한 null이나 빈 값도 포함될 수 있습니다.

이 "기타" 카테고리에 포함된 내용을 더 잘 이해하려면 다음 옵션 중 하나를 사용하여 사용자 에이전트를 추출할 수 있습니다:

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)를 통해 사용자 기기에서 검색된 정확한 사용자 에이전트 문자열을 수신할 수 있습니다.
2. [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)를 활용하여 SQL을 사용하거나 [AI 쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder)를 사용하여 사용자 에이전트를 확인할 수 있습니다.

![모바일, 데스크톱, 태블릿, 기타 기기의 클릭 수를 보여주는 기기별 인게이지먼트 보고서. 모바일 기기에서 가장 많은 클릭이 발생합니다.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

이메일 열람의 경우 Braze는 Google Image Proxy, Apple Image Proxy, Yahoo Mail Proxy를 분리합니다. 이러한 서비스는 이메일에 포함된 모든 이미지를 수신자에게 전달하기 전에 캐시하고 로드합니다. 따라서 수신자의 서버가 아닌 메일함 제공자의 서버에서 이메일 열람이 트리거되어 이메일 열람 수가 부풀려질 수 있습니다. 이러한 서비스는 이미지 로딩 시 개인정보 보호, 보안, 성능 및 효율성을 향상시키기 위한 것입니다. 프록시 서비스가 사용자 에이전트를 마스킹하고 Braze가 사용자 에이전트를 사용하여 프록시 데이터를 분류하므로, 이 데이터에는 수신자의 실제 열람도 포함될 수 있습니다.

![모바일, 데스크톱, 태블릿, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy, 기타의 클릭 수를 보여주는 기기별 인게이지먼트 보고서. 모바일 기기에서 가장 많은 열람이 발생합니다.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### 메일함 제공자별 인게이지먼트 {#engagement-by-mailbox-provider}

**메일함 제공자별 인게이지먼트** 보고서는 클릭 또는 열람에 기여하는 상위 메일함 제공자를 표시합니다. 특정 주요 메일함 제공자를 클릭하면 특정 수신 도메인에 대해 상세히 확인할 수 있습니다. 예를 들어 이 보고서에서 Microsoft가 상위 메일함 제공자 측정기준 중 하나로 나열된 경우, "outlook.com", "hotmail.com", "live.com" 등의 수신 도메인에 대한 세부 정보를 추가로 확인할 수 있습니다.

![Google, Apple iCloud, Yahoo, Microsoft, Mail.Ru Group과 해당 클릭 수를 보여주는 메일함 제공자별 인게이지먼트 보고서 예시.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### 인게이지먼트 시간 {#time-of-engagement}

**인게이지먼트 시간** 보고서는 사용자가 이메일과 상호 작용하는 시점에 대한 데이터를 표시합니다. 이를 통해 어떤 요일이나 시간대에 고객으로부터 가장 높은 인게이지먼트가 발생하는지 등의 질문에 답할 수 있습니다. 이러한 인사이트를 활용하면 더 높은 인게이지먼트를 이끌어내기 위해 메시지를 보내기 가장 좋은 요일이나 시간을 실험해 볼 수 있습니다. 이 시간은 회사의 시간대를 기준으로 합니다.

**요일별** 인게이지먼트 보고서는 요일별 열람 또는 클릭을 분류합니다.

![월요일과 수요일에 가장 많은 클릭이 발생하는 요일별 인게이지먼트 보고서 예시.]({% image_buster /assets/img_archive/time_engagement.png %})

**시간대별** 인게이지먼트 보고서는 24시간 시간 창에서 각 시간별 열람 또는 클릭을 분류합니다.

![오전 12시부터 오후 11시까지의 열람 또는 클릭을 보여주는 시간대별 인게이지먼트 보고서 예시.]({% image_buster /assets/img_archive/time_engagement_day.png %})

이메일 분석에 대한 자세한 내용은 [이메일 리포팅]({{site.baseurl}}/user_guide/channels/email/reporting)을 확인하세요.

{% endtab %}
{% tab 단문 메시지 서비스 성과 %}

### 단문 메시지 서비스 성과 대시보드 {#sms-performance-dashboard}

단문 메시지 서비스 성과 대시보드를 사용하려면 **Analytics** > **단문 메시지 서비스 Performance**로 이동한 후 데이터를 확인하려는 기간의 날짜 범위를 선택하세요. 날짜 범위는 최대 1년 전까지 설정할 수 있습니다.

![335,630건의 발송과 일 평균 11,187.667건의 발송을 보여주는 단문 메시지 서비스 Campaign 예시.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### 측정기준 계산 방식

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="단문 메시지 서비스" %}

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 발송 | 건수 | 날짜 범위 내 각 날의 총 발송 수 |
| 확인된 전달율 | 비율 | (날짜 범위 내 각 날의 총 전달 수) / (날짜 범위 내 각 날의 총 발송 수) |
| 전달 실패율 | 비율 | (날짜 범위 내 각 날의 총 실패 수) / (날짜 범위 내 각 날의 총 발송 수) |
| 거부율 | 비율 | (날짜 범위 내 각 날의 총 거부 수) / (날짜 범위 내 각 날의 총 발송 수) |
| 클릭률 | 비율 | (날짜 범위 내 각 날의 총 클릭 수) / (날짜 범위 내 각 날의 총 전달 수) |
| 총 옵트인 | 비율 | 날짜 범위 내 각 날의 인바운드 메시지 옵트인 총 수 |
| 총 옵트아웃 | 비율 | 날짜 범위 내 각 날의 인바운드 메시지 옵트아웃 총 수 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="측정기준 계산 방식" }

{% endtab %}
{% tab 푸시 성과 %}

### 푸시 성과 대시보드 {#push-performance-dashboard}

**Push Performance** 대시보드는 모든 Campaign 및 Canvases에서의 푸시 인게이지먼트에 대한 채널 수준의 뷰를 제공하므로, 개별 메시지의 데이터를 합산하지 않고도 채널의 상태를 파악할 수 있습니다.

대시보드를 열려면 **Analytics** > **Push Performance**로 이동한 후 데이터를 확인하려는 기간의 날짜 범위를 선택하세요. 날짜 범위는 최대 1년 전까지 설정할 수 있습니다.

![지난 30일간의 푸시 채널 인게이지먼트를 표시하는 푸시 성과 대시보드.]({% image_buster /assets/img_archive/push_performance_dashboard_performance_tab.png %})

#### 개요 {#overview}

개요 배너는 선택한 날짜 범위에 대한 네 가지 주요 측정기준(*발송*, *전달율*, *열람율*, *전환율*)을 요약합니다. 각 타일에는 기본 값, 지원 건수, 추가 통계 세부 정보가 포함된 툴팁이 표시됩니다.

이 대시보드의 전환율은 주요 전환 이벤트만을 대상으로 합니다. 2차 전환 이벤트를 분석하려면 [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder)를 사용하세요.

#### 시간별 인게이지먼트 {#engagement-over-time}

시간별 인게이지먼트 섹션에서는 선택한 날짜 범위에 걸쳐 각 측정기준이 라인 차트로 표시됩니다:

- 발송
- 총 열람
- 직접 열람
- 영향받은 열람
- 직접 열람율
- 전환율
- 반송

직접 열람율 차트에 업계 벤치마크를 토글할 수 있습니다. 벤치마크는 기본적으로 꺼져 있습니다. 자세한 내용은 [벤치마킹](#benchmarking)을 참조하세요.

#### 측정기준 계산 방식

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 발송 | 건수 | 날짜 범위 내 각 날의 총 발송 수 |
| 전달율 | 비율 | (날짜 범위 내 각 날의 총 전달 수) / (날짜 범위 내 각 날의 총 발송 수) |
| 반송률 | 비율 | (날짜 범위 내 각 날의 총 반송 수) / (날짜 범위 내 각 날의 총 발송 수) |
| 직접 열람율 | 비율 | (날짜 범위 내 각 날의 총 직접 열람 수) / (날짜 범위 내 각 날의 총 전달 수) |
| 영향받은 열람율 | 비율 | (날짜 범위 내 각 날의 총 영향받은 열람 수) / (날짜 범위 내 각 날의 총 전달 수) |
| 총 열람율 | 비율 | (날짜 범위 내 각 날의 총 열람 수) / (날짜 범위 내 각 날의 총 전달 수)<br><br>총 열람에는 직접 열람과 영향받은 열람이 모두 포함됩니다. |
| 전환율 | 비율 | (날짜 범위 내 각 날의 총 주요 전환 수) / (날짜 범위 내 각 날의 총 수신자 수) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="측정기준 계산 방식" }

{% endtab %}
{% tab 푸시 인사이트 %}

### 푸시 인사이트 대시보드 {#push-insights-dashboard}

푸시 인사이트 대시보드는 오디언스가 푸시에 어떻게 반응하는지에 대한 패턴을 보여주므로, 발송 내용과 빈도를 조정할 수 있습니다. 접근하려면 **Analytics** > **Push Performance** > **Insights**로 이동하세요.

#### 빈도 {#frequency}

빈도 보고서는 사용자가 수신하는 푸시 알림 수와 열람율 간의 관계를 보여주므로, 추가 발송이 더 이상 인게이지먼트를 얻지 못하는 시점을 찾을 수 있습니다. 차트는 해당 업종의 벤치마크 데이터를 기반으로 권장 발송량을 강조 표시합니다.

{% alert important %}
빈도 및 케이던스 보고서는 최소 3개월의 분석 기간을 사용합니다. 더 짧은 날짜 범위를 선택하면 Braze가 사용 가능한 경우 최대 3개월의 데이터를 포함하도록 시작 날짜를 확장할 수 있습니다. 이 보고서는 태그, Campaign, Canvas 또는 플랫폼 필터의 영향을 받지 않으며, 선택한 날짜 범위의 전체 푸시 볼륨을 항상 반영합니다.
{% endalert %}

#### 케이던스 {#cadence}

빈도 보고서가 몇 개의 메시지를 보낼지 알려준다면, 케이던스 보고서는 그 메시지를 어떻게 배분할지 알려줍니다. 이 보고서는 발송 케이던스에 따른 열람율을 플로팅하여, 발송을 몰아서 보내는 것(예: 푸시 3건이 모두 주말에 도착)이 일주일에 걸쳐 분산하는 것에 비해 인게이지먼트를 떨어뜨리는지 확인할 수 있습니다.

빈도 보고서와 함께 사용하세요: 빈도로 볼륨 목표를 설정하고, 케이던스로 배분을 설정합니다.

#### Campaign 성과 분포 {#campaign-performance-distribution}

이 보고서는 날짜 범위 내의 모든 푸시 Campaign을 열람율과 전환율로 플로팅하여, 가장 우수한 성과와 가장 약한 성과를 나란히 확인하고 공통점을 찾을 수 있습니다.

Campaign 성과 분포 차트에서 점 세 개 아이콘을 클릭하고 **데이터 테이블 보기**를 선택하면 동일한 Campaign이 나열된 정렬 가능한 테이블이 표시됩니다. 열람율 또는 전환율로 정렬하여 순위를 매길 수 있으며, 이를 사용하여 개별 Campaign의 분석을 열 수 있습니다.

{% endtab %}
{% tab 푸시 전달 가능성 %}

### 푸시 전달 가능성 대시보드 {#push-deliverability-dashboard}

푸시 전달 가능성 대시보드는 시간 경과에 따른 푸시 오디언스의 상태를 추적하여 메시징이 도달 가능한 기반에 어떤 영향을 미치는지 확인할 수 있습니다. 접근하려면 **Analytics** > **Push Performance** > **Deliverability**로 이동하세요.

이 대시보드는 날짜 범위로만 필터링되며, 각 측정기준은 플랫폼별로 분류됩니다.

#### 반송률 {#bounce-rate}

선택한 날짜 범위에서의 반송이 플랫폼별로 분류됩니다. 이 차트에 업계 벤치마크를 토글할 수 있습니다. 기본적으로 꺼져 있습니다.

#### 제거율 {#uninstall-rate}

선택한 날짜 범위에서의 제거가 플랫폼별로 분류됩니다. 대량 발송 기간이 사용자 이탈과 겹쳤는지 확인하는 데 사용하세요. 제거 데이터는 제거 추적 설정에 따라 달라집니다. [제거 추적]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)을 참조하세요. 제거 추적은 iOS, Android(Huawei 제외) 및 Kindle에서 지원됩니다. 제거 추적이 꺼져 있으면 제거율 데이터의 완성도가 낮아지고 정확도가 떨어질 수 있습니다. 운영 체제에 따라 제거 보고서가 늦게 도착하거나 일괄적으로 도착할 수 있으므로, 차트에 정확한 제거 날짜가 반영되지 않을 수 있습니다.

#### 측정기준 계산 방식

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 제거율 | 비율 | (날짜 범위 내 각 날에 Braze가 제거 신호를 수신한 총 기기 수) / (날짜 범위 내 각 날의 유효한 토큰을 가진 총 기기 수) |
| 반송률 | 비율 | (날짜 범위 내 각 날의 총 반송 수) / (날짜 범위 내 각 날의 총 발송 수) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="측정기준 계산 방식" }

{% endtab %}
{% endtabs %}

## 대시보드 필터 {#dashboard-filters}

다음 필터 옵션을 사용하여 대시보드의 데이터를 필터링할 수 있습니다:

- **태그:** 태그 하나를 선택합니다. 적용하면 대시보드에 선택한 태그에 해당하는 측정기준만 표시됩니다. 푸시 대시보드는 여러 태그를 지원합니다.
- **플랫폼:** (푸시 대시보드만 해당) **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** 또는 **Web**과 같은 푸시 플랫폼을 선택합니다. 적용하면 대시보드에 선택한 플랫폼에 해당하는 측정기준만 표시됩니다.
- **Canvas:** 최대 10개의 Canvas를 선택합니다. 적용하면 대시보드에 선택한 Canvases에 해당하는 측정기준만 표시됩니다. 태그 필터를 먼저 선택한 경우, Canvas 필터 옵션에는 선택한 태그가 포함된 Canvases만 표시됩니다.
- **Campaign:** 최대 10개의 Campaigns를 선택합니다. 적용하면 대시보드에 선택한 Campaigns에 해당하는 측정기준만 표시됩니다. 태그 필터를 먼저 선택한 경우, Campaign 필터 옵션에는 선택한 태그가 포함된 Campaigns만 표시됩니다.

{% alert note %}
필터는 푸시 대시보드마다 다르게 적용됩니다. 푸시 성능 대시보드는 모든 필터를 지원합니다. 푸시 전달 가능성 대시보드는 날짜 범위만 지원하며, 각 차트에 플랫폼별 분류가 표시됩니다. 푸시 인사이트 대시보드의 빈도 및 케이던스 보고서는 날짜 범위만 지원합니다.
{% endalert %}

![태그를 선택하고 Canvases 목록으로 필터링할 수 있는 채널 성능 대시보드의 필터 옵션]({% image_buster /assets/img_archive/dashboard_filters.png %})

## 기간 비교 {#comparing-time-periods}

채널 성능 대시보드는 날짜 범위에서 선택한 기간과 동일한 일수의 이전 기간을 자동으로 비교합니다. 예를 들어, 대시보드에서 날짜 범위로 "지난 7일"을 선택하면, 지난 7일간의 측정기준을 그 이전 7일간의 측정기준과 비교합니다. 커스텀 날짜 범위(예: 5월 10일~5월 15일, 총 6일 분량의 데이터)를 선택하면, 대시보드는 해당 기간의 측정기준을 5월 4일~5월 9일의 측정기준과 비교합니다.

비교 값은 이전 기간과 현재 기간 사이의 변화율(%)이며, 두 기간의 차이를 이전 기간의 측정기준으로 나누어 계산합니다.

### 총 수치 변화와 비율 변화 확인 {#viewing-changes-in-total-counts-and-rates}

**Show Change in Totals**(두 기간 사이의 총 수치, 예: 이메일 전달 수 비교)와 **Show Change in Rates**(비율, 예: 전달률 비교) 간에 전환할 수 있습니다.

![채널 성능 대시보드에서 총 수치 변화 또는 비율 변화 표시를 전환하는 라디오 버튼.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## 벤치마킹 {#benchmarking}

푸시 대시보드에서 Braze의 집계된 익명 데이터를 기준으로 성능을 비교할 수 있습니다.

### 사용 가능한 벤치마크 {#available-benchmarks}

| 벤치마크 | 표시 위치 | 기본값 |
| --- | --- | ---- |
| 직접 열람율 | 푸시 성능 | 꺼짐 |
| 반송률 | 푸시 전달 가능성 | 꺼짐 |
| 빈도 | 푸시 인사이트 | 켜짐 |
| 케이던스 | 푸시 인사이트 | 켜짐 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용 가능한 벤치마크" }

직접 열람율 및 반송률 벤치마크는 플랫폼별로 구분됩니다. 모든 푸시 벤치마크는 전환율이 아닌 열람율을 기준으로 측정됩니다.

### 업종 비교 {#comparing-verticals}

벤치마크 데이터는 업종별로 구분됩니다. 대시보드는 기본적으로 계정의 업종으로 설정되며, 드롭다운을 사용하여 다른 업종과 비교할 수 있습니다.

### 지역 비교 {#comparing-regions}

벤치마크 데이터는 지역별로 구분됩니다. 대시보드는 기본적으로 계정의 지역으로 설정되며, 드롭다운을 사용하여 다른 지역과 비교할 수 있습니다.

{% alert note %}
선택한 기간에 대한 최신 벤치마크 데이터를 사용할 수 없는 경우, Braze는 예측 벤치마크를 표시합니다.

벤치마크 데이터는 매월 갱신됩니다.
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 대시보드에 빈 값이 표시되는 이유는 무엇인가요? {#why-is-my-dashboard-displaying-empty-values}

측정기준에 빈 값이 표시되는 몇 가지 시나리오가 있습니다:

- 선택한 날짜 범위에서 Braze가 해당 측정기준에 대해 0을 기록했습니다.
- 선택한 날짜 범위 동안 메시지를 보내지 않았습니다.
- 선택한 날짜 범위에 열람, 클릭 또는 탈퇴와 같은 측정기준이 있었지만 전달 또는 발송이 없었습니다. 이 경우 Braze는 비율 측정기준을 계산하지 않습니다.

더 많은 측정기준을 확인하려면 날짜 범위를 확장해 보세요.

### 이메일 대시보드에 고유 열람보다 기타 열람이 더 많이 표시되는 이유는 무엇인가요? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

*고유 열람* 측정기준의 경우, Braze는 특정 사용자가 등록한 반복 열람(*머신 열람* 또는 *기타 열람* 포함)을 중복 제거하여, 사용자가 여러 번 열어도 하나의 *고유 열람*만 증가합니다. *기타 열람*의 경우, Braze는 중복 제거를 하지 않습니다.

### 빈도 및 발송 주기 보고서가 비어 있는 이유는 무엇인가요? {#why-are-my-frequency-and-cadence-reports-empty}

이 보고서는 3개월 분석 기간을 사용합니다. 선택한 범위가 더 짧은 경우, Braze는 데이터가 있는 이전 날짜를 포함하도록 범위를 확장할 수 있습니다.

날짜 범위가 충분히 길고 보고서가 여전히 비어 있는 경우, 워크스페이스에 대한 벤치마크 데이터가 아직 제공되지 않을 수 있습니다. 질문이 있으시면 Braze 지원팀에 문의하세요.

### 필터를 변경해도 빈도 및 발송 주기 보고서가 변경되지 않는 이유는 무엇인가요? {#why-dont-my-filters-change-the-frequency-and-cadence-reports}

빈도 및 발송 주기 보고서는 항상 전체 푸시 볼륨을 반영합니다. 이 보고서의 가치는 사용자에게 전달되는 총 메시지 부하를 측정하는 데 있기 때문입니다. Campaigns의 하위 집합으로 필터링하면 해당 사용자가 실제로 수신한 메시지 수가 과소 집계됩니다. 날짜 범위 필터만 적용됩니다.
<!---Temporarily hidden until functionality is added

## 데이터의 빈 값 {#empty-values-in-your-data}

### 측정기준이 "0%" 또는 "0"으로 표시되는 경우 {#if-a-metric-displays-0-or-0}

이는 선택한 기간 동안 해당 측정기준에 대해 Braze가 0을 기록했음을 의미합니다.

#### 측정기준이 "N/A"로 표시되는 경우 {#if-a-metric-displays-na}

이는 선택한 기간 동안 특정 측정기준에 대해 Braze가 긍정적 카운트를 기록했지만, 비율 계산의 분모(대부분의 경우 발송 수 또는 전달 수)가 0이었음을 의미합니다. 이메일이 특정 날짜에 발송되고 열람 및 클릭이 그 이후 날짜에 기록되었을 때, 선택한 기간에 메시지가 발송된 날짜가 포함되지 않은 경우 이러한 현상이 발생할 수 있습니다.

#### 측정기준이 "--"로 표시되는 경우 {#if-a-metric-displays}

이는 선택한 기간 동안 해당 측정기준에 대해 Braze가 데이터를 기록하지 않았음을 의미합니다. 아직 이메일을 설정하거나 발송하지 않은 경우, 전용 [이메일]({{site.baseurl}}/user_guide/channels/email) 섹션에서 자세한 방법을 알아보세요.