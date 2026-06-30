---
nav_title: "이메일용 AMP"
article_title: "이메일용 AMP"
alias: /amphtml/
page_order: 11
description: "이 참조 문서에서는 이메일용 AMP의 개요와 일반적인 사용 사례를 설명합니다."
channel:
  - email

---

# 이메일용 AMP {#amp-for-email}

> [이메일용 AMP](https://amp.dev/about/email)를 사용하면 이메일에 인터랙티브 요소를 추가하고 고객과의 커뮤니케이션을 한 단계 끌어올릴 수 있으며, 사용자의 받은편지함에 직접 풍부한 경험을 전달할 수 있습니다. AMP는 다양한 구성요소를 활용하여 설문조사, 피드백 설문지, 투표 Campaign, 리뷰, 구독 센터 등 매력적인 이메일 콘텐츠를 구축할 수 있게 해줍니다. 이러한 도구는 참여도와 리텐션을 높일 수 있는 기회를 제공합니다.

## 요구 사항 {#requirements}

Braze는 사용자가 Google에 등록하거나 필요한 보안 요구 사항을 충족하는 것에 대해 책임지지 않습니다. 이메일용 AMP는 SparkPost 및 SendGrid에서만 사용할 수 있습니다.

| 요구 사항   | 설명 |
| --------------| ----------- |
| 이메일용 AMP 활성화 | AMP는 모든 사용자가 사용할 수 있습니다. |
| Gmail 계정 인에이블먼트 | [Gmail 계정 활성화](#enabling-gmail-account)를 참조하세요. |
| Google 발신자 인증 | Gmail은 DKIM, SPF, DMARC를 사용하여 AMP 이메일의 [발신자를 인증](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication)합니다. 계정에 이를 설정해야 합니다. <br><br>- [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Domain-based Message Authentication, Reporting, and Conformance](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| AMP 이메일 요소 | 매력적인 AMP 이메일에는 다양한 구성요소의 전략적 사용이 포함됩니다. 아래 [구성요소](#components) 섹션의 필수 요소 탭을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

### 지원되는 이메일 클라이언트 {#supported-email-clients}

사용자에게 AMP 이메일을 보내려면 먼저 이메일 클라이언트에 등록해야 합니다. 등록 과정에서는 승인을 받기 위해 테스트 AMP HTML 이메일을 보내야 합니다. 승인 시간은 클라이언트마다 다릅니다. 자세한 내용은 등록 링크를 참조하세요.

| 클라이언트 | 등록 링크 |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported email clients" }

지원되는 이메일 클라이언트의 전체 목록은 [AMP 설명서](https://amp.dev/support/faq/email-support)를 참조하세요.

### Gmail 계정 활성화 {#enabling-gmail-account}

Gmail 설정으로 이동하여 **General** 탭에서 **Enable dynamic email**을 선택합니다.

![Gmail 설정에서 'Enable dynamic email' 체크박스가 선택된 예시.]({% image_buster /assets/img/dynamic-content.png %})

## API 사용법 {#api-usage}

API를 통해서도 이메일용 AMP를 사용할 수 있습니다. Braze [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging)를 사용하여 이메일을 보내는 경우, 아래와 같이 `amp_body`를 오브젝트 사양으로 추가하세요.

### 이메일 오브젝트 사양 {#email-object-specification}

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <user@example.com>"),
  "reply_to": (optional, valid email address in the format "user@example.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## AMP 이메일 만들기 {#create-your-amp-email}

먼저 [구성요소](#components)를 사용하여 AMP 이메일을 작성합니다. 그런 다음 [Braze API](#api-usage)를 사용하여 메시지를 보내되, AMP HTML에 `amp_body`를 포함해야 합니다.

AMP HTML 외에도 일반 HTML `body` 버전이 필요하며, AMP 이메일의 `plaintext_body` 버전도 함께 제공하는 것을 권장합니다. 모든 AMP 이메일은 멀티파트로 발송되므로, Braze는 HTML, 일반 텍스트, AMP HTML을 지원하는 이메일을 발송합니다. 이메일용 AMP를 아직 지원하지 않는 공급자를 통해 이메일이 발송되는 경우에도 사용자와 기기에 따라 적절한 버전으로 자동 전환되므로 유용합니다.

{% alert note %}
AMP 이메일을 작성할 때는 AMP 에디터에서 작업하고 있는지 확인하세요. AMP 코드는 HTML 에디터에 추가하면 안 됩니다.
{% endalert %}

다음 추가 리소스를 참조하세요:

- [AMP 튜토리얼](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- 최종 결과물이 어떻게 보여야 하는지 확인할 수 있는 [샘플 코드](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73).
- [AMP 이메일 구성요소 라이브러리](https://amp.dev/documentation/components/?format=email/)

### 구성요소 {#components}

AMP 요소를 작성할 때는 엔지니어링 팀과 확인하고 디자인 리소스와 요소를 포함하여 추가적인 완성도를 높이는 것을 권장합니다.

{% tabs %}
  {% tab 필수 요소 %}

이러한 각 요소는 AMP 이메일 본문에 필수입니다.

| 구성요소 | 설명 | 예시 |
|---------|--------------|---------|
| 식별 <br><br> `⚡4email` 또는 `amp4email`| 이메일을 AMP HTML 이메일로 식별합니다. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| AMP 런타임 로드 <br><br> `<script>` | JavaScript를 사용하여 이메일에서 AMP를 실행할 수 있게 합니다. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS 보일러플레이트 | AMP가 로드될 때까지 콘텐츠를 숨깁니다. <br> AMP 이메일을 지원하는 이메일 공급자는 검증된 AMP 스크립트만 클라이언트에서 실행되도록 보안 검사를 시행합니다. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Components" }

  {% endtab %}
  {% tab 동적 %}

이러한 구성요소를 사용하여 이메일에 동적 레이아웃과 동작을 만들 수 있습니다.

| 구성요소 | 설명 | 필수 스크립트 |
|---------|--------------|---------|
| [아코디언](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| 사용자가 콘텐츠 개요를 보고 원하는 섹션으로 이동할 수 있게 합니다. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [양식](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| AMP 문서에서 입력 필드를 제출하는 양식을 만듭니다. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Components" }

{% alert note %}
사용자 인증이 필요한 구성요소는 [Google 액세스 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) 또는 [프록시 어설션 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)을 사용해야 합니다.
{% endalert %}
  {% endtab %}
  {% tab 크리에이티브 %}

  AMP의 구성요소를 활용하여 오디언스에 맞게 이메일을 꾸며보세요.

| 구성요소 | 설명 | 필수 스크립트 |
|---------|--------------|---------|
| [애니메이션 이미지](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| 런타임을 통해 관리되는 애니메이션 이미지(보통 GIF)를 표시합니다. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [캐러셀](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| 유사한 여러 콘텐츠를 가로 축을 따라 표시합니다. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [이미지](https://amp.dev/documentation/components/amp-img?format=email) | HTML `img` 태그를 대체하는 런타임 관리 요소입니다. <br>  이미지에 [라이트박스를 만들](https://amp.dev/documentation/components/amp-image-lightbox?format=email) 수도 있습니다. | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Components" }

{% alert note %}
사용자 인증이 필요한 구성요소는 [Google 액세스 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) 또는 [프록시 어설션 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)을 사용해야 합니다.
{% endalert %}

  {% endtab %}
  {% tab 기타 %}

| 구성요소 | 설명 |
|---------|--------------|
| [데이터 바인딩 및 표현식](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| 데이터 바인딩과 JavaScript와 유사한 표현식을 통해 AMP 페이지에 커스텀 상태 기반 인터랙티비티를 추가합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Components" }

{% alert note %}
사용자 인증이 필요한 구성요소는 [Google 액세스 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) 또는 [프록시 어설션 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)을 사용해야 합니다.
{% endalert %}

{% endtab %}
{% endtabs %}

AMP 구성요소의 전체 목록은 [AMP 설명서](https://amp.dev/documentation/components/?format=email)를 확인하세요.

### 활용 사례 {#use-cases}

{% tabs local %}
{% tab 인터랙티브 설문조사 %}

`<amp-form>` 구성요소를 사용하면 이메일 받은편지함을 떠나지 않고도 완료할 수 있는 인터랙티브 설문조사를 만들 수 있습니다. `<amp-form>`을 사용하여 설문조사 응답을 제출하고, 백엔드에서 이 집계 데이터를 제공하도록 할 수 있습니다.

몇 가지 예시:
* 컨퍼런스 설문조사 이메일
* 피드에서 항목을 동적으로 업데이트
* 문서 북마크 이메일

이 구성요소를 사용하면 사용자가 필드 값을 제출하거나 지울 수 있습니다. 또한 이메일 설정 방식에 따라 설문조사 제출이 성공했는지 여부와 같은 추가 프롬프트를 사용자에게 제공하거나, 설문조사 결과(예: 투표 Campaign)를 보여주는 사용자 응답을 렌더링할 수 있습니다.

{% endtab %}
{% tab 접을 수 있는 콘텐츠 %}

`<amp-accordion>` 구성요소를 사용하여 콘텐츠 섹션을 확장할 수 있습니다. 이 구성요소를 사용하면 접을 수 있고 펼칠 수 있는 콘텐츠 섹션을 표시하여 독자가 콘텐츠 개요를 한눈에 보고 원하는 섹션으로 이동할 수 있습니다.

긴 교육 문서나 개인화된 추천을 자주 보내는 경우, 독자가 콘텐츠 개요를 한눈에 보고 원하는 섹션이나 특정 제품 추천으로 이동하여 자세한 내용을 확인할 수 있습니다. 이는 특히 섹션의 몇 문장만으로도 스크롤이 필요한 모바일 사용자에게 유용합니다.
{% endtab %}
{% tab 이미지가 많은 이메일 %}

리테일 브랜드처럼 전문적인 사진이 많은 이메일을 자주 보내는 경우, `<amp-image-lightbox>` 구성요소를 사용하여 사용자가 관심 있는 이미지와 상호작용할 수 있게 할 수 있습니다. 사용자가 이미지를 클릭하면 이 구성요소가 메시지 중앙에 이미지를 표시하여 라이트박스 효과를 만듭니다.

또한 `<amp-image-lightbox>` 구성요소를 사용하면 사용자가 상세한 이미지 설명을 볼 수 있습니다. 하나 이상의 이미지에 동일한 구성요소를 사용할 수 있습니다. 예를 들어, 이메일에 여러 이미지가 포함된 경우 사용자가 어떤 이미지를 클릭하든 해당 이미지가 라이트박스에 표시됩니다.

{% endtab %}
{% tab 텍스트 중심 이메일 %}

주로 텍스트에 의존하는 이메일의 경우, `<amp-fit-text>` 구성요소를 사용하여 지정된 영역 내에서 텍스트의 크기와 맞춤을 관리할 수 있습니다.

예시:

- 영역에 맞게 텍스트 크기 조정
- 최대 글꼴 크기를 설정하여 영역에 맞게 텍스트 크기 조정
- 콘텐츠가 영역을 초과할 때 텍스트 잘라내기

{% endtab %}
{% endtabs %}

### amp-mustache 사용하기 {#use-amp-mustache}

Liquid와 마찬가지로 AMP도 고급 사용 사례를 위한 스크립팅 언어를 지원합니다. 이 구성요소는 [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email)라고 합니다. Mustache 마크업 언어를 포함할 때는 Liquid의 [`raw`](https://shopify.github.io/liquid/tags/raw/) 태그로 감싸야 합니다. Liquid와 Mustache는 구문 스타일을 공유한다는 점에 유의하세요.

콘텐츠를 `raw` 태그로 감싸면 Braze 처리 엔진이 `raw` 태그 사이의 콘텐츠를 무시하고 팀에서 필요한 Mustache 변수를 그대로 발송합니다.

## 측정기준 및 분석 {#metrics-and-analytics}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="측정기준 및 분석">
  <caption>측정기준 및 분석</caption>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>세부 정보</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total Opens</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Opens' %} AMP 이메일의 경우, HTML 및 일반 텍스트 버전의 총 열람 수입니다.</td>
        </tr>
        <tr>
            <td class="no-split">Total Clicks</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %} AMP 이메일의 경우, HTML 및 일반 텍스트 버전의 총 클릭 수입니다.</td>
        </tr>
        <tr>
            <td class="no-split">AMP Opens</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">AMP Clicks</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## 테스트 및 문제 해결 {#test-and-troubleshoot}


AMP 이메일을 보내기 전에 다음을 권장합니다:

- 이 [Gmail 가이드라인](https://developers.google.com/gmail/ampemail/testing-dynamic-email)에 따라 테스트합니다.
- [Gmail AMP for Email Playground](https://amp.gmail.dev/playground/)를 사용하여 AMP 마크업을 검증합니다.
  - AMP 이메일에 Liquid 태그가 사용된 경우, Gmail AMP for Email Playground에 붙여넣기 전에 정적 플레이스홀더 값으로 대체하세요. 렌더링되지 않은 Liquid 태그는 유효성 검사 오류를 발생시킵니다.

AMP 이메일이 Gmail 계정에 전달되려면 다음 조건을 충족해야 합니다:

- 이메일용 AMP 보안 요구 사항을 충족해야 합니다.
- AMP MIME 파트에 유효한 AMP 문서가 포함되어야 합니다.
- 이메일에 HTML MIME 파트보다 AMP MIME 파트가 먼저 포함되어야 합니다.
- AMP MIME 파트는 100&nbsp;KB 미만이어야 합니다.

총 클릭 수와 고유 클릭 수에는 AMP 메시지에서 발생한 클릭이 포함되지 않습니다(HTML 및 일반 텍스트만 해당). AMP 관련 클릭은 *amp_click* 측정기준에 귀속됩니다.

이러한 조건 중 어느 것도 오류의 원인이 아닌 경우 [고객지원]({{site.baseurl}}/support_contact)에 문의하세요.

### Gmail 받은편지함에서 AMP 이메일을 렌더링하도록 설정하기 {#configure-gmail-inbox-to-render-amp-emails}

다음 단계를 수행하여 테스트 목적으로 Gmail 받은편지함에서 AMP 이메일을 렌더링하도록 설정할 수 있습니다:

1. Gmail에서 받은편지함 오른쪽 상단의 **Settings**을 선택합니다.
2. **See all settings**를 선택합니다.
3. **General** 탭에서 **Dynamic email** 섹션으로 이동하여 **Enable dynamic email** 체크박스가 선택되어 있는지 확인합니다.
4. 다음으로 **Developer Settings**를 선택하고 **Always allow dynamic emails from this sender:** 체크박스를 선택합니다.
5. 테스트 메시지의 발신자 주소와 동일한 도메인을 입력합니다.
6. 변경 사항을 저장합니다.

이제 Gmail 계정으로 테스트 이메일을 보내면 AMP 이메일이 Gmail에서 렌더링됩니다.

### 자주 묻는 질문 {#frequently-asked-questions}

#### AMP 이메일로 세그먼트를 나눠야 하나요? {#should-i-segment-with-amp-emails}

다양한 유형의 사용자에게 보내기 위해 세그먼트를 나누지 않는 것을 권장합니다. AMP 메시지는 멀티파트로 발송되어 원본 이메일에 여러 버전이 포함되기 때문입니다. 사용자가 AMP 버전을 볼 수 없는 경우 HTML로 자동 전환됩니다.