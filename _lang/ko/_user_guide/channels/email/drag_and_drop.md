---
nav_title: 드래그 앤 드롭 편집기
article_title: 드래그 앤 드롭으로 이메일 만들기
alias: /dnd/
page_order: 1
description: "이 문서에서는 이메일 메시지용 드래그 앤 드롭 편집기를 설정하고 올바르게 사용하는 방법을 다룹니다."
channel: email
tool:
- Campaigns
- Canvas
---

# 드래그 앤 드롭으로 이메일 만들기 {#create-an-email-with-drag-and-drop}

> 드래그 앤 드롭 편집기를 사용하면 HTML을 사용하지 않고도 Campaigns 또는 Canvases를 위한 완전히 커스텀되고 개인화된 이메일 메시지를 만들 수 있습니다.

## 편집기 소개 {#about-the-editor}

드래그 앤 드롭 편집기는 [콘텐츠](#content)와 [행](#rows)을 두 가지 핵심 구성요소로 사용하여 HTML을 추가로 사용하지 않고도 워크플로를 간소화합니다.

<table aria-label="편집기 소개" style="width: 100%; table-layout: fixed;">
    <caption>콘텐츠 및 행 편집기 구성요소</caption>
    <thead>
    <tr>
        <th style="width: 50%;">콘텐츠</th>
        <th style="width: 50%;">행</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="이메일 레이아웃을 위한 다양한 구조 조합이 포함된 '행' 탭." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="기본 블록, 미디어, 고급이 포함된 '콘텐츠' 탭." style="max-width: 100%; height: auto;">
        </td>
    </tr>
    </tbody>
</table>
{: .reset-td-br-1 aria-label="편집기 소개" }

### 콘텐츠 {#content}

**콘텐츠**에는 메시지에서 사용할 수 있는 다양한 유형의 콘텐츠를 나타내는 일련의 타일이 포함되어 있습니다. 이들은 기본, 미디어, 고급의 세 가지 카테고리로 구성됩니다.

{% tabs %}
{% tab 기본 %}

기본 블록은 이메일의 기초입니다. 이 블록을 사용하면 이메일 본문에 다음 요소를 추가할 수 있습니다:

- 제목
- 단락
- 목록
- 버튼
- 구분선
- 스페이서

{% endtab %}
{% tab 미디어 %}

미디어 블록을 사용하면 이미지, 동영상, 소셜 미디어 아이콘 및 링크, 커스텀 아이콘 등 다양한 시각적 콘텐츠를 추가할 수 있습니다.

{% endtab %}
{% tab 고급 %}

드래그 앤 드롭 편집기가 이러한 블록으로 워크플로를 간소화하지만, 고급 블록을 사용하여 HTML을 삽입하거나 이메일 본문에 메뉴를 추가할 수도 있습니다. 직접 작성한 HTML을 사용하면 메시지 렌더링에 영향을 줄 수 있다는 점에 유의하세요.

{% endtab %}
{% endtabs %}

### 행 {#rows}

**행**은 열을 사용하여 메시지 섹션의 수평 구성을 정의하는 구조적 단위입니다. 빈 행 또는 [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)를 사용할 수 있습니다. 두 개 이상의 열을 사용하면 서로 다른 콘텐츠 요소를 나란히 배치할 수 있습니다. 이렇게 하면 시작할 때 선택한 템플릿에 관계없이 메시지에 필요한 모든 구조적 요소를 추가할 수 있습니다.

#### 텍스트 블록 내 이미지 중첩 {#nesting-images-inside-text-blocks}

드래그 앤 드롭 편집기에서는 단락이나 다른 텍스트 블록 안에 이미지를 중첩할 수 없습니다. 텍스트 레이아웃 옆이나 안에 이미지를 배치하려면 **행**에서 열을 사용하세요. 예를 들어, 데스크탑에서는 다중 열 행에 해당 행의 **모바일에서 숨기기**를 설정하고, 별도의 모바일 전용 행(**데스크탑에서 숨기기** 및 필요에 따라 **모바일에서 쌓지 않기** 설정)을 사용하여 작은 화면에서 이미지와 텍스트가 깔끔하게 정렬되도록 합니다.

#### 카드 스타일 {#cards-style}

**카드 스타일**은 열 사이에 간격을 추가하고 모서리를 둥글게 만들 수 있는 행 속성입니다. 카드 스타일 서식을 사용하면 새로운 제품 기능, 후기, 특별 혜택, 뉴스 업데이트 등 가장 중요한 콘텐츠를 강조하는 데 도움이 되는 시각적으로 매력적인 레이아웃을 만들 수 있습니다.

## 드래그 앤 드롭 편집기 사용하기 {#using-the-drag-and-drop-editor}

이메일 메시지를 Campaign으로 보낼지 Canvas로 보낼지 확실하지 않으신가요? Campaigns는 단일 타겟 메시징 캠페인에 적합하고, Canvases는 다단계 사용자 여정에 적합합니다.

{% alert note %}
드래그 앤 드롭 이메일을 Campaign 또는 Canvas에서 직접 **템플릿** > **이메일 템플릿**에 이메일 템플릿으로 저장할 수 없습니다. 먼저 **템플릿**에서 작성하거나, [Campaign 또는 Canvas에서 작성한 드래그 앤 드롭 이메일을 템플릿으로 저장할 수 있나요?]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas)를 참조하여 드래그 앤 드롭 템플릿을 다시 만들거나 **Download file**로 HTML을 내보내세요.
{% endalert %}

