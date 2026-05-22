---
nav_title: 캔버스 복제
article_title: 캔버스 복제
page_order: 3
alias: "/cloning_canvases/"
description: "이 참조 문서에서는 기존 캔버스 편집기에서 Canvas Flow 워크플로로 캔버스를 복제하는 방법을 설명합니다."
tool: Canvas
---

# 캔버스를 Canvas Flow로 복제 {#clone-canvases-to-canvas-flow}

> 기존 편집기에서 만든 캔버스가 있는 경우, 이 캔버스를 복제하여 Canvas Flow에서 사본을 생성할 수 있습니다. 현재 캔버스 워크플로로 전환하면 경량 [캔버스 구성요소]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/), [영구 진입 속성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#canvas-entry-properties), [시작 후 편집]({{site.baseurl}}/post-launch_edits/) 기능을 사용할 수 있습니다. 기존 캔버스는 변경되거나 삭제되지 않습니다.

{% alert important %}
더 이상 기존 캔버스 경험을 사용하여 캔버스를 생성하거나 복제할 수 없습니다. Braze는 기존 캔버스 경험을 사용하는 고객이 현재 캔버스 경험인 Canvas Flow로 전환할 것을 권장합니다.
{% endalert %}

캔버스를 복제하려면 다음을 수행합니다:

1. 캔버스 대시보드로 이동합니다.
2. Canvas Flow 워크플로에서 사본을 만들 캔버스를 찾습니다. **초안**, **활성**, **중지됨** 상태의 캔버스를 복제할 수 있습니다.
3. <i class="fas fa-ellipsis-vertical"></i> **More actions**를 클릭하고 **Clone to Canvas Flow**를 선택합니다.

![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4. 새 캔버스의 이름을 입력하고 **Clone to Canvas Flow**를 클릭합니다.

![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

이제 캔버스의 두 가지 버전이 있습니다: 기존 캔버스와 Canvas Flow 버전입니다. 기존 캔버스는 원래 상태를 유지하며, 복제된 캔버스는 **초안** 상태입니다. 기존 캔버스에 계속 접근할 수 있지만, Braze는 Canvas Flow 워크플로를 사용하여 캔버스를 계속 구축할 것을 권장합니다.

이전에는 분기가 있는 일부 캔버스를 복제할 수 없었습니다. 이제 분기가 있는 캔버스도 복제할 수 있습니다. 분기가 있는 캔버스를 복제하면 연결이 끊어진 단계가 발생할 수 있습니다. 이러한 연결이 끊어진 단계(이전 단계가 연결되지 않은 단계)를 해결하여 캔버스 여정이 올바르게 매핑되도록 하세요.

{% alert note %}
활성 캔버스를 복제하면 Braze는 기존 캔버스를 통해 사용자를 계속 보냅니다. 두 캔버스에서 사용자에게 중복 메시지가 발송되는 것을 방지하려면 복제하기 전에 캔버스를 중지하는 것을 권장합니다.
{% endalert %}

![두 개의 캔버스가 나열된 캔버스 대시보드: V2 Copy of Canvas V1과 Canvas V1. V2 Copy of Canvas V1에는 Canvas Flow 워크플로를 사용하고 있음을 나타내는 아이콘이 있습니다.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Canvas Flow 워크플로로 캔버스 복제가 완료되었습니다. 이제 이 업데이트된 경험에서 캔버스를 계속 구축할 수 있습니다!

## 권장 사항 {#recommendations}

기존 캔버스를 Canvas Flow로 복제한 후 기존 사용자가 사용자 여정을 계속할 수 있도록 하려면, 기존 캔버스에 필터를 추가하여 새 사용자가 새 캔버스에 진입하지 못하도록 할 수 있습니다.

재적격성이 꺼져 있는 경우, "Entered Canvas Variation" 필터를 추가합니다. 재적격성이 켜져 있는 경우, 사용자가 동일한 캔버스에 두 번 진입하지 않도록 다음 방법을 고려할 수 있습니다:
- 기존 캔버스에 고유한 태그를 추가하도록 업데이트합니다. 새 캔버스에는 "Last Received Message from Campaign or Canvas with Tag" 필터를 추가합니다. 이렇게 하면 특정 진입 날짜 이후(기존 캔버스에서 마지막 메시지가 발송된 후 총 일수에 전환 기간을 더한 기간) 사용자가 캔버스에 두 번 진입하는 것을 방지합니다.
- **다음 방법은 데이터 포인트를 기록합니다.** 기존 캔버스를 업데이트하여 진입 시 커스텀 속성 날짜 타임스탬프를 트리거하는 Braze-to-Braze 웹훅을 포함합니다. 이 속성을 사용하여 지정된 날짜(기존 캔버스에서 마지막 메시지가 발송된 후 총 일수에 전환 기간을 더한 기간) 이후 사용자가 새 캔버스에 진입하는 것을 방지할 수 있습니다.

API 트리거 Canvases의 경우, 새 Canvases가 시작될 준비가 되면 해당 Canvases가 새 Canvas ID를 사용하도록 엔지니어링 팀과 조율하세요.

기존 캔버스 편집기와 Canvas Flow 경험의 차이점에 대한 자세한 내용은 [캔버스 FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor)를 확인하세요.