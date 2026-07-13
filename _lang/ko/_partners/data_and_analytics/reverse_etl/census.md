---
nav_title: Census
article_title: Census
description: "이 참조 문서에서는 클라우드 데이터 웨어하우스의 데이터를 사용하여 타겟 사용자 세그먼트를 동적으로 생성할 수 있는 데이터 통합 플랫폼인 Census와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census](https://www.getcensus.com/)는 Snowflake 및 BigQuery와 같은 클라우드 데이터 웨어하우스를 Braze에 연결하는 데이터 활성화 플랫폼입니다. 마케팅 팀은 퍼스트파티 데이터의 힘을 활용하여 동적 오디언스 세그먼트를 구축하고, 고객 속성을 동기화하여 개인화된 캠페인을 만들고, Braze의 모든 데이터를 최신 상태로 유지할 수 있습니다. 신뢰할 수 있고 실행 가능한 데이터로 조치를 취하는 것이 그 어느 때보다 쉬워졌습니다. CSV 업로드나 엔지니어링 지원이 필요하지 않습니다.

Braze와 Census 통합을 사용하면 오디언스 또는 제품 데이터를 Braze로 동적으로 가져와 개인화된 캠페인을 보낼 수 있습니다. 예를 들어, Braze에서 "CLV > 1000인 뉴스레터 구독자" 코호트를 생성하여 고가치 고객을 타겟팅하거나, "최근 30일 이내 활성 사용자" 코호트를 생성하여 특정 사용자를 타겟팅하여 예정된 베타 기능을 테스트할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Census 계정 | 이 파트너십을 활용하려면 [Census 계정](https://www.getcensus.com/)이 필요합니다. |
| Braze REST API 키 | 모든 사용자 데이터 권한(`users.delete` 제외)과 `segments.list` 권한이 있는 Braze REST API 키. Census가 더 많은 Braze 오브젝트를 지원함에 따라 권한 세트가 변경될 수 있으므로, 지금 더 많은 권한을 부여하거나 향후 이러한 권한을 업데이트할 계획을 세울 수 있습니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)에 따라 달라집니다. |
| 데이터 웨어하우스 및 데이터 모델 | 통합을 시작하기 전에 Census에 데이터 웨어하우스를 설정하고 Braze에 동기화할 데이터의 하위 집합 모델을 정의해야 합니다. 사용 가능한 데이터 소스 목록과 모델 생성 안내는 [Census 설명서](https://docs.getcensus.com/destinations/braze)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Braze 서비스 연결 생성 {#step-1-create-braze-service-connection}

Census 플랫폼에서 Census를 통합하려면 **Connections** 탭으로 이동하여 **New Destination**을 선택하여 새 Braze 서비스 연결을 생성합니다.

표시되는 프롬프트에서 이 연결의 이름을 지정하고 Braze 엔드포인트 URL과 Braze REST API 키를 입력합니다(선택적으로 코호트를 동기화하기 위한 데이터 가져오기 키도 입력할 수 있습니다).

![Braze 연결 자격 증명이 구성된 Census 새 대상 대화 상자.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### 2단계: Census 동기화 생성 {#step-2-create-a-census-sync}

고객을 Braze에 동기화하려면 동기화를 구축해야 합니다. 여기에서 데이터를 동기화할 위치와 두 플랫폼 간에 필드를 매핑하는 방법을 정의합니다.

1. **Syncs** 탭으로 이동하여 **New Sync**를 선택합니다.<br><br>
2. 작성기에서 데이터 웨어하우스의 소스 데이터 모델을 선택합니다.<br><br>
3. 모델이 동기화될 위치를 구성합니다. 대상으로 **Braze**를 선택하고 동기화할 [지원되는 오브젝트 유형](#supported-objects)을 선택합니다.<br>!['대상 선택' 프롬프트에서 'Braze'가 연결로 선택되고 다양한 오브젝트가 나열됩니다.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. 적용할 동기화 규칙을 선택합니다. **Update or Create**가 가장 일반적인 선택이지만, 데이터 삭제 등을 처리하기 위해 고급 규칙을 선택할 수도 있습니다.<br><br>
5. 다음으로, 레코드 매칭을 위해 동기화 키를 선택하여 Braze 오브젝트를 모델 필드에 [매핑](#supported-objects)합니다.<br>!["동기화 키 선택" 프롬프트에서 Braze의 "External User ID"가 소스의 "user_id"와 매칭됩니다.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. 마지막으로, Census 데이터 필드를 해당하는 Braze 필드에 매핑합니다.<br>![Census 매핑]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. 세부 정보를 확인하고 동기화를 생성합니다.

동기화가 실행된 후 Braze에서 사용자 데이터를 확인할 수 있습니다. 이제 Braze Segment를 생성하고 향후 Braze Campaigns 및 Canvases에 추가하여 이러한 사용자를 타겟팅할 수 있습니다.

{% alert note %}
Census와 Braze 통합을 사용할 때, Census는 각 동기화 시 델타(변경된 데이터)만 Braze에 전송합니다.
{% endalert %}

## 지원되는 오브젝트 {#supported-objects}

Census는 현재 다음 Braze 오브젝트의 동기화를 지원합니다:

| 오브젝트 이름 | 동기화 동작 |
| --- | --- |
| User | Update, Create, Mirror, Delete |
| Cohort | Update, Create, Mirror |
| Catalog | Update, Create, Mirror |
| Subscription Group Membership | Mirror |
| Event | Append |
{: .reset-td-br-1 .reset-td-br-2 aria-label="지원되는 오브젝트" }

또한 Census는 Braze에 [구조화된 데이터](https://docs.getcensus.com/destinations/braze#supported-objects)를 전송하는 것을 지원합니다:
- 사용자 푸시 토큰: 푸시 토큰을 전송하려면 데이터가 2~3개의 값(`app_id`, `token`, 선택 사항인 `device_id`)을 가진 오브젝트 배열로 구조화되어야 합니다.
- 중첩 커스텀 속성: 오브젝트와 배열 모두 지원됩니다. 2022년 4월 기준으로 이 기능은 아직 얼리 액세스 단계입니다. 액세스하려면 Braze 계정 매니저에게 문의해야 할 수 있습니다.