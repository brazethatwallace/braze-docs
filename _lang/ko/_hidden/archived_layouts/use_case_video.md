---
nav_title: 동영상 사용 사례

page_order: 7

#Required
description: "Google 검색 설명입니다. 160자를 초과하는 문자는 잘리므로 간결하게 작성하세요."
page_type: reference
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

# 사용 사례 이름 {#use-case-name}

{% multi_lang_include video.html id="XY5uXoKIvFY" align="right" %}

> 사용 사례 템플릿에 오신 것을 환영합니다! 여기에서 Braze 사용 사례 안내를 작성하는 데 필요한 모든 것을 찾을 수 있습니다. 이 첫 번째 섹션에서는 사용 사례를 몇 문장으로 설명해야 합니다. 예를 들어 "이 사용 사례에서는 푸시, 이메일 등을 사용하여 이탈 중인 사용자를 콘텐츠에 다시 유도하는 방법을 살펴봅니다."와 같은 내용이 될 수 있습니다.
>
> 여기에서 사용 사례 시나리오를 설정합니다. 왜 누군가가 이 페이지를 읽고 싶어할까요? 독자의 흥미를 끌 수 있는 가상의 시나리오를 제시하세요. 예를 들어... "가상의 화장품 회사인 Sally의 회사는 사용자 중 일부가 이메일을 열어보기는 하지만 앱에는 거의 또는 전혀 관심을 보이지 않는다는 사실을 발견했습니다. 사용자들은 아무것도 클릭하지 않지만 이메일은 열어봅니다! Sally는 이 사람들 중 20%를 다시 앱 사용자로 전환하기로 결정했습니다."
>
> 이 사용 사례의 목표는 다음과 같습니다(앞서 언급한 시나리오를 세분화하세요):
> - 목표 1
> - 목표 2
> - 목표 3


## 권장 측정기준 {#suggested-metrics}

측정에 대해 이야기할 시간입니다! Braze 사용자는 Campaign(캠페인)을 어떻게 측정해야 할까요? 어떤 전환 측정기준을 설정해야 할까요? 다음 표에 나열하세요.

| 측정기준 | 설명 | 데이터 유형 |
| ------ | ----------- | --------- |
| 전환 1 | 이것은 전환입니다. "이유" 때문에 측정해야 합니다. | 부울. |
| 전환 2 | 이것은 또 다른 전환입니다. "이유" 때문에 측정해야 합니다. | 부울. |
| 연령 | 이것은 사용자 속성입니다. "이유" 때문에 측정해야 합니다. | 정수. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Suggested Metrics" }

## 이 Campaign/Canvas를 구축하는 방법 {#how-to-build-this-campaigncanvas}

이 부분을 작성할 때 전략과 단계별로 무엇을 해야 하는지 분석하세요. 단계를 다음과 같이 명명하여 명확하게 할 수 있습니다. 단계를 명시적으로 작성하지 마세요(예: 이 버튼 클릭, 저 버튼 클릭). 대신 사용 사례의 목표를 달성하는 단계를 설명하여 안내하세요.

### 1단계: 이탈 사용자를 위한 Canvas 설정(오디언스에 대한 조언) {#step-1-set-up-your-canvas-for-lapsing-users-advise-on-audience}

오디언스에 대해 이야기할 때 Segments나 필터를 사용하는 방법을 알려줄 필요는 없습니다. 대신 오디언스를 이탈 사용자로 좁히고 다른 사람에게 전달되지 않도록 하는 방법과 그 이유를 안내하세요. 예를 들어 "며칠 동안 앱을 사용하지 않은 사용자를 선택하거나, 원하는 경우 이메일을 열지 않은 사용자를 선택하는 등 몇 가지 방법으로 이탈 사용자 범위를 좁힐 수 있습니다. 앱에서 너무 오랫동안 떠나 있어 데이터 포인트를 사용할 가치가 없는 사람을 제외하려면 필터를 적용하세요."


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

사용자가 코드 샘플에서 조정해야 할 매개변수 또는 요소를 정의하세요. 많은 사용자가 그대로 복사하여 붙여넣기만 할 것입니다.

| 변수 | 설명 |
| -------- | ----------- |
| Page Title | 페이지 제목을 원하는 대로 지을 수 있습니다. 이 항목은 필수입니다. |
| My First Heading | 대문자로 작성하는 것을 권장합니다. 이 항목은 선택 사항입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Code Sample" }


### 2단계: 적절한 시간에 메시지 보내기 {#step-2-send-your-message-at-the-right-time}

중요한 경우 메시지를 언제 보낼지에 대해 이야기하세요. 중요하지 않을 수도 있습니다! 적어도 현지 시간으로 발송하는 옵션이 있다는 것을 알려주세요. 또는 이 특정 상황을 API로 트리거하는 방법을 알려주거나, Canvas를 사용하는 경우 이메일을 열고 최소 하루 동안 클릭하지 않는 등의 동작을 기반으로 단계를 트리거하는 것이 더 나은지도 안내하세요.

### 3단계: 메시지 작성하기 {#step-3-building-your-message}

여기에서 모범 사례에 대해 조언할 수 있습니다. 이 작업을 강력히 권장하며, 몇 가지를 나열하는 것만으로도 충분합니다. 이미지도 몇 개 추가하면 좋습니다.

### 4단계: 기타 사항 {#step-4-anything-else}

Canvas에서 대기 단계 등에 대해 이야기하는 것처럼 추가 단계가 필요한 경우 여기와 후속 단계에서 계속 진행하세요. 다만 문서를 너무 길게 만들지 마세요. 독자의 관심을 잃고 싶지 않으니까요.


## 다음 단계 {#next-steps}

축하합니다! 이 튜토리얼, 문제 해결 문서 또는 솔루션을 완료했습니다! 이는 다음을 의미합니다:
1. 알아야 할 내용을 학습했고,
2. 필요한 작업을 완료했으며,
3. 지금 또는 다음에 수행할 준비가 되어 있어야 합니다.

### 관련 문서 {#related-articles}

문서에서 다룬 내용에 대해 더 알고 싶다면 다음을 확인하세요:
- [관련 문서 1](#solution-1): 도움이 되는 이유에 대한 설명.
- [관련 문서 2](#solution-2): 도움이 되는 이유에 대한 설명.
- [관련 문서 3](#solution-3): 도움이 되는 이유에 대한 설명.

### 아직 해결되지 않았나요? {#still-lost}

이 문서가 도움이 되지 않았다면 피드백을 남기거나 [고객지원 티켓]({{site.baseurl}}/braze_support/)을 제출해 주세요!