---
nav_title: 데이터 연결
article_title: 데이터 연결
page_order: 6
description: "개인화된 AI 의사 결정을 위해 고객 데이터 소스를 BrazeAI Decisioning Studio에 연결하는 방법을 알아보세요."
---

# 데이터 연결 {#connect-your-data}

> BrazeAI Decisioning Studio™ 에이전트는 효과적인 의사 결정을 내리기 위해 고객 컨텍스트를 완전히 이해해야 합니다. 이 문서에서는 고객 데이터 소스를 Decisioning Studio에 연결하는 방법을 설명합니다.

{% alert tip %}
AI Decisioning Services 팀이 최적의 성과를 위한 데이터 연결 구성을 지원합니다.
{% endalert %}

## 지원되는 통합 패턴 {#supported-integration-patterns}

Decisioning Studio는 고객 데이터를 연결하기 위한 다양한 통합 패턴을 지원합니다.

| 통합 패턴 | 적합한 용도 | 설정 복잡도 |
|---------------------|----------|------------------|
| **Braze 데이터 플랫폼** | 이미 Braze를 사용 중인 고객 | 낮음 |
| **Braze 클라우드 데이터 수집(CDI)** | 외부 데이터 웨어하우스 연결 | 중간 |
| **클라우드 스토리지(GCS, AWS, Azure)** | 다른 플랫폼에서의 직접 데이터 내보내기 | 중간 |
| **CEP 통합** | SFMC, Klaviyo 데이터 확장 | 중간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="지원되는 통합 패턴" }

## 고객 데이터 유형 {#customer-data-types}

다음 고객 데이터 자산은 에이전트가 보다 효과적으로 개인화하는 데 도움이 됩니다.

| 데이터 유형 | 설명 | 예시 |
|-----------|-------------|----------|
| **고객 프로필** | 정적이며 변경 빈도가 낮은 속성 | 고객 기간, 지역, 유입 채널, 만족도, 생애주기 가치 추정치 |
| **고객 행동** | 활동 및 인게이지먼트 패턴 | 계정 로그인, 기기 유형, 고객 서비스 상호작용, 제품 사용 |
| **트랜잭션 내역** | 구매 및 전환 데이터 | 구매한 제품, 트랜잭션 금액, 결제 수단, 구매 채널 |
| **마케팅 인게이지먼트** | 커뮤니케이션에 대한 반응 | 이메일 열람/클릭, SMS 인게이지먼트, 웹 및 모바일 활동, 설문조사 응답 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="고객 데이터 유형" }

{% alert tip %}
에이전트가 고객에 대해 더 많은 정보를 보유할수록 더 나은 성능을 발휘합니다. 비즈니스에 특히 중요한 인사이트에 대한 데이터를 포함하는 것을 고려해 보세요(예를 들어, 인공지능이 로열티 고객을 어떻게 다르게 처리하는지 확인하고 싶으신가요? 고객 데이터에 로열티 상태가 포함되어 있는지 확인하세요).
{% endalert %}

## 플랫폼별 데이터 연결 {#connect-data-by-platform}

{% tabs %}
{% tab Braze %}

### Braze를 통해 고객 데이터 전송 {#send-customer-data-through-braze}

BrazeAI Decisioning Studio는 이미 Braze 데이터 플랫폼으로 전송하고 있는 모든 데이터를 사용할 수 있습니다.

고객 프로필이나 커스텀 속성에 없는 고객 데이터의 경우, [Braze 클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 통해 두 가지 방법으로 가져올 수 있습니다.

- Braze 데이터 플랫폼으로 수집합니다. 데이터 웨어하우스 데이터를 Braze 고객 프로필, 커스텀 속성 또는 이벤트에 동기화합니다. 세분화 및 메시징을 위해 Braze에서도 데이터를 사용하려는 경우 이 방법을 선택하세요. Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric, AWS S3, Google Cloud Storage를 지원합니다.
- Decisioning Studio로 직접 전송합니다(얼리 액세스). Braze 고객 프로필이나 커스텀 속성에 추가하지 않고 데이터 웨어하우스 데이터를 Decisioning Studio로 바로 동기화합니다. Decisioning Studio에서는 사용하되 Braze의 다른 곳에서는 필요하지 않은 데이터에 이 방법을 선택하세요. 이 옵션은 얼리 액세스 중이며, 설정 방법은 [클라우드 데이터 수집: Decisioning Studio 데이터 동기화]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/decisioning_studio)를 참조하세요.

Braze 데이터 플랫폼으로 전송하는 데이터에 만족하면, AI Decisioning 서비스 팀에 연락하여 고객 프로필 또는 커스텀 속성의 어떤 필드를 AI Decisioning에 사용할지 논의하세요.

