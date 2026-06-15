---
nav_title: 오디언스 정의
article_title: 오디언스 정의
page_order: 3
page_type: reference
description: "BrazeAI Decisioning Studio 에이전트의 오디언스를 정의하고 구성하는 방법(처리 그룹 및 플랫폼별 설정 단계 포함)을 알아보세요."
---

# 오디언스 정의 {#define-your-audience}

> 사용 사례 오디언스는 일반적으로 고객 참여 플랫폼(예: Braze 또는 Salesforce Marketing Cloud)에서 정의한 후 Decisioning Studio 에이전트로 전송합니다. 그런 다음 에이전트가 무작위 대조 시험을 수행하기 위해 고객을 처리 그룹으로 나눕니다.

## 처리 그룹 {#treatment-groups}

| 그룹 | 설명 |
|-------|-------------|
| **Decisioning Studio** | AI 최적화 추천을 받는 고객 |
| **무작위 제어** | 무작위로 선택된 옵션을 받는 고객(기준 비교) |
| **기존 운영(선택 사항)** | 현재 마케팅 여정을 받는 고객(기존 성과와 비교하기 위함) |
| **홀드아웃(선택 사항)** | 커뮤니케이션을 받지 않는 고객(전체 캠페인 영향을 측정하기 위함) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Treatment groups" }

## 오디언스 구성 {#configure-your-audience}

{% tabs %}
{% tab Braze %}

1. 타겟팅할 오디언스에 대한 Segment를 생성합니다.
2. Segment ID를 인공지능 의사 결정 서비스 팀에 제공합니다.

{% alert note %}
Braze의 경우, 여러 Segments를 수집하고 결합하여 오디언스를 생성할 수 있습니다. Decisioning Studio는 기존 운영 비교 캠페인을 위한 Segment를 수집할 수 있습니다. 이러한 모든 패턴이 허용됩니다.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

1. 오디언스에 대한 SFMC 데이터 확장을 구성하고 데이터 확장 ID를 제공합니다.
2. Decisioning Studio에 필요한 적절한 권한으로 API 통합을 위한 SFMC 설치 패키지를 설정합니다.
3. Decisioning Studio가 사용 가능한 최신 증분 데이터를 가져오므로 이 데이터 확장이 매일 새로고침되는지 확인합니다.

확장 ID와 API 키를 인공지능 의사 결정 서비스 팀에 제공하면, 팀에서 고객 데이터 수집의 다음 단계를 지원합니다.

{% endtab %}
{% tab 다른 플랫폼 %}

### Google Cloud Storage

오디언스가 현재 Braze 또는 Salesforce Marketing Cloud에 저장되어 있지 않은 경우, 다음 최선의 단계는 Braze가 관리하는 Google Cloud Storage(GCS) 버킷으로 자동 내보내기를 구성하는 것입니다.

이것이 가능한지 확인하려면 해당 플랫폼의 설명서를 참조하세요. 예를 들어, mParticle은 [Google Cloud Storage와의 네이티브 통합](https://www.mparticle.com/integration/google-cloud-storage/)을 제공합니다. 이 경우 오디언스 데이터를 내보낼 GCS 버킷을 제공할 수 있습니다.

### 추가 리소스 {#additional-resources}

- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## 다음 단계 {#next-steps}

오디언스를 정의한 후 오케스트레이션 설정을 진행합니다:

- [오케스트레이션 설정]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup/)