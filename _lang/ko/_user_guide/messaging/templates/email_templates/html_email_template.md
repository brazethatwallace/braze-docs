---
nav_title: HTML 이메일 템플릿 업로드
article_title: HTML 이메일 템플릿 업로드
page_order: 2
description: "이 참조 문서에서는 Braze 대시보드를 사용하여 HTML 이메일 템플릿을 생성, 관리 및 문제 해결하는 방법을 다룹니다."
tool:
  - Templates
channel:
  - email

---

# HTML 이메일 템플릿 업로드 {#upload-an-html-email-template}

> Braze 대시보드에서는 자체 HTML 이메일 템플릿을 업로드하고 나중에 Campaign에서 사용할 수 있도록 저장할 수 있습니다. 에디터를 사용하여 [이메일 템플릿을 생성]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)할 수도 있습니다.

## 요구 사항 {#upload-requirements}

먼저 HTML 이메일 템플릿을 생성해야 합니다. 이 파일은 다음을 포함하는 ZIP 파일이어야 합니다:

* 단일 HTML 파일—이메일 본문
* HTML 파일에서 참조되는 이미지 폴더
* 50개 미만의 이미지 파일
* 5&nbsp;MB 미만의 파일 크기

## 템플릿 업로드 {#uploading-your-template}

### 1단계: 이메일 템플릿 에디터로 이동 {#step-1-go-to-the-email-template-editor}

**콘텐츠** > **이메일**로 이동합니다. **이메일 템플릿 생성**을 선택합니다.

### 2단계: 템플릿 세부 정보 추가 {#step-2-add-template-details}

템플릿 이름을 입력합니다. 선택 사항으로 설명, Teams, 태그를 추가할 수 있습니다.

### 3단계: 템플릿 업로드 {#step-3-upload-your-template}

**템플릿 콘텐츠** 섹션에서 **파일 업로드**를 선택합니다. 컴퓨터에서 템플릿을 선택합니다. 템플릿이 업로드 요구 사항을 충족하는지 [요구 사항](#upload-requirements) 섹션을 참조하세요.

### 4단계: 템플릿 완성 및 저장 {#step-4-finish-and-save-your-template}

**템플릿 저장**을 선택하여 템플릿을 저장하세요. 이제 원하는 Campaign 또는 Canvas에서 이 템플릿을 사용할 준비가 되었습니다.

{% alert note %}
기존 템플릿을 편집하면 해당 템플릿의 이전 버전을 사용하여 생성된 Campaign에는 변경 사항이 반영되지 않습니다.
{% endalert %}

## API Campaign에서 템플릿 사용 {#api_for_upload_email_templates}

API Campaign에 이메일을 사용하려면 `email_template_id`가 필요하며, 이는 Braze에서 생성된 모든 이메일 템플릿 하단에서 확인할 수 있습니다.

![HTML 이메일 템플릿의 API 식별자 섹션.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## 이메일 템플릿 관리 {#managing-email-templates}

이메일 템플릿을 [복제]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) 및 [아카이브]({{site.baseurl}}/user_guide/messaging/templates/managing_templates)할 수 있습니다. 템플릿 및 크리에이티브 콘텐츠 생성과 관리에 대해 자세히 알아보려면 [템플릿]({{site.baseurl}}/user_guide/messaging/templates)을 참조하세요.

## 문제 해결 {#troubleshooting}

### 업로드 오류 {#upload-errors}

HTML 템플릿 파일을 업로드할 때 여러 이메일 오류 메시지를 받을 수 있습니다. 오류가 발생하면 다음 표에서 일반적인 문제와 권장 해결 방법을 참조하세요:

| 오류 | 해결 방법 |
|------|---|
| `.zip over 5&nbsp;MB` | 파일 크기를 줄이고 다시 업로드하세요.|
| `.zip corrupt` | 파일을 검사하고 다시 업로드하세요. |
| `Missing HTML` | ZIP 파일에 HTML 파일을 추가하고 다시 업로드하세요.|
| `Multiple HTML` | HTML 파일 중 하나를 제거하고 다시 업로드하세요.|
| `Images over 5&nbsp;MB` | 이미지 수를 줄이고 다시 업로드하세요. |
| `Extra Images` | HTML 파일에서 참조되지 않는 추가 이미지가 파일에 있을 수 있습니다. 이 경우 실패 오류가 발생하지는 않지만 추가 이미지는 삭제됩니다. 해당 이미지가 HTML 파일에서 참조되어야 하는 경우 콘텐츠를 확인하고 오류를 수정한 후 다시 업로드하세요.|
| `Missing Images` | HTML 파일에서 참조되는 이미지가 ZIP 파일의 이미지 폴더에 포함되어 있지 않으면 파일 오류가 발생합니다. 파일을 검사하고 오류(예: 오타)를 수정하거나 누락된 이미지를 ZIP 파일에 추가한 후 다시 업로드하세요.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="문제 해결" }

Windows 컴퓨터에서 HTML Campaign, 이메일 메시지가 포함된 캔버스 단계 또는 템플릿의 파일을 다운로드할 때 `|`(파이프 문자)가 지원되지 않으므로 ZIP 파일에서 다운로드 콘텐츠를 추출하려면 다른 애플리케이션을 사용해야 할 수 있습니다.

### 이메일이 올바르게 렌더링되지 않는 경우 {#email-not-rendering-properly}

이메일이 올바르게 렌더링되지 않는 경우, 각 콘텐츠 블록에 추가 `<!doctype>` 헤더가 없는지 확인하세요.

HTML 템플릿 자체에 `<!doctype>` 헤더가 있고 콘텐츠 블록 중 하나에도 HTML doctype이 있으면 이메일이 올바르게 렌더링되지 않습니다. 콘텐츠 블록은 이메일 템플릿의 기존 문서 구조에 추가되는 HTML 프래그먼트로 취급해야 합니다. 콘텐츠 블록에는 추가 body 태그나 템플릿 HTML 코드가 포함되어서는 안 됩니다. 경우에 따라 Emailify와 같은 도구가 추가 HTML 구조가 포함된 미리 작성된 코드를 가져올 수 있으므로 가져온 콘텐츠 블록을 주의 깊게 검토하세요.

또한 템플릿과 콘텐츠 블록 전체에서 중복된 태그와 클래스 이름이 있는지 확인하세요. 이러한 요소가 렌더링 문제를 일으킬 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

이메일 템플릿에 대한 자주 묻는 질문의 답변은 [이메일 및 링크 템플릿 FAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq) 페이지를 확인하세요.