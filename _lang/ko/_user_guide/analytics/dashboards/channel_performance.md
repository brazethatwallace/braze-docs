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

> 채널 성과 대시보드는 Campaign과 Canvas 전반에 걸쳐 전체 채널의 집계 성과 측정기준을 보여줍니다. 이 대시보드는 현재 이메일, 푸시, SMS에서 사용할 수 있습니다.

## 대시보드 {#dashboards}

탭을 선택하여 사용 가능한 채널 성능 대시보드의 세부 정보를 확인하세요.

{% tabs %}
{% tab 이메일 성능 %}

### 이메일 성능 대시보드 {#email-performance-dashboard}

이메일 성능 대시보드를 보려면 **Analytics** > **Email Performance**로 이동하여 데이터를 확인할 기간의 날짜 범위를 선택합니다. 날짜 범위는 최대 1년 전까지 설정할 수 있습니다.

{% alert note %}
**Email Performance** 대시보드를 보려면 "View Usage Data" 또는 "View Dashboard Reports" 권한이 필요합니다.
{% endalert %}

![지난 30일간의 이메일 채널 인게이지먼트를 표시하는 이메일 성능 대시보드.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![335,630건의 발송과 일 평균 11,187.667건을 보여주는 이메일 Campaign 예시.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### 측정기준 계산 방법 {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 발송 | 횟수 | 날짜 범위 내 각 일자의 총 발송 수 |
| 전달율 | 비율 | (날짜 범위 내 각 일자의 총 전달 수) / (날짜 범위 내 각 일자의 총 발송 수) |
| 반송률 | 비율 | (날짜 범위 내 각 일자의 총 반송 수) / (날짜 범위 내 각 일자의 총 발송 수) |
| 탈퇴율 | 비율 | (날짜 범위 내 각 일자의 고유 탈퇴 수) / (날짜 범위 내 총 전달 수)<br><br>이 값은 고유 탈퇴를 사용하며, Campaign 분석, 개요, 보고서 빌더에서도 동일하게 사용됩니다. 이러한 탈퇴는 모든 소스(예: 대시보드, REST API, CSV 가져오기, 이메일, 목록 탈퇴)에서 기록됩니다. Campaign 및 Canvas 분석의 탈퇴율은 Braze가 전달한 이메일에서 탈퇴 클릭으로 인해 발생한 탈퇴입니다. |
| 고유 열람율 | 비율 | (날짜 범위 내 각 일자의 고유 열람 수) / (날짜 범위 내 총 전달 수) |
| 기타 열람율 | 비율 | (날짜 범위 내 각 일자의 총 기타 열람 수) / (날짜 범위 내 총 전달 수)<br><br>기타 열람에는 사용자가 이메일을 열 때와 같이 기계 열람으로 식별되지 않은 이메일이 포함됩니다. 이 측정기준은 고유하지 않으며 총 열람의 하위 측정기준입니다. |
| 고유 클릭률 | 비율 | (날짜 범위 내 각 일자의 고유 클릭 수) / (날짜 범위 내 총 전달 수) |
| 고유 클릭 대비 열람율 | 비율 | (날짜 범위 내 각 일자의 고유 클릭 수) / (날짜 범위 내 각 일자의 고유 열람 수) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="측정기준 계산 방법" }

{% endtab %}
{% tab 이메일 인사이트 %}

### 이메일 인사이트 대시보드 {#email-insights-dashboard}

이메일 인사이트 대시보드는 고객이 이메일과 상호작용하는 위치와 시간을 추적합니다. 이 보고서는 더 높은 인게이지먼트를 유도하기 위해 이메일을 최적화하는 방법에 대한 풍부하고 세분화된 데이터를 제공할 수 있습니다. 이메일 인사이트 대시보드에는 최대 6개월간의 데이터가 포함됩니다. 대시보드에 접근하려면 **Analytics** > **Email Performance** > **Email Insights**로 이동합니다.

#### 기기별 인게이지먼트 {#engagement-by-device}

**기기별 인게이지먼트** 보고서는 사용자가 이메일에 참여할 때 사용하는 기기의 분류를 제공합니다. 이 데이터는 모바일, 데스크톱, 태블릿 및 기타 기기 유형에 걸친 이메일 인게이지먼트를 추적합니다. 이 데이터는 사용자 기기에서 전달되는 사용자 에이전트 문자열을 기반으로 합니다.

{% alert note %}
CDN으로 CloudFront를 사용하는 경우, 사용자의 사용자 에이전트가 ESP로 전달되는지 확인하세요. 그렇지 않으면 모든 사용자 에이전트가 "Amazon Cloudfront"로 표시됩니다.
{% endalert %}

"기타" 카테고리에는 데스크톱, 모바일 또는 태블릿으로 식별할 수 없는 모든 사용자 문자열이 포함됩니다. 예를 들어 텔레비전, 자동차, 비디오 게임 콘솔, OTT(오버더톱 또는 스트리밍) 등이 있습니다. 여기에는 null 또는 빈 값도 포함될 수 있습니다.

이 "기타" 카테고리에 포함된 내용을 더 잘 이해하려면 다음 옵션 중 하나를 사용하여 사용자 에이전트를 추출할 수 있습니다:

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)를 사용하면 사용자 기기에서 검색된 정확한 사용자 에이전트 문자열을 받을 수 있습니다.
2. [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)를 활용하여 SQL을 사용하거나 [AI 쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder)를 사용하여 사용자 에이전트를 확인할 수 있습니다.

