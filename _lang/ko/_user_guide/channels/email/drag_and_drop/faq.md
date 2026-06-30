---
nav_title: FAQ
article_title: 드래그 앤 드롭 편집기 FAQ
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "이 문서에서는 드래그 앤 드롭 편집기와 관련된 다양한 FAQ를 다룹니다."
tool:
  - Campaigns
  - Canvas

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 페이지에서는 이메일용 드래그 앤 드롭 편집기와 관련하여 자주 묻는 질문에 대한 답변을 제공합니다.

## 다크 모드에서 이메일이 어떻게 표시되는지 미리볼 수 있나요? {#can-i-preview-how-my-email-appears-in-dark-mode}

네. 드래그 앤 드롭 편집기의 **미리보기 및 테스트** 섹션으로 이동하여 **다크 모드**를 켜세요. 다양한 사용자 플랫폼에서 이메일을 미리보기하고 테스트하는 것도 권장하며, 가능하면 행 배경 이미지에 투명 이미지를 사용하는 것이 좋습니다.

### 다크 모드와 라이트 모드에 맞게 이메일을 어떻게 디자인해야 하나요? {#how-should-i-design-emails-for-dark-mode-and-light-mode}

이메일을 라이트 모드와 다크 모드 레이아웃으로 별도로 보낼 필요는 없습니다. 이메일 클라이언트와 기기가 자체적으로 다크 테마를 적용할 수 있기 때문입니다. 그러나 외부 컨테이너와 주요 섹션에 명시적인 색상이 설정되지 않은 경우 색상이 반전되거나 배경이 숨겨질 수 있습니다. 이를 방지하려면 단색 배경색을 설정하여 다크 모드와 라이트 모드 모두에서 메시지가 명확하게 표시되도록 하는 것이 좋습니다.

### 웹 뷰의 패딩을 변경하지 않고 모바일에서만 이메일 패딩을 변경하려면 어떻게 해야 하나요? {#how-can-i-change-the-email-padding-on-mobile-without-updating-the-padding-in-the-web-view}

모바일과 웹 뷰의 패딩을 개별적으로 편집할 수 없으므로 모든 편집 내용이 두 뷰 모두에 반영됩니다. 그러나 HTML 편집기에서 화면 크기에 따라 패딩을 설정하는 CSS 로직을 추가할 수 있습니다. 이 기능은 드래그 앤 드롭 편집기에서는 지원되지 않으므로 HTML 파일을 내보내기한 후 HTML 편집기를 사용하세요.

### 데스크탑과 모바일에서 버튼 행이 가로로 유지되도록 최적화하려면 어떻게 해야 하나요? {#how-can-i-optimize-a-row-of-buttons-to-remain-horizontal-on-desktop-and-mobile}

드래그 앤 드롭 편집기를 사용하여 이메일을 작성할 때 콜투액션 버튼을 가로 행으로 만들면 모바일에서 버튼이 세로 방향으로 변경될 수 있습니다.

기기 크기에 관계없이 동일한 형식을 유지하려면 모바일에 최적화된 패딩이 적용된 CTA 버튼이 포함된 별도의 행을 만들고 데스크탑 기기에서는 해당 행을 숨기도록 설정하는 것이 좋습니다. 두 개의 별도 행을 사용하면 데스크탑과 모바일 기기에서 최적의 텍스트 렌더링을 위한 원하는 패딩을 설정할 수 있습니다.

### 드래그 앤 드롭 편집기에서 행 높이를 조정할 수 있나요? {#can-i-adjust-the-row-height-in-the-drag-and-drop-editor}

행 높이는 콘텐츠에 맞게 자동으로 조정됩니다. 대안으로 다음을 권장합니다:
1. 구분선 블록을 추가합니다.
2. 토글을 클릭하여 투명도를 켭니다.
3. 높이를 조정합니다.

### 편집기에서 레이어를 구축할 수 있나요? 배경 이미지를 추가하고, 그 위에 이미지를 겹치고, 그 위에 텍스트 레이어를 추가할 수 있나요? {#is-it-possible-to-build-layers-in-the-editor-can-i-add-a-background-image-layer-on-an-image-and-add-a-text-layer-over-that}

드래그 앤 드롭 편집기는 현재 두 개의 레이어를 지원합니다. 행 배경 이미지를 설정하고 배경색을 커스텀할 수 있습니다.

### Campaign이나 Canvas에서 작성한 드래그 앤 드롭 이메일을 템플릿으로 저장할 수 있나요? {#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

아니요. Campaign이나 Canvas에서 작성한 드래그 앤 드롭 이메일을 **템플릿** > **이메일 템플릿**에서 드래그 앤 드롭 **이메일 템플릿**으로 저장할 수 없습니다. **템플릿** > **이메일 템플릿**에서 레이아웃을 다시 만들거나, 다음에는 저장된 템플릿에서 시작하세요. 자세한 내용은 [이메일 템플릿 만들기]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)를 참조하세요.

