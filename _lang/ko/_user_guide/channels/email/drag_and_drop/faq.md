---
nav_title: FAQ
article_title: 드래그 앤 드롭 편집기 FAQ
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "드래그 앤 드롭 이메일 편집기에 대해 자주 묻는 질문입니다."
tool:
  - Campaigns
  - Canvas



---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 페이지에서는 이메일용 드래그 앤 드롭 편집기와 관련하여 자주 묻는 질문에 대한 답변을 제공합니다.

## 다크 모드에서 이메일이 어떻게 표시되는지 미리 볼 수 있나요? {#can-i-preview-how-my-email-appears-in-dark-mode}

네. 드래그 앤 드롭 편집기의 **미리보기 및 테스트** 섹션으로 이동하여 **다크 모드**를 켜세요. 다양한 사용자 플랫폼에서 이메일을 미리 보고 테스트하는 것도 권장하며, 가능하면 행 배경 이미지에 투명 이미지를 사용하는 것이 좋습니다.

## 다크 모드와 라이트 모드에 맞게 이메일을 어떻게 디자인해야 하나요? {#how-should-i-design-emails-for-dark-mode-and-light-mode}

이메일은 별도의 라이트 및 다크 레이아웃으로 발송할 필요가 없습니다. 이메일 클라이언트와 기기가 자체적으로 다크 테마를 적용할 수 있기 때문입니다. 그러나 외부 컨테이너와 주요 섹션에 명시적인 색상이 설정되어 있지 않으면 색상이 반전되거나 배경이 숨겨질 수 있습니다. 이를 방지하려면 단색 배경색을 설정하여 다크 모드와 라이트 모드 모두에서 메시지가 명확하게 표시되도록 하는 것을 권장합니다.

일부 이메일 클라이언트는 다크 모드에서 배경 이미지를 대체하거나 저대비 텍스트를 반전시키므로, 본문 텍스트가 누락되어 보이거나 클라이언트 간에 다르게 렌더링될 수 있습니다(예: iOS의 Gmail과 Android의 Gmail). 밝은 배경을 위해 배경 이미지에만 의존하지 말고, 외부 컨테이너와 주요 섹션에 `background-color`를 설정하세요.

## 드래그 앤 드롭 이메일 미리보기에서 커스텀 글꼴이 표시되지 않는 이유는 무엇인가요? {#why-doesnt-my-custom-font-appear-in-drag-and-drop-email-preview}

커스텀 글꼴은 메시지의 **텍스트** 블록이 해당 글꼴을 참조할 때 편집기 미리보기에 로드됩니다. **드래그 앤 드롭 이메일 편집기** 설정에서 커스텀 글꼴을 구성한 후에도 미리보기에 대체 글꼴이 표시되는 경우, 해당 글꼴을 사용하는 **텍스트** 블록을 추가하여 편집기가 미리보기용으로 글꼴을 로드하도록 하세요. 글꼴 파일에 교차 출처 리소스 공유(CORS)가 활성화되어 있는지 확인하세요. 발송 전에 **미리보기 및 테스트**와 대상 이메일 클라이언트를 다시 확인하세요. 설정 단계는 [커스텀 글꼴]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings#custom-font)을 참조하세요.

## 다른 애플리케이션에서 복사하여 붙여넣을 때 텍스트 서식을 유지하려면 어떻게 해야 하나요? {#how-can-i-carry-over-text-formatting-when-i-copy-and-paste-from-another-application}

텍스트 편집기와 애플리케이션마다 텍스트 서식을 처리하는 방식이 다르며, 이러한 서식이 보편적으로 인식되지 않을 수 있습니다. Braze 외부에서 서식이 적용된 텍스트를 복사하여 드래그 앤 드롭 편집기에 붙여넣으면 리치 서식이 유지되지 않을 수 있습니다.

리치 서식 없이 텍스트를 붙여넣으려면 다음 방법 중 하나를 사용하세요:
- Mac: <kbd>cmd</kbd>+<kbd>V</kbd> 대신 <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>V</kbd>를 누르세요
- Windows: <kbd>ctrl</kbd>+<kbd>V</kbd> 대신 <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>V</kbd>를 누르세요
- 편집기 내에서 마우스 오른쪽 버튼을 클릭하고 **스타일에 맞게 붙여넣기**를 선택하세요

## 모바일에서 웹 뷰의 패딩을 변경하지 않고 이메일 패딩만 변경하려면 어떻게 해야 하나요? {#how-can-i-change-the-email-padding-on-mobile-without-updating-the-padding-in-the-web-view}

