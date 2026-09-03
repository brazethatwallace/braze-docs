---
nav_title: 세그먼트 인사이트
article_title: 세그먼트 인사이트
page_order: 6
page_type: tutorial
tool:
  - Segments
  - Reports
description: "이 사용 방법 문서에서는 세그먼트 인사이트를 사용하고, 해석하고, 공유하는 방법을 안내합니다."
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}세그먼트 인사이트 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordersegment-insights}

> 세그먼트 인사이트를 사용하고, 해석하고, 공유하는 방법을 알아보세요.

세그먼트 인사이트는 미리 선택된 핵심 성과 지표(KPI) 세트를 기준으로 하나의 Segment가 다른 Segment와 비교하여 어떤 성과를 보이는지 보여줍니다.

## 세그먼트 인사이트 보기 {#viewing-segment-insights}

대시보드의 **Analytics** 아래에 있는 **세그먼트 인사이트** 페이지로 이동하여 기준선과 비교한 최대 10개의 서로 다른 Segments를 확인할 수 있습니다.

![세그먼트 인사이트 대시보드에서 기준선 Segment인 "All Users"와 비교하여 "UK Users", "FR Users", "CA Users" 세 개의 Segments를 비교하는 화면.]({% image_buster /assets/img_archive/segment_insights.png %})

{% alert note %}
세그먼트 인사이트 페이지의 통계는 기본적으로 추정값입니다. 정확한 값을 계산하려면 Segment를 열고 **Calculate Exact Statistics**를 선택하세요. 추정값은 정확한 값보다 높거나 낮을 수 있으며, 특히 대규모 워크스페이스나 소규모 Segments에서 그렇습니다.
{% endalert %}

기준선 Segment는 직접 선택한 특정 Segment이거나 모든 사용자를 포함하는 Segment일 수 있습니다. 세그먼트 인사이트를 사용하여 다음 통계를 비교할 수 있습니다:

| 측정 항목 | 설명 | 공식 |
| --------------------- | ------------- | ------------- |
| 일일 세션 수 | Segment 사용자의 일일 평균 세션 수 | (총 세션 수) / (첫 세션 이후 일수) |
| 첫 세션 이후 일수 | Segment 사용자의 첫 세션과 현재 사이의 평균 일수 | 오늘 – 첫 세션 날짜 |
| 마지막 세션 이후 일수 | Segment 사용자의 마지막 세션과 현재 사이의 평균 일수 | 오늘 – 마지막 세션 날짜 |
| 생애 매출(달러) | Segment 사용자의 평균 생애 매출(달러) | 사용자 생애 지출 |
| 첫 구매까지의 일수 | Segment 사용자의 첫 세션과 첫 구매 사이의 평균 일수 | 첫 구매 날짜 – 첫 세션 날짜 |
| 마지막 구매 이후 일수 | Segment 사용자의 마지막 구매와 현재 사이의 평균 일수 | 오늘 – 마지막 구매 날짜 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="세그먼트 인사이트 보기" }

페이지의 고유 URL을 사용하여 특정 비교 결과를 팀원과 쉽게 공유할 수 있으며, 각 Segment 옆의 눈 아이콘을 선택하여 해당 Segment에 대한 자세한 정보를 확인할 수도 있습니다. 이러한 비교 결과는 워크스페이스를 전환하면 초기화됩니다.

