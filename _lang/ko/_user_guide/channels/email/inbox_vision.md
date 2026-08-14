---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 7
description: "이 페이지에서는 마케터가 다양한 이메일 클라이언트와 모바일 기기의 관점에서 이메일을 확인할 수 있는 기능인 Inbox Vision을 설정하는 방법을 다룹니다."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision {#inbox-vision}

> Inbox Vision을 사용하면 다양한 이메일 클라이언트와 모바일 기기의 관점에서 이메일을 확인할 수 있습니다. 예를 들어, 다크 모드와 라이트 모드의 차이를 테스트하여 이메일이 의도한 대로 렌더링되는지 확인할 수 있습니다.

{% alert important %}
이메일 콘텐츠가 고객 프로필 데이터와 같은 템플릿 정보에 의존하는 경우 Inbox Vision이 작동하지 않을 수 있습니다. Braze는 이 기능을 위해 이메일을 발송할 때 빈 사용자를 템플릿으로 사용합니다.<br><br>이메일 메시지의 모든 Liquid에 기본값을 추가하세요. 기본값이 없으면 잘못된 긍정 결과를 받거나 테스트가 실패할 수 있습니다.
{% endalert %}

## 고려 사항 {#considerations}

일반적으로 사용자 프로필 정보와 같은 템플릿 정보에 의존하는 이메일 콘텐츠는 Inbox Vision에서 작동하지 않습니다. 이는 Braze가 이 기능을 사용하여 이메일을 보낼 때 빈 사용자를 템플릿으로 사용하기 때문입니다.

Inbox Vision을 실행하기 전에 이메일 메시지의 Liquid에 기본값이나 임의의 값을 추가하면 이 문제를 해결할 수 있습니다. Inbox Vision에서 테스트를 마치면 원래 이메일 메시지가 다시 나타납니다. 값이 제공되지 않으면 미리보기가 정상적으로 렌더링되지 않을 수 있습니다.

회사에는 Inbox Vision으로 미리볼 수 있는 이메일 수에 제한이 있습니다. Inbox Vision의 **이메일 미리보기** 탭에서 이를 모니터링할 수 있습니다.

미리보기를 확인하려면 제목란과 유효한 발신 도메인을 포함하세요. 데스크톱과 모바일 렌더링 차이에 유의하세요. 미리보기를 사용하여 이메일이 의도한 대로 표시되는지 확인하세요.

{% alert note %}
Campaign 미리보기 시 권한 오류가 표시되면 캐시와 쿠키를 지우거나 시크릿 창을 사용해 보세요. 브라우저 확장 프로그램이 미리보기를 차단하는 경우가 있습니다.
{% endalert %}

Inbox Vision에서 이메일 메시지를 테스트하려면:

1. 드래그 앤 드롭 편집기 또는 HTML 이메일 편집기로 이동합니다.
2. 편집기에서 **미리보기 및 테스트**를 선택합니다.
3. **Inbox Vision**을 선택합니다.
4. **Inbox Vision 실행**을 선택합니다. 최대 10분이 소요될 수 있습니다.
5. 그런 다음 타일을 선택하여 미리보기를 더 자세히 확인합니다. 미리보기는 **웹 클라이언트**, **애플리케이션 클라이언트**, **모바일 클라이언트** 섹션으로 그룹화되어 있습니다.

![미리볼 이메일 클라이언트를 선택하는 옵션]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5. **Inbox Vision 실행**을 선택합니다. 완료까지 2분에서 10분 정도 소요될 수 있습니다.

{% alert note %}
Inbox Vision은 [중단 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)이 포함된 이메일 메시지를 지원하지 않습니다. 이러한 이메일은 정적 콘텐츠로 렌더링되기 때문입니다.
{% endalert %}

### 사용자로 미리보기 {#previewing-as-a-user}

임의의 사용자로 미리볼 때 Inbox Vision은 사용자별 설정이나 속성(예: 이름 또는 환경설정)을 저장하지 않습니다. 커스텀 사용자를 선택하면 특정 사용자 데이터를 사용하기 때문에 Inbox Vision 미리보기가 다른 미리보기와 다를 수 있습니다.

## 코드 분석 {#code-analysis}

코드 분석은 잠재적인 HTML 문제를 강조 표시하고, 발생 횟수를 보여주며, 지원되지 않는 HTML 요소를 나타냅니다.

### 코드 분석 정보 보기 {#viewing-code-analysis-information}

이 정보는 **Inbox Vision** 탭에서 <i class="fas fa-list"></i> **목록 보기**를 선택하여 확인할 수 있습니다. 목록 보기는 HTML 이메일 템플릿에서만 사용할 수 있습니다. 드래그 앤 드롭 템플릿의 경우, 대신 미리보기를 사용하여 문제를 해결하세요.

![Inbox Vision 미리보기의 코드 분석 예시.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Braze가 스크린샷을 찍기 전에 이메일이 도착할 때까지 기다리기 때문에, 코드 분석이 특정 클라이언트의 미리보기보다 더 빨리 표시될 수 있습니다.
{% endalert %}

## 스팸 테스트 {#spam-testing}

스팸 테스트는 메일이 스팸으로 필터링될 가능성이 있는지 추정합니다. IronPort, SpamAssassin, Barracuda와 같은 필터와 Gmail, Outlook과 같은 ISP 필터를 대상으로 테스트가 실행되며, 기본적으로 열람이나 클릭을 하지 않는 정적 시드 받은편지함을 사용합니다.

{% alert important %}
받은편지함 배치는 주로 실시간 수신자 인게이지먼트에 의해 결정됩니다. 스팸 테스트 결과는 실제 Campaign에서 확인하는 결과와 다를 수 있습니다.
{% endalert %}

전달 가능성을 보다 명확하게 파악하려면 소규모 실시간 코호트를 대상으로 콘텐츠를 테스트하세요. 높은 열람률과 클릭률이 가장 신뢰할 수 있는 신호입니다. 스팸 테스트는 인게이지먼트 모니터링과 함께 하나의 참고 자료로 활용하세요.

### 스팸 테스트 결과 확인하기 {#viewing-spam-test-results}

스팸 테스트 결과를 확인하려면 다음을 수행하세요.

1. **Inbox Vision** 섹션에서 **Spam Testing** 탭을 선택합니다. **Spam Test Result** 테이블에 스팸 필터 이름, 상태, 유형이 표시됩니다.
2. 결과를 검토하고 이메일 캠페인에 필요한 조정을 수행합니다.
3. **Re-run Test**를 선택하여 스팸 테스트 결과를 다시 로드합니다.

## 접근성 테스트 {#accessibility-testing}

접근성 테스트는 이메일에서 잠재적인 접근성 문제를 강조하고 어떤 요소가 기준을 충족하지 못하는지 보여줍니다. Braze는 W3C에서 개발한 국제적으로 인정받는 표준 세트인 웹 콘텐츠 접근성 지침([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/))의 선별된 항목을 기준으로 콘텐츠를 분석하여 웹 콘텐츠의 접근성을 높입니다.

### 작동 방식 {#how-it-works}

Inbox Vision을 실행하면 Braze가 [WCAG 2.2 AA 규칙 세트](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa)에서 일반적인 접근성 문제(대체 텍스트 누락, 불충분한 색상 대비, 부적절한 제목 구조 등)를 자동으로 검사하고 심각도별로 분류하여 수정 우선순위를 정하는 데 도움을 줍니다. 대체 텍스트가 있더라도 [표시 방식]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text)은 Braze가 아닌 수신자의 이메일 클라이언트에 의해 제어됩니다.

{% alert important %}
접근성 테스트는 [유럽 접근성법](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers) 등 규정 또는 법률에 대한 고객의 준수 노력을 지원하는 데 사용될 수 있습니다. 그러나 고객은 접근성 테스트 사용이 고객의 준수 의무를 충족하는지 여부에 대해 Braze가 어떠한 진술이나 보증도 하지 않으며, 이와 관련된 모든 책임을 부인한다는 점을 인정합니다.
{% endalert %}

### 접근성 테스트 결과 보기 {#viewing-accessibility-testing-results}

접근성 테스트는 **접근성 테스트** 탭에서 각 규칙에 대해 통과, 실패 또는 검토 필요로 결과를 생성합니다. Braze는 WCAG의 네 가지 원칙인 POUR(인식 가능, 운용 가능, 이해 가능, 견고함)를 사용하여 각 규칙을 분류합니다.

#### POUR 카테고리 {#pour-categories}

Inbox Vision은 네 가지 기본 [POUR 원칙](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility)인 인식 가능(Perceivable), 운용 가능(Operable), 이해 가능(Understandable), 견고함(Robust)에 따라 문제를 분류합니다.

| 원칙 | 정의 |
| --- | --- |
| 인식 가능(Perceivable) | 정보와 사용자 인터페이스 구성 요소는 사용자가 인식할 수 있는 방식으로 제공되어야 합니다.<br><br>사용자는 제공되는 정보를 인식할 수 있어야 합니다(모든 감각에 보이지 않아서는 안 됩니다). |
| 운용 가능(Operable) | 사용자 인터페이스 구성 요소와 내비게이션은 운용 가능해야 합니다.<br><br>사용자는 인터페이스를 조작할 수 있어야 합니다(사용자가 수행할 수 없는 상호작용을 인터페이스가 요구해서는 안 됩니다). |
| 이해 가능(Understandable) | 정보와 사용자 인터페이스의 운용은 이해할 수 있어야 합니다.<br><br>사용자는 정보와 사용자 인터페이스의 운용을 이해할 수 있어야 합니다(콘텐츠나 운용이 사용자의 이해 범위를 넘어서는 안 됩니다). |
| 견고함(Robust) | 콘텐츠는 보조 기술을 포함한 다양한 사용자 에이전트에서 안정적으로 해석될 수 있을 만큼 견고해야 합니다.<br><br>기술이 발전함에 따라 사용자는 콘텐츠에 접근할 수 있어야 합니다(기술과 사용자 에이전트가 진화하더라도 콘텐츠는 접근 가능한 상태를 유지해야 합니다). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="POUR 카테고리" }