![모바일, 데스크톱, 태블릿 및 기타 기기의 클릭 수를 보여주는 기기별 인게이지먼트 보고서. 가장 많은 클릭이 모바일 기기에서 발생합니다.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

이메일 열람의 경우, Braze는 Google Image Proxy, Apple Image Proxy, Yahoo Mail Proxy를 분리합니다. 이러한 서비스는 이메일이 수신자에게 전달되기 전에 모든 임베디드 이미지를 캐시하고 로드합니다. 그 결과 수신자의 서버가 아닌 메일박스 공급자의 서버에서 이메일 열람이 트리거되어 이메일 열람 수가 부풀려질 수 있습니다. 이러한 서비스는 이미지 로딩 시 개인정보 보호, 보안, 성능 및 효율성을 향상시키기 위한 것입니다. 이 프록시 서비스가 사용자 에이전트를 마스킹하고 Braze가 사용자 에이전트를 사용하여 프록시 데이터를 분류하기 때문에, 수신자의 실제 열람도 포함될 수 있습니다.

![모바일, 데스크톱, 태블릿, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy 및 기타의 클릭 수를 보여주는 기기별 인게이지먼트 보고서. 가장 많은 열람이 모바일 기기에서 발생합니다.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### 메일박스 공급자별 인게이지먼트 {#engagement-by-mailbox-provider}

**메일박스 공급자별 인게이지먼트** 보고서는 클릭 또는 열람에 기여하는 상위 메일박스 공급자를 표시합니다. 특정 주요 메일박스 공급자를 클릭하여 특정 수신 도메인을 자세히 확인할 수 있습니다. 예를 들어 이 보고서에 Microsoft가 상위 메일박스 공급자 측정기준 중 하나로 나열된 경우, "outlook.com", "hotmail.com", "live.com" 등의 수신 도메인에 대한 세부 정보를 추가로 확인할 수 있습니다.

![Google, Apple iCloud, Yahoo, Microsoft, Mail.Ru Group과 해당 클릭 수를 보여주는 메일박스 공급자별 인게이지먼트 보고서 예시.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### 인게이지먼트 시간 {#time-of-engagement}

**인게이지먼트 시간** 보고서는 사용자가 이메일에 참여하는 시간에 대한 데이터를 표시합니다. 이를 통해 어떤 요일이나 시간대에 고객의 인게이지먼트가 가장 높은지와 같은 질문에 답할 수 있습니다. 이러한 인사이트를 활용하여 더 높은 인게이지먼트를 유도하기 위해 메시지를 보내기에 가장 좋은 요일이나 시간을 실험해 볼 수 있습니다. 이 시간은 회사의 시간대를 기준으로 합니다.

**요일별** 인게이지먼트 보고서는 요일별 열람 또는 클릭을 분류합니다.

![월요일과 수요일에 가장 많은 클릭이 발생한 요일별 인게이지먼트 보고서 예시.]({% image_buster /assets/img_archive/time_engagement.png %})

**시간대별** 인게이지먼트 보고서는 24시간 시간대에서 각 시간별 열람 또는 클릭을 분류합니다.

![오전 12시부터 오후 11시까지의 열람 또는 클릭을 보여주는 시간대별 인게이지먼트 보고서 예시.]({% image_buster /assets/img_archive/time_engagement_day.png %})

이메일 분석에 대한 자세한 내용은 [이메일 보고]({{site.baseurl}}/user_guide/channels/email/reporting)를 확인하세요.

{% endtab %}
{% tab SMS 성능 %}

### SMS 성능 대시보드 {#sms-performance-dashboard}

SMS 성능 대시보드를 사용하려면 **Analytics** > **SMS Performance**로 이동하여 데이터를 확인할 기간의 날짜 범위를 선택합니다. 날짜 범위는 최대 1년 전까지 설정할 수 있습니다.

![335,630건의 발송과 일 평균 11,187.667건을 보여주는 SMS Campaign 예시.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### 측정기준 계산 방법

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 발송 | 횟수 | 날짜 범위 내 각 일자의 총 발송 수 |
| 확인된 전달율 | 비율 | (날짜 범위 내 각 일자의 총 전달 수) / (날짜 범위 내 각 일자의 총 발송 수) |
| 전달 실패율 | 비율 | (날짜 범위 내 각 일자의 총 실패 수) / (날짜 범위 내 각 일자의 총 발송 수) |
| 거부율 | 비율 | (날짜 범위 내 각 일자의 총 거부 수) / (날짜 범위 내 각 일자의 총 발송 수) |
| 클릭률 | 비율 | (날짜 범위 내 각 일자의 총 클릭 수) / (날짜 범위 내 각 일자의 총 전달 수) |
| 총 옵트인 | 비율 | 날짜 범위 내 각 일자의 총 인바운드 메시지 옵트인 수 |
| 총 옵트아웃 | 비율 | 날짜 범위 내 각 일자의 총 인바운드 메시지 옵트아웃 수 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="측정기준 계산 방법" }

{% endtab %}
{% tab 푸시 성능 %}

### 푸시 성능 대시보드 {#push-performance-dashboard}

**푸시 성능** 대시보드는 발송, 반송, 전달, 직접 열람, 영향받은 열람 및 총 열람율을 포함한 푸시 인게이지먼트의 단일 채널 수준 뷰를 제공합니다. 이를 사용하여 개별 Campaign이나 Canvases의 데이터를 집계하지 않고도 푸시 채널의 전반적인 상태를 파악할 수 있습니다.

대시보드를 열려면 **Analytics** > **Dashboard Builder**로 이동한 다음 **Push Channel Dashboard**를 선택합니다. 날짜 범위는 최대 1년 전까지 설정할 수 있습니다.

![6,300만 건 이상의 발송을 보여주는 푸시 Campaign 예시.]({% image_buster /assets/img_archive/push_performance_dashboard.png %})

#### 측정기준 계산 방법

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 발송 | 횟수 | 날짜 범위 내 각 일자의 총 발송 수 |
| 반송률 | 비율 | (날짜 범위 내 각 일자의 총 반송 수) / (날짜 범위 내 각 일자의 총 발송 수) |
| 전달율 | 비율 | (날짜 범위 내 각 일자의 총 전달 수) / (날짜 범위 내 각 일자의 총 발송 수) |
| 직접 열람율 | 비율 | (날짜 범위 내 각 일자의 총 직접 열람 수) / (날짜 범위 내 각 일자의 총 전달 수) |
| 영향받은 열람율 | 비율 | (날짜 범위 내 각 일자의 총 영향받은 열람 수) / (날짜 범위 내 각 일자의 총 전달 수) |
| 총 열람율 | 비율 | (날짜 범위 내 각 일자의 총 열람 수) / (날짜 범위 내 각 일자의 총 전달 수)<br><br>총 열람에는 직접 열람과 영향받은 열람이 모두 포함됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="측정기준 계산 방법" }

{% endtab %}
{% endtabs %}

## 대시보드 필터 {#dashboard-filters}

다음 필터 옵션을 사용하여 대시보드의 데이터를 필터링할 수 있습니다:

- **태그:** 태그를 하나 선택합니다. 적용하면 대시보드에 선택한 태그에 해당하는 측정기준만 표시됩니다.
- **플랫폼:** (푸시 성능 대시보드만 해당) **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle**, **웹** 등 푸시 플랫폼을 선택합니다. 적용하면 대시보드에 선택한 플랫폼에 해당하는 측정기준만 표시됩니다.
- **Canvas:** 최대 10개의 Canvas를 선택합니다. 적용하면 대시보드에 선택한 Canvas에 해당하는 측정기준만 표시됩니다. 태그 필터를 먼저 선택하면 Canvas 필터 옵션에는 선택한 태그가 포함된 Canvas만 표시됩니다.
- **Campaign:** 최대 10개의 Campaign을 선택합니다. 적용하면 대시보드에 선택한 Campaign에 해당하는 측정기준만 표시됩니다. 태그 필터를 먼저 선택하면 Campaign 필터 옵션에는 선택한 태그가 포함된 Campaign만 표시됩니다.

![태그를 선택하고 필터링할 Canvas 목록을 선택할 수 있는 채널 성능 대시보드의 필터 옵션]({% image_buster /assets/img_archive/dashboard_filters.png %})

## 기간 비교 {#comparing-time-periods}

채널 성능 대시보드는 날짜 범위에서 선택한 기간과 동일한 일수의 이전 기간을 자동으로 비교합니다. 예를 들어, 대시보드에서 날짜 범위로 "최근 7일"을 선택하면, 최근 7일간의 측정기준이 그 이전 7일간의 측정기준과 비교됩니다. 커스텀 날짜 범위를 선택하는 경우(예: 5월 10일부터 5월 15일까지, 즉 6일간의 데이터), 대시보드는 해당 기간의 측정기준을 5월 4일부터 5월 9일까지의 측정기준과 비교합니다.

비교는 이전 기간과 현재 기간 사이의 변화율(%)로, 두 기간의 차이를 이전 기간의 측정기준으로 나누어 계산합니다.

### 총 수 및 비율 변화 보기 {#viewing-changes-in-total-counts-and-rates}

**Show Change in Totals**(두 기간 간의 총 수(예: 전달된 이메일 수)를 비교)와 **Show Change in Rates**(비율(예: 전달률)을 비교) 간에 전환할 수 있습니다.

![채널 성능 대시보드에서 총 수 변화 또는 비율 변화 표시를 전환하는 라디오 버튼.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## 자주 묻는 질문 {#frequently-asked-questions}

### 대시보드에 빈 값이 표시되는 이유는 무엇인가요? {#why-is-my-dashboard-displaying-empty-values}

측정기준에 빈 값이 표시될 수 있는 몇 가지 시나리오가 있습니다:

- 선택한 날짜 범위에서 해당 측정기준에 대해 Braze가 0을 기록했습니다.
- 선택한 날짜 범위 동안 메시지를 보내지 않았습니다.
- 선택한 날짜 범위에서 열람, 클릭 또는 탈퇴와 같은 측정기준이 있었지만 전달 또는 발송이 없었습니다. 이 경우 Braze는 비율 측정기준을 계산하지 않습니다.

더 많은 측정기준을 확인하려면 날짜 범위를 확장해 보세요.

### 이메일 대시보드에서 기타 열람이 고유 열람보다 많이 표시되는 이유는 무엇인가요? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

*고유 열람* 측정기준의 경우, Braze는 특정 사용자가 등록한 반복 열람(*기계 열람* 또는 *기타 열람* 포함 여부와 관계없이)을 중복 제거하여 사용자가 여러 번 열람하더라도 하나의 *고유 열람*만 증가하도록 합니다. *기타 열람*의 경우, Braze는 중복 제거를 수행하지 않습니다.

<!---Temporarily hidden until functionality is added

## 데이터의 빈 값 {#empty-values-in-your-data}

### 측정기준이 "0%" 또는 "0"으로 표시되는 경우 {#if-a-metric-displays-0-or-0}

이는 선택한 기간 동안 Braze가 해당 측정기준에 대해 0을 기록했음을 의미합니다.

#### 측정기준이 "N/A"로 표시되는 경우 {#if-a-metric-displays-na}

이는 선택한 기간 동안 Braze가 특정 측정기준에 대해 긍정적 수치를 기록했지만, 비율 계산의 분모(대부분의 경우 발송 수 또는 전달 수)가 0이었음을 의미합니다. 이메일이 특정 날짜에 발송되고 열람 및 클릭이 이후 날짜에 기록되었을 때, 선택한 기간에 메시지가 발송된 날짜가 포함되지 않은 경우 이러한 현상이 발생할 수 있습니다.

#### 측정기준이 "--"로 표시되는 경우 {#if-a-metric-displays}

이는 선택한 기간 동안 Braze가 해당 측정기준에 대한 데이터를 기록하지 않았음을 의미합니다. 아직 이메일을 설정하거나 발송하지 않은 경우, 전용 [이메일]({{site.baseurl}}/user_guide/channels/email) 섹션에서 자세한 방법을 확인할 수 있습니다.

--->