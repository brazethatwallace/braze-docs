---
nav_title: FAQ
article_title: 이메일 및 링크 템플릿 FAQ
page_order: 10

page_type: FAQ
description: "이 페이지에서는 이메일 템플릿과 링크 템플릿에 대해 자주 묻는 질문을 다룹니다."
tool:
  - Templates
channel: email

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 페이지에서는 이메일 템플릿과 링크 템플릿에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 이메일 템플릿 {#email-templates}

### 이메일에 "브라우저에서 이 이메일 보기" 링크를 추가할 수 있나요? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

아니요, Braze는 이 기능을 제공하지 않습니다. 이는 점점 더 많은 이메일이 모바일 기기와 최신 이메일 클라이언트에서 열리고 있으며, 이러한 클라이언트는 이미지와 콘텐츠를 문제없이 렌더링하기 때문입니다.

**해결 방법:** 동일한 결과를 얻으려면 이메일 콘텐츠를 외부 랜딩 페이지(예: 웹사이트)에 호스팅한 다음, 이메일 본문을 편집할 때 **링크** 도구를 사용하여 작성 중인 이메일 Campaign에서 해당 페이지로 링크할 수 있습니다.

### 이메일 템플릿에 커스텀 탈퇴 링크를 만들려면 어떻게 해야 하나요? {#how-do-i-create-a-custom-unsubscribe-link-for-my-email-templates}

탈퇴 페이지에 대한 리디렉션 옵션이 있습니다.

사용자 지정 바닥글의 탈퇴 링크를 {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %}에서 사용자 ID를 포함하는 쿼리 파라미터가 있는 자체 웹사이트 링크로 변경할 수 있습니다. 예시는 다음과 같습니다:
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

다음으로, [`/email/status` 엔드포인트]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)를 호출하여 사용자의 구독 상태를 업데이트할 수 있습니다. 자세한 내용은 [이메일 구독 변경]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions)에 대한 설명서를 참조하세요.

이 새 링크를 저장하려면 기본 Braze 탈퇴 태그 {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%}가 바닥글에 있어야 합니다. 즉, 태그를 주석에 넣거나 숨겨진 `<div>` 태그에 배치하여 기본 링크를 "숨기는" 방식으로 포함해야 합니다.

- **주석에 태그 넣기 예시:** 주석에 태그를 넣는 예시: `<!-- ${set_user_to_unsubscribed_url} -->`
- **숨겨진 `<div>` 태그에 주석 넣기 예시:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### 현재 Campaign에서 사용 중인 이메일 템플릿을 편집하면 어떻게 되나요? {#what-happens-if-i-edit-an-email-template-that-is-currently-being-used-in-a-campaign}

기존 템플릿에 대한 편집 사항은 해당 템플릿의 이전 버전을 사용하여 생성된 Campaign에 반영되지 않습니다. REST API 본문에서 템플릿을 사용하는 API Campaign의 경우, Braze는 발송 시점에 최신 버전의 템플릿을 사용합니다.

## 링크 템플릿 {#link-templates}

### 이메일에 여러 링크 템플릿을 업로드할 수 있나요? {#can-i-upload-multiple-link-templates-to-my-email}

네, 이메일 메시지에 원하는 만큼 많은 템플릿을 삽입할 수 있습니다. 모범 사례로, 대부분의 브라우저가 링크를 단축하거나 잘라내므로 링크가 2,000자를 초과하지 않도록 이메일을 테스트해야 합니다.

### 모든 태그가 적용된 상태에서 링크를 미리보기하려면 어떻게 해야 하나요? {#how-do-i-preview-my-links-with-all-of-the-tags-applied}

링크를 미리보기하는 방법은 여러 가지가 있습니다. [링크 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template)을 적용한 후, 자신에게 [테스트 이메일]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)을 보내 모든 링크를 확인할 수 있습니다.

새 탭의 미리보기 창에서 링크를 열어 확인할 수도 있습니다. 또한 미리보기 창에서 링크 위에 마우스를 올리면 브라우저 하단에서 링크를 확인할 수 있습니다.

### 링크 템플릿은 Liquid와 어떻게 작동하나요? {#how-does-link-templating-work-with-liquid}

링크 템플릿은 Liquid 확장이 발생하기 전에 각 URL에 확장 및 추가됩니다. URL의 일부가 Liquid 스니펫을 사용하여 생성되는 경우, 링크 템플릿이 올바르게 확장되도록 URL 기본 주소와 물음표(?)를 하드코딩하는 것이 좋습니다.

Liquid에 물음표(?)를 추가하지 마세요. 이렇게 하면 링크 템플릿이 먼저 물음표(?)를 추가하고, 이후 Liquid 확장 프로세스에서 두 번째 물음표(?)를 추가하게 됩니다.

## 링크 별칭 지정 {#link-aliasing}

### 링크 별칭 지정을 활성화하면 Content Blocks와 링크 템플릿에 어떤 영향이 있나요? {#how-will-enabling-link-aliasing-impact-my-content-blocks-and-link-templates}

새로 생성되는 모든 Content Blocks에 대해 링크 별칭 지정은 회사 수준 기능이므로 워크스페이스 전체에 적용됩니다.

기존 Content Blocks는 링크 별칭 지정이 활성화되어도 수정되지 않습니다. 기존 링크 템플릿은 수정되지 않지만, 메시지 내 기존 링크 템플릿 섹션은 제거됩니다. 자세한 내용은 [Content Blocks에서의 링크 별칭 지정]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing#link-aliasing-in-content-blocks)을 참조하세요.

### HTML 앵커 태그 내에서 Liquid 조건 로직만 사용할 수 있나요? {#can-i-use-liquid-conditional-logic-entirely-within-an-html-anchor-tag}

아니요, Braze 링크 별칭 지정은 HTML을 올바르게 인식하지 못합니다.

이러한 로직이 HTML을 구문 분석해야 하는 기능(예: 프리헤더 또는 링크 템플릿)과 함께 사용되면, HTML을 스캔하는 데 사용되는 라이브러리가 앵커 태그를 수정하여 적절한 `href`가 템플릿화되지 않을 수 있습니다. 그러면 라이브러리는 Liquid 코드를 인식하지 못하므로 HTML이 유효하지 않다고 판단합니다.

대신, 각 단계에서 완전한 앵커 태그를 포함하는 Liquid 로직을 사용하세요. 이렇게 하면 로직에 유효한 HTML의 여러 인스턴스가 포함되므로 HTML 구문 분석에 간섭하지 않습니다. 또한 변수를 할당한 다음 적절한 앵커 태그에 템플릿화하여 로직을 단순화할 수도 있습니다.