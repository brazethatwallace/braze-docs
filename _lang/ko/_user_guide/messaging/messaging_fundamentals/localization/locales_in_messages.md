---
nav_title: 다국어 메시지
article_title: 다국어 메시지
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "이 문서에서는 메시지에서 로캘을 사용하는 방법에 대한 단계를 제공합니다."
---

# 다국어 메시지 {#multi-language-messages}

> 워크스페이스에 로캘을 추가한 후, 단일 푸시, 이메일, 배너, 인앱 메시지 또는 콘텐츠 블록 내에서 다양한 언어로 사용자를 타겟팅할 수 있습니다.

## 필수 조건 {#prerequisites}

다국어 메시지 설정 및 사용에 대한 선택적 개요를 보려면 다음 동영상을 시청하세요.

{% multi_lang_include video.html id="whfstwrel5" source="wistia" %}

{% tabs %}
{% tab 다국어 로캘 %}

{% multi_lang_include locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab 메시지 유형 %}

| 기능 | 필수 사용자 권한 |
| --- | --- |
| 메시지&nbsp;유형 | Campaigns 및 Canvases에 로캘과 번역을 추가하려면 다음 권한이 필요합니다:<br><br> <ul><li>Campaigns 편집</li><li>Canvases 편집</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites"}

{% endtab %}
{% tab 템플릿 %}

| 기능 | 필수 사용자 권한 |
| --- | --- |
| 템플릿 | 로캘과 번역을 추가하려는 템플릿 유형에 대해 다음 권한이 필요합니다:<br><br> <ul><li>이메일 템플릿 편집</li><li>IAM 템플릿 편집</li><li>콘텐츠 블록 템플릿 편집</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% endtab %}
{% endtabs %}

## 로캘 사용 {#use-locales}

### 1단계: 로캘 설정 {#step-1-set-up-locales}

메시지에 번역을 추가하려면 먼저 [지원하려는 로캘을 생성]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/)해야 합니다. 로캘은 메시징에 사용할 수 있는 언어(및 선택적으로 지역) 변형을 정의합니다.

### 2단계: 번역할 콘텐츠 표시 {#step-2-mark-content-for-translation}

번역하려는 텍스트를 Liquid 번역 태그 {% raw %}`{% translation your_id_here %}` 및 `{% endtranslation %}`{% endraw %}로 감싸고 태그 ID를 할당합니다. 번역 태그 ID는 메시지 내에서 고유해야 합니다. {% raw %}`{% translation header %}`{% endraw %}와 같이 텍스트를 명확하게 설명하는 의미론적 ID 이름을 사용하는 것이 좋습니다.

번역용으로 표시된 메시지 예시: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
번역하려는 텍스트를 강조 표시하고 키보드 단축키 **Cmd + Alt + L**(macOS) 또는 **Ctrl + Alt + L**(Windows)을 사용하여 번역 태그로 감쌀 수 있습니다.<br><br> 이 단축키는 이메일 및 Content Blocks용 드래그 앤 드롭 에디터를 제외한 다국어 메시징을 지원하는 모든 채널에서 작동합니다. 해당 에디터에서는 왼쪽 사이드바의 **개인화 추가** 버튼을 사용하여 번역 태그를 추가하세요.
{% endalert %}

#### URL 현지화 {#localize-urls}

콘텐츠를 번역할 때 URL은 링크가 깨지지 않도록 특별한 처리가 필요합니다.

##### 표준(정적) URL {#standard-static-urls}

정적 URL은 에디터에서 수동으로 입력합니다(예: `https://example.com`). 다음 사항도 권장합니다:

| 권장 사항 | 이유 |
| --- | --- |
| 프로토콜(`https://`)은 번역 태그 밖에 유지하세요. 도메인과 경로만 감싸세요(예: `example.com/en`). | 번역자가 실수로 특수 문자를 변경하거나 제거하여 링크가 깨질 수 있습니다. |
| 쿼리 매개변수(예: `?utm_source=promo`)를 번역 태그 안에 포함하지 마세요. | 번역자가 실수로 특수 문자를 변경하거나 제거하여 링크가 깨질 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard (static) URLs" }

두 가지 권장 사항을 모두 따르는 표준 URL은 다음과 같습니다:

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### Liquid 생성 URL {#liquid-generated-urls}

URL이 Liquid로 생성되는 경우(예: {% raw %}`{% landing_page_url %}`{% endraw %}), 다음 사항을 권장합니다:

