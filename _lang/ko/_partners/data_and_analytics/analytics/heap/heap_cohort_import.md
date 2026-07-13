---
nav_title: Heap 코호트 가져오기
article_title: Heap 코호트 가져오기
description: "이 참조 문서에서는 디지털 인사이트 플랫폼인 Heap과 Braze 간의 통합에 대해 설명합니다. 이 통합을 통해 Heap 데이터를 Braze로 가져오고, 사용자 코호트를 생성하며, Braze 데이터를 Heap으로 내보내 세그먼트를 생성할 수 있습니다."
alias: /partners/heap_cohort_import/
page_type: partner
search_tag: Partner

---

# Heap 코호트 가져오기 {#heap-cohort-import}

> [Heap](https://heap.io/)은 디지털 인사이트 플랫폼으로, 비즈니스에 가장 큰 영향을 미치는 디지털 경험의 기회에 집중하여 마찰을 제거하고, 고객을 만족시키며, 매출을 가속화할 수 있도록 도와줍니다.

Braze와 Heap 통합을 통해 [Heap 데이터를 Braze로 가져오고](#data-import-integration), 사용자 코호트를 생성하며, [Braze 데이터를 Heap으로 내보내]({{site.baseurl}}/partners/data_and_analytics/analytics/heap) 세그먼트를 생성할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Heap 계정 | 이 파트너십을 활용하려면 [Heap](https://heap.io/about) 계정이 필요합니다. |
| Braze 데이터 가져오기 키 | Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동한 후 **Heap**을 선택하여 확인할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Braze 커런츠 | Braze에서 Heap으로 데이터를 내보내려면 계정에서 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)가 활성화되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 사용 사례 {#use-cases}
- 퍼널을 이탈한 사용자 재참여: 사용자가 구매 또는 가입 퍼널을 이탈할 때 재참여 메시징을 트리거합니다.
- 체험 경험 개인화: 체험 경험에서 마찰 지점을 파악하고, 적절한 타이밍에 리마인더를 보내 체험 기간 동안 사용자를 재참여시키고 가치를 경험할 수 있도록 돕습니다.
- 공지 및 오퍼에 대한 참여도 향상: 프로모션, 업데이트, 새로운 서비스 공지를 관련 오디언스에게 타겟팅합니다.

## 데이터 가져오기 통합 {#data-import-integration}

Heap에서 Braze로의 통합을 사용하여 Heap에서 정의된 코호트를 Braze로 자동 동기화합니다.

### 1단계: Braze 데이터 가져오기 키 가져오기 {#step-1-get-the-braze-data-import-key}

Braze에서 **파트너 통합** > **기술 파트너**로 이동한 후 **Heap**을 선택합니다.

이 페이지에서 데이터 가져오기 키와 REST 엔드포인트를 확인할 수 있습니다. 이 두 값을 기록하고 Heap 계정 매니저에게 제공하여 통합 설정을 완료합니다.

![데이터 가져오기 키와 엔드포인트가 표시된 Braze Heap 기술 파트너 페이지.]({% image_buster /assets/img/heap/heap2.png %}){: style="max-width:90%;"}

### 2단계: Braze에서 가져온 사용자를 세그먼트로 분류하기 {#step-2-segment-imported-users-in-braze}

Braze에서 **Segments**로 이동하여 Heap 코호트 세그먼트의 이름을 지정하고, 필터로 **Heap Cohorts**를 선택합니다. 여기에서 포함할 Heap 코호트를 선택할 수 있습니다. Heap 코호트 세그먼트가 생성된 후에는 Campaign 또는 Canvas를 만들 때 오디언스 필터로 선택할 수 있습니다.

![Braze 세그먼트 빌더에서 사용자 속성 필터 "Heap cohort"가 "includes" 및 "Heap Test Cohort"로 설정되어 있습니다.]({% image_buster /assets/img/heap/heap1.png %}){: style="max-width:90%;"}

### 이 통합 사용하기 {#using-this-integration}

Heap 세그먼트를 사용하려면 Braze Campaign 또는 Canvas를 생성하고 해당 세그먼트를 타겟 오디언스로 선택합니다.

![타겟팅 단계의 Braze Campaign 빌더에서 "세그먼트별로 사용자 타겟팅" 필터가 "Heap cohort"로 설정되어 있습니다.]({% image_buster /assets/img/heap/heap3.png %}){: style="max-width:90%;"}

{% alert important %}
Braze에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에 새 사용자를 생성하지 않습니다.
{% endalert %}

## 통합 세부 정보 {#integration-details}

내보낸 데이터의 페이로드 구조는 커스텀 HTTP 커넥터의 페이로드 구조와 동일하며, [커스텀 HTTP 커넥터 예제 리포지토리](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)에서 확인할 수 있습니다.

## 사용자 매칭 {#user-matching}

식별된 사용자는 `external_id` 또는 `alias`로 매칭할 수 있습니다. 익명 사용자는 `device_id`로 매칭할 수 있습니다. 원래 익명 사용자로 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.