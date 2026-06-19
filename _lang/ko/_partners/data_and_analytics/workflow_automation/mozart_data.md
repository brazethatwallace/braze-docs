---
nav_title: Mozart Data
article_title: Mozart Data
description: "이 참조 문서에서는 Braze와 올인원 최신 데이터 플랫폼인 Mozart Data 간의 파트너십을 설명합니다. Fivetran을 사용하여 Snowflake로 데이터를 가져오고, 변환을 생성하고, 데이터를 결합하는 등의 작업을 수행할 수 있습니다."
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/)는 Fivetran, Portable, Snowflake를 기반으로 하는 올인원 최신 데이터 플랫폼입니다.

Braze와 Mozart Data 통합을 통해 다음을 수행할 수 있습니다:
- Fivetran을 사용하여 Braze 데이터를 Snowflake로 가져오기
- Braze 데이터를 다른 애플리케이션 데이터와 결합하여 변환을 생성하고 사용자 행동을 효과적으로 분석하기
- Snowflake에서 Braze로 데이터를 가져와 새로운 고객 참여 기회 만들기
- Braze 데이터를 다른 애플리케이션 데이터와 결합하여 사용자 행동에 대한 보다 전체적인 이해 얻기
- 비즈니스 인텔리전스 도구와 통합하여 Snowflake에 저장된 데이터를 더 깊이 탐색하기

