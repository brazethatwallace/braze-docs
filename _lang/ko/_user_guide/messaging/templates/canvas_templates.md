---
nav_title: 캔버스 템플릿
article_title: 캔버스 템플릿 생성
page_order: 2
alias: "/canvas_templates/"
description: "재사용 가능한 캔버스 템플릿을 생성하고 관리하거나, 일반적인 사용 사례를 위해 미리 구축된 Braze 템플릿으로 시작하세요."
---

# 캔버스 템플릿 생성 {#create-a-canvas-template}

> 이 참조 문서에서는 Canvas 템플릿을 생성하고 관리하는 방법을 다룹니다. 템플릿을 사용하면 Canvases 전반에서 특정 목표에 맞게 쉽게 커스터마이즈할 수 있는 일관된 프레임워크를 만들어 메시징을 개선할 수 있습니다.

{% alert tip %}
[Braze 캔버스 템플릿](#available-braze-templates)을 사용하여 시간을 절약하고 Canvas 생성을 간소화하세요! 미리 구축된 템플릿 라이브러리를 탐색하여 사용 사례에 맞는 템플릿을 찾고 특정 요구 사항에 맞게 커스터마이즈하세요.
{% endalert %}

## 방법 1: 기존 Canvas에서 생성 {#method-1-create-from-an-existing-canvas}

### 1단계: 기존 Canvas 선택 {#step-1-select-your-existing-canvas}

Braze 대시보드에서 **메시징** > **Canvas**로 이동하여 템플릿으로 사용할 기존 Canvas를 선택합니다.

### 2단계: 템플릿 생성 {#step-2-create-your-template}

Canvas 편집기에서 Canvas가 활성 상태인지 임시저장 상태인지에 따라 **Edit Canvas** 또는 **Edit draft**를 선택합니다. 하단의 **Save as draft** 드롭다운을 펼치고 **Save as template**을 선택합니다.

![]({% image_buster /assets/img/save_canvas_as_template.png %})

### 3단계: 템플릿 저장 {#step-3-save-your-template}

다음으로 템플릿에 이름을 지정하고 관련 태그를 추가합니다. 그런 다음 **Save**를 선택합니다. 이제 템플릿을 사용하여 Canvas를 구축할 수 있으며, 기본 설정과 단계가 이미 준비되어 있어 빠르게 시작할 수 있습니다.

## 방법 2: 캔버스 템플릿 편집기를 통해 생성 {#method-2-create-via-canvas-template-editor}

### 1단계: 캔버스 템플릿 편집기로 이동 {#step-1-go-to-the-canvas-template-editor}

Braze 대시보드에서 **Content** > **Canvas**로 이동합니다.

### 2단계: 새 템플릿 생성 {#step-2-create-a-new-template}

**Create template**을 선택하고 Canvas 세부 정보를 설정합니다. 먼저 캔버스 템플릿에 이름을 지정할 수 있습니다.

![설명이 "연간 봄 프로모션에 사용"인 "연간 세일 캔버스 템플릿"이라는 이름의 캔버스 템플릿 예시.]({% image_buster /assets/img/canvas_template_example.png %})

### 3단계: 템플릿 커스터마이즈 {#step-3-customize-your-template}

다음으로 [Canvas를 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-2-build-your-canvas)하여 템플릿을 커스터마이즈합니다. 사용자가 Canvas에 진입하는 시점, Canvas에 진입할 수 있는 사용자, 발송 설정 조정, 템플릿의 사용자 여정 구축 등을 결정할 수 있습니다.

### 4단계: 템플릿 저장 {#step-4-save-your-template}

템플릿 커스터마이즈를 완료한 후 **Save template** 버튼을 선택합니다. **캔버스 템플릿** 페이지에서 <i class="fas fa-list" aria-label="템플릿 세부 정보"></i> **Template details**를 선택하여 캔버스 템플릿 세부 정보를 확인할 수 있습니다.

## 캔버스 템플릿 사용 {#using-canvas-templates}

Canvas를 작성할 때 템플릿을 사용하는 두 가지 방법이 있습니다:

- **메시징에서**: **Messaging** > **Canvas**로 이동합니다. **Create Canvas** 버튼을 선택한 다음 **Use a Canvas Template**을 선택합니다.
- **콘텐츠에서**: **Content** > **Canvas**로 이동하여 **Canvas templates**에서 원하는 템플릿을 찾습니다. 그런 다음 <i class="fas fa-ellipsis-vertical" aria-label="더 보기 메뉴"></i> 메뉴를 선택한 후 **Apply template**을 선택합니다. 그러면 Canvas 작성기에서 템플릿이 적용된 새 Canvas로 이동합니다.

### 사용 가능한 Braze 템플릿 {#available-braze-templates}

사용 가능한 캔버스 템플릿 목록은 [Braze 캔버스 템플릿]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/)을 참조하세요. eCommerce 캔버스 템플릿 사용에 대한 자세한 내용은 [eCommerce 추천 이벤트 사용 방법]({{site.baseurl}}/ecommerce_use_cases/)을 참조하세요.

## 캔버스 템플릿 관리 {#managing-canvas-templates}

캔버스 템플릿은 실제 Canvas와 마찬가지로 복제하고 아카이브할 수 있습니다. 캔버스 템플릿을 편집하려면 템플릿을 선택한 다음 **<i class="fas fa-pencil-alt"></i>Edit**를 선택합니다.

워크스페이스 수준에서 사용자 권한을 업데이트하여 캔버스 템플릿의 생성, 편집, 보기 또는 아카이브에 대한 접근을 허용하거나 제한할 수 있습니다.

### Teams 및 워크스페이스 권한 {#permissions-for-teams-and-workspaces}

특정 사용자만 특정 캔버스 템플릿에 접근하고 사용할 수 있도록 하려면 템플릿에 [팀을 추가]({{site.baseurl}}/user_guide/administer/global/user_management/teams/)한 다음 팀 수준의 "Access Campaigns, Canvases, Content Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Center" 권한을 할당합니다.

다음 권한 중 하나를 팀 수준에서 할당하되 워크스페이스 수준에서는 할당하지 않으면, 팀에 할당된 항목에 대해서만 다음 작업을 수행할 수 있습니다:

- 캔버스 템플릿 생성 및 편집
- 캔버스 템플릿 보기
- 캔버스 템플릿 아카이브

워크스페이스와 Teams 수준 모두에서 권한이 부여된 경우 워크스페이스 수준 권한이 우선합니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 캔버스 템플릿에서 불완전한 단계를 저장할 수 있나요? {#can-i-save-an-incomplete-step-in-a-canvas-template}

네, 불완전한 단계를 캔버스 템플릿으로 저장할 수 있습니다. 그러나 해당 템플릿을 사용할 때 **Save template** 버튼에 Canvas를 시작하기 위해 필요한 사항을 나타내는 오류가 표시됩니다.

### Canvas 빌더 설정을 템플릿으로 저장할 수 있나요, 아니면 단계만 저장할 수 있나요? {#can-i-save-my-canvas-builder-settings-as-a-template-or-can-i-only-save-steps}

네, 캔버스 템플릿 내에서 Canvas 빌더의 설정을 저장할 수 있습니다. 예를 들어, Segments와 필터의 조합을 자주 사용할 계획이라면 이러한 **타겟 오디언스** 설정을 캔버스 템플릿의 일부로 저장할 수 있습니다.