![과거 멤버십을 보여주는 그래프와 다양한 메시징 채널의 추정 규모를 분류한 차트가 포함된 "Premium Users (iOS VideoApp)" Segment의 세부 정보.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## Segment 세부 정보 페이지 {#segment-details-page}

세그먼트 인사이트는 **Segment 세부 정보** 보기에도 바로 내장되어 있습니다. 이전에 설정한 특정 Segment를 살펴볼 때, 동적인 회색 Segment 통계 상자 안에 동일한 6가지 통계를 확인할 수 있습니다. 여기에서 세그먼트 인사이트 도구를 빠르게 실행하여 이 특정 Segment를 이전에 설정한 다른 Segment와 비교할 수 있습니다. 단, 이렇게 하면 세그먼트 인사이트 도구에서 이전에 선택한 Segment가 덮어쓰기된다는 점에 유의하세요.

{% alert note %}
[세그먼트 인사이트](#viewing-segment-insights)와 **Segment 세부 정보** 페이지는 서로 다른 사용자 샘플과 샘플 크기를 사용하여 크기 추정치를 별도로 계산하므로, 수치가 일치하지 않을 수 있습니다.
{% endalert %}

![세그먼트 인사이트는 Segment 세부 정보 보기에도 내장되어 있습니다. 이전에 설정한 특정 Segment를 살펴볼 때, 동적인 회색 Segment 통계 상자 안에 동일한 6가지 통계를 확인할 수 있습니다. 여기에서 세그먼트 인사이트 도구를 빠르게 실행하여 이 특정 Segment를 이전에 설정한 다른 Segment와 비교할 수 있지만, 세그먼트 인사이트 도구에서 이전에 선택한 Segment가 덮어쓰기된다는 점에 유의하세요.]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## 사용 사례 {#insights-use-cases}

### 인구통계별 사용 패턴 및 구매 패턴 비교 {#comparing-demographic-usage-and-purchasing-patterns}

세그먼트 인사이트의 가장 유용한 활용 방법 중 하나는 사용자 인구통계가 앱 사용 및 Campaign 효과에 미치는 영향에 대한 질문에 답하는 것입니다. 예를 들면:

- 특정 사용자 인구통계가 평균보다 현저히 좋거나 나쁜 성과를 보이고 있나요?
- 특정 Campaign의 현지화를 재고해야 하나요?
- Campaign이 특정 인구통계의 참여를 유도하고 있나요?
- 특정 인구통계를 대상으로 한 Campaign에 어떤 목표를 설정해야 하나요?

세그먼트 인사이트는 사용자 인구통계 간의 차이를 발견하는 데 도움이 됩니다. 다음 예시는 앱의 사용자 기반을 언어별로 비교한 것으로, 영어 사용자가 다른 언어 사용자보다 더 높은 LTV와 활동 수준을 보이는 경향이 있음을 보여줍니다.

![영어, 독일어, 프랑스어, 스페인어 Segment에 대한 세그먼트 인사이트 분석.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

이 예시에서 독일어 사용자는 평균적으로 더 오래 전에 가입했으며, 이는 더 이상 활발하지 않은 이유를 설명할 수 있습니다. 이는 다양한 요인에 의한 것일 수 있습니다. 예를 들어, 앱이 처음에는 유럽에서 출시되었지만 현재는 대부분의 사람들이 영어나 스페인어를 사용하는 미국에서 더 인기가 있을 수 있습니다. 인구통계 전반에 걸쳐 핵심 성과 지표(KPI)를 분석할 때 더 견고한 결과를 얻으려면, 인구통계에 대한 일반적인 연구(예: 언어가 모든 사용자의 LTV에 영향을 미치는지)에서 나온 결과를 더 작고 유사한 모집단에서 확인하여 결과가 지속되는지 테스트하는 것이 합리적입니다.

영어 이외의 언어 사용자의 전환을 개선하려면, 좋은 첫 번째 단계는 사용자의 기기 언어에 맞게 [Campaign을 현지화]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)하고, [다변량 Campaign]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests)을 사용하여 외국어 문구의 다양한 버전을 테스트함으로써 해당 메시지의 문구가 사용자의 참여를 유도하는지 확인하는 것입니다.

### 높은 매출의 지표 이해 {#understanding-indicators-of-higher-revenue}

사용자를 구매자로 전환시키는 것은 어려울 수 있으며, 신규, 비활성 또는 이탈한 사용자를 직접 구매로 유도하려고 하면 사용자가 앱을 삭제할 수 있습니다. 세그먼트 인사이트는 사용자가 바로 구매하지 않더라도 구매 퍼널을 따라 더 나아가게 하는 행동을 발견하는 데 도움이 됩니다. 예를 들어, 뉴스레터 구독, 소셜 미디어 공유, 프로모션 메시지 수신 등록 등이 있습니다. 예를 들어, 이커머스 앱 내 다양한 행동이 구매에 미치는 영향을 차트로 나타낼 수 있습니다.

![소셜 미디어에서 공유한 사용자, 프로모션에 등록한 사용자, 뉴스레터에 등록한 사용자에 대한 세그먼트 인사이트 분석.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

이 경우, 현재 프로모션 메시지에 등록한 사용자는 비교적 적고 활동도 활발하지 않지만, 이 사용자들은 더 높은 생애 매출을 생성합니다. 매출을 늘리려면 온보딩 Campaign에 프로모션 메시지 수신 등록 초대를 포함하는 것이 좋은 방법일 수 있습니다. 이탈한 사용자를 다시 참여시키려면, 일반적인 [이탈 사용자 Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users)을 발송하고 [전환한 사용자]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#converted-from-campaign)를 타겟으로 프로모션 메시지 수신 등록을 위한 후속 Campaign을 보내는 것이 좋은 계획입니다.