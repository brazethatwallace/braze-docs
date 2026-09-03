---
nav_title: 이메일 템플릿 만들기
article_title: 이메일 템플릿 만들기
page_order: 0
description: "이 참조 문서에서는 이메일 템플릿을 만들고, 커스텀하고, 관리하는 방법을 다룹니다."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# 이메일 템플릿 만들기 {#create-an-email-template}

> Braze 대시보드에는 맞춤형의 눈길을 끄는 이메일을 만들고 나중에 Campaign에서 사용할 수 있도록 저장할 수 있는 이메일 템플릿 편집기가 있습니다. 직접 만든 [HTML 이메일 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)을 업로드할 수도 있습니다.

## 1단계: 이메일 템플릿 편집기로 이동 {#step-1-navigate-to-the-email-template-editor}

Braze 대시보드에서 **콘텐츠** > **이메일**로 이동합니다.

## 2단계: 편집 환경 선택하기 {#step-2-select-your-editing-experience}

편집 환경으로 **드래그 앤 드롭 편집기** 또는 **HTML 코드 편집기** 중에서 선택하세요.

미리 디자인된 Braze 템플릿 중에서 선택하거나, 새 템플릿을 만들거나, 기존 템플릿(일반 또는 [모바일 응답형]({{site.baseurl}}/releases/2018/may#mobile-responsive-email-templates))을 편집할 수도 있습니다.

![드래그 앤 드롭 편집기 또는 HTML 편집기를 선택하거나 Braze 템플릿에서 선택할 수 있는 옵션이 포함된 회사의 봄 세일 이메일 템플릿.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
기존의 커스텀 HTML 템플릿은 드래그 앤 드롭 편집기를 사용하여 다시 만들어야 합니다.
{% endalert %}

## 3단계: 템플릿 커스터마이즈하기 {#step-3-customize-your-template}

편집기 환경을 선택한 후, 이메일 템플릿을 자유롭게 커스터마이즈할 수 있습니다. HTML 편집기에서 HTML을 사용하여 브랜딩을 제작하고 재현하거나, 드래그 앤 드롭 편집기에서 다양한 [크리에이티브 세부 사항]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)을 포함할 수 있습니다.

### 탈퇴 링크 포함하기 {#include-an-unsubscribe-link}

이메일 템플릿을 디자인할 때 탈퇴 링크를 포함하지 않으면, Braze에서 이메일에 이를 추가하라는 메시지를 표시합니다. 탈퇴 링크는 모든 마케팅 이메일에 법적으로 필수입니다. Liquid 태그 {% raw %}``${email_footer}``{% endraw %}를 사용하여 이메일 하단에 푸터로 탈퇴 링크를 추가하거나, 템플릿에서 [푸터를 커스터마이즈]({{site.baseurl}}/user_guide/channels/email/subscriptions#custom-footer)할 수 있습니다.

## 4단계: 이메일 오류 확인 {#step-4-check-for-email-errors}

이메일 오류는 메시지 워크플로의 **작성** 탭에 표시됩니다. 오류가 있으면 다음 단계로 진행할 수 없습니다. "경고"는 모범 사례를 따르는 데 도움이 되는 알림을 나타냅니다. 비즈니스 상황에 따라 이러한 경고를 무시할 수도 있습니다.

![예시 이메일의 오류 및 경고 목록.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

에디터에서 확인되는 오류 목록은 다음과 같습니다:

- 잘못된 Liquid 구문
- [400KB를 초과하는 이메일 본문; 본문은 102KB 미만으로 유지하는 것을 적극 권장합니다]({{site.baseurl}}/user_guide/channels/email/best_practices)
- 탈퇴 링크가 없는 템플릿
- **본문** 또는 **제목**이 비어 있는 이메일
- 탈퇴 링크가 없는 이메일

## 5단계: 메시지 미리보기 및 테스트 {#step-5-preview-and-test-your-message}

템플릿 작성을 마치면 발송 전에 테스트할 수 있습니다.

개요 화면 하단에서 **미리보기 및 테스트**를 선택합니다. 여기에서 고객의 받은편지함에 이메일이 어떻게 표시되는지 미리 볼 수 있습니다. **사용자로 미리보기**를 선택하면 랜덤 사용자로 이메일을 미리 보거나, 특정 사용자를 선택하거나, 커스텀 사용자를 만들 수 있습니다. 이를 통해 연결된 콘텐츠와 개인화 호출이 올바르게 작동하는지 테스트할 수 있습니다.

그런 다음 **미리보기 링크 복사**를 클릭하면 랜덤 사용자에게 이메일이 어떻게 보이는지 확인할 수 있는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 자세한 내용은 [공유 가능한 미리보기]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview)를 참조하세요.

데스크톱, 모바일, 일반 텍스트 보기 간에 전환하여 다양한 상황에서 메시지가 어떻게 표시되는지 확인할 수도 있습니다.

{% alert tip %}
다크 모드 사용자에게 이메일이 어떻게 보이는지 궁금하신가요? **미리보기 및 테스트** 섹션에 있는 **다크 모드 미리보기** 토글을 선택하세요(드래그 앤 드롭 에디터에서만 사용 가능).
{% endalert %}

최종 확인이 준비되면 **테스트 발송**을 선택하고 자신이나 콘텐츠 테스터 그룹에게 테스트 메시지를 보내 다양한 기기와 이메일 클라이언트에서 이메일이 올바르게 표시되는지 확인하세요.

![테스트를 위해 발송될 이메일 미리보기 예시.]({% image_buster /assets/img_archive/newEmailTest.png %})

템플릿에 문제가 있거나 변경하고 싶은 부분이 있으면 **이메일 편집**을 선택하여 에디터로 돌아갑니다. **클래식** 에디터에서 수정한 내용은 HTML 에디터나 이메일 미리보기에 반영되지 않을 수 있습니다.

## 6단계: 템플릿 저장하기 {#step-6-save-your-template}

**템플릿 저장**을 선택하여 템플릿을 저장하세요. 이제 이 템플릿을 원하는 Campaign이나 Canvas 구성 요소에서 사용할 수 있습니다. 템플릿에 액세스하려면 해당 템플릿을 만들 때 사용한 편집 환경을 선택한 다음 사용 가능한 템플릿 목록에서 선택하세요.

{% alert note %}
기존 템플릿을 수정하더라도 해당 변경 사항은 이전 버전의 템플릿을 사용하여 생성된 Campaign에 반영되지 않습니다.
{% endalert %}

### 템플릿 관리하기 {#manage-your-templates}

**템플릿** > **이메일 템플릿**에서 이메일 템플릿을 확인할 수 있으며, 상태, 유형, 태그, 생성자별로 필터링하거나 템플릿 이름으로 검색할 수 있습니다. 이러한 템플릿을 보려면 **View Email Templates**와 같은 관련 사용자 권한이 필요합니다. 자세한 내용은 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)을 참조하세요.

더 많은 이메일 템플릿을 만들면서 이메일 템플릿을 [복제]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicating-templates)하거나 [보관]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archiving-templates)할 수 있습니다. 템플릿 및 크리에이티브 콘텐츠 라이브러리 생성과 관리에 대해 자세히 알아보려면 [템플릿과 미디어]({{site.baseurl}}/user_guide/messaging/templates)를 참조하세요.

