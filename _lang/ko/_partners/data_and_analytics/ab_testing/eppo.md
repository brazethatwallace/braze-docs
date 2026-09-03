---
nav_title: Eppo
article_title: Eppo
description: "Eppo와 Braze를 통합하는 방법을 알아보세요."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/)는 차세대 실험 플랫폼으로, 팀이 A/B 테스트를 실행하고, 대규모로 기능을 관리하며, AI 기반 인사이트를 활용하여 데이터 중심 의사결정을 내릴 수 있도록 지원합니다.

*이 통합은 Eppo에서 유지 관리합니다.*

Braze와 Eppo 통합을 사용하면 Braze에서 A/B 테스트를 설정하고 Eppo에서 결과를 분석하여 인사이트를 발견하고 메시지 성과를 매출이나 리텐션과 같은 장기 비즈니스 측정기준에 연결할 수 있습니다.

## 전제 조건 {#prerequisites}

| 요구 사항                        | 설명                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Eppo 계정                       | 이 파트너십을 활용하려면 Eppo 계정이 필요합니다.                   |
| Currents 또는 Snowflake 데이터 공유 | Eppo가 실험 데이터를 분석하려면 Currents 또는 Snowflake 데이터 공유가 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: Braze에서 Currents 또는 Snowflake 데이터 공유 구성 {#step-1-configure-currents-or-snowflake-data-sharing-in-braze}

Eppo는 데이터 웨어하우스에서 직접 실험을 분석합니다. 통합을 활성화하려면 Eppo에 연결된 데이터 웨어하우스에서 Braze 메시지 인게이지먼트 데이터를 사용할 수 있어야 합니다. Currents를 사용하여 Braze에서 캠페인 데이터를 내보내거나, [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)를 사용하여 Snowflake 인스턴스에서 Braze 데이터에 액세스할 수 있습니다.

### 2단계: Braze Campaign 또는 Canvas에서 실험 설정 {#step-2-set-up-your-experiment-in-a-braze-campaign-or-canvas}

Campaigns 및 Canvases에서 네이티브 A/B 테스트 기능을 사용할 수 있습니다. 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

### 3단계: Braze 실험 측정을 위한 Eppo 설정 {#step-3-set-up-eppo-to-measure-braze-experiments}

Eppo에서 Braze 데이터를 사용하여 실험을 실행하려면, Braze에서 내보낸 사용자 수준의 메시지 이벤트 데이터를 기반으로 데이터 웨어하우스에 [할당 테이블](https://docs.geteppo.com/data-management/definitions/assignment-sql/)을 생성합니다. Canvas 실험과 캠페인 실험은 서로 다른 메타데이터에 의존하므로 별도의 테이블을 사용하는 것이 권장됩니다.

{% tabs local %}
{% tab 캔버스 실험 %}
캔버스 실험의 경우 다음 중 하나의 수준에서 할당을 생성할 수 있습니다.

- Canvas 진입 수준(`users.canvas.Entry`)
- 또는 Canvas 실험 단계(`users.canvas.experimentstep.SplitEntry`)

이 경우 `canvas_name`, `experiment_step_id`, `canvas_variation_name`, `experiment_split_id` 등의 필드를 사용하여 실험 이름과 배리언트를 정의합니다.

{% endtab %}

{% tab 캠페인 실험 %}
캠페인 실험의 경우 전송 이벤트(푸시, 이메일, SMS 등)를 사용하여 사용자가 실험에 진입한 시점을 확인합니다. `campaign_name`, `message_variation_name`, `time`을 사용하여 할당 테이블을 채웁니다.

{% endtab %}
{% endtabs %}

클릭이나 열람과 같은 메시지별 측정기준을 추적하려면, 사용자 ID와 캠페인 또는 Canvas 이름을 결합한 `combined_id`를 생성하여 **보조 엔티티**를 포함합니다. 이 `combined_id`는 팩트 테이블에서도 사용되어 측정기준을 올바른 실험 및 배리언트와 연결합니다.

Eppo는 이러한 할당 및 팩트 테이블을 사용하여 결과를 분석하며, 향후 실험 설정을 표준화하기 위해 Eppo에서 **프로토콜**을 설정하는 것이 권장됩니다. 자세한 내용은 [Eppo 설명서](https://docs.geteppo.com/guides/marketing/integrating-with-braze/)를 참조하세요.

## 지원 {#support}

Braze Currents, Snowflake 데이터 공유 설정 또는 다변량 Campaigns 구성에 대한 질문이 있으시면 Braze 고객 성공 매니저에게 문의하세요.

Braze 실험을 측정하기 위한 Eppo 구성에 대한 도움이 필요하시면 Eppo 지원 팀에 문의하세요.