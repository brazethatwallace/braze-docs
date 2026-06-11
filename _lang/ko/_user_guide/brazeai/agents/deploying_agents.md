---
nav_title: 에이전트 배포
article_title: 커스텀 에이전트 배포
description: "에이전트를 생성한 후 Braze에서 커스텀 에이전트를 사용하는 방법을 알아보세요."
alias: /deploying-agents/
page_order: 2
---

# 커스텀 에이전트 배포 {#deploy-custom-agents}

> 에이전트를 생성한 후 캔버스 단계 또는 카탈로그 필드에서 커스텀 에이전트를 사용하는 방법을 알아보세요. 소개는 [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/)를 참조하세요.

## Canvas의 에이전트 {#agents-in-canvas}

에이전트를 여정의 단계로 사용하여 메시지를 개인화하거나 실시간으로 의사 결정을 안내할 수 있습니다. 자세한 설정 단계는 [에이전트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/)를 참조하세요.

### 활용 사례 {#use-cases}

| 활용 사례 | 설명 |
| --- | --- |
| 리드 스코어링 및 자격 평가 | 에이전트 단계를 사용하여 유입되는 리드를 척도(예: 1-10)로 평가합니다. 기준 점수를 초과하는 사용자를 육성 경로로 라우팅하고, 적합하지 않은 리드는 제외합니다. |
| 동적 메시지 개인화 | 에이전트가 사용자 속성이나 최근 동작을 기반으로 제목란, 제품 추천 또는 메시지 문구를 생성하도록 합니다. 응답은 메시지 단계에 직접 삽입할 수 있습니다. |
| 고객 피드백 처리 | 고객 의견을 에이전트에 전달하여 감정을 분석하고 공감하는 후속 메시지를 생성합니다. 고가치 사용자의 경우 에이전트가 응답을 에스컬레이션하거나 특전을 포함할 수 있습니다. |
| 지능형 라우팅 | 에이전트 출력(부울 또는 숫자)을 사용하여 사용자를 서로 다른 Canvas 경로로 분할합니다. 예를 들어, 사용자를 "위험" 또는 "건강"으로 분류하고 메시징 주기를 그에 맞게 조정합니다. |
| 설문조사 또는 응답 해석 | 에이전트가 개방형 설문조사 응답이나 자유 텍스트 필드를 구문 분석하여 다운스트림 경로를 유도하는 구조화된 값(예: 의도 또는 필요 분류)을 반환하도록 합니다. |
| 다단계 추론 | 에이전트가 컨텍스트 필드를 결합하고 여러 사용자 속성을 기반으로 다음 최선의 동작(이메일, SMS 또는 담당자 연결)을 추천하는 등 복잡한 결정을 내리도록 구성합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="활용 사례" }

## 카탈로그의 에이전트 {#agents-in-catalogs}

에이전트를 카탈로그 필드에 적용하여 각 행의 값을 자동으로 생성하거나 계산할 수 있습니다. 에이전트는 향후 카탈로그에 추가되는 새로운 행에서도 실행됩니다.

### 활용 사례

| 활용 사례 | 설명 |
| --- | --- |
| 제품 설명 생성 | 새로운 카탈로그 항목에 대한 짧은 마케팅 문구를 자동으로 생성합니다. 예를 들어, 이름, 카테고리, 기능 등 구조화된 제품 데이터에서 매력적인 설명을 생성합니다. |
| 제품 속성 보강 | 제품 이름과 세부 정보를 기반으로 색상 계열, 스타일 또는 시즌 등 누락된 값을 채웁니다. 예를 들어, 제품 이름이 "Laguna Polarized Sunglasses"인 경우 에이전트가 스타일을 "스포츠"로, 색상 계열을 "블루"로 지정할 수 있습니다. |
| 파생 필드 계산 | 기존 필드를 사용하여 속성 기반의 "적합 점수"나 판매 및 리뷰 수에서 파생된 "인기 태그" 등 새로운 데이터를 생성합니다. |
| 항목 분류 또는 태그 지정 | 개인화 모델이 제품을 더 효과적으로 세분화할 수 있도록 추천 로직용 태그를 할당합니다. 예를 들어, 제품에 "아웃도어", "페스티벌 준비 완료" 또는 "프리미엄" 태그를 지정합니다. |
| 콘텐츠 현지화 | 글로벌 Campaign을 위해 카탈로그 텍스트를 다른 언어로 번역하거나, 지역별 채널에 맞게 톤과 길이를 조정합니다. 예를 들어, "Classic Clubmaster Sunglasses"를 스페인어로 "Gafas de sol Classic Clubmaster"로 번역하거나, SMS Campaign을 위해 설명을 단축합니다. |
| 리뷰 또는 피드백 요약 | 감정이나 피드백을 새로운 필드로 요약합니다. 예를 들어, 긍정적, 중립적 또는 부정적 감정 점수를 할당하거나 "대부분의 고객이 좋은 핏을 언급하지만 느린 배송을 지적합니다."와 같은 짧은 텍스트 요약을 생성합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="활용 사례" }

### 단계 {#steps}

