---
nav_title: 다단계 양식
article_title: 다단계 랜딩 페이지 양식
page_order: 2
page_type: reference
description: "Braze 랜딩 페이지에서 다단계 양식을 작성하고, 드래그 앤 드롭 편집기에서 단계를 관리하며, 기본 제공 확인 단계를 커스텀하는 방법을 알아보세요."
---

# 다단계 랜딩 페이지 양식 {#multi-step-landing-page-forms}

> 긴 랜딩 페이지 양식을 여러 단계로 나누고, 각 단계에 고유한 필드를 배치하여 사용자가 한 단계씩 양식을 진행하도록 할 수 있습니다. 모든 다단계 양식에는 잠긴 확인 단계가 포함되어 있어, 사용자가 제출 후 항상 확인 화면을 볼 수 있습니다.

## 전제 조건 {#prerequisites}

랜딩 페이지 빌더에 접근하려면 [특정 권한]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites)이 필요합니다. 접근 권한이 없는 경우 Braze 관리자에게 도움을 요청하세요.

또한 [랜딩 페이지 양식 블록]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page)에 대해 숙지하고 있어야 합니다.

## 다단계 양식의 작동 방식 {#how-multi-step-forms-work}

다단계 양식을 만들려면 **빌드** 패널의 **레이아웃** 섹션에서 **Form** 행을 추가합니다. **Form** 행에는 기본 제공 실행 버튼과 다단계 지원이 포함되어 있으므로 행 구조를 직접 조립할 필요가 없습니다.

랜딩 페이지당 **Form** 행은 하나만 추가할 수 있습니다. 페이지에 드래그하면 단일 단계와 제출 후 실행되는 잠긴 확인 단계로 시작됩니다.

{% alert note %}
**Form** 행은 자체적으로 다단계 탐색을 관리하므로, 모든 단계가 한 페이지의 단일 행 안에 존재합니다. 이는 단일 단계 양식을 작성하고 **Submit** 버튼을 별도의 확인 랜딩 페이지에 연결하는 표준 방식과 다릅니다. 자세한 내용은 [4단계: 확인 페이지 만들기]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional)를 참조하세요.
{% endalert %}

![랜딩 페이지 작성기의 다단계 랜딩 페이지 양식.]({% image_buster /assets/img/landing_pages/multi_step_form.png %})

## 다단계 양식 추가 {#add-a-multi-step-form}

1. 랜딩 페이지 편집기에서 **빌드** 패널로 이동하여 **레이아웃**을 선택합니다.
2. **Form** 행을 페이지로 드래그합니다.
3. **Form** 행을 선택한 상태에서 오른쪽 속성 패널의 **Steps** 섹션을 사용하여 양식을 구성합니다:
   - **Step 1**에 [양식 블록]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-3-customize-the-page)(예: **Email Capture**, **Phone Capture**, **Input Field**, **Dropdown**, **Checkbox** 또는 **Checkbox Group**)을 추가합니다.
   - **Add step**을 선택하여 추가 단계를 만들고, 각 단계에 양식 블록을 추가합니다.

예를 들어, 3단계 양식에서 **Step 1**에서는 이름을, **Step 2**에서는 전화번호를 입력받고, **Confirmation** 단계에서 사용자에게 제출에 대한 감사 메시지를 표시할 수 있습니다.

## 편집 중 단계 간 이동 {#navigate-between-steps-while-editing}

편집기에서 두 가지 방법으로 단계 간에 이동할 수 있습니다:

| 방법 | 사용 방법 |
|--------|--------|
| 단계 탐색기 | 캔버스에서 **Step X of Y** 컨트롤을 사용하여 이전 또는 다음 단계로 이동합니다. |
| 단계 패널 | **Form** 행을 선택한 다음, 오른쪽 속성 패널의 **Steps** 섹션을 사용하여 **Confirmation** 단계를 포함한 특정 단계로 직접 이동합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="편집 중 단계 간 이동" }