### API Campaign에서 템플릿 사용하기 {#use-your-templates-in-api-campaigns}

API Campaign에 이메일을 사용하려면 `email_template_id`가 필요하며, 이는 Braze에서 생성된 모든 이메일 템플릿 하단에서 확인할 수 있습니다.

![이메일 템플릿 하단에 있는 API 식별자.]({% image_buster /assets/img/email_templates/template5.png %})

### 이메일 템플릿에 댓글 달기 {#comment-on-email-templates}

드래그 앤 드롭 에디터에서 이메일 템플릿에 대해 협업하고 댓글을 달 수 있습니다.

1. 댓글을 달고 싶은 이메일 본문의 콘텐츠 블록 또는 행을 선택합니다.
2. <i class="fas fa-comment" aria-label="댓글 아이콘"></i> 댓글 아이콘을 선택합니다.
3. 사이드바에 댓글을 입력한 다음 **제출**을 선택합니다.
4. 댓글 입력을 마친 후 **완료**를 선택합니다.
5. **템플릿 저장**을 선택하여 댓글을 저장합니다.

템플릿이 저장되면 사용자는 처리되지 않은 댓글 위에 아이콘을 볼 수 있습니다. **해결**을 선택하여 이러한 댓글을 해결하세요.

!["좋아 보여요"라는 이메일 템플릿 댓글.]({% image_buster /assets/img/email_templates/template_comment.png %})

이메일 템플릿에 대해 자주 묻는 질문의 답변은 [템플릿 FAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq)를 확인하세요.