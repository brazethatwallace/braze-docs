---
nav_title: Grouparoo
page_order: 1
page_type: update
noindex: true
description: "이 문서에서는 데이터 웨어하우스의 데이터로 마케팅, 영업, 고객지원 도구를 강화하는 데 사용되는 오픈 소스 리버스 ETL 도구인 Braze와 Grouparoo의 파트너십에 대해 설명합니다."

---

# Grouparoo

{% alert update %}
Grouparoo에 대한 지원은 2022년 4월부터 중단되었습니다.
{% endalert %}

> [Grouparoo](https://www.grouparoo.com/)는 데이터 웨어하우스에서 마케팅, 영업, 고객지원 도구로 데이터를 동기화하는 오픈 소스 리버스 ETL 도구입니다. 모델 중심의 UI를 통해 기술 전문가가 아닌 팀원도 데이터 동기화를 구성하고 스케줄할 수 있습니다.

Braze와 Grouparoo 통합은 데이터 웨어하우스 데이터를 Braze에 동기화합니다. 자동 동기화 스케줄을 통해 고객 커뮤니케이션을 최신 정보로 유지할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Grouparoo 계정 및 프로젝트 | 이 파트너십을 활용하려면 Grouparoo 계정과 프로젝트가 필요합니다.<br><br>이 통합은 Grouparoo에서 제공하는 무료 커뮤니티 에디션 및 엔터프라이즈 솔루션과 함께 사용할 수 있습니다. 설정은 Grouparoo 구성 사용자 인터페이스에서 이루어집니다. |
| Braze REST API 키 | 사용자 및 추적 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL](https://www.grouparoo.com/). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Grouparoo에서 Braze 앱 만들기 {#step-1-create-a-braze-app-in-grouparoo}

Grouparoo에서 **Apps**로 이동하여 **Braze**를 선택해 새 Braze 앱을 만듭니다. 표시되는 모달에서 Braze API 키와 REST 엔드포인트를 입력합니다.

![Braze API 키와 REST 엔드포인트 필드가 있는 Grouparoo의 Braze 앱 생성 모달.]({% image_buster /assets/img/grouparoo/add-app.png %})

### 2단계: 모델 및 데이터 소스 설정 {#step-2-set-up-a-model-and-data-source}

이 통합을 사용하려면 다음 단계로 진행하기 전에 기존 모델과 데이터 소스가 설정되어 있어야 합니다. 아직 설정하지 않았다면 Grouparoo 설명서를 방문하여 [모델](https://www.grouparoo.com/docs/config/models) 및 [데이터 소스](https://www.grouparoo.com/docs/config/sources) 설정 방법을 확인하세요.

### 3단계: Grouparoo에서 Braze 대상 생성 {#step-3-create-a-braze-destination-in-grouparoo}

#### 동기화 모드 선택 {#select-sync-mode}

Grouparoo에서 내비게이션 바의 모델을 선택합니다. 그런 다음 **Destinations** 섹션으로 스크롤하여 **Add new Destination**을 클릭합니다.

다음으로, 생성한 **Braze** 앱을 선택하고 대상 이름을 지정한 후 원하는 동기화 모드를 선택합니다.
- **Sync**: 필요에 따라 회사 사용자를 추가, 업데이트 및 제거합니다. 이 옵션은 새 레코드, 기존 레코드의 변경 사항 및 삭제를 감지합니다.
- **Additive**: 필요에 따라 회사 사용자를 추가 및 업데이트하지만 제거하지는 않습니다. 이 옵션은 Braze에 추가할 새 사용자와 기존 회사 사용자의 변경 사항을 감지하지만 삭제는 추적하지 않습니다.
- **Enrich**: Braze에 이미 존재하는 사용자만 업데이트합니다. 사용자를 추가하거나 제거하지 않습니다. 이 옵션은 Braze의 기존 사용자만 업데이트합니다.

#### 등록정보 필드 매핑 {#property-field-mapping}

다음으로, Grouparoo 등록정보 필드를 Braze 등록정보 필드에 매핑해야 합니다.

![등록정보 매핑 필드 예시. Grouparoo userID가 external_id에 매핑되도록 설정되어 있습니다. email, firstName, lastName은 각각 동일한 "email", "first_name", "last_name" Grouparoo 필드로 설정되어 있습니다.]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Braze `external_id` 필드가 소스 테이블의 기본 키에 매핑되어 있는지 확인하세요. 사용 사례에 맞게 나머지 필드를 매핑합니다.

**Send Record Properties** 섹션: 데이터를 매핑할 수 있는 미리 설정된 고객 프로필 필드 목록입니다. 이 중 어느 것이든 Grouparoo 등록정보에서 동기화할 수 있습니다.

**Optional Braze User Profile Fields** 섹션: 선택적 커스텀 Braze 고객 프로필 필드를 생성합니다. **Add New Braze User Profile Field**를 클릭하면 Braze에 매핑할 수 있는 모든 사용 가능한 등록정보를 볼 수 있습니다. 새로 만드는 필드의 이름은 Grouparoo 등록정보와 동일하지만 이름을 변경할 수 있습니다.

#### Grouparoo 그룹 {#grouparoo-groups}

매핑 외에도 Grouparoo 그룹을 Braze 구독 그룹에 추가할 수도 있습니다.

![Grouparoo 대상 구성 창의 "Braze Subscription Groups"에서 "High value with recent automotive purchase" Grouparoo 그룹이 "High value with recent automotive purchase" Braze 구독 그룹에 추가됩니다.]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
이 통합에 대한 추가 세부 정보 및 업데이트는 [Grouparoo 설명서](https://www.grouparoo.com/docs/integrations/grouparoo-braze)에서 확인할 수 있습니다.
{% endalert %}