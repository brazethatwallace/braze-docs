---
nav_title: Braze가 Currents를 사용하는 방법
article_title: Braze가 Currents를 사용하는 방법
page_order: 6
page_type: tutorial
description: "이 Currents 사용법 문서에서는 이벤트 데이터에 대한 적절한 수집을 설정하고 데이터베이스 및 비즈니스 인텔리전스(BI) 도구로 데이터를 이동하는 기본 프로세스를 안내합니다."
tool: Currents

---

# Braze가 Currents를 사용하는 방법 {#how-braze-uses-currents}

> Braze는 엄선된 [파트너]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)와 함께 내부적으로 Currents를 사용합니다.

이메일 및 푸시 Campaign에서 데이터를 필터링하여 비즈니스 인사이트 도구인 Looker로 전송하지만, 그 경로가 약간 다릅니다. 추출, 변환, 로드(ETL) 방법론의 역방향 버전인 추출, 로드, 변환(ELT)으로 순서를 전환하여 사용합니다.

## 1단계: 이벤트 데이터 수집 및 집계 {#step-1-intake-and-aggregate-event-data}

Campaigns나 Canvas와 같은 참여 툴을 사용하여 Campaign을 시작한 후에는 자체 시스템과 이메일 파트너의 일부 시스템을 사용하여 이벤트 데이터를 추적합니다. 이 데이터 중 일부는 집계되어 대시보드에 표시되지만, 더 자세히 살펴보고 싶습니다!

## 2단계: 이벤트 데이터를 데이터 저장 파트너에게 전송 {#step-2-send-event-data-to-a-data-storage-partner}

Currents를 설정하여 Braze 이벤트 데이터를 Amazon S3로 전송하여 저장 및 추출합니다. [Athena](https://aws.amazon.com/athena/)를 S3 위에 올려 쿼리를 실행할 수 있다는 것도 알고 있습니다. 단기적으로 훌륭한 솔루션입니다. 하지만 관계형 데이터베이스와 비즈니스 인텔리전스/분석 도구를 사용하는 장기적인 솔루션을 원했습니다. (여러분에게도 동일한 방법을 권장합니다.)

S3는 데이터 이동, 피벗, 분석을 위한 유연한 스토리지 및 라우팅 옵션을 제공합니다. 특정 구조를 유지하기 때문에 S3에서 데이터를 변환하지 않습니다.

## 3단계: 관계형 데이터베이스로 이벤트 데이터 변환 {#step-3-transform-event-data-with-a-relational-database}

S3에서 웨어하우스([Snowflake 데이터 공유](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) 또는 Snowflake Reader 계정, Braze의 경우)를 선택합니다. 거기서 데이터를 변환한 다음 Looker로 이동하여 데이터의 구조와 조직을 설정할 블록을 구성합니다.

Snowflake가 유일한 웨어하우스 옵션은 아닙니다. 다른 옵션으로는 [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE) 등이 있습니다!

### Snowflake Reader 계정 {#snowflake-reader-accounts}

Snowflake Reader 계정은 Snowflake 계정이나 Snowflake와의 고객 관계 없이도 [Snowflake 데이터 공유]({{site.baseurl}}/partners/snowflake)와 동일한 데이터 및 기능에 접근할 수 있도록 해줍니다. Reader 계정을 사용하면 Braze가 계정을 생성하고 데이터를 공유하며, 로그인하여 데이터에 접근할 수 있는 자격 증명을 제공합니다. 이를 통해 모든 데이터 공유 및 사용 요금이 전적으로 Braze에서 처리됩니다.

자세한 내용은 고객 성공 매니저에게 문의하세요.

#### 추가 리소스 {#additional-resources}
유용한 사용량 모니터링 리소스는 Snowflake의 [Resource Monitors](https://docs.snowflake.com/en/user-guide/resource-monitors.html) 및 [Viewing Warehouse Credit Usage](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account) 문서를 확인하세요.

## 4단계: 비즈니스 인텔리전스(BI) 도구를 사용하여 데이터 조작 {#step-4-use-a-business-intelligence-bi-tool-to-manipulate-your-data}

마지막으로, [Looker 및 Looker 블록](https://www.marketplace.looker.com/)을 사용하여 BI 도구로 데이터를 분석하고, 차트 및 기타 시각적 도구로 변환합니다. 이렇게 하면 Currents에서 데이터가 이동할 때마다 ETL이나 ELT를 수행할 필요가 없습니다.

영감을 받으셨나요? 아래 문서를 확인하여 이에 대한 자세한 정보와 데이터베이스를 구축하는 데 어떻게 활용할 수 있는지 알아보세요!

- [User Behavior Block](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Message Engagement Block](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)