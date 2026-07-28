---
nav_title: 스타일 설정
article_title: "인앱 메시지 스타일 설정"
description: "이 참조 문서에서는 드래그 앤 드롭 편집기로 인앱 메시지를 만들 때 사용할 수 있는 스타일 옵션을 다룹니다."
page_order: 1
---

# 인앱 메시지 스타일 설정 {#in-app-message-style-settings}

> 드래그 앤 드롭 편집 환경은 **구축**과 **미리보기 및 테스트** 두 섹션으로 나뉩니다. 이 문서에서는 편집기의 **구축** 탭에서 작업할 때 알아야 할 내용을 다루며, 이미 [인앱 메시지를 생성]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)했다고 가정합니다.

!["메시지 스타일" 탭.]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## 메시지 수준 스타일 {#message-level-styles}

**메시지 스타일** 탭에서 인앱 메시지의 모든 관련 블록에 적용할 특정 스타일을 설정할 수 있습니다. 예를 들어, 메시지 내 모든 텍스트의 글꼴이나 모든 링크의 색상을 커스터마이즈할 수 있습니다.

이 섹션의 스타일은 특정 블록에서 재정의하지 않는 한 메시지 전체에 적용됩니다. 메시지에 [여러 페이지]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page)가 있는 경우, 표시 유형과 최대 너비를 제외하고 개별 페이지에 대해 메시지 수준 스타일을 재정의할 수도 있습니다.

보다 쉬운 디자인 경험을 위해, 블록 수준에서 스타일을 커스터마이즈하기 전에 메시지 수준 스타일을 먼저 설정하는 것을 권장합니다.

언제든지 **메시지 스타일** 탭으로 돌아가려면:

- 개별 블록 속성의 닫기 X 버튼을 클릭합니다
- 메시지 컨테이너, 메시지 닫기 X 버튼 또는 편집기 배경을 선택합니다

### 커스텀 글꼴 {#custom-fonts}

글꼴에 대해 다음 파일 유형을 지원합니다: `.ttf`, `.woff`, `.otf`, `.woff2`. 자세한 내용은 [자산 파일]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#asset-files)을 참조하세요.

일부 스타일 옵션은 커스텀 글꼴에서 사용할 수 없을 수 있으므로, 글꼴 패밀리의 여러 변형을 추가할 수 있습니다. 현재 URL을 통한 글꼴 추가는 지원하지 않습니다.

커스텀 글꼴을 추가하려면:

1. **메시지 스타일** 탭의 **콘텐츠** 섹션으로 이동합니다.
2. **커스텀 글꼴 추가**를 클릭합니다.
3. 미디어 라이브러리를 사용하여 글꼴을 업로드합니다.

{% alert note %}
메시지 수준 글꼴은 현재 메시지와 복제된 메시지에만 적용되며, 향후 템플릿에는 적용되지 않습니다.
{% endalert %}

## 메시지 구성요소 {#message-components}

