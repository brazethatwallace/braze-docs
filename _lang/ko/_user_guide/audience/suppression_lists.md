---
nav_title: 억제 목록
article_title: 억제 목록
page_order: 7
page_type: reference
tool: Segments
description: "이 페이지에서는 억제 목록을 사용하여 메시지를 절대 수신하지 않아야 하는 사용자를 지정하는 방법을 다룹니다."

---

# 억제 목록 {#suppression-lists}

> 억제 목록은 어떤 Campaign이나 Canvases도 자동으로 수신하지 않는 사용자 그룹입니다. 억제 목록은 Segment 필터로 정의되며, 사용자는 필터 기준을 충족함에 따라 억제 목록에 진입하거나 이탈합니다. 또한 예외 태그를 설정하여 해당 태그가 있는 Campaign이나 Canvases에는 억제 목록이 적용되지 않도록 할 수 있습니다. 예외 태그가 있는 Campaign이나 Canvases의 메시지는 타겟 Segments에 포함된 억제 목록 사용자에게 여전히 도달합니다.

## 억제 목록을 사용하는 이유 {#why-use-suppression-lists}

억제 목록은 동적이며 모든 형태의 메시징에 자동으로 적용되지만, 선택한 태그에 대해 예외를 설정할 수 있습니다. 선택한 예외 태그가 Campaign이나 Canvas에 사용되면 해당 억제 목록은 그 Campaign이나 Canvas에 적용되지 않습니다. 예외 태그가 있는 Campaign이나 Canvases의 메시지는 타겟 Segments에 포함된 억제 목록 사용자에게 여전히 도달합니다.

### 억제 목록의 영향을 받는 메시지 유형 및 채널 {#message-types-and-channels-affected-by-suppression-lists}

억제 목록은 [피처 플래그]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags/)를 제외한 모든 메시지 유형과 채널에 적용됩니다. 즉, 억제 목록은 기본적으로 다음을 포함한 모든 채널, Campaign, Canvases에 적용됩니다:
- [API 캠페인]({{site.baseurl}}/api/api_campaigns/)
- API 트리거 Campaign 및 Canvases
- [트랜잭션 이메일]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/)

억제 목록이 적용되지 않는 유일한 메시지 유형은 피처 플래그입니다. 억제 목록에 있는 사용자는 피처 플래그에서는 억제되지 않지만, 다른 모든 채널에서는 억제됩니다.

