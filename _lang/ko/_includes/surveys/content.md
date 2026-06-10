{% comment %}
  공유 Braze 설문조사 설명서.
  매개변수:
  - channel (필수): "in_app_message" 또는 "landing_page"
{% endcomment %}

{% multi_lang_include surveys/beta_alert.md %}

## 필수 조건 {#prerequisites}

설문조사를 생성하기 전에 다음 조건을 충족해야 합니다:

{% if include.channel == 'in_app_message' %}
- Braze 워크스페이스에서 인앱 메시지에 대한 액세스 권한이 있어야 합니다
- [드래그 앤 드롭 편집기에서 인앱 메시지 생성]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)에 익숙해야 합니다
{% elsif include.channel == 'landing_page' %}
- Braze 워크스페이스에서 랜딩 페이지에 대한 액세스 권한이 있어야 합니다
- [랜딩 페이지 생성]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/)에 익숙해야 합니다
{% else %}
- Braze 워크스페이스에서 랜딩 페이지, 인앱 메시지 또는 둘 다에 대한 액세스 권한이 있어야 합니다
- [랜딩 페이지 생성]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/) 및 [드래그 앤 드롭 편집기에서 인앱 메시지 생성]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)에 익숙해야 합니다
{% endif %}

## 설문조사 생성 {#create-a-survey}

베타 기간 동안 설문조사는 기존 메시지 작성 플로우 내에서 구축됩니다.

{% if include.channel == 'in_app_message' %}
1. Campaign 또는 Canvas에서 [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)를 생성합니다.
2. 메시지 유형으로 **설문조사**를 선택합니다.
{% elsif include.channel == 'landing_page' %}
1. **메시징** > **랜딩 페이지**로 이동합니다.
2. 새 랜딩 페이지를 생성합니다.
3. 메시지 유형으로 **설문조사**를 선택합니다.
{% else %}
1. **메시징** > **랜딩 페이지**로 이동하거나, Campaign 또는 Canvas에서 [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)를 생성합니다.
2. 새 메시지를 생성합니다.
3. 메시지 유형으로 **설문조사**를 선택합니다.
{% endif %}

{% if include.channel == 'in_app_message' %}

## 인앱 메시지 설문조사 작성 {#compose-an-in-app-message-survey}

인앱 메시지 설문조사는 기본적으로 두 개의 페이지로 구성됩니다:

- **페이지 1**: 사용자가 질문에 답변하는 페이지
- **확인 페이지**: 설문조사가 제출되는 페이지

기본적으로 버튼은 **다음 페이지**에 연결되어 있습니다. 이 동작을 변경하려면 **동작** 패널에서 각 버튼을 업데이트합니다.