| 권장 사항 | 이유 |
| --- | --- |
| Liquid 생성 URL은 현지화가 필요한 경우에만 번역 태그로 감싸세요. | Liquid 구문이 올바르게 렌더링되려면 신중하게 보존해야 합니다. |
| 쿼리 매개변수(예: `?utm_source=promo`)를 번역 태그 안에 포함하지 마세요. | 번역자가 실수로 특수 문자를 변경하거나 제거하여 링크가 깨질 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid-generated URLs" }

두 가지 권장 사항을 모두 따르는 Liquid 생성 URL은 다음과 같습니다:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
[이메일 링크 추적](#email-link-tracking)(링크 별칭 지정 또는 링크 템플릿)을 사용하는 경우, URL이 번역 태그로 감싸져 있을 때 추가 구성이 필요합니다.
{% endalert %}

#### HTML 속성 및 구조 {#html-attributes-and-structure}

사람이 읽을 수 있는 텍스트만 번역 태그로 감싸세요. HTML 속성(`class`, `style`, `id` 등)이나 기타 구조적 코드를 감싸지 마세요. HTML 속성은 레이아웃, 스타일링 및 기능을 제어합니다. 번역 태그로 감싸면 메시지의 현지화된 버전에서 서식이나 스타일이 깨질 수 있습니다.

올바르게 감싸진 텍스트:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details 잘못 감싸진 텍스트 %}

이 텍스트는 **잘못** 감싸져 있습니다:

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### 3단계: 메시지에 로캘 추가 {#step-3-add-locales-to-your-message}

메시지에 번역 태그를 추가한 후, 에디터에서 **Manage languages**를 선택하고(이메일 및 Content Blocks용 드래그 앤 드롭 에디터에서는 **Languages**) 번역을 추가할 로캘을 하나 이상 선택합니다.

