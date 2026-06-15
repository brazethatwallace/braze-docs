---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "이 참조 문서에서는 의사결정 인텔리전스 및 증강 분석 플랫폼인 Braze와 Tellius의 파트너십에 대해 설명합니다. BI 엔지니어에 의존하지 않고 데이터를 활용하여 대시보드를 구축하고 인사이트를 생성하여 더 나은 마케팅 의사결정을 내릴 수 있습니다."
page_type: partner
search_tag: Partner

---

# Tellius

> [Tellius](https://www.tellius.com/)는 의사결정 인텔리전스 및 증강 분석 플랫폼으로, 자연어 검색을 사용하여 데이터에 대한 질문에 답하고 AI 기반 가이드 인사이트를 통해 '왜'를 더 깊이 이해할 수 있도록 지원합니다.

Braze와 Tellius 통합을 통해 사용자는 BI 엔지니어에 의존하지 않고 데이터를 활용하여 대시보드를 구축하고 인사이트를 생성하여 더 나은 마케팅 의사결정을 내릴 수 있습니다. 이 통합을 사용하려면 Braze 데이터가 Snowflake에 저장되어 있어야 하며, Tellius가 직접 연결하여 라이브 모드 통합으로 쿼리를 푸시다운할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Tellius 계정 | 이 파트너십을 활용하려면 Tellius 계정이 필요합니다. [무료 체험](https://www.tellius.com/free-trial/)으로 Tellius 여정을 시작할 수 있습니다.|
| Snowflake 데이터 공유 프로그램 | 현재 Snowflake 고객인 경우, Braze 담당자에게 Snowflake 데이터 공유 프로그램에 대해 문의하여 Braze 데이터를 Snowflake 인스턴스로 전송하세요.|
| Snowflake Reader 계정 | Snowflake 고객이 아닌 경우, Braze 담당자에게 Snowflake Reader 계정에 대해 문의하세요. Braze 데이터에 접근할 수 있도록 계정이 프로비저닝됩니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Snowflake를 통해 Braze에 접근하기 {#step-1-obtain-access-to-braze-through-snowflake}

Braze는 세분화된 고객 데이터를 Snowflake에 저장합니다. Braze Snowflake 데이터 공유 프로그램을 통해 또는 Snowflake Reader 계정을 획득하여 Braze 데이터를 활용해 인사이트를 생성할 수 있습니다.

설정하려면 [Snowflake 통합]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)을 참조하세요.

### 2단계: Snowflake에서 Tellius를 Braze 데이터에 연결하기 {#step-2-connect-tellius-to-braze-data-in-snowflake}

다음 방법 중 하나를 통해 Snowflake에서 Tellius를 Braze 데이터에 연결합니다:

- 직접 접근: Tellius에 데이터를 로드하려면 [데이터셋 로드](https://help.tellius.com/article/jn6o59d5gk-load-datasets) 단계를 따르세요.
- OAuth 접근: Snowflake에 대한 OAuth 접근의 경우, [OAuth 인증](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake) 단계를 따르세요.

### 3단계: 로드된 데이터로 Tellius에서 Business View 생성하기 {#step-3-create-business-view-in-tellius-from-loaded-data}

자연어 검색 및 자동화된 인사이트를 사용하려면 [Business View](https://help.tellius.com/article/hy9yvh5tom-create-business-view)를 생성하고 Snowflake 연결에서 데이터셋을 선택하세요.

### 4단계: Tellius를 사용하여 데이터의 가치를 극대화하기 {#step-4-get-the-most-value-out-of-your-data-using-tellius}

Tellius에는 플랫폼의 기능을 안내하는 가이드 인터페이스가 있습니다. 추가 질문 및 안내는 전체 [지식 베이스](https://help.tellius.com/)를 참조하세요.