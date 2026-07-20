---
nav_title: Heap
article_title: "Heap Analytics"
description: "이 참조 문서에서는 디지털 인사이트 플랫폼인 Heap과 Braze Currents를 사용하여 인게이지먼트 이벤트를 자동으로 분석하는 방법을 설명합니다. Heap 데이터를 Braze로 가져오고, 사용자 코호트를 생성하며, Braze 데이터를 Heap으로 내보내 세그먼트를 생성할 수 있습니다."
page_type: partner
alias: /partners/heap/
search_tag: Partner

---

# Heap analytics

> 이 문서에서는 Braze에서 Heap으로 인게이지먼트 이벤트를 자동으로 전송하여 분석하는 방법을 설명합니다. [Heap 코호트 동기화]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap#data-import-integration) 등 Heap 통합 및 기타 기능에 대한 자세한 내용은 [Heap 기본 문서]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import)를 참조하세요.

## 데이터 내보내기 통합 {#data-export-integration}

Braze Currents를 사용하여 인게이지먼트 이벤트(예: 이메일 전송, 푸시 전송)를 Braze에서 Heap으로 자동 전송하여 분석할 수 있습니다.

### 1단계: Heap 자격 증명 가져오기 {#step-1-get-heap-credentials}

이 통합을 구성하려면 웹훅 엔드포인트 URL이 필요하며, Heap 계정 매니저에게 요청하여 받을 수 있습니다.

### 2단계: Braze Currents 구성 {#step-2-configure-braze-currents}

Braze에서 **파트너 통합** > **데이터 내보내기**로 이동한 후 **새 커런트 생성**을 클릭하고 **Heap Export**를 선택합니다.

내보내기에 이름을 지정한 다음 **커런트 세부 정보** 페이지로 이동합니다. 이 페이지에서 엔드포인트와 선택적 베어러 토큰(제공된 경우)을 입력합니다.

통합 자격 증명을 구성한 후, Heap으로 내보낼 메시지 인게이지먼트, 고객 행동 및 사용자 이벤트를 모두 선택하고 **커런트 시작**을 클릭합니다.

![엔드포인트, 토큰 및 이벤트 선택 필드가 있는 Braze Heap 커런트 설정 페이지.]({% image_buster /assets/img/heap/heap4.png %}){: style="max-width:90%;"}