![기본 로캘 또는 커스텀 속성을 선택할 수 있는 옵션이 있는 로캘 추가 드롭다운.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### 번역이 포함된 Content Blocks {#content-blocks-containing-translation}

메시지에 이미 번역이 저장된 Content Blocks가 포함되어 있는 경우, 해당 번역을 다시 업로드할 필요가 없습니다. 저장된 번역은 Content Block이 메시지에 추가될 때 자동으로 적용됩니다.

**Manage languages** 모달에서 저장된 번역이 있는 Content Blocks가 지원하는 로캘과 함께 목록에 표시됩니다. 이를 통해 새 번역을 추가하기 전에 메시지의 어떤 부분이 이미 현지화되었는지 확인할 수 있습니다.

![저장된 번역이 있는 Content Blocks 목록이 표시된 Manage languages 섹션.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
각 Content Block에 메시지에 추가된 모든 로캘에 대한 번역이 포함되어 있는지 확인하세요. Content Block에 추가한 로캘 중 하나에 대한 번역이 누락된 경우, 해당 로캘의 사용자에게는 원래 언어로 표시됩니다.
{% endalert %}

### 4단계: 번역 추가 {#step-4-add-translations}

로캘을 선택한 후, 다음 방법 중 하나를 사용하여 메시지에 번역을 추가합니다:

![CSV로 번역을 업로드하거나 번역 파트너에 연결하는 옵션이 있는 번역 추가 탭.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab CSV 템플릿 업로드 %}

**Download template**을 선택하여 선택한 번역 ID와 로캘의 매트릭스가 포함된 CSV를 다운로드합니다. 각 로캘에 대한 번역을 입력합니다. 완성된 파일을 업로드하면 번역이 메시지에 적용됩니다.

{% alert important %}
영어가 아닌 문자의 표시 문제를 방지하려면 번역 CSV에 Excel을 사용하지 마세요.
{% endalert %}

![제목, 오퍼 텍스트, 오퍼 금액 및 CTA에 대한 번역 태그가 있는 CSV.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab 번역 API 사용 %}

파트너 번역 API를 사용하여 Campaigns 및 Canvases에서 번역을 관리하고 업데이트합니다. 이는 현지화를 위해 외부 시스템을 사용하거나 번역 파트너에 직접 연결하려는 경우에 유용합니다.

Canvases에서 번역 엔드포인트를 사용하려면 다음 매개변수를 포함하세요:
  - `workflow_id`
  - `step_id`
  - `message_variation_id`

{% alert note %}
Canvas가 시작된 후에 생성된 캔버스 단계에서 번역 API를 사용하는 경우, API에 전달하는 `message_variation_id`는 비어 있거나 공백이 됩니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 5단계: 번역 미리보기 {#step-5-preview-translations}

메시지를 미리보려면 **Preview as User** 드롭다운에서 **Multi-Language User** 옵션을 선택합니다. 이를 통해 다양한 로캘 정의 간에 전환하여 메시지의 모든 번역을 미리볼 수 있습니다.

![로캘 미리보기]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## 번역 관리 {#manage-translations}

### 캔버스 단계 또는 Campaign 복제와 번역 {#duplicate-canvas-steps-or-campaigns-and-translations}

캔버스 단계, Campaign 또는 배리언트를 복제하면 번역이 포함됩니다. 이는 워크스페이스 간 복사 시에도 마찬가지이며, 대상 워크스페이스에 로캘이 정의되어 있어야 합니다. Canvas 또는 Campaign을 수정할 때 번역을 검토하고 적절히 업데이트하세요.

### Content Blocks에 번역 저장 {#save-translations-in-content-blocks}

Content Blocks는 메시지와 동일한 방식으로 다국어를 지원합니다. Content Blocks를 생성하거나 편집할 때 콘텐츠에 번역 태그를 지정하고, 로캘을 추가하고, CSV 또는 [번역 API]({{site.baseurl}}/api/endpoints/translations/)를 사용하여 번역을 업로드할 수 있습니다.

저장된 번역은 Content Block과 연결된 상태로 유지됩니다. 블록이 메시지에 추가되면 해당 번역이 자동으로 포함됩니다.

### 오른쪽에서 왼쪽으로 쓰는 메시지 {#right-to-left-messages}

오른쪽에서 왼쪽으로 쓰는 언어(아랍어 등)의 번역 파일을 작성할 때, 올바른 서식이 적용되도록 번역을 `span`으로 감싸세요:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### 이메일 링크 추적 {#email-link-tracking}

이메일 Campaign에서 Braze는 각 URL에 추적 정보(쿼리 매개변수)를 추가하여 링크를 추적합니다. 이 동작은 [링크 별칭 지정]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing/) 및 [링크 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template/) 모두를 지원합니다.

URL이 번역 태그로 감싸져 있으면 Braze가 추적 정보를 어디에 추가해야 하는지 결정하지 못할 수 있습니다. 이를 올바르게 작동시키려면 URL 끝에 추적이 추가되어야 할 위치를 나타내는 특수 문자를 포함해야 합니다.

URL은 두 가지 특수 문자를 사용하여 이를 제어합니다:
  - `?`는 아직 추적이 없는 URL에 추적을 추가합니다.
  - `&`는 URL에 이미 `?`가 있는 경우 추가 추적을 추가합니다. URL에는 `?`가 하나만 포함될 수 있습니다.

| URL | `?`&nbsp;포함 여부 | 설명 | 예시 |
| --- | --- | --- | --- |
| 표준 URL | 아니요 | URL에 아직 `?`가 포함되어 있지 않은 경우 닫는 번역 태그 뒤에 `?`를 추가합니다. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| 표준 URL | 예 | URL에 이미 `?`가 포함되어 있는 경우 URL 끝(닫는 번역 태그 뒤)에 `&`를 사용합니다. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Liquid 생성 | 아니요 | 생성된 URL에 아직 `?`가 포함되어 있지 않은 경우 닫는 번역 태그 뒤에 `?`를 사용합니다. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Liquid 생성 | 예 | 생성된 URL에 이미 `?`가 포함되어 있는 경우 닫는 번역 태그 뒤에 `&`를 사용합니다. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Email link tracking" }

### 언어 설정 및 접근성 {#language-settings-and-accessibility}

WCAG 컨텍스트, 채널 및 에디터 동작(랜딩 페이지 포함), 메시지 수준 **Accessibility** 설정에 대해서는 [접근성]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/)의 [접근성 언어]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/#accessibility-language)부터 시작하세요.

**다국어 메시지**를 사용할 때, 현지화된 발송이 적절한 언어를 선언하도록 접근성 언어를 각 로캘에 맞추세요.

#### 접근성 언어 구성 {#configuring-the-accessibility-language}

접근성 언어는 두 가지 수준에서 설정할 수 있습니다:

##### 메시지 수준 {#message-level}

메시지 수준에서는 메시지 설정의 **Accessibility** 섹션에서 접근성 언어를 설정합니다. 언어 선택, Liquid 사용 및 채널별 제한 사항에 대해서는 [접근성 언어]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/#accessibility-language)를 참조하세요.

##### 로캘 수준 {#locale-level}

다국어 메시지의 경우, **현지화 설정**에서 각 로캘에 접근성 언어를 설정합니다. **Accessibility** 섹션에서 {% raw %}`{{accessibility_language}}`{% endraw %}를 사용하면 문서 또는 카드 언어가 해당 로캘 값에 매핑됩니다.

새 메시지에서 해당 토큰이 기본적으로 표시되는지 여부는 채널과 에디터에 따라 다릅니다. 예를 들어, 인앱 메시지와 배너는 랜딩 페이지 및 드래그 앤 드롭 이메일과 다르게 동작합니다. 자세한 내용은 [접근성 언어]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/#accessibility-language)를 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

#### 번역 태그의 제한은 무엇인가요? {#what-are-the-limits-for-translation-tags}

번역 태그를 사용할 때 다음 제한이 적용됩니다:

- 각 메시지에는 최대 200개의 번역 태그를 사용할 수 있습니다.
- 각 기본 텍스트(번역 태그 사이의 콘텐츠)는 최대 2,000자까지 가능합니다.
- 로캘당 번역은 최대 409,600바이트(약 409.6&nbsp;KB)까지 가능합니다.

#### 로캘 중 하나에서 번역된 텍스트를 변경할 수 있나요? {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

네. 먼저 CSV에서 편집한 다음 파일을 다시 업로드하여 번역된 텍스트를 변경할 수 있습니다.

### Braze에서 번역을 제공하나요? {#does-braze-provide-translations}

아니요. CSV를 업로드하거나 번역 API를 사용하여 [직접 번역을 제공](#step-4-add-translations)해야 합니다.

### 번역 태그를 중첩할 수 있나요? {#can-i-nest-translation-tags}

아니요.

#### 전체 HTML 메시지를 번역 태그로 감쌀 수 있나요? {#can-i-wrap-entire-html-messages-in-a-translation-tag}

아니요. 모범 사례로, 사람이 읽을 수 있는 텍스트나 현지화가 필요한 콘텐츠만 감싸야 합니다. 이렇게 하면 서식, 링크 또는 기타 비텍스트 요소가 깨지는 것을 방지할 수 있습니다.

또한 정확한 번역을 만들고 성능 또는 크기 제한을 피하기 위해 의미적으로 관련된 작은 텍스트 조각을 감싸는 것을 고려하세요.

#### 로캘 중 하나에서 번역된 텍스트를 변경할 수 있나요?

네. CSV를 사용하는 경우 먼저 파일에서 편집한 다음 다시 업로드하여 번역된 텍스트를 변경합니다. [번역 API]({{site.baseurl}}/api/endpoints/translations/)를 사용하는 경우 업데이트 엔드포인트를 사용하여 변경합니다.

#### Braze에서 어떤 유효성 검사나 추가 확인을 수행하나요? {#what-validations-or-extra-checks-does-braze-do}

| 시나리오 | Braze의 유효성 검사 |
| --- | --- |
| 메시지에 서로 다른 텍스트에 매핑되는 동일한 번역 ID가 두 개 이상 포함되어 있습니다. | 이 번역 파일은 다운로드되지 않습니다. |
| 번역 파일에 하나 이상의 번역 태그 ID가 누락되어 있습니다. | 이 번역 파일은 업로드되지 않습니다. |
| 번역 파일에 메시지에 없는 로캘이 포함되어 있습니다. | 이 번역 파일은 업로드되지 않습니다. |
| 번역 템플릿을 다운로드하기 전에 메시지에 번역 태그를 추가해야 합니다. | 이 번역 파일은 다운로드되지 않습니다. |
| 업로드한 파일에 있는 번역 태그가 메시지에 없습니다. | 추가 번역은 메시지에 저장되지 않습니다. |
| {% raw %}메시지에 하나 이상의 깨진 Liquid 태그가 포함되어 있습니다. 여는 태그에는 `{% translation your_id_here %}`를, 닫는 번역 태그에는 `{% endtranslation %}`를 사용하세요.{% endraw %} | 이 번역 파일은 다운로드되지 않습니다. |
| 번역 파일에 메시지의 내용과 일치하지 않는 기본 텍스트가 포함되어 있습니다. | 번역은 추가되지만 원본 메시지 텍스트는 업데이트되지 않습니다. |
| 메시지의 하나 이상의 로캘이 설정에서 삭제되어 더 이상 존재하지 않습니다. | 이미 추가된 번역은 메시지 내에 계속 존재합니다. 메시지에서 삭제하면 번역이 손실됩니다. |
| 번역 태그에 전체 URL 또는 Liquid 생성 URL이 포함되어 있습니다. | 깨진 링크 또는 링크 추적 문제가 발생할 경우를 대비하여 URL이 포함된 번역 태그가 식별됩니다. |
| 번역 태그에 쿼리 매개변수가 포함되어 있습니다. | 깨진 링크 또는 링크 추적 문제가 발생할 경우를 대비하여 쿼리 매개변수가 포함된 번역 태그가 식별됩니다. |
| 번역 태그에 HTML 속성 또는 구조가 포함되어 있습니다. | 스타일 및 서식 문제가 발생할 경우를 대비하여 HTML 속성 또는 구조가 포함된 번역 태그가 식별됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What validations or extra checks does Braze do?" }