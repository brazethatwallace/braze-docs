---
nav_title: Surveys
article_title: 설문조사
page_order: 9
page_type: reference
channel:
  - landing pages
  - in-app messages
description: "Braze 설문조사를 통해 랜딩 페이지와 인앱 메시지에서 퍼스트파티 피드백을 수집하는 방법을 알아보세요. 분석, 폼 블록, Currents 내보내기를 포함합니다."
---

# 설문조사 {#surveys}

> Braze 설문조사를 사용하면 Braze 대시보드를 벗어나지 않고도 사용자로부터 직접 퍼스트파티 피드백을 수집하고, 이를 후속 메시징에 활용할 수 있습니다. 설문조사를 통해 사용자 감정을 파악하고, 선호도를 수집하며, 수집된 응답을 기반으로 세그먼트와 트리거를 구축하세요.


## 채널 가용성 {#channel-availability}

설문조사는 두 가지 채널에서 사용할 수 있습니다. 각 채널 페이지에서는 채널별 생성 흐름, 구성, 리포팅 위치를 다루며, 이 페이지에서는 두 채널 모두에 적용되는 개념과 기능을 다룹니다.

| 채널 | 설문조사 작성 위치 |
| --- | --- |
| 랜딩 페이지 | [랜딩 페이지 설문조사]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| 인앱 메시지 | [인앱 메시지 설문조사]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="설문조사 채널 가용성" }

## 설문조사 페이지 {#surveys-page}

**메시징** > **설문조사**로 이동하면 랜딩 페이지, Campaigns, Canvases에 걸친 설문조사를 한곳에서 확인할 수 있습니다. 채널 전반의 설문조사 성과를 검토하기 위한 진입점으로 활용하세요.

{% alert note %}
**메시징** 아래에 **설문조사**가 보이지 않는 경우, Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 분석 {#analytics}

모든 설문조사 질문 유형에는 향상된 리포팅이 기본으로 포함되어 있어, 세그먼트를 구축하거나 별도의 도구로 내보내지 않고도 응답 데이터를 한눈에 확인할 수 있습니다.

상위 수준 분석에는 다음이 포함됩니다:

- **전체 응답:** 완료 및 미완료 응답의 총합
- **완료됨:** 모든 필수 질문을 완료한 사용자
- **부분 완료:** 일부 데이터를 제출했으나 모든 필수 질문을 완료하지 않은 사용자
- **고유 노출 횟수:** 총 페이지 조회 수

![순고객추천지수 분석과 함께 추천자, 수동자, 비추천자 비율 및 점수 분포 가로 막대 차트를 보여주는 설문조사 응답 페이지.]({% image_buster /assets/img/surveys/survey_responses.png %})

### 차트 유형 {#chart-types}

라디오 버튼, 드롭다운, 체크박스 폼 블록의 경우 설문조사 분석 보기에서 세 가지 차트 유형 중 선택할 수 있습니다. 이를 통해 서드파티 도구로 내보내지 않고도 인사이트를 더 유연하게 해석하고 공유할 수 있습니다.

| 차트 유형 | 적합한 용도 |
| --- | --- |
| **막대 차트** | 응답 수와 비율의 기본 가로 보기입니다. |
| **세로 막대 차트** | 응답 수와 비율의 세로 보기입니다. 복수 선택 질문이나 답변 옵션이 많은 질문에서 응답을 나란히 비교할 때 사용하세요. |
| **원형 차트** | 응답의 비례 분포를 보여줍니다. 단일 선택 질문에서 옵션 간 응답 분포를 확인하고 싶을 때 사용하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="설문조사 차트 유형" }

각 차트는 응답이 들어오는 대로 실시간 데이터를 표시합니다. 기본 데이터에 영향을 주지 않고 언제든지 차트 유형을 전환할 수 있습니다.

