---
nav_title: Segment 크기 측정
article_title: Segment 크기 측정
page_order: 5
page_type: reference
tool:
- Segments
description: "이 페이지에서는 Segment의 멤버십과 크기를 모니터링하는 방법을 다룹니다."
---

# Segment 크기 측정 {#measure-segment-size}

> 이 페이지에서는 Segment의 멤버십과 크기를 모니터링하는 방법을 다룹니다.

## Segment 멤버십 계산 {#segment-membership-calculation}

Braze는 데이터가 서버로 전송되고 처리될 때 사용자의 Segment 멤버십을 업데이트하며, 일반적으로 즉시 반영됩니다. 사용자의 Segment 멤버십은 해당 세션이 처리될 때까지 변경되지 않습니다. 예를 들어, 세션이 처음 시작될 때 휴면 사용자 Segment에 해당하는 사용자는 세션이 처리되면 즉시 휴면 사용자 Segment에서 제외됩니다.

### 총 도달 가능 사용자 계산 {#total-reachable-users-calculation}

각 Segment는 해당 Segment에 속한 총 사용자 수를 표시합니다. **모든 앱의 사용자**로 필터링하면 가장 자주 사용되는 메시징 채널(예: 웹 푸시 또는 이메일)과 해당 특정 채널의 도달 가능 사용자 수도 함께 표시됩니다.

총 사용자 수가 각 채널별 도달 가능 사용자 수와 다를 수 있습니다. 또한 도달 가능 사용자 테이블에 모든 채널이 나열되지는 않습니다. 예를 들어, Content Cards, 웹훅, WhatsApp은 분류에 표시되지 않습니다. 이는 총 도달 가능 사용자 수가 표시된 각 채널의 사용자 합계보다 클 수 있음을 의미합니다.

