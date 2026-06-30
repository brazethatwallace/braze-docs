---
nav_title: 피처 플래그
article_title: 피처 플래그
page_order: 8
page_type: reference
description: "이 참조 문서에서는 Canvas에서 피처 플래그를 사용하는 방법을 다룹니다."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/messaging/feature_flags/create_feature_flags'
---

# 피처 플래그 {#feature-flag}

> 피처 플래그를 사용하면 새로운 기능에 대한 가설을 실험하고 확인할 수 있습니다. 마케터는 피처 플래그를 사용하여 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)에서 오디언스를 세분화하고 기능 출시가 전환에 미치는 영향을 추적할 수 있습니다. 또한 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#experiment-paths)를 사용하면 서로 다른 메시지나 경로를 비교 테스트하여 가장 효과적인 것을 결정함으로써 이러한 전환을 최적화할 수 있습니다. 더 넓은 오디언스에게 기능을 점진적으로 출시할 때 위닝 경로를 활용하세요.

피처 플래그에 대한 자세한 정보와 Braze에서 활용하는 방법을 알고 싶으신가요? 전용 [기능 플래그]({{site.baseurl}}/developer_guide/feature_flags) 문서를 확인하세요.

## 피처 플래그 생성 {#creating-a-feature-flag}

![라이브 채팅 버튼 기능에 대한 피처 플래그 단계 예시.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

피처 플래그 구성요소를 생성하려면 먼저 Canvas에 단계를 추가합니다. 사이드바에서 구성요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 플러스 버튼을 클릭한 다음 **피처 플래그**를 선택합니다. 그런 다음 드롭다운에서 피처 플래그를 선택합니다. 드롭다운에는 아카이브되지 않은 피처 플래그가 표시됩니다.

## 이 단계의 작동 방식 {#how-this-step-works}

Canvas가 중지되거나 아카이브되거나 피처 플래그 단계가 제거되면, 해당 단계를 거친 사용자는 더 이상 해당 단계의 피처 플래그와 등록정보를 받지 않습니다.

출시 설정이 없고 피처 플래그 실험도 없는 피처 플래그의 경우, 해당 플래그를 참조하는 피처 플래그 단계가 포함된 Canvas를 중지하면:

- **피처 플래그 자격** 탭에서 해당 피처 플래그를 가진 사용자가 없습니다.
- 해당 피처 플래그에 대한 `Feature Flags` 세분화 필터와 일치하는 사용자가 없습니다.

피처 플래그에 출시 설정, 피처 플래그 실험 또는 이를 참조하는 다른 활성 Canvas가 있는 경우, 사용자는 해당 채널을 통해 여전히 자격을 가질 수 있습니다.

Canvas 단계의 등록정보는 시작 후에도, 심지어 사용자가 해당 단계를 거친 후에도 변경할 수 있습니다. 사용자는 이전에 저장된 버전이 아닌 항상 실시간의 동적 버전의 피처 플래그를 받습니다.

- **두 개의 Canvases가 동일한 피처 플래그를 참조하고 사용자가 두 Canvas 모두에 진입한 경우:** 사용자는 이전 Canvas가 아닌 가장 최근에 진입한 Canvas에서 설정된 값을 받습니다. 해당 값은 **피처 플래그 자격** 탭에 표시됩니다.
- **Canvas에 동일한 피처 플래그를 참조하는 두 개의 피처 플래그 단계가 있는 경우:** 사용자는 해당 경로에 있는 동안 두 번째 단계에서 설정된 값을 받으며, 해당 값은 **피처 플래그 자격** 탭에 표시됩니다.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## 등록정보 덮어쓰기 {#overwriting-properties}

피처 플래그를 생성할 때 기본 등록정보를 지정합니다. 피처 플래그 캔버스 단계를 설정할 때 기본값을 유지하거나 이 단계에 진입하는 사용자에 대해 값을 덮어쓸 수 있습니다.

![등록정보가 "String"이고, 등록정보 키가 "url"이며, 값이 있는 "Preference Center" 피처 플래그.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

**메시징** > **기능 플래그**로 이동하여 추가 등록정보를 편집, 추가 또는 제거할 수 있습니다.

## Canvas와 출시의 차이점 {#canvas-and-rollout-differences}

Canvas와 피처 플래그 출시(슬라이더 드래그)는 서로 독립적으로 작동할 수 있습니다. 중요한 주의사항은 Canvas 단계에 진입하면 기본 출시 구성이 덮어쓰기된다는 것입니다. 즉, 사용자가 피처 플래그 자격이 없더라도 Canvas 단계가 해당 사용자에게 기능을 활성화할 수 있습니다.

마찬가지로, 사용자가 특정 등록정보를 가진 피처 플래그 출시 자격이 있더라도 Canvas 단계에도 진입하면 해당 Canvas 단계에서 덮어쓴 값을 받게 됩니다.