#### 심각도 수준 {#severity-levels}

Inbox Vision은 접근성 문제를 심각도별로 분류하여 수정 우선순위를 정하는 데 도움을 줍니다.

| 상태 | 정의 |
| --- | --- |
| 심각(Critical) | 장애가 있는 사용자의 콘텐츠 또는 기능 접근을 차단할 수 있는 문제입니다. 가장 심각한 수준이며 우선적으로 수정해야 합니다. |
| 중대(Serious) | 상당한 장벽을 유발할 수 있지만 접근을 완전히 차단하지는 않을 수 있는 문제입니다. 신속하게 해결해야 합니다. |
| 보통(Moderate) | 장애가 있는 사용자에게 어느 정도 어려움을 줄 수 있지만 접근을 완전히 차단할 가능성은 낮은 문제입니다. |
| 경미(Minor) | 접근성에 비교적 낮은 영향을 미치며 약간의 불편만 초래할 수 있는 문제입니다. |
| 검토 필요(Needs review) | 문제가 있는지 여부를 감지할 수 없습니다. 텍스트가 배경 이미지 위에 배치되어 대비율을 판단할 수 없는 경우에 발생할 수 있습니다. 자동으로 판단할 수 없으므로 수동으로 검토해야 합니다. |
| 통과(Passed) | WCAG A, AA 또는 접근성 모범 사례를 통과했습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="심각도 수준" }

