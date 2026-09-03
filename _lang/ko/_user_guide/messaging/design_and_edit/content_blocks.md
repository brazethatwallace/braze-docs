---
nav_title: 콘텐츠 블록
article_title: 콘텐츠 블록
alias: "/dnd/content_blocks/"
page_order: 4
description: "Braze Campaigns와 Canvases에서 재사용 가능한 콘텐츠 블록을 생성, 사용 및 관리하는 방법을 알아보세요."
page_type: reference
tool:
  - Templates
  - Media

---

# 콘텐츠 블록 {#content-blocks}

> 콘텐츠 블록을 사용하면 재사용 가능한 크로스채널 콘텐츠를 하나의 중앙 위치에서 관리할 수 있습니다. Campaigns 전반에 걸쳐 일관된 디자인을 만들거나, 다양한 채널을 통해 동일한 오퍼 코드를 배포하거나, 대규모로 일관된 메시징을 위한 사전 정의된 자산을 구축하는 데 활용하세요. [API를 사용]({{site.baseurl}}/api/endpoints/templates)하여 콘텐츠 블록을 생성하고 관리할 수도 있습니다.

## 콘텐츠 블록 만들기 {#create-a-content-block}

콘텐츠 블록에는 드래그 앤 드롭과 HTML 두 가지 유형이 있습니다. 각 유형은 해당 편집기에 대응합니다.

{% tabs %}
{% tab 드래그 앤 드롭 %}

{% multi_lang_include messaging/create_content_block.md location="dnd" %}

{% alert important %}
각 드래그 앤 드롭 콘텐츠 블록은 하나의 행으로 제한됩니다. 그러나 드래그 앤 드롭 편집기 블록을 사용하여 이메일 메시징에 맞게 콘텐츠 블록을 구성하고 커스터마이즈할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include messaging/create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### 콘텐츠 블록 사양 {#content-block-specifications}

| 콘텐츠 블록 속성 | 사양 |
|---|---|
| 이름 | 최대 100자의 필수 필드입니다. 콘텐츠 블록 이름에는 문자(A-Z), 숫자(0-9), 대시(`-`), 밑줄(`_`)만 포함할 수 있습니다. 공백 및 기타 특수 문자는 허용되지 않으며 자동으로 변환됩니다(예: 공백은 밑줄로 대체됨). 콘텐츠 블록이 저장된 후에는 이름을 변경할 수 없으며, 보관된 콘텐츠 블록의 이름도 재사용할 수 없습니다. |
| 설명 | (선택 사항) 최대 250자입니다. 다른 Braze 사용자가 콘텐츠 블록의 용도와 사용 위치를 알 수 있도록 설명합니다. |
| 콘텐츠 크기 | 최대 50KB입니다. |
| 배치 | Content Blocks는 이메일 푸터 내에서 사용할 수 없지만, 이메일에서 사용할 [푸터를 포함하는 콘텐츠 블록을 만들](#email-footers) 수 있습니다. |
| 생성 | HTML 편집기 또는 드래그 앤 드롭 편집기입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="콘텐츠 블록 사양" }

{% alert tip %}
콘텐츠 블록을 만들 때 줄 바꿈을 추가하여 HTML과 Liquid를 시각화하면 도움이 될 수 있습니다. 이러한 줄 바꿈이 발송 시 그대로 남아 있으면 불필요한 공백이 생겨 블록 렌더링에 영향을 줄 수 있습니다. 이를 방지하려면 블록에 **Capture** 태그와 **&#124; strip** 필터를 함께 사용하세요.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Content Blocks 사용하기 {#use-content-blocks}

Content Blocks를 만든 후 편집기 또는 Liquid를 사용하여 메시지에 삽입할 수 있습니다.

### 드래그 앤 드롭 편집기 사용하기 {#using-the-editor}

드래그 앤 드롭 편집기에서 Content Blocks를 추가하려면:

