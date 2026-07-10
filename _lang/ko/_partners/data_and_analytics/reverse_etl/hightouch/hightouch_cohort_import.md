---
nav_title: Hightouch 코호트 가져오기
article_title: Hightouch 코호트 가져오기
description: "이 참조 문서에서는 웨어하우스의 고객 데이터를 비즈니스 도구로 동기화하는 플랫폼인 Hightouch의 코호트 가져오기 기능에 대해 설명합니다."
page_type: partner
search_tag: Partner

---
# Hightouch 코호트 가져오기 {#hightouch-cohort-import}

> 이 문서에서는 [Hightouch](https://hightouch.io)에서 Braze로 사용자 코호트를 가져와 웨어하우스에만 존재할 수 있는 데이터를 기반으로 타겟팅된 Campaign을 보내는 방법을 설명합니다. Hightouch 통합 및 기타 기능에 대한 자세한 내용은 [Hightouch 기본 문서]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch)를 참조하세요.

## 데이터 가져오기 통합 {#data-import-integration}

### 1단계: Braze 데이터 가져오기 키 가져오기 {#step-1-get-the-braze-data-import-key}
Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Hightouch**를 선택합니다.

여기에서 REST 엔드포인트를 확인하고 Braze 데이터 가져오기 키를 생성할 수 있습니다. 키가 생성되면 새 키를 만들거나 기존 키를 무효화할 수 있습니다.<br><br>![REST 엔드포인트와 데이터 가져오기 키 컨트롤이 표시된 Braze Hightouch 기술 파트너 페이지.]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"}

### 2단계: Hightouch에서 Braze 코호트를 대상으로 추가하기 {#step-2-add-braze-cohorts-as-a-destination-in-hightouch}
Hightouch 워크스페이스의 **Destination** 페이지로 이동하여 **Braze Cohorts**를 검색하고 **Continue**를 클릭합니다. 그런 다음 REST 엔드포인트와 데이터 가져오기 키를 입력하고 **Continue**를 클릭합니다.<br><br>![자격 증명 필드가 있는 Braze Cohorts용 Hightouch 대상 설정 화면.]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### 3단계: 모델(또는 오디언스)을 Braze 코호트에 동기화하기 {#step-3-sync-a-model-or-audience-into-braze-cohorts}
Hightouch에서 생성한 [모델](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) 또는 [오디언스](https://hightouch.io/docs/audiences/usage/)를 사용하여 새 동기화를 만듭니다. 다음으로, 이전 단계에서 만든 Braze Cohorts 대상을 선택합니다. 마지막으로, Braze Cohorts 대상 구성에서 매칭할 식별자를 선택하고 Hightouch가 새 Braze 코호트를 생성할지 기존 코호트를 업데이트할지 결정합니다.<br><br>![매칭 식별자 및 코호트 옵션이 있는 Hightouch Braze Cohorts 동기화 구성 화면.]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Braze에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에 새 사용자를 생성하지 않습니다.
{% endalert %}

### 4단계: Hightouch 커스텀 오디언스에서 Braze Segment 만들기 {#step-4-create-a-braze-segment-from-the-hightouch-custom-audience}
Braze에서 **Segments**로 이동하여 새 Segment를 만들고 필터로 **Hightouch Cohorts**를 선택합니다. 여기에서 포함할 Hightouch 코호트를 선택할 수 있습니다. Hightouch 코호트 Segment가 생성되면 Campaign 또는 Canvas를 만들 때 오디언스 필터로 선택할 수 있습니다.<br><br>![Hightouch Cohorts 필터를 사용하는 Braze Segment 빌더.]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### 이 통합 사용하기 {#using-this-integration}
Hightouch Segment를 사용하려면 Braze Campaign 또는 Canvas를 만들고 해당 Segment를 타겟 오디언스로 선택합니다.<br><br>![Hightouch 기반 Segment가 선택된 Braze 오디언스 타겟팅 단계.]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## 사용자 매칭 {#user-matching}

식별된 사용자는 `external_id` 또는 `alias`로 매칭할 수 있습니다. 익명 사용자는 `device_id`로 매칭할 수 있습니다. 원래 익명 사용자로 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.