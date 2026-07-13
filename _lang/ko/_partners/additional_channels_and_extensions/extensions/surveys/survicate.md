---
nav_title: Survicate
article_title: Survicate
description: "이 참조 문서에서는 여러 채널과 사용자 여정 전반에 걸쳐 고객 인사이트를 수집, 분석 및 조치할 수 있도록 도와주는 고객 피드백 플랫폼인 Survicate와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)는 여러 채널과 사용자 여정 전반에 걸쳐 고객 인사이트를 수집, 분석 및 조치하는 고객 피드백 플랫폼입니다. [빠른 데모 보기](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_이 통합은 Survicate에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Survicate와 Braze 네이티브 통합을 사용하여 이메일, 인앱, 모바일 또는 웹 설문조사 응답을 Braze 고객 프로필과 동기화할 수 있습니다. 설문조사 응답은 커스텀 속성 또는 이벤트로 Braze 고객 프로필에 자동으로 동기화됩니다. 실시간 피드백 인사이트를 통해 고객 데이터와 함께 피드백을 쉽게 추적 및 분석하고 타겟 후속 조치와 고도로 개인화된 Segments를 생성할 수 있습니다.

## 사용 사례 {#use-cases}

Braze와 Survicate는 함께 다양한 피드백 사용 사례를 지원하여 실행 가능한 사용자 인사이트를 수집하고 고객 경험을 개선하는 데 도움을 줍니다.