메시지를 작성할 위치를 선택한 후, 드래그 앤 드롭 이메일을 만드는 단계를 살펴보겠습니다.

### 1단계: 템플릿 선택 {#step-1-select-your-template}

편집 환경으로 드래그 앤 드롭 편집기를 선택한 후 다음 중 하나를 선택할 수 있습니다:

- 빈 템플릿으로 시작하기.
- 미리 디자인된 Braze 드래그 앤 드롭 이메일 템플릿 사용하기.
- 저장된 드래그 앤 드롭 이메일 템플릿 사용하기.

{% alert note %}
기존 커스텀 HTML 템플릿이나 서드파티에서 만든 템플릿을 사용하려면 **Content** > **Email**로 이동하여 편집 환경으로 **Drag-And-Drop Editor**를 선택하여 템플릿을 다시 만들어야 합니다.
{% endalert %}

**템플릿** 섹션에서 모든 템플릿에 접근할 수도 있습니다.

템플릿을 선택하면 **Email Variants** 아래에 발송 정보와 이메일 본문이 포함된 이메일 개요가 표시됩니다.

그런 다음 **Edit Email Body**를 선택하여 드래그 앤 드롭 편집기에서 이메일 구조를 디자인하기 시작합니다.

![예시 이메일 본문이 포함된 'Email Variants' 섹션.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### 2단계: 이메일 작성 {#step-2-build-your-email}

드래그 앤 드롭 편집 환경은 **Sending Settings**, **Content**, **Preview & Test**의 세 섹션으로 나뉩니다. 이메일 본문을 작성하는 핵심은 **Content** 섹션에서 이루어집니다. 이메일을 작성하기 전에 이메일 작성 경험을 안내하는 핵심 구성요소를 이해하는 것이 중요합니다. 복습이 필요하다면 [편집기 소개](#about-the-editor)를 참조하세요.

준비가 되면 드래그 앤 드롭 콘텐츠 블록을 사용하여 이메일을 작성합니다.

1. **Rows** 패널을 선택합니다. 행 구성을 메인 편집기로 드래그 앤 드롭합니다. 이렇게 하면 이메일 콘텐츠의 레이아웃이 매핑됩니다.
- 새 구성은 기존 섹션의 상단 또는 하단으로 드래그해야 합니다.
- 행 구성을 선택하면 행 배경색, 이미지, 커스텀 열 크기를 추가로 커스터마이징할 수 있는 **Row Properties** 설정이 나타납니다.
2. **Content** 패널을 선택합니다. 원하는 콘텐츠 타일을 행 구성요소로 드래그 앤 드롭합니다.
- **Content** 타일을 메인 편집기로 직접 드래그할 수도 있습니다. 이렇게 하면 타일에 대한 행이 생성됩니다.
- 타일을 선택하고 **Content Properties** 및 **Block Options**에서 필드를 조정하여 타일을 더 세밀하게 조정할 수 있습니다. 여기에는 자간, 패딩, 줄 높이 등의 편집이 포함됩니다.

드래그 앤 드롭 이메일을 추가로 커스터마이징하는 다른 방법은 [기타 커스터마이징](#other-customizations)을 확인하세요.

이메일을 작성하면서 데스크탑과 모바일 보기를 전환하여 사용자 그룹에게 이메일 메시지가 어떻게 보일지 미리 볼 수 있습니다. 이를 통해 콘텐츠가 응답형인지 확인하고 필요한 조정을 할 수 있습니다.

{% alert tip %}
멋진 카피를 작성하는 데 도움이 필요하신가요? [AI 카피라이팅 어시스턴트]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)를 사용해 보세요. 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있는 사람이 쓴 것 같은 마케팅 카피를 생성합니다.

![드래그 앤 드롭 편집기의 Content 패널에서 Style Settings 옆에 있는 카피라이터 버튼.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### 3단계: 발송 정보 추가 {#step-3-add-your-sending-information}

이메일 메시지 디자인과 작성을 완료한 후에는 **Sending Settings** 섹션에서 발송 정보를 추가할 차례입니다.

1. **Sending Info**에서 **From Display Name + Address**로 이메일을 선택합니다. **Customize From Display Name + Address**를 선택하여 커스터마이징할 수도 있습니다.
2. **Reply-To Address**로 이메일을 선택합니다. **Customize Reply-To Address**를 선택하여 커스터마이징할 수도 있습니다.
3. 다음으로 **BCC Address**로 이메일을 선택하여 이 주소에서 이메일을 볼 수 있도록 합니다.
4. 이메일에 제목란을 추가합니다. 선택적으로 프리헤더와 프리헤더 뒤의 공백도 추가할 수 있습니다.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

오른쪽 패널의 미리보기에 추가한 발송 정보가 표시됩니다. 이 정보는 **설정** > **이메일 환경설정** > **발송 구성**으로 이동하여 업데이트할 수도 있습니다.

#### 이메일 첨부 파일 추가 {#add-email-attachments}

**Sending Settings** > **Advanced**에서 다음 방법으로 이메일 첨부 파일을 추가할 수 있습니다:

{% multi_lang_include email/attachment_upload_options.md %}

고려해야 할 구체적인 모범 사례는 [이메일 가이드라인]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines)을 참조하세요.

#### 이메일 헤더 개인화(고급) {#personalize-your-email-header-advanced}

**Sending Settings**에서 이메일 헤더와 이메일 추가 항목에 대한 개인화를 추가할 수 있으며, 이를 통해 다른 이메일 서비스 공급자에게 추가 데이터를 보낼 수 있습니다. 수신자의 이름을 포함하는 등 이메일 헤더를 개인화하면 이메일이 열릴 가능성을 높이는 데 기여할 수 있습니다.

{% alert note %}
고급 기능은 Campaign 또는 Canvas 작성기에 표시됩니다. 고급 기능에서는 인라인 CSS 설정을 수정하고 헤더 또는 추가 키-값 페어를 입력할 수 있습니다(구성된 경우).
{% endalert %}

### 4단계: 이메일 테스트 {#step-4-test-your-email}

발송 정보를 추가한 후에는 마지막으로 이메일을 테스트할 차례입니다.

{% alert tip %}
편집기에서 보이는 이메일이 미리보기나 테스트 발송과 다르게 보이는 경우, 모든 태그가 닫혀 있는지, 이미지 속성에 값이 있는지, 배경 이미지가 가장자리에서 흐릿하지 않은지 확인하세요.
{% endalert %}

**Preview and Test** 섹션으로 이동합니다. 여기에서 사용자로서 이메일을 미리 보거나 테스트 메시지를 보내는 옵션이 있습니다. 이 섹션에는 다양한 모바일 및 웹 클라이언트에서 이메일이 올바르게 렌더링되었는지 확인할 수 있는 [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)도 포함되어 있습니다.

{% alert tip %}
미리보기 패널의 **Dark Mode Preview** 토글을 사용하여 다크 모드에서 이메일 본문을 확인하고 필요에 따라 이메일을 조정할 수도 있습니다.
{% endalert %}

실제 편집기, Inbox Vision, 실제 테스트 이메일에서 동일한 이메일의 세 가지 다른 버전을 볼 수 있으므로, 모든 플랫폼에서 세부 사항을 일치시키는 것이 중요합니다.

#### 미리보기 및 테스트 발송 {#preview-and-test-send}

**Preview as a User** 탭에서 다음 사용자 유형을 선택하여 메시지를 미리 볼 수 있습니다.

- **Random User:** Braze가 데이터베이스에서 무작위로 사용자를 선택하고 해당 사용자의 속성 또는 이벤트 정보를 기반으로 이메일을 미리 봅니다.
- **Select User:** 이메일 주소 또는 외부 ID를 기반으로 특정 사용자를 선택할 수 있습니다. 해당 사용자의 속성 및 이벤트 정보를 기반으로 이메일이 미리 표시됩니다.
- **Custom User:** 사용자를 커스터마이징할 수 있습니다. Braze가 사용 가능한 모든 속성 및 이벤트에 대한 입력 필드를 제공합니다. 미리보기 이메일에서 보고 싶은 정보를 입력할 수 있습니다.

{% alert note %}
랜덤 사용자는 세분화 기준에 포함될 수도 있고 포함되지 않을 수도 있습니다. 세분화는 이후에 선택되므로 이 시점에서 Braze는 타겟 오디언스를 인식하지 못합니다.
{% endalert %}

**Copy preview link**를 선택하여 랜덤 사용자에게 이메일이 어떻게 보일지 보여주는 공유 가능한 미리보기 링크를 생성하고 복사할 수도 있습니다. 이 링크는 7일 후에 다시 생성해야 합니다.

이메일 템플릿에 대한 편집 사항은 이전에 생성된 링크에 반영되지 않습니다. 편집 사항을 확인하려면 새 링크 미리보기를 생성해야 합니다.

!['Copy preview link' 버튼과 생성된 링크를 복사하는 이메일 미리보기.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Inbox Vision 사용 {#use-inbox-vision}

Inbox Vision을 사용하면 이메일 클라이언트 및 모바일 기기의 관점에서 이메일 캠페인을 볼 수 있습니다. Inbox Vision을 사용하여 이메일 메시지를 테스트하려면 **Preview & Test** 섹션에서 **Inbox Vision**을 선택하고 **Run Inbox Vision**을 선택합니다.

이메일 메시지의 세부 사항을 테스트하고 확인하는 것이 중요합니다. 예를 들어, 이메일 메시징의 배경 이미지는 때때로 이미지 사이에 흰색 선이나 끊김이 나타나거나, Windows Outlook과 같은 클라이언트에서 배경 이미지가 표시되지 않을 수 있습니다. Inbox Vision을 사용하면 클라이언트 간의 이러한 불일치를 식별하는 데 도움이 됩니다. 이 경우 대체 배경색을 설정하여 이미지가 예상대로 렌더링되도록 합니다.

자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=email)를 참조하세요.

드래그 앤 드롭 편집기를 사용하여 이메일 메시지를 디자인하고 만든 후, Campaign 또는 Canvas의 나머지 부분을 계속 [구축]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas)합니다.

{% details 업데이트된 HTML 엔진에 대해 %}
드래그 앤 드롭 편집기에서 HTML을 생성하는 기본 엔진이 최적화 및 업데이트되어 HTML 파일 압축 및 렌더링과 관련된 이점이 있습니다.

평균 내보내기 HTML 데이터 크기가 줄어들어 로딩 및 렌더링이 빨라지고, 모바일 클리핑이 줄어들며, 대역폭 소비가 감소했습니다.

조건부 주석과 CSS 미디어 쿼리의 수를 최소화하는 다음 업데이트를 기반으로 HTML 렌더링이 개선되었습니다. 결과적으로 HTML 파일이 더 작고 효율적으로 코딩됩니다.
- `<div>` 요소 기반 디자인에서 표준 `<table aria-label="Inbox Vision 사용">` 형식 코드베이스로 마이그레이션
  <caption>Inbox Vision 사용</caption>
- [편집기 블록(이메일)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)이 간결하게 재코딩됨
- 최종 HTML 코드가 태그 사이의 공백을 제거하도록 압축됨
- 투명 구분선이 자동으로 콘텐츠 패딩으로 변환됨
{% enddetails %}

## 기타 커스터마이징 {#other-customizations}

드래그 앤 드롭 이메일을 계속 작성하면서 이러한 창의적인 세부 사항의 조합을 사용하여 각 이메일 본문을 추가로 커스터마이징하여 오디언스의 관심과 흥미를 끌 수 있습니다.

{% alert tip %}
[글로벌 스타일 설정]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings)을 사용하여 드래그 앤 드롭 편집기의 커스텀 테마를 만들 수 있습니다.
{% endalert %}

### 자동 너비 이미지 {#auto-width-images}

이메일에 추가된 이미지는 자동으로 **Auto width**로 설정됩니다. 이 설정을 조정하려면 **Auto width**를 끄고 필요에 따라 너비 비율을 조정합니다.

![드래그 앤 드롭 편집기의 Content 탭에 있는 자동 너비 옵션.]({% image_buster /assets/img/dnd/dnd1.png %})

### 색상 레이어링 {#color-layering}

색상 레이어링을 사용하면 이메일 배경, 콘텐츠 영역, 다양한 콘텐츠 구성요소의 색상을 변경할 수 있습니다. 앞에서 뒤로의 색상 순서는 콘텐츠 구성요소 색상, 콘텐츠 영역 배경색, 배경색입니다.

![드래그 앤 드롭 편집기의 색상 레이어링 예시.]({% image_buster /assets/img/dnd/dnd2.png %})

### 콘텐츠 패딩 {#content-padding}

![드래그 앤 드롭 편집기의 Block Options.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

패딩을 조정하려면 **Block Options**으로 스크롤하여 **More Options**를 선택합니다. 패딩을 세밀하게 조정하여 이메일이 딱 맞게 보이도록 할 수 있습니다.

### 콘텐츠 배경 {#content-background}

행 구성에 배경 이미지를 추가하여 이메일 캠페인에 더 많은 디자인과 시각적 콘텐츠를 포함할 수 있습니다.

### 언어 속성 {#language-attribute}

**Settings** 탭으로 이동하여 원하는 언어를 선택하면 언어 속성을 설정할 수 있습니다. 메시지가 동적 언어 값을 가진 사용자를 대상으로 하는 경우 사용자 속성 {%raw%} `{{${language}}}` {%endraw%}를 타겟팅할 수도 있습니다.

![이메일의 'Language' 값 설정.]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### 개인화 {#personalization}

![드래그 앤 드롭 편집기의 개인화 추가 옵션.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

드래그 앤 드롭 이메일 편집기에서 기본 Liquid가 지원됩니다. 이메일에 개인화를 추가하려면:

1. **Content** 섹션에서 **Personalization**을 선택합니다.
2. 개인화 유형을 선택합니다. 여기에는 기본값(표준) 속성, 기기 속성, 커스텀 속성 등이 포함됩니다.
3. 추가할 속성을 검색합니다.
4. 생성된 Liquid 스니펫을 복사하여 이메일 본문에 붙여넣습니다.

이미지 블록 및 버튼 링크 유형 필드에는 Liquid 개인화가 지원되지 않습니다.

#### 동적 이미지 {#dynamic-images}

이미지 소스 속성에 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) 또는 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 포함하여 이메일 메시징에 동적 이미지를 포함할 수 있습니다. 예를 들어, 정적 이미지 대신 {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %}를 이미지 URL로 삽입하여 이미지에 사용자의 이름을 포함할 수 있습니다. 이를 통해 각 사용자에게 이메일을 개인화할 수 있습니다.

{% alert important %}
이미지 URL은 `https://`로 시작해야 합니다. `http://`를 사용하면 앱이 충돌합니다.
{% endalert %}

### 텍스트 방향 {#text-direction}

메시지를 작성할 때 해당 **Text direction** 버튼을 선택하여 왼쪽에서 오른쪽 또는 오른쪽에서 왼쪽으로 텍스트 방향을 전환할 수 있습니다. 아랍어나 히브리어와 같은 언어로 메시지를 작성할 때 이 옵션을 사용할 수 있습니다.

![오른쪽에서 왼쪽 및 왼쪽에서 오른쪽 텍스트 정렬을 전환하는 버튼이 있는 이메일 드래그 앤 드롭 편집기 메뉴.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

오른쪽에서 왼쪽 메시지의 최종 모양은 서비스 공급자가 렌더링하는 방식에 크게 좌우됩니다. 가능한 한 정확하게 표시되는 오른쪽에서 왼쪽 메시지를 작성하는 모범 사례는 [오른쪽에서 왼쪽 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)를 참조하세요.

### HTML

#### 링크에 대한 HTML 속성 {#html-attributes-to-links}

![링크에 대해 'clicktracking' 속성이 꺼진 'Attributes' 섹션.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

드래그 앤 드롭 편집기에서 링크, 버튼, 이미지, 동영상을 사용할 때 **Content** 섹션의 **Attributes**에서 **Add new attribute**를 선택하여 이메일의 HTML 태그에 추가 정보를 첨부할 수 있습니다. 이는 메시지 개인화, 세분화, 스타일링에 특히 유용할 수 있습니다.

일반적인 사용 사례는 Braze를 통해 발송할 때 클릭 추적을 비활성화하기 위해 앵커 태그에 속성을 삽입하는 것입니다.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

또 다른 일반적인 사용 사례는 특정 링크를 유니버설 링크로 표시하는 것입니다. 유니버설 링크는 앱으로 리디렉션하여 사용자에게 통합된 경험을 제공하는 링크입니다.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` ([커스텀 서브 경로](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths)를 구성해야 합니다)

유니버설 링크를 설정하려면 [유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)를 참조하세요.

또는 [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) 또는 [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer#email-deep-linking-and-click-tracking)와 같은 기여도 파트너와 통합하여 유니버설 링크를 관리할 수 있습니다.

마지막으로, 메시지의 접근성을 높이는 데 도움이 되는 사전 정의된 속성을 사용할 수 있습니다. 자세한 내용은 [Braze에서 접근 가능한 메시지 작성]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility) 문서를 참조하세요.

#### 커스텀 head 태그 {#custom-head-tags}

`<head>` 태그를 사용하여 이메일 메시지에 CSS와 메타데이터를 추가할 수 있습니다. 예를 들어, 이 태그를 사용하여 스타일시트나 파비콘을 추가할 수 있습니다. `<head>` 태그에서 Liquid가 지원됩니다.

`<head>` 태그 외부에 추가된 내용은 이메일의 `<body>` 태그 뒤에 추가됩니다. 이는 추가된 콘텐츠가 이메일에 표시된다는 것을 의미합니다.

##### 허용되는 태그 및 태그별 속성 {#allowed-tags-and-attributes-by-tag}

| 태그 이름 | 설명 | 예시 |
| --- | --- | --- |
| `base` | 메시지의 모든 상대 URL에 대한 기본 URL을 지정합니다. | `<base href="https://example.com" target="_blank">` |
| `link`| 메시지와 외부 리소스 간의 관계를 정의합니다. | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | 페이지 설명이나 키워드와 같은 메타데이터를 제공합니다. | `<meta name="description" content="Free Web tutorials">` |
| `style` | 내부 CSS 스타일을 삽입합니다. | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | 브라우저 탭에 표시되는 문서의 제목을 설정합니다. | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="허용되는 태그 및 태그별 속성" }

| 태그 | 속성 | 설명 | 예시 |
| --- | --- | --- | --- |
| `base` | `href` | 상대 URL에 사용할 기본 URL입니다. | ```<base href="https://braze.com">``` |
| `base` | `target`| 모든 하이퍼링크와 양식의 기본 타겟입니다. | ```<base target="_blank">``` |
| `link` | `href` | 외부 리소스의 URL입니다. | ```<link href="style.css">``` |
| `link` | `rel` | 현재 메시지와 연결된 메시지 간의 관계를 정의합니다. | ```<link rel="stylesheet">``` |
| `link` | `type` | 연결된 리소스의 유형입니다. | ```<link type="text/css">``` |
| `link` | `sizes` | 아이콘의 크기를 지정합니다. | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | 스타일이 적용되는 미디어 또는 기기를 지정합니다. | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | 브라우저 탭에 표시되는 문서의 제목을 설정합니다. | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | 브라우저 탭에 표시되는 문서의 제목을 설정합니다. | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | 문자 인코딩을 선언합니다. | ```<meta charset="UTF-8">``` |
| `meta` | `property` | 브라우저 탭에 표시되는 문서의 제목을 설정합니다. | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | 스타일 콘텐츠의 MIME 유형입니다. | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | 스타일이 적용되는 미디어 또는 기기를 지정합니다. | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | 속성 없음 | `title` 태그는 속성을 허용하지 않습니다. | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="허용되는 태그 및 태그별 속성" }

{% alert note %}
링크 이름은 최대 63바이트까지 가능하며, 제한을 초과하면 자동으로 잘립니다.
{% endalert %}