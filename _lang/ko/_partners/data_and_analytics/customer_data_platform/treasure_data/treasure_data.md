---
nav_title: Treasure Data
article_title: Treasure Data
description: "이 참조 문서에서는 Braze와 Treasure Data 간의 파트너십을 설명합니다. Treasure Data는 작업 결과를 Braze에 직접 기록할 수 있는 엔터프라이즈 고객 데이터 플랫폼입니다."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# Treasure Data

> [Treasure Data](https://www.treasuredata.com/)는 여러 소스에서 정보를 수집하고 마케팅 스택의 다양한 위치로 라우팅하는 고객 데이터 플랫폼(고객 데이터 플랫폼)입니다.

Braze와 Treasure Data 통합을 사용하면 Treasure Data의 작업 결과를 Braze에 직접 기록할 수 있으며, 다음과 같은 작업이 가능합니다.
* **외부 ID 매핑**: 고객 관계 관리 시스템에서 Braze 사용자 계정에 ID를 매핑합니다.
* **수신 거부 관리**: 최종 사용자가 참여하지 않기로 동의를 업데이트하는 경우입니다.
* **이벤트, 구매 또는 커스텀 프로필 속성 추적 업로드**. 이 정보는 Campaign(캠페인)의 사용자 경험을 향상시키는 정밀한 고객 세그먼트를 구축하는 데 도움이 됩니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Treasure Data 계정 | 이 파트너십을 활용하려면 [Treasure Data 계정](https://www.treasuredata.com/custom-demo/)이 필요합니다. |
| Braze REST API 키 | `users.track`, `users.delete`, `users.alias.new`, `users.identify` 권한이 있는 Braze REST API 키.<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints))에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 사용 사례 {#use-cases}

Treasure Data에서 통합된 고객 프로필을 Braze로 동기화하여 타겟 세그먼트를 구축할 수 있습니다. Treasure Data는 퍼스트파티 쿠키 데이터, 모바일 ID, CRM과 같은 서드파티 시스템 등을 지원합니다.

## 통합 {#integration}

### 1단계: 새 연결 생성 {#step-1-create-a-new-connection}

Treasure Data에서 **Integrations Hub** 아래의 **Catalog**로 이동하여 **Braze**를 검색하고 선택합니다.

표시되는 **New Authentication** 프롬프트에서 연결 이름을 지정하고 Braze REST API 키와 REST 엔드포인트를 입력합니다. 완료되면 **Done**을 선택합니다.

![REST API 키 및 엔드포인트 필드가 있는 Treasure Data Braze 인증 양식.]({% image_buster /assets/img/treasure_data/braze_authentication.png %}){: style="max-width:80%;"}

### 2단계: 쿼리 정의 {#step-2-define-your-query}

Treasure Data에서 **Data Workbench** 아래의 **Queries**로 이동하여 데이터를 내보낼 쿼리를 선택합니다. 이 쿼리를 실행하여 결과 세트를 검증합니다.

{% alert note %}
HIVE를 사용하여 쿼리를 작성하는 사용자의 경우, HIVE에서는 밑줄로 시작하는 열이나 테이블을 백쿼트로 감싸야 합니다. 예를 들어, `_merge_objects`와 같이 사용합니다.
{% endalert %}

다음으로, **Export Results**를 선택하고 기존 통합 인증을 선택합니다.

![Export Results 및 Braze 통합이 선택된 Treasure Data 쿼리 결과 페이지.]({% image_buster /assets/img/treasure_data/query_2.png %}){: style="max-width:80%;"}

다음 [커스터마이제이션 섹션](#customization)에 설명된 대로 추가 내보내기 결과 매개변수를 정의합니다. 내보내기 통합 콘텐츠에서 통합 매개변수를 검토합니다.

![내보내기 결과 페이지. 이 페이지에는 '모드', '추적 레코드 유형' 및 '미리 서식 지정된 필드'에 대한 필드가 있습니다. 이 예제에서는 'User-Track' 및 'Custom Events'가 각각 이 필드에 설정되어 있습니다.]({% image_buster /assets/img/treasure_data/braze_export_configuration.png %}){: style="max-width:80%;"}

마지막으로, **Done**을 선택하고 쿼리를 실행한 다음, 데이터가 Braze로 이동했는지 확인합니다.

### 커스터마이제이션 {#customization}

내보내기 결과 매개변수는 다음 표에 포함되어 있습니다.

| 매개변수 | 값 | 설명 |
|---------------------------|---|---|
| `mode` | User - New Alias<br>User - Identifying<br>User - Track<br>User - Delete | 커넥터 모드 |
| `pre_formatted_fields` | 문자열 | 배열 또는 JSON 열의 형식을 유지하려면 사용합니다. |
| `track_record_type` | Custom Events<br>Purchases<br>User Profile Attributes | **User - Track** 모드의 레코드 유형 |
| `skip_on_invalid_records` | 부울 | 활성화하면 JSON 열의 잘못된 레코드를 무시하고 계속 진행합니다. <br> 그렇지 않으면 작업이 중지됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="커스터마이제이션" }

{% alert note %}
미리 서식 지정된 필드, 예제 쿼리, 매개변수 세부 정보 및 쿼리 내보내기 작업 스케줄링에 대한 자세한 내용은 [Treasure Data](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration)를 참조하세요.
{% endalert %}

## 웹훅 {#webhooks}

Treasure Data 사용자는 공개 REST API를 통해 데이터를 수집할 수 있습니다. Treasure Data를 사용하여 데이터에 대한 커스텀 웹훅을 생성할 수 있습니다. 자세한 내용은 [Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API)를 참조하세요.