![카탈로그 필드의 에이전트 단계.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

카탈로그 필드에 에이전트를 추가하려면:

1. 카탈로그에서 새 필드를 추가합니다.
2. **Apply AI agent**를 선택합니다.
3. 이 필드에 에이전트를 할당합니다.
4. 입력으로 전달할 열을 선택합니다. 선택하지 않으면 에이전트가 카탈로그의 모든 열에 접근할 수 있습니다.
5. 카탈로그 행이 업데이트될 때 에이전트가 필드를 재계산할지 결정합니다. 이 옵션을 선택하지 않으면 에이전트는 행당 한 번만 실행됩니다.
6. **Add fields**를 선택하여 에이전트를 배포하고 비용 추정치를 검토합니다. **Cost estimation** 모달은 이 카탈로그에서 에이전트가 실행될 횟수를 보여주며, 대략 총 행 수와 같습니다. 계속하려면 **Confirm**을 선택합니다.

### 카탈로그 에이전트 실행 방식 {#how-catalog-agents-run}

시작 후 에이전트는 각 행을 실행하고 평가하며, 선택된 열을 컨텍스트에 포함시켜 출력을 생성합니다. 에이전트를 배포한 후 추가된 모든 새 행에서 에이전트가 실행됩니다. **Recalculate when catalog rows update**를 선택한 경우, 기존 소스 필드가 변경되면 이 필드의 모든 값이 업데이트됩니다.

에이전트를 사용하는 카탈로그의 필드를 새로고침하고 편집할 수 있습니다. 열에서 에이전트를 제거하려면 **Apply AI agent**를 선택 해제합니다. 이렇게 하면 열이 비에이전트 열로 되돌아가며, 필드는 에이전트가 카탈로그에서 마지막으로 실행했을 때 적용한 최신 값을 유지합니다.

카탈로그에서 순환 참조는 지원되지 않으며, 다음 시나리오는 발생할 수 없습니다:

- 에이전트 열 1이 에이전트 열 2를 입력으로 사용
- 에이전트 열 2가 에이전트 열 1을 입력으로 사용

![카탈로그 필드에 대해 "Apply AI agent"를 선택하는 옵션.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
카탈로그 에이전트는 행당 최대 25KB의 입력 값을 처리할 수 있습니다.
{% endalert %}

#### 응답 필드 정의 {#define-response-fields}

에이전트가 [필드]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/?tab=fields#advanced-schemas)를 출력 형식으로 사용하는 경우, 카탈로그 필드에서 사용할 에이전트의 해당 필드를 **Response Field**로 선택할 수 있습니다.

다음 필드로 출력 형식을 구조화하여 카탈로그에 제품 설명을 추가하는 에이전트가 있다고 가정해 보겠습니다:

| 필드 이름 | 값 |
| --- | --- |
| **description** | 텍스트 |
| **confidence_score_out_of_ten** | 숫자 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="응답 필드 정의" }

카탈로그에 **product_description**이라는 필드를 추가하고 **description**을 **Response Field**로 선택하여 에이전트의 설명으로 열을 채울 수 있습니다.

!["Descriptor" 에이전트가 적용된 "product_description" 필드. "description" 출력이 응답 필드로 선택되어 있습니다.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

에이전트가 생성한 셀을 수동으로 재정의하려면 **Edit Item**을 선택하고 에이전트가 생성한 설명을 직접 수정합니다. 에이전트가 생성한 설명으로 되돌리려면 셀에서 새로고침 기호를 선택하세요.

### 카탈로그의 오류 처리 {#error-handling-in-catalogs}

- 실패한 카탈로그 호출은 LLM 제공자의 [사용량 제한 오류]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors)를 포함하여 재시도되지 않습니다.
- 기반 모델 제공자에 대한 API 호출이 잘못된 API 키 오류 등 다른 오류를 반환하면 필드 값이 업데이트되지 않습니다.
- 실패한 실행에 대한 세부 정보는 에이전트의 로그에서 확인할 수 있습니다.

## 에이전트 모니터링 {#monitor-your-agent}

에이전트의 **Usage** 섹션에서 카탈로그와 Canvases에서 에이전트가 활발히 사용되고 있는 위치를 참조하고 탐색할 수 있습니다.

![Canvases에 대해 두 개의 활성 에이전트와 하나의 비활성 에이전트를 보여주는 에이전트 사용량 섹션.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

에이전트의 **Logs** 섹션에서 Canvases와 카탈로그에서 발생하는 실제 에이전트 호출을 모니터링할 수 있습니다. 날짜 범위, 결과(성공 또는 실패), 호출 위치 등의 정보로 필터링할 수 있습니다. 현재 페이지에 표시된 로그만 내보내려면 **Export CSV**를 선택할 수도 있습니다.

{% alert tip %}
[메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/)에서 일일 호출 한도 오류를 모니터링할 수도 있습니다.
{% endalert %}

![에이전트 AI Sentiment Score에 대한 로그.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

특정 에이전트 호출에 대해 **View**를 선택하여 입력, 출력 및 사용자 ID를 확인합니다.

![입력 프롬프트, 출력 응답 및 관련 사용자 ID를 보여주는 에이전트 Random Sports Assignment의 세부 정보 패널.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Currents 사용 {#use-currents}

다음 Currents 이벤트를 사용하여 Kafka 레코드 스키마에 접근할 수도 있습니다:

- 에이전트 실행 이벤트
- 도구 호출 이벤트

자세한 내용은 [메시지 참여 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)을 참조하세요.

## 관련 문서 {#related-articles}

- [에이전트 참조]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
- [자주 묻는 질문]({{site.baseurl}}/user_guide/brazeai/agents/faq/)