{% alert important %}
드래그 앤 드롭 편집기는 문서 `<title>` 요소 설정을 지원하지 않으므로 접근성 스캐너는 항상 이 검사에서 실패합니다.<br><br>이 제한 사항은 향후 개선을 위해 추적되고 있습니다. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="the drag-and-drop editor document title limitation in Inbox Vision" %}
{% endalert %}

### 자동화된 접근성 테스트 이해하기 {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

## 모범 사례 {#best-practices}

### 이메일 구독자 목록 검토 {#review-your-email-subscriber-list}

[이메일 인사이트 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-insights-dashboard)를 참조하여 구독자가 가장 많이 사용하는 기기 유형과 이메일 서비스 공급자를 확인하세요.

브라우저, 기기 모델 등 더 세부적인 정보가 필요한 경우, [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) 데이터 또는 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)를 활용하여 사용자의 최근 이메일 인게이지먼트에 대한 상세 정보를 확인할 수 있습니다.

### 의미 있는 미리보기와 영향을 받는 미리보기 선택 {#select-meaningful-previews-and-impacted-previews}

비즈니스가 주로 미국에 기반을 두고 있다면, GMX.de와 같은 해외 미리보기처럼 소수의 사용자만 사용하는 특정 미리보기가 있을 수 있습니다. 구독자 영향이 큰 받은편지함을 우선적으로 최적화하고, 미리보기를 영향력이 높은 받은편지함에 활용하는 것을 권장합니다.