## 필수 조건 {#prerequisites}

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Mozart Data 계정 | 이 파트너십을 활용하려면 Mozart Data 계정이 필요합니다. [여기에서 가입하세요.](https://app.mozartdata.com/signup)|
| Snowflake 계정<br>옵션 1: 새 계정 | Mozart Data 계정 생성 과정에서 **Create a New Snowflake Account**를 선택하면 Mozart Data가 새 Snowflake 계정을 프로비저닝합니다. |
| Snowflake 계정<br>옵션 2: 기존 계정 | 조직에 이미 Snowflake 계정이 있는 경우 Mozart Data Connected 옵션을 사용할 수 있습니다.<br><br>**Already Have a Snowflake Account** 옵션을 선택하여 기존 Snowflake 계정을 연결합니다. 이 옵션을 사용하려면 계정 수준 권한이 있는 사용자가 [다음 단계를 따라야 합니다](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

이 통합은 [Braze에서 Mozart Data로](#syncing-data-from-braze-to-mozart-data) 데이터를 동기화하는 것과 [Mozart Data에서 Braze로](#syncing-data-from-mozart-data-to-braze) 데이터를 동기화하는 것 모두 지원합니다.

### Braze에서 Mozart Data로 데이터 동기화 {#syncing-data-from-braze-to-mozart-data}

#### 1단계: Braze 커넥터 설정 {#step-1-set-up-braze-connector}

1. Mozart Data에서 **Connectors**로 이동하여 **Add Connector**를 선택합니다.
2. "Braze"를 검색하고 커넥터 카드를 선택합니다.
3. Braze에서 동기화된 모든 데이터가 저장될 대상 스키마 이름을 입력합니다. 기본 스키마 이름 `braze`를 사용하는 것을 권장합니다.
4. **Add Connector**를 선택합니다.

#### 2단계: Fivetran 커넥터 양식 작성 {#step-2-fill-out-the-fivetran-connector-form}

1단계를 완료하면 Fivetran 커넥터 페이지가 열립니다. 주어진 필드를 작성한 다음 **Continue** > **Save & Test**를 선택하여 Fivetran 커넥터를 완료합니다.

Fivetran이 Braze 계정에서 Snowflake 데이터 웨어하우스로 데이터 동기화를 시작합니다. 커넥터가 동기화를 완료한 후 Mozart Data에서 쿼리 데이터에 접근할 수 있습니다.

### Mozart Data에서 Braze로 데이터 동기화 {#syncing-data-from-mozart-data-to-braze}

#### 1단계: Snowflake 데이터 웨어하우스 설정 {#step-1-set-up-a-snowflake-data-warehouse}

[클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) 안내에 따라 Snowflake 인터페이스에서 테이블, 사용자 및 권한을 설정합니다. 이 단계에는 관리자 수준의 Snowflake 접근 권한이 필요합니다.

#### 2단계: Braze에서 Snowflake 통합 설정 {#step-2-set-up-your-snowflake-integration-in-braze}

Snowflake 웨어하우스를 설정한 후 Mozart Data에서 **Integration** 페이지로 이동하여 **Braze**를 선택합니다. **Braze** 통합 화면에 Braze에 복사할 자격 증명이 표시됩니다.

![Braze가 선택된 Mozart Data 통합 페이지와 Braze에서 사용할 Snowflake 연결 자격 증명.]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

다음으로, Braze에 로그인한 상태에서 **통합 > 기술 파트너 > Snowflake**로 이동하여 통합 프로세스를 시작합니다. Mozart Data에서 자격 증명을 복사하여 Snowflake 데이터 가져오기 페이지에 추가합니다. **Set up sync details**를 선택하고 Snowflake 계정 및 소스 테이블 정보를 입력합니다.

![Mozart Data 자격 증명으로 계정, 웨어하우스, 데이터베이스 및 스키마 필드가 채워진 Braze Snowflake 파트너 통합 양식.]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

다음으로, Braze Snowflake 가져오기 구성 화면에서 동기화 이름을 선택하고 연락처 이메일을 입력한 후 데이터 유형과 동기화 빈도를 선택합니다.

#### 3단계: Braze 사용자에 공개 키 추가 {#step-3-add-a-public-key-to-the-braze-user}
이 시점에서 설정을 완료하려면 Snowflake로 돌아가야 합니다. Braze 대시보드에 표시된 공개 키를 Braze가 Snowflake에 연결하기 위해 생성한 사용자에 추가합니다.

이 작업에 대한 자세한 내용은 [Snowflake 설명서](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)를 참조하세요. 키를 교체하려는 경우 Mozart Data가 새 키 쌍을 생성하고 새 공개 키를 제공할 수 있습니다.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### 4단계: 연결 테스트 {#step-4-test-connection}

사용자가 공개 키로 업데이트되면 Braze 대시보드로 돌아가서 **Test connection**을 선택합니다. 성공하면 데이터 미리보기가 표시됩니다. 어떤 이유로든 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

![공개 키 적용 후 성공적인 미리보기를 보여주는 Braze Snowflake 통합 연결 테스트 결과.]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
통합이 초안에서 활성 상태로 전환되려면 먼저 테스트를 성공적으로 완료해야 합니다. 생성 페이지를 닫아야 하는 경우 통합이 저장되며, 세부 정보 페이지를 다시 방문하여 변경하고 테스트할 수 있습니다.
{% endalert %}

## 이 통합 사용하기 {#using-this-integration}

### Mozart Data 사용자로서 Braze 데이터에 접근하는 방법 {#how-to-access-braze-data-as-a-mozart-data-user}
Mozart Data 계정을 성공적으로 생성하면 Mozart Data에서 Snowflake 데이터 웨어하우스로 동기화된 Braze 데이터에 접근할 수 있습니다.

#### 변환 {#transforms}
Mozart Data는 사용자가 뷰 또는 테이블을 생성할 수 있도록 SQL 변환 레이어를 제공합니다. 사용자 수준의 차원 테이블(예: `dim_users`)을 생성하여 각 사용자의 제품 사용 데이터, 트랜잭션 기록 및 Braze 메시지와의 참여 활동을 요약할 수 있습니다.

#### 분석 {#analysis}
Braze에서 동기화된 변환 모델 또는 원시 데이터를 사용하여 Braze 메시지에 대한 사용자의 참여를 분석할 수 있습니다. 또한 Braze 데이터를 다른 애플리케이션 데이터와 결합하여 Braze 메시지와의 사용자 상호작용에서 얻은 인사이트가 사용자에 대해 보유하고 있는 다른 데이터와 어떻게 관련되는지 분석할 수 있습니다. 예를 들어, 인구통계 정보, 쇼핑 기록, 제품 사용 및 고객 서비스 참여 등이 있습니다.

이를 통해 사용자 유지율을 개선하기 위한 참여 전략에 대해 보다 정보에 기반한 의사결정을 내릴 수 있습니다. 이 모든 작업은 Mozart Data의 인터페이스에서 쿼리 도구를 사용하여 수행할 수 있으며, 결과를 Google Sheet 또는 CSV로 내보내 프레젠테이션을 준비할 수 있습니다.

#### 비즈니스 인텔리전스(BI) {#business-intelligence-bi}
인사이트를 시각화하고 다른 팀원과 공유할 준비가 되셨나요? Mozart Data는 거의 모든 BI 도구와 통합됩니다. 아직 BI 도구가 없는 경우 Mozart Data에 문의하여 무료 Metabase 계정을 설정하세요.