모바일과 웹 뷰의 패딩을 개별적으로 편집할 수 없으므로, 모든 편집 사항은 두 뷰 모두에 반영됩니다. 그러나 HTML 편집기에서 화면 크기에 따라 패딩을 설정하는 CSS 로직을 추가할 수 있습니다. 이 기능은 드래그 앤 드롭 편집기에서는 지원되지 않으므로, HTML 파일을 내보내고 HTML 편집기를 대신 사용할 수 있습니다.

## 데스크톱과 모바일에서 버튼 행을 가로 방향으로 유지하려면 어떻게 최적화할 수 있나요? {#how-can-i-optimize-a-row-of-buttons-to-remain-horizontal-on-desktop-and-mobile}

드래그 앤 드롭 편집기를 사용하여 이메일을 작성할 때, 콜투액션 버튼을 가로 행으로 만들면 모바일에서 버튼이 세로 방향으로 변경될 수 있습니다.

기기 크기에 관계없이 동일한 형식을 유지하려면, 모바일에 최적화된 패딩이 적용된 CTA 버튼이 포함된 별도의 행을 만들고 데스크톱 기기에서는 해당 행을 숨기도록 설정하는 것을 권장합니다. 두 개의 별도 행을 사용하면 데스크톱과 모바일 기기에서 최적의 텍스트 렌더링을 위해 원하는 패딩을 설정할 수 있습니다.

## 드래그 앤 드롭 편집기에서 행 높이를 조정할 수 있나요? {#can-i-adjust-the-row-height-in-the-drag-and-drop-editor}

행 높이는 콘텐츠에 맞게 자동으로 조정됩니다. 대안으로 다음을 권장합니다:
1. 구분선 블록을 추가합니다.
2. 토글을 클릭하여 투명도를 켭니다.
3. 높이를 조정합니다.

## 에디터에서 레이어를 구성할 수 있나요? 배경 이미지를 추가하고, 그 위에 이미지를 겹치고, 그 위에 텍스트 레이어를 추가할 수 있나요? {#is-it-possible-to-build-layers-in-the-editor-can-i-add-a-background-image-layer-on-an-image-and-add-a-text-layer-over-that}

드래그 앤 드롭 에디터는 현재 두 개의 레이어를 지원합니다. 행 배경 이미지를 설정하고 배경 색상을 커스터마이즈할 수 있습니다.

## Campaign 또는 Canvas에서 드래그 앤 드롭 이메일을 작성한 후 템플릿으로 저장할 수 있나요? {#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

아니요. Campaign 또는 Canvas에서 작성한 드래그 앤 드롭 이메일을 **Templates** > **Email Templates**에서 드래그 앤 드롭 **이메일 템플릿**으로 저장할 수 없습니다. **Templates** > **Email Templates**에서 레이아웃을 다시 만들거나, 다음에는 저장된 템플릿에서 시작하세요. 자세한 내용은 [이메일 템플릿 만들기]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)를 참조하세요.

재사용 가능한 HTML 템플릿이 필요한 경우, 드래그 앤 드롭 본문을 편집하는 동안 **Download file**을 선택하고, ZIP에서 HTML을 열어 HTML 코드 편집기를 사용하여 [HTML 이메일 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)에 마크업을 붙여넣으세요. 이후 Liquid, 링크, 호스팅된 에셋을 다시 확인하세요.

템플릿이 어디에 있는지에 대한 자세한 내용은 [템플릿 및 미디어]({{site.baseurl}}/user_guide/messaging/templates)를 참조하세요.

## 드래그 앤 드롭 편집기에서 버튼의 채우기 색상을 변경할 수 없는 이유는 무엇인가요? {#why-cant-i-change-a-buttons-fill-color-in-the-drag-and-drop-editor}

페이지 수준 스타일이 메시지 수준 스타일을 재정의할 수 있습니다. 버튼이나 블록에서 **채우기**를 업데이트해도 아무 변화가 없다면 다음을 시도해 보세요:
1. [이메일 글로벌 스타일 설정]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings)을 열고 충돌하는 페이지 스타일에서 **기본값으로 재설정**을 선택하여 메시지 수준 색상이 적용되도록 합니다.
2. 블록에서 색상을 다시 설정합니다.

## 드래그 앤 드롭 편집기에 이메일 첨부 파일을 추가할 수 있나요? {#can-i-add-email-attachments-to-the-drag-and-drop-editor}

네. **발송 설정** > **고급**으로 이동하여 이메일 메시지에 첨부 파일을 추가할 수 있습니다.

## 드래그 앤 드롭 이메일의 원본 HTML을 어떻게 다운로드하나요? {#how-do-i-download-the-raw-html-for-a-drag-and-drop-email}

