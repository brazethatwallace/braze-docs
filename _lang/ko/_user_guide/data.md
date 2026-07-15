---
nav_title: Data
article_title: Data
page_order: 3
description: "통합, 활성화, 배포 방법을 포함하여 Braze 데이터 플랫폼에 대해 알아보세요."
---

# Braze 데이터 플랫폼 {#braze-data-platform}

> 통합, 활성화, 배포 방법을 포함하여 Braze 데이터 플랫폼에 대해 알아보세요.

Braze 데이터 플랫폼(BDP)은 고객을 위한 개인화된 경험을 만들 수 있도록 지원하는 포괄적이고 구성 가능한 데이터 기능 및 파트너 통합 세트입니다. Braze에서는 데이터를 세 가지 데이터 관련 작업 관점에서 생각합니다: [통합]({{site.baseurl}}/user_guide/data/unification), [활성화]({{site.baseurl}}/user_guide/data/activation), [배포]({{site.baseurl}}/user_guide/data/distribution).

Braze 데이터 플랫폼의 기능을 조합하여 사용하면 데이터를 활용하여 고객이 실시간으로 수행하는 행동에 반응하는 의미 있고 타겟팅된 메시지를 만들 수 있습니다.

## 작동 방식 {#how-it-works}

### 데이터 통합 {#unify-your-data}

사용자 데이터는 다양한 진입점을 통해 Braze로 유입됩니다. [API]({{site.baseurl}}/api/home) 및 [SDK]({{site.baseurl}}/developer_guide/sdk_integration)를 사용하여 모든 소스에서 퍼스트파티 데이터를 수집하고 통합하세요. [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)과 같은 내장 수집 도구를 사용하여 데이터 웨어하우스 또는 파일 스토리지 솔루션에서 Braze로의 직접 통합을 생성하거나, [데이터 변환]({{site.baseurl}}/user_guide/data/unification/data_transformation)을 사용하여 Braze로 데이터를 전송하기 위한 웹훅 통합을 구축하고 관리할 수도 있습니다.

### 데이터 활성화 {#activate-your-data}

데이터를 정리, 구성하고 사용할 수 있도록 준비하세요. 여기에는 고객 프로필과 Segments를 통해 고객의 행동과 선호도를 실시간으로 이해하는 것이 포함됩니다. 타겟팅된 메시지를 만들 때 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/analytics/metrics_glossary)을 참조하고, [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs)를 사용하여 제품 또는 콘텐츠 데이터로 메시지를 풍부하게 만드세요. 고객이 이러한 개인화된 경험에 어떻게 반응하는지 파악하세요.

### 데이터 배포 {#distribute-your-data}

외부 시스템으로 데이터를 스트리밍하고 [내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data)하여 다음 단계의 인사이트와 의사 결정에 활용하세요. [Braze 커런츠]({{site.baseurl}}/user_guide/data/distribution/braze_currents)를 사용하여 Braze 이벤트 데이터를 데이터 웨어하우스로 스트리밍하여 비즈니스 인텔리전스 도구를 지원할 수 있습니다. [기술 파트너 통합]({{site.baseurl}}/partners/data_and_analytics)으로 데이터 기능을 확장할 수도 있습니다.

## 데이터 인프라 {#data-infrastructure}

Braze 데이터 인프라에는 지연 시간(서버와 사용자 간 데이터 이동에 걸리는 시간)을 최소화하는 데 도움이 되는 [데이터 센터]({{site.baseurl}}/user_guide/data/infrastructure/data_centers)가 포함되어 있습니다. 이러한 지리적 분산을 통해 서비스의 안정성과 확장성을 보장합니다. 또한 민감한 데이터를 보호하고 Braze에서 공유되는 개인 식별 정보(PII)를 최소화하기 위해 [필드 수준 암호화]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption)를 제공합니다. 사용량 및 청구에 대한 자세한 내용은 [데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points)를 참조하세요.

## 핵심 원칙 {#core-principles}

데이터는 개인화된 경험을 만들고, 고객 행동을 이해하고, 메시징 전략을 최적화함으로써 고객 참여 전략을 강화하는 데 중요한 역할을 합니다. Braze에서는 세 가지 핵심 원칙을 염두에 두고 모든 데이터 기능을 구축합니다:

{% details 데이터의 활용도 높이기 %}
- **유연하고 구성요소 기반:** 가장 중요한 목표는 데이터를 보다 효과적이고 완벽하게 활용할 수 있도록 돕는 것입니다. 컴포저블 아키텍처로 구축되어 불필요한 미들웨어 없이도 데이터를 더욱 효율적으로 활용하는 데 필요한 기술을 활용할 수 있습니다.
- **파트너 통합:** Braze는 동급 최고의 생태계 기술과의 통합을 우선시하며, 실시간 양방향 데이터 공유를 간편하게 할 수 있는 API를 제공합니다.
- **스트림 처리 아키텍처:** 세분화, 오케스트레이션, 개인화를 위해 Braze에 수집된 모든 데이터 포인트에 대해 동작을 트리거할 수 있습니다.
{% enddetails %}

{% details 데이터 민첩성 향상을 통한 성과 촉진 %}
- **유연한 오디언스 구성:** 기술 팀에 대한 의존도를 줄여 오디언스를 생성하고 개인화된 고객 참여를 대규모로 제공할 수 있습니다.
- **속도와 성과:** 참여 데이터와 인사이트가 실시간으로 제공되므로 반복적이고 효과적인 고객 참여는 물론 더 광범위한 비즈니스 의사 결정을 지원합니다.
{% enddetails %}

{% details 데이터의 보안, 안전 및 규정 준수 유지 %}
- **업계를 선도하는 보안 관행:** 최고 수준의 업계 표준을 준수하기 위해 SOC 2 Type 2 및 ISO 27001을 포함한 정기적인 제3자 감사를 실시합니다. 공개 버그 바운티 프로그램을 운영하여 잠재적인 취약점을 사전에 해결하고, 데이터를 보호하기 위한 전담 보안 팀을 운영하고 있습니다.
- **업계 규정 준수:** GDPR 및 CCPA를 비롯한 데이터 보호 규정 준수를 촉진하는 도구를 제공합니다.
- **데이터 프라이버시:** 최종 사용자 동의를 관리하고, 요청을 처리하고, 소비자 권리를 실행할 수 있습니다.
{% enddetails %}