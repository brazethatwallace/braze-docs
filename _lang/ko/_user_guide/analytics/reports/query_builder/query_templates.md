---
nav_title: 쿼리 템플릿
article_title: 쿼리 빌더 템플릿
page_order: 1
page_type: reference
toc_headers: h2
description: "이 참조 문서에서는 쿼리 빌더에서 Snowflake의 Braze 데이터를 사용하여 생성할 수 있는 보고서 유형을 나열합니다."
tool: Reports
---

# 쿼리 빌더 템플릿 {#query-builder-templates}

> 보고서를 생성할 때 **쿼리 템플릿**을 선택하여 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) 템플릿에 액세스합니다. 모든 템플릿은 최근 60일까지의 데이터를 표시하지만, 에디터에서 해당 값 및 기타 값을 직접 편집할 수 있습니다.<br><br>쿼리 빌더 보고서에 표시될 수 있는 측정기준의 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/analytics/metrics_glossary/)을 참조하고 해당 채널별로 필터링하세요.

## 채널 템플릿 {#channel-templates}

<style>
table th:nth-child(1) {
    width: 30%;
}
table th:nth-child(2) {
    width: 70%;
}
table td {
    word-break: break-word;
}
</style>

| 쿼리 이름 | 설명 |
| --- | --- |
| 채널 참여 및 매출 | 이 보고서는 각 채널에 대해 모든 참여 측정기준(예: 열람 및 클릭), 매출, 트랜잭션 수, 평균 가격을 표시합니다. {::nomarkdown} <ul> <li> <i>트랜잭션 수:</i> 구매 이벤트 수 </li> <li> <i>평균 가격:</i> 매출을 트랜잭션으로 나눈 값 </li> </ul> {:/} ![]({% image_buster /assets/img_archive/channel_engagement_revenue.png %}) |
| Segment별 구매 및 매출 | 이 보고서는 특정 Segment에 대해 전송된 메시지의 측정기준을 표시합니다. <br><br> 구매 측정기준은 보고 기간 전체에서 고유합니다. 한 사용자는 최대 한 건의 구매를 생성할 수 있습니다. 매출은 보고 기간의 모든 구매를 고려합니다. |
| Segment별 배리언트 또는 단계의 구매 및 매출 | 이 보고서는 각 Segment에 전송된 메시지의 배리언트 또는 캔버스 단계에 대한 측정기준을 표시합니다. <br><br> 구매 측정기준은 보고 기간 전체에서 고유합니다. 한 사용자는 최대 한 건의 구매를 생성할 수 있습니다. 매출은 보고 기간의 모든 구매를 고려합니다. |
| 구매 상위/하위 메시징 | 이 보고서는 상위 또는 하위 Campaigns, Canvases 또는 캔버스 단계에 대한 구매 측정기준을 표시합니다. 각 행은 Campaign, Canvas 또는 캔버스 단계입니다. 상위 또는 하위 성과를 표시할지 여부와 이 분석을 실행할 특정 측정기준(예: *수신 시 고유 구매*, *수신 시 매출*, *고유 수신자*)을 지정해야 합니다. <br><br> 상위 성과 보고서의 행은 최고에서 최저 순으로 정렬되며, 하위 성과 보고서의 행은 최저에서 최고 순으로 정렬됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Channel templates" }

## Campaign 템플릿 {#campaign-templates}

| 쿼리 이름 | 설명 |
| --- | --- |
| 국가별 Campaign 매출 | 이 보고서는 특정 Campaign에 대한 국가별 매출을 표시합니다. 이 보고서를 실행하려면 Campaign의 API 식별자를 지정해야 합니다. Campaign의 API 식별자는 해당 Campaign 세부 정보 페이지 하단에서 확인할 수 있습니다. <br><br> 이 보고서는 각 국가에 대해 생성된 매출 금액, 주문 수, 반품 수, 순매출, 총매출을 표시합니다.<br><br> {::nomarkdown} <ul> <li> <i>주문:</i> 구매 이벤트 수 </li> <li><i> 반품:</i> 음수 매출 값을 가진 구매 이벤트 수 </li> <li><i> 순매출:</i> 반품을 제외한 모든 매출 </li> <li><i> 총매출:</i> 반품 값을 포함한 매출 </li></ul>{:/} ![]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaign templates" }

## Canvas 템플릿 {#canvas-templates}