드래그 앤 드롭 편집기에는 이메일을 ZIP 파일 내 HTML 파일로 내보낼 수 있는 **Download file** 옵션이 포함되어 있습니다.

1. Campaign 또는 Canvas를 열고 이메일 메시지를 편집합니다.
2. **Edit email body**를 선택하여 드래그 앤 드롭 편집기를 엽니다.
3. **Download file**을 선택합니다.
4. 압축 파일을 풀어 생성된 HTML에 접근합니다.

{% alert tip %}
Windows에서는 ZIP 파일을 압축 해제하기 전에 영구적인 위치(예: 다운로드 폴더)로 이동하세요. 임시 폴더에서 압축을 해제하면 해당 폴더가 삭제된 후 HTML 파일에 접근하지 못할 수 있습니다.
{% endalert %}

해당 HTML을 [HTML 블록]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#content) 또는 HTML 편집기에 붙여넣어 세부적인 편집이 필요할 때 사용할 수 있습니다(예: [특정 링크에 대한 클릭 추적 끄기]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)).

## 드래그 앤 드롭 레이아웃이 깨지는 이유는 무엇인가요? {#why-is-my-drag-and-drop-layout-breaking}

레이아웃 문제는 에디터가 생성하는 마크업과 충돌하는 **커스텀 HTML 또는 CSS**로 인해 발생하는 경우가 많습니다. 다음 단계를 시도해 보세요:

1. 커스텀 HTML 블록을 제거하거나 분리하여 문제가 사라지는지 확인하세요.
2. **드래그 앤 드롭 이메일 에디터** 설정에서 모든 클라이언트에서 로드되지 않을 수 있는 커스텀 글꼴이 있는지 확인하세요.
3. **행 속성**에서 열 패딩과 너비를 검토하세요.
4. 커스텀 HTML을 추가할 때는 테이블 기반 레이아웃, 유동적 이미지, 이메일 너비에 맞는 전체 테이블 너비를 사용하세요. 고정 픽셀 이미지나 비테이블 구조는 Outlook 및 기타 클라이언트에서 깨지는 경우가 많습니다.

## Content Blocks이 이메일 미리보기에서 렌더링되지 않는 이유는 무엇인가요? {#why-doesnt-my-content-block-render-in-email-preview}

Content Blocks이 이메일 미리보기에서 렌더링되지 않는 경우, 닫히지 않은 앵커 태그가 있는지 확인하세요. 연결된 콘텐츠 URL의 경우, `replace` 필터를 사용하여 이중 인코딩된 앰퍼샌드(`&amp;amp;`)를 단일 인코딩된 앰퍼샌드(`&amp;`)로 변환하세요. Content Blocks 중첩은 두 단계까지로 제한하세요.

## 드래그 앤 드롭 Content Blocks이 커스텀 코드 블록 안에서 모바일 스타일링을 잃는 이유는 무엇인가요? {#why-does-a-drag-and-drop-content-block-lose-mobile-styling-inside-a-custom-code-block}

드래그 앤 드롭 **Content Blocks**을 **커스텀 코드**(HTML) 블록 안에 배치하면, Content Blocks의 모바일 전용 스타일링과 정렬이 발송된 메시지에 적용되지 않을 수 있습니다. Content Blocks과 템플릿 모두 드래그 앤 드롭 에디터를 사용하는 경우, Content Blocks을 커스텀 코드 안에 중첩하는 대신 별도의 행으로 추가하세요.

여러 Content Blocks을 쌓을 때는 하나의 행에 여러 블록을 배치하는 대신 각 블록마다 별도의 행을 사용하세요.

## 드래그 앤 드롭 편집기가 정렬 설정을 무시하는 이유는 무엇인가요? {#why-is-the-drag-and-drop-editor-ignoring-alignment-settings}

드래그 앤 드롭 편집기가 정렬 설정을 무시하는 경우, 커스텀 CSS 또는 HTML 블록을 제거하고, 커스텀 글꼴을 제거하고, CSS 충돌을 확인하고, 행 블록 복제를 피하세요. 문제가 지속되면 Braze 지원팀에 문의하세요.

## 선택한 16진수 색상 코드가 이메일의 글꼴과 일치하지 않는 이유는 무엇인가요? {#why-does-my-chosen-hex-color-code-not-match-the-font-in-my-email}

Content Blocks를 사용하는 경우, 해당 블록에 자체 글꼴 색상 설정이 있을 수 있습니다. Content Blocks 내부의 텍스트 블록을 선택하고 로컬 **Font color** 재정의를 해제하여 글로벌 또는 단락 스타일링의 16진수 색상이 적용될 수 있도록 하세요.