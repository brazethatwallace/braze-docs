---
nav_title: HTML 편집기
article_title: 커스텀 HTML로 이메일 만들기
page_order: 2
description: "이 참조 문서에서는 Braze 플랫폼을 사용하여 이메일을 만드는 방법을 다룹니다. 메시지 작성, 콘텐츠 미리보기, Campaign 또는 Canvas 스케줄 설정에 대한 모범 사례가 포함되어 있습니다."
tool:
  - Campaigns
channel:
  - email
search_rank: 1
---

# 커스텀 HTML로 이메일 만들기 {#create-an-email-with-custom-html}

> 이메일 메시지는 사용자가 원하는 조건에 맞춰 콘텐츠를 전달하는 데 매우 유용합니다. 또한 앱을 삭제한 사용자를 다시 참여시키는 데에도 훌륭한 도구입니다. 맞춤화된 이메일 메시지를 보내면 사용자 경험이 향상되고, 사용자가 앱에서 최대한의 가치를 얻을 수 있도록 도와줍니다.

이메일 Campaign 예시를 확인하려면 [활용 사례](https://www.braze.com/customers)를 참조하세요.

{% alert tip %}
이메일 Campaign을 처음 만드는 경우, 다음 Braze 학습 과정을 확인하는 것을 강력히 권장합니다:<br><br>
- [이메일 옵트인 및 권한](https://learning.braze.com/messaging-channels-email)
- [프로젝트: 기본 이메일 마케팅 프로그램 구축](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## 1단계: 메시지를 작성할 위치 선택하기 {#step-1-choose-where-to-build-your-message}

단순한 단일 메시지에는 Campaign을 사용하세요. 다단계 사용자 여정에는 Canvas를 사용하세요.

{% tabs %}
{% tab Campaign %}

1. **메시징** > **Campaigns**으로 이동하여 **캠페인 생성**을 선택합니다.
2. **이메일**을 선택하거나, 여러 채널을 타겟팅하는 Campaign의 경우 **멀티채널**을 선택합니다.
3. Campaign에 명확하고 의미 있는 이름을 지정합니다.
4. 필요에 따라 [팀]({{site.baseurl}}/user_guide/administer/global/user_management/teams/)과 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/)를 추가합니다.
   * 태그를 사용하면 Campaign을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder/)를 사용할 때 특정 태그로 필터링할 수 있습니다.
5. Campaign에 필요한 만큼 배리언트를 추가하고 이름을 지정합니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing/)를 참조하세요.

{% alert tip %}
Campaign의 모든 메시지가 유사하거나 동일한 콘텐츠를 가질 경우, 추가 배리언트를 추가하기 전에 먼저 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. Canvas 작성기를 사용하여 [Canvas를 만듭니다]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).
2. Canvas를 설정한 후, Canvas 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 지정합니다.
3. [단계 스케줄]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay)을 선택하고 필요에 따라 지연을 지정합니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. Segments를 지정하고 추가 필터를 추가하여 이 단계의 수신자를 더 세밀하게 조정할 수 있습니다. 오디언스 옵션은 지연 후 메시지가 발송되는 시점에 확인됩니다.
5. [진행 동작]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/)을 선택합니다.
6. 메시지와 함께 사용할 다른 메시징 채널을 선택합니다.
{% endtab %}
{% endtabs %}

