---
nav_title: 접근성
article_title: 접근성
platform: Web
page_order: 22
page_type: reference
description: "이 문서에서는 Braze가 접근성을 지원하는 방법을 설명합니다."

---

# 접근성 {#accessibility}

> 이 문서에서는 Braze가 통합 내에서 접근성을 지원하는 방법에 대한 개요를 제공합니다.

Braze Web SDK는 [웹 콘텐츠 접근성 지침(WCAG 2.1)](https://www.w3.org/TR/WCAG21/)에서 제공하는 표준을 지원합니다. 접근성 표준을 유지하기 위해 모든 새로운 빌드에서 Content Cards 및 인앱 메시지에 대해 [100/100 라이트하우스 점수](https://developer.chrome.com/docs/lighthouse/accessibility/scoring)를 유지하고 있습니다.

## 필수 조건 {#prerequisites}

WCAG 2.1을 만족하는 최소 SDK 버전은 v3.4.0에 가깝습니다. 그러나 주요 이미지 태그 수정을 위해 최소 v6.0.0으로 업그레이드할 것을 권장합니다.

### 주요 접근성 수정 사항 {#notable-accessibility-fixes}

| 버전 | 유형 | 주요 변경 사항 |
|---------|------|-------------|
| **6.0.0** | **주요** | 이미지를 `<img>` 태그로 변경, `imageAltText` 또는 `language` 필드, 일반 UI 접근성 개선 |
| **3.5.0** | 부분 | 스크롤 가능한 텍스트 접근성 개선 |
| **3.4.0** | 수정 | Content Cards `article` 역할 수정 |
| **3.2.0** | 부분 | 버튼에 대한 최소 45x45px 터치 타겟 |
| **3.1.2** | 부분 | 이미지에 대한 기본 대체 텍스트 |
| **2.4.1** | **주요** | 시맨틱 HTML(`h1` 또는 `button`), ARIA 속성, 키보드 탐색, 포커스 관리 |
| **2.0.5** | 부분 | 포커스 관리, 키보드 탐색, 레이블 |
{: .reset-td-br-1, .reset-td-br-2 aria-label="Notable accessibility fixes" }

## 지원되는 접근성 기능 {#supported-accessibility-features}

Content Cards 및 인앱 메시지에 대해 다음 기능을 지원합니다:

- ARIA 역할 및 레이블
- 키보드 탐색 지원
- 포커스 관리
- 스크린 리더 알림
- 이미지에 대한 대체 텍스트 지원

## SDK 통합을 위한 접근성 가이드라인 {#accessibility-guidelines-for-sdk-integrations}

일반 접근성 가이드라인에 대해서는 [Braze에서 접근성 높은 메시지 구축하기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/)를 참조하세요. 이 가이드는 Braze Web SDK를 웹 애플리케이션에 통합할 때 최대 접근성을 위한 팁과 모범 사례를 제공합니다.

### Content Cards

#### 최대 높이 설정 {#setting-a-maximum-height}

Content Cards가 너무 많은 수직 공간을 차지하지 않도록 하고 접근성을 개선하기 위해, 다음 예시와 같이 피드 컨테이너에 최대 높이를 설정할 수 있습니다:

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### 뷰포트 고려사항 {#viewport-considerations}

인라인으로 표시되는 Content Cards의 경우, 다음 예시와 같이 뷰포트 제약을 고려하세요.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### 인앱 메시지 {#in-app-messages}

{% alert warning %}
중요한 정보를 슬라이드 업 인앱 메시지 내에 두지 마세요. 스크린 리더에서 접근할 수 없습니다.
{% endalert %}

### 모바일 고려사항 {#mobile-considerations}

#### 반응형 디자인 {#responsive-design}

SDK에는 반응형 중단점이 포함되어 있습니다. 다음 예시와 같이 커스텀 설정이 다양한 화면 크기에서 올바르게 작동하는지 확인하세요:

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }

  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### 접근성 테스트 {#testing-accessibility}

#### 수동 테스트 체크리스트 {#manual-test-checklist}

다음 작업을 완료하여 접근성을 수동으로 테스트하세요:

- 키보드만 사용하여 Content Cards 및 인앱 메시지를 탐색합니다(Tab, Enter, Space)
- 스크린 리더로 테스트합니다(NVDA, JAWS, VoiceOver)
- 모든 이미지에 대체 텍스트가 있는지 확인합니다
- 색상 대비 비율을 확인합니다(WebAIM Contrast Checker와 같은 도구 사용)
- 터치 기능이 있는 모바일 기기에서 테스트합니다
- 포커스 표시기가 보이는지 확인합니다
- 모달 메시지 포커스 트래핑을 테스트합니다
- 모든 상호작용 요소가 키보드로 접근 가능한지 확인합니다

### 일반적인 접근성 문제 {#common-accessibility-issues}

일반적인 접근성 문제를 피하려면 다음을 수행하세요:

1. **포커스 스타일 유지:** SDK의 포커스 표시기는 키보드 사용자에게 필수적입니다.
2. **비상호작용 요소에만 `display: none` 사용:** 상호작용 요소를 숨기려면 `visibility: hidden` 또는 `opacity: 0`를 사용하세요.
3. **ARIA 속성을 재정의하지 마세요:** SDK는 적절한 ARIA 역할과 레이블을 설정합니다.
4. **`tabindex` 속성을 사용하세요:** 이 속성은 키보드 탐색 순서를 제어합니다.
5. **`overflow: hidden`을 설정하면 스크롤을 제공하세요:** 스크롤 가능한 콘텐츠가 접근 가능하게 유지되는지 확인하세요.
6. **내장된 키보드 핸들러에 간섭하지 마세요:** 기존 키보드 탐색이 작동하는지 확인하세요.