이 과정을 간소화하려면, Decisioning Studio에서 사용해야 할 고객 행동을 가장 잘 나타낸다고 생각하는 Braze 고객 프로필 속성 목록을 작성하세요([내보내기 가능한 필드 목록]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#fields-to-export) 참조). 서비스 팀이 AI Decisioning에 가장 적합한 필드를 결정하기 위한 디스커버리 세션을 진행하는 것도 도와드릴 수 있습니다.

데이터를 전송하는 다른 옵션으로는 다음이 있습니다.

- SDK를 통해 Braze 커스텀 이벤트 전송
- REST 엔드포인트([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))를 사용하여 이벤트 전송

이러한 패턴은 더 많은 엔지니어링 노력이 필요하지만, 현재 Braze 구성에 따라 더 적합할 수 있습니다. 자세한 내용은 AI Decisioning 서비스 팀에 문의하세요.

{% endtab %}
{% tab SFMC %}

### SFMC를 통해 고객 데이터 전송 {#send-customer-data-through-sfmc}

Salesforce Marketing Cloud 통합의 경우:

1. 고객 데이터를 위한 SFMC 데이터 확장(Data Extension)을 구성합니다.
2. Decisioning Studio에서 요구하는 적절한 권한으로 API 통합을 위한 SFMC 설치 패키지를 설정합니다.
3. Decisioning Studio가 사용 가능한 최신 증분 데이터를 가져오므로, 데이터 확장이 매일 새로고침되는지 확인합니다.

확장 ID와 API 키를 AI Decisioning 서비스 팀에 제공하세요. 팀에서 고객 데이터 수집의 다음 단계를 지원해 드립니다.

{% endtab %}
{% tab Klaviyo %}

### Klaviyo를 통해 고객 데이터 전송 {#send-customer-data-through-klaviyo}

Klaviyo 통합의 경우:

1. Klaviyo 프로필에서 고객 프로필 데이터를 사용할 수 있는지 확인합니다.
2. 프로필에 대한 전체 액세스 권한이 있는 프라이빗 API 키를 생성합니다.
3. AI Decisioning 서비스 팀에 API 키를 제공합니다.

API 키 설정에 대한 자세한 내용은 [Klaviyo 설명서](https://help.klaviyo.com/hc/en-us/articles/115005237908)를 참조하세요.

{% endtab %}
{% tab Cloud Storage %}

### 기타 클라우드 솔루션(Google Cloud Storage, Azure, AWS) {#other-cloud-solutions-google-cloud-storage-azure-aws}

고객 데이터가 현재 Braze, SFMC 또는 Klaviyo에 저장되어 있지 않은 경우, 가장 좋은 다음 단계는 Braze가 관리하는 Google Cloud Storage 버킷으로 자동 내보내기를 구성하는 것입니다. AWS 또는 Azure로의 내보내기도 지원할 수 있습니다(GCS가 권장됩니다). 이러한 플랫폼의 경우, 해당 클라우드 플랫폼의 내부 클라우드 스토리지로 내보내면 Braze가 해당 데이터를 가져올 수 있습니다.

이것이 가능한지 확인하려면 사용 중인 MarTech 플랫폼의 설명서를 참조하세요. 예를 들어:

- mParticle은 [Google Cloud Storage와의 네이티브 통합](https://www.mparticle.com/integration/google-cloud-storage/)을 제공합니다.
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

이것이 가능한 경우, Decisioning Studio 전용으로 격리된 고객 데이터 내보내기를 위한 GCS 버킷을 제공해 드릴 수 있습니다.

{% endtab %}
{% endtabs %}

## 모범 사례 {#best-practices}

- **설명적 열 이름:** 고객 데이터에는 명확하고 설명적인 열 이름이 있어야 합니다. 이상적으로는 데이터 사전을 함께 제공하는 것이 좋습니다.
- **증분 업데이트:** 매일 전체 고객 이력의 스냅샷을 제공하는 것보다 증분 파일이 더 바람직합니다.
- **일관된 식별자:** 각 레코드에는 모든 데이터 자산에서 일관된 고유 고객 식별자가 포함되어야 합니다.
- **타임스탬프 포함:** 정확한 기여도 분석 및 에이전트 학습을 위해 레코드에 관련 타임스탬프가 포함되어야 합니다.

## 커스텀 통합 {#custom-integrations}

다른 옵션이나 완전히 커스텀 데이터 파이프라인도 가능합니다. 이러한 경우 팀에서 추가적인 서비스 작업이나 엔지니어링 작업이 필요할 수 있습니다. 실현 가능하고 최적인 방안을 결정하려면 AI Decisioning 서비스 팀과 협력하세요.

{% alert important %}
이 가이드는 가장 일반적인 통합 패턴을 설명합니다. 정보 보안팀은 여전히 모든 연결 지점을 검토해야 하며, 솔루션 컨설턴트가 구현에 대한 조언을 제공할 수 있습니다.
{% endalert %}

## 다음 단계 {#next-steps}

데이터 소스를 연결한 후, 오케스트레이션 설정을 진행하세요:

{% article_tiles %}
- name: 오케스트레이션 설정
  link: /docs/user_guide/brazeai/decisioning_studio/orchestration_setup
{% endarticle_tiles %}