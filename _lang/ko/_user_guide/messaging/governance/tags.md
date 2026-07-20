---
nav_title: 태그
article_title: 태그
page_order: 6
page_type: reference
description: "이 참조 문서에서는 Braze 대시보드에서 Campaigns, Canvases, Segments 및 커스텀 데이터에 사용하는 태그를 다룹니다."
tool:
  - Campaigns
  - Canvas
---

# 태그 {#tags}

> Braze는 Segments, Campaigns, Canvases에 대한 작성자, 편집자, 날짜 및 상태 정보를 추적하며, 태그를 생성하여 인게이지먼트를 더 체계적으로 정리하고 분류할 수 있는 기능을 제공합니다.

## Campaign, Canvas 및 Segment 태그 {#campaign-canvas-and-segment-tags}

Campaign, Canvas 또는 Segment를 생성하거나 편집할 때 태그를 추가할 수 있습니다. 인게이지먼트 이름 아래에 있는 <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**태그**를 클릭하고 기존 태그를 선택하거나, 입력을 시작하여 새 태그를 추가합니다.

![Campaign 생성 중 태그를 추가하는 모습.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
Campaign, Canvas 또는 Segment에 최대 175개의 태그를 추가할 수 있습니다.
{% endalert %}

### 일괄 태그 지정 {#bulk-tagging}

여러 Campaign, Canvas 또는 Segment를 선택한 후 <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As**를 선택하여 태그를 일괄 추가할 수도 있습니다.

![여러 Campaign에 동시에 태그를 추가하는 모습.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
일괄 태그 지정을 사용하여 이미 서로 다른 태그가 있는 여러 Campaign에 새 태그를 적용하면, 선택된 각 Campaign에 새 태그가 추가되고, 한 Campaign에 있는 모든 태그가 선택된 다른 모든 Campaign에도 적용됩니다. 원래 해당 태그가 연결되어 있지 않았더라도 마찬가지입니다.
{% endalert %}

### 태그 보기 {#viewing-tags}

Campaign, Canvas 또는 Segment에 설정된 태그는 인게이지먼트 이름 근처의 세부 정보 페이지에서 확인할 수 있습니다. Campaign 분석에서도 표시됩니다.

![Campaign 분석 페이지에 표시된 태그.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### 태그로 필터링 {#filtering-by-tag}

태그는 Campaign, Canvas 또는 Segment 목록에서 **Archived** 및 **Draft**와 같은 상태 레이블의 추가 태그와 함께 표시됩니다. 태그로 필터링하려면 태그 목록에서 태그 이름을 선택합니다.

![Campaign 목록의 태그.]({% image_buster /assets/img_archive/tags_grid.png %})

## 커스텀 데이터 태그 {#custom-data-tags}

[커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes) 및 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events#adding-tags)를 관리할 때 커스텀 데이터에도 태그를 추가할 수 있습니다.

{% alert important %}
이 기능은 현재 얼리 액세스 중입니다. 이 얼리 액세스에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

대시보드 전반에서 태그의 이름을 변경하거나, 제거하거나, 중첩하는 방법에 대한 자세한 내용은 [태그 관리]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 참조하세요.