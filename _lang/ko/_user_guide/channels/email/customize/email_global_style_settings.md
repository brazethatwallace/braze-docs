---
nav_title: "이메일 글로벌 스타일 설정"
article_title: "이메일 글로벌 스타일 설정"
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "이 참조 문서에서는 드래그 앤 드롭 편집기에서 Campaigns과 Canvases의 글로벌 이메일 스타일 설정을 구성하는 방법을 다룹니다."
tool:
  - Campaigns
  - Canvas
---

# 이메일 글로벌 스타일 설정 {#email-global-style-settings}

> 글로벌 스타일 설정을 사용하면 이메일 Campaigns과 Canvases의 외관을 개인화할 수 있습니다. 드래그 앤 드롭 편집기에 기본 테마를 추가하고 커스텀할 수 있습니다. 여기에는 이메일 제목, 텍스트, 버튼 등의 스타일 편집이 포함됩니다. 이러한 설정을 조합하면 이메일 메시징 전반에 걸쳐 일관된 외관을 만들 수 있습니다.

글로벌 스타일 설정을 편집하려면 **설정** > **이메일 환경설정** > **드래그 앤 드롭 이메일 환경설정**으로 이동합니다. 드래그 앤 드롭 이메일 편집기에서 스타일을 편집한 후 **저장**을 선택합니다. 이메일 Campaigns과 Canvases를 더 커스텀하려면 [편집기 블록(이메일)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)을 활용하는 방법을 확인하세요.

![드래그 앤 드롭 이메일 편집기 설정 탭의 이메일 글로벌 스타일 설정 섹션.]({% image_buster /assets/img_archive/dnd_global_style_settings.png %})

{% alert note %}
글로벌 스타일 설정에 대한 업데이트는 이후 생성되는 모든 이메일 Campaigns과 Canvases에 적용됩니다.
{% endalert %}

## 기본 스타일링 {#basic-styling}

**기본 스타일링**에서는 이메일 Campaign과 Canvases의 기본 이메일 및 콘텐츠 배경색을 설정할 수 있습니다. 또한 기본 글꼴을 선택하고, 커스텀 글꼴을 추가하며, 링크 색상을 편집할 수도 있습니다.

![이메일 및 콘텐츠 배경색, 기본 글꼴 이름, 기본 링크 색상을 편집하는 옵션이 포함된 기본 스타일링 옵션.]({% image_buster /assets/img_archive/dnd_basic_styling.png %})

## 커스텀 글꼴 {#custom-font}

커스텀 글꼴을 사용하면 다양한 이메일 플랫폼에서 브랜드 일관성을 유지하기 위해 웹 글꼴을 수동으로 추가할 수 있습니다. 각 스타일링 섹션마다 하나의 커스텀 글꼴을 추가할 수 있습니다.

{% alert note %}
CSS의 글꼴 굵기(font-weight) 설정은 무시됩니다. 대신 메시지를 작성할 때 미리 설정된 굵기 중 하나를 선택하세요.
{% endalert %}

### 요구 사항 {#requirements}

커스텀 글꼴을 추가하기 전에 커스텀 글꼴 파일이 다음 요구 사항을 충족하는지 확인하세요:

- 커스텀 글꼴 파일을 제공하는 서버에서 CORS가 활성화되어 있어야 합니다. 일반적으로 IT 팀에서 관리합니다.
  - 커스텀 글꼴 파일에는 다음 헤더가 있어야 합니다: `Access-Control-Allow-Origin: *`
- 파일 URL은 CSS 파일을 가리켜야 합니다(WOFF 또는 OTF가 아님).
- 커스텀 글꼴 이름은 CSS 파일의 글꼴 페이스 이름과 일치해야 합니다.

{% alert important %}
커스텀 글꼴 공급자가 수신자의 개인정보를 수집할 수 있습니다. 사용하기 전에 글꼴 공급자의 정책을 검토해야 합니다.
{% endalert %}

### 커스텀 글꼴 추가하기 {#adding-a-custom-font}

커스텀 글꼴을 추가하려면 다음을 수행하세요:

1. **Basic Styling**의 **Default Font Name** 섹션에서 **Add a custom font**를 선택합니다.
2. **Font Name** 필드에 커스텀 글꼴 소스 파일에 표시된 것과 동일한 글꼴 이름을 입력합니다. 이름의 대소문자와 공백이 올바른지 확인하세요.
3. **Font URL** 필드에 해당 URL을 입력합니다.
4. 미리보기에서 커스텀 글꼴이 표시되는지 확인합니다.
5. **Save**를 선택하여 커스텀 글꼴을 기본 이메일 글꼴로 사용합니다.

{% alert important %}
Gmail은 커스텀 글꼴을 지원하지 않으므로 커스텀 글꼴이 기본 시스템 글꼴로 표시될 수 있습니다. 다른 이메일 플랫폼의 경우 이메일 메시징을 발송하기 전에 커스텀 글꼴이 올바르게 표시되는지 확인하세요.
{% endalert %}

