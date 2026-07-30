---
nav_title: "이메일 가이드라인"
article_title: "이메일 가이드라인"
page_order: 1
page_type: reference
description: "이 문서에서는 다양한 사용 사례와 주제에 맞는 이메일 Campaign을 구축할 때 참고할 수 있는 일반적인 팁과 요령을 다룹니다."
channel: email

---

# 이메일 가이드라인 {#email-guidelines}

> 이메일 Campaign을 구축할 때는 다양한 사용자와 이메일 서비스 공급자(ESP)에서 이메일 메시징이 어떻게 수신되는지 염두에 두는 것이 중요합니다.

## 일반 사항 {#general}

콘텐츠를 작성할 때 참고할 수 있는 몇 가지 팁을 소개합니다.

- 이메일 서식을 지정할 때는 인라인 스타일 시트를 CSS로 사용하세요.
- 모바일과 데스크톱 버전 모두에 하나의 이메일 템플릿을 사용하려면 너비를 500픽셀 이하로 유지하세요.
- 이미지는 5&nbsp;MB 미만이어야 합니다. 최대 호환성을 위해 PNG, JPEG 또는 GIF 사용을 권장합니다. SVG와 WebP는 많은 주요 이메일 클라이언트에서 아직 지원하지 않으므로 사용을 피하세요.
- 이미지에 높이와 너비를 설정하지 마세요. 열화된 이메일에서 불필요한 여백이 발생할 수 있습니다.
- 대부분의 이메일 클라이언트가 `div` 태그 사용을 지원하지 않으므로 사용하지 않는 것이 좋습니다. 대신 중첩 테이블을 사용하세요.
- JavaScript는 어떤 ESP에서도 작동하지 않으므로 사용을 피하세요.
- 이메일 템플릿에서 CSS `position: absolute` 및 `position: relative` 사용을 피하세요. 대부분의 이메일 클라이언트가 CSS 포지셔닝을 지원하지 않아 Braze 미리보기와 실제 전달된 이메일 간에 레이아웃 차이가 발생할 수 있습니다. 레이어 또는 겹침 효과를 구현하려면 테이블 기반 레이아웃을 사용하세요.
- Braze는 글로벌 CDN을 사용하여 모든 이메일 이미지를 호스팅함으로써 로드 시간을 개선합니다.
- 모바일에서는 이미지 열이 좁지만(각 약 100px), 여러 이미지 행도 여전히 맞습니다(예: 4개의 이미지 ≈ 4개의 사용 가능한 열).

## 대체 텍스트 {#alternative-text}

스팸 필터는 메시지의 HTML 버전과 일반 텍스트 버전을 모두 확인하므로, 일반 텍스트 대체 요소를 활용하면 스팸 점수를 낮추는 데 효과적입니다. 또한 대체 텍스트(`alt=""`)는 이메일 본문에 포함된 이미지가 사용자의 이메일 공급자에 의해 필터링되었을 때 이미지를 보완하거나 대체하는 역할을 할 수 있습니다. 스크린 리더는 이미지를 설명하기 위해 대체 텍스트를 읽어주므로, 이미지에 대한 핵심 정보를 쉬운 언어로 전달할 수 있는 좋은 기회입니다.

{% alert note %}
대체 텍스트에 따옴표가 포함된 경우, 큰따옴표(`"`) 대신 작은따옴표(`'`)를 사용하세요. 큰따옴표는 HTML 속성이 조기에 닫히면서 텍스트가 잘릴 수 있습니다. 예를 들어, `alt="Product 'Premium' Edition"`은 올바르게 작동하지만, `alt="Product "Premium" Edition"`은 잘립니다.
{% endalert %}

## 이메일 유효성 검사 {#email-validation}

{% alert important %}
유효성 검사는 대시보드 이메일 주소, 최종 사용자(고객) 이메일 주소, 이메일 메시지의 발신 주소 및 회신 주소에 사용됩니다.
{% endalert %}