![프로모션 인앱 메시지를 만드는 과정을 보여주는 GIF.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

드래그 앤 드롭 편집기는 인앱 메시지를 구성하기 위해 **행**과 **블록**이라는 두 가지 핵심 구성요소를 사용합니다. 모든 블록은 행 안에 배치해야 합니다.

### 닫기 X 버튼 {#close-x-button}

Modal 및 전체화면 인앱 메시지의 경우, 메시지 상단에 <i class="fa-solid fa-xmark"></i>로 표시되는 닫기 버튼을 커스터마이즈할 수 있습니다. 커스터마이즈 옵션에는 버튼 위치, 크기, 채우기 색상, 배경 색상, 테두리 스타일, 테두리 반경이 포함됩니다.

![버튼 크기, 채우기 색상, 배경 색상, 테두리 스타일, 테두리 반경을 포함한 인앱 메시지의 닫기 X 버튼 커스터마이즈 옵션.]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### 스팬 스타일링 {#span-styling}

인앱 메시지 내 텍스트에 스팬 스타일링을 추가하면 메시지 외관을 더욱 세밀하게 커스터마이즈할 수 있어, 다양한 텍스트 색상, 글꼴, 크기를 사용할 수 있습니다. 스팬 스타일링은 핵심 정보에 주의를 끌고 전체적인 메시지 명확성을 개선하여 사용자에게 더 매력적이고 시각적으로 돋보이는 경험을 제공합니다.

![인앱 메시지에서 텍스트를 강조 표시할 때 표시되는 옵션. 작은 붓 아이콘이 스타일을 위해 스팬으로 감쌀 수 있음을 보여줍니다.]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

![최종사용자가 글꼴 패밀리, 글꼴 두께, 글꼴 크기, 자간, 텍스트 색상을 커스터마이즈할 수 있는 "스팬 속성" 사이드 패널.]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### 행 {#rows}

행은 셀을 사용하여 메시지 섹션의 수평 구성을 정의하는 구조적 단위입니다.

![인앱 메시지에 추가할 수 있는 행.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

행을 선택하면 **열 커스터마이즈** 섹션에서 필요한 열 수를 추가하거나 제거하여 다양한 콘텐츠 요소를 나란히 배치할 수 있습니다.

슬라이드하여 기존 열의 크기를 조정할 수도 있습니다.

!["열 커스터마이즈" 섹션에서 열을 조정하는 모습.]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

모범 사례로, 행 내부의 블록을 서식 지정하기 전에 행과 열 속성을 먼저 서식 지정하세요. 간격과 정렬을 조정할 수 있는 곳이 많으므로, 기초부터 시작하면 진행하면서 편집하기가 더 쉬워집니다.

#### 배경 이미지 {#background-image}

**행 속성** 패널에서 행에 배경 이미지를 추가할 수 있습니다. **배경 이미지**를 토글하여 켠 다음, 이미지 URL을 제공하거나 [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)에서 이미지를 선택합니다. 마지막으로, 대체 텍스트, 크기, 위치, 이미지가 행 전체에 패턴을 만들기 위해 반복되는지 여부를 설정합니다.

![수평 반복 패턴이 적용된 피자 배경 이미지가 있는 행.]({% image_buster /assets/img_archive/background_row.png %})

### 블록 {#blocks}

블록은 메시지에서 사용할 수 있는 다양한 유형의 콘텐츠를 나타냅니다. 기존 행 세그먼트 안으로 드래그하면 셀 너비에 맞게 자동 조정됩니다.

{% alert tip %}
블록을 추가하기 전에, 메시지 컨테이너, 글꼴, 색상 및 커스터마이즈하려는 기타 항목에 대한 [메시지 수준 스타일](#set-message-level-styles)을 설정하세요. 그런 다음 필요에 따라 개별 블록을 커스터마이즈할 수 있습니다. **닫기 버튼**은 메시지 상단 섹션에 유지되어 사용자가 항상 메시지를 닫을 수 있는 옵션을 갖게 됩니다.
{% endalert %}

![선택할 수 있는 드래그 앤 드롭 상자.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

모든 블록에는 패딩에 대한 세밀한 제어와 같은 자체 설정이 있습니다. 오른쪽 패널은 선택한 콘텐츠 요소에 대한 스타일링 패널로 자동 전환됩니다. 자세한 내용은 [편집기 블록 속성]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages#inappmessages_properties)을 참조하세요.

인앱 메시지를 구축하면서 도구 모음에서 모바일, 태블릿 또는 데스크탑 보기를 선택하여 사용자 그룹에게 인앱 메시지가 어떻게 보일지 미리 볼 수 있습니다. 이를 통해 콘텐츠가 응답형인지 확인하고, 진행하면서 필요한 조정을 할 수 있습니다.

## 크리에이티브 세부 정보 {#creative-details}

### 큰 화면에서의 전체화면 {#fullscreen}

태블릿이나 데스크탑 브라우저에서 전체화면 인앱 메시지는 앱 화면 중앙에 위치합니다. 전체화면 메시지의 최대 너비에 대한 편집은 태블릿 및 데스크탑 기기에만 적용됩니다.

![전체화면 인앱 메시지 예시.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### 배경 이미지 추가 {#adding-a-background-image}

**메시지 스타일** 탭에서 메시지 배경에 이미지를 추가할 수 있습니다.

1. 캔버스 영역에서 배경 컨테이너를 선택합니다. 이것은 메시지의 스크롤 가능한 섹션입니다.
2. **메시지 스타일** 탭에서 **배경 이미지**를 켭니다.
3. 미디어 라이브러리에서 이미지를 추가하거나, 이미지가 호스팅된 URL을 입력합니다.

{% alert tip %}
특정 블록을 선택하는 데 어려움이 있는 경우, 블록의 인라인 도구 모음에서 위쪽 화살표를 사용하여 각 상위 블록으로 포커스를 이동할 수 있습니다.
{% endalert %}

#### Liquid로 배경 이미지 동적 교체 {#swap-background-images-with-liquid}

사용자 데이터(커스텀 속성이나 사용자 속성정보 등)를 기반으로 배경 이미지를 동적으로 교체하려면, Liquid {% raw %}`{% capture %}`{% endraw %} 블록을 사용하여 HTML과 CSS가 로드되기 전에 올바른 이미지 URL을 변수에 할당합니다.

메시지 시작 부분에 Liquid 로직을 배치한 다음, 배경 이미지 URL 필드에서 캡처된 변수를 참조합니다. 이렇게 하면 각 사용자의 데이터를 기반으로 올바른 이미지가 선택됩니다.

이미지 URL을 캡처한 후, {% raw %}`{{ image_url | strip }}`{% endraw %}을 사용하여 불필요한 공백이 제거된 URL을 출력합니다. 그런 다음 이 Liquid를 배경 이미지 URL 필드에 붙여넣어 사용자마다 다른 이미지를 동적으로 표시할 수 있습니다.

##### 예시 {#example}

{% raw %}
```liquid
{% capture image_url %}
{% if {{custom_attribute.${membership_tier}}} == 'gold' %}
https://example.com/images/gold-background.png
{% elsif {{custom_attribute.${membership_tier}}} == 'silver' %}
https://example.com/images/silver-background.png
{% else %}
https://example.com/images/default-background.png
{% endif %}
{% endcapture %}
{{ image_url | strip }}
```
{% endraw %}

### Liquid 추가 {#add-liquid}

![Liquid 개인화를 추가하는 아이콘.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

인앱 메시지에 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 추가하려면, 편집기 도구 모음에서 <i class="fa-solid fa-circle-plus"></i> **개인화 추가**를 선택합니다. 여기에서 기본 속성, 기기 속성, 커스텀 속성 등 다양한 개인화 유형을 추가할 수 있습니다.

다음으로, 생성된 Liquid 스니펫을 메시지에 삽입합니다. 인앱 메시지를 디자인하고 구축한 후, **미리보기 및 테스트**로 이동하여 메시지를 미리 봅니다.

### AI 카피라이터 사용 {#using-the-ai-copywriter}

인앱 메시지에서 텍스트 블록이 선택된 상태에서, 블록 도구 모음의 <i class="fa-solid fa-wand-magic-sparkles" title="AI 카피라이터"></i> **AI 카피라이터**를 선택하여 [AI 기반 카피라이팅 어시스턴트]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)를 실행합니다. AI 카피라이팅 어시스턴트는 간략한 제품 이름이나 설명을 OpenAI의 GPT3 카피 생성 도구에 전달하여 메시징에 사용할 사람과 유사한 마케팅 카피를 생성합니다.

{% alert tip %}
블록 내의 텍스트를 강조 표시한 후 아이콘을 클릭하면 몇 번의 클릭을 절약할 수 있습니다. 강조 표시된 텍스트가 도구에 추가되고, 카피가 즉시 생성됩니다.
{% endalert %}

![AI 카피라이터의 GIF.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### 스타일을 기본값으로 재설정 {#resetting-styles-to-default}

기본 스타일에서 변경한 속성은 주황색 점으로 표시됩니다. 특정 속성을 기본 스타일로 재설정하려면, 해당 필드 위에 마우스를 올리고 **기본값으로 재설정**을 선택합니다.

![텍스트 크기를 기본 크기로 재설정하는 주황색 점.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

속성 패널 이름 옆의 <i class="fas fa-paintbrush" title="스타일 복사 또는 붙여넣기 버튼"></i>을 선택하고 **기본 스타일로 재설정**을 선택하여 선택한 요소의 모든 스타일을 재설정할 수도 있습니다.

### 스타일 복사 및 붙여넣기 {#copying-and-pasting-styles}

요소의 스타일을 변경한 후, 해당 스타일을 다른 요소에 복사하여 붙여넣을 수 있습니다. 스타일을 붙여넣을 때, 해당 요소에 관련된 속성만 적용됩니다.

![스타일 복사 옵션이 있는 드롭다운 메뉴.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. 요소가 선택된 상태에서, 속성 패널 이름 옆의 <i class="fas fa-paintbrush" title="스타일 복사 또는 붙여넣기"></i> **스타일 복사 또는 붙여넣기**를 선택합니다(예: 버튼이 선택된 경우, "버튼 속성" 옆).
2. **스타일 복사**를 클릭하고 복사한 스타일을 적용할 요소를 선택합니다.
3. <i class="fas fa-paintbrush" title="스타일 복사 또는 붙여넣기"></i> **스타일 복사 또는 붙여넣기**를 다시 선택하고 **스타일 붙여넣기**를 선택합니다.

#### 키보드 단축키 {#keyboard-shortcuts}

키보드 단축키를 사용하여 스타일을 복사하고 붙여넣을 수도 있습니다:

| 동작 | Mac | Windows |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| 스타일 복사 | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| 스타일 붙여넣기 | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="키보드 단축키" }