이메일 Campaigns에서 다른 커스텀 글꼴을 사용하려면 커스텀 글꼴이 포함된 [이메일 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) 또는 [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)를 만들 수 있습니다. 예를 들어, 세일 테마에 맞춘 축제 분위기의 커스텀 글꼴로 디자인된 특정 이메일 템플릿을 만들 수 있습니다. 선택한 글꼴이 웹에서 안전하고 이메일 플랫폼에서 지원되는지 반드시 확인하세요.

### 대체 글꼴 {#fallback-font}

대체 글꼴은 기본 글꼴 선택이 받은편지함 공급자나 운영 체제에서 지원되지 않을 때 제목, 헤더, 본문 텍스트에 사용됩니다. 기본적으로 Braze는 글로벌 스타일 설정이 저장될 때 Arial을 대체 글꼴로 자동 설정합니다. 기본 글꼴 패밀리에 세리프 또는 산세리프를 옵션으로 추가할 수도 있습니다.

![대체 글꼴로 "Arial"이 설정되고 글꼴 패밀리로 "Sans-serif"가 선택된 예시입니다.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

최대 17개의 대체 글꼴을 추가할 수 있습니다. 처음 선택한 대체 글꼴이 먼저 시도됩니다. 대체 글꼴은 새로 생성된 템플릿, 이메일 Campaigns 및 Canvas 구성 요소에만 적용됩니다. 대체 글꼴이 지정되기 전에 생성된 메시지에는 대체 글꼴이 자동으로 설정되지 않습니다. 브랜딩 전반의 일관성을 유지하기 위해 이메일 메시징과 유사한 대체 글꼴을 선택하는 것을 강력히 권장합니다.

## 제목 스타일링 {#title-styling}

여기에서 글꼴 크기, 글꼴 색상, 텍스트 정렬을 편집하여 이메일 제목의 스타일을 조정할 수 있습니다.

![가운데 정렬된 기본 헤더와 보조 헤더에 대한 제목 스타일링 설정입니다.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

선택적으로 드래그 앤 드롭 편집기 테마의 기본값 스타일을 재정의할 수 있습니다. **기본 스타일 재정의**를 선택하여 원하는 제목 스타일링을 적용합니다. 여기에는 다른 글꼴 및 링크 색상 설정이 포함될 수 있습니다.

## 단락 스타일 지정 {#paragraph-styling}

기본 단락 스타일을 설정하려면 **Paragraph Styling**으로 이동하여 **Font Size**를 입력하고 **Font Color**를 선택하여 글꼴 색상을 선택합니다. **Padding Top**, **Padding Right**, **Padding Bottom**, **Padding Left** 값을 편집하여 본문 텍스트의 블록 스타일을 조정할 수도 있습니다. 이 설정은 단락 블록을 둘러싼 네 방향의 간격에 적용됩니다.

![14pt 글꼴로 설정된 Paragraph Styling 설정.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## 리스트 스타일링 {#list-styling}

메시징에 리스트를 추가할 때 **리스트 스타일링** 섹션을 사용하면 리스트 스타일의 일관성을 유지할 수 있습니다. 여기에는 다음과 같은 세부 사항이 포함됩니다:

- 글꼴 크기
- 글꼴 색상
- 글꼴 두께
- 줄 높이
- 정렬
- 텍스트 방향
- 자간
- 리스트 항목 간격
- 리스트 항목 들여쓰기
- 리스트 유형
- 리스트 스타일 유형

**리스트 유형**을 번호 매기기 또는 글머리 기호로 설정할 수 있습니다. **리스트 스타일 유형**은 리스트 스타일에 대한 추가적인 커스텀 옵션을 제공합니다. 예를 들어 리스트 유형을 항상 글머리 기호로 설정하고 각 글머리 기호를 사각형으로 지정할 수 있습니다.

![글머리 기호 리스트의 리스트 스타일링 설정.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## 버튼 스타일링 {#button-styling}

**버튼 스타일링** 섹션에서 버튼의 다음 기본 스타일을 편집할 수 있습니다:
- 배경 색상
- 글꼴 크기
- 글꼴 색상
- 테두리 반경
- 테두리 색상
- 테두리 두께
- 버튼 패딩

![파란색 배경의 직사각형 버튼에 대한 버튼 스타일링 설정.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

다른 모든 스타일링 섹션과 마찬가지로, **상단 패딩**, **오른쪽 패딩**, **하단 패딩**, **왼쪽 패딩** 값을 편집하여 블록 스타일링을 조정할 수 있습니다.

## 이메일 템플릿 너비 {#email-template-width}

이메일 템플릿 너비를 사용하면 이메일 Campaigns 전반에서 일관성을 유지하도록 너비를 조정하고 설정할 수 있습니다.

![이메일 템플릿 너비가 600px로 설정된 화면.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## 콘텐츠 블록 너비 {#content-block-width}

이 설정은 이후 생성되는 모든 Content Blocks에 사전 구성됩니다. 기존 Content Blocks는 업데이트되지 않습니다. 모든 Content Blocks를 100%로 설정하여 콘텐츠 블록이 삽입된 위치의 너비에 맞추거나, 특정 픽셀 값을 정의할 수 있습니다.

콘텐츠 블록 너비를 이메일 템플릿 너비에 맞추는 것을 권장합니다.

![콘텐츠 블록 너비가 600px로 설정된 화면]({% image_buster /assets/img_archive/dnd_content_block_width_update.png %})