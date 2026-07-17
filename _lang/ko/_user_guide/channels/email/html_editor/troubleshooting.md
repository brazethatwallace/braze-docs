---
nav_title: 문제 해결
article_title: HTML 이메일 문제 해결
page_order: 9
description: "증상 색인과 표준 문제 해결 단계를 사용하여 HTML 이메일 렌더링 및 편집기 문제를 진단합니다."
channel: email
---

# HTML 이메일 문제 해결 {#troubleshoot-html-emails}

> 이 페이지를 사용하여 일반적인 HTML 이메일 편집기 및 테스트 발송 문제를 해결하세요. Inbox Vision 및 전달 가능성에 대해서는 [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) 및 [이메일 설정]({{site.baseurl}}/user_guide/channels/email/email_setup)을 참조하세요.

## 시작하기: 증상 매칭 {#start-here-match-your-symptom}

아래 표에서 증상을 찾아 해당 섹션으로 이동하세요.

| 증상 | 이동 |
| --- | --- |
| 테스트 이메일 HTML이 잘못 보임 | [테스트 이메일에서 HTML이 올바르게 렌더링되지 않음](#html-renders-incorrectly-in-test-emails) |
| Chrome에서 편집기가 이상하게 동작함 | [확장 프로그램 충돌](#extension-conflicts) |
| 이메일 클라이언트마다 이메일이 다르게 보임 | [이메일 렌더링](#email-rendering) |
| Inbox Vision 미리보기가 발송된 이메일과 일치하지 않음 | [CSS 인라이닝](#css-inlining) |
| 테스트 이메일에서 이미지 뒤에 여백이나 선이 나타남 | [이미지 아래 여백](#white-space-under-images) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML 이메일 증상" }

## 표준 조사 경로 {#standard-investigation-path}

HTML 이메일 렌더링 또는 편집기 동작이 예상과 다를 때 이 워크플로를 사용하세요. 1단계부터 시작하세요.

1. 편집기 또는 외부 유효성 검사 도구에서 HTML 마크업을 검증합니다.
2. [테스트 이메일]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa)을 발송하고 문제가 나타나는 이메일 클라이언트 또는 브라우저를 기록합니다.
3. [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)으로 미리보기하여 클라이언트 간 렌더링을 비교합니다.
4. 편집기 자체가 오작동하는 경우 [브라우저 확장 프로그램 충돌](#extension-conflicts)을 배제합니다.
5. 문제가 지속되면 Inbox Vision 스크린샷과 영향을 받는 클라이언트 정보를 포함하여 [고객지원 티켓]({{site.baseurl}}/braze_support)을 열어주세요.

## 테스트 이메일에서 HTML이 올바르게 렌더링되지 않음 {#html-renders-incorrectly-in-test-emails}

**증상:** [테스트 이메일]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa)이 편집기에서 예상한 것과 일치하지 않습니다.

먼저 HTML 설정을 확인한 다음 [확장 프로그램 충돌](#extension-conflicts), [이메일 렌더링](#email-rendering), [CSS 인라이닝](#css-inlining), [이미지 아래 여백](#white-space-under-images)을 검토하세요.

### 확장 프로그램 충돌 {#extension-conflicts}

특정 브라우저 확장 프로그램이 이메일 편집기에 문제를 일으킬 수 있습니다. 예를 들어 Google Chrome에서 [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)를 사용하는 경우가 있습니다. 이러한 확장 프로그램을 사용 중이라면 다음 중 하나를 수행해야 합니다:

- Grammarly가 브라우저 확장 프로그램으로 설치되지 않은 브라우저에서 Braze 이메일을 편집합니다.
- Braze 계정 매니저에게 연락하여 이메일 편집기를 HTML 전용 또는 일반 텍스트로 전환해 달라고 요청합니다.

일반 텍스트 보기는 `WYSIWYG`(위지위그, 보이는 대로 얻는) 편집기를 제거하므로, 이 요청을 하기 전에 모든 팀원이 HTML에 익숙한지 먼저 확인해야 합니다.

### 이메일 렌더링 {#email-rendering}

이메일은 브라우저와 이메일 클라이언트에 따라 다르게 렌더링되므로, 문제가 발생하는 브라우저와 이메일 클라이언트를 기록해 두세요.

- [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)을 사용하여 다양한 브라우저와 이메일 클라이언트에서 이메일이 어떻게 보이는지 미리보기할 수 있습니다.
- 문제를 일으키는 브라우저 또는 이메일 클라이언트를 파악한 후, 개발자 팀에 해당 브라우저 또는 이메일 클라이언트에 맞게 HTML을 수정해야 한다고 알려주세요.

### CSS 인라이닝 {#css-inlining}

Inbox Vision의 미리보기가 Braze에서 발송된 이메일과 여전히 일치하지 않는 경우가 있습니다. 이는 Braze와 다른 도구 간의 CSS 인라이닝 처리 방식 차이로 인해 발생할 수 있습니다. 이 경우가 의심된다면 CSS 인라이닝을 비활성화하세요.

### 이미지 아래 여백 {#white-space-under-images}

**증상:** 테스트 이메일에서 이미지 뒤에 여백이나 선이 나타납니다.

테스트 이메일에서 이미지 뒤에 여백이나 선이 나타나는 경우, 이는 일반적으로 이메일 클라이언트가 인라인 수준 요소를 렌더링하는 방식 때문입니다. 이미지는 기본적으로 인라인 수준이며 베이스라인에 정렬되어 있어, 브라우저가 디센더(베이스라인 아래로 내려가는 "g"나 "y" 같은 글자 부분)를 수용할 수 있도록 합니다. 이로 인해 여백처럼 보이는 작은 간격이 생깁니다.

이 문제를 해결하려면 이미지 CSS에 `display: block;`을 추가하세요:

```html
<style>
  img {
    display: block;
  }
</style>
```

또는 특정 이미지에 직접 스타일을 적용할 수도 있습니다:

```html
<img src="https://example.com/image.jpg" style="display: block;" alt="Image description" />
```
