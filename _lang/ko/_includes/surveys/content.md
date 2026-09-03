{% comment %}
  공유 Braze 설문조사 설명서.
  매개변수:
  - channel (필수): "in_app_message" 또는 "landing_page"
{% endcomment %}

설문조사 개요 및 채널 간 공유되는 기능에 대한 자세한 내용은 [설문조사]({{site.baseurl}}/user_guide/messaging/surveys)를 참조하세요.

## 사전 요구 사항 {#prerequisites}

설문조사를 만들기 전에 다음 사항을 확인해야 합니다:

{% if include.channel == 'in_app_message' %}
- Braze 워크스페이스에서 인앱 메시지에 대한 액세스 권한이 있어야 합니다
- [드래그 앤 드롭 편집기에서 인앱 메시지 만들기]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)에 익숙해야 합니다
{% elsif include.channel == 'landing_page' %}
- Braze 워크스페이스에서 랜딩 페이지에 대한 액세스 권한이 있어야 합니다
- [랜딩 페이지 만들기]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)에 익숙해야 합니다
{% else %}
- Braze 워크스페이스에서 랜딩 페이지, 인앱 메시지 또는 둘 다에 대한 액세스 권한이 있어야 합니다
- [랜딩 페이지 만들기]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) 및 [드래그 앤 드롭 편집기에서 인앱 메시지 만들기]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)에 익숙해야 합니다
{% endif %}

## 설문조사 만들기 {#create-a-survey}

설문조사는 기존 메시지 작성 흐름 내에서 만들 수 있습니다.

{% if include.channel == 'in_app_message' %}
1. Campaign 또는 Canvas에서 [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)를 만듭니다.
2. 메시지 유형으로 **설문조사**를 선택합니다.
{% elsif include.channel == 'landing_page' %}
1. **메시징** > **랜딩 페이지**로 이동합니다.
2. 새 랜딩 페이지를 만듭니다.
3. 메시지 유형으로 **설문조사**를 선택합니다.
{% else %}
1. **메시징** > **랜딩 페이지**로 이동하거나, Campaign 또는 Canvas에서 [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)를 만듭니다.
2. 새 메시지를 만듭니다.
3. 메시지 유형으로 **설문조사**를 선택합니다.
{% endif %}

{% if include.channel == 'in_app_message' %}

## 인앱 메시지 설문조사 작성하기 {#compose-an-in-app-message-survey}

인앱 메시지 설문조사는 기본적으로 두 개의 페이지로 구성됩니다.

- **페이지 1**: 사용자가 질문에 답변하는 페이지
- **확인 페이지**: 설문조사가 제출되는 페이지

기본적으로 버튼은 **다음 페이지**에 연결되어 있습니다. 이 동작을 변경하려면 **액션** 패널에서 각 버튼을 업데이트하세요.