- 이메일 받은편지함에서 바로 응답할 수 있는 임베디드 설문조사로 설문조사 응답률을 향상하세요.
- Braze 인앱 메시지를 통해 고객 여정의 중요한 단계에서 인사이트를 수집하세요.
- Survicate에 저장된 피드백을 사용하여 Braze에서 더 스마트한 Segments를 만들 수 있습니다.
- 고객 피드백을 기반으로 후속 Campaign을 자동화하세요.
- 고객 인사이트를 활용하여 개인화된 워크플로를 트리거하세요.
- 자동 번역된 설문조사로 더 많은 오디언스에게 다가갈 수 있습니다.
- 누군가가 설문조사에 응답하면 Braze 연락처 프로필로 이벤트를 보낼 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Survicate 계정 | 이 통합을 활성화하려면 Survicate 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 및 식별자**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합의 주요 기능 {#key-features-of-the-integration}

Survicate와 Braze 통합은 실시간 데이터 동기화를 제공하므로 Survicate 설문조사의 최신 정보를 Braze에서 즉시 사용할 수 있습니다. 설문조사 응답을 기반으로 이 데이터를 사용하여 시의적절하고 개인화된 조치를 취할 수 있습니다.

- **설문조사 응답을 커스텀 사용자 속성으로 Braze에 전송**: 설문조사 응답 데이터로 Braze 고객 프로필을 풍부하게 만들 수 있습니다.
- **Braze에서 커스텀 이벤트 트리거**: 설문조사 답변을 기반으로 한 이벤트를 사용하여 특정 그룹을 타겟팅하거나 후속 Campaign을 시작할 수 있습니다.
- **상세한 Segments 구축**: Survicate 설문조사 데이터를 사용하여 Braze Segments를 생성하고 아웃리치를 더욱 개인화할 수 있습니다.

## 통합 {#integration}

### Survicate에서 설문조사 만들기 {#creating-your-surveys-in-survicate}

#### 이메일에 설문조사를 포함하거나 공유 가능한 링크 설문조사 만들기 {#embed-your-survey-in-an-email-or-create-a-shareable-link-survey}

1.  Survicate에서 **+ Create new survey**를 클릭하고 생성 방법(템플릿, AI 설문조사 만들기 사용, 나만의 질문 추가)과 이메일 또는 공유 가능한 링크 설문조사 유형을 선택합니다:
![설문조사 작성기에서 Braze가 선택된 모습.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2. 설문조사의 Configure 탭에서 응답자를 식별할 도구로 **Braze**를 선택합니다:
![설문조사의 Configure 탭에서 Braze가 선택된 모습.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3. 설문조사를 설정한 후 Share 탭으로 이동하여 이메일 설문조사 전송 방법을 결정합니다. **설문조사를 링크로** 보내거나 **이메일에 첫 번째 질문을 포함시켜** 응답자가 이메일에서 바로 설문조사에 응답할 수 있도록 하는 두 가지 옵션이 있습니다.

{% details 설문조사 링크 옵션 %}

1. 설문조사 링크 복사 버튼에서 설문조사 링크를 가져옵니다:

![설문조사 링크 복사 버튼에서 설문조사 링크를 가져옵니다.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2. Braze 이메일의 CTA 버튼이나 하이퍼링크 뒤에 설문조사 링크를 숨기세요.

![Braze 이메일의 CTA 버튼이나 하이퍼링크 뒤에 설문조사 링크를 숨기세요.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details 이메일 임베드 옵션 %}

이메일 본문에 첫 번째 질문을 바로 표시하여 이메일에서 설문조사를 시작하세요. 그런 다음 응답자는 나머지 설문조사에 참여할 수 있는 랜딩 페이지로 리디렉션됩니다.

1. **Get email code**를 클릭한 다음 **Copy the HTML code**를 클릭합니다:

![이메일 코드 받기]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2. 설문조사에 사용하려는 Braze Campaign으로 이동하여 **Edit email body**를 클릭하고 템플릿에 HTML 블록을 추가합니다:

![HTML 블록 코드 가져오기]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3. 코드를 Survicate 설문조사에서 복사한 코드로 바꿉니다. 그러면 템플릿에 설문조사의 첫 번째 질문이 표시됩니다:

![Survicate 설문조사에서 복사한 코드로 코드를 교체합니다.]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4. 이메일을 예약하고 타겟 그룹을 선택하면 Campaign을 보낼 준비가 완료됩니다.

{% enddetails %}

### Braze 인앱 메시지 설문조사 {#braze-in-app-message-survey}

1. **+ Create new survey**를 클릭하고 생성 방법(템플릿, AI 설문조사 생성 사용, 나만의 질문 추가)을 선택한 다음 플랫폼 내 설문조사 및 Braze In-App Message 설문조사 유형을 선택합니다:

![+ Create new survey를 클릭하고 생성 방법을 선택합니다.]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2. Braze 계정으로 이동한 다음 **메시징** > **Campaigns** > **캠페인 만들기** > **인앱 메시지**로 이동하여 Braze 인앱 메시지 설문조사를 시작하세요:
![Braze 인앱 메시지 설문조사 시작하기]({% image_buster /assets/img/survicate/survicate_9.gif %})

### 기존 편집기를 통해 Braze 인앱 메시지 설문조사 시작하기 {#launch-your-braze-in-app-messenger-survey-via-the-traditional-editor}

1. 기존 편집기를 사용하는 경우 메시지 유형에서 **Custom code**를 선택합니다:

![Custom code를 선택합니다.]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2. 그런 다음 설문조사의 Launch 탭에서 HTML 필드에 코드를 붙여넣습니다:

![설문조사의 Launch 탭에서 HTML 필드에 코드를 붙여넣습니다.]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Braze는 앱의 배경이 차단된 상태에서 인앱 메시지를 기본적으로 iframe에 표시합니다. Survicate 설문조사가 표시되는 동안 앱과 상호 작용할 수 있도록 하려면 다음을 수행해야 합니다:<br><br>

- Survicate-Braze 스니펫에 `opts.useBrazeIframeClipper = true`를 추가하세요.
- Braze를 초기화하는 파일에 `@survicate/braze-bridge-npm` [패키지](https://www.npmjs.com/package/@survicate/braze-bridge-npm)를 설치하고 `initBrazeBridge` 함수를 사용합니다.

[Survicate 개발자 사이트](https://developers.survicate.com/javascript/installation/#braze)에서 샘플 스니펫과 React 구현을 확인할 수 있습니다.
{% endalert %}

{: start="3"}
3. Braze Campaign에서 타겟 및 할당 단계를 설정합니다. 완료되면 Campaign을 시작할 준비가 된 것입니다. 검토 단계에서는 Campaign이 어떻게 보이는지 확인할 수 있습니다. 설문조사는 1단계에서 설명한 대로 Survicate 패널에 지정된 위치에 웹사이트에 표시됩니다.

### Braze 통합 활성화하기 {#enabling-the-braze-integration}

1. Braze 통합을 활성화하려면 **Integrations**로 이동하여 "Braze"를 검색하고 선택합니다.

![Braze 선택]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2. **Connect**를 클릭하여 인증을 설정합니다.

3. Braze 계정 워크스페이스 API 키와 Braze 인스턴스 URL을 입력합니다:

![Braze 계정 워크스페이스 API 키와 Braze 인스턴스 URL을 입력하세요.]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
Survicate를 Braze에 연결하려면 Braze API 키에 `users.track` 권한이 있어야 합니다.
{% endalert %}

### 설문조사를 Braze에 연결하기 {#connecting-your-surveys-to-braze}

이제 Braze 통합이 연결되었으므로 각 설문조사에 대한 개별 설정을 구성할 수 있습니다. 설문조사로 이동하여 **Connect** 탭을 선택한 다음 사용 가능한 통합 목록에서 **Braze**를 선택합니다.

![설문조사로 이동하여 Connect 탭을 선택한 다음 Braze를 선택합니다.]({% image_buster /assets/img/survicate/survicate_14.png %})

### 응답을 커스텀 속성으로 Braze에 보내기 {#sending-responses-to-braze-as-custom-attributes}

설문조사 응답이 커스텀 속성으로 Braze에 전달되도록 설정하여 수집된 데이터로 Braze 고객 프로필을 풍부하게 만들 수 있습니다.

1. Braze 통합의 Settings 탭에서 **Update fields** 섹션을 찾습니다.

![Update fields 섹션을 선택합니다.]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2. 필드를 업데이트할 질문을 선택합니다. Braze 고객 프로필에 데이터가 넘치지 않도록 선택한 질문에만 응답을 보낼 수 있습니다.

![필드를 업데이트할 질문을 선택합니다.]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
순위 및 매트릭스 질문은 이 Braze 통합에서 지원되지 않습니다.
{% endalert %}

{: start="3"}
3. **User** 필드 아래에 업데이트하려는 커스텀 속성의 이름을 추가합니다:

![User 필드 아래에 업데이트하려는 커스텀 속성의 이름을 추가합니다.]({% image_buster /assets/img/survicate/survicate_17.png %})

기본적으로 Survicate는 설문조사 응답의 내용을 속성 값으로 전송합니다. **Edit mapping**을 클릭하여 레이블을 더 짧게 만들거나 데이터 구조에 맞게 값을 수정할 수 있습니다:

![속성 값으로서의 설문조사 응답]({% image_buster /assets/img/survicate/survicate_18.png %})

![Edit mapping을 클릭하여 값을 수정합니다.]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
순고객추천지수의 경우 Survicate는 NPS® 질문에 대한 응답 그룹을 기반으로 매핑된 값을 전송합니다. 그러나 숫자 값을 받으려면 Send Answers as 0-10 values를 켜면 됩니다.
{% endalert %}

![Survicate는 응답 그룹에 따라 매핑된 값을 전송합니다.]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4. **+ Add new**를 클릭하고 동일한 단계를 적용하여 더 많은 질문을 통합에 연결하세요.

![통합에 더 많은 질문 연결하기]({% image_buster /assets/img/survicate/survicate_21.png %})

### Braze 연락처 프로필에 이벤트 보내기 {#sending-events-to-braze-contacts-profiles}

이전 설정과 별도로 응답자가 설문조사 질문에 답할 때마다 Survicate는 Braze에서 `survicate-question-answered`라는 이름의 커스텀 이벤트를 보낼 수 있습니다.
Survicate 패널의 커스텀 속성으로 응답 보내기에서 모든 질문, Update fields 탭에서 선택한 질문 또는 전혀 보내지 않을지 여부를 선택할 수 있습니다:

![모든 질문에 대해 이벤트를 보낼지 여부를 선택할 수 있습니다.]({% image_buster /assets/img/survicate/survicate_22.png %})

이벤트를 보내도록 선택하면 사용자의 프로필에서 Survicate 설문조사에 응답한 횟수와 마지막으로 응답한 시간을 확인할 수 있습니다:

![응답 현황]({% image_buster /assets/img/survicate/survicate_23.png %})

이벤트에는 질문에 대한 답변과 설문조사, 질문 및 응답자에 대한 정보가 포함된 이벤트 속성정보가 포함되어 있습니다. 이 이벤트를 사용하여 Segments를 만들 수 있습니다. 예를 들어 특정 날짜 이후 또는 특정 횟수만큼 설문조사에 응답한 사용자 Segment를 만들 수 있습니다:

![이벤트에는 답변이 포함된 이벤트 속성정보가 포함되어 있습니다.]({% image_buster /assets/img/survicate/survicate_24.png %})

이 데이터는 Braze에서 Campaign을 만들 때도 사용할 수 있습니다.

![이 데이터는 Braze에서 Campaign을 생성할 때도 사용할 수 있습니다.]({% image_buster /assets/img/survicate/survicate_25.png %})

### 통합 테스트 {#test-the-integration}

설문조사가 준비되고 통합 설정이 완료되면 생성한 속성, 태그 또는 새 연락처 설정 옆에 있는 Test Integration 버튼을 클릭하여 Survicate를 종료하지 않고도 테스트할 수 있습니다. Survicate는 Braze 계정에 테스트 연락처(`braze-test@survicate.com`)를 생성합니다. 연락처의 프로필에는 설정에 따라 업데이트된 필드가 포함됩니다.

![Test Integration 버튼을 클릭합니다.]({% image_buster /assets/img/survicate/survicate_26.png %})

Braze에서는 Survicate 더미 연락처의 매핑된 필드에서 샘플 데이터를 볼 수 있습니다:

![Survicate 더미 연락처에서 매핑된 필드의 샘플 데이터]({% image_buster /assets/img/survicate/survicate_27.png %})

### 설문조사 결과 분석하기 {#analyzing-your-survey-results}

Braze 설문조사를 통해 응답을 수집했다면 이제 응답자들이 공유한 피드백과 인사이트를 살펴볼 차례입니다. Survicate를 사용하면 결과, 통계 및 추세를 쉽게 검토하여 추가 조치를 취할 수 있습니다.

### Survicate의 피드백 {#feedback-in-survicate}

설문조사에서 응답 수집이 시작되면 설문조사의 Analyze 탭에서 즉시 응답을 확인할 수 있습니다.

![Analyze 탭의 응답]({% image_buster /assets/img/survicate/survicate_28.png %})

Analyze 탭에는 통계 및 시간 경과에 따른 데이터가 포함된 전체 결과와 각 설문조사 제출을 자세히 살펴볼 수 있는 개별 응답이 표시됩니다.

### Braze의 피드백 {#feedback-in-braze}

설문조사 응답으로 사용자 필드를 업데이트하거나 커스텀 이벤트로 응답을 보내면 실시간으로 동기화된 설문조사 데이터를 확인할 수 있습니다. Braze에서 설문조사에 응답한 특정 연락처로 이동합니다. 연락처의 기본 보기에서 응답 기반 데이터와 이벤트를 모두 볼 수 있습니다.

![실시간으로 동기화된 설문조사 데이터]({% image_buster /assets/img/survicate/survicate_29.png %})