![막대 차트를 사용한 설문조사 질문별 분석.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## 다단계 랜딩 페이지 폼 {#multi-step-landing-page-forms}

여러 개의 독립적인 랜딩 페이지를 만들어 수동으로 연결하는 대신, 자동으로 연결되는 여러 단계가 포함된 하나의 랜딩 페이지로 설문조사를 구축할 수 있습니다. 예를 들어, 각 설문조사 질문에 대해 별도의 단계를 정의하고 마지막에 확인 단계를 추가할 수 있습니다.

이 기능은 랜딩 페이지 채널에만 해당됩니다. 인앱 메시지 설문조사도 단계 간 이동을 위한 페이지 관리자를 지원합니다. 자세한 내용은 [인앱 메시지 설문조사 구성]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey)을 참조하세요.

![다단계 폼 미리보기와 단계 목록 및 잠긴 확인 단계가 있는 폼 속성 패널을 보여주는 랜딩 페이지 에디터.]({% image_buster /assets/img/surveys/multi_step.png %})

## 질문 및 폼 블록 {#question-and-form-blocks}

랜딩 페이지와 인앱 메시지는 설문조사에서도 라디오 버튼 그룹, 체크박스, 체크박스 그룹, 드롭다운, 전화번호 수집, 이메일 수집, 짧은 텍스트 수집 등 모든 표준 폼 블록을 지원합니다. 이 섹션에서는 설문조사 전용 리포팅이 내장된 세 가지 폼 블록인 순고객추천지수, 숫자 척도, 장문 텍스트를 집중적으로 다룹니다.

{% tabs local %}
{% tab 순고객추천지수 %}
### 독립형 순고객추천지수 블록 {#standalone-nps-block}

**순고객추천지수** 블록은 **평점**(숫자 척도) 블록과 별개의 폼 블록이며, 평점 블록 내의 설정 옵션이 아닙니다. 설문조사에 추가하면 표준 순고객추천지수 질문(0~10)을 묻고 해당 사용 사례에 맞게 설계된 리포팅을 받을 수 있습니다.

**순고객추천지수** 블록은 동일한 목적으로 사용되는 일반 평점 질문보다 더 나은 대시보드 리포팅을 제공합니다. 번호별 응답의 단순 집계 대신, Braze가 자동으로 응답을 추천자(9~10), 수동자(7~8), 비추천자(0~6)로 그룹화하고 해당 세그먼트와 결과 순고객추천지수 점수를 설문조사 분석 보기에서 직접 표시합니다.

Currents는 **설문조사 응답** 이벤트에서 숫자 점수(및 추가된 경우 자유 텍스트 피드백 필드)를 내보냅니다. 추천자, 수동자, 비추천자 세그먼트는 별도의 Currents 필드가 아닙니다.

![모바일 순고객추천지수 설문조사와 추천자, 수동자, 비추천자 분류 및 응답 분포 차트가 포함된 설문조사 응답 대시보드.]({% image_buster /assets/img/surveys/survey_and_chart.png %})
{% endtab %}

{% tab 숫자 척도 %}
### 숫자 척도 질문 {#number-scale-questions}

채널 페이지에서는 평점 척도라고도 합니다. 두 용어 모두 동일한 **평점** 폼 블록을 가리킵니다. 1~5, 1~10, 또는 0~10 숫자 척도 질문을 사용하여 간단한 만족도 평점부터 추천 의향 점수까지 다양한 설문조사 및 리포팅 요구에 맞출 수 있습니다. 채널별 구성 스크린샷은 [랜딩 페이지 설문조사]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) 또는 [인앱 메시지 설문조사]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale) 페이지의 평점 척도 섹션을 참조하세요.

