---
nav_title: 링크 템플릿
article_title: 링크 템플릿
page_order: 4
description: "이 문서에서는 이메일에서 다양한 유형의 링크 템플릿을 만드는 방법을 설명합니다."
tool:
  - Templates
channel:
  - email

---

# 링크 템플릿 {#link-templates}

> 링크 템플릿을 사용하면 매개변수를 추가하거나 URL을 앞에 삽입하여 이메일 Campaign을 위한 동적이고 재사용 가능한 링크를 만들 수 있습니다. 이를 통해 Campaign과 메시지 전반에서 URL의 일관성을 유지할 수 있습니다.

{% alert note %}
링크 템플릿은 선택적 기능입니다. **템플릿** 섹션에 **이메일 링크 템플릿**이 표시되지 않는 경우, 계정 매니저에게 연락하여 기능을 활성화하세요.
{% endalert %}

## 작동 방식 {#how-it-works}

링크 템플릿은 주로 다음과 같은 사용 사례에서 활용됩니다:

- 특정 이메일 메시지의 모든 링크에 Google Analytics 쿼리 매개변수 추가
- 특정 이메일 메시지의 모든 링크 앞에 URL 삽입

예를 들어, 신제품 출시를 위한 프로모션 이메일 Campaign을 진행한다고 가정해 보겠습니다. 링크 템플릿을 사용하여 사용자를 제품 페이지로 안내하고, 사용자의 이름이나 특정 프로모션 코드를 포함하도록 링크를 개인화할 수 있습니다. 이를 통해 링크를 클릭한 사용자 수와 구매 여부를 추적할 수 있습니다. 이렇게 하면 링크 전반에서 일관성을 유지하고 분석을 더 효과적으로 추적할 수 있습니다.

## 링크 템플릿 만들기 {#creating-a-link-template}

다양한 요구 사항을 지원하기 위해 무제한으로 링크 템플릿을 만들 수 있습니다. 링크 템플릿을 만들려면 다음을 수행하세요:

1. **콘텐츠** > **이메일 링크**로 이동합니다.
2. **이메일 링크 템플릿 생성**을 선택합니다.
3. 링크 템플릿에 이름을 지정합니다.
4. (선택 사항) 링크 템플릿에 대한 세부 정보를 추가하기 위해 설명, 팀 또는 태그를 추가합니다.
5. (선택 사항) 이메일 Campaign 및 Canvases의 링크에 링크 템플릿을 자동으로 추가하려면 토글을 선택합니다. 이는 새 이메일 또는 기존 이메일에 새 링크를 추가할 때 적용됩니다.

만들 수 있는 링크 템플릿에는 두 가지 유형이 있습니다:

- [URL 앞에 삽입하는 링크 템플릿](#prepend-link-template)
- [URL 뒤에 삽입하는 링크 템플릿](#append-link-template)

링크 템플릿과 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)를 함께 사용할 때, 일관된 렌더링을 위해 Liquid는 본문 태그 내에서만 추가해야 합니다.

### 앞에 삽입: URL 앞에 삽입하는 링크 템플릿 만들기 {#prepend-link-template}

이메일 메시지의 링크 앞에 문자열이나 URL을 추가하려면 다음을 수행하세요:

1. 새 링크 템플릿을 만듭니다.
2. **Template Position**을 **Before URL**로 설정합니다.
3. 항상 URL 앞에 추가될 문자열을 입력합니다.

**Template Preview**에서 링크 템플릿이 URL 앞에 어떻게 삽입되는지 예시를 확인할 수 있습니다.

![URL 앞에 링크 템플릿을 삽입하는 과정의 Template Position, Prepend URL, Template Preview 필드.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### 뒤에 삽입: URL 뒤에 삽입하는 링크 템플릿 만들기 {#append-link-template}

이메일 메시지의 URL 뒤에 쿼리 매개변수를 추가하려면:

1. 새 링크 템플릿을 만듭니다.
2. **Template Position**을 **After URL**로 설정합니다.
3. 각 URL 끝에 쿼리 매개변수(`value=example`)를 입력합니다. URL 끝에 여러 매개변수를 추가할 수 있습니다.

![URL 뒤에 링크 템플릿을 삽입하는 과정의 Template Position, Query Parameters, Template Preview 필드.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## 이메일 Campaign에서 링크 템플릿 사용하기 {#using-link-templates-in-email-campaigns}

링크 템플릿을 설정한 후 이메일에 적용할 수 있습니다.

HTML 편집기 또는 드래그 앤 드롭 편집기에서 링크 템플릿을 적용하려면 다음 단계를 따르세요:

{% alert important %}
업데이트된 HTML 편집기 또는 드래그 앤 드롭 편집기에서 **Link Management** 탭에 접근하려면 링크 별칭 지정이 활성화되어 있어야 합니다. 링크 별칭 지정을 활성화하려면 계정 매니저에게 문의하세요. 자세한 내용은 [링크 별칭 지정]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing/)을 참조하세요.
{% endalert %}

- **업데이트된 HTML 편집기:** **Content** 탭에서 **Link Management**를 선택하고, **Add a Link Template**를 선택한 다음, 링크 템플릿을 선택하고 **Add**를 선택합니다.
- **드래그 앤 드롭 편집기:** **Content** 탭에서 **Link Management**를 선택하고, **Add a Link Template**를 선택한 다음, 링크 템플릿을 선택하고 **Add**를 선택합니다.

![드래그 앤 드롭 편집기의 Link Management 탭에 링크 템플릿 예시 목록이 표시된 모습.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
링크 템플릿은 일반 텍스트에는 적용되지 않습니다. 즉, Currents에서 링크 템플릿의 매개변수가 포함되지 않은 클릭이 표시될 수 있으며, 이러한 클릭은 이메일의 일반 텍스트 버전에서 발생한 것일 수 있습니다.
{% endalert %}

**Link Management** 탭에서 링크 템플릿을 추가할 때, 오른쪽으로 스크롤하여 추가한 템플릿을 확인할 수 있습니다. 이메일 내 기존 링크에 이미 링크 템플릿이 추가되어 있는 경우, 새로 추가되는 링크에도 기본적으로 해당 링크 템플릿이 추가됩니다.

## 링크 템플릿 관리하기 {#managing-link-templates}

링크 템플릿을 [복제]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)할 수도 있습니다. 템플릿 및 크리에이티브 콘텐츠를 만들고 관리하는 방법에 대한 자세한 내용은 [템플릿 및 미디어]({{site.baseurl}}/user_guide/messaging/templates/)를 참조하세요.

{% alert important %}
링크 템플릿에는 현재 아카이브 기능을 사용할 수 없습니다.
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

링크 템플릿에 대한 자주 묻는 질문의 답변은 [템플릿 FAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq/) 페이지를 확인하세요.