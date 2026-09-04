---
nav_title: 동영상이 포함된 파트너 페이지

page_order: 4

#Required
description: "Google 검색 설명입니다. 160자를 초과하는 문자는 잘리므로 간결하게 작성하세요."
page_type: partner
tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks


noindex: true
#ATTENTION: remove noindex and this alert from template

---

# [파트너 이름] {#partner-name}

{% multi_lang_include video.html id="XY5uXoKIvFY" align="right" %}

> 파트너 페이지 템플릿에 오신 것을 환영합니다! 여기에서 파트너 페이지를 만드는 데 필요한 모든 것을 찾을 수 있습니다. 첫 번째 섹션에서는 첫 번째 문단에서 파트너를 한두 문장으로 설명해야 합니다. 또한 해당 파트너의 메인 사이트로 연결되는 링크를 포함하세요.

두 번째 문단에서는 Braze와 이 파트너 간의 관계를 탐색하고 설명해야 합니다. 이 문단에서는 Braze와 이 파트너가 어떻게 협력하여 Braze 사용자와 고객 간의 유대를 강화하는지 설명합니다. Braze 사용자가 이 파트너 및 해당 서비스를 통합하거나 활용할 때 발생하는 "상승 효과"에 대해 설명합니다.

## 요구 사항 또는 전제 조건 {#requirements-or-prerequisites}

이 섹션에서는 파트너와 통합하고 서비스를 사용하기 위해 필요한 사항을 다룹니다. 이 정보를 전달하는 가장 좋은 방법은 통합에 추가적인 보안 검사 또는 승인이 필요한지 여부와 같은 비기술적이지만 중요한 "알아야 할" 세부 사항을 설명하는 간단한 안내 단락을 작성하는 것입니다. 그런 다음, 차트를 사용하여 통합의 기술적 요구 사항을 설명해야 합니다.

{% alert important %}
다음 요구 사항은 Braze에서 일반적으로 필요할 수 있는 항목입니다. 아래 차트에 나열된 제목, 출처, 링크 및 문구를 사용하는 것을 권장합니다. 각 요구 사항이 어떤 용도로 사용되는지 알 수 있도록 설명을 적절히 조정하세요.
{% endalert %}

| 요구 사항 | 출처 | 접근 | 설명 |
|---|---|---|---|
| Braze 워크스페이스 REST API 키 | Braze 플랫폼 | **설정** > **앱 설정** 페이지 | 이 설명은 워크스페이스 REST API 키로 무엇을 해야 하는지 알려줍니다. |
| Braze API 엔드포인트 | Braze 플랫폼 | [나열된 엔드포인트]({{site.baseurl}}/api/basics#endpoints)를 확인하거나 [지원 티켓]({{site.baseurl}}/braze_support)을 제출하세요. | 설명 보류 중. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요구 사항 또는 전제 조건" }

## [통합 유형] 통합 {#type-of-integration-integration}

여기에서 통합 과정을 단계별로 나누어 설명합니다. 끝없는 문단을 작성하지 마세요. 이 문서는 마케터와 개발자 모두가 통합을 구축하고 실행하는 데 사용하는 기술 문서입니다. 이 섹션의 유일한 목표는 Braze 사용자가 작업을 완료할 수 있도록 설명적인 문서를 작성하는 것입니다. 섹션 제목의 '통합 유형'이란 이것이 병렬 통합인지, 서버 간 통합인지, 기본값 통합인지를 나타냅니다. 이를 통해 파트너와 통합하는 방법이 여러 가지인 경우 여러 통합 섹션을 만들 수 있습니다.

Currents 통합인 경우 이 페이지는 Currents 섹션에 위치해야 하며, 해당 Currents 위치로 리디렉션하는 관련 내비게이션 페이지를 만들어야 합니다.

### 1단계: 1단계에 대한 간단한 설명 {#step-1-this-is-a-short-description-of-step-one}

필요한 코드를 포함하여 단계를 나누어 설명하세요. 여러 가지 다른 코드 세트를 제공할 수 있으므로 통합 방법을 하나만 제공할 필요는 없습니다.

### 2단계: 이 단계에서는 이미지를 설명합니다 {#step-2-this-step-will-describe-images}

설명서에 이미지를 넣을 수 있으므로, 신중하게 이미지를 추가하는 것을 권장합니다.

### 코드 샘플 {#code-sample}

기술적 개념을 설명하는 경우 여기에 명시하고 코드 샘플을 보여주세요.

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

사용자가 코드 샘플에서 조정해야 할 수 있는 매개변수나 요소를 반드시 정의하세요. 많은 사용자가 그대로 복사하여 붙여넣기할 수 있습니다.

| 변수 | 설명 |
| -------- | ----------- |
| Page Title | 페이지 제목은 원하는 대로 지정할 수 있습니다. 반드시 포함해야 합니다. |
| My First Heading | 대문자로 작성하는 것을 권장합니다. 선택 사항입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="코드 샘플" }


### 3단계: 단계 수 {#step-3-how-many-steps}

통합의 사용 방법을 설명하세요. 특히 메시지 작성기에 Liquid를 삽입하는 과정이 포함되는 경우 자세히 안내하세요.

## 커스터마이제이션 {#customization}

이 섹션은 **선택 사항**입니다. 여기에서 두 파트너 간의 통합을 커스터마이즈하는 구체적인 방법을 설명할 수 있습니다.

## 이 통합 사용하기 {#using-this-integration}

이 섹션에서는 통합을 사용하는 방법을 설명해야 합니다. 통합 후 버튼을 몇 번 눌러야 하는지, 아니면 별도의 작업이 필요 없는지 독자에게 알려주세요.

### 1단계: 1단계에 대한 간단한 설명

일반적인 단계별 안내입니다.

### 코드 샘플

기술적인 개념을 설명하는 경우 여기에 기록하고 코드 샘플을 보여주세요.

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

사용자가 코드 샘플에서 조정해야 할 수 있는 매개변수나 요소를 반드시 정의하세요. 많은 사용자가 그대로 복사하여 붙여넣기만 합니다.

| 변수 | 설명 |
| -------- | ----------- |
| Page Title | 페이지 제목은 원하는 대로 지정할 수 있습니다. 이 항목은 필수입니다. |
| My First Heading | 대문자로 작성하는 것을 권장합니다. 이 항목은 선택 사항입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="코드 샘플" }

## 사용 사례 {#use-cases}

이 섹션은 설명서에서 매우 중요한 부분이 될 수 있습니다. 선택 사항이지만, 통합의 일반적이거나 새로운 사용 사례를 설명하기에 좋은 곳입니다. 이를 통해 파트너십을 홍보하거나 추가 판매할 수 있으며, 맥락과 아이디어를 제공하고 무엇보다 통합의 기능을 시각적으로 보여줄 수 있습니다.