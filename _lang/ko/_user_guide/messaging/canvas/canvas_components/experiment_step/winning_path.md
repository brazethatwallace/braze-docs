---
nav_title: 위닝 경로
article_title: 실험 경로의 위닝 경로
page_type: reference
description: "이 참조 문서에서는 실험 경로 단계에서 활성화하면 A/B 테스트를 자동화할 수 있는 기능인 위닝 경로에 대해 설명합니다."
tool: Canvas
---

# 실험 경로의 위닝 경로

> 위닝 경로는 캠페인의 [위닝 배리언트]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/)와 유사하며, A/B 테스트를 자동화할 수 있습니다.

실험 경로 단계에서 위닝 경로를 활성화하면, 지정된 기간이 지난 후 모든 후속 사용자가 전환율이 가장 높은 경로로 전송됩니다.

## 위닝 경로 사용하기

### 1단계: 실험 경로 단계 추가

캔버스에 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/)를 추가한 다음 **위닝 경로**를 활성화합니다.

![실험 경로의 "후속 사용자를 위닝 경로로 분배"라는 제목의 설정. 이 섹션에는 위닝 경로 토글과 전환 이벤트 및 실험 기간을 구성하는 옵션이 포함되어 있습니다.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### 2단계: 위닝 경로 설정 구성

우승자를 결정할 전환 이벤트를 지정합니다. 사용 가능한 전환 이벤트가 없는 경우, 캔버스 설정의 첫 번째 단계로 돌아가서 [전환 이벤트를 할당]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#choose-conversion-events)합니다.

전환 이벤트로 열기 또는 클릭을 선택하는 경우, 경로의 첫 번째 단계가 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)인지 확인하세요. Braze는 각 경로의 첫 번째 메시지 단계에서 발생한 참여만 집계합니다. 경로가 다른 단계(예: 지연 또는 오디언스 경로 단계)로 시작되고 메시지가 나중에 오는 경우, 해당 메시지는 성과 평가 시 포함되지 않습니다.

다음으로 **실험 기간**을 설정합니다. **실험 기간**은 위닝 경로가 결정되고 이후 모든 사용자가 해당 경로로 전송되기까지 실험이 실행되는 시간을 지정합니다. 기간은 첫 번째 사용자가 단계에 진입할 때 시작됩니다.

![전환 이벤트 "클릭 수"가 선택되고 실험 기간이 12시간으로 설정된 위닝 경로 설정.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### 3단계: 대체 동작 결정 {#statistical-significance}

기본적으로 테스트 결과가 통계적으로 유의미한 우승자를 결정하기에 충분하지 않은 경우, 모든 향후 사용자는 가장 성과가 좋은 경로로 전송됩니다. 또는 **모든 향후 사용자에게 경로 조합을 계속 전송**을 선택할 수 있습니다. 이 옵션은 실험 경로 분배에서 지정된 비율에 따라 향후 사용자를 경로 조합으로 전송합니다.

동점인 경우, Braze는 먼저 나타나는 경로를 선택합니다.

![테스트 결과가 통계적으로 유의미하지 않을 때 수행할 작업으로 "모든 향후 사용자에게 경로 조합을 계속 전송"이 선택된 화면.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
지연 그룹은 캔버스가 일회성 진입으로 설정되어 있고 실험 단계에 세 개 이하의 경로가 있는 경우에만 경로 분배에 나타납니다. 반복 및 트리거된 캔버스에서는 위닝 경로가 활성화되어 있을 때 지연 그룹이 없습니다.
{% endalert %}

### 4단계: 경로 추가 및 캔버스 시작

단일 실험 경로 구성요소에는 최대 네 개의 경로를 포함할 수 있습니다. 그러나 캔버스가 [일회성 진입](#one-time-entry)으로 설정된 경우, 위닝 경로가 활성화되면 Braze가 자동으로 추가하는 지연 그룹을 위해 하나의 경로가 예약되어야 합니다. 따라서 일회성 진입 캔버스에서는 실험에 최대 세 개의 경로를 추가할 수 있습니다.

필요에 따라 캔버스 설정을 완료한 다음 시작합니다. 첫 번째 사용자가 실험에 진입하면, 캔버스를 확인하여 분석 데이터가 들어오는 것을 확인하고 [실험의 성과를 추적]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance)할 수 있습니다.

위닝 경로가 결정된 후, 캔버스에 진입하는 모든 후속 사용자는 위닝 경로로 이동합니다. 여기에는 재진입한 사용자와 이전에 실험 경로 단계의 대조군에 있었던 사용자도 포함됩니다.

## 분석 {#analytics}

위닝 경로가 활성화된 경우, 분석 보기는 **초기 실험**과 **위닝 경로** 두 개의 탭으로 구분됩니다.

- **초기 실험:** 실험 기간 동안 각 경로의 측정기준, 우승자로 선택된 경로, 캔버스 전환 측정기준을 표시합니다. 위닝 경로 설정에서 구성된 우승자 선택에 사용된 전환 이벤트는 캔버스 분석에서 강조 표시된 전환 측정기준과 다를 수 있습니다. 실험 경로 분석이 캔버스 전환 이벤트 및 우승 측정기준과 어떻게 관련되는지에 대한 자세한 내용은 [실험 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#winning-path-and-personalized-paths-performance)를 참조하세요.
- **위닝 경로:** 초기 실험이 완료된 시점부터 위닝 경로에 대한 측정기준만 표시합니다.

## 알아두어야 할 사항

### 일회성 진입 {#one-time-entry}

사용자가 한 번만 진입할 수 있는 캔버스에서 위닝 경로를 사용하면, 지연 그룹이 자동으로 포함됩니다. 실험 기간 동안 일정 비율의 사용자가 지연 그룹에 보류되고 나머지 사용자는 실험 경로에 진입합니다.

![위닝 경로를 위한 지연 그룹이 있는 실험 단계]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

테스트가 완료되고 위닝 경로가 결정되면, 지연 그룹에 할당된 사용자는 선택된 경로로 이동하여 캔버스를 계속 진행합니다.

![지연 그룹이 위닝 경로로 전송된 실험 단계]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### 현지 시간 전달

위닝 경로가 있는 캔버스에서는 현지 시간 전달을 사용하지 않는 것을 권장합니다. 실험 기간은 첫 번째 사용자가 통과할 때 시작되기 때문입니다. 매우 이른 시간대에 있는 사용자가 단계에 진입하여 예상보다 훨씬 일찍 실험 기간이 시작될 수 있으며, 이로 인해 일반적인 시간대에 있는 대부분의 사용자가 캔버스에 진입하거나 전환하기에 충분한 시간을 갖기 전에 실험이 종료될 수 있습니다.

대안으로, 현지 시간 전달을 사용하려면 24~48시간 이상의 실험 기간을 사용하세요. 이렇게 하면 이른 시간대의 사용자가 캔버스에 진입하여 실험이 시작되더라도 실험 기간에 충분한 시간이 남습니다. 늦은 시간대의 사용자도 실험 기간이 만료되기 전에 캔버스와 위닝 경로가 있는 실험 단계에 진입하고 전환할 수 있는 충분한 시간을 확보할 수 있습니다.

### 클릭 기반 배리언트

클릭 기반으로 위닝 경로 배리언트를 설정하는 경우, 열기와 클릭의 정의가 채널마다 다르다는 점에 유의하세요. 채널별 구체적인 측정기준과 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics) 및 [이메일 보고서 측정기준 용어집]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary)을 참조하세요.