특정 미리보기에 영향을 미치는 수정을 할 때는, 사용하지 않는 미리보기가 소모되지 않도록 영향을 받는 미리보기만 선택하세요.

### 최종 이메일 버전에서 Inbox Vision 실행 {#run-inbox-vision-on-the-final-email-version}

이메일 메시지가 프로덕션 준비가 완료되었거나 거의 완료된 상태에서 Inbox Vision을 실행하는 것을 권장합니다. 이렇게 하면 이메일이 최종 확정되어 사용자에게 발송될 준비가 되기 전에 여러 번 수정을 거치므로, 생성되는 미리보기 수를 줄일 수 있습니다.

단일 편집이나 변경을 할 때마다 Inbox Vision을 실행하면 미리보기가 빠르게 소모될 수 있습니다. 먼저 이메일에 필요한 모든 변경 사항을 적용한 후 Inbox Vision을 실행하여 모든 변경 사항이 다양한 환경에서 이메일 렌더링에 어떤 영향을 미치는지 미리보기하는 것을 권장합니다.

Braze는 실제 이메일 클라이언트를 통해 테스트를 실행하며 렌더링이 정확하도록 노력합니다. Braze는 일반적인 업계 및 전문가 데이터를 기반으로 상위 20개 미리보기를 기본값으로 설정하며, 이는 사용자가 이메일에 참여하는 대부분의 환경을 포함합니다. 데이터 분석 결과 다른 더 인기 있는 미리보기가 있다면, Inbox Vision을 실행할 때마다 기본 미리보기 세트를 정의할 수 있습니다.

특정 클라이언트에서 지속적으로 문제가 발생하는 경우, [지원 티켓]({{site.baseurl}}/braze_support)을 제출하세요.

### 테스트 정확도와 실제 받은편지함 비교 {#test-accuracy-versus-live-inboxes}

발송된 메시지는 편집기 미리보기와 다르게 보일 수 있습니다. 이메일 서비스 공급자마다 동일한 HTML을 다르게 해석하기 때문입니다. 발송된 HTML 사본을 다운로드하여 비교하고, 클라이언트가 `<style>` 블록을 제거하는 경우 CSS 인라이닝을 사용하세요.

#### 빈 이메일 본문 {#blank-email-bodies}

수신자가 발신자 이름이나 제목란은 볼 수 있지만 이메일 본문이 비어 있다고 보고하는 경우:

1. 영향을 받는 이메일 클라이언트를 확인합니다.
2. Inbox Vision을 사용하여 해당 클라이언트에서 배리언트를 테스트하고 HTML 또는 CSS 호환성 문제를 식별합니다.
3. 클라이언트가 `<style>` 블록을 제거하는 경우, 영향을 받는 HTML 요소에 `style` 속성을 추가합니다. 인라이닝 동작과 제한 사항에 대한 자세한 내용은 [CSS 인라이닝]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline)을 참조하세요. Gmail에서는 CSS가 너무 많으면 전체 `<style>` 블록이 삭제될 수 있으며, 이는 빈 이메일 본문의 일반적인 원인입니다.
4. HTML 편집기에서 **Sending Info** > **Advanced** 아래의 **Enable inline CSS**를 켜서 전체 메시지에 대한 스타일시트 규칙을 인라인할 수도 있습니다. 이 옵션은 편집기에서 이미 인라인 처리되는 드래그 앤 드롭 이메일에는 사용할 수 없습니다.
5. 향후 Campaign을 발송하기 전에 Inbox Vision에서 다시 테스트합니다.