재사용 가능한 HTML 템플릿이 필요한 경우, 드래그 앤 드롭 본문을 편집하는 동안 **파일 다운로드**를 선택하고, ZIP에서 HTML을 열어 HTML 코드 편집기를 사용하여 [HTML 이메일 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)에 마크업을 붙여넣으세요. 이후 Liquid, 링크 및 호스팅된 자산을 다시 확인하세요.

템플릿이 어디에 있는지에 대한 자세한 내용은 [템플릿 및 미디어]({{site.baseurl}}/user_guide/messaging/templates)를 참조하세요.

### 드래그 앤 드롭 편집기에서 버튼의 채우기 색상을 변경할 수 없는 이유는 무엇인가요? {#why-cant-i-change-a-buttons-fill-color-in-the-drag-and-drop-editor}

페이지 수준 스타일이 메시지 수준 스타일을 재정의할 수 있습니다. 버튼이나 블록에서 **채우기**를 업데이트해도 아무 변화가 없다면 다음을 시도해 보세요:
1. [이메일 글로벌 스타일 설정]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings)을 열고 충돌하는 페이지 스타일에서 **기본값으로 재설정**을 선택하여 메시지 수준 색상이 적용되도록 합니다.
2. 블록에서 색상을 다시 설정합니다.

### 드래그 앤 드롭 편집기에 이메일 첨부 파일을 추가할 수 있나요? {#can-i-add-email-attachments-to-the-drag-and-drop-editor}

네. **발송 설정** > **고급**으로 이동하여 이메일 메시지에 첨부 파일을 추가할 수 있습니다.

### 드래그 앤 드롭 이메일의 원본 HTML을 다운로드하려면 어떻게 하나요? {#how-do-i-download-the-raw-html-for-a-drag-and-drop-email}

1. Campaign 또는 Canvas를 열고 이메일 메시지를 편집합니다.
2. **이메일 본문 편집**을 선택하여 드래그 앤 드롭 편집기를 엽니다.
3. **파일 다운로드**(편집기 하단)를 선택합니다. 아카이브를 추출하여 생성된 HTML에 접근합니다.

해당 HTML을 [HTML 블록]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#content)이나 HTML 편집기에 붙여넣어 저수준 편집을 수행할 수 있습니다. 예를 들어, [특정 링크에 대한 클릭 추적 끄기]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis) 등이 있습니다.

### 드래그 앤 드롭 레이아웃이 깨지는 이유는 무엇인가요? {#why-is-my-drag-and-drop-layout-breaking}

레이아웃 문제는 편집기가 생성하는 마크업과 충돌하는 **커스텀 HTML 또는 CSS**로 인해 발생하는 경우가 많습니다. 다음 단계를 시도해 보세요:

1. 커스텀 HTML 블록을 제거하거나 분리하여 문제가 사라지는지 확인합니다.
2. **드래그 앤 드롭 이메일 편집기** 설정에서 모든 클라이언트에서 로드되지 않을 수 있는 커스텀 폰트를 확인합니다.
3. **행 속성**에서 열 패딩과 너비를 검토합니다.
4. 커스텀 HTML을 추가할 때는 테이블 기반 레이아웃, 유동적 이미지, 이메일 너비에 맞는 전체 테이블 너비를 사용하세요. 고정 픽셀 이미지나 비테이블 구조는 Outlook 및 기타 클라이언트에서 깨지는 경우가 많습니다.

### 이메일 미리보기에서 콘텐츠 블록이 렌더링되지 않는 이유는 무엇인가요? {#why-doesnt-my-content-block-render-in-email-preview}

콘텐츠 블록이 이메일 미리보기에서 렌더링되지 않는 경우, 닫히지 않은 앵커 태그가 있는지 확인하세요. 연결된 콘텐츠 URL의 경우, `replace` 필터를 사용하여 이중 인코딩된 앰퍼샌드(`&amp;amp;`)를 단일 인코딩된 앰퍼샌드(`&amp;`)로 변환하세요. 콘텐츠 블록 중첩은 두 단계까지로 제한하세요.

### 드래그 앤 드롭 편집기가 정렬 설정을 무시하는 이유는 무엇인가요? {#why-is-the-drag-and-drop-editor-ignoring-alignment-settings}

드래그 앤 드롭 편집기가 정렬 설정을 무시하는 경우, 커스텀 CSS 또는 HTML 블록을 제거하고, 커스텀 폰트를 제거하고, CSS 충돌을 확인하고, 행 블록 복제를 피하세요. 문제가 지속되면 Braze 고객지원에 문의하세요.