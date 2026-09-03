---
nav_title: 보고서 및 인사이트
article_title: 보고서 및 인사이트
description: "AI 기반 의사 결정이 캠페인에 어떤 영향을 미치는지 파악하기 위해 Braze에서 BrazeAI Decisioning Studio™ 보고서를 보는 방법을 알아보세요."
page_order: 6
---

# 보고서 및 인사이트 {#reports-and-insights}

> AI 기반 의사 결정이 캠페인에 어떤 영향을 미치는지 파악하기 위해 Braze에서 BrazeAI Decisioning Studio™ 보고서를 보는 방법을 알아보세요. 성과 측정기준부터 데이터 상태 및 시스템 변경 사항까지, 이러한 보고서를 통해 결과를 이해하고, 문제를 해결하고, 자신 있게 정보에 입각한 의사 결정을 내릴 수 있습니다.

## 사전 요구 사항 {#prerequisites}

Braze에서 Decisioning Studio 보고서를 확인하려면 다음 조건을 충족해야 합니다:

- Braze 및 BrazeAI Decisioning Studio<sup>TM</sup>에 대한 활성 계약이 있어야 합니다.
- CSM에게 연락하여 BrazeAI Decisioning Studio<sup>TM</sup>를 활성화해 달라고 요청하세요.
- 활성 상태의 BrazeAI Decisioning Studio<sup>TM</sup> 에이전트가 있어야 합니다.

## 보고서 보기 {#view}

Braze에서 Decisioning Studio 에이전트의 측정기준을 보려면 **AI Decisioning** > **BrazeAI Decisioning Studio™**로 이동한 다음 에이전트를 선택합니다.

여기에서 성과, 인사이트, 진단 및 타임라인과 같은 보고서를 볼 수 있습니다. 자세한 내용은 [사용 가능한 보고서](#available-reports)를 참조하세요.

## 보고서 날짜 변경 {#change-report-dates}

[보고서를 열고 나서](#view) 캘린더 드롭다운에서 새로운 시작 날짜와 종료 날짜를 선택하여 날짜 범위를 변경할 수 있습니다.

![BrazeAI Decisioning Studio™ 날짜 범위 선택기가 캘린더 드롭다운으로 열려 있는 화면. 캘린더에서 보고서 보기를 커스텀하기 위해 시작 날짜와 종료 날짜를 선택할 수 있습니다.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

기본값 시작 날짜를 설정하거나 항상 제외할 날짜를 선택할 수도 있습니다. 제외된 날짜는 해당 에이전트의 모든 보고서에서 필터링됩니다.

날짜를 설정하거나 제외하려면 <i class="fa-solid fa-gear" aria-label="설정"></i> **Settings**를 선택한 다음 기본값 날짜를 변경하거나 필요에 따라 날짜를 제외합니다.

![BrazeAI Decisioning Studio™에서 설정 패널이 열려 있으며 기본값 시작 날짜를 설정하고 보고서에서 특정 날짜를 제외하는 옵션이 표시됩니다. 패널에는 기본값 시작 날짜와 날짜 제외 두 개의 섹션이 있습니다. 날짜 제외 아래에 각 날짜 옆에 체크박스가 있는 여러 날짜가 나열되어 있습니다.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## 사용 가능한 보고서 {#available-reports}

- [성과]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/performance): 처리 그룹과 대조군을 비교하는 고수준 에이전트 측정기준으로, **Trending** 및 **Driver Tree** 보기를 제공합니다.
- [인사이트]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/insights): 에이전트 선호도 및 SHAP 보고서를 포함하여 동작 뱅크의 추천 옵션이 어떻게 생성되는지 보여줍니다.
- [진단]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/diagnostics): 추천 볼륨 및 데이터 피드 모니터링을 포함한 아웃바운드 및 인바운드 데이터 상태를 보여줍니다.
- [타임라인]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/timeline): 에이전트 실행, 구성 변경, 가드레일 업데이트 등 주요 이벤트를 성과 측정기준과 함께 시각적으로 기록합니다.