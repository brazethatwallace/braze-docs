---
nav_title: Census
article_title: Census 코호트 가져오기
description: "이 참고 문서에서는 클라우드 데이터 웨어하우스의 데이터를 사용하여 타겟 사용자 세그먼트를 동적으로 생성할 수 있는 데이터 통합 플랫폼인 Census의 코호트 가져오기 기능에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Census 코호트 가져오기 {#census-cohort-import}

> 이 문서에서는 [Census](https://www.getcensus.com/)에서 Braze로 사용자 코호트를 가져오는 방법을 설명합니다. Census 통합에 대한 자세한 내용은 [Census 기본 문서]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census)를 참조하세요.

## 코호트 가져오기 통합 {#cohort-import-integration}

### 1단계: Braze 서비스 연결 생성 {#step-1-create-braze-service-connection}

Census 플랫폼에서 Census를 통합하려면 **Connections** 탭으로 이동하여 **New Destination**을 선택하고 새 Braze 서비스 연결을 생성합니다.

표시되는 프롬프트에서 이 연결의 이름을 지정하고 Braze 엔드포인트 URL, Braze REST API 키, 데이터 가져오기 키를 입력합니다. 데이터 가져오기 키는 코호트를 동기화하는 데 필요하며, Braze에서 **파트너 통합** > **기술 파트너** > **Census**로 이동하여 찾을 수 있습니다.

![Braze 코호트 가져오기 자격 증명이 구성된 Census 새 대상 대화 상자.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### 2단계: Census 동기화 생성 {#step-2-create-a-census-sync}

고객을 Braze에 동기화하려면 동기화를 구축해야 합니다. 여기에서 데이터를 동기화할 위치와 두 플랫폼 간에 필드를 매핑하는 방법을 정의합니다.

1. **Syncs** 탭으로 이동하여 **New Sync**를 선택합니다.<br><br>
2. 작성기에서 데이터 웨어하우스의 소스 데이터 모델을 선택합니다.<br><br>
3. 모델이 동기화될 위치를 구성합니다. 대상으로 **Braze**를 선택하고 동기화할 오브젝트로 **User & Cohort**를 선택합니다.<br>!['대상 선택' 프롬프트에서 'Braze'가 연결로 선택되고 다양한 오브젝트가 나열됩니다.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. 코호트에 추가할 사용자를 식별하는 **Source Column**을 선택하고, **식별자 유형**으로 **External User ID**를 선택합니다.<br><br>
5. **Cohort Name** 드롭다운에서 코호트를 선택하거나, 코호트를 생성하거나, 코호트 이름을 채울 Source Column을 선택합니다.<br><br>
6. **When a record is removed from source data** 드롭다운을 사용하여 소스 데이터셋에서 사용자가 제거될 때 수행할 작업을 선택합니다. 예를 들어 **Do nothing** 또는 **Remove matching record from cohort** 등이 있습니다.<br><br>
7. 마지막으로, Census 데이터 필드를 해당하는 Braze 필드에 매핑합니다.<br>![Census 매핑 구성 화면.]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
8. 세부 사항을 확인하고 동기화를 생성합니다.

이제 동기화를 실행할 수 있습니다!

동기화 중에 매핑한 모든 필드가 먼저 사용자 오브젝트에 동기화되어 Braze에 이미 존재하는 항목을 업데이트합니다. 그런 다음 업데이트된 사용자가 지정된 코호트에 추가됩니다.

동기화 후에는 Census 코호트 필터가 포함된 Braze 세그먼트를 생성하여 향후 Braze Campaigns 및 Canvases에 추가하고 해당 사용자를 타겟팅할 수 있습니다.

{% alert note %}
Census와 Braze 통합을 사용할 때 Census는 각 동기화 시 델타(변경된 데이터)만 Braze에 전송합니다.
{% endalert %}

{% alert important %}
Braze에 이미 존재하는 사용자만 코호트에 추가하거나 제거할 수 있습니다. 코호트 가져오기는 Braze에 새 사용자를 생성하지 않습니다.
{% endalert %}

## 사용자 매칭 {#user-matching}

식별된 사용자는 `external_id` 또는 `alias`로 매칭할 수 있습니다. 익명 사용자는 `device_id`로 매칭할 수 있습니다. 원래 익명 사용자로 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.