1. 편집기에서 **행** 탭으로 이동하여 **Content Blocks**를 선택합니다.
2. Content Blocks를 이메일 편집기로 드래그 앤 드롭합니다.
3. (선택 사항) 탐색 메뉴에서 버튼을 선택하여 Content Blocks의 너비를 조정합니다. 이메일 글로벌 스타일 설정에서 지정하지 않은 경우 기본값 너비는 100%이며, 그렇지 않으면 글로벌 설정이 적용됩니다. <br><br>![너비를 편집할 수 있는 옵션이 있는 양방향 화살표.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

{% alert note %}
드래그 앤 드롭으로 추가된 Content Blocks는 원본 Content Blocks에 **연결되지 않습니다**. 원본에 대한 변경 사항을 확인하려면 이메일 편집기로 다시 드래그하세요.
{% endalert %}

드래그 앤 드롭 편집기에서 여러 Content Blocks를 단일 행 블록에 추가하면 정렬이 맞지 않을 수 있습니다. 행 수준에서 콘텐츠 정렬을 유지하려면 별도의 행 블록을 사용해 보세요.

### Liquid 사용하기 {#using-liquid}

Liquid를 사용하여 Content Blocks를 삽입하려면:

1. **Content Blocks 세부 정보** 섹션에서 **Content Blocks Liquid 태그**를 복사합니다.
2. Content Blocks Liquid 태그를 메시지에 삽입합니다. Liquid를 입력하기 시작하면 태그가 자동으로 채워질 수도 있습니다.

드래그 앤 드롭 편집기에서는 **개인화** 패널을 통해 Content Blocks를 추가할 수도 있습니다:

1. 이메일 Campaign으로 이동하여 **이메일 본문 편집**을 선택합니다.
2. <i class="fas fa-plus"></i> **개인화**를 클릭합니다.
3. **개인화 유형** 드롭다운에서 **Content Blocks**를 선택합니다.
4. **속성** 필드에서 Content Blocks의 이름을 선택합니다.
5. Liquid 스니펫을 복사하여 텍스트 편집기 블록에 붙여넣습니다. <br>![옵션이 있는 개인화 추가 탭.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

{% alert important %}
Liquid를 통해 삽입된 Content Blocks는 원본 Content Blocks에 **연결되어** 있으며 템플릿에 대한 모든 변경 사항이 반영됩니다.
{% endalert %}

## Content Blocks 미리보기 {#preview-content-blocks}

활성 Campaign 또는 Canvas에 콘텐츠 블록을 추가한 후, Content Blocks 라이브러리에서 해당 콘텐츠 블록 위에 마우스를 올리고 <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 선택하여 미리보기할 수 있습니다.

이 미리보기에는 콘텐츠 블록에 대한 정보가 포함되어 있습니다. 예를 들어 작성자, 태그, 생성일, 마지막 수정일, 설명, 편집기 유형, 포함 횟수 및 세부 정보(해당 콘텐츠 블록을 사용하는 메시지 또는 Content Blocks의 클릭 가능한 목록), 그리고 콘텐츠 블록의 실제 미리보기가 표시됩니다.

{% alert note %}
콘텐츠 블록이 사용되는 위치를 감사할 때는 연결된 각 메시지 또는 단계를 개별적으로 검토하여 상태를 확인하세요.
{% endalert %}

## Content Blocks 중첩 {#nest-content-blocks}

Content Blocks는 중첩할 수 있지만, 한 단계만 가능합니다. Content Block A를 Content Block B에 중첩할 수 있지만, Content Block B를 Content Block C에 다시 중첩할 수는 없습니다.

{% alert warning %}
세 번째 수준의 Content Block 중첩을 방지하는 기능은 없지만, 두 번째 수준을 넘어서는 중첩에서는 콘텐츠가 확장되지 않습니다. 콘텐츠와 Liquid 스니펫이 메시지에서 제거됩니다.
{% endalert %}

중첩된 Content Block 내부의 링크는 상위 메시지의 전체 링크 수에 포함됩니다. 현지화를 위한 국가별 URL과 같이 조건부 링크가 많은 단일 Content Block을 사용하면, 상위 메시지에 많은 수의 링크가 누적되어 Canvas 저장이 느려지거나 저장되지 않을 수 있습니다. 대규모 현지화의 경우, 단일 Content Block의 조건부 링크보다 [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)가 더 적합합니다.

## Content Blocks 업데이트 및 복사 {#update-and-copy-content-blocks}

Content Blocks를 업데이트하면 Liquid를 통해 해당 콘텐츠 블록이 삽입된 모든 메시지에서 업데이트됩니다. 드래그 앤 드롭 편집기의 **행** 아래에 있는 **Content Blocks** 드롭다운을 사용하여 콘텐츠 블록을 가져온 경우에는 모든 메시지에서 업데이트되지 않습니다.

단일 메시지에 대해 콘텐츠 블록을 업데이트하거나 다른 메시지에서 사용할 사본을 만들려면, 원본 메시지의 HTML을 새 메시지로 복사하거나 원본 콘텐츠 블록을 편집(이미 메시지에서 사용된 적이 있어야 함)한 후 저장할 수 있습니다. 새 콘텐츠 블록으로 저장할 수 있는 프롬프트가 표시됩니다.

콘텐츠 블록을 편집한 후 **Content Block 시작**을 선택하여 업데이트된 콘텐츠 블록을 저장하고 시작할 수 있습니다. 또는 **더 보기** > **복제**를 선택하여 콘텐츠 블록의 사본을 만들 수 있습니다.

![뉴스레터에 오신 것을 환영합니다라고 표시된 콘텐츠 블록]({% image_buster /assets/img/copy-content-block.png %})

## 콘텐츠 블록에서 이메일 바닥글 사용 {#email-footers}

콘텐츠 블록은 이메일 바닥글 내에서 사용할 수 없지만, 이메일에서 사용할 바닥글 콘텐츠를 포함하는 콘텐츠 블록을 생성할 수 있습니다. 방법은 다음과 같습니다:

1. **설정** > **이메일 환경설정** > **커스텀 바닥글**로 이동하여 바닥글을 생성합니다.
2. **콘텐츠 블록 라이브러리**에서 콘텐츠 블록에 바닥글을 추가합니다.
3. 해당 콘텐츠 블록을 이메일 템플릿 또는 메시지에 추가합니다.

## 알아두어야 할 사항 {#things-to-know}

- 드래그 앤 드롭 이메일에서 HTML Content Blocks를 사용하거나 HTML 이메일에서 드래그 앤 드롭 Content Blocks를 사용하면 예기치 않은 렌더링 문제가 발생할 수 있습니다. 이는 드래그 앤 드롭 편집기가 콘텐츠를 동적으로 렌더링하는 HTML과 CSS를 생성하는 반면, HTML 편집기는 보다 정적이기 때문입니다.
- Liquid를 사용하여 드래그 앤 드롭 콘텐츠 블록을 삽입하면 Braze는 해당 블록의 HTML `<head>`에 있는 스타일을 포함하지 않습니다. 모바일 전용 CSS와 같은 응답형 스타일이 예상대로 렌더링되지 않을 수 있습니다. 블록이 응답형 CSS에 의존하는 경우, 해당 CSS를 콘텐츠 블록을 포함하는 메시지 또는 템플릿에 추가하세요.
- Canvas 진입 속성은 Canvases에서만 지원됩니다. Canvas 진입 속성이 포함된 콘텐츠 블록을 Campaign에서 참조하면 값이 채워지지 않습니다.
- 여러 Content Blocks가 포함된 메시지가 예상대로 렌더링되지 않는 경우(예: Liquid 태그나 HTML이 처리되지 않고 텍스트로 표시되는 경우), Content Blocks 중 하나에 닫히지 않은 태그 또는 기타 오류가 원인인 경우가 많습니다. 원인을 파악하려면 다음을 수행하세요.
    1. 영향을 받는 메시지에서 Content Blocks를 하나씩 제거합니다.
    2. 각 제거 후 메시지가 올바르게 렌더링되는지 확인합니다.
    3. 문제가 사라지기 직전에 제거한 콘텐츠 블록이 문제를 일으키는 블록입니다.
- `<code>` HTML 태그는 콘텐츠 블록에 설정된 글꼴 스타일과 관계없이 대부분의 이메일 클라이언트에서 기본적으로 고정폭 글꼴로 렌더링됩니다. 고정폭 글꼴 표시를 원하지 않는 한 텍스트를 `<code>` 태그로 감싸지 마세요.
- Liquid를 사용하여 커스텀 HTML 이메일 템플릿에 콘텐츠 블록을 삽입하면, 상위 템플릿의 CSS 규칙이 콘텐츠 블록 내부에 정의된 스타일을 재정의할 수 있습니다. 자세한 내용은 [커스텀 HTML 템플릿의 Content Blocks]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline#content-blocks-in-custom-html-templates)를 참조하세요.

## Content Blocks 보관하기 {#archive-content-blocks}

![설정 드롭다운 메뉴가 펼쳐져 보관, 복제, 워크스페이스로 복사의 세 가지 옵션이 표시됩니다.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Content Blocks 사용을 마치면 **템플릿** 페이지에서 보관할 수 있습니다. 보관된 Content Blocks는 읽기 전용이므로, 편집하려면 먼저 보관을 해제해야 합니다. 메시지에서 사용 중인 Content Blocks는 보관할 수 없습니다.

### 모범 사례 {#best-practices}

- 블록이 소수의 이메일에서만 사용되는 경우, 오래된 블록을 보관하고 보관되지 않은 최신 블록으로 라이브 메시지를 업데이트하는 것을 권장합니다.
- 블록에 오타만 있거나 사소한 변경이 필요한 경우, 블록을 보관하지 않는 것을 권장합니다. 대신 블록을 업데이트하고 바로 발송하세요!
- 블록이 이 목록의 첫 번째 제안으로 합리적으로 관리할 수 있는 것보다 더 많은 메시지에서 사용되는 경우, 블록에서 모든 콘텐츠를 제거하는 것을 권장합니다. 이렇게 하면 오래된 정보가 메시지에 포함되는 것을 방지할 수 있습니다.
- 실수로 Content Blocks를 보관한 경우, 보관을 해제할 수 있습니다.

![저장된 Content Blocks 패널에서 "Test_32"의 설정 드롭다운 메뉴가 펼쳐져 보관 해제, 복제, 워크스페이스로 복사의 세 가지 옵션이 표시됩니다.]({% image_buster /assets/img/unarchive-content-block.png %})