---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "이 참조 문서에서는 개인화된 추천을 통해 매출 성장을 촉진하는 AI 기반 SaaS(software-as-a-service) 비즈니스 플랫폼인 Personalize.AI와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/personalize_ai/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/)는 Braze와 파트너십을 맺고, Braze를 통해 전송되는 개인화된 메시지와 오퍼를 제공하여 점진적인 매출을 창출합니다.

Braze와 Personalize.AI 통합을 통해 Personalize.AI에서 Braze 플랫폼으로 데이터를 내보내 메시지 개인화 및 타겟팅에 활용할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Personalize.AI 인스턴스 | 이 파트너십을 활용하려면 Personalize.AI 인스턴스가 필요합니다. |
| Braze REST API 키 | 모든 권한이 포함된 Braze REST API 키. <br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 활용 사례 {#use-cases}

* 유연한 계층화를 포함한 테스트를 배포하여 고객 피드백으로부터 결과를 도출합니다
* 처리, 타이밍, 콘텐츠를 포함한 아이템 및 오퍼에 대한 개인화된 추천을 제공합니다
* 우선순위가 지정된 목표를 식별하고 Braze를 통해 최적의 오디언스를 타겟팅합니다
* 이탈한 사용자를 다시 참여시킬 기회를 식별합니다
* 지리 위치 데이터를 사용하여 새로 오픈한 위치에 적합한 오디언스를 찾습니다
* 유사 모델링을 사용하여 신규 사용자의 제한된 데이터를 기반으로 가장 관련성 높은 추천과 매칭합니다
* 고객 라이프사이클 전반에 걸쳐 올바른 참여 방법을 식별합니다
* 고객이탈 가능성을 사전에 평가하고 위험 점수를 할당하여 고객이탈의 초기 지표를 파악합니다
* 개인화된 개입으로 고객을 타겟팅하여 비활성 상태가 되는 것을 방지합니다

## 통합 {#integration}

### Personalize.AI에서 Braze 연결 구성하기 {#configure-a-connection-with-braze-in-personalizeai}

1. Personalize.AI에서 Personalize.AI 인스턴스의 **Operationalization** 아래에 있는 **Integrations** 탭으로 이동합니다.
2. **Braze**를 클릭합니다.
3. Braze와의 통합을 구성합니다.
    * **Connection Name:** 연결 이름을 지정합니다. 이 이름은 Personalize.AI에서 통합을 참조하는 데 사용됩니다.
    * **Sync Frequency:** 동기화 빈도는 Personalize.AI가 Braze로 데이터를 내보내는 주기를 제어합니다. **Daily**, **Weekly** 또는 **Monthly**를 선택합니다.
    * **API Key:** Braze API 키를 추가합니다.
    * **API URL:** Braze REST 엔드포인트 URL을 추가합니다.
4. **EXPORT**를 클릭하여 Braze로 데이터를 내보냅니다.

데이터가 내보내지면, Personalize.AI는 통합 시 설정한 동기화 빈도에 따라 결정된 간격으로 계속해서 Braze에 데이터를 전달합니다.

## 이 통합 사용하기 {#using-this-integration}

Personalize.AI는 개인화된 타겟팅에 사용되는 식별자를 Braze로 내보냅니다. 이러한 커스텀 속성은 각 고객에 대한 타이밍, 콘텐츠, 처리 및 오퍼를 나타냅니다. 통합에 따라 필드는 이벤트로 전달되거나 고객 프로필에 저장하는 대신 [연결된 콘텐츠 API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/public_apis/)로 가져올 수 있습니다. Personalize.AI는 식별자로 `external_id` 사용을 지원합니다.

Braze로 가져온 데이터 속성은 일관된 용어를 따르며 Canvases에서 사용하기 쉽도록 직관적으로 명명됩니다. 예를 들어, Personalize.AI의 속성 `C402_Target_Variant`는 Braze에 `"P.AI_Model_Treatment"`로 내보내집니다. Personalize.AI에서 내보낸 속성은 기존 속성이나 추적을 방해하지 않도록 설계되었습니다. 이러한 속성은 지속적으로 검증되어 안심하고 참조할 수 있습니다.

예를 들어, 다음은 고객이탈 중심 Canvas 예시와 관련된 고객 속성 세트입니다.

| Personalize.AI 속성 | 값 |
| ----------- | ------------- |
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Churn_Mitigation" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | Treatment |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | "Caesar Salad" |
| `C4_Subject_Line` | "We miss you" |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이 통합 사용하기" }