![이메일, iOS 푸시, Android 푸시, 웹 푸시, Kindle 푸시별 도달 가능 사용자로 분류된 총 도달 가능 사용자를 표시하는 테이블.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

사용자가 특정 채널을 통해 도달 가능한 것으로 나열되려면 다음 두 가지 조건을 모두 충족해야 합니다:
* 프로필에 유효한 이메일 주소 또는 푸시 토큰이 연결되어 있어야 하며,
* 앱에 옵트인 또는 가입되어 있어야 합니다.

단일 사용자가 여러 도달 가능 사용자 그룹에 속할 수 있습니다. 예를 들어, 사용자가 유효한 이메일 주소와 유효한 Android 푸시 토큰을 모두 가지고 있고 둘 다 옵트인했지만, 연결된 iOS 푸시 토큰이 없을 수 있습니다. 총 도달 가능 사용자와 각 채널 합계 간의 차이는 Segment에 해당하지만 해당 커뮤니케이션 채널을 통해 도달할 수 없는 사용자 수입니다.

{% alert note %}
**총 도달 가능 사용자**에는 더 이상 채널에 가입되어 있지 않더라도 Segment 필터에 일치하는 모든 사용자가 포함됩니다. **iOS**와 같은 채널 행은 [채널별 도달 가능 사용자](#reachable-users-by-channel)의 규칙에 따라 해당 채널에서만 도달 가능한 사용자를 카운트합니다. Segment 합계를 가입된 사용자와 일치시키려면 **Push enabled for iOS**가 true인 필터(또는 해당 채널에 해당하는 필터)를 추가하세요.
{% endalert %}

## Segment 크기 통계 {#statistics-for-segment-size}

추정 통계는 Segment의 일부만 샘플링하여 근사치를 구하므로, 추정 크기가 실제 값보다 크거나 작을 수 있으며, 워크스페이스가 클수록 오차 범위가 더 클 수 있습니다. Segment의 정확한 사용자 수를 확인하려면 **Calculate Exact Statistics**를 선택하세요. 정확한 Segment 멤버십은 Campaign 또는 Canvas에서 전송되는 메시지에 의해 Segment가 영향을 받기 전에 항상 계산됩니다.

Braze는 Segment 크기에 대해 다음과 같은 통계를 제공합니다.

### 필터 통계 {#filter-statistics}

각 필터 그룹에 대해 추정 도달 가능 사용자를 확인할 수 있습니다. 채널별 분류를 보려면 **Expand extra funnel statistics**를 선택하세요.

![세션 수가 정확히 1인 사용자에 대한 필터가 있는 필터 그룹.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## 도달 가능 사용자 추정 {#reachable-users-estimate}

**Reachable users** 사이드 패널에서 전체 Segment의 추정 도달 가능 사용자와 각 채널별 추정 사용자 수를 확인할 수 있습니다. 이 **추정치**는 Segment 크기의 대략적인 범위와 전체 사용자 기반 중 이 Segment에 해당하는 비율의 추정치를 보여줍니다. 추정 통계는 Segment를 편집하지 않는 한 15분 동안 캐시되며, 편집하면 추정 통계가 자동으로 업데이트됩니다. **Calculate exact statistics**를 선택하여 도달 가능 사용자의 정확한 수(Segment 전체 및 채널별 모두)를 확인할 수도 있습니다.


![추정 사용자가 230만~240만 명이라고 표시하는 "Reachable users" 패널.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### 추정 수에 대한 고려 사항 {#considerations-for-estimate-counts}

Braze는 사용자의 하위 집합을 쿼리한 다음 그 결과를 전체 오디언스로 외삽하여 추정 사용자 수를 측정합니다. Braze가 쿼리하는 사용자의 하위 집합은 추정치를 계산할 때마다 다를 수 있으므로, 오디언스 멤버십이 기술적으로 동일하게 유지되어야 하는 경우에도 추정치가 변경될 수 있습니다. 예를 들어, 필터 순서를 변경하거나 다른 시간에 동일한 Segment를 다시 확인하면 추정 수가 변경될 수 있습니다(Segment가 변경되지 않았다면 **Calculate exact stats**는 동일한 결과를 보여줍니다).

워크스페이스에 대규모 사용자 모집단이 있는 경우, 특히 Segment가 전체 워크스페이스 모집단의 매우 작은 비율인 경우 추정 수와 정확한 계산 수 사이에 더 큰 차이가 나타날 수 있습니다. 이는 Braze가 사용자의 하위 집합을 쿼리하고 그 결과를 전체 사용자 기반으로 외삽하여 추정치를 측정하기 때문입니다. 사용자 기반이 클수록 추정치와 정확한 수 사이의 차이가 더 클 수 있습니다.

매우 작은 Segment의 경우 추정 범위에 0이 포함될 수 있으며, 이는 전체 사용자 비율이 0으로 반올림될 수 있음을 의미합니다. 이러한 경우 **Calculate exact stats**를 사용하면 실제로 0이 아닐 수 있는 Segment 크기의 정확한 수를 확인할 수 있습니다.

![정확한 사용자 수가 "31"로 표시된 "Reachable users" 사이드 패널.]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### 채널별 도달 가능 사용자 {#reachable-users-by-channel}

각 메시지 채널별 도달 가능 사용자 수를 확인하려면 **Reachable users** 패널에서 **Show breakdown**을 선택하세요. 이 화면에서는 가장 자주 사용되는 메시징 채널(예: 웹 푸시 또는 이메일)과 해당 특정 채널의 도달 가능 사용자 수를 표시합니다.

_Total_ 측정기준은 고유 사용자를 나타냅니다. 예를 들어, 사용자가 Android 푸시와 iOS 푸시를 모두 가지고 있으면 두 행 모두에 카운트되지만, _Total_ 행에서는 1명의 사용자로만 카운트됩니다.

그러나 단일 사용자가 여러 도달 가능 사용자 그룹에 속할 수 있으므로, 총 사용자 수가 각 채널별 도달 가능 사용자 합계와 다를 수 있습니다. 예를 들어, 사용자가 유효한 이메일 주소와 유효한 Android 푸시 토큰을 모두 가지고 있고 둘 다 옵트인했지만, 연결된 iOS 푸시 토큰이 없을 수 있습니다.

**Reachable users** 테이블에 모든 채널이 나열되지는 않습니다(예: Content Cards, 웹훅, WhatsApp). 예를 들어, WhatsApp을 통해서만 도달 가능한 사용자가 있는 경우 _Total_에는 반영되지만 채널별 행에는 표시되지 않습니다. 이는 총 도달 가능 사용자 수가 표시된 각 채널의 사용자 합계와 다를 수 있음을 의미합니다.

_Total_이 채널 합계보다 높은 경우, 그 차이는 Segment에 해당하지만 해당 커뮤니케이션 채널을 통해 도달할 수 없는 사용자 수를 나타냅니다.

사용자가 특정 채널을 통해 도달 가능한 것으로 나열되려면 다음 조건을 충족해야 합니다:
- 프로필에 유효한 이메일 주소 또는 푸시 토큰이 연결되어 있어야 하며,
- 앱에 옵트인 또는 가입되어 있어야 합니다.

#### 채널별 도달 가능 사용자에 적용되는 필터 {#applied-filters-for-channel-specific-reachable-users}

도달 가능 사용자를 결정할 때 각 채널에 적용되는 필터는 다음과 같습니다.

| 채널 | 필터 |
| --- | --- |
| 이메일 | **Email Available**이 true입니다. |
| 푸시 | **Foreground Push Enabled**가 true입니다. |
| SMS | **Subscription Group**이 SMS 구독 그룹 중 하나입니다. **Invalid Phone Number**가 false입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="채널별 도달 가능 사용자에 적용되는 필터" }

## 정확한 통계 계산 {#calculating-exact-statistics}

Segment의 정확한 사용자 수를 확인하려면 **Reachable users** 패널에서 **Calculate exact stats**를 선택하세요.

이전에 실행한 계산의 통계를 업데이트하려면 **Refresh exact statistics**를 선택하세요. 이 계산이 마지막으로 실행된 날짜가 자동으로 업데이트됩니다.

계산의 정확도는 99.999% 이상입니다. 따라서 대규모 Segment의 경우 정확한 통계를 계산할 때에도 약간의 변동이 있을 수 있으며, 이는 정상적인 동작입니다. 또한 정확한 통계 결과는 Segment를 편집하지 않는 한 24시간 동안 캐시되며, 편집하면 정확한 통계를 다시 계산할 수 있습니다.

{% alert note %}
[무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)로 균등하게 나눈 Segments는 동일한 크기가 되지 않습니다. 예를 들어, **Random Bucket # less than 5000** 필터로 하나의 Segment를 만들고 **Random Bucket # at least 5000** 필터로 다른 Segment를 만들면, Segment 크기가 몇 퍼센트 포인트까지 차이가 날 수 있습니다. 이는 비활성 사용자 삭제 및 도달 불가능한 사용자 등의 상황 때문입니다.
{% endalert %}

![정확한 통계와 확장된 분류 메뉴가 표시된 Reachable users 패널의 스크린샷.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

필터 수준의 통계는 정확한 통계를 계산하더라도 항상 추정치입니다. **Calculate exact stats**는 필터 또는 필터 그룹 수준이 아닌 Segment 수준에서만 정확한 통계를 계산합니다. 이 계산은 실행하는 데 몇 분이 걸릴 수 있습니다. 특히 대규모 워크스페이스의 경우 계산을 완료하는 데 더 오랜 시간이 필요할 수 있습니다. **Reachable users** 패널의 진행률 표시줄에서 진행 상황을 추적할 수 있습니다. 계산이 5분 이상 소요될 것으로 예상되면 Braze가 결과를 이메일로 보내드립니다.

Braze는 워크스페이스당 한 번에 하나의 계산을 우선 처리하므로, 여러 계산을 동시에 실행하면 지연이 발생합니다. **View calculation queue**를 선택하면 앞에 있는 Segments, 진행 상황, 시작한 사람을 확인하고 계산이 언제 우선 처리될지 파악할 수 있습니다.

![하나의 계산이 있는 계산 대기줄.]({% image_buster /assets/img_archive/calculation_queue.png %})

**Cancel**을 선택하여 정확한 통계 계산을 취소할 수 있습니다. 대기줄에 여러 계산이 있고 다른 계산을 먼저 우선 처리하고 싶을 때 유용합니다.


## 과거 Segment 멤버십 크기 보기 {#viewing-historical-segment-membership-size}

모든 Segments에 대해 각 날짜별 추정 Segment 멤버십을 보여주는 과거 멤버십 차트를 확인할 수 있습니다. 이 차트는 시간에 따른 Segment 크기의 변화를 보여줍니다. 드롭다운을 사용하여 날짜 범위별로 Segment 멤버십을 필터링하세요.

![Historical Membership 드롭다운을 사용하여 날짜 범위별로 Segment 멤버십을 필터링합니다.]({% image_buster /assets/img_archive/historical_membership2.png %})

이 차트의 목적은 전체적인 Segment 멤버십 추세를 파악하는 것이므로, 일일 수는 **Calculate Exact Statistics**를 선택하기 전의 Segment 크기와 유사한 추정치입니다. 이 그래프는 추정치를 보여주므로, 실제 크기(**Calculate Exact Stats**를 선택한 후 확인 가능)가 "0"이 아니더라도 차트에서 Segment 크기가 "0"으로 표시될 수 있습니다. 특히 Segment가 워크스페이스 모집단 크기에 비해 매우 작은 경우 차트에서 "0"으로 추정될 가능성이 높습니다.

예를 들어, 워크스페이스에 1억 명의 사용자가 있고 Segment에 약 700명의 사용자가 있다고 가정해 보겠습니다. 일부 날에는 Segment에 사용자가 없고, 과거 멤버십 추정에 사용되는 무작위 버킷 범위에 해당하는 사용자가 없어 해당 날의 멤버십 수가 0이 될 수 있습니다.

Braze는 사용자의 하위 집합을 쿼리한 다음 그 결과를 전체 오디언스로 외삽하여 Segment 멤버십 수를 추정합니다. 이는 차트의 결과가 해당 날의 Segment 멤버십에 대한 추정치만 제공하며, 매일 다른 사용자 샘플이 쿼리될 수 있으므로 일별 변동이 예상됨을 의미합니다.

{% alert note %}
모든 추정치는 워크스페이스 전체 모집단 크기의 약 1%만큼 표시된 값보다 높거나 낮을 수 있습니다. 사용자가 더 많은 대규모 워크스페이스는 차이가 여전히 워크스페이스 사용자 모집단의 1%이더라도 정확한 계산과 수치적으로 더 큰 차이가 날 수 있는 추정치를 가질 가능성이 높습니다. 이는 대규모 워크스페이스에서 추정치와 정확한 수 사이의 더 큰 차이가 예상됨을 의미합니다.
{% endalert %}

### 큰 변동의 원인 {#reasons-for-significant-changes}

멤버십 수는 다음 표에 나열된 것과 같은 여러 이유로 크게 변경될 수 있습니다.

| 원인 | 예시 |
| --- | --- |
| 일반적인 사용자 동작 | 특히 성공적인 Campaign 이후 사용자가 가입합니다. |
| CSV로 사용자 가져오기 | Segment 멤버십을 크게 증가시킨 사용자 CSV 파일을 가져왔습니다. |
| Segment 오디언스 기준 수정 | 기존 Segment의 오디언스 규칙(예: 필터)이 변경되어 Segment 멤버십에 큰 변화가 발생했습니다. |
| 사용자 삭제 | 상당수의 사용자가 삭제되었습니다. |
| 파트너 통합이 Braze와 동기화 | 서드파티가 Braze에 데이터를 전송하여 Segment 멤버십에 큰 영향을 미쳤습니다. |
| 휴면 사용자 아카이브 | 상당수의 비활성 프로필이 아카이브되었습니다. 예를 들어, CSV로 가져온 많은 사용자가 활동을 기록하지 않아 동시에 아카이브됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="큰 변동의 원인" }