![인앱 메시지 설문조사 페이지 플로우 및 동작 설정.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## 설문조사 양식 블록 사용 {#use-survey-form-blocks}

공유 스타일링 및 작성 컨트롤에 대해서는 다음을 참조하세요:

{% if include.channel == 'in_app_message' %}
- [인앱 메시지 드래그 앤 드롭 편집기 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [랜딩 페이지 양식 블록]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)
{% else %}
- [인앱 메시지 드래그 앤 드롭 편집기 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [랜딩 페이지 양식 블록]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)
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

### 긴 텍스트 캡처 {#long-text-capture}

긴 텍스트 캡처는 정성적 피드백에 유용합니다.

다음을 구성할 수 있습니다:

- 최소 및 최대 문자 수(최대 1,000자)
- 작성 중 문자 제한 표시 여부
- 텍스트 영역 높이(행)
- 입력 안내 텍스트

베타 기간 동안 긴 텍스트 응답은 보고서 및 내보내기에서 확인할 수 있지만, 고객 프로필 커스텀 속성으로 기록할 수는 없습니다.

![긴 텍스트 캡처 블록 설정.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## 필수 필드 및 속성 구성 {#configure-required-fields-and-attributes}

각 양식 블록에 대해 오른쪽 설정 패널에서 **보고용 식별자**를 입력합니다. 이 식별자는 설문조사 보고서 및 CSV 내보내기에 표시됩니다.

베타 기간 동안:

- 대부분의 설문조사 응답을 고객 프로필 커스텀 속성으로 기록할 수 있습니다.
- 긴 텍스트 응답은 커스텀 속성으로 기록할 수 없습니다.
- 응답을 사용자 속성으로 기록하지 않기로 선택하면, 해당 응답 값으로 사용자를 세분화할 수 없습니다.

![보고용 식별자 및 속성 기록 설정.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## 보고서 및 분석 보기 {#view-reporting-and-analytics}

시작 후 다음에서 결과를 확인합니다:

{% if include.channel == 'in_app_message' %}
- 인앱 메시지 설문조사의 **응답** 탭
{% elsif include.channel == 'landing_page' %}
- 랜딩 페이지 설문조사의 랜딩 페이지 분석 보기
{% else %}
- 인앱 메시지 설문조사의 **응답** 탭
- 랜딩 페이지 설문조사의 랜딩 페이지 분석 보기
{% endif %}

![랜딩 페이지 분석 탭.]({% image_buster /assets/img/surveys/survey-analytics-1.png %})

상위 수준 분석에는 다음이 포함됩니다:

- **전체 응답:** 완료 및 미완료 응답의 총합
- **완료:** 모든 필수 질문을 완료한 사용자
- **부분 완료:** 일부 데이터를 제출했지만 모든 필수 질문을 완료하지 않은 사용자
- **고유 노출 횟수:** 총 페이지 조회 수

{% if include.channel == 'landing_page' %}
{% alert note %}
베타 기간 동안 랜딩 페이지 설문조사는 부분 완료 응답을 추적하지 않습니다.
{% endalert %}
{% endif %}

질문별 응답 분석을 검토하고 데이터를 CSV로 내보낼 수도 있습니다.

### 차트 유형 선택 {#choose-a-chart-type}

라디오 버튼, 드롭다운 및 체크박스 양식 블록의 경우, 설문조사 분석 보기에서 세 가지 차트 유형 중 선택할 수 있습니다. 이를 통해 서드파티 도구로 내보내지 않고도 인사이트를 해석하고 공유할 수 있는 유연성이 높아집니다.

| 차트 유형 | 적합한 용도 |
| --- | --- |
| 막대 차트 | 응답 수와 백분율의 기본 가로 보기입니다. |
| 세로 막대 차트 | 응답 수와 백분율의 세로 보기입니다. 이 차트는 다중 선택 질문이나 답변 옵션이 많은 질문에서 응답을 나란히 비교할 때 사용합니다. |
| 원형 차트 | 응답의 비율 분석입니다. 이 차트는 단일 선택 질문에서 응답이 옵션 전체에 어떻게 분포되어 있는지 확인할 때 사용합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="설문조사 차트 유형" }

각 차트는 응답이 들어올 때 실시간으로 업데이트됩니다. 기본 데이터에 영향을 주지 않고 언제든지 차트 유형을 전환할 수 있습니다.

![막대 차트를 사용한 설문조사 질문별 분석.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## 리타겟 및 트리거 {#retarget-and-trigger}

베타 기간 동안 다음을 수행할 수 있습니다:

- 사용자 속성으로 기록된 설문조사 응답을 기준으로 사용자를 세분화합니다.
- 설문조사 완료 상태를 기준으로 사용자를 세분화합니다.

{% if include.channel == 'in_app_message' %}

![설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- 사용자가 인앱 메시지 Campaign에서 설문조사를 완료하면 Campaigns 및 Canvases를 트리거합니다.

![인앱 메시지 Campaign 설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![랜딩 페이지 설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- 사용자가 랜딩 페이지에서 설문조사를 완료하면 Campaigns 및 Canvases를 트리거합니다.

{% else %}

![설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- 사용자가 랜딩 페이지 또는 인앱 메시지 Campaign에서 설문조사를 완료하면 Campaigns 및 Canvases를 트리거합니다.

![랜딩 페이지 설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![인앱 메시지 Campaign 설문조사 후속 조치를 위한 트리거 설정 및 세분화 필터.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### 제한 사항 {#limitations}

베타 기간 동안 다음과 같은 제한 사항이 있습니다:

- 긴 텍스트 응답을 기준으로 사용자를 세분화할 수 없습니다.
- 기록된 사용자 속성에 의존하지 않는 질문-답변 트리거는 사용할 수 없습니다.