## 단계 관리 {#manage-steps}

**Form** 행의 속성 패널에 있는 **Steps** 섹션을 사용하여 단계를 추가, 제거 및 재정렬할 수 있습니다:

| 작업 | 사용 방법 |
|--------|--------|
| 단계 추가 | **Add step**을 선택합니다. 새 단계는 기존 단계 뒤, **Confirmation** 단계 앞에 추가됩니다. |
| 단계 제거 | 제거하려는 단계 옆의 휴지통 아이콘을 선택합니다.<br><br>**Confirmation** 단계에는 휴지통 아이콘이 없으며 제거하거나 재정렬할 수 없습니다. 확인 단계는 사용자가 이전 단계를 모두 완료한 후 항상 마지막에 실행됩니다. |
| 단계 재정렬 | 단계 옆의 드래그 핸들을 사용하여 순서를 변경합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="단계 관리" }

## 확인 단계 커스텀 {#customize-the-confirmation-step}

모든 다단계 양식에는 **Steps** 섹션의 **After submission** 아래에 **Confirmation** 단계가 포함되어 있습니다. 이 단계는 삭제할 수 없도록 잠겨 있어, 사용자가 양식을 제출한 후 항상 확인 화면을 볼 수 있습니다.

**Confirmation** 단계는 제거할 수 없지만, 다른 단계와 마찬가지로 커스텀할 수 있습니다. **Steps** 섹션에서 해당 단계를 선택한 다음, 블록을 추가하고 스타일을 지정하여 확인 메시지를 작성하세요.

## 부분 완료된 양식의 데이터 추적 {#track-data-from-partially-completed-forms}

사용자가 **Confirmation** 단계에 도달하기 전에 양식을 떠나더라도, Braze는 완료된 단계의 데이터를 고객 프로필에 저장합니다. **Submitted a Landing Page form** 이벤트는 사용자가 모든 단계를 완료하고 **Confirmation** 단계에 도달할 때까지 기록되지 않습니다.

{% alert note %}
[리타겟팅 및 트리거 전달]({{site.baseurl}}/user_guide/messaging/landing_pages/retargeting_users)은 **Submitted a Landing Page form** 이벤트에 의존합니다. 일부 단계만 제출한 사용자의 데이터는 프로필에 저장되지만, 부분 데이터가 캡처되었더라도 해당 이벤트에는 포함되지 않습니다.
{% endalert %}

이는 최종 단계에 도달하지 못한 사용자가 부분 제출로 추적되는 [랜딩 페이지 설문조사]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys)와 다릅니다.

## 제한 사항 및 고려 사항 {#limitations-and-considerations}

- 랜딩 페이지는 단일 **Form** 행을 지원하므로, 모든 단계와 확인 단계가 하나의 행에 존재합니다.
- 데이터 수집 단계는 최대 10개까지 추가할 수 있습니다. **Confirmation** 단계는 이 제한에 포함되지 않습니다.
- 각 단계에는 클릭 시 다음 단계로 이동하도록 설정된 기본 버튼이 포함되어 있습니다. 이 동작은 현재 단계의 입력을 검증하고 저장합니다. 마지막 데이터 수집 단계에서는 **Submitted a Landing Page form** 이벤트도 기록하고 **Confirmation** 단계로 진행합니다. 단계가 연결되지 않은 경우, 버튼이 다음 단계로 이동하도록 클릭 시 동작을 추가하세요. 자세한 내용은 편집기 블록의 [버튼]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages)을 참조하세요.
- **Confirmation** 단계가 **Form** 행에 기본 제공되므로, 확인 화면으로 사용할 두 번째 랜딩 페이지를 만들거나 연결할 필요가 없습니다.
- **레이아웃** 아래에 **Form** 행이 보이지 않는 경우, Braze 계정 매니저에게 문의하세요.