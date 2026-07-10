---
nav_title: Kubit
article_title: Kubit 코호트 가져오기
description: "이 참조 문서에서는 노코드 셀프서비스 분석 플랫폼인 Kubit의 코호트 가져오기 기능을 설명합니다. Kubit은 즉각적인 제품 인사이트를 제공하며, Kubit 사용자 코호트를 가져와 Braze 메시징에서 타겟팅할 수 있습니다."
page_type: partner
search_tag: Partner
---

# Kubit 코호트 가져오기 {#kubit-cohort-import}

> 이 문서에서는 [Kubit](https://kubit.ai/)에서 Braze로 사용자 코호트를 가져오는 방법을 설명합니다. Kubit 통합 및 기타 기능에 대한 자세한 내용은 [Kubit 기본 문서]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit)를 참조하세요.

## 데이터 가져오기 통합 {#data-import-integration}

### 1단계: Braze 데이터 가져오기 키 받기 {#step-1-get-the-braze-data-import-key}

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Kubit**을 선택합니다. 여기에서 REST 엔드포인트를 확인하고 Braze 데이터 가져오기 키를 생성할 수 있습니다.

키가 생성되면 새 키를 만들거나 기존 키를 무효화할 수 있습니다. 데이터 가져오기 키와 REST 엔드포인트는 다음 단계에서 Kubit 대시보드에 포스트백을 설정할 때 사용됩니다.

![Braze의 Kubit 기술 파트너 페이지.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### 2단계: Kubit에서 Braze 구성하기 {#step-2-configure-braze-in-kubit}

Braze 데이터 가져오기 키와 Braze REST 엔드포인트를 Kubit 지원 담당자에게 제공합니다. 담당자가 자체적으로 통합을 구성하고 통합이 활성화되면 알려줍니다.

### 3단계: Braze로 코호트 가져오기 {#step-3-import-cohorts-to-braze}

#### Kubit에서 코호트 만들기 {#create-a-cohort-in-kubit}
Kubit에서 [코호트를 만들고](https://www.kubit.ai/doc/fundamentals#cohort) 타겟 사용자의 기준을 정의합니다.<br><br>![타겟 사용자 기준이 구성된 Kubit 코호트 빌더.]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Braze로 사용자 가져오기 {#import-users-to-braze}
코호트를 저장한 후 Braze로 가져와 Braze 세그먼트에서 사용할 수 있습니다. 이러한 세그먼트는 타겟팅된 이메일 또는 푸시 Campaigns 및 Canvases를 만드는 데 사용할 수 있습니다.

이를 수행하려면 기존 코호트로 이동하여 **Cohort Control**에서 **Import to Braze**를 선택합니다.

![Import to Braze가 선택된 Kubit Cohort Control 메뉴.]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

다음으로 원하는 가져오기 주기를 선택합니다. 일회성 가져오기를 사용하면 지금 한 번 가져올 수 있습니다. 예약 가져오기를 사용하면 특정 시간에 매일, 매주 또는 매월 가져올 수 있습니다. 각 코호트에는 하나의 활성 가져오기 스케줄만 설정할 수 있습니다.

![Braze 가져오기를 위한 주기 옵션이 있는 Kubit 가져오기 스케줄 설정.]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Braze에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에 새 사용자를 생성하지 않습니다.
{% endalert %}

#### 가져오기 상태 확인 {#verify-import-status}
가져오기가 완료되면 가져오기 스케줄에 지정된 수신자에게 이메일 알림이 전송됩니다. Kubit의 **Schedule**에서 코호트의 가져오기 상태를 확인할 수도 있습니다. 스케줄 기록에는 모든 가져오기 실행 시간, 결과, 그리고 Braze로 가져온 코호트 내 총 사용자 수가 표시됩니다.<br><br>![가져오기 실행 시간, 결과 및 가져온 사용자 수를 보여주는 Kubit 스케줄 기록.]({% image_buster /assets/img/kubit/import_history.png %})<br><br>해당 가져오기 스케줄의 **Import to Braze** 아이콘을 클릭하여 수동으로 가져오기를 트리거할 수 있습니다.

### 4단계: Kubit 코호트로 Braze 세그먼트 만들기 {#step-4-create-braze-segments-with-kubit-cohorts}
Braze로 코호트를 가져온 후 필터로 사용하여 Braze 세그먼트를 만들고 Braze Campaigns 또는 Canvas에 포함할 수 있습니다. [Braze 세그먼트를 만드는 방법]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#step-4-add-filters-to-your-segment)에 대해 자세히 알아보려면 세그먼트 설명서를 참조하세요.

![Braze 세그먼트 빌더에서 사용자 속성 "Kubit 코호트"가 "includes_value"로 설정되어 사용 가능한 코호트 목록을 표시합니다.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## 사용자 매칭 {#user-matching}

식별된 사용자는 `external_id` 또는 `alias`로 매칭할 수 있습니다. 익명 사용자는 `device_id`로 매칭할 수 있습니다. 원래 익명 사용자로 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.