이메일 유효성 검사는 사용자의 이메일 주소가 업데이트되거나 API, CSV 업로드, SDK를 통해 Braze로 가져오거나 대시보드에서 수정될 때 수행됩니다. 이메일 주소에는 공백이 포함될 수 없으며, API를 사용하여 전송할 경우 공백이 있으면 `400` 오류가 발생할 수 있습니다.

Braze 서버를 통해 타겟팅되는 이메일 주소는 [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822) 표준에 따라 유효성이 검사되어야 하며, Braze는 특정 문자를 허용하지 않고 유효하지 않은 것으로 인식합니다. 이메일이 반송되면 Braze는 해당 이메일을 유효하지 않은 것으로 표시하며 가입 상태는 변경되지 않습니다.

허용되지 않는 문자 및 이메일 유효성 검사 규칙에 대한 자세한 내용은 [이메일 유효성 검사]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation#how-it-works)를 참조하세요.

## 시작 및 회신 주소 {#from-and-reply-to-addresses}

"시작" 주소를 설정할 때, "시작" 이메일 도메인이 발신 도메인(예: `marketing.yourdomain.com`)과 일치하는지 확인하세요. 이를 지키지 않으면 SPF 및 DKIM 정렬이 맞지 않을 수 있습니다. 모든 회신 주소 이메일은 루트 도메인으로 설정할 수 있습니다.

{% alert note %}
"시작" 주소에서는 유니코드 인코딩이 지원되지 않습니다.
{% endalert %}

## 이메일 첨부 파일 {#attachments}

이메일 메시지에 첨부 파일을 추가할 때는 다음 전달 가능성 모범 사례를 따르세요:

- 스팸 필터가 첨부 파일을 검사하여 메시지를 스팸으로 표시할 수 있습니다.
- 메일 공급자가 첨부 파일이 포함된 메시지를 수락하는 데 더 오래 걸릴 수 있습니다.
- 일대일 메시지 외에 첨부 파일은 받은편지함에서 메시지가 위험해 보이게 만들 수 있습니다.
- 각 첨부 파일은 2&nbsp;MB 미만으로 유지하세요.
- 민감한 정보를 첨부 파일로 보내지 마세요. 대신 사용자를 보안 포털로 안내하여 해당 정보를 확인하도록 하세요.

## 레이아웃 (드래그 앤 드롭 및 커스텀 HTML) {#layout-drag-and-drop-and-custom-html}

Braze에서 생성된 HTML/CSS가 커스텀 HTML과 충돌하면 레이아웃이 깨질 수 있습니다. 이 경우 다음을 수행하세요:

- 먼저 커스텀 HTML/CSS를 제거하세요
- 미리보기에서 커스텀 폰트가 올바르게 로드되는지 확인하세요
- 행과 열의 패딩을 확인하세요
- 테이블 기반 레이아웃을 사용하고, 에디터의 너비 범위 내에서 작업하세요.

에디터 외부에서 HTML을 가져오는 Content Blocks도 레이아웃을 깨뜨릴 수 있습니다.

## 이메일 URL의 UTM 매개변수 {#utm-parameters-in-email-urls}

UTM 매개변수는 분석을 위해 URL에 태그를 추가합니다. Liquid와 커스텀 속성을 사용하여 빌드할 수 있습니다.

- 최종 URL에는 물음표 `?`를 하나만 사용하세요(추가 `?` 문자는 요청을 중단시킬 수 있습니다).
- 값에 공백이나 특수 문자를 사용하지 마세요(`_` 또는 `-`를 사용하세요).
- 분석 도구가 UTM을 수집하는지 확인하세요. Liquid `capture` 블록 내부의 후행 공백을 제거하세요. UTM은 대소문자를 구분합니다.

### HTML 세부 사항 확인 {#check-html-details}

일부 HTML 태그와 속성은 브라우저에서 악성코드가 실행될 수 있으므로 허용되지 않습니다.

이메일에서 허용되지 않는 HTML 태그와 속성에 대한 다음 목록을 확인하세요:
{% details 허용되지 않는 HTML 태그 펼치기 %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `iframe`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`
{% enddetails %}

{% details 허용되지 않는 HTML 속성 펼치기 %}
- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`
{% enddetails %}