| 쿼리 이름 | 설명 |
| --- | --- |
| 국가별 Canvas 매출 | 이 보고서는 특정 Canvas에 대한 국가별 매출을 표시합니다. 이 보고서를 실행하려면 Canvas의 API 식별자를 지정해야 합니다. Canvas API 식별자는 **Analyze Variants** 아래에서 확인할 수 있습니다. <br><br> 이 보고서는 각 국가에 대해 생성된 매출 금액, 주문 수, 반품 수, 순매출, 총매출을 표시합니다.<br><br> {::nomarkdown} <ul> <li> <i>주문:</i> 구매 이벤트 수 </li> <li><i> 반품:</i> 음수 매출 값을 가진 구매 이벤트 수 </li> <li><i> 순매출:</i> 반품을 제외한 모든 매출 </li> <li><i> 총매출:</i> 반품 값을 포함한 매출 </li></ul>{:/} ![]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas templates" }

## 이메일 템플릿 {#email-templates}

| 쿼리 이름 | 설명 |
| --- | --- |
| 도메인별 이메일 반송 | 이메일 도메인별 반송 수로, 총 반송, 하드바운스, 소프트바운스로 분류됩니다. <br> ![]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:60%;"} |
| 일별 이메일 전달 측정기준 | 이 보고서는 각 날짜에 전송된 메시지의 측정기준을 표시합니다. 예를 들어 전송된 이메일 수, 전달된 수, 소프트바운스 수, 하드바운스 수 등이 포함됩니다. <br><br> 모든 측정기준은 보고 기간 전체에서 고유합니다. 예를 들어, 환영 이메일이 11월 21일에 한 번 소프트바운스되고, 11월 22일에 두 번 소프트바운스되었으며, 전달되지 않은 경우: {::nomarkdown} <ul><li> 11월 21일의 <i>소프트바운스</i> 측정기준이 1 증가합니다.</li><li> 11월 22일의 <i>소프트바운스</i> 측정기준은 영향을 받지 않습니다. </li></ul>{:/} ![]({% image_buster /assets/img_archive/email_delivery_day.png %})|
| Segment별 이메일 참여 측정기준 | 이 보고서는 각 Segment에 전송된 메시지의 측정기준을 표시합니다. 예를 들어 전송된 이메일 수, 전달된 수, 소프트바운스 수, 하드바운스 수 등이 포함됩니다. <br><br> 모든 측정기준은 보고 기간 전체에서 고유합니다. 예를 들어, 환영 이메일이 11월 21일에 한 번 소프트바운스되고, 11월 22일에 두 번 소프트바운스되었으며, 전달되지 않은 경우: {::nomarkdown} <ul><li> 11월 21일의 <i>소프트바운스</i> 측정기준이 1 증가합니다. </li><li> 11월 22일의 <i>소프트바운스</i> 측정기준은 영향을 받지 않습니다.</li></ul>{:/} ![]({% image_buster /assets/img_archive/email_engagement_segment.png %}) |
| Segment별 배리언트 또는 단계의 이메일 참여 측정기준 | 이 보고서는 각 Segment에 전송된 메시지의 배리언트 또는 캔버스 단계에 대한 측정기준을 표시합니다. 이러한 측정기준에는 전송된 이메일 수, 전달된 수, 소프트바운스 수, 하드바운스 수가 포함됩니다. <br><br> 모든 측정기준은 보고 기간 전체에서 고유합니다. 예를 들어, 환영 이메일이 11월 21일에 한 번 소프트바운스되고, 11월 22일에 두 번 소프트바운스되었으며, 전달되지 않은 경우: {::nomarkdown} <ul><li> 11월 21일의 <i>소프트바운스</i> 측정기준이 1 증가합니다. </li> <li> 11월 22일의 <i>소프트바운스</i> 측정기준은 영향을 받지 않습니다.</li></ul> {:/} |
| 국가별 이메일 성과 | 이 보고서는 각 국가에 대해 다음 측정기준을 표시합니다: 전송 수, 간접 열람률, 직접 열람률. 국가는 푸시 전송 시점의 사용자 국가입니다. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| 이메일 구독 변경 로그 | 이 보고서는 각 사용자의 구독 변경에 대해 기록된 측정기준을 표시합니다. 예를 들어 이메일 주소, 구독 상태, 상태가 변경된 시간, 관련 Canvas 또는 Campaign 등이 포함됩니다. |
| 이메일 구독 그룹 옵트인 및 옵트아웃 | 이 보고서는 모든 이메일 구독 그룹에 대해 매주 고유 사용자 옵트인 및 옵트아웃 수를 표시합니다. 이 쿼리를 실행하려면 워크스페이스에 최소 하나의 [이메일 구독 그룹]({{site.baseurl}}/user_guide/channels/email/subscriptions/)이 있어야 합니다. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"} |
| 클릭된 이메일 URL | 이 보고서는 이메일의 각 링크가 받은 클릭 수를 표시합니다. 이 보고서를 실행하려면 Campaign 또는 Canvas의 API 식별자를 지정해야 합니다. Campaign의 API 식별자는 해당 Campaign 세부 정보 페이지 하단에서, Canvas API 식별자는 **Analyze Variants** 아래에서 확인할 수 있습니다. <br><br> 이 보고서는 비개인화된 링크와 각 링크의 클릭 수를 표시합니다. CSV 다운로드에는 클릭한 모든 사용자의 사용자 ID, 클릭한 링크, 클릭한 타임스탬프가 포함됩니다. <br><br> *비개인화된 URL:* Liquid 태그가 제거된 URL입니다. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"} |
| 이메일 참여 상위/하위 메시징 | 이 보고서는 상위 또는 하위 Campaigns, Canvases 또는 캔버스 단계에 대한 이메일 참여 측정기준을 표시합니다. 상위 또는 하위 성과를 표시할지 여부와 이 분석을 실행할 특정 측정기준(예: *전송*, *소프트바운스*, *고유 열람*)을 지정해야 합니다. <br><br> 상위 성과 보고서의 행은 최고에서 최저 순으로 정렬되며, 하위 성과 보고서의 행은 최저에서 최고 순으로 정렬됩니다. <br><br> ![]({% image_buster /assets/img_archive/top-bottom-email.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

## 모바일 템플릿 {#mobile-templates}

| 쿼리 이름 | 설명 |
| --- | --- |
| 기기 통신사 | Verizon, T-Mobile 등 기기 통신사별 사용자 수입니다. <br><br> ![]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:50%;"} |
| 기기 모델 | iPhone 15 Pro, Pixel 7 등 기기 모델별 사용자 수입니다. <br><br> ![]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:50%;"} |
| 기기 운영체제 | 17.4, Android 14 등 운영체제별 사용자 수입니다. <br><br> ![]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:50%;"} |
| 기기 화면 해상도 | 1179x2556, 750x1334 등 기기 화면 해상도별 사용자 수입니다. <br><br> ![]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"} |
| SMS 오류 코드 | 이 보고서는 각 SMS 오류 코드에 대한 오류 유형과 오류 수를 표시합니다. <br><br>![]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"} |
| 사용자별 SMS 제공자 오류 | 이 보고서는 특정 사용자에 대한 SMS 오류 코드를 표시합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mobile templates" }

## 푸시 템플릿 {#push-templates}

| 쿼리 이름 | 설명 |
| --- | --- |
| 국가별 푸시 성과 | 이 보고서는 각 국가에 대해 다음 측정기준을 표시합니다: 전달 수, 열람률, 클릭률. 국가는 이메일 전송 시점의 사용자 국가입니다. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push templates" }

## Segment 분석 {#segment-breakdown}

| 쿼리 이름 | 설명 |
| -- | -- |
| Segment별 이메일 참여 측정기준 | 이 보고서는 Campaign 또는 Canvas 수준에서 Segment별로 분류된 이메일 성과 측정기준을 표시합니다. |
| Segment별 구매 및 매출 | 이 보고서는 특정 Campaign 또는 Canvas에 대해 Segment별로 분류된 구매 및 매출 측정기준을 표시합니다. |
| 이메일 참여 상위/하위 메시징 | 이 보고서는 지정된 이메일 참여 측정기준에서 최고 또는 최저 성과를 보인 Campaigns, Canvases 또는 캔버스 단계를 표시합니다. |
| 구매 상위/하위 메시징 | 이 보고서는 지정된 구매 또는 매출 측정기준에서 최고 또는 최저 성과를 보인 Campaigns, Canvases 또는 캔버스 단계를 표시합니다. |
| Segment별 푸시 성과 | 이 보고서는 Segment별로 분류된 푸시 측정기준을 표시합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment breakdown" }