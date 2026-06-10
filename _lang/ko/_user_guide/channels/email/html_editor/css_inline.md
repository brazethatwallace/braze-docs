---
nav_title: CSS 인라이닝
article_title: CSS 인라이닝
page_order: 5.1
description: "이 참조 문서에서는 CSS 인라이닝을 활성화하는 방법과 몇 가지 모범 사례를 다룹니다."
channel:
  - email

---

# CSS 인라이닝 {#css-inlining}

> CSS 인라이닝은 CSS 스타일 시트의 스타일을 HTML 이메일 본문으로 이동하는 이메일 전처리의 한 형태입니다. "인라이닝"이라는 용어는 스타일이 개별 HTML 요소에 "인라인"으로 적용된다는 사실을 의미합니다.

일부 이메일 클라이언트의 경우 CSS 인라이닝을 사용하면 이메일이 렌더링되는 방식을 개선하고 이메일이 예상한 대로 표시되는지 확인할 수 있습니다. 이미 CSS의 대부분이 인라인 처리되었거나 HTML과 CSS가 대부분의 메일 클라이언트의 요구 사항과 호환된다고 확신하는 경우, 이 기능을 활성화할 필요가 없을 수 있습니다. 동적으로 삽입된 스타일이 기존 인라인 스타일과 충돌할 수 있으며, 예상하는 미리보기 및 이메일 렌더링이 변경될 수 있습니다.

## CSS 인라이닝 사용 {#using-css-inlining}

이메일 메시지에 대해 CSS 인라이닝을 켜거나 끌 수 있습니다. HTML 편집기의 **발송 정보** 탭에 있는 **인라인 CSS 활성화** 토글을 사용하세요.

![HTML 작성기에서 CSS 인라이닝을 관리하는 체크박스.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### 기본 인라이닝 상태 {#default-inlining-state}

**설정** > **이메일 환경설정**에서 전역적으로 기본 켜기 또는 끄기 상태를 설정할 수 있습니다. **CSS 인라이닝** 설정을 찾으세요. 이 설정은 모든 새 이메일 메시지가 시작할 때 적용되는 기본값을 결정합니다. 이 설정을 변경해도 기존 이메일 메시지에는 영향을 미치지 않습니다. 이메일 메시지를 작성하는 동안 언제든지 이 기본값을 재정의할 수도 있습니다.

![이메일 설정에 있는 새 이메일의 인라인 CSS 기본 옵션.]({% image_buster /assets/img_archive/css-inline1.png %})

## 연결된 콘텐츠와 CSS 인라이닝 {#connected-content-and-css-inlining}

CSS 인라이닝은 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)가 평가되기 **전에** 실행됩니다. 연결된 콘텐츠에서 반환된 HTML은 동일한 인라이닝 단계를 **거치지 않습니다**. 연결된 콘텐츠에서 필요한 스타일은 응답에 직접 포함하거나(인라인 `style` 속성 또는 임베디드 규칙), 템플릿에 더 적합한 경우 해당 메시지의 인라이닝을 비활성화하세요.

## 커스텀 HTML 템플릿의 Content Blocks {#content-blocks-in-custom-html-templates}

**커스텀 HTML** 이메일 템플릿이나 Campaign에서 Liquid를 사용하여 [콘텐츠 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)을 가져올 때, 상위 템플릿의 CSS 규칙이 콘텐츠 블록 내부에 정의된 스타일을 재정의할 수 있습니다. 템플릿 래퍼에서 충돌하는 선택자나 전역 규칙이 있는지 확인하세요.