{% alert tip %}
커스텀 HTML을 작성할 계획이고 기기 다크 모드가 켜진 Gmail 모바일 앱에서 배경이 일관되게 유지되어야 하는 경우, [Gmail 모바일 앱과 다크 모드 배경색](#gmail-dark-mode)을 참조하세요.
{% endalert %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## 2단계: 편집 환경 선택하기 {#step-2-choose-your-template-and-compose-your-email}

Braze는 이메일 Campaign을 만들 때 두 가지 편집 환경을 제공합니다: [드래그 앤 드롭 편집기]({{site.baseurl}}/dnd/)와 표준 HTML 편집기입니다. 원하는 편집 환경에 맞는 타일을 선택하세요.

![이메일 편집 환경으로 드래그 앤 드롭 편집기, HTML 편집기 또는 템플릿 중에서 선택하기.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

그런 다음 기존 [이메일 템플릿]({{site.baseurl}}/user_guide/channels/email/html_editor/#creating-an-email-template)을 선택하거나, 파일에서 [템플릿을 업로드]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template/)하거나(HTML 편집기만 해당), 빈 템플릿을 사용할 수 있습니다.

HTML 편집기를 사용하고 기기가 다크 모드일 때 Gmail 모바일 앱에서 배경색이 일관되게 유지되어야 하는 경우, [Gmail 모바일 앱과 다크 모드 배경색](#gmail-dark-mode)을 참조하세요.

{% alert tip %}
이메일 Campaign당 하나의 편집 환경을 선택하는 것을 권장합니다. 예를 들어, 단일 이메일 Campaign에서 편집기 간에 전환하지 말고 **HTML Classic** 또는 **Block editor** 중 하나를 선택하세요.
{% endalert %}

## 3단계: 이메일 작성하기 {#step-3-compose-your-email}

템플릿을 선택하면 이메일 개요가 표시되며, 여기서 전체화면 편집기로 바로 이동하여 이메일을 작성하고, 발송 정보를 변경하고, 전달 가능성 또는 법률 준수에 대한 경고를 확인할 수 있습니다. 작성하는 동안 HTML, 클래식, 일반 텍스트, [AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email/) 탭 간에 전환할 수 있습니다.

!["HTML에서 재생성" 버튼.]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

Braze는 일반 텍스트 버전에 대한 편집이 감지될 때까지 HTML 버전에서 자동으로 일반 텍스트 버전을 업데이트합니다. Braze가 편집을 감지하면 의도적인 변경이 이루어졌다고 판단하여 자동 업데이트를 중단합니다. 자동 동기화를 복원하려면 **Plaintext**로 이동하여 **Regenerate from HTML**을 선택합니다(일반 텍스트가 동기화되지 않을 때만 표시됨).

{% alert tip %}
정확한 미리보기와 함께 이메일에 모션을 추가하려면 JavaScript 대신 GIF를 사용하세요. 대부분의 받은편지함에서 JavaScript를 지원하지 않습니다.
{% endalert %}


{% alert important %}
Braze는 속성으로 참조된 HTML 이벤트 핸들러를 자동으로 제거합니다. 이로 인해 HTML이 수정되므로, 작성을 완료한 후 이메일을 다시 확인하세요. [HTML 핸들러](https://www.w3schools.com/tags/ref_eventattributes.asp)에 대해 자세히 알아보세요.
{% endalert %}

{% alert tip %}
멋진 카피를 작성하는 데 도움이 필요하신가요? [AI 카피라이팅 어시스턴트]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/)를 사용해 보세요. 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있는 사람이 쓴 것 같은 마케팅 카피를 생성합니다.

![이메일 작성기의 본문 탭에 있는 AI 카피라이터 시작 버튼.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

아랍어나 히브리어와 같은 오른쪽에서 왼쪽으로 쓰는 언어의 메시지를 작성하는 데 도움이 필요하신가요? 모범 사례는 [오른쪽에서 왼쪽으로 쓰는 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/)를 참조하세요.

### Gmail 모바일 앱과 다크 모드 {#gmail-dark-mode}

Gmail 모바일 앱(Android 및 iOS)은 기기가 다크 모드일 때 배경색을 반전시킬 수 있습니다. 이로 인해 이메일 배경이 이미지 가장자리나 특정 브랜드 색상과 일치해야 하는 레이아웃이 깨질 수 있습니다.

이를 방지하려면, 안정적인 배경이 필요한 테이블 셀에서 `background-color` 대신 단색 CSS `linear-gradient`를 사용하세요. Gmail은 단색 배경색보다 이 처리를 반전시킬 가능성이 낮습니다.

예를 들어, 셀에 흰색 배경을 유지하려면 다음을 사용하세요:

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

`#ffffff`를 원하는 색상으로 교체하세요.

{% alert note %}
이 방법은 `<table aria-label="Gmail mobile app and dark mode #gmail-dark-mode">` 요소에만 단독으로 적용하면 안정적으로 작동하지 않으므로, 테이블이 아닌 셀에 그라디언트를 설정하세요.
  <caption>Gmail 모바일 앱과 다크 모드</caption>
{% endalert %}

그라디언트 구문에 대한 자세한 내용은 [W3Schools의 CSS 그라디언트](https://www.w3schools.com/css/css3_gradients.asp)를 참조하세요.

### 3.1단계: 발송 정보 추가하기 {#step-31-add-your-sending-information}

이메일 메시지 디자인과 작성을 완료한 후, **Sending Settings**에서 발송 정보를 추가합니다.

1. **Sending Info**에서 **From Display Name + Address**로 이메일을 선택합니다. **Customize From Display Name + Address**를 선택하여 커스터마이즈할 수도 있습니다.
2. **Reply-To Address**로 이메일을 선택합니다. **Customize Reply-To Address**를 선택하여 커스터마이즈할 수도 있습니다.
3. 다음으로, **BCC Address**로 이메일을 선택하여 이 주소에서 이메일을 볼 수 있도록 합니다.
4. 이메일에 제목란을 추가합니다. 선택적으로 프리헤더와 프리헤더 뒤의 공백도 추가할 수 있습니다.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

오른쪽 패널의 미리보기에 추가한 발송 정보가 표시됩니다. 이 정보는 **설정** > **이메일 환경설정** > **발송 구성**으로 이동하여 업데이트할 수도 있습니다.

#### 고급 {#advanced}

**Sending Settings** > **Advanced**에서 가장 넓은 클라이언트 지원을 위해 **인라인 CSS**를 켭니다. 메시지가 잘리거나 이미지가 행 높이로 늘어나는 경우, 인라인 CSS를 일시적으로 **끄기**로 해보세요. 일부 템플릿은 인라인 처리 없이 더 잘 작동합니다.

이메일 헤더와 이메일 추가 정보에 개인화를 추가하여 다른 이메일 서비스 제공업체로 추가 데이터를 보낼 수도 있습니다.

##### 이메일 첨부 파일 {#email-attachments}

다음 방법으로 이메일 첨부 파일을 추가할 수도 있습니다:

- **파일 업로드:** 컴퓨터에서 직접 파일을 드래그 앤 드롭하거나 찾아보기로 이메일에 업로드합니다. Braze는 업로드 전에 파일 유형과 크기(기본적으로 최대 2&nbsp;MB)를 검증한 후 미디어 라이브러리에 업로드합니다. 2&nbsp;MB 제한을 초과하는 파일은 업로드할 수 없습니다.
- **미디어 라이브러리 사용:** [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)에 이미 저장된 자산을 찾아보고 선택합니다. PDF, Word 문서, Excel 파일, PowerPoint 프레젠테이션이 모두 지원됩니다.
- **URL에서 추가:** 파일을 가리키는 URL을 입력하고 표시 파일 이름을 제공합니다. Braze는 이메일 작성 중에 임의의 URL의 크기를 확인할 수 없으므로, 파일 크기는 발송 시점에 적용됩니다. 이 필드에서는 Liquid가 지원되지 않습니다.

구체적인 모범 사례는 [이메일 가이드라인]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines/)을 참조하세요.

##### 이메일 헤더 {#email-headers}

이메일 헤더를 추가하려면 **Add New Header**를 선택합니다. 이메일 헤더에는 발송되는 이메일에 대한 정보가 포함됩니다. 이러한 [키-값 페어]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/)에는 일반적으로 발신자, 수신자, 인증 프로토콜 및 라우팅 정보가 포함됩니다. Braze는 이메일이 받은편지함 제공업체에 도달할 수 있도록 RFC에서 요구하는 헤더 정보를 자동으로 추가합니다.

Braze는 고급 사용 사례를 위해 필요에 따라 추가 이메일 헤더를 추가할 수 있는 유연성을 제공합니다. Braze 플랫폼이 발송 중에 덮어쓰는 몇 가지 예약된 필드가 있습니다.

다음 키는 사용하지 마세요:

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table aria-label="이메일 헤더" id="reserved-fields">
  <caption>이메일 헤더</caption>
<thead>
  <tr>
    <th>예약된 필드</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>dkim-signature</td>
    <td>Reply-To</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>From</td>
    <td>Subject</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>MIME-Version</td>
    <td>To</td>
  </tr>
  <tr>
    <td>Content-Type</td>
    <td>Received</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>DKIM-Signature</td>
    <td>received</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### 이메일 추가 정보 추가하기 {#adding-email-extras}

이메일 추가 정보를 사용하면 다른 이메일 서비스 제공업체로 추가 데이터를 보낼 수 있습니다. 이는 고급 사용 사례에만 적용되므로, 회사에서 이미 이 기능을 설정한 경우에만 이메일 추가 정보를 사용해야 합니다.

이메일 추가 정보를 추가하려면 **Sending Info**로 이동하여 **Add New Extra**를 선택합니다.

{% alert warning %}
추가된 키-값 페어의 총 크기는 1KB를 초과하지 않아야 합니다. 그렇지 않으면 메시지가 중단됩니다.
{% endalert %}

이메일 추가 정보 값은 Currents 또는 Snowflake에 게시되지 않습니다. Currents 또는 Snowflake로 추가 메타데이터나 동적 값을 보내려면 [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras/)를 대신 사용하세요.

### 3.2단계: 메시지 미리보기 및 테스트하기 {#step-3b-preview-and-test-your-message}

이메일 작성을 완료한 후, 발송하기 전에 테스트하세요. 개요 화면 하단에서 **미리보기 및 테스트**를 선택합니다.

여기서 고객의 받은편지함에 이메일이 어떻게 표시되는지 미리볼 수 있습니다. **사용자로 미리보기**를 선택하면 랜덤 사용자로 이메일을 미리보거나, 특정 사용자를 선택하거나, 커스텀 사용자를 만들 수 있습니다. 이를 통해 연결된 콘텐츠와 개인화 호출이 제대로 작동하는지 테스트할 수 있습니다.

그런 다음 **미리보기 링크 복사**를 사용하여 랜덤 사용자에게 이메일이 어떻게 보이는지 보여주는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 이 링크는 7일 후에 재생성해야 합니다.

데스크탑, 모바일, 일반 텍스트 보기 간에 전환하여 다양한 컨텍스트에서 메시지가 어떻게 표시되는지 확인할 수도 있습니다.

{% alert tip %}
다크 모드 사용자에게 이메일이 어떻게 보이는지 궁금하신가요? **미리보기 및 테스트** 섹션에 있는 **다크 모드 미리보기** 토글을 선택하세요(드래그 앤 드롭 편집기만 해당). HTML 편집기를 사용하는 경우에도 [Gmail 모바일 앱과 다크 모드](#gmail-dark-mode)를 통해 Gmail 모바일 다크 모드 렌더링을 처리할 수 있습니다.
{% endalert %}

최종 확인 준비가 되면 **테스트 발송**을 선택하고 자신이나 테스터 그룹에 테스트 메시지를 보내 이메일이 기기와 클라이언트에서 올바르게 표시되는지 확인합니다.

![이메일 작성 시 테스트 발송 옵션과 예시 이메일 미리보기.]({% image_buster /assets/img_archive/newEmailTest.png %})

이메일에 문제가 있거나 변경하고 싶은 사항이 있으면 **이메일 편집**을 선택하여 편집기로 돌아갑니다.

{% alert tip %}
미리보기 텍스트를 지원하는 이메일 클라이언트는 항상 사용 가능한 모든 미리보기 텍스트 공간을 채울 만큼 충분한 문자를 가져옵니다. 그러나 이로 인해 미리보기 텍스트가 불완전하거나 최적화되지 않은 상황이 발생할 수 있습니다.
<br><br>이를 방지하려면 원하는 미리보기 텍스트 뒤에 공백을 만들어 이메일 클라이언트가 다른 방해가 되는 텍스트나 문자를 봉투 콘텐츠로 가져오지 않도록 할 수 있습니다. 이를 위해 표시하려는 미리보기 텍스트 뒤에 제로 너비 비결합자(‌`&zwnj;`)와 줄바꿈 없는 공백(`&nbsp;`)의 체인을 추가합니다. <br><br>프리헤더 섹션의 미리보기 텍스트 끝에 추가하면, HTML 편집기용 다음 코드가 원하는 공백을 추가합니다:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

드래그 앤 드롭 편집기의 경우, **Sending Settings** 섹션의 프리헤더에 `<div>` 서식 없이 제로 너비 비결합자(‌`&zwnj;`)만 직접 추가합니다.
{% endalert %}

{% alert note %}
Apple Mail 앱에서 HTML 이메일의 이미지 링크가 클릭 가능하려면 `https://` URL을 사용해야 합니다. Apple Mail 수신자의 클릭이 예상되는 경우 앵커 태그로 감싼 모든 이미지에 보안 링크를 사용하세요.
{% endalert %}

### 3.3단계: 이메일 오류 확인하기 {#step-33-check-for-email-errors}

발송 전에 편집기가 일반적인 문제를 표시합니다:

- 보낸 사람 표시 이름과 헤더가 함께 설정되지 않음
- 잘못된 보낸 사람 또는 회신 주소
- 중복된 헤더 키
- Liquid 구문 오류
- 전체 `<!DOCTYPE html>`을 포함하는 Content Blocks
- 이메일 본문이 400&nbsp;KB를 초과함
  - 잘림을 방지하려면 [102&nbsp;KB 미만]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size)을 목표로 하세요.
- 빈 본문 또는 제목
- 탈퇴 링크 누락
- 보낸 사람 도메인이 허용 목록에 없음(발송이 크게 제한됨)

## 4단계: Campaign 또는 Canvas의 나머지 부분 구축하기 {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}
다음으로, Campaign의 나머지 부분을 구축합니다. Braze 도구를 사용하여 이메일 Campaign을 구축하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

### 전달 스케줄 또는 트리거 선택하기 {#choose-delivery-schedule-or-trigger}

예약된 시간, 동작 또는 API 트리거를 기반으로 이메일을 전달합니다. 자세한 내용은 [Campaign 스케줄 설정]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/)을 참조하세요.

{% alert note %}
API 트리거 Campaign의 경우, 트리거 동작이 **Interact With Campaign**으로 설정되어 있을 때 상호작용으로 **Receive** 옵션을 선택하면, 해당 메시지가 반송되거나 전달에 실패하더라도 Braze가 선택한 Campaign을 발송 완료로 표시하는 즉시 새 Campaign이 트리거됩니다.
{% endalert %}

Campaign의 기간을 설정하고, [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/)을 지정하고, [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping) 규칙을 설정할 수도 있습니다.

### 타겟 사용자 선택하기 {#choose-users-to-target}

다음으로, Segments 또는 필터를 선택하여 [사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/)합니다. Braze는 이메일을 통해 도달 가능한 사용자 수를 포함하여 Segment 모집단의 실시간 미리보기를 표시합니다. 정확한 Segment 멤버십은 발송 직전에 계산됩니다.

{% multi_lang_include target_audiences.md %}

이메일에 가입하고 옵트인한 사용자와 같이 특정 [구독 상태]({{site.baseurl}}/user_guide/channels/email/subscriptions/)를 가진 사용자에게만 Campaign을 보내도록 선택할 수도 있습니다.

선택적으로, Segment 내 지정된 수의 사용자에게만 전달을 제한하거나, Campaign이 반복될 때 사용자가 동일한 메시지를 두 번 받을 수 있도록 허용할 수도 있습니다.

{% alert note %}
새 이메일 Campaign을 만들 때 대조군은 기본적으로 20%로 설정되며, Campaign에 맞게 조정하거나 제거할 수 있습니다.
{% endalert %}

#### 이메일과 푸시를 포함하는 멀티채널 Campaign {#multichannel-campaigns-with-email-and-push}

이메일과 푸시 채널을 모두 타겟팅하는 멀티채널 Campaign의 경우, 명시적으로 옵트인한 사용자만 메시지를 받도록 Campaign을 제한할 수 있습니다(가입됨 또는 가입 취소된 사용자 제외). 예를 들어, 서로 다른 옵트인 상태를 가진 세 명의 사용자가 있다고 가정해 보겠습니다:

- **사용자 A**는 이메일에 가입되어 있고 푸시가 활성화되어 있습니다. 이 사용자는 이메일을 받지 않지만 푸시를 받습니다.
- **사용자 B**는 이메일에 옵트인했지만 푸시가 활성화되어 있지 않습니다. 이 사용자는 이메일을 받지만 푸시를 받지 않습니다.
- **사용자 C**는 이메일에 옵트인했고 푸시가 활성화되어 있습니다. 이 사용자는 이메일과 푸시를 모두 받습니다.

이를 위해 **오디언스 요약**에서 이 Campaign을 "옵트인한 사용자에게만" 보내도록 선택합니다. 이 옵션은 옵트인한 사용자만 이메일을 받도록 하며, Braze는 기본적으로 푸시가 활성화된 사용자에게만 푸시를 보냅니다.

{% alert important %}
이 구성에서는 **타겟 오디언스** 단계에서 오디언스를 단일 채널로 제한하는 필터(예: `Foreground Push Enabled = True` 또는 `Email Subscription = Opted-In`)를 포함하지 마세요.
{% endalert %}

### 전환 이벤트 선택하기 {#choose-conversion-events}

Braze를 사용하면 Campaign을 수신한 후 사용자가 특정 동작인 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 다음 동작 중 하나를 전환 이벤트로 지정할 수 있습니다:

- 앱 열기
- 구매하기(일반 구매 또는 특정 항목일 수 있음)
- 특정 커스텀 이벤트 수행
- 이메일 열기

사용자가 지정된 동작을 수행하면 Braze가 전환을 카운트하는 최대 30일의 기간을 허용할 수 있습니다. Braze는 열기와 클릭을 자동으로 추적하지만, [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/)을 사용하려면 전환 이벤트를 열기 또는 클릭으로 설정할 수 있습니다.
{% endtab %}

{% tab Canvas %}
아직 완료하지 않았다면, Canvas 구성요소의 나머지 섹션을 완료하세요. Canvas의 나머지 부분을 구축하고, 다변량 테스트와 지능형 선택을 구현하는 방법 등에 대한 자세한 내용은 Canvas 설명서의 [Canvas 구축하기]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.
{% endtab %}
{% endtabs %}

## 5단계: 검토 및 배포하기 {#step-5-review-and-deploy}

마지막 섹션에서는 설계한 Campaign의 요약을 보여줍니다. 모든 관련 세부 정보를 확인하고 **캠페인 시작**을 선택합니다.

이메일 Campaign의 결과에 액세스하는 방법을 알아보려면 [이메일 보고서]({{site.baseurl}}/user_guide/channels/email/reporting/)를 확인하세요.