![인앱 메시지 설문조사 페이지 흐름 및 액션 설정.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## 설문조사 양식 블록 사용 {#use-survey-form-blocks}

공유 스타일링 및 구성 컨트롤에 대해서는 다음을 참조하세요:

{% if include.channel == 'in_app_message' %}
- [인앱 메시지 드래그 앤 드롭 편집기 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [랜딩 페이지 양식 블록]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- [인앱 메시지 드래그 앤 드롭 편집기 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [랜딩 페이지 양식 블록]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% endif %}

설문조사에 다음 양식 블록을 추가할 수 있습니다:

- 전화번호 캡처
- 이메일 캡처
- 라디오 버튼 그룹
- 짧은 텍스트 캡처
- 긴 텍스트 캡처
- 드롭다운
- 단일 체크박스
- 체크박스 그룹
- 평점 척도
- 순고객추천지수

### 답변 선택지 무작위화 {#randomize-answer-choices}

라디오 버튼 그룹, 체크박스 그룹 및 드롭다운 블록은 무작위 답변 선택지를 지원합니다. **Randomize choice order**를 켜면 설문조사가 로드될 때마다 선택지가 셔플됩니다. 자세한 내용은 [무작위 선택지 순서]({{site.baseurl}}/user_guide/messaging/surveys#randomized-choice-order)를 참조하세요.

### 긴 텍스트 캡처 {#long-text-capture}

긴 텍스트 캡처는 최대 1,000자까지의 정성적 피드백을 수집하는 데 유용합니다. 자세한 내용은 [긴 텍스트 캡처]({{site.baseurl}}/user_guide/messaging/surveys#long-form-text-capture)를 참조하세요.

### 평점 척도 {#rating-scale}

평점 척도(숫자 척도 질문이라고도 함)는 감정, 만족도 또는 추천 가능성을 단일 숫자로 캡처하는 데 유용합니다. 자세한 내용은 [숫자 척도 질문]({{site.baseurl}}/user_guide/messaging/surveys#number-scale-questions)을 참조하세요.

{% if include.channel == 'in_app_message' %}
![매장 경험을 1점부터 5점까지 평가하는 평점 척도.]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![친구에게 제품을 추천할 가능성을 1점부터 10점까지 평가하는 평점 척도.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![친구에게 제품을 추천할 가능성을 1점부터 10점까지 평가하는 평점 척도.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## 필수 필드 및 속성 구성 {#configure-required-fields-and-attributes}

각 양식 블록에 대해 오른쪽 설정 패널에서 **Identifier for Reporting**을 입력합니다. 이 식별자는 설문조사 보고서와 CSV 내보내기에 표시됩니다.

유의 사항:

- 대부분의 설문조사 응답을 고객 프로필 커스텀 속성에 기록할 수 있습니다.
- 긴 텍스트 응답은 커스텀 속성으로 기록할 수 없습니다.
- 응답을 사용자 속성으로 기록하지 않으면 해당 응답 값을 기준으로 사용자를 세분화할 수 없습니다.

![보고용 식별자 및 속성 기록 설정.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## 리포트 및 분석 보기 {#view-reporting-and-analytics}

출시 후 다음에서 결과를 확인하세요:

{% if include.channel == 'in_app_message' %}
- 인앱 메시지 설문조사의 **응답** 탭
{% elsif include.channel == 'landing_page' %}
- 랜딩 페이지 설문조사의 랜딩 페이지 분석 보기
{% else %}
- 인앱 메시지 설문조사의 **응답** 탭
- 랜딩 페이지 설문조사의 랜딩 페이지 분석 보기
{% endif %}

모든 설문조사에 사용할 수 있는 최상위 분석 항목(전체 응답, 완료, 부분 완료, 고유 노출 횟수)의 정의는 [분석]({{site.baseurl}}/user_guide/messaging/surveys#analytics)을 참조하세요.

{% if include.channel == 'landing_page' %}
{% alert note %}
랜딩 페이지 설문조사는 설문조사가 [다단계 양식]({{site.baseurl}}/user_guide/messaging/surveys#multi-step-landing-page-forms)을 사용할 때 부분 완료 응답을 추적합니다.
{% endalert %}
{% endif %}

또한 질문별 응답 분석을 검토하고, 세 가지 차트 유형 중에서 선택하며, 데이터를 CSV로 내보낼 수 있습니다. 자세한 내용은 [차트 유형]({{site.baseurl}}/user_guide/messaging/surveys#chart-types)을 참조하세요.

## 리타겟 및 트리거 {#retarget-and-trigger}

다음과 같은 작업을 수행할 수 있습니다:

- 사용자 속성으로 기록된 설문조사 응답을 기준으로 사용자를 세분화할 수 있습니다.
- 설문조사 완료 상태를 기준으로 사용자를 세분화할 수 있습니다.

{% if include.channel == 'in_app_message' %}

![설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- 사용자가 인앱 메시지 Campaign에서 설문조사를 완료하면 Campaigns 및 Canvases를 트리거할 수 있습니다.

![인앱 메시지 Campaign 설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![랜딩 페이지 설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- 사용자가 랜딩 페이지에서 설문조사를 완료하면 Campaigns 및 Canvases를 트리거할 수 있습니다.

{% else %}

![설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- 사용자가 랜딩 페이지 또는 인앱 메시지 Campaign에서 설문조사를 완료하면 Campaigns 및 Canvases를 트리거할 수 있습니다.

![랜딩 페이지 설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![인앱 메시지 Campaign 설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### 제한 사항 {#limitations}

다음과 같은 제한 사항이 있습니다:

- 장문 텍스트 응답으로는 사용자를 세분화할 수 없습니다.
- 기록된 사용자 속성에 의존하지 않는 질문-응답 트리거링은 사용할 수 없습니다.