평점을 설문조사 응답으로 수집하거나, 정수 커스텀 속성으로 기록하거나, 또는 두 가지 모두 수행할 수 있습니다. 숫자 척도 질문을 [장문 텍스트 수집](#long-form-text-capture) 블록과 결합하면 동일한 설문조사에서 숫자 점수와 함께 정성적 피드백을 수집할 수 있습니다.

![1~5 평점 질문이 선택되고 오른쪽에 평점 속성 패널이 열린 랜딩 페이지 설문조사 에디터.]({% image_buster /assets/img/surveys/rating_block.png %})
{% endtab %}

{% tab 장문 텍스트 %}
### 장문 텍스트 수집 {#long-form-text-capture}

장문 텍스트 수집은 정성적 피드백에 유용합니다. 최소 및 최대 글자 수(최대 1,000자), 작성 시 글자 제한 표시 여부, 텍스트 영역 높이, 입력 안내 텍스트를 설정할 수 있습니다.

![장문 텍스트 수집 블록 설정.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

장문 텍스트 응답은 리포팅 및 내보내기에서 확인할 수 있지만, 고객 프로필 커스텀 속성으로 기록할 수는 없습니다. 따라서 장문 응답 값으로 직접 사용자를 세분화할 수 없습니다. 자세한 내용은 각 채널 페이지의 [제한 사항]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations)을 참조하세요.

Currents에서 장문 응답은 `answer_type = 'free_form_text'`를 사용하며, 텍스트는 `answer_long_string`에 포함됩니다.
{% endtab %}
{% endtabs %}

## 선택지 순서 무작위화 {#randomized-choice-order}

라디오 버튼 그룹, 체크박스 그룹, 드롭다운 블록은 무작위 답변 선택지를 지원합니다. **선택지 순서 무작위화**를 켜면 설문조사가 로드될 때마다 선택지가 섞여, 동일한 첫 번째 옵션이 응답을 왜곡할 수 있는 순서 편향을 줄일 수 있습니다.

무작위화는 각 설문조사 응답자에 대한 표시 순서만 변경합니다. 리포팅 레이블과 값은 설정한 선택지에 매핑된 상태로 유지되므로, 특정 사용자가 본 순서에 관계없이 분석, CSV 내보내기, 세분화에서 동일한 응답 데이터를 사용합니다.

## 설문조사 템플릿 {#survey-templates}

랜딩 페이지 또는 인앱 메시지 템플릿 라이브러리에서 설문조사를 템플릿으로 저장하면, 매번 동일한 질문과 폼 블록을 다시 만들지 않고 템플릿에서 시작할 수 있습니다. 워크스페이스에서 설문조사 템플릿이 활성화되어 있으면, 라이브러리에서 **설문조사**로 필터링하여 Campaigns, Canvases, 랜딩 페이지 전반에서 저장된 설문조사 구조를 찾아 재사용할 수 있습니다.

## 설문조사 응답 이벤트 {#survey-response-events}

설문조사 응답은 [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)로 전달되어 데이터 웨어하우스 또는 서드파티 BI 도구로 설문조사 데이터를 내보낼 수 있습니다. 이를 통해 다른 인게이지먼트 데이터와 조인하고, 대시보드 기본 분석을 넘어서는 커스텀 리포팅을 위한 다운스트림 분석이 가능합니다.

Braze는 **설문조사 응답** 이벤트(`users.messages.survey.Response`)를 통해 개별 설문조사 답변을 Currents로 내보냅니다. 각 이벤트는 한 응답자가 하나의 설문조사 질문에 대해 제출한 답변을 나타냅니다. 전체 필드 레퍼런스는 Currents 이벤트 용어집의 [설문조사 응답 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events)를 참조하세요.

## 랜딩 페이지 인게이지먼트 퍼널 {#landing-page-engagement-funnel}

랜딩 페이지 설문조사는 페이지 조회 및 추적된 클릭에 대해 **랜딩 페이지 노출** 및 **랜딩 페이지 클릭** 이벤트도 생성합니다. 랜딩 페이지 설문조사를 완료하면 **설문조사 응답** 이벤트가 기록됩니다. 표준(비설문조사) 랜딩 페이지 폼에 해당하는 일반적인 **랜딩 페이지 폼 제출** 이벤트는 발생하지 않습니다. 이러한 이벤트의 전체 필드 레퍼런스는 [Currents 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)을 참조하세요.

## 관련 문서 {#related-articles}

- [랜딩 페이지 설문조사]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys): 랜딩 페이지 채널의 생성 흐름, 구성, 리포팅
- [인앱 메시지 설문조사]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys): 인앱 메시지 채널의 생성 흐름, 구성, 리포팅
- [드래그 앤 드롭 편집기 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks): 설문조사에 추가할 수 있는 폼 블록의 전체 레퍼런스
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents): 데이터 웨어하우스 또는 BI 도구로의 데이터 내보내기 설정