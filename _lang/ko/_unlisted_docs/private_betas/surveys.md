---
nav_title: 설문조사
article_title: Braze 설문조사
description: "인앱 메시지 및 랜딩 페이지에서 설문조사를 생성하고, 응답을 검토하며, 비공개 베타 기간 동안 사용자를 리타겟하는 방법을 알아보세요."
permalink: /braze_surveys/
hidden: true
---

# Braze 설문조사 {#braze-surveys}

> Braze 설문조사는 인앱 메시지와 랜딩 페이지에서 피드백을 수집하여 분석하고 후속 메시징에 활용할 수 있습니다.

{% alert important %}
Braze 설문조사는 비공개 베타 중입니다. 베타에 대한 피드백은 [surveys-feedback@braze.com](mailto:surveys-feedback@braze.com)으로 보내주세요.
{% endalert %}

## 필수 조건 {#prerequisites}

설문조사를 생성하기 전에 다음 사항을 충족해야 합니다:

- Braze 워크스페이스에서 랜딩 페이지, 인앱 메시지 또는 둘 다에 대한 액세스 권한 확보
- [랜딩 페이지 생성](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/)에 대한 숙지
- [드래그 앤 드롭 인앱 메시지 생성](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)에 대한 숙지

## 설문조사 생성 {#create-a-survey}

베타 기간 동안 설문조사는 기존 메시지 작성 플로우 내에서 구축됩니다.

1. **메시징** > **랜딩 페이지**로 이동하거나, Campaign 또는 Canvas에서 [인앱 메시지](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/)를 생성합니다.
2. 새 메시지를 생성합니다.
3. 메시지 유형으로 **설문조사**를 선택합니다.

## 인앱 메시지 설문조사 작성 {#compose-an-in-app-message-survey}

인앱 메시지 설문조사는 기본적으로 두 페이지로 구성됩니다:

- **페이지 1**: 사용자가 질문에 답변하는 페이지
- **확인 페이지**: 설문조사가 제출되는 페이지

기본적으로 버튼은 **다음 페이지**에 연결되어 있습니다. 이 동작을 변경하려면 **동작** 패널에서 각 버튼을 업데이트하세요.

![인앱 메시지 설문조사 페이지 플로우 및 동작 설정.]({% image_buster /assets/unlisted_docs/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

## 설문조사 양식 블록 사용 {#use-survey-form-blocks}

공유 스타일링 및 작성 컨트롤에 대해서는 다음을 참조하세요:

- [인앱 메시지 드래그 앤 드롭 편집기 블록](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)
- [랜딩 페이지 양식 블록](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks)

설문조사에 다음 양식 블록을 추가할 수 있습니다:

- 전화번호 캡처
- 이메일 캡처
- 라디오 버튼 그룹
- 짧은 텍스트 캡처
- 긴 텍스트 캡처
- 드롭다운
- 단일 체크박스
- 체크박스 그룹

### 긴 텍스트 캡처 {#long-text-capture}

긴 텍스트 캡처는 정성적 피드백에 유용합니다.

다음을 구성할 수 있습니다:

- 최소 및 최대 문자 수(최대 1,000자)
- 작성 중 문자 제한 표시 여부
- 텍스트 영역 높이(행)
- 입력 안내 텍스트

베타 기간 동안 긴 텍스트 응답은 보고서 및 내보내기에서 확인할 수 있지만, 고객 프로필 커스텀 속성으로 기록할 수는 없습니다.

![긴 텍스트 캡처 블록 설정.]({% image_buster /assets/unlisted_docs/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## 필수 필드 및 속성 구성 {#configure-required-fields-and-attributes}

각 양식 블록에 대해 오른쪽 설정 패널에서 **보고용 식별자**를 입력합니다. 이 식별자는 설문조사 보고서 및 CSV 내보내기에 표시됩니다.

베타 기간 동안:

- 대부분의 설문조사 응답을 고객 프로필 커스텀 속성으로 기록할 수 있습니다.
- 긴 텍스트 응답은 커스텀 속성으로 기록할 수 없습니다.
- 응답을 사용자 속성으로 기록하지 않기로 선택하면, 해당 응답 값으로 사용자를 세분화할 수 없습니다.

![보고용 식별자 및 속성 기록 설정.]({% image_buster /assets/unlisted_docs/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## 보고서 및 분석 보기 {#view-reporting-and-analytics}

출시 후 다음에서 결과를 검토할 수 있습니다:

- 인앱 메시지 설문조사의 **응답** 탭
- 랜딩 페이지 설문조사의 랜딩 페이지 분석 뷰

![랜딩 페이지 분석 탭.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-1.png %})

상위 수준 분석에는 다음이 포함됩니다:

- **전체 응답:** 완료 및 미완료 응답의 총합
- **완료:** 모든 필수 질문을 완료한 사용자
- **부분 완료:** 일부 데이터를 제출했지만 모든 필수 질문을 완료하지 않은 사용자
- **고유 노출 횟수:** 총 페이지 조회 수

{% alert note %}
랜딩 페이지 설문조사는 베타 기간 동안 부분 완료 응답을 추적하지 않습니다.
{% endalert %}

질문별 응답 분석을 검토하고 데이터를 CSV로 내보낼 수도 있습니다.

![설문조사 분석 개요 및 질문별 분석.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-text.png %})

![설문조사 질문별 분석 막대 차트.]({% image_buster /assets/unlisted_docs/img/surveys/bar-charts-1.png %})

## 리타겟 및 트리거 {#retarget-and-trigger}

베타 기간 동안 다음을 수행할 수 있습니다:

- 사용자 속성으로 기록된 설문조사 응답을 기준으로 사용자를 세분화합니다.
- 설문조사 완료 상태를 기준으로 사용자를 세분화합니다. <br><br>![설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/unlisted_docs/img/surveys/submit-survey-segment.png %})<br><br>
- 사용자가 랜딩 페이지 또는 인앱 메시지 Campaign에서 설문조사를 완료하면 Campaign 및 Canvases를 트리거합니다. <br><br>![랜딩 페이지 설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/unlisted_docs/img/surveys/trigger_landing_page_survey.png %}) <br><br>![인앱 메시지 Campaign 설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/unlisted_docs/img/surveys/interact-campaign-step.png %})

### 제한 사항 {#limitations}

베타 기간 동안 다음과 같은 제한 사항이 있습니다:

- 긴 텍스트 응답을 기준으로 사용자를 세분화할 수 없습니다.
- 기록된 사용자 속성에 의존하지 않는 질문-답변 트리거는 사용할 수 없습니다.