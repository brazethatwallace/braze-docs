---
nav_title: 템플릿 관리
article_title: 템플릿 관리
page_order: 1

page_type: reference
description: "이 참조 문서에서는 Braze 대시보드의 템플릿 섹션에서 템플릿을 복제하고 아카이브하는 방법을 설명합니다."
tool:
  - Templates
  - Media

---

# 템플릿 관리 {#manage-templates}

> 템플릿을 아카이브하거나 복제하면 더 효과적으로 정리하고 관리할 수 있습니다. 이 참조 문서에서는 Braze 대시보드의 **템플릿** 섹션에서 템플릿을 아카이브하고 복제하는 방법을 다룹니다.

## 템플릿 복제 {#duplicating-templates}

{% tabs %}
{% tab 개별 템플릿 %}

![복제 옵션이 있는 드롭다운 메뉴.]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

개별 템플릿을 복제하려면 해당 템플릿의 <i class="fas fa-ellipsis-v"></i> **추가 옵션**을 선택한 다음, 드롭다운 메뉴에서 **복제**를 선택합니다.
<br><br>

{% alert note %}
[콘텐츠 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) 템플릿의 경우 초안 사본이 생성됩니다. 다른 모든 템플릿의 경우 새 복제 사본이 자동으로 생성됩니다.
{% endalert %}

{% endtab %}
{% tab 다중 템플릿 %}

{% raw %}

여러 템플릿을 복제하려면 템플릿 이름 옆의 체크박스를 선택합니다. 먼저 템플릿을 선택한 다음 **복제**를 선택합니다.

복제된 템플릿은 **마지막 수정일** 열을 정렬하여 찾을 수 있습니다. 기본적으로 새 템플릿의 이름은 `Copy of ORIGINAL_TEMPLATE_NAME`으로 지정됩니다.

{% endraw %}

![마지막 수정 시간 기준으로 정렬된 세 개의 템플릿으로, 복사된 템플릿이 목록 상단에 표시됩니다.]({% image_buster /assets/img/duplicate_multiple_template.gif %})

{% endtab %}
{% endtabs %}

## 템플릿 아카이브 {#archiving-templates}

![세 가지 옵션이 표시된 확장된 설정 드롭다운 메뉴: "아카이브", "복제", "워크스페이스에 복사"이며 "아카이브" 옵션이 강조 표시되어 있습니다.]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

개별 템플릿을 아카이브하려면 템플릿 그리드 화면에서 <i class="fas fa-ellipsis-v"></i> **추가 옵션**을 선택하고 **아카이브**를 선택합니다. 템플릿이 아카이브되면 다음과 같은 시나리오에 유의하세요:

- 활성 Campaign은 아카이브된 템플릿을 중단 없이 계속 사용합니다.
- 초안 Campaign은 아카이브된 템플릿의 콘텐츠를 유지하며 편집 및 시작이 가능합니다.
- 아카이브된 템플릿을 편집하려면 먼저 아카이브를 해제해야 합니다. 마찬가지로, 아카이브된 템플릿을 Campaign에 사용하려면 먼저 템플릿의 아카이브를 해제해야 합니다.

여러 템플릿을 아카이브하려면 아카이브할 각 템플릿 옆의 체크박스를 선택합니다. 여러 템플릿을 선택한 후 **아카이브**를 선택합니다. 아카이브된 템플릿은 템플릿 그리드에서 **표시** 아래의 **아카이브됨**을 선택하여 찾을 수 있습니다.

![저장된 드래그 앤 드롭 이메일 템플릿 섹션으로, 두 개의 템플릿이 선택되어 있고 아카이브 옵션이 있는 도구 모음이 표시됩니다.]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
아카이브 기능은 현재 [링크 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing#link-templates)에서는 사용할 수 없습니다.
{% endalert %}