예외 태그를 사용하면 억제 목록 사용자가 특정 Campaign 및 Canvases의 타겟이 될 수 있습니다. 자세한 내용은 [억제 목록 설정하기](#setup)의 4단계를 참조하세요. 억제 목록에 예외 태그를 추가하지 않으면 해당 억제 목록의 사용자는 피처 플래그를 제외한 어떤 메시징의 타겟도 되지 않습니다.

{% alert note %}
억제 목록은 Braze 대시보드에서 `campaign_id`로 생성된 API 캠페인에 적용됩니다. 억제 목록은 연결된 `campaign_id` 없이 [Braze 메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/)를 통해 전송된 메시지에는 적용되지 않습니다.
{% endalert %}

![API 트리거 Campaign 및 Canvases에 억제 목록을 적용하지 않는 체크박스가 있는 '예외 설정' 섹션.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## 억제 목록 설정하기 {#setup}

{% alert note %}
모든 사용자가 억제 목록을 볼 수 있지만, [관리자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions?tab=admin)이 있는 사용자만 억제 목록을 생성하고 관리할 수 있습니다.
{% endalert %}

1. **오디언스** > **억제 목록**으로 이동합니다.<br><br>![세 개의 억제 목록이 나열된 '억제 목록' 페이지.]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. **억제 목록 생성**을 선택하고 이름을 추가합니다.<br><br>![이름을 입력하는 필드가 있는 '억제 목록 생성' 창.]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
3. Segment 필터를 사용하여 억제 목록에 포함할 사용자를 식별합니다. 최소 하나 이상을 선택해야 합니다.

{% alert important %}
설정 과정이 [Segment 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/)과 유사해 보이지만, 억제 목록은 Segment 멤버십과 관계없이 메시지를 보내고 싶지 **않은** 사용자 그룹입니다.
{% endalert %}

![90일 이상 이메일을 열지 않은 사용자에 대한 필터가 있는 억제 목록 빌더.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4. Segment 이름 아래의 체크박스를 선택하여 태그 기반 예외를 설정할지 결정한 다음(자세한 내용은 [억제 목록을 사용하는 이유](#why-use-suppression-lists) 참조), 이 억제 목록의 사용자가 여전히 수신해야 하는 Campaign 또는 Canvases의 태그를 추가합니다.<br><br>즉, 예외 태그 "배송 확인"을 추가하면 억제 목록의 사용자는 "배송 확인" 태그를 사용하는 메시지를 제외한 모든 메시징에서 제외됩니다.<br><br>!['배송 확인'이라는 예외 태그가 적용된 '배송 목록 세부 정보' 섹션.]({% image_buster /assets/img/exception_tags.png %})<br><br>
5. 억제 목록을 저장하거나 활성화합니다.
- 저장하면 억제 목록이 저장되지만 활성화되지 않으므로 효력이 발생하지 않습니다. 억제 목록은 활성화할 때까지 비활성 상태로 유지되며, 비활성 억제 목록은 메시징에 영향을 미치지 않습니다(사용자가 메시지에서 제외되지 않습니다).
- 활성화하면 억제 목록이 저장되고 즉시 효력이 발생하여, 억제 목록의 사용자가 Campaign 또는 Canvases(예외 태그가 포함된 것 제외)에서 즉시 제외됩니다.

{% alert note %}
관리자만 억제 목록을 저장하거나 활성화할 수 있습니다. 베타 기간 동안 한 번에 최대 5개의 활성 억제 목록을 가질 수 있습니다.
{% endalert %}

더 이상 필요하지 않은 억제 목록은 비활성화하거나 아카이브할 수 있습니다.
- 비활성화하려면 활성 억제 목록을 선택하고 **비활성화**를 선택합니다. 비활성화된 억제 목록은 나중에 다시 활성화할 수 있습니다.
- 아카이브하려면 **억제 목록** 페이지에서 수행합니다.

## 억제 목록 사용 {#suppression-list-usage}

억제 목록이 사용자의 메시지 수신을 차단했는지 확인하려면 Campaign 또는 Canvas의 **타겟 오디언스** 단계에서 **사용자 조회**를 사용하세요. 여기에서 해당 사용자가 어떤 억제 목록에 포함되어 있는지 확인할 수 있습니다.

{% alert note %}
억제 목록은 Campaign이 시작된 후가 아니라 메시지가 전송되기 전에 업데이트됩니다. 즉, Campaign 시작 후 메시지 전송 전에 억제 목록에 추가된 사용자는 여전히 메시지를 수신하지 못할 수 있습니다.
{% endalert %}

![사용자가 억제 목록에 있음을 보여주는 '사용자 조회' 창.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
**요약** 단계에서도 적용된 억제 목록을 확인할 수 있습니다.
{% endalert %}

Campaign 또는 Canvas를 생성하는 동안 **타겟 오디언스** 단계에서 **사용자 조회**를 사용하여 사용자를 검색하고, 해당 사용자가 타겟 오디언스에 포함되지 않은 경우 어떤 억제 목록에 포함되어 있는지 확인할 수 있습니다.

![사용자가 억제 목록에 있음을 보여주는 '사용자 조회' 창.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Campaign

사용자가 억제 목록에 있는 경우, 해당 억제 목록이 적용되는 Campaign을 수신하지 않습니다. 억제 목록이 적용되지 않는 경우에 대해서는 [억제 목록의 영향을 받는 메시지 유형 및 채널](#message-types-and-channels-affected-by-suppression-lists)을 참조하세요.

!['낮은 마케팅 건강 점수'라는 하나의 활성 억제 목록이 있는 '억제 목록' 섹션.]({% image_buster /assets/img/active_suppression_list.png %})

### Canvas

사용자가 억제 목록에 추가되는 순간부터 Canvases에 진입하지 않습니다. 이미 Canvas에 진입한 경우 메시지 단계를 수신하지 않습니다. 즉, 사용자가 이미 Canvas 내에 있을 때 억제 목록에 추가되면 다음 메시지 단계까지 Canvas를 진행한 후, 메시지 단계를 수신하지 않고 이탈합니다.

예를 들어, Canvas에 사용자 업데이트 단계 다음에 메시지 단계가 있다고 가정해 보겠습니다. 사용자가 Canvas에 진입한 후 억제 목록에 추가되면, 해당 사용자는 사용자 업데이트 단계(업데이트될 수 있음)를 계속 진행한 다음 메시지 단계에서 이탈하며, 이 시점에서 이탈 측정기준에 포함됩니다.