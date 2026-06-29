---
nav_title: Databricks Mosaic
article_title: Databricks Mosaic
description: "이 참조 문서에서는 Braze와 Databricks Mosaic 간의 파트너십에 대해 설명합니다. 이 파트너십을 통해 Databricks 모델을 Braze에 연결하여 커스텀 AI 에이전트에서 사용할 수 있습니다."
alias: /partners/databricks_mosaic/
page_type: partner
search_tag: Partner

---

# Databricks Mosaic

> [Databricks Mosaic AI](https://www.databricks.com/product/artificial-intelligence)는 Databricks Data Intelligence Platform에서 AI 및 머신 러닝 모델을 대규모로 구축, 배포, 관리할 수 있는 Databricks의 통합 플랫폼입니다.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_이 통합은 Databricks에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Databricks Mosaic 통합을 사용하면 Databricks 토큰과 워크스페이스를 Braze에 연결하여 커스텀 AI 에이전트를 구축할 때 Databricks 모델을 사용할 수 있습니다. Braze는 Databricks Mosaic 자격 증명을 사용하여 고객을 위한 콘텐츠를 생성합니다. 이 통합을 통해 에이전트는 개인화된 카피를 생성하고, 실시간 의사 결정을 내리거나, Databricks 모델을 사용하여 카탈로그 필드를 업데이트할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| 개인 액세스 토큰이 있는 Databricks 계정 | [개인 액세스 토큰](https://docs.databricks.com/en/dev-tools/auth/pat.html)이 있는 Databricks 계정이 필요합니다. 도움이 필요하면 관리자 또는 [Databricks 고객지원](https://help.databricks.com/)에 문의하세요. |
| Databricks 워크스페이스 이름 | Databricks 계정의 워크스페이스 이름(또는 인스턴스)입니다. `.cloud.databricks.com` 또는 `.azuredatabricks.net` 앞의 서브도메인입니다(예: `dbc-eb57d699-f22c`). |
| Braze 인스턴스 | Braze 인스턴스는 [API 개요 페이지]({{site.baseurl}}/api/basics/#endpoints)에서 확인하거나 Braze 온보딩 매니저에게 문의할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

Databricks Mosaic 자격 증명을 Braze에 연결하려면 다음을 수행하세요.

1. Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Databricks Mosaic Integration**을 찾습니다.
2. **Databricks Token**을 입력합니다.
3. **Databricks Workspace Name**을 입력합니다. `.cloud.databricks.com` 또는 `.azuredatabricks.net` 앞의 서브도메인입니다.
4. **저장**을 선택합니다.

저장 후 Braze에 연결 날짜 및 시간과 함께 연결됨 상태가 표시됩니다. 에이전트 콘솔에서 [커스텀 에이전트를 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)할 때 Databricks 모델을 선택할 수 있습니다.

통합을 제거하려면 **Databricks Mosaic Integration** 페이지에서 **연결 해제**를 선택하세요.

통합과 관련된 문제나 질문이 있으면 [Databricks 고객지원](https://help.databricks.com/)에 문의하세요.