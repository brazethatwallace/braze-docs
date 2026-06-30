---
nav_title: 계정 기반 세분화
article_title: 계정 기반 세분화 설정
page_order: 2
page_type: reference
description: "다양한 Braze 기능을 사용하여 B2B 계정 기반 세분화 사용 사례를 지원하는 방법을 알아보세요."
---

# 계정 기반 세분화 설정 {#set-up-account-based-segmentation}

> 이 페이지에서는 B2B 계정 기반 세분화 사용 사례를 지원하기 위해 다양한 Braze 기능을 사용하는 방법을 보여줍니다.

[B2B 데이터 모델]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models) 설정 방식에 따라 두 가지 방법으로 B2B 계정 기반 세분화를 수행할 수 있습니다:

- [비즈니스 오브젝트에 카탈로그를 사용하는 경우](#option-1-when-using-catalogs-for-your-business-objects)
- [비즈니스 오브젝트에 연결된 소스를 사용하는 경우](#option-2-when-using-connected-sources-for-your-business-objects)

## B2B 계정 기반 세분화 설정 {#setting-up-b2b-account-based-segmentation}

### 옵션 1: 비즈니스 오브젝트에 카탈로그를 사용하는 경우 {#option-1-when-using-catalogs-for-your-business-objects}

#### 기본 SQL 템플릿 세분화 {#basic-sql-template-segmentation}

시작하는 데 도움이 되도록 간단한 계정 기반 세분화를 위한 기본 SQL 템플릿을 만들었습니다.

타겟 엔터프라이즈 계정의 직원인 사용자를 세분화하고자 한다고 가정해 보겠습니다.

1. **오디언스** > **세그먼트 확장** > **새 확장 만들기** > **템플릿으로 시작**으로 이동한 다음 **이벤트용 카탈로그 세그먼트** 템플릿을 선택합니다. <br><br> ![이벤트 또는 구매용 카탈로그 세그먼트 옵션이 있는 "템플릿 선택" 모달.]({% image_buster /assets/img/b2b/select_a_template.png %})<br><br>SQL 편집기에 사용자 이벤트 데이터와 카탈로그 데이터를 조인하여 특정 카탈로그 항목에 참여한 사용자를 세분화하는 템플릿이 자동으로 채워집니다. <br><br>!["변수" 탭이 열려 있는 새 확장용 SQL 편집기.]({% image_buster /assets/img/b2b/enter_new_name.png %})<br><br>
2. 세그먼트를 생성하기 전에 **변수** 탭을 사용하여 템플릿에 필요한 필드를 입력합니다.<br><br>Braze가 카탈로그 항목에 대한 참여를 기반으로 사용자를 식별하려면 다음을 수행해야 합니다:
- 카탈로그 필드가 포함된 카탈로그를 선택합니다
- 이벤트 속성정보가 포함된 커스텀 이벤트를 선택합니다
- 카탈로그 필드와 이벤트 속성정보 값을 일치시킵니다

##### B2B 사용 사례를 위한 변수 가이드라인 {#variables-guidelines-for-b2b-use-cases}

B2B 계정 기반 세분화 사용 사례에 대해 다음 변수를 선택합니다:

| 변수 | 등록정보 |
| --- | --- |
| 카탈로그 | 계정 카탈로그 |
| 카탈로그 필드 | ID |
| 커스텀 이벤트 | account_linked |
| 커스텀 이벤트 속성정보 | account_id |
| (SQL 결과 필터 아래) 카탈로그 필드 | 분류 |
| (SQL 결과 필터 아래) 값 | 엔터프라이즈 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="B2B 사용 사례를 위한 변수 가이드라인" }

#### 정교한 SQL 세분화 {#sophisticated-sql-segmentation}

보다 정교하거나 복잡한 세분화는 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)을 참조하세요. 시작하는 데 도움이 되도록 B2B 계정 기반 세분화에 활용할 수 있는 몇 가지 SQL 템플릿을 소개합니다:

1. 단일 카탈로그에서 두 개의 필터를 비교하는 세그먼트를 만듭니다(예: 엔터프라이즈급 계정의 레스토랑 업계에 종사하는 사용자). 카탈로그 ID와 항목 ID를 포함해야 합니다.

```sql
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_accounts.Classification = 'Enterprise'
;
```

{: start="2"}
2. 두 개의 개별 카탈로그에서 두 개의 필터를 비교하는 세그먼트를 만듭니다(예: "Stage 3" 기회가 열려 있는 엔터프라이즈 타겟 계정과 연결된 사용자).

```sql
-- Reformat catalog data into a table with columns for each field
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
),
salesforce_opportunities AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Account_ID' THEN FIELD_VALUE END) AS Account_ID,
       MAX(CASE WHEN FIELD_NAME = 'Stage' THEN FIELD_VALUE END) AS Stage,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655f84a348f0f0059ad0627' -- salesforce_opportunities
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
JOIN salesforce_opportunities
ON salesforce_accounts.id = salesforce_opportunities.Account_ID
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_opportunities.Stage = 'Closed Won'
;
```

### 옵션 2: 비즈니스 오브젝트에 연결된 소스를 사용하는 경우 {#option-2-when-using-connected-sources-for-your-business-objects}

세분화에서 연결된 소스를 사용하는 방법에 대한 기본 사항은 [CDI 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)을 참조하세요. 소스 테이블의 형식은 원하는 방식으로 자유롭게 지정할 수 있으므로, [카탈로그 사용 시](#option-1-when-using-catalogs-for-your-business-objects)에서 다루는 템플릿을 참고하세요.

## 세그먼트에서 계정 기반 확장 사용 {#using-your-account-based-extension-in-a-segment}

위 단계에서 계정 수준 세분화를 생성한 후에는 해당 세그먼트 확장을 타겟팅 기준에 바로 적용할 수 있습니다. 역할, 이전 Campaign 참여도 등과 같은 추가 사용자 인구통계학적 기준을 레이어링하는 것도 간편합니다. 자세한 내용은 [세그먼트에서 확장 사용하기]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment)를 참조하세요.