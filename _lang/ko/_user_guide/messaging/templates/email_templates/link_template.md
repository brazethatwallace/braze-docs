---
nav_title: 링크 템플릿
article_title: 링크 템플릿
page_order: 4
description: "이 문서에서는 이메일에서 다양한 유형의 링크 템플릿을 만드는 방법을 설명합니다."
tool:
  - Templates
channel:
  - email

---

# 링크 템플릿 {#link-templates}

> 링크 템플릿을 사용하면 매개변수를 추가하거나 URL을 앞에 삽입하여 이메일 Campaign을 위한 동적이고 재사용 가능한 링크를 만들 수 있습니다. 이를 통해 Campaign과 메시지 전반에서 URL의 일관성을 유지할 수 있습니다.

{% alert note %}
링크 템플릿은 선택적 기능입니다. **템플릿** 섹션에 **이메일 링크 템플릿**이 표시되지 않는 경우, 계정 매니저에게 연락하여 기능을 활성화하세요.
{% endalert %}

## 작동 방식 {#how-it-works}

링크 템플릿은 주로 다음과 같은 사용 사례에서 활용됩니다:

- 특정 이메일 메시지의 모든 링크에 Google Analytics 쿼리 파라미터 추가
- 특정 이메일 메시지의 모든 링크 앞에 URL 추가

예를 들어, 신제품 출시를 위한 프로모션 이메일 Campaign을 진행한다고 가정해 보겠습니다. 링크 템플릿을 사용하면 사용자를 제품 페이지로 안내하고, 사용자의 이름이나 특정 프로모션 코드를 포함하여 링크를 개인화할 수 있습니다. 이를 통해 얼마나 많은 사용자가 링크를 클릭하고 구매를 완료했는지 추적할 수 있습니다. 이렇게 하면 링크 전반에 걸쳐 일관성을 유지하고 분석을 더 효과적으로 추적할 수 있습니다.

## 링크 템플릿 만들기 {#creating-a-link-template}

다양한 요구 사항을 지원하기 위해 링크 템플릿을 무제한으로 만들 수 있습니다. 링크 템플릿을 만들려면 다음을 수행하세요:

1. **콘텐츠** > **이메일 링크**로 이동합니다.
2. **이메일 링크 템플릿 만들기**를 선택합니다.
3. 링크 템플릿에 이름을 지정합니다.
4. (선택 사항) 링크 템플릿에 대한 세부 정보를 추가하기 위해 설명, 팀 또는 태그를 추가합니다.
5. (선택 사항) 이메일 Campaigns 및 Canvases의 링크에 링크 템플릿을 자동으로 추가하려면 토글을 선택합니다. 이 설정은 새 이메일 또는 기존 이메일에 새 링크를 추가할 때 적용됩니다.

만들 수 있는 링크 템플릿에는 두 가지 유형이 있습니다:

- [URL 앞에 삽입하는 링크 템플릿](#prepend-link-template)
- [URL 뒤에 삽입하는 링크 템플릿](#append-link-template)

링크 템플릿과 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 함께 사용할 때, 일관된 렌더링을 위해 Liquid는 본문 태그 내에서만 추가해야 합니다.

### 앞에 추가: URL 앞에 삽입하는 링크 템플릿 만들기 {#prepend-link-template}

이메일 메시지의 링크 앞에 문자열 또는 URL을 추가하려면 다음을 수행하세요:

1. 새 링크 템플릿을 만듭니다.
2. **템플릿 위치**를 **URL 앞**으로 설정합니다.
3. 항상 URL 앞에 추가될 문자열을 입력합니다.

**템플릿 미리보기**에서 링크 템플릿이 URL 앞에 어떻게 삽입되는지 예시를 확인할 수 있습니다.

![URL 앞에 링크 템플릿을 삽입하는 과정의 템플릿 위치, 앞에 추가할 URL, 템플릿 미리보기 필드.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### 뒤에 추가: URL 뒤에 삽입하는 링크 템플릿 만들기 {#append-link-template}

이메일 메시지의 URL 뒤에 쿼리 파라미터를 추가하려면 다음을 수행하세요:

1. 새 링크 템플릿을 만듭니다.
2. **템플릿 위치**를 **URL 뒤**로 설정합니다.
3. 각 URL 끝에 쿼리 파라미터(`value=example`)를 입력합니다. URL 끝에 여러 파라미터를 추가할 수 있습니다.

![URL 뒤에 링크 템플릿을 삽입하는 과정의 템플릿 위치, 쿼리 파라미터, 템플릿 미리보기 필드.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## 이메일 Campaign에서 링크 템플릿 사용하기 {#using-link-templates-in-email-campaigns}

링크 템플릿을 설정한 후 이메일에 적용할 수 있습니다.

HTML 편집기 또는 드래그 앤 드롭 편집기에서 링크 템플릿을 적용하려면 다음 단계를 따르세요:

{% alert note %}
워크스페이스에서 이메일 링크 템플릿 또는 [링크 별칭 지정]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing)이 활성화된 경우, 업데이트된 HTML 편집기와 드래그 앤 드롭 편집기에서 **링크 관리** 탭에 접근할 수 있습니다.
{% endalert %}

- **업데이트된 HTML 편집기:** **콘텐츠** 탭에서 **링크 관리**를 선택하고, **링크 템플릿 추가**를 선택한 다음, 링크 템플릿을 선택하고 **추가**를 선택합니다.
- **드래그 앤 드롭 편집기:** **콘텐츠** 탭에서 **링크 관리**를 선택하고, **링크 템플릿 추가**를 선택한 다음, 링크 템플릿을 선택하고 **추가**를 선택합니다.

![링크 템플릿 예시 목록이 표시된 드래그 앤 드롭 편집기의 링크 관리 탭.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
링크 템플릿은 일반 텍스트에는 적용되지 않습니다. 따라서 Currents에서 링크 템플릿의 매개변수가 포함되지 않은 클릭이 표시될 수 있으며, 이러한 클릭은 이메일의 일반 텍스트 버전에서 발생한 것일 수 있습니다.
{% endalert %}

**링크 관리** 탭에서 링크 템플릿을 추가하면 각 템플릿이 테이블에 추가 열로 표시됩니다. 이메일 내 기존 링크에 이미 링크 템플릿이 추가되어 있는 경우, 새로 추가된 링크에도 기본적으로 해당 링크 템플릿이 적용됩니다.

{% alert tip %}
메시지에 링크를 포함할 때 URL이 `http://` 또는 `https://`로 시작하는지 확인하세요.
{% endalert %}

## 링크 템플릿 관리 {#managing-link-templates}

링크 템플릿을 [복제]({{site.baseurl}}/user_guide/messaging/templates/managing_templates)할 수도 있습니다. 템플릿 및 크리에이티브 콘텐츠를 만들고 관리하는 방법에 대해 자세히 알아보려면 [템플릿 및 미디어]({{site.baseurl}}/user_guide/messaging/templates)를 참조하세요.

{% alert important %}
링크 템플릿에는 현재 템플릿 보관 기능을 사용할 수 없습니다.
{% endalert %}

## 문제 해결 {#troubleshooting}

### UTM 매개변수 누락 {#missing-utm-parameters}

링크 템플릿은 표준 HTML 주석(`<!-- ... -->`) 내의 링크에는 적용되지 않습니다. Outlook 조건부 주석(예: `<!--[if mso]>`)의 경우, 워크스페이스에서 링크 별칭 지정이 활성화되어 있으면 링크 템플릿이 적용됩니다. 링크 별칭 지정이 활성화되지 않은 워크스페이스에서는 조건부 주석이 여전히 건너뛰어집니다.

### 브라우저에는 UTM 매개변수가 있지만 링크에서 누락되는 경우 {#utm-parameters-present-in-browser-but-missing-from-links}

이메일의 URL 경로가 의도한 전체 경로와 일치하지 않을 때(예: 웹사이트의 전체 URL과 다르거나 단축된 경로) 이런 현상이 발생할 수 있습니다.

- **확인할 사항:** 이메일의 `href`에 페이지의 전체 경로가 포함되어 있는지 확인합니다(리다이렉트에 의존하는 부분 경로만 포함되어 있지 않은지).
- **예상 동작:** 이메일의 경로가 불완전하거나 다른 경우, 웹사이트가 방문자를 올바른 페이지로 리다이렉트하더라도 링크 템플릿의 UTM 매개변수가 해당 링크를 클릭할 때 적용되지 않을 수 있습니다.

예를 들어, 전체 링크가 `https://www.somewebsite.com/women/designer/johnjane`인데 이메일에서 `https://www.somewebsite.com/designer/johnjane`을 사용하는 경우, UTM 매개변수가 이메일 링크에 추가되지 않는 것은 예상된 동작입니다.

### Liquid로 렌더링된 링크에서 UTM 매개변수 누락 {#utm-parameters-missing-from-liquid-rendered-links}

링크 템플릿을 적용할 때 Braze는 각 URL을 파싱하여 매개변수를 추가할 위치를 결정합니다. Liquid 태그가 유효한 URI로 파싱할 수 없는 URL을 렌더링하면 링크 템플릿이 자동으로 건너뛰어집니다. Liquid 출력이 올바른 형식의 URL을 생성하는지 확인하세요. 특정 사용자에 대해 메시지를 미리보기하여 렌더링된 URL이 유효한지 확인하세요. URL의 경로나 쿼리 문자열에 Liquid 변수가 포함된 경우, 출력에 잘못된 문자나 깨진 인코딩이 포함되어 있지 않은지 확인하세요.

### 테스트 발송 시 UTM 값 누락 {#utm-values-missing-in-test-sends}

링크 템플릿을 테스트 발송할 때 {% raw %}`{{${user_id}}}`{% endraw %}는 렌더링되지 않습니다. 대신 Campaign을 복제하고 내부 사용자의 이메일 또는 `external_id`를 타겟으로 설정한 후 Campaign을 실행하여 링크 템플릿의 모든 UTM 매개변수가 올바르게 채워지는지 확인하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

링크 템플릿에 대해 자주 묻는 질문의 답변은 [템플릿 FAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq) 페이지를 확인하세요.